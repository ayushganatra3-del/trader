# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T15:25:05.000126+00:00 · 28521 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.37%)

Closed trades 80, win rate 38.8%, fees £2.76, max drawdown -9.78%.

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

Today: 18180 decisions in 2292 calls, $0.2349 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T15:25 | 11 / 16 / 2 | SOXL 16%, ETHU 16%, TECL 14% |  |
| Breezy | 2026-10-19T15:25 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-10-19T15:25 | 7 / 21 / 1 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |
| VWAP reversion | BITX | 1.52 | +2.60% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 10.33 | 3.45 | -3.27 | 18 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.74 | 4.74 | 0 | — | 5.71 | 2.79 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.49 | 2.49 | 72 | 45.8 | -7.60 | -2.04 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.81 | -0.19 | 3 | 33.3 | 4.07 | 0.91 | -7.93 | 9 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.75 | -0.25 | 0 | — | 2.34 | 0.99 | -5.18 | 1 |
| 10 | Hold SPY | benchmark | 99.44 | -0.56 | 0 | — | 0.14 | 0.13 | -3.13 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.18 | -1.82 | 54 | 31.5 | 3.10 | 1.72 | -2.17 | 63 |
| 13 | Hold BTC | benchmark | 97.86 | -2.14 | 0 | — | 27.07 | 3.21 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 97.83 | -2.17 | 111 | 32.4 | -3.16 | -1.49 | -5.45 | 279 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.32 | -2.68 | 0 | — | -0.57 | -0.17 | -5.31 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.18 | -2.82 | 36 | 16.7 | -10.17 | -1.64 | -20.68 | 107 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.98 | -2.25 | -5.83 | 1 |
| 18 | Trend pullback · 1h | trend | 96.17 | -3.83 | 87 | 24.1 | -19.82 | -5.87 | -20.58 | 135 |
| 19 | Copy: Insider buying | copy | 96.16 | -3.84 | 23 | 43.5 | -15.08 | -2.73 | -20.62 | 73 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.10 | -3.90 | 0 | — | -7.03 | -2.78 | -7.55 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Gap and go | momentum | 93.87 | -6.13 | 70 | 12.9 | 10.26 | 2.57 | -6.54 | 203 |
| 23 | Daily: Momentum burst | daily | 93.65 | -6.35 | 6 | 16.7 | -4.98 | -0.59 | -20.58 | 40 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.01 | 0.97 | -9.46 | 95 |
| 25 | ADX DI cross · 1h | trend | 93.26 | -6.74 | 86 | 18.6 | -13.19 | -2.48 | -15.13 | 252 |
| 26 | Max aggression: 5-day momentum | meta | 93.11 | -6.89 | 8 | 37.5 | -21.89 | -1.86 | -34.64 | 26 |
| 27 | Daily: Bullish score | daily | 92.12 | -7.88 | 7 | 0.0 | -2.46 | -0.11 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.85 | -8.15 | 78 | 23.1 | -1.68 | -0.09 | -14.31 | 111 |
| 29 | Parabolic SAR · 1h | trend | 91.84 | -8.16 | 102 | 22.5 | -12.81 | -2.34 | -23.90 | 269 |
| 30 | Opening range 30m | breakout | 91.40 | -8.60 | 197 | 29.4 | -11.16 | -3.06 | -17.60 | 563 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.70 | -2.41 | -16.91 | 1 |
| 32 | Bollinger breakout · 1h | breakout | 90.74 | -9.27 | 84 | 28.6 | -2.13 | -0.18 | -15.14 | 264 |
| 33 | Agent | meta | 90.63 | -9.37 | 80 | 38.8 | -8.67 | -4.46 | -12.59 | 235 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 90.55 | -9.45 | 0 | — | 4.11 | 0.77 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 90.12 | -9.88 | 58 | 13.8 | -18.74 | -3.41 | -20.51 | 129 |
| 36 | RSI momentum · 1h | momentum | 89.75 | -10.25 | 78 | 16.7 | -17.64 | -3.09 | -28.10 | 215 |
| 37 | Stochastic reversion · 1h | reversion | 89.28 | -10.72 | 151 | 45.7 | -16.68 | -2.79 | -22.24 | 370 |
| 38 | Connors RSI(2) · 1h | reversion | 88.93 | -11.07 | 149 | 40.9 | -23.66 | -7.13 | -24.79 | 207 |
| 39 | Ichimoku · 1h | trend | 88.84 | -11.16 | 55 | 14.5 | -17.38 | -3.28 | -18.08 | 113 |
| 40 | Supertrend · 1h | trend | 87.94 | -12.06 | 85 | 11.8 | -20.11 | -4.20 | -24.40 | 218 |
| 41 | Agent (aggressive) | meta | 87.73 | -12.27 | 40 | 32.5 | -0.62 | -0.09 | -9.23 | 109 |
| 42 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 56 | 23.2 | -11.41 | -1.51 | -28.00 | 207 |
| 43 | Max aggression: 1-day momentum | meta | 87.35 | -12.65 | 15 | 33.3 | -10.84 | -0.26 | -37.31 | 42 |
| 44 | Triple EMA stack · 1h | trend | 87.20 | -12.80 | 85 | 15.3 | -22.40 | -3.00 | -33.93 | 218 |
| 45 | MACD cross · 1h | trend | 86.85 | -13.15 | 186 | 21.0 | -24.93 | -4.55 | -31.95 | 469 |
| 46 | Opening range 15m | breakout | 86.84 | -13.16 | 247 | 25.1 | -16.28 | -4.19 | -21.40 | 701 |
| 47 | Z-score reversion · 1h | reversion | 86.60 | -13.40 | 91 | 30.8 | -12.42 | -1.91 | -21.32 | 197 |
| 48 | OBV trend · 1h | momentum | 85.65 | -14.35 | 174 | 17.8 | -27.72 | -4.49 | -34.49 | 321 |
| 49 | MFI reversion · 1h | reversion | 85.09 | -14.91 | 209 | 31.1 | -16.40 | -2.53 | -21.34 | 139 |
| 50 | Agent (ML meta-label) | meta | 85.04 | -14.96 | 664 | 18.8 | -13.64 | -2.11 | -19.15 | 380 |
| 51 | MACD zero-line · 1h | trend | 84.55 | -15.45 | 86 | 15.1 | -24.68 | -4.94 | -25.14 | 218 |
| 52 | Donchian 20/10 · 1h | breakout | 83.44 | -16.56 | 81 | 17.3 | -0.56 | 0.15 | -23.16 | 217 |
| 53 | Williams %R · 1h | reversion | 83.06 | -16.94 | 182 | 42.9 | -32.80 | -5.10 | -36.50 | 534 |
| 54 | Bollinger reversion · 1h | reversion | 82.77 | -17.23 | 153 | 32.7 | -28.47 | -5.48 | -33.14 | 352 |
| 55 | Three white soldiers | momentum | 82.77 | -17.23 | 225 | 18.2 | -47.29 | -19.01 | -47.49 | 604 |
| 56 | RSI(14) reversion · 1h | reversion | 81.59 | -18.41 | 75 | 21.3 | -11.39 | -1.89 | -22.27 | 175 |
| 57 | CCI reversion · 1h | reversion | 81.58 | -18.42 | 161 | 38.5 | -19.17 | -2.41 | -27.44 | 444 |
| 58 | ROC + volume · 1h | momentum | 81.39 | -18.61 | 197 | 20.8 | -14.03 | -1.78 | -29.08 | 393 |
| 59 | EMA 9/21 cross · 1h | trend | 80.95 | -19.05 | 131 | 11.5 | -18.82 | -3.18 | -28.89 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 79.91 | -20.09 | 212 | 22.6 | -35.63 | -5.90 | -43.98 | 667 |
| 61 | VWAP momentum · 1h | momentum | 78.90 | -21.10 | 417 | 20.4 | -35.75 | -4.78 | -47.95 | 1248 |
| 62 | Candlestick reversal · 1h | reversion | 78.68 | -21.32 | 209 | 26.3 | -34.67 | -5.91 | -37.46 | 535 |
| 63 | ROC + volume | momentum | 62.62 | -37.38 | 574 | 22.1 | -75.47 | -17.30 | -78.19 | 1730 |
| 64 | Volume breakout | breakout | 61.84 | -38.16 | 351 | 12.8 | -62.48 | -17.61 | -64.19 | 876 |
| 65 | Squeeze breakout | breakout | 60.80 | -39.20 | 455 | 14.1 | -64.10 | -20.82 | -65.58 | 1204 |
| 66 | Donchian 55/20 | breakout | 59.76 | -40.24 | 463 | 17.9 | -67.88 | -13.96 | -72.80 | 1275 |
| 67 | RSI(14) reversion | reversion | 57.85 | -42.15 | 700 | 24.9 | -74.58 | -16.51 | -74.62 | 1599 |
| 68 | EMA 20/50 cross | trend | 57.57 | -42.43 | 489 | 18.8 | -75.45 | -14.32 | -80.26 | 1433 |
| 69 | VWAP reversion | reversion | 53.85 | -46.15 | 737 | 25.0 | -72.24 | -14.90 | -72.96 | 1511 |
| 70 | Keltner breakout | breakout | 51.72 | -48.28 | 653 | 15.8 | -82.47 | -26.16 | -83.37 | 1814 |
| 71 | AI bee: Boozy | ai | 50.92 | -49.08 | 346 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.76 | -98.66 | 5339 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.20 | -29.51 | -93.67 | 2570 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.15 | -19.93 | -87.87 | 1896 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.90 | -23.80 | -90.92 | 2347 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.96 | -25.62 | -91.02 | 2274 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -32.14 | -97.46 | 3492 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.57 | -35.61 | -96.71 | 3587 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -26.01 | -94.67 | 2581 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.46 | -22.65 | -82.84 | 1705 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.14 | -99.38 | 5726 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.99 | -25.12 | -91.85 | 2618 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -31.65 | -96.12 | 3482 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.68 | -99.74 | 6192 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.36 | -28.69 | -91.50 | 2346 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -38.40 | -97.54 | 3628 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.52 | -98.48 | 4700 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -32.34 | -93.78 | 2796 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.20 | -99.53 | 6163 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.19 | -86.76 | 2149 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.79 | -26.53 | -87.87 | 2139 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.72 | -95.90 | 3764 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.69 | -31.66 | -88.97 | 2089 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.45 | -95.74 | 4097 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.32 | -99.90 | 8277 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T15:25 | Agent (ML meta-label) | buy | AMD | 4.31 | — | rebalance up |
| 2026-10-19T15:25 | Agent (ML meta-label) | sell | LABU | 8.58 | 0.05 | selected signal exited |
| 2026-10-19T15:25 | Agent (aggressive) | sell | SQQQ | 87.73 | -1.91 | selected signal exited |
| 2026-10-19T15:25 | Agent | sell | SQQQ | 35.81 | -0.66 | selected signal exited |
| 2026-10-19T15:25 | VWAP reversion | sell | SOL-USD | 13.47 | 0.03 | exit signal |
| 2026-10-19T15:25 | VWAP reversion | sell | ETH-USD | 13.46 | -0.00 | exit signal |
| 2026-10-19T15:25 | VWAP reversion | sell | COIN | 13.48 | 0.09 | exit signal |
| 2026-10-19T15:25 | VWAP reversion | sell | BTC-USD | 13.45 | -0.02 | exit signal |
| 2026-10-19T15:25 | RSI(14) reversion | sell | ETH-USD | 11.62 | 0.01 | exit signal |
| 2026-10-19T15:25 | RSI(14) reversion | sell | BTC-USD | 11.61 | -0.03 | exit signal |
| 2026-10-19T15:25 | Donchian 55/20 | buy | UPRO | 5.42 | — | entry |
| 2026-10-19T15:25 | Donchian 55/20 | buy | TECL | 5.43 | — | entry |
| 2026-10-19T15:25 | Donchian 55/20 | buy | SOXL | 5.43 | — | entry signal |
| 2026-10-19T15:25 | Donchian 55/20 | buy | NVDA | 5.43 | — | entry |
| 2026-10-19T15:25 | Donchian 55/20 | sell | TSLA | 3.12 | 0.03 | rebalance down |
| 2026-10-19T15:25 | Donchian 55/20 | sell | TQQQ | 3.15 | 0.04 | rebalance down |
| 2026-10-19T15:25 | Donchian 55/20 | sell | SPY | 3.05 | 0.00 | rebalance down |
| 2026-10-19T15:25 | Donchian 55/20 | sell | QQQ | 3.07 | 0.01 | rebalance down |
| 2026-10-19T15:25 | Donchian 55/20 | sell | PLTR | 3.18 | 0.05 | rebalance down |
| 2026-10-19T15:25 | Donchian 55/20 | sell | MSFT | 3.03 | -0.00 | rebalance down |
| 2026-10-19T15:25 | Donchian 55/20 | sell | AMZN | 3.14 | 0.04 | rebalance down |
| 2026-10-19T15:25 | ROC + volume | buy | ETHU | 2.64 | — | entry signal |
| 2026-10-19T15:25 | ROC + volume | buy | BITX | 6.26 | — | entry signal |
| 2026-10-19T15:25 | ROC + volume | sell | GOOGL | 8.90 | 0.01 | exit signal |
| 2026-10-19T15:20 | Donchian 20/10 · 1h | buy | SQQQ | 4.18 | — | rebalance up |
| 2026-10-19T15:20 | Triple EMA stack · 1h | buy | SQQQ | 4.37 | — | rebalance up |
| 2026-10-19T15:20 | RSI(14) reversion | sell | XRP-USD | 11.58 | -0.02 | exit signal |
| 2026-10-19T15:20 | Volume breakout | buy | TQQQ | 15.43 | — | entry signal |
| 2026-10-19T15:20 | Volume breakout | sell | MSFT | 15.41 | -0.05 | exit signal |
| 2026-10-19T15:20 | ROC + volume | buy | SOL-USD | 4.99 | — | entry signal |
| 2026-10-19T15:20 | ROC + volume | buy | MSFT | 5.54 | — | rebalance up |
| 2026-10-19T15:20 | ROC + volume | buy | META | 6.95 | — | entry |
| 2026-10-19T15:20 | ROC + volume | sell | TSLA | 3.50 | 0.05 | rebalance down |
| 2026-10-19T15:20 | ROC + volume | sell | QQQ | 3.44 | 0.00 | rebalance down |
| 2026-10-19T15:20 | ROC + volume | sell | PLTR | 3.56 | 0.08 | rebalance down |
| 2026-10-19T15:20 | ROC + volume | sell | NVDA | 3.46 | 0.01 | rebalance down |
| 2026-10-19T15:20 | ROC + volume | sell | AMZN | 3.52 | 0.06 | rebalance down |
| 2026-10-19T15:15 | Agent (ML meta-label) | buy | LABU | 8.54 | — | entry |
| 2026-10-19T15:15 | Agent (ML meta-label) | sell | SOXL | 4.30 | 0.09 | rebalance down |
| 2026-10-19T15:15 | Agent (ML meta-label) | sell | AMD | 4.23 | 0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 15:25:05.000126+00:00 -> 2026-10-19 15:35:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
