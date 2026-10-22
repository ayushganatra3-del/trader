# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T02:50:05.000123+00:00 · 31373 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 2115 decisions in 423 calls, $0.0297 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T02:50 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-22T02:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T02:50 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.08 | 6.08 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.55 | 1.55 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.28 | 0.28 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.67 | -0.33 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.45 | -0.55 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Hold BTC | benchmark | 97.95 | -2.05 | 0 | — | 10.67 | 1.69 | -8.68 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.54 | -2.46 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.10 | -2.90 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.73 | -3.27 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.79 | -4.21 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | ADX DI cross · 1h | trend | 95.51 | -4.49 | 92 | 19.6 | -10.94 | -2.00 | -16.14 | 259 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 22 | Daily: Momentum burst | daily | 94.97 | -5.03 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.88 | -5.12 | 92 | 23.9 | -20.41 | -6.36 | -20.58 | 129 |
| 24 | Donchian 55/20 · 1h | breakout | 94.63 | -5.37 | 43 | 16.3 | -15.75 | -3.23 | -16.82 | 103 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.97 | -7.04 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.83 | -7.17 | 113 | 25.7 | -16.62 | -3.68 | -19.79 | 272 |
| 29 | Squeeze breakout · 1h | breakout | 92.50 | -7.50 | 50 | 24.0 | -2.55 | -0.55 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.22 | -7.78 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.04 | -7.96 | 93 | 30.1 | -9.96 | -1.80 | -14.57 | 261 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -18.98 | -6.65 | -19.20 | 262 |
| 34 | Volume breakout · 1h | breakout | 90.39 | -9.61 | 95 | 24.2 | -14.53 | -2.56 | -14.53 | 110 |
| 35 | Supertrend · 1h | trend | 89.69 | -10.31 | 92 | 14.1 | -21.14 | -4.23 | -26.66 | 218 |
| 36 | Stochastic reversion · 1h | reversion | 89.57 | -10.43 | 169 | 47.3 | -13.60 | -2.22 | -22.24 | 363 |
| 37 | RSI momentum · 1h | momentum | 89.14 | -10.86 | 89 | 18.0 | -19.23 | -3.87 | -20.75 | 220 |
| 38 | EMA 20/50 cross · 1h | trend | 88.56 | -11.44 | 62 | 12.9 | -21.21 | -3.66 | -23.57 | 141 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Connors RSI(2) · 1h | reversion | 87.81 | -12.19 | 162 | 41.4 | -23.84 | -7.10 | -23.85 | 199 |
| 41 | Keltner breakout · 1h | breakout | 87.70 | -12.30 | 67 | 23.9 | -18.98 | -3.57 | -24.10 | 201 |
| 42 | MACD cross · 1h | trend | 87.47 | -12.53 | 202 | 22.3 | -23.89 | -4.53 | -26.95 | 467 |
| 43 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -15.84 | -4.43 | -16.97 | 128 |
| 44 | Z-score reversion · 1h | reversion | 86.81 | -13.19 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.54 | -13.46 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.43 | -14.57 | 87 | 20.7 | -22.90 | -4.26 | -28.82 | 230 |
| 47 | Triple EMA stack · 1h | trend | 85.26 | -14.74 | 92 | 15.2 | -26.21 | -4.79 | -27.39 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.02 | -21.11 | 141 |
| 49 | Agent (ML meta-label) | meta | 84.66 | -15.34 | 735 | 20.1 | -14.81 | -2.72 | -18.16 | 369 |
| 50 | MACD zero-line · 1h | trend | 84.56 | -15.44 | 92 | 15.2 | -23.35 | -4.54 | -26.06 | 228 |
| 51 | OBV trend · 1h | momentum | 83.63 | -16.37 | 189 | 18.0 | -30.32 | -5.66 | -31.52 | 307 |
| 52 | ROC + volume · 1h | momentum | 82.81 | -17.19 | 218 | 23.9 | -27.79 | -5.02 | -32.91 | 390 |
| 53 | Williams %R · 1h | reversion | 82.62 | -17.39 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.60 | -17.40 | 163 | 36.2 | -29.10 | -5.61 | -32.84 | 348 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.58 | -18.05 | -46.47 | 605 |
| 56 | CCI reversion · 1h | reversion | 82.14 | -17.86 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.43 | -18.57 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | RSI(14) reversion · 1h | reversion | 80.90 | -19.10 | 85 | 24.7 | -16.91 | -2.89 | -24.99 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 80.80 | -19.20 | 144 | 11.1 | -26.77 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 79.05 | -20.95 | 231 | 30.3 | -38.45 | -7.05 | -41.79 | 537 |
| 61 | VWAP momentum · 1h | momentum | 79.01 | -20.99 | 483 | 22.2 | -46.42 | -8.75 | -52.84 | 1255 |
| 62 | Max aggression: 1-day momentum | meta | 77.18 | -22.82 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.85 | -21.99 | -78.97 | 1713 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.31 | -19.56 | -64.95 | 862 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.34 | -19.63 | -74.04 | 1282 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -66.96 | -22.62 | -67.93 | 1206 |
| 67 | RSI(14) reversion | reversion | 55.71 | -44.29 | 771 | 26.8 | -74.98 | -16.85 | -75.18 | 1622 |
| 68 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.94 | -19.39 | -80.87 | 1439 |
| 69 | VWAP reversion | reversion | 53.68 | -46.32 | 768 | 25.9 | -71.18 | -14.28 | -72.15 | 1469 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -32.02 | -98.87 | 5299 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.10 | -34.33 | -94.26 | 2595 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.04 | -23.78 | -88.71 | 1894 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.25 | -28.08 | -91.74 | 2363 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.13 | -25.28 | -91.26 | 2263 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -35.11 | -97.81 | 3507 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.91 | -37.54 | -97.02 | 3600 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.58 | -28.22 | -94.69 | 2565 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.11 | -27.95 | -83.41 | 1732 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -37.30 | -99.42 | 5743 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.09 | -28.95 | -92.69 | 2622 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -31.08 | -95.89 | 3472 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.06 | -99.77 | 6157 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -30.17 | -91.92 | 2337 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -39.31 | -97.82 | 3627 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -37.40 | -98.55 | 4710 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.24 | -35.20 | -94.46 | 2801 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.46 | -28.02 | -84.44 | 1799 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.56 | -40.03 | -99.56 | 6197 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.35 | -23.10 | -87.41 | 2158 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.11 | -26.95 | -88.15 | 2143 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.09 | -33.63 | -96.09 | 3772 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -33.74 | -89.51 | 2097 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.00 | -34.29 | -96.02 | 4096 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.02 | -99.91 | 8298 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T02:50 | VWAP reversion | buy | XRP-USD | 13.44 | — | entry signal |
| 2026-10-22T02:50 | VWAP reversion | buy | SOL-USD | 13.45 | — | entry signal |
| 2026-10-22T02:50 | VWAP reversion | buy | BTC-USD | 13.45 | — | entry signal |
| 2026-10-22T02:45 | Connors RSI(2) · 1h | sell | ETH-USD | 21.92 | -0.46 | stop-loss |
| 2026-10-22T02:45 | VWAP reversion | sell | XRP-USD | 13.44 | -0.15 | stop-loss |
| 2026-10-22T02:45 | VWAP reversion | sell | DOGE-USD | 13.35 | -0.18 | stop-loss |
| 2026-10-22T02:40 | RSI(14) reversion | buy | SOL-USD | 13.95 | — | entry signal |
| 2026-10-22T02:25 | VWAP reversion | buy | ETH-USD | 13.53 | — | entry signal |
| 2026-10-22T02:25 | VWAP reversion | buy | DOGE-USD | 13.53 | — | entry signal |
| 2026-10-22T02:20 | Connors RSI(2) · 1h | sell | XRP-USD | 21.90 | -0.56 | stop-loss |
| 2026-10-22T02:20 | VWAP reversion | sell | DOGE-USD | 13.43 | -0.16 | stop-loss |
| 2026-10-22T02:20 | RSI(14) reversion | sell | SOL-USD | 13.82 | -0.17 | stop-loss |
| 2026-10-22T02:10 | RSI(14) reversion | buy | SOL-USD | 13.99 | — | entry signal |
| 2026-10-22T02:05 | Connors RSI(2) · 1h | buy | BTC-USD | 17.53 | — | rebalance up |
| 2026-10-22T02:05 | Connors RSI(2) · 1h | sell | DOGE-USD | 21.97 | -0.49 | stop-loss |
| 2026-10-22T02:00 | Connors RSI(2) · 1h | buy | BTC-USD | 4.58 | — | entry signal |
| 2026-10-22T02:00 | Connors RSI(2) · 1h | sell | SOL-USD | 4.42 | -0.06 | rebalance down |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | XRP-USD | 7.69 | 0.19 | exit signal |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | ETH-USD | 7.68 | -0.12 | exit signal |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | DOGE-USD | 7.67 | 0.07 | exit signal |
| 2026-10-22T02:00 | Donchian 20/10 · 1h | sell | BTC-USD | 7.70 | -0.09 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | XRP-USD | 7.48 | 0.17 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | SOL-USD | 8.82 | -0.09 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | ETH-USD | 4.14 | -0.11 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | DOGE-USD | 4.87 | 0.03 | exit signal |
| 2026-10-22T02:00 | RSI momentum · 1h | sell | BTC-USD | 6.30 | -0.03 | exit signal |
| 2026-10-22T02:00 | Ichimoku · 1h | sell | BTC-USD | 17.61 | -0.08 | exit signal |
| 2026-10-22T02:00 | ADX DI cross · 1h | sell | BTC-USD | 7.86 | -0.10 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | XRP-USD | 5.96 | 0.12 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | ETH-USD | 4.40 | -0.01 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | DOGE-USD | 4.88 | 0.07 | exit signal |
| 2026-10-22T02:00 | Supertrend · 1h | sell | BTC-USD | 4.46 | -0.02 | exit signal |
| 2026-10-22T02:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 4.17 | 0.02 | exit signal |
| 2026-10-22T02:00 | VWAP reversion | buy | XRP-USD | 13.59 | — | entry signal |
| 2026-10-22T02:00 | VWAP reversion | buy | DOGE-USD | 13.59 | — | entry signal |
| 2026-10-22T01:45 | ROC + volume · 1h | sell | BTC-USD | 3.92 | -0.03 | stop-loss |
| 2026-10-22T01:40 | Squeeze breakout · 1h | sell | BTC-USD | 18.51 | 0.08 | stop-loss |
| 2026-10-22T01:40 | Keltner breakout · 1h | sell | BTC-USD | 9.73 | 0.04 | stop-loss |
| 2026-10-22T01:40 | Bollinger breakout · 1h | sell | BTC-USD | 7.63 | 0.08 | stop-loss |
| 2026-10-22T01:40 | RSI(14) reversion | sell | XRP-USD | 13.96 | -0.19 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 02:50:05.000123+00:00 -> 2026-10-22 03:00:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
