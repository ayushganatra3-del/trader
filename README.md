# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T10:25:05.000121+00:00 · 27079 ticks

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
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7917 decisions in 1584 calls, $0.1106 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T10:25 | 3 / 2 / 0 | SOL-USD 18% |  |
| Breezy | 2026-10-18T10:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T10:25 | 3 / 2 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 2.34 | +2.45% | 9 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| VWAP reversion | ETHU | 1.80 | +2.34% | 5 |
| VWAP momentum · 1h | SQQQ | 1.77 | +10.81% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.29 | -3.28 | -13.79 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 0.65 | 0.28 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.37 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 97.49 | -2.51 | 0 | — | 28.72 | 3.39 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -5.72 | -2.90 | -6.96 | 289 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -19.52 | -5.88 | -19.70 | 140 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.58 | -5.42 | 82 | 19.5 | -3.09 | -0.35 | -13.93 | 255 |
| 24 | Squeeze breakout · 1h | breakout | 93.69 | -6.31 | 41 | 24.4 | 3.69 | 0.85 | -9.46 | 101 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.37 | 2.38 | -6.56 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -12.68 | -1.95 | -21.23 | 126 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -3.14 | -0.29 | -22.55 | 272 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.41 | -1.86 | -8.25 | 117 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -11.63 | -6.35 | -14.52 | 238 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.57 | -0.07 | -14.55 | 114 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.13 | -8.87 | 76 | 17.1 | 2.31 | 0.48 | -26.55 | 217 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.88 | 1.07 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -12.46 | -1.31 | -33.23 | 228 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.38 | -17.98 | 112 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Supertrend · 1h | trend | 89.24 | -10.76 | 84 | 11.9 | -22.38 | -4.63 | -26.17 | 208 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.80 | -0.93 | -27.05 | 201 |
| 42 | MACD cross · 1h | trend | 88.18 | -11.82 | 177 | 22.0 | -15.19 | -1.94 | -29.77 | 459 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -24.91 | -7.65 | -25.57 | 231 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.96 | -0.63 | -33.87 | 316 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.55 | -13.45 | 143 | 44.1 | -20.95 | -3.83 | -22.11 | 368 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.13 | -4.32 | -23.77 | 216 |
| 49 | Donchian 20/10 · 1h | breakout | 84.98 | -15.02 | 78 | 17.9 | 2.19 | 0.47 | -21.63 | 213 |
| 50 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 205 | 30.2 | -21.68 | -3.59 | -22.26 | 142 |
| 51 | Three white soldiers | momentum | 83.69 | -16.30 | 215 | 18.6 | -47.64 | -20.18 | -47.66 | 607 |
| 52 | Z-score reversion · 1h | reversion | 83.34 | -16.66 | 86 | 31.4 | -15.71 | -2.74 | -20.30 | 185 |
| 53 | ROC + volume · 1h | momentum | 82.93 | -17.07 | 192 | 21.4 | -12.63 | -1.66 | -27.12 | 396 |
| 54 | Agent (ML meta-label) | meta | 82.42 | -17.58 | 649 | 18.2 | -12.57 | -1.79 | -20.79 | 417 |
| 55 | EMA 9/21 cross · 1h | trend | 81.70 | -18.30 | 129 | 11.6 | -6.59 | -0.57 | -30.14 | 315 |
| 56 | VWAP momentum · 1h | momentum | 81.22 | -18.78 | 402 | 20.4 | -37.63 | -5.76 | -45.74 | 1261 |
| 57 | Heikin-Ashi · 1h | trend | 81.10 | -18.90 | 205 | 22.4 | -32.29 | -5.30 | -42.08 | 677 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.81 | -36.60 | 531 |
| 59 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.14 | -2.51 | -21.70 | 166 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 146 | 31.5 | -30.68 | -6.39 | -32.71 | 348 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.04 | -2.61 | -26.62 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.87 | -6.52 | -36.35 | 544 |
| 63 | Volume breakout | breakout | 62.82 | -37.18 | 334 | 12.9 | -63.30 | -18.39 | -63.58 | 880 |
| 64 | ROC + volume | momentum | 62.21 | -37.79 | 557 | 21.7 | -75.84 | -17.82 | -77.75 | 1725 |
| 65 | Squeeze breakout | breakout | 61.94 | -38.06 | 441 | 14.5 | -62.85 | -17.96 | -64.75 | 1215 |
| 66 | RSI(14) reversion | reversion | 60.55 | -39.45 | 671 | 25.5 | -73.98 | -16.45 | -74.07 | 1622 |
| 67 | Donchian 55/20 | breakout | 59.49 | -40.51 | 450 | 17.3 | -69.23 | -14.76 | -72.50 | 1286 |
| 68 | EMA 20/50 cross | trend | 57.27 | -42.73 | 475 | 18.5 | -76.97 | -15.27 | -79.91 | 1443 |
| 69 | VWAP reversion | reversion | 54.46 | -45.54 | 703 | 23.8 | -73.04 | -15.49 | -73.25 | 1510 |
| 70 | Keltner breakout | breakout | 52.54 | -47.46 | 629 | 15.6 | -83.23 | -27.49 | -83.27 | 1829 |
| 71 | AI bee: Boozy | ai | 52.38 | -47.62 | 331 | 6.0 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.46 | -98.65 | 5334 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.57 | -31.01 | -93.58 | 2600 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.56 | -20.54 | -87.64 | 1917 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.41 | -24.98 | -90.80 | 2366 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.11 | -26.37 | -91.11 | 2296 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -33.05 | -97.47 | 3528 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -37.54 | -96.78 | 3630 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -27.97 | -94.57 | 2608 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.10 | -23.63 | -82.38 | 1735 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.36 | -99.39 | 5813 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.31 | -26.14 | -91.51 | 2644 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.06 | -32.02 | -96.06 | 3516 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.31 | -99.74 | 6243 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -29.83 | -91.77 | 2370 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -39.53 | -97.51 | 3664 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.45 | -98.48 | 4770 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.75 | -34.11 | -93.76 | 2813 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.39 | -99.53 | 6247 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.62 | -22.26 | -86.63 | 2166 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.18 | -27.47 | -88.18 | 2163 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -33.22 | -95.89 | 3814 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -34.71 | -89.44 | 2111 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.84 | -34.67 | -95.85 | 4161 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.73 | -99.89 | 8311 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T10:25 | Keltner breakout | sell | XRP-USD | 10.41 | -0.07 | stop-loss |
| 2026-10-18T10:10 | Volume breakout | sell | ETH-USD | 15.66 | -0.09 | exit signal |
| 2026-10-18T10:10 | Keltner breakout | buy | XRP-USD | 10.47 | — | entry |
| 2026-10-18T10:10 | Keltner breakout | sell | SOL-USD | 2.63 | -0.01 | rebalance down |
| 2026-10-18T10:10 | Keltner breakout | sell | ETH-USD | 2.62 | -0.02 | rebalance down |
| 2026-10-18T10:05 | Agent (ML meta-label) | buy | XRP-USD | 5.14 | — | entry |
| 2026-10-18T10:05 | Volume breakout | sell | SOL-USD | 15.67 | -0.08 | exit signal |
| 2026-10-18T10:05 | Keltner breakout | buy | SOL-USD | 2.63 | — | rebalance up |
| 2026-10-18T10:05 | Keltner breakout | buy | ETH-USD | 2.64 | — | rebalance up |
| 2026-10-18T10:05 | Keltner breakout | sell | XRP-USD | 10.49 | -0.06 | stop-loss |
| 2026-10-18T10:00 | Squeeze breakout · 1h | buy | BTC-USD | 23.44 | — | entry signal |
| 2026-10-18T10:00 | RSI momentum · 1h | buy | BTC-USD | 22.80 | — | entry signal |
| 2026-10-18T10:00 | ROC + volume · 1h | buy | BTC-USD | 20.74 | — | entry signal |
| 2026-10-18T10:00 | VWAP momentum · 1h | buy | XRP-USD | 5.62 | — | entry signal |
| 2026-10-18T10:00 | VWAP momentum · 1h | buy | SOL-USD | 13.56 | — | entry signal |
| 2026-10-18T10:00 | VWAP momentum · 1h | buy | ETH-USD | 13.56 | — | entry signal |
| 2026-10-18T10:00 | VWAP momentum · 1h | buy | DOGE-USD | 13.56 | — | entry signal |
| 2026-10-18T10:00 | VWAP momentum · 1h | buy | BTC-USD | 13.56 | — | entry signal |
| 2026-10-18T10:00 | Supertrend · 1h | buy | BTC-USD | 22.25 | — | entry signal |
| 2026-10-18T09:52 | AI bee: Boozy | sell | ETH-USD | 15.33 | -0.08 | Jev: sell |
| 2026-10-18T09:45 | ROC + volume | buy | SOL-USD | 15.57 | — | entry signal |
| 2026-10-18T09:37 | AI bee: Boozy | buy | ETH-USD | 15.41 | — | Jev: buy (buy p=0.74) |
| 2026-10-18T09:37 | Donchian 55/20 | buy | XRP-USD | 5.95 | — | rebalance up |
| 2026-10-18T09:37 | Donchian 55/20 | sell | ETH-USD | 2.98 | -0.01 | rebalance down |
| 2026-10-18T09:37 | Donchian 55/20 | sell | BTC-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-18T09:37 | EMA 20/50 cross | buy | XRP-USD | 5.73 | — | rebalance up |
| 2026-10-18T09:37 | EMA 20/50 cross | sell | ETH-USD | 2.87 | -0.01 | rebalance down |
| 2026-10-18T09:37 | EMA 20/50 cross | sell | BTC-USD | 2.87 | -0.01 | rebalance down |
| 2026-10-18T09:35 | VWAP reversion | sell | DOGE-USD | 13.59 | -0.04 | target is flat |
| 2026-10-18T09:35 | Donchian 55/20 | buy | XRP-USD | 5.98 | — | entry signal |
| 2026-10-18T09:35 | Donchian 55/20 | buy | SOL-USD | 11.93 | — | entry signal |
| 2026-10-18T09:35 | Donchian 55/20 | buy | DOGE-USD | 11.93 | — | entry signal |
| 2026-10-18T09:35 | ROC + volume | buy | XRP-USD | 15.60 | — | entry signal |
| 2026-10-18T09:35 | ROC + volume | buy | DOGE-USD | 15.60 | — | entry signal |
| 2026-10-18T09:35 | EMA 20/50 cross | buy | XRP-USD | 5.76 | — | entry signal |
| 2026-10-18T09:35 | EMA 20/50 cross | buy | SOL-USD | 11.49 | — | entry signal |
| 2026-10-18T09:35 | EMA 20/50 cross | buy | DOGE-USD | 11.49 | — | entry signal |
| 2026-10-18T09:20 | AI bee: Boozy | sell | ETH-USD | 15.41 | -0.07 | Jev: add (buy p=0.52) |
| 2026-10-18T09:15 | VWAP reversion | buy | DOGE-USD | 13.62 | — | entry |
| 2026-10-18T09:15 | EMA 20/50 cross | buy | ETH-USD | 14.35 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 10:25:05.000121+00:00 -> 2026-10-18 10:35:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
