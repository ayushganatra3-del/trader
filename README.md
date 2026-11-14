# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-14T00:40:05.000153+00:00 · 58791 ticks

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
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 450 decisions in 90 calls, $0.0063 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-14T00:40 | 2 / 2 / 1 | cash |  |
| Breezy | 2026-11-14T00:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-14T00:40 | 1 / 4 / 0 | cash |  |

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
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -13.09 | -3.38 | -13.26 | 153 |
| 16 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -5.00 | -0.93 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.28 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 20 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -15.11 | -5.58 | -17.77 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.26 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.63 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.64 | -7.34 | -15.23 | 201 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.62 | -3.37 | -22.50 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.41 | -4.62 | -17.28 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.14 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -18.15 | -6.39 | -18.32 | 115 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 32 | Hold BTC | benchmark | 80.53 | -19.47 | 1 | 0.0 | -12.06 | -1.59 | -22.32 | 1 |
| 33 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.18 | -3.47 | -25.39 | 170 |
| 34 | Stochastic reversion · 1h | reversion | 79.55 | -20.45 | 303 | 47.5 | -26.55 | -3.92 | -28.07 | 401 |
| 35 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.71 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 77.85 | -22.15 | 401 | 35.4 | -22.42 | -2.83 | -26.60 | 168 |
| 37 | ADX DI cross · 1h | trend | 76.53 | -23.47 | 200 | 20.0 | -24.59 | -3.68 | -32.66 | 273 |
| 38 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 240 |
| 41 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 42 | Heikin-Ashi · 1h | trend | 74.62 | -25.38 | 445 | 24.0 | -38.33 | -6.86 | -39.47 | 671 |
| 43 | MACD cross · 1h | trend | 73.59 | -26.41 | 389 | 23.4 | -30.23 | -4.45 | -39.06 | 470 |
| 44 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.56 | -4.63 | -30.99 | 200 |
| 45 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.62 | -4.07 | -37.92 | 208 |
| 46 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.28 | -4.78 | -40.51 | 120 |
| 47 | Supertrend · 1h | trend | 72.16 | -27.84 | 181 | 14.9 | -29.37 | -4.96 | -36.66 | 211 |
| 48 | Bollinger reversion · 1h | reversion | 71.80 | -28.20 | 303 | 41.6 | -33.38 | -5.23 | -35.72 | 384 |
| 49 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.38 | -4.50 | -38.65 | 202 |
| 50 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -31.64 | -5.74 | -38.37 | 377 |
| 51 | CCI reversion · 1h | reversion | 70.79 | -29.21 | 347 | 43.2 | -37.71 | -5.90 | -38.71 | 471 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -29.06 | -5.08 | -38.34 | 272 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.51 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -30.32 | -5.42 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.65 | -32.35 | 383 | 43.6 | -42.72 | -6.97 | -44.04 | 539 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -21.37 | -3.41 | -25.34 | 328 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -37.89 | -7.58 | -43.16 | 330 |
| 58 | Z-score reversion · 1h | reversion | 64.58 | -35.42 | 205 | 37.1 | -31.47 | -4.42 | -31.87 | 238 |
| 59 | RSI(14) reversion · 1h | reversion | 63.99 | -36.01 | 186 | 32.8 | -37.13 | -5.50 | -38.24 | 236 |
| 60 | VWAP momentum · 1h | momentum | 62.60 | -37.40 | 915 | 22.3 | -53.30 | -10.34 | -53.84 | 1240 |
| 61 | Candlestick reversal · 1h | reversion | 62.01 | -37.99 | 488 | 28.3 | -44.88 | -8.27 | -45.94 | 603 |
| 62 | Three white soldiers | momentum | 58.30 | -41.70 | 543 | 14.5 | -49.54 | -21.84 | -49.55 | 664 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.11 | -99.01 | 5309 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.18 | -24.98 | -80.47 | 1426 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.75 | -43.84 | -93.78 | 2544 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -31.08 | -89.35 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -39.85 | -91.19 | 2349 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.83 | -30.62 | -89.83 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -49.64 | -97.87 | 3504 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -53.34 | -96.22 | 3451 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.72 | -32.85 | -93.73 | 2340 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.03 | -33.28 | -83.09 | 1657 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -51.53 | -99.58 | 6048 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -40.87 | -92.16 | 2631 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -36.05 | -95.43 | 3479 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.36 | -99.81 | 6176 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -41.84 | -92.29 | 2285 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.92 | -25.71 | -75.96 | 1657 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -56.43 | -97.60 | 3521 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -57.84 | -98.89 | 4947 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.54 | -26.51 | -68.60 | 1251 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -53.60 | -94.70 | 2808 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.13 | -37.98 | -85.16 | 1791 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -65.66 | -99.67 | 6389 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.24 | -31.42 | -90.28 | 2335 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.21 | -19.39 | -79.33 | 1814 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.81 | -35.58 | -90.83 | 2199 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.08 | -46.46 | -97.09 | 3898 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -55.49 | -89.42 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.36 | -29.79 | -66.36 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.23 | -22.58 | -71.37 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.83 | -18.68 | -80.22 | 1741 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.48 | -47.14 | -97.49 | 4366 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -92.32 | -99.93 | 8464 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-14T00:30 | Three white soldiers | sell | DOGE-USD | 14.55 | -0.03 | exit signal |
| 2026-11-14T00:00 | Stochastic reversion · 1h | buy | ETH-USD | 4.29 | — | entry signal |
| 2026-11-14T00:00 | Stochastic reversion · 1h | sell | BTC-USD | 4.29 | -0.03 | rebalance down |
| 2026-11-14T00:00 | Z-score reversion · 1h | buy | SOL-USD | 10.75 | — | entry signal |
| 2026-11-14T00:00 | Candlestick reversal · 1h | buy | BTC-USD | 3.78 | — | entry signal |
| 2026-11-13T23:35 | Three white soldiers | buy | DOGE-USD | 14.58 | — | entry signal |
| 2026-11-13T23:20 | MACD cross · 1h | sell | BTC-USD | 18.28 | -0.27 | stop-loss |
| 2026-11-13T23:05 | Candlestick reversal · 1h | sell | DOGE-USD | 3.78 | -0.11 | stop-loss |
| 2026-11-13T23:00 | CCI reversion · 1h | sell | SOL-USD | 4.58 | -0.14 | stop-loss |
| 2026-11-13T23:00 | MACD cross · 1h | buy | BTC-USD | 6.06 | — | rebalance up |
| 2026-11-13T23:00 | MACD cross · 1h | sell | XRP-USD | 10.44 | -0.21 | exit signal |
| 2026-11-13T23:00 | MACD cross · 1h | sell | DOGE-USD | 12.30 | -0.29 | exit signal |
| 2026-11-13T22:15 | Z-score reversion · 1h | sell | SOL-USD | 10.75 | -0.34 | stop-loss |
| 2026-11-13T22:00 | VWAP momentum · 1h | sell | DOGE-USD | 3.25 | -0.04 | exit signal |
| 2026-11-13T22:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 9.18 | -0.22 | exit signal |
| 2026-11-13T22:00 | Supertrend · 1h | sell | SOL-USD | 10.17 | -0.18 | exit signal |
| 2026-11-13T22:00 | MACD cross · 1h | sell | SOL-USD | 12.28 | -0.24 | exit signal |
| 2026-11-13T21:00 | Candlestick reversal · 1h | buy | XRP-USD | 2.24 | — | entry |
| 2026-11-13T21:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.89 | — | entry |
| 2026-11-13T21:00 | Candlestick reversal · 1h | sell | BTC-USD | 6.13 | -0.01 | exit signal |
| 2026-11-13T20:55 | Day trade: Stocks in Play ORB | sell | SQQQ | 25.65 | 0.46 | target is flat |
| 2026-11-13T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.88 | -0.01 | target is flat |
| 2026-11-13T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 111.21 | -1.41 | target is flat |
| 2026-11-13T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 92.12 | -1.06 | target is flat |
| 2026-11-13T20:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 114.23 | 2.50 | target is flat |
| 2026-11-13T20:55 | ADX DI cross · 1h | sell | TSLA | 15.71 | 0.32 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-13T20:55 | ADX DI cross · 1h | sell | SQQQ | 18.79 | -0.45 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-13T20:55 | Opening range 30m | sell | SQQQ | 21.21 | -0.27 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 30m | sell | MSFT | 21.60 | 0.06 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 30m | sell | META | 21.63 | 0.13 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 15m | sell | SQQQ | 19.69 | 0.14 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 15m | sell | MSFT | 19.78 | 0.17 | end-of-day flatten |
| 2026-11-13T20:55 | Opening range 15m | sell | META | 19.75 | 0.15 | end-of-day flatten |
| 2026-11-13T20:35 | Keltner breakout · 1h | sell | AAPL | 20.10 | -0.14 | stop-loss |
| 2026-11-13T20:35 | OBV trend · 1h | buy | TSLA | 17.41 | — | entry |
| 2026-11-13T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 93.19 | — | entry |
| 2026-11-13T20:30 | Connors RSI(2) · 1h | buy | AAPL | 20.16 | — | entry signal |
| 2026-11-13T20:30 | OBV trend · 1h | sell | TSLA | 17.37 | -0.03 | target is flat |
| 2026-11-13T20:30 | ROC + volume · 1h | sell | AAPL | 18.15 | -0.00 | exit signal |
| 2026-11-13T20:30 | VWAP momentum · 1h | buy | AMD | 2.84 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-16 00:40:05.000153+00:00 -> 2026-11-14 00:50:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
