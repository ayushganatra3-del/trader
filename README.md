# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-14T11:40:05.000114+00:00 · 59342 ticks

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

Today: 8709 decisions in 1743 calls, $0.1218 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-14T11:40 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-11-14T11:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-14T11:40 | 3 / 2 / 0 | cash |  |

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
| 15 | VWAP reversion · 1h | reversion | 95.41 | -4.59 | 144 | 47.2 | -12.89 | -3.34 | -13.17 | 153 |
| 16 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.38 | -1.27 | -14.79 | 60 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.28 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 20 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -15.11 | -5.58 | -17.77 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.30 | -0.70 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.26 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.63 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.63 | -7.33 | -15.23 | 201 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.61 | -3.37 | -22.50 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.39 | -4.61 | -17.28 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.14 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -18.15 | -6.39 | -18.32 | 115 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 32 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.10 | -3.45 | -25.39 | 170 |
| 33 | Stochastic reversion · 1h | reversion | 79.31 | -20.69 | 306 | 47.1 | -27.04 | -4.01 | -28.07 | 404 |
| 34 | Hold BTC | benchmark | 79.31 | -20.69 | 1 | 0.0 | -12.74 | -1.81 | -23.75 | 1 |
| 35 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.71 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 77.71 | -22.29 | 402 | 35.3 | -22.12 | -2.88 | -26.60 | 166 |
| 37 | ADX DI cross · 1h | trend | 76.53 | -23.47 | 200 | 20.0 | -24.07 | -3.59 | -32.66 | 267 |
| 38 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.66 | -4.71 | -30.71 | 238 |
| 41 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 42 | Heikin-Ashi · 1h | trend | 74.62 | -25.38 | 445 | 24.0 | -37.31 | -6.86 | -39.47 | 666 |
| 43 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.28 | -4.56 | -30.99 | 199 |
| 44 | MACD cross · 1h | trend | 73.42 | -26.58 | 389 | 23.4 | -30.21 | -4.45 | -39.21 | 471 |
| 45 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.67 | -4.08 | -37.92 | 208 |
| 46 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.29 | -4.78 | -40.51 | 120 |
| 47 | Supertrend · 1h | trend | 71.93 | -28.07 | 182 | 14.8 | -29.58 | -5.01 | -36.83 | 211 |
| 48 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.23 | -4.47 | -38.66 | 201 |
| 49 | Bollinger reversion · 1h | reversion | 71.49 | -28.51 | 304 | 41.4 | -34.07 | -5.37 | -35.68 | 388 |
| 50 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -31.47 | -5.77 | -38.37 | 376 |
| 51 | CCI reversion · 1h | reversion | 70.41 | -29.59 | 351 | 42.7 | -38.40 | -6.06 | -38.71 | 474 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -29.02 | -5.07 | -38.28 | 271 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.51 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -30.70 | -5.52 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.08 | -32.92 | 386 | 43.3 | -43.70 | -7.26 | -43.88 | 540 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -26.79 | -4.65 | -30.13 | 327 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -36.96 | -7.42 | -43.16 | 323 |
| 58 | RSI(14) reversion · 1h | reversion | 63.13 | -36.87 | 189 | 32.3 | -37.98 | -5.67 | -38.51 | 241 |
| 59 | Z-score reversion · 1h | reversion | 62.78 | -37.22 | 210 | 36.2 | -33.04 | -4.69 | -33.50 | 240 |
| 60 | VWAP momentum · 1h | momentum | 62.56 | -37.44 | 916 | 22.3 | -52.36 | -10.36 | -53.88 | 1235 |
| 61 | Candlestick reversal · 1h | reversion | 61.79 | -38.21 | 492 | 28.0 | -45.38 | -8.42 | -45.91 | 607 |
| 62 | Three white soldiers | momentum | 58.30 | -41.70 | 543 | 14.5 | -49.14 | -21.84 | -49.43 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -44.85 | -99.03 | 5321 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.00 | -25.23 | -80.63 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.74 | -44.60 | -93.75 | 2544 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.48 | -31.83 | -89.53 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -40.96 | -91.32 | 2352 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.65 | -30.62 | -89.66 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -52.04 | -97.90 | 3509 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -55.91 | -96.23 | 3462 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -32.52 | -93.47 | 2317 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.06 | -33.70 | -83.09 | 1657 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -54.69 | -99.56 | 6036 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.16 | -42.35 | -92.18 | 2633 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.29 | -36.11 | -95.29 | 3462 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.22 | -99.81 | 6170 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.37 | -43.66 | -92.40 | 2287 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.34 | -26.32 | -76.34 | 1664 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -57.20 | -97.60 | 3522 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -63.00 | -98.89 | 4943 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.61 | -27.09 | -68.91 | 1252 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -56.00 | -94.75 | 2811 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.20 | -38.72 | -85.21 | 1792 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -71.10 | -99.66 | 6377 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.14 | -32.41 | -90.20 | 2327 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.84 | -19.81 | -79.04 | 1808 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.60 | -36.58 | -90.62 | 2188 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.06 | -49.00 | -97.06 | 3891 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -57.46 | -89.44 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.31 | -29.81 | -66.31 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.35 | -22.65 | -71.36 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.11 | -18.85 | -79.38 | 1729 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.40 | -49.03 | -97.40 | 4351 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -112.15 | -99.94 | 8479 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-16 11:40:05.000114+00:00 -> 2026-11-14 11:50:05.000114+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
