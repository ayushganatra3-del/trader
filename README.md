# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T18:55:05.000158+00:00 · 48772 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.06 (-10.94%)

Closed trades 147, win rate 37.4%, fees £4.06, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-05 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 32403 decisions in 3018 calls, $0.4065 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T18:55 | 0 / 18 / 13 | cash |  |
| Breezy | 2026-11-05T18:55 | 0 / 23 / 8 | cash |  |
| Boozy | 2026-11-05T18:55 | 5 / 20 / 6 | BITX 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.22 | 13.22 | 18 | 66.7 | 16.93 | 3.28 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.41 | 12.41 | 0 | — | 14.08 | 4.87 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.46 | 7.46 | 28 | 25.0 | 16.34 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.38 | 3.38 | 28 | 42.9 | 1.90 | 0.58 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 98.87 | -1.13 | 0 | — | 2.80 | 0.88 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.62 | -1.38 | 106 | 46.2 | -14.05 | -3.50 | -14.84 | 143 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.68 | -2.32 | 116 | 34.5 | 4.93 | 2.52 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.25 | -4.75 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.34 | 0.20 | -9.18 | 220 |
| 14 | Agent (rotation) | meta | 94.89 | -5.11 | 174 | 27.6 | -5.84 | -3.48 | -10.09 | 176 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Hold SPY | benchmark | 94.02 | -5.98 | 0 | — | -4.47 | -1.72 | -5.91 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -11.51 | -1.29 | -17.84 | 8 |
| 18 | Trend pullback · 1h | trend | 92.12 | -7.88 | 105 | 22.9 | -15.37 | -5.50 | -17.86 | 81 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 89.98 | -10.02 | 0 | — | -6.79 | -2.03 | -10.50 | 1 |
| 21 | Opening range 30m | breakout | 89.82 | -10.18 | 365 | 32.9 | -15.07 | -4.85 | -17.21 | 584 |
| 22 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -13.41 | -7.55 | -13.81 | 212 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.23 | -3.21 | -14.15 | 86 |
| 24 | Hold BTC ⏸ | benchmark | 88.43 | -11.57 | 1 | 0.0 | -4.96 | -0.62 | -13.41 | 1 |
| 25 | Daily: Bullish score | daily | 88.39 | -11.61 | 14 | 21.4 | -8.12 | -1.22 | -16.58 | 14 |
| 26 | Parabolic SAR · 1h | trend | 87.21 | -12.79 | 166 | 27.1 | -17.92 | -3.96 | -21.06 | 242 |
| 27 | Copy: Insider buying | copy | 86.58 | -13.42 | 40 | 37.5 | -24.79 | -4.92 | -25.48 | 65 |
| 28 | Donchian 55/20 · 1h | breakout | 86.26 | -13.74 | 71 | 14.1 | -13.59 | -2.89 | -19.94 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -33.99 | -2.13 | -37.55 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.08 | -5.32 | -18.47 | 97 |
| 31 | Opening range 15m | breakout | 83.60 | -16.40 | 445 | 30.6 | -19.14 | -5.66 | -21.20 | 712 |
| 32 | Volume breakout · 1h | breakout | 82.39 | -17.61 | 144 | 27.8 | -13.79 | -3.14 | -18.40 | 96 |
| 33 | Keltner breakout · 1h | breakout | 81.65 | -18.35 | 106 | 23.6 | -25.28 | -5.39 | -26.12 | 188 |
| 34 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -27.79 | -4.54 | -28.55 | 381 |
| 35 | Connors RSI(2) · 1h | reversion | 80.51 | -19.49 | 202 | 40.1 | -21.00 | -6.83 | -21.51 | 133 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -15.92 | -2.17 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.88 | -3.89 | -26.45 | 263 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -17.26 | -2.49 | -19.25 | 150 |
| 39 | Bollinger breakout · 1h | breakout | 78.85 | -21.15 | 165 | 23.6 | -23.19 | -4.76 | -26.52 | 252 |
| 40 | Ichimoku · 1h | trend | 78.38 | -21.62 | 94 | 14.9 | -24.28 | -4.94 | -28.68 | 131 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -27.51 | -4.38 | -29.42 | 445 |
| 42 | Heikin-Ashi · 1h | trend | 76.79 | -23.21 | 385 | 23.1 | -42.42 | -8.81 | -44.06 | 676 |
| 43 | EMA 20/50 cross · 1h | trend | 76.30 | -23.70 | 102 | 10.8 | -21.11 | -3.87 | -27.90 | 134 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -28.48 | -5.84 | -29.20 | 214 |
| 45 | Triple EMA stack · 1h | trend | 74.72 | -25.28 | 142 | 14.8 | -30.76 | -6.24 | -33.27 | 211 |
| 46 | RSI momentum · 1h | momentum | 73.57 | -26.43 | 158 | 12.7 | -30.76 | -5.89 | -32.35 | 226 |
| 47 | Supertrend · 1h | trend | 73.51 | -26.50 | 166 | 13.3 | -32.84 | -5.86 | -33.89 | 232 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.63 | -6.78 | -38.80 | 474 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -26.56 | -4.29 | -26.79 | 217 |
| 50 | Bollinger reversion · 1h | reversion | 72.49 | -27.51 | 237 | 40.1 | -33.02 | -6.33 | -33.34 | 361 |
| 51 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -35.04 | -4.91 | -37.28 | 32 |
| 52 | Donchian 20/10 · 1h | breakout | 72.09 | -27.91 | 140 | 20.0 | -32.37 | -5.98 | -34.25 | 220 |
| 53 | Williams %R · 1h ⏸ | reversion | 71.97 | -28.03 | 310 | 44.8 | -36.99 | -6.35 | -37.74 | 529 |
| 54 | ROC + volume · 1h | momentum | 71.50 | -28.50 | 340 | 25.6 | -37.02 | -7.25 | -38.35 | 386 |
| 55 | OBV trend · 1h | momentum | 71.24 | -28.76 | 264 | 17.4 | -34.43 | -7.25 | -34.74 | 297 |
| 56 | VWAP momentum · 1h | momentum | 68.11 | -31.89 | 756 | 22.2 | -54.92 | -11.92 | -55.98 | 1221 |
| 57 | EMA 9/21 cross · 1h | trend | 67.62 | -32.38 | 241 | 10.0 | -41.07 | -8.14 | -41.49 | 337 |
| 58 | Three white soldiers | momentum | 67.20 | -32.80 | 446 | 16.1 | -47.28 | -21.90 | -47.28 | 635 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -27.00 | -4.30 | -29.66 | 210 |
| 60 | Agent (ML meta-label) | meta | 65.37 | -34.63 | 1500 | 22.3 | -9.75 | -1.43 | -18.11 | 322 |
| 61 | Candlestick reversal · 1h | reversion | 65.27 | -34.73 | 388 | 29.1 | -39.00 | -7.19 | -39.21 | 564 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -42.88 | -2.70 | -54.67 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.67 | -98.93 | 5127 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.88 | -25.19 | -80.16 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.31 | -46.34 | -93.31 | 2499 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.81 | -30.78 | -88.93 | 1900 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.40 | -37.81 | -90.48 | 2284 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.72 | -32.51 | -90.79 | 2239 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -52.93 | -97.63 | 3418 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -56.51 | -96.12 | 3356 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.77 | -33.44 | -93.82 | 2454 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.69 | -36.05 | -81.75 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.51 | -99.52 | 5924 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.40 | -41.43 | -92.55 | 2561 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -37.91 | -95.91 | 3434 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.89 | -99.80 | 6140 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.55 | -42.70 | -91.55 | 2235 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.11 | -25.35 | -74.47 | 1532 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -60.45 | -97.71 | 3504 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -59.92 | -98.77 | 4847 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.02 | -27.68 | -70.03 | 1181 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.46 | -53.48 | -94.46 | 2717 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.46 | -35.70 | -84.48 | 1778 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.44 | -99.64 | 6318 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.01 | -30.38 | -89.08 | 2260 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.73 | -19.37 | -77.88 | 1728 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.17 | -35.47 | -91.22 | 2224 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.56 | -50.34 | -96.60 | 3832 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.11 | -51.05 | -89.11 | 2132 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.40 | -27.57 | -65.73 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.03 | -23.75 | -73.85 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.57 | -17.70 | -77.72 | 1654 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -48.63 | -97.25 | 4307 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.05 | -99.92 | 8179 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T18:55 | Agent (ML meta-label) | buy | GOOGL | 4.28 | — | entry |
| 2026-11-05T18:50 | Agent (ML meta-label) | sell | GOOGL | 5.93 | -0.01 | selected signal exited |
| 2026-11-05T18:45 | Agent (ML meta-label) | buy | GOOGL | 5.94 | — | entry |
| 2026-11-05T18:45 | Agent (ML meta-label) | sell | SQQQ | 6.03 | 0.07 | selected signal exited |
| 2026-11-05T18:30 | Agent (ML meta-label) | buy | TNA | 5.95 | — | entry |
| 2026-11-05T18:30 | Agent (ML meta-label) | buy | IWM | 5.95 | — | entry |
| 2026-11-05T18:30 | Bollinger reversion · 1h | buy | PLTR | 18.19 | — | entry signal |
| 2026-11-05T18:30 | Bollinger reversion · 1h | buy | LABU | 18.19 | — | entry signal |
| 2026-11-05T18:30 | Candlestick reversal · 1h | buy | TNA | 9.35 | — | entry signal |
| 2026-11-05T18:30 | Candlestick reversal · 1h | buy | IWM | 9.36 | — | entry signal |
| 2026-11-05T18:30 | Candlestick reversal · 1h | buy | COIN | 9.36 | — | entry signal |
| 2026-11-05T18:30 | Candlestick reversal · 1h | sell | PLTR | 3.77 | -0.02 | rebalance down |
| 2026-11-05T18:30 | Candlestick reversal · 1h | sell | MSTR | 3.87 | -0.01 | rebalance down |
| 2026-11-05T18:30 | Candlestick reversal · 1h | sell | GOOGL | 6.95 | -0.06 | rebalance down |
| 2026-11-05T18:30 | Candlestick reversal · 1h | sell | BITX | 7.12 | -0.01 | rebalance down |
| 2026-11-05T18:30 | ROC + volume · 1h | buy | AAPL | 17.68 | — | entry |
| 2026-11-05T18:30 | Supertrend · 1h | sell | MSFT | 18.23 | -0.22 | exit signal |
| 2026-11-05T18:25 | EMA 9/21 cross · 1h | sell | AAPL | 16.56 | -0.41 | stop-loss |
| 2026-11-05T18:20 | Agent (ML meta-label) | sell | GOOGL | 6.52 | -0.03 | selected signal exited |
| 2026-11-05T18:15 | Agent (ML meta-label) | buy | GOOGL | 6.55 | — | entry |
| 2026-11-05T18:15 | Agent (ML meta-label) | sell | SOXL | 6.65 | 0.12 | selected signal exited |
| 2026-11-05T18:15 | Candlestick reversal · 1h | buy | GOOGL | 3.30 | — | rebalance up |
| 2026-11-05T18:10 | Agent (ML meta-label) | buy | SOXL | 6.53 | — | following Connors RSI(2) |
| 2026-11-05T18:08 | Copy: Insider buying | buy | KNOP | 1.99 | — | entry |
| 2026-11-05T18:08 | Copy: Insider buying | buy | ASPE | 10.85 | — | entry |
| 2026-11-05T18:08 | Copy: Insider buying | sell | PLBY | 1.03 | -0.12 | target is flat |
| 2026-11-05T18:08 | Copy: Insider buying | sell | BPRE | 11.82 | -0.90 | target is flat |
| 2026-11-05T18:05 | Agent (ML meta-label) | buy | AAPL | 7.25 | — | entry |
| 2026-11-05T18:05 | Agent (ML meta-label) | sell | UPRO | 4.85 | -0.24 | selected signal exited |
| 2026-11-05T18:05 | Agent (ML meta-label) | sell | TECL | 6.44 | -0.10 | selected signal exited |
| 2026-11-05T18:05 | Hold BTC | sell | BTC-USD | 88.43 | -11.57 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T18:05 | Candlestick reversal · 1h | buy | BITX | 3.26 | — | rebalance up |
| 2026-11-05T18:05 | Candlestick reversal · 1h | sell | TECL | 12.90 | -0.61 | stop-loss |
| 2026-11-05T18:00 | Agent (ML meta-label) | buy | TECL | 6.55 | — | entry |
| 2026-11-05T18:00 | Agent (ML meta-label) | sell | AAPL | 5.06 | -0.11 | selected signal exited |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | TECL | 3.86 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | PLTR | 3.71 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | MSTR | 3.73 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | GOOGL | 3.74 | — | rebalance up |
| 2026-11-05T18:00 | Candlestick reversal · 1h | buy | BITX | 3.68 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 18:55:05.000158+00:00 -> 2026-11-05 19:05:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 18:55:05.000158+00:00 -> 2026-11-05 19:05:05.000158+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 18:55:05.000158+00:00 -> 2026-11-05 19:05:05.000158+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
