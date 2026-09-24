import {createHash} from 'node:crypto';
import {preflight} from './broker.mjs';
import {signal,rsiValues,validateBars} from './engine.mjs';
export async function paperStep({broker,state,save,enabled=false,strategy='trend',symbol='SPY',now=Date.now(),log=()=>{}}){
 const budget=100,maxPosition=25,maxBuy=5,lossLimit=2;
 const note=(event,details={})=>state.journal.push({at:new Date(now).toISOString(),event,...details});
 const [account,clock,positions,orders,asset,bar]=await Promise.all([broker.account(),broker.clock(),broker.positions(),broker.orders(),broker.asset(symbol),broker.latest(symbol)]);
 const configuration=JSON.stringify({strategy,symbol,budget,maxPosition,maxBuy,lossLimit});
 if(state.accountId&&state.accountId!==account.id)throw Error('Journal belongs to another account. Use a separate state directory.');
 if(state.configuration&&state.configuration!==configuration)throw Error('Configuration changed. Reconcile the account and use a separate journal.');
 state.accountId=account.id;state.configuration=configuration;await save();
 if(state.pending){const existing=await broker.findOrder(state.pending.client_order_id);if(!existing)throw Error('An earlier order has an unknown outcome. Manual reconciliation is required; it will not be resubmitted.');
  if(!['filled','canceled','expired','rejected'].includes(existing.status))throw Error('Earlier order is still pending at the paper broker.');
  note('reconciled',{id:existing.id,status:existing.status,filledQty:existing.filled_qty});state.pending=null;await save();return;}
 if(!clock.is_open){log('Paper runner: market closed; no order.');return;}
 const balances=preflight({account,clock,positions,orders,asset,bar,symbol,now});
 if(balances.equity>125)throw Error('Reset a dedicated paper account to approximately $100 before enabling this runner. Large default paper balances are rejected.');
 const day=new Intl.DateTimeFormat('en-CA',{timeZone:'America/New_York',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date(clock.timestamp));
 const daily=state.days[day]??={openingEquity:balances.equity,halted:false,acted:false};
 if(daily.openingEquity-balances.equity>=lossLimit)daily.halted=true;
 await save();
 if(daily.acted&&(!daily.halted||balances.qty===0||daily.riskExited)){log('Paper runner: today’s action is complete.');return;}
 const bars=validateBars(await broker.bars(symbol));
 const age=Date.parse(day)-Date.parse(bars.at(-1).date);if(age<=0||age>4*86400000)throw Error('Completed daily signal data is stale or not strictly before today.');
 const long=signal(bars,bars.length-1,strategy,balances.qty>0,rsiValues(bars));
 let order;const riskExit=daily.halted&&balances.qty>0;const key=createHash('sha256').update(account.id+configuration+day+(riskExit?'riskexit':'signal')).digest('hex').slice(0,28);const base={symbol,type:'market',time_in_force:'day',extended_hours:false,client_order_id:'sterling-'+key};
 if(balances.qty>0&&(!long||daily.halted)){order={...base,side:'sell',qty:String(Math.floor(balances.qty*1e8)/1e8)};}
 else if(long&&balances.qty===0&&!daily.halted){const notional=Math.floor(Math.min(maxBuy,maxPosition-balances.value,budget-balances.value,balances.cash-.10,balances.buying-.10)*100)/100;if(notional>=1)order={...base,side:'buy',notional:notional.toFixed(2)};}
 if(!order){log('Paper runner: hold; no order.');return;}
 if(!enabled){log('DRY RUN: paper order candidate',order);return;}
 // Persist before submission. Even a timeout/404 never authorizes a blind resubmission.
 const duplicate=await broker.findOrder(base.client_order_id);if(duplicate){daily.acted=true;if(riskExit)daily.riskExited=true;state.pending=order;note('existing_order',{id:duplicate.id,status:duplicate.status});await save();return;}
 state.pending=order;daily.acted=true;if(riskExit)daily.riskExited=true;note('intent',{...order,signalDate:bars.at(-1).date});await save();
 try{const result=await broker.submit(order);note('accepted',{id:result.id,status:result.status});await save();log('Paper order accepted; awaiting reconciliation. This is not a confirmed fill.');}catch(e){note('submission_unknown');await save();throw e;}
}
