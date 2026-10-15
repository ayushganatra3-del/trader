# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T05:25:05.000164+00:00 · 23260 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 4050 decisions in 810 calls, $0.0568 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T05:25 | 1 / 1 / 3 | TNA 15% |  |
| Breezy | 2026-10-15T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T05:25 | 1 / 3 / 1 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.54 | +0.60% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Triple EMA stack | NVDA | 1.50 | +0.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.38 | 4.38 | 0 | — | 4.16 | 1.99 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.69 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.45 | -0.74 | -9.84 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.97 | -7.55 | 43 |
| 6 | VWAP reversion · 1h | reversion | 100.81 | 0.81 | 46 | 39.1 | -8.87 | -2.65 | -13.79 | 126 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.40 | 0.40 | 0 | — | 4.04 | 1.58 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.21 | 0.21 | 20 | 45.0 | -16.02 | -2.54 | -21.97 | 76 |
| 9 | Hold SPY | benchmark | 100.02 | 0.02 | 0 | — | -0.98 | -0.53 | -3.44 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.28 | -3.79 | -3.91 | 21 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.68 | -1.32 | 0 | — | -1.10 | -0.42 | -3.75 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 98.47 | -1.53 | 0 | — | -5.15 | -2.02 | -6.99 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.01 | -2.07 | 67 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 98.38 | -1.62 | 0 | — | -4.93 | -2.74 | -5.36 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 97.00 | -3.00 | 36 | 16.7 | 5.91 | 0.86 | -22.11 | 114 |
| 18 | Trend pullback · 1h | trend | 96.87 | -3.13 | 86 | 24.4 | -24.18 | -6.92 | -24.88 | 168 |
| 19 | Hold BTC | benchmark | 96.85 | -3.15 | 0 | — | 28.09 | 3.26 | -8.68 | 1 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 22 | Agent (rotation) | meta | 96.16 | -3.84 | 93 | 30.1 | -12.29 | -4.23 | -13.61 | 270 |
| 23 | ADX DI cross · 1h | trend | 95.71 | -4.29 | 70 | 21.4 | -10.50 | -1.91 | -14.52 | 250 |
| 24 | Daily: Bullish score | daily | 94.74 | -5.26 | 5 | 0.0 | -2.87 | -0.17 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 94.65 | -5.35 | 13 | 38.5 | -9.94 | -0.18 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.56 | -5.45 | 0 | — | -15.33 | -2.92 | -16.54 | 1 |
| 27 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.60 | 2.41 | -6.73 | 199 |
| 28 | EMA 20/50 cross · 1h | trend | 93.85 | -6.15 | 48 | 16.7 | 5.14 | 0.77 | -23.21 | 138 |
| 29 | Parabolic SAR · 1h | trend | 93.79 | -6.21 | 93 | 22.6 | 0.54 | 0.26 | -23.42 | 287 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.07 | 1.09 | -9.46 | 102 |
| 31 | MACD cross · 1h | trend | 93.38 | -6.62 | 149 | 22.8 | -11.85 | -1.59 | -21.42 | 454 |
| 32 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -5.92 | -2.11 | -9.56 | 240 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 92.82 | -7.18 | 0 | — | 3.87 | 0.74 | -11.29 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 91.96 | -8.04 | 8 | 37.5 | -6.02 | -0.21 | -34.64 | 27 |
| 35 | Bollinger breakout · 1h | breakout | 91.80 | -8.20 | 78 | 29.5 | 7.55 | 1.12 | -14.21 | 277 |
| 36 | RSI momentum · 1h | momentum | 91.71 | -8.29 | 73 | 17.8 | 0.98 | 0.32 | -25.52 | 224 |
| 37 | Supertrend · 1h | trend | 91.54 | -8.46 | 73 | 13.7 | 1.72 | 0.41 | -23.21 | 207 |
| 38 | Stochastic reversion · 1h | reversion | 91.30 | -8.70 | 119 | 47.1 | -17.26 | -3.23 | -17.97 | 358 |
| 39 | Volume breakout · 1h | breakout | 90.85 | -9.15 | 77 | 22.1 | 7.66 | 1.21 | -12.60 | 121 |
| 40 | Ichimoku · 1h | trend | 90.41 | -9.59 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 41 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.47 | -2.75 | -10.83 | 121 |
| 42 | Triple EMA stack · 1h | trend | 90.23 | -9.77 | 77 | 16.9 | -11.04 | -0.99 | -34.69 | 237 |
| 43 | Connors RSI(2) · 1h | reversion | 89.42 | -10.58 | 137 | 40.1 | -23.03 | -6.86 | -24.82 | 249 |
| 44 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.00 | -17.60 | 556 |
| 45 | Z-score reversion · 1h | reversion | 88.72 | -11.28 | 65 | 35.4 | -9.51 | -1.73 | -13.93 | 166 |
| 46 | MFI reversion · 1h | reversion | 88.24 | -11.76 | 180 | 29.4 | -17.98 | -3.16 | -18.13 | 136 |
| 47 | OBV trend · 1h | momentum | 88.04 | -11.96 | 164 | 18.9 | -11.00 | -0.96 | -35.00 | 320 |
| 48 | Keltner breakout · 1h | breakout | 87.54 | -12.46 | 51 | 21.6 | -7.86 | -0.83 | -26.76 | 217 |
| 49 | Agent (ML meta-label) | meta | 87.43 | -12.57 | 540 | 18.1 | -5.50 | -0.71 | -16.53 | 395 |
| 50 | MACD zero-line · 1h | trend | 87.24 | -12.76 | 74 | 16.2 | -23.33 | -4.51 | -23.82 | 227 |
| 51 | Donchian 20/10 · 1h | breakout | 86.55 | -13.45 | 71 | 19.7 | -1.04 | 0.07 | -20.38 | 217 |
| 52 | VWAP momentum · 1h | momentum | 85.85 | -14.15 | 347 | 21.9 | -36.79 | -5.52 | -42.60 | 1240 |
| 53 | ROC + volume · 1h | momentum | 85.65 | -14.35 | 179 | 21.2 | -11.73 | -1.59 | -25.35 | 396 |
| 54 | Heikin-Ashi · 1h | trend | 85.59 | -14.41 | 169 | 26.0 | -31.37 | -5.13 | -39.47 | 663 |
| 55 | RSI(14) reversion · 1h | reversion | 85.12 | -14.88 | 53 | 24.5 | -6.34 | -0.93 | -15.32 | 162 |
| 56 | EMA 9/21 cross · 1h | trend | 85.05 | -14.95 | 120 | 12.5 | -10.31 | -1.18 | -26.92 | 325 |
| 57 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.22 | -4.91 | -21.41 | 692 |
| 58 | Bollinger reversion · 1h | reversion | 84.60 | -15.40 | 110 | 32.7 | -26.02 | -5.49 | -28.69 | 329 |
| 59 | Three white soldiers | momentum | 84.01 | -15.99 | 184 | 16.3 | -48.84 | -21.86 | -48.84 | 593 |
| 60 | CCI reversion · 1h | reversion | 83.59 | -16.41 | 132 | 41.7 | -17.43 | -2.29 | -21.40 | 417 |
| 61 | Williams %R · 1h | reversion | 82.10 | -17.90 | 158 | 42.4 | -33.38 | -5.51 | -34.15 | 509 |
| 62 | Candlestick reversal · 1h | reversion | 81.32 | -18.68 | 163 | 27.0 | -31.78 | -5.87 | -31.78 | 518 |
| 63 | ROC + volume | momentum | 66.78 | -33.22 | 486 | 21.4 | -74.45 | -16.51 | -76.53 | 1671 |
| 64 | Volume breakout | breakout | 65.88 | -34.12 | 307 | 13.7 | -63.16 | -17.68 | -63.17 | 886 |
| 65 | RSI(14) reversion | reversion | 65.42 | -34.58 | 545 | 26.6 | -73.80 | -16.74 | -74.03 | 1549 |
| 66 | Squeeze breakout | breakout | 64.67 | -35.33 | 401 | 14.7 | -63.28 | -17.77 | -63.28 | 1211 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -69.00 | -14.34 | -70.95 | 1270 |
| 68 | EMA 20/50 cross | trend | 62.11 | -37.89 | 414 | 19.1 | -77.38 | -15.08 | -78.05 | 1431 |
| 69 | VWAP reversion | reversion | 58.28 | -41.72 | 570 | 23.7 | -73.10 | -15.26 | -73.25 | 1445 |
| 70 | AI bee: Boozy | ai | 57.65 | -42.35 | 272 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.05 | -43.95 | 552 | 14.1 | -83.35 | -26.23 | -83.35 | 1826 |
| 72 | Supertrend | trend | 54.79 | -45.21 | 573 | 18.8 | -86.53 | -20.14 | -86.53 | 1893 |
| 73 | Ichimoku | trend | 53.88 | -46.12 | 489 | 9.8 | -81.89 | -22.19 | -81.89 | 1702 |
| 74 | AI bee: Bizzy | ai | 51.59 | -48.41 | 995 | 8.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -29.07 | -98.60 | 5294 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -29.02 | -93.44 | 2567 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -24.13 | -90.61 | 2339 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.68 | -26.07 | -91.71 | 2342 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.49 | -31.83 | -97.49 | 3510 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -34.22 | -96.53 | 3554 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -24.23 | -94.36 | 2622 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -34.99 | -99.40 | 5749 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.16 | -25.04 | -91.16 | 2613 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -30.08 | -96.32 | 3567 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.39 | -99.73 | 6150 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.01 | -29.13 | -92.01 | 2353 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.43 | -36.39 | -97.43 | 3638 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -35.83 | -98.55 | 4688 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -31.68 | -93.54 | 2778 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.17 | -99.56 | 6155 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.38 | -22.20 | -86.48 | 2100 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.91 | -26.79 | -88.02 | 2131 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.07 | -32.04 | -96.08 | 3764 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.62 | -33.46 | -89.62 | 2104 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.78 | -32.98 | -95.80 | 4071 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.16 | -99.89 | 8198 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T05:20 | ROC + volume | sell | DOGE-USD | 16.60 | -0.25 | exit signal |
| 2026-10-15T05:20 | Supertrend | sell | XRP-USD | 13.60 | -0.26 | exit signal |
| 2026-10-15T05:20 | Supertrend | sell | SOL-USD | 13.59 | -0.27 | exit signal |
| 2026-10-15T05:15 | ROC + volume | sell | XRP-USD | 16.62 | -0.23 | stop-loss |
| 2026-10-15T05:15 | ROC + volume | sell | BTC-USD | 16.69 | -0.17 | stop-loss |
| 2026-10-15T05:10 | Squeeze breakout | sell | DOGE-USD | 16.07 | -0.13 | exit signal |
| 2026-10-15T05:10 | Keltner breakout | sell | XRP-USD | 13.83 | -0.24 | stop-loss |
| 2026-10-15T05:00 | MFI reversion · 1h | buy | ETH-USD | 4.50 | — | entry signal |
| 2026-10-15T05:00 | MFI reversion · 1h | sell | DOGE-USD | 4.50 | 0.03 | rebalance down |
| 2026-10-15T05:00 | CCI reversion · 1h | buy | SOL-USD | 6.28 | — | entry signal |
| 2026-10-15T05:00 | CCI reversion · 1h | buy | BTC-USD | 13.97 | — | entry signal |
| 2026-10-15T05:00 | Z-score reversion · 1h | buy | XRP-USD | 14.88 | — | entry signal |
| 2026-10-15T05:00 | Z-score reversion · 1h | buy | SOL-USD | 14.88 | — | entry signal |
| 2026-10-15T05:00 | Z-score reversion · 1h | buy | BTC-USD | 14.88 | — | entry signal |
| 2026-10-15T05:00 | Bollinger reversion · 1h | buy | ETH-USD | 4.71 | — | entry signal |
| 2026-10-15T05:00 | Bollinger reversion · 1h | buy | DOGE-USD | 4.71 | — | entry signal |
| 2026-10-15T05:00 | RSI(14) reversion · 1h | buy | XRP-USD | 9.52 | — | entry signal |
| 2026-10-15T05:00 | RSI(14) reversion · 1h | buy | SOL-USD | 9.52 | — | entry signal |
| 2026-10-15T05:00 | RSI(14) reversion · 1h | buy | ETH-USD | 9.52 | — | entry signal |
| 2026-10-15T05:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 9.52 | — | entry signal |
| 2026-10-15T05:00 | RSI(14) reversion · 1h | buy | BTC-USD | 9.52 | — | entry signal |
| 2026-10-15T05:00 | Candlestick reversal · 1h | buy | ETH-USD | 3.88 | — | entry signal |
| 2026-10-15T05:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.88 | — | entry signal |
| 2026-10-15T04:50 | ROC + volume | buy | DOGE-USD | 16.85 | — | entry signal |
| 2026-10-15T04:47 | AI bee: Bizzy | sell | XRP-USD | 8.06 | -0.03 | Jev: sell (sell p=0.57) after 15 min |
| 2026-10-15T04:45 | Keltner breakout | buy | XRP-USD | 14.07 | — | entry signal |
| 2026-10-15T04:45 | Supertrend | buy | BTC-USD | 13.85 | — | entry signal |
| 2026-10-15T04:40 | RSI(14) reversion | sell | ETH-USD | 16.26 | -0.04 | exit signal |
| 2026-10-15T04:40 | ROC + volume | buy | BTC-USD | 16.85 | — | entry signal |
| 2026-10-15T04:40 | Supertrend | buy | XRP-USD | 13.86 | — | entry signal |
| 2026-10-15T04:40 | Supertrend | buy | SOL-USD | 13.86 | — | entry signal |
| 2026-10-15T04:35 | ROC + volume | buy | XRP-USD | 16.86 | — | entry signal |
| 2026-10-15T04:32 | AI bee: Bizzy | buy | XRP-USD | 8.09 | — | Jev: buy (buy p=0.63) |
| 2026-10-15T04:30 | VWAP reversion | sell | ETH-USD | 14.53 | 0.01 | exit signal |
| 2026-10-15T04:30 | RSI(14) reversion | sell | DOGE-USD | 16.41 | 0.07 | exit signal |
| 2026-10-15T04:25 | RSI(14) reversion | sell | XRP-USD | 16.38 | 0.06 | exit signal |
| 2026-10-15T04:25 | RSI(14) reversion | sell | SOL-USD | 16.37 | 0.06 | exit signal |
| 2026-10-15T04:25 | Squeeze breakout | buy | DOGE-USD | 16.20 | — | entry signal |
| 2026-10-15T04:15 | AI bee: Bizzy | sell | SOL-USD | 7.39 | -0.07 | Jev: sell (sell p=0.71) after 11 min |
| 2026-10-15T04:04 | AI bee: Bizzy | buy | SOL-USD | 7.46 | — | Jev: buy (buy p=0.58) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 05:25:05.000164+00:00 -> 2026-10-15 05:35:05.000164+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
