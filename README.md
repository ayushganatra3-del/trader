# Trading agent

An autonomous, multi-strategy trading agent. It runs **63 strategies** at the same time: 33 well-known intraday rules on 5-minute bars, 30 hourly "swing" versions of them, and daily market-timing and swing sleeves (plus the optional Kronos AI forecaster) on US stocks, leveraged/inverse ETFs and crypto. Each strategy trades its own separate **£100 paper account**, so you can see which ones actually make money.

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
| Meta | **Agent** (top 5 strategy/symbol pairs), **Agent (aggressive)** (top 2, concentrated), **Agent (rotation)** (copies the top 3 whole strategies by 20-day risk-adjusted return), **Consensus** (majority vote) |
| Benchmarks | Hold SPY, Hold BTC |
| Copy trading | **Famous investors' 13F holdings** (Buffett, Burry, Ackman, Druckenmiller, Tepper, Cathie Wood), **company insiders' big purchases**, the **top AI agents on AI-Trader**, and a fund that copies **Congress** (NANC: Democrats, including Pelosi), hedge-fund gurus (GURU), ARKK and Berkshire (BRK-B). See below. |
| Hourly swing | Every rule above except opening-range and gap-and-go, re-run on 1-hour bars (named "… · 1h"). They trade far less, so costs eat less, and they may hold stocks overnight. |
| Daily | **Nasdaq market timing** on TQQQ and QQQ (distribution days and follow-through days, the IBD method), **momentum burst** and **exhaustion hammer** (Stockbee setups), and the **bullish score** (top-scoring trend names). They use 2 years of daily bars and hold for days. See below. |

- **Universe:** 21 symbols by default: SPY, QQQ, IWM, TQQQ, SQQQ, SOXL, NVDA, TSLA, AAPL, MSFT, AMD, META, AMZN, GOOGL, PLTR, COIN, plus BTC, ETH, SOL, XRP and DOGE. Crypto trades 24/7, so the agent is never idle.
- **Data:** 5-minute bars. Stocks come from Yahoo Finance via `yfinance`; crypto comes from Coinbase. If a source rate-limits the agent, it is skipped for 10 minutes and the next one is used.
- **Execution:** a signal on a bar's close is executed on the next tick.

**Risk rules** (per sleeve):
- Long only, at most 4 positions of 25% each.
- ATR stop-losses and trailing stops.
- Intraday sleeves sell stocks 10 minutes before the US close, so they hold nothing overnight. Hourly swing sleeves may hold overnight.
- A −6% day pauses the sleeve until the next day.
- A −50% drawdown shuts the sleeve down for good.
- The sleeve a real broker account copies gets extra brakes: −5% in a week or −8% in a month pauses it until the next week/month, and 2 losing trades in a row stop new buys for 24 hours. The broker mirrors what that paper sleeve actually holds, so every pause applies to real money too.
- Costs are modelled on every trade: 5 bps per side for stocks, 30 bps per side for crypto.

## Copy trading

Each copy source is its own £100 paper sleeve, so you can see whether copying actually pays:

| Sleeve | What it copies | How out of date |
|---|---|---|
| `Copy: <manager> 13F` | Top 10 long stock holdings in the manager's latest SEC 13F filing (EDGAR), weighted by size | Filed up to 45 days after each quarter ends, so the positions can be months old |
| `Copy: Insider buying` | The 8 stocks where company officers and directors bought the most on the open market (at least $250k) in the last 10 days (SEC Form 4 via OpenInsider) | Filed within 2 business days of the trade |
| `Copy: AI-Trader top agents` | The long stock and crypto positions of the most profitable AI trading agents on [AI-Trader](https://github.com/HKUDS/AI-Trader) (ai4trade.ai public leaderboard), blended equally | Live, but AI-Trader publishes no history, so this sleeve's record starts the day it is switched on |
| `Copy: Congress Democrats (NANC)` | ETF that copies stock trades disclosed by Democratic members of Congress (its Republican twin, KRUZ, has closed) | Congress has up to 45 days to disclose |
| `Copy: Hedge-fund gurus (GURU)`, `Cathie Wood (ARKK)`, `Warren Buffett (BRK-B)` | Buy-and-hold the fund or company itself | None: these trade live |

Every copied position is bought only at the first market open **after** it was made public, including in backtests. You can't copy anyone's trade at the price they got. Research on whether copying beats the market is mixed. The leaderboard shows the honest result, with costs. Managers can be changed under `[copy]` in `config.toml`. A manager whose latest 13F is over 200 days old (for example because the fund closed) is shown but not traded.

The SEC asks automated tools to identify themselves. If EDGAR refuses requests, set the repository variable `SEC_USER_AGENT` to something like `your-name your@email.com`.

## Daily sleeves and the market regime

These trade on completed daily bars, and each signal is acted on at the next US open:

| Sleeve | Rule |
|---|---|
| `Timing: Nasdaq FTD · TQQQ` / `· QQQ` | Counts **distribution days** (QQQ down ≥0.2% on higher volume) in the last 25 sessions. It holds 100% with 0–2 of them, 75% with 3–4, 50% with 5 and 25% with 6 or more. After a correction (−10% from the high, or 5+ distribution days below the 50-day average) it holds nothing until a **follow-through day** (day 4–10 of a rally attempt, +1.25% on higher volume). It also holds nothing while ^VXN (Nasdaq volatility) is 35 or higher. |
| `Daily: Momentum burst` | +4% day on higher volume, closing near the high. Holds up to 4 days, or exits if the trigger day's low breaks. |
| `Daily: Exhaustion hammer` | Long-lower-wick reversal that undercuts recent lows during a 5–25% pullback in an uptrend. Holds up to 5 days. |
| `Daily: Bullish score` | Scores trend and momentum (SMA 20/50, RSI, MACD, EMA 9/21, ADX, 3-month return). Holds the top 4 names scoring 6 or more. |

The leaderboard and dashboard show the current **market regime**: uptrend or correction, distribution-day count, timing exposure, VXN, VIX and the latest follow-through day. The rules are adapted from [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) and [staskh/trading_skills](https://github.com/staskh/trading_skills).

## Start it (no computer needed)

1. Once the code is on `main`, the **Trading agent** workflow trades in 29-minute runs, back to back, in paper mode.
2. To start immediately, go to **Actions → Trading agent → Run workflow**. Each run starts the next one when it finishes, and a schedule at :07 and :37 past each hour restarts the chain if it ever breaks.
3. To stop it, set the repository variable `AGENT_ENABLED` to `false` (**Settings → Secrets and variables → Actions → Variables**), or disable the workflow in Actions.
4. Watch results at **`https://github.com/ayushganatra3-del/trader/tree/agent-state`**. Its README is the live leaderboard. `dashboard.html` has charts and `trades.jsonl` lists every trade.

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
| `agent/copytrade.py` | copy trading: SEC 13F holdings, insider purchases, disclosure-time schedules |
| `agent/daily.py` | daily bars, market regime (distribution/follow-through days), daily swing setups |
| `tests/` | look-ahead checks, random-walk "no fake edge" check, paper-vs-backtest parity, accounting, broker safety |

Run the tests: `pip install -r requirements-dev.txt && python -m pytest tests -q`

## Legacy

The earlier GPT-built system still lives in `cloud/` (a virtual ETF journal trading 3 London ETFs), `trading-lab/` (research website) and the `trading-state` branch. It is untouched and independent: see [docs/virtual-etf-monitor.md](docs/virtual-etf-monitor.md).
