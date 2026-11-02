# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T03:55:05.000152+00:00 · 44580 ticks

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

Today: 3120 decisions in 624 calls, $0.0436 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T03:55 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-02T03:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T03:55 | 2 / 3 / 0 | ETH-USD 66% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.56 | 6.56 | 0 | — | 7.73 | 3.79 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.63 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 2.05 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 96 | 44.8 | -12.42 | -3.45 | -12.61 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.09 | 0 | — | 3.11 | 1.35 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.18 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.23 | -2.77 | 0 | — | -1.35 | -0.73 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.55 | -5.83 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.98 | -5.02 | 129 | 31.0 | -4.44 | -3.15 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.45 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.69 | -5.31 | 0 | — | -7.15 | -2.74 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.10 | -5.90 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.87 | -7.13 | 0 | — | -0.51 | 0.09 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.57 | -5.07 | -12.21 | 209 |
| 21 | Parabolic SAR · 1h | trend | 91.52 | -8.48 | 141 | 28.4 | -16.26 | -3.68 | -20.27 | 251 |
| 22 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -17.74 | -6.53 | -18.02 | 86 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.69 | -16.91 | 2 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.08 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.09 | -9.91 | 59 | 23.7 | -6.20 | -1.70 | -12.99 | 90 |
| 26 | Copy: Insider buying | copy | 89.52 | -10.48 | 34 | 35.3 | -22.37 | -4.52 | -23.61 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 89.20 | -10.80 | 58 | 13.8 | -16.99 | -3.74 | -18.18 | 106 |
| 28 | Daily: Bullish score | daily | 88.58 | -11.42 | 14 | 21.4 | -6.72 | -1.08 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Volume breakout · 1h | breakout | 85.94 | -14.06 | 127 | 29.1 | -16.04 | -3.29 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.63 | -14.37 | 224 | 47.3 | -17.42 | -3.02 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 85.38 | -14.62 | 141 | 19.1 | -15.15 | -2.86 | -20.33 | 258 |
| 34 | Keltner breakout · 1h | breakout | 85.17 | -14.83 | 86 | 24.4 | -23.21 | -4.50 | -25.77 | 185 |
| 35 | Bollinger breakout · 1h | breakout | 83.41 | -16.59 | 134 | 26.1 | -15.00 | -2.74 | -21.61 | 242 |
| 36 | Connors RSI(2) · 1h | reversion | 83.41 | -16.59 | 188 | 40.4 | -21.48 | -6.87 | -21.89 | 152 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.37 | -19.33 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.61 | -30.48 | 38 |
| 39 | MFI reversion · 1h | reversion | 82.40 | -17.60 | 295 | 31.9 | -16.84 | -2.66 | -20.24 | 151 |
| 40 | Ichimoku · 1h | trend | 82.09 | -17.91 | 79 | 13.9 | -20.76 | -4.14 | -24.80 | 118 |
| 41 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.59 | -37.35 | 25 |
| 42 | Supertrend · 1h | trend | 80.55 | -19.45 | 137 | 13.1 | -25.81 | -4.69 | -29.38 | 217 |
| 43 | CCI reversion · 1h | reversion | 80.02 | -19.98 | 255 | 45.9 | -25.04 | -3.87 | -27.91 | 446 |
| 44 | EMA 20/50 cross · 1h | trend | 79.85 | -20.15 | 89 | 11.2 | -23.21 | -4.38 | -26.92 | 137 |
| 45 | RSI momentum · 1h | momentum | 79.63 | -20.37 | 130 | 13.1 | -25.89 | -4.62 | -30.16 | 215 |
| 46 | MACD cross · 1h | trend | 79.54 | -20.46 | 288 | 24.3 | -26.99 | -4.72 | -32.86 | 468 |
| 47 | Williams %R · 1h | reversion | 79.07 | -20.93 | 258 | 46.9 | -34.07 | -6.03 | -34.88 | 522 |
| 48 | MACD zero-line · 1h | trend | 78.42 | -21.58 | 134 | 15.7 | -23.25 | -4.65 | -27.62 | 213 |
| 49 | Z-score reversion · 1h | reversion | 78.34 | -21.66 | 135 | 33.3 | -17.08 | -2.64 | -22.55 | 207 |
| 50 | Triple EMA stack · 1h | trend | 78.10 | -21.90 | 121 | 14.9 | -30.22 | -5.56 | -33.51 | 209 |
| 51 | Heikin-Ashi · 1h | trend | 78.05 | -21.95 | 340 | 23.5 | -40.76 | -8.74 | -42.28 | 662 |
| 52 | Bollinger reversion · 1h | reversion | 78.04 | -21.96 | 203 | 37.4 | -29.51 | -6.17 | -30.72 | 373 |
| 53 | OBV trend · 1h | momentum | 77.77 | -22.23 | 234 | 17.5 | -32.85 | -6.60 | -36.12 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 76.27 | -23.73 | 117 | 20.5 | -25.89 | -4.48 | -29.81 | 217 |
| 55 | ROC + volume · 1h | momentum | 75.75 | -24.25 | 293 | 25.6 | -28.45 | -4.98 | -32.73 | 380 |
| 56 | Max aggression: 1-day momentum | meta | 73.41 | -26.59 | 21 | 33.3 | -33.79 | -1.99 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.08 | -26.92 | 122 | 26.2 | -21.95 | -3.88 | -26.17 | 197 |
| 58 | VWAP momentum · 1h | momentum | 72.09 | -27.91 | 665 | 22.3 | -51.20 | -10.77 | -51.46 | 1243 |
| 59 | Candlestick reversal · 1h | reversion | 71.55 | -28.45 | 328 | 27.7 | -33.99 | -6.65 | -35.71 | 547 |
| 60 | EMA 9/21 cross · 1h | trend | 71.14 | -28.86 | 210 | 10.0 | -33.78 | -6.30 | -37.32 | 334 |
| 61 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -17.45 | -2.85 | -18.36 | 343 |
| 62 | Three white soldiers | momentum | 70.82 | -29.18 | 399 | 16.3 | -45.16 | -20.95 | -45.45 | 625 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -42.94 | -98.90 | 5238 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.52 | -23.57 | -79.67 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.54 | -44.24 | -93.59 | 2540 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.80 | -31.15 | -88.95 | 1944 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.20 | -37.84 | -91.27 | 2357 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.46 | -30.75 | -90.47 | 2253 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -51.84 | -97.77 | 3532 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -56.78 | -96.24 | 3414 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.83 | -34.76 | -93.84 | 2475 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.21 | -34.21 | -82.23 | 1700 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -54.00 | -99.48 | 5925 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -43.37 | -92.96 | 2640 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -36.29 | -95.51 | 3464 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -74.74 | -99.78 | 6252 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.97 | -45.26 | -91.97 | 2316 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.02 | -26.96 | -75.06 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -58.92 | -97.71 | 3583 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.25 | -98.65 | 4867 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.65 | -27.90 | -68.74 | 1209 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -54.62 | -94.68 | 2797 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.59 | -38.14 | -84.64 | 1815 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.00 | -99.62 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.10 | -30.25 | -88.17 | 2257 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.13 | -19.65 | -77.26 | 1737 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.30 | -36.82 | -90.35 | 2246 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -50.75 | -96.43 | 3846 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.64 | -52.16 | -89.78 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.09 | -25.26 | -64.27 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.48 | -24.93 | -73.73 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.51 | -18.90 | -76.78 | 1600 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.77 | -49.58 | -96.77 | 4257 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.61 | -99.93 | 8378 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T03:10 | Three white soldiers | buy | BTC-USD | 17.71 | — | entry signal |
| 2026-11-02T03:00 | Squeeze breakout · 1h | buy | ETH-USD | 22.50 | — | entry signal |
| 2026-11-02T03:00 | Keltner breakout · 1h | buy | ETH-USD | 21.27 | — | entry signal |
| 2026-11-02T03:00 | OBV trend · 1h | buy | BTC-USD | 18.54 | — | entry signal |
| 2026-11-02T02:00 | CCI reversion · 1h | buy | SOL-USD | 6.60 | — | rebalance up |
| 2026-11-02T02:00 | CCI reversion · 1h | buy | DOGE-USD | 6.61 | — | rebalance up |
| 2026-11-02T02:00 | CCI reversion · 1h | sell | XRP-USD | 15.95 | -0.01 | exit signal |
| 2026-11-02T02:00 | Bollinger reversion · 1h | sell | SOL-USD | 1.89 | 0.00 | exit signal |
| 2026-11-02T02:00 | Bollinger reversion · 1h | sell | DOGE-USD | 3.90 | -0.00 | exit signal |
| 2026-11-02T02:00 | Bollinger breakout · 1h | buy | ETH-USD | 20.80 | — | entry signal |
| 2026-11-02T02:00 | Donchian 55/20 · 1h | buy | ETH-USD | 21.79 | — | entry signal |
| 2026-11-02T02:00 | Donchian 20/10 · 1h | buy | ETH-USD | 19.02 | — | entry signal |
| 2026-11-02T02:00 | ROC + volume · 1h | buy | ETH-USD | 18.91 | — | entry signal |
| 2026-11-02T02:00 | VWAP momentum · 1h | buy | SOL-USD | 4.50 | — | entry signal |
| 2026-11-02T02:00 | VWAP momentum · 1h | buy | ETH-USD | 9.00 | — | entry signal |
| 2026-11-02T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.00 | — | entry signal |
| 2026-11-02T02:00 | VWAP momentum · 1h | buy | BTC-USD | 9.00 | — | entry signal |
| 2026-11-02T02:00 | Heikin-Ashi · 1h | buy | ETH-USD | 19.48 | — | entry signal |
| 2026-11-02T02:00 | Parabolic SAR · 1h | buy | XRP-USD | 8.86 | — | entry signal |
| 2026-11-02T02:00 | Parabolic SAR · 1h | buy | DOGE-USD | 18.24 | — | entry signal |
| 2026-11-02T02:00 | Parabolic SAR · 1h | sell | ETH-USD | 4.62 | 0.00 | rebalance down |
| 2026-11-02T02:00 | Supertrend · 1h | buy | ETH-USD | 20.09 | — | entry signal |
| 2026-11-02T02:00 | MACD cross · 1h | buy | XRP-USD | 15.61 | — | entry signal |
| 2026-11-02T02:00 | MACD cross · 1h | buy | SOL-USD | 15.86 | — | entry signal |
| 2026-11-02T02:00 | MACD cross · 1h | buy | ETH-USD | 15.86 | — | entry signal |
| 2026-11-02T02:00 | MACD cross · 1h | sell | BTC-USD | 3.96 | -0.01 | rebalance down |
| 2026-11-02T02:00 | Triple EMA stack · 1h | buy | BTC-USD | 19.48 | — | entry signal |
| 2026-11-02T01:55 | Three white soldiers | sell | SOL-USD | 17.63 | -0.15 | exit signal |
| 2026-11-02T01:50 | Three white soldiers | sell | DOGE-USD | 17.66 | -0.11 | exit signal |
| 2026-11-02T01:15 | Three white soldiers | buy | SOL-USD | 17.77 | — | entry signal |
| 2026-11-02T01:15 | Three white soldiers | buy | DOGE-USD | 17.77 | — | entry signal |
| 2026-11-02T01:00 | CCI reversion · 1h | buy | XRP-USD | 7.52 | — | rebalance up |
| 2026-11-02T01:00 | CCI reversion · 1h | sell | ETH-USD | 12.80 | -0.03 | exit signal |
| 2026-11-02T01:00 | VWAP momentum · 1h | sell | ETH-USD | 10.25 | -0.07 | exit signal |
| 2026-11-02T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 10.22 | -0.10 | exit signal |
| 2026-11-02T01:00 | VWAP momentum · 1h | sell | BTC-USD | 10.23 | -0.09 | exit signal |
| 2026-11-02T01:00 | ADX DI cross · 1h | buy | ETH-USD | 21.27 | — | entry signal |
| 2026-11-02T01:00 | MACD cross · 1h | buy | BTC-USD | 19.82 | — | entry signal |
| 2026-11-02T00:00 | Z-score reversion · 1h | buy | SOL-USD | 13.04 | — | entry signal |
| 2026-11-02T00:00 | Bollinger reversion · 1h | sell | ETH-USD | 3.90 | -0.00 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 03:55:05.000152+00:00 -> 2026-11-02 04:05:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
