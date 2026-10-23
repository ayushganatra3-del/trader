# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T14:45:05.000196+00:00 · 33166 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.68 (-10.31%)

Closed trades 99, win rate 39.4%, fees £3.16, max drawdown -10.73%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 15780 decisions in 2265 calls, $0.2081 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T14:45 | 8 / 19 / 3 | AMD 16%, SOXL 16%, MSTR 15% |  |
| Breezy | 2026-10-23T14:45 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-23T14:45 | 10 / 18 / 2 | MSTR 83% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.94 | 6.94 | 0 | — | 8.43 | 4.51 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.52 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.48 | -3.19 | -13.74 | 154 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.61 | 0.61 | 0 | — | 3.23 | 1.53 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.78 | -0.22 | 72 | 33.3 | 5.94 | 2.88 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 98.06 | -1.94 | 0 | — | -0.49 | -0.25 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.71 | -3.29 | 0 | — | 1.72 | 0.46 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.49 | -3.51 | 118 | 31.4 | -1.95 | -1.14 | -6.22 | 193 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 17 | Copy: Congress Democrats (NANC) | copy | 95.44 | -4.56 | 0 | — | -1.13 | -0.43 | -5.87 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.49 | -5.51 | 0 | — | -6.56 | -2.78 | -7.76 | 1 |
| 19 | Gap and go | momentum | 94.11 | -5.89 | 91 | 22.0 | 4.92 | 1.65 | -8.69 | 184 |
| 20 | Opening range 30m | breakout | 94.10 | -5.90 | 238 | 35.3 | -10.19 | -3.16 | -17.21 | 557 |
| 21 | Copy: Insider buying | copy | 93.90 | -6.10 | 25 | 40.0 | -15.08 | -2.89 | -20.68 | 71 |
| 22 | Trend pullback · 1h | trend | 93.71 | -6.29 | 95 | 23.2 | -21.59 | -7.10 | -21.85 | 115 |
| 23 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -16.96 | -1.58 | -27.80 | 24 |
| 24 | Donchian 55/20 · 1h | breakout | 92.80 | -7.20 | 48 | 16.7 | -16.41 | -3.73 | -17.38 | 98 |
| 25 | Parabolic SAR · 1h | trend | 91.75 | -8.25 | 117 | 25.6 | -21.20 | -5.03 | -24.17 | 254 |
| 26 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 27 | Daily: Momentum burst | daily | 91.28 | -8.72 | 10 | 10.0 | -18.02 | -3.51 | -20.97 | 40 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.95 | -9.05 | 107 | 18.7 | -11.88 | -2.44 | -14.40 | 255 |
| 30 | Agent | meta | 89.68 | -10.31 | 99 | 39.4 | -10.43 | -7.36 | -11.16 | 203 |
| 31 | Daily: Bullish score | daily | 89.43 | -10.57 | 9 | 0.0 | -8.16 | -1.07 | -14.40 | 14 |
| 32 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 88.82 | -11.18 | 0 | — | -5.67 | -0.84 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.69 | -11.31 | 105 | 27.6 | -12.56 | -2.50 | -16.50 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 88.20 | -11.80 | 186 | 45.2 | -19.49 | -3.66 | -22.47 | 383 |
| 36 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -11.87 | -4.10 | -14.77 | 94 |
| 37 | Opening range 15m | breakout | 86.92 | -13.08 | 305 | 30.2 | -15.21 | -4.41 | -17.87 | 699 |
| 38 | EMA 20/50 cross · 1h | trend | 86.22 | -13.78 | 71 | 11.3 | -22.77 | -4.56 | -25.02 | 137 |
| 39 | Keltner breakout · 1h | breakout | 85.98 | -14.02 | 73 | 23.3 | -22.98 | -4.90 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 85.89 | -14.11 | 108 | 14.8 | -23.89 | -5.05 | -26.44 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.26 | -14.74 | 101 | 15.8 | -21.80 | -4.68 | -23.38 | 216 |
| 42 | MACD cross · 1h | trend | 85.11 | -14.89 | 216 | 23.1 | -22.62 | -4.52 | -26.15 | 451 |
| 43 | Connors RSI(2) · 1h | reversion | 84.96 | -15.04 | 170 | 39.4 | -26.69 | -8.22 | -27.06 | 195 |
| 44 | Z-score reversion · 1h | reversion | 84.82 | -15.19 | 106 | 34.0 | -13.99 | -2.33 | -21.48 | 193 |
| 45 | Ichimoku · 1h | trend | 83.60 | -16.40 | 65 | 12.3 | -24.00 | -5.02 | -25.63 | 110 |
| 46 | Triple EMA stack · 1h | trend | 83.54 | -16.46 | 98 | 15.3 | -26.17 | -5.25 | -28.44 | 210 |
| 47 | MFI reversion · 1h | reversion | 82.26 | -17.73 | 256 | 31.6 | -17.33 | -2.83 | -20.54 | 141 |
| 48 | MACD zero-line · 1h | trend | 82.16 | -17.84 | 103 | 15.5 | -21.17 | -4.43 | -24.81 | 217 |
| 49 | Three white soldiers | momentum | 81.58 | -18.42 | 271 | 20.3 | -43.36 | -20.92 | -43.47 | 585 |
| 50 | Williams %R · 1h | reversion | 81.47 | -18.53 | 213 | 44.1 | -35.06 | -6.30 | -36.69 | 514 |
| 51 | CCI reversion · 1h | reversion | 81.32 | -18.68 | 198 | 42.9 | -25.45 | -3.79 | -28.17 | 437 |
| 52 | Donchian 20/10 · 1h | breakout | 81.23 | -18.77 | 96 | 19.8 | -24.52 | -4.78 | -27.39 | 217 |
| 53 | OBV trend · 1h | momentum | 81.14 | -18.86 | 201 | 17.4 | -31.52 | -6.98 | -32.99 | 302 |
| 54 | Bollinger reversion · 1h | reversion | 80.89 | -19.11 | 171 | 34.5 | -30.51 | -6.32 | -32.19 | 356 |
| 55 | Agent (ML meta-label) | meta | 80.51 | -19.49 | 841 | 18.8 | -13.92 | -2.49 | -16.97 | 375 |
| 56 | Heikin-Ashi · 1h | trend | 79.58 | -20.42 | 262 | 23.3 | -42.57 | -9.97 | -43.38 | 646 |
| 57 | RSI(14) reversion · 1h | reversion | 78.67 | -21.33 | 91 | 23.1 | -14.25 | -2.60 | -23.51 | 185 |
| 58 | Candlestick reversal · 1h | reversion | 78.17 | -21.83 | 252 | 29.0 | -34.15 | -6.41 | -36.06 | 535 |
| 59 | ROC + volume · 1h | momentum | 78.17 | -21.84 | 239 | 23.8 | -30.95 | -6.22 | -31.99 | 379 |
| 60 | EMA 9/21 cross · 1h | trend | 77.36 | -22.64 | 158 | 12.0 | -29.95 | -6.16 | -33.53 | 317 |
| 61 | VWAP momentum · 1h | momentum | 76.74 | -23.26 | 503 | 21.7 | -49.50 | -11.54 | -50.12 | 1196 |
| 62 | Max aggression: 1-day momentum | meta | 66.40 | -33.60 | 18 | 27.8 | -43.33 | -3.07 | -50.18 | 42 |
| 63 | ROC + volume | momentum | 58.03 | -41.97 | 700 | 22.9 | -74.85 | -27.42 | -74.98 | 1543 |
| 64 | Volume breakout | breakout | 57.14 | -42.86 | 417 | 13.2 | -60.51 | -26.14 | -60.51 | 758 |
| 65 | Squeeze breakout | breakout | 54.07 | -45.93 | 545 | 14.1 | -65.94 | -28.76 | -66.19 | 1138 |
| 66 | Donchian 55/20 | breakout | 54.05 | -45.95 | 558 | 19.4 | -71.05 | -24.00 | -71.25 | 1248 |
| 67 | RSI(14) reversion | reversion | 53.04 | -46.96 | 815 | 26.0 | -76.50 | -19.74 | -76.80 | 1664 |
| 68 | EMA 20/50 cross | trend | 52.61 | -47.39 | 604 | 20.4 | -78.49 | -23.85 | -78.82 | 1392 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -45.17 | -98.66 | 4987 |
| 70 | VWAP reversion | reversion | 50.56 | -49.44 | 811 | 25.0 | -74.63 | -17.59 | -74.77 | 1538 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -48.48 | -93.65 | 2481 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.23 | -30.10 | -88.50 | 1864 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.98 | -38.17 | -91.13 | 2292 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.19 | -31.49 | -90.23 | 2133 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.57 | -54.01 | -97.62 | 3406 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.89 | -62.77 | -95.92 | 3296 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.69 | -35.49 | -93.72 | 2421 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.43 | -36.46 | -82.48 | 1662 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.38 | -99.31 | 5623 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.06 | -41.87 | -92.20 | 2562 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.26 | -40.60 | -95.27 | 3340 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.88 | -99.74 | 6019 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -45.67 | -91.85 | 2282 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -66.62 | -97.45 | 3487 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.43 | -58.72 | -98.45 | 4673 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.08 | -60.09 | -94.14 | 2719 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.42 | -40.16 | -83.57 | 1764 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -64.91 | -99.52 | 6105 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.57 | -28.98 | -87.65 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.04 | -37.80 | -90.13 | 2220 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -47.29 | -95.87 | 3714 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.20 | -50.00 | -89.30 | 2070 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.01 | -48.16 | -96.06 | 4082 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.82 | -99.90 | 8060 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T14:45 | VWAP reversion | sell | LABU | 12.74 | 0.08 | target is flat |
| 2026-10-23T14:45 | RSI(14) reversion | buy | TNA | 7.58 | — | entry |
| 2026-10-23T14:45 | RSI(14) reversion | sell | PLTR | 7.63 | 0.16 | take-profit |
| 2026-10-23T14:45 | Three white soldiers | sell | ETHU | 20.50 | 0.14 | target is flat |
| 2026-10-23T14:45 | Volume breakout | buy | TQQQ | 14.29 | — | entry signal |
| 2026-10-23T14:45 | Donchian 55/20 | buy | SOXL | 13.46 | — | entry signal |
| 2026-10-23T14:45 | Donchian 55/20 | buy | NVDA | 13.52 | — | entry signal |
| 2026-10-23T14:45 | ROC + volume | buy | TQQQ | 14.51 | — | entry signal |
| 2026-10-23T14:45 | EMA 20/50 cross | buy | TECL | 13.15 | — | entry signal |
| 2026-10-23T14:40 | OBV trend · 1h | sell | IWM | 20.35 | -0.03 | target is flat |
| 2026-10-23T14:40 | VWAP reversion | sell | BTC-USD | 12.66 | -0.01 | exit signal |
| 2026-10-23T14:40 | Opening range 30m | buy | TQQQ | 9.36 | — | entry signal |
| 2026-10-23T14:40 | Opening range 30m | buy | SOXL | 9.38 | — | entry signal |
| 2026-10-23T14:40 | Opening range 30m | buy | QQQ | 9.38 | — | entry signal |
| 2026-10-23T14:40 | Opening range 30m | buy | NVDA | 9.38 | — | entry signal |
| 2026-10-23T14:40 | Opening range 30m | sell | TECL | 6.34 | 0.06 | rebalance down |
| 2026-10-23T14:40 | Opening range 30m | sell | PLTR | 6.33 | 0.00 | rebalance down |
| 2026-10-23T14:40 | Opening range 30m | sell | MSFT | 6.23 | -0.00 | rebalance down |
| 2026-10-23T14:40 | Opening range 30m | sell | META | 6.15 | -0.01 | rebalance down |
| 2026-10-23T14:40 | Opening range 30m | sell | GOOGL | 6.18 | -0.02 | rebalance down |
| 2026-10-23T14:40 | Opening range 30m | sell | AMD | 6.29 | 0.04 | rebalance down |
| 2026-10-23T14:40 | Donchian 55/20 | buy | TECL | 13.49 | — | entry signal |
| 2026-10-23T14:40 | Donchian 55/20 | buy | AMD | 13.49 | — | entry signal |
| 2026-10-23T14:40 | Gap and go | buy | ETHU | 23.55 | — | entry signal |
| 2026-10-23T14:40 | ROC + volume | buy | TECL | 14.49 | — | entry |
| 2026-10-23T14:40 | EMA 20/50 cross | buy | ETH-USD | 13.15 | — | entry signal |
| 2026-10-23T14:35 | Three white soldiers | buy | ETHU | 20.36 | — | entry signal |
| 2026-10-23T14:30 | CCI reversion · 1h | buy | TECL | 10.60 | — | entry signal |
| 2026-10-23T14:30 | CCI reversion · 1h | buy | SOXL | 13.38 | — | entry signal |
| 2026-10-23T14:30 | CCI reversion · 1h | buy | AMD | 13.38 | — | entry signal |
| 2026-10-23T14:30 | CCI reversion · 1h | sell | XRP-USD | 6.71 | -0.10 | rebalance down |
| 2026-10-23T14:30 | CCI reversion · 1h | sell | COIN | 6.54 | -0.14 | rebalance down |
| 2026-10-23T14:30 | Williams %R · 1h | buy | TSLA | 10.09 | — | entry signal |
| 2026-10-23T14:30 | Williams %R · 1h | buy | NVDA | 10.10 | — | entry signal |
| 2026-10-23T14:30 | Williams %R · 1h | buy | MSFT | 10.10 | — | entry signal |
| 2026-10-23T14:30 | Williams %R · 1h | buy | AMD | 10.10 | — | entry signal |
| 2026-10-23T14:30 | Williams %R · 1h | sell | TNA | 6.11 | -0.07 | rebalance down |
| 2026-10-23T14:30 | Williams %R · 1h | sell | MSTR | 10.21 | -0.04 | rebalance down |
| 2026-10-23T14:30 | Williams %R · 1h | sell | IWM | 6.16 | -0.03 | rebalance down |
| 2026-10-23T14:30 | Williams %R · 1h | sell | COIN | 10.02 | -0.20 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 14:45:05.000196+00:00 -> 2026-10-23 14:55:05.000196+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
