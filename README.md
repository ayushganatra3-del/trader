# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T00:20:05.000123+00:00 · 66230 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.36 (-14.64%)

Closed trades 233, win rate 36.9%, fees £6.31, max drawdown -17.33%.

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

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 255 decisions in 51 calls, $0.0036 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T00:20 | 2 / 2 / 1 | cash |  |
| Breezy | 2026-11-20T00:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-20T00:20 | 3 / 2 / 0 | ETH-USD 64% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| CCI reversion | SOXL | 1.96 | +18.18% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.02 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.74 | 14.74 | 0 | — | 12.51 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.94 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.42 | 3.42 | 0 | — | 4.30 | 1.23 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.61 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.11 | -3.89 | 211 | 28.9 | -1.12 | -0.32 | -7.73 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.16 | -5.84 | 0 | — | -7.00 | -2.35 | -8.40 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.28 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.32 | -8.68 | 0 | — | -8.86 | -2.30 | -10.09 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.41 | -10.18 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 90.61 | -9.39 | 8 | 50.0 | -10.85 | -0.86 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.96 | -10.04 | 0 | — | -10.81 | -3.01 | -13.10 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.64 | -18.48 | 149 |
| 19 | Trend pullback · 1h | trend | 89.82 | -10.18 | 115 | 23.5 | -12.07 | -6.71 | -13.27 | 49 |
| 20 | Copy: Insider buying | copy | 89.44 | -10.56 | 55 | 40.0 | -9.31 | -1.82 | -14.79 | 67 |
| 21 | Daily: Bullish score | daily | 87.60 | -12.40 | 17 | 17.6 | -14.48 | -3.80 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.81 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.51 | -18.94 | 71 |
| 25 | Agent | meta | 85.36 | -14.64 | 233 | 36.9 | -13.89 | -6.32 | -16.51 | 214 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.49 | -3.98 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.39 | -18.61 | 194 | 27.8 | -26.67 | -8.03 | -28.86 | 197 |
| 28 | Connors RSI(2) · 1h | reversion | 80.45 | -19.55 | 217 | 40.6 | -14.98 | -6.64 | -15.33 | 75 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.48 | -5.32 | -21.55 | 73 |
| 30 | Donchian 55/20 · 1h | breakout | 78.61 | -21.39 | 79 | 12.7 | -26.18 | -6.85 | -30.98 | 85 |
| 31 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.50 | -6.18 | -25.33 | 143 |
| 32 | Opening range 15m | breakout | 77.33 | -22.67 | 547 | 31.8 | -21.22 | -6.47 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.99 | -25.01 | 2 | 0.0 | -23.95 | -3.42 | -27.37 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 73.68 | -26.32 | 22 | 40.9 | -52.81 | -3.66 | -58.09 | 21 |
| 35 | Ichimoku · 1h | trend | 73.66 | -26.34 | 107 | 14.0 | -30.75 | -9.41 | -32.08 | 109 |
| 36 | Hold BTC | benchmark | 73.26 | -26.74 | 2 | 0.0 | -23.77 | -3.88 | -29.59 | 1 |
| 37 | ADX DI cross · 1h | trend | 72.90 | -27.10 | 226 | 20.4 | -28.34 | -4.45 | -35.87 | 277 |
| 38 | Stochastic reversion · 1h | reversion | 71.28 | -28.71 | 356 | 42.1 | -36.33 | -5.50 | -36.77 | 426 |
| 39 | Triple EMA stack · 1h | trend | 70.28 | -29.72 | 161 | 14.3 | -30.71 | -6.47 | -37.24 | 170 |
| 40 | Bollinger breakout · 1h | breakout | 70.06 | -29.94 | 195 | 21.5 | -32.97 | -8.48 | -36.32 | 216 |
| 41 | Supertrend · 1h | trend | 69.91 | -30.09 | 198 | 16.7 | -33.42 | -5.57 | -39.93 | 204 |
| 42 | EMA 20/50 cross · 1h | trend | 69.57 | -30.43 | 119 | 10.1 | -36.21 | -7.63 | -43.77 | 126 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.14 | -37.91 | 31 |
| 44 | MFI reversion · 1h | reversion | 69.25 | -30.75 | 466 | 33.7 | -30.01 | -4.50 | -31.66 | 174 |
| 45 | Heikin-Ashi · 1h | trend | 68.14 | -31.86 | 483 | 23.0 | -46.14 | -10.17 | -47.85 | 617 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.19 | -5.59 | -34.12 | 207 |
| 47 | RSI momentum · 1h | momentum | 67.83 | -32.17 | 184 | 14.1 | -35.25 | -6.73 | -41.55 | 202 |
| 48 | OBV trend · 1h | momentum | 67.76 | -32.24 | 315 | 19.4 | -35.54 | -7.77 | -41.22 | 240 |
| 49 | CCI reversion · 1h | reversion | 66.49 | -33.51 | 398 | 42.0 | -42.81 | -7.18 | -44.29 | 480 |
| 50 | Max aggression: 1-day momentum | meta | 65.56 | -34.44 | 33 | 27.3 | -47.44 | -3.22 | -57.50 | 38 |
| 51 | MACD cross · 1h | trend | 64.88 | -35.12 | 431 | 21.6 | -43.48 | -6.98 | -49.07 | 496 |
| 52 | ROC + volume · 1h | momentum | 64.82 | -35.18 | 431 | 27.6 | -38.27 | -6.67 | -43.63 | 341 |
| 53 | Donchian 20/10 · 1h | breakout | 64.65 | -35.35 | 165 | 17.6 | -37.01 | -7.07 | -43.26 | 191 |
| 54 | Bollinger reversion · 1h | reversion | 62.14 | -37.86 | 357 | 38.1 | -39.47 | -5.95 | -40.69 | 421 |
| 55 | EMA 9/21 cross · 1h | trend | 62.12 | -37.88 | 291 | 11.3 | -40.95 | -7.94 | -47.32 | 323 |
| 56 | Williams %R · 1h | reversion | 61.39 | -38.60 | 447 | 40.5 | -48.49 | -8.50 | -48.61 | 576 |
| 57 | Agent (ML meta-label) | meta | 58.07 | -41.93 | 1995 | 24.7 | -32.54 | -6.01 | -32.58 | 327 |
| 58 | RSI(14) reversion · 1h | reversion | 57.95 | -42.05 | 219 | 33.8 | -40.61 | -5.85 | -43.68 | 273 |
| 59 | Z-score reversion · 1h | reversion | 55.50 | -44.50 | 233 | 34.3 | -39.09 | -5.41 | -41.82 | 261 |
| 60 | Candlestick reversal · 1h | reversion | 54.67 | -45.33 | 579 | 26.8 | -49.75 | -9.22 | -49.77 | 673 |
| 61 | VWAP momentum · 1h | momentum | 54.62 | -45.38 | 1004 | 21.6 | -57.12 | -11.47 | -60.68 | 1191 |
| 62 | Three white soldiers | momentum | 52.86 | -47.14 | 609 | 14.3 | -51.64 | -22.76 | -51.64 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -45.49 | -99.09 | 5315 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.95 | -29.06 | -83.44 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.31 | -44.21 | -94.35 | 2455 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.58 | -33.79 | -90.60 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.97 | -42.18 | -91.99 | 2286 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.27 | -29.15 | -90.35 | 2028 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.13 | -47.67 | -98.14 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.76 | -49.61 | -96.77 | 3392 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.82 | -34.64 | -93.84 | 2222 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.42 | -34.26 | -83.43 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.63 | -53.48 | -99.63 | 6226 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.80 | -43.93 | -92.80 | 2526 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.67 | -36.80 | -94.72 | 3171 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -66.47 | -99.83 | 6238 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.17 | -44.80 | -93.19 | 2277 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.61 | -24.84 | -78.61 | 1638 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -55.64 | -97.81 | 3382 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -55.04 | -99.11 | 5024 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.64 | -28.87 | -70.64 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.84 | -52.39 | -94.85 | 2715 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.05 | -38.83 | -86.05 | 1708 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -65.94 | -99.72 | 6474 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.13 | -31.25 | -91.21 | 2406 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.44 | -19.18 | -80.64 | 1879 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.84 | -36.83 | -91.89 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.72 | -45.42 | -97.73 | 3973 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.95 | -49.50 | -89.99 | 2173 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.64 | -31.54 | -67.66 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.31 | -28.16 | -74.57 | 1205 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.51 | -18.64 | -82.66 | 1794 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.62 | -44.90 | -97.63 | 4373 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -92.13 | -99.94 | 8414 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T00:00 | Max aggression: 5-day momentum | buy | SOL-USD | 73.75 | — | entry |
| 2026-11-20T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.47 | — | entry signal |
| 2026-11-19T23:10 | Three white soldiers | sell | DOGE-USD | 13.12 | -0.12 | exit signal |
| 2026-11-19T23:00 | MFI reversion · 1h | buy | XRP-USD | 2.48 | — | entry signal |
| 2026-11-19T23:00 | MFI reversion · 1h | buy | BTC-USD | 7.69 | — | entry signal |
| 2026-11-19T23:00 | Stochastic reversion · 1h | buy | XRP-USD | 6.48 | — | entry signal |
| 2026-11-19T23:00 | Z-score reversion · 1h | buy | BTC-USD | 5.53 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | SOL-USD | 4.45 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | ETH-USD | 8.89 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | DOGE-USD | 8.89 | — | entry signal |
| 2026-11-19T23:00 | Bollinger reversion · 1h | buy | BTC-USD | 8.89 | — | entry signal |
| 2026-11-19T22:36 | Three white soldiers | buy | DOGE-USD | 13.24 | — | entry signal |
| 2026-11-19T22:00 | Candlestick reversal · 1h | sell | ETH-USD | 6.10 | -0.16 | time stop |
| 2026-11-19T22:00 | Supertrend · 1h | sell | SOL-USD | 17.04 | -0.71 | exit signal |
| 2026-11-19T22:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 16.87 | -0.41 | exit signal |
| 2026-11-19T21:00 | Supertrend · 1h | sell | ETH-USD | 17.34 | -0.47 | exit signal |
| 2026-11-19T20:55 | Agent (rotation) | sell | SQQQ | 33.96 | 2.89 | selected signal exited |
| 2026-11-19T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 99.63 | 1.04 | target is flat |
| 2026-11-19T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 121.75 | 10.36 | target is flat |
| 2026-11-19T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.03 | -0.62 | target is flat |
| 2026-11-19T20:55 | Agent (ML meta-label) | buy | TQQQ | 7.30 | — | entry |
| 2026-11-19T20:55 | Agent (aggressive) | sell | SOXL | 41.73 | -0.15 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | TSLA | 17.23 | 0.11 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | SQQQ | 17.18 | 0.08 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | SOXL | 17.02 | -0.06 | selected signal exited |
| 2026-11-19T20:55 | Agent | sell | META | 17.00 | -0.06 | selected signal exited |
| 2026-11-19T20:55 | MFI reversion · 1h | buy | AMD | 11.58 | — | entry |
| 2026-11-19T20:55 | MFI reversion · 1h | sell | TSLA | 9.96 | 0.02 | target is flat |
| 2026-11-19T20:55 | MFI reversion · 1h | sell | BITX | 9.88 | -0.21 | target is flat |
| 2026-11-19T20:55 | Candlestick reversal · 1h | buy | MSTR | 4.69 | — | entry |
| 2026-11-19T20:55 | Opening range 30m | sell | SQQQ | 23.53 | 2.26 | end-of-day flatten |
| 2026-11-19T20:55 | Opening range 15m | sell | SQQQ | 21.06 | 2.03 | end-of-day flatten |
| 2026-11-19T20:52 | Agent (ML meta-label) | sell | AAPL | 7.30 | -0.01 | selected signal exited |
| 2026-11-19T20:50 | Agent (ML meta-label) | buy | AAPL | 7.30 | — | entry |
| 2026-11-19T20:45 | Agent (ML meta-label) | sell | TQQQ | 7.28 | -0.02 | selected signal exited |
| 2026-11-19T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 91.65 | — | entry |
| 2026-11-19T20:30 | CCI reversion · 1h | buy | AMD | 1.68 | — | entry signal |
| 2026-11-19T20:30 | Candlestick reversal · 1h | buy | TQQQ | 3.11 | — | rebalance up |
| 2026-11-19T20:30 | Candlestick reversal · 1h | buy | QQQ | 3.24 | — | rebalance up |
| 2026-11-19T20:30 | Candlestick reversal · 1h | sell | TECL | 4.98 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 00:20:05.000123+00:00 -> 2026-11-20 00:30:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-22 00:20:05.000123+00:00 -> 2026-11-20 00:30:05.000123+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
