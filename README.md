# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-01T08:55:05.000148+00:00 · 43567 ticks

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

Today: 6909 decisions in 1392 calls, $0.0963 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-01T08:55 | 0 / 1 / 3 | cash |  |
| Breezy | 2026-11-01T08:55 | 0 / 4 / 0 | cash |  |
| Boozy | 2026-11-01T08:55 | 3 / 0 / 1 | ETH-USD 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | ETHU | 2.60 | +6.95% | 13 |
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Connors RSI(2) | SQQQ | 2.21 | +2.50% | 13 |
| RSI(14) reversion | TSLA | 2.13 | +7.39% | 5 |
| Candlestick reversal | LABU | 2.13 | +6.25% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.51 | 6.51 | 0 | — | 7.73 | 3.83 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.60 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.65 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.07 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.89 | -0.11 | 96 | 44.8 | -12.42 | -3.48 | -12.61 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.11 | 1.36 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.21 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.19 | -2.81 | 0 | — | -1.35 | -0.74 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.57 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.61 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.42 | -3.16 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.46 | 1.48 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -7.15 | -2.76 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.67 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -3.56 | -1.33 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.25 | -7.75 | 0 | — | -0.88 | 0.06 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.63 | -5.16 | -12.21 | 210 |
| 21 | Parabolic SAR · 1h | trend | 91.49 | -8.51 | 140 | 28.6 | -16.23 | -3.71 | -20.27 | 246 |
| 22 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -18.48 | -6.86 | -18.48 | 89 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.71 | -16.91 | 1 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.11 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.50 | -1.80 | -12.70 | 89 |
| 26 | Copy: Insider buying | copy | 89.48 | -10.52 | 34 | 35.3 | -22.37 | -4.56 | -23.61 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 89.33 | -10.66 | 57 | 14.0 | -16.81 | -3.73 | -17.83 | 103 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -1.09 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.42 | -3.81 | -15.04 | 97 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -16.04 | -3.32 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.47 | -14.53 | 224 | 47.3 | -19.00 | -3.38 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -15.73 | -3.01 | -20.33 | 259 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.27 | -4.55 | -25.77 | 184 |
| 35 | Bollinger breakout · 1h | breakout | 83.56 | -16.44 | 132 | 26.5 | -15.25 | -2.81 | -21.61 | 241 |
| 36 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.53 | -6.95 | -21.92 | 153 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.42 | -19.33 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.65 | -3.64 | -30.48 | 35 |
| 39 | MFI reversion · 1h | reversion | 82.36 | -17.64 | 295 | 31.9 | -16.32 | -2.58 | -20.24 | 151 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.36 | -19.64 | 137 | 13.1 | -25.96 | -4.76 | -29.25 | 215 |
| 43 | CCI reversion · 1h | reversion | 80.29 | -19.71 | 252 | 46.0 | -26.38 | -4.13 | -28.40 | 447 |
| 44 | EMA 20/50 cross · 1h | trend | 80.09 | -19.91 | 88 | 11.4 | -22.88 | -4.34 | -26.79 | 135 |
| 45 | MACD cross · 1h | trend | 79.92 | -20.08 | 283 | 24.0 | -28.23 | -5.00 | -32.86 | 467 |
| 46 | Williams %R · 1h | reversion | 79.30 | -20.70 | 257 | 47.1 | -34.95 | -6.27 | -35.77 | 524 |
| 47 | RSI momentum · 1h | momentum | 79.16 | -20.84 | 130 | 13.1 | -26.27 | -4.75 | -30.14 | 215 |
| 48 | MACD zero-line · 1h | trend | 78.95 | -21.05 | 130 | 16.2 | -22.71 | -4.55 | -27.49 | 213 |
| 49 | Z-score reversion · 1h | reversion | 78.46 | -21.55 | 134 | 33.6 | -15.97 | -2.45 | -22.55 | 210 |
| 50 | Heikin-Ashi · 1h | trend | 78.25 | -21.75 | 337 | 23.7 | -41.06 | -8.92 | -42.14 | 664 |
| 51 | Bollinger reversion · 1h | reversion | 78.09 | -21.91 | 199 | 37.7 | -31.56 | -6.72 | -32.79 | 377 |
| 52 | Triple EMA stack · 1h | trend | 78.04 | -21.96 | 120 | 15.0 | -30.08 | -5.56 | -33.28 | 206 |
| 53 | OBV trend · 1h | momentum | 77.91 | -22.09 | 232 | 17.7 | -32.80 | -6.66 | -36.05 | 298 |
| 54 | Donchian 20/10 · 1h | breakout | 76.18 | -23.82 | 116 | 20.7 | -25.95 | -4.53 | -29.81 | 216 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -28.60 | -5.07 | -32.78 | 378 |
| 56 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -28.37 | -1.52 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.10 | -26.90 | 122 | 26.2 | -21.00 | -3.73 | -26.17 | 195 |
| 58 | VWAP momentum · 1h | momentum | 72.95 | -27.05 | 654 | 22.6 | -51.40 | -10.96 | -51.65 | 1235 |
| 59 | Candlestick reversal · 1h | reversion | 71.73 | -28.27 | 325 | 28.0 | -35.48 | -7.02 | -35.90 | 550 |
| 60 | Three white soldiers | momentum | 71.68 | -28.32 | 392 | 16.6 | -45.11 | -21.11 | -45.11 | 623 |
| 61 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -20.40 | -4.36 | -22.46 | 354 |
| 62 | EMA 9/21 cross · 1h | trend | 71.01 | -28.99 | 208 | 10.1 | -33.74 | -6.36 | -37.02 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -44.65 | -98.87 | 5230 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.57 | -23.79 | -79.61 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.62 | -46.13 | -93.62 | 2542 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.76 | -31.27 | -88.86 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.23 | -38.45 | -91.23 | 2355 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.23 | -31.67 | -90.26 | 2238 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -53.62 | -97.80 | 3536 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -60.85 | -96.26 | 3416 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.85 | -35.74 | -93.85 | 2471 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.02 | -33.86 | -82.03 | 1693 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.87 | -99.47 | 5920 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -44.03 | -92.94 | 2640 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.70 | -95.50 | 3462 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -79.34 | -99.77 | 6246 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -44.88 | -91.93 | 2315 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.88 | -26.63 | -75.05 | 1572 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -63.49 | -97.73 | 3588 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.35 | -98.65 | 4864 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -28.48 | -69.32 | 1219 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.83 | -94.72 | 2801 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -38.50 | -84.70 | 1818 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -71.59 | -99.62 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.91 | -30.29 | -87.97 | 2250 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.87 | -19.68 | -77.08 | 1728 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.27 | -37.16 | -90.28 | 2246 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.34 | -51.26 | -96.34 | 3836 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.78 | -51.95 | -89.78 | 2152 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.72 | -25.37 | -64.74 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.82 | -25.57 | -73.93 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.83 | -18.85 | -76.14 | 1591 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -51.39 | -96.79 | 4265 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -108.62 | -99.92 | 8386 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-01T08:40 | Three white soldiers | sell | DOGE-USD | 17.83 | -0.12 | stop-loss |
| 2026-11-01T08:35 | Three white soldiers | buy | DOGE-USD | 17.95 | — | entry signal |
| 2026-11-01T08:10 | Three white soldiers | sell | XRP-USD | 17.87 | -0.10 | exit signal |
| 2026-11-01T08:00 | VWAP momentum · 1h | buy | XRP-USD | 5.07 | — | entry |
| 2026-11-01T08:00 | VWAP momentum · 1h | sell | SOL-USD | 5.07 | -0.04 | exit signal |
| 2026-11-01T07:35 | Three white soldiers | buy | XRP-USD | 17.98 | — | entry signal |
| 2026-11-01T07:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.24 | — | entry signal |
| 2026-11-01T06:40 | Three white soldiers | sell | BTC-USD | 17.90 | -0.10 | exit signal |
| 2026-11-01T06:00 | Candlestick reversal · 1h | buy | SOL-USD | 8.97 | — | entry signal |
| 2026-11-01T06:00 | Bollinger breakout · 1h | buy | BTC-USD | 20.88 | — | entry signal |
| 2026-11-01T06:00 | Donchian 20/10 · 1h | buy | BTC-USD | 19.03 | — | entry signal |
| 2026-11-01T06:00 | RSI momentum · 1h | buy | BTC-USD | 19.78 | — | entry signal |
| 2026-11-01T06:00 | VWAP momentum · 1h | buy | SOL-USD | 5.11 | — | entry signal |
| 2026-11-01T06:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.12 | — | entry signal |
| 2026-11-01T06:00 | VWAP momentum · 1h | sell | ETH-USD | 5.43 | -0.03 | rebalance down |
| 2026-11-01T06:00 | VWAP momentum · 1h | sell | BTC-USD | 5.48 | -0.01 | rebalance down |
| 2026-11-01T06:00 | Three white soldiers | buy | BTC-USD | 18.00 | — | entry signal |
| 2026-11-01T05:01 | EMA 9/21 cross · 1h | buy | DOGE-USD | 3.53 | — | rebalance up |
| 2026-11-01T05:01 | EMA 9/21 cross · 1h | sell | BTC-USD | 3.53 | -0.01 | rebalance down |
| 2026-11-01T05:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 3.17 | — | entry signal |
| 2026-11-01T05:00 | Three white soldiers | sell | XRP-USD | 17.91 | -0.12 | exit signal |
| 2026-11-01T04:30 | Three white soldiers | buy | XRP-USD | 18.03 | — | entry signal |
| 2026-11-01T04:00 | Williams %R · 1h | buy | DOGE-USD | 19.81 | — | entry signal |
| 2026-11-01T04:00 | RSI(14) reversion · 1h | buy | SOL-USD | 4.94 | — | rebalance up |
| 2026-11-01T04:00 | RSI(14) reversion · 1h | sell | BTC-USD | 7.33 | 0.00 | exit signal |
| 2026-11-01T04:00 | VWAP momentum · 1h | buy | ETH-USD | 14.60 | — | entry signal |
| 2026-11-01T04:00 | VWAP momentum · 1h | sell | BTC-USD | 3.65 | -0.01 | rebalance down |
| 2026-11-01T04:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 5.89 | — | rebalance up |
| 2026-11-01T04:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 3.51 | -0.03 | exit signal |
| 2026-11-01T04:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 5.55 | -0.06 | exit signal |
| 2026-11-01T03:00 | VWAP momentum · 1h | buy | BTC-USD | 9.11 | — | rebalance up |
| 2026-11-01T03:00 | VWAP momentum · 1h | sell | SOL-USD | 12.11 | -0.11 | exit signal |
| 2026-11-01T03:00 | VWAP momentum · 1h | sell | ETH-USD | 9.14 | 0.02 | exit signal |
| 2026-11-01T03:00 | Heikin-Ashi · 1h | buy | ETH-USD | 19.55 | — | entry signal |
| 2026-11-01T03:00 | Heikin-Ashi · 1h | buy | BTC-USD | 19.55 | — | entry signal |
| 2026-11-01T02:00 | VWAP momentum · 1h | buy | SOL-USD | 6.94 | — | rebalance up |
| 2026-11-01T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 9.08 | -0.08 | exit signal |
| 2026-11-01T01:00 | RSI(14) reversion · 1h | sell | XRP-USD | 7.28 | -0.04 | exit signal |
| 2026-11-01T01:00 | RSI momentum · 1h | buy | ETH-USD | 19.78 | — | entry signal |
| 2026-11-01T01:00 | VWAP momentum · 1h | buy | SOL-USD | 5.27 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-03 08:55:05.000148+00:00 -> 2026-11-01 09:05:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
