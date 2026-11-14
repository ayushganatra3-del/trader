# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-14T12:40:05.000128+00:00 · 59395 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-14 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 9504 decisions in 1902 calls, $0.1330 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-14T12:40 | 1 / 2 / 2 | XRP-USD 14% |  |
| Breezy | 2026-11-14T12:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-14T12:40 | 1 / 4 / 0 | XRP-USD 50% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 3.17 | +3.60% | 9 |
| RSI momentum | TNA | 2.20 | +2.77% | 6 |
| Z-score reversion | TQQQ | 2.19 | +4.95% | 6 |
| Williams %R | TSLA | 2.15 | +8.36% | 18 |
| Gap and go | TQQQ | 1.80 | +5.84% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.89 | 17.89 | 0 | — | 15.31 | 5.11 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 3.29 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.99 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.58 | 1.81 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 1.00 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 7.52 | 2.97 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.58 | 1.87 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.33 | -1.67 | 0 | — | -0.61 | -0.13 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.12 | 1 | 0.0 | -3.27 | -2.15 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.69 | -3.31 | 191 | 30.4 | -2.89 | -1.02 | -8.46 | 157 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.35 | -3.65 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.52 | -4.48 | 144 | 47.2 | -12.79 | -3.31 | -13.17 | 153 |
| 16 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.38 | -1.27 | -14.79 | 60 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.13 | -3.91 | -5.99 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.28 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 20 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -15.11 | -5.58 | -17.77 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.26 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.63 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.63 | -7.33 | -15.23 | 201 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.04 | -3.23 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.39 | -4.61 | -17.28 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.14 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -18.15 | -6.39 | -18.32 | 115 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 32 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.11 | -3.45 | -25.39 | 169 |
| 33 | Hold BTC | benchmark | 79.35 | -20.65 | 1 | 0.0 | -12.74 | -1.80 | -23.75 | 1 |
| 34 | Stochastic reversion · 1h | reversion | 79.31 | -20.69 | 306 | 47.1 | -27.03 | -4.01 | -28.07 | 404 |
| 35 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.71 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 77.70 | -22.30 | 402 | 35.3 | -22.13 | -2.89 | -26.60 | 166 |
| 37 | ADX DI cross · 1h | trend | 76.53 | -23.47 | 200 | 20.0 | -23.69 | -3.52 | -32.66 | 266 |
| 38 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.66 | -4.71 | -30.71 | 238 |
| 41 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 42 | Heikin-Ashi · 1h | trend | 74.62 | -25.38 | 445 | 24.0 | -37.31 | -6.86 | -39.47 | 666 |
| 43 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.28 | -4.56 | -30.99 | 199 |
| 44 | MACD cross · 1h | trend | 73.42 | -26.58 | 389 | 23.4 | -29.61 | -4.34 | -39.22 | 471 |
| 45 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.59 | -4.07 | -37.92 | 208 |
| 46 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.29 | -4.78 | -40.51 | 120 |
| 47 | Supertrend · 1h | trend | 71.93 | -28.07 | 182 | 14.8 | -29.58 | -5.01 | -36.83 | 211 |
| 48 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.23 | -4.47 | -38.66 | 201 |
| 49 | Bollinger reversion · 1h | reversion | 71.53 | -28.47 | 304 | 41.4 | -34.04 | -5.37 | -35.68 | 388 |
| 50 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -31.54 | -5.79 | -38.37 | 376 |
| 51 | CCI reversion · 1h | reversion | 70.43 | -29.57 | 351 | 42.7 | -38.38 | -6.06 | -38.71 | 474 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -28.54 | -4.97 | -38.28 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.51 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -30.83 | -5.55 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.10 | -32.90 | 386 | 43.3 | -43.68 | -7.26 | -43.88 | 540 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -22.20 | -3.63 | -25.95 | 326 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -36.96 | -7.42 | -43.16 | 323 |
| 58 | RSI(14) reversion · 1h | reversion | 63.15 | -36.85 | 189 | 32.3 | -37.93 | -5.66 | -38.51 | 241 |
| 59 | Z-score reversion · 1h | reversion | 62.87 | -37.13 | 210 | 36.2 | -32.95 | -4.68 | -33.50 | 240 |
| 60 | VWAP momentum · 1h | momentum | 62.55 | -37.45 | 916 | 22.3 | -52.37 | -10.36 | -53.89 | 1235 |
| 61 | Candlestick reversal · 1h | reversion | 61.80 | -38.20 | 492 | 28.0 | -45.13 | -8.41 | -45.68 | 606 |
| 62 | Three white soldiers | momentum | 58.30 | -41.70 | 543 | 14.5 | -49.11 | -21.84 | -49.43 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -44.92 | -99.04 | 5325 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.00 | -25.22 | -80.63 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -44.78 | -93.78 | 2545 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.45 | -31.80 | -89.52 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -40.92 | -91.34 | 2353 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.65 | -30.63 | -89.66 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -52.13 | -97.90 | 3505 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.25 | -56.30 | -96.25 | 3465 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -32.35 | -93.49 | 2318 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.04 | -33.73 | -83.08 | 1657 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -54.72 | -99.56 | 6037 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -42.30 | -92.19 | 2633 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -36.13 | -95.28 | 3461 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.83 | -99.81 | 6175 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.37 | -43.66 | -92.40 | 2287 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.36 | -26.34 | -76.37 | 1665 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -57.71 | -97.59 | 3521 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -63.21 | -98.89 | 4941 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.63 | -27.12 | -68.96 | 1252 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -56.31 | -94.76 | 2812 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.16 | -38.72 | -85.16 | 1789 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -71.13 | -99.65 | 6368 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.14 | -32.41 | -90.20 | 2327 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.75 | -19.81 | -79.04 | 1804 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.55 | -36.50 | -90.59 | 2186 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.05 | -49.04 | -97.05 | 3888 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -57.46 | -89.38 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.31 | -29.81 | -66.31 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.47 | -22.68 | -71.49 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.08 | -18.84 | -79.35 | 1728 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.40 | -49.05 | -97.40 | 4350 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -113.22 | -99.94 | 8483 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-14T11:01 | VWAP momentum · 1h | buy | ETH-USD | 3.66 | — | entry |
| 2026-11-14T11:01 | VWAP momentum · 1h | sell | BTC-USD | 3.65 | -0.03 | exit signal |
| 2026-11-14T10:00 | CCI reversion · 1h | buy | XRP-USD | 3.36 | — | entry signal |
| 2026-11-14T10:00 | CCI reversion · 1h | buy | DOGE-USD | 3.36 | — | entry signal |
| 2026-11-14T10:00 | CCI reversion · 1h | buy | BTC-USD | 3.36 | — | entry signal |
| 2026-11-14T10:00 | Williams %R · 1h | buy | XRP-USD | 3.36 | — | entry signal |
| 2026-11-14T10:00 | Z-score reversion · 1h | buy | SOL-USD | 15.72 | — | entry signal |
| 2026-11-14T10:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.44 | — | entry signal |
| 2026-11-14T10:00 | Candlestick reversal · 1h | buy | BTC-USD | 3.44 | — | entry signal |
| 2026-11-14T10:00 | VWAP momentum · 1h | buy | BTC-USD | 3.68 | — | entry signal |
| 2026-11-14T10:00 | MACD cross · 1h | buy | ETH-USD | 14.72 | — | entry signal |
| 2026-11-14T10:00 | MACD cross · 1h | buy | BTC-USD | 14.72 | — | entry signal |
| 2026-11-14T09:00 | CCI reversion · 1h | buy | SOL-USD | 3.91 | — | entry signal |
| 2026-11-14T09:00 | VWAP reversion · 1h | buy | XRP-USD | 23.82 | — | entry signal |
| 2026-11-14T07:20 | Williams %R · 1h | sell | XRP-USD | 6.55 | -0.27 | stop-loss |
| 2026-11-14T07:20 | Stochastic reversion · 1h | buy | BTC-USD | 3.47 | — | entry |
| 2026-11-14T07:20 | Stochastic reversion · 1h | sell | XRP-USD | 3.47 | -0.05 | stop-loss |
| 2026-11-14T07:20 | RSI(14) reversion · 1h | buy | SOL-USD | 1.41 | — | rebalance up |
| 2026-11-14T07:20 | RSI(14) reversion · 1h | buy | BTC-USD | 9.00 | — | entry |
| 2026-11-14T07:20 | RSI(14) reversion · 1h | sell | XRP-USD | 10.40 | -0.33 | stop-loss |
| 2026-11-14T07:20 | Candlestick reversal · 1h | sell | XRP-USD | 4.02 | -0.11 | stop-loss |
| 2026-11-14T07:00 | CCI reversion · 1h | buy | ETH-USD | 4.14 | — | entry signal |
| 2026-11-14T06:00 | Williams %R · 1h | buy | SOL-USD | 2.58 | — | entry signal |
| 2026-11-14T06:00 | Z-score reversion · 1h | buy | XRP-USD | 15.77 | — | entry signal |
| 2026-11-14T06:00 | Z-score reversion · 1h | buy | DOGE-USD | 15.77 | — | entry signal |
| 2026-11-14T06:00 | RSI(14) reversion · 1h | buy | SOL-USD | 3.59 | — | entry signal |
| 2026-11-14T05:00 | MFI reversion · 1h | buy | ETH-USD | 9.42 | — | entry signal |
| 2026-11-14T05:00 | Bollinger reversion · 1h | buy | DOGE-USD | 1.01 | — | entry signal |
| 2026-11-14T05:00 | RSI(14) reversion · 1h | buy | ETH-USD | 10.56 | — | entry signal |
| 2026-11-14T05:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 10.56 | — | entry signal |
| 2026-11-14T05:00 | RSI(14) reversion · 1h | sell | XRP-USD | 5.32 | -0.11 | rebalance down |
| 2026-11-14T03:35 | Stochastic reversion · 1h | buy | XRP-USD | 3.52 | — | entry |
| 2026-11-14T03:35 | Stochastic reversion · 1h | buy | SOL-USD | 4.96 | — | entry |
| 2026-11-14T03:35 | Stochastic reversion · 1h | sell | ETH-USD | 4.17 | -0.12 | stop-loss |
| 2026-11-14T03:35 | Stochastic reversion · 1h | sell | BTC-USD | 4.31 | -0.12 | stop-loss |
| 2026-11-14T03:00 | Williams %R · 1h | buy | ETH-USD | 3.54 | — | entry signal |
| 2026-11-14T03:00 | Williams %R · 1h | buy | DOGE-USD | 3.54 | — | entry signal |
| 2026-11-14T03:00 | Williams %R · 1h | buy | BTC-USD | 3.54 | — | entry signal |
| 2026-11-14T03:00 | Bollinger reversion · 1h | buy | XRP-USD | 8.95 | — | entry signal |
| 2026-11-14T03:00 | Candlestick reversal · 1h | buy | XRP-USD | 4.13 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-16 12:40:05.000128+00:00 -> 2026-11-14 12:50:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
