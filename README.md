# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T19:40:05.000123+00:00 · 73395 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.32 (-23.68%)

Closed trades 249, win rate 36.1%, fees £6.86, max drawdown -24.07%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 30.36 | -0.42 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 34356 decisions in 3009 calls, $0.4268 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T19:40 | 0 / 22 / 8 | cash |  |
| Breezy | 2026-11-25T19:40 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-25T19:40 | 7 / 22 / 1 | COIN 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 23.61 | 3.54 | -5.42 | 29 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.12 | 16.11 | 0 | — | 15.30 | 5.16 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.03 | 5.03 | 0 | — | 5.31 | 1.56 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.49 | -0.06 | -8.01 | 210 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.73 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 0.68 | 0.31 | -6.09 | 163 |
| 12 | Hold SPY | benchmark | 94.13 | -5.87 | 0 | — | -6.50 | -1.67 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.63 | -6.37 | 21 | 9.5 | -5.30 | -8.06 | -6.66 | 27 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.00 | -7.00 | 0 | — | -8.24 | -1.68 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 91.85 | -8.15 | 62 | 40.3 | -5.93 | -1.05 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.56 | -8.44 | 116 | 24.1 | -7.44 | -4.39 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.13 | -10.87 | 0 | — | -12.06 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.26 | -2.97 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 87.07 | -12.93 | 478 | 32.4 | -9.89 | -2.97 | -15.54 | 552 |
| 21 | Daily: Bullish score | daily | 85.81 | -14.19 | 20 | 20.0 | -13.22 | -2.91 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.70 | -6.60 | -17.73 | 68 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.18 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 79.41 | -20.59 | 601 | 30.3 | -18.53 | -5.10 | -24.08 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.60 | -23.40 | 172 | 28.5 | -22.33 | -9.49 | -22.46 | 68 |
| 28 | Agent | meta | 76.32 | -23.68 | 249 | 36.1 | -27.26 | -6.13 | -27.57 | 195 |
| 29 | Agent (aggressive) | meta | 75.68 | -24.32 | 114 | 33.3 | -17.89 | -4.64 | -18.52 | 92 |
| 30 | Parabolic SAR · 1h | trend | 75.29 | -24.71 | 210 | 27.6 | -35.35 | -8.66 | -35.97 | 184 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.48 | -7.83 | -29.49 | 74 |
| 32 | Max aggression: 5-day momentum | meta | 74.04 | -25.96 | 27 | 37.0 | -56.70 | -3.02 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.60 | -26.40 | 141 | 24.8 | -27.05 | -6.63 | -27.43 | 151 |
| 34 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -29.86 | -7.64 | -30.60 | 99 |
| 35 | Daily: Momentum burst | daily | 71.07 | -28.93 | 31 | 16.1 | -33.63 | -4.66 | -36.37 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.84 | -30.16 | 264 | 18.9 | -38.33 | -7.41 | -39.22 | 277 |
| 37 | Hold BTC | benchmark | 69.32 | -30.68 | 3 | 0.0 | -29.10 | -5.16 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -32.00 | -8.42 | -32.42 | 205 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.96 | -32.04 | 3 | 0.0 | -25.59 | -3.20 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 66.81 | -33.19 | 221 | 17.6 | -40.35 | -8.03 | -42.08 | 214 |
| 41 | OBV trend · 1h | momentum | 66.58 | -33.42 | 325 | 19.7 | -40.67 | -9.90 | -42.15 | 214 |
| 42 | Stochastic reversion · 1h | reversion | 66.50 | -33.50 | 411 | 39.9 | -34.29 | -3.67 | -43.59 | 442 |
| 43 | EMA 20/50 cross · 1h | trend | 65.86 | -34.13 | 126 | 9.5 | -38.25 | -10.65 | -38.51 | 113 |
| 44 | Triple EMA stack · 1h | trend | 65.08 | -34.92 | 172 | 15.1 | -42.59 | -10.55 | -42.86 | 171 |
| 45 | MACD zero-line · 1h | trend | 63.19 | -36.80 | 202 | 16.3 | -34.70 | -9.51 | -35.06 | 198 |
| 46 | RSI momentum · 1h | momentum | 62.55 | -37.45 | 203 | 14.8 | -43.37 | -9.76 | -43.71 | 188 |
| 47 | MFI reversion · 1h | reversion | 62.51 | -37.49 | 514 | 32.3 | -32.47 | -4.83 | -37.91 | 201 |
| 48 | Donchian 20/10 · 1h | breakout | 61.25 | -38.75 | 183 | 17.5 | -41.17 | -9.25 | -42.88 | 199 |
| 49 | Heikin-Ashi · 1h ⏸ | trend | 60.88 | -39.12 | 547 | 21.9 | -49.62 | -10.27 | -50.72 | 641 |
| 50 | ROC + volume · 1h | momentum | 60.70 | -39.30 | 465 | 26.7 | -40.21 | -7.90 | -41.29 | 337 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -61.87 | -4.66 | -63.59 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.16 | -41.84 | 314 | 12.1 | -45.22 | -10.53 | -46.54 | 328 |
| 53 | MACD cross · 1h | trend | 57.17 | -42.83 | 492 | 20.3 | -54.31 | -11.13 | -55.86 | 511 |
| 54 | Agent (ML meta-label) | meta | 56.29 | -43.71 | 2074 | 25.4 | -23.15 | -3.26 | -29.61 | 314 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.02 | -9.06 | -55.33 | 508 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.57 | -4.98 | -45.46 | 431 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.55 | -9.33 | -58.85 | 701 |
| 58 | VWAP momentum · 1h | momentum | 50.96 | -49.04 | 1086 | 21.5 | -60.83 | -13.36 | -62.12 | 1190 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.55 | -9.52 | -59.60 | 610 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.34 | -99.19 | 5375 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.63 | -32.34 | -84.45 | 1430 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.25 | -46.20 | -94.44 | 2402 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.50 | -31.19 | -91.16 | 1897 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -39.96 | -91.81 | 2219 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.93 | -27.77 | -88.99 | 1914 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -48.22 | -98.24 | 3419 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.79 | -50.14 | -96.92 | 3328 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.61 | -34.13 | -92.76 | 2038 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.03 | -34.60 | -82.39 | 1502 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -57.64 | -99.70 | 6297 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.90 | -37.32 | -93.25 | 2474 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.02 | -35.42 | -94.05 | 3120 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.00 | -99.83 | 6089 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.90 | -42.51 | -93.23 | 2259 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.53 | -18.12 | -52.45 | 664 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.51 | -22.27 | -78.82 | 1596 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -57.26 | -97.74 | 3231 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.90 | -99.22 | 5133 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.20 | -21.57 | -71.18 | 1198 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.45 | -44.18 | -94.76 | 2650 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.83 | -6.60 | -51.26 | 292 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.01 | -32.14 | -84.72 | 1656 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.38 | -99.78 | 6526 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.60 | -31.66 | -91.97 | 2502 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.92 | -20.27 | -83.44 | 1970 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.95 | -34.19 | -92.26 | 2173 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -50.70 | -98.24 | 4063 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.29 | -46.70 | -90.86 | 2199 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.12 | -22.89 | -67.92 | 779 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.87 | -27.85 | -73.38 | 1157 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.95 | -19.55 | -85.15 | 1839 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.09 | -51.10 | -98.12 | 4401 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -106.59 | -99.94 | 8283 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -48.39 | -7.26 | -54.28 | 304 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T19:35 | ROC + volume · 1h | buy | META | 8.62 | — | rebalance up |
| 2026-11-25T19:35 | ROC + volume · 1h | sell | DOGE-USD | 8.62 | -0.07 | target is flat |
| 2026-11-25T19:31 | Agent (ML meta-label) | sell | SQQQ | 14.47 | 0.18 | selected signal exited |
| 2026-11-25T19:31 | Three white soldiers · 1h | buy | UPRO | 13.37 | — | entry signal |
| 2026-11-25T19:31 | Three white soldiers · 1h | buy | SPY | 13.41 | — | entry signal |
| 2026-11-25T19:31 | Three white soldiers · 1h | buy | QQQ | 13.41 | — | entry signal |
| 2026-11-25T19:31 | Three white soldiers · 1h | buy | IWM | 13.41 | — | entry signal |
| 2026-11-25T19:31 | Three white soldiers · 1h | buy | GOOGL | 13.41 | — | entry signal |
| 2026-11-25T19:31 | Three white soldiers · 1h | sell | MSTR | 10.77 | 0.46 | rebalance down |
| 2026-11-25T19:31 | Three white soldiers · 1h | sell | DOGE-USD | 10.00 | 0.07 | rebalance down |
| 2026-11-25T19:31 | Volume breakout · 1h | buy | META | 19.16 | — | entry signal |
| 2026-11-25T19:31 | Donchian 20/10 · 1h | buy | XRP-USD | 8.75 | — | entry |
| 2026-11-25T19:31 | Donchian 20/10 · 1h | buy | PLTR | 8.76 | — | entry signal |
| 2026-11-25T19:31 | Donchian 20/10 · 1h | sell | TNA | 3.57 | 0.04 | rebalance down |
| 2026-11-25T19:31 | Donchian 20/10 · 1h | sell | META | 3.44 | -0.00 | rebalance down |
| 2026-11-25T19:31 | Donchian 20/10 · 1h | sell | LABU | 3.57 | 0.30 | rebalance down |
| 2026-11-25T19:31 | Donchian 20/10 · 1h | sell | IWM | 3.48 | 0.01 | rebalance down |
| 2026-11-25T19:31 | Donchian 20/10 · 1h | sell | AAPL | 3.45 | 0.00 | rebalance down |
| 2026-11-25T19:31 | OBV trend · 1h | sell | SQQQ | 15.22 | -2.31 | exit signal |
| 2026-11-25T19:31 | RSI momentum · 1h | buy | PLTR | 15.64 | — | entry signal |
| 2026-11-25T19:31 | ROC + volume · 1h | buy | META | 1.05 | — | entry signal |
| 2026-11-25T19:31 | ROC + volume · 1h | buy | DOGE-USD | 8.69 | — | entry |
| 2026-11-25T19:31 | Supertrend · 1h | buy | PLTR | 5.64 | — | entry signal |
| 2026-11-25T19:31 | Supertrend · 1h | buy | MSTR | 6.09 | — | entry signal |
| 2026-11-25T19:31 | Supertrend · 1h | buy | COIN | 6.09 | — | entry signal |
| 2026-11-25T19:31 | Supertrend · 1h | sell | TNA | 3.72 | 0.25 | rebalance down |
| 2026-11-25T19:31 | Supertrend · 1h | sell | META | 3.49 | 0.14 | rebalance down |
| 2026-11-25T19:31 | Supertrend · 1h | sell | IWM | 3.53 | 0.06 | rebalance down |
| 2026-11-25T19:31 | Supertrend · 1h | sell | DOGE-USD | 3.59 | 0.05 | rebalance down |
| 2026-11-25T19:31 | Supertrend · 1h | sell | AAPL | 3.49 | 0.06 | rebalance down |
| 2026-11-25T19:31 | MACD zero-line · 1h | buy | TNA | 15.82 | — | entry signal |
| 2026-11-25T19:31 | MACD zero-line · 1h | buy | IWM | 15.82 | — | entry signal |
| 2026-11-25T19:31 | MACD cross · 1h | buy | COIN | 1.80 | — | entry signal |
| 2026-11-25T19:31 | MACD cross · 1h | buy | AMD | 3.18 | — | entry signal |
| 2026-11-25T19:31 | EMA 9/21 cross · 1h | buy | META | 7.46 | — | entry signal |
| 2026-11-25T19:31 | EMA 9/21 cross · 1h | sell | TNA | 2.94 | 0.02 | rebalance down |
| 2026-11-25T19:20 | Agent | buy | SQQQ | 15.39 | — | rebalance up |
| 2026-11-25T19:16 | MFI reversion · 1h | buy | GOOGL | 3.81 | — | entry |
| 2026-11-25T19:16 | MFI reversion · 1h | sell | ETHU | 3.49 | 0.10 | target is flat |
| 2026-11-25T19:16 | Volume breakout · 1h | sell | META | 19.11 | -0.06 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 19:40:05.000123+00:00 -> 2026-11-25 19:50:05.000123+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
