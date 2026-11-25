# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T12:40:05.000122+00:00 · 73049 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.94 (-22.06%)

Closed trades 245, win rate 35.9%, fees £6.71, max drawdown -22.52%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.50 | -0.11 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, COHR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 9855 decisions in 1971 calls, $0.1380 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T12:40 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-25T12:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T12:40 | 2 / 3 / 0 | ETH-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.46 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.08 | 16.08 | 0 | — | 13.68 | 4.60 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.18 | 5.18 | 0 | — | 5.25 | 1.42 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | 0.00 | 0.09 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.50 | -3.50 | 229 | 28.4 | -1.63 | -0.48 | -7.61 | 142 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.69 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.37 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.78 | -5.22 | 0 | — | -6.20 | -1.57 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.16 | -5.84 | 20 | 10.0 | -4.59 | -7.39 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.05 | -6.95 | 0 | — | -7.92 | -1.59 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.84 | -7.16 | 61 | 41.0 | -6.79 | -1.22 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.19 | -8.81 | 116 | 24.1 | -7.93 | -3.99 | -10.85 | 40 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.96 | -10.04 | 0 | — | -11.39 | -2.44 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.74 | -11.13 | 24 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.46 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 85.66 | -14.34 | 170 | 45.3 | -12.01 | -2.20 | -20.49 | 156 |
| 21 | Daily: Bullish score | daily | 85.47 | -14.53 | 20 | 20.0 | -13.12 | -2.89 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.24 | -13.73 | 543 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.17 | -7.33 | -21.50 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.86 | -13.02 | 61 |
| 26 | Parabolic SAR · 1h | trend | 79.25 | -20.75 | 206 | 28.2 | -31.71 | -8.27 | -32.38 | 181 |
| 27 | Volume breakout · 1h | breakout | 78.51 | -21.49 | 169 | 27.8 | -21.81 | -6.52 | -23.66 | 71 |
| 28 | Agent | meta | 77.94 | -22.06 | 245 | 35.9 | -26.46 | -5.97 | -26.72 | 197 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.17 | -4.18 | -18.47 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.19 | -22.81 | 138 | 24.6 | -24.69 | -6.33 | -27.01 | 148 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -21.85 | -6.71 | -22.57 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.48 | -23.52 | 87 | 13.8 | -29.08 | -7.76 | -29.57 | 82 |
| 33 | Ichimoku · 1h | trend | 74.91 | -25.09 | 113 | 15.9 | -29.47 | -7.46 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.86 | -29.14 | 260 | 19.2 | -37.21 | -7.00 | -38.51 | 292 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.76 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.36 | -30.64 | 208 | 22.1 | -30.94 | -7.98 | -33.57 | 207 |
| 37 | Supertrend · 1h | trend | 69.12 | -30.88 | 207 | 18.4 | -36.58 | -7.18 | -37.75 | 208 |
| 38 | Triple EMA stack · 1h | trend | 68.63 | -31.37 | 169 | 15.4 | -38.27 | -9.76 | -38.73 | 171 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 68.28 | -31.72 | 3 | 0.0 | -25.78 | -3.19 | -32.18 | 1 |
| 40 | Hold BTC | benchmark | 68.08 | -31.92 | 3 | 0.0 | -30.35 | -5.42 | -36.10 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 68.03 | -31.97 | 124 | 9.7 | -37.77 | -10.00 | -38.92 | 110 |
| 42 | OBV trend · 1h | momentum | 66.78 | -33.22 | 323 | 19.8 | -39.34 | -9.80 | -40.34 | 227 |
| 43 | RSI momentum · 1h | momentum | 65.89 | -34.10 | 200 | 15.0 | -40.09 | -9.12 | -41.87 | 196 |
| 44 | Heikin-Ashi · 1h | trend | 64.88 | -35.12 | 543 | 21.9 | -48.58 | -9.92 | -49.70 | 625 |
| 45 | MACD zero-line · 1h | trend | 64.75 | -35.25 | 199 | 16.6 | -34.06 | -9.19 | -34.71 | 198 |
| 46 | Max aggression: 1-day momentum | meta | 64.40 | -35.60 | 34 | 26.5 | -55.97 | -4.13 | -60.68 | 38 |
| 47 | ROC + volume · 1h | momentum | 63.30 | -36.70 | 456 | 27.0 | -40.86 | -7.94 | -42.67 | 337 |
| 48 | Stochastic reversion · 1h | reversion | 63.03 | -36.97 | 402 | 40.3 | -35.72 | -3.87 | -42.69 | 433 |
| 49 | Donchian 20/10 · 1h | breakout | 62.52 | -37.48 | 181 | 17.7 | -40.61 | -8.97 | -42.28 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 62.17 | -37.83 | 26 | 34.6 | -63.25 | -4.16 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.63 | -39.37 | 310 | 12.3 | -43.41 | -10.02 | -44.98 | 327 |
| 52 | MFI reversion · 1h | reversion | 59.39 | -40.61 | 511 | 31.9 | -33.46 | -4.96 | -35.63 | 185 |
| 53 | MACD cross · 1h | trend | 57.98 | -42.02 | 483 | 20.7 | -53.00 | -10.69 | -53.41 | 501 |
| 54 | Agent (ML meta-label) | meta | 56.83 | -43.16 | 2072 | 25.4 | -25.30 | -3.15 | -35.16 | 324 |
| 55 | CCI reversion · 1h | reversion | 55.85 | -44.15 | 448 | 39.1 | -52.10 | -8.87 | -52.59 | 495 |
| 56 | Bollinger reversion · 1h | reversion | 54.90 | -45.10 | 396 | 37.1 | -40.81 | -4.94 | -45.42 | 428 |
| 57 | VWAP momentum · 1h | momentum | 53.27 | -46.73 | 1081 | 21.5 | -58.48 | -12.94 | -59.90 | 1173 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.87 | -8.49 | -53.20 | 686 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.45 | -9.38 | -56.88 | 593 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -48.81 | -99.18 | 5377 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.88 | -32.43 | -84.15 | 1411 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.50 | -49.31 | -94.50 | 2428 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.99 | -32.47 | -91.00 | 1896 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.91 | -41.42 | -91.91 | 2230 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.33 | -27.34 | -89.42 | 1943 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.22 | -48.74 | -98.23 | 3439 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -53.14 | -96.95 | 3370 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.86 | -34.27 | -92.88 | 2066 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.70 | -35.88 | -82.70 | 1529 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -54.19 | -99.69 | 6293 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.26 | -38.52 | -93.29 | 2492 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.04 | -34.19 | -94.05 | 3138 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -66.14 | -99.82 | 6115 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.24 | -43.91 | -93.26 | 2259 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.76 | -22.18 | -51.89 | 644 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.66 | -23.64 | -78.71 | 1609 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -55.71 | -97.75 | 3271 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -56.16 | -99.20 | 5148 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.32 | -26.97 | -71.42 | 1206 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.93 | -48.44 | -94.93 | 2665 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.85 | -6.54 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.95 | -35.80 | -85.20 | 1654 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -68.12 | -99.77 | 6537 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.66 | -30.98 | -91.68 | 2477 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.60 | -19.64 | -82.86 | 1944 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.97 | -30.81 | -92.10 | 2165 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -46.76 | -98.17 | 4078 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.30 | -46.02 | -90.40 | 2199 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.14 | -29.19 | -68.14 | 788 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.10 | -27.55 | -73.19 | 1153 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.40 | -19.08 | -84.52 | 1816 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -47.41 | -98.10 | 4425 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.61 | -99.94 | 8262 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.61 | -7.28 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T12:00 | MACD cross · 1h | sell | XRP-USD | 4.40 | -0.06 | exit signal |
| 2026-11-25T11:15 | VWAP reversion · 1h | buy | DOGE-USD | 21.46 | — | entry |
| 2026-11-25T11:10 | VWAP reversion · 1h | sell | DOGE-USD | 21.38 | -0.12 | target is flat |
| 2026-11-25T11:05 | VWAP reversion · 1h | buy | DOGE-USD | 21.50 | — | entry |
| 2026-11-25T11:00 | Bollinger reversion · 1h | buy | DOGE-USD | 5.63 | — | entry signal |
| 2026-11-25T11:00 | Bollinger reversion · 1h | sell | SOL-USD | 2.79 | -0.02 | rebalance down |
| 2026-11-25T11:00 | Bollinger reversion · 1h | sell | ETH-USD | 2.78 | -0.02 | rebalance down |
| 2026-11-25T10:30 | Bollinger reversion · 1h | buy | BTC-USD | 2.75 | — | rebalance up |
| 2026-11-25T10:01 | VWAP momentum · 1h | sell | XRP-USD | 6.58 | -0.09 | exit signal |
| 2026-11-25T10:01 | VWAP momentum · 1h | sell | BTC-USD | 6.59 | -0.08 | exit signal |
| 2026-11-25T09:30 | CCI reversion · 1h | sell | DOGE-USD | 3.91 | -0.12 | stop-loss |
| 2026-11-25T09:15 | MFI reversion · 1h | sell | SOL-USD | 3.85 | -0.14 | stop-loss |
| 2026-11-25T09:15 | MFI reversion · 1h | sell | DOGE-USD | 3.88 | -0.10 | stop-loss |
| 2026-11-25T09:15 | CCI reversion · 1h | sell | SOL-USD | 3.20 | -0.10 | stop-loss |
| 2026-11-25T09:15 | Bollinger reversion · 1h | buy | SOL-USD | 5.37 | — | rebalance up |
| 2026-11-25T09:15 | Bollinger reversion · 1h | buy | ETH-USD | 2.77 | — | rebalance up |
| 2026-11-25T09:15 | Bollinger reversion · 1h | sell | DOGE-USD | 10.95 | -0.28 | stop-loss |
| 2026-11-25T09:00 | Agent | buy | ETH-USD | 15.61 | — | following Bollinger reversion · 1h, RSI(14) reversion · 1h |
| 2026-11-25T09:00 | CCI reversion · 1h | buy | BTC-USD | 3.50 | — | entry signal |
| 2026-11-25T09:00 | VWAP reversion · 1h | buy | SOL-USD | 21.53 | — | entry signal |
| 2026-11-25T09:00 | Bollinger reversion · 1h | buy | SOL-USD | 8.48 | — | entry signal |
| 2026-11-25T09:00 | Bollinger reversion · 1h | buy | ETH-USD | 11.08 | — | entry signal |
| 2026-11-25T09:00 | Bollinger reversion · 1h | sell | XRP-USD | 11.16 | -0.05 | exit signal |
| 2026-11-25T09:00 | Bollinger reversion · 1h | sell | DOGE-USD | 2.77 | -0.05 | rebalance down |
| 2026-11-25T09:00 | Bollinger reversion · 1h | sell | BTC-USD | 2.81 | 0.01 | rebalance down |
| 2026-11-25T09:00 | VWAP momentum · 1h | buy | XRP-USD | 6.68 | — | entry signal |
| 2026-11-25T09:00 | VWAP momentum · 1h | buy | BTC-USD | 6.68 | — | entry signal |
| 2026-11-25T08:00 | VWAP momentum · 1h | sell | XRP-USD | 6.62 | -0.07 | exit signal |
| 2026-11-25T08:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.59 | -0.11 | exit signal |
| 2026-11-25T07:45 | MACD cross · 1h | sell | SOL-USD | 2.65 | -0.08 | stop-loss |
| 2026-11-25T07:40 | Agent | sell | ETH-USD | 15.30 | -0.39 | selected signal exited |
| 2026-11-25T07:40 | Stochastic reversion · 1h | sell | BTC-USD | 5.79 | -0.14 | stop-loss |
| 2026-11-25T07:40 | Bollinger reversion · 1h | buy | DOGE-USD | 2.83 | — | rebalance up |
| 2026-11-25T07:40 | Bollinger reversion · 1h | buy | BTC-USD | 13.79 | — | entry |
| 2026-11-25T07:40 | Bollinger reversion · 1h | sell | SOL-USD | 10.92 | -0.36 | stop-loss |
| 2026-11-25T07:40 | Bollinger reversion · 1h | sell | ETH-USD | 8.52 | -0.25 | stop-loss |
| 2026-11-25T07:00 | VWAP reversion · 1h | sell | DOGE-USD | 21.32 | -0.04 | exit signal |
| 2026-11-25T07:00 | VWAP momentum · 1h | buy | XRP-USD | 6.69 | — | entry signal |
| 2026-11-25T07:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.69 | — | entry signal |
| 2026-11-25T05:00 | Stochastic reversion · 1h | buy | DOGE-USD | 5.74 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 12:40:05.000122+00:00 -> 2026-11-25 12:50:05.000122+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
