# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T18:55:05.000115+00:00 · 28667 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 83, win rate 39.8%, fees £2.81, max drawdown -9.80%.

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

Today: 31185 decisions in 2730 calls, $0.3872 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T18:55 | 3 / 16 / 10 | cash |  |
| Breezy | 2026-10-19T18:55 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-10-19T18:55 | 4 / 22 / 3 | ETHU 67% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.08 | 5.08 | 0 | — | 5.91 | 2.88 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.10 | 0 | — | 2.24 | 0.95 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.28 | -0.72 | 0 | — | -0.05 | 0.02 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.38 | 3 | 33.3 | 2.70 | 0.67 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.23 | -1.77 | 54 | 31.5 | 3.03 | 1.68 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.42 | -1.01 | -5.70 | 280 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.41 | -2.59 | 0 | — | -0.94 | -0.33 | -5.31 | 1 |
| 15 | Hold BTC | benchmark | 97.37 | -2.63 | 0 | — | 26.37 | 3.14 | -8.68 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.34 | -2.66 | 36 | 16.7 | -9.08 | -1.51 | -19.01 | 99 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.98 | -2.25 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.56 | -3.44 | 0 | — | -5.71 | -2.25 | -7.04 | 1 |
| 19 | Trend pullback · 1h | trend | 96.43 | -3.57 | 88 | 23.9 | -19.66 | -5.81 | -20.58 | 137 |
| 20 | Copy: Insider buying | copy | 96.03 | -3.97 | 23 | 43.5 | -15.30 | -2.77 | -20.62 | 73 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.05 | -4.95 | 8 | 37.5 | -20.38 | -1.72 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.72 | -6.28 | 87 | 18.4 | -14.43 | -2.55 | -16.96 | 259 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 9.78 | 2.46 | -6.51 | 202 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 93.15 | -6.85 | 6 | 16.7 | -5.77 | -0.72 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.09 | -7.91 | 7 | 0.0 | -2.73 | -0.15 | -13.10 | 12 |
| 28 | Parabolic SAR · 1h | trend | 91.92 | -8.08 | 102 | 22.5 | -14.10 | -2.65 | -24.57 | 266 |
| 29 | Volume breakout · 1h | breakout | 91.89 | -8.11 | 78 | 23.1 | -5.77 | -0.79 | -16.37 | 107 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.72 | -2.42 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 91.04 | -8.96 | 201 | 28.9 | -12.05 | -3.33 | -17.60 | 564 |
| 32 | Bollinger breakout · 1h | breakout | 90.78 | -9.22 | 84 | 28.6 | -8.23 | -1.36 | -16.89 | 257 |
| 33 | Agent | meta | 90.67 | -9.33 | 83 | 39.8 | -8.53 | -3.28 | -17.15 | 265 |
| 34 | EMA 20/50 cross · 1h | trend | 90.37 | -9.63 | 58 | 13.8 | -19.05 | -3.39 | -21.31 | 126 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 89.90 | -10.10 | 0 | — | 3.61 | 0.70 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.76 | -10.24 | 78 | 16.7 | -16.70 | -2.76 | -28.00 | 213 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.38 | -6.61 | -23.94 | 206 |
| 38 | Ichimoku · 1h | trend | 88.77 | -11.23 | 55 | 14.5 | -17.47 | -3.29 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.48 | -11.52 | 152 | 46.1 | -17.18 | -2.96 | -22.24 | 362 |
| 40 | Agent (aggressive) | meta | 87.92 | -12.08 | 41 | 34.1 | -3.30 | -0.78 | -13.58 | 118 |
| 41 | Keltner breakout · 1h | breakout | 87.71 | -12.29 | 56 | 23.2 | -11.97 | -1.66 | -27.31 | 200 |
| 42 | Triple EMA stack · 1h | trend | 87.61 | -12.39 | 85 | 15.3 | -21.71 | -3.03 | -33.01 | 230 |
| 43 | Supertrend · 1h | trend | 87.43 | -12.56 | 86 | 12.8 | -22.80 | -4.67 | -26.48 | 214 |
| 44 | Opening range 15m | breakout | 86.52 | -13.48 | 250 | 24.8 | -17.05 | -4.43 | -21.40 | 702 |
| 45 | MACD cross · 1h | trend | 86.15 | -13.85 | 189 | 20.6 | -26.06 | -4.86 | -32.65 | 469 |
| 46 | Z-score reversion · 1h | reversion | 85.47 | -14.53 | 91 | 30.8 | -13.95 | -2.27 | -21.32 | 197 |
| 47 | OBV trend · 1h | momentum | 85.47 | -14.53 | 179 | 17.9 | -22.81 | -3.12 | -34.82 | 319 |
| 48 | MFI reversion · 1h | reversion | 84.77 | -15.23 | 209 | 31.1 | -17.68 | -2.76 | -21.34 | 139 |
| 49 | MACD zero-line · 1h | trend | 84.23 | -15.77 | 87 | 14.9 | -24.91 | -4.98 | -25.19 | 219 |
| 50 | Agent (ML meta-label) | meta | 83.99 | -16.01 | 675 | 18.7 | -10.62 | -1.86 | -16.33 | 396 |
| 51 | Donchian 20/10 · 1h | breakout | 83.80 | -16.20 | 81 | 17.3 | -1.02 | 0.09 | -25.26 | 214 |
| 52 | Max aggression: 1-day momentum | meta | 83.08 | -16.92 | 15 | 33.3 | -15.32 | -0.56 | -37.31 | 42 |
| 53 | Bollinger reversion · 1h | reversion | 82.78 | -17.23 | 157 | 34.4 | -27.86 | -5.33 | -33.53 | 349 |
| 54 | Three white soldiers | momentum | 82.64 | -17.36 | 230 | 19.1 | -47.29 | -18.83 | -47.43 | 602 |
| 55 | Williams %R · 1h | reversion | 82.21 | -17.79 | 182 | 42.9 | -33.51 | -5.32 | -36.50 | 533 |
| 56 | ROC + volume · 1h | momentum | 81.50 | -18.50 | 197 | 20.8 | -18.56 | -2.53 | -33.77 | 390 |
| 57 | CCI reversion · 1h | reversion | 80.86 | -19.14 | 163 | 39.3 | -19.80 | -2.50 | -27.44 | 440 |
| 58 | RSI(14) reversion · 1h | reversion | 80.41 | -19.59 | 75 | 21.3 | -14.47 | -2.57 | -22.27 | 178 |
| 59 | EMA 9/21 cross · 1h | trend | 80.27 | -19.73 | 134 | 11.2 | -29.20 | -6.04 | -29.55 | 314 |
| 60 | Heikin-Ashi · 1h | trend | 79.04 | -20.96 | 223 | 21.5 | -36.49 | -6.07 | -44.77 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.98 | -22.02 | 433 | 20.8 | -39.58 | -6.20 | -48.18 | 1246 |
| 62 | Candlestick reversal · 1h | reversion | 77.46 | -22.54 | 213 | 27.2 | -36.01 | -6.49 | -37.48 | 535 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 590 | 22.5 | -75.75 | -17.89 | -78.03 | 1730 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.48 | -17.54 | -64.19 | 876 |
| 65 | Squeeze breakout | breakout | 60.78 | -39.22 | 458 | 14.4 | -63.65 | -20.20 | -65.58 | 1195 |
| 66 | Donchian 55/20 | breakout | 59.20 | -40.80 | 474 | 18.6 | -67.90 | -13.54 | -72.80 | 1261 |
| 67 | RSI(14) reversion | reversion | 57.97 | -42.03 | 703 | 25.0 | -74.65 | -16.57 | -74.80 | 1607 |
| 68 | EMA 20/50 cross | trend | 57.05 | -42.95 | 497 | 19.3 | -75.37 | -13.88 | -80.26 | 1421 |
| 69 | VWAP reversion | reversion | 53.85 | -46.16 | 743 | 25.0 | -72.23 | -14.90 | -72.88 | 1511 |
| 70 | Keltner breakout | breakout | 51.56 | -48.44 | 667 | 16.3 | -82.48 | -26.01 | -83.37 | 1812 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.62 | -98.65 | 5288 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.06 | -27.82 | -93.67 | 2560 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.23 | -19.82 | -88.04 | 1893 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.76 | -22.55 | -91.02 | 2337 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.89 | -25.41 | -91.01 | 2266 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -31.85 | -97.52 | 3484 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.52 | -34.23 | -96.71 | 3574 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -27.64 | -94.47 | 2527 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.00 | -24.67 | -82.93 | 1696 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.87 | -99.37 | 5755 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.07 | -25.14 | -91.91 | 2615 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.13 | -31.57 | -96.14 | 3485 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.97 | -99.74 | 6185 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.70 | -29.56 | -91.74 | 2327 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -36.15 | -97.59 | 3623 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.37 | -98.46 | 4707 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.64 | -32.30 | -93.88 | 2791 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.99 | -99.53 | 6174 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.88 | -22.40 | -86.94 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.95 | -26.78 | -87.99 | 2141 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.81 | -31.93 | -95.82 | 3747 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.88 | -32.19 | -88.97 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.21 | -95.73 | 4114 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.53 | -99.90 | 8281 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T18:55 | Agent (ML meta-label) | buy | COIN | 5.25 | — | following EMA 20/50 cross |
| 2026-10-19T18:55 | Squeeze breakout | sell | AAPL | 15.19 | -0.00 | stop-loss |
| 2026-10-19T18:51 | Agent (ML meta-label) | buy | SQQQ | 4.52 | — | rebalance up |
| 2026-10-19T18:51 | Agent (ML meta-label) | sell | COIN | 5.19 | -0.13 | selected signal exited |
| 2026-10-19T18:51 | Keltner breakout | sell | AAPL | 12.86 | -0.04 | exit signal |
| 2026-10-19T18:41 | VWAP reversion | buy | AMD | 5.40 | — | entry signal |
| 2026-10-19T18:41 | VWAP reversion | sell | ETH-USD | 2.71 | -0.01 | rebalance down |
| 2026-10-19T18:41 | VWAP reversion | sell | COIN | 2.69 | -0.01 | rebalance down |
| 2026-10-19T18:41 | RSI(14) reversion | buy | AMD | 14.44 | — | entry signal |
| 2026-10-19T18:36 | VWAP reversion | buy | MSTR | 13.40 | — | entry signal |
| 2026-10-19T18:36 | Gap and go | sell | AMZN | 23.36 | -0.03 | stop-loss |
| 2026-10-19T18:36 | EMA 20/50 cross | buy | SQQQ | 5.70 | — | entry signal |
| 2026-10-19T18:36 | EMA 20/50 cross | sell | NVDA | 3.34 | -0.01 | exit signal |
| 2026-10-19T18:30 | Agent (ML meta-label) | buy | AMZN | 5.24 | — | entry |
| 2026-10-19T18:30 | Agent (ML meta-label) | sell | TSLA | 5.23 | -0.02 | selected signal exited |
| 2026-10-19T18:30 | Agent | sell | BITX | 18.07 | -0.08 | selected signal exited |
| 2026-10-19T18:30 | CCI reversion · 1h | buy | META | 4.03 | — | entry signal |
| 2026-10-19T18:30 | CCI reversion · 1h | buy | AAPL | 4.03 | — | entry signal |
| 2026-10-19T18:30 | Connors RSI(2) · 1h | sell | SQQQ | 22.56 | 0.26 | exit signal |
| 2026-10-19T18:30 | Candlestick reversal · 1h | buy | MSTR | 6.66 | — | entry |
| 2026-10-19T18:30 | OBV trend · 1h | buy | AAPL | 21.31 | — | entry |
| 2026-10-19T18:30 | VWAP momentum · 1h | buy | SQQQ | 19.48 | — | entry signal |
| 2026-10-19T18:30 | VWAP momentum · 1h | buy | META | 19.50 | — | entry signal |
| 2026-10-19T18:30 | VWAP momentum · 1h | sell | TSLA | 19.53 | -0.05 | exit signal |
| 2026-10-19T18:30 | VWAP momentum · 1h | sell | PLTR | 19.45 | -0.12 | exit signal |
| 2026-10-19T18:30 | Trend pullback · 1h | buy | MSFT | 24.14 | — | entry signal |
| 2026-10-19T18:30 | Heikin-Ashi · 1h | buy | TSLA | 4.51 | — | rebalance up |
| 2026-10-19T18:30 | Heikin-Ashi · 1h | buy | PLTR | 4.55 | — | rebalance up |
| 2026-10-19T18:30 | Heikin-Ashi · 1h | buy | MSFT | 4.46 | — | rebalance up |
| 2026-10-19T18:30 | Heikin-Ashi · 1h | buy | LABU | 4.55 | — | rebalance up |
| 2026-10-19T18:30 | Heikin-Ashi · 1h | buy | AMZN | 4.50 | — | rebalance up |
| 2026-10-19T18:30 | Heikin-Ashi · 1h | sell | NVDA | 11.27 | -0.05 | exit signal |
| 2026-10-19T18:30 | Heikin-Ashi · 1h | sell | GOOGL | 11.30 | -0.03 | exit signal |
| 2026-10-19T18:30 | EMA 9/21 cross · 1h | buy | TSLA | 13.29 | — | entry signal |
| 2026-10-19T18:30 | EMA 9/21 cross · 1h | buy | AAPL | 13.35 | — | entry signal |
| 2026-10-19T18:30 | EMA 9/21 cross · 1h | sell | XRP-USD | 6.63 | -0.06 | rebalance down |
| 2026-10-19T18:30 | EMA 9/21 cross · 1h | sell | SOL-USD | 6.66 | -0.06 | rebalance down |
| 2026-10-19T18:30 | EMA 9/21 cross · 1h | sell | DOGE-USD | 6.66 | -0.09 | rebalance down |
| 2026-10-19T18:30 | EMA 9/21 cross · 1h | sell | AMZN | 6.69 | -0.03 | rebalance down |
| 2026-10-19T18:30 | VWAP reversion | buy | DOGE-USD | 13.42 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 18:55:05.000115+00:00 -> 2026-10-19 19:05:05.000115+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
