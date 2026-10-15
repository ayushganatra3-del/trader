# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T19:55:05.000132+00:00 · 23952 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.85 (-7.14%)

Closed trades 76, win rate 39.5%, fees £2.65, max drawdown -7.57%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 36372 decisions in 2886 calls, $0.4486 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T19:55 | 0 / 17 / 13 | cash |  |
| Breezy | 2026-10-15T19:55 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-15T19:55 | 2 / 27 / 1 | COIN 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| VWAP reversion | PLTR | 1.50 | +3.07% | 7 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.16 | 5.16 | 1 | 100.0 | 5.91 | 1.48 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.03 | 4.03 | 0 | — | 4.65 | 2.25 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.72 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.04 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.15 | 0.15 | 0 | — | -0.50 | -0.25 | -3.24 | 1 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.12 | 0.12 | 0 | — | 3.70 | 1.46 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Copy: Insider buying | copy | 99.95 | -0.05 | 20 | 45.0 | -16.07 | -2.55 | -21.97 | 76 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 11 | VWAP reversion · 1h | reversion | 99.87 | -0.13 | 58 | 39.7 | -10.89 | -3.13 | -13.79 | 128 |
| 12 | Copy: Congress Democrats (NANC) | copy | 98.84 | -1.16 | 0 | — | -0.59 | -0.20 | -4.45 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 14 | Hold BTC | benchmark | 98.19 | -1.81 | 0 | — | 30.65 | 3.52 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.89 | -2.11 | 0 | — | -5.13 | -2.85 | -6.38 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.02 | -2.98 | 0 | — | -5.50 | -2.16 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 97.01 | -2.99 | 36 | 16.7 | 6.47 | 0.92 | -22.11 | 112 |
| 19 | Trend pullback · 1h | trend | 96.75 | -3.25 | 86 | 24.4 | -21.40 | -6.00 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.37 | -3.63 | 11 | 0.0 | -4.03 | -3.07 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.10 | -3.90 | 106 | 32.1 | -15.75 | -5.45 | -17.36 | 298 |
| 22 | ADX DI cross · 1h | trend | 95.87 | -4.13 | 70 | 21.4 | -10.77 | -1.96 | -15.34 | 254 |
| 23 | Daily: Momentum burst | daily | 95.60 | -4.40 | 5 | 20.0 | -4.67 | -0.56 | -17.75 | 39 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 94.18 | -5.82 | 0 | — | 4.73 | 0.86 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.71 | 1.04 | -9.46 | 102 |
| 26 | Parabolic SAR · 1h | trend | 93.67 | -6.33 | 93 | 22.6 | 3.07 | 0.57 | -22.05 | 281 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.37 | 2.35 | -6.78 | 200 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.35 | -6.65 | 0 | — | -15.83 | -3.01 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.29 | -6.71 | 7 | 0.0 | -4.25 | -0.35 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.17 | -6.83 | 51 | 15.7 | 4.43 | 0.68 | -24.47 | 134 |
| 31 | MACD cross · 1h | trend | 92.97 | -7.03 | 154 | 22.1 | -13.17 | -1.77 | -26.23 | 460 |
| 32 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.31 | -6.08 | -10.86 | 245 |
| 33 | Bollinger breakout · 1h | breakout | 92.19 | -7.81 | 79 | 30.4 | 6.71 | 1.04 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 91.99 | -8.01 | 8 | 37.5 | -7.58 | -0.38 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.87 | -3.25 | -17.60 | 568 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -2.60 | -0.23 | -14.55 | 117 |
| 37 | Supertrend · 1h | trend | 91.62 | -8.38 | 74 | 13.5 | -1.58 | 0.03 | -28.77 | 213 |
| 38 | RSI momentum · 1h | momentum | 91.51 | -8.49 | 73 | 17.8 | 0.10 | 0.23 | -26.34 | 224 |
| 39 | Stochastic reversion · 1h | reversion | 91.31 | -8.69 | 128 | 44.5 | -15.78 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -5.95 | -2.18 | -7.37 | 120 |
| 42 | Triple EMA stack · 1h | trend | 90.17 | -9.83 | 77 | 16.9 | -7.23 | -0.55 | -32.05 | 234 |
| 43 | MFI reversion · 1h | reversion | 90.07 | -9.93 | 191 | 30.4 | -17.49 | -3.02 | -20.77 | 145 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.93 | -25.00 | 244 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -18.79 | -0.73 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.52 | -11.48 | 73 | 35.6 | -10.22 | -1.85 | -17.27 | 183 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -13.76 | -1.86 | -29.15 | 209 |
| 48 | OBV trend · 1h | momentum | 87.88 | -12.12 | 165 | 18.8 | -10.86 | -0.93 | -34.81 | 316 |
| 49 | Agent (ML meta-label) | meta | 87.35 | -12.65 | 568 | 18.5 | -4.70 | -0.59 | -16.15 | 415 |
| 50 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.94 | -4.36 | -21.40 | 706 |
| 51 | MACD zero-line · 1h | trend | 87.20 | -12.80 | 74 | 16.2 | -21.91 | -4.25 | -22.42 | 226 |
| 52 | VWAP momentum · 1h | momentum | 86.60 | -13.40 | 354 | 21.8 | -34.40 | -4.99 | -43.06 | 1256 |
| 53 | Heikin-Ashi · 1h | trend | 86.47 | -13.53 | 170 | 26.5 | -29.79 | -4.78 | -39.17 | 672 |
| 54 | ROC + volume · 1h | momentum | 86.32 | -13.69 | 180 | 21.7 | -8.44 | -1.01 | -25.31 | 399 |
| 55 | Donchian 20/10 · 1h | breakout | 86.06 | -13.94 | 72 | 19.4 | 0.00 | 0.20 | -20.56 | 219 |
| 56 | Three white soldiers | momentum | 85.86 | -14.14 | 200 | 19.5 | -47.54 | -19.02 | -48.85 | 607 |
| 57 | Bollinger reversion · 1h | reversion | 85.17 | -14.83 | 132 | 31.8 | -26.80 | -5.78 | -31.47 | 340 |
| 58 | EMA 9/21 cross · 1h | trend | 84.85 | -15.15 | 120 | 12.5 | -5.37 | -0.41 | -29.09 | 321 |
| 59 | Williams %R · 1h | reversion | 84.12 | -15.88 | 168 | 42.9 | -31.26 | -5.11 | -34.85 | 528 |
| 60 | CCI reversion · 1h | reversion | 83.45 | -16.55 | 142 | 42.3 | -15.19 | -1.95 | -23.38 | 429 |
| 61 | RSI(14) reversion · 1h | reversion | 83.42 | -16.57 | 61 | 23.0 | -12.32 | -2.31 | -18.95 | 171 |
| 62 | Candlestick reversal · 1h | reversion | 80.43 | -19.57 | 183 | 25.7 | -32.20 | -6.04 | -33.79 | 524 |
| 63 | RSI(14) reversion | reversion | 66.62 | -33.38 | 572 | 28.7 | -73.41 | -16.30 | -74.29 | 1557 |
| 64 | ROC + volume | momentum | 66.30 | -33.70 | 524 | 22.7 | -74.72 | -16.94 | -76.52 | 1701 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.43 | -17.89 | -63.43 | 891 |
| 66 | Squeeze breakout | breakout | 64.56 | -35.44 | 419 | 15.0 | -62.80 | -17.49 | -63.44 | 1216 |
| 67 | Donchian 55/20 | breakout | 63.55 | -36.45 | 416 | 18.3 | -68.81 | -14.10 | -71.15 | 1282 |
| 68 | EMA 20/50 cross | trend | 62.13 | -37.87 | 431 | 19.7 | -76.95 | -14.81 | -78.49 | 1446 |
| 69 | AI bee: Boozy | ai | 58.98 | -41.02 | 278 | 5.4 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.50 | -14.97 | -72.55 | 1430 |
| 71 | Keltner breakout | breakout | 56.43 | -43.57 | 589 | 16.5 | -83.56 | -25.84 | -83.78 | 1852 |
| 72 | Supertrend | trend | 54.80 | -45.20 | 607 | 20.4 | -86.24 | -19.82 | -86.56 | 1915 |
| 73 | Ichimoku | trend | 53.67 | -46.33 | 526 | 12.0 | -81.87 | -22.23 | -82.04 | 1727 |
| 74 | AI bee: Bizzy | ai | 51.46 | -48.54 | 1033 | 9.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.57 | -28.67 | -98.61 | 5293 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.35 | -28.43 | -93.47 | 2586 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -23.79 | -90.73 | 2365 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.49 | -25.99 | -91.54 | 2323 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -31.10 | -97.45 | 3518 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -33.98 | -96.58 | 3581 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -24.16 | -94.40 | 2634 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -34.79 | -99.40 | 5717 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.19 | -24.93 | -91.27 | 2644 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -30.24 | -96.18 | 3543 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -38.68 | -99.73 | 6158 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -28.38 | -91.83 | 2368 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.44 | -36.04 | -97.45 | 3653 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -34.97 | -98.51 | 4679 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.55 | -31.36 | -93.58 | 2800 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.39 | -99.55 | 6166 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.05 | -21.71 | -86.36 | 2103 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.41 | -26.16 | -87.78 | 2101 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.96 | -31.44 | -96.06 | 3759 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -32.30 | -89.45 | 2105 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -32.39 | -95.83 | 4072 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.30 | -99.89 | 8224 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T19:55 | Agent (rotation) | sell | TQQQ | 32.20 | 0.24 | selected signal exited |
| 2026-10-15T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 103.54 | 0.77 | target is flat |
| 2026-10-15T19:55 | MFI reversion · 1h | buy | PLTR | 1.99 | — | entry |
| 2026-10-15T19:55 | VWAP reversion | sell | SQQQ | 14.47 | -0.05 | end-of-day flatten |
| 2026-10-15T19:55 | VWAP reversion | sell | AAPL | 14.59 | 0.02 | end-of-day flatten |
| 2026-10-15T19:55 | RSI(14) reversion | sell | SQQQ | 16.62 | -0.06 | end-of-day flatten |
| 2026-10-15T19:55 | RSI(14) reversion | sell | AAPL | 16.66 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TQQQ | 21.53 | 0.13 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TNA | 21.54 | 0.12 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TECL | 21.37 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | QQQ | 21.42 | 0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Volume breakout | sell | TNA | 16.19 | -0.02 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | TSLA | 16.18 | 0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | PLTR | 16.12 | -0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | AMD | 13.13 | 0.21 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | buy | ETH-USD | 14.13 | — | entry |
| 2026-10-15T19:55 | Keltner breakout | sell | UPRO | 5.10 | 0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | TQQQ | 5.13 | 0.04 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | TNA | 5.15 | 0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | TECL | 5.16 | 0.06 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | SPY | 5.10 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | SOXL | 5.22 | 0.12 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | QQQ | 5.11 | 0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | IWM | 5.11 | 0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | COIN | 5.17 | 0.06 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | AMZN | 5.10 | -0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | AMD | 5.12 | 0.03 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | UPRO | 5.35 | 0.04 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | TSLA | 5.33 | 0.02 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | TQQQ | 5.40 | 0.09 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | TNA | 5.35 | 0.13 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | TECL | 5.43 | 0.12 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | SPY | 1.64 | 0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | SOXL | 5.53 | 0.22 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | QQQ | 5.33 | 0.02 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | NVDA | 8.14 | 0.04 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | MSTR | 5.52 | 0.37 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | META | 1.61 | 0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | LABU | 5.33 | 0.02 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | IWM | 5.32 | 0.04 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 19:55:05.000132+00:00 -> 2026-10-15 20:05:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
