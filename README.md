# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T13:00:05.000136+00:00 · 54613 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.80 (-13.20%)

Closed trades 163, win rate 35.0%, fees £4.99, max drawdown -13.60%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 9926 decisions in 1987 calls, $0.1389 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T13:00 | 3 / 2 / 0 | ETH-USD 17% |  |
| Breezy | 2026-11-10T13:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-10T13:00 | 4 / 1 / 0 | ETH-USD 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| VWAP momentum | TSLA | 1.44 | +2.06% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 18.87 | 3.78 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.47 | 12.47 | 0 | — | 13.79 | 4.66 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.93 | 11.93 | 31 | 29.0 | 20.12 | 3.01 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.55 | 1.55 | 126 | 36.5 | 10.08 | 3.80 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.24 | 1.24 | 0 | — | 4.81 | 1.38 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.02 | 1.02 | 7 | 42.9 | -0.93 | 0.19 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.67 | 1.09 | -9.06 | 239 |
| 11 | Agent (rotation) | meta | 98.14 | -1.86 | 177 | 28.2 | -3.44 | -1.36 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.08 | -2.92 | 132 | 47.0 | -11.99 | -3.06 | -12.16 | 151 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.53 | -3.47 | 0 | — | -1.49 | -0.45 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.93 | -5.07 | 0 | — | -3.54 | -0.88 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.84 | -7.16 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.58 | -7.42 | 108 | 23.1 | -13.74 | -5.12 | -17.96 | 79 |
| 20 | Copy: Insider buying | copy | 92.11 | -7.88 | 42 | 38.1 | -8.47 | -1.75 | -15.11 | 66 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 90.34 | -9.66 | 391 | 34.3 | -13.39 | -4.24 | -15.24 | 595 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.56 | -3.42 | -14.68 | 80 |
| 24 | Agent | meta | 86.80 | -13.20 | 163 | 35.0 | -13.62 | -7.01 | -14.09 | 203 |
| 25 | Hold BTC | benchmark | 86.36 | -13.64 | 1 | 0.0 | -6.28 | -0.83 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.11 | -13.89 | 15 | 20.0 | -10.31 | -1.57 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.62 | -14.38 | 167 | 26.9 | -10.83 | -1.93 | -21.29 | 225 |
| 28 | Agent (aggressive) | meta | 83.88 | -16.12 | 76 | 31.6 | -16.53 | -4.71 | -18.49 | 94 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 83.80 | -16.20 | 2 | 0.0 | -7.65 | -0.84 | -24.16 | 1 |
| 30 | Opening range 15m | breakout | 83.50 | -16.50 | 481 | 32.4 | -18.38 | -5.20 | -19.91 | 728 |
| 31 | Donchian 55/20 · 1h | breakout | 83.41 | -16.59 | 71 | 14.1 | -17.54 | -3.81 | -22.45 | 103 |
| 32 | Stochastic reversion · 1h | reversion | 83.25 | -16.75 | 279 | 48.4 | -23.18 | -3.41 | -27.06 | 387 |
| 33 | Keltner breakout · 1h | breakout | 82.02 | -17.98 | 107 | 23.4 | -22.13 | -4.45 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.32 | -18.68 | 145 | 27.6 | -14.82 | -3.34 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.60 | -19.40 | 205 | 40.0 | -19.67 | -6.55 | -19.99 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 79.83 | -20.17 | 401 | 22.7 | -39.78 | -7.37 | -43.08 | 675 |
| 37 | ADX DI cross · 1h | trend | 79.40 | -20.60 | 179 | 18.4 | -23.05 | -3.96 | -28.34 | 278 |
| 38 | Max aggression: 5-day momentum | meta | 79.24 | -20.76 | 18 | 44.4 | -39.47 | -2.63 | -45.81 | 25 |
| 39 | MFI reversion · 1h | reversion | 78.90 | -21.10 | 353 | 34.3 | -17.08 | -2.19 | -21.23 | 166 |
| 40 | CCI reversion · 1h | reversion | 78.59 | -21.41 | 321 | 45.8 | -22.00 | -3.35 | -30.29 | 456 |
| 41 | Ichimoku · 1h | trend | 77.13 | -22.87 | 96 | 15.6 | -29.76 | -8.45 | -29.87 | 120 |
| 42 | Bollinger breakout · 1h | breakout | 76.81 | -23.19 | 170 | 22.9 | -22.64 | -4.72 | -27.92 | 240 |
| 43 | Bollinger reversion · 1h | reversion | 75.38 | -24.62 | 272 | 41.2 | -23.48 | -3.55 | -32.06 | 371 |
| 44 | MACD cross · 1h | trend | 74.93 | -25.07 | 355 | 22.3 | -32.46 | -5.31 | -39.46 | 481 |
| 45 | Z-score reversion · 1h | reversion | 74.84 | -25.16 | 180 | 37.2 | -21.74 | -3.14 | -27.66 | 227 |
| 46 | MACD zero-line · 1h | trend | 74.46 | -25.54 | 157 | 16.6 | -25.03 | -5.12 | -29.25 | 215 |
| 47 | Williams %R · 1h | reversion | 74.23 | -25.77 | 339 | 46.6 | -35.46 | -5.74 | -37.86 | 543 |
| 48 | EMA 20/50 cross · 1h | trend | 74.14 | -25.86 | 102 | 10.8 | -23.70 | -4.21 | -32.62 | 126 |
| 49 | Supertrend · 1h | trend | 73.35 | -26.65 | 167 | 13.2 | -29.08 | -4.99 | -34.92 | 226 |
| 50 | RSI momentum · 1h | momentum | 73.03 | -26.97 | 159 | 12.6 | -24.29 | -3.86 | -33.01 | 217 |
| 51 | Triple EMA stack · 1h | trend | 72.46 | -27.54 | 143 | 14.7 | -26.11 | -4.52 | -34.87 | 203 |
| 52 | ROC + volume · 1h | momentum | 71.81 | -28.19 | 349 | 25.5 | -35.91 | -6.67 | -38.89 | 380 |
| 53 | OBV trend · 1h | momentum | 71.70 | -28.30 | 274 | 18.2 | -27.05 | -4.99 | -34.09 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.43 | -29.57 | 142 | 19.7 | -29.92 | -5.50 | -35.64 | 207 |
| 55 | Daily: Momentum burst | daily | 70.38 | -29.62 | 26 | 11.5 | -39.31 | -5.63 | -39.66 | 31 |
| 56 | Max aggression: 1-day momentum | meta | 68.35 | -31.65 | 27 | 25.9 | -31.45 | -1.58 | -57.50 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 68.15 | -31.85 | 163 | 31.3 | -30.20 | -4.45 | -33.86 | 247 |
| 58 | VWAP momentum · 1h | momentum | 67.53 | -32.47 | 815 | 21.5 | -51.77 | -11.05 | -53.43 | 1236 |
| 59 | Agent (ML meta-label) | meta | 67.42 | -32.58 | 1637 | 24.1 | -8.95 | -1.43 | -18.20 | 334 |
| 60 | EMA 9/21 cross · 1h | trend | 65.50 | -34.50 | 249 | 9.6 | -38.89 | -7.67 | -40.15 | 337 |
| 61 | Candlestick reversal · 1h | reversion | 64.08 | -35.92 | 440 | 28.2 | -36.71 | -6.67 | -37.79 | 592 |
| 62 | Three white soldiers | momentum | 61.45 | -38.55 | 501 | 15.0 | -48.86 | -22.89 | -48.90 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -45.62 | -98.95 | 5253 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.79 | -26.07 | -79.79 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.11 | -44.46 | -93.11 | 2509 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.10 | -31.53 | -89.11 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.58 | -38.43 | -90.58 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.12 | -31.09 | -90.17 | 2200 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -53.01 | -97.70 | 3462 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -55.20 | -96.27 | 3430 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -31.80 | -93.83 | 2433 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.19 | -33.90 | -82.19 | 1675 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -55.85 | -99.55 | 5997 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.21 | -42.49 | -92.22 | 2600 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -36.29 | -95.51 | 3410 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.69 | -99.80 | 6172 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -42.79 | -91.83 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.90 | -23.86 | -75.11 | 1589 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -59.15 | -97.70 | 3523 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.87 | -62.92 | -98.87 | 4891 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.55 | -26.85 | -69.01 | 1217 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -52.42 | -94.51 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.23 | -35.32 | -84.25 | 1767 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -73.32 | -99.65 | 6370 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.90 | -32.78 | -89.93 | 2284 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.49 | -20.11 | -78.51 | 1747 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -36.86 | -90.60 | 2211 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.79 | -52.05 | -96.79 | 3883 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.18 | -55.82 | -89.18 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.71 | -27.59 | -66.38 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -70.78 | -22.40 | -71.23 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.32 | -19.38 | -80.39 | 1700 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -49.27 | -97.28 | 4313 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -109.66 | -99.93 | 8320 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T13:00 | VWAP reversion · 1h | buy | XRP-USD | 24.29 | — | entry signal |
| 2026-11-10T13:00 | Bollinger reversion · 1h | buy | XRP-USD | 11.38 | — | entry signal |
| 2026-11-10T13:00 | Bollinger reversion · 1h | buy | SOL-USD | 15.11 | — | entry signal |
| 2026-11-10T13:00 | Bollinger reversion · 1h | buy | ETH-USD | 15.11 | — | entry signal |
| 2026-11-10T13:00 | Bollinger reversion · 1h | buy | DOGE-USD | 15.11 | — | entry signal |
| 2026-11-10T13:00 | Candlestick reversal · 1h | buy | ETH-USD | 10.69 | — | entry signal |
| 2026-11-10T13:00 | Candlestick reversal · 1h | buy | BTC-USD | 10.69 | — | entry signal |
| 2026-11-10T13:00 | Candlestick reversal · 1h | sell | XRP-USD | 5.21 | -0.07 | rebalance down |
| 2026-11-10T12:40 | Agent (ML meta-label) | sell | ETH-USD | 7.37 | -0.22 | selected signal exited |
| 2026-11-10T12:40 | MFI reversion · 1h | sell | ETH-USD | 12.92 | -0.38 | stop-loss |
| 2026-11-10T12:40 | Williams %R · 1h | buy | BTC-USD | 12.21 | — | entry |
| 2026-11-10T12:40 | Williams %R · 1h | sell | ETH-USD | 12.21 | -0.26 | stop-loss |
| 2026-11-10T12:00 | VWAP reversion · 1h | buy | SOL-USD | 24.29 | — | entry signal |
| 2026-11-10T12:00 | VWAP reversion · 1h | buy | ETH-USD | 24.29 | — | entry signal |
| 2026-11-10T12:00 | Z-score reversion · 1h | buy | SOL-USD | 8.31 | — | entry signal |
| 2026-11-10T12:00 | Bollinger reversion · 1h | buy | BTC-USD | 18.90 | — | entry signal |
| 2026-11-10T12:00 | RSI(14) reversion · 1h | buy | SOL-USD | 9.73 | — | entry signal |
| 2026-11-10T11:00 | Williams %R · 1h | buy | XRP-USD | 12.32 | — | entry |
| 2026-11-10T11:00 | Williams %R · 1h | sell | SOL-USD | 12.19 | -0.29 | stop-loss |
| 2026-11-10T11:00 | MACD cross · 1h | sell | XRP-USD | 4.42 | -0.10 | exit signal |
| 2026-11-10T11:00 | MACD cross · 1h | sell | ETH-USD | 5.05 | -0.11 | exit signal |
| 2026-11-10T11:00 | MACD cross · 1h | sell | DOGE-USD | 5.10 | -0.07 | exit signal |
| 2026-11-10T11:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 4.03 | -0.06 | exit signal |
| 2026-11-10T10:35 | CCI reversion · 1h | sell | SOL-USD | 11.01 | -0.32 | stop-loss |
| 2026-11-10T10:35 | Z-score reversion · 1h | sell | SOL-USD | 8.16 | -0.27 | stop-loss |
| 2026-11-10T10:35 | RSI(14) reversion · 1h | buy | ETH-USD | 3.95 | — | rebalance up |
| 2026-11-10T10:35 | RSI(14) reversion · 1h | sell | SOL-USD | 7.34 | -0.24 | stop-loss |
| 2026-11-10T10:00 | Candlestick reversal · 1h | buy | XRP-USD | 16.08 | — | entry signal |
| 2026-11-10T10:00 | Candlestick reversal · 1h | sell | ETH-USD | 16.03 | -0.18 | exit signal |
| 2026-11-10T10:00 | MACD cross · 1h | sell | SOL-USD | 3.53 | -0.05 | exit signal |
| 2026-11-10T09:05 | Candlestick reversal · 1h | buy | ETH-USD | 3.29 | — | rebalance up |
| 2026-11-10T09:05 | Candlestick reversal · 1h | sell | SOL-USD | 10.66 | -0.17 | stop-loss |
| 2026-11-10T09:05 | VWAP momentum · 1h | sell | DOGE-USD | 3.71 | -0.05 | target is flat |
| 2026-11-10T09:00 | Candlestick reversal · 1h | buy | ETH-USD | 12.92 | — | entry signal |
| 2026-11-10T09:00 | Candlestick reversal · 1h | sell | DOGE-USD | 12.86 | -0.10 | time stop |
| 2026-11-10T09:00 | VWAP momentum · 1h | sell | BTC-USD | 2.14 | -0.02 | exit signal |
| 2026-11-10T08:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.65 | — | rebalance up |
| 2026-11-10T08:00 | Candlestick reversal · 1h | sell | XRP-USD | 9.23 | -0.05 | exit signal |
| 2026-11-10T08:00 | VWAP momentum · 1h | buy | BTC-USD | 2.16 | — | entry signal |
| 2026-11-10T08:00 | VWAP momentum · 1h | sell | XRP-USD | 2.16 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 13:00:05.000136+00:00 -> 2026-11-10 13:10:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
