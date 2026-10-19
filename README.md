# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T03:55:05.000167+00:00 · 27949 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

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

Today: 2880 decisions in 576 calls, $0.0402 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T03:55 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-19T03:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T03:55 | 1 / 3 / 1 | COIN 72% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.83 | 4.83 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.95 | -0.05 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.57 | -0.43 | 64 | 39.1 | -11.25 | -3.24 | -13.79 | 140 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Max aggression: 5-day momentum | meta | 98.76 | -1.24 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 12 | Donchian 55/20 · 1h | breakout | 98.70 | -1.30 | 36 | 16.7 | -5.03 | -0.55 | -22.12 | 110 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.63 | -1.37 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.17 | -1.83 | 20 | 45.0 | -13.17 | -2.35 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 97.85 | -2.15 | 0 | — | 28.06 | 3.31 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -5.37 | -2.78 | -6.57 | 276 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.45 | -3.55 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.44 | -3.56 | 0 | — | -6.58 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -19.10 | -5.70 | -19.70 | 138 |
| 21 | Three white soldiers · 1h | momentum | 95.80 | -4.20 | 12 | 0.0 | 0.32 | 0.22 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.57 | -4.43 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.84 | -5.16 | 82 | 19.5 | -8.14 | -1.43 | -13.37 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 0.54 | 0.23 | -9.46 | 94 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.23 | -6.77 | 97 | 21.6 | -9.60 | -1.47 | -22.75 | 274 |
| 27 | Daily: Momentum burst | daily | 93.02 | -6.99 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.51 | -7.49 | 55 | 14.5 | -18.37 | -3.15 | -21.23 | 127 |
| 29 | Agent (aggressive) | meta | 92.16 | -7.84 | 38 | 31.6 | -5.81 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.96 | -5.32 | -13.12 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.81 | -9.19 | 77 | 16.9 | -17.17 | -2.98 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.67 | -9.33 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.42 | 1.12 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.36 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 89.93 | -10.07 | 81 | 16.0 | -18.49 | -2.28 | -33.23 | 230 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.48 | -10.53 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.27 | -10.73 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Supertrend · 1h | trend | 88.99 | -11.01 | 85 | 11.8 | -22.51 | -4.62 | -26.38 | 213 |
| 41 | Keltner breakout · 1h | breakout | 88.97 | -11.04 | 52 | 23.1 | -8.21 | -0.99 | -27.05 | 204 |
| 42 | Connors RSI(2) · 1h | reversion | 88.00 | -12.00 | 145 | 40.0 | -24.46 | -7.47 | -25.48 | 221 |
| 43 | MACD cross · 1h | trend | 87.72 | -12.28 | 181 | 21.5 | -23.73 | -4.12 | -30.63 | 459 |
| 44 | OBV trend · 1h | momentum | 87.60 | -12.40 | 170 | 18.2 | -16.63 | -1.91 | -33.85 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.69 | -13.31 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.97 | -14.03 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.21 | -14.79 | 82 | 15.9 | -23.79 | -4.72 | -24.17 | 219 |
| 49 | MFI reversion · 1h | reversion | 85.08 | -14.92 | 206 | 30.1 | -21.02 | -3.24 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.57 | -15.43 | 79 | 17.7 | 1.25 | 0.36 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 83.60 | -16.40 | 219 | 18.7 | -47.30 | -19.60 | -47.38 | 606 |
| 52 | Z-score reversion · 1h | reversion | 82.80 | -17.20 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.65 | -17.35 | 193 | 21.2 | -12.75 | -1.61 | -27.49 | 394 |
| 54 | Agent (ML meta-label) | meta | 82.22 | -17.78 | 655 | 18.0 | -19.26 | -3.38 | -20.73 | 386 |
| 55 | Heikin-Ashi · 1h | trend | 81.12 | -18.88 | 206 | 22.3 | -32.29 | -5.25 | -42.46 | 682 |
| 56 | EMA 9/21 cross · 1h | trend | 80.96 | -19.04 | 131 | 11.5 | -18.95 | -3.12 | -29.40 | 316 |
| 57 | Williams %R · 1h | reversion | 80.10 | -19.90 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 58 | VWAP momentum · 1h | momentum | 80.08 | -19.92 | 409 | 20.0 | -37.06 | -5.55 | -46.96 | 1252 |
| 59 | RSI(14) reversion · 1h | reversion | 80.03 | -19.97 | 74 | 20.3 | -14.57 | -2.58 | -22.27 | 167 |
| 60 | Bollinger reversion · 1h | reversion | 79.89 | -20.11 | 150 | 32.0 | -30.68 | -6.34 | -33.03 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.05 | -20.95 | 161 | 38.5 | -20.33 | -2.64 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.13 | -23.87 | 205 | 25.4 | -35.84 | -6.46 | -36.73 | 542 |
| 63 | Volume breakout | breakout | 62.86 | -37.14 | 341 | 13.2 | -62.79 | -17.84 | -63.59 | 881 |
| 64 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.50 | -77.85 | 1733 |
| 65 | Squeeze breakout | breakout | 61.29 | -38.71 | 448 | 14.3 | -63.00 | -17.89 | -65.03 | 1215 |
| 66 | Donchian 55/20 | breakout | 59.80 | -40.20 | 455 | 17.1 | -68.44 | -14.24 | -72.80 | 1280 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.48 | -16.44 | -74.57 | 1629 |
| 68 | EMA 20/50 cross | trend | 57.50 | -42.50 | 480 | 18.3 | -76.19 | -14.77 | -80.16 | 1433 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.77 | -15.27 | -73.29 | 1513 |
| 70 | Keltner breakout | breakout | 52.52 | -47.48 | 643 | 16.0 | -82.67 | -26.37 | -83.10 | 1819 |
| 71 | AI bee: Boozy | ai | 51.47 | -48.53 | 340 | 5.9 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.74 | -98.65 | 5335 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -29.68 | -93.50 | 2584 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.11 | -19.78 | -87.78 | 1908 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.00 | -23.79 | -90.90 | 2353 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.98 | -25.62 | -90.99 | 2291 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -31.69 | -97.45 | 3521 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.67 | -35.77 | -96.70 | 3610 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -26.47 | -94.72 | 2587 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.85 | -23.06 | -82.55 | 1723 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.27 | -99.39 | 5812 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.15 | -25.53 | -91.63 | 2639 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.05 | -31.35 | -96.05 | 3514 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.67 | -99.74 | 6235 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.48 | -28.64 | -91.61 | 2359 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -38.62 | -97.52 | 3661 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.23 | -98.48 | 4761 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.61 | -32.99 | -93.65 | 2809 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.72 | -99.53 | 6239 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.18 | -86.84 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.27 | -26.95 | -88.34 | 2172 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.09 | -95.89 | 3808 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.02 | -32.25 | -89.36 | 2108 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -33.40 | -95.79 | 4149 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.62 | -99.90 | 8334 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T03:50 | ROC + volume | sell | SOL-USD | 15.62 | -0.02 | target is flat |
| 2026-10-19T03:45 | Squeeze breakout | sell | BTC-USD | 15.26 | -0.14 | stop-loss |
| 2026-10-19T03:45 | Keltner breakout | sell | BTC-USD | 13.15 | -0.12 | stop-loss |
| 2026-10-19T03:25 | Keltner breakout | sell | DOGE-USD | 13.13 | -0.14 | target is flat |
| 2026-10-19T03:20 | Three white soldiers | sell | BTC-USD | 20.84 | -0.12 | exit signal |
| 2026-10-19T03:20 | Squeeze breakout | sell | XRP-USD | 15.25 | -0.15 | exit signal |
| 2026-10-19T03:20 | Keltner breakout | sell | SOL-USD | 13.12 | -0.14 | stop-loss |
| 2026-10-19T03:07 | AI bee: Boozy | sell | ETH-USD | 14.41 | -0.16 | Jev: sell (sell p=0.51) after 17 min |
| 2026-10-19T03:05 | Three white soldiers | sell | ETH-USD | 20.82 | -0.14 | exit signal |
| 2026-10-19T03:05 | Keltner breakout | sell | ETH-USD | 13.12 | -0.15 | stop-loss |
| 2026-10-19T03:00 | Keltner breakout · 1h | buy | SOL-USD | 21.58 | — | entry signal |
| 2026-10-19T03:00 | Donchian 55/20 · 1h | buy | SOL-USD | 24.72 | — | entry signal |
| 2026-10-19T03:00 | Donchian 20/10 · 1h | buy | SOL-USD | 4.23 | — | rebalance up |
| 2026-10-19T03:00 | Donchian 20/10 · 1h | sell | BTC-USD | 4.23 | -0.00 | rebalance down |
| 2026-10-19T03:00 | RSI momentum · 1h | buy | DOGE-USD | 10.41 | — | entry signal |
| 2026-10-19T03:00 | RSI momentum · 1h | sell | XRP-USD | 5.18 | -0.01 | rebalance down |
| 2026-10-19T03:00 | RSI momentum · 1h | sell | BTC-USD | 5.23 | 0.01 | rebalance down |
| 2026-10-19T03:00 | MACD zero-line · 1h | buy | DOGE-USD | 21.37 | — | entry signal |
| 2026-10-19T03:00 | Triple EMA stack · 1h | buy | BTC-USD | 22.51 | — | entry signal |
| 2026-10-19T02:50 | AI bee: Boozy | buy | ETH-USD | 14.57 | — | Jev: buy (buy p=0.74) |
| 2026-10-19T02:50 | Squeeze breakout | buy | XRP-USD | 15.39 | — | entry signal |
| 2026-10-19T02:50 | Squeeze breakout | buy | BTC-USD | 15.39 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | SOL-USD | 13.27 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | ETH-USD | 13.27 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | DOGE-USD | 13.27 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | BTC-USD | 13.27 | — | entry signal |
| 2026-10-19T02:45 | Three white soldiers | buy | ETH-USD | 20.97 | — | entry signal |
| 2026-10-19T02:45 | Three white soldiers | buy | BTC-USD | 20.97 | — | entry signal |
| 2026-10-19T02:30 | Squeeze breakout | sell | SOL-USD | 15.37 | -0.06 | stop-loss |
| 2026-10-19T02:30 | Keltner breakout | sell | SOL-USD | 13.26 | -0.05 | stop-loss |
| 2026-10-19T02:25 | Squeeze breakout | sell | DOGE-USD | 15.32 | -0.11 | stop-loss |
| 2026-10-19T02:25 | Keltner breakout | sell | ETH-USD | 13.27 | 0.19 | stop-loss |
| 2026-10-19T02:25 | Keltner breakout | sell | DOGE-USD | 10.65 | 0.22 | stop-loss |
| 2026-10-19T02:25 | Keltner breakout | sell | BTC-USD | 13.28 | 0.02 | exit signal |
| 2026-10-19T02:24 | AI bee: Boozy | sell | SOL-USD | 14.57 | -0.13 | Jev: sell (sell p=0.52) after 15 min |
| 2026-10-19T02:20 | Volume breakout | sell | DOGE-USD | 15.65 | -0.08 | exit signal |
| 2026-10-19T02:20 | ROC + volume | sell | BTC-USD | 12.56 | 0.05 | exit signal |
| 2026-10-19T02:09 | AI bee: Boozy | buy | SOL-USD | 14.70 | — | Jev: buy (buy p=0.73) |
| 2026-10-19T02:02 | RSI momentum · 1h | buy | SOL-USD | 4.54 | — | rebalance up |
| 2026-10-19T02:02 | RSI momentum · 1h | sell | XRP-USD | 4.54 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 03:55:05.000167+00:00 -> 2026-10-19 04:05:05.000167+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
