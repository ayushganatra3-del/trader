# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T19:25:05.000238+00:00 · 48801 ticks

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

Today: 35031 decisions in 3105 calls, $0.4373 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T19:25 | 1 / 5 / 25 | cash |  |
| Breezy | 2026-11-05T19:25 | 0 / 24 / 7 | cash |  |
| Boozy | 2026-11-05T19:25 | 3 / 21 / 7 | COIN 61% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.33 | 13.33 | 18 | 66.7 | 15.24 | 3.27 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.17 | 12.17 | 0 | — | 14.46 | 4.97 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.57 | 7.57 | 28 | 25.0 | 16.46 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.48 | 3.48 | 28 | 42.9 | 2.00 | 0.60 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 98.77 | -1.23 | 0 | — | 2.70 | 0.85 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.35 | -1.65 | 106 | 46.2 | -14.32 | -3.53 | -14.84 | 144 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.71 | -2.29 | 116 | 34.5 | 4.95 | 2.53 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.25 | -4.75 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.57 | 0.27 | -9.18 | 219 |
| 14 | Agent (rotation) | meta | 94.89 | -5.11 | 174 | 27.6 | -6.67 | -4.30 | -10.09 | 178 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Hold SPY | benchmark | 93.93 | -6.07 | 0 | — | -4.21 | -1.61 | -5.99 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -11.66 | -1.30 | -17.84 | 8 |
| 18 | Trend pullback · 1h | trend | 91.98 | -8.02 | 105 | 22.9 | -15.27 | -5.48 | -17.86 | 80 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.17 | -9.83 | 0 | — | -6.68 | -2.03 | -10.50 | 1 |
| 21 | Opening range 30m | breakout | 89.84 | -10.16 | 365 | 32.9 | -15.01 | -4.83 | -17.18 | 584 |
| 22 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -13.66 | -7.71 | -13.66 | 215 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.35 | -3.26 | -14.15 | 84 |
| 24 | Daily: Bullish score | daily | 88.45 | -11.55 | 14 | 21.4 | -8.31 | -1.25 | -16.58 | 14 |
| 25 | Hold BTC ⏸ | benchmark | 88.43 | -11.57 | 1 | 0.0 | -5.13 | -0.64 | -13.41 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.23 | -12.77 | 166 | 27.1 | -17.90 | -3.95 | -21.06 | 242 |
| 27 | Copy: Insider buying | copy | 86.50 | -13.50 | 40 | 37.5 | -24.85 | -4.93 | -25.48 | 65 |
| 28 | Donchian 55/20 · 1h | breakout | 86.28 | -13.72 | 71 | 14.1 | -13.57 | -2.89 | -19.94 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -34.26 | -2.14 | -37.55 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -19.46 | -5.82 | -19.60 | 104 |
| 31 | Opening range 15m | breakout | 83.62 | -16.38 | 445 | 30.6 | -19.13 | -5.66 | -21.17 | 712 |
| 32 | Volume breakout · 1h | breakout | 82.41 | -17.59 | 144 | 27.8 | -13.82 | -3.15 | -18.40 | 96 |
| 33 | Keltner breakout · 1h | breakout | 81.67 | -18.33 | 106 | 23.6 | -25.78 | -5.49 | -26.60 | 186 |
| 34 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -27.77 | -4.54 | -28.54 | 382 |
| 35 | Connors RSI(2) · 1h | reversion | 80.36 | -19.64 | 202 | 40.1 | -21.14 | -6.83 | -21.51 | 133 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -14.68 | -2.01 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.72 | -3.86 | -26.45 | 262 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -17.10 | -2.48 | -19.25 | 150 |
| 39 | Bollinger breakout · 1h | breakout | 78.87 | -21.13 | 165 | 23.6 | -23.31 | -4.79 | -26.52 | 252 |
| 40 | Ichimoku · 1h | trend | 78.40 | -21.60 | 94 | 14.9 | -24.26 | -4.94 | -28.68 | 131 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -28.20 | -4.48 | -30.10 | 445 |
| 42 | Heikin-Ashi · 1h | trend | 76.81 | -23.19 | 385 | 23.1 | -42.46 | -8.83 | -44.05 | 674 |
| 43 | EMA 20/50 cross · 1h | trend | 76.32 | -23.68 | 102 | 10.8 | -20.87 | -3.83 | -27.90 | 134 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -28.24 | -5.80 | -29.20 | 214 |
| 45 | Triple EMA stack · 1h | trend | 74.74 | -25.26 | 142 | 14.8 | -30.06 | -6.13 | -33.27 | 210 |
| 46 | RSI momentum · 1h | momentum | 73.54 | -26.46 | 158 | 12.7 | -30.80 | -5.89 | -32.35 | 226 |
| 47 | Supertrend · 1h | trend | 73.51 | -26.49 | 166 | 13.3 | -31.46 | -5.75 | -33.59 | 233 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.63 | -6.78 | -38.80 | 474 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -26.67 | -4.30 | -26.79 | 217 |
| 50 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -35.62 | -5.00 | -37.28 | 32 |
| 51 | Donchian 20/10 · 1h | breakout | 72.11 | -27.89 | 140 | 20.0 | -32.42 | -6.00 | -34.25 | 220 |
| 52 | Bollinger reversion · 1h ⏸ | reversion | 72.03 | -27.97 | 244 | 38.9 | -33.20 | -6.31 | -33.53 | 365 |
| 53 | Williams %R · 1h ⏸ | reversion | 71.97 | -28.03 | 310 | 44.8 | -36.99 | -6.34 | -37.72 | 529 |
| 54 | ROC + volume · 1h | momentum | 71.39 | -28.61 | 341 | 25.8 | -36.93 | -7.25 | -38.15 | 384 |
| 55 | OBV trend · 1h | momentum | 71.19 | -28.81 | 265 | 17.4 | -34.57 | -7.25 | -34.79 | 297 |
| 56 | VWAP momentum · 1h | momentum | 68.13 | -31.87 | 756 | 22.2 | -55.03 | -11.93 | -56.09 | 1220 |
| 57 | EMA 9/21 cross · 1h | trend | 67.59 | -32.41 | 241 | 10.0 | -41.11 | -8.15 | -41.50 | 337 |
| 58 | Three white soldiers | momentum | 67.20 | -32.80 | 446 | 16.1 | -47.20 | -21.90 | -47.20 | 634 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -26.91 | -4.39 | -29.66 | 212 |
| 60 | Agent (ML meta-label) | meta | 65.29 | -34.71 | 1505 | 22.4 | -11.37 | -1.61 | -19.98 | 327 |
| 61 | Candlestick reversal · 1h ⏸ | reversion | 64.98 | -35.02 | 395 | 28.6 | -39.81 | -7.53 | -40.02 | 567 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -43.12 | -2.71 | -54.67 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -45.30 | -98.92 | 5122 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.89 | -25.19 | -80.16 | 1406 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.28 | -46.22 | -93.28 | 2495 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.81 | -30.77 | -88.92 | 1893 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.43 | -37.89 | -90.51 | 2285 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.68 | -32.44 | -90.76 | 2235 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.67 | -53.56 | -97.67 | 3421 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.07 | -55.71 | -96.07 | 3345 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -33.43 | -93.81 | 2454 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.74 | -36.14 | -81.77 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.73 | -99.52 | 5920 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.54 | -42.50 | -92.58 | 2566 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -37.90 | -95.91 | 3433 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -69.64 | -99.80 | 6137 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.53 | -42.70 | -91.53 | 2228 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.51 | -25.91 | -74.59 | 1533 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -60.12 | -97.70 | 3496 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -59.73 | -98.77 | 4836 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.07 | -27.84 | -70.03 | 1182 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -54.15 | -94.55 | 2725 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.54 | -35.92 | -84.54 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.63 | -99.64 | 6313 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.01 | -30.37 | -89.08 | 2260 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.69 | -19.34 | -77.83 | 1720 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.06 | -35.80 | -91.10 | 2237 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.53 | -50.41 | -96.59 | 3830 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.31 | -52.41 | -89.31 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.51 | -27.72 | -65.84 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.98 | -23.74 | -73.80 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.69 | -17.74 | -77.80 | 1656 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.22 | -48.61 | -97.24 | 4301 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.45 | -99.93 | 8185 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T19:25 | Agent (ML meta-label) | buy | AAPL | 6.53 | — | entry |
| 2026-11-05T19:25 | Agent (ML meta-label) | sell | SQQQ | 6.53 | 0.00 | selected signal exited |
| 2026-11-05T19:20 | Agent (ML meta-label) | sell | GOOGL | 5.40 | -0.02 | selected signal exited |
| 2026-11-05T19:20 | Agent (ML meta-label) | sell | AAPL | 5.44 | -0.01 | selected signal exited |
| 2026-11-05T19:15 | Agent (ML meta-label) | buy | GOOGL | 5.42 | — | entry |
| 2026-11-05T19:15 | Agent (ML meta-label) | buy | AAPL | 5.46 | — | entry |
| 2026-11-05T19:15 | VWAP reversion · 1h | buy | XRP-USD | 4.93 | — | rebalance up |
| 2026-11-05T19:15 | VWAP reversion · 1h | sell | ETH-USD | 4.93 | -0.05 | rebalance down |
| 2026-11-05T19:10 | Agent (ML meta-label) | buy | SQQQ | 6.53 | — | entry |
| 2026-11-05T19:10 | Agent (ML meta-label) | sell | AAPL | 7.25 | 0.00 | selected signal exited |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | SOL-USD | 10.26 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | PLTR | 10.34 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | META | 10.33 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | LABU | 10.25 | -0.22 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | ETH-USD | 10.28 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | DOGE-USD | 10.28 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | BTC-USD | 10.29 | -0.08 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Candlestick reversal · 1h | sell | TNA | 9.21 | -0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Candlestick reversal · 1h | sell | PLTR | 9.31 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Candlestick reversal · 1h | sell | MSTR | 9.25 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Candlestick reversal · 1h | sell | IWM | 9.31 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Candlestick reversal · 1h | sell | GOOGL | 9.34 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Candlestick reversal · 1h | sell | COIN | 9.26 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Candlestick reversal · 1h | sell | BITX | 9.30 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:00 | Agent (ML meta-label) | sell | GOOGL | 4.29 | 0.01 | selected signal exited |
| 2026-11-05T19:00 | VWAP reversion · 1h | buy | XRP-USD | 9.93 | — | entry signal |
| 2026-11-05T19:00 | VWAP reversion · 1h | sell | DOGE-USD | 5.00 | -0.04 | rebalance down |
| 2026-11-05T19:00 | VWAP reversion · 1h | sell | BTC-USD | 4.93 | -0.05 | rebalance down |
| 2026-11-05T19:00 | Bollinger reversion · 1h | buy | SOL-USD | 10.35 | — | entry signal |
| 2026-11-05T19:00 | Bollinger reversion · 1h | buy | ETH-USD | 10.37 | — | entry signal |
| 2026-11-05T19:00 | Bollinger reversion · 1h | buy | DOGE-USD | 10.37 | — | entry signal |
| 2026-11-05T19:00 | Bollinger reversion · 1h | buy | BTC-USD | 10.37 | — | entry signal |
| 2026-11-05T19:00 | Bollinger reversion · 1h | sell | PLTR | 7.76 | -0.03 | rebalance down |
| 2026-11-05T19:00 | Bollinger reversion · 1h | sell | META | 7.71 | -0.07 | rebalance down |
| 2026-11-05T19:00 | Bollinger reversion · 1h | sell | LABU | 7.63 | -0.08 | rebalance down |
| 2026-11-05T19:00 | OBV trend · 1h | sell | MSFT | 17.69 | -0.21 | target is flat |
| 2026-11-05T19:00 | ROC + volume · 1h | sell | AAPL | 17.71 | 0.02 | target is flat |
| 2026-11-05T18:55 | Agent (ML meta-label) | buy | GOOGL | 4.28 | — | entry |
| 2026-11-05T18:50 | Agent (ML meta-label) | sell | GOOGL | 5.93 | -0.01 | selected signal exited |
| 2026-11-05T18:45 | Agent (ML meta-label) | buy | GOOGL | 5.94 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 19:25:05.000238+00:00 -> 2026-11-05 19:35:05.000238+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 19:25:05.000238+00:00 -> 2026-11-05 19:35:05.000238+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 19:25:05.000238+00:00 -> 2026-11-05 19:35:05.000238+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
