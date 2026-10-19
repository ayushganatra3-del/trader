# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T06:25:05.000189+00:00 · 28069 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.22 |
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

Today: 4680 decisions in 936 calls, $0.0654 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T06:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-19T06:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T06:25 | 1 / 4 / 0 | COIN 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | BITX | 2.25 | +2.55% | 6 |
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
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.94 | -0.06 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.56 | -0.44 | 64 | 39.1 | -11.25 | -3.24 | -13.79 | 140 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.85 | -1.15 | 36 | 16.7 | -5.47 | -0.62 | -22.12 | 110 |
| 12 | Max aggression: 5-day momentum | meta | 98.75 | -1.25 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.62 | -1.38 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.16 | -1.84 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 16 | Hold BTC | benchmark | 98.12 | -1.88 | 0 | — | 28.27 | 3.33 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -4.43 | -2.26 | -5.64 | 263 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.44 | -3.56 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Three white soldiers · 1h | momentum | 96.02 | -3.98 | 12 | 0.0 | 0.56 | 0.35 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.56 | -4.44 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.95 | -5.04 | 82 | 19.5 | -7.97 | -1.39 | -13.37 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.14 | 0.91 | -9.46 | 98 |
| 25 | Parabolic SAR · 1h | trend | 93.41 | -6.59 | 97 | 21.6 | -9.43 | -1.44 | -22.75 | 274 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 27 | Daily: Momentum burst | daily | 93.01 | -7.00 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.48 | -7.52 | 55 | 14.5 | -18.39 | -3.15 | -21.23 | 128 |
| 29 | Agent (aggressive) | meta | 92.16 | -7.84 | 38 | 31.6 | -5.81 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.96 | -5.32 | -13.12 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.92 | -9.08 | 77 | 16.9 | -17.02 | -2.95 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.66 | -9.34 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.34 | 1.11 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.01 | -9.99 | 52 | 15.4 | -18.19 | -3.41 | -18.38 | 116 |
| 37 | Triple EMA stack · 1h | trend | 89.91 | -10.10 | 81 | 16.0 | -19.34 | -2.44 | -33.23 | 231 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.53 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.26 | -10.74 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.16 | -10.84 | 52 | 23.1 | -8.05 | -0.97 | -27.05 | 204 |
| 41 | Supertrend · 1h | trend | 89.02 | -10.98 | 85 | 11.8 | -22.39 | -4.59 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.99 | -12.01 | 145 | 40.0 | -24.46 | -7.47 | -25.48 | 221 |
| 43 | MACD cross · 1h | trend | 87.75 | -12.25 | 181 | 21.5 | -23.67 | -4.11 | -30.63 | 460 |
| 44 | OBV trend · 1h | momentum | 87.58 | -12.43 | 170 | 18.2 | -17.29 | -2.04 | -33.85 | 319 |
| 45 | Stochastic reversion · 1h | reversion | 86.69 | -13.31 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.96 | -14.04 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.33 | -14.67 | 82 | 15.9 | -23.68 | -4.69 | -24.31 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.20 | -14.80 | 206 | 30.1 | -20.91 | -3.21 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.72 | -15.28 | 79 | 17.7 | 1.45 | 0.38 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 83.47 | -16.53 | 220 | 18.6 | -47.27 | -19.63 | -47.29 | 606 |
| 52 | Z-score reversion · 1h | reversion | 82.79 | -17.21 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.71 | -17.29 | 193 | 21.2 | -12.66 | -1.59 | -27.49 | 393 |
| 54 | Agent (ML meta-label) | meta | 82.21 | -17.79 | 655 | 18.0 | -19.90 | -3.56 | -21.37 | 377 |
| 55 | Heikin-Ashi · 1h | trend | 81.19 | -18.81 | 207 | 22.2 | -31.65 | -5.12 | -42.46 | 678 |
| 56 | EMA 9/21 cross · 1h | trend | 81.10 | -18.90 | 131 | 11.5 | -18.96 | -3.14 | -29.40 | 317 |
| 57 | VWAP momentum · 1h | momentum | 80.24 | -19.76 | 410 | 20.0 | -36.96 | -5.52 | -46.96 | 1252 |
| 58 | Williams %R · 1h | reversion | 80.09 | -19.91 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 59 | RSI(14) reversion · 1h | reversion | 80.02 | -19.98 | 74 | 20.3 | -14.43 | -2.55 | -22.27 | 168 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 150 | 32.0 | -30.68 | -6.34 | -33.03 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.04 | -20.96 | 161 | 38.5 | -20.28 | -2.63 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.12 | -23.88 | 205 | 25.4 | -35.83 | -6.46 | -36.73 | 546 |
| 63 | Volume breakout | breakout | 62.54 | -37.46 | 343 | 13.1 | -62.79 | -17.93 | -63.68 | 880 |
| 64 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.50 | -77.85 | 1733 |
| 65 | Squeeze breakout | breakout | 60.80 | -39.20 | 451 | 14.2 | -63.26 | -18.05 | -65.32 | 1218 |
| 66 | Donchian 55/20 | breakout | 59.80 | -40.20 | 457 | 17.5 | -68.45 | -14.24 | -72.80 | 1280 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.49 | -16.45 | -74.58 | 1629 |
| 68 | EMA 20/50 cross | trend | 57.63 | -42.37 | 480 | 18.3 | -76.10 | -14.71 | -80.16 | 1432 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.94 | -15.35 | -73.46 | 1518 |
| 70 | Keltner breakout | breakout | 52.26 | -47.74 | 645 | 16.0 | -82.60 | -26.37 | -83.11 | 1815 |
| 71 | AI bee: Boozy | ai | 51.18 | -48.82 | 343 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.93 | -98.66 | 5342 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.34 | -29.99 | -93.50 | 2585 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.08 | -19.81 | -87.78 | 1906 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.02 | -23.89 | -90.90 | 2354 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.01 | -25.69 | -91.01 | 2293 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -31.84 | -97.43 | 3521 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.69 | -36.61 | -96.69 | 3614 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -26.99 | -94.79 | 2595 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.97 | -23.29 | -82.70 | 1728 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.36 | -99.39 | 5813 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.21 | -25.59 | -91.70 | 2640 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.03 | -31.14 | -96.03 | 3509 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.10 | -99.74 | 6243 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.44 | -28.64 | -91.57 | 2357 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -38.84 | -97.52 | 3662 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.34 | -98.48 | 4758 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.64 | -33.17 | -93.65 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.03 | -99.53 | 6245 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.18 | -86.82 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.26 | -27.03 | -88.30 | 2171 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.11 | -95.87 | 3805 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.05 | -32.30 | -89.38 | 2109 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -33.58 | -95.80 | 4153 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.96 | -99.90 | 8336 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T06:25 | Three white soldiers | sell | ETH-USD | 20.77 | -0.13 | exit signal |
| 2026-10-19T06:20 | AI bee: Boozy | sell | ETH-USD | 14.13 | -0.07 | Jev: add (buy p=0.57) |
| 2026-10-19T06:04 | AI bee: Boozy | buy | ETH-USD | 14.19 | — | Jev: buy (buy p=0.73) |
| 2026-10-19T06:00 | OBV trend · 1h | buy | SOL-USD | 21.92 | — | entry signal |
| 2026-10-19T06:00 | Ichimoku · 1h | buy | BTC-USD | 22.53 | — | entry signal |
| 2026-10-19T06:00 | Triple EMA stack · 1h | buy | SOL-USD | 22.50 | — | entry signal |
| 2026-10-19T06:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 23.15 | — | entry signal |
| 2026-10-19T06:00 | Three white soldiers | buy | ETH-USD | 20.90 | — | entry signal |
| 2026-10-19T05:47 | AI bee: Boozy | sell | ETH-USD | 14.19 | -0.09 | Jev: buy |
| 2026-10-19T05:32 | AI bee: Boozy | buy | ETH-USD | 14.28 | — | Jev: buy (buy p=0.75) |
| 2026-10-19T05:05 | Volume breakout | sell | SOL-USD | 15.55 | -0.16 | stop-loss |
| 2026-10-19T05:05 | Volume breakout | sell | BTC-USD | 15.56 | -0.15 | stop-loss |
| 2026-10-19T05:05 | Squeeze breakout | sell | XRP-USD | 15.14 | -0.18 | stop-loss |
| 2026-10-19T05:05 | Squeeze breakout | sell | SOL-USD | 15.13 | -0.19 | stop-loss |
| 2026-10-19T05:05 | Squeeze breakout | sell | BTC-USD | 15.19 | -0.13 | stop-loss |
| 2026-10-19T05:05 | Keltner breakout | sell | SOL-USD | 12.99 | -0.14 | stop-loss |
| 2026-10-19T05:05 | Keltner breakout | sell | BTC-USD | 13.01 | -0.11 | stop-loss |
| 2026-10-19T05:05 | Donchian 55/20 | sell | XRP-USD | 11.91 | 0.09 | exit signal |
| 2026-10-19T05:03 | AI bee: Boozy | sell | ETH-USD | 14.28 | -0.13 | Jev: sell |
| 2026-10-19T05:00 | Heikin-Ashi · 1h | buy | XRP-USD | 10.71 | — | rebalance up |
| 2026-10-19T05:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 13.45 | -0.04 | exit signal |
| 2026-10-19T05:00 | Ichimoku · 1h | buy | XRP-USD | 22.57 | — | entry signal |
| 2026-10-19T05:00 | Ichimoku · 1h | buy | SOL-USD | 22.57 | — | entry signal |
| 2026-10-19T05:00 | Ichimoku · 1h | buy | ETH-USD | 22.57 | — | entry signal |
| 2026-10-19T04:50 | Volume breakout | buy | BTC-USD | 15.71 | — | entry signal |
| 2026-10-19T04:50 | Squeeze breakout | buy | XRP-USD | 15.32 | — | entry signal |
| 2026-10-19T04:50 | Squeeze breakout | buy | SOL-USD | 15.32 | — | entry signal |
| 2026-10-19T04:48 | AI bee: Boozy | buy | ETH-USD | 14.41 | — | Jev: buy (buy p=0.73) |
| 2026-10-19T04:45 | Volume breakout | buy | SOL-USD | 15.72 | — | entry signal |
| 2026-10-19T04:45 | Squeeze breakout | buy | BTC-USD | 15.32 | — | entry signal |
| 2026-10-19T04:45 | Keltner breakout | buy | SOL-USD | 13.13 | — | entry signal |
| 2026-10-19T04:45 | Keltner breakout | buy | BTC-USD | 13.13 | — | entry signal |
| 2026-10-19T04:30 | Donchian 55/20 | buy | ETH-USD | 3.00 | — | rebalance up |
| 2026-10-19T04:30 | Donchian 55/20 | buy | BTC-USD | 3.01 | — | rebalance up |
| 2026-10-19T04:30 | Donchian 55/20 | sell | DOGE-USD | 11.86 | 0.04 | exit signal |
| 2026-10-19T04:15 | MACD zero-line · 1h | buy | ETH-USD | 4.25 | — | rebalance up |
| 2026-10-19T04:15 | MACD zero-line · 1h | sell | XRP-USD | 4.25 | -0.03 | rebalance down |
| 2026-10-19T04:00 | VWAP momentum · 1h | sell | DOGE-USD | 2.34 | -0.02 | exit signal |
| 2026-10-19T04:00 | MACD zero-line · 1h | buy | ETH-USD | 8.63 | — | entry signal |
| 2026-10-19T04:00 | MACD zero-line · 1h | sell | SOL-USD | 4.32 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 06:25:05.000189+00:00 -> 2026-10-19 06:35:05.000189+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
