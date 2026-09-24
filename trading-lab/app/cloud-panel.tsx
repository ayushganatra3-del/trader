'use client';
import { useEffect, useState } from 'react';
import { Cloud, RefreshCw, ArrowUpRight, Download, Clock3, ShieldCheck } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from '@/components/ui/table';
import { cloudWorkflow, repository } from '@/lib/cloud-ledger.mjs';

type Fill = { event_id: string; type: string; symbol: string; side: string; quantity: number; execution_price_gbp: number; decision_at: string; effective_fill_at: string; recognised_at: string; realised_gbp: number; reason: string };
type Session = { session_day: string; status: string; last_check_at: string | null; starting_cash_gbp: number; halted: boolean; halt_reason: string | null; buy_fills: number; events: Fill[]; intents: { intent_id: string; symbol: string; side: string; status: string; decision_at: string; reason: string }[]; positions: Record<string, { quantity: number; mark_gbp: number; mark_bar_end: string; mark_observed_at: string }>; quotes: Record<string, { status: string; error?: string; latest_end?: string }>; totals: { cash_gbp: number; holdings_gbp: number; equity_gbp: number; realised_gbp: number; unrealised_gbp: number; total_pl_gbp: number } };
type Ledger = { generated_at: string; fetched_at: string; control: { active_session: string | null }; sessions: Session[]; last_check?: unknown };
const money = (v: number) => new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP' }).format(v);
const time = (v?: string | null) => v && Number.isFinite(Date.parse(v)) ? new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit', timeZoneName: 'short' }).format(new Date(v)) : 'Not yet checked';

export function CloudPanel() {
  const [ledger, setLedger] = useState<Ledger | null>(null), [error, setError] = useState(''), [busy, setBusy] = useState(false), [selected, setSelected] = useState('');
  async function refresh() {
    setBusy(true);
    try {
      const response = await fetch('/api/cloud', { cache: 'no-store' });
      const body = await response.json() as Ledger & { message?: string };
      if (!response.ok) throw Error(body.message || 'Could not load the cloud ledger.');
      setLedger(body); setError('');
    } catch (e) { setError(e instanceof Error ? e.message : 'Cloud ledger unavailable.'); }
    finally { setBusy(false); }
  }
  useEffect(() => { void refresh(); const interval = setInterval(() => { if (document.visibilityState === 'visible') void refresh(); }, 60000); return () => clearInterval(interval); }, []);
  const sessions = ledger?.sessions.slice().sort((a, b) => b.session_day.localeCompare(a.session_day)) || [];
  const session = sessions.find(s => s.session_day === selected) || sessions[0];
  const fills = session?.events.filter(e => e.type === 'fill') || [];
  const pending = session?.intents.filter(i => ['pending', 'unresolved'].includes(i.status)) || [];
  const open = Object.entries(session?.positions || {});
  function download() {
    const url = URL.createObjectURL(new Blob([JSON.stringify(session, null, 2)], { type: 'application/json' }));
    const a = document.createElement('a'); a.href = url; a.download = `sterling-${session?.session_day}.json`; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  return <>
    <div className="page-heading"><div><p className="eyebrow">VIRTUAL MONEY · CLOUD RECORDS</p><h1>Your trading desk<span>.</span></h1><p className="muted">Market checks and trade history run in the cloud. Your computer can be off.</p></div><Button variant="outline" disabled={busy} onClick={refresh}><RefreshCw size={16}/>{busy ? 'Loading…' : 'Refresh records'}</Button></div>
    <div className="cloud-status panel"><div className="cloud-status-heading"><Cloud size={23}/><div><h2>{ledger ? ledger.control.active_session ? `Session armed · ${ledger.control.active_session}` : 'No session running' : 'Connecting to your cloud ledger'}</h2><p className="muted">{ledger?.control.active_session ? 'Automatic checks are scheduled about every 15 minutes. Delays and missed checks are possible.' : 'Start one dated £100 virtual session when you are ready. Previous results stay unchanged.'}</p></div></div><a className="external-button" href={cloudWorkflow} target="_blank" rel="noreferrer">Session controls on GitHub <ArrowUpRight size={16}/></a></div>
    {error && <p className="error-message" role="alert">{error}{ledger ? ' The records below are from the last successful refresh.' : ''}</p>}
    <section className="cloud-guide"><ShieldCheck size={19}/><p>Virtual GBP portfolio, no broker orders. Choose <strong>Run workflow → start</strong> and a London date in the cloud controls. Use <strong>stop</strong> to stop new entries and request exits. Stopping cannot invent a fill when prices are missing.</p></section>
    {!session ? <section className="panel prose"><h2>{busy ? 'Loading your sessions…' : 'No sessions available'}</h2><p>{error ? 'Your ledger could not be loaded. Refresh to try again.' : 'A dated session appears here after it has been created in the cloud controls.'}</p></section> : <>
      <div className="cloud-session-select"><label htmlFor="session-date">Session</label><select id="session-date" value={session.session_day} onChange={e => setSelected(e.target.value)}>{sessions.map(s => <option key={s.session_day} value={s.session_day}>{s.session_day} · {s.status}</option>)}</select><span className="mini-tag">{session.status === 'incomplete' ? 'Incomplete close' : session.status}</span><Button variant="outline" onClick={download}><Download size={16}/>Export session</Button></div>
      {session.status === 'incomplete' && <div className="notice"><Clock3 size={20}/><p><strong>Not a realised closing result.</strong> An exit could not be verified. Open holdings use the last valid recorded prices shown below.</p></div>}
      <div className="cloud-metrics">{[['Total recorded value', session.totals.equity_gbp], ['Cash', session.totals.cash_gbp], ['Open holdings', session.totals.holdings_gbp], ['Total profit / loss', session.totals.total_pl_gbp]].map(([label, value]) => <section className="panel cloud-metric" key={label as string}><span>{label}</span><strong className={label === 'Total profit / loss' ? Number(value) >= 0 ? 'positive' : 'negative' : ''}>{money(Number(value))}</strong></section>)}</div>
      <div className="cloud-meta"><span>Started with {money(session.starting_cash_gbp)} · {session.buy_fills} buys</span><span>Realised {money(session.totals.realised_gbp)} · Unrealised {money(session.totals.unrealised_gbp)}</span><span>Last market check {time(session.last_check_at)}</span></div>
      {session.halted && <p className="error-message">New entries stopped: {session.halt_reason}</p>}
      <section className="panel comparison"><div className="panel-head"><h2>Open holdings</h2><span className="muted">Value includes modelled entry costs in P/L</span></div><Table><TableHeader><TableRow><TableHead>Instrument</TableHead><TableHead>Units</TableHead><TableHead>Last price</TableHead><TableHead>Price time</TableHead><TableHead>Holding value</TableHead></TableRow></TableHeader><TableBody>{open.map(([symbol, p]) => <TableRow key={symbol}><TableCell>{symbol}</TableCell><TableCell>{p.quantity.toFixed(8)}</TableCell><TableCell>{money(p.mark_gbp)}</TableCell><TableCell>{time(p.mark_bar_end)}</TableCell><TableCell>{money(p.quantity * p.mark_gbp)}</TableCell></TableRow>)}</TableBody></Table>{!open.length && <p className="empty-message">No open holdings.</p>}</section>
      {pending.length > 0 && <section className="panel trade-panel"><h2>Pending and unresolved decisions</h2>{pending.map(i => <div className="cloud-intent" key={i.intent_id}><strong>{i.symbol} · {i.side} · {i.status}</strong><p>{i.reason}</p><small>Decided {time(i.decision_at)}. This is not a completed trade.</small></div>)}</section>}
      <section className="panel comparison"><div className="panel-head"><div><p className="eyebrow">RECORDED SIMULATED FILLS</p><h2>Trade history</h2></div><span className="muted">0.10% modelled cost per side</span></div><Table><TableHeader><TableRow><TableHead>Instrument / action</TableHead><TableHead>Units</TableHead><TableHead>Fill price</TableHead><TableHead>Decision time</TableHead><TableHead>Effective fill</TableHead><TableHead>Recognised</TableHead><TableHead>Realised P/L</TableHead></TableRow></TableHeader><TableBody>{fills.map(f => <TableRow key={f.event_id}><TableCell>{f.symbol} · {f.side}</TableCell><TableCell>{f.quantity.toFixed(8)}</TableCell><TableCell>{money(f.execution_price_gbp)}</TableCell><TableCell>{time(f.decision_at)}</TableCell><TableCell>{time(f.effective_fill_at)}</TableCell><TableCell>{time(f.recognised_at)}</TableCell><TableCell>{f.side === 'sell' ? money(f.realised_gbp) : '—'}</TableCell></TableRow>)}</TableBody></Table>{!fills.length && <p className="empty-message">No fills recorded for this session.</p>}<p className="cloud-caption">A decision is recorded first. A later check can recognise a hypothetical fill from a complete bar after that decision. Delayed prices are not live executable quotes.</p></section>
      <details className="panel cloud-details"><summary>Data quality and session rules</summary><p>ISF, VUSA and EQQQ. Up to two £40 positions, six entries, no leverage. Entries require price above session VWAP and positive 20-minute momentum. Exits follow VWAP, a 1% stop signal or a 2% profit signal. A £3 portfolio loss halts entries; it is not a guaranteed loss limit.</p><p>London time: entries stop at 15:45, exits are requested from 16:15, and the session finalises from 17:00. Public prices may be delayed or missing; unavailable observations cannot create trades.</p>{Object.entries(session.quotes || {}).map(([symbol, q]) => <p key={symbol}><strong>{symbol}</strong>: {q.status}. Last valid bar {time(q.latest_end)}{q.error ? ` · ${q.error}` : ''}</p>)}</details>
    </>}
    <p className="cloud-caption">The <a href={repository} target="_blank" rel="noreferrer">repository</a> and its virtual-trading ledger are public. Saved research experiments remain private to your signed-in account. Cloud records updated {time(ledger?.generated_at)}.</p>
  </>;
}
