/** Transparent daily-bar research engine. No broker calls. */
export const strategies = [
 {id:'hold',name:'Buy & hold',family:'Passive',rule:'Buy at the first evaluation open and hold.'},
 {id:'trend',name:'Moving-average trend',family:'Trend',rule:'Long when the previous close is above its 100-session average; otherwise cash.'},
 {id:'momentum',name:'Absolute momentum',family:'Momentum',rule:'Long when the previous close exceeds the close 63 sessions earlier; otherwise cash.'},
 {id:'breakout',name:'Channel breakout',family:'Breakout',rule:'Enter above the prior 20-session high. Exit below the prior 10-session low.'},
 {id:'rsi',name:'RSI mean reversion',family:'Mean reversion',rule:'Enter below Wilder RSI(14) 30. Exit above 50. Hold between thresholds.'},
];
export const defaultConfig={capital:100,allocation:25,costBps:10,fee:0,drawdownStop:10,split:0.7,currency:'GBP'};
export function validateBars(bars){
 if(!Array.isArray(bars)||bars.length<180||bars.length>10000)throw Error('Use between 180 and 10,000 daily price rows.');
 let last='';
 for(const b of bars){
  if(!/^\d{4}-\d{2}-\d{2}$/.test(b.date)||Number.isNaN(Date.parse(b.date))||new Date(b.date+'T00:00:00Z').toISOString().slice(0,10)!==b.date||b.date<=last)throw Error('Dates must be valid, unique and in ascending order.');
  if(!['open','high','low','close'].every(k=>Number.isFinite(b[k])&&b[k]>0)||b.high<Math.max(b.open,b.close,b.low)||b.low>Math.min(b.open,b.close,b.high))throw Error('Each price must be positive and inside its daily high/low.');
  last=b.date;
 }
 return bars;
}
export function parseCSV(text){
 const lines=text.trim().replace(/^\uFEFF/,'').split(/\r?\n/);const head=lines.shift().toLowerCase().split(',').map(s=>s.trim());
 const required=['date','open','high','low','close'];if(!required.every(k=>head.includes(k)))throw Error('CSV needs date,open,high,low,close columns.');
 if(new Set(head).size!==head.length)throw Error('CSV column names must be unique.');
 const bars=lines.filter(s=>s.trim()).map(s=>{const c=s.split(',').map(v=>v.trim());const b={};for(const k of required)b[k]=k==='date'?c[head.indexOf(k)]:Number(c[head.indexOf(k)]);return b;});return validateBars(bars);
}
export function demoBars(regime='mixed'){
 let seed=92814,price=100;const random=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/4294967296;};const out=[];const day=new Date('2023-01-02T00:00:00Z');
 while(out.length<756){if(day.getUTCDay()!==0&&day.getUTCDay()!==6){let i=out.length;const drift=regime==='trend'?0.0012:regime==='stress'?(i>470&&i<550?-0.014:0.00025):(i<230?0.001:i<410?-0.0012:i<590?0:0.0007);const open=price*(1+(random()-.5)*.01);price=Math.max(1,open*(1+drift+(random()-.5)*.036));out.push({date:day.toISOString().slice(0,10),open,high:Math.max(open,price)*(1+random()*.012),low:Math.min(open,price)*(1-random()*.012),close:price});}day.setUTCDate(day.getUTCDate()+1);}return out;
}
export function rsiValues(bars,period=14){
 let gain=0,loss=0;const out=Array(bars.length).fill(null);
 for(let i=1;i<bars.length;i++){const delta=bars[i].close-bars[i-1].close;if(i<=period){gain+=Math.max(0,delta)/period;loss+=Math.max(0,-delta)/period;}else{gain=(gain*(period-1)+Math.max(0,delta))/period;loss=(loss*(period-1)+Math.max(0,-delta))/period;}if(i>=period)out[i]=gain===0&&loss===0?50:loss===0?100:100-100/(1+gain/loss);}
 return out;
}
export function signal(bars,i,id,held,rsi){
 if(id==='hold')return true;
 if(id==='trend')return bars[i].close>bars.slice(i-99,i+1).reduce((s,b)=>s+b.close,0)/100;
 if(id==='momentum')return bars[i].close>bars[i-63].close;
 if(id==='breakout')return held?!(bars[i].close<Math.min(...bars.slice(i-10,i).map(b=>b.low))):bars[i].close>Math.max(...bars.slice(i-20,i).map(b=>b.high));
 if(id==='rsi'){const val=rsi[i];return held?val<=50:val<30;}
 throw Error('Unknown strategy.');
}
export function validateConfig(c){
 for(const k of ['capital','allocation','costBps','fee','drawdownStop','split'])if(!Number.isFinite(c[k]))throw Error('Enter valid numeric assumptions.');
 if(c.capital<1||c.capital>1e8||c.allocation<1||c.allocation>100||c.costBps<0||c.costBps>500||c.fee<0||c.fee>100||c.drawdownStop<1||c.drawdownStop>100||c.split<.5||c.split>.85)throw Error('An assumption is outside the supported range.');
 if(!['GBP','USD','EUR'].includes(c.currency))throw Error('Choose the currency of the imported prices.');return c;
}
export function backtest(bars,id,config=defaultConfig,phase='research'){
 validateBars(bars);const c=validateConfig({...defaultConfig,...config});if(!strategies.some(s=>s.id===id))throw Error('Unknown strategy.');if(!['research','holdout','all'].includes(phase))throw Error('Unknown evaluation window.');
 const cut=Math.floor(bars.length*c.split),start=phase==='holdout'?cut:101,end=phase==='research'?cut:bars.length;
 let cash=c.capital,qty=0,peak=c.capital,maxDrawdown=0,totalCosts=0,entryValue=0,halted=false,pendingStop=false;let wins=0,closed=0;const curve=[],trades=[],rsi=rsiValues(bars);const bps=c.costBps/10000;
 function buy(b,index){const budget=Math.min(cash,(cash+qty*b.open)*c.allocation/100);if(budget<=c.fee)return;const price=b.open*(1+bps);qty=(budget-c.fee)/price;entryValue=budget;cash-=budget;totalCosts+=c.fee+qty*(price-b.open);trades.push({date:b.date,signalDate:bars[index-1].date,side:'buy',price,qty,fee:c.fee,reason:strategies.find(s=>s.id===id).name});}
 function sell(b,reason){const price=b.open*(1-bps),proceeds=qty*price-c.fee;cash+=proceeds;totalCosts+=c.fee+qty*(b.open-price);closed++;if(proceeds>entryValue)wins++;trades.push({date:b.date,side:'sell',price,qty,fee:c.fee,reason});qty=0;}
 for(let i=start;i<end;i++){
  const b=bars[i];if(pendingStop){if(qty>0)sell(b,'Drawdown stop: next open');pendingStop=false;halted=true;}
  if(!halted){const long=signal(bars,i-1,id,qty>0,rsi);if(long&&qty===0)buy(b,i);else if(!long&&qty>0)sell(b,'Signal exit');}
  const equity=cash+qty*b.close;peak=Math.max(peak,equity);const drawdown=(peak-equity)/peak*100;maxDrawdown=Math.max(maxDrawdown,drawdown);if(drawdown>=c.drawdownStop&&!halted){pendingStop=true;halted=true;}
  curve.push({date:b.date,equity,drawdown,cash,qty});
 }
 const finalEquity=curve.at(-1)?.equity??c.capital;return {id,phase,config:c,start:bars[start].date,end:bars[end-1].date,finalEquity,returnPct:(finalEquity/c.capital-1)*100,maxDrawdown,totalCosts,trades,curve,winRate:closed?wins/closed*100:null,closed,halted,openPosition:qty>0,pendingStop};
}
export function barsToCSV(bars){return 'date,open,high,low,close\n'+bars.map(b=>[b.date,b.open,b.high,b.low,b.close].join(',')).join('\n');}
