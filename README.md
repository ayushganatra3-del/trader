# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T00:55:05.000125+00:00 · 44424 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.52 (-8.48%)

Closed trades 130, win rate 40.8%, fees £3.76, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-30 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 780 decisions in 156 calls, $0.0110 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T00:55 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-02T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T00:55 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Bollinger reversion | AMZN | 2.17 | +2.35% | 10 |
| Stochastic reversion | ETHU | 2.10 | +5.34% | 11 |
| Z-score reversion | BITX | 2.10 | +6.37% | 7 |
| Williams %R | MSTR | 2.00 | +3.35% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.51 | 6.51 | 0 | — | 7.73 | 3.79 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.63 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.05 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.89 | -0.11 | 96 | 44.8 | -12.42 | -3.45 | -12.61 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.18 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.19 | -2.81 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.18 | -7.82 | 0 | — | -0.80 | 0.04 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -17.74 | -6.53 | -18.02 | 86 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 23 | Parabolic SAR · 1h | trend | 90.92 | -9.08 | 141 | 28.4 | -16.75 | -3.82 | -20.27 | 249 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.01 | -9.99 | 59 | 23.7 | -6.27 | -1.72 | -12.93 | 89 |
| 26 | Copy: Insider buying | copy | 89.48 | -10.52 | 34 | 35.3 | -22.37 | -4.52 | -23.61 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 88.89 | -11.11 | 58 | 13.8 | -17.25 | -3.81 | -18.18 | 105 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -16.04 | -3.29 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.46 | -14.54 | 224 | 47.3 | -18.07 | -3.16 | -24.77 | 392 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -15.41 | -2.92 | -20.33 | 257 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.27 | -4.51 | -25.77 | 184 |
| 35 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.48 | -6.87 | -21.89 | 152 |
| 36 | Bollinger breakout · 1h | breakout | 83.12 | -16.88 | 134 | 26.1 | -15.26 | -2.79 | -21.61 | 241 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 39 | MFI reversion · 1h | reversion | 82.36 | -17.64 | 295 | 31.9 | -16.21 | -2.54 | -20.24 | 151 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.14 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.27 | -19.73 | 137 | 13.1 | -26.04 | -4.75 | -29.38 | 216 |
| 43 | EMA 20/50 cross · 1h | trend | 79.69 | -20.31 | 89 | 11.2 | -23.13 | -4.35 | -26.76 | 137 |
| 44 | CCI reversion · 1h | reversion | 79.54 | -20.46 | 253 | 46.2 | -25.49 | -3.96 | -27.91 | 446 |
| 45 | MACD cross · 1h | trend | 79.29 | -20.71 | 288 | 24.3 | -27.38 | -4.81 | -32.86 | 464 |
| 46 | RSI momentum · 1h | momentum | 79.11 | -20.89 | 130 | 13.1 | -26.29 | -4.71 | -30.16 | 215 |
| 47 | Williams %R · 1h | reversion | 78.79 | -21.21 | 258 | 46.9 | -34.25 | -6.08 | -34.88 | 521 |
| 48 | MACD zero-line · 1h | trend | 78.42 | -21.58 | 134 | 15.7 | -23.25 | -4.65 | -27.62 | 213 |
| 49 | Z-score reversion · 1h | reversion | 78.12 | -21.88 | 135 | 33.3 | -17.30 | -2.68 | -22.55 | 207 |
| 50 | Bollinger reversion · 1h | reversion | 77.98 | -22.02 | 201 | 37.3 | -29.57 | -6.19 | -30.74 | 373 |
| 51 | Heikin-Ashi · 1h | trend | 77.93 | -22.07 | 340 | 23.5 | -40.84 | -8.77 | -42.23 | 661 |
| 52 | Triple EMA stack · 1h | trend | 77.74 | -22.26 | 121 | 14.9 | -30.53 | -5.65 | -33.51 | 208 |
| 53 | OBV trend · 1h | momentum | 77.41 | -22.59 | 234 | 17.5 | -33.09 | -6.66 | -36.12 | 301 |
| 54 | Donchian 20/10 · 1h | breakout | 76.00 | -24.00 | 117 | 20.5 | -26.12 | -4.53 | -29.81 | 216 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -28.55 | -5.00 | -32.73 | 379 |
| 56 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -33.79 | -1.99 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 72.88 | -27.12 | 122 | 26.2 | -21.81 | -3.85 | -26.17 | 197 |
| 58 | VWAP momentum · 1h | momentum | 72.03 | -27.97 | 662 | 22.4 | -51.40 | -10.85 | -51.42 | 1239 |
| 59 | Candlestick reversal · 1h | reversion | 71.24 | -28.75 | 328 | 27.7 | -34.70 | -6.83 | -35.71 | 549 |
| 60 | Three white soldiers | momentum | 71.09 | -28.91 | 397 | 16.4 | -45.05 | -20.76 | -45.21 | 623 |
| 61 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -18.95 | -3.38 | -20.87 | 340 |
| 62 | EMA 9/21 cross · 1h | trend | 70.71 | -29.29 | 210 | 10.0 | -33.97 | -6.31 | -37.32 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -42.76 | -98.89 | 5227 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.66 | -23.83 | -79.67 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.60 | -44.82 | -93.64 | 2541 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -31.37 | -88.93 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -38.10 | -91.35 | 2357 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.43 | -30.64 | -90.44 | 2249 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -52.05 | -97.77 | 3532 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -58.25 | -96.28 | 3415 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.85 | -34.74 | -93.85 | 2474 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.14 | -33.90 | -82.16 | 1695 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -54.14 | -99.48 | 5927 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.92 | -43.36 | -92.93 | 2636 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -35.97 | -95.49 | 3459 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -73.65 | -99.78 | 6249 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -44.94 | -91.95 | 2314 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.94 | -26.48 | -74.98 | 1567 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -59.30 | -97.73 | 3581 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.59 | -98.65 | 4868 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.65 | -27.71 | -68.74 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -53.37 | -94.65 | 2792 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.59 | -37.89 | -84.64 | 1811 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.44 | -99.62 | 6382 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.18 | -30.40 | -88.22 | 2259 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.16 | -19.66 | -77.30 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.31 | -36.98 | -90.37 | 2249 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -50.76 | -96.43 | 3845 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.79 | -53.60 | -89.84 | 2158 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.13 | -25.12 | -64.15 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.84 | -25.51 | -73.97 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.09 | -18.88 | -76.36 | 1595 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.78 | -49.79 | -96.78 | 4258 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -91.67 | -99.93 | 8380 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T00:00 | Z-score reversion · 1h | buy | SOL-USD | 13.04 | — | entry signal |
| 2026-11-02T00:00 | Bollinger reversion · 1h | sell | ETH-USD | 3.90 | -0.00 | exit signal |
| 2026-11-02T00:00 | Candlestick reversal · 1h | buy | XRP-USD | 7.14 | — | entry signal |
| 2026-11-02T00:00 | Candlestick reversal · 1h | buy | SOL-USD | 7.14 | — | entry signal |
| 2026-11-02T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 7.14 | — | entry signal |
| 2026-11-02T00:00 | Bollinger breakout · 1h | buy | BTC-USD | 20.81 | — | entry signal |
| 2026-11-02T00:00 | Donchian 55/20 · 1h | buy | BTC-USD | 22.26 | — | entry signal |
| 2026-11-02T00:00 | OBV trend · 1h | buy | ETH-USD | 19.38 | — | entry signal |
| 2026-11-02T00:00 | VWAP momentum · 1h | buy | ETH-USD | 10.32 | — | entry signal |
| 2026-11-02T00:00 | VWAP momentum · 1h | buy | DOGE-USD | 10.32 | — | entry signal |
| 2026-11-02T00:00 | VWAP momentum · 1h | buy | BTC-USD | 10.32 | — | entry signal |
| 2026-11-02T00:00 | Parabolic SAR · 1h | buy | ETH-USD | 22.79 | — | entry signal |
| 2026-11-02T00:00 | Parabolic SAR · 1h | buy | BTC-USD | 22.79 | — | entry signal |
| 2026-11-02T00:00 | Triple EMA stack · 1h | buy | ETH-USD | 19.46 | — | entry signal |
| 2026-11-02T00:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 19.95 | — | entry signal |
| 2026-11-02T00:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 17.71 | — | entry signal |
| 2026-11-01T23:00 | Candlestick reversal · 1h | sell | XRP-USD | 7.09 | -0.07 | exit signal |
| 2026-11-01T23:00 | Triple EMA stack · 1h | sell | ETH-USD | 19.31 | -0.20 | exit signal |
| 2026-11-01T23:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 14.18 | -0.01 | exit signal |
| 2026-11-01T22:25 | Z-score reversion · 1h | sell | SOL-USD | 12.85 | -0.23 | stop-loss |
| 2026-11-01T22:25 | Candlestick reversal · 1h | sell | SOL-USD | 7.04 | -0.12 | stop-loss |
| 2026-11-01T22:20 | Williams %R · 1h | buy | DOGE-USD | 4.01 | — | rebalance up |
| 2026-11-01T22:20 | Williams %R · 1h | sell | SOL-USD | 15.13 | -0.30 | stop-loss |
| 2026-11-01T22:00 | CCI reversion · 1h | buy | ETH-USD | 12.83 | — | entry signal |
| 2026-11-01T22:00 | CCI reversion · 1h | sell | SOL-USD | 6.30 | -0.18 | rebalance down |
| 2026-11-01T22:00 | CCI reversion · 1h | sell | DOGE-USD | 6.53 | -0.10 | rebalance down |
| 2026-11-01T22:00 | Z-score reversion · 1h | buy | SOL-USD | 13.08 | — | entry signal |
| 2026-11-01T21:55 | Three white soldiers | sell | SOL-USD | 17.71 | -0.13 | exit signal |
| 2026-11-01T21:55 | Three white soldiers | sell | BTC-USD | 17.72 | -0.11 | exit signal |
| 2026-11-01T21:35 | Three white soldiers | buy | SOL-USD | 17.83 | — | entry signal |
| 2026-11-01T21:35 | Three white soldiers | buy | BTC-USD | 17.83 | — | entry signal |
| 2026-11-01T21:20 | Three white soldiers | sell | ETH-USD | 17.74 | -0.12 | exit signal |
| 2026-11-01T21:00 | CCI reversion · 1h | buy | XRP-USD | 8.44 | — | entry signal |
| 2026-11-01T21:00 | Bollinger reversion · 1h | buy | SOL-USD | 1.89 | — | entry signal |
| 2026-11-01T21:00 | Bollinger reversion · 1h | buy | ETH-USD | 3.90 | — | entry signal |
| 2026-11-01T21:00 | Bollinger reversion · 1h | buy | DOGE-USD | 3.90 | — | entry signal |
| 2026-11-01T21:00 | Candlestick reversal · 1h | buy | XRP-USD | 7.16 | — | entry signal |
| 2026-11-01T21:00 | Candlestick reversal · 1h | buy | SOL-USD | 7.16 | — | entry signal |
| 2026-11-01T20:40 | Three white soldiers | buy | ETH-USD | 17.86 | — | entry signal |
| 2026-11-01T20:00 | Stochastic reversion · 1h | buy | SOL-USD | 4.75 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 00:55:05.000125+00:00 -> 2026-11-02 01:05:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
