# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-07T04:50:05.000136+00:00 · 50467 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.16 (-11.84%)

Closed trades 152, win rate 36.8%, fees £4.42, max drawdown -12.25%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 3612 decisions in 723 calls, $0.0504 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-07T04:50 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-07T04:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-07T04:50 | 2 / 3 / 0 | ETH-USD 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI(14) reversion | SQQQ | 2.31 | +7.36% | 4 |
| Z-score reversion | SQQQ | 1.94 | +4.38% | 7 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Candlestick reversal · 1h | DOGE-USD | 1.92 | +7.45% | 7 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.16 | -0.84 | 122 | 47.5 | -12.80 | -3.01 | -14.47 | 151 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -6.89 | -3.99 | -10.36 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.58 | -0.44 | -9.18 | 229 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.11 | -0.97 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.74 | -5.72 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.48 | -5.32 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.35 | -4.49 | -26.04 | 65 |
| 23 | Daily: Bullish score | daily | 88.76 | -11.23 | 15 | 20.0 | -5.00 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.54 | -3.67 | -14.68 | 86 |
| 25 | Hold BTC | benchmark | 88.54 | -11.46 | 1 | 0.0 | -5.57 | -0.74 | -14.09 | 1 |
| 26 | Agent | meta | 88.16 | -11.84 | 152 | 36.8 | -13.93 | -7.48 | -14.05 | 201 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -14.21 | -3.15 | -20.50 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 85.95 | -14.05 | 71 | 14.1 | -13.28 | -2.72 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.37 | -5.50 | -18.65 | 96 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.05 | -17.95 | 261 | 46.7 | -26.12 | -3.88 | -29.25 | 394 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.78 | -3.80 | -21.73 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.62 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.37 | -20.63 | 175 | 18.3 | -24.33 | -4.07 | -27.04 | 261 |
| 38 | MFI reversion · 1h | reversion | 78.46 | -21.54 | 337 | 34.1 | -19.54 | -2.85 | -20.96 | 157 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.89 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.49 | -22.51 | 168 | 23.2 | -23.64 | -4.93 | -27.32 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.66 | -23.34 | 289 | 45.7 | -31.20 | -5.16 | -31.78 | 465 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -23.33 | -4.23 | -30.58 | 130 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -43.09 | -9.17 | -43.54 | 678 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.31 | -5.47 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -28.95 | -6.14 | -33.48 | 203 |
| 46 | Supertrend · 1h | trend | 73.63 | -26.37 | 166 | 13.3 | -30.10 | -5.24 | -34.80 | 216 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -28.08 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.13 | -26.86 | 336 | 22.9 | -36.36 | -6.48 | -38.81 | 484 |
| 49 | Z-score reversion · 1h | reversion | 73.00 | -27.00 | 163 | 35.6 | -25.45 | -3.80 | -28.10 | 233 |
| 50 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 251 | 40.2 | -31.28 | -5.37 | -34.52 | 372 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -37.85 | -6.16 | -39.68 | 534 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.92 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.59 | -28.41 | 140 | 20.0 | -29.79 | -5.51 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.23 | -6.21 | -33.83 | 284 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -38.11 | -7.47 | -38.33 | 382 |
| 56 | EMA 9/21 cross · 1h | trend | 67.31 | -32.69 | 242 | 9.9 | -39.57 | -8.20 | -39.72 | 334 |
| 57 | VWAP momentum · 1h | momentum | 66.98 | -33.02 | 781 | 22.0 | -55.75 | -12.34 | -55.90 | 1237 |
| 58 | Agent (ML meta-label) | meta | 66.34 | -33.66 | 1540 | 23.0 | -9.90 | -1.54 | -20.19 | 349 |
| 59 | RSI(14) reversion · 1h | reversion | 66.23 | -33.77 | 143 | 27.3 | -28.92 | -4.54 | -31.54 | 218 |
| 60 | Candlestick reversal · 1h | reversion | 65.41 | -34.59 | 409 | 28.6 | -38.01 | -7.01 | -38.39 | 570 |
| 61 | Three white soldiers | momentum | 64.95 | -35.05 | 465 | 15.7 | -48.64 | -22.88 | -48.68 | 644 |
| 62 | Max aggression: 1-day momentum | meta | 62.24 | -37.76 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -45.35 | -98.94 | 5218 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.84 | -25.31 | -80.84 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -45.53 | -93.51 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.24 | -31.30 | -89.25 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.84 | -38.75 | -90.85 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.23 | -32.39 | -90.24 | 2195 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -51.98 | -97.73 | 3478 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -54.63 | -96.31 | 3393 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -33.44 | -93.71 | 2439 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.51 | -34.83 | -82.51 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.51 | -99.52 | 5992 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -42.69 | -92.70 | 2603 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.73 | -38.10 | -95.73 | 3416 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.78 | -99.81 | 6201 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -41.91 | -91.93 | 2280 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.19 | -25.36 | -76.21 | 1578 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -61.48 | -97.76 | 3514 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.79 | -59.66 | -98.79 | 4887 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.86 | -28.89 | -69.91 | 1203 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -52.60 | -94.69 | 2746 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.99 | -37.05 | -85.01 | 1765 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -71.04 | -99.65 | 6384 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.27 | -31.22 | -89.27 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.94 | -19.57 | -77.94 | 1750 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.29 | -37.61 | -91.29 | 2240 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.63 | -51.94 | -96.63 | 3885 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -53.26 | -89.51 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.91 | -28.26 | -65.91 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.56 | -24.15 | -73.56 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.71 | -18.21 | -78.71 | 1673 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -48.80 | -97.28 | 4334 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -101.68 | -99.93 | 8306 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-07T04:05 | Three white soldiers | sell | SOL-USD | 16.16 | -0.10 | exit signal |
| 2026-11-07T04:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.00 | -0.04 | exit signal |
| 2026-11-07T04:00 | VWAP momentum · 1h | buy | ETH-USD | 4.95 | — | rebalance up |
| 2026-11-07T04:00 | VWAP momentum · 1h | sell | SOL-USD | 6.66 | -0.05 | exit signal |
| 2026-11-07T04:00 | VWAP momentum · 1h | sell | BTC-USD | 5.55 | -0.04 | exit signal |
| 2026-11-07T04:00 | Three white soldiers | buy | SOL-USD | 16.26 | — | entry signal |
| 2026-11-07T03:35 | CCI reversion · 1h | sell | XRP-USD | 3.93 | -0.11 | stop-loss |
| 2026-11-07T03:35 | Stochastic reversion · 1h | sell | XRP-USD | 2.32 | -0.06 | stop-loss |
| 2026-11-07T03:35 | VWAP reversion · 1h | sell | XRP-USD | 24.26 | -0.71 | stop-loss |
| 2026-11-07T03:20 | Z-score reversion · 1h | sell | XRP-USD | 4.18 | -0.10 | stop-loss |
| 2026-11-07T03:00 | Agent | sell | DOGE-USD | 17.52 | -0.14 | selected signal exited |
| 2026-11-07T02:35 | MFI reversion · 1h | sell | XRP-USD | 7.09 | -0.19 | stop-loss |
| 2026-11-07T02:35 | MACD cross · 1h | sell | XRP-USD | 6.53 | -0.19 | stop-loss |
| 2026-11-07T02:25 | Three white soldiers | sell | SOL-USD | 16.18 | -0.11 | exit signal |
| 2026-11-07T02:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.04 | — | entry |
| 2026-11-07T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.42 | 0.00 | exit signal |
| 2026-11-07T02:00 | Bollinger breakout · 1h | buy | ETH-USD | 19.40 | — | entry signal |
| 2026-11-07T02:00 | VWAP momentum · 1h | buy | ETH-USD | 2.51 | — | entry signal |
| 2026-11-07T02:00 | VWAP momentum · 1h | buy | BTC-USD | 5.59 | — | entry signal |
| 2026-11-07T02:00 | Three white soldiers | buy | SOL-USD | 16.29 | — | entry signal |
| 2026-11-07T01:00 | Agent | buy | DOGE-USD | 17.66 | — | following Candlestick reversal · 1h |
| 2026-11-07T01:00 | CCI reversion · 1h | buy | XRP-USD | 4.04 | — | entry signal |
| 2026-11-07T01:00 | VWAP momentum · 1h | buy | SOL-USD | 6.72 | — | entry signal |
| 2026-11-07T01:00 | VWAP momentum · 1h | sell | ETH-USD | 6.08 | -0.03 | exit signal |
| 2026-11-07T01:00 | VWAP momentum · 1h | sell | BTC-USD | 7.44 | -0.02 | exit signal |
| 2026-11-07T00:51 | Agent (ML meta-label) | sell | BTC-USD | 3.88 | -0.02 | selected signal exited |
| 2026-11-07T00:45 | Agent (ML meta-label) | buy | BTC-USD | 3.90 | — | entry |
| 2026-11-07T00:30 | Three white soldiers | sell | ETH-USD | 16.21 | -0.11 | exit signal |
| 2026-11-07T00:21 | Agent (ML meta-label) | sell | BTC-USD | 4.02 | -0.02 | selected signal exited |
| 2026-11-07T00:15 | Three white soldiers | buy | ETH-USD | 16.32 | — | entry signal |
| 2026-11-07T00:10 | Agent (ML meta-label) | buy | BTC-USD | 4.05 | — | entry |
| 2026-11-07T00:05 | Agent (ML meta-label) | sell | BTC-USD | 3.88 | -0.02 | selected signal exited |
| 2026-11-07T00:00 | ROC + volume · 1h | sell | DOGE-USD | 17.40 | -0.22 | exit signal |
| 2026-11-07T00:00 | Three white soldiers | sell | ETH-USD | 16.25 | -0.11 | exit signal |
| 2026-11-06T23:55 | Three white soldiers | sell | XRP-USD | 16.26 | -0.12 | exit signal |
| 2026-11-06T23:35 | Three white soldiers | buy | ETH-USD | 16.36 | — | entry signal |
| 2026-11-06T23:20 | Three white soldiers | buy | XRP-USD | 16.37 | — | entry signal |
| 2026-11-06T23:00 | Agent (ML meta-label) | buy | BTC-USD | 3.91 | — | entry |
| 2026-11-06T23:00 | Agent (ML meta-label) | sell | DOGE-USD | 3.88 | -0.03 | selected signal exited |
| 2026-11-06T23:00 | CCI reversion · 1h | sell | ETH-USD | 5.15 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-09 04:50:05.000136+00:00 -> 2026-11-07 05:00:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-09 04:50:05.000136+00:00 -> 2026-11-07 05:00:05.000136+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-09 04:50:05.000136+00:00 -> 2026-11-07 05:00:05.000136+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
