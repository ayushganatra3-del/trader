# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T10:56:05.000154+00:00 · 28289 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.00 (-8.00%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.22 |
| SQQQ | 19.18 | +0.81 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, FLSC 12%, REF 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7980 decisions in 1596 calls, $0.1115 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T10:56 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-19T10:56 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T10:56 | 2 / 3 / 0 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | BITX | 2.21 | +2.15% | 7 |
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.06 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.44 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.00 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.85 | 4.85 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.96 | -0.04 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.58 | -0.42 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Max aggression: 5-day momentum | meta | 98.77 | -1.23 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 12 | Donchian 55/20 · 1h | breakout | 98.66 | -1.34 | 36 | 16.7 | -10.57 | -1.69 | -22.12 | 111 |
| 13 | Hold SPY | benchmark | 98.64 | -1.36 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 15 | Copy: Insider buying | copy | 98.18 | -1.82 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 16 | Hold BTC | benchmark | 97.85 | -2.15 | 0 | — | 27.76 | 3.28 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -4.46 | -2.28 | -5.67 | 262 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.46 | -3.54 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.44 | -3.56 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Three white soldiers · 1h | momentum | 95.73 | -4.27 | 12 | 0.0 | 0.25 | 0.18 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.59 | -4.41 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.73 | -5.27 | 82 | 19.5 | -12.15 | -2.35 | -13.34 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -3.03 | -0.67 | -9.46 | 93 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.09 | -6.91 | 97 | 21.6 | -11.18 | -1.77 | -22.75 | 273 |
| 27 | Daily: Momentum burst | daily | 93.02 | -6.98 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | Agent (aggressive) | meta | 92.17 | -7.83 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 29 | EMA 20/50 cross · 1h | trend | 92.06 | -7.94 | 55 | 14.5 | -18.82 | -3.23 | -21.70 | 130 |
| 30 | Agent | meta | 92.00 | -8.00 | 77 | 39.0 | -9.45 | -5.81 | -13.80 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.71 | -9.29 | 77 | 16.9 | -17.26 | -3.00 | -27.69 | 221 |
| 34 | Daily: Bullish score | daily | 90.68 | -9.32 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.74 | 1.15 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 89.68 | -10.32 | 52 | 15.4 | -18.51 | -3.48 | -18.92 | 116 |
| 37 | Triple EMA stack · 1h | trend | 89.55 | -10.45 | 81 | 16.0 | -26.41 | -4.15 | -30.81 | 233 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.48 | -10.52 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.28 | -10.72 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Supertrend · 1h | trend | 88.95 | -11.05 | 85 | 11.8 | -14.66 | -2.31 | -28.83 | 215 |
| 41 | Keltner breakout · 1h | breakout | 88.41 | -11.59 | 55 | 21.8 | -8.45 | -1.02 | -27.05 | 204 |
| 42 | Connors RSI(2) · 1h | reversion | 88.01 | -11.99 | 145 | 40.0 | -24.75 | -7.60 | -25.12 | 218 |
| 43 | MACD cross · 1h | trend | 87.63 | -12.37 | 181 | 21.5 | -23.81 | -4.14 | -30.63 | 459 |
| 44 | OBV trend · 1h | momentum | 87.33 | -12.67 | 170 | 18.2 | -20.18 | -2.58 | -33.88 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.70 | -13.30 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.98 | -14.02 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MFI reversion · 1h | reversion | 85.03 | -14.97 | 209 | 31.1 | -21.06 | -3.24 | -23.01 | 148 |
| 49 | MACD zero-line · 1h | trend | 84.99 | -15.02 | 82 | 15.9 | -24.00 | -4.77 | -24.71 | 220 |
| 50 | Donchian 20/10 · 1h | breakout | 84.42 | -15.58 | 79 | 17.7 | 1.06 | 0.33 | -22.07 | 216 |
| 51 | Z-score reversion · 1h | reversion | 82.81 | -17.19 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 52 | Three white soldiers | momentum | 82.70 | -17.30 | 224 | 18.3 | -47.38 | -19.13 | -47.40 | 605 |
| 53 | ROC + volume · 1h | momentum | 82.69 | -17.31 | 193 | 21.2 | -10.82 | -1.26 | -27.41 | 392 |
| 54 | Agent (ML meta-label) | meta | 82.23 | -17.77 | 655 | 18.0 | -20.23 | -3.48 | -21.62 | 387 |
| 55 | Heikin-Ashi · 1h | trend | 81.00 | -19.00 | 210 | 22.9 | -31.83 | -5.16 | -42.46 | 678 |
| 56 | EMA 9/21 cross · 1h | trend | 80.85 | -19.15 | 131 | 11.5 | -19.07 | -3.15 | -29.65 | 316 |
| 57 | Williams %R · 1h | reversion | 80.11 | -19.89 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 58 | RSI(14) reversion · 1h | reversion | 80.04 | -19.96 | 74 | 20.3 | -14.58 | -2.58 | -22.27 | 167 |
| 59 | VWAP momentum · 1h | momentum | 80.01 | -19.99 | 410 | 20.0 | -37.19 | -5.56 | -46.96 | 1252 |
| 60 | Bollinger reversion · 1h | reversion | 79.90 | -20.10 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.06 | -20.95 | 161 | 38.5 | -20.31 | -2.64 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.13 | -23.86 | 205 | 25.4 | -36.34 | -6.53 | -37.22 | 543 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.67 | -17.46 | -77.84 | 1731 |
| 64 | Volume breakout | breakout | 61.88 | -38.12 | 349 | 12.9 | -63.01 | -18.05 | -64.06 | 883 |
| 65 | Squeeze breakout | breakout | 60.56 | -39.44 | 453 | 14.1 | -63.12 | -17.97 | -65.45 | 1214 |
| 66 | Donchian 55/20 | breakout | 59.27 | -40.73 | 463 | 17.9 | -68.68 | -14.41 | -72.80 | 1279 |
| 67 | RSI(14) reversion | reversion | 58.52 | -41.48 | 687 | 25.0 | -74.46 | -16.43 | -74.54 | 1632 |
| 68 | EMA 20/50 cross | trend | 57.14 | -42.86 | 485 | 19.0 | -75.89 | -14.69 | -80.16 | 1423 |
| 69 | VWAP reversion | reversion | 53.43 | -46.57 | 720 | 23.9 | -72.94 | -15.35 | -73.44 | 1518 |
| 70 | Keltner breakout | breakout | 51.60 | -48.40 | 651 | 15.8 | -82.68 | -26.39 | -83.30 | 1816 |
| 71 | AI bee: Boozy | ai | 50.99 | -49.01 | 345 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.96 | -98.65 | 5343 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -30.47 | -93.60 | 2587 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.16 | -19.99 | -87.78 | 1907 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.08 | -24.11 | -90.90 | 2352 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.21 | -26.08 | -91.21 | 2304 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -32.31 | -97.41 | 3522 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -36.95 | -96.73 | 3614 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.49 | -26.63 | -94.85 | 2593 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.94 | -23.33 | -82.82 | 1722 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.54 | -99.38 | 5812 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.28 | -25.66 | -91.83 | 2642 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.09 | -31.50 | -96.09 | 3519 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.42 | -99.74 | 6247 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.43 | -28.82 | -91.49 | 2354 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.56 | -39.10 | -97.56 | 3665 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.60 | -98.48 | 4761 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.67 | -33.21 | -93.73 | 2812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.22 | -99.53 | 6245 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.82 | -22.30 | -86.82 | 2174 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.15 | -27.21 | -88.20 | 2172 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.27 | -95.89 | 3809 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.89 | -32.19 | -89.18 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.83 | -34.06 | -95.83 | 4157 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.34 | -99.90 | 8342 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T10:40 | VWAP reversion | buy | XRP-USD | 13.37 | — | entry signal |
| 2026-10-19T10:40 | VWAP reversion | buy | DOGE-USD | 13.37 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | XRP-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | SOL-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | ETH-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | DOGE-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | BTC-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | EMA 20/50 cross | sell | ETH-USD | 11.47 | 0.10 | exit signal |
| 2026-10-19T10:35 | Keltner breakout · 1h | sell | XRP-USD | 22.02 | -0.25 | stop-loss |
| 2026-10-19T10:35 | Keltner breakout · 1h | sell | SOL-USD | 21.24 | -0.34 | stop-loss |
| 2026-10-19T10:30 | Keltner breakout · 1h | sell | BTC-USD | 22.15 | -0.10 | stop-loss |
| 2026-10-19T10:30 | EMA 20/50 cross | sell | DOGE-USD | 14.24 | -0.05 | exit signal |
| 2026-10-19T10:30 | EMA 20/50 cross | sell | BTC-USD | 14.29 | 0.01 | exit signal |
| 2026-10-19T10:25 | EMA 20/50 cross | sell | XRP-USD | 14.31 | 0.06 | exit signal |
| 2026-10-19T10:20 | EMA 20/50 cross | buy | XRP-USD | 2.88 | — | rebalance up |
| 2026-10-19T10:20 | EMA 20/50 cross | buy | DOGE-USD | 2.93 | — | rebalance up |
| 2026-10-19T10:20 | EMA 20/50 cross | buy | BTC-USD | 2.91 | — | rebalance up |
| 2026-10-19T10:20 | EMA 20/50 cross | sell | SOL-USD | 11.54 | 0.17 | exit signal |
| 2026-10-19T10:02 | Triple EMA stack · 1h | buy | XRP-USD | 4.48 | — | rebalance up |
| 2026-10-19T10:02 | Triple EMA stack · 1h | sell | BTC-USD | 4.48 | -0.02 | rebalance down |
| 2026-10-19T10:00 | MFI reversion · 1h | sell | XRP-USD | 21.49 | 0.52 | exit signal |
| 2026-10-19T10:00 | MFI reversion · 1h | sell | DOGE-USD | 21.33 | 0.44 | exit signal |
| 2026-10-19T10:00 | Heikin-Ashi · 1h | sell | SOL-USD | 20.19 | 0.03 | exit signal |
| 2026-10-19T10:00 | Triple EMA stack · 1h | buy | XRP-USD | 2.12 | — | entry signal |
| 2026-10-19T10:00 | Triple EMA stack · 1h | buy | ETH-USD | 17.98 | — | entry signal |
| 2026-10-19T10:00 | Three white soldiers | sell | BTC-USD | 20.56 | -0.19 | stop-loss |
| 2026-10-19T10:00 | Keltner breakout | sell | ETH-USD | 12.81 | -0.12 | stop-loss |
| 2026-10-19T10:00 | Donchian 55/20 | sell | ETH-USD | 14.72 | -0.14 | stop-loss |
| 2026-10-19T09:53 | AI bee: Boozy | sell | BTC-USD | 13.94 | -0.10 | Jev: buy |
| 2026-10-19T09:45 | Three white soldiers | sell | SOL-USD | 20.59 | -0.18 | exit signal |
| 2026-10-19T09:40 | Keltner breakout | buy | ETH-USD | 12.93 | — | entry signal |
| 2026-10-19T09:40 | Donchian 55/20 | buy | ETH-USD | 14.85 | — | entry signal |
| 2026-10-19T09:37 | AI bee: Boozy | buy | BTC-USD | 14.04 | — | Jev: buy (buy p=0.73) |
| 2026-10-19T09:35 | Three white soldiers | buy | BTC-USD | 20.75 | — | entry signal |
| 2026-10-19T09:33 | AI bee: Boozy | sell | ETH-USD | 14.04 | -0.09 | Jev: add (buy p=0.52) |
| 2026-10-19T09:25 | Three white soldiers | buy | SOL-USD | 20.77 | — | entry signal |
| 2026-10-19T09:18 | AI bee: Boozy | buy | ETH-USD | 14.13 | — | Jev: buy (buy p=0.74) |
| 2026-10-19T09:00 | OBV trend · 1h | buy | ETH-USD | 7.25 | — | entry signal |
| 2026-10-19T09:00 | OBV trend · 1h | sell | SOL-USD | 7.25 | -0.03 | rebalance down |
| 2026-10-19T09:00 | Heikin-Ashi · 1h | buy | SOL-USD | 6.66 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 10:56:05.000154+00:00 -> 2026-10-19 11:06:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
