# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T18:40:05.000136+00:00 · 58508 ticks

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

Today: 31059 decisions in 2979 calls, $0.3902 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T18:40 | 3 / 15 / 12 | AMD 16% |  |
| Breezy | 2026-11-13T18:40 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-13T18:40 | 3 / 25 / 2 | MSTR 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| MFI reversion | TSLA | 1.72 | +2.15% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.70 | 17.70 | 0 | — | 15.11 | 5.05 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 115.94 | 15.94 | 34 | 29.4 | 24.32 | 3.47 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.88 | 12.88 | 22 | 68.2 | 16.27 | 3.33 | -4.91 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.43 | 5.43 | 32 | 43.8 | 5.33 | 1.34 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 105.12 | 5.12 | 0 | — | 7.07 | 1.92 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.34 | 1.34 | 141 | 34.8 | 7.91 | 3.11 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.10 | -1.90 | 0 | — | -0.85 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.62 | -3.38 | 1 | 0.0 | -3.53 | -2.27 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.33 | -3.67 | 191 | 30.4 | -2.61 | -0.89 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.26 | -3.74 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 93.92 | -6.08 | 43 | 39.5 | -5.44 | -1.02 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 19 | Copy: Congress Democrats (NANC) | copy | 93.11 | -6.89 | 0 | — | -5.41 | -1.45 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 91.90 | -8.10 | 110 | 22.7 | -14.62 | -5.35 | -17.77 | 71 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -11.26 | -2.40 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.97 | -14.03 | 433 | 33.3 | -10.15 | -3.21 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.90 | -14.10 | 16 | 18.8 | -10.07 | -1.59 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -15.44 | -7.73 | -15.99 | 209 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.62 | -3.37 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -17.73 | -5.00 | -18.65 | 100 |
| 28 | Donchian 55/20 · 1h | breakout | 81.84 | -18.16 | 73 | 13.7 | -23.23 | -4.84 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.28 | -18.72 | 1 | 0.0 | -11.01 | -1.56 | -22.00 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 80.89 | -19.11 | 2 | 0.0 | -9.86 | -1.13 | -24.16 | 1 |
| 31 | Connors RSI(2) · 1h | reversion | 80.67 | -19.33 | 211 | 40.3 | -18.12 | -6.37 | -18.32 | 114 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Keltner breakout · 1h | breakout | 80.53 | -19.48 | 120 | 25.8 | -17.37 | -3.51 | -25.32 | 171 |
| 34 | Stochastic reversion · 1h | reversion | 79.49 | -20.51 | 303 | 47.5 | -26.29 | -3.87 | -28.24 | 402 |
| 35 | Opening range 15m | breakout | 78.42 | -21.58 | 526 | 31.2 | -17.38 | -4.67 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 77.66 | -22.34 | 398 | 35.2 | -22.87 | -2.97 | -27.13 | 168 |
| 37 | ADX DI cross · 1h | trend | 76.74 | -23.26 | 198 | 19.7 | -23.55 | -3.54 | -32.11 | 271 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -41.52 | -2.68 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 240 |
| 41 | Heikin-Ashi · 1h | trend | 75.03 | -24.97 | 442 | 24.2 | -37.89 | -7.06 | -39.26 | 663 |
| 42 | MACD cross · 1h | trend | 74.70 | -25.30 | 385 | 23.6 | -29.27 | -4.34 | -38.65 | 469 |
| 43 | Max aggression: 1-day momentum | meta | 74.47 | -25.53 | 29 | 27.6 | -20.61 | -0.64 | -57.50 | 41 |
| 44 | MACD zero-line · 1h | trend | 73.46 | -26.54 | 171 | 18.7 | -23.24 | -4.55 | -30.99 | 202 |
| 45 | RSI momentum · 1h | momentum | 72.68 | -27.32 | 171 | 14.0 | -27.00 | -4.16 | -37.92 | 208 |
| 46 | Supertrend · 1h | trend | 72.59 | -27.41 | 180 | 15.0 | -30.54 | -5.22 | -36.51 | 215 |
| 47 | EMA 20/50 cross · 1h | trend | 72.23 | -27.77 | 109 | 10.1 | -28.60 | -4.82 | -40.51 | 120 |
| 48 | Bollinger reversion · 1h | reversion | 71.84 | -28.16 | 302 | 41.7 | -33.38 | -5.23 | -35.72 | 383 |
| 49 | Triple EMA stack · 1h | trend | 71.41 | -28.59 | 150 | 14.0 | -28.58 | -4.72 | -38.65 | 205 |
| 50 | ROC + volume · 1h | momentum | 71.36 | -28.64 | 397 | 28.7 | -31.40 | -5.77 | -38.37 | 376 |
| 51 | CCI reversion · 1h | reversion | 71.06 | -28.94 | 346 | 43.4 | -38.64 | -6.11 | -39.55 | 469 |
| 52 | OBV trend · 1h | momentum | 69.69 | -30.31 | 298 | 19.1 | -30.50 | -5.39 | -38.12 | 277 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -33.53 | -4.55 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.32 | -30.68 | 153 | 19.0 | -30.24 | -5.42 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.78 | -32.22 | 383 | 43.6 | -42.61 | -6.96 | -44.04 | 542 |
| 56 | Z-score reversion · 1h | reversion | 65.37 | -34.63 | 204 | 37.3 | -30.66 | -4.33 | -31.55 | 237 |
| 57 | Agent (ML meta-label) | meta | 64.78 | -35.22 | 1846 | 24.8 | -19.85 | -3.06 | -24.16 | 324 |
| 58 | EMA 9/21 cross · 1h | trend | 64.78 | -35.22 | 266 | 11.3 | -37.83 | -7.64 | -43.16 | 329 |
| 59 | RSI(14) reversion · 1h | reversion | 64.20 | -35.80 | 186 | 32.8 | -37.70 | -5.62 | -38.92 | 241 |
| 60 | VWAP momentum · 1h | momentum | 62.63 | -37.37 | 913 | 22.2 | -52.98 | -10.67 | -53.58 | 1222 |
| 61 | Candlestick reversal · 1h | reversion | 61.85 | -38.16 | 486 | 28.4 | -45.17 | -8.33 | -46.01 | 605 |
| 62 | Three white soldiers | momentum | 58.34 | -41.66 | 542 | 14.6 | -49.50 | -22.28 | -49.51 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -44.56 | -99.02 | 5298 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.05 | -25.63 | -80.23 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.85 | -46.52 | -93.85 | 2535 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -31.68 | -89.28 | 1927 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.33 | -41.68 | -91.35 | 2345 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.80 | -31.27 | -89.80 | 2197 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -52.41 | -97.90 | 3506 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -56.89 | -96.26 | 3425 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.80 | -33.61 | -93.80 | 2344 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.24 | -34.85 | -83.28 | 1665 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.57 | -99.58 | 6041 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -43.20 | -92.26 | 2632 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.10 | -95.40 | 3474 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.17 | -99.81 | 6167 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -43.24 | -92.31 | 2281 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.75 | -26.11 | -75.83 | 1643 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -60.94 | -97.63 | 3514 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.04 | -98.89 | 4942 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.72 | -27.02 | -68.82 | 1251 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -57.27 | -94.77 | 2806 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.08 | -39.42 | -85.18 | 1788 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.87 | -99.66 | 6379 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.06 | -32.63 | -90.20 | 2327 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.58 | -20.17 | -78.93 | 1800 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.76 | -36.70 | -90.90 | 2195 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.02 | -51.97 | -97.02 | 3887 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.43 | -58.30 | -89.49 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.46 | -30.64 | -66.46 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.39 | -23.07 | -71.43 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.02 | -19.28 | -80.35 | 1746 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.41 | -51.01 | -97.42 | 4353 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.51 | -99.93 | 8446 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-13T18:15 | MFI reversion · 1h | buy | NVDA | 9.67 | — | entry |
| 2026-11-13T18:15 | MFI reversion · 1h | sell | TECL | 5.76 | 0.03 | rebalance down |
| 2026-11-13T18:15 | MFI reversion · 1h | sell | QQQ | 5.82 | -0.01 | rebalance down |
| 2026-11-13T18:15 | MFI reversion · 1h | sell | META | 5.82 | 0.03 | rebalance down |
| 2026-11-13T18:15 | MFI reversion · 1h | sell | BTC-USD | 5.76 | -0.05 | rebalance down |
| 2026-11-13T18:15 | MFI reversion · 1h | sell | AMZN | 5.82 | -0.04 | rebalance down |
| 2026-11-13T18:15 | VWAP momentum · 1h | buy | TSLA | 9.49 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 18:40:05.000136+00:00 -> 2026-11-13 18:50:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
