# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T13:30:05.000135+00:00 · 39071 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 116, win rate 38.8%, fees £3.50, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-28 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 9711 decisions in 1947 calls, $0.1357 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T13:30 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-28T13:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T13:30 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | SQQQ | 2.48 | +5.29% | 6 |
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| VWAP momentum · 1h | LABU | 2.05 | +21.96% | 3 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.28 | 7.29 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.29 | 1.29 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.36 | -3.69 | -14.23 | 148 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.74 | -0.26 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.95 | 3.72 | -1.98 | 95 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.89 | -2.11 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.44 | -3.56 | 123 | 31.7 | -4.47 | -2.47 | -7.67 | 186 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.17 | -3.83 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 95.89 | -4.12 | 0 | — | 0.38 | 0.23 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.37 | 1.75 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.64 | -6.36 | 51 | 15.7 | -13.68 | -3.05 | -15.40 | 101 |
| 22 | Trend pullback · 1h | trend | 93.21 | -6.79 | 96 | 22.9 | -20.98 | -6.96 | -21.20 | 110 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.74 | -7.26 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.71 | -7.29 | 125 | 28.0 | -20.12 | -4.91 | -22.91 | 247 |
| 25 | ADX DI cross · 1h | trend | 92.07 | -7.93 | 120 | 18.3 | -14.13 | -3.04 | -15.89 | 270 |
| 26 | Daily: Momentum burst | daily | 92.07 | -7.93 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 91.99 | -8.01 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.47 | -8.53 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.39 | -8.61 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 91.04 | -8.96 | 55 | 23.6 | -4.77 | -1.25 | -12.22 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.33 | -9.67 | 113 | 26.5 | -12.82 | -2.67 | -16.02 | 105 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.22 | -6.48 | -12.01 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 88.92 | -11.08 | 114 | 27.2 | -11.44 | -2.21 | -18.15 | 247 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -10.87 | -3.57 | -14.77 | 96 |
| 36 | Stochastic reversion · 1h | reversion | 87.97 | -12.03 | 205 | 47.3 | -20.38 | -3.78 | -22.35 | 387 |
| 37 | Keltner breakout · 1h | breakout | 87.47 | -12.53 | 74 | 23.0 | -19.21 | -3.68 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.10 | -12.90 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 85.99 | -14.01 | 114 | 14.0 | -23.79 | -4.81 | -26.59 | 232 |
| 41 | RSI momentum · 1h | momentum | 85.15 | -14.85 | 106 | 15.1 | -24.35 | -4.84 | -26.87 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 84.86 | -15.14 | 176 | 40.9 | -23.56 | -7.36 | -23.76 | 178 |
| 43 | EMA 20/50 cross · 1h | trend | 84.55 | -15.45 | 73 | 11.0 | -22.82 | -4.64 | -24.49 | 137 |
| 44 | MACD cross · 1h | trend | 84.40 | -15.60 | 248 | 23.0 | -27.42 | -5.30 | -29.94 | 475 |
| 45 | Ichimoku · 1h | trend | 84.25 | -15.75 | 68 | 11.8 | -19.93 | -4.04 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.76 | -16.23 | 101 | 14.9 | -28.39 | -5.39 | -31.19 | 205 |
| 47 | MFI reversion · 1h | reversion | 83.56 | -16.44 | 274 | 32.1 | -16.15 | -2.49 | -20.54 | 154 |
| 48 | CCI reversion · 1h | reversion | 82.72 | -17.28 | 230 | 45.2 | -23.83 | -3.40 | -28.06 | 461 |
| 49 | Williams %R · 1h | reversion | 82.27 | -17.73 | 232 | 47.0 | -34.22 | -5.81 | -35.31 | 534 |
| 50 | Donchian 20/10 · 1h | breakout | 82.16 | -17.84 | 101 | 20.8 | -23.12 | -4.37 | -26.02 | 220 |
| 51 | MACD zero-line · 1h | trend | 81.40 | -18.60 | 112 | 15.2 | -23.97 | -5.11 | -25.67 | 229 |
| 52 | Agent (ML meta-label) | meta | 80.97 | -19.03 | 982 | 20.6 | -9.29 | -1.67 | -18.19 | 347 |
| 53 | Bollinger reversion · 1h | reversion | 80.93 | -19.07 | 182 | 37.4 | -29.10 | -5.95 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.74 | -19.26 | 209 | 17.7 | -31.08 | -6.39 | -33.47 | 295 |
| 55 | RSI(14) reversion · 1h | reversion | 80.53 | -19.47 | 107 | 27.1 | -15.82 | -2.95 | -24.48 | 183 |
| 56 | ROC + volume · 1h | momentum | 79.49 | -20.51 | 259 | 25.9 | -29.21 | -5.51 | -31.48 | 377 |
| 57 | Heikin-Ashi · 1h | trend | 78.43 | -21.57 | 305 | 22.6 | -42.73 | -9.34 | -43.95 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.55 | -22.45 | 285 | 29.5 | -35.54 | -7.18 | -36.48 | 539 |
| 59 | VWAP momentum · 1h | momentum | 76.95 | -23.05 | 585 | 22.7 | -49.54 | -10.83 | -50.51 | 1234 |
| 60 | EMA 9/21 cross · 1h | trend | 76.85 | -23.15 | 176 | 10.8 | -29.64 | -6.25 | -31.61 | 337 |
| 61 | Three white soldiers | momentum | 76.19 | -23.81 | 334 | 18.6 | -45.32 | -21.38 | -45.35 | 612 |
| 62 | Max aggression: 1-day momentum | meta | 72.70 | -27.30 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 52.08 | -47.92 | 826 | 21.9 | -75.71 | -27.59 | -75.71 | 1574 |
| 64 | Volume breakout | breakout | 51.00 | -49.00 | 502 | 12.4 | -64.51 | -26.49 | -64.53 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.86 | -43.55 | -98.86 | 5127 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.03 | -23.30 | -79.13 | 1408 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.66 | -45.34 | -93.66 | 2528 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.20 | -30.29 | -89.21 | 1918 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -37.68 | -91.53 | 2336 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.50 | -31.65 | -90.50 | 2201 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -52.32 | -97.86 | 3499 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -58.41 | -96.18 | 3377 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -36.59 | -94.06 | 2469 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.49 | -34.27 | -82.49 | 1693 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -53.13 | -99.42 | 5757 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.15 | -44.01 | -93.16 | 2640 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.71 | -95.43 | 3398 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.18 | -99.79 | 6178 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.40 | -44.90 | -92.41 | 2310 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -63.94 | -97.79 | 3585 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.83 | -98.66 | 4788 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.33 | -30.12 | -69.36 | 1189 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -56.81 | -94.80 | 2774 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.02 | -40.03 | -85.02 | 1817 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.97 | -99.61 | 6298 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -28.87 | -88.34 | 2226 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.84 | -19.18 | -76.99 | 1688 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.63 | -36.95 | -90.64 | 2261 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.30 | -47.62 | -96.30 | 3814 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -48.77 | -90.05 | 2129 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.10 | -24.59 | -73.14 | 1276 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.19 | -17.94 | -76.34 | 1578 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.64 | -49.69 | -96.65 | 4204 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -103.72 | -99.92 | 8285 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T13:25 | Donchian 20/10 · 1h | sell | SOL-USD | 5.44 | -0.04 | stop-loss |
| 2026-10-28T13:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 21.24 | — | entry signal |
| 2026-10-28T13:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 3.89 | — | rebalance up |
| 2026-10-28T13:00 | Donchian 55/20 · 1h | sell | XRP-USD | 3.89 | -0.06 | exit signal |
| 2026-10-28T13:00 | Donchian 20/10 · 1h | buy | SOL-USD | 5.48 | — | entry |
| 2026-10-28T13:00 | Donchian 20/10 · 1h | sell | XRP-USD | 8.28 | 0.02 | exit signal |
| 2026-10-28T13:00 | RSI momentum · 1h | buy | DOGE-USD | 5.07 | — | entry |
| 2026-10-28T13:00 | RSI momentum · 1h | buy | BTC-USD | 5.33 | — | entry |
| 2026-10-28T13:00 | RSI momentum · 1h | sell | XRP-USD | 5.64 | -0.02 | exit signal |
| 2026-10-28T13:00 | RSI momentum · 1h | sell | ETH-USD | 4.25 | -0.02 | exit signal |
| 2026-10-28T13:00 | VWAP momentum · 1h | sell | SOL-USD | 3.20 | 0.00 | exit signal |
| 2026-10-28T13:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.44 | 0.08 | exit signal |
| 2026-10-28T13:00 | Heikin-Ashi · 1h | sell | SOL-USD | 4.83 | -0.08 | exit signal |
| 2026-10-28T13:00 | Parabolic SAR · 1h | sell | DOGE-USD | 11.51 | 0.23 | exit signal |
| 2026-10-28T13:00 | Parabolic SAR · 1h | sell | BTC-USD | 11.34 | 0.06 | exit signal |
| 2026-10-28T13:00 | MACD zero-line · 1h | buy | SOL-USD | 6.79 | — | entry |
| 2026-10-28T13:00 | MACD zero-line · 1h | sell | ETH-USD | 8.95 | -0.05 | exit signal |
| 2026-10-28T13:00 | MACD cross · 1h | sell | ETH-USD | 5.22 | 0.04 | exit signal |
| 2026-10-28T13:00 | MACD cross · 1h | sell | DOGE-USD | 3.64 | -0.04 | exit signal |
| 2026-10-28T13:00 | MACD cross · 1h | sell | BTC-USD | 4.91 | 0.03 | exit signal |
| 2026-10-28T12:35 | Bollinger breakout · 1h | sell | SOL-USD | 5.49 | -0.08 | stop-loss |
| 2026-10-28T12:35 | Donchian 55/20 · 1h | buy | DOGE-USD | 5.44 | — | rebalance up |
| 2026-10-28T12:35 | Donchian 55/20 · 1h | sell | BTC-USD | 5.44 | -0.08 | stop-loss |
| 2026-10-28T12:35 | VWAP momentum · 1h | sell | ETH-USD | 4.47 | -0.08 | stop-loss |
| 2026-10-28T12:35 | VWAP momentum · 1h | sell | BTC-USD | 4.23 | -0.07 | stop-loss |
| 2026-10-28T12:15 | Squeeze breakout · 1h | sell | BTC-USD | 18.20 | -0.01 | stop-loss |
| 2026-10-28T12:15 | Bollinger breakout · 1h | sell | DOGE-USD | 5.18 | -0.07 | stop-loss |
| 2026-10-28T12:15 | Bollinger breakout · 1h | sell | BTC-USD | 6.36 | 0.02 | stop-loss |
| 2026-10-28T12:10 | Squeeze breakout · 1h | sell | ETH-USD | 18.25 | -0.03 | stop-loss |
| 2026-10-28T12:10 | Bollinger breakout · 1h | buy | SOL-USD | 4.49 | — | rebalance up |
| 2026-10-28T12:10 | Bollinger breakout · 1h | sell | ETH-USD | 6.35 | 0.05 | stop-loss |
| 2026-10-28T12:00 | Connors RSI(2) · 1h | buy | XRP-USD | 21.30 | — | entry signal |
| 2026-10-28T12:00 | Squeeze breakout · 1h | sell | XRP-USD | 18.24 | 0.05 | exit signal |
| 2026-10-28T12:00 | Bollinger breakout · 1h | buy | SOL-USD | 1.08 | — | entry |
| 2026-10-28T12:00 | Bollinger breakout · 1h | buy | DOGE-USD | 5.25 | — | entry |
| 2026-10-28T12:00 | Bollinger breakout · 1h | sell | XRP-USD | 6.33 | 0.05 | exit signal |
| 2026-10-28T12:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 4.00 | 0.09 | exit signal |
| 2026-10-28T12:00 | Heikin-Ashi · 1h | sell | BTC-USD | 4.33 | -0.03 | exit signal |
| 2026-10-28T12:00 | Parabolic SAR · 1h | sell | ETH-USD | 11.43 | 0.14 | exit signal |
| 2026-10-28T10:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.36 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 13:30:05.000135+00:00 -> 2026-10-28 13:40:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
