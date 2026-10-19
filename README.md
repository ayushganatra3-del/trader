# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T07:25:05.000172+00:00 · 28114 ticks

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

Today: 5355 decisions in 1071 calls, $0.0748 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T07:25 | 3 / 2 / 0 | XRP-USD 19% |  |
| Breezy | 2026-10-19T07:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T07:25 | 5 / 0 / 0 | COIN 72% |  |

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
| 10 | Donchian 55/20 · 1h | breakout | 98.96 | -1.04 | 36 | 16.7 | -5.50 | -0.62 | -22.12 | 110 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 12 | Max aggression: 5-day momentum | meta | 98.74 | -1.26 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Hold BTC | benchmark | 98.28 | -1.72 | 0 | — | 28.64 | 3.36 | -8.68 | 1 |
| 16 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -4.43 | -2.26 | -5.64 | 263 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Three white soldiers · 1h | momentum | 96.19 | -3.81 | 12 | 0.0 | 0.74 | 0.44 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.56 | -4.44 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 95.08 | -4.92 | 82 | 19.5 | -11.75 | -2.26 | -13.34 | 256 |
| 24 | Parabolic SAR · 1h | trend | 93.59 | -6.41 | 97 | 21.6 | -9.24 | -1.40 | -22.75 | 274 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.14 | 0.91 | -9.46 | 98 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 27 | Daily: Momentum burst | daily | 93.00 | -7.00 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.58 | -7.42 | 55 | 14.5 | -18.30 | -3.13 | -21.23 | 128 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.81 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.96 | -5.32 | -13.12 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.05 | -8.95 | 77 | 16.9 | -16.88 | -2.92 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.66 | -9.34 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.33 | 1.11 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.20 | -9.79 | 52 | 15.4 | -18.01 | -3.37 | -18.38 | 116 |
| 37 | Triple EMA stack · 1h | trend | 90.00 | -10.00 | 81 | 16.0 | -19.38 | -2.45 | -33.23 | 231 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.53 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Keltner breakout · 1h | breakout | 89.33 | -10.67 | 52 | 23.1 | -7.89 | -0.95 | -27.05 | 204 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Supertrend · 1h | trend | 89.06 | -10.94 | 85 | 11.8 | -22.27 | -4.56 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.99 | -12.01 | 145 | 40.0 | -24.46 | -7.47 | -25.48 | 221 |
| 43 | MACD cross · 1h | trend | 87.81 | -12.19 | 181 | 21.5 | -23.56 | -4.09 | -30.63 | 460 |
| 44 | OBV trend · 1h | momentum | 87.67 | -12.33 | 170 | 18.2 | -18.99 | -2.38 | -33.85 | 319 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.31 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.53 | -14.47 | 82 | 15.9 | -23.51 | -4.65 | -24.31 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.26 | -14.74 | 207 | 30.4 | -20.85 | -3.20 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.89 | -15.11 | 79 | 17.7 | 1.66 | 0.40 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 83.47 | -16.53 | 220 | 18.6 | -47.27 | -19.63 | -47.29 | 606 |
| 52 | Z-score reversion · 1h | reversion | 82.79 | -17.21 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.73 | -17.27 | 193 | 21.2 | -12.64 | -1.59 | -27.49 | 393 |
| 54 | Agent (ML meta-label) | meta | 82.21 | -17.79 | 655 | 18.0 | -17.84 | -3.32 | -19.34 | 386 |
| 55 | Heikin-Ashi · 1h | trend | 81.32 | -18.68 | 207 | 22.2 | -31.53 | -5.09 | -42.46 | 678 |
| 56 | EMA 9/21 cross · 1h | trend | 81.25 | -18.75 | 131 | 11.5 | -18.76 | -3.09 | -29.40 | 317 |
| 57 | VWAP momentum · 1h | momentum | 80.36 | -19.64 | 410 | 20.0 | -36.85 | -5.50 | -46.96 | 1252 |
| 58 | Williams %R · 1h | reversion | 80.09 | -19.91 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 59 | RSI(14) reversion · 1h | reversion | 80.02 | -19.98 | 74 | 20.3 | -14.57 | -2.58 | -22.27 | 167 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 150 | 32.0 | -30.68 | -6.34 | -33.03 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.27 | -2.63 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.84 | -6.46 | -36.73 | 542 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.50 | -77.85 | 1733 |
| 64 | Volume breakout | breakout | 62.45 | -37.55 | 344 | 13.1 | -62.85 | -17.97 | -63.73 | 881 |
| 65 | Squeeze breakout | breakout | 60.74 | -39.26 | 451 | 14.2 | -63.21 | -18.03 | -65.35 | 1218 |
| 66 | Donchian 55/20 | breakout | 59.83 | -40.17 | 457 | 17.5 | -68.30 | -14.17 | -72.80 | 1279 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.59 | -16.52 | -74.68 | 1632 |
| 68 | EMA 20/50 cross | trend | 57.76 | -42.24 | 480 | 18.3 | -75.75 | -14.55 | -80.16 | 1426 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.79 | -15.29 | -73.31 | 1514 |
| 70 | Keltner breakout | breakout | 52.19 | -47.81 | 646 | 15.9 | -82.63 | -26.40 | -83.11 | 1816 |
| 71 | AI bee: Boozy | ai | 51.18 | -48.82 | 343 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -29.93 | -98.66 | 5346 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.31 | -29.89 | -93.50 | 2585 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.00 | -19.76 | -87.78 | 1905 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.93 | -23.80 | -90.90 | 2351 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.00 | -25.69 | -91.01 | 2293 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -31.70 | -97.41 | 3518 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -36.65 | -96.70 | 3617 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -26.50 | -94.72 | 2588 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.83 | -23.18 | -82.70 | 1724 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.36 | -99.39 | 5812 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.22 | -25.61 | -91.71 | 2643 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.02 | -31.11 | -96.02 | 3509 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.12 | -99.74 | 6244 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.41 | -28.59 | -91.55 | 2356 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -38.84 | -97.53 | 3663 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.31 | -98.47 | 4754 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.66 | -33.23 | -93.67 | 2813 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.90 | -99.53 | 6238 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.77 | -22.18 | -86.81 | 2170 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.23 | -27.01 | -88.27 | 2170 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -32.09 | -95.86 | 3802 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.94 | -32.17 | -89.29 | 2104 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.77 | -33.54 | -95.77 | 4148 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.22 | -99.90 | 8341 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T07:20 | Donchian 55/20 | buy | XRP-USD | 14.96 | — | entry signal |
| 2026-10-19T07:15 | Volume breakout | sell | BTC-USD | 15.54 | -0.10 | exit signal |
| 2026-10-19T07:10 | Squeeze breakout | buy | BTC-USD | 15.20 | — | entry signal |
| 2026-10-19T07:10 | Keltner breakout | sell | DOGE-USD | 12.99 | -0.08 | target is flat |
| 2026-10-19T07:05 | Keltner breakout | buy | DOGE-USD | 13.07 | — | entry signal |
| 2026-10-19T07:00 | MFI reversion · 1h | sell | ETH-USD | 21.40 | 0.58 | exit signal |
| 2026-10-19T06:40 | Volume breakout | buy | BTC-USD | 15.64 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 07:25:05.000172+00:00 -> 2026-10-19 07:35:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
