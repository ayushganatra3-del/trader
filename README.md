# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T16:24:05.000117+00:00 · 55955 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.47 (-13.53%)

Closed trades 174, win rate 35.1%, fees £5.23, max drawdown -13.93%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.38 | +0.04 |
| SQQQ | 34.52 | -0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 18639 decisions in 2451 calls, $0.2427 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T16:24 | 12 / 14 / 4 | cash |  |
| Breezy | 2026-11-11T16:24 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-11T16:24 | 10 / 18 / 2 | MSTR 79% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| MFI reversion | LABU | 1.66 | +5.37% | 3 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.11 | 3.83 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.49 | 14.49 | 0 | — | 14.56 | 4.77 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 4.15 | 1.07 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.38 | 3.38 | 0 | — | 5.79 | 1.61 | -6.60 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.89 | -0.11 | 133 | 34.6 | 10.50 | 3.62 | -3.18 | 85 |
| 9 | Gap and go | momentum | 99.42 | -0.58 | 183 | 30.6 | 6.25 | 1.79 | -9.06 | 247 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.41 | -1.59 | 0 | — | -0.08 | 0.05 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.18 | -1.82 | 181 | 28.2 | -1.39 | -0.45 | -8.35 | 157 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.19 | -3.81 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.46 | -5.54 | 0 | — | -3.52 | -0.90 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.11 | -5.89 | 43 | 39.5 | -7.12 | -1.43 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.89 | -3.50 | -5.99 | 29 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.60 | -8.40 | 109 | 22.9 | -16.29 | -5.70 | -18.84 | 80 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.93 | -11.07 | 404 | 33.2 | -13.30 | -4.04 | -14.11 | 595 |
| 23 | Max aggression: 5-day momentum | meta | 88.77 | -11.23 | 19 | 47.4 | -26.50 | -1.34 | -45.81 | 25 |
| 24 | Squeeze breakout · 1h | breakout | 88.64 | -11.36 | 64 | 21.9 | -8.33 | -2.53 | -14.25 | 78 |
| 25 | Hold BTC | benchmark | 87.09 | -12.91 | 1 | 0.0 | -4.41 | -0.53 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.58 | -13.42 | 168 | 26.8 | -14.22 | -2.99 | -21.98 | 225 |
| 27 | Agent | meta | 86.47 | -13.53 | 174 | 35.1 | -14.90 | -7.66 | -15.00 | 203 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 85.32 | -14.68 | 2 | 0.0 | -5.00 | -0.45 | -24.16 | 1 |
| 29 | Daily: Bullish score | daily | 84.39 | -15.61 | 16 | 18.8 | -7.88 | -1.15 | -19.22 | 15 |
| 30 | Agent (aggressive) | meta | 84.25 | -15.75 | 83 | 33.7 | -17.71 | -5.04 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 83.30 | -16.70 | 72 | 13.9 | -22.96 | -4.80 | -28.76 | 97 |
| 32 | ADX DI cross · 1h | trend | 82.77 | -17.23 | 185 | 18.9 | -22.02 | -3.50 | -30.55 | 275 |
| 33 | Keltner breakout · 1h | breakout | 82.49 | -17.51 | 110 | 23.6 | -19.56 | -4.00 | -25.32 | 181 |
| 34 | Max aggression: 1-day momentum | meta | 82.28 | -17.72 | 27 | 25.9 | -16.45 | -0.35 | -57.50 | 40 |
| 35 | Stochastic reversion · 1h | reversion | 82.20 | -17.80 | 288 | 47.9 | -24.14 | -3.44 | -27.17 | 392 |
| 36 | Volume breakout · 1h | breakout | 81.02 | -18.98 | 148 | 27.7 | -13.20 | -3.02 | -21.11 | 97 |
| 37 | Opening range 15m | breakout | 80.97 | -19.03 | 501 | 31.3 | -19.04 | -5.13 | -21.11 | 731 |
| 38 | Heikin-Ashi · 1h | trend | 80.51 | -19.49 | 417 | 24.5 | -38.37 | -6.95 | -41.80 | 674 |
| 39 | Connors RSI(2) · 1h | reversion | 80.29 | -19.71 | 208 | 39.9 | -20.14 | -6.70 | -20.30 | 126 |
| 40 | MFI reversion · 1h | reversion | 79.70 | -20.30 | 372 | 35.2 | -16.19 | -1.99 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.41 | -21.59 | 362 | 22.1 | -28.06 | -4.33 | -38.78 | 475 |
| 42 | CCI reversion · 1h | reversion | 77.78 | -22.22 | 331 | 45.0 | -26.72 | -4.03 | -31.08 | 452 |
| 43 | Bollinger breakout · 1h | breakout | 77.77 | -22.23 | 171 | 22.8 | -20.35 | -4.14 | -28.24 | 243 |
| 44 | MACD zero-line · 1h | trend | 75.98 | -24.02 | 160 | 16.9 | -21.18 | -4.09 | -31.04 | 213 |
| 45 | Bollinger reversion · 1h | reversion | 75.82 | -24.18 | 284 | 41.2 | -24.77 | -3.70 | -32.51 | 371 |
| 46 | Supertrend · 1h | trend | 75.51 | -24.49 | 168 | 13.1 | -28.95 | -4.99 | -36.07 | 229 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 48 | EMA 20/50 cross · 1h | trend | 75.20 | -24.80 | 102 | 10.8 | -25.69 | -4.35 | -36.29 | 114 |
| 49 | RSI momentum · 1h | momentum | 75.12 | -24.88 | 159 | 12.6 | -25.85 | -3.90 | -37.25 | 215 |
| 50 | Daily: Momentum burst | daily | 74.94 | -25.06 | 27 | 11.1 | -31.77 | -4.15 | -38.23 | 33 |
| 51 | Triple EMA stack · 1h | trend | 74.21 | -25.79 | 144 | 14.6 | -26.68 | -4.40 | -36.72 | 208 |
| 52 | ROC + volume · 1h | momentum | 73.22 | -26.78 | 376 | 27.7 | -33.96 | -6.14 | -39.15 | 389 |
| 53 | Williams %R · 1h | reversion | 72.91 | -27.09 | 350 | 45.7 | -34.92 | -5.42 | -36.48 | 530 |
| 54 | Donchian 20/10 · 1h | breakout | 72.44 | -27.56 | 142 | 19.7 | -29.36 | -5.33 | -35.62 | 216 |
| 55 | OBV trend · 1h | momentum | 71.88 | -28.12 | 279 | 18.6 | -26.25 | -4.67 | -34.76 | 283 |
| 56 | Z-score reversion · 1h | reversion | 71.59 | -28.41 | 195 | 37.9 | -22.64 | -3.06 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.01 | -30.98 | 174 | 32.2 | -29.41 | -4.46 | -33.09 | 224 |
| 58 | VWAP momentum · 1h | momentum | 68.27 | -31.73 | 850 | 22.1 | -51.61 | -10.40 | -54.48 | 1234 |
| 59 | EMA 9/21 cross · 1h | trend | 67.56 | -32.44 | 253 | 9.9 | -34.48 | -6.42 | -41.68 | 335 |
| 60 | Agent (ML meta-label) | meta | 67.08 | -32.92 | 1721 | 24.9 | -9.64 | -1.52 | -18.60 | 346 |
| 61 | Candlestick reversal · 1h | reversion | 65.16 | -34.84 | 459 | 28.8 | -36.83 | -6.72 | -39.36 | 576 |
| 62 | Three white soldiers | momentum | 60.29 | -39.71 | 513 | 14.6 | -49.27 | -22.61 | -49.31 | 655 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -45.19 | -99.06 | 5335 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.94 | -25.81 | -80.54 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -44.99 | -93.56 | 2551 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.33 | -31.58 | -89.40 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.00 | -39.12 | -91.21 | 2347 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.30 | -32.04 | -90.44 | 2208 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -52.77 | -97.84 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -57.13 | -96.38 | 3470 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.23 | -31.53 | -93.43 | 2339 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.96 | -33.57 | -83.31 | 1683 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.25 | -99.54 | 5952 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.25 | -42.30 | -92.31 | 2625 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -37.30 | -95.56 | 3425 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.98 | -99.80 | 6141 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.99 | -42.34 | -92.04 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.71 | -24.59 | -75.38 | 1638 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -59.17 | -97.74 | 3537 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -61.32 | -98.84 | 4892 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.24 | -26.19 | -69.04 | 1243 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -52.50 | -94.75 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.80 | -36.69 | -85.23 | 1797 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.59 | -99.63 | 6322 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.48 | -31.75 | -89.48 | 2285 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.49 | -19.53 | -77.74 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.55 | -35.82 | -90.66 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.68 | -50.45 | -96.69 | 3825 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.03 | -53.80 | -89.10 | 2135 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.60 | -27.68 | -66.68 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.13 | -22.35 | -72.05 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.21 | -18.25 | -78.48 | 1686 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.17 | -47.53 | -97.18 | 4277 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -100.82 | -99.93 | 8345 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T16:20 | Agent (ML meta-label) | sell | TSLA | 16.74 | -0.03 | selected signal exited |
| 2026-11-11T16:20 | Three white soldiers | buy | IWM | 15.08 | — | entry |
| 2026-11-11T16:15 | Agent (ML meta-label) | buy | TSLA | 16.78 | — | entry |
| 2026-11-11T16:15 | Agent (ML meta-label) | buy | AMD | 16.78 | — | entry |
| 2026-11-11T16:15 | Agent (aggressive) | buy | COIN | 42.11 | — | following Donchian 20/10 |
| 2026-11-11T16:10 | Agent (ML meta-label) | sell | AMD | 16.63 | -0.21 | selected signal exited |
| 2026-11-11T16:10 | Agent | buy | SQQQ | 17.24 | — | rebalance up |
| 2026-11-11T16:05 | Agent (aggressive) | buy | SQQQ | 42.11 | — | following Stochastic reversion, Williams %R |
| 2026-11-11T16:05 | Agent | buy | SQQQ | 17.31 | — | following Stochastic reversion, Williams %R |
| 2026-11-11T16:05 | Opening range 30m | buy | GOOGL | 2.24 | — | entry signal |
| 2026-11-11T16:00 | Agent (ML meta-label) | buy | AMD | 16.84 | — | entry |
| 2026-11-11T16:00 | CCI reversion · 1h | buy | NVDA | 7.85 | — | rebalance up |
| 2026-11-11T16:00 | CCI reversion · 1h | buy | ETHU | 9.28 | — | rebalance up |
| 2026-11-11T16:00 | CCI reversion · 1h | buy | COIN | 8.02 | — | rebalance up |
| 2026-11-11T16:00 | CCI reversion · 1h | buy | BITX | 8.34 | — | rebalance up |
| 2026-11-11T16:00 | CCI reversion · 1h | sell | XRP-USD | 11.11 | -0.01 | exit signal |
| 2026-11-11T16:00 | CCI reversion · 1h | sell | ETH-USD | 7.78 | 0.11 | exit signal |
| 2026-11-11T16:00 | CCI reversion · 1h | sell | DOGE-USD | 11.07 | 0.01 | exit signal |
| 2026-11-11T16:00 | Z-score reversion · 1h | buy | XRP-USD | 7.12 | — | rebalance up |
| 2026-11-11T16:00 | Z-score reversion · 1h | buy | NVDA | 7.19 | — | rebalance up |
| 2026-11-11T16:00 | Z-score reversion · 1h | buy | ETHU | 7.08 | — | rebalance up |
| 2026-11-11T16:00 | Z-score reversion · 1h | buy | ETH-USD | 7.20 | — | rebalance up |
| 2026-11-11T16:00 | Z-score reversion · 1h | buy | BTC-USD | 7.25 | — | rebalance up |
| 2026-11-11T16:00 | Z-score reversion · 1h | sell | SOL-USD | 7.18 | 0.12 | exit signal |
| 2026-11-11T16:00 | Z-score reversion · 1h | sell | DOGE-USD | 7.16 | 0.10 | exit signal |
| 2026-11-11T16:00 | RSI(14) reversion · 1h | buy | NVDA | 5.68 | — | rebalance up |
| 2026-11-11T16:00 | RSI(14) reversion · 1h | buy | MSTR | 5.94 | — | rebalance up |
| 2026-11-11T16:00 | RSI(14) reversion · 1h | buy | ETH-USD | 5.98 | — | rebalance up |
| 2026-11-11T16:00 | RSI(14) reversion · 1h | buy | BITX | 5.83 | — | rebalance up |
| 2026-11-11T16:00 | RSI(14) reversion · 1h | sell | XRP-USD | 11.13 | 0.18 | exit signal |
| 2026-11-11T16:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 11.35 | 0.25 | exit signal |
| 2026-11-11T16:00 | Candlestick reversal · 1h | sell | ETH-USD | 16.22 | 0.04 | exit signal |
| 2026-11-11T16:00 | Volume breakout · 1h | buy | ETH-USD | 19.87 | — | entry signal |
| 2026-11-11T16:00 | Squeeze breakout · 1h | buy | SOL-USD | 22.18 | — | entry signal |
| 2026-11-11T16:00 | Bollinger breakout · 1h | buy | XRP-USD | 11.13 | — | entry signal |
| 2026-11-11T16:00 | Bollinger breakout · 1h | buy | ETH-USD | 11.17 | — | entry signal |
| 2026-11-11T16:00 | Bollinger breakout · 1h | buy | DOGE-USD | 11.17 | — | entry signal |
| 2026-11-11T16:00 | Bollinger breakout · 1h | sell | TSLA | 8.08 | 0.02 | rebalance down |
| 2026-11-11T16:00 | Bollinger breakout · 1h | sell | TECL | 8.48 | 0.19 | rebalance down |
| 2026-11-11T16:00 | Bollinger breakout · 1h | sell | SOXL | 8.74 | 0.31 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 16:24:05.000117+00:00 -> 2026-11-11 16:34:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
