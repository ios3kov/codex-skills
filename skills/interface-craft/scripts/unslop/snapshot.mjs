// Adapted from heydamir/unslop (4652254), Damir Sokolovsky, CC BY 4.0.
// Changed: inert bounded export, coverage report, readiness and no overwrite.
import {createRequire} from 'node:module';
import {existsSync,mkdirSync,openSync,closeSync,writeFileSync,rmSync} from 'node:fs';
import {resolve,dirname,join} from 'node:path';
import {safeHttp,boundedInt,captureDocument} from './capture-core.mjs';
const usage='node snapshot.mjs <http(s)-url> <fresh-output-directory> [--dark|--light] [--width=1440] [--height=900]\nRequires an already installed playwright or playwright-core and Chromium. No installs. Produces inert original.html, original.live.png and coverage.json. Never exports a functional app.';
const args=process.argv.slice(2);
if(args.includes('--help')){console.log(usage);process.exit(0)}
const flag=(n,d)=>args.find(a=>a.startsWith('--'+n+'='))?.slice(n.length+3)??d;
let browser;let reserved=false;let output;
try{
  const options=args.filter(a=>a.startsWith('--'));if(options.some(a=>!/^--(dark|light|width=\d+|height=\d+)$/.test(a))||args.includes('--dark')&&args.includes('--light'))throw Error('Invalid options');
  const pos=args.filter(a=>!a.startsWith('--'));if(pos.length!==2)throw Error(usage);
  const url=safeHttp(pos[0]);output=resolve(pos[1]);if(existsSync(output))throw Error('Output directory already exists; choose a fresh path');
  const width=boundedInt(flag('width','1440'),240,7680,'width'),height=boundedInt(flag('height','900'),240,7680,'height');
  let kit;for(const name of ['playwright','playwright-core']){try{kit=await import(name);break}catch{}try{kit=createRequire(join(process.cwd(),'package.json'))(name);break}catch{}}
  if(!kit)throw Error('Missing Playwright. Use an existing authorized project runtime; nothing was installed.');
  const chrome=[process.env.CHROME_PATH,'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].find(p=>p&&existsSync(p));
  browser=await kit.chromium.launch(chrome?{executablePath:chrome}:{});
  const context=await browser.newContext({viewport:{width,height},colorScheme:args.includes('--dark')?'dark':args.includes('--light')?'light':'no-preference',serviceWorkers:'block',acceptDownloads:false});
  const page=await context.newPage();await page.goto(url,{waitUntil:'domcontentloaded',timeout:20000});await page.locator('body').waitFor({state:'visible',timeout:10000});
  const readiness=await page.evaluate(async()=>{const result=await Promise.race([document.fonts.ready.then(()=>true),new Promise(r=>setTimeout(()=>r(false),5000))]);return{fontsReady:result,pendingImages:[...document.images].filter(i=>!i.complete).length}});
  mkdirSync(output,{recursive:false});reserved=true;
  await page.screenshot({path:join(output,'original.live.png')});
  const result=await page.evaluate(captureDocument);result.coverage.readiness=readiness;result.coverage.url=url;result.coverage.viewport={width,height};
  writeFileSync(join(output,'original.html'),result.html,{flag:'wx'});writeFileSync(join(output,'coverage.json'),JSON.stringify(result.coverage,null,2),{flag:'wx'});
  console.log(JSON.stringify({status:'PARTIAL',output,coverage:result.coverage}));
}catch(e){if(reserved)writeFileSync(join(output,'failure.json'),JSON.stringify({status:'FAIL',error:e.message}));console.error(e.message);process.exitCode=1}finally{await browser?.close().catch(()=>{})}
