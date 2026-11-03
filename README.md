# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T02:20:05.000121+00:00 · 45648 ticks

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

Today: 1680 decisions in 336 calls, $0.0235 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T02:20 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-03T02:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T02:20 | 0 / 5 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.01 | 9.01 | 0 | — | 9.68 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.53 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.12 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.31 | -1.69 | 103 | 45.6 | -13.55 | -3.72 | -13.81 | 142 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.08 | -1.92 | 0 | — | 1.42 | 0.64 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.59 | -3.41 | 0 | — | -1.84 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.25 | 1.64 | -2.89 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -4.91 | -3.01 | -8.90 | 159 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.18 | -5.82 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.87 | 1.29 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.68 | -6.32 | 0 | — | -2.94 | -1.09 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 90.97 | -9.03 | 101 | 21.8 | -16.63 | -6.16 | -17.67 | 80 |
| 21 | Hold BTC | benchmark | 90.69 | -9.31 | 0 | — | -1.16 | -0.02 | -12.65 | 1 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.35 | -12.20 | 209 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.01 | -17.21 | 578 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.73 | -2.09 | -13.40 | 88 |
| 25 | Donchian 55/20 · 1h | breakout | 89.42 | -10.58 | 60 | 13.3 | -13.71 | -3.07 | -18.06 | 99 |
| 26 | Parabolic SAR · 1h | trend | 88.77 | -11.23 | 149 | 26.8 | -16.02 | -3.77 | -17.40 | 241 |
| 27 | Daily: Bullish score | daily | 88.76 | -11.24 | 14 | 21.4 | -5.96 | -0.72 | -14.73 | 14 |
| 28 | Copy: Insider buying | copy | 88.64 | -11.36 | 35 | 37.1 | -22.53 | -4.57 | -23.69 | 62 |
| 29 | Max aggression: 5-day momentum | meta | 87.10 | -12.89 | 15 | 40.0 | -30.82 | -2.05 | -37.35 | 26 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.13 | -14.87 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.77 | -15.22 | 129 | 28.7 | -17.56 | -3.93 | -18.81 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.76 | -15.24 | 89 | 23.6 | -20.47 | -3.94 | -24.08 | 172 |
| 34 | Connors RSI(2) · 1h | reversion | 84.21 | -15.79 | 191 | 40.8 | -20.81 | -6.65 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.65 | -16.35 | 148 | 18.2 | -20.00 | -3.76 | -22.16 | 249 |
| 36 | Stochastic reversion · 1h | reversion | 83.04 | -16.96 | 232 | 46.6 | -25.67 | -5.39 | -25.89 | 390 |
| 37 | MFI reversion · 1h | reversion | 82.40 | -17.60 | 299 | 32.8 | -17.19 | -2.79 | -18.26 | 147 |
| 38 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.47 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 82.16 | -17.84 | 82 | 13.4 | -17.96 | -3.63 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -15.69 | -2.90 | -22.79 | 233 |
| 41 | EMA 20/50 cross · 1h | trend | 78.88 | -21.12 | 90 | 11.1 | -21.89 | -4.09 | -27.42 | 125 |
| 42 | CCI reversion · 1h | reversion | 78.36 | -21.64 | 263 | 44.9 | -27.81 | -4.45 | -28.51 | 445 |
| 43 | Supertrend · 1h | trend | 77.68 | -22.32 | 141 | 12.8 | -28.21 | -5.42 | -29.57 | 219 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.79 | -5.58 | -27.67 | 208 |
| 45 | Triple EMA stack · 1h | trend | 77.21 | -22.79 | 125 | 14.4 | -30.41 | -5.59 | -30.89 | 208 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -28.44 | -3.77 | -33.54 | 33 |
| 47 | MACD cross · 1h | trend | 76.93 | -23.07 | 299 | 23.4 | -33.04 | -6.54 | -35.09 | 469 |
| 48 | RSI momentum · 1h | momentum | 76.88 | -23.12 | 135 | 12.6 | -30.36 | -5.83 | -30.86 | 213 |
| 49 | Heikin-Ashi · 1h | trend | 76.50 | -23.50 | 356 | 22.5 | -40.63 | -8.71 | -43.18 | 659 |
| 50 | Bollinger reversion · 1h | reversion | 76.31 | -23.69 | 215 | 38.1 | -31.30 | -6.51 | -31.50 | 375 |
| 51 | Williams %R · 1h | reversion | 76.09 | -23.91 | 267 | 46.1 | -36.59 | -6.65 | -36.77 | 517 |
| 52 | OBV trend · 1h | momentum | 76.06 | -23.94 | 239 | 17.6 | -32.85 | -6.99 | -33.49 | 301 |
| 53 | Donchian 20/10 · 1h | breakout | 76.05 | -23.95 | 119 | 20.2 | -25.95 | -4.35 | -30.95 | 206 |
| 54 | Z-score reversion · 1h | reversion | 74.91 | -25.09 | 139 | 33.8 | -17.35 | -2.68 | -22.92 | 211 |
| 55 | ROC + volume · 1h | momentum | 74.86 | -25.14 | 299 | 25.4 | -29.94 | -5.22 | -34.50 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 70.84 | -29.16 | 128 | 25.8 | -21.52 | -3.88 | -26.27 | 193 |
| 57 | Three white soldiers | momentum | 70.13 | -29.86 | 407 | 16.2 | -45.55 | -21.08 | -45.60 | 609 |
| 58 | Candlestick reversal · 1h | reversion | 69.18 | -30.82 | 342 | 28.1 | -38.20 | -7.86 | -38.47 | 543 |
| 59 | EMA 9/21 cross · 1h | trend | 69.08 | -30.92 | 218 | 9.6 | -37.03 | -7.33 | -39.06 | 325 |
| 60 | Max aggression: 1-day momentum | meta | 68.78 | -31.22 | 23 | 30.4 | -35.26 | -2.08 | -50.32 | 42 |
| 61 | VWAP momentum · 1h | momentum | 68.75 | -31.25 | 694 | 21.6 | -53.41 | -10.87 | -55.11 | 1224 |
| 62 | Agent (ML meta-label) | meta | 68.38 | -31.62 | 1302 | 20.4 | -18.20 | -3.23 | -18.97 | 306 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.09 | -98.96 | 5171 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.71 | -23.98 | -79.86 | 1399 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -46.54 | -93.68 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -30.96 | -88.89 | 1896 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.40 | -38.12 | -91.40 | 2321 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.89 | -32.40 | -90.89 | 2238 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -52.37 | -97.77 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -60.70 | -96.35 | 3381 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.32 | -34.25 | -93.48 | 2401 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.11 | -34.48 | -82.11 | 1682 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -52.34 | -99.48 | 5868 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.06 | -43.51 | -93.06 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -36.78 | -95.58 | 3382 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -71.54 | -99.79 | 6170 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -43.76 | -91.85 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.64 | -26.10 | -74.69 | 1557 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.43 | -97.75 | 3540 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -58.98 | -98.68 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.50 | -28.42 | -69.72 | 1204 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -53.70 | -94.72 | 2763 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -37.14 | -84.75 | 1797 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.20 | -99.62 | 6310 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.38 | -30.38 | -88.39 | 2229 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.20 | -19.63 | -77.28 | 1700 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.34 | -36.09 | -90.35 | 2237 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.48 | -50.10 | -96.48 | 3817 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.57 | -52.38 | -89.57 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.03 | -25.10 | -64.85 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.17 | -25.86 | -74.17 | 1274 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.92 | -18.99 | -76.93 | 1610 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.84 | -49.23 | -96.84 | 4240 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.28 | -99.92 | 8222 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-02T20:55 | Keltner breakout · 1h | sell | AMZN | 20.53 | -0.58 | stop-loss |
| 2026-11-02T20:55 | Opening range 30m | sell | SQQQ | 23.23 | 1.02 | end-of-day flatten |
| 2026-11-02T20:55 | Opening range 15m | sell | SQQQ | 17.11 | 0.75 | end-of-day flatten |
| 2026-11-02T20:52 | Candlestick reversal · 1h | buy | SOXL | 7.69 | — | entry |
| 2026-11-02T20:52 | Candlestick reversal · 1h | sell | ETHU | 6.91 | -0.01 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 02:20:05.000121+00:00 -> 2026-11-03 02:30:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
