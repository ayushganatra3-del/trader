# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T10:25:05.000143+00:00 · 28261 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

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

Today: 7560 decisions in 1512 calls, $0.1056 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T10:25 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-10-19T10:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T10:25 | 3 / 2 / 0 | COIN 73% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.82 | 4.82 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.55 | -0.45 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Max aggression: 5-day momentum | meta | 98.74 | -1.26 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 12 | Donchian 55/20 · 1h | breakout | 98.69 | -1.31 | 36 | 16.7 | -10.51 | -1.68 | -22.12 | 111 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 16 | Hold BTC | benchmark | 97.89 | -2.11 | 0 | — | 27.81 | 3.28 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -4.46 | -2.28 | -5.67 | 262 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Three white soldiers · 1h | momentum | 95.81 | -4.19 | 12 | 0.0 | 0.35 | 0.23 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.56 | -4.44 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.79 | -5.21 | 82 | 19.5 | -12.06 | -2.33 | -13.34 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 0.52 | 0.23 | -9.46 | 94 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.18 | -6.82 | 97 | 21.6 | -11.05 | -1.74 | -22.75 | 273 |
| 27 | Daily: Momentum burst | daily | 93.00 | -7.00 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 29 | EMA 20/50 cross · 1h | trend | 92.13 | -7.87 | 55 | 14.5 | -18.74 | -3.22 | -21.34 | 130 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.45 | -5.81 | -13.80 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.77 | -9.23 | 77 | 16.9 | -17.17 | -2.98 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.66 | -9.34 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.72 | 1.15 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 89.76 | -10.24 | 52 | 15.4 | -18.42 | -3.46 | -18.45 | 116 |
| 37 | Triple EMA stack · 1h | trend | 89.60 | -10.40 | 81 | 16.0 | -26.35 | -4.14 | -30.49 | 233 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.53 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Supertrend · 1h | trend | 88.96 | -11.04 | 85 | 11.8 | -22.51 | -4.62 | -26.38 | 213 |
| 41 | Keltner breakout · 1h | breakout | 88.93 | -11.06 | 52 | 23.1 | -7.97 | -0.95 | -27.05 | 204 |
| 42 | Connors RSI(2) · 1h | reversion | 87.99 | -12.01 | 145 | 40.0 | -24.75 | -7.60 | -25.12 | 218 |
| 43 | MACD cross · 1h | trend | 87.67 | -12.33 | 181 | 21.5 | -23.74 | -4.12 | -30.63 | 459 |
| 44 | OBV trend · 1h | momentum | 87.36 | -12.64 | 170 | 18.2 | -20.12 | -2.57 | -33.85 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.31 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.10 | -14.90 | 82 | 15.9 | -23.88 | -4.74 | -24.31 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.03 | -14.97 | 209 | 31.1 | -21.06 | -3.24 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.51 | -15.49 | 79 | 17.7 | 1.20 | 0.35 | -21.74 | 216 |
| 51 | Z-score reversion · 1h | reversion | 82.79 | -17.21 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 52 | Three white soldiers | momentum | 82.70 | -17.30 | 224 | 18.3 | -47.38 | -19.13 | -47.40 | 605 |
| 53 | ROC + volume · 1h | momentum | 82.69 | -17.31 | 193 | 21.2 | -10.80 | -1.26 | -27.41 | 392 |
| 54 | Agent (ML meta-label) | meta | 82.21 | -17.79 | 655 | 18.0 | -16.31 | -2.69 | -17.76 | 378 |
| 55 | Heikin-Ashi · 1h | trend | 80.99 | -19.01 | 210 | 22.9 | -31.82 | -5.16 | -42.46 | 678 |
| 56 | EMA 9/21 cross · 1h | trend | 80.93 | -19.07 | 131 | 11.5 | -18.97 | -3.13 | -29.40 | 316 |
| 57 | Williams %R · 1h | reversion | 80.09 | -19.91 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 58 | VWAP momentum · 1h | momentum | 80.06 | -19.94 | 410 | 20.0 | -37.12 | -5.55 | -46.96 | 1252 |
| 59 | RSI(14) reversion · 1h | reversion | 80.02 | -19.98 | 74 | 20.3 | -14.58 | -2.58 | -22.27 | 167 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.30 | -2.63 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.34 | -6.53 | -37.22 | 543 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.50 | -77.84 | 1732 |
| 64 | Volume breakout | breakout | 61.88 | -38.12 | 349 | 12.9 | -63.01 | -18.05 | -64.06 | 883 |
| 65 | Squeeze breakout | breakout | 60.56 | -39.44 | 453 | 14.1 | -63.13 | -17.98 | -65.45 | 1215 |
| 66 | Donchian 55/20 | breakout | 59.27 | -40.73 | 463 | 17.9 | -68.68 | -14.41 | -72.80 | 1279 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.39 | -16.38 | -74.48 | 1626 |
| 68 | EMA 20/50 cross | trend | 57.38 | -42.62 | 482 | 18.7 | -75.82 | -14.64 | -80.16 | 1424 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.84 | -15.29 | -73.36 | 1514 |
| 70 | Keltner breakout | breakout | 51.60 | -48.40 | 651 | 15.8 | -82.71 | -26.44 | -83.30 | 1817 |
| 71 | AI bee: Boozy | ai | 50.99 | -49.01 | 345 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.92 | -98.65 | 5339 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -30.46 | -93.60 | 2587 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.16 | -19.99 | -87.78 | 1907 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.08 | -24.11 | -90.90 | 2352 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.21 | -26.07 | -91.21 | 2304 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -32.31 | -97.41 | 3522 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.76 | -37.07 | -96.76 | 3619 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -26.68 | -94.73 | 2582 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.94 | -23.33 | -82.82 | 1723 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.44 | -99.38 | 5807 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.28 | -25.66 | -91.83 | 2642 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.06 | -31.42 | -96.06 | 3516 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.48 | -99.74 | 6249 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.45 | -28.85 | -91.50 | 2355 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.56 | -39.10 | -97.56 | 3665 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.50 | -98.47 | 4756 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.67 | -33.21 | -93.73 | 2812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.18 | -99.53 | 6240 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.77 | -22.22 | -86.78 | 2169 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.13 | -27.15 | -88.17 | 2169 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.20 | -95.87 | 3804 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.94 | -32.26 | -89.23 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -33.81 | -95.79 | 4155 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.39 | -99.90 | 8343 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-19T09:00 | Heikin-Ashi · 1h | buy | ETH-USD | 6.73 | — | rebalance up |
| 2026-10-19T09:00 | Heikin-Ashi · 1h | sell | XRP-USD | 16.22 | -0.02 | exit signal |
| 2026-10-19T09:00 | Heikin-Ashi · 1h | sell | BTC-USD | 13.55 | 0.06 | exit signal |
| 2026-10-19T09:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 7.78 | — | entry signal |
| 2026-10-19T09:00 | EMA 20/50 cross · 1h | sell | BTC-USD | 4.67 | 0.00 | rebalance down |
| 2026-10-19T08:10 | Donchian 55/20 | sell | SOL-USD | 12.02 | 0.20 | exit signal |
| 2026-10-19T08:10 | Donchian 55/20 | sell | BTC-USD | 11.89 | 0.05 | exit signal |
| 2026-10-19T08:05 | Donchian 55/20 | sell | XRP-USD | 14.82 | -0.14 | stop-loss |
| 2026-10-19T08:05 | Donchian 55/20 | sell | ETH-USD | 11.89 | 0.07 | exit signal |
| 2026-10-19T08:00 | OBV trend · 1h | buy | XRP-USD | 6.60 | — | entry signal |
| 2026-10-19T08:00 | OBV trend · 1h | sell | BTC-USD | 4.39 | -0.01 | rebalance down |
| 2026-10-19T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 2.34 | — | entry signal |
| 2026-10-19T08:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 23.11 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 10:25:05.000143+00:00 -> 2026-10-19 10:35:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
