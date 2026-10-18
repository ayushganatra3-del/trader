# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T12:55:05.000181+00:00 · 27211 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 9888 decisions in 1980 calls, $0.1382 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T12:55 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-18T12:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T12:55 | 3 / 2 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 2.34 | +2.45% | 9 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| VWAP reversion | ETHU | 1.80 | +2.34% | 5 |
| VWAP momentum · 1h | SQQQ | 1.77 | +10.81% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.15 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.39 | -3.30 | -13.80 | 134 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 0.65 | 0.28 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.37 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 97.22 | -2.78 | 0 | — | 28.36 | 3.36 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -5.04 | -2.59 | -6.37 | 285 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -19.52 | -5.88 | -19.70 | 140 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.58 | -5.42 | 82 | 19.5 | -8.30 | -1.47 | -13.33 | 252 |
| 24 | Squeeze breakout · 1h | breakout | 93.63 | -6.37 | 41 | 24.4 | 4.35 | 0.96 | -9.46 | 98 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -9.90 | -1.53 | -22.55 | 270 |
| 28 | EMA 20/50 cross · 1h | trend | 92.81 | -7.19 | 54 | 14.8 | -18.09 | -3.11 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.92 | -2.04 | -8.74 | 116 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.42 | -6.33 | -13.56 | 238 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.58 | -0.07 | -14.55 | 114 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.07 | -8.93 | 76 | 17.1 | -16.83 | -2.93 | -27.38 | 216 |
| 34 | Bollinger breakout · 1h | breakout | 90.73 | -9.27 | 83 | 28.9 | 6.80 | 1.06 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.30 | -9.70 | 80 | 16.2 | -12.79 | -1.36 | -33.23 | 229 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.38 | -17.98 | 112 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Supertrend · 1h | trend | 89.18 | -10.82 | 84 | 11.9 | -8.37 | -0.96 | -28.73 | 211 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.15 | -0.99 | -27.05 | 203 |
| 42 | MACD cross · 1h | trend | 88.14 | -11.87 | 177 | 22.0 | -15.34 | -1.97 | -29.77 | 459 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -24.91 | -7.65 | -25.57 | 231 |
| 44 | OBV trend · 1h | momentum | 87.88 | -12.12 | 169 | 18.3 | -8.99 | -0.76 | -34.04 | 317 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.55 | -13.45 | 143 | 44.1 | -21.11 | -3.87 | -22.11 | 366 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.69 | -14.30 | 81 | 16.0 | -22.07 | -4.29 | -23.77 | 216 |
| 49 | Donchian 20/10 · 1h | breakout | 84.92 | -15.08 | 78 | 17.9 | 2.12 | 0.46 | -21.63 | 213 |
| 50 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 205 | 30.2 | -20.92 | -3.45 | -21.51 | 142 |
| 51 | Three white soldiers | momentum | 83.56 | -16.44 | 216 | 18.5 | -47.51 | -19.54 | -47.79 | 602 |
| 52 | Z-score reversion · 1h | reversion | 83.31 | -16.69 | 86 | 31.4 | -15.77 | -2.75 | -20.30 | 185 |
| 53 | ROC + volume · 1h | momentum | 82.88 | -17.12 | 192 | 21.4 | -12.38 | -1.62 | -27.07 | 395 |
| 54 | Agent (ML meta-label) | meta | 82.34 | -17.66 | 652 | 18.1 | -14.84 | -2.20 | -23.30 | 392 |
| 55 | EMA 9/21 cross · 1h | trend | 81.58 | -18.41 | 129 | 11.6 | -5.75 | -0.44 | -29.84 | 314 |
| 56 | VWAP momentum · 1h | momentum | 81.02 | -18.98 | 403 | 20.3 | -37.08 | -5.66 | -45.93 | 1257 |
| 57 | Heikin-Ashi · 1h | trend | 81.02 | -18.98 | 205 | 22.4 | -32.37 | -5.32 | -42.15 | 678 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.81 | -36.60 | 531 |
| 59 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.53 | -2.59 | -21.70 | 162 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 146 | 31.5 | -30.69 | -6.39 | -32.71 | 348 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.04 | -2.61 | -26.62 | 426 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.15 | -6.53 | -36.84 | 538 |
| 63 | Volume breakout | breakout | 62.76 | -37.24 | 335 | 12.8 | -63.24 | -18.36 | -63.59 | 879 |
| 64 | ROC + volume | momentum | 62.11 | -37.89 | 560 | 21.6 | -75.89 | -17.86 | -77.78 | 1723 |
| 65 | Squeeze breakout | breakout | 61.75 | -38.25 | 444 | 14.4 | -62.96 | -18.04 | -64.76 | 1215 |
| 66 | RSI(14) reversion | reversion | 60.55 | -39.45 | 671 | 25.5 | -73.97 | -16.45 | -74.07 | 1622 |
| 67 | Donchian 55/20 | breakout | 59.13 | -40.87 | 455 | 17.1 | -69.24 | -14.75 | -72.67 | 1282 |
| 68 | EMA 20/50 cross | trend | 57.00 | -43.00 | 478 | 18.4 | -77.05 | -15.32 | -80.01 | 1442 |
| 69 | VWAP reversion | reversion | 54.46 | -45.54 | 703 | 23.8 | -73.11 | -15.51 | -73.33 | 1511 |
| 70 | Keltner breakout | breakout | 52.35 | -47.65 | 633 | 15.5 | -83.21 | -27.50 | -83.22 | 1826 |
| 71 | AI bee: Boozy | ai | 52.17 | -47.83 | 333 | 6.0 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.38 | -98.64 | 5328 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.64 | -31.31 | -93.64 | 2601 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.59 | -20.58 | -87.66 | 1912 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -25.08 | -90.85 | 2364 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.21 | -26.69 | -91.22 | 2302 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -33.19 | -97.47 | 3526 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -37.78 | -96.81 | 3627 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.29 | -28.27 | -94.53 | 2590 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.18 | -23.76 | -82.51 | 1735 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.48 | -99.39 | 5820 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.33 | -26.22 | -91.53 | 2643 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -32.28 | -96.11 | 3525 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.27 | -99.74 | 6239 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.71 | -29.67 | -91.73 | 2365 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -39.79 | -97.52 | 3664 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.43 | -98.48 | 4768 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.77 | -34.21 | -93.77 | 2812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.34 | -99.53 | 6245 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.62 | -22.26 | -86.63 | 2166 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.05 | -27.52 | -88.08 | 2164 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -33.10 | -95.87 | 3812 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -33.94 | -89.22 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -34.47 | -95.80 | 4156 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.71 | -99.89 | 8312 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T12:35 | Three white soldiers | sell | DOGE-USD | 20.79 | -0.13 | exit signal |
| 2026-10-18T12:35 | EMA 20/50 cross | sell | ETH-USD | 14.21 | -0.12 | exit signal |
| 2026-10-18T12:20 | AI bee: Boozy | sell | ETH-USD | 15.11 | -0.11 | Jev: sell (sell p=0.57) after 16 min |
| 2026-10-18T12:04 | AI bee: Boozy | buy | ETH-USD | 15.22 | — | Jev: buy (buy p=0.71) |
| 2026-10-18T12:00 | VWAP momentum · 1h | buy | DOGE-USD | 2.83 | — | entry signal |
| 2026-10-18T12:00 | Triple EMA stack · 1h | buy | BTC-USD | 22.60 | — | entry signal |
| 2026-10-18T12:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 20.42 | — | entry signal |
| 2026-10-18T12:00 | Three white soldiers | buy | DOGE-USD | 20.92 | — | entry signal |
| 2026-10-18T11:50 | Donchian 55/20 | sell | SOL-USD | 11.82 | -0.12 | exit signal |
| 2026-10-18T11:50 | Donchian 55/20 | sell | BTC-USD | 11.86 | -0.07 | exit signal |
| 2026-10-18T11:35 | Donchian 55/20 | sell | ETH-USD | 14.78 | -0.12 | stop-loss |
| 2026-10-18T11:10 | Donchian 55/20 | buy | ETH-USD | 2.97 | — | rebalance up |
| 2026-10-18T11:10 | Donchian 55/20 | sell | XRP-USD | 11.81 | -0.13 | stop-loss |
| 2026-10-18T11:10 | Donchian 55/20 | sell | DOGE-USD | 11.82 | -0.11 | stop-loss |
| 2026-10-18T11:10 | EMA 20/50 cross | buy | ETH-USD | 2.86 | — | rebalance up |
| 2026-10-18T11:10 | EMA 20/50 cross | sell | XRP-USD | 11.37 | -0.12 | stop-loss |
| 2026-10-18T11:10 | EMA 20/50 cross | sell | DOGE-USD | 11.38 | -0.11 | stop-loss |
| 2026-10-18T11:05 | VWAP momentum · 1h | buy | XRP-USD | 10.64 | — | rebalance up |
| 2026-10-18T11:05 | VWAP momentum · 1h | sell | DOGE-USD | 13.46 | -0.10 | target is flat |
| 2026-10-18T11:00 | OBV trend · 1h | buy | BTC-USD | 21.99 | — | entry signal |
| 2026-10-18T11:00 | Heikin-Ashi · 1h | buy | BTC-USD | 20.28 | — | entry signal |
| 2026-10-18T11:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 23.23 | — | entry signal |
| 2026-10-18T11:00 | Keltner breakout | sell | SOL-USD | 10.49 | -0.05 | exit signal |
| 2026-10-18T11:00 | Keltner breakout | sell | BTC-USD | 10.50 | -0.05 | exit signal |
| 2026-10-18T10:55 | Keltner breakout | sell | DOGE-USD | 10.49 | -0.06 | target is flat |
| 2026-10-18T10:50 | Agent (ML meta-label) | sell | XRP-USD | 4.31 | -0.03 | selected signal exited |
| 2026-10-18T10:50 | Squeeze breakout | sell | SOL-USD | 15.40 | -0.07 | exit signal |
| 2026-10-18T10:50 | Squeeze breakout | sell | BTC-USD | 15.44 | -0.03 | exit signal |
| 2026-10-18T10:50 | Keltner breakout | sell | ETH-USD | 10.47 | -0.08 | stop-loss |
| 2026-10-18T10:45 | AI bee: Boozy | sell | ETH-USD | 15.22 | -0.11 | Jev: sell |
| 2026-10-18T10:45 | Agent (ML meta-label) | buy | XRP-USD | 4.34 | — | entry |
| 2026-10-18T10:40 | Agent (ML meta-label) | sell | XRP-USD | 4.30 | -0.03 | selected signal exited |
| 2026-10-18T10:40 | Volume breakout | sell | BTC-USD | 15.69 | -0.06 | exit signal |
| 2026-10-18T10:40 | Squeeze breakout | sell | ETH-USD | 15.43 | -0.04 | exit signal |
| 2026-10-18T10:40 | ROC + volume | sell | SOL-USD | 15.49 | -0.08 | exit signal |
| 2026-10-18T10:35 | Agent (ML meta-label) | buy | XRP-USD | 4.34 | — | entry |
| 2026-10-18T10:35 | ROC + volume | sell | XRP-USD | 15.50 | -0.10 | exit signal |
| 2026-10-18T10:35 | ROC + volume | sell | DOGE-USD | 15.49 | -0.11 | exit signal |
| 2026-10-18T10:29 | AI bee: Boozy | buy | ETH-USD | 15.33 | — | Jev: buy (buy p=0.71) |
| 2026-10-18T10:26 | Agent (ML meta-label) | sell | XRP-USD | 5.11 | -0.03 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 12:55:05.000181+00:00 -> 2026-10-18 13:05:05.000181+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
