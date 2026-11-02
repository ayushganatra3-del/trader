# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T04:55:05.000140+00:00 · 44632 ticks

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

Today: 3900 decisions in 780 calls, $0.0545 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T04:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-02T04:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T04:55 | 1 / 4 / 0 | ETH-USD 51% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.53 | 6.53 | 0 | — | 7.73 | 3.79 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.63 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.05 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.90 | -0.10 | 96 | 44.8 | -12.42 | -3.45 | -12.61 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.88 | -0.12 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.18 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.20 | -2.80 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.66 | -5.34 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.07 | -5.93 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.61 | -7.38 | 0 | — | -1.30 | -0.04 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -17.83 | -6.56 | -18.02 | 86 |
| 22 | Parabolic SAR · 1h | trend | 91.24 | -8.76 | 141 | 28.4 | -16.51 | -3.75 | -20.27 | 251 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 89.83 | -10.17 | 59 | 23.7 | -6.45 | -1.77 | -13.10 | 91 |
| 26 | Copy: Insider buying | copy | 89.49 | -10.51 | 34 | 35.3 | -22.37 | -4.52 | -23.61 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 88.99 | -11.01 | 58 | 13.8 | -17.16 | -3.79 | -18.18 | 106 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -16.04 | -3.29 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.58 | -14.42 | 226 | 47.8 | -17.45 | -3.03 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 85.05 | -14.95 | 141 | 19.1 | -15.45 | -2.93 | -20.33 | 259 |
| 34 | Keltner breakout · 1h | breakout | 85.03 | -14.97 | 86 | 24.4 | -23.32 | -4.52 | -25.77 | 185 |
| 35 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.48 | -6.87 | -21.89 | 152 |
| 36 | Bollinger breakout · 1h | breakout | 83.03 | -16.97 | 134 | 26.1 | -15.40 | -2.82 | -21.61 | 244 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 39 | MFI reversion · 1h | reversion | 82.37 | -17.63 | 295 | 31.9 | -16.84 | -2.66 | -20.24 | 151 |
| 40 | Ichimoku · 1h | trend | 82.08 | -17.91 | 79 | 13.9 | -20.76 | -4.14 | -24.80 | 118 |
| 41 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 42 | Supertrend · 1h | trend | 80.14 | -19.86 | 137 | 13.1 | -26.18 | -4.78 | -29.42 | 219 |
| 43 | CCI reversion · 1h | reversion | 79.90 | -20.10 | 257 | 45.5 | -25.17 | -3.89 | -27.91 | 446 |
| 44 | EMA 20/50 cross · 1h | trend | 79.79 | -20.21 | 89 | 11.2 | -23.32 | -4.41 | -26.92 | 137 |
| 45 | RSI momentum · 1h | momentum | 79.38 | -20.62 | 130 | 13.1 | -26.03 | -4.63 | -30.16 | 217 |
| 46 | MACD cross · 1h | trend | 79.22 | -20.78 | 288 | 24.3 | -27.37 | -4.87 | -32.86 | 467 |
| 47 | Williams %R · 1h | reversion | 79.01 | -20.99 | 259 | 47.1 | -34.06 | -6.04 | -34.88 | 521 |
| 48 | Z-score reversion · 1h | reversion | 78.30 | -21.70 | 136 | 33.8 | -17.13 | -2.65 | -22.55 | 207 |
| 49 | MACD zero-line · 1h | trend | 78.15 | -21.85 | 134 | 15.7 | -23.51 | -4.71 | -27.86 | 215 |
| 50 | Bollinger reversion · 1h | reversion | 78.02 | -21.98 | 203 | 37.4 | -29.51 | -6.17 | -30.72 | 373 |
| 51 | Triple EMA stack · 1h | trend | 77.92 | -22.08 | 121 | 14.9 | -30.39 | -5.61 | -33.51 | 209 |
| 52 | Heikin-Ashi · 1h | trend | 77.71 | -22.29 | 340 | 23.5 | -41.13 | -8.86 | -42.52 | 665 |
| 53 | OBV trend · 1h | momentum | 77.59 | -22.41 | 234 | 17.5 | -33.04 | -6.66 | -36.12 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 76.09 | -23.91 | 117 | 20.5 | -26.04 | -4.52 | -29.81 | 217 |
| 55 | ROC + volume · 1h | momentum | 75.38 | -24.62 | 293 | 25.6 | -28.78 | -5.06 | -32.73 | 382 |
| 56 | Max aggression: 1-day momentum | meta | 73.38 | -26.61 | 21 | 33.3 | -33.79 | -1.99 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.04 | -26.96 | 123 | 26.0 | -20.84 | -3.67 | -26.17 | 188 |
| 58 | VWAP momentum · 1h | momentum | 71.95 | -28.05 | 665 | 22.3 | -51.33 | -10.82 | -51.46 | 1243 |
| 59 | Candlestick reversal · 1h | reversion | 71.47 | -28.53 | 330 | 28.2 | -33.09 | -6.41 | -35.71 | 537 |
| 60 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -19.85 | -3.69 | -23.89 | 338 |
| 61 | EMA 9/21 cross · 1h | trend | 70.94 | -29.06 | 210 | 10.0 | -34.07 | -6.38 | -37.32 | 336 |
| 62 | Three white soldiers | momentum | 70.75 | -29.25 | 400 | 16.2 | -45.05 | -20.83 | -45.48 | 624 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -42.89 | -98.88 | 5229 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.61 | -23.75 | -79.67 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.58 | -44.87 | -93.61 | 2540 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -31.35 | -88.95 | 1944 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.26 | -38.29 | -91.30 | 2357 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.52 | -31.01 | -90.52 | 2254 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -52.60 | -97.78 | 3532 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -57.58 | -96.25 | 3414 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.81 | -34.54 | -93.81 | 2471 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.28 | -34.38 | -82.31 | 1700 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -54.07 | -99.48 | 5926 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.90 | -43.50 | -92.91 | 2635 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -36.77 | -95.57 | 3473 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -75.70 | -99.78 | 6252 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.97 | -45.26 | -91.97 | 2316 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.93 | -26.98 | -74.97 | 1567 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -59.71 | -97.72 | 3583 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.25 | -98.65 | 4867 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.66 | -28.00 | -68.74 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -54.87 | -94.67 | 2793 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -37.98 | -84.62 | 1811 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.29 | -99.62 | 6379 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.07 | -30.20 | -88.17 | 2256 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.06 | -19.62 | -77.19 | 1736 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.30 | -36.82 | -90.35 | 2246 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -50.86 | -96.43 | 3847 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.70 | -52.99 | -89.80 | 2156 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.03 | -25.12 | -64.34 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.62 | -25.13 | -73.78 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.37 | -18.91 | -76.64 | 1599 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.78 | -50.13 | -96.78 | 4262 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.86 | -99.92 | 8372 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T04:01 | Bollinger breakout · 1h | buy | XRP-USD | 4.16 | — | rebalance up |
| 2026-11-02T04:01 | Bollinger breakout · 1h | sell | BTC-USD | 4.16 | -0.01 | rebalance down |
| 2026-11-02T04:00 | CCI reversion · 1h | sell | SOL-USD | 20.02 | -0.20 | exit signal |
| 2026-11-02T04:00 | CCI reversion · 1h | sell | DOGE-USD | 20.01 | -0.04 | exit signal |
| 2026-11-02T04:00 | Williams %R · 1h | sell | DOGE-USD | 19.93 | 0.08 | exit signal |
| 2026-11-02T04:00 | Stochastic reversion · 1h | sell | SOL-USD | 4.80 | 0.05 | exit signal |
| 2026-11-02T04:00 | Stochastic reversion · 1h | sell | DOGE-USD | 4.79 | 0.04 | exit signal |
| 2026-11-02T04:00 | Z-score reversion · 1h | sell | SOL-USD | 13.11 | 0.07 | exit signal |
| 2026-11-02T04:00 | RSI(14) reversion · 1h | sell | SOL-USD | 12.14 | -0.12 | exit signal |
| 2026-11-02T04:00 | Candlestick reversal · 1h | sell | XRP-USD | 7.16 | 0.02 | exit signal |
| 2026-11-02T04:00 | Candlestick reversal · 1h | sell | DOGE-USD | 7.16 | 0.02 | exit signal |
| 2026-11-02T04:00 | Squeeze breakout · 1h | buy | BTC-USD | 22.52 | — | entry signal |
| 2026-11-02T04:00 | Bollinger breakout · 1h | buy | XRP-USD | 8.14 | — | entry signal |
| 2026-11-02T04:00 | Bollinger breakout · 1h | buy | DOGE-USD | 16.68 | — | entry signal |
| 2026-11-02T04:00 | Bollinger breakout · 1h | sell | ETH-USD | 4.23 | 0.01 | rebalance down |
| 2026-11-02T04:00 | RSI momentum · 1h | buy | DOGE-USD | 13.27 | — | entry signal |
| 2026-11-02T04:00 | RSI momentum · 1h | sell | ETH-USD | 6.85 | 0.10 | rebalance down |
| 2026-11-02T04:00 | RSI momentum · 1h | sell | BTC-USD | 6.62 | 0.03 | rebalance down |
| 2026-11-02T04:00 | ROC + volume · 1h | buy | XRP-USD | 18.45 | — | entry signal |
| 2026-11-02T04:00 | ROC + volume · 1h | buy | BTC-USD | 18.94 | — | entry signal |
| 2026-11-02T04:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.08 | — | entry signal |
| 2026-11-02T04:00 | Heikin-Ashi · 1h | buy | BTC-USD | 19.51 | — | entry signal |
| 2026-11-02T04:00 | ADX DI cross · 1h | buy | SOL-USD | 21.34 | — | entry signal |
| 2026-11-02T04:00 | Supertrend · 1h | buy | SOL-USD | 15.81 | — | entry signal |
| 2026-11-02T04:00 | Supertrend · 1h | buy | DOGE-USD | 16.11 | — | entry signal |
| 2026-11-02T04:00 | Supertrend · 1h | sell | ETH-USD | 4.08 | 0.01 | rebalance down |
| 2026-11-02T04:00 | Supertrend · 1h | sell | BTC-USD | 4.02 | -0.00 | rebalance down |
| 2026-11-02T04:00 | MACD zero-line · 1h | buy | XRP-USD | 19.61 | — | entry signal |
| 2026-11-02T04:00 | MACD zero-line · 1h | buy | DOGE-USD | 19.61 | — | entry signal |
| 2026-11-02T04:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 9.16 | — | entry signal |
| 2026-11-02T04:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 6.06 | 0.06 | rebalance down |
| 2026-11-02T04:00 | Three white soldiers | sell | BTC-USD | 17.63 | -0.08 | exit signal |
| 2026-11-02T03:10 | Three white soldiers | buy | BTC-USD | 17.71 | — | entry signal |
| 2026-11-02T03:00 | Squeeze breakout · 1h | buy | ETH-USD | 22.50 | — | entry signal |
| 2026-11-02T03:00 | Keltner breakout · 1h | buy | ETH-USD | 21.27 | — | entry signal |
| 2026-11-02T03:00 | OBV trend · 1h | buy | BTC-USD | 18.54 | — | entry signal |
| 2026-11-02T02:00 | CCI reversion · 1h | buy | SOL-USD | 6.60 | — | rebalance up |
| 2026-11-02T02:00 | CCI reversion · 1h | buy | DOGE-USD | 6.61 | — | rebalance up |
| 2026-11-02T02:00 | CCI reversion · 1h | sell | XRP-USD | 15.95 | -0.01 | exit signal |
| 2026-11-02T02:00 | Bollinger reversion · 1h | sell | SOL-USD | 1.89 | 0.00 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 04:55:05.000140+00:00 -> 2026-11-02 05:05:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
