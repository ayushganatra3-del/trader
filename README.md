# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T15:55:05.000130+00:00 · 18067 ticks

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

Today: 12037 decisions in 2408 calls, $0.1682 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T15:55 | 1 / 2 / 2 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-10T15:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T15:55 | 1 / 3 / 1 | COIN 75% |  |

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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.22 | 2.44 | -1.58 | 86 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -10.63 | -2.06 | -14.61 | 344 |
| 19 | Hold BTC | benchmark | 99.18 | -0.82 | 0 | — | 26.84 | 3.22 | -8.68 | 1 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.56 | 0.44 | -8.60 | 160 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 5.96 | 0.87 | -19.85 | 131 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.82 | -0.12 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.81 | -0.20 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.83 | -5.49 | -10.38 | 243 |
| 33 | MACD cross · 1h | trend | 95.87 | -4.12 | 110 | 24.5 | -16.60 | -2.69 | -18.23 | 472 |
| 34 | Supertrend · 1h | trend | 95.35 | -4.65 | 52 | 13.5 | -0.07 | 0.18 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.12 | -5.88 | 35 | 25.7 | 24.07 | 3.28 | -8.76 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.68 | -2.56 | -7.39 | 112 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.27 | -1.79 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.73 | -0.71 | -9.03 | 152 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 92.93 | -7.07 | 41 | 19.5 | -0.64 | 0.12 | -20.02 | 122 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -7.64 | -1.33 | -14.72 | 415 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.34 | 0.61 | -17.07 | 224 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.30 | 1.15 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.91 | -8.10 | 67 | 29.9 | 6.50 | 1.00 | -12.90 | 286 |
| 47 | Williams %R · 1h | reversion | 91.76 | -8.24 | 120 | 47.5 | -24.48 | -4.22 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.41 | -0.83 | -26.38 | 234 |
| 50 | Candlestick reversal · 1h | reversion | 90.30 | -9.70 | 114 | 30.7 | -27.55 | -5.44 | -29.43 | 519 |
| 51 | CCI reversion · 1h | reversion | 89.78 | -10.22 | 100 | 45.0 | -8.60 | -1.11 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 278 | 22.3 | -34.61 | -5.22 | -39.27 | 1283 |
| 53 | MACD zero-line · 1h | trend | 89.23 | -10.77 | 62 | 19.4 | -6.57 | -0.70 | -19.72 | 241 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Donchian 20/10 · 1h | breakout | 88.85 | -11.15 | 58 | 19.0 | -0.10 | 0.19 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.51 | -1.29 | -28.53 | 316 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.37 | -5.29 | -36.60 | 704 |
| 58 | Three white soldiers | momentum | 88.02 | -11.98 | 136 | 18.4 | -48.02 | -23.43 | -48.02 | 589 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.88 | -12.12 | 101 | 13.9 | -8.89 | -1.00 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.50 | -1.28 | -23.91 | 412 |
| 63 | RSI(14) reversion | reversion | 75.28 | -24.72 | 355 | 28.7 | -72.97 | -18.35 | -73.04 | 1498 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.91 | -16.73 | -73.81 | 1670 |
| 65 | Squeeze breakout | breakout | 72.07 | -27.93 | 316 | 15.2 | -62.39 | -18.59 | -62.39 | 1230 |
| 66 | Donchian 55/20 | breakout | 71.42 | -28.58 | 320 | 18.4 | -67.69 | -14.57 | -67.71 | 1296 |
| 67 | EMA 20/50 cross | trend | 71.35 | -28.65 | 318 | 20.4 | -77.49 | -15.56 | -77.50 | 1466 |
| 68 | Volume breakout | breakout | 70.61 | -29.39 | 257 | 13.2 | -63.08 | -18.37 | -63.08 | 903 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.55 | -16.53 | -72.69 | 1452 |
| 70 | Supertrend | trend | 65.63 | -34.37 | 443 | 20.5 | -86.35 | -21.24 | -86.36 | 1922 |
| 71 | Keltner breakout | breakout | 63.87 | -36.13 | 436 | 14.7 | -84.00 | -28.34 | -84.00 | 1854 |
| 72 | Z-score reversion | reversion | 61.19 | -38.81 | 486 | 23.5 | -85.73 | -23.57 | -85.73 | 2095 |
| 73 | Ichimoku | trend | 60.87 | -39.13 | 398 | 9.8 | -81.76 | -23.50 | -81.76 | 1748 |
| 74 | AI bee: Boozy | ai | 60.76 | -39.24 | 251 | 5.2 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.61 | -39.39 | 496 | 21.8 | -87.70 | -28.61 | -87.70 | 2121 |
| 76 | AI bee: Bizzy | ai | 59.64 | -40.36 | 800 | 9.1 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.03 | -41.97 | 526 | 10.5 | -89.49 | -34.55 | -89.49 | 2126 |
| 78 | Donchian 20/10 | breakout | 57.11 | -42.89 | 613 | 18.6 | -90.86 | -26.51 | -90.86 | 2668 |
| 79 | RSI momentum | momentum | 56.35 | -43.65 | 580 | 17.6 | -90.40 | -26.12 | -90.41 | 2386 |
| 80 | Trend pullback | trend | 56.17 | -43.83 | 572 | 15.2 | -90.70 | -27.39 | -90.71 | 2321 |
| 81 | MACD zero-line | trend | 55.61 | -44.39 | 565 | 15.2 | -91.69 | -30.36 | -91.69 | 2370 |
| 82 | Triple EMA stack | trend | 54.96 | -45.05 | 606 | 15.8 | -93.19 | -30.95 | -93.20 | 2618 |
| 83 | Bollinger breakout | breakout | 52.37 | -47.63 | 647 | 14.5 | -93.59 | -33.89 | -93.59 | 2822 |
| 84 | Consensus | meta | 51.11 | -48.89 | 609 | 10.0 | -94.26 | -26.17 | -94.26 | 2696 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -31.01 | -98.70 | 5407 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -33.73 | -97.39 | 3550 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -37.42 | -96.47 | 3612 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.68 | -99.35 | 5698 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -32.13 | -96.29 | 3607 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -43.40 | -99.74 | 6212 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.02 | -97.35 | 3681 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.89 | -98.48 | 4717 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.98 | -99.51 | 6150 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -34.12 | -95.87 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.60 | -35.27 | -95.60 | 4087 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.12 | -99.90 | 8332 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T15:55 | Squeeze breakout | sell | SOL-USD | 18.00 | -0.11 | exit signal |
| 2026-10-10T15:55 | Bollinger breakout | sell | SOL-USD | 10.47 | -0.06 | exit signal |
| 2026-10-10T15:40 | Donchian 55/20 | buy | DOGE-USD | 14.21 | — | entry |
| 2026-10-10T15:40 | Donchian 55/20 | sell | XRP-USD | 3.57 | -0.02 | rebalance down |
| 2026-10-10T15:40 | EMA 20/50 cross | buy | DOGE-USD | 17.86 | — | entry |
| 2026-10-10T15:35 | Consensus | buy | BTC-USD | 12.79 | — | entry |
| 2026-10-10T15:35 | Donchian 55/20 | buy | XRP-USD | 3.59 | — | rebalance up |
| 2026-10-10T15:35 | Donchian 55/20 | sell | DOGE-USD | 14.24 | -0.12 | stop-loss |
| 2026-10-10T15:35 | EMA 20/50 cross | sell | DOGE-USD | 17.73 | -0.15 | stop-loss |
| 2026-10-10T15:30 | Consensus | sell | BTC-USD | 12.80 | -0.08 | target is flat |
| 2026-10-10T15:30 | ROC + volume | sell | SOL-USD | 18.59 | -0.14 | exit signal |
| 2026-10-10T15:30 | MACD zero-line | sell | BTC-USD | 13.89 | -0.08 | exit signal |
| 2026-10-10T15:25 | Consensus | sell | SOL-USD | 12.78 | -0.09 | target is flat |
| 2026-10-10T15:25 | Three white soldiers | sell | SOL-USD | 21.94 | -0.14 | exit signal |
| 2026-10-10T15:20 | Trend pullback | buy | XRP-USD | 14.06 | — | entry signal |
| 2026-10-10T15:20 | Trend pullback | buy | DOGE-USD | 14.06 | — | entry signal |
| 2026-10-10T15:20 | MACD zero-line | sell | DOGE-USD | 13.90 | -0.06 | exit signal |
| 2026-10-10T15:15 | Consensus | sell | ETH-USD | 10.25 | -0.07 | target is flat |
| 2026-10-10T15:15 | Three white soldiers | sell | BTC-USD | 21.92 | -0.15 | exit signal |
| 2026-10-10T15:15 | Volume breakout | sell | ETH-USD | 17.63 | -0.11 | exit signal |
| 2026-10-10T15:15 | Keltner breakout | sell | ETH-USD | 12.75 | -0.08 | stop-loss |
| 2026-10-10T15:15 | Bollinger breakout | sell | ETH-USD | 10.46 | -0.07 | stop-loss |
| 2026-10-10T15:15 | ROC + volume | sell | ETH-USD | 18.57 | -0.15 | stop-loss |
| 2026-10-10T15:15 | Ichimoku | sell | XRP-USD | 15.14 | -0.11 | exit signal |
| 2026-10-10T15:15 | MACD zero-line | sell | XRP-USD | 13.86 | -0.11 | exit signal |
| 2026-10-10T15:10 | Volume breakout | sell | DOGE-USD | 17.62 | -0.13 | exit signal |
| 2026-10-10T15:10 | Triple EMA stack | sell | DOGE-USD | 13.70 | -0.11 | stop-loss |
| 2026-10-10T15:05 | Ichimoku | buy | XRP-USD | 15.24 | — | entry signal |
| 2026-10-10T15:00 | AI bee: Bizzy | sell | SOL-USD | 9.03 | -0.01 | Jev: sell (sell p=0.53) after 41 min |
| 2026-10-10T15:00 | Consensus | sell | DOGE-USD | 10.24 | -0.07 | target is flat |
| 2026-10-10T15:00 | CCI reversion · 1h | sell | SOL-USD | 5.65 | 0.03 | exit signal |
| 2026-10-10T15:00 | Squeeze breakout · 1h | buy | ETH-USD | 23.55 | — | entry signal |
| 2026-10-10T15:00 | Ichimoku · 1h | buy | BTC-USD | 23.25 | — | entry signal |
| 2026-10-10T15:00 | Volume breakout | sell | XRP-USD | 17.61 | -0.13 | exit signal |
| 2026-10-10T15:00 | Squeeze breakout | sell | XRP-USD | 17.97 | -0.14 | stop-loss |
| 2026-10-10T15:00 | Squeeze breakout | sell | DOGE-USD | 18.05 | -0.06 | stop-loss |
| 2026-10-10T15:00 | Keltner breakout | sell | XRP-USD | 12.73 | -0.10 | stop-loss |
| 2026-10-10T15:00 | Keltner breakout | sell | DOGE-USD | 12.79 | -0.04 | stop-loss |
| 2026-10-10T15:00 | Bollinger breakout | sell | XRP-USD | 10.44 | -0.08 | stop-loss |
| 2026-10-10T15:00 | Bollinger breakout | sell | DOGE-USD | 10.49 | -0.03 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 15:55:05.000130+00:00 -> 2026-10-10 16:05:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
