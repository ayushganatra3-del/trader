const PAPER='https://paper-api.alpaca.markets';
const DATA='https://data.alpaca.markets';
export const supportedSymbols=['SPY','AAPL','MSFT'];
export function createPaperBroker(env,fetcher=globalThis.fetch){
 const configured=Boolean(env.APCA_API_KEY_ID&&env.APCA_API_SECRET_KEY);
 async function request(path,{method='GET',body,data=false,allow404=false}={}){
  if(!configured)throw Error('Paper broker is not configured. Add paper credentials on the server.');
  const response=await fetcher((data?DATA:PAPER)+path,{method,redirect:'error',headers:{'APCA-API-KEY-ID':env.APCA_API_KEY_ID,'APCA-API-SECRET-KEY':env.APCA_API_SECRET_KEY,'Content-Type':'application/json'},body:body?JSON.stringify(body):undefined,signal:AbortSignal.timeout(12000)});
  if(allow404&&response.status===404)return null;
  if(!response.ok)throw Error(`Paper broker request failed (${response.status}). Check credentials, data access and account status.`);
  return response.status===204?null:response.json();
 }
 return {configured,
  account:()=>request('/v2/account'),clock:()=>request('/v2/clock'),positions:()=>request('/v2/positions'),
  orders:()=>request('/v2/orders?status=open&limit=500'),
  historyOrders:()=>request('/v2/orders?status=all&limit=50&direction=desc'),
  asset:(symbol)=>{if(!supportedSymbols.includes(symbol))throw Error('Unsupported symbol.');return request('/v2/assets/'+symbol);},
  findOrder:(id)=>request('/v2/orders:by_client_order_id?client_order_id='+encodeURIComponent(id),{allow404:true}),
  submit:order=>{if(!supportedSymbols.includes(order.symbol)||!['buy','sell'].includes(order.side)||order.type!=='market'||order.time_in_force!=='day'||order.extended_hours!==false||!/^sterling-[a-zA-Z0-9-]{1,38}$/.test(order.client_order_id))throw Error('Paper order failed validation.');if(order.side==='buy'&&(!Number.isFinite(Number(order.notional))||Number(order.notional)<1||Number(order.notional)>5||order.qty!==undefined))throw Error('Paper buy must be between $1 and $5.');if(order.side==='sell'&&(!Number.isFinite(Number(order.qty))||Number(order.qty)<=0||order.notional!==undefined))throw Error('Invalid exit quantity.');return request('/v2/orders',{method:'POST',body:order});},
  latest:async symbol=>{if(!supportedSymbols.includes(symbol))throw Error('Unsupported symbol.');const r=await request('/v2/stocks/bars/latest?symbols='+symbol+'&feed=iex',{data:true});return r.bars?.[symbol];},
  bars:async(symbol)=>{
   if(!supportedSymbols.includes(symbol))throw Error('Unsupported symbol.');const start=new Date();start.setUTCFullYear(start.getUTCFullYear()-3);const today=new Date().toISOString().slice(0,10);let page='',all=[];
   for(let i=0;i<10;i++){const q=new URLSearchParams({timeframe:'1Day',start:start.toISOString(),end:today+'T00:00:00Z',adjustment:'all',feed:'iex',limit:'10000',sort:'asc'});if(page)q.set('page_token',page);const r=await request('/v2/stocks/'+symbol+'/bars?'+q,{data:true});all.push(...(r.bars??[]));if(!r.next_page_token)break;page=r.next_page_token;if(i===9)throw Error('Price history exceeded the pagination limit.');}
   return all.map(b=>({date:b.t.slice(0,10),open:b.o,high:b.h,low:b.l,close:b.c})).filter(b=>b.date<today);
  },
 };
}
export function preflight({account,clock,asset,positions,orders,bar,symbol,now=Date.now()}){
 if(!supportedSymbols.includes(symbol))throw Error('Symbol is not allowed.');
 if(account.status!=='ACTIVE'||account.trading_blocked||account.account_blocked||account.trade_suspended_by_user)throw Error('Account is not available for trading.');
 if(account.currency!=='USD')throw Error('This paper adapter requires a USD account.');
 const equity=Number(account.equity),cash=Number(account.cash),buying=Number(account.non_marginable_buying_power);
 if(![equity,cash,buying].every(Number.isFinite)||equity<=0||cash<0||buying<0)throw Error('Invalid account balances.');
 if(!clock.is_open||!Number.isFinite(Date.parse(clock.timestamp))||Math.abs(now-Date.parse(clock.timestamp))>120000)throw Error('Regular market session is closed or clock is stale.');
 if(asset.status!=='active'||!asset.tradable||!asset.fractionable)throw Error('Asset is not active, tradable and fractional.');
 if(!bar||!Number.isFinite(bar.c)||bar.c<=0||!Number.isFinite(Date.parse(bar.t))||now-Date.parse(bar.t)>180000||Date.parse(bar.t)>now+5000)throw Error('Latest IEX minute bar is missing or stale.');
 if(orders.length)throw Error('Open orders must be reconciled before the next action.');
 if(positions.some(p=>p.symbol!==symbol||p.side!=='long'||!Number.isFinite(Number(p.qty))||Number(p.qty)<0))throw Error('Use a dedicated paper account with only the configured long position.');
 const position=positions.find(p=>p.symbol===symbol);const value=position?Number(position.market_value):0;
 if(!Number.isFinite(value)||value<0)throw Error('Invalid position value.');
 const qty=position?Number(position.qty_available??position.qty):0;if(!Number.isFinite(qty)||qty<0)throw Error('Invalid available quantity.');
 return {equity,cash,buying,value,qty};
}
