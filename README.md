# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T10:20:05.000157+00:00 · 66736 ticks

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
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 7845 decisions in 1569 calls, $0.1098 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T10:20 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-11-20T10:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-20T10:20 | 0 / 5 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.64 | 14.64 | 0 | — | 12.51 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.94 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.33 | 3.33 | 0 | — | 4.30 | 1.23 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.61 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.11 | -3.89 | 211 | 28.9 | -1.67 | -0.51 | -8.24 | 162 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.08 | -5.92 | 0 | — | -7.00 | -2.35 | -8.40 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.28 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.24 | -8.76 | 0 | — | -8.86 | -2.30 | -10.09 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.41 | -10.18 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 90.53 | -9.47 | 8 | 50.0 | -10.85 | -0.86 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.88 | -10.12 | 0 | — | -10.81 | -3.01 | -13.10 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.28 | -3.59 | -18.48 | 148 |
| 19 | Trend pullback · 1h | trend | 89.80 | -10.20 | 115 | 23.5 | -11.37 | -6.50 | -12.59 | 49 |
| 20 | Copy: Insider buying | copy | 89.37 | -10.63 | 55 | 40.0 | -6.73 | -1.27 | -14.79 | 65 |
| 21 | Daily: Bullish score | daily | 87.55 | -12.46 | 17 | 17.6 | -14.48 | -3.80 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.81 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.51 | -18.94 | 71 |
| 25 | Agent | meta | 85.36 | -14.64 | 233 | 36.9 | -13.89 | -6.32 | -16.51 | 214 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.49 | -3.98 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.37 | -18.63 | 194 | 27.8 | -26.95 | -8.20 | -28.86 | 196 |
| 28 | Connors RSI(2) · 1h | reversion | 80.44 | -19.56 | 217 | 40.6 | -15.15 | -6.75 | -15.33 | 71 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.34 | -21.55 | 73 |
| 30 | Donchian 55/20 · 1h | breakout | 78.59 | -21.41 | 79 | 12.7 | -28.41 | -8.83 | -29.80 | 85 |
| 31 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -23.03 | -6.45 | -25.33 | 145 |
| 32 | Opening range 15m | breakout | 77.33 | -22.67 | 547 | 31.8 | -21.22 | -6.47 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.93 | -25.07 | 2 | 0.0 | -23.95 | -3.42 | -27.37 | 1 |
| 34 | Ichimoku · 1h | trend | 73.64 | -26.36 | 107 | 14.0 | -30.75 | -9.41 | -32.08 | 109 |
| 35 | ADX DI cross · 1h | trend | 72.87 | -27.13 | 226 | 20.4 | -28.09 | -4.40 | -35.87 | 276 |
| 36 | Hold BTC | benchmark | 72.60 | -27.40 | 2 | 0.0 | -24.44 | -4.02 | -29.74 | 1 |
| 37 | Max aggression: 5-day momentum | meta | 72.27 | -27.73 | 22 | 40.9 | -53.68 | -3.76 | -58.33 | 21 |
| 38 | Stochastic reversion · 1h | reversion | 71.21 | -28.79 | 356 | 42.1 | -35.84 | -5.39 | -36.83 | 425 |
| 39 | Triple EMA stack · 1h | trend | 70.26 | -29.74 | 161 | 14.3 | -33.99 | -8.65 | -37.24 | 170 |
| 40 | Bollinger breakout · 1h | breakout | 70.04 | -29.96 | 195 | 21.5 | -32.97 | -8.48 | -36.32 | 216 |
| 41 | Supertrend · 1h | trend | 69.89 | -30.11 | 198 | 16.7 | -33.42 | -5.57 | -39.93 | 204 |
| 42 | EMA 20/50 cross · 1h | trend | 69.55 | -30.45 | 119 | 10.1 | -38.19 | -11.62 | -40.64 | 122 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.14 | -37.91 | 31 |
| 44 | MFI reversion · 1h | reversion | 68.67 | -31.33 | 468 | 33.5 | -30.54 | -4.58 | -32.50 | 173 |
| 45 | Heikin-Ashi · 1h | trend | 68.12 | -31.88 | 483 | 23.0 | -46.09 | -10.17 | -47.85 | 616 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.15 | -5.58 | -34.12 | 207 |
| 47 | RSI momentum · 1h | momentum | 67.81 | -32.19 | 184 | 14.1 | -39.32 | -9.00 | -41.77 | 202 |
| 48 | OBV trend · 1h | momentum | 67.74 | -32.26 | 315 | 19.4 | -38.07 | -10.05 | -41.22 | 240 |
| 49 | CCI reversion · 1h | reversion | 66.43 | -33.57 | 398 | 42.0 | -42.11 | -6.97 | -44.29 | 483 |
| 50 | Max aggression: 1-day momentum | meta | 65.56 | -34.44 | 33 | 27.3 | -47.44 | -3.22 | -57.50 | 38 |
| 51 | ROC + volume · 1h | momentum | 64.82 | -35.18 | 431 | 27.6 | -38.27 | -6.67 | -43.63 | 342 |
| 52 | Donchian 20/10 · 1h | breakout | 64.64 | -35.36 | 165 | 17.6 | -37.12 | -7.15 | -43.26 | 192 |
| 53 | MACD cross · 1h | trend | 64.61 | -35.39 | 433 | 21.5 | -48.13 | -9.47 | -48.47 | 494 |
| 54 | EMA 9/21 cross · 1h | trend | 62.10 | -37.90 | 291 | 11.3 | -40.95 | -7.94 | -47.32 | 323 |
| 55 | Bollinger reversion · 1h | reversion | 61.63 | -38.37 | 359 | 38.2 | -40.44 | -6.17 | -41.37 | 417 |
| 56 | Williams %R · 1h | reversion | 61.27 | -38.73 | 448 | 40.4 | -47.37 | -8.17 | -48.15 | 575 |
| 57 | Agent (ML meta-label) | meta | 58.02 | -41.98 | 1995 | 24.7 | -23.70 | -4.09 | -26.25 | 292 |
| 58 | RSI(14) reversion · 1h | reversion | 57.90 | -42.10 | 219 | 33.8 | -40.56 | -5.84 | -43.68 | 267 |
| 59 | Z-score reversion · 1h | reversion | 55.41 | -44.59 | 233 | 34.3 | -39.56 | -5.50 | -42.29 | 262 |
| 60 | Candlestick reversal · 1h | reversion | 54.40 | -45.60 | 583 | 26.6 | -49.50 | -9.13 | -49.78 | 670 |
| 61 | VWAP momentum · 1h | momentum | 53.76 | -46.24 | 1010 | 21.5 | -57.28 | -11.53 | -60.85 | 1195 |
| 62 | Three white soldiers | momentum | 52.80 | -47.20 | 610 | 14.3 | -51.36 | -22.59 | -51.36 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -47.70 | -99.16 | 5339 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.41 | -30.05 | -83.80 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.42 | -45.94 | -94.42 | 2456 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.84 | -34.66 | -90.90 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.13 | -43.89 | -92.13 | 2287 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -28.63 | -90.21 | 2022 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -50.32 | -98.20 | 3485 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -52.56 | -96.85 | 3396 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.90 | -39.05 | -93.91 | 2219 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.41 | -34.42 | -83.44 | 1575 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.64 | -56.06 | -99.64 | 6236 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.91 | -45.68 | -92.92 | 2526 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -36.01 | -94.64 | 3162 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -70.22 | -99.83 | 6238 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.32 | -46.73 | -93.32 | 2281 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.59 | -25.27 | -78.59 | 1633 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.86 | -58.91 | -97.86 | 3385 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -56.39 | -99.10 | 5028 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.68 | -29.14 | -70.70 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.91 | -54.97 | -94.92 | 2716 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.01 | -39.28 | -86.01 | 1705 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -69.31 | -99.72 | 6472 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.09 | -31.23 | -91.13 | 2409 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.33 | -19.09 | -80.41 | 1873 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.85 | -37.36 | -91.85 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.72 | -46.07 | -97.72 | 3980 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.21 | -52.98 | -90.22 | 2178 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.75 | -32.05 | -67.75 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.51 | -28.63 | -74.79 | 1206 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.44 | -18.59 | -82.66 | 1801 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.61 | -45.32 | -97.61 | 4371 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -105.48 | -99.95 | 8415 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T10:00 | MACD cross · 1h | buy | ETH-USD | 5.79 | — | rebalance up |
| 2026-11-20T10:00 | MACD cross · 1h | sell | XRP-USD | 7.04 | -0.16 | exit signal |
| 2026-11-20T10:00 | MACD cross · 1h | sell | BTC-USD | 5.83 | -0.05 | exit signal |
| 2026-11-20T09:00 | VWAP momentum · 1h | buy | ETH-USD | 4.42 | — | rebalance up |
| 2026-11-20T09:00 | VWAP momentum · 1h | sell | XRP-USD | 8.90 | -0.10 | exit signal |
| 2026-11-20T09:00 | VWAP momentum · 1h | sell | SOL-USD | 10.73 | -0.09 | exit signal |
| 2026-11-20T09:00 | VWAP momentum · 1h | sell | DOGE-USD | 8.93 | -0.10 | exit signal |
| 2026-11-20T09:00 | MACD cross · 1h | buy | ETH-USD | 1.40 | — | entry signal |
| 2026-11-20T09:00 | MACD cross · 1h | buy | BTC-USD | 5.88 | — | entry signal |
| 2026-11-20T08:55 | Three white soldiers | sell | ETH-USD | 13.16 | -0.05 | exit signal |
| 2026-11-20T08:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.95 | — | entry signal |
| 2026-11-20T08:00 | Candlestick reversal · 1h | sell | XRP-USD | 5.91 | -0.03 | exit signal |
| 2026-11-20T08:00 | VWAP momentum · 1h | buy | SOL-USD | 7.15 | — | rebalance up |
| 2026-11-20T08:00 | VWAP momentum · 1h | sell | BTC-USD | 8.96 | -0.07 | exit signal |
| 2026-11-20T07:50 | Three white soldiers | buy | ETH-USD | 13.21 | — | entry signal |
| 2026-11-20T07:00 | MACD cross · 1h | buy | XRP-USD | 7.20 | — | entry signal |
| 2026-11-20T06:00 | MFI reversion · 1h | buy | DOGE-USD | 3.48 | — | entry signal |
| 2026-11-20T06:00 | MFI reversion · 1h | sell | BTC-USD | 3.48 | -0.02 | rebalance down |
| 2026-11-20T06:00 | Bollinger reversion · 1h | buy | DOGE-USD | 2.76 | — | entry |
| 2026-11-20T06:00 | Bollinger reversion · 1h | sell | XRP-USD | 2.76 | 0.04 | exit signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | SOL-USD | 3.67 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | ETH-USD | 9.03 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.03 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | BTC-USD | 9.03 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | sell | XRP-USD | 4.58 | 0.00 | rebalance down |
| 2026-11-20T05:00 | VWAP momentum · 1h | sell | BTC-USD | 13.34 | -0.26 | exit signal |
| 2026-11-20T04:36 | MFI reversion · 1h | buy | XRP-USD | 2.90 | — | rebalance up |
| 2026-11-20T04:36 | MFI reversion · 1h | buy | BTC-USD | 5.72 | — | rebalance up |
| 2026-11-20T04:36 | MFI reversion · 1h | sell | ETH-USD | 8.63 | -0.29 | stop-loss |
| 2026-11-20T04:00 | Candlestick reversal · 1h | buy | XRP-USD | 5.94 | — | entry signal |
| 2026-11-20T04:00 | VWAP momentum · 1h | buy | XRP-USD | 13.58 | — | entry signal |
| 2026-11-20T03:00 | VWAP momentum · 1h | buy | BTC-USD | 13.60 | — | entry signal |
| 2026-11-20T02:30 | Bollinger reversion · 1h | buy | XRP-USD | 2.73 | — | entry |
| 2026-11-20T02:30 | Bollinger reversion · 1h | buy | SOL-USD | 5.92 | — | rebalance up |
| 2026-11-20T02:30 | Bollinger reversion · 1h | sell | DOGE-USD | 8.65 | -0.23 | stop-loss |
| 2026-11-20T02:10 | Williams %R · 1h | buy | BTC-USD | 3.41 | — | entry |
| 2026-11-20T02:10 | Williams %R · 1h | sell | DOGE-USD | 3.34 | -0.11 | stop-loss |
| 2026-11-20T02:00 | Candlestick reversal · 1h | sell | XRP-USD | 1.00 | -0.01 | exit signal |
| 2026-11-20T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 4.94 | -0.02 | exit signal |
| 2026-11-20T02:00 | VWAP momentum · 1h | sell | BTC-USD | 13.44 | -0.21 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 10:20:05.000157+00:00 -> 2026-11-20 10:30:05.000157+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
