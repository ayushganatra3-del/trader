# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-31T17:55:05.000121+00:00 · 42796 ticks

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

Today: 13392 decisions in 2685 calls, $0.1869 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-31T17:55 | 2 / 3 / 0 | BTC-USD 19% |  |
| Breezy | 2026-10-31T17:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-31T17:55 | 2 / 3 / 0 | ETH-USD 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.83 | +1.03% | 6 |
| Candlestick reversal | LABU | 2.63 | +8.02% | 17 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Stochastic reversion | ETHU | 2.47 | +6.74% | 16 |
| Connors RSI(2) | SQQQ | 2.21 | +2.50% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.51 | 6.51 | 0 | — | 7.73 | 3.81 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.60 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.65 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.87 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.89 | -0.11 | 96 | 44.8 | -12.42 | -3.48 | -12.61 | 144 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.11 | 1.36 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.75 | 3.21 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.19 | -2.81 | 0 | — | -1.35 | -0.67 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.49 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.61 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.42 | -3.16 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.46 | 1.48 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -7.15 | -2.76 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.67 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 91.73 | -8.27 | 0 | — | -2.10 | 0.16 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.64 | -5.16 | -12.21 | 218 |
| 21 | Parabolic SAR · 1h | trend | 91.49 | -8.51 | 140 | 28.6 | -16.23 | -3.71 | -20.27 | 246 |
| 22 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -19.01 | -7.03 | -19.04 | 91 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.64 | -16.91 | 1 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -3.68 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.03 | -1.66 | -12.70 | 88 |
| 26 | Copy: Insider buying | copy | 89.48 | -10.52 | 34 | 35.3 | -23.06 | -4.70 | -23.73 | 68 |
| 27 | Donchian 55/20 · 1h | breakout | 89.33 | -10.66 | 57 | 14.0 | -16.81 | -3.73 | -17.83 | 103 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -0.84 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.44 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.27 | -3.75 | -15.04 | 98 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -16.04 | -3.32 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.47 | -14.53 | 224 | 47.3 | -19.07 | -3.39 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -16.24 | -3.11 | -20.33 | 260 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.75 | -4.70 | -25.77 | 184 |
| 35 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.47 | -6.92 | -22.04 | 155 |
| 36 | Bollinger breakout · 1h | breakout | 83.38 | -16.62 | 132 | 26.5 | -15.90 | -2.95 | -21.61 | 241 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -4.98 | -19.33 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.65 | -3.47 | -30.48 | 35 |
| 39 | MFI reversion · 1h | reversion | 82.36 | -17.64 | 295 | 31.9 | -16.32 | -2.58 | -20.24 | 151 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.36 | -19.64 | 137 | 13.1 | -25.99 | -4.78 | -29.25 | 215 |
| 43 | CCI reversion · 1h | reversion | 80.30 | -19.70 | 252 | 46.0 | -26.55 | -4.16 | -28.56 | 447 |
| 44 | EMA 20/50 cross · 1h | trend | 80.09 | -19.91 | 88 | 11.4 | -23.05 | -4.38 | -26.95 | 135 |
| 45 | MACD cross · 1h | trend | 79.70 | -20.30 | 283 | 24.0 | -29.10 | -5.19 | -32.86 | 470 |
| 46 | Williams %R · 1h | reversion | 79.23 | -20.77 | 257 | 47.1 | -35.15 | -6.31 | -35.91 | 523 |
| 47 | RSI momentum · 1h | momentum | 79.11 | -20.89 | 130 | 13.1 | -26.32 | -4.76 | -30.14 | 213 |
| 48 | MACD zero-line · 1h | trend | 78.88 | -21.12 | 130 | 16.2 | -23.25 | -4.68 | -27.22 | 211 |
| 49 | Z-score reversion · 1h | reversion | 78.50 | -21.50 | 132 | 34.1 | -17.68 | -2.76 | -22.55 | 213 |
| 50 | Heikin-Ashi · 1h | trend | 78.27 | -21.73 | 336 | 23.8 | -41.81 | -9.14 | -42.04 | 668 |
| 51 | Bollinger reversion · 1h | reversion | 78.09 | -21.91 | 199 | 37.7 | -31.72 | -6.75 | -32.94 | 377 |
| 52 | Triple EMA stack · 1h | trend | 78.04 | -21.96 | 120 | 15.0 | -30.42 | -5.69 | -33.25 | 206 |
| 53 | OBV trend · 1h | momentum | 77.91 | -22.09 | 232 | 17.7 | -32.80 | -6.65 | -36.05 | 298 |
| 54 | Donchian 20/10 · 1h | breakout | 76.02 | -23.98 | 116 | 20.7 | -26.46 | -4.65 | -29.81 | 216 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -29.10 | -5.18 | -32.78 | 380 |
| 56 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -28.37 | -1.52 | -50.32 | 42 |
| 57 | VWAP momentum · 1h | momentum | 73.30 | -26.70 | 648 | 22.7 | -51.26 | -10.86 | -51.85 | 1232 |
| 58 | RSI(14) reversion · 1h | reversion | 73.19 | -26.80 | 118 | 26.3 | -21.21 | -3.77 | -26.17 | 192 |
| 59 | Three white soldiers | momentum | 72.45 | -27.55 | 385 | 16.9 | -44.96 | -21.18 | -44.96 | 621 |
| 60 | Candlestick reversal · 1h | reversion | 71.75 | -28.25 | 325 | 28.0 | -35.48 | -7.03 | -35.90 | 549 |
| 61 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -18.25 | -3.44 | -20.01 | 342 |
| 62 | EMA 9/21 cross · 1h | trend | 70.97 | -29.03 | 206 | 10.2 | -35.36 | -6.73 | -36.73 | 336 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -44.96 | -98.85 | 5214 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.25 | -23.94 | -79.41 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -46.53 | -93.60 | 2539 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.54 | -30.93 | -88.55 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.15 | -38.72 | -91.15 | 2350 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.15 | -31.90 | -90.17 | 2231 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -54.26 | -97.73 | 3523 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -61.74 | -96.20 | 3405 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -34.80 | -93.68 | 2456 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -34.38 | -82.15 | 1696 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -56.04 | -99.47 | 5920 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.83 | -44.38 | -92.83 | 2630 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -38.75 | -95.49 | 3465 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.21 | -99.78 | 6249 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -45.37 | -91.85 | 2307 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.10 | -27.50 | -75.32 | 1576 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -65.54 | -97.72 | 3584 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -63.29 | -98.68 | 4866 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.97 | -28.61 | -68.97 | 1213 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -56.38 | -94.67 | 2793 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.40 | -38.54 | -84.40 | 1808 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -72.87 | -99.62 | 6382 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.99 | -30.42 | -87.99 | 2250 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.59 | -19.59 | -77.75 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.62 | -37.82 | -90.67 | 2261 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -51.61 | -96.42 | 3846 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.80 | -54.79 | -89.80 | 2153 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.47 | -26.15 | -64.48 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.72 | -25.91 | -73.75 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.87 | -18.71 | -77.06 | 1602 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.83 | -51.91 | -96.83 | 4269 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -115.83 | -99.92 | 8364 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-31T17:50 | Three white soldiers | buy | BTC-USD | 18.12 | — | entry signal |
| 2026-10-31T17:30 | Three white soldiers | sell | BTC-USD | 18.03 | -0.13 | stop-loss |
| 2026-10-31T17:20 | Three white soldiers | buy | BTC-USD | 18.16 | — | entry signal |
| 2026-10-31T17:00 | Williams %R · 1h | sell | DOGE-USD | 19.82 | -0.18 | exit signal |
| 2026-10-31T17:00 | Z-score reversion · 1h | sell | XRP-USD | 9.75 | -0.08 | exit signal |
| 2026-10-31T17:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.58 | — | entry signal |
| 2026-10-31T17:00 | MACD zero-line · 1h | buy | ETH-USD | 19.72 | — | entry signal |
| 2026-10-31T17:00 | Three white soldiers | sell | XRP-USD | 18.10 | -0.09 | exit signal |
| 2026-10-31T16:35 | Three white soldiers | sell | SOL-USD | 18.10 | -0.11 | exit signal |
| 2026-10-31T16:01 | VWAP reversion · 1h | sell | DOGE-USD | 24.83 | -0.05 | exit signal |
| 2026-10-31T16:01 | VWAP momentum · 1h | buy | XRP-USD | 1.38 | — | entry signal |
| 2026-10-31T16:01 | VWAP momentum · 1h | buy | DOGE-USD | 10.47 | — | entry signal |
| 2026-10-31T16:01 | VWAP momentum · 1h | sell | ETH-USD | 4.17 | -0.02 | rebalance down |
| 2026-10-31T16:01 | VWAP momentum · 1h | sell | BTC-USD | 4.16 | -0.02 | rebalance down |
| 2026-10-31T16:01 | EMA 9/21 cross · 1h | buy | BTC-USD | 17.49 | — | entry signal |
| 2026-10-31T15:35 | Three white soldiers | buy | XRP-USD | 18.19 | — | entry signal |
| 2026-10-31T15:30 | Three white soldiers | buy | SOL-USD | 18.21 | — | entry signal |
| 2026-10-31T14:40 | Agent (ML meta-label) | sell | SOL-USD | 8.46 | -0.05 | selected signal exited |
| 2026-10-31T14:35 | Agent (ML meta-label) | buy | SOL-USD | 8.51 | — | entry |
| 2026-10-31T14:00 | Candlestick reversal · 1h | sell | XRP-USD | 8.92 | -0.05 | exit signal |
| 2026-10-31T13:55 | Three white soldiers | sell | SOL-USD | 18.12 | -0.15 | stop-loss |
| 2026-10-31T13:55 | Three white soldiers | sell | BTC-USD | 18.14 | -0.13 | exit signal |
| 2026-10-31T13:50 | Three white soldiers | buy | BTC-USD | 18.27 | — | entry signal |
| 2026-10-31T13:45 | Three white soldiers | buy | SOL-USD | 18.27 | — | entry signal |
| 2026-10-31T13:00 | Bollinger breakout · 1h | buy | ETH-USD | 20.85 | — | entry signal |
| 2026-10-31T13:00 | Donchian 20/10 · 1h | buy | ETH-USD | 19.01 | — | entry signal |
| 2026-10-31T13:00 | Three white soldiers | sell | DOGE-USD | 18.19 | -0.11 | exit signal |
| 2026-10-31T12:25 | Three white soldiers | buy | DOGE-USD | 18.30 | — | entry signal |
| 2026-10-31T12:00 | CCI reversion · 1h | buy | DOGE-USD | 7.66 | — | rebalance up |
| 2026-10-31T12:00 | CCI reversion · 1h | sell | BTC-USD | 16.00 | -0.00 | exit signal |
| 2026-10-31T12:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 17.74 | — | entry signal |
| 2026-10-31T11:45 | Agent (ML meta-label) | sell | SOL-USD | 3.08 | -0.01 | selected signal exited |
| 2026-10-31T11:40 | Agent (ML meta-label) | buy | SOL-USD | 3.09 | — | entry |
| 2026-10-31T10:00 | CCI reversion · 1h | buy | DOGE-USD | 12.39 | — | entry signal |
| 2026-10-31T10:00 | CCI reversion · 1h | sell | BTC-USD | 4.06 | -0.01 | rebalance down |
| 2026-10-31T10:00 | Candlestick reversal · 1h | buy | XRP-USD | 8.97 | — | entry signal |
| 2026-10-31T10:00 | VWAP momentum · 1h | buy | ETH-USD | 14.67 | — | entry signal |
| 2026-10-31T10:00 | VWAP momentum · 1h | buy | BTC-USD | 14.67 | — | entry signal |
| 2026-10-31T08:00 | Agent (ML meta-label) | sell | SOL-USD | 11.80 | -0.07 | selected signal exited |
| 2026-10-31T08:00 | Candlestick reversal · 1h | sell | DOGE-USD | 5.91 | -0.10 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-02 17:55:05.000121+00:00 -> 2026-10-31 18:05:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
