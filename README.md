# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T11:40:05.000149+00:00 · 72997 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.89 (-22.11%)

Closed trades 245, win rate 35.9%, fees £6.71, max drawdown -22.52%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.45 | -0.16 |

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

Today: 9075 decisions in 1815 calls, $0.1271 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T11:40 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-11-25T11:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T11:40 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.00 | 16.00 | 0 | — | 13.68 | 4.59 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.10 | 5.10 | 0 | — | 5.25 | 1.42 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.40 | -0.04 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.47 | -3.53 | 229 | 28.4 | -1.77 | -0.53 | -7.61 | 142 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.69 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.37 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.70 | -5.29 | 0 | — | -6.20 | -1.57 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.14 | -5.86 | 20 | 10.0 | -4.59 | -7.39 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.98 | -7.02 | 0 | — | -7.92 | -1.59 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.77 | -7.23 | 61 | 41.0 | -6.79 | -1.22 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.18 | -8.82 | 116 | 24.1 | -7.93 | -3.99 | -10.85 | 40 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.89 | -10.11 | 0 | — | -11.39 | -2.44 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.74 | -11.13 | 24 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.46 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 85.59 | -14.40 | 170 | 45.3 | -12.05 | -2.21 | -20.49 | 156 |
| 21 | Daily: Bullish score | daily | 85.45 | -14.55 | 20 | 20.0 | -13.12 | -2.89 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.24 | -13.73 | 543 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -19.98 | -6.93 | -20.01 | 72 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.92 | -5.89 | -13.09 | 62 |
| 26 | Parabolic SAR · 1h | trend | 79.20 | -20.80 | 206 | 28.2 | -32.15 | -8.37 | -32.89 | 183 |
| 27 | Volume breakout · 1h | breakout | 78.49 | -21.50 | 169 | 27.8 | -22.17 | -6.60 | -24.01 | 71 |
| 28 | Agent | meta | 77.89 | -22.11 | 245 | 35.9 | -26.50 | -5.98 | -26.72 | 197 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.17 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.16 | -22.84 | 138 | 24.6 | -24.61 | -6.31 | -27.07 | 149 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -22.28 | -6.84 | -22.99 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.46 | -23.54 | 87 | 13.8 | -29.08 | -7.76 | -29.57 | 82 |
| 33 | Ichimoku · 1h | trend | 74.89 | -25.11 | 113 | 15.9 | -29.47 | -7.46 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.81 | -29.19 | 260 | 19.2 | -37.21 | -7.00 | -38.51 | 292 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.76 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.34 | -30.66 | 208 | 22.1 | -30.94 | -7.98 | -33.57 | 207 |
| 37 | Supertrend · 1h | trend | 69.08 | -30.92 | 207 | 18.4 | -36.58 | -7.18 | -37.75 | 208 |
| 38 | Triple EMA stack · 1h | trend | 68.60 | -31.40 | 169 | 15.4 | -38.47 | -9.82 | -38.85 | 171 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 68.23 | -31.77 | 3 | 0.0 | -25.78 | -3.19 | -32.18 | 1 |
| 40 | EMA 20/50 cross · 1h | trend | 67.99 | -32.01 | 124 | 9.7 | -37.77 | -10.00 | -38.92 | 110 |
| 41 | Hold BTC | benchmark | 67.86 | -32.14 | 3 | 0.0 | -30.14 | -5.35 | -36.10 | 1 |
| 42 | OBV trend · 1h | momentum | 66.75 | -33.25 | 323 | 19.8 | -39.34 | -9.80 | -40.34 | 227 |
| 43 | RSI momentum · 1h | momentum | 65.86 | -34.14 | 200 | 15.0 | -39.71 | -9.00 | -41.87 | 195 |
| 44 | Heikin-Ashi · 1h | trend | 64.85 | -35.15 | 543 | 21.9 | -48.58 | -9.92 | -49.70 | 625 |
| 45 | MACD zero-line · 1h | trend | 64.71 | -35.28 | 199 | 16.6 | -34.02 | -9.18 | -34.56 | 197 |
| 46 | Max aggression: 1-day momentum | meta | 64.35 | -35.65 | 34 | 26.5 | -55.96 | -4.13 | -60.67 | 38 |
| 47 | ROC + volume · 1h | momentum | 63.25 | -36.74 | 456 | 27.0 | -41.24 | -8.02 | -42.99 | 337 |
| 48 | Stochastic reversion · 1h | reversion | 62.97 | -37.03 | 402 | 40.3 | -35.63 | -3.86 | -42.69 | 434 |
| 49 | Donchian 20/10 · 1h | breakout | 62.49 | -37.51 | 181 | 17.7 | -40.59 | -8.97 | -42.26 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 62.12 | -37.88 | 26 | 34.6 | -63.25 | -4.16 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.58 | -39.42 | 310 | 12.3 | -43.30 | -9.98 | -44.87 | 326 |
| 52 | MFI reversion · 1h | reversion | 59.39 | -40.61 | 511 | 31.9 | -33.19 | -4.93 | -35.63 | 186 |
| 53 | MACD cross · 1h | trend | 57.95 | -42.05 | 482 | 20.7 | -52.99 | -10.68 | -53.41 | 501 |
| 54 | Agent (ML meta-label) | meta | 56.80 | -43.20 | 2072 | 25.4 | -22.76 | -2.71 | -31.99 | 322 |
| 55 | CCI reversion · 1h | reversion | 55.79 | -44.21 | 448 | 39.1 | -52.12 | -8.88 | -52.59 | 495 |
| 56 | Bollinger reversion · 1h | reversion | 54.77 | -45.23 | 396 | 37.1 | -40.89 | -4.95 | -45.42 | 428 |
| 57 | VWAP momentum · 1h | momentum | 53.25 | -46.75 | 1081 | 21.5 | -58.82 | -13.15 | -59.93 | 1177 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.97 | -8.50 | -53.26 | 688 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.49 | -9.39 | -56.86 | 593 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -47.67 | -99.18 | 5369 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.87 | -32.43 | -84.14 | 1410 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.46 | -48.90 | -94.50 | 2429 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.99 | -32.47 | -91.00 | 1896 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.89 | -41.34 | -91.92 | 2231 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.33 | -27.34 | -89.42 | 1943 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.22 | -48.62 | -98.22 | 3437 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -52.71 | -96.96 | 3375 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.84 | -34.40 | -92.87 | 2062 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.78 | -36.12 | -82.79 | 1532 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -54.01 | -99.69 | 6299 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.18 | -37.44 | -93.28 | 2491 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.04 | -34.19 | -94.05 | 3138 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -65.57 | -99.82 | 6108 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.23 | -43.84 | -93.25 | 2258 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.92 | -22.26 | -52.05 | 646 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.69 | -23.63 | -78.83 | 1612 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -55.61 | -97.75 | 3270 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -55.79 | -99.19 | 5143 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.32 | -26.97 | -71.42 | 1206 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.92 | -48.32 | -94.92 | 2666 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.85 | -6.54 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.99 | -35.90 | -85.27 | 1656 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -68.15 | -99.77 | 6537 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.64 | -30.91 | -91.64 | 2474 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.56 | -19.61 | -82.86 | 1942 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.99 | -31.12 | -92.12 | 2160 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -46.56 | -98.16 | 4073 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.33 | -46.29 | -90.40 | 2200 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.12 | -29.10 | -68.26 | 791 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.41 | -27.82 | -73.42 | 1155 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.32 | -19.08 | -84.40 | 1815 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -47.40 | -98.10 | 4424 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.99 | -99.94 | 8257 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.62 | -7.28 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-25T04:00 | VWAP reversion · 1h | sell | SOL-USD | 21.33 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 11:40:05.000149+00:00 -> 2026-11-25 11:50:05.000149+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
