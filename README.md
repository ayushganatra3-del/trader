# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T16:25:05.000147+00:00 · 23796 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.04 (-6.96%)

Closed trades 74, win rate 40.5%, fees £2.60, max drawdown -7.41%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 22422 decisions in 2418 calls, $0.2855 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T16:25 | 1 / 12 / 18 | cash |  |
| Breezy | 2026-10-15T16:25 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-10-15T16:25 | 0 / 30 / 1 | MSTR 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.65 | 4.65 | 0 | — | 4.23 | 2.02 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 103.58 | 3.58 | 1 | 100.0 | 4.17 | 1.14 | -7.93 | 9 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.76 | 2.12 | -3.27 | 19 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -3.22 | -0.99 | -9.61 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.56 | 0.56 | 0 | — | 4.30 | 1.68 | -5.18 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 9 | Hold SPY | benchmark | 99.92 | -0.08 | 0 | — | -0.91 | -0.49 | -3.31 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 58 | 39.7 | -11.77 | -3.24 | -14.08 | 115 |
| 11 | Copy: Insider buying | copy | 99.45 | -0.55 | 20 | 45.0 | -16.60 | -2.65 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.57 | -1.43 | 0 | — | -1.15 | -0.44 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 98.09 | -1.92 | 0 | — | 29.70 | 3.42 | -8.68 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Donchian 55/20 · 1h | breakout | 97.60 | -2.40 | 36 | 16.7 | 7.06 | 0.98 | -22.11 | 112 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.60 | -2.40 | 0 | — | -5.39 | -2.96 | -6.38 | 1 |
| 18 | Trend pullback · 1h | trend | 96.91 | -3.09 | 86 | 24.4 | -24.86 | -7.41 | -25.42 | 163 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 96.73 | -3.27 | 0 | — | -6.15 | -2.39 | -7.50 | 1 |
| 20 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.12 | -3.13 | -5.30 | 30 |
| 21 | Daily: Momentum burst | daily | 96.16 | -3.84 | 5 | 20.0 | -4.55 | -0.54 | -17.67 | 39 |
| 22 | ADX DI cross · 1h | trend | 96.12 | -3.88 | 70 | 21.4 | -10.59 | -1.93 | -15.61 | 254 |
| 23 | Agent (rotation) | meta | 95.87 | -4.13 | 105 | 31.4 | -13.09 | -4.44 | -14.10 | 256 |
| 24 | Max aggression: 5-day momentum | meta | 94.19 | -5.81 | 8 | 37.5 | -5.51 | -0.19 | -34.64 | 26 |
| 25 | Parabolic SAR · 1h | trend | 93.83 | -6.17 | 93 | 22.6 | 2.59 | 0.51 | -22.46 | 281 |
| 26 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.89 | 1.07 | -9.46 | 102 |
| 27 | EMA 20/50 cross · 1h | trend | 93.49 | -6.51 | 51 | 15.7 | 5.49 | 0.80 | -23.96 | 133 |
| 28 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 8.94 | 2.25 | -6.78 | 202 |
| 29 | Daily: Bullish score | daily | 93.31 | -6.69 | 7 | 0.0 | -4.41 | -0.37 | -12.76 | 13 |
| 30 | Agent | meta | 93.04 | -6.96 | 74 | 40.5 | -6.45 | -2.62 | -8.72 | 233 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 92.70 | -7.30 | 0 | — | 3.74 | 0.72 | -13.89 | 1 |
| 32 | MACD cross · 1h | trend | 92.51 | -7.49 | 154 | 22.1 | -12.47 | -1.70 | -22.51 | 464 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 92.36 | -7.64 | 0 | — | -16.54 | -3.13 | -19.22 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 92.08 | -7.92 | 79 | 30.4 | 7.44 | 1.12 | -14.21 | 275 |
| 35 | RSI momentum · 1h | momentum | 91.99 | -8.01 | 73 | 17.8 | 1.69 | 0.40 | -25.51 | 223 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | 10.62 | 1.48 | -12.68 | 118 |
| 37 | Supertrend · 1h | trend | 91.59 | -8.41 | 74 | 13.5 | 0.28 | 0.23 | -22.72 | 213 |
| 38 | Triple EMA stack · 1h | trend | 90.80 | -9.20 | 77 | 16.9 | -7.10 | -0.53 | -32.35 | 232 |
| 39 | Opening range 30m | breakout | 90.45 | -9.55 | 170 | 22.9 | -12.89 | -3.74 | -17.60 | 570 |
| 40 | Ichimoku · 1h | trend | 90.45 | -9.55 | 51 | 15.7 | 0.93 | 0.32 | -22.64 | 123 |
| 41 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -13.03 | -4.28 | -13.23 | 116 |
| 42 | Stochastic reversion · 1h | reversion | 90.21 | -9.79 | 128 | 44.5 | -18.48 | -3.43 | -20.82 | 354 |
| 43 | Connors RSI(2) · 1h | reversion | 89.58 | -10.42 | 141 | 39.7 | -23.32 | -6.98 | -24.89 | 248 |
| 44 | MFI reversion · 1h | reversion | 89.45 | -10.55 | 186 | 29.0 | -17.55 | -3.04 | -20.02 | 144 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -16.96 | -0.63 | -37.31 | 43 |
| 46 | OBV trend · 1h | momentum | 88.52 | -11.48 | 164 | 18.9 | -11.33 | -0.98 | -35.23 | 319 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.38 | -2.01 | -29.15 | 210 |
| 48 | MACD zero-line · 1h | trend | 87.83 | -12.17 | 74 | 16.2 | -21.84 | -4.17 | -22.82 | 225 |
| 49 | Z-score reversion · 1h | reversion | 87.40 | -12.60 | 71 | 33.8 | -11.54 | -2.04 | -17.27 | 178 |
| 50 | Agent (ML meta-label) | meta | 86.81 | -13.19 | 568 | 18.5 | -6.27 | -0.80 | -15.36 | 434 |
| 51 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 180 | 21.7 | -9.44 | -1.19 | -25.31 | 402 |
| 52 | Opening range 15m | breakout | 86.26 | -13.74 | 216 | 20.4 | -18.16 | -4.89 | -21.40 | 709 |
| 53 | Donchian 20/10 · 1h | breakout | 86.16 | -13.84 | 72 | 19.4 | -0.43 | 0.15 | -20.45 | 220 |
| 54 | Heikin-Ashi · 1h | trend | 85.90 | -14.11 | 169 | 26.0 | -30.39 | -4.93 | -39.15 | 660 |
| 55 | VWAP momentum · 1h | momentum | 85.85 | -14.15 | 353 | 21.8 | -35.62 | -5.29 | -43.06 | 1248 |
| 56 | Three white soldiers | momentum | 85.85 | -14.15 | 195 | 18.5 | -47.47 | -19.11 | -48.85 | 604 |
| 57 | EMA 9/21 cross · 1h | trend | 85.08 | -14.92 | 120 | 12.5 | -9.40 | -1.02 | -28.05 | 321 |
| 58 | Bollinger reversion · 1h | reversion | 83.65 | -16.35 | 132 | 31.8 | -28.21 | -6.09 | -31.47 | 338 |
| 59 | Williams %R · 1h | reversion | 83.10 | -16.90 | 166 | 42.2 | -32.26 | -5.31 | -34.82 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 82.68 | -17.32 | 61 | 23.0 | -15.12 | -2.75 | -18.95 | 176 |
| 61 | CCI reversion · 1h | reversion | 82.67 | -17.33 | 141 | 41.8 | -18.54 | -2.45 | -23.38 | 426 |
| 62 | Candlestick reversal · 1h | reversion | 79.81 | -20.19 | 182 | 25.3 | -33.28 | -6.20 | -34.22 | 530 |
| 63 | ROC + volume | momentum | 67.18 | -32.81 | 503 | 22.3 | -74.29 | -16.62 | -76.48 | 1689 |
| 64 | RSI(14) reversion | reversion | 66.68 | -33.32 | 570 | 28.8 | -73.30 | -16.24 | -74.21 | 1559 |
| 65 | Volume breakout | breakout | 65.01 | -34.99 | 313 | 13.4 | -63.63 | -17.85 | -63.67 | 890 |
| 66 | Squeeze breakout | breakout | 64.69 | -35.31 | 405 | 14.8 | -62.88 | -17.47 | -63.39 | 1208 |
| 67 | Donchian 55/20 | breakout | 63.37 | -36.63 | 401 | 17.0 | -68.82 | -14.19 | -71.15 | 1278 |
| 68 | EMA 20/50 cross | trend | 61.66 | -38.34 | 422 | 18.7 | -77.33 | -14.95 | -78.49 | 1441 |
| 69 | VWAP reversion | reversion | 58.35 | -41.66 | 581 | 24.6 | -72.53 | -15.05 | -72.78 | 1440 |
| 70 | AI bee: Boozy | ai | 57.81 | -42.19 | 277 | 5.1 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.49 | -43.51 | 564 | 14.4 | -83.24 | -25.77 | -83.57 | 1837 |
| 72 | Supertrend | trend | 54.62 | -45.38 | 582 | 18.7 | -86.39 | -19.97 | -86.61 | 1909 |
| 73 | Ichimoku | trend | 53.77 | -46.23 | 493 | 9.7 | -81.90 | -22.18 | -82.12 | 1701 |
| 74 | AI bee: Bizzy | ai | 51.04 | -48.96 | 1018 | 8.3 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -28.83 | -98.63 | 5347 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.35 | -28.53 | -93.45 | 2573 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.53 | -23.92 | -90.69 | 2349 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.45 | -25.84 | -91.47 | 2317 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -31.42 | -97.48 | 3513 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.51 | -33.90 | -96.56 | 3565 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -24.31 | -94.32 | 2603 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.28 | -99.42 | 5741 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.09 | -24.86 | -91.21 | 2624 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.16 | -29.84 | -96.17 | 3538 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.35 | -99.73 | 6158 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -28.67 | -91.95 | 2363 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -36.18 | -97.47 | 3632 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.63 | -98.55 | 4687 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.45 | -31.10 | -93.56 | 2775 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.84 | -99.55 | 6166 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.25 | -21.89 | -86.50 | 2117 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.69 | -26.36 | -88.01 | 2108 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.04 | -31.81 | -96.12 | 3781 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -32.91 | -89.50 | 2115 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -32.86 | -95.91 | 4068 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.43 | -99.89 | 8192 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T16:25 | Agent | sell | AAPL | 18.60 | -0.01 | selected signal exited |
| 2026-10-15T16:25 | Three white soldiers | sell | MSTR | 21.47 | 0.64 | exit signal |
| 2026-10-15T16:25 | Opening range 15m | buy | TSLA | 4.11 | — | entry |
| 2026-10-15T16:25 | Opening range 15m | sell | LABU | 4.32 | 0.02 | rebalance down |
| 2026-10-15T16:25 | Supertrend | buy | PLTR | 2.73 | — | entry |
| 2026-10-15T16:25 | Supertrend | sell | GOOGL | 3.00 | -0.00 | exit signal |
| 2026-10-15T16:22 | AI bee: Bizzy | sell | LABU | 7.24 | -0.11 | Jev: sell (sell p=0.88) after 12 min |
| 2026-10-15T16:20 | MFI reversion · 1h | buy | ETHU | 6.24 | — | entry |
| 2026-10-15T16:20 | MFI reversion · 1h | sell | SOXL | 6.24 | -0.09 | target is flat |
| 2026-10-15T16:20 | Three white soldiers | sell | ETH-USD | 21.43 | 0.21 | exit signal |
| 2026-10-15T16:20 | Volume breakout | sell | LABU | 16.09 | -0.25 | stop-loss |
| 2026-10-15T16:20 | Volume breakout | sell | ETH-USD | 16.32 | -0.01 | exit signal |
| 2026-10-15T16:20 | Squeeze breakout | sell | SOL-USD | 16.38 | 0.28 | exit signal |
| 2026-10-15T16:20 | Keltner breakout | sell | UPRO | 4.02 | -0.01 | exit signal |
| 2026-10-15T16:20 | Keltner breakout | sell | LABU | 4.66 | -0.05 | stop-loss |
| 2026-10-15T16:20 | Opening range 30m | buy | META | 1.61 | — | entry |
| 2026-10-15T16:20 | Opening range 30m | buy | AMD | 4.53 | — | entry |
| 2026-10-15T16:20 | Opening range 30m | sell | GOOGL | 5.30 | -0.05 | stop-loss |
| 2026-10-15T16:20 | Opening range 15m | buy | TQQQ | 2.27 | — | entry |
| 2026-10-15T16:20 | Opening range 15m | buy | TECL | 4.11 | — | entry |
| 2026-10-15T16:20 | Opening range 15m | buy | SPY | 4.11 | — | entry |
| 2026-10-15T16:20 | Opening range 15m | buy | SOXL | 4.11 | — | entry |
| 2026-10-15T16:20 | Opening range 15m | buy | QQQ | 4.11 | — | entry |
| 2026-10-15T16:20 | Opening range 15m | buy | PLTR | 4.11 | — | entry signal |
| 2026-10-15T16:20 | Opening range 15m | buy | MSFT | 4.11 | — | entry signal |
| 2026-10-15T16:20 | Opening range 15m | sell | TNA | 4.35 | 0.02 | rebalance down |
| 2026-10-15T16:20 | Opening range 15m | sell | META | 4.41 | -0.00 | rebalance down |
| 2026-10-15T16:20 | Opening range 15m | sell | IWM | 4.37 | 0.00 | rebalance down |
| 2026-10-15T16:20 | Opening range 15m | sell | COIN | 4.74 | 0.19 | rebalance down |
| 2026-10-15T16:20 | Opening range 15m | sell | BITX | 4.67 | 0.15 | rebalance down |
| 2026-10-15T16:20 | Opening range 15m | sell | AMZN | 4.42 | 0.02 | rebalance down |
| 2026-10-15T16:20 | Donchian 55/20 | buy | DOGE-USD | 5.29 | — | entry |
| 2026-10-15T16:20 | Donchian 55/20 | sell | TNA | 6.25 | -0.03 | exit signal |
| 2026-10-15T16:20 | Gap and go | sell | LABU | 23.36 | 0.02 | stop-loss |
| 2026-10-15T16:20 | ROC + volume | buy | MSFT | 10.02 | — | rebalance up |
| 2026-10-15T16:20 | ROC + volume | buy | ETHU | 8.41 | — | rebalance up |
| 2026-10-15T16:20 | ROC + volume | buy | ETH-USD | 10.67 | — | rebalance up |
| 2026-10-15T16:20 | ROC + volume | buy | COIN | 10.68 | — | rebalance up |
| 2026-10-15T16:20 | ROC + volume | sell | XRP-USD | 6.10 | 0.07 | exit signal |
| 2026-10-15T16:20 | ROC + volume | sell | NVDA | 6.14 | -0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 16:25:05.000147+00:00 -> 2026-10-15 16:35:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
