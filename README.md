# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-02T15:36:05.000156+00:00 · 9013 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.24 (-0.76%)

Closed trades 32, win rate 65.6%, fees £0.92, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, ETRA 12%, BBD 12%, BPRE 12%, GME 12%, NYAX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-01)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.51 · VIX 16.39 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.6, PLTR 8.5, META 7.7, AMD 7.5, TECL 7.1, BITX 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 17748 decisions in 2187 calls, $0.2297 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-02T15:36 | 2 / 23 / 5 | TSLA 14% |  |
| Breezy | 2026-10-02T15:36 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-02T15:36 | 1 / 27 / 2 | MSTR 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| Bollinger reversion · 1h | UPRO | 2.12 | +4.42% | 3 |
| Connors RSI(2) · 1h | TQQQ | 2.12 | +4.58% | 4 |
| Z-score reversion | MSFT | 2.05 | +2.32% | 5 |
| Stochastic reversion · 1h | SPY | 2.03 | +1.53% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.51 | 2.51 | 0 | — | 3.35 | 0.98 | -7.93 | 7 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.22 | 2.22 | 0 | — | -6.94 | -1.25 | -15.27 | 2 |
| 3 | Hold BTC | benchmark | 102.03 | 2.03 | 0 | — | 35.33 | 4.29 | -8.68 | 1 |
| 4 | Daily: Bullish score | daily | 100.86 | 0.86 | 3 | 0.0 | 3.22 | 0.64 | -12.76 | 14 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 100.83 | 0.83 | 0 | — | -1.90 | -1.06 | -5.09 | 2 |
| 6 | Copy: Congress Democrats (NANC) | copy | 100.47 | 0.47 | 0 | — | 3.81 | 1.74 | -3.62 | 1 |
| 7 | Candlestick reversal · 1h | reversion | 100.36 | 0.35 | 53 | 37.7 | -23.34 | -5.36 | -26.02 | 491 |
| 8 | RSI(14) reversion · 1h | reversion | 100.19 | 0.19 | 10 | 60.0 | 4.57 | 1.33 | -6.57 | 117 |
| 9 | Donchian 55/20 · 1h | breakout | 100.04 | 0.04 | 17 | 0.0 | 7.17 | 1.11 | -16.96 | 115 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.97 | -0.03 | 15 | 33.3 | 4.03 | 2.00 | -1.46 | 86 |
| 13 | Hold SPY | benchmark | 99.96 | -0.04 | 0 | — | 1.85 | 1.10 | -3.66 | 1 |
| 14 | Stochastic reversion · 1h | reversion | 99.93 | -0.07 | 39 | 61.5 | -7.86 | -1.63 | -9.86 | 328 |
| 15 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 24 | 33.3 | -11.06 | -3.75 | -14.05 | 111 |
| 16 | Z-score reversion · 1h | reversion | 99.90 | -0.10 | 17 | 58.8 | 5.69 | 1.30 | -8.60 | 156 |
| 17 | Bollinger reversion · 1h | reversion | 99.81 | -0.19 | 38 | 44.7 | -15.04 | -4.02 | -17.68 | 303 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 99.43 | -0.57 | 0 | — | -2.40 | -0.93 | -7.65 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.33 | -0.67 | 2 | 50.0 | -0.42 | -0.49 | -1.70 | 18 |
| 20 | Agent | meta | 99.24 | -0.76 | 32 | 65.6 | -9.45 | -5.95 | -11.27 | 222 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Trend pullback · 1h | trend | 99.05 | -0.95 | 44 | 20.5 | -22.91 | -5.79 | -25.84 | 162 |
| 23 | Copy: Hedge-fund gurus (GURU) | copy | 99.02 | -0.98 | 0 | — | -2.59 | -1.22 | -5.14 | 1 |
| 24 | EMA 20/50 cross · 1h | trend | 98.91 | -1.09 | 23 | 8.7 | 15.16 | 1.86 | -14.40 | 129 |
| 25 | CCI reversion · 1h | reversion | 98.87 | -1.13 | 63 | 49.2 | 1.87 | 0.47 | -12.41 | 413 |
| 26 | Connors RSI(2) · 1h | reversion | 98.82 | -1.18 | 53 | 49.1 | -11.69 | -3.98 | -13.59 | 224 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.77 | -1.23 | 0 | — | 23.22 | 3.46 | -6.29 | 1 |
| 28 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 29 | Williams %R · 1h | reversion | 98.49 | -1.51 | 69 | 55.1 | -16.07 | -2.93 | -19.41 | 495 |
| 30 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.35 | -2.67 | -3.95 | 26 |
| 31 | Agent (aggressive) | meta | 98.22 | -1.78 | 14 | 50.0 | -0.97 | -0.47 | -4.23 | 104 |
| 32 | Agent (rotation) | meta | 97.93 | -2.07 | 48 | 18.8 | -3.54 | -1.33 | -8.90 | 227 |
| 33 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 34 | Max aggression: 1-day momentum | meta | 97.55 | -2.45 | 5 | 40.0 | -22.16 | -1.07 | -41.28 | 43 |
| 35 | Agent (ML meta-label) | meta | 97.48 | -2.52 | 200 | 17.5 | 3.46 | 0.76 | -11.47 | 365 |
| 36 | Daily: SMA 20/50 cross · AAPL | daily | 97.24 | -2.76 | 0 | — | -0.21 | 0.02 | -5.18 | 1 |
| 37 | Daily: Momentum burst | daily | 97.03 | -2.98 | 3 | 0.0 | -1.00 | 0.03 | -16.40 | 46 |
| 38 | Parabolic SAR · 1h | trend | 96.92 | -3.08 | 45 | 15.6 | -7.34 | -0.87 | -19.70 | 312 |
| 39 | Supertrend · 1h | trend | 96.71 | -3.29 | 23 | 4.3 | 2.91 | 0.58 | -16.43 | 203 |
| 40 | MFI reversion · 1h | reversion | 96.64 | -3.36 | 68 | 29.4 | -6.00 | -0.97 | -16.99 | 121 |
| 41 | ADX DI cross · 1h | trend | 96.63 | -3.37 | 41 | 12.2 | -4.50 | -0.59 | -13.84 | 269 |
| 42 | Gap and go | momentum | 96.30 | -3.70 | 33 | 6.1 | 11.98 | 2.91 | -4.73 | 199 |
| 43 | MACD cross · 1h | trend | 96.06 | -3.94 | 66 | 13.6 | -14.94 | -2.37 | -17.97 | 485 |
| 44 | Squeeze breakout · 1h | breakout | 95.70 | -4.30 | 22 | 18.2 | 20.72 | 2.97 | -8.06 | 113 |
| 45 | Copy: Insider buying | copy | 95.23 | -4.77 | 4 | 50.0 | -18.90 | -3.74 | -20.40 | 71 |
| 46 | Opening range 30m | breakout | 95.20 | -4.80 | 68 | 17.6 | -13.86 | -4.13 | -16.12 | 565 |
| 47 | Ichimoku · 1h | trend | 95.19 | -4.81 | 26 | 11.5 | 6.63 | 0.95 | -16.19 | 129 |
| 48 | RSI momentum · 1h | momentum | 94.76 | -5.24 | 35 | 2.9 | 2.10 | 0.48 | -16.65 | 228 |
| 49 | Triple EMA stack · 1h | trend | 93.95 | -6.05 | 46 | 6.5 | -7.43 | -0.70 | -23.88 | 241 |
| 50 | Opening range 15m | breakout | 93.92 | -6.08 | 82 | 17.1 | -15.34 | -4.39 | -18.04 | 691 |
| 51 | VWAP momentum · 1h | momentum | 93.86 | -6.14 | 169 | 23.1 | -40.47 | -6.33 | -42.55 | 1277 |
| 52 | Bollinger breakout · 1h | breakout | 93.43 | -6.57 | 34 | 17.6 | 5.84 | 0.94 | -12.06 | 293 |
| 53 | Three white soldiers | momentum | 92.82 | -7.18 | 64 | 17.2 | -49.52 | -26.65 | -49.52 | 598 |
| 54 | Volume breakout · 1h | breakout | 92.77 | -7.23 | 30 | 6.7 | 3.22 | 0.63 | -12.60 | 129 |
| 55 | Max aggression: 5-day momentum | meta | 92.65 | -7.35 | 5 | 40.0 | -20.14 | -1.75 | -29.56 | 30 |
| 56 | EMA 9/21 cross · 1h | trend | 92.48 | -7.53 | 63 | 11.1 | -4.44 | -0.41 | -18.47 | 343 |
| 57 | Heikin-Ashi · 1h | trend | 91.80 | -8.21 | 75 | 20.0 | -32.27 | -5.66 | -33.58 | 687 |
| 58 | MACD zero-line · 1h | trend | 91.45 | -8.55 | 34 | 5.9 | -4.65 | -0.40 | -18.32 | 237 |
| 59 | Donchian 20/10 · 1h | breakout | 91.01 | -8.99 | 28 | 10.7 | -0.59 | 0.14 | -16.18 | 222 |
| 60 | OBV trend · 1h | momentum | 90.13 | -9.87 | 90 | 11.1 | -14.15 | -1.59 | -26.61 | 337 |
| 61 | RSI(14) reversion | reversion | 89.32 | -10.68 | 164 | 36.6 | -72.54 | -21.13 | -72.69 | 1466 |
| 62 | Keltner breakout · 1h | breakout | 88.58 | -11.42 | 21 | 0.0 | -11.84 | -1.42 | -23.03 | 216 |
| 63 | ROC + volume · 1h | momentum | 87.63 | -12.37 | 80 | 13.8 | -13.39 | -1.74 | -24.25 | 423 |
| 64 | Squeeze breakout | breakout | 83.18 | -16.82 | 169 | 16.0 | -60.24 | -18.25 | -60.82 | 1204 |
| 65 | Donchian 55/20 | breakout | 82.47 | -17.53 | 168 | 18.5 | -68.09 | -15.27 | -68.36 | 1309 |
| 66 | VWAP reversion | reversion | 81.19 | -18.81 | 180 | 28.3 | -70.97 | -17.22 | -70.97 | 1385 |
| 67 | EMA 20/50 cross | trend | 80.25 | -19.75 | 189 | 19.0 | -78.83 | -16.70 | -79.22 | 1483 |
| 68 | Volume breakout | breakout | 80.20 | -19.80 | 155 | 14.2 | -64.04 | -20.04 | -64.11 | 919 |
| 69 | ROC + volume | momentum | 79.98 | -20.02 | 256 | 20.3 | -73.56 | -17.86 | -73.82 | 1680 |
| 70 | AI bee: Bizzy | ai | 79.47 | -20.53 | 368 | 11.1 | — | — | — | — |
| 71 | AI bee: Boozy | ai | 79.05 | -20.95 | 131 | 3.8 | — | — | — | — |
| 72 | Z-score reversion | reversion | 79.05 | -20.95 | 260 | 31.9 | -85.56 | -26.59 | -85.56 | 2103 |
| 73 | MFI reversion | reversion | 77.47 | -22.53 | 242 | 21.9 | -88.21 | -33.25 | -88.27 | 2136 |
| 74 | Ichimoku | trend | 76.27 | -23.73 | 199 | 9.5 | -81.40 | -25.51 | -81.54 | 1762 |
| 75 | Keltner breakout | breakout | 76.27 | -23.73 | 242 | 13.6 | -85.31 | -32.37 | -85.33 | 1905 |
| 76 | Supertrend | trend | 75.25 | -24.75 | 263 | 20.5 | -87.28 | -23.43 | -87.45 | 1952 |
| 77 | Donchian 20/10 | breakout | 72.96 | -27.04 | 330 | 19.1 | -90.72 | -27.77 | -90.79 | 2677 |
| 78 | ADX DI cross | trend | 72.15 | -27.85 | 290 | 9.3 | -89.74 | -41.71 | -89.74 | 2120 |
| 79 | MACD zero-line | trend | 72.07 | -27.93 | 320 | 16.9 | -91.69 | -32.43 | -91.69 | 2361 |
| 80 | Trend pullback | trend | 71.64 | -28.36 | 291 | 17.9 | -91.60 | -33.44 | -91.60 | 2327 |
| 81 | Triple EMA stack | trend | 71.63 | -28.37 | 331 | 17.5 | -93.13 | -33.61 | -93.18 | 2616 |
| 82 | RSI momentum | momentum | 71.02 | -28.98 | 313 | 16.0 | -90.51 | -27.61 | -90.59 | 2396 |
| 83 | Bollinger breakout | breakout | 70.22 | -29.78 | 336 | 16.4 | -93.94 | -38.33 | -93.94 | 2852 |
| 84 | Stochastic reversion | reversion | 68.71 | -31.29 | 469 | 24.5 | -95.86 | -42.48 | -95.87 | 4053 |
| 85 | Consensus | meta | 67.47 | -32.53 | 308 | 9.4 | -94.73 | -29.19 | -94.73 | 2659 |
| 86 | Bollinger reversion | reversion | 67.15 | -32.85 | 455 | 17.1 | -95.96 | -41.57 | -95.96 | 3713 |
| 87 | Connors RSI(2) ⏸ | reversion | 66.29 | -33.71 | 420 | 19.3 | -96.70 | -39.46 | -96.71 | 3648 |
| 88 | EMA 9/21 cross | trend | 66.16 | -33.84 | 432 | 18.5 | -97.37 | -37.21 | -97.40 | 3542 |
| 89 | Candlestick reversal | reversion | 65.24 | -34.76 | 492 | 17.1 | -99.34 | -44.38 | -99.34 | 5609 |
| 90 | OBV trend | momentum | 64.63 | -35.37 | 468 | 16.2 | -96.14 | -43.07 | -96.15 | 3586 |
| 91 | CCI reversion | reversion | 64.45 | -35.55 | 418 | 17.2 | -98.51 | -44.95 | -98.51 | 4702 |
| 92 | VWAP momentum | momentum | 62.82 | -37.18 | 515 | 9.3 | -98.61 | -33.64 | -98.61 | 5314 |
| 93 | Parabolic SAR | trend | 61.88 | -38.12 | 446 | 14.3 | -97.16 | -48.46 | -97.16 | 3649 |
| 94 | MACD cross | trend | 60.40 | -39.60 | 521 | 15.2 | -99.71 | -52.38 | -99.71 | 6111 |
| 95 | Williams %R ⏸ | reversion | 59.36 | -40.64 | 582 | 23.0 | -99.53 | -51.18 | -99.53 | 6122 |
| 96 | Heikin-Ashi ⏸ | trend | 58.33 | -41.67 | 502 | 10.0 | -99.90 | -63.14 | -99.90 | 8305 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-02T15:36 | Consensus | buy | SOXL | 16.87 | — | entry |
| 2026-10-02T15:36 | Consensus | buy | NVDA | 16.87 | — | entry |
| 2026-10-02T15:36 | MFI reversion | sell | LABU | 19.35 | -0.03 | target is flat |
| 2026-10-02T15:36 | CCI reversion | buy | UPRO | 3.53 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | TNA | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | TECL | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | SPY | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | SOXL | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | SOL-USD | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | META | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | IWM | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | ETHU | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | ETH-USD | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | DOGE-USD | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | buy | COIN | 3.59 | — | entry signal |
| 2026-10-02T15:36 | CCI reversion | sell | XRP-USD | 7.09 | -0.06 | rebalance down |
| 2026-10-02T15:36 | CCI reversion | sell | MSTR | 7.17 | -0.01 | rebalance down |
| 2026-10-02T15:36 | CCI reversion | sell | MSFT | 7.19 | -0.00 | rebalance down |
| 2026-10-02T15:36 | CCI reversion | sell | BTC-USD | 7.17 | -0.06 | rebalance down |
| 2026-10-02T15:36 | CCI reversion | sell | BITX | 7.18 | -0.03 | rebalance down |
| 2026-10-02T15:36 | CCI reversion | sell | AAPL | 7.19 | 0.01 | rebalance down |
| 2026-10-02T15:36 | Candlestick reversal | buy | PLTR | 5.02 | — | entry signal |
| 2026-10-02T15:36 | Candlestick reversal | buy | GOOGL | 5.02 | — | entry signal |
| 2026-10-02T15:36 | Candlestick reversal | sell | LABU | 4.36 | 0.01 | target is flat |
| 2026-10-02T15:36 | Candlestick reversal | sell | ETHU | 4.35 | -0.03 | target is flat |
| 2026-10-02T15:36 | Candlestick reversal | sell | ETH-USD | 4.34 | -0.04 | exit signal |
| 2026-10-02T15:36 | Candlestick reversal | sell | BITX | 4.35 | -0.02 | target is flat |
| 2026-10-02T15:36 | OBV trend | buy | SOXL | 16.16 | — | entry signal |
| 2026-10-02T15:36 | VWAP momentum | buy | SOXL | 15.71 | — | entry signal |
| 2026-10-02T15:36 | Trend pullback | buy | TNA | 17.92 | — | entry signal |
| 2026-10-02T15:36 | Trend pullback | buy | SOXL | 17.92 | — | entry signal |
| 2026-10-02T15:36 | Trend pullback | buy | IWM | 17.92 | — | entry signal |
| 2026-10-02T15:36 | ADX DI cross | buy | TNA | 14.43 | — | entry signal |
| 2026-10-02T15:36 | ADX DI cross | buy | SOXL | 14.44 | — | entry signal |
| 2026-10-02T15:36 | ADX DI cross | buy | IWM | 14.44 | — | entry signal |
| 2026-10-02T15:36 | ADX DI cross | buy | AMD | 14.44 | — | entry signal |
| 2026-10-02T15:36 | ADX DI cross | sell | SQQQ | 3.61 | 0.00 | rebalance down |
| 2026-10-02T15:36 | Parabolic SAR | buy | TSLA | 15.47 | — | entry signal |
| 2026-10-02T15:30 | AI bee: Bizzy | buy | TSLA | 11.01 | — | Jev: buy (buy p=0.55) |
| 2026-10-02T15:30 | Consensus | buy | TSLA | 16.87 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
