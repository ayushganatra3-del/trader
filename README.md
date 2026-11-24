# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T16:11:05.000157+00:00 · 72001 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.87 (-21.13%)

Closed trades 242, win rate 36.0%, fees £6.54, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.77 | -0.01 |

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

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 19422 decisions in 2583 calls, $0.2539 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T16:11 | 5 / 20 / 5 | cash |  |
| Breezy | 2026-11-24T16:11 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-24T16:11 | 4 / 24 / 2 | BITX 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |
| Opening range 30m | SQQQ | 1.57 | +20.80% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 28.60 | 4.33 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.77 | 15.77 | 0 | — | 13.37 | 4.73 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.02 | 4.02 | 0 | — | 4.38 | 1.22 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.93 | -1.07 | 218 | 31.7 | 0.38 | 0.21 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.28 | -3.72 | 228 | 28.5 | 0.01 | 0.09 | -7.48 | 156 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.66 | -2.88 | -7.38 | 1 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.28 | -5.49 | 19 |
| 13 | Hold SPY | benchmark | 93.78 | -6.22 | 0 | — | -6.93 | -1.79 | -11.71 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.95 | -8.05 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.57 | -8.43 | 116 | 24.1 | -8.53 | -4.53 | -11.83 | 40 |
| 16 | Copy: Insider buying | copy | 91.11 | -8.89 | 58 | 39.7 | -8.28 | -1.58 | -14.79 | 70 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.35 | -10.65 | 0 | — | -10.80 | -2.31 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.14 | -2.99 | -20.94 | 1 |
| 20 | Daily: Bullish score | daily | 85.82 | -14.18 | 20 | 20.0 | -12.88 | -2.95 | -19.56 | 14 |
| 21 | VWAP reversion · 1h | reversion | 85.80 | -14.20 | 165 | 46.1 | -11.59 | -2.06 | -20.49 | 152 |
| 22 | Opening range 30m | breakout | 85.01 | -14.99 | 468 | 32.9 | -14.31 | -4.78 | -14.39 | 549 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -19.58 | -7.27 | -19.64 | 74 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 26 | Agent | meta | 78.87 | -21.13 | 242 | 36.0 | -24.85 | -5.61 | -25.49 | 195 |
| 27 | Parabolic SAR · 1h | trend | 78.46 | -21.54 | 206 | 28.2 | -32.44 | -8.51 | -32.55 | 184 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 29 | Volume breakout · 1h | breakout | 76.93 | -23.07 | 169 | 27.8 | -23.40 | -7.21 | -23.97 | 72 |
| 30 | Opening range 15m | breakout | 76.23 | -23.77 | 584 | 30.5 | -22.91 | -7.13 | -22.95 | 671 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -29.72 | -7.86 | -29.73 | 83 |
| 32 | Keltner breakout · 1h | breakout | 75.56 | -24.44 | 137 | 24.8 | -27.08 | -7.08 | -27.97 | 150 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.66 | -8.08 | -31.53 | 101 |
| 34 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.62 | -4.86 | -36.38 | 24 |
| 35 | ADX DI cross · 1h | trend | 69.36 | -30.64 | 259 | 19.3 | -40.21 | -7.47 | -40.65 | 279 |
| 36 | Hold BTC | benchmark | 68.98 | -31.02 | 3 | 0.0 | -29.01 | -5.25 | -36.10 | 1 |
| 37 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.14 | -10.35 | -39.14 | 175 |
| 38 | Supertrend · 1h | trend | 68.15 | -31.85 | 205 | 18.5 | -36.02 | -6.87 | -36.28 | 213 |
| 39 | EMA 20/50 cross · 1h | trend | 68.04 | -31.96 | 124 | 9.7 | -36.11 | -9.97 | -37.44 | 115 |
| 40 | Bollinger breakout · 1h | breakout | 67.96 | -32.04 | 208 | 22.1 | -33.73 | -8.97 | -35.03 | 213 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 67.23 | -32.77 | 3 | 0.0 | -25.96 | -3.16 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 66.83 | -33.17 | 323 | 19.8 | -39.37 | -9.99 | -40.78 | 231 |
| 43 | MACD zero-line · 1h | trend | 64.20 | -35.80 | 199 | 16.6 | -34.03 | -9.04 | -34.28 | 204 |
| 44 | Heikin-Ashi · 1h | trend | 64.13 | -35.87 | 538 | 22.1 | -48.50 | -9.91 | -49.48 | 629 |
| 45 | RSI momentum · 1h | momentum | 64.12 | -35.88 | 200 | 15.0 | -41.63 | -9.69 | -42.28 | 196 |
| 46 | Stochastic reversion · 1h | reversion | 63.57 | -36.43 | 399 | 40.6 | -35.47 | -3.89 | -43.59 | 434 |
| 47 | Max aggression: 5-day momentum | meta | 63.20 | -36.80 | 26 | 34.6 | -62.48 | -4.10 | -67.33 | 23 |
| 48 | ROC + volume · 1h | momentum | 61.67 | -38.33 | 453 | 27.2 | -43.63 | -8.65 | -44.19 | 341 |
| 49 | Donchian 20/10 · 1h | breakout | 61.29 | -38.71 | 181 | 17.7 | -40.90 | -8.76 | -42.73 | 193 |
| 50 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.79 | -5.11 | -35.63 | 178 |
| 51 | Max aggression: 1-day momentum | meta | 59.57 | -40.43 | 34 | 26.5 | -59.10 | -4.35 | -60.68 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 59.12 | -40.88 | 309 | 12.3 | -44.70 | -10.60 | -46.34 | 331 |
| 53 | MACD cross · 1h | trend | 57.43 | -42.57 | 476 | 21.0 | -52.91 | -10.61 | -53.64 | 507 |
| 54 | Agent (ML meta-label) | meta | 56.60 | -43.40 | 2055 | 25.1 | -20.36 | -2.40 | -29.17 | 344 |
| 55 | CCI reversion · 1h | reversion | 56.02 | -43.98 | 441 | 39.2 | -50.94 | -8.61 | -51.93 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 55.40 | -44.60 | 392 | 37.5 | -40.57 | -4.93 | -45.42 | 429 |
| 57 | VWAP momentum · 1h | momentum | 53.08 | -46.92 | 1064 | 21.6 | -57.68 | -13.23 | -58.43 | 1183 |
| 58 | Williams %R · 1h | reversion | 50.99 | -49.01 | 509 | 37.7 | -54.97 | -8.99 | -56.24 | 592 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.76 | -8.63 | -53.02 | 680 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.93 | -99.16 | 5405 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.82 | -33.66 | -84.09 | 1434 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.53 | -50.03 | -94.57 | 2442 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.73 | -32.57 | -90.76 | 1911 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.87 | -42.41 | -91.87 | 2248 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.79 | -29.09 | -89.89 | 1959 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.64 | -98.20 | 3430 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.01 | -55.47 | -97.02 | 3388 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.26 | -38.19 | -93.27 | 2100 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.40 | -34.98 | -83.52 | 1563 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.47 | -99.68 | 6270 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.34 | -39.45 | -93.35 | 2502 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.36 | -36.74 | -94.37 | 3157 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.78 | -99.82 | 6128 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.31 | -44.88 | -93.32 | 2263 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.72 | -22.33 | -51.75 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.19 | -23.91 | -79.19 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -60.55 | -97.82 | 3287 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -62.21 | -99.19 | 5126 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.29 | -27.45 | -71.29 | 1201 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.04 | -48.81 | -95.04 | 2670 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -47.07 | -6.61 | -48.78 | 280 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.65 | -37.50 | -85.71 | 1680 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.03 | -99.77 | 6539 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -31.11 | -91.59 | 2497 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.12 | -20.42 | -83.17 | 1954 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.90 | -31.66 | -91.93 | 2187 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -50.03 | -98.15 | 4057 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.35 | -48.60 | -90.36 | 2192 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -69.17 | -29.50 | -69.17 | 800 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.83 | -28.68 | -73.87 | 1170 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.08 | -19.38 | -84.23 | 1825 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.04 | -50.41 | -98.05 | 4415 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -103.82 | -99.94 | 8265 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -49.05 | -7.47 | -51.38 | 301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T16:10 | Agent | buy | SQQQ | 15.78 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T16:05 | Day trade: Stocks in Play ORB | sell | TNA | 23.52 | -0.71 | target is flat |
| 2026-11-24T16:05 | Agent | sell | SQQQ | 15.92 | 0.19 | selected signal exited |
| 2026-11-24T16:05 | Bollinger reversion · 1h | sell | AMD | 12.56 | -2.00 | stop-loss |
| 2026-11-24T16:05 | Opening range 15m | buy | MSFT | 3.82 | — | rebalance up |
| 2026-11-24T16:05 | Opening range 15m | sell | AMZN | 18.97 | -0.22 | stop-loss |
| 2026-11-24T16:05 | Opening range 15m | sell | AAPL | 19.08 | -0.12 | stop-loss |
| 2026-11-24T16:00 | Agent (ML meta-label) | buy | COIN | 7.71 | — | entry |
| 2026-11-24T16:00 | Agent (ML meta-label) | sell | MSTR | 4.60 | -0.17 | rebalance down |
| 2026-11-24T16:00 | Agent (ML meta-label) | sell | ETHU | 3.11 | -0.20 | rebalance down |
| 2026-11-24T16:00 | Stochastic reversion · 1h | buy | SOL-USD | 7.08 | — | entry signal |
| 2026-11-24T16:00 | VWAP momentum · 1h | sell | BTC-USD | 13.13 | -0.21 | exit signal |
| 2026-11-24T16:00 | Opening range 15m | buy | AMZN | 3.85 | — | rebalance up |
| 2026-11-24T16:00 | Opening range 15m | buy | AAPL | 3.84 | — | rebalance up |
| 2026-11-24T16:00 | Opening range 15m | sell | PLTR | 15.25 | -0.16 | stop-loss |
| 2026-11-24T15:50 | Agent (ML meta-label) | buy | SQQQ | 6.55 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T15:50 | Agent (ML meta-label) | sell | BITX | 2.86 | 0.01 | rebalance down |
| 2026-11-24T15:45 | Agent (ML meta-label) | buy | BITX | 14.18 | — | entry |
| 2026-11-24T15:45 | Agent (ML meta-label) | sell | SQQQ | 14.39 | 0.20 | selected signal exited |
| 2026-11-24T15:45 | CCI reversion · 1h | sell | TQQQ | 2.40 | -0.29 | stop-loss |
| 2026-11-24T15:45 | CCI reversion · 1h | sell | QQQ | 2.57 | -0.11 | stop-loss |
| 2026-11-24T15:45 | Parabolic SAR · 1h | sell | QQQ | 19.51 | -0.60 | stop-loss |
| 2026-11-24T15:45 | MACD cross · 1h | sell | TQQQ | 3.12 | -0.11 | stop-loss |
| 2026-11-24T15:45 | Opening range 30m | sell | AMZN | 21.13 | -0.22 | stop-loss |
| 2026-11-24T15:40 | Agent (ML meta-label) | buy | SQQQ | 7.84 | — | rebalance up |
| 2026-11-24T15:40 | Agent (ML meta-label) | sell | BITX | 11.31 | -0.05 | selected signal exited |
| 2026-11-24T15:35 | Agent (ML meta-label) | buy | SQQQ | 6.35 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T15:35 | Agent (ML meta-label) | sell | BITX | 2.86 | 0.02 | rebalance down |
| 2026-11-24T15:35 | Opening range 30m | buy | MSFT | 21.24 | — | entry signal |
| 2026-11-24T15:30 | Agent (rotation) | buy | SQQQ | 8.02 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T15:30 | Agent (ML meta-label) | buy | BITX | 14.20 | — | entry |
| 2026-11-24T15:30 | Agent (ML meta-label) | sell | SQQQ | 14.26 | 0.08 | selected signal exited |
| 2026-11-24T15:30 | Agent | buy | SQQQ | 15.74 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | UPRO | 4.55 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | TSLA | 3.25 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | TQQQ | 3.12 | -0.33 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | SPY | 3.18 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | QQQ | 3.16 | -0.12 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | PLTR | 3.18 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-24T15:30 | MFI reversion · 1h | sell | MSTR | 3.07 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 16:11:05.000157+00:00 -> 2026-11-24 16:21:05.000157+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
