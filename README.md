# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T14:40:05.000110+00:00 · 58304 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.54 (-14.46%)

Closed trades 190, win rate 35.3%, fees £5.55, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 17.10 | -0.01 |

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

Today: 12597 decisions in 2367 calls, $0.1742 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T14:40 | 4 / 16 / 11 | AAPL 16%, META 14% |  |
| Breezy | 2026-11-13T14:40 | 0 / 26 / 5 | cash |  |
| Boozy | 2026-11-13T14:40 | 4 / 25 / 2 | COIN 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| MFI reversion | LABU | 1.94 | +6.82% | 7 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.78 | 17.78 | 0 | — | 15.41 | 5.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 22 | 68.2 | 16.23 | 3.32 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.10 | 12.11 | 34 | 29.4 | 20.45 | 3.04 | -8.66 | 45 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.44 | 5.44 | 0 | — | 7.61 | 2.05 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.70 | 0.70 | 140 | 35.0 | 7.29 | 2.88 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.49 | -1.51 | 0 | — | -0.26 | -0.01 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 97.63 | -2.37 | 191 | 30.4 | -1.17 | -0.37 | -8.69 | 161 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.50 | -2.50 | 1 | 0.0 | -2.47 | -1.69 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.07 | -3.93 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 95.36 | -4.64 | 43 | 39.5 | -3.93 | -0.70 | -14.81 | 66 |
| 16 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.59 | -5.41 | 0 | — | -3.72 | -0.96 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Trend pullback · 1h | trend | 92.22 | -7.78 | 110 | 22.7 | -12.90 | -4.38 | -17.58 | 72 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 92.05 | -7.96 | 1 | 0.0 | -8.24 | -1.84 | -16.91 | 2 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 86.24 | -13.76 | 174 | 28.7 | -14.75 | -3.17 | -21.80 | 217 |
| 24 | Opening range 30m | breakout | 85.89 | -14.11 | 433 | 33.3 | -10.12 | -3.20 | -14.11 | 601 |
| 25 | Agent | meta | 85.54 | -14.46 | 190 | 35.3 | -15.16 | -7.61 | -15.16 | 207 |
| 26 | Daily: Bullish score | daily | 85.43 | -14.57 | 16 | 18.8 | -10.41 | -1.66 | -19.56 | 15 |
| 27 | Agent (aggressive) | meta | 83.73 | -16.27 | 92 | 33.7 | -16.99 | -4.77 | -18.51 | 99 |
| 28 | Donchian 55/20 · 1h | breakout | 83.58 | -16.42 | 73 | 13.7 | -21.51 | -4.50 | -29.68 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 81.65 | -18.35 | 2 | 0.0 | -8.84 | -0.99 | -24.16 | 1 |
| 30 | Hold BTC | benchmark | 81.43 | -18.57 | 1 | 0.0 | -11.03 | -1.51 | -22.00 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.26 | -18.74 | 115 | 24.3 | -16.24 | -3.27 | -25.14 | 170 |
| 32 | Connors RSI(2) · 1h | reversion | 81.01 | -18.99 | 210 | 40.5 | -17.74 | -6.21 | -18.30 | 114 |
| 33 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 34 | Max aggression: 5-day momentum | meta | 80.16 | -19.84 | 20 | 45.0 | -36.08 | -2.30 | -45.81 | 22 |
| 35 | ADX DI cross · 1h | trend | 79.43 | -20.57 | 192 | 19.3 | -21.86 | -3.37 | -29.76 | 273 |
| 36 | Stochastic reversion · 1h | reversion | 78.50 | -21.50 | 300 | 47.3 | -27.24 | -4.04 | -28.24 | 390 |
| 37 | Opening range 15m | breakout | 78.23 | -21.77 | 524 | 31.3 | -17.52 | -4.71 | -21.36 | 715 |
| 38 | MFI reversion · 1h | reversion | 78.09 | -21.91 | 394 | 35.3 | -21.17 | -2.77 | -24.58 | 162 |
| 39 | Heikin-Ashi · 1h | trend | 76.25 | -23.75 | 438 | 24.4 | -36.88 | -6.91 | -38.20 | 660 |
| 40 | MACD cross · 1h | trend | 75.90 | -24.10 | 380 | 23.4 | -27.91 | -4.15 | -38.65 | 472 |
| 41 | Bollinger breakout · 1h | breakout | 75.73 | -24.27 | 180 | 22.2 | -22.58 | -4.72 | -30.16 | 240 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 43 | Max aggression: 1-day momentum | meta | 75.30 | -24.70 | 29 | 27.6 | -19.57 | -0.58 | -57.50 | 41 |
| 44 | Supertrend · 1h | trend | 74.84 | -25.16 | 172 | 14.0 | -28.41 | -4.90 | -36.51 | 214 |
| 45 | RSI momentum · 1h | momentum | 74.43 | -25.57 | 162 | 13.6 | -24.90 | -3.88 | -36.35 | 210 |
| 46 | MACD zero-line · 1h | trend | 74.28 | -25.72 | 170 | 18.2 | -22.34 | -4.37 | -30.99 | 203 |
| 47 | EMA 20/50 cross · 1h | trend | 74.10 | -25.90 | 105 | 10.5 | -27.39 | -4.66 | -38.62 | 121 |
| 48 | Triple EMA stack · 1h | trend | 72.91 | -27.09 | 147 | 14.3 | -27.67 | -4.56 | -37.19 | 205 |
| 49 | ROC + volume · 1h | momentum | 72.58 | -27.42 | 394 | 28.9 | -30.13 | -5.54 | -38.37 | 374 |
| 50 | Daily: Momentum burst | daily | 71.84 | -28.16 | 27 | 11.1 | -32.45 | -4.42 | -36.97 | 33 |
| 51 | CCI reversion · 1h | reversion | 71.58 | -28.42 | 345 | 43.5 | -37.84 | -5.99 | -38.14 | 461 |
| 52 | Bollinger reversion · 1h | reversion | 71.54 | -28.46 | 300 | 41.3 | -33.36 | -5.21 | -35.72 | 381 |
| 53 | Donchian 20/10 · 1h | breakout | 71.29 | -28.71 | 145 | 19.3 | -27.94 | -5.08 | -35.90 | 209 |
| 54 | OBV trend · 1h | momentum | 71.23 | -28.77 | 292 | 19.2 | -28.26 | -4.96 | -36.70 | 275 |
| 55 | Williams %R · 1h | reversion | 67.83 | -32.17 | 379 | 43.5 | -43.09 | -7.09 | -43.62 | 533 |
| 56 | EMA 9/21 cross · 1h | trend | 66.56 | -33.44 | 259 | 10.0 | -35.84 | -7.39 | -41.97 | 329 |
| 57 | Z-score reversion · 1h | reversion | 65.89 | -34.11 | 204 | 37.3 | -29.87 | -4.23 | -30.00 | 236 |
| 58 | Agent (ML meta-label) | meta | 65.27 | -34.73 | 1823 | 24.7 | -17.64 | -2.79 | -23.50 | 333 |
| 59 | VWAP momentum · 1h | momentum | 64.90 | -35.10 | 902 | 22.3 | -51.16 | -10.49 | -51.73 | 1217 |
| 60 | RSI(14) reversion · 1h | reversion | 63.83 | -36.17 | 185 | 32.4 | -37.59 | -5.59 | -37.88 | 239 |
| 61 | Candlestick reversal · 1h | reversion | 61.53 | -38.47 | 482 | 28.4 | -44.87 | -8.24 | -45.38 | 591 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.42 | -22.17 | -49.51 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -43.77 | -98.98 | 5256 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.86 | -25.46 | -79.91 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -45.99 | -93.78 | 2530 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.17 | -31.14 | -89.31 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.23 | -40.84 | -91.24 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.72 | -30.94 | -89.72 | 2192 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -51.80 | -97.89 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -56.80 | -96.24 | 3436 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.78 | -33.94 | -93.79 | 2346 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.18 | -34.57 | -83.18 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -54.97 | -99.58 | 6009 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.24 | -43.17 | -92.24 | 2610 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.31 | -36.37 | -95.31 | 3464 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.02 | -99.81 | 6146 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -42.78 | -92.29 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.93 | -26.18 | -75.93 | 1643 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -60.31 | -97.64 | 3509 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -63.53 | -98.89 | 4926 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.79 | -27.11 | -68.79 | 1238 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -56.73 | -94.75 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.21 | -39.85 | -85.21 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.32 | -99.66 | 6358 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.08 | -32.50 | -90.12 | 2305 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.77 | -20.15 | -78.88 | 1782 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.73 | -36.28 | -90.80 | 2173 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.99 | -52.75 | -96.99 | 3870 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.31 | -57.72 | -89.32 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.41 | -30.56 | -66.41 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.47 | -23.09 | -71.48 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.45 | -19.29 | -80.68 | 1735 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.36 | -50.16 | -97.38 | 4315 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -109.69 | -99.93 | 8371 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 25.18 | — | entry |
| 2026-11-13T14:40 | Day trade: Stocks in Play ORB | buy | COIN | 25.18 | — | entry |
| 2026-11-13T14:40 | Agent | buy | AMZN | 17.11 | — | following Supertrend |
| 2026-11-13T14:40 | Bollinger breakout · 1h | sell | AMD | 18.00 | -0.99 | stop-loss |
| 2026-11-13T14:40 | ROC + volume · 1h | sell | AMD | 18.10 | -0.12 | stop-loss |
| 2026-11-13T14:40 | VWAP momentum · 1h | buy | SOL-USD | 4.73 | — | rebalance up |
| 2026-11-13T14:40 | VWAP momentum · 1h | sell | AMD | 6.37 | -0.35 | stop-loss |
| 2026-11-13T14:35 | Max aggression: 5-day momentum | buy | SOXL | 81.45 | — | entry |
| 2026-11-13T14:35 | Max aggression: 1-day momentum | buy | NVDA | 76.00 | — | entry |
| 2026-11-13T14:35 | Agent (rotation) | buy | TQQQ | 32.61 | — | following Z-score reversion |
| 2026-11-13T14:35 | Agent (rotation) | buy | QQQ | 32.61 | — | entry |
| 2026-11-13T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 111.73 | — | entry |
| 2026-11-13T14:35 | Agent (ML meta-label) | buy | AAPL | 5.94 | — | entry |
| 2026-11-13T14:35 | Agent (ML meta-label) | sell | MSFT | 3.62 | -0.08 | selected signal exited |
| 2026-11-13T14:35 | Agent (ML meta-label) | sell | LABU | 1.82 | -0.15 | selected signal exited |
| 2026-11-13T14:35 | Agent (ML meta-label) | sell | ETHU | 3.70 | -0.22 | selected signal exited |
| 2026-11-13T14:35 | MFI reversion · 1h | buy | TECL | 19.51 | — | entry |
| 2026-11-13T14:35 | MFI reversion · 1h | buy | META | 19.52 | — | entry |
| 2026-11-13T14:35 | MFI reversion · 1h | buy | BTC-USD | 6.42 | — | rebalance up |
| 2026-11-13T14:35 | MFI reversion · 1h | buy | AMZN | 13.38 | — | rebalance up |
| 2026-11-13T14:35 | MFI reversion · 1h | sell | NVDA | 10.05 | 0.01 | target is flat |
| 2026-11-13T14:35 | MFI reversion · 1h | sell | MSFT | 6.53 | -0.17 | stop-loss |
| 2026-11-13T14:35 | MFI reversion · 1h | sell | LABU | 6.94 | -0.30 | target is flat |
| 2026-11-13T14:35 | MFI reversion · 1h | sell | ETHU | 5.84 | -0.34 | stop-loss |
| 2026-11-13T14:35 | CCI reversion · 1h | buy | NVDA | 8.94 | — | entry |
| 2026-11-13T14:35 | CCI reversion · 1h | buy | COIN | 8.94 | — | entry |
| 2026-11-13T14:35 | CCI reversion · 1h | buy | AMZN | 8.94 | — | entry |
| 2026-11-13T14:35 | Williams %R · 1h | buy | SQQQ | 9.66 | — | entry |
| 2026-11-13T14:35 | Williams %R · 1h | buy | META | 9.66 | — | entry |
| 2026-11-13T14:35 | Williams %R · 1h | buy | ETH-USD | 4.81 | — | rebalance up |
| 2026-11-13T14:35 | Williams %R · 1h | buy | COIN | 9.66 | — | entry |
| 2026-11-13T14:35 | Williams %R · 1h | buy | BTC-USD | 4.86 | — | rebalance up |
| 2026-11-13T14:35 | Williams %R · 1h | buy | AMZN | 9.66 | — | entry |
| 2026-11-13T14:35 | Stochastic reversion · 1h | buy | BTC-USD | 4.14 | — | rebalance up |
| 2026-11-13T14:35 | Stochastic reversion · 1h | sell | BITX | 8.65 | -0.78 | stop-loss |
| 2026-11-13T14:35 | Z-score reversion · 1h | buy | ETH-USD | 4.71 | — | rebalance up |
| 2026-11-13T14:35 | Z-score reversion · 1h | sell | ETHU | 12.85 | -1.14 | stop-loss |
| 2026-11-13T14:35 | Bollinger reversion · 1h | buy | MSFT | 8.94 | — | rebalance up |
| 2026-11-13T14:35 | Bollinger reversion · 1h | buy | META | 8.66 | — | rebalance up |
| 2026-11-13T14:35 | Bollinger reversion · 1h | buy | ETH-USD | 10.60 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 14:40:05.000110+00:00 -> 2026-11-13 14:50:05.000110+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
