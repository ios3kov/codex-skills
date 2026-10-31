import assert from 'node:assert/strict';
import {captureDocument} from '../../../../interface-craft/scripts/unslop/capture-core.mjs';
class Node {
 constructor(tag,attrs={},text='',children=[]){this.tagName=tag.toUpperCase();this.a={...attrs};this.textContent=text;this.children=children;for(const c of children)c.parent=this;}
 get textContent(){return this._text||''} set textContent(v){this._text=v;this.children=[]}
 get attributes(){return Object.entries(this.a).map(([name,value])=>({name,value}))}
 getAttribute(k){return this.a[k]??null} setAttribute(k,v){this.a[k]=v}removeAttribute(k){delete this.a[k]}hasAttribute(k){return k in this.a}
 matches(sel){return sel.split(',').some(p=>{const m=p.trim().match(/^([\w*-]+)?(?:\[([^\]]+)\])?$/);return m&&(!m[1]||m[1]==='*'||m[1].toUpperCase()===this.tagName)&&(!m[2]||this.hasAttribute(m[2]))})}
 querySelectorAll(sel){let out=[];for(const c of this.children){if(c.matches(sel))out.push(c);out.push(...c.querySelectorAll(sel))}return out}querySelector(sel){return this.querySelectorAll(sel)[0]||null}
 replaceChildren(){this.children=[];this.textContent='';}
 cloneNode(){return new Node(this.tagName,this.a,this.textContent,this.children.map(c=>c.cloneNode()))}remove(){this.parent.children=this.parent.children.filter(n=>n!==this)}appendChild(c){c.parent=this;this.children.push(c)}prepend(c){c.parent=this;this.children.unshift(c)}
 set httpEquiv(v){this.a['http-equiv']=v}set content(v){this.a.content=v}
 get outerHTML(){return `<${this.tagName.toLowerCase()} ${Object.entries(this.a).map(([k,v])=>`${k}="${v}"`).join(' ')}>${this.textContent}${this.children.map(n=>n.outerHTML).join('')}</${this.tagName.toLowerCase()}>`}
}
const huge='data:image/png;base64,'+'A'.repeat(4000100);
const hugePlain='data:image/png,'+'A'.repeat(3500000);
const root=new Node('html',{onload:'window.rootHandlerRuns=true',style:'color:red'},'',[new Node('head'),new Node('body',{},'',[new Node('svg',{},'',[new Node('a',{},'',[new Node('animate',{attributeName:'href',values:'https://example.com',dur:'1s'})])]),new Node('select',{},'',[new Node('option',{selected:'',value:'secret-id'},'PRIVATE-SELECT-VALUE')]),new Node('img',{src:huge}),new Node('img',{src:hugePlain})])]);
globalThis.location={href:'https://example.com/'};globalThis.document={styleSheets:[{cssRules:[{cssText:'.probe { --x: "</style><meta http-equiv="refresh" content="0;url=https://example.com">"; }'}],ownerNode:{}}],documentElement:root,querySelector:s=>root.querySelector(s),querySelectorAll:s=>root.querySelectorAll(s),createElement:t=>new Node(t)};
const r=await captureDocument();
const result={svgAnimateSurvives:r.html.includes('<animate'),selectedSurvives:r.html.includes('selected='),selectTextSurvives:r.html.includes('PRIVATE-SELECT-VALUE'),oversizeDataUriSurvives:r.html.includes(huge),nonBase64Survives:r.html.includes(hugePlain),rootHandlerSurvives:r.html.includes('onload='),reportedAssetBytes:r.coverage.assetBytesRead,styleBreakoutText:r.html.includes('</style><meta http-equiv="refresh"')};
console.log(JSON.stringify(result,null,2));
assert.equal(result.svgAnimateSurvives,false);assert.equal(result.selectedSurvives,false);assert.equal(result.selectTextSurvives,false);assert.equal(result.oversizeDataUriSurvives,false);assert.equal(result.styleBreakoutText,false);assert.equal(result.reportedAssetBytes,0);assert.equal(result.nonBase64Survives,false);assert.equal(result.rootHandlerSurvives,false);console.log('PASS regression cases');
root.setAttribute('contenteditable','true');try {await captureDocument();console.log('Root editable result completed');}catch(e){console.log('ROOT_EDITABLE_ERROR: '+e.message)}
