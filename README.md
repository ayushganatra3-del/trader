# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T14:55:05.000130+00:00 · 28492 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.00 (-9.00%)

Closed trades 78, win rate 38.5%, fees £2.73, max drawdown -9.42%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.40 | +0.09 |
| SQQQ | 36.23 | -0.24 |

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

Today: 15588 decisions in 2205 calls, $0.2047 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T14:55 | 3 / 19 / 8 | cash |  |
| Breezy | 2026-10-19T14:55 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-19T14:55 | 2 / 27 / 1 | COIN 73% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.69 | 4.69 | 0 | — | 5.79 | 2.83 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.03 | 2.03 | 72 | 45.8 | -8.02 | -2.21 | -13.79 | 136 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.07 | 0.07 | 0 | — | 2.57 | 1.08 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.22 | -0.78 | 0 | — | -0.10 | -0.01 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.98 | -1.02 | 3 | 33.3 | 3.21 | 0.77 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.18 | -1.82 | 54 | 31.5 | 3.10 | 1.71 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.83 | -2.17 | 111 | 32.4 | -2.56 | -1.29 | -4.94 | 279 |
| 14 | Hold BTC | benchmark | 97.47 | -2.53 | 0 | — | 26.28 | 3.13 | -8.68 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.19 | -2.81 | 36 | 16.7 | -10.17 | -1.64 | -20.69 | 107 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.17 | -2.83 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.95 | -2.23 | -5.83 | 1 |
| 18 | Copy: Insider buying | copy | 96.44 | -3.56 | 23 | 43.5 | -14.84 | -2.69 | -20.62 | 73 |
| 19 | Trend pullback · 1h | trend | 96.27 | -3.73 | 87 | 24.1 | -19.74 | -5.84 | -20.58 | 135 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.10 | -3.90 | 0 | — | -7.03 | -2.78 | -7.55 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 94.14 | -5.86 | 8 | 37.5 | -21.03 | -1.78 | -34.64 | 26 |
| 23 | Daily: Momentum burst | daily | 93.75 | -6.25 | 6 | 16.7 | -4.78 | -0.56 | -20.58 | 40 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 1.99 | 0.55 | -9.46 | 95 |
| 25 | ADX DI cross · 1h | trend | 93.43 | -6.57 | 84 | 19.0 | -12.47 | -2.38 | -14.53 | 255 |
| 26 | Gap and go | momentum | 93.43 | -6.58 | 70 | 12.9 | 9.74 | 2.45 | -6.54 | 202 |
| 27 | Daily: Bullish score | daily | 92.11 | -7.89 | 7 | 0.0 | -2.51 | -0.12 | -13.10 | 12 |
| 28 | Parabolic SAR · 1h | trend | 91.88 | -8.12 | 101 | 22.8 | -12.02 | -2.00 | -23.43 | 270 |
| 29 | Volume breakout · 1h | breakout | 91.84 | -8.16 | 78 | 23.1 | -1.68 | -0.09 | -14.31 | 111 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.62 | -2.40 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 91.17 | -8.83 | 196 | 29.6 | -11.44 | -3.15 | -17.60 | 560 |
| 32 | Agent | meta | 91.00 | -9.00 | 78 | 38.5 | -9.31 | -5.60 | -12.05 | 237 |
| 33 | Bollinger breakout · 1h | breakout | 90.73 | -9.27 | 84 | 28.6 | -2.15 | -0.18 | -15.16 | 264 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 90.31 | -9.69 | 0 | — | 3.90 | 0.74 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 90.26 | -9.74 | 58 | 13.8 | -18.60 | -3.39 | -20.37 | 129 |
| 36 | RSI momentum · 1h | momentum | 89.68 | -10.32 | 78 | 16.7 | -17.74 | -3.11 | -28.14 | 215 |
| 37 | Connors RSI(2) · 1h | reversion | 89.18 | -10.82 | 149 | 40.9 | -23.45 | -7.02 | -24.79 | 207 |
| 38 | Agent (aggressive) | meta | 88.75 | -11.25 | 39 | 33.3 | -5.53 | -1.89 | -9.01 | 114 |
| 39 | Ichimoku · 1h | trend | 88.73 | -11.27 | 55 | 14.5 | -17.47 | -3.29 | -18.08 | 113 |
| 40 | Stochastic reversion · 1h | reversion | 88.67 | -11.33 | 151 | 45.7 | -17.39 | -2.96 | -22.24 | 370 |
| 41 | Supertrend · 1h | trend | 87.71 | -12.29 | 85 | 11.8 | -23.54 | -4.89 | -27.31 | 216 |
| 42 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 56 | 23.2 | -11.76 | -1.53 | -29.37 | 205 |
| 43 | Triple EMA stack · 1h | trend | 87.42 | -12.58 | 85 | 15.3 | -22.01 | -2.95 | -33.79 | 218 |
| 44 | Opening range 15m | breakout | 86.62 | -13.38 | 246 | 25.2 | -16.54 | -4.27 | -21.40 | 697 |
| 45 | MACD cross · 1h | trend | 86.55 | -13.45 | 186 | 21.0 | -25.18 | -4.61 | -31.95 | 469 |
| 46 | Z-score reversion · 1h | reversion | 85.99 | -14.01 | 91 | 30.8 | -13.03 | -2.06 | -21.32 | 197 |
| 47 | OBV trend · 1h | momentum | 85.84 | -14.16 | 174 | 17.8 | -23.12 | -3.19 | -34.55 | 316 |
| 48 | Max aggression: 1-day momentum | meta | 84.95 | -15.05 | 15 | 33.3 | -13.30 | -0.42 | -37.31 | 42 |
| 49 | MFI reversion · 1h | reversion | 84.86 | -15.14 | 209 | 31.1 | -17.12 | -2.66 | -21.34 | 138 |
| 50 | MACD zero-line · 1h | trend | 84.46 | -15.54 | 86 | 15.1 | -24.75 | -4.95 | -25.14 | 218 |
| 51 | Agent (ML meta-label) | meta | 84.16 | -15.84 | 662 | 18.7 | -8.58 | -1.22 | -15.27 | 364 |
| 52 | Donchian 20/10 · 1h | breakout | 83.50 | -16.50 | 81 | 17.3 | -0.52 | 0.15 | -23.17 | 217 |
| 53 | Three white soldiers | momentum | 82.54 | -17.46 | 225 | 18.2 | -47.44 | -19.02 | -47.48 | 602 |
| 54 | Williams %R · 1h | reversion | 82.53 | -17.47 | 182 | 42.9 | -33.15 | -5.21 | -36.50 | 530 |
| 55 | Bollinger reversion · 1h | reversion | 82.13 | -17.87 | 153 | 32.7 | -29.26 | -5.78 | -33.16 | 352 |
| 56 | ROC + volume · 1h | momentum | 81.33 | -18.67 | 197 | 20.8 | -14.13 | -1.80 | -29.10 | 393 |
| 57 | CCI reversion · 1h | reversion | 81.08 | -18.92 | 161 | 38.5 | -19.06 | -2.42 | -27.44 | 444 |
| 58 | RSI(14) reversion · 1h | reversion | 80.88 | -19.12 | 75 | 21.3 | -12.56 | -2.14 | -22.27 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 80.66 | -19.34 | 131 | 11.5 | -19.11 | -3.23 | -28.90 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 79.91 | -20.09 | 212 | 22.6 | -35.17 | -5.85 | -43.58 | 667 |
| 61 | VWAP momentum · 1h | momentum | 78.51 | -21.49 | 417 | 20.4 | -36.04 | -4.82 | -47.95 | 1247 |
| 62 | Candlestick reversal · 1h | reversion | 78.13 | -21.88 | 209 | 26.3 | -34.89 | -6.02 | -37.17 | 535 |
| 63 | ROC + volume | momentum | 62.52 | -37.48 | 573 | 22.0 | -75.51 | -17.33 | -78.19 | 1727 |
| 64 | Volume breakout | breakout | 61.82 | -38.18 | 350 | 12.9 | -62.57 | -17.68 | -64.14 | 875 |
| 65 | Squeeze breakout | breakout | 60.74 | -39.26 | 455 | 14.1 | -62.07 | -15.79 | -65.58 | 1207 |
| 66 | Donchian 55/20 | breakout | 59.59 | -40.41 | 463 | 17.9 | -68.07 | -14.08 | -72.80 | 1275 |
| 67 | RSI(14) reversion | reversion | 57.99 | -42.01 | 695 | 24.9 | -74.61 | -16.53 | -74.77 | 1608 |
| 68 | EMA 20/50 cross | trend | 57.23 | -42.77 | 489 | 18.8 | -75.65 | -14.54 | -80.26 | 1431 |
| 69 | VWAP reversion | reversion | 53.67 | -46.33 | 731 | 24.6 | -72.35 | -14.98 | -72.95 | 1507 |
| 70 | Keltner breakout | breakout | 51.51 | -48.49 | 653 | 15.8 | -82.55 | -26.10 | -83.37 | 1812 |
| 71 | AI bee: Boozy | ai | 50.62 | -49.38 | 346 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -29.87 | -98.66 | 5335 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.25 | -29.71 | -93.67 | 2575 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.05 | -19.81 | -87.84 | 1888 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.97 | -23.93 | -90.92 | 2341 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.99 | -25.67 | -91.05 | 2275 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.33 | -97.46 | 3492 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.58 | -35.62 | -96.71 | 3587 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.52 | -26.65 | -94.85 | 2598 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.49 | -22.68 | -82.83 | 1703 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.36 | -99.38 | 5748 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.11 | -25.31 | -91.85 | 2622 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.10 | -31.68 | -96.11 | 3486 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.72 | -99.74 | 6186 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.38 | -28.76 | -91.50 | 2341 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -38.49 | -97.54 | 3633 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.54 | -98.48 | 4698 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.56 | -32.47 | -93.78 | 2788 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.21 | -99.53 | 6163 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.71 | -22.18 | -86.79 | 2153 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.86 | -26.68 | -87.89 | 2139 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.62 | -95.89 | 3763 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.88 | -32.34 | -89.02 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -33.50 | -95.76 | 4099 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.48 | -99.90 | 8269 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T14:55 | Agent (ML meta-label) | sell | LABU | 14.07 | 0.04 | selected signal exited |
| 2026-10-19T14:55 | VWAP reversion | buy | SOXL | 3.51 | — | rebalance up |
| 2026-10-19T14:55 | VWAP reversion | buy | SOL-USD | 3.60 | — | rebalance up |
| 2026-10-19T14:55 | VWAP reversion | buy | ETH-USD | 3.00 | — | rebalance up |
| 2026-10-19T14:55 | VWAP reversion | buy | COIN | 3.00 | — | rebalance up |
| 2026-10-19T14:55 | VWAP reversion | buy | BTC-USD | 3.61 | — | rebalance up |
| 2026-10-19T14:55 | VWAP reversion | buy | BITX | 3.59 | — | rebalance up |
| 2026-10-19T14:55 | VWAP reversion | sell | ETHU | 6.00 | 0.04 | exit signal |
| 2026-10-19T14:55 | RSI(14) reversion | buy | XRP-USD | 3.33 | — | rebalance up |
| 2026-10-19T14:55 | RSI(14) reversion | buy | SQQQ | 3.34 | — | rebalance up |
| 2026-10-19T14:55 | RSI(14) reversion | buy | SOL-USD | 3.31 | — | rebalance up |
| 2026-10-19T14:55 | RSI(14) reversion | buy | ETH-USD | 3.32 | — | rebalance up |
| 2026-10-19T14:55 | RSI(14) reversion | buy | BTC-USD | 3.34 | — | rebalance up |
| 2026-10-19T14:55 | RSI(14) reversion | sell | META | 8.34 | 0.05 | exit signal |
| 2026-10-19T14:50 | Agent (ML meta-label) | buy | LABU | 14.02 | — | entry |
| 2026-10-19T14:50 | VWAP reversion | sell | META | 5.99 | 0.03 | exit signal |
| 2026-10-19T14:50 | VWAP reversion | sell | DOGE-USD | 5.34 | 0.00 | exit signal |
| 2026-10-19T14:50 | RSI(14) reversion | sell | DOGE-USD | 8.30 | 0.01 | exit signal |
| 2026-10-19T14:50 | Volume breakout | buy | MSFT | 15.46 | — | entry signal |
| 2026-10-19T14:45 | Gap and go | buy | QQQ | 23.30 | — | entry signal |
| 2026-10-19T14:41 | Agent (aggressive) | buy | SQQQ | 44.51 | — | rebalance up |
| 2026-10-19T14:41 | Agent | buy | SQQQ | 18.13 | — | rebalance up |
| 2026-10-19T14:41 | VWAP reversion | buy | COIN | 5.94 | — | entry signal |
| 2026-10-19T14:41 | VWAP reversion | sell | TNA | 5.33 | -0.00 | target is flat |
| 2026-10-19T14:41 | Opening range 30m | buy | GOOGL | 9.09 | — | entry |
| 2026-10-19T14:41 | Opening range 30m | sell | UPRO | 10.03 | -0.05 | exit signal |
| 2026-10-19T14:41 | Gap and go | sell | NVDA | 23.24 | -0.09 | exit signal |
| 2026-10-19T14:35 | EMA 20/50 cross · 1h | sell | XRP-USD | 22.53 | -0.41 | stop-loss |
| 2026-10-19T14:35 | Opening range 15m | buy | NVDA | 9.51 | — | entry |
| 2026-10-19T14:35 | Opening range 15m | buy | GOOGL | 9.59 | — | entry |
| 2026-10-19T14:35 | Opening range 15m | sell | UPRO | 9.53 | -0.05 | exit signal |
| 2026-10-19T14:35 | Opening range 15m | sell | SPY | 9.57 | -0.03 | exit signal |
| 2026-10-19T14:35 | Gap and go | buy | TQQQ | 4.71 | — | rebalance up |
| 2026-10-19T14:35 | Gap and go | buy | NVDA | 13.88 | — | rebalance up |
| 2026-10-19T14:35 | Gap and go | sell | UPRO | 23.18 | -0.11 | exit signal |
| 2026-10-19T14:35 | Gap and go | sell | QQQ | 23.28 | -0.05 | exit signal |
| 2026-10-19T14:35 | ROC + volume | buy | MSFT | 1.42 | — | entry |
| 2026-10-19T14:35 | ROC + volume | buy | GOOGL | 8.90 | — | entry signal |
| 2026-10-19T14:35 | ROC + volume | sell | LABU | 10.31 | 0.21 | exit signal |
| 2026-10-19T14:30 | Agent (ML meta-label) | sell | AMZN | 14.24 | 0.32 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 14:55:05.000130+00:00 -> 2026-10-19 15:05:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
