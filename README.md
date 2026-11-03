# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T03:50:05.000148+00:00 · 45720 ticks

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

Today: 2760 decisions in 552 calls, $0.0386 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T03:50 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-11-03T03:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T03:50 | 4 / 1 / 0 | ETH-USD 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| VWAP reversion | COIN | 1.90 | +3.41% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.16 | 9.16 | 0 | — | 9.79 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.53 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.12 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.32 | -1.68 | 103 | 45.6 | -13.20 | -3.64 | -13.45 | 143 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.12 | -1.88 | 0 | — | 1.41 | 0.63 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.63 | -3.37 | 0 | — | -1.85 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.49 | 1.76 | -2.66 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -4.95 | -3.04 | -8.93 | 159 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.22 | -5.78 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.75 | 1.25 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.71 | -6.29 | 0 | — | -2.94 | -1.09 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 90.98 | -9.02 | 101 | 21.8 | -16.63 | -6.16 | -17.67 | 80 |
| 21 | Hold BTC | benchmark | 90.69 | -9.31 | 0 | — | -1.21 | -0.02 | -12.65 | 1 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.35 | -12.20 | 209 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.01 | -17.21 | 578 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -7.24 | -2.35 | -13.40 | 87 |
| 25 | Donchian 55/20 · 1h | breakout | 89.44 | -10.56 | 60 | 13.3 | -13.71 | -3.07 | -18.06 | 99 |
| 26 | Parabolic SAR · 1h | trend | 88.79 | -11.21 | 149 | 26.8 | -16.02 | -3.77 | -17.40 | 241 |
| 27 | Daily: Bullish score | daily | 88.76 | -11.24 | 14 | 21.4 | -5.96 | -0.72 | -14.73 | 14 |
| 28 | Copy: Insider buying | copy | 88.67 | -11.33 | 35 | 37.1 | -22.53 | -4.57 | -23.69 | 62 |
| 29 | Max aggression: 5-day momentum | meta | 87.14 | -12.86 | 15 | 40.0 | -30.82 | -2.05 | -37.35 | 26 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.17 | -14.83 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.77 | -15.22 | 129 | 28.7 | -17.56 | -3.93 | -18.81 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.77 | -15.23 | 89 | 23.6 | -20.06 | -3.82 | -24.02 | 172 |
| 34 | Connors RSI(2) · 1h | reversion | 84.22 | -15.78 | 191 | 40.8 | -20.81 | -6.65 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.66 | -16.34 | 148 | 18.2 | -20.00 | -3.76 | -22.16 | 249 |
| 36 | Stochastic reversion · 1h | reversion | 83.07 | -16.93 | 232 | 46.6 | -25.67 | -5.39 | -25.90 | 390 |
| 37 | MFI reversion · 1h | reversion | 82.45 | -17.55 | 299 | 32.8 | -17.12 | -2.78 | -18.26 | 148 |
| 38 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.47 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 82.17 | -17.83 | 82 | 13.4 | -17.96 | -3.63 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -15.63 | -2.88 | -22.79 | 233 |
| 41 | EMA 20/50 cross · 1h | trend | 78.89 | -21.11 | 90 | 11.1 | -21.97 | -4.09 | -27.42 | 126 |
| 42 | CCI reversion · 1h | reversion | 78.42 | -21.58 | 263 | 44.9 | -27.78 | -4.44 | -28.51 | 445 |
| 43 | Supertrend · 1h | trend | 77.70 | -22.30 | 141 | 12.8 | -28.21 | -5.42 | -29.57 | 219 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.79 | -5.58 | -27.67 | 208 |
| 45 | Triple EMA stack · 1h | trend | 77.22 | -22.78 | 125 | 14.4 | -30.28 | -5.57 | -30.89 | 208 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -28.44 | -3.77 | -33.54 | 33 |
| 47 | MACD cross · 1h | trend | 76.96 | -23.04 | 299 | 23.4 | -33.20 | -6.59 | -35.11 | 468 |
| 48 | RSI momentum · 1h | momentum | 76.90 | -23.10 | 135 | 12.6 | -30.96 | -5.92 | -31.26 | 214 |
| 49 | Heikin-Ashi · 1h | trend | 76.51 | -23.49 | 356 | 22.5 | -40.63 | -8.71 | -43.18 | 659 |
| 50 | Bollinger reversion · 1h | reversion | 76.34 | -23.66 | 215 | 38.1 | -31.30 | -6.51 | -31.54 | 375 |
| 51 | Williams %R · 1h | reversion | 76.13 | -23.87 | 267 | 46.1 | -36.59 | -6.64 | -36.77 | 517 |
| 52 | OBV trend · 1h | momentum | 76.08 | -23.92 | 239 | 17.6 | -33.00 | -7.02 | -33.46 | 301 |
| 53 | Donchian 20/10 · 1h | breakout | 76.06 | -23.94 | 119 | 20.2 | -25.82 | -4.30 | -30.95 | 206 |
| 54 | Z-score reversion · 1h | reversion | 74.94 | -25.06 | 139 | 33.8 | -17.34 | -2.68 | -22.95 | 211 |
| 55 | ROC + volume · 1h | momentum | 74.89 | -25.11 | 299 | 25.4 | -29.94 | -5.22 | -34.50 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 70.87 | -29.13 | 128 | 25.8 | -21.51 | -3.87 | -26.26 | 193 |
| 57 | Three white soldiers | momentum | 70.00 | -30.00 | 408 | 16.2 | -45.66 | -21.26 | -45.66 | 610 |
| 58 | Candlestick reversal · 1h | reversion | 69.23 | -30.77 | 342 | 28.1 | -38.16 | -7.85 | -38.45 | 544 |
| 59 | EMA 9/21 cross · 1h | trend | 69.10 | -30.90 | 218 | 9.6 | -37.13 | -7.37 | -39.06 | 325 |
| 60 | Max aggression: 1-day momentum | meta | 68.78 | -31.22 | 23 | 30.4 | -35.26 | -2.08 | -50.32 | 42 |
| 61 | VWAP momentum · 1h | momentum | 68.60 | -31.40 | 696 | 21.6 | -53.17 | -10.76 | -55.28 | 1221 |
| 62 | Agent (ML meta-label) | meta | 68.40 | -31.60 | 1302 | 20.4 | -16.14 | -2.93 | -17.98 | 289 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.58 | -98.96 | 5174 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -24.13 | -79.94 | 1399 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.63 | -47.27 | -93.63 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.89 | -31.00 | -88.89 | 1896 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.39 | -38.30 | -91.39 | 2320 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.87 | -32.32 | -90.87 | 2236 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.00 | -97.77 | 3474 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -61.88 | -96.31 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.31 | -34.12 | -93.48 | 2404 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.99 | -34.58 | -81.99 | 1678 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.37 | -99.48 | 5877 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.07 | -43.75 | -93.07 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.56 | -36.69 | -95.57 | 3381 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -73.04 | -99.79 | 6173 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -43.99 | -91.85 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.62 | -26.12 | -74.67 | 1554 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -61.42 | -97.76 | 3540 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -61.05 | -98.70 | 4834 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.40 | -28.29 | -69.68 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -53.94 | -94.71 | 2761 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -37.14 | -84.75 | 1797 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.33 | -99.62 | 6312 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.43 | -30.58 | -88.45 | 2234 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.46 | -19.72 | -77.53 | 1706 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.39 | -36.53 | -90.40 | 2239 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.50 | -50.90 | -96.50 | 3823 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -52.76 | -89.41 | 2125 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.02 | -25.10 | -64.84 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.11 | -25.81 | -74.11 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.97 | -18.99 | -76.97 | 1605 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.85 | -49.53 | -96.85 | 4239 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.21 | -99.92 | 8225 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T03:30 | Three white soldiers | sell | BTC-USD | 17.40 | -0.14 | exit signal |
| 2026-11-03T03:20 | MFI reversion · 1h | sell | SOL-USD | 4.12 | -0.02 | rebalance down |
| 2026-11-03T03:20 | Three white soldiers | buy | BTC-USD | 17.53 | — | entry signal |
| 2026-11-03T03:00 | VWAP momentum · 1h | sell | ETH-USD | 17.13 | -0.15 | exit signal |
| 2026-11-03T03:00 | VWAP momentum · 1h | sell | BTC-USD | 17.08 | -0.19 | exit signal |
| 2026-11-03T02:00 | VWAP momentum · 1h | buy | ETH-USD | 3.45 | — | rebalance up |
| 2026-11-03T02:00 | VWAP momentum · 1h | buy | BTC-USD | 3.45 | — | rebalance up |
| 2026-11-03T02:00 | VWAP momentum · 1h | sell | SOL-USD | 9.94 | -0.07 | exit signal |
| 2026-11-03T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 13.72 | -0.10 | exit signal |
| 2026-11-03T01:45 | MFI reversion · 1h | buy | SOL-USD | 4.16 | — | rebalance up |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 03:50:05.000148+00:00 -> 2026-11-03 04:00:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
