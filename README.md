# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T07:10:05.000174+00:00 · 36375 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, IAM 12%, APLD 12%, BPRE 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 5247 decisions in 1050 calls, $0.0735 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T07:10 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-26T07:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-26T07:10 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 3.95 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 2.30 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.01 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.81 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.47 | -2.99 | -13.74 | 156 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 5.84 | 2.80 | -1.76 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.16 | 0 | — | -0.72 | -0.41 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.01 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 192 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 1.07 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.38 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 94.68 | -5.32 | 0 | — | -0.42 | 0.48 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.16 | -5.84 | 25 | 40.0 | -16.03 | -3.05 | -21.73 | 58 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.62 | -6.95 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.83 | -3.56 | -16.76 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.21 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.70 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.65 | -8.35 | 119 | 25.2 | -22.89 | -5.61 | -23.85 | 253 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.18 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.34 | -9.66 | 112 | 17.9 | -12.65 | -2.57 | -15.15 | 260 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.00 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.85 | -2.85 | -17.00 | 114 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.76 | -7.81 | -12.35 | 206 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.84 | 0 | — | -5.31 | -0.75 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.74 | -11.26 | 106 | 27.4 | -12.35 | -2.41 | -16.41 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.57 | -4.29 | -14.77 | 93 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -21.01 | -3.95 | -22.47 | 392 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -23.06 | -4.84 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -23.49 | -4.77 | -24.06 | 137 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.44 | -17.87 | 703 |
| 40 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 41 | RSI momentum · 1h | momentum | 85.30 | -14.71 | 102 | 15.7 | -23.07 | -4.96 | -23.57 | 216 |
| 42 | Supertrend · 1h | trend | 84.46 | -15.54 | 113 | 14.2 | -26.58 | -5.87 | -27.09 | 215 |
| 43 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -24.15 | -5.05 | -24.49 | 109 |
| 44 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -27.27 | -5.48 | -28.32 | 211 |
| 45 | Z-score reversion · 1h | reversion | 83.34 | -16.66 | 112 | 33.0 | -15.82 | -2.67 | -21.48 | 206 |
| 46 | MACD cross · 1h | trend | 83.09 | -16.91 | 233 | 22.3 | -23.96 | -4.69 | -27.96 | 465 |
| 47 | MFI reversion · 1h | reversion | 81.50 | -18.50 | 262 | 31.7 | -17.42 | -2.78 | -20.66 | 148 |
| 48 | MACD zero-line · 1h | trend | 81.17 | -18.84 | 106 | 15.1 | -22.09 | -4.59 | -25.51 | 219 |
| 49 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -32.05 | -7.03 | -32.91 | 304 |
| 50 | Williams %R · 1h | reversion | 80.94 | -19.06 | 213 | 44.1 | -35.62 | -6.21 | -36.17 | 538 |
| 51 | Donchian 20/10 · 1h | breakout | 80.88 | -19.12 | 98 | 19.4 | -24.54 | -4.70 | -27.41 | 217 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -30.38 | -6.20 | -31.49 | 374 |
| 53 | CCI reversion · 1h | reversion | 79.70 | -20.30 | 205 | 42.0 | -25.91 | -3.83 | -28.08 | 465 |
| 54 | Three white soldiers | momentum | 79.30 | -20.70 | 289 | 19.0 | -44.39 | -20.35 | -44.39 | 596 |
| 55 | Agent (ML meta-label) | meta | 79.14 | -20.86 | 879 | 18.7 | -19.31 | -3.62 | -19.51 | 356 |
| 56 | Heikin-Ashi · 1h | trend | 78.00 | -22.00 | 279 | 22.9 | -43.68 | -10.04 | -44.10 | 658 |
| 57 | ROC + volume · 1h | momentum | 77.86 | -22.14 | 241 | 23.7 | -29.94 | -5.90 | -31.54 | 378 |
| 58 | Candlestick reversal · 1h | reversion | 76.73 | -23.27 | 265 | 27.9 | -34.22 | -6.42 | -34.53 | 556 |
| 59 | RSI(14) reversion · 1h | reversion | 76.56 | -23.44 | 99 | 23.2 | -14.68 | -2.68 | -24.48 | 190 |
| 60 | EMA 9/21 cross · 1h | trend | 76.23 | -23.77 | 169 | 11.2 | -31.55 | -6.47 | -34.40 | 327 |
| 61 | VWAP momentum · 1h | momentum | 75.17 | -24.83 | 532 | 20.9 | -50.97 | -11.65 | -51.24 | 1236 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.95 | -44.05 | 725 | 22.1 | -74.86 | -27.11 | -74.86 | 1551 |
| 64 | Volume breakout | breakout | 54.47 | -45.53 | 444 | 12.4 | -62.61 | -26.08 | -62.64 | 787 |
| 65 | Donchian 55/20 | breakout | 51.84 | -48.16 | 581 | 18.9 | -71.96 | -23.58 | -71.96 | 1258 |
| 66 | Squeeze breakout | breakout | 51.35 | -48.65 | 577 | 13.7 | -67.58 | -28.69 | -67.58 | 1169 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -45.24 | -98.90 | 5131 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.46 | -23.41 | -79.47 | 1423 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.91 | -45.48 | -93.91 | 2527 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -30.56 | -89.29 | 1911 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.49 | -38.04 | -91.49 | 2328 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.43 | -29.89 | -90.44 | 2159 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -52.99 | -97.91 | 3524 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -57.70 | -96.18 | 3361 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.21 | -35.38 | -94.27 | 2465 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.94 | -35.24 | -82.94 | 1691 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -55.30 | -99.46 | 5803 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.62 | -41.98 | -92.62 | 2606 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.88 | -95.50 | 3381 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -79.94 | -99.79 | 6193 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.39 | -44.32 | -92.39 | 2344 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -62.92 | -97.69 | 3560 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.71 | -60.66 | -98.72 | 4813 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -55.64 | -94.61 | 2774 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.22 | -38.80 | -84.22 | 1788 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -66.48 | -99.61 | 6287 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.73 | -29.47 | -88.78 | 2250 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.45 | -19.74 | -78.50 | 1713 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.95 | -37.69 | -90.96 | 2281 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -48.04 | -96.41 | 3827 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.04 | -50.41 | -90.06 | 2129 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.00 | -17.84 | -77.08 | 1607 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.48 | -47.92 | -96.49 | 4193 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.02 | -99.92 | 8257 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T07:05 | Agent (ML meta-label) | buy | DOGE-USD | 4.40 | — | entry |
| 2026-10-26T06:25 | Donchian 55/20 | sell | DOGE-USD | 12.87 | -0.12 | stop-loss |
| 2026-10-26T06:10 | Squeeze breakout | sell | DOGE-USD | 12.79 | -0.07 | stop-loss |
| 2026-10-26T06:10 | Squeeze breakout | sell | BTC-USD | 12.81 | -0.05 | exit signal |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | XRP-USD | 5.09 | -0.05 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | SOL-USD | 12.62 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | ETH-USD | 12.62 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | DOGE-USD | 10.11 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | BTC-USD | 10.13 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-26T06:00 | Z-score reversion · 1h | buy | BTC-USD | 6.37 | — | rebalance up |
| 2026-10-26T06:00 | Z-score reversion · 1h | sell | DOGE-USD | 6.90 | -0.08 | exit signal |
| 2026-10-26T06:00 | VWAP momentum · 1h | buy | BTC-USD | 6.83 | — | entry signal |
| 2026-10-26T06:00 | MACD cross · 1h | buy | DOGE-USD | 13.86 | — | entry signal |
| 2026-10-26T05:40 | EMA 20/50 cross | buy | XRP-USD | 5.13 | — | entry signal |
| 2026-10-26T05:40 | EMA 20/50 cross | sell | DOGE-USD | 2.55 | -0.01 | rebalance down |
| 2026-10-26T05:40 | EMA 20/50 cross | sell | BTC-USD | 2.54 | -0.01 | rebalance down |
| 2026-10-26T05:25 | EMA 20/50 cross | buy | ETH-USD | 12.73 | — | entry signal |
| 2026-10-26T05:10 | Donchian 55/20 | buy | DOGE-USD | 12.99 | — | entry |
| 2026-10-26T05:10 | EMA 20/50 cross | buy | SOL-USD | 12.73 | — | entry signal |
| 2026-10-26T05:00 | CCI reversion · 1h | buy | BTC-USD | 3.35 | — | entry signal |
| 2026-10-26T05:00 | Z-score reversion · 1h | buy | BTC-USD | 1.21 | — | entry signal |
| 2026-10-26T05:00 | Candlestick reversal · 1h | buy | ETH-USD | 4.64 | — | entry signal |
| 2026-10-26T05:00 | EMA 20/50 cross | buy | DOGE-USD | 12.75 | — | entry signal |
| 2026-10-26T05:00 | EMA 20/50 cross | buy | BTC-USD | 12.75 | — | entry signal |
| 2026-10-26T04:35 | Squeeze breakout | buy | DOGE-USD | 12.86 | — | entry signal |
| 2026-10-26T04:15 | Squeeze breakout | buy | BTC-USD | 12.87 | — | entry signal |
| 2026-10-26T03:55 | Z-score reversion · 1h | sell | ETH-USD | 1.21 | -0.04 | stop-loss |
| 2026-10-26T03:00 | Donchian 20/10 · 1h | sell | XRP-USD | 19.93 | -0.39 | exit signal |
| 2026-10-26T03:00 | ROC + volume · 1h | sell | SOL-USD | 19.21 | -0.34 | exit signal |
| 2026-10-26T03:00 | Supertrend · 1h | sell | XRP-USD | 20.95 | -0.37 | exit signal |
| 2026-10-26T02:40 | CCI reversion · 1h | sell | ETH-USD | 3.35 | -0.11 | stop-loss |
| 2026-10-26T02:25 | Agent (ML meta-label) | sell | ETH-USD | 4.13 | -0.04 | selected signal exited |
| 2026-10-26T02:25 | Agent (ML meta-label) | sell | DOGE-USD | 4.14 | -0.03 | selected signal exited |
| 2026-10-26T02:05 | Agent (ML meta-label) | buy | ETH-USD | 4.17 | — | entry |
| 2026-10-26T02:05 | Agent (ML meta-label) | buy | DOGE-USD | 4.17 | — | entry |
| 2026-10-26T02:00 | Candlestick reversal · 1h | sell | DOGE-USD | 4.64 | -0.06 | exit signal |
| 2026-10-26T02:00 | MACD cross · 1h | sell | SOL-USD | 9.19 | -0.11 | exit signal |
| 2026-10-26T02:00 | MACD cross · 1h | sell | DOGE-USD | 10.33 | -0.15 | exit signal |
| 2026-10-26T01:42 | Agent (ML meta-label) | sell | ETH-USD | 4.32 | -0.04 | selected signal exited |
| 2026-10-26T01:35 | Agent (ML meta-label) | buy | ETH-USD | 4.36 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 07:10:05.000174+00:00 -> 2026-10-26 07:20:05.000174+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
