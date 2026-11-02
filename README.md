# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T12:23:05.000195+00:00 · 44990 ticks

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

Today: 9246 decisions in 1854 calls, $0.1293 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T12:23 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-02T12:23 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T12:23 | 2 / 3 / 0 | ETH-USD 70% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.39 | 6.39 | 0 | — | 7.73 | 3.79 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.63 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.05 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.80 | -0.20 | 96 | 44.8 | -11.70 | -3.22 | -12.13 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.75 | -0.25 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.18 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.08 | -2.92 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.93 | -5.07 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.54 | -5.46 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.95 | -6.05 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.01 | -7.99 | 0 | — | -0.04 | 0.16 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -16.99 | -6.24 | -17.93 | 83 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 23 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 24 | Parabolic SAR · 1h | trend | 90.58 | -9.41 | 144 | 27.8 | -17.93 | -4.21 | -19.78 | 249 |
| 25 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.78 | -1.87 | -13.40 | 91 |
| 26 | Copy: Insider buying | copy | 89.38 | -10.62 | 34 | 35.3 | -21.47 | -4.33 | -23.10 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 88.62 | -11.38 | 59 | 13.6 | -16.09 | -3.62 | -17.73 | 103 |
| 28 | Daily: Bullish score | daily | 88.55 | -11.45 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.90 | -14.10 | 127 | 29.1 | -16.04 | -3.29 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.49 | -14.51 | 226 | 47.8 | -17.45 | -3.03 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 84.88 | -15.12 | 142 | 19.0 | -15.37 | -2.77 | -20.33 | 262 |
| 34 | Keltner breakout · 1h | breakout | 84.88 | -15.12 | 87 | 24.1 | -23.92 | -4.71 | -25.77 | 185 |
| 35 | Connors RSI(2) · 1h | reversion | 83.34 | -16.66 | 188 | 40.4 | -20.90 | -6.67 | -21.28 | 151 |
| 36 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 37 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 38 | Bollinger breakout · 1h | breakout | 82.38 | -17.62 | 138 | 25.4 | -16.00 | -2.94 | -22.06 | 244 |
| 39 | MFI reversion · 1h | reversion | 82.27 | -17.73 | 295 | 31.9 | -15.00 | -2.32 | -20.24 | 149 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 81.84 | -18.16 | 81 | 13.6 | -20.97 | -4.19 | -24.93 | 121 |
| 42 | CCI reversion · 1h | reversion | 79.85 | -20.14 | 257 | 45.5 | -23.63 | -3.62 | -27.91 | 442 |
| 43 | Supertrend · 1h | trend | 79.82 | -20.18 | 137 | 13.1 | -27.28 | -5.33 | -28.09 | 215 |
| 44 | EMA 20/50 cross · 1h | trend | 79.49 | -20.51 | 90 | 11.1 | -23.89 | -4.80 | -26.11 | 133 |
| 45 | RSI momentum · 1h | momentum | 78.98 | -21.02 | 132 | 12.9 | -28.69 | -5.54 | -29.09 | 215 |
| 46 | Williams %R · 1h | reversion | 78.95 | -21.05 | 259 | 47.1 | -33.35 | -5.90 | -34.88 | 518 |
| 47 | MACD cross · 1h | trend | 78.37 | -21.63 | 293 | 23.9 | -31.47 | -6.28 | -33.36 | 463 |
| 48 | Z-score reversion · 1h | reversion | 78.30 | -21.70 | 136 | 33.8 | -17.13 | -2.65 | -22.55 | 207 |
| 49 | Bollinger reversion · 1h | reversion | 77.93 | -22.07 | 203 | 37.4 | -29.13 | -6.07 | -30.63 | 371 |
| 50 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -23.74 | -4.73 | -28.23 | 215 |
| 51 | Triple EMA stack · 1h | trend | 77.61 | -22.39 | 122 | 14.8 | -33.40 | -6.55 | -33.55 | 209 |
| 52 | Heikin-Ashi · 1h | trend | 77.41 | -22.59 | 343 | 23.3 | -41.39 | -8.94 | -42.77 | 665 |
| 53 | OBV trend · 1h | momentum | 77.33 | -22.66 | 235 | 17.4 | -32.99 | -6.63 | -36.12 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 75.81 | -24.19 | 118 | 20.3 | -26.24 | -4.56 | -29.81 | 217 |
| 55 | ROC + volume · 1h | momentum | 74.86 | -25.14 | 296 | 25.3 | -29.24 | -5.16 | -33.16 | 383 |
| 56 | Max aggression: 1-day momentum | meta | 73.29 | -26.71 | 21 | 33.3 | -33.79 | -1.99 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.04 | -26.96 | 123 | 26.0 | -21.09 | -3.72 | -26.17 | 191 |
| 58 | Candlestick reversal · 1h | reversion | 71.42 | -28.58 | 331 | 28.1 | -33.03 | -6.39 | -35.71 | 539 |
| 59 | VWAP momentum · 1h | momentum | 71.29 | -28.71 | 670 | 22.1 | -51.72 | -10.96 | -51.77 | 1244 |
| 60 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -19.64 | -3.59 | -22.60 | 337 |
| 61 | Three white soldiers | momentum | 70.60 | -29.40 | 401 | 16.2 | -45.17 | -20.94 | -45.60 | 626 |
| 62 | EMA 9/21 cross · 1h | trend | 70.58 | -29.42 | 212 | 9.9 | -34.27 | -6.39 | -37.62 | 336 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -43.95 | -98.91 | 5247 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.47 | -23.57 | -79.47 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -43.89 | -93.56 | 2539 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -31.97 | -88.99 | 1944 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.16 | -37.91 | -91.30 | 2354 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.68 | -31.53 | -90.68 | 2264 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.39 | -97.77 | 3533 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -56.32 | -96.26 | 3414 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -34.95 | -93.70 | 2470 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.07 | -33.75 | -82.11 | 1696 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -56.48 | -99.48 | 5927 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.89 | -43.58 | -92.93 | 2638 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.67 | -37.51 | -95.67 | 3486 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -77.92 | -99.78 | 6260 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.88 | -45.61 | -91.88 | 2315 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.02 | -27.04 | -75.06 | 1570 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -57.31 | -97.70 | 3577 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.43 | -98.65 | 4868 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.07 | -28.50 | -69.19 | 1215 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -55.14 | -94.71 | 2797 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -37.94 | -84.72 | 1815 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -69.82 | -99.61 | 6372 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.15 | -30.57 | -88.28 | 2253 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.88 | -19.62 | -77.14 | 1731 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.20 | -37.39 | -90.29 | 2241 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.36 | -52.10 | -96.40 | 3843 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.69 | -55.60 | -89.74 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -63.97 | -25.02 | -64.34 | 815 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.65 | -25.09 | -73.89 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.61 | -18.64 | -75.98 | 1586 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.73 | -50.00 | -96.77 | 4253 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.91 | -99.93 | 8377 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T12:15 | Three white soldiers | buy | SOL-USD | 17.66 | — | entry signal |
| 2026-11-02T12:00 | Donchian 20/10 · 1h | sell | BTC-USD | 18.90 | -0.13 | exit signal |
| 2026-11-02T12:00 | RSI momentum · 1h | buy | XRP-USD | 6.48 | — | rebalance up |
| 2026-11-02T12:00 | RSI momentum · 1h | buy | ETH-USD | 6.61 | — | rebalance up |
| 2026-11-02T12:00 | RSI momentum · 1h | sell | BTC-USD | 13.09 | -0.09 | exit signal |
| 2026-11-02T12:00 | ROC + volume · 1h | sell | XRP-USD | 18.16 | -0.30 | exit signal |
| 2026-11-02T12:00 | Parabolic SAR · 1h | sell | ETH-USD | 18.14 | -0.04 | exit signal |
| 2026-11-02T12:00 | MACD cross · 1h | sell | SOL-USD | 19.54 | -0.30 | exit signal |
| 2026-11-02T12:00 | MACD cross · 1h | sell | ETH-USD | 15.72 | -0.14 | exit signal |
| 2026-11-02T11:50 | Donchian 55/20 · 1h | sell | BTC-USD | 21.95 | -0.31 | stop-loss |
| 2026-11-02T11:50 | Triple EMA stack · 1h | sell | BTC-USD | 19.19 | -0.28 | stop-loss |
| 2026-11-02T11:50 | EMA 20/50 cross · 1h | sell | BTC-USD | 19.68 | -0.27 | stop-loss |
| 2026-11-02T11:00 | Ichimoku · 1h | sell | XRP-USD | 20.32 | -0.14 | exit signal |
| 2026-11-02T11:00 | Parabolic SAR · 1h | sell | XRP-USD | 22.51 | -0.24 | exit signal |
| 2026-11-02T11:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.91 | — | rebalance up |
| 2026-11-02T11:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 8.90 | -0.07 | exit signal |
| 2026-11-02T10:05 | MACD zero-line · 1h | sell | XRP-USD | 19.22 | -0.39 | target is flat |
| 2026-11-02T10:05 | MACD cross · 1h | sell | XRP-USD | 19.55 | -0.27 | target is flat |
| 2026-11-02T10:00 | ROC + volume · 1h | buy | ETH-USD | 18.70 | — | entry signal |
| 2026-11-02T10:00 | VWAP momentum · 1h | sell | ETH-USD | 17.67 | -0.19 | exit signal |
| 2026-11-02T10:00 | Ichimoku · 1h | buy | XRP-USD | 20.46 | — | entry signal |
| 2026-11-02T09:00 | Candlestick reversal · 1h | buy | SOL-USD | 7.94 | — | entry signal |
| 2026-11-02T09:00 | VWAP momentum · 1h | buy | ETH-USD | 17.86 | — | entry signal |
| 2026-11-02T09:00 | Ichimoku · 1h | sell | BTC-USD | 20.41 | -0.11 | exit signal |
| 2026-11-02T09:00 | MACD cross · 1h | buy | XRP-USD | 4.21 | — | rebalance up |
| 2026-11-02T09:00 | MACD cross · 1h | buy | SOL-USD | 3.98 | — | rebalance up |
| 2026-11-02T09:00 | MACD cross · 1h | sell | DOGE-USD | 15.67 | -0.06 | exit signal |
| 2026-11-02T09:00 | Three white soldiers | sell | XRP-USD | 17.58 | -0.11 | exit signal |
| 2026-11-02T08:35 | Three white soldiers | buy | XRP-USD | 17.69 | — | entry signal |
| 2026-11-02T08:00 | OBV trend · 1h | sell | BTC-USD | 18.32 | -0.21 | exit signal |
| 2026-11-02T08:00 | Ichimoku · 1h | buy | ETH-USD | 20.51 | — | entry signal |
| 2026-11-02T08:00 | Ichimoku · 1h | buy | BTC-USD | 20.51 | — | entry signal |
| 2026-11-02T08:00 | Parabolic SAR · 1h | buy | XRP-USD | 13.89 | — | rebalance up |
| 2026-11-02T08:00 | Parabolic SAR · 1h | buy | DOGE-USD | 4.64 | — | rebalance up |
| 2026-11-02T08:00 | Parabolic SAR · 1h | sell | BTC-USD | 22.56 | -0.23 | exit signal |
| 2026-11-02T08:00 | MACD cross · 1h | buy | DOGE-USD | 15.73 | — | entry |
| 2026-11-02T08:00 | MACD cross · 1h | sell | BTC-USD | 15.73 | -0.12 | exit signal |
| 2026-11-02T07:50 | ROC + volume · 1h | sell | BTC-USD | 18.65 | -0.29 | stop-loss |
| 2026-11-02T07:35 | Squeeze breakout · 1h | sell | BTC-USD | 22.20 | -0.32 | stop-loss |
| 2026-11-02T07:35 | RSI momentum · 1h | buy | XRP-USD | 13.26 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 12:23:05.000195+00:00 -> 2026-11-02 12:33:05.000195+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
