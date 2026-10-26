# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T02:40:05.000133+00:00 · 36164 ticks

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

Today: 2085 decisions in 417 calls, $0.0292 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T02:40 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-26T02:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-26T02:40 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Bollinger reversion | BITX | 2.12 | +2.39% | 13 |
| VWAP momentum | PLTR | 1.73 | +4.99% | 6 |
| Stochastic reversion | BITX | 1.67 | +3.43% | 12 |
| RSI(14) reversion | TSLA | 1.52 | +3.62% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.42 | 6.42 | 0 | — | 7.97 | 3.95 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 2.30 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.02 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.75 | 0.75 | 0 | — | 3.44 | 1.81 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.04 | -3.11 | -13.74 | 157 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 6.21 | 2.99 | -1.37 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.77 | -2.23 | 0 | — | -0.72 | -0.41 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.01 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.11 | -3.89 | 120 | 30.8 | -2.30 | -1.33 | -6.22 | 192 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 1.07 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.62 | -4.38 | 0 | — | -0.88 | -0.38 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.48 | -5.52 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 18 | Copy: Insider buying | copy | 94.06 | -5.94 | 25 | 40.0 | -17.34 | -3.33 | -21.47 | 61 |
| 19 | Hold BTC | benchmark | 94.01 | -5.99 | 0 | — | -1.06 | 0.38 | -9.28 | 1 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.76 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.74 | -6.26 | 95 | 23.2 | -21.62 | -6.95 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.13 | -6.87 | 48 | 16.7 | -15.84 | -3.55 | -16.92 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.21 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Daily: Momentum burst | daily | 91.68 | -8.32 | 10 | 10.0 | -17.52 | -3.70 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.63 | -8.37 | 119 | 25.2 | -22.70 | -5.61 | -23.48 | 252 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.18 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.33 | -9.67 | 112 | 17.9 | -12.59 | -2.56 | -15.15 | 260 |
| 30 | Daily: Bullish score | daily | 89.49 | -10.51 | 9 | 0.0 | -8.04 | -1.00 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -14.69 | -2.97 | -17.81 | 114 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.76 | -7.81 | -12.35 | 206 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.10 | -10.90 | 0 | — | -5.31 | -0.75 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.73 | -11.27 | 106 | 27.4 | -12.35 | -2.41 | -16.41 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.57 | -4.29 | -14.77 | 93 |
| 36 | Stochastic reversion · 1h | reversion | 87.12 | -12.88 | 186 | 45.2 | -21.08 | -3.91 | -22.47 | 393 |
| 37 | Keltner breakout · 1h | breakout | 86.30 | -13.70 | 73 | 23.3 | -23.06 | -4.84 | -24.23 | 189 |
| 38 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.06 | -4.43 | -17.87 | 703 |
| 39 | EMA 20/50 cross · 1h | trend | 86.12 | -13.88 | 71 | 11.3 | -23.39 | -4.75 | -23.88 | 137 |
| 40 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 41 | RSI momentum · 1h | momentum | 85.26 | -14.73 | 102 | 15.7 | -23.42 | -5.05 | -23.76 | 216 |
| 42 | Supertrend · 1h | trend | 84.49 | -15.51 | 112 | 14.3 | -26.19 | -5.75 | -27.03 | 215 |
| 43 | Ichimoku · 1h | trend | 83.90 | -16.10 | 65 | 12.3 | -24.15 | -5.05 | -24.49 | 109 |
| 44 | Triple EMA stack · 1h | trend | 83.41 | -16.59 | 98 | 15.3 | -26.82 | -5.34 | -28.26 | 211 |
| 45 | Z-score reversion · 1h | reversion | 83.26 | -16.74 | 110 | 33.6 | -15.79 | -2.66 | -21.48 | 204 |
| 46 | MACD cross · 1h | trend | 83.18 | -16.82 | 233 | 22.3 | -25.22 | -5.13 | -27.78 | 463 |
| 47 | MFI reversion · 1h | reversion | 81.45 | -18.55 | 262 | 31.7 | -16.12 | -2.49 | -20.54 | 148 |
| 48 | MACD zero-line · 1h | trend | 81.15 | -18.85 | 106 | 15.1 | -22.59 | -4.73 | -25.51 | 219 |
| 49 | OBV trend · 1h | momentum | 81.04 | -18.95 | 203 | 17.2 | -31.48 | -6.84 | -32.82 | 304 |
| 50 | Donchian 20/10 · 1h | breakout | 80.92 | -19.08 | 97 | 19.6 | -24.48 | -4.69 | -27.35 | 217 |
| 51 | Williams %R · 1h | reversion | 80.88 | -19.12 | 213 | 44.1 | -35.43 | -6.17 | -36.03 | 535 |
| 52 | Bollinger reversion · 1h | reversion | 80.14 | -19.86 | 171 | 34.5 | -30.91 | -6.32 | -31.39 | 371 |
| 53 | CCI reversion · 1h | reversion | 79.64 | -20.36 | 205 | 42.0 | -26.51 | -3.91 | -28.08 | 462 |
| 54 | Three white soldiers | momentum | 79.30 | -20.70 | 289 | 19.0 | -44.43 | -20.39 | -44.43 | 597 |
| 55 | Agent (ML meta-label) | meta | 79.11 | -20.89 | 879 | 18.7 | -17.44 | -3.35 | -18.28 | 352 |
| 56 | Heikin-Ashi · 1h | trend | 78.00 | -22.00 | 279 | 22.9 | -43.68 | -10.04 | -44.10 | 658 |
| 57 | ROC + volume · 1h | momentum | 77.89 | -22.11 | 240 | 23.8 | -30.05 | -5.91 | -31.64 | 378 |
| 58 | Candlestick reversal · 1h | reversion | 76.70 | -23.30 | 265 | 27.9 | -34.45 | -6.47 | -35.07 | 554 |
| 59 | RSI(14) reversion · 1h | reversion | 76.34 | -23.66 | 99 | 23.2 | -15.94 | -2.95 | -24.42 | 193 |
| 60 | EMA 9/21 cross · 1h | trend | 76.20 | -23.80 | 169 | 11.2 | -31.55 | -6.47 | -34.40 | 327 |
| 61 | VWAP momentum · 1h | momentum | 75.15 | -24.85 | 532 | 20.9 | -50.74 | -11.56 | -50.97 | 1233 |
| 62 | Max aggression: 1-day momentum | meta | 67.36 | -32.64 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.95 | -44.05 | 725 | 22.1 | -74.84 | -26.88 | -74.84 | 1551 |
| 64 | Volume breakout | breakout | 54.47 | -45.53 | 444 | 12.4 | -62.85 | -26.06 | -62.85 | 789 |
| 65 | Donchian 55/20 | breakout | 51.96 | -48.04 | 580 | 19.0 | -71.88 | -23.46 | -71.88 | 1257 |
| 66 | Squeeze breakout | breakout | 51.47 | -48.53 | 575 | 13.7 | -67.63 | -28.49 | -67.63 | 1168 |
| 67 | EMA 20/50 cross | trend | 51.00 | -49.00 | 639 | 20.2 | -79.13 | -23.02 | -79.13 | 1416 |
| 68 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -44.67 | -98.87 | 5115 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -44.24 | -93.83 | 2520 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -30.18 | -89.25 | 1907 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.42 | -37.47 | -91.42 | 2324 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.43 | -29.89 | -90.44 | 2159 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -51.81 | -97.91 | 3520 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -56.00 | -96.12 | 3357 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.15 | -35.47 | -94.20 | 2462 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.91 | -35.12 | -82.92 | 1690 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.45 | -54.16 | -99.45 | 5801 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.64 | -41.26 | -92.64 | 2604 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.88 | -95.50 | 3381 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -78.17 | -99.79 | 6190 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.38 | -43.62 | -92.38 | 2341 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -61.60 | -97.67 | 3552 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.72 | -59.00 | -98.72 | 4811 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -55.18 | -94.64 | 2775 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.25 | -38.55 | -84.25 | 1788 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.70 | -99.61 | 6285 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.94 | -29.34 | -88.94 | 2253 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.43 | -19.74 | -78.52 | 1713 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.98 | -37.55 | -91.02 | 2283 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -47.54 | -96.42 | 3824 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.94 | -48.38 | -89.94 | 2120 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.34 | -17.76 | -77.40 | 1603 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.49 | -47.17 | -96.49 | 4193 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -91.24 | -99.92 | 8247 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-26T01:25 | Agent (ML meta-label) | sell | ETH-USD | 4.40 | -0.01 | selected signal exited |
| 2026-10-26T01:10 | Agent (ML meta-label) | buy | ETH-USD | 4.41 | — | entry |
| 2026-10-26T01:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 12.70 | -0.09 | exit signal |
| 2026-10-26T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.69 | — | entry |
| 2026-10-26T00:00 | Candlestick reversal · 1h | sell | BTC-USD | 4.69 | -0.04 | exit signal |
| 2026-10-26T00:00 | MACD cross · 1h | sell | ETH-USD | 10.35 | -0.12 | exit signal |
| 2026-10-25T23:00 | EMA 20/50 cross | sell | SOL-USD | 12.69 | -0.09 | exit signal |
| 2026-10-25T22:55 | EMA 20/50 cross | buy | SOL-USD | 12.77 | — | entry signal |
| 2026-10-25T22:15 | Volume breakout | sell | SOL-USD | 13.54 | -0.15 | stop-loss |
| 2026-10-25T22:15 | Volume breakout | sell | BTC-USD | 13.55 | -0.13 | stop-loss |
| 2026-10-25T22:15 | Squeeze breakout | sell | SOL-USD | 12.80 | -0.14 | stop-loss |
| 2026-10-25T22:15 | Squeeze breakout | sell | BTC-USD | 12.81 | -0.12 | stop-loss |
| 2026-10-25T22:05 | Volume breakout | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-10-25T22:05 | Volume breakout | buy | BTC-USD | 13.69 | — | entry signal |
| 2026-10-25T22:05 | Squeeze breakout | buy | SOL-USD | 12.93 | — | entry signal |
| 2026-10-25T22:05 | Squeeze breakout | buy | BTC-USD | 12.93 | — | entry signal |
| 2026-10-25T22:00 | RSI momentum · 1h | sell | XRP-USD | 21.08 | -0.33 | exit signal |
| 2026-10-25T22:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.87 | -0.09 | exit signal |
| 2026-10-25T22:00 | Parabolic SAR · 1h | sell | XRP-USD | 22.61 | -0.40 | exit signal |
| 2026-10-25T22:00 | MACD cross · 1h | sell | XRP-USD | 3.98 | -0.07 | exit signal |
| 2026-10-25T22:00 | MACD cross · 1h | sell | BTC-USD | 10.36 | -0.11 | exit signal |
| 2026-10-25T22:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 4.25 | — | rebalance up |
| 2026-10-25T22:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 9.46 | -0.11 | exit signal |
| 2026-10-25T22:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 8.38 | -0.13 | exit signal |
| 2026-10-25T22:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 2.94 | -0.04 | exit signal |
| 2026-10-25T21:15 | EMA 20/50 cross | sell | SOL-USD | 12.75 | -0.05 | exit signal |
| 2026-10-25T21:15 | EMA 20/50 cross | sell | DOGE-USD | 10.23 | -0.00 | exit signal |
| 2026-10-25T21:05 | EMA 9/21 cross · 1h | buy | DOGE-USD | 2.97 | — | entry |
| 2026-10-25T21:00 | ROC + volume · 1h | buy | SOL-USD | 19.55 | — | entry signal |
| 2026-10-25T21:00 | ADX DI cross · 1h | sell | SOL-USD | 22.53 | -0.20 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 02:40:05.000133+00:00 -> 2026-10-26 02:50:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
