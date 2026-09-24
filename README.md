# Trading agent

An autonomous, multi-strategy day-trading agent. It runs **33 well-known strategies** at the same time (plus the optional Kronos AI forecaster) on US stocks, leveraged/inverse ETFs and crypto. Each strategy trades its own separate **£100 paper account**, so you can see which ones actually make money.

On top of the strategies sits the **Agent**: a walk-forward selector. Every day it trades whichever strategy/symbol pairs made the best risk-adjusted returns over the previous 10 days. That is how it "gets better": it keeps moving money toward what is working and away from what isn't.

> **Reality check.** Nothing here guarantees profit. Most day-trading strategies lose money once costs are counted, and a strategy that worked last week often stops working. The leaderboard shows this honestly, costs included. Run it on paper first and only consider real money after weeks of paper results that beat simply holding SPY/BTC.

## What trades

| Group | Sleeves |
|---|---|
| Trend | EMA 9/21, EMA 20/50, Triple EMA, MACD cross, MACD zero-line, Supertrend, Parabolic SAR, ADX/DI, Ichimoku, Heikin-Ashi, Trend pullback |
| Momentum | VWAP momentum (the old GPT rule), ROC + volume, RSI momentum, OBV trend, Gap-and-go |
| Breakout | Donchian 20/10 and 55/20, Opening range 15m/30m, Bollinger, Keltner, Squeeze, Volume breakout |
| Mean reversion | RSI(14), Connors RSI(2), Bollinger, Z-score, VWAP, Stochastic, Williams %R, CCI, MFI |
| AI model | Kronos forecast (optional, [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)) |
| Meta | **Agent** (top 5 pairs), **Agent (aggressive)** (top 2, concentrated), **Consensus** (majority vote) |
| Benchmarks | Hold SPY, Hold BTC |

- **Universe:** 21 symbols by default: SPY, QQQ, IWM, TQQQ, SQQQ, SOXL, NVDA, TSLA, AAPL, MSFT, AMD, META, AMZN, GOOGL, PLTR, COIN, plus BTC, ETH, SOL, XRP and DOGE. Crypto trades 24/7, so the agent is never idle.
- **Data:** 5-minute bars from Yahoo Finance, with Coinbase as a fallback for crypto.
- **Execution:** a signal on a bar's close is executed on the next tick.

**Risk rules** (per sleeve):
- Long only, at most 4 positions of 25% each.
- ATR stop-losses and trailing stops.
- Stocks are sold 10 minutes before the US close, so nothing is held overnight.
- A −6% day pauses the sleeve until the next day.
- A −50% drawdown shuts the sleeve down for good.
- Costs are modelled on every trade: 5 bps per side for stocks, 30 bps per side for crypto.

## Start it (no computer needed)

1. Merge this branch into `main`. The **Trading agent** workflow then runs every 30 minutes and trades for 29 minutes each run, so it runs non-stop in paper mode.
2. To start immediately, go to **Actions → Trading agent → Run workflow**.
3. Watch results at **`https://github.com/ayushganatra3-del/trader/tree/agent-state`**. Its README is the live leaderboard. `dashboard.html` has charts and `trades.jsonl` lists every trade.

The first run downloads 60 days of history, so the backtest leaderboard and today's picks appear straight away. The paper results then build up from that moment on.

Notes:
- This repository is **public**, so the paper ledger is public too.
- GitHub's scheduler can run late.
- GitHub's terms are aimed at CI use. For a heavy 24/7 bot, a cheap VPS or a home PC is the sturdier option (below).

## Run it on your own machine

```sh
pip install -r requirements.txt
python -m agent backtest              # 60-day backtest of every strategy, printed as a leaderboard
python -m agent backtest --out reports  # ...and write README/dashboard.html to ./reports
python -m agent doctor                # check data (and broker) connectivity
python -m agent run                   # trade forever (Ctrl+C to stop); ledger in ./state
python -m agent run --minutes 60      # or for a fixed time
```

No internet? `python -m agent backtest --synthetic` runs on generated data.

## Going live with real money (only when paper results justify it)

The agent can copy the **Agent** sleeve into an [Alpaca](https://alpaca.markets) account. Alpaca offers commission-free US stocks, fractional shares from $1, crypto, and a free paper-trading account. Check it accepts UK residents before signing up.

1. Create Alpaca API keys. Start with the *paper* account.
2. In GitHub, go to **Settings → Secrets and variables → Actions**:
   - Add the secrets `APCA_API_KEY_ID` and `APCA_API_SECRET_KEY`.
   - Set the variable `AGENT_MODE` to `alpaca-paper`.
3. When you want real money:
   - Use your **live** keys.
   - Set `AGENT_MODE=alpaca-live`.
   - Add the secret `AGENT_LIVE_CONFIRM` = `I-ACCEPT-REAL-MONEY-RISK`.

   Without that exact phrase the agent refuses to trade real money.

Safety rails in live mode:
- It never deploys more than `broker.capital_gbp` (£100), however much the account holds.
- It never uses margin.
- It only trades stocks while the market is open.
- It skips new stock buys when the US **pattern-day-trader** rule would block them (under $25k equity, 3 day trades in 5 days).
- It will not submit the same order twice.

Crypto is not subject to the PDT rule.

## Kronos AI forecaster (optional)

```sh
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-kronos.txt
AGENT_KRONOS=1 python -m agent run
```

In GitHub Actions, set the variable `AGENT_KRONOS=true`.

It forecasts the next hour of each symbol with `Kronos-small`, which takes about 6 seconds per symbol on a CPU. It goes long when the forecast return is above +0.4%. Its results only build up going forward, because running it over 60 days of history would be too slow. The Agent starts picking it once it has a 10-day record.

## Configuration

Copy `config.example.toml` to `config.toml`. You can change:
- the symbols, costs and risk limits
- the Agent's look-back and number of picks
- which strategies are switched off

## Code map

| Path | What |
|---|---|
| `agent/strategies/library.py` | all strategy rules, a few lines each |
| `agent/indicators.py` | causal indicators (EMA, RSI, ATR, MACD, VWAP, Supertrend, ...) |
| `agent/research.py` | vectorised backtest, position/stop engine, walk-forward Agent selection |
| `agent/portfolio.py` | paper accounting with costs, daily-loss and kill switches |
| `agent/engine.py` | the tick loop: data → signals → trades → broker → reports |
| `agent/live.py`, `agent/brokers/alpaca.py` | Alpaca sync with safety rails |
| `agent/kronos/` | Kronos model (vendored, MIT) and forecaster |
| `tests/` | look-ahead checks, random-walk "no fake edge" check, paper-vs-backtest parity, accounting, broker safety |

Run the tests: `pip install -r requirements-dev.txt && python -m pytest tests -q`

## Legacy

The earlier GPT-built system still lives in `cloud/` (a virtual ETF journal trading 3 London ETFs), `trading-lab/` (research website) and the `trading-state` branch. It is untouched and independent: see [docs/virtual-etf-monitor.md](docs/virtual-etf-monitor.md).
