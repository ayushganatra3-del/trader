# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T20:10:05.000137+00:00 · 58587 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 38160 decisions in 3216 calls, $0.4731 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T20:10 | 6 / 17 / 7 | cash |  |
| Breezy | 2026-11-13T20:10 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-13T20:10 | 5 / 23 / 2 | COIN 79% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| MFI reversion | LABU | 1.92 | +6.76% | 3 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.48 | 17.48 | 0 | — | 14.91 | 4.99 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 115.20 | 15.20 | 34 | 29.4 | 23.54 | 3.39 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.15 | 12.15 | 22 | 68.2 | 15.54 | 3.18 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.76 | 4.76 | 0 | — | 6.71 | 1.84 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.76 | 4.75 | 32 | 43.8 | 4.67 | 1.20 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.17 | 1.17 | 141 | 34.8 | 7.74 | 3.05 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.22 | -1.78 | 0 | — | -0.71 | -0.17 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.83 | -3.17 | 1 | 0.0 | -3.32 | -2.17 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.61 | -3.39 | 191 | 30.4 | -2.31 | -0.79 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.24 | -3.76 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 94.32 | -5.68 | 43 | 39.5 | -4.99 | -0.93 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.54 | -6.46 | 0 | — | -4.96 | -1.32 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Trend pullback · 1h | trend | 91.80 | -8.20 | 110 | 22.7 | -15.14 | -5.59 | -17.77 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.65 | -2.31 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.97 | -14.03 | 433 | 33.3 | -10.13 | -3.20 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.65 | -14.35 | 16 | 18.8 | -10.30 | -1.64 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.58 | -7.32 | -15.72 | 211 |
| 26 | Parabolic SAR · 1h | trend | 85.17 | -14.84 | 176 | 29.0 | -15.72 | -3.39 | -22.50 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.11 | -4.44 | -18.51 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.94 | -18.06 | 73 | 13.7 | -23.13 | -4.83 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.54 | -18.46 | 1 | 0.0 | -10.81 | -1.52 | -22.00 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.15 | -18.85 | 2 | 0.0 | -9.56 | -1.09 | -24.16 | 1 |
| 31 | Connors RSI(2) · 1h | reversion | 80.66 | -19.34 | 212 | 40.1 | -18.13 | -6.38 | -18.32 | 114 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Keltner breakout · 1h | breakout | 80.46 | -19.55 | 120 | 25.8 | -16.84 | -3.39 | -25.35 | 170 |
| 34 | Stochastic reversion · 1h | reversion | 79.88 | -20.12 | 303 | 47.5 | -26.31 | -3.87 | -28.07 | 398 |
| 35 | Opening range 15m | breakout | 78.42 | -21.58 | 526 | 31.2 | -17.37 | -4.66 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 78.04 | -21.96 | 401 | 35.4 | -22.18 | -2.89 | -27.13 | 169 |
| 37 | ADX DI cross · 1h | trend | 76.63 | -23.37 | 198 | 19.7 | -24.08 | -3.63 | -32.21 | 272 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -40.25 | -2.60 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.42 | -4.65 | -30.71 | 239 |
| 41 | Max aggression: 1-day momentum | meta | 74.93 | -25.07 | 29 | 27.6 | -20.11 | -0.61 | -57.50 | 41 |
| 42 | MACD cross · 1h | trend | 74.89 | -25.11 | 385 | 23.6 | -29.06 | -4.32 | -38.65 | 470 |
| 43 | Heikin-Ashi · 1h | trend | 74.82 | -25.18 | 443 | 24.2 | -38.05 | -7.08 | -39.26 | 665 |
| 44 | MACD zero-line · 1h | trend | 73.45 | -26.55 | 171 | 18.7 | -23.79 | -4.68 | -30.99 | 202 |
| 45 | Supertrend · 1h | trend | 72.59 | -27.41 | 180 | 15.0 | -30.59 | -5.23 | -36.51 | 216 |
| 46 | RSI momentum · 1h | momentum | 72.58 | -27.42 | 171 | 14.0 | -26.63 | -4.08 | -37.92 | 208 |
| 47 | EMA 20/50 cross · 1h | trend | 72.48 | -27.52 | 109 | 10.1 | -28.33 | -4.79 | -40.51 | 120 |
| 48 | Bollinger reversion · 1h | reversion | 72.21 | -27.79 | 303 | 41.6 | -32.93 | -5.15 | -35.72 | 383 |
| 49 | Triple EMA stack · 1h | trend | 71.66 | -28.34 | 151 | 14.6 | -28.25 | -4.67 | -38.65 | 205 |
| 50 | CCI reversion · 1h | reversion | 71.31 | -28.69 | 346 | 43.4 | -37.36 | -5.85 | -38.71 | 470 |
| 51 | ROC + volume · 1h | momentum | 71.21 | -28.79 | 398 | 28.6 | -31.49 | -5.79 | -38.37 | 377 |
| 52 | OBV trend · 1h | momentum | 69.73 | -30.27 | 298 | 19.1 | -30.22 | -5.34 | -38.15 | 276 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -32.98 | -4.49 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -30.32 | -5.42 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 68.04 | -31.96 | 383 | 43.6 | -42.20 | -6.88 | -44.04 | 543 |
| 56 | Z-score reversion · 1h | reversion | 65.75 | -34.25 | 204 | 37.3 | -30.24 | -4.28 | -31.55 | 237 |
| 57 | Agent (ML meta-label) | meta | 65.21 | -34.79 | 1855 | 24.7 | -18.44 | -2.97 | -24.30 | 357 |
| 58 | EMA 9/21 cross · 1h | trend | 64.77 | -35.23 | 266 | 11.3 | -37.84 | -7.65 | -43.16 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 64.65 | -35.35 | 186 | 32.8 | -36.78 | -5.45 | -38.35 | 239 |
| 60 | VWAP momentum · 1h | momentum | 62.76 | -37.24 | 913 | 22.2 | -52.70 | -10.68 | -53.45 | 1240 |
| 61 | Candlestick reversal · 1h | reversion | 62.24 | -37.76 | 486 | 28.4 | -44.69 | -8.23 | -45.99 | 604 |
| 62 | Three white soldiers | momentum | 58.34 | -41.66 | 542 | 14.6 | -49.50 | -22.28 | -49.51 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.55 | -99.00 | 5306 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.99 | -25.57 | -80.30 | 1427 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -46.53 | -93.84 | 2547 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.20 | -31.50 | -89.28 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -41.51 | -91.32 | 2355 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.81 | -31.30 | -89.81 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -52.02 | -97.89 | 3506 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -56.34 | -96.22 | 3434 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -32.75 | -93.77 | 2339 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -34.70 | -83.20 | 1662 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.58 | -99.57 | 6038 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -42.82 | -92.25 | 2636 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -37.17 | -95.41 | 3476 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.23 | -99.81 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.26 | -43.00 | -92.30 | 2285 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.86 | -26.17 | -75.93 | 1647 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -60.79 | -97.62 | 3526 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.05 | -98.88 | 4944 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.50 | -26.82 | -68.70 | 1254 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -56.94 | -94.76 | 2816 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.09 | -39.33 | -85.21 | 1793 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.80 | -99.66 | 6386 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.05 | -32.63 | -90.19 | 2328 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.54 | -20.17 | -78.91 | 1799 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.68 | -36.42 | -90.84 | 2183 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.02 | -51.94 | -97.02 | 3889 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -58.38 | -89.40 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.59 | -30.91 | -66.61 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.38 | -23.05 | -71.44 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.12 | -19.28 | -80.49 | 1755 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.41 | -51.01 | -97.42 | 4353 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.07 | -99.93 | 8469 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T20:06 | Agent (ML meta-label) | buy | META | 3.10 | — | entry |
| 2026-11-13T20:06 | Agent (ML meta-label) | buy | AMZN | 4.07 | — | following Supertrend |
| 2026-11-13T20:00 | Bollinger reversion · 1h | buy | MSTR | 3.54 | — | entry |
| 2026-11-13T20:00 | Bollinger reversion · 1h | buy | ETHU | 6.75 | — | rebalance up |
| 2026-11-13T20:00 | Bollinger reversion · 1h | sell | ETH-USD | 10.30 | -0.04 | exit signal |
| 2026-11-13T20:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 18.60 | — | entry signal |
| 2026-11-13T19:55 | Agent (ML meta-label) | sell | AMZN | 5.89 | -0.01 | selected signal exited |
| 2026-11-13T19:50 | Agent (ML meta-label) | buy | AMZN | 5.90 | — | following Supertrend |
| 2026-11-13T19:45 | Agent (ML meta-label) | sell | MSTR | 5.73 | -0.02 | selected signal exited |
| 2026-11-13T19:45 | Agent (ML meta-label) | sell | AMZN | 1.45 | -0.00 | selected signal exited |
| 2026-11-13T19:45 | MFI reversion · 1h | buy | SOXL | 3.83 | — | entry |
| 2026-11-13T19:45 | MFI reversion · 1h | buy | ETHU | 7.79 | — | entry |
| 2026-11-13T19:45 | MFI reversion · 1h | buy | COIN | 4.55 | — | rebalance up |
| 2026-11-13T19:45 | MFI reversion · 1h | sell | TSLA | 9.67 | 0.03 | target is flat |
| 2026-11-13T19:45 | MFI reversion · 1h | sell | BITX | 6.49 | -0.01 | target is flat |
| 2026-11-13T19:45 | ROC + volume · 1h | buy | META | 17.81 | — | entry |
| 2026-11-13T19:41 | Agent (ML meta-label) | buy | AMZN | 1.45 | — | following Supertrend |
| 2026-11-13T19:41 | Agent (ML meta-label) | sell | PLTR | 1.45 | -0.00 | selected signal exited |
| 2026-11-13T19:35 | Agent (ML meta-label) | buy | PLTR | 1.45 | — | following VWAP reversion |
| 2026-11-13T19:35 | Agent (ML meta-label) | buy | MSTR | 5.75 | — | entry |
| 2026-11-13T19:35 | Agent (ML meta-label) | sell | UPRO | 3.79 | -0.02 | selected signal exited |
| 2026-11-13T19:35 | Agent (ML meta-label) | sell | AMZN | 3.41 | -0.01 | selected signal exited |
| 2026-11-13T19:30 | MFI reversion · 1h | buy | COIN | 3.25 | — | entry signal |
| 2026-11-13T19:30 | MFI reversion · 1h | buy | BITX | 6.50 | — | entry |
| 2026-11-13T19:30 | MFI reversion · 1h | sell | META | 9.75 | 0.14 | exit signal |
| 2026-11-13T19:30 | CCI reversion · 1h | buy | MSTR | 3.39 | — | entry signal |
| 2026-11-13T19:30 | CCI reversion · 1h | buy | IWM | 3.39 | — | entry signal |
| 2026-11-13T19:30 | CCI reversion · 1h | buy | AMD | 3.39 | — | entry signal |
| 2026-11-13T19:30 | CCI reversion · 1h | sell | XRP-USD | 3.71 | -0.01 | rebalance down |
| 2026-11-13T19:30 | CCI reversion · 1h | sell | ETH-USD | 3.73 | -0.00 | rebalance down |
| 2026-11-13T19:30 | CCI reversion · 1h | sell | BTC-USD | 3.70 | -0.02 | rebalance down |
| 2026-11-13T19:30 | Connors RSI(2) · 1h | sell | AMZN | 20.10 | -0.16 | exit signal |
| 2026-11-13T19:30 | RSI momentum · 1h | buy | META | 18.14 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | UPRO | 3.26 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | TQQQ | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | TNA | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | TECL | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | SPY | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | SOXL | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | QQQ | 3.31 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 20:10:05.000137+00:00 -> 2026-11-13 20:20:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
