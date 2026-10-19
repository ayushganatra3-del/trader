# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T12:25:05.000133+00:00 · 28368 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.98 (-8.02%)

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
| Copy: Insider buying | 2026-10-19 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, APLD 12%, FLSC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 9165 decisions in 1833 calls, $0.1280 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T12:25 | 4 / 1 / 0 | cash |  |
| Breezy | 2026-10-19T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T12:25 | 3 / 2 / 0 | BTC-USD 27% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.80 | 4.80 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 12 | Donchian 55/20 · 1h | breakout | 98.71 | -1.29 | 36 | 16.7 | -10.49 | -1.67 | -22.12 | 111 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.14 | -1.86 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 16 | Hold BTC | benchmark | 97.91 | -2.09 | 0 | — | 28.45 | 3.35 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -4.46 | -2.28 | -5.67 | 262 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.42 | -3.58 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.46 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -0.02 | 0.04 | -5.48 | 33 |
| 23 | ADX DI cross · 1h | trend | 94.72 | -5.28 | 83 | 19.3 | -12.13 | -2.35 | -13.37 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 1.53 | 0.45 | -9.46 | 95 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.98 | -7.02 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 100 | 23.0 | -11.96 | -1.97 | -22.78 | 272 |
| 28 | EMA 20/50 cross · 1h | trend | 92.18 | -7.83 | 55 | 14.5 | -18.72 | -3.21 | -21.74 | 130 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.98 | -8.02 | 77 | 39.0 | -9.45 | -5.81 | -13.80 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.83 | -9.17 | 77 | 16.9 | -17.12 | -2.97 | -27.72 | 221 |
| 34 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.74 | 1.15 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 89.78 | -10.22 | 52 | 15.4 | -18.39 | -3.46 | -18.98 | 116 |
| 37 | Triple EMA stack · 1h | trend | 89.59 | -10.41 | 81 | 16.0 | -20.91 | -2.71 | -33.60 | 233 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.24 | -10.76 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Supertrend · 1h | trend | 88.98 | -11.02 | 85 | 11.8 | -22.47 | -4.61 | -26.38 | 213 |
| 41 | Keltner breakout · 1h | breakout | 88.40 | -11.60 | 55 | 21.8 | -8.53 | -1.03 | -27.05 | 204 |
| 42 | Connors RSI(2) · 1h | reversion | 87.94 | -12.06 | 145 | 40.0 | -24.77 | -7.61 | -25.12 | 219 |
| 43 | MACD cross · 1h | trend | 87.70 | -12.29 | 181 | 21.5 | -23.76 | -4.13 | -30.63 | 460 |
| 44 | OBV trend · 1h | momentum | 87.30 | -12.70 | 171 | 18.1 | -20.36 | -2.62 | -33.91 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.32 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.94 | -14.06 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.18 | -14.82 | 82 | 15.9 | -23.82 | -4.72 | -24.76 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.03 | -14.97 | 209 | 31.1 | -21.06 | -3.24 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.60 | -15.40 | 79 | 17.7 | 1.32 | 0.36 | -22.10 | 216 |
| 51 | Z-score reversion · 1h | reversion | 82.78 | -17.22 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 52 | Three white soldiers | momentum | 82.63 | -17.37 | 224 | 18.3 | -47.43 | -19.14 | -47.45 | 606 |
| 53 | ROC + volume · 1h | momentum | 82.60 | -17.40 | 193 | 21.2 | -10.87 | -1.27 | -27.70 | 394 |
| 54 | Agent (ML meta-label) | meta | 82.20 | -17.80 | 655 | 18.0 | -18.18 | -2.62 | -20.89 | 380 |
| 55 | EMA 9/21 cross · 1h | trend | 80.98 | -19.02 | 131 | 11.5 | -23.71 | -4.63 | -27.90 | 315 |
| 56 | Heikin-Ashi · 1h | trend | 80.91 | -19.09 | 211 | 22.7 | -31.89 | -5.18 | -42.46 | 678 |
| 57 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.32 | -5.76 | -36.90 | 532 |
| 58 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.58 | -2.58 | -22.27 | 167 |
| 59 | Bollinger reversion · 1h | reversion | 79.87 | -20.13 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 60 | VWAP momentum · 1h | momentum | 79.79 | -20.21 | 415 | 20.5 | -37.10 | -5.51 | -46.96 | 1250 |
| 61 | CCI reversion · 1h | reversion | 79.02 | -20.98 | 161 | 38.5 | -20.33 | -2.64 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.10 | -23.90 | 205 | 25.4 | -36.29 | -6.52 | -37.22 | 545 |
| 63 | ROC + volume | momentum | 62.46 | -37.54 | 567 | 22.0 | -75.69 | -17.47 | -77.84 | 1732 |
| 64 | Volume breakout | breakout | 61.85 | -38.15 | 349 | 12.9 | -63.01 | -18.05 | -64.09 | 884 |
| 65 | Squeeze breakout | breakout | 60.56 | -39.44 | 453 | 14.1 | -63.13 | -17.98 | -65.45 | 1215 |
| 66 | Donchian 55/20 | breakout | 59.27 | -40.73 | 463 | 17.9 | -68.62 | -14.38 | -72.80 | 1278 |
| 67 | RSI(14) reversion | reversion | 58.26 | -41.74 | 692 | 24.9 | -74.56 | -16.51 | -74.69 | 1633 |
| 68 | EMA 20/50 cross | trend | 57.14 | -42.86 | 485 | 19.0 | -75.89 | -14.69 | -80.16 | 1423 |
| 69 | VWAP reversion | reversion | 53.38 | -46.62 | 723 | 24.1 | -72.89 | -15.32 | -73.36 | 1517 |
| 70 | Keltner breakout | breakout | 51.58 | -48.42 | 651 | 15.8 | -82.69 | -26.40 | -83.31 | 1817 |
| 71 | AI bee: Boozy | ai | 50.94 | -49.06 | 345 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -30.06 | -98.67 | 5353 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -30.46 | -93.60 | 2586 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.17 | -20.00 | -87.78 | 1907 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.09 | -24.14 | -90.90 | 2353 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.19 | -26.02 | -91.19 | 2303 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -32.32 | -97.41 | 3523 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -36.92 | -96.73 | 3613 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -26.52 | -94.72 | 2584 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.94 | -23.33 | -82.82 | 1722 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.76 | -99.39 | 5812 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.30 | -25.67 | -91.84 | 2646 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.10 | -31.52 | -96.10 | 3521 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.35 | -99.74 | 6247 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.42 | -28.83 | -91.47 | 2352 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.55 | -39.01 | -97.55 | 3662 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.79 | -98.48 | 4758 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.68 | -33.22 | -93.74 | 2815 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.23 | -99.53 | 6243 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.92 | -22.47 | -86.98 | 2179 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.18 | -27.34 | -88.23 | 2170 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.38 | -95.88 | 3803 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.90 | -32.30 | -89.16 | 2104 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.77 | -33.87 | -95.78 | 4151 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.38 | -99.90 | 8348 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T12:20 | ROC + volume | buy | XRP-USD | 15.63 | — | entry signal |
| 2026-10-19T12:17 | AI bee: Boozy | buy | BTC-USD | 13.94 | — | Jev: buy (buy p=0.73) |
| 2026-10-19T12:15 | VWAP reversion | sell | XRP-USD | 13.34 | 0.03 | exit signal |
| 2026-10-19T12:15 | VWAP reversion | sell | DOGE-USD | 13.39 | 0.02 | exit signal |
| 2026-10-19T12:15 | RSI(14) reversion | sell | SOL-USD | 11.69 | -0.04 | exit signal |
| 2026-10-19T12:15 | RSI(14) reversion | sell | BTC-USD | 11.67 | -0.06 | exit signal |
| 2026-10-19T12:15 | Three white soldiers | buy | DOGE-USD | 20.68 | — | entry signal |
| 2026-10-19T12:10 | RSI(14) reversion | sell | DOGE-USD | 11.72 | -0.01 | exit signal |
| 2026-10-19T12:10 | Volume breakout | buy | DOGE-USD | 15.47 | — | entry signal |
| 2026-10-19T12:10 | Keltner breakout | buy | DOGE-USD | 12.90 | — | entry signal |
| 2026-10-19T12:05 | OBV trend · 1h | buy | ETH-USD | 6.52 | — | rebalance up |
| 2026-10-19T12:05 | OBV trend · 1h | sell | XRP-USD | 6.52 | -0.08 | target is flat |
| 2026-10-19T12:00 | Parabolic SAR · 1h | sell | XRP-USD | 22.42 | -0.10 | exit signal |
| 2026-10-19T12:00 | Parabolic SAR · 1h | sell | SOL-USD | 18.59 | 0.03 | exit signal |
| 2026-10-19T11:40 | VWAP reversion | buy | XRP-USD | 13.31 | — | entry signal |
| 2026-10-19T11:40 | RSI(14) reversion | buy | ETH-USD | 14.54 | — | entry signal |
| 2026-10-19T11:35 | VWAP reversion | sell | XRP-USD | 13.22 | -0.15 | stop-loss |
| 2026-10-19T11:35 | RSI(14) reversion | sell | XRP-USD | 11.59 | -0.13 | stop-loss |
| 2026-10-19T11:35 | RSI(14) reversion | sell | ETH-USD | 11.59 | -0.14 | stop-loss |
| 2026-10-19T11:00 | Connors RSI(2) · 1h | buy | BTC-USD | 21.93 | — | entry signal |
| 2026-10-19T11:00 | Three white soldiers · 1h | sell | XRP-USD | 23.69 | -0.17 | exit signal |
| 2026-10-19T11:00 | Three white soldiers · 1h | sell | SOL-USD | 23.96 | 0.12 | exit signal |
| 2026-10-19T11:00 | Three white soldiers · 1h | sell | ETH-USD | 24.01 | 0.17 | exit signal |
| 2026-10-19T11:00 | ROC + volume · 1h | buy | SOL-USD | 20.06 | — | entry signal |
| 2026-10-19T11:00 | ROC + volume · 1h | buy | BTC-USD | 20.67 | — | entry signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | XRP-USD | 15.89 | -0.08 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | SOL-USD | 13.36 | 0.07 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | ETH-USD | 13.39 | 0.09 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | DOGE-USD | 2.31 | -0.03 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | BTC-USD | 13.33 | 0.03 | exit signal |
| 2026-10-19T11:00 | Heikin-Ashi · 1h | sell | ETH-USD | 20.16 | -0.06 | exit signal |
| 2026-10-19T11:00 | ADX DI cross · 1h | buy | ETH-USD | 10.75 | — | entry |
| 2026-10-19T11:00 | ADX DI cross · 1h | sell | DOGE-USD | 10.75 | -0.08 | exit signal |
| 2026-10-19T11:00 | Parabolic SAR · 1h | buy | DOGE-USD | 14.02 | — | rebalance up |
| 2026-10-19T11:00 | Parabolic SAR · 1h | sell | BTC-USD | 18.60 | 0.04 | exit signal |
| 2026-10-19T10:40 | VWAP reversion | buy | XRP-USD | 13.37 | — | entry signal |
| 2026-10-19T10:40 | VWAP reversion | buy | DOGE-USD | 13.37 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | XRP-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | SOL-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | ETH-USD | 11.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 12:25:05.000133+00:00 -> 2026-10-19 12:35:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
