# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-07T17:50:05.000143+00:00 · 51146 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.92 (-12.09%)

Closed trades 153, win rate 36.6%, fees £4.57, max drawdown -12.56%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| DOGE-USD | 17.48 | -0.12 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 13760 decisions in 2758 calls, $0.1920 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-07T17:50 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-11-07T17:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-07T17:50 | 3 / 2 / 0 | ETH-USD 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI(14) reversion | SQQQ | 2.31 | +7.36% | 4 |
| Z-score reversion | SQQQ | 1.94 | +4.38% | 7 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Candlestick reversal · 1h | DOGE-USD | 1.92 | +7.45% | 7 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.49 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.15 | -0.85 | 122 | 47.5 | -12.45 | -2.93 | -14.34 | 151 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.46 | 2.83 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -6.88 | -3.99 | -10.35 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.54 | -0.42 | -9.14 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.11 | -0.97 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -16.31 | -6.00 | -17.86 | 81 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.46 | -4.41 | -26.45 | 64 |
| 23 | Daily: Bullish score | daily | 88.76 | -11.23 | 15 | 20.0 | -5.00 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.00 | -3.48 | -14.68 | 85 |
| 25 | Hold BTC | benchmark | 88.51 | -11.49 | 1 | 0.0 | -5.50 | -0.75 | -14.09 | 1 |
| 26 | Agent | meta | 87.92 | -12.09 | 153 | 36.6 | -14.06 | -7.55 | -14.24 | 202 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -13.50 | -2.98 | -20.50 | 236 |
| 28 | Donchian 55/20 · 1h | breakout | 85.95 | -14.05 | 71 | 14.1 | -12.74 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.37 | -5.50 | -18.65 | 96 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.04 | -17.96 | 261 | 46.7 | -25.02 | -3.69 | -29.25 | 393 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -19.76 | -6.60 | -20.39 | 127 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.62 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.37 | -20.63 | 175 | 18.3 | -23.79 | -3.96 | -27.04 | 260 |
| 38 | MFI reversion · 1h | reversion | 78.44 | -21.56 | 337 | 34.1 | -18.73 | -2.68 | -20.14 | 156 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.74 | -4.65 | -29.43 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.47 | -4.89 | -27.58 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.59 | -23.41 | 290 | 45.9 | -30.41 | -5.01 | -30.94 | 465 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -23.08 | -4.18 | -30.58 | 130 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -43.04 | -9.10 | -43.08 | 676 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.78 | -5.34 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -28.56 | -6.01 | -33.48 | 203 |
| 46 | Supertrend · 1h | trend | 73.63 | -26.37 | 166 | 13.3 | -30.63 | -5.34 | -34.80 | 217 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -28.58 | -5.43 | -32.60 | 220 |
| 48 | MACD cross · 1h | trend | 73.05 | -26.95 | 338 | 23.4 | -35.12 | -6.22 | -38.81 | 478 |
| 49 | Z-score reversion · 1h | reversion | 73.00 | -27.00 | 163 | 35.6 | -25.10 | -3.74 | -27.66 | 227 |
| 50 | Bollinger reversion · 1h | reversion | 72.90 | -27.10 | 251 | 40.2 | -31.21 | -5.35 | -34.33 | 373 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -37.04 | -6.01 | -39.03 | 536 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.92 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.47 | -28.53 | 141 | 19.9 | -29.91 | -5.54 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.78 | -6.16 | -34.07 | 286 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -38.83 | -7.55 | -39.36 | 382 |
| 56 | EMA 9/21 cross · 1h | trend | 67.14 | -32.85 | 243 | 9.9 | -38.94 | -8.03 | -39.08 | 333 |
| 57 | VWAP momentum · 1h | momentum | 66.84 | -33.16 | 785 | 21.9 | -55.66 | -12.37 | -55.66 | 1237 |
| 58 | Agent (ML meta-label) | meta | 66.34 | -33.66 | 1540 | 23.0 | -8.07 | -1.31 | -17.58 | 339 |
| 59 | RSI(14) reversion · 1h | reversion | 66.21 | -33.79 | 143 | 27.3 | -30.22 | -4.78 | -31.54 | 222 |
| 60 | Candlestick reversal · 1h | reversion | 65.33 | -34.67 | 411 | 28.5 | -38.25 | -7.10 | -38.48 | 575 |
| 61 | Three white soldiers | momentum | 63.96 | -36.04 | 476 | 15.3 | -49.29 | -23.27 | -49.40 | 653 |
| 62 | Max aggression: 1-day momentum | meta | 62.24 | -37.76 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.38 | -98.95 | 5227 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.75 | -25.95 | -80.77 | 1429 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.48 | -47.40 | -93.48 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.26 | -32.05 | -89.26 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.76 | -39.93 | -90.77 | 2301 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -32.14 | -90.13 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -54.94 | -97.76 | 3486 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -56.89 | -96.30 | 3392 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.72 | -33.57 | -93.72 | 2445 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.31 | -35.10 | -82.31 | 1651 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -55.88 | -99.52 | 5989 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.72 | -44.13 | -92.73 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -37.87 | -95.69 | 3412 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -75.83 | -99.80 | 6188 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -43.50 | -91.84 | 2278 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.10 | -25.29 | -76.16 | 1580 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -63.69 | -97.75 | 3511 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -63.27 | -98.79 | 4889 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.67 | -29.46 | -69.73 | 1201 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -54.53 | -94.64 | 2743 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.92 | -37.26 | -84.94 | 1763 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -75.23 | -99.64 | 6381 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.33 | -31.95 | -89.35 | 2300 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.89 | -19.84 | -77.91 | 1752 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.21 | -38.49 | -91.22 | 2235 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.66 | -53.80 | -96.66 | 3892 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.58 | -56.68 | -89.58 | 2170 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.67 | -28.38 | -65.68 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.28 | -24.39 | -73.28 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.38 | -18.29 | -78.51 | 1676 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.29 | -50.66 | -97.30 | 4339 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -118.42 | -99.93 | 8309 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-07T17:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.79 | — | entry signal |
| 2026-11-07T16:00 | Bollinger breakout · 1h | sell | ETH-USD | 19.20 | -0.19 | exit signal |
| 2026-11-07T16:00 | Donchian 20/10 · 1h | sell | SOL-USD | 17.45 | -0.37 | exit signal |
| 2026-11-07T16:00 | MACD cross · 1h | sell | SOL-USD | 6.61 | -0.01 | exit signal |
| 2026-11-07T16:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 16.66 | -0.16 | exit signal |
| 2026-11-07T14:30 | Three white soldiers | sell | XRP-USD | 15.94 | -0.12 | exit signal |
| 2026-11-07T14:30 | Three white soldiers | sell | ETH-USD | 16.00 | -0.09 | exit signal |
| 2026-11-07T14:20 | Three white soldiers | sell | BTC-USD | 15.97 | -0.10 | exit signal |
| 2026-11-07T14:15 | Three white soldiers | sell | SOL-USD | 16.00 | -0.09 | exit signal |
| 2026-11-07T14:05 | Three white soldiers | buy | XRP-USD | 16.06 | — | entry signal |
| 2026-11-07T14:00 | Bollinger reversion · 1h | buy | SOL-USD | 4.45 | — | entry signal |
| 2026-11-07T13:45 | Three white soldiers | buy | BTC-USD | 16.07 | — | entry signal |
| 2026-11-07T13:30 | Three white soldiers | buy | SOL-USD | 16.09 | — | entry signal |
| 2026-11-07T13:30 | Three white soldiers | buy | ETH-USD | 16.09 | — | entry signal |
| 2026-11-07T13:00 | Bollinger breakout · 1h | sell | BTC-USD | 19.20 | -0.19 | exit signal |
| 2026-11-07T13:00 | VWAP momentum · 1h | sell | XRP-USD | 1.13 | -0.01 | exit signal |
| 2026-11-07T13:00 | VWAP momentum · 1h | sell | ETH-USD | 7.37 | -0.07 | exit signal |
| 2026-11-07T13:00 | VWAP momentum · 1h | sell | BTC-USD | 6.04 | -0.05 | exit signal |
| 2026-11-07T12:35 | Three white soldiers | sell | DOGE-USD | 16.01 | -0.11 | exit signal |
| 2026-11-07T12:30 | Three white soldiers | buy | DOGE-USD | 16.11 | — | entry signal |
| 2026-11-07T12:00 | Three white soldiers | sell | SOL-USD | 16.05 | -0.11 | exit signal |
| 2026-11-07T12:00 | Three white soldiers | sell | BTC-USD | 16.07 | -0.10 | exit signal |
| 2026-11-07T11:40 | Three white soldiers | buy | SOL-USD | 16.16 | — | entry signal |
| 2026-11-07T11:35 | Three white soldiers | buy | BTC-USD | 16.17 | — | entry signal |
| 2026-11-07T11:15 | Three white soldiers | sell | DOGE-USD | 16.08 | -0.11 | target is flat |
| 2026-11-07T11:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.88 | — | entry signal |
| 2026-11-07T10:45 | Three white soldiers | buy | DOGE-USD | 16.20 | — | entry signal |
| 2026-11-07T10:00 | Three white soldiers · 1h | sell | XRP-USD | 23.31 | -0.22 | exit signal |
| 2026-11-07T10:00 | Candlestick reversal · 1h | sell | SOL-USD | 4.88 | -0.02 | exit signal |
| 2026-11-07T09:05 | Agent | buy | DOGE-USD | 17.61 | — | following Candlestick reversal · 1h |
| 2026-11-07T09:05 | Candlestick reversal · 1h | buy | DOGE-USD | 5.37 | — | entry |
| 2026-11-07T09:00 | CCI reversion · 1h | buy | DOGE-USD | 3.83 | — | entry signal |
| 2026-11-07T09:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.37 | -0.01 | exit signal |
| 2026-11-07T09:00 | Bollinger breakout · 1h | buy | BTC-USD | 19.39 | — | entry signal |
| 2026-11-07T08:50 | Three white soldiers | sell | XRP-USD | 16.20 | -0.04 | exit signal |
| 2026-11-07T08:05 | Agent | sell | DOGE-USD | 17.51 | -0.12 | selected signal exited |
| 2026-11-07T08:05 | Three white soldiers | sell | DOGE-USD | 16.11 | -0.12 | exit signal |
| 2026-11-07T08:00 | Agent | buy | DOGE-USD | 17.63 | — | following Candlestick reversal · 1h |
| 2026-11-07T08:00 | CCI reversion · 1h | sell | BTC-USD | 5.15 | 0.03 | exit signal |
| 2026-11-07T08:00 | Three white soldiers · 1h | buy | XRP-USD | 23.53 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-09 17:50:05.000143+00:00 -> 2026-11-07 18:00:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-09 17:50:05.000143+00:00 -> 2026-11-07 18:00:05.000143+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-09 17:50:05.000143+00:00 -> 2026-11-07 18:00:05.000143+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
