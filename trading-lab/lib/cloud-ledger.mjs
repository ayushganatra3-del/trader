import { boundedJSON } from './bounded-json.mjs';
export const repository = 'https://github.com/ayushganatra3-del/trader';
export const cloudWorkflow = `${repository}/actions/workflows/virtual-trading.yml`;
export const ledgerURL = 'https://raw.githubusercontent.com/ayushganatra3-del/trader/trading-state/data/dashboard.json';

export function validateDashboard(value) {
  if (!value || value.version !== 1 || !Array.isArray(value.sessions) || value.sessions.length > 366 || !value.control) throw Error('Cloud ledger format is invalid.');
  if (value.control.active_session !== null && (typeof value.control.active_session !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value.control.active_session))) throw Error('Invalid cloud session control.');
  if (typeof value.generated_at !== 'string' || !Number.isFinite(Date.parse(value.generated_at))) throw Error('The ledger is missing its update time.');
  for (const session of value.sessions) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(session.session_day) || !['active', 'complete', 'incomplete', 'scheduled', 'stopping'].includes(session.status)) throw Error('Invalid session record.');
    if (!Array.isArray(session.events) || session.events.length > 10000 || !Array.isArray(session.intents) || !session.positions || Array.isArray(session.positions) || !session.quotes || !session.totals) throw Error('Incomplete session record.');
    if (!Number.isFinite(session.starting_cash_gbp) || session.starting_cash_gbp <= 0 || !Number.isInteger(session.buy_fills) || session.buy_fills < 0) throw Error('Invalid session accounting.');
    for (const [symbol, p] of Object.entries(session.positions)) {
      if (!['ISF.L', 'VUSA.L', 'EQQQ.L'].includes(symbol) || !p || !Number.isFinite(p.quantity) || p.quantity <= 0 || !Number.isFinite(p.mark_gbp) || p.mark_gbp <= 0 || !Number.isFinite(Date.parse(p.mark_bar_end))) throw Error('Invalid holding record.');
    }
    for (const intent of session.intents) if (!intent || typeof intent.intent_id !== 'string' || typeof intent.symbol !== 'string' || !['buy', 'sell'].includes(intent.side) || typeof intent.status !== 'string' || typeof intent.reason !== 'string') throw Error('Invalid intention record.');
    for (const quote of Object.values(session.quotes)) if (!quote || typeof quote.status !== 'string' || (quote.error !== undefined && typeof quote.error !== 'string')) throw Error('Invalid quote status.');
    const t = session.totals;
    for (const key of ['cash_gbp', 'holdings_gbp', 'equity_gbp', 'realised_gbp', 'unrealised_gbp', 'total_pl_gbp']) if (!Number.isFinite(t[key])) throw Error('Invalid portfolio totals.');
    if (Math.abs(t.cash_gbp + t.holdings_gbp - t.equity_gbp) > 1e-6 || Math.abs(t.realised_gbp + t.unrealised_gbp - t.total_pl_gbp) > 1e-6 || Math.abs(t.equity_gbp - session.starting_cash_gbp - t.total_pl_gbp) > 1e-6) throw Error('Portfolio totals do not reconcile.');
    for (const e of session.events.filter(e => e.type === 'fill')) {
      if (!['buy', 'sell'].includes(e.side) || !['ISF.L', 'VUSA.L', 'EQQQ.L'].includes(e.symbol) || !Number.isFinite(e.quantity) || e.quantity <= 0 || !Number.isFinite(e.execution_price_gbp) || e.execution_price_gbp <= 0) throw Error('Invalid simulated fill.');
      const decision = Date.parse(e.decision_at), fill = Date.parse(e.effective_fill_at), recognition = Date.parse(e.recognised_at);
      if (![decision, fill, recognition].every(Number.isFinite) || fill < decision || recognition < fill + 300000) throw Error('Invalid fill chronology.');
    }
  }
  return value;
}

export async function readCloudLedger(fetcher = fetch) {
  const response = await fetcher(ledgerURL, { redirect: 'manual', cache: 'no-store', signal: AbortSignal.timeout(15000), headers: { Accept: 'application/json' } });
  if (!response.ok) throw Error(response.status === 404 ? 'The cloud ledger has not been published yet.' : 'The cloud ledger could not be reached.');
  return validateDashboard(await boundedJSON(response, 4_000_000));
}
