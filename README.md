# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T18:41:05.000168+00:00 · 73349 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £77.01 (-22.99%)

Closed trades 249, win rate 36.1%, fees £6.83, max drawdown -23.35%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 30.73 | -0.14 |

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

Today: 30201 decisions in 2871 calls, $0.3785 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T18:41 | 3 / 21 / 6 | TNA 14% |  |
| Breezy | 2026-11-25T18:41 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-25T18:41 | 10 / 18 / 2 | COIN 72% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.06 | 16.06 | 0 | — | 14.37 | 4.98 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.18 | 1.02 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.81 | 4.81 | 0 | — | 4.96 | 1.49 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.98 | -0.22 | -8.58 | 212 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.68 | -2.88 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | -0.45 | -0.06 | -6.21 | 167 |
| 12 | Hold SPY | benchmark | 93.79 | -6.21 | 0 | — | -6.97 | -1.77 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 92.49 | -7.51 | 21 | 9.5 | -6.40 | -6.73 | -6.57 | 20 |
| 14 | Trend pullback · 1h | trend | 92.10 | -7.90 | 116 | 24.1 | -5.84 | -2.91 | -9.95 | 36 |
| 15 | Copy: Insider buying | copy | 91.85 | -8.15 | 62 | 40.3 | -5.92 | -1.05 | -14.79 | 72 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 90.38 | -9.62 | 0 | — | -10.88 | -2.25 | -13.91 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 88.64 | -11.37 | 0 | — | -12.33 | -2.68 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.15 | -2.97 | -20.94 | 1 |
| 20 | Daily: Bullish score | daily | 86.33 | -13.67 | 20 | 20.0 | -12.55 | -2.78 | -19.56 | 14 |
| 21 | Opening range 30m | breakout | 86.24 | -13.77 | 478 | 32.4 | -11.34 | -3.68 | -15.61 | 552 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.79 | -2.38 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.12 | -6.35 | -17.15 | 68 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -12.87 | -5.92 | -13.04 | 60 |
| 26 | Opening range 15m | breakout | 78.20 | -21.80 | 601 | 30.3 | -20.73 | -6.10 | -24.95 | 685 |
| 27 | Agent | meta | 77.01 | -22.99 | 249 | 36.1 | -27.33 | -6.23 | -27.58 | 198 |
| 28 | Volume breakout · 1h | breakout | 76.64 | -23.36 | 170 | 28.2 | -22.14 | -9.40 | -22.30 | 69 |
| 29 | Agent (aggressive) | meta | 76.55 | -23.45 | 114 | 33.3 | -17.20 | -4.49 | -18.44 | 92 |
| 30 | Parabolic SAR · 1h | trend | 74.86 | -25.14 | 209 | 27.8 | -35.80 | -8.63 | -35.99 | 185 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.44 | -7.82 | -29.45 | 74 |
| 32 | Keltner breakout · 1h | breakout | 73.39 | -26.61 | 141 | 24.8 | -28.92 | -7.03 | -29.08 | 150 |
| 33 | Max aggression: 5-day momentum | meta | 73.21 | -26.79 | 27 | 37.0 | -57.21 | -3.11 | -67.33 | 23 |
| 34 | Ichimoku · 1h | trend | 73.10 | -26.90 | 114 | 15.8 | -31.17 | -7.96 | -31.69 | 102 |
| 35 | Daily: Momentum burst | daily | 70.87 | -29.13 | 31 | 16.1 | -33.75 | -4.71 | -36.38 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.62 | -30.38 | 264 | 18.9 | -38.54 | -7.47 | -39.16 | 274 |
| 37 | Hold BTC | benchmark | 68.83 | -31.17 | 3 | 0.0 | -29.68 | -5.29 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 209 | 22.5 | -31.90 | -8.38 | -32.32 | 204 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.07 | -32.93 | 3 | 0.0 | -27.37 | -3.48 | -33.66 | 1 |
| 40 | OBV trend · 1h | momentum | 66.73 | -33.27 | 324 | 19.8 | -39.09 | -9.46 | -40.77 | 226 |
| 41 | Supertrend · 1h | trend | 66.69 | -33.31 | 221 | 17.6 | -40.35 | -7.99 | -41.89 | 209 |
| 42 | EMA 20/50 cross · 1h | trend | 66.24 | -33.76 | 126 | 9.5 | -38.21 | -10.70 | -38.40 | 114 |
| 43 | Stochastic reversion · 1h | reversion | 65.17 | -34.83 | 411 | 39.9 | -35.53 | -3.89 | -43.52 | 443 |
| 44 | Triple EMA stack · 1h | trend | 65.17 | -34.83 | 171 | 15.2 | -42.52 | -10.46 | -42.84 | 170 |
| 45 | MACD zero-line · 1h | trend | 63.27 | -36.73 | 202 | 16.3 | -34.95 | -9.61 | -35.24 | 197 |
| 46 | RSI momentum · 1h | momentum | 62.49 | -37.51 | 202 | 14.9 | -43.67 | -9.84 | -44.00 | 189 |
| 47 | MFI reversion · 1h | reversion | 61.74 | -38.26 | 512 | 32.0 | -33.06 | -4.94 | -37.72 | 198 |
| 48 | Donchian 20/10 · 1h | breakout | 61.01 | -38.99 | 183 | 17.5 | -41.57 | -9.32 | -42.89 | 196 |
| 49 | Heikin-Ashi · 1h ⏸ | trend | 60.88 | -39.12 | 547 | 21.9 | -50.40 | -10.38 | -51.05 | 623 |
| 50 | ROC + volume · 1h | momentum | 60.28 | -39.72 | 461 | 26.9 | -41.24 | -8.15 | -41.48 | 338 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 60.11 | -39.90 | 35 | 28.6 | -61.00 | -4.62 | -62.74 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 57.93 | -42.06 | 313 | 12.1 | -45.56 | -10.54 | -46.60 | 327 |
| 53 | MACD cross · 1h | trend | 56.76 | -43.24 | 491 | 20.4 | -54.21 | -10.99 | -55.40 | 504 |
| 54 | Agent (ML meta-label) | meta | 56.50 | -43.50 | 2073 | 25.4 | -18.62 | -2.25 | -25.69 | 322 |
| 55 | CCI reversion · 1h ⏸ | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.99 | -9.14 | -55.42 | 511 |
| 56 | Bollinger reversion · 1h ⏸ | reversion | 52.13 | -47.87 | 405 | 36.3 | -41.82 | -5.16 | -45.50 | 431 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.31 | -9.41 | -59.13 | 704 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -57.13 | -9.63 | -59.60 | 610 |
| 59 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.77 | -99.20 | 5389 |
| 60 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.84 | -33.26 | -84.45 | 1428 |
| 61 | VWAP momentum · 1h | momentum | 50.50 | -49.49 | 1086 | 21.5 | -60.69 | -13.22 | -61.71 | 1180 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.31 | -48.15 | -94.42 | 2403 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.67 | -32.05 | -91.19 | 1904 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.56 | -41.12 | -91.82 | 2224 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.03 | -27.82 | -89.06 | 1916 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -49.07 | -98.25 | 3422 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -52.16 | -96.92 | 3336 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.70 | -35.34 | -92.73 | 2026 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.18 | -35.03 | -82.45 | 1506 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -57.79 | -99.70 | 6321 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.10 | -38.08 | -93.35 | 2482 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.03 | -35.39 | -94.05 | 3122 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.78 | -99.82 | 6094 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.07 | -43.81 | -93.29 | 2267 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -50.22 | -19.58 | -52.43 | 664 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.04 | -23.01 | -78.97 | 1597 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -58.13 | -97.75 | 3217 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.21 | -63.75 | -99.23 | 5147 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.69 | -23.45 | -71.19 | 1202 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -45.67 | -94.82 | 2654 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -47.99 | -6.82 | -51.26 | 292 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.33 | -33.87 | -84.80 | 1658 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -76.89 | -99.78 | 6535 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.58 | -31.61 | -91.97 | 2502 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.93 | -20.33 | -83.58 | 1978 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.11 | -34.41 | -92.32 | 2176 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -50.39 | -98.24 | 4081 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.31 | -47.93 | -90.75 | 2203 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.31 | -27.17 | -68.24 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.11 | -28.24 | -73.42 | 1147 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.89 | -19.57 | -85.15 | 1835 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -51.28 | -98.13 | 4410 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -108.31 | -99.94 | 8273 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.60 | -6.96 | -52.54 | 297 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T18:40 | Volume breakout · 1h | buy | IWM | 19.16 | — | entry |
| 2026-11-25T18:35 | Agent | buy | SQQQ | 15.37 | — | rebalance up |
| 2026-11-25T18:35 | Copy: Insider buying | buy | PLTR | 10.34 | — | rebalance up |
| 2026-11-25T18:35 | Copy: Insider buying | sell | FUN | 10.97 | -0.61 | target is flat |
| 2026-11-25T18:30 | Agent | sell | SQQQ | 15.30 | -0.09 | rebalance down |
| 2026-11-25T18:30 | Three white soldiers · 1h | buy | MSTR | 23.14 | — | entry signal |
| 2026-11-25T18:30 | Volume breakout · 1h | buy | META | 19.16 | — | entry signal |
| 2026-11-25T18:30 | Keltner breakout · 1h | buy | LABU | 18.35 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | TNA | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | META | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | IWM | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | buy | AAPL | 12.21 | — | entry signal |
| 2026-11-25T18:30 | Donchian 20/10 · 1h | sell | LABU | 4.28 | 0.32 | rebalance down |
| 2026-11-25T18:30 | OBV trend · 1h | buy | AAPL | 16.68 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | TNA | 4.15 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | PLTR | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | IWM | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | ETHU | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | COIN | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | buy | AAPL | 4.22 | — | entry signal |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | XRP-USD | 4.19 | -0.03 | rebalance down |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | SOL-USD | 4.20 | -0.02 | rebalance down |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | META | 4.26 | 0.07 | rebalance down |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | ETH-USD | 4.20 | -0.02 | rebalance down |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | DOGE-USD | 4.20 | -0.02 | rebalance down |
| 2026-11-25T18:30 | VWAP momentum · 1h | sell | BTC-USD | 4.20 | -0.02 | rebalance down |
| 2026-11-25T18:30 | Heikin-Ashi · 1h | sell | SQQQ | 14.31 | -1.21 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-25T18:30 | Ichimoku · 1h | sell | SQQQ | 16.86 | -1.43 | exit signal |
| 2026-11-25T18:30 | ADX DI cross · 1h | buy | TNA | 9.91 | — | entry signal |
| 2026-11-25T18:30 | ADX DI cross · 1h | buy | META | 9.94 | — | entry signal |
| 2026-11-25T18:30 | ADX DI cross · 1h | buy | IWM | 9.94 | — | entry signal |
| 2026-11-25T18:30 | ADX DI cross · 1h | sell | XRP-USD | 7.31 | -0.04 | rebalance down |
| 2026-11-25T18:30 | ADX DI cross · 1h | sell | SQQQ | 5.79 | -0.01 | rebalance down |
| 2026-11-25T18:30 | ADX DI cross · 1h | sell | PLTR | 7.73 | 0.18 | rebalance down |
| 2026-11-25T18:30 | ADX DI cross · 1h | sell | LABU | 8.76 | 0.55 | rebalance down |
| 2026-11-25T18:30 | Parabolic SAR · 1h | buy | TNA | 9.30 | — | entry signal |
| 2026-11-25T18:30 | Parabolic SAR · 1h | buy | PLTR | 9.36 | — | entry signal |
| 2026-11-25T18:30 | Parabolic SAR · 1h | buy | META | 9.36 | — | entry signal |
| 2026-11-25T18:30 | Parabolic SAR · 1h | buy | IWM | 9.36 | — | entry signal |
| 2026-11-25T18:30 | Parabolic SAR · 1h | buy | AAPL | 9.36 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 18:41:05.000168+00:00 -> 2026-11-25 18:51:05.000168+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
