// Original hardening helpers for the adapted Unslop story renderer.
import { openSync, closeSync, fstatSync, readFileSync, realpathSync, constants, existsSync, mkdirSync, mkdtempSync, rmSync, copyFileSync, lstatSync, renameSync } from 'node:fs';
import { dirname, resolve, relative, isAbsolute, sep, extname, join } from 'node:path';
import { tmpdir } from 'node:os';

export const MIME = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.avif':'image/avif','.svg':'image/svg+xml','.woff2':'font/woff2','.woff':'font/woff','.mp4':'video/mp4'};
export function within(root, target) {
  const part = relative(root, target);
  return part === '' || (!isAbsolute(part) && part !== '..' && !part.startsWith('..' + sep));
}
function decodeEntity(s) {
  return s.replace(/&(#x[\da-f]+|#\d+|amp|quot|apos|lt|gt);/gi, (_, e) => {
    const names={amp:'&',quot:'"',apos:"'",lt:'<',gt:'>'};
    if(e[0]!=='#')return names[e.toLowerCase()];
    const n=e[1].toLowerCase()==='x'?parseInt(e.slice(2),16):parseInt(e.slice(1),10);
    return n>0 && n<=0x10ffff && !(n>=0xd800&&n<=0xdfff)?String.fromCodePoint(n):'\uFFFD';
  });
}
export function readMeta(html, wanted) {
  // Metadata belongs in the head. Ignore comments and script/style content.
  const head = /<head\b[^>]*>([\s\S]*?)<\/head\s*>/i.exec(html)?.[1] ?? html;
  const clean=head.replace(/<!--[\s\S]*?-->/g,'').replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1\s*>/gi,'');
  for(const tag of clean.matchAll(/<meta\b(?:[^>"']|"[^"]*"|'[^']*')*>/gi)) {
    const attrs={};
    for(const m of tag[0].slice(5,-1).matchAll(/([^\s=/>]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?/g)) {
      const name=m[1].toLowerCase();if(!(name in attrs))attrs[name]=decodeEntity(m[2]??m[3]??m[4]??'');
    }
    if(attrs.name?.toLowerCase()===wanted.toLowerCase())return attrs.content;
  }
}
export function storyConfig(html, flags={}) {
  const steps=(readMeta(html,'unslop-steps')??'').split(',').map(s=>s.trim()).filter(Boolean);
  if(!steps.length || steps.length>12)throw Error('Provide 1–12 comma-separated unslop-steps in a meta element.');
  const frame=(readMeta(html,'unslop-frame')??'0 0 960').trim().split(/\s+/).map(Number);
  if(frame.length!==3 || frame.some(n=>!Number.isFinite(n)) || frame[0]<0 || frame[0]>10000 || frame[1]<0 || frame[1]>10000 || frame[2]<1 || frame[2]>10000)throw Error('unslop-frame requires x/y from 0 to 10000 and width from 1 to 10000.');
  const width=flags.width??(flags.wide?1920:1080),height=flags.height??1080,fps=flags.fps??30;
  if(!Number.isInteger(width)||!Number.isInteger(height)||width<64||height<64||width>3840||height>3840||width%2||height%2)throw Error('Output width/height must be even integers from 64 to 3840.');
  if(!Number.isInteger(fps)||fps<1||fps>60)throw Error('fps must be an integer from 1 to 60.');
  return {steps,frame,width,height,fps};
}
export function makeHandler(directory, stage) {
  const root=realpathSync(directory);
  return (request,response)=>{
    const end=(status,body='')=>{response.writeHead(status,{'content-type':'text/plain; charset=utf-8','cache-control':'no-store'});response.end(body);};
    if(!['GET','HEAD'].includes(request.method??'GET'))return end(405,'Method not allowed');
    if(request.headers?.host && !/^127\.0\.0\.1:\d+$/.test(request.headers.host))return end(403,'Invalid host');
    let pathname;
    try{pathname=decodeURIComponent(new URL(request.url,'http://127.0.0.1').pathname);if(pathname.includes('\0')||pathname.includes('\\'))return end(400,'Invalid path');}
    catch{return end(400,'Invalid URL');}
    const headers={'cache-control':'no-store','x-content-type-options':'nosniff','content-security-policy':"default-src 'self' data: blob:; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'self'"};
    if(pathname==='/__stage.html'){response.writeHead(200,{...headers,'content-type':MIME['.html']});return response.end(request.method==='HEAD'?'':stage);}
    if(!pathname.startsWith('/__story/'))return end(404,'Not found');
    let fd;
    try{
      const requested=resolve(root,pathname.slice('/__story/'.length));
      if(!within(root,requested))return end(404,'Not found');
      const target=realpathSync(requested);
      if(!within(root,target)||!MIME[extname(target).toLowerCase()])return end(404,'Not found');
      fd=openSync(target,constants.O_RDONLY|(constants.O_NOFOLLOW??0));
      const stat=fstatSync(fd);if(!stat.isFile())return end(404,'Not found');
      if(stat.size>30_000_000)return end(413,'Asset too large');
      const data=request.method==='HEAD'?'':readFileSync(fd);
      response.writeHead(200,{...headers,'content-type':MIME[extname(target).toLowerCase()]});response.end(data);
    }catch(error){if(!response.headersSent)return end(error.code==='EACCES'?403:404,'Not found');response.destroy?.();}
    finally{if(fd!==undefined)closeSync(fd);}
  };
}
export function makeWorkspace(){return mkdtempSync(join(tmpdir(),'ui-story-'));}
export function removeWorkspace(path){rmSync(path,{recursive:true,force:true});}
export function publishOutput(temp,target,overwrite=false){
  target=resolve(target);mkdirSync(dirname(target),{recursive:true});
  // COPYFILE_EXCL prevents a time-of-check-to-time-of-use overwrite race.
  if(overwrite){
    // Publish by rename from a private sibling, never follow a pre-existing symlink.
    const staging=mkdtempSync(join(dirname(target),'.ui-story-publish-'));
    try{const candidate=join(staging,'render.mp4');copyFileSync(temp,candidate,constants.COPYFILE_EXCL);renameSync(candidate,target);}
    finally{rmSync(staging,{recursive:true,force:true});}
  }else copyFileSync(temp,target,constants.COPYFILE_EXCL);
}
export function assertOutputAvailable(target, overwrite=false) {
  if(extname(target).toLowerCase()!=='.mp4')throw Error('Output must have an .mp4 extension.');
  if(existsSync(target)&&!lstatSync(target).isFile())throw Error('Output target must be a regular file, not a directory or symbolic link.');
  if(!overwrite&&existsSync(target))throw Error('Output already exists. Choose a fresh path or explicitly use --overwrite.');
}
