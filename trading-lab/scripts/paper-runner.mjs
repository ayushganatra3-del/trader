/** Explicitly started, paper-only runner. Never imported by the hosted application. */
import { mkdir,open,readFile,rename,unlink,writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { paperStep } from '../lib/paper-session.mjs';
import { createPaperBroker,supportedSymbols } from '../lib/broker.mjs';
import { strategies } from '../lib/engine.mjs';
const dir=resolve(process.env.PAPER_STATE_DIR??'.paper-state');
const strategy=process.env.PAPER_STRATEGY??'trend',symbol=process.env.PAPER_SYMBOL??'SPY';
const enabled=process.argv.includes('--enable-paper-orders');
const once=process.argv.includes('--once');
if(!supportedSymbols.includes(symbol)||!strategies.some(s=>s.id===strategy))throw Error('Invalid paper strategy or symbol.');
const broker=createPaperBroker(process.env);if(!broker.configured)throw Error('Set Alpaca PAPER credentials in the local environment first.');
await mkdir(dir,{recursive:true,mode:0o700});
const lock=await open(resolve(dir,'runner.lock'),'wx',0o600).catch(()=>{throw Error('Runner lock exists. Confirm the earlier process has stopped before removing the stale lock.');});
await lock.writeFile(String(process.pid));
const file=resolve(dir,'journal.json');
let state;try{state=JSON.parse(await readFile(file,'utf8'));}catch(e){if(e.code!=='ENOENT')throw e;state={version:1,accountId:null,configuration:null,pending:null,days:{},journal:[]};}
async function save(){const temp=file+'.tmp';const handle=await open(temp,'w',0o600);try{await handle.writeFile(JSON.stringify(state,null,2));await handle.sync();}finally{await handle.close();}await rename(temp,file);const folder=await open(dir,'r');try{await folder.sync();}finally{await folder.close();}}
let stopping=false;for(const s of ['SIGINT','SIGTERM'])process.on(s,()=>{stopping=true;});

console.log(enabled?'PAPER ORDERS ENABLED. Fixed Alpaca paper endpoint; USD only.':'DRY RUN. No orders will be submitted.');
try{do{try{await paperStep({broker,state,save,enabled,strategy,symbol,log:console.log});}catch(e){console.error(e.message);if(once)process.exitCode=1;}if(!once&&!stopping)await new Promise(r=>{const timeout=setTimeout(()=>{clearInterval(interval);r();},60000);const interval=setInterval(()=>{if(stopping){clearInterval(interval);clearTimeout(timeout);r();}},250);});}while(!once&&!stopping);}finally{await lock.close();await unlink(resolve(dir,'runner.lock'));}
