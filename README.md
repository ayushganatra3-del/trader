# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T13:54:05.000140+00:00 · 30756 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.85 (-9.15%)

Closed trades 90, win rate 41.1%, fees £2.99, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 18.16 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.22 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 11433 decisions in 2031 calls, $0.1562 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T13:54 | 1 / 18 / 11 | cash |  |
| Breezy | 2026-10-21T13:54 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-21T13:54 | 4 / 22 / 4 | COIN 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Max aggression: 5-day momentum | meta | 106.58 | 6.58 | 10 | 50.0 | -2.65 | 0.09 | -34.64 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.36 | 6.36 | 0 | — | 8.41 | 3.89 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.43 | -0.03 | -8.92 | 26 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.20 | -0.80 | 4 | 50.0 | 7.07 | 1.55 | -7.93 | 8 |
| 10 | Hold SPY | benchmark | 99.12 | -0.88 | 0 | — | 0.53 | 0.35 | -3.13 | 1 |
| 11 | Hold BTC | benchmark | 98.97 | -1.03 | 0 | — | 16.48 | 2.34 | -8.68 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.82 | -1.18 | 62 | 35.5 | 2.17 | 1.28 | -2.29 | 64 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 98.49 | -1.51 | 0 | — | -0.75 | -0.23 | -5.02 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.40 | -1.93 | -5.83 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 96.94 | -3.06 | 0 | — | 0.48 | 0.26 | -5.31 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 96.81 | -3.19 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 18 | Agent (rotation) | meta | 96.08 | -3.92 | 114 | 31.6 | -6.33 | -3.17 | -8.13 | 294 |
| 19 | Donchian 55/20 · 1h | breakout | 95.90 | -4.09 | 40 | 15.0 | -14.51 | -2.91 | -15.93 | 100 |
| 20 | ADX DI cross · 1h | trend | 95.81 | -4.20 | 89 | 18.0 | -10.96 | -2.05 | -15.70 | 256 |
| 21 | Copy: Insider buying | copy | 95.75 | -4.25 | 25 | 40.0 | -12.21 | -2.10 | -20.62 | 72 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | Trend pullback · 1h | trend | 95.35 | -4.65 | 90 | 23.3 | -19.50 | -5.91 | -19.73 | 130 |
| 24 | Daily: Momentum burst | daily | 95.12 | -4.88 | 6 | 16.7 | -8.72 | -1.26 | -20.58 | 38 |
| 25 | Gap and go | momentum | 93.38 | -6.62 | 79 | 17.7 | 4.59 | 1.47 | -6.57 | 202 |
| 26 | Squeeze breakout · 1h | breakout | 92.81 | -7.19 | 46 | 21.7 | -2.10 | -0.43 | -11.48 | 98 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.79 | -7.21 | 0 | — | 2.65 | 0.57 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.71 | -7.29 | 106 | 21.7 | -17.14 | -3.64 | -20.69 | 271 |
| 29 | Bollinger breakout · 1h | breakout | 92.20 | -7.80 | 87 | 29.9 | -11.00 | -2.00 | -16.55 | 255 |
| 30 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -12.22 | -3.57 | -17.26 | 555 |
| 31 | Daily: Bullish score | daily | 91.27 | -8.73 | 8 | 0.0 | -5.59 | -0.59 | -13.10 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.06 | -2.09 | -16.91 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.98 | -9.02 | 87 | 24.1 | -12.93 | -2.32 | -14.22 | 104 |
| 34 | Agent | meta | 90.85 | -9.15 | 90 | 41.1 | -7.94 | -3.71 | -11.06 | 222 |
| 35 | RSI momentum · 1h | momentum | 90.10 | -9.90 | 83 | 15.7 | -23.06 | -4.54 | -24.70 | 218 |
| 36 | Connors RSI(2) · 1h | reversion | 89.74 | -10.26 | 155 | 41.9 | -21.76 | -6.45 | -23.42 | 195 |
| 37 | Supertrend · 1h | trend | 89.51 | -10.49 | 88 | 12.5 | -21.62 | -4.26 | -26.73 | 221 |
| 38 | EMA 20/50 cross · 1h | trend | 89.44 | -10.56 | 62 | 12.9 | -20.13 | -3.54 | -23.33 | 135 |
| 39 | Stochastic reversion · 1h | reversion | 88.96 | -11.04 | 165 | 46.7 | -13.39 | -2.18 | -22.24 | 362 |
| 40 | Keltner breakout · 1h | breakout | 88.71 | -11.29 | 60 | 21.7 | -18.98 | -3.68 | -26.37 | 196 |
| 41 | Opening range 15m | breakout | 88.21 | -11.79 | 270 | 29.3 | -16.73 | -4.51 | -19.78 | 693 |
| 42 | Agent (aggressive) | meta | 88.07 | -11.93 | 44 | 36.4 | -5.48 | -1.82 | -9.68 | 105 |
| 43 | Ichimoku · 1h | trend | 87.74 | -12.26 | 60 | 13.3 | -17.76 | -3.30 | -20.25 | 117 |
| 44 | MACD cross · 1h | trend | 87.30 | -12.70 | 197 | 20.8 | -25.36 | -4.79 | -30.20 | 471 |
| 45 | Z-score reversion · 1h | reversion | 85.89 | -14.11 | 96 | 30.2 | -12.58 | -2.00 | -21.32 | 195 |
| 46 | Donchian 20/10 · 1h | breakout | 85.81 | -14.19 | 81 | 17.3 | -19.77 | -3.63 | -29.10 | 218 |
| 47 | Triple EMA stack · 1h | trend | 85.66 | -14.34 | 91 | 14.3 | -30.63 | -5.67 | -31.37 | 228 |
| 48 | MFI reversion · 1h | reversion | 85.18 | -14.82 | 225 | 32.0 | -14.35 | -2.17 | -21.11 | 139 |
| 49 | MACD zero-line · 1h | trend | 84.85 | -15.14 | 91 | 15.4 | -25.10 | -4.83 | -27.32 | 221 |
| 50 | Agent (ML meta-label) | meta | 84.80 | -15.20 | 711 | 19.1 | -6.14 | -0.94 | -15.00 | 355 |
| 51 | OBV trend · 1h | momentum | 84.26 | -15.74 | 186 | 17.2 | -30.84 | -5.75 | -31.99 | 313 |
| 52 | ROC + volume · 1h | momentum | 82.49 | -17.51 | 208 | 22.6 | -26.40 | -4.75 | -33.11 | 385 |
| 53 | Three white soldiers | momentum | 82.36 | -17.64 | 252 | 19.4 | -46.37 | -18.13 | -47.10 | 609 |
| 54 | Bollinger reversion · 1h | reversion | 82.23 | -17.77 | 162 | 35.8 | -29.52 | -5.72 | -32.96 | 347 |
| 55 | Williams %R · 1h | reversion | 82.09 | -17.91 | 195 | 43.6 | -29.75 | -4.53 | -36.53 | 523 |
| 56 | CCI reversion · 1h | reversion | 81.51 | -18.49 | 178 | 41.6 | -18.16 | -2.28 | -27.44 | 441 |
| 57 | Heikin-Ashi · 1h | trend | 81.36 | -18.64 | 235 | 20.9 | -42.77 | -9.18 | -46.87 | 673 |
| 58 | EMA 9/21 cross · 1h | trend | 80.94 | -19.06 | 143 | 10.5 | -28.53 | -5.76 | -30.69 | 327 |
| 59 | RSI(14) reversion · 1h | reversion | 80.68 | -19.32 | 83 | 22.9 | -11.31 | -1.89 | -23.28 | 171 |
| 60 | Candlestick reversal · 1h | reversion | 78.47 | -21.53 | 226 | 28.8 | -37.42 | -6.64 | -40.35 | 537 |
| 61 | VWAP momentum · 1h | momentum | 78.33 | -21.67 | 467 | 20.6 | -45.47 | -8.26 | -51.81 | 1250 |
| 62 | Max aggression: 1-day momentum | meta | 75.50 | -24.50 | 17 | 29.4 | -35.58 | -2.25 | -41.21 | 42 |
| 63 | ROC + volume | momentum | 60.42 | -39.58 | 640 | 22.8 | -77.67 | -21.69 | -78.91 | 1726 |
| 64 | Volume breakout | breakout | 59.78 | -40.22 | 390 | 13.6 | -64.20 | -19.86 | -64.74 | 866 |
| 65 | RSI(14) reversion | reversion | 57.15 | -42.85 | 746 | 26.5 | -74.26 | -16.32 | -74.89 | 1614 |
| 66 | Squeeze breakout | breakout | 57.13 | -42.87 | 502 | 13.9 | -66.78 | -22.76 | -67.48 | 1222 |
| 67 | Donchian 55/20 | breakout | 56.58 | -43.42 | 515 | 18.8 | -71.71 | -18.63 | -73.91 | 1284 |
| 68 | EMA 20/50 cross | trend | 55.30 | -44.70 | 558 | 19.5 | -78.35 | -17.77 | -80.87 | 1456 |
| 69 | VWAP reversion | reversion | 53.60 | -46.40 | 757 | 25.2 | -71.22 | -14.39 | -72.15 | 1478 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.78 | -31.20 | -98.80 | 5328 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.96 | -33.69 | -94.19 | 2607 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.51 | -22.04 | -88.64 | 1901 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.91 | -26.22 | -91.65 | 2360 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.36 | -26.33 | -91.57 | 2264 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -34.19 | -97.76 | 3535 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.97 | -38.85 | -96.99 | 3625 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.43 | -27.82 | -94.61 | 2536 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.83 | -27.70 | -83.30 | 1717 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.08 | -99.38 | 5747 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.95 | -27.92 | -92.62 | 2631 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.97 | -31.68 | -95.97 | 3457 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.95 | -99.76 | 6187 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -29.65 | -91.85 | 2364 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.80 | -40.28 | -97.80 | 3617 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.23 | -98.48 | 4716 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.24 | -35.72 | -94.41 | 2810 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.24 | -27.27 | -84.37 | 1801 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.19 | -99.53 | 6183 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.20 | -87.01 | 2145 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.51 | -25.35 | -88.05 | 2144 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -32.62 | -95.93 | 3769 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -33.60 | -89.36 | 2105 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -33.44 | -95.77 | 4109 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.49 | -99.91 | 8298 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T13:50 | Day trade: Stocks in Play ORB | buy | TSLA | 24.71 | — | entry |
| 2026-10-21T13:50 | Agent (aggressive) | buy | TSLA | 44.05 | — | following Opening range 30m, Opening range 15m |
| 2026-10-21T13:50 | Agent | buy | TSLA | 18.17 | — | following Opening range 30m, Opening range 15m |
| 2026-10-21T13:50 | MFI reversion · 1h | sell | TECL | 21.24 | 0.19 | target is flat |
| 2026-10-21T13:50 | RSI(14) reversion | buy | GOOGL | 14.29 | — | entry signal |
| 2026-10-21T13:50 | RSI(14) reversion | sell | AMZN | 14.25 | -0.09 | stop-loss |
| 2026-10-21T13:50 | Opening range 15m | buy | TSLA | 17.65 | — | entry signal |
| 2026-10-21T13:50 | Opening range 15m | buy | META | 17.65 | — | entry signal |
| 2026-10-21T13:50 | Opening range 15m | buy | LABU | 17.65 | — | entry signal |
| 2026-10-21T13:50 | Opening range 15m | buy | COIN | 17.65 | — | entry signal |
| 2026-10-21T13:50 | Opening range 15m | buy | BITX | 17.65 | — | entry signal |
| 2026-10-21T13:50 | Donchian 55/20 | buy | TSLA | 5.12 | — | entry signal |
| 2026-10-21T13:50 | Donchian 55/20 | buy | PLTR | 5.15 | — | entry |
| 2026-10-21T13:50 | Donchian 55/20 | buy | LABU | 5.15 | — | entry |
| 2026-10-21T13:50 | Donchian 55/20 | buy | BITX | 5.15 | — | entry signal |
| 2026-10-21T13:50 | Donchian 55/20 | sell | XRP-USD | 2.92 | 0.01 | rebalance down |
| 2026-10-21T13:50 | Donchian 55/20 | sell | TNA | 2.91 | -0.00 | rebalance down |
| 2026-10-21T13:50 | Donchian 55/20 | sell | MSTR | 2.92 | -0.00 | rebalance down |
| 2026-10-21T13:50 | Donchian 55/20 | sell | META | 2.97 | 0.01 | rebalance down |
| 2026-10-21T13:50 | Donchian 55/20 | sell | IWM | 2.93 | -0.00 | rebalance down |
| 2026-10-21T13:50 | Donchian 55/20 | sell | ETH-USD | 2.93 | -0.01 | rebalance down |
| 2026-10-21T13:50 | Donchian 55/20 | sell | COIN | 2.98 | 0.02 | rebalance down |
| 2026-10-21T13:50 | Gap and go | buy | TSLA | 14.03 | — | entry signal |
| 2026-10-21T13:50 | Gap and go | buy | TNA | 18.68 | — | entry signal |
| 2026-10-21T13:50 | Gap and go | buy | BITX | 18.68 | — | entry signal |
| 2026-10-21T13:50 | Gap and go | sell | COIN | 4.81 | 0.03 | rebalance down |
| 2026-10-21T13:50 | ROC + volume | buy | BITX | 4.32 | — | entry |
| 2026-10-21T13:50 | ROC + volume | sell | UPRO | 5.03 | 0.00 | target is flat |
| 2026-10-21T13:45 | RSI(14) reversion | buy | SQQQ | 14.33 | — | entry signal |
| 2026-10-21T13:45 | Gap and go | sell | TNA | 23.22 | -0.14 | exit signal |
| 2026-10-21T13:41 | Day trade: Stocks in Play ORB | buy | PLTR | 24.68 | — | entry |
| 2026-10-21T13:41 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 104.25 | -0.08 | target is flat |
| 2026-10-21T13:41 | Ichimoku · 1h | buy | AMZN | 4.39 | — | rebalance up |
| 2026-10-21T13:41 | RSI(14) reversion | buy | AMZN | 14.34 | — | entry signal |
| 2026-10-21T13:41 | Squeeze breakout | buy | TSLA | 4.76 | — | entry signal |
| 2026-10-21T13:41 | Squeeze breakout | buy | TQQQ | 4.76 | — | entry signal |
| 2026-10-21T13:41 | Squeeze breakout | buy | TNA | 4.76 | — | entry signal |
| 2026-10-21T13:41 | Squeeze breakout | buy | SPY | 4.76 | — | entry signal |
| 2026-10-21T13:41 | Squeeze breakout | buy | SOXL | 4.76 | — | entry signal |
| 2026-10-21T13:41 | Squeeze breakout | buy | QQQ | 4.76 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 13:54:05.000140+00:00 -> 2026-10-21 14:04:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
