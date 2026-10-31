# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-31T03:25:05.000116+00:00 · 42065 ticks

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

Today: 2460 decisions in 492 calls, $0.0343 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-31T03:25 | 1 / 1 / 3 | cash |  |
| Breezy | 2026-10-31T03:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-31T03:25 | 2 / 3 / 0 | SOL-USD 67% |  |

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
| 7 | VWAP reversion · 1h | reversion | 99.94 | -0.06 | 95 | 45.3 | -12.46 | -3.49 | -12.60 | 142 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.11 | 1.36 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.23 | 2.94 | -2.46 | 95 |
| 10 | Hold SPY | benchmark | 97.19 | -2.81 | 0 | — | -1.35 | -0.67 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.49 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.61 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.42 | -3.16 | -8.60 | 144 |
| 15 | Three white soldiers · 1h | momentum | 94.87 | -5.13 | 17 | 11.8 | -2.56 | -2.35 | -5.07 | 28 |
| 16 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.44 | 1.48 | -8.76 | 203 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -7.15 | -2.76 | -8.12 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.87 | -5.40 | -12.21 | 219 |
| 20 | Parabolic SAR · 1h | trend | 91.49 | -8.51 | 140 | 28.6 | -18.26 | -4.16 | -20.29 | 251 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -20.58 | -7.54 | -20.58 | 96 |
| 22 | Hold BTC | benchmark | 91.31 | -8.69 | 0 | — | -1.41 | 0.08 | -12.65 | 1 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.64 | -16.91 | 1 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.27 | -3.68 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.03 | -1.66 | -12.70 | 88 |
| 26 | Copy: Insider buying | copy | 89.48 | -10.52 | 34 | 35.3 | -23.46 | -4.82 | -23.91 | 69 |
| 27 | Donchian 55/20 · 1h | breakout | 89.34 | -10.66 | 57 | 14.0 | -16.81 | -3.73 | -17.83 | 103 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -0.84 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.44 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.15 | -3.71 | -15.04 | 98 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -14.35 | -3.08 | -17.96 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 85.50 | -14.50 | 222 | 47.3 | -17.86 | -3.08 | -24.77 | 395 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -17.46 | -3.41 | -20.33 | 263 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.75 | -4.70 | -25.77 | 184 |
| 35 | Bollinger breakout · 1h | breakout | 83.42 | -16.58 | 132 | 26.5 | -15.87 | -2.94 | -21.61 | 240 |
| 36 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.31 | -6.85 | -22.05 | 158 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -4.98 | -19.32 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.65 | -3.47 | -30.47 | 35 |
| 39 | MFI reversion · 1h | reversion | 82.37 | -17.63 | 295 | 31.9 | -20.69 | -3.33 | -22.47 | 153 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.36 | -19.64 | 137 | 13.1 | -26.47 | -4.89 | -29.25 | 216 |
| 43 | CCI reversion · 1h | reversion | 80.36 | -19.64 | 251 | 46.2 | -26.02 | -4.05 | -28.85 | 451 |
| 44 | EMA 20/50 cross · 1h | trend | 80.09 | -19.91 | 88 | 11.4 | -22.94 | -4.34 | -26.95 | 135 |
| 45 | MACD cross · 1h | trend | 79.55 | -20.45 | 283 | 24.0 | -28.85 | -5.15 | -32.85 | 469 |
| 46 | Williams %R · 1h | reversion | 79.35 | -20.65 | 254 | 46.9 | -34.94 | -6.10 | -36.14 | 528 |
| 47 | RSI momentum · 1h | momentum | 79.11 | -20.89 | 130 | 13.1 | -26.63 | -4.83 | -30.14 | 214 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.16 | -4.88 | -27.15 | 213 |
| 49 | Heikin-Ashi · 1h | trend | 78.63 | -21.37 | 334 | 23.7 | -41.53 | -9.06 | -41.89 | 667 |
| 50 | Z-score reversion · 1h | reversion | 78.49 | -21.51 | 131 | 34.4 | -17.69 | -2.76 | -22.55 | 213 |
| 51 | Bollinger reversion · 1h | reversion | 78.09 | -21.91 | 199 | 37.7 | -31.08 | -6.54 | -33.02 | 381 |
| 52 | Triple EMA stack · 1h | trend | 78.04 | -21.96 | 120 | 15.0 | -30.28 | -5.64 | -33.28 | 206 |
| 53 | OBV trend · 1h | momentum | 77.91 | -22.09 | 232 | 17.7 | -33.01 | -6.72 | -35.72 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 76.05 | -23.95 | 116 | 20.7 | -26.43 | -4.64 | -29.81 | 215 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -29.13 | -5.16 | -32.80 | 379 |
| 56 | VWAP momentum · 1h | momentum | 73.51 | -26.49 | 647 | 22.7 | -51.46 | -10.95 | -51.83 | 1233 |
| 57 | Three white soldiers | momentum | 73.45 | -26.55 | 377 | 17.2 | -44.77 | -20.74 | -44.77 | 619 |
| 58 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -28.37 | -1.52 | -50.32 | 42 |
| 59 | RSI(14) reversion · 1h | reversion | 73.18 | -26.82 | 118 | 26.3 | -20.45 | -3.60 | -26.17 | 195 |
| 60 | Candlestick reversal · 1h | reversion | 71.97 | -28.03 | 321 | 28.3 | -35.70 | -7.02 | -36.80 | 557 |
| 61 | Agent (ML meta-label) | meta | 71.52 | -28.48 | 1179 | 20.9 | -16.89 | -3.20 | -18.92 | 371 |
| 62 | EMA 9/21 cross · 1h | trend | 71.11 | -28.89 | 205 | 10.2 | -35.17 | -6.69 | -36.61 | 334 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -43.83 | -98.84 | 5213 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.98 | -23.45 | -79.40 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -44.69 | -93.55 | 2534 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.59 | -30.23 | -88.77 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.96 | -37.15 | -91.07 | 2341 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.02 | -31.42 | -90.02 | 2219 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -51.64 | -97.71 | 3522 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -58.96 | -96.16 | 3401 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.92 | -36.12 | -93.92 | 2464 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.82 | -33.26 | -81.91 | 1685 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -53.39 | -99.47 | 5920 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.82 | -42.86 | -92.85 | 2633 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -38.03 | -95.41 | 3449 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -74.06 | -99.78 | 6250 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -43.63 | -91.87 | 2307 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.57 | -27.49 | -75.79 | 1586 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -61.93 | -97.66 | 3574 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.01 | -98.67 | 4861 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.93 | -28.07 | -69.11 | 1213 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -52.90 | -94.68 | 2797 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -37.40 | -84.71 | 1820 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -66.93 | -99.61 | 6379 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.22 | -29.65 | -88.35 | 2254 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.63 | -19.41 | -77.94 | 1738 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.65 | -37.22 | -90.78 | 2266 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.39 | -49.17 | -96.39 | 3840 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.82 | -52.18 | -89.90 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.68 | -25.59 | -64.70 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.82 | -25.35 | -73.84 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.10 | -18.26 | -76.63 | 1593 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.80 | -49.16 | -96.80 | 4266 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.06 | -99.92 | 8354 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-31T03:20 | Agent (ML meta-label) | sell | ETH-USD | 5.92 | -0.04 | selected signal exited |
| 2026-10-31T03:00 | Agent (ML meta-label) | sell | ETH-USD | 3.82 | -0.02 | rebalance down |
| 2026-10-31T03:00 | Heikin-Ashi · 1h | sell | XRP-USD | 19.60 | -0.02 | exit signal |
| 2026-10-31T03:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 17.79 | — | entry signal |
| 2026-10-31T02:26 | Agent (ML meta-label) | buy | ETH-USD | 3.84 | — | rebalance up |
| 2026-10-31T02:05 | Agent (ML meta-label) | buy | ETH-USD | 5.97 | — | entry |
| 2026-10-31T02:00 | Agent (ML meta-label) | sell | ETH-USD | 11.87 | -0.07 | selected signal exited |
| 2026-10-31T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.97 | -0.04 | exit signal |
| 2026-10-31T02:00 | VWAP momentum · 1h | buy | SOL-USD | 18.41 | — | entry |
| 2026-10-31T02:00 | VWAP momentum · 1h | sell | XRP-USD | 10.46 | 0.03 | exit signal |
| 2026-10-31T02:00 | VWAP momentum · 1h | sell | ETH-USD | 12.27 | 0.01 | exit signal |
| 2026-10-31T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.03 | -0.01 | exit signal |
| 2026-10-31T02:00 | VWAP momentum · 1h | sell | BTC-USD | 4.28 | -0.03 | exit signal |
| 2026-10-31T01:56 | Agent (ML meta-label) | buy | ETH-USD | 11.94 | — | entry |
| 2026-10-31T01:26 | Agent (ML meta-label) | sell | ETH-USD | 11.65 | -0.07 | selected signal exited |
| 2026-10-31T01:25 | Three white soldiers | sell | SOL-USD | 18.29 | -0.14 | exit signal |
| 2026-10-31T01:25 | Three white soldiers | sell | BTC-USD | 18.34 | -0.10 | exit signal |
| 2026-10-31T01:20 | Agent (ML meta-label) | buy | ETH-USD | 11.72 | — | entry |
| 2026-10-31T01:00 | CCI reversion · 1h | buy | SOL-USD | 17.60 | — | rebalance up |
| 2026-10-31T01:00 | CCI reversion · 1h | buy | BTC-USD | 8.62 | — | rebalance up |
| 2026-10-31T01:00 | CCI reversion · 1h | sell | XRP-USD | 11.51 | 0.06 | exit signal |
| 2026-10-31T01:00 | CCI reversion · 1h | sell | ETH-USD | 11.48 | 0.07 | exit signal |
| 2026-10-31T01:00 | CCI reversion · 1h | sell | DOGE-USD | 11.55 | -0.03 | exit signal |
| 2026-10-31T01:00 | Williams %R · 1h | buy | DOGE-USD | 13.26 | — | entry |
| 2026-10-31T01:00 | Williams %R · 1h | sell | SOL-USD | 13.46 | 0.06 | exit signal |
| 2026-10-31T01:00 | Stochastic reversion · 1h | sell | SOL-USD | 4.55 | 0.02 | exit signal |
| 2026-10-31T01:00 | Bollinger reversion · 1h | sell | BTC-USD | 4.11 | -0.00 | exit signal |
| 2026-10-31T01:00 | Three white soldiers · 1h | buy | SOL-USD | 23.73 | — | entry signal |
| 2026-10-31T01:00 | VWAP momentum · 1h | buy | BTC-USD | 4.32 | — | entry signal |
| 2026-10-31T01:00 | VWAP momentum · 1h | sell | XRP-USD | 4.32 | 0.03 | rebalance down |
| 2026-10-31T01:00 | Heikin-Ashi · 1h | buy | BTC-USD | 19.39 | — | entry signal |
| 2026-10-31T00:55 | Three white soldiers | sell | XRP-USD | 18.42 | -0.05 | exit signal |
| 2026-10-31T00:50 | Three white soldiers | buy | SOL-USD | 18.43 | — | entry signal |
| 2026-10-31T00:47 | Agent (ML meta-label) | sell | SOL-USD | 10.23 | -0.04 | selected signal exited |
| 2026-10-31T00:47 | Agent (ML meta-label) | sell | ETH-USD | 10.20 | -0.06 | selected signal exited |
| 2026-10-31T00:45 | Agent (ML meta-label) | buy | ETH-USD | 10.26 | — | entry |
| 2026-10-31T00:45 | Agent (ML meta-label) | sell | SOL-USD | 7.68 | -0.03 | rebalance down |
| 2026-10-31T00:45 | Three white soldiers | buy | BTC-USD | 18.44 | — | entry signal |
| 2026-10-31T00:30 | Three white soldiers | sell | SOL-USD | 18.37 | -0.10 | exit signal |
| 2026-10-31T00:30 | Three white soldiers | sell | BTC-USD | 18.47 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-02 03:25:05.000116+00:00 -> 2026-10-31 03:35:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
