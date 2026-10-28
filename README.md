# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T06:30:05.000156+00:00 · 38748 ticks

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
| Copy: Insider buying | 2026-10-27 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 4881 decisions in 978 calls, $0.0682 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T06:30 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-28T06:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T06:30 | 0 / 3 / 2 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| VWAP reversion | META | 2.17 | +2.15% | 4 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP momentum · 1h | TSLA | 1.89 | +11.08% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.27 | 7.27 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.76 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.28 | 1.28 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.73 | -0.27 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.80 | 3.65 | -2.12 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.88 | -2.12 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.43 | -3.56 | 123 | 31.7 | -2.82 | -1.43 | -7.67 | 188 |
| 15 | Hold BTC | benchmark | 96.22 | -3.78 | 0 | — | 2.16 | 0.52 | -9.28 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.16 | -3.84 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.18 | 1.69 | -8.76 | 203 |
| 20 | Donchian 55/20 · 1h | breakout | 93.92 | -6.08 | 49 | 16.3 | -12.90 | -2.86 | -15.40 | 99 |
| 21 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 22 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -20.73 | -6.86 | -20.95 | 109 |
| 23 | Parabolic SAR · 1h | trend | 92.86 | -7.14 | 121 | 25.6 | -19.97 | -4.86 | -23.02 | 248 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.73 | -7.27 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 25 | ADX DI cross · 1h | trend | 92.24 | -7.76 | 120 | 18.3 | -13.55 | -2.91 | -15.49 | 270 |
| 26 | Daily: Momentum burst | daily | 92.06 | -7.94 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 91.98 | -8.02 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.46 | -8.54 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.38 | -8.62 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 91.19 | -8.81 | 52 | 23.1 | -4.48 | -1.16 | -12.21 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.32 | -9.68 | 113 | 26.5 | -12.16 | -2.51 | -16.10 | 106 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.32 | -6.60 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 89.12 | -10.88 | 109 | 26.6 | -11.23 | -2.17 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.97 | -12.03 | 205 | 47.3 | -20.52 | -3.80 | -22.35 | 388 |
| 37 | Keltner breakout · 1h | breakout | 87.46 | -12.54 | 74 | 23.0 | -18.83 | -3.60 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.09 | -12.91 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 86.04 | -13.96 | 114 | 14.0 | -23.66 | -4.78 | -26.59 | 232 |
| 41 | RSI momentum · 1h | momentum | 85.29 | -14.71 | 104 | 15.4 | -23.88 | -4.74 | -26.87 | 212 |
| 42 | Connors RSI(2) · 1h | reversion | 85.18 | -14.82 | 176 | 40.9 | -23.31 | -7.26 | -23.85 | 177 |
| 43 | EMA 20/50 cross · 1h | trend | 84.77 | -15.23 | 73 | 11.0 | -22.50 | -4.56 | -24.49 | 137 |
| 44 | MACD cross · 1h | trend | 84.54 | -15.46 | 245 | 22.4 | -27.54 | -5.33 | -29.94 | 476 |
| 45 | Ichimoku · 1h | trend | 84.24 | -15.76 | 68 | 11.8 | -19.70 | -3.99 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.89 | -16.11 | 101 | 14.9 | -28.18 | -5.34 | -31.19 | 205 |
| 47 | MFI reversion · 1h | reversion | 83.56 | -16.44 | 274 | 32.1 | -16.25 | -2.51 | -20.70 | 154 |
| 48 | CCI reversion · 1h | reversion | 82.71 | -17.29 | 230 | 45.2 | -24.11 | -3.44 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.36 | -17.64 | 99 | 20.2 | -22.87 | -4.31 | -26.02 | 219 |
| 50 | Williams %R · 1h | reversion | 82.26 | -17.74 | 232 | 47.0 | -34.64 | -5.85 | -35.74 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.51 | -18.49 | 111 | 15.3 | -23.72 | -5.05 | -25.67 | 229 |
| 52 | Agent (ML meta-label) | meta | 80.96 | -19.04 | 982 | 20.6 | -10.50 | -1.99 | -19.04 | 352 |
| 53 | Bollinger reversion · 1h | reversion | 80.92 | -19.08 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.88 | -19.12 | 209 | 17.7 | -31.33 | -6.42 | -33.82 | 295 |
| 55 | RSI(14) reversion · 1h | reversion | 80.53 | -19.47 | 107 | 27.1 | -15.19 | -2.80 | -24.48 | 187 |
| 56 | ROC + volume · 1h | momentum | 79.48 | -20.52 | 259 | 25.9 | -29.16 | -5.53 | -31.39 | 376 |
| 57 | Heikin-Ashi · 1h | trend | 78.53 | -21.46 | 302 | 22.5 | -42.60 | -9.29 | -43.96 | 663 |
| 58 | Candlestick reversal · 1h | reversion | 77.54 | -22.46 | 285 | 29.5 | -36.23 | -7.36 | -37.11 | 543 |
| 59 | VWAP momentum · 1h | momentum | 77.17 | -22.83 | 581 | 22.5 | -49.65 | -10.82 | -50.81 | 1238 |
| 60 | EMA 9/21 cross · 1h | trend | 77.00 | -23.00 | 176 | 10.8 | -29.55 | -6.22 | -31.61 | 337 |
| 61 | Three white soldiers | momentum | 76.69 | -23.31 | 327 | 19.0 | -45.02 | -21.09 | -45.18 | 610 |
| 62 | Max aggression: 1-day momentum | meta | 72.69 | -27.31 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 52.59 | -47.41 | 821 | 22.0 | -75.26 | -27.12 | -75.32 | 1572 |
| 64 | Volume breakout | breakout | 51.29 | -48.71 | 496 | 12.5 | -64.89 | -26.53 | -64.89 | 815 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -42.69 | -98.85 | 5114 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.20 | -23.43 | -79.62 | 1413 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.63 | -44.97 | -93.68 | 2529 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.11 | -29.96 | -89.28 | 1918 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -37.21 | -91.61 | 2338 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -32.05 | -90.48 | 2202 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.85 | -51.95 | -97.86 | 3502 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -58.61 | -96.19 | 3389 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.17 | -37.16 | -94.17 | 2477 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -34.26 | -82.54 | 1693 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -52.40 | -99.41 | 5750 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.20 | -44.07 | -93.20 | 2644 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -38.48 | -95.40 | 3388 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -75.71 | -99.79 | 6182 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.35 | -44.29 | -92.45 | 2311 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.83 | -65.16 | -97.83 | 3595 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -57.04 | -98.65 | 4786 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.12 | -29.90 | -69.37 | 1188 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -56.16 | -94.80 | 2778 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -39.28 | -84.86 | 1814 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.91 | -99.61 | 6291 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.61 | -88.27 | 2222 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.35 | -18.67 | -76.79 | 1678 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.50 | -36.32 | -90.50 | 2262 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -46.52 | -96.24 | 3809 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -48.47 | -90.05 | 2129 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.22 | -24.84 | -73.50 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.23 | -17.95 | -76.47 | 1575 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.36 | -96.54 | 4192 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -101.65 | -99.92 | 8293 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T06:20 | Three white soldiers | buy | SOL-USD | 19.19 | — | entry signal |
| 2026-10-28T06:15 | Three white soldiers | buy | DOGE-USD | 19.20 | — | entry signal |
| 2026-10-28T06:01 | Volume breakout · 1h | sell | ETH-USD | 22.47 | -0.11 | exit signal |
| 2026-10-28T06:01 | VWAP momentum · 1h | sell | ETH-USD | 4.03 | -0.03 | exit signal |
| 2026-10-28T06:01 | VWAP momentum · 1h | sell | BTC-USD | 4.04 | -0.02 | exit signal |
| 2026-10-28T06:01 | MACD cross · 1h | buy | DOGE-USD | 3.68 | — | entry |
| 2026-10-28T06:01 | MACD cross · 1h | sell | XRP-USD | 4.94 | 0.07 | exit signal |
| 2026-10-28T05:01 | VWAP momentum · 1h | sell | XRP-USD | 4.01 | -0.05 | exit signal |
| 2026-10-28T05:01 | Heikin-Ashi · 1h | sell | ETH-USD | 4.87 | -0.04 | exit signal |
| 2026-10-28T04:25 | ROC + volume | sell | DOGE-USD | 13.07 | -0.15 | stop-loss |
| 2026-10-28T04:10 | ROC + volume | sell | SOL-USD | 13.09 | -0.12 | stop-loss |
| 2026-10-28T04:00 | Heikin-Ashi · 1h | buy | ETH-USD | 4.91 | — | entry signal |
| 2026-10-28T03:55 | Volume breakout | sell | SOL-USD | 12.74 | -0.11 | exit signal |
| 2026-10-28T03:35 | Volume breakout | buy | SOL-USD | 12.85 | — | entry signal |
| 2026-10-28T03:35 | ROC + volume | buy | SOL-USD | 13.22 | — | entry signal |
| 2026-10-28T03:35 | ROC + volume | buy | DOGE-USD | 13.22 | — | entry signal |
| 2026-10-28T03:15 | ROC + volume | sell | ETH-USD | 13.20 | -0.09 | exit signal |
| 2026-10-28T02:45 | ROC + volume | sell | XRP-USD | 13.19 | -0.10 | stop-loss |
| 2026-10-28T02:45 | ROC + volume | sell | SOL-USD | 13.18 | -0.11 | exit signal |
| 2026-10-28T02:30 | Three white soldiers | sell | XRP-USD | 19.13 | -0.10 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | XRP-USD | 12.88 | -0.07 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | SOL-USD | 12.83 | -0.12 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | ETH-USD | 12.83 | -0.12 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | BTC-USD | 12.85 | -0.09 | exit signal |
| 2026-10-28T02:20 | Volume breakout | buy | SOL-USD | 12.94 | — | entry signal |
| 2026-10-28T02:20 | Volume breakout | buy | ETH-USD | 12.94 | — | entry signal |
| 2026-10-28T02:20 | ROC + volume | buy | SOL-USD | 13.30 | — | entry signal |
| 2026-10-28T02:15 | Volume breakout | buy | BTC-USD | 12.94 | — | entry signal |
| 2026-10-28T02:15 | ROC + volume | buy | ETH-USD | 13.29 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | XRP-USD | 4.06 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | ETH-USD | 4.06 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | BTC-USD | 4.06 | — | entry signal |
| 2026-10-28T01:45 | Volume breakout · 1h | buy | ETH-USD | 9.63 | — | rebalance up |
| 2026-10-28T01:45 | Three white soldiers | buy | XRP-USD | 19.23 | — | entry signal |
| 2026-10-28T01:45 | Volume breakout | buy | XRP-USD | 12.95 | — | entry signal |
| 2026-10-28T01:45 | ROC + volume | buy | XRP-USD | 13.29 | — | entry signal |
| 2026-10-28T01:15 | Volume breakout · 1h | buy | ETH-USD | 5.39 | — | rebalance up |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | XRP-USD | 6.47 | 0.09 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | ETH-USD | 5.45 | 0.02 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | BTC-USD | 2.95 | 0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 06:30:05.000156+00:00 -> 2026-10-28 06:40:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
