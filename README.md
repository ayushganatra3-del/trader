# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T20:11:05.000155+00:00 · 73424 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.56 (-23.43%)

Closed trades 249, win rate 36.1%, fees £6.86, max drawdown -24.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 30.61 | -0.17 |

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

Today: 36942 decisions in 3096 calls, $0.4570 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T20:11 | 1 / 11 / 17 | cash |  |
| Breezy | 2026-11-25T20:11 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-11-25T20:11 | 5 / 22 / 2 | COIN 66% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.10 | 16.09 | 0 | — | 15.08 | 5.09 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.81 | 4.81 | 0 | — | 5.86 | 1.57 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.09 | 0.06 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.11 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.33 | 0.51 | -5.49 | 177 |
| 12 | Hold SPY | benchmark | 93.94 | -6.06 | 0 | — | -6.85 | -1.76 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.29 | -6.71 | 22 | 9.1 | -5.56 | -7.73 | -6.57 | 25 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.00 | -7.00 | 0 | — | -8.24 | -1.68 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 92.18 | -7.82 | 63 | 41.3 | -5.89 | -1.04 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.75 | -8.25 | 116 | 24.1 | -7.25 | -4.23 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.65 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.17 | -10.83 | 0 | — | -12.02 | -2.62 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.19 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.74 | -13.26 | 478 | 32.4 | -10.42 | -3.23 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.99 | -14.01 | 20 | 20.0 | -13.13 | -2.91 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.03 | -16.97 | 77 | 19.5 | -19.73 | -6.78 | -19.76 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.18 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 78.98 | -21.02 | 601 | 30.3 | -18.97 | -5.37 | -24.05 | 678 |
| 27 | Agent | meta | 76.56 | -23.43 | 249 | 36.1 | -27.03 | -6.09 | -27.61 | 195 |
| 28 | Volume breakout · 1h | breakout | 76.56 | -23.44 | 172 | 28.5 | -22.15 | -9.41 | -22.31 | 70 |
| 29 | Agent (aggressive) | meta | 75.98 | -24.02 | 114 | 33.3 | -17.55 | -4.57 | -18.54 | 92 |
| 30 | Parabolic SAR · 1h | trend | 75.13 | -24.87 | 210 | 27.6 | -35.71 | -8.74 | -36.17 | 186 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.48 | -7.83 | -29.49 | 74 |
| 32 | Max aggression: 5-day momentum | meta | 73.88 | -26.12 | 27 | 37.0 | -56.79 | -3.03 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.56 | -26.44 | 141 | 24.8 | -26.80 | -6.61 | -27.15 | 144 |
| 34 | Ichimoku · 1h | trend | 73.28 | -26.73 | 114 | 15.8 | -29.90 | -7.65 | -30.60 | 99 |
| 35 | Daily: Momentum burst | daily | 71.04 | -28.96 | 31 | 16.1 | -33.21 | -4.59 | -35.97 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.66 | -30.34 | 264 | 18.9 | -37.23 | -7.01 | -38.09 | 286 |
| 37 | Hold BTC | benchmark | 69.19 | -30.81 | 3 | 0.0 | -29.20 | -5.19 | -36.10 | 1 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 68.17 | -31.83 | 3 | 0.0 | -24.98 | -3.10 | -33.66 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 67.86 | -32.14 | 209 | 22.5 | -31.60 | -8.21 | -31.77 | 206 |
| 40 | Supertrend · 1h | trend | 66.72 | -33.28 | 221 | 17.6 | -40.51 | -8.10 | -42.12 | 209 |
| 41 | OBV trend · 1h | momentum | 66.51 | -33.49 | 325 | 19.7 | -40.92 | -9.99 | -42.35 | 224 |
| 42 | Stochastic reversion · 1h | reversion | 66.05 | -33.95 | 411 | 39.9 | -33.45 | -3.55 | -42.70 | 440 |
| 43 | EMA 20/50 cross · 1h | trend | 65.97 | -34.03 | 126 | 9.5 | -38.14 | -10.65 | -38.45 | 112 |
| 44 | Triple EMA stack · 1h | trend | 65.05 | -34.95 | 172 | 15.1 | -43.04 | -10.62 | -43.33 | 172 |
| 45 | MACD zero-line · 1h | trend | 63.12 | -36.88 | 202 | 16.3 | -37.18 | -10.48 | -37.36 | 197 |
| 46 | RSI momentum · 1h | momentum | 62.33 | -37.67 | 203 | 14.8 | -43.86 | -9.83 | -44.02 | 193 |
| 47 | MFI reversion · 1h | reversion | 62.21 | -37.79 | 515 | 32.2 | -32.76 | -4.89 | -37.94 | 199 |
| 48 | Donchian 20/10 · 1h | breakout | 61.12 | -38.88 | 183 | 17.5 | -41.67 | -9.37 | -43.16 | 200 |
| 49 | Heikin-Ashi · 1h ⏸ | trend | 60.88 | -39.12 | 547 | 21.9 | -49.83 | -10.28 | -50.70 | 642 |
| 50 | ROC + volume · 1h | momentum | 60.58 | -39.42 | 465 | 26.7 | -40.18 | -7.86 | -41.07 | 338 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -61.56 | -4.65 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 57.91 | -42.09 | 314 | 12.1 | -45.39 | -10.52 | -46.48 | 332 |
| 53 | MACD cross · 1h | trend | 56.99 | -43.01 | 492 | 20.3 | -54.46 | -11.15 | -55.84 | 508 |
| 54 | Agent (ML meta-label) | meta | 56.14 | -43.86 | 2074 | 25.4 | -22.50 | -3.09 | -28.07 | 311 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.50 | -9.09 | -55.51 | 503 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.89 | -5.03 | -45.50 | 431 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.43 | -9.19 | -58.72 | 687 |
| 58 | VWAP momentum · 1h | momentum | 50.80 | -49.20 | 1086 | 21.5 | -61.17 | -13.44 | -61.72 | 1187 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.65 | -9.54 | -59.58 | 608 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.42 | -99.19 | 5373 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.51 | -32.11 | -84.43 | 1426 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.25 | -46.79 | -94.41 | 2396 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.52 | -31.37 | -91.13 | 1888 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.50 | -40.33 | -91.84 | 2219 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.84 | -27.80 | -88.85 | 1918 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -48.59 | -98.24 | 3409 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -50.82 | -96.91 | 3323 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.68 | -34.76 | -92.78 | 2048 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.04 | -34.91 | -82.35 | 1501 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -57.73 | -99.70 | 6294 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -37.66 | -93.25 | 2474 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.03 | -35.50 | -94.03 | 3119 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -68.49 | -99.83 | 6073 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.98 | -43.25 | -93.25 | 2257 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.49 | -18.43 | -52.16 | 661 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.79 | -22.74 | -78.83 | 1595 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -58.03 | -97.74 | 3231 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.86 | -99.23 | 5131 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.34 | -22.60 | -71.08 | 1199 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.50 | -45.13 | -94.76 | 2650 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.81 | -6.58 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.08 | -32.79 | -84.70 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -77.05 | -99.77 | 6524 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.58 | -31.62 | -91.97 | 2502 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.95 | -20.35 | -83.49 | 1972 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.06 | -34.60 | -92.25 | 2161 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -50.72 | -98.24 | 4063 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.28 | -46.96 | -90.81 | 2196 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.84 | -26.05 | -68.05 | 778 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.90 | -28.11 | -73.38 | 1156 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.93 | -19.56 | -85.15 | 1832 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.09 | -51.21 | -98.12 | 4395 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -107.76 | -99.94 | 8281 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.57 | -6.98 | -52.53 | 291 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-25T20:00 | EMA 9/21 cross · 1h | sell | IWM | 5.14 | -0.00 | rebalance down |
| 2026-11-25T19:45 | MFI reversion · 1h | buy | ETHU | 3.80 | — | entry |
| 2026-11-25T19:45 | MFI reversion · 1h | sell | GOOGL | 3.80 | -0.01 | target is flat |
| 2026-11-25T19:45 | Three white soldiers · 1h | sell | QQQ | 13.35 | -0.06 | target is flat |
| 2026-11-25T19:45 | Volume breakout · 1h | buy | IWM | 19.13 | — | entry |
| 2026-11-25T19:45 | EMA 9/21 cross · 1h | buy | META | 2.91 | — | rebalance up |
| 2026-11-25T19:45 | EMA 9/21 cross · 1h | sell | IWM | 2.91 | -0.00 | rebalance down |
| 2026-11-25T19:42 | Copy: Insider buying | buy | SHMD | 11.33 | — | entry |
| 2026-11-25T19:42 | Copy: Insider buying | sell | BH | 10.70 | 0.10 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 20:11:05.000155+00:00 -> 2026-11-25 20:21:05.000155+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
