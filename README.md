# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T07:35:05.000143+00:00 · 73976 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.44 (-23.56%)

Closed trades 250, win rate 36.0%, fees £6.87, max drawdown -24.09%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 5250 decisions in 1050 calls, $0.0733 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T07:35 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-26T07:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T07:35 | 2 / 3 / 0 | ETH-USD 54% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.45 | +1.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.63 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.08 | 16.08 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.21 | 5.21 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | 0.39 | 0.21 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.46 | 0.55 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.20 | -5.80 | 0 | — | -6.75 | -1.73 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.66 | -6.34 | 24 | 12.5 | -5.35 | -7.76 | -6.57 | 25 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.42 | -6.58 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.26 | -6.74 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.60 | -8.40 | 116 | 24.1 | -7.45 | -4.36 | -10.99 | 34 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.29 | -10.71 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.29 | -3.14 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.85 | -14.15 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.94 | -2.38 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.53 | -16.47 | 77 | 19.5 | -19.32 | -6.54 | -19.85 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 221 | 40.7 | -13.28 | -6.11 | -13.46 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.41 | -5.13 | -23.63 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.84 | -23.16 | 174 | 29.3 | -22.18 | -8.80 | -22.44 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.57 | -24.43 | 210 | 27.6 | -34.23 | -8.23 | -35.47 | 182 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.10 | -25.91 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.51 | -26.49 | 141 | 24.8 | -26.62 | -6.50 | -26.75 | 145 |
| 34 | Ichimoku · 1h | trend | 73.33 | -26.67 | 114 | 15.8 | -29.15 | -7.38 | -29.77 | 96 |
| 35 | Daily: Momentum burst | daily | 71.09 | -28.91 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | ADX DI cross · 1h | trend | 70.09 | -29.91 | 264 | 18.9 | -37.67 | -7.06 | -38.77 | 289 |
| 37 | Hold BTC | benchmark | 70.01 | -29.99 | 3 | 0.0 | -28.48 | -5.00 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.60 | -31.40 | 209 | 22.5 | -30.99 | -7.92 | -31.80 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.93 | -32.07 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.03 | -32.98 | 221 | 17.6 | -40.30 | -7.97 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.73 | -33.27 | 411 | 39.9 | -32.93 | -3.43 | -42.70 | 438 |
| 42 | OBV trend · 1h | momentum | 66.51 | -33.49 | 325 | 19.7 | -42.75 | -10.48 | -42.86 | 230 |
| 43 | EMA 20/50 cross · 1h | trend | 65.87 | -34.13 | 126 | 9.5 | -38.10 | -10.53 | -38.31 | 116 |
| 44 | Triple EMA stack · 1h | trend | 64.82 | -35.18 | 172 | 15.1 | -43.45 | -10.67 | -43.58 | 176 |
| 45 | MACD zero-line · 1h | trend | 63.37 | -36.63 | 202 | 16.3 | -36.81 | -10.18 | -37.43 | 201 |
| 46 | RSI momentum · 1h | momentum | 62.81 | -37.19 | 203 | 14.8 | -42.91 | -9.42 | -43.57 | 192 |
| 47 | MFI reversion · 1h | reversion | 62.73 | -37.27 | 520 | 32.7 | -33.33 | -4.95 | -37.91 | 195 |
| 48 | Donchian 20/10 · 1h | breakout | 61.41 | -38.59 | 183 | 17.5 | -40.95 | -9.04 | -42.84 | 199 |
| 49 | ROC + volume · 1h | momentum | 60.99 | -39.01 | 465 | 26.7 | -40.24 | -7.79 | -41.16 | 336 |
| 50 | Heikin-Ashi · 1h | trend | 60.82 | -39.18 | 553 | 21.9 | -49.46 | -10.11 | -49.96 | 641 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.31 | -41.69 | 314 | 12.1 | -45.00 | -10.29 | -46.31 | 332 |
| 53 | MACD cross · 1h | trend | 57.39 | -42.61 | 492 | 20.3 | -53.88 | -10.88 | -55.70 | 512 |
| 54 | Agent (ML meta-label) | meta | 56.28 | -43.72 | 2074 | 25.4 | -20.56 | -2.62 | -27.14 | 328 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.14 | -8.97 | -55.52 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.76 | -4.96 | -45.50 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.53 | -8.99 | -58.31 | 679 |
| 58 | VWAP momentum · 1h | momentum | 50.93 | -49.07 | 1098 | 21.6 | -61.78 | -13.40 | -62.21 | 1192 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.31 | -9.36 | -59.58 | 607 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -47.96 | -99.16 | 5377 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.63 | -31.50 | -84.23 | 1423 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.40 | -46.61 | -94.43 | 2398 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.22 | -29.77 | -90.82 | 1875 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.42 | -39.31 | -91.63 | 2212 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.62 | -26.93 | -88.62 | 1920 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -46.97 | -98.20 | 3405 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.88 | -51.14 | -96.91 | 3345 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.11 | -35.53 | -93.11 | 2087 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.27 | -35.58 | -82.27 | 1510 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -53.35 | -99.69 | 6280 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.89 | -37.21 | -93.10 | 2470 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.20 | -35.17 | -94.20 | 3133 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -64.33 | -99.82 | 6073 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.96 | -41.87 | -93.18 | 2250 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.78 | -18.77 | -52.27 | 662 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.95 | -23.45 | -78.34 | 1605 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -56.99 | -97.73 | 3236 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -58.64 | -99.19 | 5118 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.14 | -23.21 | -70.48 | 1194 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -46.38 | -94.64 | 2649 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.44 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.28 | -33.92 | -84.52 | 1644 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -68.79 | -99.77 | 6524 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.56 | -30.70 | -91.88 | 2496 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.85 | -19.99 | -83.37 | 1969 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.52 | -31.89 | -91.85 | 2155 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -47.89 | -98.23 | 4051 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.35 | -46.30 | -90.69 | 2193 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.35 | -29.78 | -68.35 | 781 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.50 | -27.64 | -72.58 | 1148 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.71 | -19.08 | -85.01 | 1822 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -48.73 | -98.10 | 4400 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.69 | -99.94 | 8289 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -45.99 | -6.74 | -52.52 | 290 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T07:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 19.99 | — | entry signal |
| 2026-11-26T07:00 | Three white soldiers · 1h | sell | DOGE-USD | 18.80 | 0.21 | exit signal |
| 2026-11-26T07:00 | Volume breakout · 1h | sell | DOGE-USD | 19.21 | 0.08 | exit signal |
| 2026-11-26T07:00 | VWAP momentum · 1h | sell | XRP-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | XRP-USD | 2.40 | -0.03 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | SOL-USD | 2.43 | -0.00 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | BTC-USD | 2.43 | -0.01 | exit signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | buy | ETH-USD | 5.33 | — | entry signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | sell | DOGE-USD | 5.33 | -0.06 | rebalance down |
| 2026-11-26T06:25 | VWAP momentum · 1h | sell | DOGE-USD | 2.11 | -0.01 | target is flat |
| 2026-11-26T06:25 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.42 | -0.01 | target is flat |
| 2026-11-26T06:20 | VWAP momentum · 1h | buy | DOGE-USD | 2.12 | — | entry |
| 2026-11-26T06:20 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.43 | — | entry |
| 2026-11-26T06:05 | VWAP momentum · 1h | sell | DOGE-USD | 1.95 | -0.02 | target is flat |
| 2026-11-26T06:05 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.44 | 0.01 | target is flat |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | SOL-USD | 1.94 | -0.02 | exit signal |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | BTC-USD | 1.95 | -0.02 | exit signal |
| 2026-11-26T05:00 | MFI reversion · 1h | sell | SOL-USD | 4.81 | 0.18 | exit signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | SOL-USD | 6.49 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | sell | XRP-USD | 3.30 | 0.00 | rebalance down |
| 2026-11-26T04:00 | VWAP momentum · 1h | sell | SOL-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.44 | — | entry signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | sell | ETH-USD | 2.43 | -0.01 | exit signal |
| 2026-11-26T04:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 3.75 | — | entry signal |
| 2026-11-26T04:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 3.75 | -0.01 | rebalance down |
| 2026-11-26T03:00 | MFI reversion · 1h | sell | BTC-USD | 5.16 | 0.15 | exit signal |
| 2026-11-26T03:00 | VWAP momentum · 1h | sell | BTC-USD | 1.95 | -0.02 | exit signal |
| 2026-11-26T02:20 | ROC + volume · 1h | buy | DOGE-USD | 3.34 | — | rebalance up |
| 2026-11-26T02:20 | ROC + volume · 1h | buy | BTC-USD | 3.37 | — | rebalance up |
| 2026-11-26T02:00 | Keltner breakout · 1h | buy | XRP-USD | 18.40 | — | entry signal |
| 2026-11-26T02:00 | Keltner breakout · 1h | buy | DOGE-USD | 18.40 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | XRP-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T02:00 | Triple EMA stack · 1h | buy | XRP-USD | 16.27 | — | entry signal |
| 2026-11-26T02:00 | Triple EMA stack · 1h | buy | DOGE-USD | 16.27 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 07:35:05.000143+00:00 -> 2026-11-26 07:45:05.000143+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
