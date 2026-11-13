# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T15:11:05.000177+00:00 · 58333 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.45 (-14.55%)

Closed trades 190, win rate 35.3%, fees £5.56, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 17.01 | -0.10 |
| PLTR | 17.08 | -0.01 |

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

Today: 15240 decisions in 2454 calls, $0.2052 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T15:11 | 1 / 4 / 26 | cash |  |
| Breezy | 2026-11-13T15:11 | 0 / 22 / 9 | cash |  |
| Boozy | 2026-11-13T15:11 | 3 / 18 / 10 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.59 | +2.90% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.61 | 17.61 | 0 | — | 15.24 | 5.09 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 115.61 | 15.61 | 34 | 29.4 | 24.21 | 3.46 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.56 | 12.56 | 22 | 68.2 | 16.17 | 3.31 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.16 | 5.16 | 0 | — | 7.32 | 1.98 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.13 | 5.13 | 32 | 43.8 | 5.23 | 1.32 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.27 | 1.27 | 141 | 34.8 | 7.88 | 3.10 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.86 | -2.14 | 0 | — | -0.89 | -0.23 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.46 | -3.54 | 1 | 0.0 | -3.51 | -2.26 | -5.91 | 2 |
| 13 | Agent (rotation) | meta | 96.24 | -3.76 | 191 | 30.4 | -2.58 | -0.88 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.07 | -3.93 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 94.77 | -5.22 | 43 | 39.5 | -4.53 | -0.83 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.41 | -6.59 | 0 | — | -4.92 | -1.31 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Trend pullback · 1h | trend | 92.03 | -7.97 | 110 | 22.7 | -13.07 | -4.46 | -17.58 | 72 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 89.09 | -10.91 | 1 | 0.0 | -11.19 | -2.39 | -17.11 | 2 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Daily: Bullish score | daily | 85.94 | -14.06 | 16 | 18.8 | -9.89 | -1.55 | -19.56 | 15 |
| 24 | Opening range 30m | breakout | 85.88 | -14.12 | 433 | 33.3 | -10.13 | -3.20 | -14.11 | 602 |
| 25 | Parabolic SAR · 1h | trend | 85.52 | -14.48 | 175 | 28.6 | -15.47 | -3.34 | -21.93 | 217 |
| 26 | Agent | meta | 85.45 | -14.55 | 190 | 35.3 | -15.10 | -7.61 | -15.27 | 211 |
| 27 | Agent (aggressive) | meta | 83.71 | -16.29 | 92 | 33.7 | -17.57 | -4.95 | -18.51 | 100 |
| 28 | Donchian 55/20 · 1h | breakout | 82.37 | -17.63 | 73 | 13.7 | -22.63 | -4.74 | -29.95 | 90 |
| 29 | Hold BTC | benchmark | 81.03 | -18.97 | 1 | 0.0 | -11.43 | -1.58 | -22.00 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.76 | -19.24 | 211 | 40.3 | -17.99 | -6.32 | -18.30 | 114 |
| 31 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 120 | 25.8 | -16.42 | -3.29 | -25.25 | 169 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 80.31 | -19.69 | 2 | 0.0 | -10.33 | -1.20 | -24.16 | 1 |
| 34 | Stochastic reversion · 1h | reversion | 78.68 | -21.32 | 301 | 47.2 | -27.04 | -4.00 | -28.25 | 390 |
| 35 | Opening range 15m | breakout | 78.47 | -21.53 | 524 | 31.3 | -17.27 | -4.63 | -21.36 | 718 |
| 36 | ADX DI cross · 1h | trend | 77.58 | -22.42 | 194 | 19.1 | -23.69 | -3.63 | -31.36 | 273 |
| 37 | MFI reversion · 1h | reversion | 77.26 | -22.74 | 395 | 35.2 | -21.31 | -2.79 | -24.71 | 162 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -41.73 | -2.69 | -47.37 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Heikin-Ashi · 1h | trend | 75.36 | -24.64 | 440 | 24.3 | -37.63 | -7.03 | -38.77 | 660 |
| 41 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.42 | -4.65 | -30.71 | 239 |
| 42 | MACD cross · 1h | trend | 74.95 | -25.05 | 381 | 23.4 | -28.83 | -4.29 | -38.65 | 472 |
| 43 | Max aggression: 1-day momentum | meta | 74.25 | -25.75 | 29 | 27.6 | -20.69 | -0.65 | -57.50 | 41 |
| 44 | MACD zero-line · 1h | trend | 73.60 | -26.40 | 170 | 18.2 | -23.14 | -4.53 | -30.99 | 203 |
| 45 | Supertrend · 1h | trend | 73.09 | -26.91 | 172 | 14.0 | -30.08 | -5.18 | -36.51 | 214 |
| 46 | RSI momentum · 1h | momentum | 73.05 | -26.95 | 164 | 13.4 | -26.53 | -4.12 | -37.09 | 209 |
| 47 | EMA 20/50 cross · 1h | trend | 72.66 | -27.34 | 108 | 10.2 | -28.85 | -4.91 | -39.61 | 121 |
| 48 | ROC + volume · 1h | momentum | 71.84 | -28.16 | 394 | 28.9 | -30.83 | -5.68 | -38.37 | 375 |
| 49 | Triple EMA stack · 1h | trend | 71.67 | -28.32 | 149 | 14.1 | -28.79 | -4.79 | -38.02 | 205 |
| 50 | Bollinger reversion · 1h | reversion | 71.37 | -28.63 | 300 | 41.3 | -33.55 | -5.24 | -35.72 | 381 |
| 51 | CCI reversion · 1h | reversion | 70.95 | -29.05 | 346 | 43.4 | -38.24 | -6.02 | -38.47 | 461 |
| 52 | Daily: Momentum burst | daily | 70.27 | -29.73 | 27 | 11.1 | -33.83 | -4.58 | -37.08 | 33 |
| 53 | OBV trend · 1h | momentum | 70.09 | -29.91 | 295 | 19.0 | -29.97 | -5.29 | -37.93 | 276 |
| 54 | Donchian 20/10 · 1h | breakout | 69.54 | -30.46 | 147 | 19.0 | -29.80 | -5.37 | -36.96 | 209 |
| 55 | Williams %R · 1h | reversion | 67.77 | -32.23 | 380 | 43.4 | -42.86 | -7.03 | -43.62 | 531 |
| 56 | Z-score reversion · 1h | reversion | 65.39 | -34.61 | 204 | 37.3 | -30.47 | -4.31 | -30.54 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 65.12 | -34.88 | 260 | 10.0 | -37.48 | -7.67 | -42.29 | 329 |
| 58 | Agent (ML meta-label) | meta | 64.39 | -35.61 | 1832 | 24.8 | -13.98 | -2.08 | -20.14 | 325 |
| 59 | RSI(14) reversion · 1h | reversion | 63.80 | -36.20 | 185 | 32.4 | -37.51 | -5.56 | -37.87 | 240 |
| 60 | VWAP momentum · 1h | momentum | 63.39 | -36.61 | 907 | 22.3 | -52.45 | -10.68 | -52.99 | 1216 |
| 61 | Candlestick reversal · 1h | reversion | 61.42 | -38.58 | 482 | 28.4 | -44.89 | -8.23 | -45.48 | 592 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.42 | -22.17 | -49.51 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -44.23 | -98.99 | 5253 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.04 | -25.65 | -80.08 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.80 | -46.23 | -93.81 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.26 | -31.54 | -89.31 | 1919 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -41.17 | -91.28 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.75 | -31.06 | -89.75 | 2192 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -52.38 | -97.90 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -56.79 | -96.24 | 3434 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.83 | -33.89 | -93.83 | 2351 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.15 | -34.65 | -83.16 | 1660 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -55.41 | -99.58 | 6001 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -42.72 | -92.24 | 2610 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.36 | -36.85 | -95.36 | 3468 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.35 | -99.81 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -42.78 | -92.29 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.88 | -25.99 | -76.02 | 1652 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -60.31 | -97.64 | 3509 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.90 | -63.82 | -98.90 | 4931 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.64 | -26.91 | -68.79 | 1240 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -56.86 | -94.75 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.10 | -39.35 | -85.21 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.90 | -99.67 | 6362 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.17 | -32.67 | -90.18 | 2310 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.70 | -20.17 | -78.75 | 1777 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.96 | -36.65 | -90.96 | 2180 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.00 | -52.68 | -97.01 | 3877 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -58.11 | -89.36 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.41 | -30.56 | -66.41 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.31 | -22.92 | -71.48 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.34 | -19.29 | -80.57 | 1741 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.41 | -50.85 | -97.41 | 4333 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -109.52 | -99.93 | 8373 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T15:10 | Agent (aggressive) | buy | PLTR | 41.87 | — | following VWAP reversion |
| 2026-11-13T15:10 | Agent | buy | PLTR | 17.09 | — | following VWAP reversion |
| 2026-11-13T15:10 | Connors RSI(2) · 1h | sell | IWM | 20.00 | -0.23 | stop-loss |
| 2026-11-13T15:10 | Keltner breakout · 1h | sell | GOOGL | 20.04 | 0.15 | stop-loss |
| 2026-11-13T15:10 | Bollinger breakout · 1h | sell | GOOGL | 19.26 | 0.25 | stop-loss |
| 2026-11-13T15:10 | VWAP momentum · 1h | buy | XRP-USD | 4.41 | — | rebalance up |
| 2026-11-13T15:10 | VWAP momentum · 1h | sell | TSLA | 10.57 | -0.23 | stop-loss |
| 2026-11-13T15:10 | Parabolic SAR · 1h | sell | TSLA | 21.08 | -0.56 | stop-loss |
| 2026-11-13T15:10 | MACD cross · 1h | buy | SOL-USD | 8.33 | — | entry |
| 2026-11-13T15:10 | MACD cross · 1h | sell | TSLA | 9.37 | -0.25 | stop-loss |
| 2026-11-13T15:05 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 112.62 | — | entry |
| 2026-11-13T15:05 | Agent (ML meta-label) | buy | TECL | 3.75 | — | rebalance up |
| 2026-11-13T15:05 | Agent (ML meta-label) | buy | SQQQ | 3.33 | — | rebalance up |
| 2026-11-13T15:05 | Agent (ML meta-label) | buy | NVDA | 3.52 | — | rebalance up |
| 2026-11-13T15:05 | Agent (ML meta-label) | buy | MSTR | 3.60 | — | rebalance up |
| 2026-11-13T15:05 | Agent (ML meta-label) | buy | AMZN | 4.76 | — | rebalance up |
| 2026-11-13T15:05 | Agent (ML meta-label) | buy | AMD | 3.70 | — | rebalance up |
| 2026-11-13T15:05 | Agent (ML meta-label) | sell | GOOGL | 8.03 | -0.04 | selected signal exited |
| 2026-11-13T15:05 | Agent (ML meta-label) | sell | AAPL | 8.03 | -0.04 | selected signal exited |
| 2026-11-13T15:05 | Keltner breakout · 1h | sell | TSLA | 20.09 | -0.23 | stop-loss |
| 2026-11-13T15:05 | Bollinger breakout · 1h | sell | TSLA | 18.85 | -0.19 | stop-loss |
| 2026-11-13T15:05 | Donchian 20/10 · 1h | sell | TECL | 6.02 | -0.51 | stop-loss |
| 2026-11-13T15:05 | OBV trend · 1h | buy | TSLA | 7.39 | — | rebalance up |
| 2026-11-13T15:05 | OBV trend · 1h | buy | GOOGL | 9.22 | — | rebalance up |
| 2026-11-13T15:05 | OBV trend · 1h | buy | AMD | 6.20 | — | rebalance up |
| 2026-11-13T15:05 | OBV trend · 1h | buy | AAPL | 5.65 | — | rebalance up |
| 2026-11-13T15:05 | OBV trend · 1h | sell | TQQQ | 7.81 | -0.17 | stop-loss |
| 2026-11-13T15:05 | OBV trend · 1h | sell | SPY | 8.88 | -0.07 | stop-loss |
| 2026-11-13T15:05 | OBV trend · 1h | sell | QQQ | 11.77 | -0.23 | stop-loss |
| 2026-11-13T15:05 | RSI momentum · 1h | sell | TECL | 4.58 | -0.39 | stop-loss |
| 2026-11-13T15:05 | Triple EMA stack · 1h | buy | TSLA | 5.80 | — | rebalance up |
| 2026-11-13T15:05 | Triple EMA stack · 1h | buy | GOOGL | 5.79 | — | rebalance up |
| 2026-11-13T15:05 | Triple EMA stack · 1h | sell | UPRO | 5.95 | -0.21 | stop-loss |
| 2026-11-13T15:05 | Triple EMA stack · 1h | sell | QQQ | 12.01 | -0.27 | stop-loss |
| 2026-11-13T15:05 | EMA 20/50 cross · 1h | buy | UPRO | 11.23 | — | rebalance up |
| 2026-11-13T15:05 | EMA 20/50 cross · 1h | buy | TSLA | 7.59 | — | rebalance up |
| 2026-11-13T15:05 | EMA 20/50 cross · 1h | buy | GOOGL | 5.71 | — | rebalance up |
| 2026-11-13T15:05 | EMA 20/50 cross · 1h | buy | AMD | 8.32 | — | rebalance up |
| 2026-11-13T15:05 | EMA 20/50 cross · 1h | sell | TQQQ | 10.11 | -0.60 | stop-loss |
| 2026-11-13T15:05 | EMA 20/50 cross · 1h | sell | SPY | 10.58 | -0.09 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 15:11:05.000177+00:00 -> 2026-11-13 15:21:05.000177+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
