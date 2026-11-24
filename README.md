# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T17:10:05.000118+00:00 · 72049 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.61 (-21.39%)

Closed trades 242, win rate 36.0%, fees £6.54, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.51 | -0.27 |

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

Today: 23778 decisions in 2727 calls, $0.3048 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T17:10 | 8 / 21 / 1 | TNA 17%, AMD 16% |  |
| Breezy | 2026-11-24T17:10 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-24T17:10 | 8 / 21 / 1 | BITX 65% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.57 | 15.57 | 0 | — | 13.17 | 4.68 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.06 | 4.06 | 0 | — | 4.21 | 1.23 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.12 | 0.05 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.15 | -3.85 | 229 | 28.4 | -0.15 | 0.04 | -7.48 | 156 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.06 | -3.51 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.44 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.23 | -5.78 | 0 | — | -6.65 | -1.67 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.28 | -5.49 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.95 | -8.05 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 91.45 | -8.55 | 58 | 39.7 | -7.99 | -1.51 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.19 | -8.81 | 116 | 24.1 | -8.95 | -4.82 | -11.87 | 41 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.17 | -10.83 | 0 | — | -11.51 | -2.48 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.51 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 85.95 | -14.05 | 165 | 46.1 | -11.42 | -2.04 | -20.49 | 154 |
| 21 | Daily: Bullish score | daily | 85.46 | -14.54 | 20 | 20.0 | -12.92 | -3.06 | -19.56 | 14 |
| 22 | Opening range 30m | breakout | 85.20 | -14.80 | 468 | 32.9 | -14.12 | -4.73 | -14.39 | 552 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.50 | -6.39 | -17.99 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.62 | -6.51 | -14.78 | 66 |
| 26 | Parabolic SAR · 1h | trend | 78.65 | -21.36 | 206 | 28.2 | -32.27 | -8.48 | -32.65 | 184 |
| 27 | Agent | meta | 78.61 | -21.39 | 242 | 36.0 | -25.88 | -5.91 | -26.37 | 193 |
| 28 | Volume breakout · 1h | breakout | 77.60 | -22.40 | 169 | 27.8 | -22.74 | -6.98 | -23.97 | 72 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 30 | Opening range 15m | breakout | 76.43 | -23.57 | 584 | 30.5 | -22.74 | -7.08 | -22.98 | 674 |
| 31 | Keltner breakout · 1h | breakout | 76.25 | -23.75 | 138 | 24.6 | -26.19 | -6.83 | -27.73 | 149 |
| 32 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -29.72 | -7.86 | -29.73 | 83 |
| 33 | Ichimoku · 1h | trend | 74.06 | -25.94 | 113 | 15.9 | -30.17 | -7.87 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.05 | -29.95 | 259 | 19.3 | -38.72 | -7.36 | -39.77 | 277 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.13 | -4.86 | -36.38 | 24 |
| 36 | Hold BTC | benchmark | 69.05 | -30.95 | 3 | 0.0 | -29.28 | -5.23 | -36.10 | 1 |
| 37 | Supertrend · 1h | trend | 68.69 | -31.31 | 205 | 18.5 | -35.35 | -6.82 | -36.30 | 213 |
| 38 | Bollinger breakout · 1h | breakout | 68.55 | -31.45 | 208 | 22.1 | -32.78 | -8.71 | -34.65 | 212 |
| 39 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.74 | -10.37 | -39.74 | 176 |
| 40 | EMA 20/50 cross · 1h | trend | 67.75 | -32.25 | 124 | 9.7 | -36.28 | -10.07 | -37.34 | 113 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 67.26 | -32.74 | 3 | 0.0 | -25.91 | -3.16 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 66.58 | -33.42 | 323 | 19.8 | -39.24 | -10.06 | -40.24 | 230 |
| 43 | RSI momentum · 1h | momentum | 64.82 | -35.18 | 200 | 15.0 | -41.01 | -9.51 | -42.20 | 195 |
| 44 | Heikin-Ashi · 1h | trend | 64.53 | -35.47 | 538 | 22.1 | -48.15 | -9.86 | -49.45 | 630 |
| 45 | MACD zero-line · 1h | trend | 64.22 | -35.78 | 199 | 16.6 | -35.29 | -9.53 | -35.62 | 201 |
| 46 | Stochastic reversion · 1h | reversion | 63.53 | -36.47 | 400 | 40.5 | -35.91 | -3.96 | -43.59 | 433 |
| 47 | ROC + volume · 1h | momentum | 62.34 | -37.66 | 453 | 27.2 | -43.05 | -8.45 | -44.23 | 341 |
| 48 | Max aggression: 5-day momentum | meta | 62.15 | -37.85 | 26 | 34.6 | -63.10 | -4.18 | -67.33 | 23 |
| 49 | Donchian 20/10 · 1h | breakout | 61.82 | -38.18 | 181 | 17.7 | -40.04 | -8.60 | -42.39 | 192 |
| 50 | Max aggression: 1-day momentum | meta | 61.61 | -38.38 | 34 | 26.5 | -57.69 | -4.28 | -60.68 | 38 |
| 51 | MFI reversion · 1h ⏸ | reversion | 59.77 | -40.23 | 507 | 32.1 | -33.63 | -5.11 | -35.78 | 182 |
| 52 | EMA 9/21 cross · 1h | trend | 59.71 | -40.29 | 309 | 12.3 | -43.97 | -10.33 | -46.09 | 329 |
| 53 | MACD cross · 1h | trend | 57.86 | -42.14 | 477 | 21.0 | -52.12 | -10.46 | -53.39 | 503 |
| 54 | Agent (ML meta-label) | meta | 56.87 | -43.13 | 2061 | 25.1 | -23.01 | -3.05 | -32.82 | 336 |
| 55 | CCI reversion · 1h | reversion | 56.24 | -43.76 | 442 | 39.1 | -50.48 | -8.52 | -51.83 | 505 |
| 56 | Bollinger reversion · 1h | reversion | 55.62 | -44.38 | 392 | 37.5 | -40.41 | -4.92 | -45.42 | 428 |
| 57 | VWAP momentum · 1h | momentum | 53.55 | -46.45 | 1064 | 21.6 | -58.28 | -13.45 | -59.19 | 1174 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.40 | -8.82 | -53.86 | 669 |
| 59 | Williams %R · 1h | reversion | 50.96 | -49.04 | 509 | 37.7 | -55.19 | -9.04 | -56.51 | 591 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.82 | -99.16 | 5397 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.82 | -33.79 | -84.02 | 1428 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.53 | -50.07 | -94.56 | 2444 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -32.56 | -90.76 | 1914 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.72 | -42.29 | -91.77 | 2248 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.67 | -28.84 | -89.84 | 1965 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -49.52 | -98.20 | 3425 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -55.65 | -97.01 | 3381 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.24 | -37.95 | -93.30 | 2088 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.37 | -35.66 | -83.41 | 1560 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.51 | -99.68 | 6285 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.33 | -39.40 | -93.36 | 2502 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.34 | -36.63 | -94.35 | 3155 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.71 | -99.82 | 6142 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.22 | -44.62 | -93.29 | 2259 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.72 | -22.33 | -51.75 | 640 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.31 | -23.78 | -79.37 | 1623 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -59.98 | -97.81 | 3287 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -62.44 | -99.19 | 5134 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.24 | -27.53 | -71.28 | 1202 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.00 | -48.50 | -95.03 | 2676 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.10 | -6.43 | -48.58 | 279 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.51 | -37.29 | -85.67 | 1679 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.97 | -99.77 | 6530 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.52 | -31.19 | -91.64 | 2480 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.84 | -20.29 | -83.14 | 1956 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.86 | -31.75 | -91.94 | 2185 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -50.04 | -98.16 | 4055 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.38 | -48.51 | -90.38 | 2196 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.97 | -29.79 | -68.97 | 800 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.56 | -28.53 | -73.64 | 1169 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.06 | -19.31 | -84.32 | 1821 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.02 | -50.43 | -98.06 | 4415 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -103.37 | -99.94 | 8250 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -48.07 | -7.29 | -51.32 | 290 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T17:10 | Agent (rotation) | sell | SQQQ | 7.94 | -0.08 | selected signal exited |
| 2026-11-24T17:10 | Opening range 30m | buy | TNA | 13.00 | — | entry signal |
| 2026-11-24T17:10 | Opening range 30m | buy | IWM | 17.04 | — | entry signal |
| 2026-11-24T17:10 | Opening range 30m | sell | MSFT | 4.34 | 0.03 | rebalance down |
| 2026-11-24T17:10 | Opening range 30m | sell | LABU | 4.52 | 0.06 | rebalance down |
| 2026-11-24T17:10 | Opening range 15m | buy | TNA | 11.65 | — | entry signal |
| 2026-11-24T17:10 | Opening range 15m | buy | IWM | 15.29 | — | entry signal |
| 2026-11-24T17:10 | Opening range 15m | sell | MSFT | 4.01 | 0.04 | rebalance down |
| 2026-11-24T17:10 | Opening range 15m | sell | LABU | 4.05 | 0.05 | rebalance down |
| 2026-11-24T17:10 | Gap and go | sell | SQQQ | 24.45 | -0.23 | exit signal |
| 2026-11-24T17:00 | Agent (ML meta-label) | buy | BITX | 8.05 | — | entry |
| 2026-11-24T17:00 | VWAP reversion · 1h | buy | SOL-USD | 21.35 | — | entry signal |
| 2026-11-24T17:00 | VWAP reversion · 1h | buy | DOGE-USD | 21.35 | — | entry signal |
| 2026-11-24T16:50 | Agent (ML meta-label) | sell | MSFT | 8.05 | 0.03 | selected signal exited |
| 2026-11-24T16:50 | Opening range 15m | buy | SQQQ | 3.82 | — | rebalance up |
| 2026-11-24T16:45 | Opening range 30m | buy | LABU | 21.28 | — | entry signal |
| 2026-11-24T16:45 | Opening range 15m | buy | LABU | 19.09 | — | entry signal |
| 2026-11-24T16:42 | Agent (ML meta-label) | buy | MSFT | 8.02 | — | entry |
| 2026-11-24T16:42 | Agent (ML meta-label) | sell | BITX | 8.02 | -0.06 | rebalance down |
| 2026-11-24T16:30 | Agent (ML meta-label) | buy | SQQQ | 8.06 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T16:30 | Agent (ML meta-label) | buy | COIN | 8.07 | — | entry |
| 2026-11-24T16:30 | Agent (ML meta-label) | buy | AMD | 8.07 | — | entry |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | UPRO | 3.26 | 0.01 | rebalance down |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | MSTR | 6.03 | -0.18 | rebalance down |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | ETHU | 6.05 | -0.29 | rebalance down |
| 2026-11-24T16:30 | Agent (ML meta-label) | sell | BITX | 3.24 | -0.01 | rebalance down |
| 2026-11-24T16:30 | CCI reversion · 1h | sell | AAPL | 2.67 | -0.01 | exit signal |
| 2026-11-24T16:30 | Keltner breakout · 1h | sell | TSLA | 18.36 | -0.56 | exit signal |
| 2026-11-24T16:30 | Heikin-Ashi · 1h | buy | SQQQ | 16.06 | — | entry signal |
| 2026-11-24T16:30 | Ichimoku · 1h | buy | LABU | 18.38 | — | entry signal |
| 2026-11-24T16:30 | Supertrend · 1h | buy | AAPL | 3.41 | — | entry signal |
| 2026-11-24T16:30 | MACD zero-line · 1h | buy | AAPL | 16.02 | — | entry signal |
| 2026-11-24T16:25 | Agent (ML meta-label) | buy | MSTR | 4.73 | — | rebalance up |
| 2026-11-24T16:25 | Agent (ML meta-label) | buy | ETHU | 4.74 | — | rebalance up |
| 2026-11-24T16:25 | Agent (ML meta-label) | sell | SQQQ | 2.93 | -0.04 | selected signal exited |
| 2026-11-24T16:25 | Agent (ML meta-label) | sell | AMD | 12.17 | -1.61 | selected signal exited |
| 2026-11-24T16:20 | Agent (ML meta-label) | buy | SQQQ | 2.97 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion, CCI reversion, Opening range 30m |
| 2026-11-24T16:15 | Agent (ML meta-label) | buy | UPRO | 11.27 | — | entry |
| 2026-11-24T16:15 | Agent (ML meta-label) | buy | BITX | 4.56 | — | rebalance up |
| 2026-11-24T16:15 | Agent (ML meta-label) | sell | SQQQ | 10.03 | 0.06 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 17:10:05.000118+00:00 -> 2026-11-24 17:20:05.000118+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
