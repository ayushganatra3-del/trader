# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T16:25:05.000153+00:00 · 65843 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.25 (-14.75%)

Closed trades 225, win rate 36.4%, fees £6.18, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.12 | +0.08 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, LRN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.12 · VIX 24.56 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 19467 decisions in 2595 calls, $0.2540 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T16:25 | 2 / 24 / 4 | cash |  |
| Breezy | 2026-11-19T16:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-19T16:25 | 7 / 23 / 0 | COIN 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| VWAP reversion | META | 1.88 | +2.72% | 4 |
| Connors RSI(2) | SQQQ | 1.81 | +3.66% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 25 | 64.0 | 20.92 | 4.18 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.45 | 13.45 | 0 | — | 11.51 | 3.77 | -4.70 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.11 | 3.11 | 0 | — | 4.43 | 1.18 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -3.86 | -3.43 | -4.83 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Hold SPY | benchmark | 95.52 | -4.48 | 0 | — | -4.06 | -1.42 | -6.99 | 1 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.46 | -4.54 | 8 | 50.0 | -3.03 | -0.19 | -18.69 | 6 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.46 | -8.82 | -5.52 | 20 |
| 14 | Agent (rotation) | meta | 93.83 | -6.17 | 210 | 28.6 | -3.00 | -1.06 | -7.63 | 152 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.81 | -7.19 | 0 | — | -7.32 | -1.93 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.47 | -8.53 | 0 | — | -7.68 | -2.04 | -12.67 | 1 |
| 18 | Copy: Insider buying | copy | 90.83 | -9.17 | 52 | 40.4 | -8.98 | -1.75 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 88.66 | -11.35 | 115 | 23.5 | -17.17 | -8.35 | -17.67 | 57 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 86.42 | -13.58 | 17 | 17.6 | -10.68 | -2.45 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.29 | -9.18 | -16.49 | 71 |
| 24 | Agent | meta | 85.25 | -14.75 | 225 | 36.4 | -14.51 | -6.88 | -17.06 | 203 |
| 25 | Opening range 30m | breakout | 84.83 | -15.17 | 448 | 33.5 | -12.99 | -4.48 | -14.66 | 561 |
| 26 | Agent (aggressive) | meta | 84.05 | -15.95 | 105 | 34.3 | -15.01 | -3.87 | -19.74 | 98 |
| 27 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 216 | 40.3 | -14.25 | -6.32 | -15.00 | 78 |
| 28 | Parabolic SAR · 1h | trend | 80.60 | -19.40 | 193 | 27.5 | -27.39 | -8.22 | -29.07 | 199 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.43 | -5.35 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -25.33 | -6.88 | -28.06 | 150 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 76.93 | -23.07 | 2 | 0.0 | -19.14 | -2.69 | -26.43 | 1 |
| 33 | Opening range 15m | breakout | 75.92 | -24.08 | 546 | 31.7 | -21.73 | -6.37 | -23.39 | 674 |
| 34 | Hold BTC | benchmark | 74.08 | -25.92 | 2 | 0.0 | -22.08 | -3.57 | -28.91 | 1 |
| 35 | ADX DI cross · 1h | trend | 74.05 | -25.95 | 213 | 19.7 | -27.54 | -4.46 | -34.67 | 279 |
| 36 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.38 | -3.22 | -57.31 | 22 |
| 37 | Stochastic reversion · 1h | reversion | 73.65 | -26.35 | 352 | 42.6 | -34.13 | -5.15 | -36.16 | 427 |
| 38 | Ichimoku · 1h | trend | 72.70 | -27.30 | 107 | 14.0 | -32.80 | -9.94 | -33.17 | 110 |
| 39 | Bollinger breakout · 1h | breakout | 72.16 | -27.84 | 193 | 21.8 | -31.63 | -8.62 | -35.28 | 218 |
| 40 | MFI reversion · 1h | reversion | 71.01 | -28.99 | 460 | 33.9 | -28.05 | -4.17 | -31.02 | 171 |
| 41 | Supertrend · 1h | trend | 70.62 | -29.38 | 192 | 16.7 | -33.63 | -5.65 | -40.12 | 207 |
| 42 | Triple EMA stack · 1h | trend | 69.79 | -30.21 | 158 | 14.6 | -31.66 | -6.51 | -38.23 | 177 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.33 | -4.99 | -37.91 | 31 |
| 44 | MACD zero-line · 1h | trend | 68.79 | -31.21 | 187 | 17.6 | -29.19 | -5.88 | -35.30 | 207 |
| 45 | EMA 20/50 cross · 1h | trend | 68.41 | -31.59 | 118 | 10.2 | -38.51 | -8.38 | -44.60 | 125 |
| 46 | Heikin-Ashi · 1h | trend | 68.29 | -31.71 | 480 | 22.9 | -46.73 | -10.28 | -47.72 | 627 |
| 47 | CCI reversion · 1h | reversion | 67.97 | -32.03 | 395 | 42.0 | -41.75 | -6.94 | -44.29 | 480 |
| 48 | RSI momentum · 1h | momentum | 67.91 | -32.09 | 183 | 14.2 | -35.20 | -6.78 | -41.13 | 202 |
| 49 | MACD cross · 1h | trend | 67.77 | -32.23 | 421 | 22.1 | -40.31 | -6.51 | -46.96 | 495 |
| 50 | ROC + volume · 1h | momentum | 67.72 | -32.27 | 421 | 28.3 | -36.23 | -6.69 | -41.76 | 342 |
| 51 | OBV trend · 1h | momentum | 66.88 | -33.12 | 315 | 19.4 | -35.56 | -7.79 | -40.67 | 248 |
| 52 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -36.67 | -2.14 | -57.50 | 39 |
| 53 | Donchian 20/10 · 1h | breakout | 65.37 | -34.63 | 163 | 17.8 | -36.48 | -7.09 | -42.41 | 191 |
| 54 | Williams %R · 1h | reversion | 63.89 | -36.11 | 441 | 41.0 | -46.40 | -8.06 | -47.71 | 573 |
| 55 | Bollinger reversion · 1h | reversion | 63.03 | -36.97 | 354 | 38.4 | -39.22 | -6.00 | -39.90 | 417 |
| 56 | EMA 9/21 cross · 1h | trend | 61.73 | -38.27 | 286 | 11.5 | -40.72 | -8.00 | -46.73 | 324 |
| 57 | Agent (ML meta-label) | meta | 59.83 | -40.17 | 1966 | 24.7 | -22.20 | -3.54 | -23.31 | 289 |
| 58 | RSI(14) reversion · 1h | reversion | 59.46 | -40.55 | 215 | 34.4 | -40.00 | -5.84 | -43.22 | 262 |
| 59 | Z-score reversion · 1h | reversion | 57.72 | -42.28 | 228 | 35.1 | -36.77 | -5.09 | -39.76 | 258 |
| 60 | Candlestick reversal · 1h | reversion | 56.16 | -43.84 | 568 | 27.1 | -47.11 | -8.59 | -48.69 | 650 |
| 61 | VWAP momentum · 1h | momentum | 55.27 | -44.73 | 998 | 21.7 | -57.66 | -11.77 | -60.61 | 1205 |
| 62 | Three white soldiers | momentum | 53.92 | -46.08 | 598 | 14.5 | -51.03 | -23.18 | -51.09 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -47.69 | -99.09 | 5328 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.04 | -29.97 | -83.23 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.34 | -47.02 | -94.34 | 2478 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.58 | -35.50 | -90.62 | 1938 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.00 | -46.59 | -92.00 | 2299 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.54 | -31.10 | -90.55 | 2054 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.06 | -53.11 | -98.06 | 3465 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.74 | -55.53 | -96.74 | 3408 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.85 | -37.54 | -93.85 | 2222 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.57 | -35.26 | -83.57 | 1595 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -54.64 | -99.61 | 6124 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.74 | -47.20 | -92.75 | 2558 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.73 | -39.22 | -94.83 | 3206 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -75.33 | -99.83 | 6186 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.93 | -49.44 | -92.93 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.73 | -27.05 | -77.75 | 1666 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -61.84 | -97.81 | 3408 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.08 | -57.48 | -99.08 | 4986 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.68 | -29.89 | -70.73 | 1243 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.91 | -57.29 | -94.92 | 2746 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.10 | -40.70 | -86.10 | 1742 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -72.01 | -99.71 | 6431 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.76 | -30.68 | -91.01 | 2382 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.77 | -18.88 | -80.32 | 1839 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.49 | -36.35 | -91.60 | 2162 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.66 | -47.36 | -97.67 | 3932 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.72 | -61.56 | -89.76 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.65 | -32.24 | -67.69 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.11 | -28.74 | -74.30 | 1212 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.63 | -18.49 | -81.76 | 1766 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -45.49 | -97.58 | 4345 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -112.66 | -99.94 | 8422 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T16:25 | Agent (ML meta-label) | buy | NVDA | 3.49 | — | entry |
| 2026-11-19T16:20 | MFI reversion · 1h | sell | QQQ | 6.35 | -0.01 | target is flat |
| 2026-11-19T16:10 | Agent (ML meta-label) | sell | NVDA | 3.49 | -0.02 | selected signal exited |
| 2026-11-19T16:06 | Agent (ML meta-label) | buy | NVDA | 3.50 | — | entry |
| 2026-11-19T16:01 | Agent (ML meta-label) | buy | GOOGL | 4.60 | — | entry |
| 2026-11-19T16:01 | Agent (ML meta-label) | sell | AMZN | 4.58 | 0.01 | selected signal exited |
| 2026-11-19T16:01 | MFI reversion · 1h | buy | QQQ | 6.36 | — | entry |
| 2026-11-19T16:01 | OBV trend · 1h | sell | XRP-USD | 15.80 | -0.34 | exit signal |
| 2026-11-19T16:01 | OBV trend · 1h | sell | SOL-USD | 16.72 | -0.36 | exit signal |
| 2026-11-19T16:01 | ROC + volume · 1h | sell | SOL-USD | 5.62 | -0.13 | exit signal |
| 2026-11-19T16:01 | VWAP momentum · 1h | sell | XRP-USD | 10.99 | -0.29 | exit signal |
| 2026-11-19T16:01 | VWAP momentum · 1h | sell | SOL-USD | 10.98 | -0.29 | exit signal |
| 2026-11-19T16:01 | VWAP momentum · 1h | sell | ETH-USD | 11.11 | -0.18 | exit signal |
| 2026-11-19T16:01 | VWAP momentum · 1h | sell | DOGE-USD | 11.07 | -0.21 | exit signal |
| 2026-11-19T16:01 | VWAP momentum · 1h | sell | BTC-USD | 11.11 | -0.16 | exit signal |
| 2026-11-19T16:01 | Heikin-Ashi · 1h | sell | XRP-USD | 16.70 | -0.52 | exit signal |
| 2026-11-19T16:01 | Ichimoku · 1h | sell | SOL-USD | 18.07 | -0.45 | exit signal |
| 2026-11-19T16:01 | ADX DI cross · 1h | sell | ETH-USD | 4.37 | -0.09 | exit signal |
| 2026-11-19T16:01 | ADX DI cross · 1h | sell | BTC-USD | 4.37 | -0.08 | exit signal |
| 2026-11-19T16:01 | Parabolic SAR · 1h | buy | AMZN | 6.65 | — | rebalance up |
| 2026-11-19T16:01 | Parabolic SAR · 1h | sell | XRP-USD | 13.27 | -0.43 | exit signal |
| 2026-11-19T16:01 | Parabolic SAR · 1h | sell | SOL-USD | 13.38 | -0.22 | exit signal |
| 2026-11-19T16:01 | Parabolic SAR · 1h | sell | ETH-USD | 13.26 | -0.23 | exit signal |
| 2026-11-19T16:01 | Parabolic SAR · 1h | sell | DOGE-USD | 13.39 | -0.24 | exit signal |
| 2026-11-19T16:01 | MACD zero-line · 1h | sell | SOL-USD | 17.02 | -0.32 | exit signal |
| 2026-11-19T16:01 | MACD cross · 1h | buy | MSFT | 3.06 | — | entry |
| 2026-11-19T16:01 | MACD cross · 1h | sell | DOGE-USD | 3.06 | -0.03 | exit signal |
| 2026-11-19T15:55 | Agent (ML meta-label) | buy | AMZN | 4.57 | — | entry |
| 2026-11-19T15:55 | Agent (ML meta-label) | sell | MSFT | 4.25 | -0.02 | selected signal exited |
| 2026-11-19T15:55 | Williams %R · 1h | sell | IWM | 3.92 | -0.03 | stop-loss |
| 2026-11-19T15:55 | Z-score reversion · 1h | buy | MSTR | 4.11 | — | entry |
| 2026-11-19T15:55 | Z-score reversion · 1h | buy | META | 2.99 | — | rebalance up |
| 2026-11-19T15:55 | Z-score reversion · 1h | sell | IWM | 7.10 | -0.06 | stop-loss |
| 2026-11-19T15:55 | Bollinger reversion · 1h | sell | IWM | 15.91 | -0.20 | stop-loss |
| 2026-11-19T15:55 | RSI(14) reversion · 1h | buy | ETHU | 4.84 | — | rebalance up |
| 2026-11-19T15:55 | RSI(14) reversion · 1h | sell | IWM | 7.50 | -0.09 | stop-loss |
| 2026-11-19T15:51 | Agent (ML meta-label) | buy | SQQQ | 4.56 | — | following Connors RSI(2) |
| 2026-11-19T15:51 | Agent (ML meta-label) | sell | TNA | 4.27 | -0.10 | selected signal exited |
| 2026-11-19T15:51 | Agent (ML meta-label) | sell | AMD | 3.99 | -0.42 | selected signal exited |
| 2026-11-19T15:51 | MFI reversion · 1h | buy | MSTR | 4.40 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 16:25:05.000153+00:00 -> 2026-11-19 16:35:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 16:25:05.000153+00:00 -> 2026-11-19 16:35:05.000153+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
