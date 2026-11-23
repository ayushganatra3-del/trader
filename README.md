# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T16:45:05.000129+00:00 · 70776 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £79.17 (-20.83%)

Closed trades 239, win rate 36.0%, fees £6.49, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 18872 decisions in 2494 calls, $0.2456 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T16:45 | 3 / 16 / 11 | cash |  |
| Breezy | 2026-11-23T16:45 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-23T16:45 | 4 / 21 / 5 | COIN 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 32.17 | 4.75 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.99 | 15.99 | 0 | — | 14.09 | 4.71 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.54 | 1.38 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.68 | 3.68 | 0 | — | 1.56 | 0.52 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.53 | -0.47 | 213 | 31.9 | -0.41 | -0.04 | -8.71 | 210 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.16 | -3.84 | 223 | 28.7 | -0.81 | -0.18 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.31 | -4.69 | 0 | — | -6.89 | -1.79 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.17 | -3.10 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.53 | -7.47 | 0 | — | -8.73 | -1.79 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | VWAP reversion · 1h | reversion | 91.69 | -8.31 | 163 | 46.0 | -5.73 | -0.82 | -20.49 | 156 |
| 17 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.07 | -3.58 | -9.21 | 32 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.04 | -8.96 | 0 | — | -10.36 | -2.19 | -17.03 | 1 |
| 19 | Copy: Insider buying | copy | 89.56 | -10.44 | 57 | 40.4 | -18.51 | -3.62 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.69 | -3.21 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 86.31 | -13.69 | 454 | 33.5 | -13.21 | -4.39 | -14.52 | 542 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.03 | -13.97 | 9 | 44.4 | -11.69 | -0.68 | -26.65 | 6 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -16.71 | -3.83 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.92 | -16.08 | 75 | 20.0 | -16.17 | -6.13 | -16.97 | 74 |
| 25 | Connors RSI(2) · 1h | reversion | 81.33 | -18.67 | 219 | 40.6 | -12.77 | -5.26 | -14.31 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.95 | -19.05 | 200 | 27.0 | -27.54 | -7.47 | -30.19 | 190 |
| 27 | Agent | meta | 79.17 | -20.83 | 239 | 36.0 | -25.67 | -5.62 | -26.39 | 197 |
| 28 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.44 | -4.20 | -24.77 | 92 |
| 29 | Donchian 55/20 · 1h | breakout | 78.17 | -21.83 | 82 | 12.2 | -27.88 | -7.76 | -28.72 | 84 |
| 30 | Opening range 15m | breakout | 77.31 | -22.70 | 565 | 31.0 | -22.32 | -6.90 | -23.54 | 661 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.50 | -7.11 | -22.67 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -26.71 | -6.84 | -27.17 | 149 |
| 33 | Ichimoku · 1h | trend | 74.44 | -25.56 | 110 | 13.6 | -28.76 | -7.70 | -30.49 | 106 |
| 34 | Hold BTC | benchmark | 72.37 | -27.63 | 3 | 0.0 | -28.38 | -4.98 | -36.21 | 1 |
| 35 | Triple EMA stack · 1h | trend | 71.35 | -28.65 | 161 | 14.3 | -34.79 | -8.76 | -38.28 | 166 |
| 36 | Supertrend · 1h | trend | 71.30 | -28.70 | 199 | 16.6 | -34.81 | -6.69 | -39.05 | 219 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 71.29 | -28.71 | 3 | 0.0 | -23.40 | -2.74 | -32.18 | 1 |
| 38 | EMA 20/50 cross · 1h | trend | 71.03 | -28.97 | 119 | 10.1 | -35.27 | -9.71 | -39.53 | 123 |
| 39 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -36.15 | -6.52 | -38.57 | 281 |
| 40 | Daily: Momentum burst | daily | 69.47 | -30.53 | 30 | 13.3 | -37.21 | -5.28 | -38.52 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.60 | -31.40 | 207 | 22.2 | -33.40 | -8.73 | -34.38 | 213 |
| 42 | OBV trend · 1h | momentum | 68.34 | -31.66 | 319 | 19.4 | -37.48 | -9.75 | -40.32 | 231 |
| 43 | Stochastic reversion · 1h | reversion | 67.05 | -32.95 | 392 | 40.6 | -36.10 | -3.92 | -44.30 | 435 |
| 44 | Max aggression: 5-day momentum | meta | 66.38 | -33.62 | 24 | 37.5 | -60.72 | -3.96 | -64.58 | 23 |
| 45 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -34.96 | -9.50 | -35.30 | 208 |
| 46 | RSI momentum · 1h | momentum | 65.99 | -34.01 | 188 | 13.8 | -37.78 | -8.39 | -39.43 | 203 |
| 47 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -47.02 | -9.46 | -47.48 | 633 |
| 48 | MFI reversion · 1h | reversion | 63.54 | -36.46 | 486 | 32.9 | -32.18 | -4.68 | -37.45 | 185 |
| 49 | Donchian 20/10 · 1h | breakout | 63.49 | -36.51 | 173 | 16.8 | -39.22 | -8.55 | -40.79 | 194 |
| 50 | ROC + volume · 1h | momentum | 62.16 | -37.84 | 442 | 27.4 | -42.09 | -8.60 | -42.09 | 341 |
| 51 | EMA 9/21 cross · 1h | trend | 61.31 | -38.69 | 298 | 11.1 | -43.68 | -10.40 | -45.56 | 327 |
| 52 | Agent (ML meta-label) | meta | 60.34 | -39.66 | 2034 | 25.0 | -21.51 | -2.59 | -33.19 | 313 |
| 53 | MACD cross · 1h | trend | 59.64 | -40.36 | 464 | 20.9 | -49.08 | -9.44 | -50.17 | 519 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -53.90 | -3.88 | -54.71 | 38 |
| 55 | CCI reversion · 1h | reversion | 58.12 | -41.88 | 430 | 40.0 | -49.48 | -8.24 | -52.04 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 57.98 | -42.02 | 391 | 37.6 | -38.34 | -4.57 | -45.42 | 436 |
| 57 | Williams %R · 1h | reversion | 54.23 | -45.77 | 492 | 38.2 | -54.64 | -8.98 | -55.98 | 595 |
| 58 | VWAP momentum · 1h | momentum | 53.67 | -46.33 | 1037 | 21.5 | -58.40 | -13.46 | -58.96 | 1197 |
| 59 | RSI(14) reversion · 1h | reversion | 51.07 | -48.93 | 239 | 31.4 | -46.66 | -7.06 | -49.37 | 289 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.09 | -8.59 | -54.62 | 685 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -47.90 | -99.14 | 5333 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.91 | -32.78 | -84.53 | 1435 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.53 | -48.78 | -94.54 | 2425 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.88 | -31.47 | -91.06 | 1927 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.76 | -40.83 | -91.77 | 2244 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.33 | -27.64 | -89.40 | 1943 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -48.12 | -98.15 | 3414 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.00 | -51.80 | -97.00 | 3351 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -38.72 | -93.53 | 2140 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.28 | 650 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.38 | -34.92 | -83.42 | 1546 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -52.67 | -99.66 | 6280 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.17 | -40.42 | -93.17 | 2497 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.31 | -35.56 | -94.31 | 3140 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -61.28 | -99.82 | 6131 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.23 | -42.76 | -93.43 | 2265 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.48 | -24.08 | -78.95 | 1618 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -55.82 | -97.78 | 3284 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -57.42 | -99.17 | 5090 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.84 | -28.21 | -70.98 | 1198 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.95 | -48.84 | -94.97 | 2676 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.02 | -6.24 | -48.72 | 281 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.80 | -37.41 | -85.82 | 1692 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.75 | -99.76 | 6513 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.40 | -29.75 | -91.60 | 2483 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.76 | -19.56 | -82.92 | 1957 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.75 | -28.85 | -92.08 | 2165 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.12 | -47.07 | -98.13 | 4056 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.14 | -46.42 | -90.20 | 2191 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.60 | -29.88 | -68.61 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.23 | -28.32 | -74.23 | 1170 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.90 | -19.01 | -83.90 | 1844 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.98 | -48.18 | -97.98 | 4437 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -90.90 | -99.94 | 8282 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T16:45 | Agent (rotation) | sell | UPRO | 3.51 | -0.07 | selected signal exited |
| 2026-11-23T16:45 | Gap and go | sell | UPRO | 24.87 | -0.43 | exit signal |
| 2026-11-23T16:40 | Agent (rotation) | sell | TSLA | 7.96 | -0.08 | selected signal exited |
| 2026-11-23T16:40 | Agent | sell | SQQQ | 16.47 | -0.14 | selected signal exited |
| 2026-11-23T16:40 | Donchian 55/20 · 1h | sell | BTC-USD | 19.64 | -0.38 | stop-loss |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | XRP-USD | 2.58 | 0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | UPRO | 2.46 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TSLA | 2.60 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TQQQ | 2.57 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TNA | 2.59 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | TECL | 2.57 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | SPY | 2.60 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | SOXL | 2.55 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | SOL-USD | 2.58 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | QQQ | 2.60 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | PLTR | 2.58 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | NVDA | 2.57 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | MSTR | 2.58 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | MSFT | 2.61 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | META | 2.61 | -0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | LABU | 2.59 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | IWM | 2.61 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | GOOGL | 2.60 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | ETHU | 2.60 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.58 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | COIN | 2.59 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | BITX | 2.59 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | AMZN | 2.60 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | AMD | 2.59 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | Heikin-Ashi · 1h | sell | AAPL | 2.61 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T16:40 | MACD cross · 1h | buy | META | 2.01 | — | entry |
| 2026-11-23T16:40 | MACD cross · 1h | buy | IWM | 2.60 | — | entry |
| 2026-11-23T16:40 | MACD cross · 1h | sell | BTC-USD | 4.61 | -0.11 | stop-loss |
| 2026-11-23T16:40 | Opening range 30m | buy | META | 9.51 | — | entry |
| 2026-11-23T16:40 | Opening range 30m | buy | COIN | 9.60 | — | entry |
| 2026-11-23T16:40 | Opening range 30m | sell | TQQQ | 9.47 | -0.28 | exit signal |
| 2026-11-23T16:40 | Opening range 30m | sell | QQQ | 9.65 | -0.10 | exit signal |
| 2026-11-23T16:40 | Opening range 15m | buy | META | 9.67 | — | entry |
| 2026-11-23T16:40 | Opening range 15m | sell | TQQQ | 8.49 | -0.25 | exit signal |
| 2026-11-23T16:40 | Opening range 15m | sell | QQQ | 8.65 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 16:45:05.000129+00:00 -> 2026-11-23 16:55:05.000129+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
