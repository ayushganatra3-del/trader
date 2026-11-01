# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-01T05:55:05.000117+00:00 · 43424 ticks

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

Today: 4782 decisions in 963 calls, $0.0667 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-01T05:55 | 2 / 3 / 0 | DOGE-USD 17% |  |
| Breezy | 2026-11-01T05:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-01T05:55 | 2 / 3 / 0 | cash |  |

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
| 19 | Hold BTC | benchmark | 91.90 | -8.10 | 0 | — | -0.73 | 0.00 | -12.65 | 1 |
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
| 32 | Stochastic reversion · 1h | reversion | 85.47 | -14.53 | 224 | 47.3 | -19.01 | -3.38 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -15.73 | -3.01 | -20.33 | 259 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.27 | -4.55 | -25.77 | 184 |
| 35 | Bollinger breakout · 1h | breakout | 83.49 | -16.51 | 132 | 26.5 | -15.31 | -2.82 | -21.61 | 240 |
| 36 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.53 | -6.95 | -21.92 | 153 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.42 | -19.33 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.65 | -3.64 | -30.48 | 35 |
| 39 | MFI reversion · 1h | reversion | 82.36 | -17.64 | 295 | 31.9 | -16.32 | -2.58 | -20.24 | 151 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.36 | -19.64 | 137 | 13.1 | -25.99 | -4.78 | -29.25 | 215 |
| 43 | CCI reversion · 1h | reversion | 80.21 | -19.79 | 252 | 46.0 | -26.46 | -4.15 | -28.40 | 447 |
| 44 | EMA 20/50 cross · 1h | trend | 80.09 | -19.91 | 88 | 11.4 | -22.87 | -4.33 | -26.83 | 135 |
| 45 | MACD cross · 1h | trend | 79.82 | -20.18 | 283 | 24.0 | -28.29 | -5.02 | -32.86 | 467 |
| 46 | Williams %R · 1h | reversion | 79.25 | -20.75 | 257 | 47.1 | -34.99 | -6.28 | -35.78 | 524 |
| 47 | RSI momentum · 1h | momentum | 79.10 | -20.90 | 130 | 13.1 | -26.25 | -4.73 | -30.14 | 214 |
| 48 | MACD zero-line · 1h | trend | 78.82 | -21.18 | 130 | 16.2 | -22.84 | -4.58 | -27.49 | 213 |
| 49 | Z-score reversion · 1h | reversion | 78.46 | -21.55 | 134 | 33.6 | -15.97 | -2.45 | -22.55 | 210 |
| 50 | Heikin-Ashi · 1h | trend | 78.14 | -21.86 | 337 | 23.7 | -41.37 | -8.93 | -42.02 | 665 |
| 51 | Bollinger reversion · 1h | reversion | 78.09 | -21.91 | 199 | 37.7 | -31.58 | -6.72 | -32.80 | 377 |
| 52 | Triple EMA stack · 1h | trend | 78.04 | -21.96 | 120 | 15.0 | -30.18 | -5.60 | -33.28 | 206 |
| 53 | OBV trend · 1h | momentum | 77.91 | -22.09 | 232 | 17.7 | -32.76 | -6.64 | -36.05 | 298 |
| 54 | Donchian 20/10 · 1h | breakout | 76.12 | -23.88 | 116 | 20.7 | -26.01 | -4.55 | -29.81 | 215 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -28.60 | -5.07 | -32.78 | 378 |
| 56 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -28.37 | -1.52 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.08 | -26.92 | 122 | 26.2 | -20.92 | -3.72 | -26.17 | 194 |
| 58 | VWAP momentum · 1h | momentum | 72.98 | -27.02 | 653 | 22.7 | -51.32 | -10.93 | -51.54 | 1232 |
| 59 | Three white soldiers | momentum | 72.01 | -27.99 | 389 | 16.7 | -44.92 | -20.87 | -44.94 | 621 |
| 60 | Candlestick reversal · 1h | reversion | 71.75 | -28.25 | 325 | 28.0 | -35.58 | -7.04 | -36.11 | 551 |
| 61 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -19.48 | -4.06 | -21.27 | 352 |
| 62 | EMA 9/21 cross · 1h | trend | 70.90 | -29.10 | 208 | 10.1 | -33.55 | -6.26 | -36.95 | 331 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -44.44 | -98.87 | 5229 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.60 | -23.73 | -79.62 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.66 | -44.97 | -93.66 | 2543 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.64 | -30.90 | -88.75 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -37.90 | -91.28 | 2355 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.11 | -31.25 | -90.12 | 2230 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -52.15 | -97.78 | 3531 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -58.73 | -96.28 | 3415 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.80 | -35.31 | -93.80 | 2462 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.22 | -33.70 | -82.22 | 1696 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -54.07 | -99.46 | 5918 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -43.21 | -92.94 | 2638 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -37.33 | -95.51 | 3463 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -76.41 | -99.77 | 6247 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.91 | -44.27 | -91.92 | 2313 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.94 | -26.63 | -75.11 | 1573 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -62.05 | -97.73 | 3587 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -60.55 | -98.65 | 4865 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -28.21 | -69.22 | 1217 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -53.80 | -94.75 | 2803 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.63 | -37.60 | -84.63 | 1814 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -69.71 | -99.61 | 6375 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.95 | -30.25 | -87.96 | 2251 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.86 | -19.68 | -77.08 | 1729 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -36.93 | -90.27 | 2244 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.35 | -50.86 | -96.35 | 3838 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.81 | -51.94 | -89.81 | 2154 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.66 | -25.18 | -64.67 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.01 | -25.50 | -74.02 | 1280 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.77 | -18.85 | -76.14 | 1589 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.78 | -50.88 | -96.78 | 4264 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -102.79 | -99.92 | 8379 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-01T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.16 | — | entry signal |
| 2026-11-01T01:00 | VWAP momentum · 1h | sell | ETH-USD | 5.52 | 0.00 | rebalance down |
| 2026-11-01T01:00 | VWAP momentum · 1h | sell | BTC-USD | 5.49 | -0.02 | rebalance down |
| 2026-11-01T01:00 | MACD zero-line · 1h | buy | XRP-USD | 19.71 | — | entry signal |
| 2026-11-01T01:00 | MACD zero-line · 1h | buy | BTC-USD | 19.71 | — | entry signal |
| 2026-11-01T00:50 | Three white soldiers | sell | XRP-USD | 17.93 | -0.14 | stop-loss |
| 2026-11-01T00:35 | Three white soldiers | buy | XRP-USD | 18.07 | — | entry signal |
| 2026-10-31T23:05 | VWAP momentum · 1h | buy | ETH-USD | 4.16 | — | rebalance up |
| 2026-10-31T23:05 | VWAP momentum · 1h | buy | BTC-USD | 4.18 | — | rebalance up |
| 2026-10-31T23:05 | VWAP momentum · 1h | sell | DOGE-USD | 10.40 | -0.07 | target is flat |
| 2026-10-31T22:00 | MACD zero-line · 1h | buy | DOGE-USD | 19.72 | — | entry signal |
| 2026-10-31T21:30 | Three white soldiers | sell | ETH-USD | 17.98 | -0.12 | exit signal |
| 2026-10-31T21:25 | Three white soldiers | buy | ETH-USD | 18.10 | — | entry signal |
| 2026-10-31T21:00 | VWAP momentum · 1h | sell | XRP-USD | 1.37 | -0.01 | exit signal |
| 2026-10-31T21:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.45 | -0.12 | exit signal |
| 2026-10-31T19:00 | Z-score reversion · 1h | sell | DOGE-USD | 9.76 | -0.06 | exit signal |
| 2026-10-31T19:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 7.28 | -0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-03 05:55:05.000117+00:00 -> 2026-11-01 06:05:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
