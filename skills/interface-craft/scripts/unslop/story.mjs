// Adapted from Unslop by Damir Sokolovsky (@heydamir), CC BY 4.0.
// https://github.com/heydamir/unslop commit 4652254daff586ff4739849395a127b56f7f8cc7
// Modified 2026-10-31: isolated I/O, path containment, strict options, exact dimensions,
// explicit overwrite, bounded readiness, preview mode and honest errors.
import {createRequire} from 'node:module';
import {createServer} from 'node:http';
import {existsSync,readFileSync,mkdirSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {dirname,resolve,join} from 'node:path';
import {pathToFileURL} from 'node:url';
import {storyConfig,makeHandler,makeWorkspace,removeWorkspace,publishOutput,assertOutputAvailable} from './story-support.mjs';
import {runtimeTemplate} from './story-runtime.mjs';
import {makeStage} from './story-stage.mjs';

const usage=`Usage: node story.mjs story.html output.mp4 [--wide] [--width=N --height=N] [--fps=N] [--overwrite]
       node story.mjs story.html --serve
       node story.mjs story.html --play
Use only reviewed, trusted local HTML. Network requests are blocked except local assets.
Default output: 1080x1080 at 30fps. --wide: 1920x1080. No automatic dependency installation.
--serve starts a localhost preview for the host browser; --play opens a separate browser.
Requires Node, an available Playwright module/browser for render/play, and ffmpeg for export.`;
function options(args){
 const flags={},pos=[];
 for(const arg of args){
  if(['--wide','--play','--serve','--overwrite'].includes(arg))flags[arg.slice(2)]=true;
  else if(/^--(width|height|fps)=\d+$/.test(arg)){const[k,v]=arg.slice(2).split('=');flags[k]=Number(v);}
  else if(arg.startsWith('--'))throw Error(`Unknown option ${arg}`);else pos.push(arg);
 }
 if(pos.length<1||pos.length>2||(!flags.play&&!flags.serve&&!pos[1]))throw Error(usage);
 if(flags.play&&flags.serve)throw Error('Choose --play or --serve, not both.');
 if((flags.play||flags.serve)&&pos[1])throw Error('Preview modes do not accept an output path.');
 return {...flags,input:pos[0],output:pos[1]};
}
async function browserKit(){
 for(const name of ['playwright','playwright-core']){
  try{return await import(name);}catch{}
  try{return createRequire(join(process.cwd(),'package.json'))(name);}catch{}
 }
 throw Error('Playwright is unavailable. Use the project’s approved environment, or --serve with the host browser. Nothing was installed.');
}
export function timeline(steps,slop){
 const kind=name=>/spac/i.test(name)?'spacing':/detail|radius|corner/i.test(name)?'details':null;
 const plan=[];let cursor=.5;
 const at=(time,name,value)=>plan.push({time,name,value});
 if(slop){at(cursor,'show','audit');at(cursor+.9,'clear');cursor+=1.1;}
 const blocks=steps.map(n=>kind(n)?1.75:1.25),fit=Math.min(1,(10-cursor-1.6)/blocks.reduce((a,b)=>a+b,0));
 steps.forEach((name,i)=>{const k=kind(name);if(k){at(cursor,'show',k);at(cursor+.35*fit,'step',i+1);at(cursor+1.35*fit,'settle');at(cursor+1.7*fit,'clear');}else at(cursor,'step',i+1);cursor+=blocks[i]*fit;});
 return {events:plan.sort((a,b)=>a.time-b.time),total:cursor+1.6};
}
export function previewBootstrap(runtime,steps,paddingCss){
 const safeScript=JSON.stringify(runtime).replace(/</g,'\\u003c');
 return `<script>window.addEventListener('load',()=>{const f=document.getElementById('page');const d=f.contentDocument;
 const padding=d.createElement('style');padding.textContent=${JSON.stringify(paddingCss).replace(/</g,'\\u003c')};d.head.appendChild(padding);
 const script=d.createElement('script');script.textContent=${safeScript};d.head.appendChild(script);const api=f.contentWindow.__story;api.install();
 const steps=${JSON.stringify(steps).replace(/</g,'\\u003c')};let timers=[];
 const clear=()=>{timers.forEach(clearTimeout);timers=[];};
 const button=(label,action)=>{const b=document.createElement('button');b.textContent=label;b.onclick=action;document.getElementById('preview-controls').appendChild(b);};
 button('Initial state',()=>{clear();api.reset();});button('Final state',()=>{clear();api.reset();steps.forEach((_,i)=>api.step(i+1));});
 steps.forEach((name,i)=>button(name,()=>{clear();api.reset();for(let k=1;k<=i+1;k++)api.step(k);}));
 document.getElementById('preview-status').textContent='Ready — '+steps.length+' steps';
});</script><div id="preview-controls" style="position:fixed;bottom:0;left:0;z-index:100;background:white;color:black;padding:8px"><span id="preview-status">Loading</span></div>`;
}
export async function main(args=process.argv.slice(2)){
 if(args.includes('--help')||args.includes('-h')){console.log(usage);return;}
 const opt=options(args),file=resolve(opt.input),root=dirname(file),html=readFileSync(file,'utf8'),conf=storyConfig(html,opt);
 if(opt.output)assertOutputAvailable(opt.output,opt.overwrite);
 let browser,server,temp;
 const errors=[],remote=[];
 try{
  if(opt.output){execFileSync('ffmpeg',['-version'],{stdio:'ignore'});}
  const FRAME={width:conf.width,height:conf.height},play=Boolean(opt.play),VIEW=.75;
  const[frameX,frameY,frameWidth]=conf.frame,scale=(FRAME.width-72)/frameWidth;
  const offsetX=72/scale-frameX,offsetY=72/scale-frameY,padLeft=Math.max(0,offsetX),padTop=Math.max(0,offsetY),left=Math.min(0,offsetX)*scale,top=Math.min(0,offsetY)*scale;
  const pageWidth=Math.max(1440+padLeft,Math.ceil((FRAME.width-left)/scale)+2),padRight=pageWidth-1440-padLeft,pageHeight=Math.max(900+padTop,Math.ceil((FRAME.height-top)/scale)+2);
  const runtime=runtimeTemplate.replace('__UNSLOP_STEPS__',JSON.stringify(conf.steps).replace(/</g,'\\u003c'));
  let stage=makeStage({FRAME,play,VIEW,left,top,pageWidth,pageHeight,scale,file,root});
  const paddingCss=`html {padding:${padTop}px ${padRight}px 0 ${padLeft}px !important;}`;
  if(opt.serve)stage=stage.replace('</body>',previewBootstrap(runtime,conf.steps,paddingCss)+'</body>');
  server=createServer(makeHandler(root,stage));
  await new Promise((done,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',done);});
  const base=`http://127.0.0.1:${server.address().port}`;
  if(opt.serve){
   console.log(JSON.stringify({url:base+'/__stage.html',width:conf.width,height:conf.height,steps:conf.steps,status:'preview_server_ready'}));
   await new Promise(done=>{process.once('SIGINT',done);process.once('SIGTERM',done);});return;
  }
  const {chromium}=await browserKit();
  const chrome=[process.env.CHROME_PATH,'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].find(p=>p&&existsSync(p));
  browser=await chromium.launch({...chrome?{executablePath:chrome}:{},headless:!play});
  const context=await browser.newContext({viewport:play?{width:Math.round(FRAME.width*VIEW),height:Math.round(FRAME.height*VIEW)}:FRAME,deviceScaleFactor:1,serviceWorkers:'block'});
  await context.route('**/*',async route=>{const u=route.request().url();if(u.startsWith(base+'/')||/^(data:|blob:)/.test(u))return route.continue();remote.push(u);return route.abort();});
  const page=await context.newPage();page.setDefaultTimeout(15000);page.setDefaultNavigationTimeout(15000);
  page.on('pageerror',e=>errors.push(e.message));
  page.on('response',r=>{if(r.status()>=400&&!r.url().endsWith('/favicon.ico'))errors.push('HTTP '+r.status()+' '+r.url());});
  await page.goto(base+'/__stage.html',{waitUntil:'domcontentloaded'});
  const frame=page.frames().find(f=>f!==page.mainFrame());if(!frame)throw Error('Story iframe did not load.');
  await frame.waitForLoadState('domcontentloaded');
  await frame.evaluate(async()=>{await Promise.race([document.fonts.ready,new Promise((_,reject)=>setTimeout(()=>reject(Error('Font readiness timed out')),10000))]);});
  await frame.waitForFunction(()=>[...document.images].every(img=>img.complete),undefined,{timeout:15000});
  const broken=await frame.evaluate(()=>[...document.images].filter(img=>!img.naturalWidth).map(img=>img.getAttribute('src')));
  if(broken.length)throw Error('Broken story images: '+broken.join(', '));
  if(remote.length)throw Error('External resources were blocked: '+[...new Set(remote)].join(', '));
  await frame.addStyleTag({content:paddingCss});
  await frame.addScriptTag({content:runtime});await frame.evaluate(()=>window.__story.install());
  const slop=await frame.evaluate(()=>document.querySelectorAll('[data-slop]').length),plan=timeline(conf.steps,slop);
  if(play){
   console.log('Preview running; close its browser window to stop.');
   while(browser.isConnected()){
    try{await frame.evaluate(()=>window.__story.reset());const start=Date.now();for(const e of plan.events){await new Promise(r=>setTimeout(r,Math.max(0,start+e.time*1000-Date.now())));await frame.evaluate(e=>window.__story[e.name](e.value),e);if(errors.length)throw Error('Story script errors: '+errors.join('; '));}await new Promise(r=>setTimeout(r,Math.max(0,start+plan.total*1000-Date.now())));}
    catch(e){if(!browser.isConnected())break;throw e;}
   }
  }else{
   temp=makeWorkspace();const frames=join(temp,'frames');mkdirSync(frames);let next=0;
   const count=Math.ceil(plan.total*conf.fps);
   for(let i=0;i<count;i++){const now=i/conf.fps;while(next<plan.events.length&&plan.events[next].time<=now+1e-6){await frame.evaluate(e=>window.__story[e.name](e.value),plan.events[next++]);}await frame.evaluate(ms=>window.__story.tick(ms),now*1000);await page.screenshot({path:join(frames,`f-${String(i).padStart(5,'0')}.jpg`),type:'jpeg',quality:92});}
   if(errors.length)throw Error('Story script errors: '+errors.join('; '));
   if(remote.length)throw Error('External resources were blocked: '+[...new Set(remote)].join(', '));
   const staged=join(temp,'render.mp4');execFileSync('ffmpeg',['-n','-loglevel','error','-framerate',String(conf.fps),'-i',join(frames,'f-%05d.jpg'),'-vf',`scale=${FRAME.width}:${FRAME.height}:flags=lanczos`,'-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-movflags','+faststart',staged],{timeout:180000});
   publishOutput(staged,opt.output,opt.overwrite);
   console.log(JSON.stringify({output:resolve(opt.output),width:FRAME.width,height:FRAME.height,fps:conf.fps,frames:count,duration:count/conf.fps,status:'render_complete',verification:'Inspect delivered frames and metadata separately.'}));
  }
  if(errors.length)throw Error('Story script errors: '+errors.join('; '));
 }finally{
  if(browser)await browser.close().catch(()=>{});
  if(server)await new Promise(done=>server.close(done));
  if(temp)removeWorkspace(temp);
 }
}
if(process.argv[1] && import.meta.url===pathToFileURL(resolve(process.argv[1])).href){main().catch(e=>{console.error('Story failed: '+e.message);process.exitCode=1;});}
