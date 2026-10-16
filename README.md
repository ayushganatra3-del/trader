# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T18:26:05.000143+00:00 · 25066 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.93 (-8.07%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.13 | -0.24 |
| SQQQ | 19.14 | +0.76 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 32285 decisions in 2749 calls, $0.4016 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T18:26 | 1 / 16 / 13 | cash |  |
| Breezy | 2026-10-16T18:26 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-10-16T18:26 | 2 / 25 / 3 | ETHU 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.35 | 7.35 | 9 | 66.7 | 8.73 | 3.03 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.63 | 6.63 | 10 | 70.0 | 0.77 | 0.32 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.44 | 5.44 | 14 | 35.7 | 7.67 | 1.95 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.34 | 4.34 | 0 | — | 5.35 | 2.58 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.78 | -0.22 | 59 | 39.0 | -11.54 | -3.35 | -13.79 | 125 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.56 | -0.44 | 0 | — | 3.54 | 1.41 | -5.18 | 1 |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.96 | -1.04 | 1 | 100.0 | 0.00 | 0.13 | -7.93 | 9 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.79 | -1.21 | 51 | 31.4 | 1.98 | 1.09 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.77 | -1.23 | 36 | 16.7 | 8.94 | 1.19 | -22.12 | 109 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.76 | -3.91 | 20 |
| 13 | Hold SPY | benchmark | 98.59 | -1.41 | 0 | — | -1.68 | -0.90 | -3.23 | 1 |
| 14 | Max aggression: 5-day momentum | meta | 98.52 | -1.48 | 8 | 37.5 | -17.43 | -1.43 | -34.64 | 26 |
| 15 | Copy: Insider buying | copy | 98.30 | -1.70 | 20 | 45.0 | -12.28 | -2.10 | -20.62 | 75 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.35 | -2.65 | 0 | — | -4.87 | -1.95 | -7.50 | 1 |
| 17 | Agent (rotation) | meta | 96.90 | -3.10 | 107 | 32.7 | -8.06 | -3.01 | -11.52 | 294 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.71 | -3.29 | 0 | — | -2.41 | -0.95 | -5.15 | 1 |
| 19 | Hold BTC | benchmark | 96.65 | -3.35 | 0 | — | 28.63 | 3.34 | -8.68 | 1 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 96.53 | -3.47 | 0 | — | -6.52 | -3.55 | -6.72 | 1 |
| 21 | Trend pullback · 1h | trend | 96.13 | -3.87 | 87 | 24.1 | -21.22 | -6.28 | -22.40 | 151 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.64 | -5.36 | 81 | 19.8 | -8.93 | -1.59 | -13.33 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Daily: Momentum burst | daily | 93.40 | -6.60 | 5 | 20.0 | -6.86 | -0.90 | -19.89 | 42 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.31 | -6.78 | 197 |
| 27 | Parabolic SAR · 1h | trend | 93.21 | -6.79 | 95 | 22.1 | 3.23 | 0.59 | -22.55 | 278 |
| 28 | EMA 20/50 cross · 1h | trend | 92.87 | -7.13 | 54 | 14.8 | -4.01 | -0.35 | -22.92 | 128 |
| 29 | Agent (aggressive) | meta | 92.05 | -7.95 | 38 | 31.6 | -6.19 | -2.15 | -9.30 | 121 |
| 30 | Agent | meta | 91.93 | -8.07 | 77 | 39.0 | -9.81 | -5.21 | -10.73 | 243 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.79 | -0.11 | -14.55 | 118 |
| 32 | Opening range 30m | breakout | 91.14 | -8.86 | 193 | 29.5 | -12.32 | -3.41 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.06 | -8.94 | 76 | 17.1 | 0.69 | 0.29 | -26.55 | 219 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.48 | 0.89 | -14.21 | 274 |
| 35 | Daily: Bullish score | daily | 90.58 | -9.42 | 7 | 0.0 | -6.13 | -0.60 | -12.93 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.33 | -9.67 | 80 | 16.2 | -8.54 | -0.69 | -33.23 | 235 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.69 | -10.30 | 0 | — | -19.56 | -3.71 | -20.15 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.42 | -10.57 | 0 | — | -0.04 | 0.17 | -13.89 | 1 |
| 40 | Supertrend · 1h | trend | 89.32 | -10.68 | 83 | 12.0 | -3.74 | -0.22 | -30.09 | 213 |
| 41 | MACD cross · 1h | trend | 89.31 | -10.69 | 170 | 22.9 | -14.36 | -1.89 | -27.71 | 453 |
| 42 | Keltner breakout · 1h | breakout | 89.04 | -10.96 | 52 | 23.1 | -9.31 | -1.15 | -27.05 | 210 |
| 43 | Connors RSI(2) · 1h | reversion | 88.05 | -11.95 | 144 | 40.3 | -24.94 | -7.42 | -25.74 | 243 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.03 | 168 | 18.5 | -8.98 | -0.73 | -34.01 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 87.25 | -12.75 | 135 | 43.7 | -20.38 | -3.71 | -21.69 | 357 |
| 46 | Opening range 15m | breakout | 86.53 | -13.47 | 242 | 25.2 | -17.30 | -4.50 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 86.30 | -13.70 | 14 | 35.7 | -10.42 | -0.22 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.28 | -4.56 | -23.33 | 221 |
| 49 | Donchian 20/10 · 1h | breakout | 84.93 | -15.07 | 78 | 17.9 | 0.83 | 0.31 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.78 | -15.22 | 207 | 18.8 | -47.77 | -19.89 | -48.45 | 610 |
| 51 | Z-score reversion · 1h | reversion | 84.38 | -15.62 | 84 | 32.1 | -14.66 | -2.58 | -19.00 | 180 |
| 52 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -22.25 | -3.66 | -22.52 | 140 |
| 53 | Heikin-Ashi · 1h | trend | 83.86 | -16.14 | 189 | 24.3 | -31.20 | -5.10 | -40.33 | 673 |
| 54 | VWAP momentum · 1h | momentum | 83.84 | -16.16 | 387 | 21.2 | -36.26 | -5.49 | -43.85 | 1253 |
| 55 | Agent (ML meta-label) | meta | 83.65 | -16.35 | 603 | 19.1 | -5.33 | -0.59 | -15.33 | 386 |
| 56 | ROC + volume · 1h | momentum | 82.94 | -17.06 | 191 | 21.5 | -12.47 | -1.65 | -26.42 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.17 | -17.83 | 127 | 11.8 | -7.18 | -0.64 | -29.65 | 320 |
| 58 | Williams %R · 1h | reversion | 80.64 | -19.36 | 180 | 42.2 | -34.11 | -5.56 | -35.42 | 523 |
| 59 | Bollinger reversion · 1h | reversion | 80.54 | -19.46 | 138 | 31.2 | -30.01 | -6.21 | -31.96 | 337 |
| 60 | RSI(14) reversion · 1h | reversion | 80.18 | -19.82 | 73 | 20.5 | -14.19 | -2.51 | -21.39 | 159 |
| 61 | CCI reversion · 1h | reversion | 79.91 | -20.09 | 160 | 38.8 | -18.56 | -2.42 | -24.64 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 76.39 | -23.61 | 203 | 25.1 | -34.62 | -6.22 | -35.40 | 516 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -62.88 | -17.72 | -62.88 | 896 |
| 64 | ROC + volume | momentum | 63.40 | -36.60 | 546 | 21.8 | -75.82 | -17.48 | -77.45 | 1708 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -62.95 | -17.80 | -63.91 | 1217 |
| 66 | RSI(14) reversion | reversion | 63.03 | -36.97 | 622 | 26.8 | -74.73 | -16.77 | -74.77 | 1626 |
| 67 | Donchian 55/20 | breakout | 61.46 | -38.53 | 434 | 17.7 | -69.09 | -14.41 | -71.81 | 1283 |
| 68 | EMA 20/50 cross | trend | 59.89 | -40.11 | 454 | 19.2 | -77.22 | -15.11 | -79.04 | 1451 |
| 69 | AI bee: Boozy | ai | 55.86 | -44.14 | 295 | 6.1 | — | — | — | — |
| 70 | VWAP reversion | reversion | 55.83 | -44.17 | 639 | 22.8 | -73.53 | -15.45 | -73.57 | 1493 |
| 71 | Keltner breakout | breakout | 54.73 | -45.27 | 606 | 16.0 | -83.59 | -26.80 | -83.72 | 1845 |
| 72 | Ichimoku | trend | 51.97 | -48.03 | 552 | 11.6 | -81.99 | -22.76 | -82.11 | 1733 |
| 73 | Supertrend | trend | 51.49 | -48.51 | 632 | 19.8 | -86.52 | -20.33 | -86.98 | 1916 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.41 | -98.65 | 5317 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -29.83 | -93.53 | 2601 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -24.53 | -90.58 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.82 | -27.15 | -91.84 | 2346 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -31.96 | -97.45 | 3527 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -35.76 | -96.71 | 3594 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -26.13 | -94.43 | 2614 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -36.00 | -99.41 | 5825 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.40 | -25.72 | -91.47 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.69 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.49 | -99.73 | 6211 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.10 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -37.51 | -97.47 | 3654 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -36.07 | -98.51 | 4756 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.66 | -32.65 | -93.71 | 2807 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.05 | -99.55 | 6247 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.64 | -22.19 | -86.66 | 2163 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.09 | -27.21 | -88.11 | 2144 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.02 | -32.24 | -96.02 | 3816 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -33.73 | -89.39 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.87 | -33.48 | -95.88 | 4154 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.92 | -99.89 | 8276 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T18:25 | RSI(14) reversion · 1h | buy | NVDA | 4.03 | — | rebalance up |
| 2026-10-16T18:25 | VWAP reversion | buy | META | 2.33 | — | entry signal |
| 2026-10-16T18:25 | VWAP reversion | buy | GOOGL | 2.33 | — | entry signal |
| 2026-10-16T18:20 | VWAP reversion | sell | NVDA | 2.22 | -0.01 | stop-loss |
| 2026-10-16T18:20 | VWAP reversion | sell | GOOGL | 2.22 | -0.01 | stop-loss |
| 2026-10-16T18:20 | RSI(14) reversion | buy | IWM | 1.49 | — | entry |
| 2026-10-16T18:20 | RSI(14) reversion | buy | ETHU | 3.00 | — | entry |
| 2026-10-16T18:20 | RSI(14) reversion | sell | GOOGL | 4.49 | -0.02 | stop-loss |
| 2026-10-16T18:19 | AI bee: Boozy | buy | ETHU | 32.08 | — | Jev: buy (buy p=0.57) |
| 2026-10-16T18:19 | AI bee: Boozy | sell | COIN | 29.43 | 0.04 | Jev: hold |
| 2026-10-16T18:15 | VWAP reversion | buy | LABU | 2.33 | — | entry signal |
| 2026-10-16T18:15 | VWAP reversion | sell | SOXL | 2.04 | -0.00 | target is flat |
| 2026-10-16T18:15 | VWAP reversion | sell | META | 2.22 | -0.01 | stop-loss |
| 2026-10-16T18:10 | VWAP reversion | buy | SOXL | 2.04 | — | entry signal |
| 2026-10-16T18:10 | VWAP reversion | buy | AMZN | 2.23 | — | entry signal |
| 2026-10-16T18:05 | Agent (ML meta-label) | sell | SQQQ | 7.00 | 0.02 | selected signal exited |
| 2026-10-16T18:05 | Agent (ML meta-label) | sell | IWM | 5.29 | -0.06 | selected signal exited |
| 2026-10-16T18:05 | CCI reversion · 1h | buy | SOXL | 6.80 | — | rebalance up |
| 2026-10-16T18:05 | CCI reversion · 1h | buy | NVDA | 6.65 | — | rebalance up |
| 2026-10-16T18:05 | CCI reversion · 1h | buy | ETHU | 6.45 | — | rebalance up |
| 2026-10-16T18:05 | CCI reversion · 1h | buy | AMD | 6.66 | — | rebalance up |
| 2026-10-16T18:05 | CCI reversion · 1h | sell | IWM | 13.29 | -0.08 | stop-loss |
| 2026-10-16T18:05 | Z-score reversion · 1h | buy | TQQQ | 4.81 | — | rebalance up |
| 2026-10-16T18:05 | Z-score reversion · 1h | buy | TECL | 4.81 | — | rebalance up |
| 2026-10-16T18:05 | Z-score reversion · 1h | buy | SOXL | 4.90 | — | rebalance up |
| 2026-10-16T18:05 | Z-score reversion · 1h | buy | NVDA | 4.80 | — | rebalance up |
| 2026-10-16T18:05 | Z-score reversion · 1h | buy | AMD | 6.35 | — | rebalance up |
| 2026-10-16T18:05 | Z-score reversion · 1h | sell | IWM | 12.06 | -0.11 | stop-loss |
| 2026-10-16T18:05 | RSI(14) reversion · 1h | sell | SOXL | 13.22 | -0.33 | stop-loss |
| 2026-10-16T18:05 | RSI(14) reversion · 1h | sell | IWM | 16.04 | -0.13 | stop-loss |
| 2026-10-16T18:05 | MACD cross · 1h | buy | ETHU | 4.57 | — | rebalance up |
| 2026-10-16T18:05 | MACD cross · 1h | buy | COIN | 4.48 | — | rebalance up |
| 2026-10-16T18:05 | MACD cross · 1h | sell | SOXL | 17.58 | -0.54 | stop-loss |
| 2026-10-16T18:05 | VWAP reversion | sell | AMZN | 2.22 | -0.01 | stop-loss |
| 2026-10-16T18:05 | RSI(14) reversion | buy | ETH-USD | 2.34 | — | entry |
| 2026-10-16T18:05 | RSI(14) reversion | buy | BTC-USD | 3.31 | — | entry |
| 2026-10-16T18:05 | RSI(14) reversion | buy | BITX | 3.31 | — | entry |
| 2026-10-16T18:05 | RSI(14) reversion | sell | UPRO | 4.48 | -0.03 | stop-loss |
| 2026-10-16T18:05 | RSI(14) reversion | sell | LABU | 4.48 | -0.04 | stop-loss |
| 2026-10-16T18:03 | AI bee: Boozy | buy | COIN | 29.39 | — | Jev: buy (buy p=0.53) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 18:26:05.000143+00:00 -> 2026-10-16 18:36:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
