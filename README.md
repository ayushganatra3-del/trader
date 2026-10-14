# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T20:25:05.000173+00:00 · 22819 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 21.14 · VIX 16.89 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 36256 decisions in 2915 calls, $0.4486 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T20:25 | 0 / 3 / 2 | TNA 15% |  |
| Breezy | 2026-10-14T20:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T20:25 | 2 / 2 / 1 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.79 | +4.30% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |
| Keltner breakout | LABU | 1.69 | +7.27% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.90 | 4.90 | 0 | — | 4.13 | 2.00 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.71 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.45 | -0.74 | -9.84 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | VWAP reversion · 1h | reversion | 101.65 | 1.65 | 45 | 40.0 | -8.65 | -2.60 | -13.79 | 123 |
| 6 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.98 | -7.55 | 43 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.92 | 0.92 | 0 | — | 4.04 | 1.60 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.67 | 0.67 | 20 | 45.0 | -16.02 | -2.56 | -21.97 | 76 |
| 9 | Hold SPY | benchmark | 100.54 | 0.54 | 0 | — | -0.98 | -0.54 | -3.44 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.19 | -0.81 | 0 | — | -1.10 | -0.43 | -3.75 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 98.98 | -1.02 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 98.76 | -1.24 | 0 | — | -4.93 | -2.76 | -5.36 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.28 | -3.82 | -3.91 | 21 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.02 | -2.07 | 67 |
| 17 | Hold BTC | benchmark | 98.30 | -1.70 | 0 | — | 28.77 | 3.36 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 97.13 | -2.87 | 36 | 16.7 | 5.91 | 0.87 | -22.11 | 114 |
| 19 | Trend pullback · 1h | trend | 96.99 | -3.01 | 86 | 24.4 | -24.08 | -6.94 | -24.83 | 168 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 22 | Agent (rotation) | meta | 96.52 | -3.48 | 91 | 30.8 | -13.38 | -4.78 | -14.99 | 278 |
| 23 | ADX DI cross · 1h | trend | 95.96 | -4.04 | 70 | 21.4 | -10.98 | -2.02 | -14.52 | 256 |
| 24 | Daily: Bullish score | daily | 95.22 | -4.78 | 5 | 0.0 | -2.89 | -0.18 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 95.14 | -4.86 | 13 | 38.5 | -9.94 | -0.19 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.92 | -5.08 | 0 | — | -15.33 | -2.94 | -16.54 | 1 |
| 27 | EMA 20/50 cross · 1h | trend | 94.31 | -5.69 | 48 | 16.7 | 5.17 | 0.78 | -24.13 | 136 |
| 28 | Parabolic SAR · 1h | trend | 93.91 | -6.09 | 93 | 22.6 | 0.36 | 0.24 | -23.41 | 288 |
| 29 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.54 | 2.41 | -6.78 | 199 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.07 | 1.10 | -9.46 | 102 |
| 31 | MACD cross · 1h | trend | 93.51 | -6.49 | 149 | 22.8 | -11.64 | -1.57 | -21.42 | 453 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 93.30 | -6.70 | 0 | — | 3.86 | 0.74 | -11.29 | 1 |
| 33 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -5.60 | -2.02 | -9.22 | 243 |
| 34 | Stochastic reversion · 1h | reversion | 92.78 | -7.22 | 114 | 49.1 | -17.14 | -3.23 | -17.93 | 362 |
| 35 | Max aggression: 5-day momentum | meta | 92.44 | -7.56 | 8 | 37.5 | -6.02 | -0.22 | -34.64 | 27 |
| 36 | Bollinger breakout · 1h | breakout | 91.93 | -8.07 | 78 | 29.5 | 7.55 | 1.13 | -14.21 | 277 |
| 37 | RSI momentum · 1h | momentum | 91.92 | -8.08 | 73 | 17.8 | 0.77 | 0.30 | -25.52 | 225 |
| 38 | Supertrend · 1h | trend | 91.89 | -8.11 | 73 | 13.7 | 0.67 | 0.28 | -23.21 | 210 |
| 39 | Z-score reversion · 1h | reversion | 91.52 | -8.47 | 60 | 38.3 | -7.09 | -1.29 | -12.17 | 162 |
| 40 | Volume breakout · 1h | breakout | 90.97 | -9.03 | 77 | 22.1 | 8.57 | 1.33 | -12.60 | 118 |
| 41 | MFI reversion · 1h | reversion | 90.59 | -9.41 | 177 | 29.9 | -15.81 | -2.78 | -17.12 | 135 |
| 42 | Ichimoku · 1h | trend | 90.53 | -9.47 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 43 | Triple EMA stack · 1h | trend | 90.35 | -9.64 | 77 | 16.9 | -11.18 | -1.01 | -34.69 | 237 |
| 44 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.36 | -2.69 | -10.72 | 122 |
| 45 | Connors RSI(2) · 1h | reversion | 89.82 | -10.18 | 137 | 40.1 | -23.04 | -6.92 | -24.82 | 253 |
| 46 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.02 | -17.60 | 556 |
| 47 | Agent (ML meta-label) | meta | 88.84 | -11.16 | 525 | 18.7 | -7.56 | -1.23 | -15.72 | 408 |
| 48 | OBV trend · 1h | momentum | 88.25 | -11.75 | 164 | 18.9 | -10.96 | -0.96 | -34.91 | 317 |
| 49 | Keltner breakout · 1h | breakout | 87.66 | -12.34 | 51 | 21.6 | -7.31 | -0.76 | -26.76 | 215 |
| 50 | MACD zero-line · 1h | trend | 87.37 | -12.63 | 74 | 16.2 | -23.43 | -4.57 | -23.92 | 228 |
| 51 | RSI(14) reversion · 1h | reversion | 87.34 | -12.66 | 48 | 27.1 | -3.41 | -0.44 | -13.96 | 154 |
| 52 | Donchian 20/10 · 1h | breakout | 86.76 | -13.24 | 71 | 19.7 | -1.06 | 0.07 | -20.38 | 217 |
| 53 | VWAP momentum · 1h | momentum | 85.97 | -14.03 | 347 | 21.9 | -37.10 | -5.62 | -42.74 | 1237 |
| 54 | ROC + volume · 1h | momentum | 85.74 | -14.26 | 179 | 21.2 | -11.93 | -1.64 | -25.34 | 396 |
| 55 | Heikin-Ashi · 1h | trend | 85.71 | -14.29 | 169 | 26.0 | -31.64 | -5.22 | -39.47 | 665 |
| 56 | Bollinger reversion · 1h | reversion | 85.65 | -14.35 | 105 | 34.3 | -25.52 | -5.41 | -28.60 | 329 |
| 57 | EMA 9/21 cross · 1h | trend | 85.16 | -14.84 | 120 | 12.5 | -10.99 | -1.29 | -26.93 | 329 |
| 58 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.21 | -4.95 | -21.40 | 692 |
| 59 | CCI reversion · 1h | reversion | 84.75 | -15.26 | 130 | 42.3 | -14.99 | -1.97 | -19.36 | 411 |
| 60 | Williams %R · 1h | reversion | 84.71 | -15.29 | 154 | 43.5 | -31.63 | -5.27 | -32.32 | 507 |
| 61 | Three white soldiers | momentum | 84.20 | -15.79 | 183 | 16.4 | -48.80 | -22.47 | -48.80 | 593 |
| 62 | Candlestick reversal · 1h | reversion | 82.47 | -17.54 | 157 | 28.0 | -30.78 | -5.71 | -31.14 | 509 |
| 63 | ROC + volume | momentum | 67.43 | -32.57 | 483 | 21.5 | -74.00 | -16.45 | -76.13 | 1655 |
| 64 | Volume breakout | breakout | 65.88 | -34.12 | 307 | 13.7 | -63.37 | -17.84 | -63.38 | 886 |
| 65 | Squeeze breakout | breakout | 65.54 | -34.47 | 395 | 14.9 | -63.13 | -18.18 | -63.21 | 1211 |
| 66 | RSI(14) reversion | reversion | 65.26 | -34.73 | 541 | 26.2 | -74.35 | -17.27 | -74.46 | 1555 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -69.06 | -14.53 | -70.95 | 1271 |
| 68 | EMA 20/50 cross | trend | 63.07 | -36.93 | 408 | 19.4 | -77.27 | -15.18 | -77.77 | 1430 |
| 69 | VWAP reversion | reversion | 59.75 | -40.25 | 557 | 23.7 | -73.26 | -15.33 | -73.35 | 1452 |
| 70 | AI bee: Boozy | ai | 57.65 | -42.35 | 272 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.42 | -43.58 | 550 | 14.2 | -83.36 | -26.93 | -83.43 | 1828 |
| 72 | Supertrend ⏸ | trend | 56.10 | -43.90 | 568 | 19.0 | -86.28 | -20.25 | -86.30 | 1891 |
| 73 | Ichimoku | trend | 54.40 | -45.60 | 485 | 9.9 | -81.75 | -22.40 | -81.88 | 1699 |
| 74 | AI bee: Bizzy | ai | 52.13 | -47.87 | 985 | 8.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 51.08 | -48.92 | 740 | 20.0 | -87.84 | -27.38 | -87.88 | 2124 |
| 76 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.55 | -29.21 | -98.55 | 5267 |
| 77 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -29.66 | -93.44 | 2568 |
| 78 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -24.60 | -90.55 | 2339 |
| 79 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.72 | -26.80 | -91.75 | 2344 |
| 80 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.20 | -97.41 | 3503 |
| 81 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -35.18 | -96.50 | 3531 |
| 82 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -24.87 | -94.45 | 2624 |
| 83 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.73 | -99.40 | 5744 |
| 84 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.14 | -25.52 | -91.16 | 2615 |
| 85 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -31.17 | -96.36 | 3574 |
| 86 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.63 | -99.73 | 6153 |
| 87 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -29.29 | -91.77 | 2344 |
| 88 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.40 | -37.10 | -97.40 | 3637 |
| 89 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.70 | -98.53 | 4686 |
| 90 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.51 | -32.62 | -93.52 | 2779 |
| 91 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.72 | -99.55 | 6152 |
| 92 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.25 | -22.16 | -86.28 | 2103 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -32.05 | -96.03 | 3762 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -33.79 | -89.48 | 2097 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -33.34 | -95.78 | 4078 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.12 | -99.89 | 8199 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T20:14 | AI bee: Bizzy | sell | SOL-USD | 7.32 | -0.05 | Jev: sell (sell p=0.81) after 10 min |
| 2026-10-14T20:04 | AI bee: Bizzy | buy | SOL-USD | 7.37 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T20:00 | MFI reversion · 1h | buy | ETH-USD | 12.94 | — | entry signal |
| 2026-10-14T20:00 | MFI reversion · 1h | buy | DOGE-USD | 12.94 | — | entry signal |
| 2026-10-14T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.11 | 1.70 | target is flat |
| 2026-10-14T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 102.77 | 2.24 | target is flat |
| 2026-10-14T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 98.73 | -0.08 | target is flat |
| 2026-10-14T19:55 | MFI reversion · 1h | sell | SPY | 22.67 | -0.01 | target is flat |
| 2026-10-14T19:55 | MFI reversion · 1h | sell | AMD | 22.60 | -0.04 | target is flat |
| 2026-10-14T19:55 | MFI reversion | buy | XRP-USD | 6.27 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | SOL-USD | 6.29 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | ETH-USD | 6.28 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | DOGE-USD | 8.22 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | BTC-USD | 7.21 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | sell | UPRO | 3.42 | 0.01 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | TSLA | 3.41 | 0.00 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | TNA | 3.66 | 0.02 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | QQQ | 1.15 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | MSFT | 3.94 | -0.01 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | META | 1.65 | 0.00 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | ETHU | 3.67 | 0.02 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | COIN | 3.01 | -0.01 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | AMZN | 3.01 | -0.01 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | AMD | 3.93 | -0.02 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | buy | XRP-USD | 10.38 | — | rebalance up |
| 2026-10-14T19:55 | VWAP reversion | buy | SOL-USD | 7.63 | — | rebalance up |
| 2026-10-14T19:55 | VWAP reversion | buy | ETH-USD | 7.64 | — | rebalance up |
| 2026-10-14T19:55 | VWAP reversion | buy | DOGE-USD | 7.64 | — | rebalance up |
| 2026-10-14T19:55 | VWAP reversion | buy | BTC-USD | 7.64 | — | rebalance up |
| 2026-10-14T19:55 | VWAP reversion | sell | TSLA | 2.99 | 0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | TQQQ | 3.00 | 0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | SPY | 1.07 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | SOXL | 2.87 | 0.01 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | QQQ | 2.49 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | MSFT | 2.84 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | META | 2.74 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | IWM | 2.84 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | GOOGL | 1.14 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | ETHU | 4.30 | 0.03 | end-of-day flatten |
| 2026-10-14T19:55 | VWAP reversion | sell | COIN | 3.14 | -0.03 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 20:25:05.000173+00:00 -> 2026-10-14 20:35:05.000173+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
