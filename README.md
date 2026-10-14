# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T00:55:05.000146+00:00 · 21894 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.12 (-4.88%)

Closed trades 64, win rate 46.9%, fees £2.37, max drawdown -5.38%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-13 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-13)

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 705 decisions in 141 calls, $0.0098 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T00:55 | 1 / 3 / 1 | AMD 14% |  |
| Breezy | 2026-10-14T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T00:55 | 1 / 4 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Three white soldiers | NVDA | 1.77 | +1.00% | 3 |
| ROC + volume | META | 1.74 | +2.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.13 | 3.13 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.00 | -2.66 | -13.79 | 116 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.43 | 1.44 | 18 | 50.0 | -15.67 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.66 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.06 | 1.05 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.42 | 0.42 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.85 | -0.15 | 0 | — | 4.59 | 1.77 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.83 | -0.17 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.58 | -0.42 | 0 | — | 31.20 | 3.59 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.95 | -1.05 | 0 | — | -8.33 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.41 | -1.58 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.80 | -2.20 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.48 | -2.52 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.38 | -2.62 | 5 | 0.0 | 0.46 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.02 | -2.86 | -8.81 | 307 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.48 | -3.52 | 64 | 18.8 | -10.96 | -2.00 | -14.81 | 248 |
| 26 | Stochastic reversion · 1h | reversion | 96.26 | -3.74 | 107 | 51.4 | -14.34 | -2.77 | -16.50 | 345 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.79 | -4.21 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.61 | -4.39 | 132 | 23.5 | -8.93 | -1.15 | -19.25 | 459 |
| 29 | Z-score reversion · 1h | reversion | 95.52 | -4.48 | 50 | 44.0 | 2.90 | 0.70 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.38 | -4.62 | 45 | 15.6 | 10.11 | 1.27 | -19.71 | 137 |
| 31 | Max aggression: 1-day momentum | meta | 95.37 | -4.63 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.87 | -5.00 | -9.05 | 235 |
| 33 | Supertrend · 1h | trend | 94.04 | -5.96 | 60 | 13.3 | 2.27 | 0.48 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.94 | -6.06 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.78 | -6.22 | 90 | 22.2 | 1.39 | 0.37 | -22.66 | 289 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.09 | -0.31 | -5.63 | 113 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.56 | 2.17 | -6.74 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.63 | -7.37 | 66 | 15.2 | 0.86 | 0.31 | -25.56 | 228 |
| 39 | MFI reversion · 1h | reversion | 92.54 | -7.46 | 165 | 31.5 | -7.95 | -1.22 | -17.02 | 131 |
| 40 | Connors RSI(2) · 1h | reversion | 92.03 | -7.97 | 127 | 42.5 | -19.96 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.52 | -8.48 | 37 | 32.4 | 5.65 | 1.30 | -9.40 | 128 |
| 42 | Ichimoku · 1h | trend | 91.31 | -8.69 | 48 | 16.7 | 2.06 | 0.44 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 91.07 | -8.93 | 485 | 18.1 | -1.10 | -0.08 | -12.72 | 362 |
| 44 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 71 | 15.5 | -7.56 | -0.58 | -32.27 | 241 |
| 45 | Volume breakout · 1h | breakout | 90.68 | -9.32 | 75 | 22.7 | 8.82 | 1.34 | -12.60 | 119 |
| 46 | Bollinger breakout · 1h | breakout | 90.68 | -9.32 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 90.02 | -9.98 | 97 | 37.1 | -23.78 | -5.71 | -24.98 | 321 |
| 48 | Williams %R · 1h | reversion | 89.43 | -10.57 | 143 | 45.5 | -28.06 | -4.75 | -29.94 | 511 |
| 49 | CCI reversion · 1h | reversion | 89.04 | -10.96 | 117 | 45.3 | -9.52 | -1.24 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.03 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.12 | -11.88 | 158 | 18.4 | -9.67 | -0.81 | -33.87 | 322 |
| 52 | VWAP momentum · 1h | momentum | 87.67 | -12.34 | 325 | 23.1 | -34.29 | -5.11 | -40.76 | 1255 |
| 53 | MACD zero-line · 1h | trend | 87.63 | -12.37 | 69 | 17.4 | -21.94 | -4.25 | -22.68 | 227 |
| 54 | Donchian 20/10 · 1h | breakout | 87.00 | -13.00 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Heikin-Ashi · 1h | trend | 86.78 | -13.22 | 165 | 26.7 | -29.94 | -4.91 | -38.32 | 679 |
| 56 | Max aggression: 5-day momentum | meta | 86.77 | -13.23 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 57 | EMA 9/21 cross · 1h | trend | 86.70 | -13.30 | 110 | 12.7 | -10.43 | -1.32 | -24.14 | 329 |
| 58 | Keltner breakout · 1h | breakout | 86.69 | -13.31 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 59 | Candlestick reversal · 1h | reversion | 86.56 | -13.44 | 141 | 31.2 | -30.22 | -5.80 | -30.80 | 477 |
| 60 | Three white soldiers | momentum | 86.35 | -13.65 | 163 | 18.4 | -47.57 | -21.96 | -47.74 | 586 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.82 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.34 | -14.66 | 173 | 20.2 | -8.82 | -1.01 | -24.84 | 399 |
| 63 | ROC + volume | momentum | 71.32 | -28.68 | 454 | 22.5 | -73.10 | -16.33 | -75.00 | 1667 |
| 64 | Squeeze breakout | breakout | 67.81 | -32.19 | 377 | 15.4 | -62.27 | -17.71 | -62.29 | 1219 |
| 65 | Volume breakout | breakout | 67.78 | -32.22 | 293 | 14.3 | -61.88 | -17.41 | -61.89 | 888 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.72 | -16.91 | -74.10 | 1485 |
| 67 | EMA 20/50 cross | trend | 66.11 | -33.89 | 388 | 20.4 | -76.31 | -14.83 | -76.62 | 1437 |
| 68 | Donchian 55/20 | breakout | 64.46 | -35.53 | 385 | 17.1 | -68.87 | -14.38 | -70.12 | 1283 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -71.93 | -14.94 | -72.00 | 1386 |
| 70 | AI bee: Boozy | ai | 60.01 | -39.98 | 268 | 4.9 | — | — | — | — |
| 71 | Supertrend | trend | 59.69 | -40.31 | 540 | 20.0 | -85.57 | -20.05 | -85.59 | 1908 |
| 72 | Keltner breakout | breakout | 58.75 | -41.25 | 529 | 14.6 | -83.19 | -26.53 | -83.19 | 1848 |
| 73 | Ichimoku | trend | 54.81 | -45.19 | 474 | 9.7 | -82.30 | -22.63 | -82.31 | 1724 |
| 74 | AI bee: Bizzy | ai | 53.65 | -46.35 | 947 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.10 | -46.90 | 671 | 20.3 | -87.86 | -26.72 | -87.87 | 2117 |
| 76 | Z-score reversion | reversion | 52.35 | -47.65 | 622 | 23.2 | -86.20 | -21.79 | -86.21 | 2089 |
| 77 | ADX DI cross | trend | 51.86 | -48.14 | 645 | 10.5 | -89.18 | -32.67 | -89.21 | 2115 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.42 | -28.20 | -98.43 | 5286 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.31 | -29.18 | -93.31 | 2609 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.24 | -24.23 | -90.24 | 2369 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.65 | -26.29 | -91.65 | 2356 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.28 | -31.12 | -97.30 | 3526 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -34.28 | -96.45 | 3590 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -24.96 | -94.44 | 2639 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -34.63 | -99.36 | 5628 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.76 | -25.02 | -90.77 | 2631 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.33 | -30.18 | -96.33 | 3590 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -38.99 | -99.72 | 6163 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.36 | -28.57 | -91.36 | 2353 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -35.70 | -97.37 | 3670 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -34.46 | -98.51 | 4671 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.37 | -31.49 | -93.37 | 2798 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.12 | -99.54 | 6119 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.00 | -31.18 | -96.00 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -32.49 | -95.67 | 4043 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.90 | -99.89 | 8219 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T00:55 | Keltner breakout | sell | ETH-USD | 14.66 | -0.10 | stop-loss |
| 2026-10-14T00:55 | Donchian 55/20 | sell | ETH-USD | 16.08 | -0.15 | stop-loss |
| 2026-10-14T00:55 | Ichimoku | sell | ETH-USD | 13.63 | -0.13 | stop-loss |
| 2026-10-14T00:55 | EMA 20/50 cross | sell | ETH-USD | 13.14 | -0.10 | stop-loss |
| 2026-10-14T00:53 | EMA 20/50 cross | buy | ETH-USD | 3.30 | — | rebalance up |
| 2026-10-14T00:53 | EMA 20/50 cross | sell | SOL-USD | 3.30 | -0.02 | rebalance down |
| 2026-10-14T00:52 | EMA 20/50 cross | buy | ETH-USD | 3.30 | — | rebalance up |
| 2026-10-14T00:52 | EMA 20/50 cross | sell | XRP-USD | 3.30 | -0.02 | rebalance down |
| 2026-10-14T00:50 | AI bee: Boozy | sell | ETH-USD | 13.70 | -0.08 | Jev: buy |
| 2026-10-14T00:50 | Three white soldiers | sell | SOL-USD | 21.46 | -0.21 | stop-loss |
| 2026-10-14T00:50 | Volume breakout | sell | XRP-USD | 16.86 | -0.17 | stop-loss |
| 2026-10-14T00:50 | Volume breakout | sell | DOGE-USD | 16.89 | -0.14 | exit signal |
| 2026-10-14T00:50 | Squeeze breakout | sell | SOL-USD | 16.91 | -0.06 | stop-loss |
| 2026-10-14T00:50 | Keltner breakout | sell | XRP-USD | 11.75 | -0.06 | stop-loss |
| 2026-10-14T00:50 | Keltner breakout | sell | SOL-USD | 11.76 | -0.04 | stop-loss |
| 2026-10-14T00:50 | Keltner breakout | sell | DOGE-USD | 11.75 | -0.07 | stop-loss |
| 2026-10-14T00:50 | Keltner breakout | sell | BTC-USD | 8.82 | -0.07 | stop-loss |
| 2026-10-14T00:50 | Donchian 55/20 | buy | ETH-USD | 3.23 | — | rebalance up |
| 2026-10-14T00:50 | Donchian 55/20 | sell | XRP-USD | 12.87 | -0.13 | stop-loss |
| 2026-10-14T00:50 | Donchian 55/20 | sell | BTC-USD | 12.89 | -0.11 | stop-loss |
| 2026-10-14T00:50 | ROC + volume | sell | XRP-USD | 17.78 | -0.12 | stop-loss |
| 2026-10-14T00:50 | ROC + volume | sell | DOGE-USD | 17.75 | -0.15 | stop-loss |
| 2026-10-14T00:50 | Ichimoku | sell | BTC-USD | 13.68 | -0.11 | stop-loss |
| 2026-10-14T00:50 | EMA 20/50 cross | buy | ETH-USD | 3.31 | — | rebalance up |
| 2026-10-14T00:50 | EMA 20/50 cross | sell | BTC-USD | 3.31 | -0.02 | rebalance down |
| 2026-10-14T00:45 | EMA 20/50 cross | buy | ETH-USD | 3.33 | — | entry signal |
| 2026-10-14T00:45 | EMA 20/50 cross | sell | DOGE-USD | 3.33 | -0.01 | rebalance down |
| 2026-10-14T00:42 | Keltner breakout | buy | BTC-USD | 2.95 | — | rebalance up |
| 2026-10-14T00:42 | Keltner breakout | sell | XRP-USD | 2.95 | -0.00 | rebalance down |
| 2026-10-14T00:42 | Donchian 55/20 | buy | XRP-USD | 3.25 | — | rebalance up |
| 2026-10-14T00:42 | Donchian 55/20 | sell | SOL-USD | 3.25 | -0.01 | rebalance down |
| 2026-10-14T00:40 | MFI reversion | sell | XRP-USD | 13.31 | 0.03 | exit signal |
| 2026-10-14T00:40 | MFI reversion | sell | ETH-USD | 13.24 | -0.03 | exit signal |
| 2026-10-14T00:40 | Three white soldiers | buy | SOL-USD | 21.67 | — | entry signal |
| 2026-10-14T00:40 | Volume breakout | buy | XRP-USD | 17.03 | — | entry signal |
| 2026-10-14T00:40 | Keltner breakout | buy | BTC-USD | 5.94 | — | entry signal |
| 2026-10-14T00:40 | Keltner breakout | sell | SOL-USD | 2.97 | -0.00 | rebalance down |
| 2026-10-14T00:40 | Keltner breakout | sell | DOGE-USD | 2.95 | -0.00 | rebalance down |
| 2026-10-14T00:40 | Donchian 55/20 | buy | XRP-USD | 9.75 | — | entry signal |
| 2026-10-14T00:40 | Donchian 55/20 | buy | ETH-USD | 12.99 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 00:55:05.000146+00:00 -> 2026-10-14 01:05:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
