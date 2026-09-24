import { backtest, validateBars, validateConfig, strategies } from './engine.mjs';

export function validateExperiment(value, now = new Date().toISOString()) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw Error('Invalid experiment.');
  const { id, data, phase, rule } = value;
  if (typeof id !== 'string' || !/^[a-zA-Z0-9-]{16,80}$/.test(id)) throw Error('Invalid experiment identifier.');
  if (typeof data !== 'string' || !data.trim() || data.length > 240) throw Error('Give the dataset a name of at most 240 characters.');
  if (!['research', 'holdout'].includes(phase) || !strategies.some(s => s.id === rule)) throw Error('Unknown evaluation or strategy.');
  if (!value.config || typeof value.config !== 'object') throw Error('Experiment settings are required.');
  const config = validateConfig(Object.fromEntries(['capital', 'allocation', 'costBps', 'fee', 'drawdownStop', 'split', 'currency'].map(key => [key, value.config[key]])));
  if (value.currency !== config.currency) throw Error('Price currency must match the experiment settings.');
  let bars = null, result = null;
  if (value.bars != null) {
    validateBars(value.bars);
    bars = value.bars.map(b => ({ date: b.date, open: b.open, high: b.high, low: b.low, close: b.close }));
    result = backtest(bars, rule, config, phase);
  } else if (!value.legacy) {
    throw Error('Include the prices to save a complete experiment.');
  }
  const equity = result ? result.finalEquity : value.equity;
  if (!Number.isFinite(equity) || equity < 0 || equity > 1e15) throw Error('Invalid final value.');
  const at = value.legacy && typeof value.at === 'string' && Number.isFinite(Date.parse(value.at)) ? new Date(value.at).toISOString() : now;
  const summary = { id, at, data: data.trim(), phase, rule, equity, currency: config.currency, config, hasData: !!bars, synthetic: value.synthetic === true };
  return { summary, payload: { ...summary, bars, result } };
}
