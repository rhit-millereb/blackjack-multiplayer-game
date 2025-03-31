/*!--------------------------------------------------------
 * Copyright (C) Microsoft Corporation. All rights reserved.
 *--------------------------------------------------------*/var T=function(e,r){return T=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,n){t.__proto__=n}||function(t,n){for(var s in n)Object.prototype.hasOwnProperty.call(n,s)&&(t[s]=n[s])},T(e,r)};export function __extends(e,r){if(typeof r!="function"&&r!==null)throw new TypeError("Class extends value "+String(r)+" is not a constructor or null");T(e,r);function t(){this.constructor=e}e.prototype=r===null?Object.create(r):(t.prototype=r.prototype,new t)}export var __assign=function(){return __assign=Object.assign||function(r){for(var t,n=1,s=arguments.length;n<s;n++){t=arguments[n];for(var o in t)Object.prototype.hasOwnProperty.call(t,o)&&(r[o]=t[o])}return r},__assign.apply(this,arguments)};export function __rest(e,r){var t={};for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&r.indexOf(n)<0&&(t[n]=e[n]);if(e!=null&&typeof Object.getOwnPropertySymbols=="function")for(var s=0,n=Object.getOwnPropertySymbols(e);s<n.length;s++)r.indexOf(n[s])<0&&Object.prototype.propertyIsEnumerable.call(e,n[s])&&(t[n[s]]=e[n[s]]);return t}export function __decorate(e,r,t,n){var s=arguments.length,o=s<3?r:n===null?n=Object.getOwnPropertyDescriptor(r,t):n,i;if(typeof Reflect=="object"&&typeof Reflect.decorate=="function")o=Reflect.decorate(e,r,t,n);else for(var f=e.length-1;f>=0;f--)(i=e[f])&&(o=(s<3?i(o):s>3?i(r,t,o):i(r,t))||o);return s>3&&o&&Object.defineProperty(r,t,o),o}export function __param(e,r){return function(t,n){r(t,n,e)}}export function __esDecorate(e,r,t,n,s,o){function i(y){if(y!==void 0&&typeof y!="function")throw new TypeError("Function expected");return y}for(var f=n.kind,d=f==="getter"?"get":f==="setter"?"set":"value",a=!r&&e?n.static?e:e.prototype:null,u=r||(a?Object.getOwnPropertyDescriptor(a,n.name):{}),c,_=!1,p=t.length-1;p>=0;p--){var l={};for(var m in n)l[m]=m==="access"?{}:n[m];for(var m in n.access)l.access[m]=n.access[m];l.addInitializer=function(y){if(_)throw new TypeError("Cannot add initializers after decoration has completed");o.push(i(y||null))};var g=(0,t[p])(f==="accessor"?{get:u.get,set:u.set}:u[d],l);if(f==="accessor"){if(g===void 0)continue;if(g===null||typeof g!="object")throw new TypeError("Object expected");(c=i(g.get))&&(u.get=c),(c=i(g.set))&&(u.set=c),(c=i(g.init))&&s.unshift(c)}else(c=i(g))&&(f==="field"?s.unshift(c):u[d]=c)}a&&Object.defineProperty(a,n.name,u),_=!0}export function __runInitializers(e,r,t){for(var n=arguments.length>2,s=0;s<r.length;s++)t=n?r[s].call(e,t):r[s].call(e);return n?t:void 0}export function __propKey(e){return typeof e=="symbol"?e:"".concat(e)}export function __setFunctionName(e,r,t){return typeof r=="symbol"&&(r=r.description?"[".concat(r.description,"]"):""),Object.defineProperty(e,"name",{configurable:!0,value:t?"".concat(t," ",r):r})}export function __metadata(e,r){if(typeof Reflect=="object"&&typeof Reflect.metadata=="function")return Reflect.metadata(e,r)}export function __awaiter(e,r,t,n){function s(o){return o instanceof t?o:new t(function(i){i(o)})}return new(t||(t=Promise))(function(o,i){function f(u){try{a(n.next(u))}catch(c){i(c)}}function d(u){try{a(n.throw(u))}catch(c){i(c)}}function a(u){u.done?o(u.value):s(u.value).then(f,d)}a((n=n.apply(e,r||[])).next())})}export function __generator(e,r){var t={label:0,sent:function(){if(o[0]&1)throw o[1];return o[1]},trys:[],ops:[]},n,s,o,i;return i={next:f(0),throw:f(1),return:f(2)},typeof Symbol=="function"&&(i[Symbol.iterator]=function(){return this}),i;function f(a){return function(u){return d([a,u])}}function d(a){if(n)throw new TypeError("Generator is already executing.");for(;i&&(i=0,a[0]&&(t=0)),t;)try{if(n=1,s&&(o=a[0]&2?s.return:a[0]?s.throw||((o=s.return)&&o.call(s),0):s.next)&&!(o=o.call(s,a[1])).done)return o;switch(s=0,o&&(a=[a[0]&2,o.value]),a[0]){case 0:case 1:o=a;break;case 4:return t.label++,{value:a[1],done:!1};case 5:t.label++,s=a[1],a=[0];continue;case 7:a=t.ops.pop(),t.trys.pop();continue;default:if(o=t.trys,!(o=o.length>0&&o[o.length-1])&&(a[0]===6||a[0]===2)){t=0;continue}if(a[0]===3&&(!o||a[1]>o[0]&&a[1]<o[3])){t.label=a[1];break}if(a[0]===6&&t.label<o[1]){t.label=o[1],o=a;break}if(o&&t.label<o[2]){t.label=o[2],t.ops.push(a);break}o[2]&&t.ops.pop(),t.trys.pop();continue}a=r.call(e,t)}catch(u){a=[6,u],s=0}finally{n=o=0}if(a[0]&5)throw a[1];return{value:a[0]?a[1]:void 0,done:!0}}}export var __createBinding=Object.create?function(e,r,t,n){n===void 0&&(n=t);var s=Object.getOwnPropertyDescriptor(r,t);(!s||("get"in s?!r.__esModule:s.writable||s.configurable))&&(s={enumerable:!0,get:function(){return r[t]}}),Object.defineProperty(e,n,s)}:function(e,r,t,n){n===void 0&&(n=t),e[n]=r[t]};export function __exportStar(e,r){for(var t in e)t!=="default"&&!Object.prototype.hasOwnProperty.call(r,t)&&__createBinding(r,e,t)}export function __values(e){var r=typeof Symbol=="function"&&Symbol.iterator,t=r&&e[r],n=0;if(t)return t.call(e);if(e&&typeof e.length=="number")return{next:function(){return e&&n>=e.length&&(e=void 0),{value:e&&e[n++],done:!e}}};throw new TypeError(r?"Object is not iterable.":"Symbol.iterator is not defined.")}export function __read(e,r){var t=typeof Symbol=="function"&&e[Symbol.iterator];if(!t)return e;var n=t.call(e),s,o=[],i;try{for(;(r===void 0||r-- >0)&&!(s=n.next()).done;)o.push(s.value)}catch(f){i={error:f}}finally{try{s&&!s.done&&(t=n.return)&&t.call(n)}finally{if(i)throw i.error}}return o}export function __spread(){for(var e=[],r=0;r<arguments.length;r++)e=e.concat(__read(arguments[r]));return e}export function __spreadArrays(){for(var e=0,r=0,t=arguments.length;r<t;r++)e+=arguments[r].length;for(var n=Array(e),s=0,r=0;r<t;r++)for(var o=arguments[r],i=0,f=o.length;i<f;i++,s++)n[s]=o[i];return n}export function __spreadArray(e,r,t){if(t||arguments.length===2)for(var n=0,s=r.length,o;n<s;n++)(o||!(n in r))&&(o||(o=Array.prototype.slice.call(r,0,n)),o[n]=r[n]);return e.concat(o||Array.prototype.slice.call(r))}export function __await(e){return this instanceof __await?(this.v=e,this):new __await(e)}export function __asyncGenerator(e,r,t){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var n=t.apply(e,r||[]),s,o=[];return s={},f("next"),f("throw"),f("return",i),s[Symbol.asyncIterator]=function(){return this},s;function i(p){return function(l){return Promise.resolve(l).then(p,c)}}function f(p,l){n[p]&&(s[p]=function(m){return new Promise(function(g,y){o.push([p,m,g,y])>1||d(p,m)})},l&&(s[p]=l(s[p])))}function d(p,l){try{a(n[p](l))}catch(m){_(o[0][3],m)}}function a(p){p.value instanceof __await?Promise.resolve(p.value.v).then(u,c):_(o[0][2],p)}function u(p){d("next",p)}function c(p){d("throw",p)}function _(p,l){p(l),o.shift(),o.length&&d(o[0][0],o[0][1])}}export function __asyncDelegator(e){var r,t;return r={},n("next"),n("throw",function(s){throw s}),n("return"),r[Symbol.iterator]=function(){return this},r;function n(s,o){r[s]=e[s]?function(i){return(t=!t)?{value:__await(e[s](i)),done:!1}:o?o(i):i}:o}}export function __asyncValues(e){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var r=e[Symbol.asyncIterator],t;return r?r.call(e):(e=typeof __values=="function"?__values(e):e[Symbol.iterator](),t={},n("next"),n("throw"),n("return"),t[Symbol.asyncIterator]=function(){return this},t);function n(o){t[o]=e[o]&&function(i){return new Promise(function(f,d){i=e[o](i),s(f,d,i.done,i.value)})}}function s(o,i,f,d){Promise.resolve(d).then(function(a){o({value:a,done:f})},i)}}export function __makeTemplateObject(e,r){return Object.defineProperty?Object.defineProperty(e,"raw",{value:r}):e.raw=r,e}var ie=Object.create?function(e,r){Object.defineProperty(e,"default",{enumerable:!0,value:r})}:function(e,r){e.default=r};export function __importStar(e){if(e&&e.__esModule)return e;var r={};if(e!=null)for(var t in e)t!=="default"&&Object.prototype.hasOwnProperty.call(e,t)&&__createBinding(r,e,t);return ie(r,e),r}export function __importDefault(e){return e&&e.__esModule?e:{default:e}}export function __classPrivateFieldGet(e,r,t,n){if(t==="a"&&!n)throw new TypeError("Private accessor was defined without a getter");if(typeof r=="function"?e!==r||!n:!r.has(e))throw new TypeError("Cannot read private member from an object whose class did not declare it");return t==="m"?n:t==="a"?n.call(e):n?n.value:r.get(e)}export function __classPrivateFieldSet(e,r,t,n,s){if(n==="m")throw new TypeError("Private method is not writable");if(n==="a"&&!s)throw new TypeError("Private accessor was defined without a setter");if(typeof r=="function"?e!==r||!s:!r.has(e))throw new TypeError("Cannot write private member to an object whose class did not declare it");return n==="a"?s.call(e,t):s?s.value=t:r.set(e,t),t}export function __classPrivateFieldIn(e,r){if(r===null||typeof r!="object"&&typeof r!="function")throw new TypeError("Cannot use 'in' operator on non-object");return typeof e=="function"?r===e:e.has(r)}export function __addDisposableResource(e,r,t){if(r!=null){if(typeof r!="object"&&typeof r!="function")throw new TypeError("Object expected.");var n,s;if(t){if(!Symbol.asyncDispose)throw new TypeError("Symbol.asyncDispose is not defined.");n=r[Symbol.asyncDispose]}if(n===void 0){if(!Symbol.dispose)throw new TypeError("Symbol.dispose is not defined.");n=r[Symbol.dispose],t&&(s=n)}if(typeof n!="function")throw new TypeError("Object not disposable.");s&&(n=function(){try{s.call(this)}catch(o){return Promise.reject(o)}}),e.stack.push({value:r,dispose:n,async:t})}else t&&e.stack.push({async:!0});return r}var ae=typeof SuppressedError=="function"?SuppressedError:function(e,r,t){var n=new Error(t);return n.name="SuppressedError",n.error=e,n.suppressed=r,n};export function __disposeResources(e){function r(n){e.error=e.hasError?new ae(n,e.error,"An error was suppressed during disposal."):n,e.hasError=!0}function t(){for(;e.stack.length;){var n=e.stack.pop();try{var s=n.dispose&&n.dispose.call(n.value);if(n.async)return Promise.resolve(s).then(t,function(o){return r(o),t()})}catch(o){r(o)}}if(e.hasError)throw e.error}return t()}export default{__extends,__assign,__rest,__decorate,__param,__metadata,__awaiter,__generator,__createBinding,__exportStar,__values,__read,__spread,__spreadArrays,__spreadArray,__await,__asyncGenerator,__asyncDelegator,__asyncValues,__makeTemplateObject,__importStar,__importDefault,__classPrivateFieldGet,__classPrivateFieldSet,__classPrivateFieldIn,__addDisposableResource,__disposeResources};var ce=Object.defineProperty,le=(e,r)=>{for(var t in r)ce(e,t,{get:r[t],enumerable:!0})};delete process.env.ELECTRON_RUN_AS_NODE;import*as $ from"path";import*as J from"http";import*as fe from"os";import*as ue from"readline";import{performance as H}from"perf_hooks";import{fileURLToPath as pe}from"url";import de from"minimist";import*as E from"path";import*as K from"fs";import{fileURLToPath as me}from"url";import{createRequire as _e}from"node:module";var q=_e(import.meta.url),h={exports:{}},ge=E.dirname(me(import.meta.url));if(Error.stackTraceLimit=100,!process.env.VSCODE_HANDLES_SIGPIPE){let e=!1;process.on("SIGPIPE",()=>{e||(e=!0,console.error(new Error("Unexpected SIGPIPE")))})}function ye(){try{typeof process.env.VSCODE_CWD!="string"&&(process.env.VSCODE_CWD=process.cwd()),process.platform==="win32"&&process.chdir(E.dirname(process.execPath))}catch(e){console.error(e)}}ye(),h.exports.devInjectNodeModuleLookupPath=function(e){if(!process.env.VSCODE_DEV)return;if(!e)throw new Error("Missing injectPath");q("node:module").register("./bootstrap-import.js",{parentURL:import.meta.url,data:e})},h.exports.removeGlobalNodeJsModuleLookupPaths=function(){if(typeof process?.versions?.electron=="string")return;const e=q("module"),r=e.globalPaths,t=e._resolveLookupPaths;e._resolveLookupPaths=function(n,s){const o=t(n,s);if(Array.isArray(o)){let i=0;for(;i<o.length&&o[o.length-1-i]===r[r.length-1-i];)i++;return o.slice(0,o.length-i)}return o}},h.exports.configurePortable=function(e){const r=E.dirname(ge);function t(d){return process.env.VSCODE_DEV?r:process.platform==="darwin"?d.dirname(d.dirname(d.dirname(r))):d.dirname(d.dirname(r))}function n(d){if(process.env.VSCODE_PORTABLE)return process.env.VSCODE_PORTABLE;if(process.platform==="win32"||process.platform==="linux")return d.join(t(d),"data");const a=e.portable||`${e.applicationName}-portable-data`;return d.join(d.dirname(t(d)),a)}const s=n(E),o=!("target"in e)&&K.existsSync(s),i=E.join(s,"tmp"),f=o&&K.existsSync(i);return o?process.env.VSCODE_PORTABLE=s:delete process.env.VSCODE_PORTABLE,f&&(process.platform==="win32"?(process.env.TMP=i,process.env.TEMP=i):process.env.TMPDIR=i),{portableDataPath:s,isPortable:o}},h.exports.enableASARSupport=function(){},h.exports.fileUriFromPath=function(e,r){let t=e.replace(/\\/g,"/");t.length>0&&t.charAt(0)!=="/"&&(t=`/${t}`);let n;return r.isWindows&&t.startsWith("//")?n=encodeURI(`${r.scheme||"file"}:${t}`):n=encodeURI(`${r.scheme||"file"}://${r.fallbackAuthority||""}${t}`),n.replace(/#/g,"%23")};var he=h.exports.devInjectNodeModuleLookupPath,Ke=h.exports.removeGlobalNodeJsModuleLookupPaths,qe=h.exports.configurePortable,Be=h.exports.enableASARSupport,We=h.exports.fileUriFromPath;import*as ve from"path";import*as R from"fs";import{fileURLToPath as Se}from"url";import{createRequire as be,register as we}from"node:module";import{createRequire as Oe}from"node:module";var B=Oe(import.meta.url),x={exports:{}},A={BUILD_INSERT_PRODUCT_CONFIGURATION:"BUILD_INSERT_PRODUCT_CONFIGURATION"};A.BUILD_INSERT_PRODUCT_CONFIGURATION&&(A=B("../product.json"));var k={"name":"Code","version":"1.94.1","private":true,"overrides":{"node-gyp-build":"4.8.1"},"type":"module"};k.BUILD_INSERT_PACKAGE_CONFIGURATION&&(k=B("../package.json")),x.exports.product=A,x.exports.pkg=k;var v=x.exports.product,Ee=x.exports.pkg,W={};le(W,{getMarks:()=>Pe,mark:()=>S});var P={exports:{}};(function(){function r(o){const i=[];typeof o=="number"&&i.push("code/timeOrigin",o);function f(a){i.push(a,Date.now())}function d(){const a=[];for(let u=0;u<i.length;u+=2)a.push({name:i[u],startTime:i[u+1]});return a}return{mark:f,getMarks:d}}function t(){if(typeof performance=="object"&&typeof performance.mark=="function"&&!performance.nodeTiming)return typeof performance.timeOrigin!="number"&&!performance.timing?r():{mark(o){performance.mark(o)},getMarks(){let o=performance.timeOrigin;typeof o!="number"&&(o=performance.timing.navigationStart||performance.timing.redirectStart||performance.timing.fetchStart);const i=[{name:"code/timeOrigin",startTime:Math.round(o)}];for(const f of performance.getEntriesByType("mark"))i.push({name:f.name,startTime:Math.round(o+f.startTime)});return i}};if(typeof process=="object"){const o=performance?.timeOrigin;return r(o)}else return console.trace("perf-util loaded in UNKNOWN environment"),r()}function n(o){return o.MonacoPerformanceMarks||(o.MonacoPerformanceMarks=t()),o.MonacoPerformanceMarks}var s;typeof global=="object"?s=global:typeof self=="object"?s=self:s={},typeof P=="object"&&typeof P.exports=="object"?P.exports=n(s):(console.trace("perf-util defined in UNKNOWN context (neither requirejs or commonjs)"),s.perf=n(s))})();var S=P.exports.mark,Pe=P.exports.getMarks,xe=be(import.meta.url),z={exports:{}},Ne=ve.dirname(Se(import.meta.url));if((process.env.ELECTRON_RUN_AS_NODE||process.versions.electron)&&we(`data:text/javascript;base64,${Buffer.from(`
	export async function resolve(specifier, context, nextResolve) {
		if (specifier === 'fs') {
			return {
				format: 'builtin',
				shortCircuit: true,
				url: 'node:original-fs'
			};
		}

		// Defer to the next hook in the chain, which would be the
		// Node.js default resolve if this is the last user-specified loader.
		return nextResolve(specifier, context);
	}`).toString("base64")}`,import.meta.url),globalThis._VSCODE_PRODUCT_JSON={...v},process.env.VSCODE_DEV)try{const e=xe("../product.overrides.json");globalThis._VSCODE_PRODUCT_JSON=Object.assign(globalThis._VSCODE_PRODUCT_JSON,e)}catch{}globalThis._VSCODE_PACKAGE_JSON={...Ee},globalThis._VSCODE_FILE_ROOT=Ne;var L=void 0;function De(){return L||(L=je()),L}async function je(){S("code/amd/willLoadNls");let e,r;if(process.env.VSCODE_NLS_CONFIG)try{e=JSON.parse(process.env.VSCODE_NLS_CONFIG),e?.languagePack?.messagesFile?r=e.languagePack.messagesFile:e?.defaultMessagesFile&&(r=e.defaultMessagesFile),globalThis._VSCODE_NLS_LANGUAGE=e?.resolvedLanguage}catch(t){console.error(`Error reading VSCODE_NLS_CONFIG from environment: ${t}`)}if(!(process.env.VSCODE_DEV||!r)){try{globalThis._VSCODE_NLS_MESSAGES=JSON.parse((await R.promises.readFile(r)).toString())}catch(t){if(console.error(`Error reading NLS messages file ${r}: ${t}`),e?.languagePack?.corruptMarkerFile)try{await R.promises.writeFile(e.languagePack.corruptMarkerFile,"corrupted")}catch(n){console.error(`Error writing corrupted NLS marker file: ${n}`)}if(e?.defaultMessagesFile&&e.defaultMessagesFile!==r)try{globalThis._VSCODE_NLS_MESSAGES=JSON.parse((await R.promises.readFile(e.defaultMessagesFile)).toString())}catch(n){console.error(`Error reading default NLS messages file ${e.defaultMessagesFile}: ${n}`)}}return S("code/amd/didLoadNls"),e}}z.exports.load=function(e,r,t){e&&(e=`./${e}.js`,r=r||function(){},t=t||function(n){console.error(n)},De().then(()=>{S("code/fork/willLoadCode"),import(e).then(r,t)}))};var Ce=z.exports.load;import*as Te from"path";import*as Re from"fs";var N={exports:{}};(function(){function r(t,n,s){async function o(c){try{return await n.promises.access(c),!0}catch{return!1}}function i(c){const _=new Date;return n.promises.utimes(c,_,_)}async function f(c){const _=t.join(c,"languagepacks.json");try{return JSON.parse(await n.promises.readFile(_,"utf-8"))}catch{return}}function d(c,_){try{for(;_;){if(c[_])return _;const p=_.lastIndexOf("-");if(p>0)_=_.substring(0,p);else return}}catch(p){console.error("Resolving language pack configuration failed.",p)}}function a(c,_,p){return s.mark("code/didGenerateNls"),{userLocale:c,osLocale:_,resolvedLanguage:"en",defaultMessagesFile:t.join(p,"nls.messages.json"),locale:c,availableLanguages:{}}}async function u({userLocale:c,osLocale:_,userDataPath:p,commit:l,nlsMetadataPath:m}){if(s.mark("code/willGenerateNls"),process.env.VSCODE_DEV||c==="pseudo"||c.startsWith("en")||!l||!p)return a(c,_,m);try{const g=await f(p);if(!g)return a(c,_,m);const y=d(g,c);if(!y)return a(c,_,m);const b=g[y],D=b?.translations?.vscode;if(!b||typeof b.hash!="string"||!b.translations||typeof D!="string"||!await o(D))return a(c,_,m);const F=`${b.hash}.${y}`,w=t.join(p,"clp",F),O=t.join(w,l),M=t.join(O,"nls.messages.json"),j=t.join(w,"tcf.json"),C=t.join(w,"corrupted.info");await o(C)&&await n.promises.rm(w,{recursive:!0,force:!0,maxRetries:3});const U={userLocale:c,osLocale:_,resolvedLanguage:y,defaultMessagesFile:t.join(m,"nls.messages.json"),languagePack:{translationsConfigFile:j,messagesFile:M,corruptMarkerFile:C},locale:c,availableLanguages:{"*":y},_languagePackId:F,_languagePackSupport:!0,_translationsConfigFile:j,_cacheRoot:w,_resolvedLanguagePackCoreLocation:O,_corruptedFile:C};if(await o(O))return i(O).catch(()=>{}),s.mark("code/didGenerateNls"),U;const[,Z,ee,re]=await Promise.all([n.promises.mkdir(O,{recursive:!0}),JSON.parse(await n.promises.readFile(t.join(m,"nls.keys.json"),"utf-8")),JSON.parse(await n.promises.readFile(t.join(m,"nls.messages.json"),"utf-8")),JSON.parse(await n.promises.readFile(D,"utf-8"))]),V=[];let G=0;for(const[te,ne]of Z){const oe=re.contents[te];for(const se of ne)V.push(oe?.[se]||ee[G]),G++}return await Promise.all([n.promises.writeFile(M,JSON.stringify(V),"utf-8"),n.promises.writeFile(j,JSON.stringify(b.translations),"utf-8")]),s.mark("code/didGenerateNls"),U}catch(g){console.error("Generating translation files failed.",g)}return a(c,_,m)}return{resolveNLSConfiguration:u}}if(typeof N=="object"&&typeof N.exports=="object")N.exports=r(Te,Re,W);else throw new Error("vs/base/node/nls defined in UNKNOWN context (neither requirejs or commonjs)")})();var Ae=N.exports.resolveNLSConfiguration,Q=$.dirname(pe(import.meta.url));S("code/server/start"),global.vscodeServerStartTime=H.now();async function ke(){const e=de(process.argv.slice(2),{boolean:["start-server","list-extensions","print-ip-address","help","version","accept-server-license-terms","update-extensions"],string:["install-extension","install-builtin-extension","uninstall-extension","locate-extension","socket-path","host","port","compatibility"],alias:{help:"h",version:"v"}});["host","port","accept-server-license-terms"].forEach(l=>{if(!e[l]){const m=process.env[`VSCODE_SERVER_${l.toUpperCase().replace("-","_")}`];m&&(e[l]=m)}});const r=["list-extensions","locate-extension"],t=["install-extension","install-builtin-extension","uninstall-extension","update-extensions"],n=e.help||e.version||r.some(l=>!!e[l])||t.some(l=>!!e[l])&&!e["start-server"],s=await Ae({userLocale:"en",osLocale:"en",commit:v.commit,userDataPath:"",nlsMetadataPath:Q});if(n){Y(s).then(l=>{l.spawnCli()});return}let o=null,i=null;const f=()=>(i||(i=Y(s).then(async l=>{const m=await l.createServer(u);return o=m,m})),i);if(Array.isArray(v.serverLicense)&&v.serverLicense.length&&(console.log(v.serverLicense.join(`
`)),v.serverLicensePrompt&&e["accept-server-license-terms"]!==!0)){Me()&&(console.log("To accept the license terms, start the server with --accept-server-license-terms"),process.exit(1));try{await X(v.serverLicensePrompt)||process.exit(1)}catch(l){console.log(l),process.exit(1)}}let d=!0,a=!0,u=null;const c=J.createServer(async(l,m)=>(d&&(d=!1,S("code/server/firstRequest")),(await f()).handleRequest(l,m)));c.on("upgrade",async(l,m)=>(a&&(a=!1,S("code/server/firstWebSocket")),(await f()).handleUpgrade(l,m))),c.on("error",async l=>(await f()).handleServerError(l));const _=I(e.host)||(e.compatibility!=="1.63"?"localhost":void 0),p=e["socket-path"]?{path:I(e["socket-path"])}:{host:_,port:await Le(_,I(e.port))};c.listen(p,async()=>{let l=Array.isArray(v.serverGreeting)&&v.serverGreeting.length?`

${v.serverGreeting.join(`
`)}

`:"";if(typeof p.port=="number"&&e["print-ip-address"]){const m=fe.networkInterfaces();Object.keys(m).forEach(function(g){m[g]?.forEach(function(y){!y.internal&&y.family==="IPv4"&&(l+=`IP Address: ${y.address}
`)})})}if(u=c.address(),u===null)throw new Error("Unexpected server address");l+=`Server bound to ${typeof u=="string"?u:`${u.address}:${u.port} (${u.family})`}
`,l+=`Extension host agent listening on ${typeof u=="string"?u:u.port}
`,console.log(l),S("code/server/started"),global.vscodeServerListenTime=H.now(),await f()}),process.on("exit",()=>{c.close(),o&&o.dispose()})}function I(e){return Array.isArray(e)&&(e=e.pop()),typeof e=="string"?e:void 0}async function Le(e,r){if(r){let t;if(r.match(/^\d+$/))return parseInt(r,10);if(t=Ie(r)){const n=await Fe(e,t.start,t.end);if(n!==void 0)return n;console.warn(`--port: Could not find free port in range: ${t.start} - ${t.end} (inclusive).`),process.exit(1)}else console.warn(`--port "${r}" is not a valid number or range. Ranges must be in the form 'from-to' with 'from' an integer larger than 0 and not larger than 'end'.`),process.exit(1)}return 8e3}function Ie(e){const r=e.match(/^(\d+)-(\d+)$/);if(r){const t=parseInt(r[1],10),n=parseInt(r[2],10);if(t>0&&t<=n&&n<=65535)return{start:t,end:n}}}async function Fe(e,r,t){const n=s=>new Promise(o=>{const i=J.createServer();i.listen(s,e,()=>{i.close(),o(!0)}).on("error",()=>{o(!1)})});for(let s=r;s<=t;s++)if(await n(s))return s}function Y(e){return new Promise((r,t)=>{process.env.VSCODE_NLS_CONFIG=JSON.stringify(e),process.env.VSCODE_HANDLES_SIGPIPE="true",process.env.VSCODE_DEV?(process.env.VSCODE_DEV_INJECT_NODE_MODULE_LOOKUP_PATH=process.env.VSCODE_DEV_INJECT_NODE_MODULE_LOOKUP_PATH||$.join(Q,"..","remote","node_modules"),he(process.env.VSCODE_DEV_INJECT_NODE_MODULE_LOOKUP_PATH)):delete process.env.VSCODE_DEV_INJECT_NODE_MODULE_LOOKUP_PATH,Ce("vs/server/node/server.main",r,t)})}function Me(){try{return!process.stdin.isTTY}catch{}return!1}function X(e){const r=ue.createInterface({input:process.stdin,output:process.stdout});return new Promise((t,n)=>{r.question(e+" ",async function(s){r.close();const o=s.toString().trim().toLowerCase();o===""||o==="y"||o==="yes"?t(!0):o==="n"||o==="no"?t(!1):(process.stdout.write(`
Invalid Response. Answer either yes (y, yes) or no (n, no)
`),t(await X(e)))})})}ke();

//# sourceMappingURL=https://main.vscode-cdn.net/sourcemaps/e10f2369d0d9614a452462f2e01cdc4aa9486296/core/server-main.js.map
