# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T19:25:05.000181+00:00 · 25116 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.16 | -0.22 |
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
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 36821 decisions in 2899 calls, $0.4548 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T19:25 | 8 / 20 / 2 | AMD 16%, TNA 14% |  |
| Breezy | 2026-10-16T19:25 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-16T19:25 | 5 / 25 / 0 | COIN 54% |  |

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
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.58 | 7.58 | 9 | 66.7 | 8.96 | 3.07 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.87 | 6.87 | 10 | 70.0 | 0.98 | 0.38 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.67 | 5.67 | 14 | 35.7 | 7.89 | 1.99 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.41 | 4.41 | 0 | — | 5.41 | 2.62 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.85 | -0.15 | 0 | — | 3.82 | 1.53 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.82 | -0.18 | 59 | 39.0 | -11.37 | -3.31 | -13.79 | 126 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.85 | -1.15 | 51 | 31.4 | 2.04 | 1.13 | -2.96 | 69 |
| 10 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 9.00 | 1.21 | -22.12 | 109 |
| 11 | Max aggression: 5-day momentum | meta | 98.74 | -1.26 | 8 | 37.5 | -17.26 | -1.41 | -34.64 | 26 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.79 | -3.91 | 20 |
| 13 | Hold SPY | benchmark | 98.67 | -1.33 | 0 | — | -1.61 | -0.88 | -3.23 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 98.63 | -1.37 | 3 | 33.3 | -0.01 | 0.13 | -7.93 | 9 |
| 15 | Copy: Insider buying | copy | 98.18 | -1.82 | 20 | 45.0 | -12.38 | -2.13 | -20.62 | 75 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.36 | -2.64 | 0 | — | -4.87 | -1.96 | -7.50 | 1 |
| 17 | Agent (rotation) | meta | 97.04 | -2.96 | 107 | 32.7 | -9.51 | -3.26 | -13.22 | 293 |
| 18 | Hold BTC | benchmark | 96.77 | -3.23 | 0 | — | 28.83 | 3.38 | -8.68 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.51 | -3.49 | 0 | — | -2.62 | -1.04 | -5.31 | 1 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 96.50 | -3.50 | 0 | — | -6.56 | -3.58 | -6.88 | 1 |
| 21 | Trend pullback · 1h | trend | 96.20 | -3.80 | 87 | 24.1 | -21.16 | -6.31 | -22.47 | 151 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.77 | -5.24 | 81 | 19.8 | -8.82 | -1.58 | -13.33 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.25 | -6.75 | 96 | 21.9 | 3.26 | 0.60 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.26 | -0.97 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -4.25 | -0.39 | -22.92 | 129 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.09 | -2.12 | -9.30 | 121 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.13 | -5.27 | -11.11 | 242 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.79 | -0.11 | -14.55 | 118 |
| 32 | Opening range 30m | breakout | 91.19 | -8.81 | 193 | 29.5 | -12.27 | -3.42 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.17 | -8.83 | 76 | 17.1 | 0.81 | 0.31 | -26.55 | 219 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.72 | 0.92 | -14.21 | 273 |
| 35 | Daily: Bullish score | daily | 90.55 | -9.45 | 7 | 0.0 | -6.16 | -0.61 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.91 | -0.62 | -33.23 | 234 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.58 | -10.42 | 0 | — | -19.66 | -3.75 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.36 | -10.64 | 84 | 11.9 | -3.71 | -0.22 | -30.09 | 213 |
| 40 | MACD cross · 1h | trend | 89.34 | -10.66 | 171 | 22.8 | -14.41 | -1.91 | -27.78 | 453 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -9.26 | -1.15 | -27.05 | 210 |
| 42 | Copy: Cathie Wood (ARKK) | copy | 88.94 | -11.06 | 0 | — | -0.60 | 0.09 | -14.38 | 1 |
| 43 | OBV trend · 1h | momentum | 87.97 | -12.03 | 169 | 18.3 | -8.82 | -0.72 | -33.94 | 320 |
| 44 | Connors RSI(2) · 1h | reversion | 87.92 | -12.08 | 145 | 40.0 | -25.24 | -7.58 | -26.03 | 239 |
| 45 | Stochastic reversion · 1h | reversion | 87.15 | -12.85 | 136 | 43.4 | -20.45 | -3.74 | -22.11 | 357 |
| 46 | Opening range 15m | breakout | 86.57 | -13.43 | 242 | 25.2 | -17.26 | -4.52 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 86.27 | -13.73 | 14 | 35.7 | -10.45 | -0.22 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.09 | -4.55 | -23.33 | 220 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 0.88 | 0.32 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.80 | -20.30 | -48.45 | 610 |
| 51 | Z-score reversion · 1h | reversion | 84.28 | -15.71 | 85 | 31.8 | -14.67 | -2.60 | -19.86 | 181 |
| 52 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -22.13 | -3.69 | -23.01 | 141 |
| 53 | Heikin-Ashi · 1h | trend | 83.91 | -16.09 | 189 | 24.3 | -31.15 | -5.13 | -40.33 | 673 |
| 54 | VWAP momentum · 1h | momentum | 83.89 | -16.11 | 387 | 21.2 | -36.11 | -5.50 | -43.85 | 1252 |
| 55 | Agent (ML meta-label) | meta | 83.64 | -16.36 | 607 | 19.1 | -8.15 | -1.19 | -17.48 | 379 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.44 | -1.66 | -26.42 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.23 | -17.77 | 127 | 11.8 | -7.35 | -0.67 | -29.70 | 320 |
| 58 | Williams %R · 1h | reversion | 80.66 | -19.34 | 180 | 42.2 | -34.10 | -5.60 | -35.92 | 523 |
| 59 | Bollinger reversion · 1h | reversion | 80.55 | -19.45 | 138 | 31.2 | -30.05 | -6.27 | -32.42 | 340 |
| 60 | RSI(14) reversion · 1h | reversion | 80.17 | -19.83 | 74 | 20.3 | -14.86 | -2.65 | -21.70 | 165 |
| 61 | CCI reversion · 1h | reversion | 79.77 | -20.23 | 161 | 38.5 | -18.70 | -2.45 | -25.25 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 76.45 | -23.55 | 204 | 25.0 | -34.72 | -6.30 | -35.45 | 517 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.21 | -18.25 | -63.22 | 881 |
| 64 | ROC + volume | momentum | 63.52 | -36.48 | 546 | 21.8 | -75.90 | -17.79 | -77.55 | 1694 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -63.01 | -18.09 | -63.96 | 1218 |
| 66 | RSI(14) reversion ⏸ | reversion | 62.42 | -37.58 | 646 | 25.9 | -74.83 | -16.92 | -74.99 | 1641 |
| 67 | Donchian 55/20 | breakout | 61.50 | -38.50 | 434 | 17.7 | -69.08 | -14.57 | -71.81 | 1283 |
| 68 | EMA 20/50 cross | trend | 59.93 | -40.07 | 454 | 19.2 | -77.21 | -15.28 | -79.04 | 1451 |
| 69 | VWAP reversion | reversion | 55.77 | -44.23 | 654 | 22.6 | -73.59 | -15.63 | -73.75 | 1503 |
| 70 | AI bee: Boozy | ai | 55.75 | -44.25 | 297 | 6.4 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.76 | -45.24 | 606 | 16.0 | -83.55 | -27.31 | -83.68 | 1844 |
| 72 | Ichimoku | trend | 52.00 | -48.00 | 552 | 11.6 | -81.98 | -23.15 | -82.11 | 1733 |
| 73 | Supertrend ⏸ | trend | 50.88 | -49.12 | 638 | 19.6 | -86.50 | -20.57 | -87.06 | 1915 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.02 | -98.64 | 5315 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -30.33 | -93.49 | 2597 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.47 | -24.86 | -90.54 | 2366 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.82 | -27.73 | -91.83 | 2346 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -32.98 | -97.46 | 3533 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -36.63 | -96.69 | 3571 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -26.67 | -94.42 | 2613 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -37.24 | -99.42 | 5848 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.40 | -26.25 | -91.47 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -32.56 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.13 | -99.74 | 6234 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -29.69 | -91.75 | 2367 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -38.70 | -97.46 | 3654 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -37.14 | -98.52 | 4778 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.65 | -33.59 | -93.71 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -40.51 | -99.55 | 6266 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.71 | -22.52 | -86.78 | 2168 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.13 | -27.65 | -88.19 | 2157 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -33.11 | -96.06 | 3830 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -34.55 | -89.39 | 2115 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.87 | -34.35 | -95.89 | 4161 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.90 | -99.89 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T19:25 | Agent (ML meta-label) | sell | ETHU | 6.41 | -0.08 | selected signal exited |
| 2026-10-16T19:20 | ROC + volume | buy | LABU | 15.87 | — | entry |
| 2026-10-16T19:15 | VWAP reversion | buy | AMD | 2.32 | — | entry signal |
| 2026-10-16T19:15 | VWAP reversion | sell | SOXL | 2.35 | 0.04 | target is flat |
| 2026-10-16T19:15 | Three white soldiers | sell | SQQQ | 21.26 | 0.08 | exit signal |
| 2026-10-16T19:12 | AI bee: Boozy | buy | COIN | 29.67 | — | Jev: buy (buy p=0.53) |
| 2026-10-16T19:12 | AI bee: Boozy | sell | BITX | 29.02 | 0.07 | Jev: buy |
| 2026-10-16T19:10 | Z-score reversion · 1h | buy | BITX | 16.65 | — | entry |
| 2026-10-16T19:10 | Z-score reversion · 1h | sell | TQQQ | 16.65 | -0.42 | stop-loss |
| 2026-10-16T19:10 | VWAP reversion | buy | TSLA | 2.31 | — | entry signal |
| 2026-10-16T19:10 | VWAP reversion | buy | SOXL | 2.31 | — | entry |
| 2026-10-16T19:10 | VWAP reversion | buy | COIN | 2.31 | — | entry signal |
| 2026-10-16T19:10 | VWAP reversion | sell | AMD | 2.31 | -0.02 | stop-loss |
| 2026-10-16T19:05 | Connors RSI(2) · 1h | sell | META | 21.93 | -0.51 | stop-loss |
| 2026-10-16T19:05 | MACD cross · 1h | buy | NVDA | 4.46 | — | rebalance up |
| 2026-10-16T19:05 | VWAP reversion | sell | TSLA | 2.22 | -0.01 | stop-loss |
| 2026-10-16T19:00 | Agent (ML meta-label) | sell | BITX | 6.42 | 0.03 | selected signal exited |
| 2026-10-16T19:00 | Candlestick reversal · 1h | buy | NVDA | 19.09 | — | entry |
| 2026-10-16T19:00 | OBV trend · 1h | sell | AAPL | 21.80 | -0.14 | target is flat |
| 2026-10-16T19:00 | VWAP reversion | buy | UPRO | 2.41 | — | entry signal |
| 2026-10-16T19:00 | VWAP reversion | buy | TQQQ | 2.41 | — | entry signal |
| 2026-10-16T19:00 | VWAP reversion | buy | TECL | 2.41 | — | entry signal |
| 2026-10-16T19:00 | VWAP reversion | buy | QQQ | 2.41 | — | entry signal |
| 2026-10-16T19:00 | VWAP reversion | buy | NVDA | 2.41 | — | entry |
| 2026-10-16T19:00 | VWAP reversion | buy | MSTR | 2.41 | — | entry signal |
| 2026-10-16T19:00 | VWAP reversion | sell | LABU | 2.34 | 0.01 | target is flat |
| 2026-10-16T19:00 | VWAP reversion | sell | BITX | 2.13 | -0.01 | target is flat |
| 2026-10-16T18:56 | Agent (ML meta-label) | buy | BITX | 6.39 | — | entry |
| 2026-10-16T18:56 | RSI(14) reversion | sell | XRP-USD | 4.46 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | TNA | 3.29 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | PLTR | 6.25 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | MSFT | 3.14 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | META | 6.25 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | IWM | 6.25 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | GOOGL | 6.25 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | DOGE-USD | 4.48 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | AMZN | 6.25 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:56 | RSI(14) reversion | sell | AMD | 4.49 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T18:55 | Agent (ML meta-label) | sell | TECL | 8.26 | -0.39 | selected signal exited |
| 2026-10-16T18:55 | CCI reversion · 1h | sell | AMD | 19.88 | -0.22 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 19:25:05.000181+00:00 -> 2026-10-16 19:35:05.000181+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
