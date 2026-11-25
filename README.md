# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T14:40:05.000140+00:00 · 73147 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.72 (-22.28%)

Closed trades 245, win rate 35.9%, fees £6.71, max drawdown -22.65%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.29 | -0.32 |

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

Today: 11931 decisions in 2265 calls, $0.1654 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T14:40 | 0 / 7 / 23 | cash |  |
| Breezy | 2026-11-25T14:40 | 0 / 22 / 8 | cash |  |
| Boozy | 2026-11-25T14:40 | 4 / 21 / 5 | MSTR 50% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.06 | 16.06 | 0 | — | 13.68 | 4.59 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.87 | 1.43 | -9.74 | 33 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.20 | 4.20 | 42 | 28.6 | 1.19 | 0.36 | -12.43 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.73 | 3.73 | 0 | — | 3.77 | 1.05 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.49 | -1.51 | 219 | 31.5 | -0.41 | -0.04 | -8.58 | 211 |
| 9 | Agent (rotation) | meta | 96.13 | -3.87 | 230 | 28.7 | -1.63 | -0.48 | -7.61 | 156 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.78 | -4.22 | 170 | 32.9 | -4.22 | -3.76 | -4.79 | 54 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.24 | -2.53 | -7.38 | 1 |
| 12 | Trend pullback · 1h | trend | 94.05 | -5.95 | 116 | 24.1 | -4.81 | -1.90 | -10.65 | 38 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 93.03 | -6.97 | 0 | — | -7.92 | -1.59 | -13.87 | 1 |
| 14 | Copy: Insider buying | copy | 92.82 | -7.18 | 61 | 41.0 | -6.87 | -1.24 | -14.79 | 72 |
| 15 | Three white soldiers · 1h | momentum | 92.57 | -7.43 | 21 | 9.5 | -6.18 | -6.94 | -6.29 | 19 |
| 16 | Hold SPY | benchmark | 92.11 | -7.89 | 0 | — | -8.60 | -2.14 | -11.71 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.94 | -10.05 | 0 | — | -11.39 | -2.44 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.74 | -11.13 | 24 |
| 19 | Daily: Bullish score | daily | 88.18 | -11.82 | 20 | 20.0 | -10.78 | -2.21 | -19.56 | 14 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.95 | -2.62 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.66 | -4.23 | -13.37 | 525 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.84 | -2.36 | -20.49 | 156 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -19.08 | -6.81 | -19.08 | 74 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.86 | -5.86 | -13.02 | 61 |
| 26 | Agent | meta | 77.72 | -22.28 | 245 | 35.9 | -26.67 | -6.02 | -26.87 | 197 |
| 27 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.17 | -18.44 | 88 |
| 28 | Parabolic SAR · 1h | trend | 76.91 | -23.09 | 207 | 28.0 | -34.73 | -8.85 | -34.73 | 181 |
| 29 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -22.39 | -6.88 | -22.87 | 651 |
| 30 | Volume breakout · 1h | breakout | 76.65 | -23.35 | 169 | 27.8 | -22.77 | -9.19 | -22.87 | 70 |
| 31 | Keltner breakout · 1h | breakout | 74.90 | -25.10 | 140 | 25.0 | -26.82 | -6.75 | -27.02 | 146 |
| 32 | Donchian 55/20 · 1h | breakout | 74.76 | -25.24 | 87 | 13.8 | -30.71 | -8.19 | -30.71 | 82 |
| 33 | Ichimoku · 1h | trend | 73.17 | -26.83 | 113 | 15.9 | -31.07 | -7.87 | -31.55 | 102 |
| 34 | Daily: Momentum burst | daily | 69.58 | -30.42 | 31 | 16.1 | -34.90 | -4.90 | -36.38 | 25 |
| 35 | ADX DI cross · 1h | trend | 69.20 | -30.80 | 261 | 19.2 | -39.97 | -7.58 | -40.57 | 274 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 68.27 | -31.73 | 3 | 0.0 | -25.78 | -3.19 | -32.18 | 1 |
| 37 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -32.56 | -8.45 | -33.76 | 206 |
| 38 | Max aggression: 5-day momentum | meta | 68.08 | -31.92 | 27 | 37.0 | -60.63 | -3.71 | -67.33 | 23 |
| 39 | EMA 20/50 cross · 1h | trend | 67.74 | -32.26 | 126 | 9.5 | -36.61 | -10.16 | -37.43 | 110 |
| 40 | OBV trend · 1h | momentum | 67.18 | -32.82 | 324 | 19.8 | -39.21 | -9.59 | -40.74 | 229 |
| 41 | Hold BTC | benchmark | 67.04 | -32.96 | 3 | 0.0 | -31.77 | -5.67 | -36.10 | 1 |
| 42 | Triple EMA stack · 1h | trend | 66.54 | -33.46 | 171 | 15.2 | -39.55 | -9.92 | -40.01 | 153 |
| 43 | Supertrend · 1h | trend | 65.95 | -34.05 | 207 | 18.4 | -38.67 | -7.18 | -38.75 | 211 |
| 44 | MACD zero-line · 1h | trend | 63.33 | -36.67 | 201 | 16.4 | -34.81 | -9.45 | -34.97 | 198 |
| 45 | RSI momentum · 1h | momentum | 62.67 | -37.33 | 201 | 14.9 | -43.79 | -9.83 | -43.79 | 194 |
| 46 | Heikin-Ashi · 1h | trend | 62.25 | -37.75 | 545 | 21.8 | -49.58 | -10.20 | -50.19 | 624 |
| 47 | Stochastic reversion · 1h | reversion | 61.39 | -38.61 | 408 | 39.7 | -38.89 | -4.25 | -42.70 | 436 |
| 48 | ROC + volume · 1h | momentum | 60.51 | -39.49 | 460 | 27.0 | -41.94 | -8.23 | -42.26 | 333 |
| 49 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -57.66 | -4.33 | -60.67 | 38 |
| 50 | Donchian 20/10 · 1h | breakout | 59.90 | -40.10 | 183 | 17.5 | -43.20 | -9.47 | -43.63 | 194 |
| 51 | MFI reversion · 1h | reversion | 59.26 | -40.74 | 511 | 31.9 | -36.20 | -5.32 | -37.70 | 187 |
| 52 | EMA 9/21 cross · 1h | trend | 57.39 | -42.61 | 313 | 12.1 | -47.20 | -10.72 | -47.20 | 325 |
| 53 | Agent (ML meta-label) | meta | 56.85 | -43.15 | 2073 | 25.4 | -17.78 | -2.17 | -26.44 | 319 |
| 54 | MACD cross · 1h | trend | 55.56 | -44.44 | 489 | 20.4 | -55.00 | -10.86 | -55.00 | 503 |
| 55 | CCI reversion · 1h | reversion | 52.87 | -47.13 | 460 | 38.0 | -55.27 | -9.23 | -55.29 | 496 |
| 56 | Bollinger reversion · 1h | reversion | 52.83 | -47.17 | 400 | 36.8 | -43.16 | -5.21 | -45.42 | 428 |
| 57 | VWAP momentum · 1h | momentum | 51.22 | -48.78 | 1083 | 21.4 | -60.84 | -13.17 | -61.70 | 1174 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -58.34 | -9.25 | -58.37 | 665 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -58.22 | -9.59 | -58.85 | 593 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -48.96 | -99.18 | 5388 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.25 | -33.68 | -84.27 | 1417 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.46 | -48.96 | -94.47 | 2422 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.03 | -32.53 | -91.03 | 1887 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.77 | -41.02 | -91.77 | 2217 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.19 | -27.21 | -89.28 | 1937 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.24 | -48.92 | -98.24 | 3419 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.91 | -52.32 | -96.92 | 3359 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.77 | -33.82 | -92.80 | 2031 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.69 | -35.83 | -82.69 | 1524 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -54.72 | -99.70 | 6301 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.24 | -37.90 | -93.26 | 2489 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.06 | -34.25 | -94.06 | 3135 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -65.63 | -99.82 | 6109 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.27 | -43.91 | -93.28 | 2249 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.76 | -22.11 | -51.87 | 645 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.39 | -23.66 | -78.47 | 1611 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -55.19 | -97.75 | 3244 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -59.23 | -99.21 | 5138 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.16 | -26.44 | -71.51 | 1200 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.84 | -47.11 | -94.87 | 2659 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -50.49 | -7.03 | -50.96 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.78 | -35.13 | -85.02 | 1650 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -69.26 | -99.77 | 6530 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.89 | -31.23 | -91.89 | 2484 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.92 | -19.89 | -83.10 | 1960 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.10 | -32.91 | -92.20 | 2159 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -48.14 | -98.21 | 4079 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.33 | -45.73 | -90.39 | 2182 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.55 | -28.33 | -67.87 | 786 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.21 | -27.44 | -73.22 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.72 | -18.98 | -84.93 | 1832 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -48.40 | -98.12 | 4410 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -96.77 | -99.94 | 8251 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -52.28 | -8.24 | -53.12 | 280 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T14:40 | Agent (rotation) | buy | SQQQ | 8.01 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 23.95 | — | entry |
| 2026-11-25T14:40 | Stochastic reversion · 1h | buy | SQQQ | 4.25 | — | rebalance up |
| 2026-11-25T14:40 | Stochastic reversion · 1h | buy | ETHU | 5.05 | — | rebalance up |
| 2026-11-25T14:40 | Stochastic reversion · 1h | sell | AMZN | 10.16 | -0.37 | stop-loss |
| 2026-11-25T14:40 | OBV trend · 1h | sell | LABU | 15.32 | -1.30 | stop-loss |
| 2026-11-25T14:40 | ROC + volume · 1h | sell | LABU | 14.48 | -0.33 | stop-loss |
| 2026-11-25T14:40 | ROC + volume · 1h | sell | AAPL | 15.63 | -0.05 | target is flat |
| 2026-11-25T14:40 | EMA 20/50 cross · 1h | sell | LABU | 15.59 | -1.32 | stop-loss |
| 2026-11-25T14:40 | Gap and go | buy | SQQQ | 24.63 | — | entry signal |
| 2026-11-25T14:35 | Max aggression: 5-day momentum | buy | LABU | 69.75 | — | entry |
| 2026-11-25T14:35 | Max aggression: 5-day momentum | sell | SQQQ | 69.75 | 8.02 | target is flat |
| 2026-11-25T14:35 | Max aggression: 1-day momentum | sell | LABU | 60.11 | 0.95 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T14:35 | Agent (rotation) | sell | AAPL | 32.33 | 0.33 | selected signal exited |
| 2026-11-25T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 103.91 | — | entry |
| 2026-11-25T14:35 | Agent (ML meta-label) | sell | MSTR | 13.24 | -1.16 | selected signal exited |
| 2026-11-25T14:35 | Daily: Momentum burst | buy | LABU | 17.50 | — | entry |
| 2026-11-25T14:35 | Copy: Insider buying | buy | PLTR | 1.08 | — | entry |
| 2026-11-25T14:35 | MFI reversion · 1h | buy | TNA | 14.85 | — | entry |
| 2026-11-25T14:35 | MFI reversion · 1h | buy | IWM | 14.85 | — | entry |
| 2026-11-25T14:35 | MFI reversion · 1h | buy | ETHU | 14.85 | — | entry |
| 2026-11-25T14:35 | CCI reversion · 1h | buy | PLTR | 10.66 | — | rebalance up |
| 2026-11-25T14:35 | CCI reversion · 1h | buy | META | 10.64 | — | rebalance up |
| 2026-11-25T14:35 | CCI reversion · 1h | buy | ETH-USD | 9.58 | — | rebalance up |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | UPRO | 2.39 | -0.29 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | TSLA | 2.48 | -0.20 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | SPY | 2.58 | -0.10 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | SOXL | 3.30 | -1.03 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | MSTR | 3.70 | -0.32 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | MSFT | 2.57 | -0.11 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | GOOGL | 2.50 | -0.18 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | COIN | 3.79 | -0.24 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | AMZN | 2.52 | -0.17 | stop-loss |
| 2026-11-25T14:35 | CCI reversion · 1h | sell | AMD | 3.16 | -0.36 | stop-loss |
| 2026-11-25T14:35 | Stochastic reversion · 1h | buy | MSFT | 5.30 | — | rebalance up |
| 2026-11-25T14:35 | Stochastic reversion · 1h | buy | DOGE-USD | 4.04 | — | rebalance up |
| 2026-11-25T14:35 | Stochastic reversion · 1h | buy | BTC-USD | 4.63 | — | rebalance up |
| 2026-11-25T14:35 | Stochastic reversion · 1h | buy | AMZN | 5.37 | — | rebalance up |
| 2026-11-25T14:35 | Stochastic reversion · 1h | sell | MSTR | 7.13 | -1.50 | stop-loss |
| 2026-11-25T14:35 | Stochastic reversion · 1h | sell | COIN | 3.88 | -0.24 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 14:40:05.000140+00:00 -> 2026-11-25 14:50:05.000140+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
