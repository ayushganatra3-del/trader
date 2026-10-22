# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T23:45:05.000165+00:00 · 32398 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 98, win rate 39.8%, fees £3.14, max drawdown -10.53%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 40863 decisions in 3498 calls, $0.5080 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T23:45 | 2 / 2 / 1 | SOL-USD 15% |  |
| Breezy | 2026-10-22T23:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T23:45 | 3 / 1 / 1 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.17 | 7.17 | 0 | — | 8.93 | 4.37 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.96 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.33 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.82 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.78 | 0.78 | 0 | — | 4.24 | 1.83 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.26 | 0.26 | 78 | 46.2 | -10.28 | -2.76 | -13.79 | 142 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.30 | -0.70 | 10 | 50.0 | -16.15 | -1.27 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.23 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.07 | -4.06 | 22 |
| 12 | Hold SPY | benchmark | 98.16 | -1.84 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -2.00 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.54 | -3.46 | 118 | 31.4 | -3.72 | -1.63 | -7.58 | 234 |
| 15 | Hold BTC | benchmark | 95.94 | -4.06 | 0 | — | 4.10 | 0.79 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.75 | -4.25 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.03 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.95 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.40 | -4.60 | 0 | — | -4.72 | -1.77 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.17 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.24 | -5.76 | 25 | 40.0 | -13.46 | -2.32 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.75 | -6.25 | 95 | 23.2 | -22.45 | -7.03 | -22.70 | 121 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.74 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.04 | -6.96 | 48 | 16.7 | -18.51 | -3.78 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.93 | -7.07 | 115 | 26.1 | -16.86 | -3.74 | -20.59 | 263 |
| 26 | Daily: Momentum burst | daily | 92.53 | -7.47 | 8 | 12.5 | -16.39 | -2.92 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.45 | -7.55 | 103 | 19.4 | -10.11 | -1.96 | -12.90 | 251 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.42 | -0.76 | -11.76 | 95 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.14 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -13.25 | -6.17 | -14.04 | 261 |
| 31 | Daily: Bullish score | daily | 89.70 | -10.30 | 8 | 0.0 | -7.26 | -0.85 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.43 | -10.57 | 104 | 27.9 | -11.50 | -2.05 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.12 | -10.88 | 101 | 22.8 | -12.69 | -2.29 | -14.45 | 107 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.92 | -11.08 | 0 | — | -3.71 | -0.43 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -15.67 | -3.52 | -16.68 | 131 |
| 36 | EMA 20/50 cross · 1h | trend | 87.52 | -12.48 | 68 | 11.8 | -24.31 | -4.46 | -25.66 | 144 |
| 37 | Stochastic reversion · 1h | reversion | 87.08 | -12.92 | 179 | 45.3 | -16.38 | -2.71 | -22.24 | 389 |
| 38 | Supertrend · 1h | trend | 86.92 | -13.08 | 104 | 15.4 | -23.81 | -4.67 | -27.15 | 218 |
| 39 | RSI momentum · 1h | momentum | 86.64 | -13.36 | 96 | 16.7 | -20.78 | -3.95 | -22.88 | 213 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.30 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.21 | -13.79 | 73 | 23.3 | -23.21 | -4.51 | -24.29 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.05 | -14.95 | 168 | 39.9 | -26.16 | -7.15 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 84.71 | -15.29 | 216 | 23.1 | -28.48 | -5.19 | -29.90 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.34 | -15.66 | 96 | 15.6 | -27.44 | -5.15 | -29.45 | 215 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.74 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 82.94 | -17.06 | 104 | 33.7 | -14.14 | -2.07 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.66 | -17.34 | 93 | 20.4 | -24.80 | -4.51 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.24 | -17.76 | 198 | 17.7 | -29.98 | -5.68 | -31.86 | 299 |
| 49 | MACD zero-line · 1h | trend | 82.21 | -17.79 | 103 | 15.5 | -24.65 | -4.80 | -25.17 | 226 |
| 50 | MFI reversion · 1h | reversion | 81.91 | -18.09 | 245 | 31.4 | -18.66 | -2.87 | -21.11 | 149 |
| 51 | Williams %R · 1h | reversion | 81.77 | -18.23 | 204 | 44.1 | -33.57 | -5.36 | -37.94 | 529 |
| 52 | Three white soldiers | momentum | 81.58 | -18.42 | 268 | 19.8 | -45.32 | -18.35 | -45.32 | 600 |
| 53 | CCI reversion · 1h | reversion | 80.41 | -19.59 | 193 | 43.0 | -24.08 | -3.27 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.20 | -19.80 | 827 | 19.0 | -15.89 | -3.03 | -18.63 | 382 |
| 55 | Bollinger reversion · 1h | reversion | 80.06 | -19.94 | 168 | 35.1 | -31.11 | -6.01 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 79.97 | -20.03 | 260 | 23.5 | -43.26 | -9.33 | -44.09 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.70 | -20.30 | 233 | 24.0 | -28.53 | -5.15 | -29.04 | 380 |
| 58 | EMA 9/21 cross · 1h | trend | 78.17 | -21.83 | 155 | 11.6 | -33.01 | -6.30 | -33.53 | 333 |
| 59 | RSI(14) reversion · 1h | reversion | 77.65 | -22.35 | 90 | 23.3 | -23.64 | -4.32 | -24.19 | 194 |
| 60 | Candlestick reversal · 1h | reversion | 77.19 | -22.81 | 244 | 29.1 | -39.43 | -7.04 | -41.12 | 569 |
| 61 | VWAP momentum · 1h | momentum | 76.95 | -23.05 | 499 | 21.4 | -50.00 | -10.26 | -50.94 | 1231 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.85 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.79 | -41.21 | 693 | 23.1 | -78.67 | -23.05 | -79.49 | 1684 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -65.16 | -20.89 | -65.32 | 853 |
| 65 | Donchian 55/20 | breakout | 56.05 | -43.95 | 542 | 19.9 | -73.73 | -19.95 | -74.14 | 1266 |
| 66 | Squeeze breakout | breakout | 54.94 | -45.06 | 535 | 14.4 | -67.79 | -24.17 | -68.49 | 1201 |
| 67 | EMA 20/50 cross | trend | 53.89 | -46.11 | 590 | 20.5 | -80.17 | -21.20 | -80.17 | 1443 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.57 | -17.04 | -77.05 | 1684 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -73.63 | -14.64 | -73.85 | 1518 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -33.01 | -98.88 | 5257 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.17 | -35.47 | -94.33 | 2555 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.65 | -25.13 | -88.65 | 1884 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.90 | -29.85 | -92.16 | 2337 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.77 | -25.27 | -90.88 | 2204 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -36.90 | -97.95 | 3497 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.02 | -39.24 | -97.11 | 3556 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -28.92 | -94.47 | 2546 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.43 | -29.30 | -83.43 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -37.09 | -99.49 | 5879 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.77 | -31.94 | -93.21 | 2619 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -30.96 | -95.67 | 3417 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -44.28 | -99.79 | 6190 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.31 | -32.84 | -92.31 | 2331 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -40.62 | -97.76 | 3568 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -38.90 | -98.66 | 4769 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -37.91 | -94.74 | 2785 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.05 | -29.35 | -84.77 | 1778 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -40.95 | -99.60 | 6230 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.08 | -23.96 | -88.13 | 2198 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.79 | -27.29 | -88.79 | 2180 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -34.58 | -96.29 | 3802 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.84 | -34.91 | -89.85 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.21 | -34.98 | -96.22 | 4134 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.36 | -99.91 | 8241 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T23:40 | EMA 20/50 cross | sell | DOGE-USD | 13.43 | -0.11 | exit signal |
| 2026-10-22T23:00 | CCI reversion · 1h | buy | XRP-USD | 4.19 | — | entry signal |
| 2026-10-22T23:00 | CCI reversion · 1h | buy | ETH-USD | 4.95 | — | rebalance up |
| 2026-10-22T23:00 | CCI reversion · 1h | sell | DOGE-USD | 4.57 | -0.04 | rebalance down |
| 2026-10-22T23:00 | CCI reversion · 1h | sell | BTC-USD | 4.57 | -0.04 | rebalance down |
| 2026-10-22T23:00 | Candlestick reversal · 1h | sell | SOL-USD | 5.11 | -0.05 | exit signal |
| 2026-10-22T23:00 | MACD cross · 1h | buy | DOGE-USD | 21.20 | — | entry signal |
| 2026-10-22T22:45 | EMA 20/50 cross | sell | BTC-USD | 13.44 | -0.10 | exit signal |
| 2026-10-22T22:20 | Squeeze breakout | sell | ETH-USD | 13.65 | -0.11 | stop-loss |
| 2026-10-22T22:20 | Donchian 55/20 | sell | ETH-USD | 13.94 | -0.14 | stop-loss |
| 2026-10-22T22:20 | Donchian 55/20 | sell | BTC-USD | 13.96 | -0.11 | stop-loss |
| 2026-10-22T22:20 | EMA 20/50 cross | sell | ETH-USD | 13.42 | -0.14 | stop-loss |
| 2026-10-22T22:15 | ROC + volume | sell | ETH-USD | 14.64 | -0.13 | exit signal |
| 2026-10-22T22:10 | Three white soldiers | sell | BTC-USD | 20.32 | -0.14 | exit signal |
| 2026-10-22T22:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.15 | — | entry signal |
| 2026-10-22T22:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.15 | — | entry signal |
| 2026-10-22T22:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.15 | — | entry signal |
| 2026-10-22T21:55 | EMA 20/50 cross | buy | DOGE-USD | 13.54 | — | entry signal |
| 2026-10-22T21:35 | Three white soldiers | sell | XRP-USD | 20.34 | -0.13 | exit signal |
| 2026-10-22T21:35 | ROC + volume | sell | SOL-USD | 14.61 | -0.16 | stop-loss |
| 2026-10-22T21:35 | EMA 20/50 cross | buy | BTC-USD | 13.54 | — | entry signal |
| 2026-10-22T21:25 | Donchian 55/20 | buy | BTC-USD | 14.07 | — | entry signal |
| 2026-10-22T21:25 | EMA 20/50 cross | buy | ETH-USD | 13.56 | — | entry signal |
| 2026-10-22T21:20 | Three white soldiers | buy | BTC-USD | 20.46 | — | entry signal |
| 2026-10-22T21:20 | Donchian 55/20 | buy | ETH-USD | 14.08 | — | entry signal |
| 2026-10-22T21:20 | ROC + volume | buy | SOL-USD | 14.77 | — | entry signal |
| 2026-10-22T21:20 | ROC + volume | buy | ETH-USD | 14.77 | — | entry signal |
| 2026-10-22T21:15 | Squeeze breakout | buy | ETH-USD | 13.76 | — | entry signal |
| 2026-10-22T21:10 | Three white soldiers | buy | XRP-USD | 20.46 | — | entry signal |
| 2026-10-22T21:00 | Stochastic reversion · 1h | buy | XRP-USD | 2.38 | — | entry signal |
| 2026-10-22T21:00 | Candlestick reversal · 1h | sell | ETH-USD | 7.68 | -0.05 | exit signal |
| 2026-10-22T21:00 | Candlestick reversal · 1h | sell | DOGE-USD | 7.67 | -0.06 | exit signal |
| 2026-10-22T21:00 | Candlestick reversal · 1h | sell | BTC-USD | 7.68 | -0.05 | exit signal |
| 2026-10-22T20:46 | Agent (ML meta-label) | buy | ETH-USD | 3.96 | — | entry |
| 2026-10-22T20:25 | Agent (ML meta-label) | sell | ETH-USD | 3.96 | -0.03 | selected signal exited |
| 2026-10-22T20:20 | Stochastic reversion · 1h | buy | BTC-USD | 4.84 | — | entry |
| 2026-10-22T20:20 | Stochastic reversion · 1h | sell | XRP-USD | 7.22 | -0.19 | stop-loss |
| 2026-10-22T20:00 | MFI reversion · 1h | buy | BTC-USD | 4.82 | — | entry signal |
| 2026-10-22T20:00 | MFI reversion · 1h | sell | SOL-USD | 4.82 | -0.04 | rebalance down |
| 2026-10-22T20:00 | CCI reversion · 1h | buy | ETH-USD | 6.57 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 23:45:05.000165+00:00 -> 2026-10-22 23:55:05.000165+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
