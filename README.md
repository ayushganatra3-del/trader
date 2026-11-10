# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T18:26:05.000142+00:00 · 54857 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.51 (-12.49%)

Closed trades 169, win rate 35.5%, fees £5.10, max drawdown -13.61%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 26447 decisions in 2719 calls, $0.3347 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T18:26 | 5 / 9 / 16 | XRP-USD 15% |  |
| Breezy | 2026-11-10T18:26 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-10T18:26 | 4 / 18 / 8 | BITX 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.91 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.94 | 14.94 | 0 | — | 14.87 | 4.92 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.30 | 1.30 | 0 | — | 4.06 | 1.18 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -2.80 | -1.11 | -9.22 | 148 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.42 | -3.58 | 0 | — | -2.30 | -0.73 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.51 | -4.49 | 137 | 46.0 | -13.44 | -3.43 | -13.73 | 153 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -4.82 | -1.26 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.89 | -3.50 | -5.99 | 29 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 93.03 | -6.97 | 108 | 23.1 | -13.19 | -4.89 | -17.51 | 78 |
| 19 | Copy: Insider buying | copy | 92.83 | -7.17 | 42 | 38.1 | -8.10 | -1.67 | -15.11 | 67 |
| 20 | Copy: Congress Democrats (NANC) | copy | 92.34 | -7.66 | 0 | — | -4.57 | -1.21 | -10.64 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.75 | -11.25 | 403 | 33.3 | -14.68 | -4.55 | -14.78 | 605 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.28 | -2.87 | -14.15 | 76 |
| 24 | Agent | meta | 87.51 | -12.49 | 169 | 35.5 | -13.37 | -6.79 | -14.52 | 200 |
| 25 | Daily: Bullish score | daily | 86.92 | -13.08 | 15 | 20.0 | -7.97 | -1.18 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.72 | -14.28 | 1 | 0.0 | -7.09 | -0.95 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.12 | -14.88 | 168 | 26.8 | -14.14 | -2.88 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.98 | -15.02 | 79 | 32.9 | -15.53 | -4.33 | -18.49 | 95 |
| 29 | Donchian 55/20 · 1h | breakout | 84.49 | -15.51 | 71 | 14.1 | -16.28 | -3.38 | -22.08 | 101 |
| 30 | Keltner breakout · 1h | breakout | 81.53 | -18.47 | 110 | 23.6 | -21.09 | -4.36 | -25.32 | 176 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 81.51 | -18.49 | 2 | 0.0 | -10.16 | -1.18 | -24.16 | 1 |
| 32 | Opening range 15m | breakout | 81.22 | -18.78 | 499 | 31.5 | -19.59 | -5.38 | -20.33 | 740 |
| 33 | Connors RSI(2) · 1h | reversion | 80.84 | -19.16 | 206 | 39.8 | -19.58 | -6.51 | -19.99 | 126 |
| 34 | Stochastic reversion · 1h | reversion | 80.76 | -19.24 | 284 | 47.5 | -26.23 | -3.85 | -27.81 | 393 |
| 35 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -15.42 | -3.59 | -22.08 | 93 |
| 36 | Max aggression: 5-day momentum | meta | 79.21 | -20.79 | 18 | 44.4 | -37.24 | -2.40 | -45.81 | 25 |
| 37 | Heikin-Ashi · 1h | trend | 78.90 | -21.10 | 416 | 24.5 | -40.11 | -7.46 | -42.43 | 664 |
| 38 | ADX DI cross · 1h | trend | 78.63 | -21.37 | 184 | 19.0 | -25.12 | -4.33 | -29.95 | 270 |
| 39 | CCI reversion · 1h | reversion | 77.33 | -22.67 | 326 | 45.1 | -25.69 | -3.88 | -30.69 | 453 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.19 | -4.37 | -27.99 | 236 |
| 41 | MFI reversion · 1h | reversion | 76.44 | -23.56 | 359 | 33.7 | -19.65 | -2.49 | -22.11 | 158 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.53 | -8.91 | -31.64 | 121 |
| 43 | EMA 20/50 cross · 1h | trend | 75.03 | -24.96 | 102 | 10.8 | -24.24 | -4.04 | -35.48 | 119 |
| 44 | MACD cross · 1h | trend | 74.08 | -25.92 | 359 | 22.0 | -32.59 | -5.34 | -39.48 | 470 |
| 45 | Bollinger reversion · 1h | reversion | 73.51 | -26.49 | 278 | 40.3 | -27.00 | -4.15 | -32.16 | 369 |
| 46 | MACD zero-line · 1h | trend | 73.44 | -26.56 | 159 | 16.4 | -25.89 | -5.27 | -30.82 | 214 |
| 47 | Supertrend · 1h | trend | 73.04 | -26.96 | 168 | 13.1 | -32.81 | -5.99 | -36.07 | 233 |
| 48 | RSI momentum · 1h | momentum | 72.98 | -27.02 | 159 | 12.6 | -24.60 | -3.96 | -34.05 | 210 |
| 49 | Triple EMA stack · 1h | trend | 72.06 | -27.94 | 144 | 14.6 | -27.24 | -4.79 | -35.45 | 204 |
| 50 | Williams %R · 1h | reversion | 71.98 | -28.02 | 346 | 45.7 | -35.61 | -5.56 | -36.02 | 531 |
| 51 | OBV trend · 1h | momentum | 71.82 | -28.18 | 275 | 18.2 | -27.14 | -4.76 | -35.70 | 277 |
| 52 | ROC + volume · 1h | momentum | 70.68 | -29.32 | 361 | 26.6 | -35.97 | -6.86 | -38.22 | 377 |
| 53 | Z-score reversion · 1h ⏸ | reversion | 70.59 | -29.41 | 190 | 36.3 | -27.29 | -3.87 | -28.98 | 228 |
| 54 | Donchian 20/10 · 1h | breakout | 70.54 | -29.46 | 142 | 19.7 | -31.68 | -5.87 | -35.64 | 208 |
| 55 | Daily: Momentum burst | daily | 70.28 | -29.72 | 27 | 11.1 | -39.03 | -5.59 | -39.41 | 34 |
| 56 | VWAP momentum · 1h | momentum | 66.41 | -33.59 | 838 | 22.0 | -53.25 | -11.32 | -54.38 | 1222 |
| 57 | RSI(14) reversion · 1h | reversion | 66.09 | -33.91 | 170 | 30.6 | -25.75 | -3.50 | -32.54 | 237 |
| 58 | Max aggression: 1-day momentum | meta | 65.22 | -34.78 | 27 | 25.9 | -32.85 | -1.67 | -57.50 | 41 |
| 59 | EMA 9/21 cross · 1h | trend | 65.12 | -34.88 | 251 | 9.6 | -37.56 | -7.41 | -41.69 | 333 |
| 60 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1682 | 24.3 | -16.84 | -2.43 | -22.67 | 342 |
| 61 | Candlestick reversal · 1h | reversion | 63.40 | -36.59 | 445 | 27.9 | -38.75 | -7.01 | -39.88 | 589 |
| 62 | Three white soldiers | momentum | 61.04 | -38.97 | 505 | 14.9 | -48.84 | -22.59 | -48.85 | 650 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.38 | -98.95 | 5239 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.72 | -25.85 | -79.84 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.17 | -44.36 | -93.20 | 2500 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -31.51 | -89.37 | 1916 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.66 | -38.43 | -90.69 | 2311 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.25 | -31.53 | -90.30 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -51.78 | -97.77 | 3446 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -53.92 | -96.20 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -32.33 | -93.63 | 2378 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.30 | -33.80 | -82.40 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -53.32 | -99.56 | 6026 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -41.89 | -92.21 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -36.57 | -95.54 | 3433 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -69.47 | -99.81 | 6155 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -42.10 | -92.00 | 2252 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.53 | -24.30 | -75.58 | 1592 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -58.33 | -97.72 | 3517 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.87 | -61.63 | -98.88 | 4897 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.65 | -26.97 | -68.99 | 1218 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -51.73 | -94.57 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.47 | -36.15 | -84.57 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -70.58 | -99.65 | 6350 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.81 | -31.55 | -89.87 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.54 | -20.13 | -78.64 | 1771 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.90 | -36.39 | -90.96 | 2213 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.82 | -51.76 | -96.83 | 3881 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.37 | -54.94 | -89.38 | 2158 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.42 | -27.07 | -66.10 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.02 | -22.55 | -71.09 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.48 | -19.54 | -80.53 | 1701 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.63 | -97.28 | 4301 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.57 | -99.93 | 8289 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T18:25 | Agent (ML meta-label) | buy | SOXL | 3.96 | — | entry |
| 2026-11-10T18:20 | Three white soldiers | sell | SOXL | 15.17 | -0.04 | exit signal |
| 2026-11-10T18:10 | Agent (ML meta-label) | sell | SOXL | 3.96 | -0.01 | selected signal exited |
| 2026-11-10T18:05 | Agent (ML meta-label) | buy | SOXL | 3.97 | — | entry |
| 2026-11-10T18:05 | VWAP reversion · 1h | sell | DOGE-USD | 23.72 | -0.19 | target is flat |
| 2026-11-10T18:05 | Three white soldiers | buy | SOXL | 3.10 | — | rebalance up |
| 2026-11-10T18:05 | Three white soldiers | sell | TQQQ | 6.21 | -0.03 | exit signal |
| 2026-11-10T18:05 | Three white soldiers | sell | QQQ | 12.23 | -0.03 | exit signal |
| 2026-11-10T18:00 | Agent | sell | TSLA | 17.55 | 0.06 | selected signal exited |
| 2026-11-10T18:00 | Williams %R · 1h | buy | XRP-USD | 17.97 | — | entry signal |
| 2026-11-10T18:00 | Williams %R · 1h | buy | BTC-USD | 17.97 | — | entry signal |
| 2026-11-10T18:00 | Stochastic reversion · 1h | buy | SOL-USD | 13.45 | — | entry signal |
| 2026-11-10T18:00 | Stochastic reversion · 1h | buy | ETH-USD | 13.46 | — | entry signal |
| 2026-11-10T18:00 | Stochastic reversion · 1h | buy | BTC-USD | 13.46 | — | entry signal |
| 2026-11-10T18:00 | Stochastic reversion · 1h | sell | SQQQ | 7.20 | 0.27 | rebalance down |
| 2026-11-10T18:00 | Stochastic reversion · 1h | sell | ETHU | 6.73 | 0.03 | rebalance down |
| 2026-11-10T18:00 | Stochastic reversion · 1h | sell | COIN | 6.62 | -0.21 | rebalance down |
| 2026-11-10T18:00 | VWAP reversion · 1h | buy | SOL-USD | 23.80 | — | entry signal |
| 2026-11-10T18:00 | VWAP reversion · 1h | buy | ETH-USD | 23.90 | — | entry signal |
| 2026-11-10T18:00 | VWAP reversion · 1h | buy | DOGE-USD | 23.90 | — | entry signal |
| 2026-11-10T18:00 | Bollinger reversion · 1h | buy | XRP-USD | 12.26 | — | entry signal |
| 2026-11-10T18:00 | Bollinger reversion · 1h | buy | SOL-USD | 12.26 | — | entry signal |
| 2026-11-10T18:00 | Bollinger reversion · 1h | buy | ETH-USD | 12.26 | — | entry signal |
| 2026-11-10T18:00 | Bollinger reversion · 1h | buy | BTC-USD | 12.26 | — | entry signal |
| 2026-11-10T18:00 | Bollinger reversion · 1h | sell | NVDA | 6.12 | 0.00 | rebalance down |
| 2026-11-10T18:00 | Bollinger reversion · 1h | sell | ETHU | 6.18 | 0.02 | rebalance down |
| 2026-11-10T18:00 | RSI(14) reversion · 1h | buy | XRP-USD | 16.54 | — | entry signal |
| 2026-11-10T18:00 | Candlestick reversal · 1h | buy | SOL-USD | 11.88 | — | entry signal |
| 2026-11-10T18:00 | Candlestick reversal · 1h | buy | ETH-USD | 12.68 | — | entry signal |
| 2026-11-10T18:00 | Candlestick reversal · 1h | buy | BTC-USD | 12.68 | — | entry signal |
| 2026-11-10T18:00 | Candlestick reversal · 1h | sell | ETHU | 3.21 | 0.01 | rebalance down |
| 2026-11-10T18:00 | ROC + volume · 1h | buy | META | 6.44 | — | entry |
| 2026-11-10T18:00 | ROC + volume · 1h | sell | AAPL | 5.56 | -0.01 | target is flat |
| 2026-11-10T18:00 | Three white soldiers | buy | TQQQ | 6.24 | — | entry signal |
| 2026-11-10T18:00 | Three white soldiers | buy | QQQ | 12.26 | — | entry signal |
| 2026-11-10T18:00 | Three white soldiers | sell | SOXL | 3.21 | 0.04 | rebalance down |
| 2026-11-10T17:55 | Three white soldiers | buy | TNA | 15.29 | — | entry signal |
| 2026-11-10T17:55 | Three white soldiers | buy | SOXL | 15.29 | — | entry signal |
| 2026-11-10T17:55 | Three white soldiers | buy | BTC-USD | 15.29 | — | entry signal |
| 2026-11-10T17:50 | Agent (ML meta-label) | sell | SQQQ | 1.31 | -0.00 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 18:26:05.000142+00:00 -> 2026-11-10 18:36:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
