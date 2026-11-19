# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T23:20:05.000119+00:00 · 66184 ticks

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

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 35.92 · VIX 27.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 41046 decisions in 3618 calls, $0.5111 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T23:20 | 1 / 4 / 0 | SOL-USD 15% |  |
| Breezy | 2026-11-19T23:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-19T23:20 | 2 / 3 / 0 | ETH-USD 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| Connors RSI(2) | SQQQ | 1.81 | +3.66% | 10 |
| Squeeze breakout | SQQQ | 1.74 | +6.13% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.05 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.77 | 14.77 | 0 | — | 12.51 | 4.19 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.44 | 3.44 | 0 | — | 4.30 | 1.24 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.64 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.11 | -3.89 | 211 | 28.9 | -1.12 | -0.32 | -7.73 | 153 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.18 | -5.83 | 0 | — | -7.00 | -2.37 | -8.40 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.34 | -8.66 | 0 | — | -8.86 | -2.31 | -10.09 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.49 | -10.18 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 90.62 | -9.38 | 8 | 50.0 | -10.85 | -0.87 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.98 | -10.02 | 0 | — | -10.81 | -3.03 | -13.10 | 1 |
| 18 | Trend pullback · 1h | trend | 89.83 | -10.17 | 115 | 23.5 | -12.17 | -6.74 | -13.38 | 52 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.45 | -3.67 | -18.48 | 149 |
| 20 | Copy: Insider buying | copy | 89.46 | -10.54 | 55 | 40.0 | -9.31 | -1.84 | -14.79 | 67 |
| 21 | Daily: Bullish score | daily | 87.62 | -12.38 | 17 | 17.6 | -14.48 | -3.83 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.84 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.61 | -18.94 | 71 |
| 25 | Agent | meta | 85.36 | -14.64 | 233 | 36.9 | -13.89 | -6.38 | -16.51 | 214 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.49 | -4.02 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.39 | -18.61 | 194 | 27.8 | -26.95 | -8.28 | -28.86 | 196 |
| 28 | Connors RSI(2) · 1h | reversion | 80.46 | -19.54 | 217 | 40.6 | -14.98 | -6.70 | -15.33 | 75 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.38 | -21.55 | 73 |
| 30 | Donchian 55/20 · 1h | breakout | 78.61 | -21.39 | 79 | 12.7 | -26.18 | -6.91 | -30.98 | 85 |
| 31 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.50 | -6.24 | -25.33 | 143 |
| 32 | Opening range 15m | breakout | 77.33 | -22.67 | 547 | 31.8 | -21.22 | -6.52 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 75.01 | -24.99 | 2 | 0.0 | -23.95 | -3.45 | -27.37 | 1 |
| 34 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -52.80 | -3.69 | -58.09 | 21 |
| 35 | Ichimoku · 1h | trend | 73.66 | -26.34 | 107 | 14.0 | -30.75 | -9.50 | -32.08 | 109 |
| 36 | Hold BTC | benchmark | 73.17 | -26.83 | 2 | 0.0 | -23.65 | -3.90 | -29.59 | 1 |
| 37 | ADX DI cross · 1h | trend | 72.91 | -27.09 | 226 | 20.4 | -28.34 | -4.49 | -35.87 | 277 |
| 38 | Stochastic reversion · 1h | reversion | 71.28 | -28.72 | 356 | 42.1 | -36.34 | -5.55 | -36.76 | 426 |
| 39 | Triple EMA stack · 1h | trend | 70.28 | -29.72 | 161 | 14.3 | -30.42 | -6.33 | -37.24 | 170 |
| 40 | Bollinger breakout · 1h | breakout | 70.06 | -29.94 | 195 | 21.5 | -32.97 | -8.56 | -36.32 | 216 |
| 41 | Supertrend · 1h | trend | 69.91 | -30.09 | 198 | 16.7 | -33.42 | -5.61 | -39.93 | 204 |
| 42 | EMA 20/50 cross · 1h | trend | 69.57 | -30.43 | 119 | 10.1 | -37.39 | -9.84 | -41.82 | 124 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 44 | MFI reversion · 1h | reversion | 69.23 | -30.77 | 466 | 33.7 | -29.90 | -4.52 | -31.66 | 174 |
| 45 | Heikin-Ashi · 1h | trend | 68.14 | -31.86 | 483 | 23.0 | -46.31 | -10.36 | -47.85 | 618 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.06 | -5.61 | -34.12 | 207 |
| 47 | RSI momentum · 1h | momentum | 67.83 | -32.17 | 184 | 14.1 | -35.21 | -6.75 | -41.59 | 202 |
| 48 | OBV trend · 1h | momentum | 67.76 | -32.24 | 315 | 19.4 | -36.01 | -8.27 | -41.22 | 241 |
| 49 | CCI reversion · 1h | reversion | 66.50 | -33.50 | 398 | 42.0 | -42.78 | -7.23 | -44.29 | 480 |
| 50 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -47.44 | -3.25 | -57.50 | 38 |
| 51 | MACD cross · 1h | trend | 64.89 | -35.11 | 431 | 21.6 | -43.62 | -7.09 | -49.07 | 496 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -38.73 | -6.84 | -43.63 | 342 |
| 53 | Donchian 20/10 · 1h | breakout | 64.66 | -35.34 | 165 | 17.6 | -37.12 | -7.22 | -43.26 | 192 |
| 54 | Bollinger reversion · 1h | reversion | 62.12 | -37.88 | 357 | 38.1 | -39.52 | -6.02 | -40.63 | 421 |
| 55 | EMA 9/21 cross · 1h | trend | 62.12 | -37.88 | 291 | 11.3 | -40.95 | -8.01 | -47.32 | 323 |
| 56 | Williams %R · 1h | reversion | 61.40 | -38.60 | 447 | 40.5 | -48.42 | -8.57 | -48.53 | 576 |
| 57 | Agent (ML meta-label) | meta | 58.08 | -41.92 | 1995 | 24.7 | -32.72 | -5.67 | -34.94 | 293 |
| 58 | RSI(14) reversion · 1h | reversion | 57.96 | -42.04 | 219 | 33.8 | -40.54 | -5.89 | -43.68 | 266 |
| 59 | Z-score reversion · 1h | reversion | 55.50 | -44.50 | 233 | 34.3 | -39.12 | -5.47 | -41.77 | 261 |
| 60 | Candlestick reversal · 1h | reversion | 54.69 | -45.31 | 579 | 26.8 | -49.06 | -9.09 | -49.35 | 666 |
| 61 | VWAP momentum · 1h | momentum | 54.62 | -45.38 | 1004 | 21.6 | -57.12 | -11.59 | -60.68 | 1191 |
| 62 | Three white soldiers | momentum | 52.86 | -47.14 | 609 | 14.3 | -51.64 | -23.21 | -51.64 | 665 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -47.54 | -99.09 | 5307 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -82.95 | -29.86 | -83.44 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.36 | -46.88 | -94.39 | 2458 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.60 | -35.18 | -90.64 | 1943 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.96 | -44.94 | -91.98 | 2287 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.28 | -30.01 | -90.37 | 2030 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.13 | -51.32 | -98.14 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -53.20 | -96.78 | 3394 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.77 | -37.25 | -93.78 | 2216 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.48 | -35.59 | -83.48 | 1579 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.63 | -57.87 | -99.64 | 6226 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.83 | -46.47 | -92.83 | 2527 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.67 | -38.32 | -94.73 | 3175 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.43 | -99.83 | 6237 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.14 | -48.06 | -93.16 | 2275 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.62 | -25.78 | -78.66 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -60.74 | -97.82 | 3382 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.69 | -99.11 | 5026 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.64 | -29.66 | -70.64 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.87 | -56.95 | -94.88 | 2717 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.09 | -40.57 | -86.09 | 1710 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -74.11 | -99.72 | 6472 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.13 | -32.21 | -91.21 | 2406 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.41 | -19.46 | -80.56 | 1875 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.84 | -38.38 | -91.89 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.72 | -48.07 | -97.73 | 3973 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.99 | -54.70 | -89.99 | 2176 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.64 | -32.53 | -67.66 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.31 | -28.90 | -74.57 | 1205 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.45 | -18.91 | -82.67 | 1794 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.62 | -47.45 | -97.63 | 4373 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.30 | -99.94 | 8417 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-19T20:30 | Candlestick reversal · 1h | sell | COIN | 6.05 | -0.09 | stop-loss |
| 2026-11-19T20:30 | Bollinger breakout · 1h | buy | SQQQ | 17.50 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 23:20:05.000119+00:00 -> 2026-11-19 23:30:05.000119+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 23:20:05.000119+00:00 -> 2026-11-19 23:30:05.000119+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
