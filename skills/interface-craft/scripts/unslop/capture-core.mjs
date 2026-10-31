// Adapted from heydamir/unslop, Damir Sokolovsky, CC BY 4.0.
// Local adaptation: inert export, explicit coverage and bounded resource capture.
export function safeHttp(value) {
  const u = new URL(value);
  if (!['http:', 'https:'].includes(u.protocol) || u.username || u.password) throw new Error('Expected HTTP(S) URL without embedded credentials');
  return u.href;
}
export function boundedInt(value, low, high, name) {
  if (!/^\d+$/.test(String(value))) throw new Error(`Invalid ${name}`);
  const n=Number(value); if(n<low||n>high)throw new Error(`${name} outside ${low}..${high}`);return n;
}
export async function captureDocument() {
  const gaps=[]; const unresolved=new Set(); const cache=new Map();let total=0;let resources=0;const began=Date.now();
  const abs=(x,base=location.href)=>{try{return new URL(x,base).href}catch{return x}};
  const resource=async(url)=>{
    if(!url||url.startsWith('#'))return url;
    if(++resources>64||Date.now()-began>20000||total>=20000000){gaps.push({kind:'resource-budget',reason:'capture limit reached'});return ''}
    if(url.startsWith('data:')){const bytes=url.length;if(bytes>3000000||total+bytes>20000000){gaps.push({kind:'data-budget',reason:'inline asset omitted'});return ''}total+=bytes;if(/^data:(image\/(?!svg)|font\/|application\/(font|x-font|octet-stream))/i.test(url))return url;unresolved.add(url.slice(0,80));return '';}
    url=abs(url);if(cache.has(url))return cache.get(url);
    const task=(async()=>{try{
      if(!/^https?:/.test(url))throw Error('unsupported scheme');
      const r=await fetch(url,{credentials:'omit',signal:AbortSignal.timeout(6000)});
      if(!r.ok)throw Error('HTTP '+r.status);
      const type=(r.headers.get('content-type')||'').split(';')[0];
      if(!/^(image\/(?!svg)|font\/|application\/(font|x-font|octet-stream))/i.test(type))throw Error('unsupported MIME '+type);
      const reader=r.body.getReader();let size=0;const chunks=[];
      try{while(true){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;total+=value.byteLength;if(size>3000000||total>20000000)throw Error('asset budget exceeded');chunks.push(value)}}finally{await reader.cancel().catch(()=>{})}
      return await new Promise((resolve,reject)=>{const f=new FileReader();f.onload=()=>resolve(f.result);f.onerror=reject;f.readAsDataURL(new Blob(chunks,{type}))});
    }catch(e){unresolved.add(url);gaps.push({resource:url,reason:String(e.message)});return ''}})();cache.set(url,task);return task;
  };
  const cssUrls=async(text,base)=>{
    if(/@import\b/i.test(text)){gaps.push({kind:'css-import',source:base});text=text.replace(/@import\s+(?:url\([^)]*\)|["'][^"']*["'])[^;]*;/gi,'');}
    const matches=[...text.matchAll(/url\(\s*(["']?)(.*?)\1\s*\)/g)];
    for(const [whole,,url] of matches){const val=url.startsWith('#')?url:await resource(abs(url,base));text=text.split(whole).join(`url("${val.replaceAll('"','%22')}")`)}return text;
  };
  const styles=[];
  for(const sheet of document.styleSheets){try{let text=[...sheet.cssRules].map(r=>r.cssText).join('\n');text=await cssUrls(text,sheet.href||location.href);const media=sheet.media?.mediaText;styles.push(media&&media!=='all'?`@media ${media}{${text}}`:text)}catch{gaps.push({kind:'stylesheet',source:sheet.href||'inline',reason:'CSS rules inaccessible'})}}
  const copy=document.documentElement.cloneNode(true);
  if(copy.hasAttribute('contenteditable')&&copy.getAttribute('contenteditable')!=='false')throw Error('Root contenteditable document cannot be safely redacted; export unsupported');
  for(const [tag,label] of [['canvas','canvas pixels'],['iframe','embedded frame'],['video','video playback'],['audio','audio playback']]){
    if(copy.querySelector(tag))gaps.push({kind:label,reason:'not retained as active content'});
  }
  if([...document.querySelectorAll('*')].some(n=>n.shadowRoot))gaps.push({kind:'shadow-dom',reason:'not serialized'});
  if(document.querySelector('input,textarea,select'))gaps.push({kind:'forms',reason:'disabled and values redacted'});
  copy.querySelectorAll('script,noscript,iframe,object,embed,base,link,style,meta[http-equiv],source,video,audio,canvas,animate,animateTransform,animateMotion,set,discard,mpath').forEach(n=>n.remove());
  copy.querySelectorAll('select').forEach(n=>n.replaceChildren());
  copy.querySelectorAll('[contenteditable]').forEach(n=>{if(n.getAttribute('contenteditable')!=='false'){n.textContent='';gaps.push({kind:'editable-content',reason:'redacted'})}n.removeAttribute('contenteditable')});
  const originals=[...document.querySelectorAll('img')];let i=0;
  for(const img of copy.querySelectorAll('img')){const src=originals[i++]?.currentSrc||img.getAttribute('src');img.setAttribute('src',await resource(abs(src||'')));img.removeAttribute('srcset');img.removeAttribute('loading');}
  for(const n of [copy,...copy.querySelectorAll('*')]){
    for(const a of [...n.attributes]){
      if(/^on/i.test(a.name)||/^(href|xlink:href|action|formaction|srcdoc|srcset|integrity|nonce|ping|autofocus|value)$/i.test(a.name))n.removeAttribute(a.name);
      if(a.name==='src'&&n.tagName!=='IMG')n.removeAttribute(a.name);
    }
    if(n.hasAttribute('contenteditable'))n.removeAttribute('contenteditable');
    if(n.hasAttribute('style'))n.setAttribute('style',await cssUrls(n.getAttribute('style'),location.href));
    if(n.matches('input,textarea,select,button')){n.setAttribute('disabled','');n.removeAttribute('checked');n.removeAttribute('selected');if(n.tagName==='TEXTAREA')n.textContent='';}
  }
  const style=document.createElement('style');style.textContent=(styles.join('\n')+'\n*,*::before,*::after{animation:none!important;transition:none!important}').replaceAll('<','\\3c ');copy.querySelector('head').appendChild(style);
  const csp=document.createElement('meta');csp.httpEquiv='Content-Security-Policy';csp.content="default-src 'none'; img-src data:; font-src data:; style-src 'unsafe-inline'; script-src 'none'; connect-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'";copy.querySelector('head').prepend(csp);
  gaps.push({kind:'interaction',reason:'inert visual export; not functional site backup'},{kind:'animations',reason:'paused at export; compare original screenshot'});
  return {html:'<!doctype html>\n'+copy.outerHTML,coverage:{complete:false,gaps,unresolved:[...unresolved],assetBytesRead:total}};
}
