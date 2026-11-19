# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T19:50:05.000140+00:00 · 66007 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.52 (-14.48%)

Closed trades 229, win rate 36.7%, fees £6.26, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 17.13 | +0.07 |
| TSLA | 17.28 | +0.16 |

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

Today: 34248 decisions in 3087 calls, $0.4272 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T19:50 | 1 / 4 / 25 | cash |  |
| Breezy | 2026-11-19T19:50 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-11-19T19:50 | 3 / 20 / 7 | COIN 52% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| VWAP reversion | META | 1.90 | +2.79% | 4 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 120.65 | 20.65 | 25 | 64.0 | 29.45 | 4.67 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.25 | 14.25 | 0 | — | 12.40 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.41 | 3.41 | 0 | — | 3.92 | 1.20 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.23 | -3.79 | -4.99 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 39 | 41.0 | -2.96 | -0.55 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -2.22 | -0.66 | -9.06 | 204 |
| 10 | Agent (rotation) | meta | 95.80 | -4.20 | 210 | 28.6 | -0.93 | -0.26 | -7.49 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.50 | -5.50 | 0 | — | -6.50 | -2.23 | -8.00 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.16 | -6.84 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.00 | -8.00 | 8 | 50.0 | -8.05 | -0.58 | -18.69 | 6 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Insider buying | copy | 90.19 | -9.81 | 55 | 40.0 | -8.73 | -1.69 | -14.79 | 67 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.17 | -9.84 | 0 | — | -10.46 | -2.95 | -12.78 | 1 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.67 | -3.74 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 89.39 | -10.61 | 115 | 23.5 | -13.91 | -7.04 | -15.29 | 52 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.21 | -12.79 | 17 | 17.6 | -11.32 | -2.35 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -17.88 | -10.04 | -17.93 | 70 |
| 24 | Opening range 30m | breakout | 86.20 | -13.80 | 448 | 33.5 | -12.21 | -4.16 | -14.79 | 551 |
| 25 | Agent | meta | 85.52 | -14.48 | 229 | 36.7 | -14.16 | -6.59 | -17.14 | 209 |
| 26 | Agent (aggressive) | meta | 83.75 | -16.25 | 106 | 34.0 | -15.30 | -3.96 | -19.65 | 100 |
| 27 | Parabolic SAR · 1h | trend | 81.00 | -19.00 | 194 | 27.8 | -28.16 | -8.71 | -29.73 | 198 |
| 28 | Connors RSI(2) · 1h | reversion | 80.55 | -19.45 | 217 | 40.6 | -14.72 | -6.56 | -15.33 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.45 | -5.37 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -23.47 | -6.34 | -26.67 | 147 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -26.22 | -6.92 | -30.88 | 84 |
| 32 | Opening range 15m | breakout | 77.14 | -22.86 | 546 | 31.7 | -21.88 | -6.79 | -23.60 | 660 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 75.51 | -24.49 | 2 | 0.0 | -23.33 | -3.36 | -26.96 | 1 |
| 34 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.39 | -3.22 | -57.68 | 22 |
| 35 | Hold BTC | benchmark | 73.52 | -26.48 | 2 | 0.0 | -23.20 | -3.73 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 73.31 | -26.70 | 107 | 14.0 | -31.05 | -9.60 | -32.08 | 109 |
| 37 | ADX DI cross · 1h | trend | 72.66 | -27.34 | 225 | 20.0 | -29.79 | -4.72 | -37.00 | 274 |
| 38 | Stochastic reversion · 1h | reversion | 71.78 | -28.22 | 356 | 42.1 | -35.98 | -5.53 | -36.31 | 427 |
| 39 | Supertrend · 1h | trend | 70.21 | -29.79 | 195 | 16.9 | -34.22 | -5.73 | -40.73 | 205 |
| 40 | Bollinger breakout · 1h | breakout | 70.01 | -29.99 | 195 | 21.5 | -33.90 | -8.87 | -36.65 | 218 |
| 41 | Triple EMA stack · 1h | trend | 69.98 | -30.02 | 161 | 14.3 | -31.98 | -6.57 | -38.58 | 173 |
| 42 | MFI reversion · 1h | reversion | 69.91 | -30.09 | 463 | 33.7 | -28.92 | -4.34 | -31.02 | 173 |
| 43 | EMA 20/50 cross · 1h | trend | 69.49 | -30.51 | 118 | 10.2 | -38.30 | -8.64 | -44.71 | 123 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.46 | -4.99 | -37.91 | 31 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -30.25 | -6.05 | -35.99 | 205 |
| 46 | Heikin-Ashi · 1h | trend | 67.82 | -32.18 | 483 | 23.0 | -47.03 | -10.43 | -48.37 | 625 |
| 47 | RSI momentum · 1h | momentum | 67.51 | -32.49 | 184 | 14.1 | -34.47 | -6.57 | -40.62 | 204 |
| 48 | OBV trend · 1h | momentum | 67.44 | -32.56 | 315 | 19.4 | -36.20 | -8.20 | -41.32 | 244 |
| 49 | CCI reversion · 1h | reversion | 66.98 | -33.02 | 397 | 42.1 | -42.47 | -7.16 | -44.29 | 482 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -41.58 | -2.61 | -57.50 | 39 |
| 51 | MACD cross · 1h | trend | 65.52 | -34.48 | 429 | 21.7 | -43.58 | -7.12 | -49.18 | 494 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -39.74 | -6.92 | -44.56 | 341 |
| 53 | Donchian 20/10 · 1h | breakout | 64.61 | -35.39 | 165 | 17.6 | -37.10 | -7.21 | -43.11 | 191 |
| 54 | Bollinger reversion · 1h | reversion | 62.41 | -37.59 | 357 | 38.1 | -39.15 | -5.96 | -40.16 | 416 |
| 55 | Williams %R · 1h | reversion | 62.02 | -37.98 | 447 | 40.5 | -48.32 | -8.59 | -48.59 | 579 |
| 56 | EMA 9/21 cross · 1h | trend | 61.82 | -38.18 | 291 | 11.3 | -40.86 | -8.05 | -47.01 | 323 |
| 57 | Agent (ML meta-label) | meta | 58.65 | -41.35 | 1990 | 24.7 | -25.86 | -4.28 | -26.29 | 272 |
| 58 | RSI(14) reversion · 1h | reversion | 58.42 | -41.58 | 219 | 33.8 | -42.07 | -6.32 | -43.71 | 256 |
| 59 | Z-score reversion · 1h | reversion | 55.91 | -44.09 | 233 | 34.3 | -38.70 | -5.43 | -41.10 | 257 |
| 60 | Candlestick reversal · 1h | reversion | 55.33 | -44.66 | 574 | 27.0 | -50.32 | -9.56 | -50.50 | 639 |
| 61 | VWAP momentum · 1h | momentum | 54.37 | -45.63 | 1003 | 21.6 | -58.17 | -11.88 | -61.17 | 1194 |
| 62 | Three white soldiers | momentum | 52.98 | -47.02 | 608 | 14.3 | -51.66 | -23.34 | -51.66 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -48.25 | -99.11 | 5284 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.22 | -30.05 | -83.43 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.44 | -46.99 | -94.46 | 2468 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.61 | -35.35 | -90.61 | 1946 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.09 | -45.08 | -92.11 | 2294 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -30.42 | -90.53 | 2044 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -51.85 | -98.14 | 3478 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.75 | -53.09 | -96.76 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -36.02 | -93.74 | 2191 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.74 | -35.79 | -83.76 | 1586 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.63 | -56.57 | -99.63 | 6196 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -46.86 | -92.93 | 2532 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.72 | -38.71 | -94.78 | 3184 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -76.01 | -99.83 | 6233 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.18 | -48.62 | -93.19 | 2270 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.32 | -26.03 | -78.34 | 1626 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.81 | -97.83 | 3392 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.33 | -99.10 | 5014 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.62 | -29.90 | -70.62 | 1224 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.89 | -57.51 | -94.89 | 2719 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.03 | -40.32 | -86.04 | 1718 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -73.81 | -99.71 | 6458 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.90 | -31.55 | -90.97 | 2395 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.44 | -19.36 | -80.54 | 1869 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.66 | -37.67 | -91.67 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.69 | -47.77 | -97.71 | 3954 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.09 | -57.47 | -90.09 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.54 | -32.03 | -67.54 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.48 | -29.32 | -74.52 | 1207 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.33 | -18.93 | -82.34 | 1800 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.61 | -46.87 | -97.61 | 4366 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.79 | -99.94 | 8419 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T19:50 | Agent (ML meta-label) | sell | TECL | 7.30 | -0.06 | selected signal exited |
| 2026-11-19T19:50 | MACD cross · 1h | buy | MSFT | 3.59 | — | rebalance up |
| 2026-11-19T19:50 | MACD cross · 1h | buy | COIN | 3.49 | — | rebalance up |
| 2026-11-19T19:50 | MACD cross · 1h | sell | NVDA | 5.10 | -0.19 | stop-loss |
| 2026-11-19T19:46 | Agent (ML meta-label) | buy | TECL | 7.36 | — | entry |
| 2026-11-19T19:40 | Williams %R · 1h | buy | DOGE-USD | 3.45 | — | entry |
| 2026-11-19T19:40 | Williams %R · 1h | sell | NVDA | 3.81 | -0.15 | stop-loss |
| 2026-11-19T19:36 | Agent (aggressive) | sell | SOXL | 41.73 | -0.30 | selected signal exited |
| 2026-11-19T19:36 | Agent | sell | SOXL | 17.01 | -0.12 | selected signal exited |
| 2026-11-19T19:31 | Agent | sell | SQQQ | 17.35 | 0.28 | selected signal exited |
| 2026-11-19T19:31 | CCI reversion · 1h | buy | AAPL | 3.47 | — | entry signal |
| 2026-11-19T19:31 | Bollinger reversion · 1h | buy | TNA | 15.63 | — | entry signal |
| 2026-11-19T19:31 | Connors RSI(2) · 1h | sell | AAPL | 20.26 | 0.11 | exit signal |
| 2026-11-19T19:31 | Candlestick reversal · 1h | buy | QQQ | 2.87 | — | entry signal |
| 2026-11-19T19:31 | Candlestick reversal · 1h | buy | PLTR | 4.28 | — | entry signal |
| 2026-11-19T19:31 | Candlestick reversal · 1h | buy | MSFT | 4.28 | — | entry signal |
| 2026-11-19T19:31 | VWAP momentum · 1h | buy | AAPL | 13.57 | — | entry signal |
| 2026-11-19T19:31 | VWAP momentum · 1h | sell | ETHU | 13.47 | -0.14 | exit signal |
| 2026-11-19T19:31 | Heikin-Ashi · 1h | buy | SQQQ | 16.92 | — | entry signal |
| 2026-11-19T19:25 | MFI reversion · 1h | buy | TSLA | 1.96 | — | entry |
| 2026-11-19T19:25 | RSI(14) reversion · 1h | buy | COIN | 2.79 | — | rebalance up |
| 2026-11-19T19:25 | Candlestick reversal · 1h | sell | MSTR | 6.08 | -0.13 | target is flat |
| 2026-11-19T19:25 | VWAP momentum · 1h | sell | COIN | 13.31 | -0.36 | target is flat |
| 2026-11-19T19:25 | VWAP momentum · 1h | sell | BITX | 13.50 | -0.23 | target is flat |
| 2026-11-19T19:21 | Agent (ML meta-label) | sell | TECL | 7.34 | -0.01 | selected signal exited |
| 2026-11-19T19:20 | Agent (ML meta-label) | buy | TECL | 7.35 | — | entry |
| 2026-11-19T19:15 | Agent | buy | META | 17.06 | — | following VWAP reversion |
| 2026-11-19T19:05 | MFI reversion · 1h | buy | MSTR | 10.01 | — | entry |
| 2026-11-19T19:05 | MFI reversion · 1h | sell | GOOGL | 11.46 | -0.14 | stop-loss |
| 2026-11-19T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 98.59 | — | entry |
| 2026-11-19T19:00 | MACD cross · 1h | buy | MSTR | 3.46 | — | rebalance up |
| 2026-11-19T19:00 | MACD cross · 1h | buy | GOOGL | 3.47 | — | rebalance up |
| 2026-11-19T19:00 | MACD cross · 1h | sell | AMZN | 5.13 | -0.09 | stop-loss |
| 2026-11-19T18:55 | Agent | sell | META | 16.94 | -0.20 | selected signal exited |
| 2026-11-19T18:50 | ADX DI cross · 1h | buy | LABU | 3.73 | — | rebalance up |
| 2026-11-19T18:50 | Three white soldiers | sell | XRP-USD | 13.21 | -0.12 | exit signal |
| 2026-11-19T18:50 | Three white soldiers | sell | SOL-USD | 13.21 | -0.13 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | buy | XRP-USD | 5.68 | — | rebalance up |
| 2026-11-19T18:45 | Three white soldiers | buy | SOL-USD | 5.68 | — | rebalance up |
| 2026-11-19T18:45 | Three white soldiers | sell | UPRO | 7.54 | -0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 19:50:05.000140+00:00 -> 2026-11-19 20:00:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 19:50:05.000140+00:00 -> 2026-11-19 20:00:05.000140+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
