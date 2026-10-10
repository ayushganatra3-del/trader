# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T12:25:05.000147+00:00 · 17886 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 9322 decisions in 1865 calls, $0.1303 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T12:25 | 0 / 2 / 3 | NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T12:25 | 1 / 4 / 0 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |
| Bollinger reversion | TECL | 1.82 | +2.00% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -13.59 | -2.18 | -22.02 | 69 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.33 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -10.64 | -2.07 | -14.61 | 344 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 99.00 | -1.00 | 0 | — | 26.88 | 3.23 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.21 | -2.79 | 41 | 43.9 | 1.94 | 0.51 | -8.60 | 161 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 5.02 | 0.77 | -19.85 | 134 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 1.49 | 0.46 | -8.77 | 251 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.31 | -0.04 | -13.84 | 255 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.86 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.82 | -4.18 | 108 | 23.1 | -16.77 | -2.72 | -18.33 | 472 |
| 34 | Supertrend · 1h | trend | 95.16 | -4.84 | 52 | 13.5 | -0.24 | 0.16 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.07 | -5.93 | 35 | 25.7 | 24.00 | 3.27 | -8.76 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.43 | -1.96 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.29 | -0.39 | -9.03 | 147 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -4.49 | -0.67 | -13.24 | 419 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.32 | 0.60 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.80 | -8.20 | 67 | 29.9 | 6.45 | 0.99 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.76 | -8.24 | 120 | 47.5 | -24.48 | -4.22 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.69 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.23 | -9.77 | 114 | 30.7 | -27.33 | -5.40 | -29.13 | 517 |
| 51 | CCI reversion · 1h | reversion | 89.75 | -10.25 | 99 | 44.4 | -8.63 | -1.12 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.69 | -10.31 | 278 | 22.3 | -34.93 | -5.27 | -39.28 | 1282 |
| 53 | MACD zero-line · 1h | trend | 89.22 | -10.78 | 60 | 20.0 | -6.56 | -0.70 | -19.64 | 241 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Donchian 20/10 · 1h | breakout | 88.82 | -11.18 | 58 | 19.0 | -0.12 | 0.19 | -17.72 | 221 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.45 | -1.42 | -28.47 | 318 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.34 | -5.28 | -36.60 | 704 |
| 58 | Three white soldiers | momentum | 88.46 | -11.54 | 133 | 18.8 | -48.02 | -23.59 | -48.02 | 589 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.83 | -12.17 | 101 | 13.9 | -8.98 | -1.01 | -21.49 | 336 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.32 | -24.68 | 353 | 28.9 | -72.85 | -18.26 | -72.94 | 1496 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1666 |
| 65 | Squeeze breakout | breakout | 72.83 | -27.17 | 310 | 15.5 | -61.99 | -18.47 | -61.99 | 1223 |
| 66 | Donchian 55/20 | breakout | 71.77 | -28.23 | 319 | 18.5 | -67.58 | -14.52 | -67.67 | 1291 |
| 67 | EMA 20/50 cross | trend | 71.60 | -28.40 | 315 | 20.6 | -77.33 | -15.46 | -77.33 | 1460 |
| 68 | Volume breakout | breakout | 70.99 | -29.01 | 254 | 13.4 | -62.99 | -18.38 | -62.99 | 898 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.17 | -16.38 | -72.31 | 1443 |
| 70 | Supertrend | trend | 65.62 | -34.38 | 442 | 20.6 | -86.35 | -21.24 | -86.35 | 1919 |
| 71 | Keltner breakout | breakout | 64.17 | -35.83 | 433 | 14.8 | -84.05 | -28.45 | -84.05 | 1855 |
| 72 | Z-score reversion | reversion | 61.22 | -38.78 | 484 | 23.6 | -85.77 | -23.62 | -85.77 | 2097 |
| 73 | Ichimoku | trend | 61.02 | -38.98 | 397 | 9.8 | -81.80 | -23.62 | -81.80 | 1749 |
| 74 | AI bee: Boozy | ai | 60.97 | -39.03 | 249 | 5.2 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.61 | -39.39 | 496 | 21.8 | -87.70 | -28.61 | -87.70 | 2119 |
| 76 | AI bee: Bizzy | ai | 59.95 | -40.05 | 793 | 9.2 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.03 | -41.97 | 526 | 10.5 | -89.52 | -34.73 | -89.52 | 2128 |
| 78 | Donchian 20/10 | breakout | 57.46 | -42.54 | 610 | 18.7 | -90.89 | -26.62 | -90.89 | 2668 |
| 79 | Trend pullback | trend | 56.88 | -43.12 | 563 | 15.5 | -90.64 | -27.55 | -90.64 | 2314 |
| 80 | RSI momentum | momentum | 56.68 | -43.32 | 577 | 17.7 | -90.42 | -26.19 | -90.42 | 2384 |
| 81 | MACD zero-line | trend | 56.18 | -43.81 | 557 | 15.4 | -91.58 | -30.06 | -91.58 | 2364 |
| 82 | Triple EMA stack | trend | 55.32 | -44.68 | 601 | 16.0 | -93.22 | -31.21 | -93.22 | 2618 |
| 83 | Bollinger breakout | breakout | 52.95 | -47.05 | 640 | 14.7 | -93.55 | -33.88 | -93.55 | 2818 |
| 84 | Consensus | meta | 51.57 | -48.43 | 604 | 10.1 | -94.21 | -26.01 | -94.21 | 2684 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -31.14 | -98.71 | 5400 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.71 | -97.36 | 3542 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -37.90 | -96.50 | 3617 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.55 | -99.35 | 5693 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.26 | -32.13 | -96.26 | 3602 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.17 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.43 | -97.35 | 3682 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.83 | -98.48 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.81 | -99.51 | 6145 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -34.12 | -95.88 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.59 | -35.20 | -95.59 | 4084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.74 | -99.90 | 8338 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T12:25 | Consensus | sell | BTC-USD | 12.84 | -0.08 | target is flat |
| 2026-10-10T12:25 | Squeeze breakout | sell | BTC-USD | 18.14 | -0.12 | exit signal |
| 2026-10-10T12:25 | Keltner breakout | sell | BTC-USD | 16.02 | -0.11 | exit signal |
| 2026-10-10T12:25 | Bollinger breakout | sell | BTC-USD | 13.21 | -0.09 | exit signal |
| 2026-10-10T12:25 | Ichimoku | sell | BTC-USD | 15.18 | -0.10 | exit signal |
| 2026-10-10T12:05 | Consensus | sell | ETH-USD | 12.85 | -0.09 | target is flat |
| 2026-10-10T12:05 | Volume breakout | sell | ETH-USD | 17.66 | -0.12 | exit signal |
| 2026-10-10T12:05 | Squeeze breakout | sell | ETH-USD | 18.14 | -0.12 | stop-loss |
| 2026-10-10T12:05 | Keltner breakout | sell | SOL-USD | 15.97 | -0.13 | stop-loss |
| 2026-10-10T12:05 | Keltner breakout | sell | ETH-USD | 16.02 | -0.11 | stop-loss |
| 2026-10-10T12:05 | Bollinger breakout | sell | SOL-USD | 13.20 | -0.10 | stop-loss |
| 2026-10-10T12:05 | Bollinger breakout | sell | ETH-USD | 13.22 | -0.09 | stop-loss |
| 2026-10-10T12:05 | Donchian 55/20 | sell | ETH-USD | 17.85 | -0.13 | stop-loss |
| 2026-10-10T12:05 | Donchian 20/10 | sell | SOL-USD | 14.28 | -0.12 | stop-loss |
| 2026-10-10T12:05 | RSI momentum | sell | SOL-USD | 14.09 | -0.12 | stop-loss |
| 2026-10-10T12:05 | ADX DI cross | sell | SOL-USD | 14.43 | -0.11 | exit signal |
| 2026-10-10T12:00 | MACD zero-line · 1h | buy | ETH-USD | 4.50 | — | entry signal |
| 2026-10-10T12:00 | MACD zero-line · 1h | sell | XRP-USD | 4.50 | -0.01 | rebalance down |
| 2026-10-10T12:00 | MACD zero-line | buy | SOL-USD | 14.07 | — | entry signal |
| 2026-10-10T11:58 | AI bee: Boozy | sell | ETH-USD | 15.22 | -0.09 | Jev: sell |
| 2026-10-10T11:55 | AI bee: Bizzy | sell | ETH-USD | 9.33 | -0.06 | Jev: sell (sell p=0.56) after 11 min |
| 2026-10-10T11:55 | AI bee: Bizzy | sell | BTC-USD | 8.63 | -0.05 | Jev: sell (sell p=0.68) after 10 min |
| 2026-10-10T11:55 | Keltner breakout | buy | SOL-USD | 16.11 | — | entry signal |
| 2026-10-10T11:55 | Donchian 20/10 | buy | SOL-USD | 14.40 | — | entry signal |
| 2026-10-10T11:55 | RSI momentum | buy | SOL-USD | 14.20 | — | entry signal |
| 2026-10-10T11:50 | Consensus | buy | BTC-USD | 12.93 | — | entry |
| 2026-10-10T11:50 | Ichimoku | buy | BTC-USD | 15.28 | — | entry signal |
| 2026-10-10T11:49 | AI bee: Bizzy | sell | XRP-USD | 8.77 | -0.05 | Jev: sell (sell p=0.83) after 11 min |
| 2026-10-10T11:45 | AI bee: Bizzy | buy | BTC-USD | 8.68 | — | Jev: buy (buy p=0.58) |
| 2026-10-10T11:45 | Consensus | buy | ETH-USD | 12.94 | — | entry |
| 2026-10-10T11:45 | MFI reversion | sell | ETH-USD | 15.23 | -0.06 | exit signal |
| 2026-10-10T11:45 | MFI reversion | sell | DOGE-USD | 15.11 | -0.08 | exit signal |
| 2026-10-10T11:45 | Z-score reversion | sell | SOL-USD | 15.27 | -0.07 | exit signal |
| 2026-10-10T11:45 | RSI(14) reversion | sell | SOL-USD | 18.81 | -0.06 | exit signal |
| 2026-10-10T11:45 | Squeeze breakout | buy | BTC-USD | 18.26 | — | entry signal |
| 2026-10-10T11:45 | Keltner breakout | buy | ETH-USD | 16.13 | — | entry signal |
| 2026-10-10T11:45 | Keltner breakout | buy | BTC-USD | 16.13 | — | entry signal |
| 2026-10-10T11:45 | Bollinger breakout | buy | SOL-USD | 13.30 | — | entry signal |
| 2026-10-10T11:45 | Bollinger breakout | buy | BTC-USD | 13.30 | — | entry signal |
| 2026-10-10T11:45 | Donchian 55/20 | buy | ETH-USD | 17.97 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 12:25:05.000147+00:00 -> 2026-10-10 12:35:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
