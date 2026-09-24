import { env } from 'cloudflare:workers';
import { createPaperBroker } from '@/lib/broker.mjs';
const headers={'Cache-Control':'no-store, private','X-Content-Type-Options':'nosniff'};
export async function GET(request:Request){
 if(!request.headers.get('oai-authenticated-user-id'))return Response.json({connected:false,message:'Sign in to this private Site to view the paper account.'},{status:401,headers});
 const broker=createPaperBroker(env as Record<string,string>);
 if(!broker.configured)return Response.json({connected:false,mode:'paper',message:'No paper broker connected. Server-side credentials are required.'},{headers});
 try{
  const symbol=new URL(request.url).searchParams.get('symbol');
  if(symbol){const bars=await broker.bars(symbol);return Response.json({symbol,currency:'USD',feed:'iex',adjustment:'all',bars},{headers});}
  const [account,positions,orders,clock]=await Promise.all([broker.account(),broker.positions(),broker.historyOrders(),broker.clock()]);
  return Response.json({connected:true,mode:'paper',currency:account.currency,equity:account.equity,cash:account.cash,status:account.status,marketOpen:clock.is_open,asOf:clock.timestamp,positions:positions.map((p:any)=>({symbol:p.symbol,qty:p.qty,marketValue:p.market_value,unrealized:p.unrealized_pl})),orders:orders.map((o:any)=>({id:o.id,symbol:o.symbol,side:o.side,status:o.status,notional:o.notional,qty:o.qty,filledQty:o.filled_qty,filledPrice:o.filled_avg_price,submittedAt:o.submitted_at}))},{headers});
 }catch(error){return Response.json({connected:false,mode:'paper',message:error instanceof Error?error.message:'Paper broker unavailable.'},{status:502,headers});}
}
