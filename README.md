# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T05:25:05.000124+00:00 · 28023 ticks

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

Today: 3990 decisions in 798 calls, $0.0557 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T05:25 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-19T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T05:25 | 2 / 2 / 1 | COIN 72% |  |

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
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.55 | -0.45 | 64 | 39.1 | -11.25 | -3.24 | -13.79 | 140 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.79 | -1.21 | 36 | 16.7 | -5.52 | -0.62 | -22.12 | 110 |
| 12 | Max aggression: 5-day momentum | meta | 98.74 | -1.26 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 16 | Hold BTC | benchmark | 97.97 | -2.03 | 0 | — | 27.97 | 3.30 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -4.43 | -2.26 | -5.64 | 263 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Three white soldiers · 1h | momentum | 95.87 | -4.13 | 12 | 0.0 | 0.41 | 0.27 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.56 | -4.44 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.84 | -5.16 | 82 | 19.5 | -8.12 | -1.42 | -13.37 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.14 | 0.91 | -9.46 | 98 |
| 25 | Parabolic SAR · 1h | trend | 93.27 | -6.73 | 97 | 21.6 | -9.58 | -1.47 | -22.75 | 274 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 27 | Daily: Momentum burst | daily | 93.00 | -7.00 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.53 | -7.47 | 55 | 14.5 | -18.34 | -3.14 | -21.23 | 127 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.81 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.96 | -5.32 | -13.12 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.82 | -9.18 | 77 | 16.9 | -17.15 | -2.97 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.66 | -9.34 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.33 | 1.11 | -14.21 | 265 |
| 36 | Triple EMA stack · 1h | trend | 89.95 | -10.05 | 81 | 16.0 | -19.28 | -2.43 | -33.23 | 230 |
| 37 | Ichimoku · 1h | trend | 89.95 | -10.05 | 52 | 15.4 | -18.24 | -3.43 | -18.38 | 115 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.53 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.05 | -10.95 | 52 | 23.1 | -8.06 | -0.97 | -27.05 | 204 |
| 41 | Supertrend · 1h | trend | 88.96 | -11.04 | 85 | 11.8 | -22.49 | -4.62 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.99 | -12.02 | 145 | 40.0 | -24.46 | -7.47 | -25.48 | 221 |
| 43 | MACD cross · 1h | trend | 87.68 | -12.32 | 181 | 21.5 | -23.72 | -4.12 | -30.63 | 459 |
| 44 | OBV trend · 1h | momentum | 87.62 | -12.38 | 170 | 18.2 | -17.26 | -2.04 | -33.85 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.32 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.13 | -14.87 | 82 | 15.9 | -23.85 | -4.73 | -24.31 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.00 | -15.00 | 206 | 30.1 | -21.08 | -3.25 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.57 | -15.43 | 79 | 17.7 | 1.27 | 0.36 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 83.60 | -16.40 | 219 | 18.7 | -47.19 | -19.56 | -47.27 | 605 |
| 52 | Z-score reversion · 1h | reversion | 82.79 | -17.21 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.65 | -17.35 | 193 | 21.2 | -12.81 | -1.62 | -27.49 | 394 |
| 54 | Agent (ML meta-label) | meta | 82.21 | -17.80 | 655 | 18.0 | -19.86 | -3.67 | -21.33 | 376 |
| 55 | Heikin-Ashi · 1h | trend | 81.08 | -18.92 | 207 | 22.2 | -31.75 | -5.14 | -42.46 | 678 |
| 56 | EMA 9/21 cross · 1h | trend | 80.96 | -19.04 | 131 | 11.5 | -19.10 | -3.17 | -29.40 | 317 |
| 57 | VWAP momentum · 1h | momentum | 80.13 | -19.88 | 410 | 20.0 | -37.06 | -5.55 | -46.96 | 1252 |
| 58 | Williams %R · 1h | reversion | 80.09 | -19.91 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 59 | RSI(14) reversion · 1h | reversion | 80.02 | -19.98 | 74 | 20.3 | -14.57 | -2.58 | -22.27 | 167 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 150 | 32.0 | -30.68 | -6.34 | -33.03 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.33 | -2.64 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.84 | -6.46 | -36.73 | 542 |
| 63 | Volume breakout | breakout | 62.54 | -37.46 | 343 | 13.1 | -62.79 | -17.93 | -63.68 | 880 |
| 64 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.50 | -77.85 | 1733 |
| 65 | Squeeze breakout | breakout | 60.80 | -39.20 | 451 | 14.2 | -63.25 | -18.05 | -65.32 | 1217 |
| 66 | Donchian 55/20 | breakout | 59.72 | -40.28 | 457 | 17.5 | -68.48 | -14.26 | -72.80 | 1280 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.50 | -16.46 | -74.59 | 1630 |
| 68 | EMA 20/50 cross | trend | 57.50 | -42.50 | 480 | 18.3 | -76.18 | -14.76 | -80.16 | 1433 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.77 | -15.27 | -73.29 | 1513 |
| 70 | Keltner breakout | breakout | 52.26 | -47.74 | 645 | 16.0 | -82.66 | -26.43 | -83.11 | 1817 |
| 71 | AI bee: Boozy | ai | 51.34 | -48.66 | 341 | 5.9 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.91 | -98.65 | 5336 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.32 | -29.95 | -93.50 | 2583 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.12 | -19.85 | -87.78 | 1907 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.01 | -23.88 | -90.90 | 2353 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.00 | -25.67 | -91.01 | 2291 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -31.86 | -97.45 | 3523 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -36.38 | -96.68 | 3610 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -26.96 | -94.81 | 2596 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.93 | -23.24 | -82.66 | 1725 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.38 | -99.39 | 5814 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.22 | -25.59 | -91.69 | 2640 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.03 | -31.22 | -96.03 | 3512 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.02 | -99.74 | 6240 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.46 | -28.63 | -91.60 | 2358 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -38.80 | -97.52 | 3660 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.34 | -98.48 | 4758 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.64 | -33.17 | -93.65 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.03 | -99.53 | 6245 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.79 | -22.21 | -86.82 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.26 | -27.03 | -88.30 | 2171 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.14 | -95.89 | 3807 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.04 | -32.35 | -89.36 | 2108 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -33.56 | -95.81 | 4153 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.77 | -99.90 | 8331 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-19T04:00 | MACD zero-line · 1h | sell | BTC-USD | 4.32 | -0.01 | rebalance down |
| 2026-10-19T03:50 | ROC + volume | sell | SOL-USD | 15.62 | -0.02 | target is flat |
| 2026-10-19T03:45 | Squeeze breakout | sell | BTC-USD | 15.26 | -0.14 | stop-loss |
| 2026-10-19T03:45 | Keltner breakout | sell | BTC-USD | 13.15 | -0.12 | stop-loss |
| 2026-10-19T03:25 | Keltner breakout | sell | DOGE-USD | 13.13 | -0.14 | target is flat |
| 2026-10-19T03:20 | Three white soldiers | sell | BTC-USD | 20.84 | -0.12 | exit signal |
| 2026-10-19T03:20 | Squeeze breakout | sell | XRP-USD | 15.25 | -0.15 | exit signal |
| 2026-10-19T03:20 | Keltner breakout | sell | SOL-USD | 13.12 | -0.14 | stop-loss |
| 2026-10-19T03:07 | AI bee: Boozy | sell | ETH-USD | 14.41 | -0.16 | Jev: sell (sell p=0.51) after 17 min |
| 2026-10-19T03:05 | Three white soldiers | sell | ETH-USD | 20.82 | -0.14 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 05:25:05.000124+00:00 -> 2026-10-19 05:35:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
