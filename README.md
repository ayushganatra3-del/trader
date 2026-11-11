# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T19:50:05.000128+00:00 · 56139 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 35220 decisions in 3003 calls, $0.4361 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T19:50 | 2 / 14 / 14 | cash |  |
| Breezy | 2026-11-11T19:50 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-11T19:50 | 4 / 24 / 2 | COIN 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| MFI reversion | LABU | 1.94 | +6.20% | 4 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.59 | 16.59 | 20 | 70.0 | 18.63 | 3.74 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.52 | 15.52 | 0 | — | 15.13 | 5.00 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.64 | 3.64 | 0 | — | 6.10 | 1.68 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 6.30 | 1.77 | -9.06 | 234 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.76 | -0.23 | 133 | 34.6 | 10.38 | 3.58 | -3.22 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.66 | -1.34 | 0 | — | -0.72 | -0.17 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.39 | -1.60 | 187 | 30.5 | -2.29 | -0.81 | -9.42 | 161 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.15 | -3.85 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -11.68 | -2.97 | -13.44 | 154 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.65 | -5.35 | 0 | — | -3.31 | -0.83 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.50 | -5.50 | 43 | 39.5 | -6.76 | -1.34 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.59 | -3.30 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.70 | -8.30 | 109 | 22.9 | -15.82 | -5.55 | -18.49 | 79 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 89.34 | -10.66 | 404 | 33.2 | -12.23 | -3.79 | -14.11 | 599 |
| 23 | Max aggression: 5-day momentum | meta | 89.25 | -10.75 | 19 | 47.4 | -26.07 | -1.30 | -45.81 | 25 |
| 24 | Squeeze breakout · 1h | breakout | 88.60 | -11.40 | 64 | 21.9 | -7.58 | -2.63 | -14.29 | 74 |
| 25 | Hold BTC | benchmark | 87.40 | -12.60 | 1 | 0.0 | -4.07 | -0.47 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.68 | -13.32 | 168 | 26.8 | -14.00 | -2.93 | -21.98 | 225 |
| 27 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -15.20 | -7.61 | -15.56 | 204 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 84.66 | -15.34 | 2 | 0.0 | -6.60 | -0.68 | -24.16 | 1 |
| 29 | Daily: Bullish score | daily | 84.25 | -15.75 | 16 | 18.8 | -8.93 | -1.33 | -19.56 | 15 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -17.23 | -4.86 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 83.44 | -16.56 | 72 | 13.9 | -22.77 | -4.73 | -29.00 | 96 |
| 32 | ADX DI cross · 1h | trend | 82.98 | -17.02 | 185 | 18.9 | -19.63 | -3.04 | -30.50 | 267 |
| 33 | Keltner breakout · 1h | breakout | 82.73 | -17.27 | 111 | 24.3 | -18.03 | -3.65 | -25.32 | 178 |
| 34 | Max aggression: 1-day momentum | meta | 82.73 | -17.27 | 27 | 25.9 | -15.96 | -0.31 | -57.50 | 40 |
| 35 | Stochastic reversion · 1h | reversion | 82.16 | -17.84 | 292 | 48.3 | -23.64 | -3.38 | -26.97 | 395 |
| 36 | Volume breakout · 1h | breakout | 81.38 | -18.62 | 148 | 27.7 | -11.92 | -2.66 | -21.11 | 96 |
| 37 | Opening range 15m | breakout | 81.31 | -18.69 | 501 | 31.3 | -18.37 | -4.94 | -21.11 | 725 |
| 38 | Heikin-Ashi · 1h | trend | 80.71 | -19.29 | 417 | 24.5 | -35.80 | -6.56 | -39.47 | 664 |
| 39 | Connors RSI(2) · 1h | reversion | 80.12 | -19.88 | 208 | 39.9 | -20.80 | -6.93 | -21.13 | 123 |
| 40 | MFI reversion · 1h | reversion | 79.66 | -20.34 | 374 | 35.6 | -16.44 | -2.03 | -23.02 | 159 |
| 41 | MACD cross · 1h | trend | 78.64 | -21.36 | 362 | 22.1 | -28.20 | -4.36 | -38.69 | 472 |
| 42 | CCI reversion · 1h | reversion | 78.13 | -21.86 | 332 | 45.2 | -27.62 | -4.19 | -31.08 | 447 |
| 43 | Bollinger breakout · 1h | breakout | 77.69 | -22.31 | 171 | 22.8 | -20.25 | -4.12 | -28.24 | 242 |
| 44 | MACD zero-line · 1h | trend | 76.29 | -23.71 | 160 | 16.9 | -19.77 | -3.68 | -30.85 | 209 |
| 45 | Bollinger reversion · 1h | reversion | 75.85 | -24.15 | 286 | 41.6 | -27.80 | -4.22 | -34.84 | 367 |
| 46 | Supertrend · 1h | trend | 75.65 | -24.35 | 168 | 13.1 | -28.69 | -4.93 | -36.25 | 223 |
| 47 | Daily: Momentum burst | daily | 75.40 | -24.60 | 27 | 11.1 | -31.51 | -4.06 | -38.23 | 33 |
| 48 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 49 | RSI momentum · 1h | momentum | 75.36 | -24.64 | 159 | 12.6 | -25.73 | -3.85 | -37.57 | 216 |
| 50 | EMA 20/50 cross · 1h | trend | 74.88 | -25.12 | 103 | 10.7 | -26.22 | -4.35 | -36.88 | 116 |
| 51 | Triple EMA stack · 1h | trend | 74.42 | -25.58 | 144 | 14.6 | -25.79 | -4.19 | -36.32 | 210 |
| 52 | ROC + volume · 1h | momentum | 73.50 | -26.50 | 376 | 27.7 | -32.88 | -5.84 | -38.60 | 384 |
| 53 | Donchian 20/10 · 1h | breakout | 72.64 | -27.36 | 142 | 19.7 | -28.03 | -5.02 | -35.64 | 211 |
| 54 | Williams %R · 1h | reversion | 72.47 | -27.53 | 353 | 46.2 | -35.80 | -5.53 | -37.03 | 528 |
| 55 | OBV trend · 1h | momentum | 71.99 | -28.01 | 281 | 19.2 | -27.32 | -4.61 | -37.14 | 271 |
| 56 | Z-score reversion · 1h | reversion | 71.40 | -28.60 | 197 | 38.6 | -22.80 | -3.10 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.00 | -31.00 | 175 | 32.6 | -31.58 | -4.83 | -35.16 | 226 |
| 58 | VWAP momentum · 1h | momentum | 68.48 | -31.52 | 859 | 22.6 | -52.10 | -10.84 | -54.26 | 1227 |
| 59 | EMA 9/21 cross · 1h | trend | 67.64 | -32.36 | 253 | 9.9 | -34.13 | -6.44 | -41.61 | 339 |
| 60 | Agent (ML meta-label) | meta | 66.77 | -33.23 | 1749 | 24.8 | -12.99 | -1.87 | -21.44 | 345 |
| 61 | Candlestick reversal · 1h | reversion | 65.24 | -34.76 | 460 | 28.9 | -39.56 | -7.27 | -42.08 | 560 |
| 62 | Three white soldiers | momentum | 60.30 | -39.70 | 519 | 14.8 | -49.22 | -22.25 | -49.37 | 657 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -44.33 | -99.04 | 5294 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.00 | -25.70 | -80.49 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -43.66 | -93.64 | 2530 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -31.34 | -89.51 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.06 | -39.09 | -91.29 | 2336 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.40 | -32.18 | -90.53 | 2217 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -51.47 | -97.82 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.36 | -55.45 | -96.46 | 3438 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.44 | -31.99 | -93.44 | 2337 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -33.62 | -83.47 | 1668 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.20 | -99.54 | 5965 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.13 | -41.22 | -92.34 | 2615 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -37.42 | -95.56 | 3465 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -68.16 | -99.80 | 6131 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.92 | -41.43 | -91.95 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.24 | -23.78 | -75.59 | 1621 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -58.12 | -97.73 | 3537 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -60.63 | -98.84 | 4898 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.33 | -26.26 | -68.82 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -51.45 | -94.76 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.85 | -36.61 | -85.30 | 1796 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -71.49 | -99.64 | 6336 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.38 | -31.25 | -89.38 | 2284 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.62 | -19.65 | -77.80 | 1740 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.60 | -35.69 | -90.61 | 2176 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.71 | -50.95 | -96.72 | 3840 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.06 | -53.27 | -89.06 | 2133 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.50 | -28.01 | -66.26 | 827 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.29 | -22.53 | -72.14 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.28 | -18.34 | -78.54 | 1684 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.20 | -48.11 | -97.20 | 4284 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.43 | -99.93 | 8362 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T19:50 | Agent (ML meta-label) | buy | TSLA | 16.70 | — | entry |
| 2026-11-11T19:50 | Agent (ML meta-label) | sell | TQQQ | 16.68 | -0.04 | selected signal exited |
| 2026-11-11T19:50 | OBV trend · 1h | buy | TSLA | 4.87 | — | rebalance up |
| 2026-11-11T19:50 | OBV trend · 1h | buy | LABU | 4.57 | — | rebalance up |
| 2026-11-11T19:50 | OBV trend · 1h | sell | IWM | 14.40 | 0.15 | target is flat |
| 2026-11-11T19:40 | Agent (ML meta-label) | buy | TQQQ | 16.71 | — | entry |
| 2026-11-11T19:40 | Agent (ML meta-label) | sell | TSLA | 16.69 | -0.02 | selected signal exited |
| 2026-11-11T19:35 | Agent (ML meta-label) | buy | TSLA | 16.71 | — | entry |
| 2026-11-11T19:35 | Agent (ML meta-label) | buy | AMD | 16.71 | — | entry |
| 2026-11-11T19:35 | Agent (ML meta-label) | sell | AMZN | 13.46 | -0.01 | selected signal exited |
| 2026-11-11T19:35 | Agent (ML meta-label) | sell | AAPL | 16.72 | -0.01 | selected signal exited |
| 2026-11-11T19:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 103.89 | -0.08 | target is flat |
| 2026-11-11T19:30 | Agent (ML meta-label) | buy | AAPL | 16.72 | — | entry |
| 2026-11-11T19:30 | Agent (ML meta-label) | sell | TSLA | 16.70 | -0.01 | selected signal exited |
| 2026-11-11T19:30 | Agent (ML meta-label) | sell | AMD | 16.74 | -0.07 | selected signal exited |
| 2026-11-11T19:30 | MFI reversion · 1h | buy | SQQQ | 19.92 | — | entry signal |
| 2026-11-11T19:30 | Stochastic reversion · 1h | buy | SQQQ | 11.75 | — | entry signal |
| 2026-11-11T19:30 | RSI(14) reversion · 1h | buy | SQQQ | 7.01 | — | entry signal |
| 2026-11-11T19:30 | RSI(14) reversion · 1h | sell | ETHU | 3.55 | 0.01 | rebalance down |
| 2026-11-11T19:30 | Candlestick reversal · 1h | buy | SQQQ | 16.33 | — | entry signal |
| 2026-11-11T19:30 | Keltner breakout · 1h | buy | SPY | 2.43 | — | entry |
| 2026-11-11T19:30 | Keltner breakout · 1h | buy | GOOGL | 9.20 | — | entry |
| 2026-11-11T19:30 | Keltner breakout · 1h | sell | META | 11.63 | 0.05 | exit signal |
| 2026-11-11T19:30 | OBV trend · 1h | buy | SPY | 12.01 | — | entry signal |
| 2026-11-11T19:30 | OBV trend · 1h | sell | META | 14.24 | -0.02 | exit signal |
| 2026-11-11T19:30 | VWAP momentum · 1h | buy | QQQ | 3.11 | — | entry |
| 2026-11-11T19:30 | VWAP momentum · 1h | sell | TSLA | 1.70 | -0.01 | exit signal |
| 2026-11-11T19:30 | VWAP momentum · 1h | sell | MSTR | 1.78 | -0.01 | exit signal |
| 2026-11-11T19:30 | EMA 20/50 cross · 1h | buy | SPY | 11.15 | — | entry signal |
| 2026-11-11T19:30 | EMA 20/50 cross · 1h | sell | TSLA | 3.78 | -0.01 | rebalance down |
| 2026-11-11T19:30 | EMA 20/50 cross · 1h | sell | LABU | 3.78 | -0.01 | rebalance down |
| 2026-11-11T19:30 | EMA 9/21 cross · 1h | buy | BTC-USD | 3.22 | — | entry |
| 2026-11-11T19:30 | EMA 9/21 cross · 1h | sell | IWM | 3.44 | 0.05 | rebalance down |
| 2026-11-11T19:25 | Agent (ML meta-label) | buy | TSLA | 16.70 | — | entry |
| 2026-11-11T19:25 | Agent (ML meta-label) | sell | AAPL | 13.40 | -0.02 | selected signal exited |
| 2026-11-11T19:20 | Agent (ML meta-label) | buy | TECL | 3.41 | — | rebalance up |
| 2026-11-11T19:20 | Agent (ML meta-label) | buy | AMD | 5.59 | — | rebalance up |
| 2026-11-11T19:20 | Agent (ML meta-label) | sell | TSLA | 10.03 | -0.03 | selected signal exited |
| 2026-11-11T19:20 | Agent (ML meta-label) | sell | TQQQ | 5.54 | -0.03 | selected signal exited |
| 2026-11-11T19:15 | Agent (ML meta-label) | buy | TQQQ | 5.57 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 19:50:05.000128+00:00 -> 2026-11-11 20:00:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
