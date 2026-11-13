# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T19:10:05.000108+00:00 · 58536 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 33579 decisions in 3063 calls, $0.4196 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T19:10 | 9 / 19 / 2 | AMD 19%, ETHU 15%, SOXL 14%, MSTR 14% |  |
| Breezy | 2026-11-13T19:10 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-13T19:10 | 8 / 21 / 1 | MSTR 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| MFI reversion | LABU | 1.70 | +6.24% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.68 | 17.68 | 0 | — | 15.09 | 5.04 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.91 | 14.91 | 34 | 29.4 | 23.22 | 3.36 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.87 | 11.87 | 22 | 68.2 | 15.24 | 3.12 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.27 | 5.28 | 0 | — | 7.23 | 1.96 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.49 | 4.49 | 32 | 43.8 | 4.39 | 1.13 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.11 | 1.11 | 141 | 34.8 | 7.67 | 3.02 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.27 | -1.73 | 0 | — | -0.68 | -0.16 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.92 | -3.08 | 1 | 0.0 | -3.24 | -2.13 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.73 | -3.27 | 191 | 30.4 | -2.20 | -0.75 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.26 | -3.74 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 94.21 | -5.79 | 43 | 39.5 | -5.08 | -0.95 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.59 | -6.41 | 0 | — | -4.92 | -1.31 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Trend pullback · 1h | trend | 92.05 | -7.95 | 110 | 22.7 | -14.49 | -5.29 | -17.77 | 71 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.42 | -2.27 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.98 | -14.02 | 433 | 33.3 | -10.14 | -3.20 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.74 | -14.26 | 16 | 18.8 | -10.22 | -1.62 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.58 | -7.30 | -15.82 | 212 |
| 26 | Parabolic SAR · 1h | trend | 85.32 | -14.68 | 176 | 29.0 | -15.58 | -3.36 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -17.23 | -4.85 | -18.51 | 99 |
| 28 | Donchian 55/20 · 1h | breakout | 82.06 | -17.94 | 73 | 13.7 | -23.02 | -4.81 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.51 | -18.50 | 1 | 0.0 | -10.88 | -1.53 | -22.00 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.01 | -18.99 | 2 | 0.0 | -9.73 | -1.12 | -24.16 | 1 |
| 31 | Connors RSI(2) · 1h | reversion | 80.68 | -19.32 | 211 | 40.3 | -18.11 | -6.37 | -18.32 | 114 |
| 32 | Keltner breakout · 1h | breakout | 80.56 | -19.45 | 120 | 25.8 | -16.44 | -3.30 | -25.32 | 169 |
| 33 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 34 | Stochastic reversion · 1h | reversion | 79.74 | -20.26 | 303 | 47.5 | -25.84 | -3.78 | -28.25 | 402 |
| 35 | Opening range 15m | breakout | 78.43 | -21.57 | 526 | 31.2 | -17.37 | -4.66 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 78.09 | -21.91 | 398 | 35.2 | -22.40 | -2.91 | -27.13 | 168 |
| 37 | ADX DI cross · 1h | trend | 76.64 | -23.36 | 198 | 19.7 | -24.29 | -3.67 | -32.19 | 273 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -40.26 | -2.60 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.42 | -4.65 | -30.71 | 239 |
| 41 | Heikin-Ashi · 1h | trend | 75.03 | -24.98 | 442 | 24.2 | -37.89 | -7.06 | -39.26 | 663 |
| 42 | Max aggression: 1-day momentum | meta | 74.81 | -25.19 | 29 | 27.6 | -20.25 | -0.62 | -57.50 | 41 |
| 43 | MACD cross · 1h | trend | 74.77 | -25.23 | 385 | 23.6 | -29.15 | -4.33 | -38.65 | 469 |
| 44 | MACD zero-line · 1h | trend | 73.46 | -26.54 | 171 | 18.7 | -23.78 | -4.68 | -30.99 | 201 |
| 45 | RSI momentum · 1h | momentum | 72.78 | -27.22 | 171 | 14.0 | -26.85 | -4.13 | -37.92 | 208 |
| 46 | Supertrend · 1h | trend | 72.65 | -27.35 | 180 | 15.0 | -30.62 | -5.24 | -36.51 | 215 |
| 47 | EMA 20/50 cross · 1h | trend | 72.61 | -27.39 | 109 | 10.1 | -28.22 | -4.77 | -40.51 | 120 |
| 48 | Bollinger reversion · 1h | reversion | 72.04 | -27.95 | 302 | 41.7 | -33.10 | -5.18 | -35.72 | 383 |
| 49 | Triple EMA stack · 1h | trend | 71.81 | -28.19 | 150 | 14.0 | -28.16 | -4.65 | -38.65 | 205 |
| 50 | CCI reversion · 1h | reversion | 71.28 | -28.72 | 346 | 43.4 | -37.36 | -5.86 | -38.71 | 464 |
| 51 | ROC + volume · 1h | momentum | 71.23 | -28.77 | 398 | 28.6 | -31.54 | -5.80 | -38.37 | 376 |
| 52 | OBV trend · 1h | momentum | 69.92 | -30.08 | 298 | 19.1 | -30.40 | -5.36 | -38.14 | 277 |
| 53 | Donchian 20/10 · 1h | breakout | 69.42 | -30.58 | 153 | 19.0 | -30.14 | -5.41 | -37.58 | 209 |
| 54 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -33.18 | -4.51 | -37.81 | 33 |
| 55 | Williams %R · 1h | reversion | 67.97 | -32.03 | 383 | 43.6 | -42.33 | -6.91 | -44.04 | 542 |
| 56 | Z-score reversion · 1h | reversion | 65.63 | -34.37 | 204 | 37.3 | -30.38 | -4.30 | -31.55 | 237 |
| 57 | Agent (ML meta-label) | meta | 65.15 | -34.85 | 1849 | 24.8 | -17.55 | -2.74 | -24.25 | 343 |
| 58 | EMA 9/21 cross · 1h | trend | 64.86 | -35.14 | 266 | 11.3 | -37.93 | -7.70 | -43.16 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 64.41 | -35.59 | 186 | 32.8 | -36.28 | -5.34 | -38.24 | 240 |
| 60 | VWAP momentum · 1h | momentum | 62.88 | -37.12 | 913 | 22.2 | -52.64 | -10.68 | -53.43 | 1222 |
| 61 | Candlestick reversal · 1h | reversion | 62.27 | -37.73 | 486 | 28.4 | -44.96 | -8.31 | -46.11 | 604 |
| 62 | Three white soldiers | momentum | 58.34 | -41.66 | 542 | 14.6 | -49.50 | -22.28 | -49.51 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -44.56 | -99.01 | 5301 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.00 | -25.58 | -80.25 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.85 | -46.52 | -93.85 | 2540 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.21 | -31.53 | -89.28 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -41.42 | -91.31 | 2355 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.79 | -31.21 | -89.80 | 2197 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -52.08 | -97.89 | 3506 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -56.33 | -96.24 | 3428 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.78 | -33.05 | -93.80 | 2343 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.18 | -34.69 | -83.25 | 1664 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.57 | -99.57 | 6034 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -42.81 | -92.26 | 2635 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -37.18 | -95.41 | 3474 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.65 | -99.81 | 6170 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.23 | -42.86 | -92.29 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.63 | -25.94 | -75.83 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -60.71 | -97.63 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.06 | -98.89 | 4942 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.55 | -26.75 | -68.82 | 1256 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -56.82 | -94.79 | 2813 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.07 | -39.19 | -85.21 | 1792 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.82 | -99.66 | 6377 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.04 | -32.61 | -90.19 | 2326 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.51 | -20.17 | -78.89 | 1798 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.68 | -36.45 | -90.88 | 2187 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.02 | -51.85 | -97.02 | 3887 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -58.29 | -89.44 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.41 | -30.58 | -66.47 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.34 | -23.02 | -71.43 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.99 | -19.28 | -80.41 | 1747 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.41 | -51.01 | -97.41 | 4352 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.21 | -99.93 | 8451 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T19:10 | Agent (ML meta-label) | buy | UPRO | 3.80 | — | entry |
| 2026-11-13T19:05 | Agent (ML meta-label) | sell | UPRO | 3.80 | 0.01 | selected signal exited |
| 2026-11-13T19:00 | ROC + volume · 1h | sell | SOL-USD | 17.87 | -0.23 | exit signal |
| 2026-11-13T18:55 | Agent (ML meta-label) | buy | AMZN | 3.42 | — | following Supertrend |
| 2026-11-13T18:42 | Agent (ML meta-label) | buy | UPRO | 3.80 | — | entry |
| 2026-11-13T18:42 | Agent (ML meta-label) | sell | MSTR | 1.87 | -0.00 | selected signal exited |
| 2026-11-13T18:42 | Agent (ML meta-label) | sell | AMZN | 5.35 | -0.00 | selected signal exited |
| 2026-11-13T18:40 | VWAP momentum · 1h | buy | MSFT | 3.14 | — | rebalance up |
| 2026-11-13T18:35 | Agent (ML meta-label) | buy | MSTR | 1.87 | — | entry |
| 2026-11-13T18:30 | Agent (ML meta-label) | sell | MSTR | 1.87 | 0.01 | selected signal exited |
| 2026-11-13T18:30 | Agent | sell | TQQQ | 17.32 | 0.27 | selected signal exited |
| 2026-11-13T18:30 | CCI reversion · 1h | buy | TQQQ | 1.85 | — | entry signal |
| 2026-11-13T18:30 | CCI reversion · 1h | buy | SPY | 4.74 | — | entry signal |
| 2026-11-13T18:30 | CCI reversion · 1h | buy | QQQ | 4.74 | — | entry |
| 2026-11-13T18:30 | CCI reversion · 1h | buy | LABU | 4.74 | — | entry signal |
| 2026-11-13T18:30 | CCI reversion · 1h | buy | COIN | 4.74 | — | entry signal |
| 2026-11-13T18:30 | CCI reversion · 1h | sell | SOL-USD | 4.16 | 0.00 | rebalance down |
| 2026-11-13T18:30 | CCI reversion · 1h | sell | NVDA | 3.99 | -0.10 | rebalance down |
| 2026-11-13T18:30 | CCI reversion · 1h | sell | META | 4.23 | 0.07 | rebalance down |
| 2026-11-13T18:30 | CCI reversion · 1h | sell | DOGE-USD | 4.28 | 0.05 | rebalance down |
| 2026-11-13T18:30 | CCI reversion · 1h | sell | AMZN | 4.15 | -0.02 | rebalance down |
| 2026-11-13T18:30 | Williams %R · 1h | buy | MSTR | 2.83 | — | entry signal |
| 2026-11-13T18:30 | Williams %R · 1h | buy | COIN | 3.99 | — | entry signal |
| 2026-11-13T18:30 | Williams %R · 1h | sell | META | 6.82 | 0.10 | exit signal |
| 2026-11-13T18:30 | Stochastic reversion · 1h | buy | MSTR | 3.54 | — | entry |
| 2026-11-13T18:30 | Stochastic reversion · 1h | buy | AMD | 5.30 | — | entry signal |
| 2026-11-13T18:30 | Stochastic reversion · 1h | sell | META | 8.84 | 0.17 | exit signal |
| 2026-11-13T18:30 | Z-score reversion · 1h | buy | BITX | 8.14 | — | entry signal |
| 2026-11-13T18:30 | Bollinger reversion · 1h | buy | ETHU | 2.24 | — | entry |
| 2026-11-13T18:30 | Bollinger reversion · 1h | buy | BITX | 7.99 | — | entry |
| 2026-11-13T18:30 | Bollinger reversion · 1h | sell | MSFT | 10.23 | 0.16 | exit signal |
| 2026-11-13T18:30 | RSI(14) reversion · 1h | buy | MSTR | 5.22 | — | entry signal |
| 2026-11-13T18:30 | RSI(14) reversion · 1h | sell | XRP-USD | 5.22 | -0.02 | rebalance down |
| 2026-11-13T18:30 | VWAP momentum · 1h | buy | TSLA | 6.16 | — | rebalance up |
| 2026-11-13T18:30 | VWAP momentum · 1h | sell | SQQQ | 15.44 | -0.16 | exit signal |
| 2026-11-13T18:30 | Heikin-Ashi · 1h | buy | META | 18.76 | — | entry signal |
| 2026-11-13T18:30 | MACD cross · 1h | buy | META | 7.26 | — | entry signal |
| 2026-11-13T18:30 | Triple EMA stack · 1h | buy | META | 17.84 | — | entry signal |
| 2026-11-13T18:15 | MFI reversion · 1h | buy | TSLA | 9.64 | — | entry |
| 2026-11-13T18:15 | MFI reversion · 1h | buy | TQQQ | 9.67 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 19:10:05.000108+00:00 -> 2026-11-13 19:20:05.000108+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
