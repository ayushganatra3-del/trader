# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-01T15:25:05.000139+00:00 · 43909 ticks

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

Today: 12006 decisions in 2418 calls, $0.1675 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-01T15:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-01T15:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-01T15:25 | 1 / 2 / 2 | cash |  |

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
| 7 | VWAP reversion · 1h | reversion | 99.89 | -0.11 | 96 | 44.8 | -12.51 | -3.50 | -12.67 | 143 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.11 | 1.36 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.23 | 2.94 | -2.46 | 95 |
| 10 | Hold SPY | benchmark | 97.19 | -2.81 | 0 | — | -1.35 | -0.74 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.57 | -5.83 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.61 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.42 | -3.16 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.37 | 1.46 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -7.15 | -2.76 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.67 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -3.56 | -1.33 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 92.11 | -7.89 | 0 | — | -1.21 | 0.04 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.63 | -5.16 | -12.21 | 210 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -18.11 | -6.71 | -18.30 | 88 |
| 22 | Parabolic SAR · 1h | trend | 91.33 | -8.67 | 140 | 28.6 | -16.37 | -3.75 | -20.27 | 247 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.71 | -16.91 | 2 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.28 | -4.11 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.12 | -9.88 | 58 | 24.1 | -6.15 | -1.70 | -12.89 | 89 |
| 26 | Copy: Insider buying | copy | 89.48 | -10.52 | 34 | 35.3 | -22.37 | -4.56 | -23.61 | 62 |
| 27 | Donchian 55/20 · 1h | breakout | 89.20 | -10.80 | 57 | 14.0 | -16.93 | -3.76 | -17.94 | 104 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -1.09 | -14.73 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.70 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.42 | -3.81 | -15.04 | 97 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -16.04 | -3.32 | -19.57 | 106 |
| 32 | Stochastic reversion · 1h | reversion | 85.47 | -14.53 | 224 | 47.3 | -19.08 | -3.39 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -15.40 | -2.94 | -20.33 | 257 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.75 | -4.70 | -25.77 | 184 |
| 35 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.48 | -6.93 | -21.89 | 152 |
| 36 | Bollinger breakout · 1h | breakout | 83.35 | -16.65 | 133 | 26.3 | -15.03 | -2.76 | -21.61 | 240 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -5.42 | -19.33 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.60 | -3.64 | -30.47 | 38 |
| 39 | MFI reversion · 1h | reversion | 82.37 | -17.63 | 295 | 31.9 | -19.00 | -3.05 | -21.21 | 150 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.26 | -19.74 | 137 | 13.1 | -26.09 | -4.80 | -29.36 | 216 |
| 43 | EMA 20/50 cross · 1h | trend | 79.97 | -20.03 | 88 | 11.4 | -22.99 | -4.36 | -26.79 | 136 |
| 44 | CCI reversion · 1h | reversion | 79.95 | -20.05 | 253 | 46.2 | -26.80 | -4.21 | -28.52 | 447 |
| 45 | MACD cross · 1h | trend | 79.54 | -20.46 | 285 | 24.2 | -28.69 | -5.11 | -32.85 | 468 |
| 46 | Williams %R · 1h | reversion | 79.19 | -20.81 | 257 | 47.1 | -35.22 | -6.32 | -35.94 | 525 |
| 47 | RSI momentum · 1h | momentum | 79.09 | -20.91 | 130 | 13.1 | -26.26 | -4.73 | -30.14 | 215 |
| 48 | MACD zero-line · 1h | trend | 78.60 | -21.40 | 132 | 15.9 | -23.08 | -4.64 | -27.53 | 213 |
| 49 | Z-score reversion · 1h | reversion | 78.46 | -21.55 | 134 | 33.6 | -16.93 | -2.63 | -22.55 | 205 |
| 50 | Bollinger reversion · 1h | reversion | 78.08 | -21.92 | 199 | 37.7 | -31.10 | -6.61 | -32.20 | 375 |
| 51 | Triple EMA stack · 1h | trend | 77.98 | -22.02 | 120 | 15.0 | -30.18 | -5.59 | -33.37 | 207 |
| 52 | Heikin-Ashi · 1h | trend | 77.93 | -22.07 | 340 | 23.5 | -41.35 | -9.01 | -42.23 | 664 |
| 53 | OBV trend · 1h | momentum | 77.62 | -22.38 | 233 | 17.6 | -33.07 | -6.73 | -36.08 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 75.99 | -24.01 | 117 | 20.5 | -26.13 | -4.57 | -29.81 | 216 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -28.63 | -5.04 | -32.80 | 377 |
| 56 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -33.79 | -2.00 | -50.32 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 73.00 | -27.00 | 122 | 26.2 | -21.49 | -3.83 | -26.17 | 193 |
| 58 | VWAP momentum · 1h | momentum | 72.54 | -27.46 | 658 | 22.5 | -51.56 | -11.05 | -51.56 | 1235 |
| 59 | Candlestick reversal · 1h | reversion | 71.59 | -28.41 | 326 | 27.9 | -35.39 | -7.02 | -35.71 | 547 |
| 60 | Three white soldiers | momentum | 71.45 | -28.55 | 394 | 16.5 | -45.03 | -21.13 | -45.10 | 623 |
| 61 | Agent (ML meta-label) | meta | 71.09 | -28.91 | 1191 | 20.7 | -16.50 | -3.13 | -18.66 | 351 |
| 62 | EMA 9/21 cross · 1h | trend | 70.94 | -29.06 | 208 | 10.1 | -33.61 | -6.27 | -37.09 | 332 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -45.19 | -98.90 | 5241 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.72 | -24.15 | -79.72 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.66 | -46.78 | -93.68 | 2545 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -31.64 | -88.93 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.25 | -38.81 | -91.29 | 2354 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.30 | -31.44 | -90.31 | 2240 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -54.73 | -97.78 | 3533 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -61.70 | -96.29 | 3418 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.74 | -35.22 | -93.74 | 2457 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.97 | -34.31 | -82.00 | 1690 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -56.40 | -99.47 | 5913 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.91 | -44.52 | -92.92 | 2637 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.12 | -95.46 | 3455 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.56 | -99.78 | 6244 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.99 | -45.74 | -91.99 | 2317 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.60 | -26.62 | -74.84 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -64.63 | -97.75 | 3584 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -63.70 | -98.66 | 4866 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.92 | -28.48 | -69.01 | 1213 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -55.99 | -94.66 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.60 | -38.74 | -84.64 | 1813 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -73.94 | -99.62 | 6374 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.02 | -30.66 | -88.07 | 2254 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.97 | -19.77 | -77.08 | 1730 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.33 | -37.94 | -90.33 | 2249 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.35 | -52.08 | -96.37 | 3837 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.72 | -53.11 | -89.77 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.47 | -25.72 | -64.49 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.70 | -25.78 | -73.82 | 1275 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.87 | -18.89 | -76.17 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.80 | -52.15 | -96.80 | 4259 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -114.14 | -99.93 | 8385 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-01T15:00 | Bollinger reversion · 1h | buy | SOL-USD | 4.34 | — | entry signal |
| 2026-11-01T15:00 | VWAP momentum · 1h | buy | ETH-USD | 7.94 | — | entry signal |
| 2026-11-01T15:00 | VWAP momentum · 1h | buy | BTC-USD | 12.11 | — | entry signal |
| 2026-11-01T15:00 | VWAP momentum · 1h | sell | XRP-USD | 6.00 | -0.04 | rebalance down |
| 2026-11-01T15:00 | MACD cross · 1h | buy | DOGE-USD | 19.91 | — | entry signal |
| 2026-11-01T14:00 | OBV trend · 1h | buy | ETH-USD | 19.42 | — | entry signal |
| 2026-11-01T14:00 | VWAP momentum · 1h | buy | XRP-USD | 18.18 | — | entry signal |
| 2026-11-01T13:25 | Three white soldiers | sell | DOGE-USD | 17.79 | -0.10 | target is flat |
| 2026-11-01T13:20 | Three white soldiers | buy | DOGE-USD | 17.89 | — | entry signal |
| 2026-11-01T13:05 | Williams %R · 1h | sell | DOGE-USD | 3.95 | -0.01 | rebalance down |
| 2026-11-01T13:05 | MACD zero-line · 1h | sell | DOGE-USD | 19.54 | -0.18 | target is flat |
| 2026-11-01T13:05 | MACD cross · 1h | sell | DOGE-USD | 19.87 | -0.01 | target is flat |
| 2026-11-01T13:00 | Williams %R · 1h | buy | SOL-USD | 15.43 | — | entry signal |
| 2026-11-01T13:00 | Bollinger breakout · 1h | sell | ETH-USD | 20.81 | -0.04 | exit signal |
| 2026-11-01T13:00 | Donchian 20/10 · 1h | sell | ETH-USD | 18.97 | -0.04 | exit signal |
| 2026-11-01T13:00 | OBV trend · 1h | sell | ETH-USD | 19.24 | -0.24 | exit signal |
| 2026-11-01T13:00 | VWAP momentum · 1h | sell | XRP-USD | 5.02 | -0.05 | exit signal |
| 2026-11-01T13:00 | VWAP momentum · 1h | sell | ETH-USD | 9.06 | -0.08 | exit signal |
| 2026-11-01T13:00 | VWAP momentum · 1h | sell | DOGE-USD | 9.04 | -0.08 | exit signal |
| 2026-11-01T13:00 | VWAP momentum · 1h | sell | BTC-USD | 9.10 | -0.02 | exit signal |
| 2026-11-01T13:00 | MACD zero-line · 1h | sell | ETH-USD | 19.70 | -0.03 | exit signal |
| 2026-11-01T13:00 | MACD cross · 1h | buy | XRP-USD | 4.06 | — | rebalance up |
| 2026-11-01T13:00 | MACD cross · 1h | buy | DOGE-USD | 4.01 | — | rebalance up |
| 2026-11-01T13:00 | MACD cross · 1h | buy | BTC-USD | 4.15 | — | rebalance up |
| 2026-11-01T13:00 | MACD cross · 1h | sell | ETH-USD | 15.99 | 0.13 | exit signal |
| 2026-11-01T12:20 | Candlestick reversal · 1h | sell | SOL-USD | 8.81 | -0.15 | stop-loss |
| 2026-11-01T12:00 | Heikin-Ashi · 1h | sell | BTC-USD | 19.49 | -0.06 | exit signal |
| 2026-11-01T11:00 | Heikin-Ashi · 1h | sell | ETH-USD | 19.47 | -0.07 | exit signal |
| 2026-11-01T11:00 | Parabolic SAR · 1h | buy | XRP-USD | 22.87 | — | entry signal |
| 2026-11-01T11:00 | Triple EMA stack · 1h | buy | ETH-USD | 19.51 | — | entry signal |
| 2026-11-01T10:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.11 | -0.13 | exit signal |
| 2026-11-01T10:00 | Three white soldiers | sell | XRP-USD | 17.80 | -0.12 | target is flat |
| 2026-11-01T09:50 | Three white soldiers | buy | XRP-USD | 17.92 | — | entry signal |
| 2026-11-01T09:05 | CCI reversion · 1h | buy | DOGE-USD | 20.06 | — | entry |
| 2026-11-01T09:00 | CCI reversion · 1h | sell | DOGE-USD | 20.16 | 0.11 | exit signal |
| 2026-11-01T09:00 | Squeeze breakout · 1h | buy | BTC-USD | 22.56 | — | entry signal |
| 2026-11-01T09:00 | Donchian 55/20 · 1h | buy | ETH-USD | 22.33 | — | entry signal |
| 2026-11-01T09:00 | OBV trend · 1h | buy | ETH-USD | 19.48 | — | entry signal |
| 2026-11-01T09:00 | Supertrend · 1h | buy | BTC-USD | 20.09 | — | entry signal |
| 2026-11-01T09:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 20.02 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-03 15:25:05.000139+00:00 -> 2026-11-01 15:35:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
