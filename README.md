# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T19:55:05.000130+00:00 · 48823 ticks

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

Today: 37026 decisions in 3171 calls, $0.4606 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T19:55 | 1 / 23 / 6 | cash |  |
| Breezy | 2026-11-05T19:55 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-05T19:55 | 8 / 21 / 1 | COIN 68% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 111.95 | 11.95 | 0 | — | 13.72 | 4.74 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 18 | 66.7 | 12.91 | 3.22 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.56 | 5.56 | 28 | 25.0 | 14.10 | 2.65 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.54 | 1.54 | 28 | 42.9 | -0.06 | 0.09 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.75 | -0.25 | 0 | — | 3.55 | 1.10 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.17 | -0.83 | 106 | 46.2 | -13.74 | -3.48 | -14.84 | 144 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.22 | -2.78 | 116 | 34.5 | 4.42 | 2.36 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.22 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.40 | -4.60 | 0 | — | -3.49 | -1.30 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.04 | 0.10 | -9.18 | 218 |
| 14 | Hold SPY | benchmark | 94.66 | -5.34 | 0 | — | -3.53 | -1.43 | -5.99 | 1 |
| 15 | Agent (rotation) | meta | 94.57 | -5.43 | 174 | 27.6 | -8.14 | -5.60 | -10.99 | 173 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.34 | -7.66 | 105 | 22.9 | -14.99 | -5.36 | -17.86 | 80 |
| 18 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -9.03 | -1.11 | -17.84 | 8 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.34 | -9.66 | 0 | — | -6.92 | -2.13 | -10.50 | 1 |
| 21 | Opening range 30m | breakout | 89.41 | -10.59 | 365 | 32.9 | -16.07 | -5.27 | -17.38 | 580 |
| 22 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -13.62 | -7.74 | -14.01 | 209 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.48 | -3.33 | -14.15 | 85 |
| 24 | Hold BTC ⏸ | benchmark | 88.43 | -11.57 | 1 | 0.0 | -4.63 | -0.52 | -13.41 | 1 |
| 25 | Daily: Bullish score | daily | 88.22 | -11.78 | 14 | 21.4 | -8.57 | -1.31 | -16.58 | 14 |
| 26 | Parabolic SAR · 1h | trend | 86.81 | -13.19 | 166 | 27.1 | -17.99 | -3.89 | -21.06 | 241 |
| 27 | Copy: Insider buying | copy | 86.36 | -13.64 | 40 | 37.5 | -25.13 | -4.99 | -26.00 | 65 |
| 28 | Donchian 55/20 · 1h | breakout | 85.85 | -14.15 | 71 | 14.1 | -14.19 | -3.10 | -19.99 | 104 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -33.41 | -2.11 | -37.55 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.37 | -5.47 | -18.47 | 98 |
| 31 | Opening range 15m | breakout | 83.21 | -16.79 | 445 | 30.6 | -19.98 | -6.05 | -21.37 | 707 |
| 32 | Volume breakout · 1h | breakout | 82.02 | -17.98 | 144 | 27.8 | -14.20 | -3.28 | -18.40 | 96 |
| 33 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -26.52 | -4.55 | -28.37 | 384 |
| 34 | Keltner breakout · 1h | breakout | 81.28 | -18.73 | 106 | 23.6 | -25.67 | -5.49 | -26.12 | 187 |
| 35 | Connors RSI(2) · 1h | reversion | 80.88 | -19.12 | 202 | 40.1 | -20.59 | -6.90 | -21.37 | 133 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -14.28 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -24.84 | -3.99 | -26.47 | 259 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -17.01 | -2.58 | -19.25 | 152 |
| 39 | Bollinger breakout · 1h | breakout | 78.49 | -21.51 | 165 | 23.6 | -23.61 | -4.86 | -26.52 | 252 |
| 40 | Ichimoku · 1h | trend | 78.03 | -21.97 | 94 | 14.9 | -24.64 | -5.00 | -28.82 | 131 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -28.20 | -4.52 | -30.10 | 445 |
| 42 | Heikin-Ashi · 1h | trend | 76.44 | -23.56 | 385 | 23.1 | -42.77 | -8.93 | -44.06 | 674 |
| 43 | EMA 20/50 cross · 1h | trend | 76.01 | -23.99 | 102 | 10.8 | -21.07 | -3.71 | -28.28 | 132 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -28.09 | -5.80 | -29.20 | 213 |
| 45 | Triple EMA stack · 1h | trend | 74.38 | -25.62 | 142 | 14.8 | -30.36 | -6.17 | -33.24 | 211 |
| 46 | Supertrend · 1h | trend | 73.53 | -26.47 | 166 | 13.3 | -31.91 | -5.90 | -33.80 | 229 |
| 47 | RSI momentum · 1h | momentum | 73.36 | -26.64 | 158 | 12.7 | -29.00 | -5.41 | -31.84 | 223 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.12 | -6.57 | -38.80 | 473 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -25.33 | -4.24 | -26.79 | 218 |
| 50 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -34.66 | -4.94 | -37.28 | 32 |
| 51 | Bollinger reversion · 1h ⏸ | reversion | 72.03 | -27.97 | 244 | 38.9 | -32.70 | -6.49 | -34.02 | 373 |
| 52 | Williams %R · 1h ⏸ | reversion | 71.97 | -28.03 | 310 | 44.8 | -36.28 | -6.42 | -38.37 | 526 |
| 53 | Donchian 20/10 · 1h | breakout | 71.76 | -28.24 | 140 | 20.0 | -32.74 | -6.07 | -34.25 | 220 |
| 54 | OBV trend · 1h | momentum | 71.36 | -28.64 | 265 | 17.4 | -33.86 | -6.97 | -34.30 | 296 |
| 55 | ROC + volume · 1h | momentum | 71.33 | -28.67 | 341 | 25.8 | -37.03 | -7.32 | -38.14 | 384 |
| 56 | VWAP momentum · 1h | momentum | 67.91 | -32.09 | 756 | 22.2 | -55.18 | -12.09 | -56.10 | 1219 |
| 57 | EMA 9/21 cross · 1h | trend | 67.43 | -32.57 | 241 | 10.0 | -41.12 | -8.21 | -41.33 | 335 |
| 58 | Three white soldiers | momentum | 67.24 | -32.77 | 447 | 16.3 | -47.19 | -22.31 | -47.22 | 638 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -29.53 | -4.89 | -29.66 | 222 |
| 60 | Agent (ML meta-label) | meta | 65.95 | -34.05 | 1506 | 22.4 | -11.44 | -1.95 | -20.06 | 329 |
| 61 | Candlestick reversal · 1h ⏸ | reversion | 64.98 | -35.02 | 395 | 28.6 | -37.99 | -6.93 | -38.97 | 565 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -42.38 | -2.69 | -54.67 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -46.62 | -98.93 | 5124 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.82 | -25.87 | -80.03 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.29 | -48.77 | -93.29 | 2492 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.70 | -31.57 | -88.88 | 1896 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -39.54 | -90.49 | 2282 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.74 | -33.62 | -90.78 | 2234 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.62 | -55.78 | -97.65 | 3438 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -60.22 | -96.12 | 3343 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -34.39 | -93.77 | 2438 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.70 | -37.43 | -81.70 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -56.51 | -99.52 | 5931 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.39 | -42.85 | -92.57 | 2584 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.89 | -39.50 | -95.91 | 3432 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -77.91 | -99.80 | 6131 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.51 | -44.38 | -91.53 | 2244 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.47 | -26.45 | -74.66 | 1545 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -65.64 | -97.69 | 3487 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.76 | -64.54 | -98.77 | 4837 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.94 | -28.00 | -70.07 | 1203 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.45 | -55.66 | -94.54 | 2746 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.67 | -37.53 | -84.67 | 1779 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -77.15 | -99.64 | 6302 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.89 | -31.55 | -89.08 | 2260 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.54 | -19.75 | -77.96 | 1722 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.97 | -37.67 | -91.15 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.54 | -53.07 | -96.59 | 3828 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -55.93 | -89.26 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.51 | -28.43 | -65.84 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -24.51 | -73.80 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.28 | -18.07 | -77.70 | 1647 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.20 | -52.27 | -97.25 | 4292 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -112.99 | -99.93 | 8202 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T19:55 | Three white soldiers | buy | SOXL | 3.36 | — | rebalance up |
| 2026-11-05T19:55 | Three white soldiers | buy | ETHU | 13.44 | — | rebalance up |
| 2026-11-05T19:55 | Three white soldiers | sell | SPY | 16.81 | 0.01 | target is flat |
| 2026-11-05T19:50 | Three white soldiers | buy | ETHU | 3.39 | — | entry |
| 2026-11-05T19:50 | Three white soldiers | sell | SOXL | 3.39 | 0.01 | rebalance down |
| 2026-11-05T19:45 | Agent (ML meta-label) | buy | TQQQ | 1.04 | — | entry |
| 2026-11-05T19:45 | Agent (ML meta-label) | buy | SOXL | 4.70 | — | following Connors RSI(2) |
| 2026-11-05T19:45 | Agent (ML meta-label) | sell | SQQQ | 4.94 | -0.08 | selected signal exited |
| 2026-11-05T19:45 | Three white soldiers | buy | SPY | 16.80 | — | entry signal |
| 2026-11-05T19:45 | Three white soldiers | buy | SOXL | 16.80 | — | entry signal |
| 2026-11-05T19:45 | Three white soldiers | buy | IWM | 16.80 | — | entry signal |
| 2026-11-05T19:45 | Three white soldiers | buy | AMZN | 16.80 | — | entry signal |
| 2026-11-05T19:30 | Agent (ML meta-label) | buy | SQQQ | 5.03 | — | entry |
| 2026-11-05T19:30 | Agent (ML meta-label) | buy | AMD | 5.03 | — | entry |
| 2026-11-05T19:30 | VWAP momentum · 1h | buy | AMZN | 17.04 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 19:55:05.000130+00:00 -> 2026-11-05 20:05:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 19:55:05.000130+00:00 -> 2026-11-05 20:05:05.000130+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 19:55:05.000130+00:00 -> 2026-11-05 20:05:05.000130+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
