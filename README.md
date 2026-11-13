# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T15:40:05.000109+00:00 · 58362 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.03 (-14.97%)

Closed trades 192, win rate 34.9%, fees £5.60, max drawdown -15.42%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 17.01 | -0.01 |
| TSLA | 17.00 | -0.01 |

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

Today: 17907 decisions in 2541 calls, $0.2365 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T15:40 | 1 / 16 / 14 | cash |  |
| Breezy | 2026-11-13T15:40 | 0 / 22 / 9 | cash |  |
| Boozy | 2026-11-13T15:40 | 3 / 21 / 7 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| MFI reversion | TSLA | 1.59 | +1.86% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 117.81 | 17.81 | 34 | 29.4 | 26.71 | 3.65 | -8.66 | 45 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 117.29 | 17.29 | 0 | — | 15.05 | 5.03 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.70 | 14.70 | 22 | 68.2 | 18.50 | 3.69 | -4.91 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.13 | 7.13 | 32 | 43.8 | 7.35 | 1.73 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 105.01 | 5.01 | 0 | — | 7.28 | 1.97 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.76 | 1.76 | 141 | 34.8 | 8.42 | 3.27 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.47 | -2.53 | 0 | — | -1.18 | -0.33 | -6.18 | 1 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.97 | -4.03 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 95.68 | -4.32 | 1 | 0.0 | -4.19 | -2.50 | -6.57 | 2 |
| 14 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 15 | Agent (rotation) | meta | 95.26 | -4.74 | 191 | 30.4 | -3.52 | -1.16 | -8.69 | 161 |
| 16 | Copy: Insider buying | copy | 94.47 | -5.53 | 43 | 39.5 | -4.80 | -0.89 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.42 | -7.58 | 0 | — | -5.83 | -1.56 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 91.75 | -8.25 | 110 | 22.7 | -13.28 | -4.54 | -17.58 | 72 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.13 | -2.62 | -18.92 | 2 |
| 23 | Opening range 30m | breakout | 86.29 | -13.71 | 433 | 33.3 | -9.68 | -3.04 | -14.11 | 602 |
| 24 | Daily: Bullish score | daily | 86.13 | -13.87 | 16 | 18.8 | -9.65 | -1.51 | -19.56 | 15 |
| 25 | Agent | meta | 85.03 | -14.97 | 192 | 34.9 | -15.62 | -7.86 | -15.84 | 213 |
| 26 | Parabolic SAR · 1h | trend | 85.01 | -14.99 | 175 | 28.6 | -15.93 | -3.44 | -22.35 | 218 |
| 27 | Agent (aggressive) | meta | 83.01 | -16.99 | 93 | 33.3 | -18.55 | -5.24 | -18.82 | 102 |
| 28 | Donchian 55/20 · 1h | breakout | 81.59 | -18.41 | 73 | 13.7 | -23.30 | -4.85 | -30.56 | 90 |
| 29 | Connors RSI(2) · 1h | reversion | 80.56 | -19.44 | 211 | 40.3 | -18.17 | -6.39 | -18.30 | 114 |
| 30 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 31 | Keltner breakout · 1h | breakout | 80.50 | -19.50 | 120 | 25.8 | -16.73 | -3.37 | -25.32 | 170 |
| 32 | Hold BTC | benchmark | 80.21 | -19.79 | 1 | 0.0 | -12.23 | -1.69 | -22.00 | 1 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 79.85 | -20.15 | 2 | 0.0 | -10.75 | -1.25 | -24.16 | 1 |
| 34 | Opening range 15m | breakout | 78.60 | -21.39 | 526 | 31.2 | -17.07 | -4.56 | -21.36 | 719 |
| 35 | Stochastic reversion · 1h | reversion | 78.37 | -21.63 | 302 | 47.4 | -27.24 | -4.04 | -28.25 | 392 |
| 36 | ADX DI cross · 1h | trend | 76.89 | -23.11 | 198 | 19.7 | -24.33 | -3.69 | -32.07 | 274 |
| 37 | MFI reversion · 1h | reversion | 76.58 | -23.42 | 395 | 35.2 | -21.98 | -2.87 | -25.30 | 162 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -45.12 | -2.86 | -50.19 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.42 | -4.65 | -30.71 | 239 |
| 41 | Heikin-Ashi · 1h | trend | 74.72 | -25.28 | 440 | 24.3 | -38.14 | -7.09 | -39.26 | 660 |
| 42 | MACD cross · 1h | trend | 74.10 | -25.90 | 384 | 23.4 | -29.68 | -4.40 | -38.65 | 472 |
| 43 | MACD zero-line · 1h | trend | 73.46 | -26.54 | 171 | 18.7 | -23.27 | -4.55 | -30.99 | 203 |
| 44 | Max aggression: 1-day momentum | meta | 73.07 | -26.93 | 29 | 27.6 | -21.87 | -0.72 | -57.50 | 41 |
| 45 | RSI momentum · 1h | momentum | 72.42 | -27.58 | 169 | 13.0 | -27.39 | -4.22 | -37.83 | 209 |
| 46 | Supertrend · 1h | trend | 72.17 | -27.83 | 180 | 15.0 | -30.83 | -5.26 | -36.51 | 215 |
| 47 | EMA 20/50 cross · 1h | trend | 71.72 | -28.27 | 109 | 10.1 | -29.68 | -5.02 | -40.33 | 121 |
| 48 | ROC + volume · 1h | momentum | 71.32 | -28.68 | 396 | 28.8 | -31.27 | -5.75 | -38.37 | 376 |
| 49 | Triple EMA stack · 1h | trend | 71.14 | -28.86 | 150 | 14.0 | -29.31 | -4.87 | -38.47 | 205 |
| 50 | Bollinger reversion · 1h | reversion | 70.73 | -29.27 | 300 | 41.3 | -34.07 | -5.31 | -35.72 | 381 |
| 51 | CCI reversion · 1h | reversion | 70.06 | -29.94 | 346 | 43.4 | -39.35 | -6.19 | -39.57 | 462 |
| 52 | OBV trend · 1h | momentum | 69.42 | -30.59 | 296 | 18.9 | -30.56 | -5.37 | -38.46 | 276 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -34.33 | -4.63 | -37.57 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.00 | -31.00 | 153 | 19.0 | -30.41 | -5.43 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.07 | -32.93 | 381 | 43.6 | -43.38 | -7.11 | -44.04 | 531 |
| 56 | Z-score reversion · 1h | reversion | 64.49 | -35.51 | 204 | 37.3 | -31.49 | -4.42 | -31.55 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 64.31 | -35.69 | 260 | 10.0 | -38.41 | -7.72 | -43.13 | 329 |
| 58 | Agent (ML meta-label) | meta | 63.98 | -36.02 | 1835 | 24.7 | -16.63 | -2.40 | -22.67 | 333 |
| 59 | RSI(14) reversion · 1h | reversion | 63.05 | -36.95 | 186 | 32.8 | -38.47 | -5.71 | -38.79 | 240 |
| 60 | VWAP momentum · 1h | momentum | 62.28 | -37.73 | 909 | 22.2 | -52.60 | -10.68 | -53.13 | 1216 |
| 61 | Candlestick reversal · 1h | reversion | 60.95 | -39.05 | 486 | 28.4 | -45.31 | -8.28 | -45.92 | 593 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.42 | -22.17 | -49.51 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.42 | -99.00 | 5257 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.14 | -25.71 | -80.18 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -46.38 | -93.83 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.64 | -89.31 | 1919 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -41.24 | -91.31 | 2335 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.76 | -31.12 | -89.77 | 2193 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -52.46 | -97.90 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -57.61 | -96.28 | 3436 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.81 | -33.88 | -93.81 | 2348 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.21 | -34.87 | -83.21 | 1660 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -55.68 | -99.59 | 6026 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -42.64 | -92.24 | 2610 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.12 | -95.40 | 3468 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.13 | -99.81 | 6146 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -42.78 | -92.29 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.64 | -25.94 | -75.84 | 1658 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -60.31 | -97.63 | 3508 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.91 | -64.07 | -98.91 | 4936 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.57 | -26.79 | -68.79 | 1240 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -56.86 | -94.74 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.99 | -38.94 | -85.18 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.87 | -99.67 | 6368 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.20 | -32.72 | -90.20 | 2313 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.03 | -20.14 | -79.04 | 1787 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.04 | -37.05 | -91.04 | 2190 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.06 | -52.05 | -97.06 | 3891 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -58.22 | -89.39 | 2135 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.63 | -30.91 | -66.63 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.32 | -22.94 | -71.48 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.74 | -19.19 | -80.74 | 1750 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.45 | -51.00 | -97.45 | 4348 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -109.04 | -99.93 | 8376 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T15:40 | Candlestick reversal · 1h | buy | ETH-USD | 5.27 | — | rebalance up |
| 2026-11-13T15:40 | Candlestick reversal · 1h | buy | BTC-USD | 5.17 | — | rebalance up |
| 2026-11-13T15:40 | Candlestick reversal · 1h | sell | XRP-USD | 9.99 | -0.30 | stop-loss |
| 2026-11-13T15:40 | Candlestick reversal · 1h | sell | SQQQ | 10.81 | 0.74 | take-profit |
| 2026-11-13T15:40 | ADX DI cross · 1h | sell | DOGE-USD | 19.01 | -0.55 | stop-loss |
| 2026-11-13T15:40 | MACD cross · 1h | buy | SOL-USD | 4.19 | — | rebalance up |
| 2026-11-13T15:40 | MACD cross · 1h | buy | DOGE-USD | 4.97 | — | rebalance up |
| 2026-11-13T15:40 | MACD cross · 1h | buy | BTC-USD | 4.88 | — | rebalance up |
| 2026-11-13T15:40 | MACD cross · 1h | sell | ETH-USD | 10.54 | -0.25 | stop-loss |
| 2026-11-13T15:35 | VWAP momentum · 1h | buy | XRP-USD | 3.10 | — | rebalance up |
| 2026-11-13T15:35 | MACD cross · 1h | buy | ETH-USD | 3.72 | — | rebalance up |
| 2026-11-13T15:30 | Agent (ML meta-label) | buy | GOOGL | 11.25 | — | rebalance up |
| 2026-11-13T15:30 | Agent (ML meta-label) | buy | AAPL | 3.68 | — | rebalance up |
| 2026-11-13T15:30 | Agent (ML meta-label) | sell | TECL | 10.61 | -0.51 | selected signal exited |
| 2026-11-13T15:30 | Agent (ML meta-label) | sell | AMD | 10.67 | -0.31 | selected signal exited |
| 2026-11-13T15:30 | CCI reversion · 1h | buy | META | 8.81 | — | entry signal |
| 2026-11-13T15:30 | Williams %R · 1h | buy | META | 3.88 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | buy | ETH-USD | 4.03 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | buy | BTC-USD | 3.93 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | buy | AMZN | 3.91 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | sell | SQQQ | 10.11 | 0.44 | exit signal |
| 2026-11-13T15:30 | Stochastic reversion · 1h | buy | TNA | 5.60 | — | entry signal |
| 2026-11-13T15:30 | Stochastic reversion · 1h | buy | IWM | 13.09 | — | entry signal |
| 2026-11-13T15:30 | Stochastic reversion · 1h | sell | SQQQ | 12.69 | 0.94 | exit signal |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | XRP-USD | 3.25 | — | rebalance up |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | NVDA | 3.53 | — | rebalance up |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | ETH-USD | 3.36 | — | rebalance up |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | BTC-USD | 3.23 | — | rebalance up |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | sell | SQQQ | 13.37 | 0.59 | exit signal |
| 2026-11-13T15:30 | Candlestick reversal · 1h | buy | MSFT | 12.24 | — | entry signal |
| 2026-11-13T15:30 | Candlestick reversal · 1h | sell | NVDA | 9.91 | -0.36 | exit signal |
| 2026-11-13T15:30 | Donchian 20/10 · 1h | buy | TSLA | 3.49 | — | rebalance up |
| 2026-11-13T15:30 | Donchian 20/10 · 1h | buy | GOOGL | 3.49 | — | rebalance up |
| 2026-11-13T15:30 | Donchian 20/10 · 1h | buy | AAPL | 3.48 | — | rebalance up |
| 2026-11-13T15:30 | Donchian 20/10 · 1h | sell | SPY | 13.80 | -0.05 | exit signal |
| 2026-11-13T15:30 | Donchian 20/10 · 1h | sell | AMD | 13.92 | 0.58 | exit signal |
| 2026-11-13T15:30 | OBV trend · 1h | sell | TSLA | 17.48 | -0.14 | exit signal |
| 2026-11-13T15:30 | RSI momentum · 1h | sell | SPY | 12.10 | -0.04 | exit signal |
| 2026-11-13T15:30 | ROC + volume · 1h | buy | SQQQ | 17.63 | — | entry signal |
| 2026-11-13T15:30 | ROC + volume · 1h | buy | GOOGL | 17.86 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 15:40:05.000109+00:00 -> 2026-11-13 15:50:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
