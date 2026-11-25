# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T14:10:05.000110+00:00 · 73123 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.84 (-22.16%)

Closed trades 245, win rate 35.9%, fees £6.71, max drawdown -22.57%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.40 | -0.21 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 10965 decisions in 2193 calls, $0.1535 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T14:10 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-25T14:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T14:10 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.99 | 15.99 | 0 | — | 13.68 | 4.60 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.09 | 5.09 | 0 | — | 5.25 | 1.42 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | 0.00 | 0.09 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.47 | -3.53 | 229 | 28.4 | -1.63 | -0.48 | -7.61 | 142 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.69 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.37 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.70 | -5.30 | 0 | — | -6.20 | -1.57 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.14 | -5.86 | 20 | 10.0 | -4.59 | -7.39 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.97 | -7.03 | 0 | — | -7.92 | -1.59 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.77 | -7.23 | 61 | 41.0 | -6.79 | -1.22 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.18 | -8.82 | 116 | 24.1 | -8.21 | -4.01 | -11.12 | 40 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.89 | -10.11 | 0 | — | -11.39 | -2.44 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.74 | -11.13 | 24 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.46 | -20.94 | 1 |
| 20 | Daily: Bullish score | daily | 85.45 | -14.55 | 20 | 20.0 | -13.12 | -2.89 | -19.56 | 14 |
| 21 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.24 | -13.73 | 543 |
| 22 | VWAP reversion · 1h | reversion | 84.89 | -15.11 | 172 | 44.8 | -12.62 | -2.32 | -20.49 | 156 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.93 | -7.30 | -20.93 | 74 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.86 | -13.02 | 61 |
| 26 | Parabolic SAR · 1h | trend | 79.20 | -20.80 | 206 | 28.2 | -32.01 | -8.34 | -32.68 | 182 |
| 27 | Volume breakout · 1h | breakout | 78.49 | -21.51 | 169 | 27.8 | -21.84 | -6.53 | -23.69 | 71 |
| 28 | Agent | meta | 77.84 | -22.16 | 245 | 35.9 | -26.54 | -5.99 | -26.78 | 197 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.17 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.16 | -22.84 | 138 | 24.6 | -23.85 | -6.10 | -25.94 | 144 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -21.85 | -6.71 | -22.57 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.46 | -23.54 | 87 | 13.8 | -29.11 | -7.77 | -29.59 | 82 |
| 33 | Ichimoku · 1h | trend | 74.89 | -25.11 | 113 | 15.9 | -29.49 | -7.47 | -31.55 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.80 | -29.20 | 260 | 19.2 | -36.83 | -6.90 | -38.51 | 290 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.76 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.34 | -30.66 | 208 | 22.1 | -30.87 | -7.94 | -33.23 | 205 |
| 37 | Supertrend · 1h | trend | 69.08 | -30.92 | 207 | 18.4 | -36.58 | -7.18 | -37.75 | 208 |
| 38 | Triple EMA stack · 1h | trend | 68.60 | -31.40 | 169 | 15.4 | -38.28 | -9.61 | -39.13 | 169 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 68.23 | -31.77 | 3 | 0.0 | -25.78 | -3.19 | -32.18 | 1 |
| 40 | EMA 20/50 cross · 1h | trend | 67.99 | -32.02 | 124 | 9.7 | -38.15 | -10.15 | -39.24 | 111 |
| 41 | Hold BTC | benchmark | 67.50 | -32.50 | 3 | 0.0 | -30.84 | -5.50 | -36.10 | 1 |
| 42 | OBV trend · 1h | momentum | 66.75 | -33.25 | 323 | 19.8 | -39.38 | -9.81 | -40.38 | 227 |
| 43 | RSI momentum · 1h | momentum | 65.85 | -34.15 | 200 | 15.0 | -40.28 | -9.17 | -42.05 | 197 |
| 44 | Heikin-Ashi · 1h | trend | 64.85 | -35.16 | 543 | 21.9 | -48.55 | -9.91 | -49.70 | 625 |
| 45 | MACD zero-line · 1h | trend | 64.71 | -35.29 | 199 | 16.6 | -34.05 | -9.19 | -34.71 | 198 |
| 46 | Max aggression: 1-day momentum | meta | 64.35 | -35.65 | 34 | 26.5 | -54.78 | -4.00 | -60.68 | 37 |
| 47 | ROC + volume · 1h | momentum | 63.25 | -36.75 | 456 | 27.0 | -40.28 | -7.80 | -42.10 | 335 |
| 48 | Stochastic reversion · 1h | reversion | 62.77 | -37.23 | 404 | 40.1 | -35.95 | -3.90 | -42.69 | 435 |
| 49 | Donchian 20/10 · 1h | breakout | 62.48 | -37.52 | 181 | 17.7 | -40.75 | -8.98 | -42.42 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 62.12 | -37.88 | 26 | 34.6 | -64.06 | -4.26 | -67.33 | 22 |
| 51 | EMA 9/21 cross · 1h | trend | 60.58 | -39.42 | 310 | 12.3 | -43.52 | -10.04 | -45.08 | 327 |
| 52 | MFI reversion · 1h | reversion | 59.39 | -40.61 | 511 | 31.9 | -33.49 | -4.97 | -35.63 | 185 |
| 53 | MACD cross · 1h | trend | 57.94 | -42.06 | 483 | 20.7 | -52.93 | -10.66 | -53.34 | 501 |
| 54 | Agent (ML meta-label) | meta | 56.80 | -43.20 | 2072 | 25.4 | -24.49 | -3.04 | -34.16 | 331 |
| 55 | CCI reversion · 1h | reversion | 55.67 | -44.33 | 450 | 38.9 | -52.21 | -8.90 | -52.58 | 495 |
| 56 | Bollinger reversion · 1h | reversion | 54.38 | -45.62 | 398 | 36.9 | -41.42 | -5.02 | -45.42 | 428 |
| 57 | VWAP momentum · 1h | momentum | 53.24 | -46.76 | 1081 | 21.5 | -58.48 | -12.94 | -59.90 | 1173 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.96 | -8.53 | -53.27 | 684 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.75 | -9.46 | -57.15 | 594 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -48.94 | -99.18 | 5382 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.11 | -33.24 | -84.20 | 1416 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.43 | -48.57 | -94.47 | 2424 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.96 | -32.26 | -90.99 | 1892 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.86 | -41.04 | -91.86 | 2228 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.27 | -27.32 | -89.36 | 1940 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.23 | -48.77 | -98.24 | 3438 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.92 | -52.28 | -96.93 | 3365 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.82 | -34.06 | -92.85 | 2066 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.69 | -35.85 | -82.70 | 1529 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -54.16 | -99.70 | 6301 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.20 | -38.08 | -93.22 | 2488 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.04 | -34.19 | -94.05 | 3138 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -65.12 | -99.82 | 6108 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.29 | -44.18 | -93.31 | 2261 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.76 | -22.18 | -51.89 | 644 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.37 | -23.36 | -78.51 | 1606 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -55.68 | -97.75 | 3269 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -56.38 | -99.20 | 5148 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.41 | -27.11 | -71.51 | 1207 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.83 | -46.96 | -94.86 | 2661 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.85 | -6.54 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.77 | -35.19 | -85.00 | 1648 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -68.44 | -99.77 | 6537 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.73 | -31.12 | -91.73 | 2479 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.75 | -19.75 | -82.97 | 1948 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.97 | -30.83 | -92.08 | 2163 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.16 | -46.90 | -98.19 | 4084 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.32 | -45.69 | -90.42 | 2193 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.78 | -28.58 | -67.96 | 786 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -27.52 | -73.18 | 1153 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.80 | -19.19 | -84.87 | 1824 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.08 | -47.48 | -98.11 | 4426 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -96.69 | -99.94 | 8259 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.61 | -7.28 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T14:00 | Stochastic reversion · 1h | buy | DOGE-USD | 6.28 | — | entry signal |
| 2026-11-25T14:00 | Bollinger reversion · 1h | sell | BTC-USD | 13.50 | -0.26 | stop-loss |
| 2026-11-25T13:55 | CCI reversion · 1h | sell | XRP-USD | 3.64 | -0.11 | stop-loss |
| 2026-11-25T13:55 | VWAP reversion · 1h | sell | DOGE-USD | 20.98 | -0.43 | target is flat |
| 2026-11-25T13:55 | Bollinger reversion · 1h | buy | SOL-USD | 2.75 | — | rebalance up |
| 2026-11-25T13:55 | Bollinger reversion · 1h | sell | DOGE-USD | 5.47 | -0.15 | target is flat |
| 2026-11-25T13:45 | CCI reversion · 1h | sell | BTC-USD | 3.41 | -0.09 | stop-loss |
| 2026-11-25T13:45 | Stochastic reversion · 1h | sell | SOL-USD | 6.85 | -0.23 | stop-loss |
| 2026-11-25T13:20 | Stochastic reversion · 1h | sell | DOGE-USD | 5.60 | -0.14 | stop-loss |
| 2026-11-25T13:00 | CCI reversion · 1h | buy | ETH-USD | 3.72 | — | entry signal |
| 2026-11-25T13:00 | Stochastic reversion · 1h | buy | BTC-USD | 5.73 | — | entry signal |
| 2026-11-25T12:55 | VWAP reversion · 1h | buy | DOGE-USD | 21.40 | — | entry |
| 2026-11-25T12:50 | VWAP reversion · 1h | sell | DOGE-USD | 21.20 | -0.26 | target is flat |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 14:10:05.000110+00:00 -> 2026-11-25 14:20:05.000110+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
