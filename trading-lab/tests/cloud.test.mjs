import test from 'node:test';
import assert from 'node:assert/strict';
import { validateExperiment } from '../lib/experiments.mjs';
import { demoBars, defaultConfig, backtest } from '../lib/engine.mjs';
import { boundedJSON } from '../lib/bounded-json.mjs';
import { validateDashboard, readCloudLedger, ledgerURL } from '../lib/cloud-ledger.mjs';

const sample = () => ({ id: 'test-12345678901234567890', data: 'Test synthetic prices', phase: 'research', rule: 'trend', config: defaultConfig, currency: 'GBP', bars: demoBars(), synthetic: true, equity: 999999 });
test('cloud save recalculates claimed performance and keeps the input prices', () => {
  const v = sample(), saved = validateExperiment(v);
  assert.equal(saved.summary.equity, backtest(v.bars, v.rule, v.config, v.phase).finalEquity);
  assert.notEqual(saved.summary.equity, v.equity);
  assert.equal(saved.payload.bars.length, v.bars.length);
  assert.equal(saved.summary.hasData, true);
});
test('cloud save rejects ambiguous currency, malformed prices and unknown strategy', () => {
  assert.throws(() => validateExperiment({ ...sample(), currency: 'USD' }), /currency/);
  assert.throws(() => validateExperiment({ ...sample(), bars: [{ date: '2026-01-01', close: -1 }] }));
  assert.throws(() => validateExperiment({ ...sample(), rule: 'unproven' }), /Unknown/);
});
test('extra configuration fields cannot turn summary reads into unbounded payload reads', () => {
  const v = sample(); v.config = { ...v.config, extra: 'x'.repeat(500000) };
  const result = validateExperiment(v);
  assert.equal(result.summary.config.extra, undefined);
  assert.ok(JSON.stringify(result.summary).length < 1000);
});
test('legacy migration is explicitly a summary with no invented price history', () => {
  const { bars, ...v } = sample();
  assert.throws(() => validateExperiment(v), /Include the prices/);
  const old = validateExperiment({ ...v, legacy: true, at: '2026-09-10T12:00:00Z' });
  assert.equal(old.summary.hasData, false);
  assert.equal(old.payload.bars, null);
  assert.equal(old.summary.at, '2026-09-10T12:00:00.000Z');
});
test('bounded JSON refuses a streaming oversized body even without content-length', async () => {
  await assert.rejects(boundedJSON(new Response(JSON.stringify({ big: 'x'.repeat(100) })), 20), /limit/);
  assert.deepEqual(await boundedJSON(new Response('{"ok":true}'), 20), { ok: true });
});
const dashboard = () => ({ version: 1, generated_at: '2026-09-10T16:02:35Z', control: { active_session: null }, sessions: [{ session_day: '2026-09-10', status: 'incomplete', starting_cash_gbp: 100, buy_fills: 1, positions: {}, intents: [], quotes: {}, events: [], totals: { cash_gbp: 60, holdings_gbp: 39, equity_gbp: 99, realised_gbp: -0.5, unrealised_gbp: -0.5, total_pl_gbp: -1 } }] });
test('ledger rejects missing intentions and malformed holdings before rendering', () => {
  const missing = dashboard(); delete missing.sessions[0].intents;
  assert.throws(() => validateDashboard(missing), /Incomplete/);
  const bad = dashboard(); bad.sessions[0].positions['EQQQ.L'] = { quantity: 'unknown', mark_gbp: 100 };
  assert.throws(() => validateDashboard(bad), /holding/);
});
test('ledger fails closed on unreconciled or missing portfolio values', () => {
  assert.equal(validateDashboard(dashboard()).sessions[0].status, 'incomplete');
  const bad = dashboard(); bad.sessions[0].totals.equity_gbp = 100;
  assert.throws(() => validateDashboard(bad), /reconcile/);
  assert.throws(() => validateDashboard({ version: 1 }), /format/);
});
test('ledger rejects a hypothetical fill before its recorded decision', () => {
  const bad = dashboard(); bad.sessions[0].events.push({ type: 'fill', symbol: 'VUSA.L', side: 'buy', quantity: 1, execution_price_gbp: 100, decision_at: '2026-09-10T11:02:00Z', effective_fill_at: '2026-09-10T11:00:00Z', recognised_at: '2026-09-10T11:20:00Z' });
  assert.throws(() => validateDashboard(bad), /chronology/);
});
test('ledger fetch stays on the fixed public data URL and rejects unavailable source', async () => {
  let url, options;
  const result = await readCloudLedger(async (u, o) => { url = u; options = o; return Response.json(dashboard()); });
  assert.equal(url, ledgerURL); assert.equal(options.redirect, 'manual'); assert.equal(result.version, 1);
  await assert.rejects(readCloudLedger(async () => new Response('', { status: 404 })), /not been published/);
  await assert.rejects(readCloudLedger(async () => new Response('', { status: 302, headers: { Location: 'https://unrelated.example' } })), /could not be reached/);
});
