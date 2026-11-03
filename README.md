# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T01:20:05.000161+00:00 · 45605 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.57 (-9.43%)

Closed trades 139, win rate 39.6%, fees £3.92, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 1035 decisions in 207 calls, $0.0144 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T01:20 | 4 / 0 / 1 | cash |  |
| Breezy | 2026-11-03T01:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T01:20 | 3 / 2 / 0 | ETH-USD 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| MACD zero-line | MSFT | 1.87 | +0.67% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.05 | 9.05 | 0 | — | 9.68 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.53 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.12 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.31 | -1.69 | 103 | 45.6 | -13.55 | -3.72 | -13.81 | 142 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.11 | -1.89 | 0 | — | 1.42 | 0.64 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.62 | -3.38 | 0 | — | -1.84 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.25 | 1.64 | -2.89 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -4.85 | -2.98 | -8.91 | 157 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.21 | -5.79 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.83 | 1.27 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.29 | 0 | — | -2.94 | -1.09 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Hold BTC | benchmark | 91.10 | -8.90 | 0 | — | -0.36 | 0.11 | -12.65 | 1 |
| 21 | Trend pullback · 1h | trend | 90.98 | -9.02 | 101 | 21.8 | -16.63 | -6.16 | -17.67 | 80 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.35 | -12.20 | 209 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.01 | -17.21 | 578 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.05 | -1.76 | -13.40 | 90 |
| 25 | Donchian 55/20 · 1h | breakout | 89.43 | -10.56 | 60 | 13.3 | -13.71 | -3.07 | -18.06 | 99 |
| 26 | Parabolic SAR · 1h | trend | 88.79 | -11.21 | 149 | 26.8 | -16.02 | -3.77 | -17.40 | 241 |
| 27 | Daily: Bullish score | daily | 88.76 | -11.24 | 14 | 21.4 | -5.96 | -0.72 | -14.73 | 14 |
| 28 | Copy: Insider buying | copy | 88.57 | -11.43 | 35 | 37.1 | -22.66 | -4.59 | -23.82 | 62 |
| 29 | Max aggression: 5-day momentum | meta | 87.13 | -12.87 | 15 | 40.0 | -30.82 | -2.05 | -37.35 | 26 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.16 | -14.84 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.77 | -15.22 | 129 | 28.7 | -17.56 | -3.93 | -18.81 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.77 | -15.23 | 89 | 23.6 | -21.55 | -4.26 | -24.09 | 172 |
| 34 | Connors RSI(2) · 1h | reversion | 84.21 | -15.79 | 191 | 40.8 | -20.81 | -6.65 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.66 | -16.34 | 148 | 18.2 | -20.00 | -3.76 | -22.16 | 249 |
| 36 | Stochastic reversion · 1h | reversion | 83.12 | -16.88 | 232 | 46.6 | -25.64 | -5.38 | -25.91 | 390 |
| 37 | MFI reversion · 1h | reversion | 82.67 | -17.33 | 299 | 32.8 | -17.27 | -2.81 | -18.26 | 148 |
| 38 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.47 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 82.17 | -17.83 | 82 | 13.4 | -17.96 | -3.63 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -15.70 | -2.90 | -22.79 | 233 |
| 41 | EMA 20/50 cross · 1h | trend | 78.89 | -21.11 | 90 | 11.1 | -22.12 | -4.15 | -27.42 | 124 |
| 42 | CCI reversion · 1h | reversion | 78.54 | -21.46 | 263 | 44.9 | -27.58 | -4.40 | -28.51 | 445 |
| 43 | Supertrend · 1h | trend | 77.69 | -22.30 | 141 | 12.8 | -28.21 | -5.42 | -29.57 | 219 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.79 | -5.58 | -27.67 | 208 |
| 45 | Triple EMA stack · 1h | trend | 77.22 | -22.78 | 125 | 14.4 | -30.01 | -5.53 | -30.89 | 208 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -28.44 | -3.77 | -33.54 | 33 |
| 47 | MACD cross · 1h | trend | 76.96 | -23.04 | 299 | 23.4 | -33.01 | -6.53 | -35.08 | 469 |
| 48 | RSI momentum · 1h | momentum | 76.90 | -23.10 | 135 | 12.6 | -30.28 | -5.81 | -30.86 | 213 |
| 49 | Heikin-Ashi · 1h | trend | 76.51 | -23.49 | 356 | 22.5 | -40.63 | -8.71 | -43.18 | 659 |
| 50 | Bollinger reversion · 1h | reversion | 76.44 | -23.55 | 215 | 38.1 | -31.20 | -6.48 | -31.50 | 375 |
| 51 | Williams %R · 1h | reversion | 76.27 | -23.73 | 267 | 46.1 | -36.43 | -6.60 | -36.77 | 517 |
| 52 | OBV trend · 1h | momentum | 76.08 | -23.93 | 239 | 17.6 | -32.89 | -7.00 | -33.53 | 301 |
| 53 | Donchian 20/10 · 1h | breakout | 76.06 | -23.94 | 119 | 20.2 | -25.95 | -4.35 | -30.95 | 206 |
| 54 | Z-score reversion · 1h | reversion | 74.98 | -25.02 | 139 | 33.8 | -17.20 | -2.65 | -22.92 | 211 |
| 55 | ROC + volume · 1h | momentum | 74.88 | -25.12 | 299 | 25.4 | -29.94 | -5.22 | -34.50 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 70.86 | -29.14 | 128 | 25.8 | -21.36 | -3.84 | -26.27 | 193 |
| 57 | Three white soldiers | momentum | 70.13 | -29.86 | 407 | 16.2 | -45.56 | -21.09 | -45.69 | 610 |
| 58 | Candlestick reversal · 1h | reversion | 69.37 | -30.63 | 342 | 28.1 | -38.06 | -7.82 | -38.47 | 543 |
| 59 | EMA 9/21 cross · 1h | trend | 69.10 | -30.90 | 218 | 9.6 | -37.22 | -7.49 | -39.06 | 324 |
| 60 | VWAP momentum · 1h | momentum | 69.06 | -30.95 | 692 | 21.7 | -53.10 | -10.75 | -54.96 | 1222 |
| 61 | Max aggression: 1-day momentum | meta | 68.78 | -31.22 | 23 | 30.4 | -35.26 | -2.08 | -50.32 | 42 |
| 62 | Agent (ML meta-label) | meta | 68.40 | -31.60 | 1302 | 20.4 | -13.84 | -2.35 | -16.54 | 308 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -43.49 | -98.93 | 5161 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.61 | -23.79 | -79.85 | 1399 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.66 | -45.36 | -93.66 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.79 | -30.52 | -88.88 | 1896 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.35 | -37.43 | -91.42 | 2322 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.90 | -32.43 | -90.90 | 2239 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -51.45 | -97.75 | 3471 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -58.66 | -96.35 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.22 | -33.88 | -93.41 | 2398 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.07 | -33.82 | -82.12 | 1684 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -52.45 | -99.48 | 5869 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.05 | -42.70 | -93.07 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.59 | -36.91 | -95.59 | 3385 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -70.56 | -99.79 | 6170 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -43.49 | -91.84 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.78 | -25.92 | -74.85 | 1562 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -59.94 | -97.74 | 3539 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -58.98 | -98.68 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.38 | -28.11 | -69.64 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -52.89 | -94.73 | 2765 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.80 | -36.99 | -84.83 | 1799 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -67.13 | -99.62 | 6305 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.37 | -30.33 | -88.39 | 2228 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.23 | -19.64 | -77.31 | 1700 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.36 | -36.05 | -90.36 | 2236 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.46 | -49.67 | -96.47 | 3813 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.47 | -52.75 | -89.47 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.06 | -25.12 | -64.83 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.94 | -25.47 | -74.07 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.66 | -18.64 | -76.95 | 1603 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.83 | -49.02 | -96.84 | 4238 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.02 | -99.92 | 8225 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T01:20 | MFI reversion · 1h | sell | SOL-USD | 4.14 | -0.01 | rebalance down |
| 2026-11-03T01:00 | VWAP reversion · 1h | sell | SOL-USD | 24.61 | -0.07 | exit signal |
| 2026-11-03T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 24.56 | 0.04 | exit signal |
| 2026-11-03T01:00 | VWAP reversion · 1h | sell | BTC-USD | 24.53 | -0.13 | exit signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | SOL-USD | 10.01 | — | entry signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | ETH-USD | 13.82 | — | entry signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 13.82 | — | entry signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | BTC-USD | 13.82 | — | entry signal |
| 2026-11-03T00:00 | CCI reversion · 1h | buy | ETH-USD | 12.97 | — | entry signal |
| 2026-11-03T00:00 | CCI reversion · 1h | sell | XRP-USD | 6.58 | -0.04 | rebalance down |
| 2026-11-03T00:00 | CCI reversion · 1h | sell | DOGE-USD | 6.39 | -0.04 | rebalance down |
| 2026-11-02T23:00 | CCI reversion · 1h | buy | DOGE-USD | 19.54 | — | entry signal |
| 2026-11-02T23:00 | VWAP momentum · 1h | sell | XRP-USD | 17.17 | -0.13 | exit signal |
| 2026-11-02T22:00 | MFI reversion · 1h | buy | SOL-USD | 20.67 | — | entry signal |
| 2026-11-02T22:00 | MFI reversion · 1h | buy | DOGE-USD | 20.67 | — | entry signal |
| 2026-11-02T22:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.77 | — | entry signal |
| 2026-11-02T22:00 | Z-score reversion · 1h | sell | XRP-USD | 8.77 | -0.05 | exit signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | buy | SOL-USD | 5.46 | — | entry signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | buy | ETH-USD | 5.46 | — | entry signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | sell | XRP-USD | 6.38 | -0.03 | exit signal |
| 2026-11-02T22:00 | VWAP momentum · 1h | buy | XRP-USD | 17.31 | — | entry signal |
| 2026-11-02T21:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.52 | — | entry signal |
| 2026-11-02T21:00 | Bollinger reversion · 1h | buy | DOGE-USD | 5.87 | — | entry signal |
| 2026-11-02T21:00 | VWAP momentum · 1h | sell | XRP-USD | 17.09 | -0.18 | exit signal |
| 2026-11-02T20:55 | Agent (rotation) | sell | SQQQ | 63.46 | 0.85 | selected signal exited |
| 2026-11-02T20:55 | Day trade: Stocks in Play ORB | sell | AMZN | 24.03 | -0.38 | target is flat |
| 2026-11-02T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.14 | 0.79 | target is flat |
| 2026-11-02T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 106.61 | 2.02 | target is flat |
| 2026-11-02T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 96.26 | 0.74 | target is flat |
| 2026-11-02T20:55 | Agent | sell | MSTR | 18.08 | -0.05 | selected signal exited |
| 2026-11-02T20:55 | Keltner breakout · 1h | sell | AMZN | 20.53 | -0.58 | stop-loss |
| 2026-11-02T20:55 | Opening range 30m | sell | SQQQ | 23.23 | 1.02 | end-of-day flatten |
| 2026-11-02T20:55 | Opening range 15m | sell | SQQQ | 17.11 | 0.75 | end-of-day flatten |
| 2026-11-02T20:52 | Candlestick reversal · 1h | buy | SOXL | 7.69 | — | entry |
| 2026-11-02T20:52 | Candlestick reversal · 1h | sell | ETHU | 6.91 | -0.01 | target is flat |
| 2026-11-02T20:35 | Agent (aggressive) | sell | AMZN | 43.15 | -0.32 | selected signal exited |
| 2026-11-02T20:35 | Agent | sell | AMZN | 18.00 | -0.13 | selected signal exited |
| 2026-11-02T20:35 | Three white soldiers | sell | DOGE-USD | 17.43 | -0.13 | exit signal |
| 2026-11-02T20:30 | Agent (rotation) | buy | SQQQ | 31.25 | — | rebalance up |
| 2026-11-02T20:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 102.35 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 01:20:05.000161+00:00 -> 2026-11-03 01:30:05.000161+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
