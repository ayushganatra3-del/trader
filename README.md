# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T00:10:05.000132+00:00 · 72401 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.35 (-21.66%)

Closed trades 244, win rate 36.1%, fees £6.61, max drawdown -22.02%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.59 | -0.09 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 135 decisions in 27 calls, $0.0019 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T00:10 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-25T00:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T00:10 | 0 / 5 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.62 | 15.62 | 0 | — | 13.68 | 4.60 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.75 | 4.75 | 0 | — | 5.25 | 1.42 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | 0.00 | 0.09 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.37 | -3.63 | 229 | 28.4 | -1.63 | -0.48 | -7.61 | 142 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.69 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.37 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.40 | -5.60 | 0 | — | -6.20 | -1.57 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.06 | -5.94 | 20 | 10.0 | -4.59 | -7.39 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.67 | -7.33 | 0 | — | -7.92 | -1.59 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.47 | -7.53 | 61 | 41.0 | -6.79 | -1.22 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.10 | -8.90 | 116 | 24.1 | -8.02 | -4.00 | -10.94 | 40 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.60 | -10.40 | 0 | — | -11.39 | -2.44 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.74 | -11.13 | 24 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.46 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.40 | -13.60 | 167 | 46.1 | -11.27 | -2.05 | -20.49 | 154 |
| 21 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.24 | -13.73 | 543 |
| 22 | Daily: Bullish score | daily | 85.38 | -14.62 | 20 | 20.0 | -13.12 | -2.89 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.88 | -7.27 | -21.10 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.53 | -6.40 | -14.68 | 65 |
| 26 | Parabolic SAR · 1h | trend | 79.01 | -20.99 | 206 | 28.2 | -31.98 | -8.33 | -32.65 | 184 |
| 27 | Volume breakout · 1h | breakout | 78.43 | -21.57 | 169 | 27.8 | -21.81 | -6.52 | -23.66 | 71 |
| 28 | Agent | meta | 78.35 | -21.66 | 244 | 36.1 | -26.03 | -5.85 | -26.43 | 196 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.17 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.03 | -22.97 | 138 | 24.6 | -24.63 | -6.31 | -26.91 | 148 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -21.85 | -6.71 | -22.57 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.40 | -23.60 | 87 | 13.8 | -29.20 | -7.75 | -29.68 | 82 |
| 33 | Ichimoku · 1h | trend | 74.83 | -25.17 | 113 | 15.9 | -29.47 | -7.46 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.59 | -29.41 | 260 | 19.2 | -36.86 | -6.91 | -38.49 | 290 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.76 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.28 | -30.72 | 208 | 22.1 | -30.94 | -7.98 | -33.57 | 207 |
| 37 | Hold BTC | benchmark | 68.91 | -31.09 | 3 | 0.0 | -29.51 | -5.26 | -36.10 | 1 |
| 38 | Supertrend · 1h | trend | 68.91 | -31.09 | 207 | 18.4 | -36.58 | -7.18 | -37.75 | 208 |
| 39 | Triple EMA stack · 1h | trend | 68.49 | -31.51 | 169 | 15.4 | -38.93 | -9.85 | -39.43 | 172 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.01 | -31.99 | 3 | 0.0 | -25.78 | -3.19 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.82 | -32.18 | 124 | 9.7 | -37.95 | -10.06 | -39.04 | 111 |
| 42 | OBV trend · 1h | momentum | 66.65 | -33.35 | 323 | 19.8 | -39.77 | -9.94 | -40.76 | 228 |
| 43 | RSI momentum · 1h | momentum | 65.70 | -34.30 | 200 | 15.0 | -40.19 | -9.15 | -41.97 | 196 |
| 44 | Heikin-Ashi · 1h | trend | 64.73 | -35.27 | 542 | 22.0 | -48.13 | -9.71 | -49.69 | 629 |
| 45 | MACD zero-line · 1h | trend | 64.56 | -35.44 | 199 | 16.6 | -34.06 | -9.19 | -34.72 | 198 |
| 46 | Max aggression: 1-day momentum | meta | 64.14 | -35.86 | 34 | 26.5 | -55.97 | -4.13 | -60.68 | 38 |
| 47 | Stochastic reversion · 1h | reversion | 63.29 | -36.71 | 400 | 40.5 | -35.21 | -3.79 | -42.69 | 433 |
| 48 | ROC + volume · 1h | momentum | 63.05 | -36.95 | 456 | 27.0 | -41.23 | -8.07 | -42.61 | 340 |
| 49 | Donchian 20/10 · 1h | breakout | 62.33 | -37.67 | 181 | 17.7 | -40.71 | -8.97 | -42.38 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 61.92 | -38.08 | 26 | 34.6 | -63.25 | -4.16 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.38 | -39.62 | 310 | 12.3 | -43.92 | -10.20 | -45.77 | 330 |
| 52 | MFI reversion · 1h | reversion | 59.68 | -40.32 | 507 | 32.1 | -33.04 | -4.88 | -35.63 | 186 |
| 53 | MACD cross · 1h | trend | 58.07 | -41.93 | 478 | 20.9 | -53.09 | -10.71 | -53.99 | 503 |
| 54 | Agent (ML meta-label) | meta | 56.66 | -43.34 | 2072 | 25.4 | -22.93 | -2.98 | -31.57 | 318 |
| 55 | CCI reversion · 1h | reversion | 56.04 | -43.96 | 444 | 39.4 | -51.76 | -8.77 | -52.62 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 55.74 | -44.26 | 392 | 37.5 | -39.49 | -4.73 | -45.42 | 424 |
| 57 | VWAP momentum · 1h | momentum | 53.48 | -46.52 | 1077 | 21.5 | -58.13 | -12.79 | -59.89 | 1176 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.90 | -8.50 | -53.33 | 690 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.90 | -9.22 | -56.43 | 591 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -46.92 | -99.14 | 5373 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.83 | -32.49 | -83.87 | 1417 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.48 | -48.14 | -94.49 | 2436 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.78 | -31.43 | -90.78 | 1903 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.79 | -40.19 | -91.81 | 2237 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.76 | -28.30 | -89.80 | 1964 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -46.97 | -98.19 | 3443 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -52.10 | -96.96 | 3377 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.98 | -34.44 | -93.00 | 2076 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.01 | -35.61 | -83.03 | 1540 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -53.21 | -99.67 | 6270 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.22 | -37.83 | -93.22 | 2499 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.35 | -35.51 | -94.35 | 3170 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -61.74 | -99.82 | 6103 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.23 | -42.72 | -93.23 | 2264 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.63 | -22.03 | -51.68 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.61 | -23.48 | -78.61 | 1619 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -54.71 | -97.74 | 3278 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -55.98 | -99.17 | 5143 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.34 | -27.10 | -71.51 | 1211 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.86 | -46.59 | -94.86 | 2673 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.75 | -6.52 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.09 | -35.75 | -85.29 | 1661 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -67.92 | -99.77 | 6541 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.49 | -30.37 | -91.65 | 2464 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.91 | -20.04 | -83.27 | 1950 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.72 | -30.21 | -91.86 | 2171 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.16 | -47.12 | -98.16 | 4072 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.26 | -45.28 | -90.29 | 2198 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.59 | -29.07 | -68.59 | 795 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.26 | -27.80 | -73.36 | 1162 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.21 | -19.02 | -84.48 | 1811 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.05 | -47.94 | -98.05 | 4427 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -87.36 | -99.94 | 8261 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.59 | -7.28 | -50.46 | 307 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T00:05 | Agent | buy | ETH-USD | 15.69 | — | following Bollinger reversion · 1h, RSI(14) reversion · 1h |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | SOL-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | ETH-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | DOGE-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | BTC-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | Heikin-Ashi · 1h | buy | SOL-USD | 16.13 | — | entry signal |
| 2026-11-25T00:00 | MACD cross · 1h | buy | SOL-USD | 2.73 | — | entry signal |
| 2026-11-25T00:00 | MACD cross · 1h | buy | DOGE-USD | 3.63 | — | entry signal |
| 2026-11-24T23:00 | MACD cross · 1h | buy | ETH-USD | 4.47 | — | entry signal |
| 2026-11-24T23:00 | MACD cross · 1h | buy | BTC-USD | 4.47 | — | entry signal |
| 2026-11-24T21:01 | CCI reversion · 1h | buy | SOL-USD | 3.30 | — | entry signal |
| 2026-11-24T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 89.28 | -1.31 | target is flat |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | SQQQ | 6.12 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | MSTR | 6.11 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | ETHU | 6.07 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | TECL | 8.15 | 0.04 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | MSFT | 8.12 | 0.00 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | COIN | 8.10 | -0.00 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | AMD | 8.12 | 0.01 | selected signal exited |
| 2026-11-24T20:55 | Opening range 30m | sell | TNA | 21.26 | -0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | MSFT | 21.14 | -0.08 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | LABU | 17.71 | 0.90 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | IWM | 21.31 | -0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | UPRO | 10.19 | -0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | TNA | 11.66 | 0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | SPY | 10.92 | -0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | MSFT | 10.82 | 0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | LABU | 11.29 | 0.57 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | IWM | 10.93 | -0.00 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | AAPL | 10.89 | 0.00 | end-of-day flatten |
| 2026-11-24T20:50 | Agent (ML meta-label) | buy | TECL | 8.11 | — | entry |
| 2026-11-24T20:50 | Agent (ML meta-label) | buy | MSFT | 8.12 | — | entry |
| 2026-11-24T20:50 | Agent (ML meta-label) | buy | AMD | 8.12 | — | entry |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | SQQQ | 3.22 | -0.03 | rebalance down |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | MSTR | 6.04 | -0.14 | rebalance down |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | ETHU | 6.04 | -0.18 | rebalance down |
| 2026-11-24T20:50 | Agent (ML meta-label) | sell | COIN | 6.08 | 0.01 | rebalance down |
| 2026-11-24T20:45 | ROC + volume · 1h | buy | TNA | 15.67 | — | entry |
| 2026-11-24T20:45 | VWAP momentum · 1h | buy | TSLA | 2.69 | — | rebalance up |
| 2026-11-24T20:45 | VWAP momentum · 1h | buy | IWM | 2.68 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 00:10:05.000132+00:00 -> 2026-11-25 00:20:05.000132+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
