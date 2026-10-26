# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T22:38:05.000122+00:00 · 37163 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 110, win rate 39.1%, fees £3.39, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-26 | PAM 12%, PEP 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.13 · VIX 18.42 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 41028 decisions in 3414 calls, $0.5070 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T22:38 | 2 / 2 / 1 | cash |  |
| Breezy | 2026-10-26T22:38 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-26T22:38 | 3 / 2 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Bollinger reversion | BITX | 2.12 | +2.39% | 13 |
| VWAP momentum | PLTR | 1.73 | +4.99% | 6 |
| Stochastic reversion | BITX | 1.67 | +3.43% | 12 |
| RSI(14) reversion | TSLA | 1.52 | +3.64% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.98 | 7.98 | 0 | — | 8.51 | 4.30 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.48 | 1.15 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.57 | 5.57 | 21 | 33.3 | 10.57 | 2.75 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.20 | 2.03 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.99 | -0.01 | 0 | — | 2.80 | 1.30 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.77 | -1.23 | 0 | — | -0.04 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 7.97 | 3.34 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -4.13 | -4.76 | -4.49 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.54 | -3.46 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.14 | -3.86 | 121 | 31.4 | -1.91 | -1.10 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.90 | -5.10 | 0 | — | -6.95 | -2.95 | -7.83 | 1 |
| 18 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 4.98 | 1.64 | -8.76 | 200 |
| 19 | Hold BTC | benchmark | 94.69 | -5.31 | 0 | — | 1.19 | 0.44 | -9.28 | 1 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -7.05 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.97 | -3.37 | -17.21 | 577 |
| 22 | Copy: Insider buying | copy | 92.17 | -7.83 | 27 | 37.0 | -17.34 | -3.33 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 91.56 | -8.44 | 49 | 16.3 | -16.01 | -3.65 | -16.70 | 98 |
| 24 | Daily: Momentum burst | daily | 91.31 | -8.69 | 10 | 10.0 | -19.39 | -3.82 | -20.15 | 40 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.18 | -16.91 | 1 |
| 26 | Squeeze breakout · 1h | breakout | 91.22 | -8.78 | 51 | 23.5 | -2.33 | -0.53 | -11.69 | 92 |
| 27 | Max aggression: 5-day momentum | meta | 91.12 | -8.88 | 11 | 45.5 | -15.58 | -1.43 | -27.80 | 25 |
| 28 | Daily: Bullish score | daily | 90.63 | -9.37 | 11 | 18.2 | -6.77 | -0.82 | -14.40 | 13 |
| 29 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.89 | -6.88 | -12.54 | 214 |
| 30 | Parabolic SAR · 1h | trend | 89.81 | -10.20 | 121 | 25.6 | -22.11 | -5.59 | -22.33 | 246 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.30 | -10.70 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 32 | Volume breakout · 1h | breakout | 88.92 | -11.08 | 103 | 23.3 | -12.76 | -2.67 | -15.89 | 111 |
| 33 | ADX DI cross · 1h | trend | 88.76 | -11.24 | 114 | 17.5 | -12.79 | -2.77 | -14.56 | 263 |
| 34 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.16 | -3.35 | -14.77 | 93 |
| 35 | Stochastic reversion · 1h | reversion | 87.66 | -12.34 | 198 | 47.0 | -20.77 | -3.77 | -23.11 | 395 |
| 36 | Bollinger breakout · 1h | breakout | 87.19 | -12.81 | 108 | 26.9 | -12.32 | -2.40 | -17.70 | 238 |
| 37 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.53 | -4.15 | -17.87 | 704 |
| 38 | Keltner breakout · 1h | breakout | 85.58 | -14.42 | 74 | 23.0 | -20.25 | -3.97 | -23.13 | 185 |
| 39 | Connors RSI(2) · 1h | reversion | 85.07 | -14.93 | 174 | 40.2 | -26.47 | -8.03 | -26.96 | 198 |
| 40 | Z-score reversion · 1h | reversion | 84.71 | -15.29 | 116 | 33.6 | -14.55 | -2.41 | -21.48 | 210 |
| 41 | EMA 20/50 cross · 1h | trend | 84.48 | -15.52 | 72 | 11.1 | -21.67 | -4.30 | -23.13 | 128 |
| 42 | RSI momentum · 1h | momentum | 83.43 | -16.57 | 104 | 15.4 | -22.45 | -4.43 | -23.76 | 202 |
| 43 | MACD cross · 1h | trend | 83.03 | -16.97 | 239 | 22.6 | -29.89 | -6.34 | -30.39 | 473 |
| 44 | Supertrend · 1h | trend | 82.83 | -17.17 | 114 | 14.0 | -28.70 | -6.16 | -29.82 | 226 |
| 45 | MFI reversion · 1h | reversion | 82.44 | -17.56 | 263 | 31.6 | -16.26 | -2.54 | -20.70 | 154 |
| 46 | Ichimoku · 1h | trend | 82.15 | -17.85 | 68 | 11.8 | -21.80 | -4.60 | -24.73 | 109 |
| 47 | Triple EMA stack · 1h | trend | 81.52 | -18.48 | 101 | 14.9 | -30.44 | -6.16 | -30.71 | 206 |
| 48 | Bollinger reversion · 1h | reversion | 81.17 | -18.83 | 179 | 37.4 | -29.91 | -6.21 | -31.08 | 368 |
| 49 | CCI reversion · 1h | reversion | 81.02 | -18.98 | 222 | 44.6 | -24.62 | -3.52 | -28.06 | 466 |
| 50 | Williams %R · 1h | reversion | 81.02 | -18.98 | 228 | 46.1 | -34.94 | -5.98 | -35.69 | 543 |
| 51 | MACD zero-line · 1h | trend | 80.21 | -19.79 | 109 | 15.6 | -24.02 | -5.17 | -24.84 | 218 |
| 52 | Donchian 20/10 · 1h | breakout | 79.63 | -20.37 | 99 | 20.2 | -24.65 | -4.71 | -27.59 | 212 |
| 53 | OBV trend · 1h | momentum | 78.84 | -21.16 | 206 | 17.5 | -35.18 | -7.39 | -35.56 | 295 |
| 54 | Agent (ML meta-label) | meta | 78.74 | -21.26 | 924 | 19.4 | -17.02 | -3.30 | -18.49 | 359 |
| 55 | Three white soldiers | momentum | 78.73 | -21.27 | 301 | 19.3 | -44.01 | -20.76 | -44.10 | 599 |
| 56 | RSI(14) reversion · 1h | reversion | 78.14 | -21.86 | 100 | 24.0 | -16.26 | -2.57 | -24.48 | 212 |
| 57 | Heikin-Ashi · 1h | trend | 76.52 | -23.48 | 289 | 22.1 | -45.04 | -10.32 | -45.66 | 661 |
| 58 | ROC + volume · 1h | momentum | 76.46 | -23.54 | 248 | 24.2 | -30.57 | -6.04 | -32.20 | 381 |
| 59 | Candlestick reversal · 1h | reversion | 76.24 | -23.75 | 272 | 27.9 | -33.71 | -6.22 | -35.06 | 573 |
| 60 | EMA 9/21 cross · 1h | trend | 75.12 | -24.88 | 175 | 10.9 | -32.37 | -6.64 | -35.27 | 333 |
| 61 | VWAP momentum · 1h | momentum | 74.96 | -25.04 | 554 | 20.9 | -49.40 | -11.04 | -50.23 | 1239 |
| 62 | Max aggression: 1-day momentum | meta | 67.06 | -32.94 | 19 | 26.3 | -42.14 | -2.90 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.24 | -44.76 | 759 | 22.1 | -74.26 | -26.82 | -74.43 | 1572 |
| 64 | Volume breakout | breakout | 54.18 | -45.82 | 456 | 12.9 | -62.58 | -26.50 | -62.64 | 799 |
| 65 | Squeeze breakout | breakout | 50.90 | -49.10 | 594 | 14.3 | -67.41 | -28.82 | -67.82 | 1173 |
| 66 | Donchian 55/20 | breakout | 50.88 | -49.12 | 610 | 19.7 | -72.04 | -23.94 | -72.35 | 1274 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -45.40 | -98.90 | 5149 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.14 | -23.56 | -79.14 | 1423 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.96 | -47.36 | -93.98 | 2546 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.23 | -31.18 | -89.24 | 1927 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.34 | -38.46 | -91.34 | 2336 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.62 | -30.95 | -90.63 | 2169 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.95 | -56.26 | -97.95 | 3531 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -61.10 | -96.23 | 3381 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.15 | -37.23 | -94.19 | 2467 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.59 | -35.07 | -82.80 | 1689 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -57.21 | -99.44 | 5794 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.68 | -43.44 | -92.68 | 2617 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -38.53 | -95.55 | 3381 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -83.40 | -99.78 | 6172 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.45 | -46.94 | -92.45 | 2340 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -66.72 | -97.74 | 3573 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -62.41 | -98.66 | 4804 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -58.68 | -94.57 | 2769 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.33 | -39.87 | -84.33 | 1806 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -69.62 | -99.60 | 6297 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.32 | -29.74 | -88.43 | 2230 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.85 | -19.42 | -77.24 | 1708 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.71 | -38.39 | -90.71 | 2298 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.29 | -49.91 | -96.29 | 3825 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.24 | -51.23 | -90.24 | 2148 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.78 | -17.99 | -75.97 | 1578 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -51.15 | -96.54 | 4206 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -112.91 | -99.92 | 8264 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T22:15 | Squeeze breakout | sell | SOL-USD | 12.68 | -0.11 | stop-loss |
| 2026-10-26T22:15 | Squeeze breakout | sell | DOGE-USD | 12.68 | -0.11 | exit signal |
| 2026-10-26T22:15 | Squeeze breakout | sell | BTC-USD | 12.72 | -0.09 | stop-loss |
| 2026-10-26T22:00 | CCI reversion · 1h | buy | SOL-USD | 7.85 | — | entry signal |
| 2026-10-26T21:40 | Squeeze breakout | buy | DOGE-USD | 12.79 | — | entry signal |
| 2026-10-26T21:35 | Squeeze breakout | buy | SOL-USD | 12.79 | — | entry signal |
| 2026-10-26T21:30 | Squeeze breakout | buy | BTC-USD | 12.80 | — | entry signal |
| 2026-10-26T21:05 | Bollinger breakout · 1h | buy | DOGE-USD | 21.67 | — | entry |
| 2026-10-26T21:00 | Bollinger breakout · 1h | sell | DOGE-USD | 21.67 | -0.38 | exit signal |
| 2026-10-26T21:00 | VWAP momentum · 1h | sell | XRP-USD | 9.31 | -0.10 | exit signal |
| 2026-10-26T21:00 | Ichimoku · 1h | sell | XRP-USD | 16.35 | -0.18 | exit signal |
| 2026-10-26T21:00 | MACD cross · 1h | sell | ETH-USD | 4.56 | -0.08 | exit signal |
| 2026-10-26T21:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 8.23 | -0.10 | exit signal |
| 2026-10-26T20:00 | VWAP momentum · 1h | buy | XRP-USD | 4.02 | — | rebalance up |
| 2026-10-26T20:00 | VWAP momentum · 1h | buy | DOGE-USD | 4.00 | — | rebalance up |
| 2026-10-26T20:00 | MACD cross · 1h | sell | BTC-USD | 6.35 | -0.05 | exit signal |
| 2026-10-26T19:55 | Agent (rotation) | sell | TQQQ | 63.41 | 0.28 | selected signal exited |
| 2026-10-26T19:55 | Day trade: Stocks in Play ORB | sell | UPRO | 24.86 | 0.13 | target is flat |
| 2026-10-26T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.25 | 0.73 | target is flat |
| 2026-10-26T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 106.08 | 0.19 | target is flat |
| 2026-10-26T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 97.78 | -0.43 | target is flat |
| 2026-10-26T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 105.57 | 1.98 | target is flat |
| 2026-10-26T19:55 | Agent (aggressive) | sell | BITX | 44.26 | -0.06 | selected signal exited |
| 2026-10-26T19:55 | Agent | sell | PLTR | 18.21 | 0.35 | selected signal exited |
| 2026-10-26T19:55 | Agent | sell | BITX | 18.01 | -0.02 | selected signal exited |
| 2026-10-26T19:55 | Squeeze breakout | sell | AAPL | 12.80 | -0.00 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | UPRO | 7.16 | -0.00 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | TSLA | 7.05 | -0.11 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | TQQQ | 7.22 | 0.03 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | TNA | 7.04 | -0.06 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | TECL | 7.87 | 0.13 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | SPY | 7.17 | -0.02 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | QQQ | 7.19 | -0.00 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | MSTR | 7.09 | -0.10 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | MSFT | 2.07 | 0.00 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | IWM | 7.13 | -0.02 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | ETHU | 7.14 | -0.05 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | COIN | 7.14 | -0.05 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | BITX | 6.18 | -0.03 | end-of-day flatten |
| 2026-10-26T19:55 | Opening range 30m | sell | AMD | 5.18 | -0.01 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 22:38:05.000122+00:00 -> 2026-10-26 22:48:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
