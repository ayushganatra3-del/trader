# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T10:10:05.000137+00:00 · 72915 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.90 (-22.10%)

Closed trades 245, win rate 35.9%, fees £6.71, max drawdown -22.52%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.47 | -0.14 |

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

Today: 7845 decisions in 1569 calls, $0.1099 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T10:10 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-25T10:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T10:10 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.90 | 15.90 | 0 | — | 13.68 | 4.59 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.01 | 5.00 | 0 | — | 5.25 | 1.42 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.40 | -0.04 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.45 | -3.56 | 229 | 28.4 | -1.77 | -0.53 | -7.61 | 142 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.69 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.37 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.62 | -5.38 | 0 | — | -6.20 | -1.57 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.12 | -5.88 | 20 | 10.0 | -4.59 | -7.39 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.90 | -7.11 | 0 | — | -7.92 | -1.59 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.69 | -7.31 | 61 | 41.0 | -6.79 | -1.22 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.16 | -8.84 | 116 | 24.1 | -7.93 | -3.99 | -10.85 | 40 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.82 | -10.18 | 0 | — | -11.39 | -2.44 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.74 | -11.13 | 24 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.46 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 85.90 | -14.10 | 169 | 45.6 | -11.83 | -2.17 | -20.49 | 155 |
| 21 | Daily: Bullish score | daily | 85.43 | -14.57 | 20 | 20.0 | -13.12 | -2.89 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.24 | -13.73 | 543 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.80 | -7.23 | -21.18 | 74 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.40 | -6.12 | -13.56 | 63 |
| 26 | Parabolic SAR · 1h | trend | 79.15 | -20.85 | 206 | 28.2 | -31.91 | -8.32 | -32.66 | 182 |
| 27 | Volume breakout · 1h | breakout | 78.48 | -21.52 | 169 | 27.8 | -21.81 | -6.52 | -23.66 | 71 |
| 28 | Agent | meta | 77.90 | -22.10 | 245 | 35.9 | -26.47 | -5.97 | -26.72 | 197 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.17 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.13 | -22.87 | 138 | 24.6 | -24.69 | -6.33 | -27.01 | 148 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -22.28 | -6.84 | -22.99 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.45 | -23.55 | 87 | 13.8 | -29.08 | -7.76 | -29.57 | 82 |
| 33 | Ichimoku · 1h | trend | 74.88 | -25.12 | 113 | 15.9 | -29.47 | -7.46 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.75 | -29.25 | 260 | 19.2 | -37.21 | -7.00 | -38.51 | 292 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.76 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.33 | -30.67 | 208 | 22.1 | -30.94 | -7.98 | -33.57 | 207 |
| 37 | Supertrend · 1h | trend | 69.03 | -30.97 | 207 | 18.4 | -36.58 | -7.18 | -37.75 | 208 |
| 38 | Triple EMA stack · 1h | trend | 68.57 | -31.43 | 169 | 15.4 | -38.60 | -9.86 | -38.98 | 171 |
| 39 | Hold BTC | benchmark | 68.38 | -31.62 | 3 | 0.0 | -29.61 | -5.26 | -36.10 | 1 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.17 | -31.83 | 3 | 0.0 | -25.78 | -3.19 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.94 | -32.06 | 124 | 9.7 | -37.77 | -10.00 | -38.92 | 110 |
| 42 | OBV trend · 1h | momentum | 66.72 | -33.28 | 323 | 19.8 | -39.27 | -9.77 | -40.28 | 227 |
| 43 | RSI momentum · 1h | momentum | 65.81 | -34.19 | 200 | 15.0 | -40.21 | -9.15 | -41.99 | 196 |
| 44 | Heikin-Ashi · 1h | trend | 64.81 | -35.20 | 543 | 21.9 | -48.58 | -9.92 | -49.70 | 625 |
| 45 | MACD zero-line · 1h | trend | 64.67 | -35.33 | 199 | 16.6 | -34.02 | -9.18 | -34.56 | 197 |
| 46 | Max aggression: 1-day momentum | meta | 64.29 | -35.71 | 34 | 26.5 | -55.96 | -4.13 | -60.67 | 38 |
| 47 | ROC + volume · 1h | momentum | 63.20 | -36.80 | 456 | 27.0 | -40.91 | -7.96 | -42.67 | 336 |
| 48 | Stochastic reversion · 1h | reversion | 62.96 | -37.04 | 402 | 40.3 | -35.69 | -3.87 | -42.69 | 433 |
| 49 | Donchian 20/10 · 1h | breakout | 62.44 | -37.55 | 181 | 17.7 | -40.61 | -8.97 | -42.29 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 62.07 | -37.93 | 26 | 34.6 | -63.25 | -4.16 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.53 | -39.47 | 310 | 12.3 | -43.41 | -10.02 | -44.98 | 327 |
| 52 | MFI reversion · 1h | reversion | 59.39 | -40.61 | 511 | 31.9 | -33.23 | -4.93 | -35.63 | 186 |
| 53 | MACD cross · 1h | trend | 57.95 | -42.05 | 482 | 20.7 | -53.02 | -10.69 | -53.47 | 501 |
| 54 | Agent (ML meta-label) | meta | 56.77 | -43.23 | 2072 | 25.4 | -23.41 | -2.95 | -31.64 | 319 |
| 55 | CCI reversion · 1h | reversion | 55.82 | -44.18 | 448 | 39.1 | -52.09 | -8.87 | -52.62 | 495 |
| 56 | Bollinger reversion · 1h | reversion | 54.93 | -45.07 | 396 | 37.1 | -40.62 | -4.92 | -45.42 | 427 |
| 57 | VWAP momentum · 1h | momentum | 53.21 | -46.79 | 1081 | 21.5 | -58.81 | -13.15 | -59.93 | 1178 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.13 | -8.55 | -53.19 | 691 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.39 | -9.37 | -56.81 | 593 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -48.06 | -99.17 | 5372 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.87 | -32.43 | -84.14 | 1410 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.54 | -49.59 | -94.54 | 2431 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.97 | -32.43 | -90.99 | 1896 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.88 | -41.27 | -91.91 | 2232 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.33 | -27.34 | -89.42 | 1943 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -48.04 | -98.22 | 3436 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.94 | -52.49 | -96.97 | 3377 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.83 | -34.30 | -92.85 | 2061 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.83 | -36.24 | -82.88 | 1534 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -54.20 | -99.69 | 6294 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.18 | -37.40 | -93.28 | 2493 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.08 | -34.29 | -94.09 | 3142 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -65.01 | -99.82 | 6109 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.21 | -43.72 | -93.23 | 2257 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.87 | -22.21 | -52.00 | 646 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.61 | -23.56 | -78.83 | 1612 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -56.06 | -97.76 | 3276 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -55.87 | -99.19 | 5146 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.36 | -27.05 | -71.85 | 1211 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.87 | -47.70 | -94.91 | 2669 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.85 | -6.54 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.88 | -35.59 | -85.23 | 1655 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -68.24 | -99.77 | 6538 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.62 | -30.87 | -91.63 | 2474 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.54 | -19.59 | -82.85 | 1943 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.97 | -31.11 | -92.10 | 2162 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -46.69 | -98.16 | 4074 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.29 | -45.92 | -90.40 | 2201 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.08 | -29.09 | -68.25 | 791 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.41 | -27.82 | -73.42 | 1155 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.20 | -19.00 | -84.31 | 1812 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -47.13 | -98.09 | 4424 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.99 | -99.94 | 8259 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.62 | -7.28 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-25T03:00 | MACD cross · 1h | buy | XRP-USD | 4.45 | — | entry signal |
| 2026-11-25T02:10 | CCI reversion · 1h | sell | ETH-USD | 2.43 | -0.10 | stop-loss |
| 2026-11-25T02:05 | MFI reversion · 1h | sell | BTC-USD | 3.91 | -0.07 | stop-loss |
| 2026-11-25T02:00 | MACD cross · 1h | sell | ETH-USD | 4.38 | -0.10 | exit signal |
| 2026-11-25T02:00 | MACD cross · 1h | sell | DOGE-USD | 3.57 | -0.06 | exit signal |
| 2026-11-25T02:00 | MACD cross · 1h | sell | BTC-USD | 4.39 | -0.08 | exit signal |
| 2026-11-25T01:50 | CCI reversion · 1h | sell | BTC-USD | 2.90 | -0.07 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 10:10:05.000137+00:00 -> 2026-11-25 10:20:05.000137+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
