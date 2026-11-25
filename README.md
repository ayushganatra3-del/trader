# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T20:40:05.000133+00:00 · 73453 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.89 (-23.11%)

Closed trades 249, win rate 36.1%, fees £6.86, max drawdown -24.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 30.94 | +0.16 |

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

Today: 39540 decisions in 3183 calls, $0.4873 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T20:40 | 1 / 17 / 12 | cash |  |
| Breezy | 2026-11-25T20:40 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-25T20:40 | 6 / 22 / 2 | MSTR 54% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.66 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.98 | 15.98 | 0 | — | 14.97 | 5.06 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.58 | 4.58 | 0 | — | 5.61 | 1.51 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.09 | 0.06 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.11 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.33 | 0.51 | -5.49 | 177 |
| 12 | Hold SPY | benchmark | 93.69 | -6.31 | 0 | — | -7.11 | -1.84 | -11.71 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 93.01 | -6.99 | 0 | — | -8.24 | -1.68 | -13.91 | 1 |
| 14 | Three white soldiers · 1h | momentum | 92.85 | -7.15 | 23 | 8.7 | -6.07 | -7.14 | -6.57 | 26 |
| 15 | Copy: Insider buying | copy | 92.55 | -7.45 | 63 | 41.3 | -5.52 | -0.96 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 92.00 | -8.00 | 116 | 24.1 | -7.01 | -4.01 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.65 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.01 | -10.99 | 0 | — | -12.19 | -2.66 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.19 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.27 | -13.72 | 478 | 32.4 | -10.96 | -3.50 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 86.23 | -13.77 | 20 | 20.0 | -12.90 | -2.85 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.01 | -16.99 | 77 | 19.5 | -19.76 | -6.79 | -19.79 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.18 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 78.37 | -21.63 | 601 | 30.3 | -19.46 | -5.67 | -24.05 | 678 |
| 27 | Agent | meta | 76.89 | -23.11 | 249 | 36.1 | -26.72 | -6.04 | -27.61 | 195 |
| 28 | Volume breakout · 1h | breakout | 76.41 | -23.59 | 173 | 28.9 | -22.35 | -9.52 | -22.45 | 69 |
| 29 | Agent (aggressive) | meta | 76.39 | -23.61 | 114 | 33.3 | -17.12 | -4.47 | -18.54 | 92 |
| 30 | Parabolic SAR · 1h | trend | 74.83 | -25.17 | 210 | 27.6 | -36.01 | -8.71 | -36.16 | 186 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.48 | -7.83 | -29.49 | 74 |
| 32 | Max aggression: 5-day momentum | meta | 73.48 | -26.52 | 27 | 37.0 | -57.03 | -3.08 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.46 | -26.54 | 141 | 24.8 | -26.90 | -6.60 | -27.15 | 144 |
| 34 | Ichimoku · 1h | trend | 73.17 | -26.83 | 114 | 15.8 | -29.99 | -7.67 | -30.60 | 99 |
| 35 | Daily: Momentum burst | daily | 70.94 | -29.06 | 31 | 16.1 | -33.30 | -4.61 | -35.97 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.49 | -30.51 | 264 | 18.9 | -37.39 | -7.05 | -38.09 | 286 |
| 37 | Hold BTC | benchmark | 69.10 | -30.90 | 3 | 0.0 | -29.41 | -5.22 | -36.10 | 1 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 67.90 | -32.10 | 3 | 0.0 | -25.39 | -3.16 | -33.66 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 67.79 | -32.21 | 209 | 22.5 | -31.69 | -8.22 | -31.77 | 206 |
| 40 | Supertrend · 1h | trend | 66.49 | -33.51 | 221 | 17.6 | -41.11 | -8.20 | -42.48 | 211 |
| 41 | OBV trend · 1h | momentum | 66.41 | -33.59 | 325 | 19.7 | -41.00 | -10.03 | -42.35 | 226 |
| 42 | EMA 20/50 cross · 1h | trend | 66.03 | -33.97 | 126 | 9.5 | -38.10 | -10.65 | -38.45 | 113 |
| 43 | Stochastic reversion · 1h | reversion | 65.54 | -34.46 | 411 | 39.9 | -34.01 | -3.64 | -42.70 | 440 |
| 44 | Triple EMA stack · 1h | trend | 65.01 | -34.99 | 172 | 15.1 | -43.07 | -10.61 | -43.36 | 172 |
| 45 | MACD zero-line · 1h | trend | 62.86 | -37.14 | 202 | 16.3 | -37.44 | -10.50 | -37.57 | 198 |
| 46 | RSI momentum · 1h | momentum | 62.11 | -37.89 | 203 | 14.8 | -44.06 | -9.81 | -44.17 | 193 |
| 47 | MFI reversion · 1h | reversion | 61.85 | -38.15 | 515 | 32.2 | -33.10 | -4.95 | -37.91 | 201 |
| 48 | Heikin-Ashi · 1h ⏸ | trend | 60.88 | -39.12 | 547 | 21.9 | -50.24 | -10.29 | -50.89 | 647 |
| 49 | Donchian 20/10 · 1h | breakout | 60.80 | -39.20 | 183 | 17.5 | -41.93 | -9.42 | -43.16 | 200 |
| 50 | ROC + volume · 1h | momentum | 60.41 | -39.59 | 465 | 26.7 | -40.22 | -7.87 | -41.07 | 337 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -61.15 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 57.68 | -42.32 | 314 | 12.1 | -45.65 | -10.52 | -46.48 | 333 |
| 53 | MACD cross · 1h | trend | 56.77 | -43.23 | 492 | 20.3 | -54.76 | -11.18 | -55.84 | 513 |
| 54 | Agent (ML meta-label) | meta | 56.20 | -43.80 | 2074 | 25.4 | -22.29 | -2.92 | -29.22 | 316 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.91 | -9.12 | -55.51 | 503 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -41.30 | -5.09 | -45.50 | 431 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.67 | -9.19 | -58.72 | 688 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -57.20 | -9.68 | -59.58 | 609 |
| 59 | VWAP momentum · 1h | momentum | 50.64 | -49.36 | 1086 | 21.5 | -61.28 | -13.42 | -61.61 | 1187 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.71 | -99.18 | 5367 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.59 | -32.48 | -84.42 | 1426 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.29 | -47.61 | -94.42 | 2396 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.57 | -31.65 | -91.13 | 1888 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.54 | -40.77 | -91.83 | 2220 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.86 | -27.92 | -88.86 | 1919 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.16 | -48.95 | -98.24 | 3409 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -52.02 | -96.89 | 3323 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.74 | -34.99 | -92.78 | 2050 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.06 | -35.00 | -82.34 | 1501 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -57.71 | -99.70 | 6289 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.98 | -38.16 | -93.23 | 2473 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.05 | -35.61 | -94.05 | 3124 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.29 | -99.83 | 6069 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.99 | -43.21 | -93.26 | 2258 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.83 | -19.35 | -52.31 | 663 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.64 | -22.84 | -78.74 | 1595 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -58.32 | -97.73 | 3230 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.82 | -99.23 | 5132 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.45 | -23.03 | -71.08 | 1199 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -45.98 | -94.75 | 2649 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -47.31 | -6.68 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.20 | -34.06 | -84.66 | 1645 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.21 | -99.77 | 6528 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.54 | -31.50 | -91.95 | 2501 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.88 | -20.31 | -83.47 | 1971 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.99 | -34.52 | -92.26 | 2162 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -50.71 | -98.24 | 4063 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.37 | -47.59 | -90.83 | 2198 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.10 | -22.90 | -67.90 | 777 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.80 | -28.30 | -73.36 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.87 | -19.57 | -85.15 | 1832 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.09 | -51.21 | -98.12 | 4396 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -108.23 | -99.94 | 8280 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.23 | -7.18 | -52.53 | 291 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T20:30 | Three white soldiers · 1h | sell | GOOGL | 13.35 | -0.06 | exit signal |
| 2026-11-25T20:30 | OBV trend · 1h | buy | SQQQ | 15.56 | — | entry signal |
| 2026-11-25T20:30 | OBV trend · 1h | buy | PLTR | 16.62 | — | entry signal |
| 2026-11-25T20:30 | MACD zero-line · 1h | buy | META | 15.77 | — | entry signal |
| 2026-11-25T20:30 | MACD cross · 1h | buy | MSFT | 2.48 | — | entry signal |
| 2026-11-25T20:30 | MACD cross · 1h | sell | SOL-USD | 3.46 | 0.07 | rebalance down |
| 2026-11-25T20:30 | EMA 20/50 cross · 1h | buy | PLTR | 16.50 | — | entry signal |
| 2026-11-25T20:15 | Three white soldiers · 1h | buy | QQQ | 13.33 | — | entry |
| 2026-11-25T20:15 | Volume breakout · 1h | sell | IWM | 19.14 | 0.00 | target is flat |
| 2026-11-25T20:01 | ADX DI cross · 1h | buy | SOL-USD | 3.48 | — | rebalance up |
| 2026-11-25T20:01 | ADX DI cross · 1h | sell | SQQQ | 3.48 | -0.06 | rebalance down |
| 2026-11-25T20:00 | Volume breakout · 1h | buy | DOGE-USD | 19.14 | — | entry signal |
| 2026-11-25T20:00 | Squeeze breakout · 1h | buy | XRP-USD | 20.80 | — | entry signal |
| 2026-11-25T20:00 | Squeeze breakout · 1h | buy | ETH-USD | 20.80 | — | entry signal |
| 2026-11-25T20:00 | Bollinger breakout · 1h | buy | XRP-USD | 17.03 | — | entry signal |
| 2026-11-25T20:00 | Bollinger breakout · 1h | buy | SOL-USD | 17.03 | — | entry signal |
| 2026-11-25T20:00 | Bollinger breakout · 1h | buy | ETH-USD | 17.03 | — | entry signal |
| 2026-11-25T20:00 | Bollinger breakout · 1h | buy | DOGE-USD | 17.03 | — | entry signal |
| 2026-11-25T20:00 | RSI momentum · 1h | buy | XRP-USD | 9.43 | — | entry signal |
| 2026-11-25T20:00 | RSI momentum · 1h | buy | SOL-USD | 12.49 | — | entry signal |
| 2026-11-25T20:00 | RSI momentum · 1h | buy | DOGE-USD | 12.49 | — | entry signal |
| 2026-11-25T20:00 | RSI momentum · 1h | sell | LABU | 4.90 | 0.41 | rebalance down |
| 2026-11-25T20:00 | ADX DI cross · 1h | buy | SOL-USD | 2.84 | — | entry |
| 2026-11-25T20:00 | ADX DI cross · 1h | buy | ETH-USD | 6.34 | — | entry |
| 2026-11-25T20:00 | ADX DI cross · 1h | buy | DOGE-USD | 6.34 | — | entry signal |
| 2026-11-25T20:00 | ADX DI cross · 1h | buy | BTC-USD | 6.34 | — | entry signal |
| 2026-11-25T20:00 | ADX DI cross · 1h | sell | XRP-USD | 3.74 | 0.03 | rebalance down |
| 2026-11-25T20:00 | ADX DI cross · 1h | sell | TNA | 3.60 | 0.01 | rebalance down |
| 2026-11-25T20:00 | ADX DI cross · 1h | sell | PLTR | 3.65 | 0.10 | rebalance down |
| 2026-11-25T20:00 | ADX DI cross · 1h | sell | META | 3.57 | -0.01 | rebalance down |
| 2026-11-25T20:00 | ADX DI cross · 1h | sell | LABU | 3.70 | 0.26 | rebalance down |
| 2026-11-25T20:00 | ADX DI cross · 1h | sell | IWM | 3.60 | -0.00 | rebalance down |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 6.43 | — | entry signal |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 6.44 | — | entry signal |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 6.44 | — | entry signal |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 6.44 | — | entry signal |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | sell | TNA | 5.11 | -0.00 | rebalance down |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | sell | PLTR | 5.19 | 0.10 | rebalance down |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | sell | META | 3.90 | -0.01 | rebalance down |
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | sell | LABU | 6.42 | 0.80 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 20:40:05.000133+00:00 -> 2026-11-25 20:50:05.000133+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
