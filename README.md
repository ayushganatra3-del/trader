# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T09:50:05.000125+00:00 · 46034 ticks

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

Today: 7470 decisions in 1494 calls, $0.1043 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T09:50 | 2 / 2 / 1 | cash |  |
| Breezy | 2026-11-03T09:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T09:50 | 3 / 2 / 0 | ETH-USD 74% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.03 | 9.03 | 0 | — | 9.79 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.53 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.12 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.29 | -1.71 | 103 | 45.6 | -13.20 | -3.64 | -13.45 | 143 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.00 | -2.00 | 0 | — | 1.41 | 0.63 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.51 | -3.49 | 0 | — | -1.85 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.49 | 1.76 | -2.66 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -4.98 | -3.06 | -8.93 | 169 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.10 | -5.90 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.75 | 1.25 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.60 | -6.40 | 0 | — | -2.94 | -1.09 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 90.95 | -9.04 | 101 | 21.8 | -16.63 | -6.16 | -17.67 | 80 |
| 21 | Hold BTC | benchmark | 90.65 | -9.35 | 0 | — | 0.19 | 0.20 | -12.65 | 1 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.35 | -12.20 | 209 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.01 | -17.21 | 578 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -7.84 | -2.60 | -13.40 | 87 |
| 25 | Donchian 55/20 · 1h | breakout | 89.38 | -10.62 | 60 | 13.3 | -13.71 | -3.07 | -18.06 | 99 |
| 26 | Daily: Bullish score | daily | 88.74 | -11.26 | 14 | 21.4 | -5.96 | -0.72 | -14.73 | 14 |
| 27 | Parabolic SAR · 1h | trend | 88.72 | -11.28 | 149 | 26.8 | -14.60 | -3.43 | -17.40 | 239 |
| 28 | Copy: Insider buying | copy | 88.57 | -11.43 | 35 | 37.1 | -22.54 | -4.61 | -23.08 | 59 |
| 29 | Max aggression: 5-day momentum | meta | 87.03 | -12.96 | 15 | 40.0 | -30.82 | -2.05 | -37.35 | 26 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.06 | -14.94 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.77 | -15.22 | 129 | 28.7 | -17.56 | -3.93 | -18.81 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.74 | -15.26 | 89 | 23.6 | -21.38 | -4.22 | -24.03 | 172 |
| 34 | Connors RSI(2) · 1h | reversion | 84.19 | -15.81 | 191 | 40.8 | -20.81 | -6.65 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.64 | -16.36 | 148 | 18.2 | -20.00 | -3.76 | -22.16 | 249 |
| 36 | Stochastic reversion · 1h | reversion | 83.01 | -16.99 | 232 | 46.6 | -25.64 | -5.38 | -25.93 | 390 |
| 37 | MFI reversion · 1h | reversion | 82.35 | -17.65 | 299 | 32.8 | -17.13 | -2.78 | -18.26 | 149 |
| 38 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.47 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 81.92 | -18.08 | 83 | 13.3 | -18.16 | -3.67 | -25.58 | 120 |
| 40 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -16.91 | -3.28 | -22.79 | 233 |
| 41 | EMA 20/50 cross · 1h | trend | 78.85 | -21.15 | 90 | 11.1 | -22.12 | -4.15 | -27.42 | 124 |
| 42 | CCI reversion · 1h | reversion | 78.36 | -21.64 | 264 | 44.7 | -27.72 | -4.43 | -28.59 | 445 |
| 43 | Supertrend · 1h | trend | 77.64 | -22.36 | 141 | 12.8 | -28.21 | -5.42 | -29.57 | 219 |
| 44 | MACD zero-line · 1h | trend | 77.59 | -22.41 | 136 | 15.4 | -25.81 | -5.59 | -27.76 | 209 |
| 45 | Triple EMA stack · 1h | trend | 77.17 | -22.82 | 125 | 14.4 | -28.12 | -5.16 | -30.89 | 203 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -28.44 | -3.77 | -33.54 | 33 |
| 47 | MACD cross · 1h | trend | 76.87 | -23.13 | 299 | 23.4 | -33.37 | -6.64 | -35.32 | 471 |
| 48 | RSI momentum · 1h | momentum | 76.84 | -23.16 | 135 | 12.6 | -28.79 | -5.49 | -30.84 | 210 |
| 49 | Heikin-Ashi · 1h | trend | 76.48 | -23.52 | 356 | 22.5 | -40.55 | -8.68 | -43.18 | 658 |
| 50 | Bollinger reversion · 1h | reversion | 76.29 | -23.71 | 215 | 38.1 | -31.25 | -6.49 | -31.58 | 375 |
| 51 | Williams %R · 1h | reversion | 76.13 | -23.87 | 267 | 46.1 | -36.52 | -6.63 | -36.79 | 517 |
| 52 | OBV trend · 1h | momentum | 76.04 | -23.96 | 239 | 17.6 | -32.49 | -6.94 | -33.25 | 299 |
| 53 | Donchian 20/10 · 1h | breakout | 76.01 | -23.99 | 119 | 20.2 | -27.15 | -4.73 | -31.02 | 206 |
| 54 | Z-score reversion · 1h | reversion | 74.85 | -25.15 | 139 | 33.8 | -17.31 | -2.67 | -23.02 | 211 |
| 55 | ROC + volume · 1h | momentum | 74.82 | -25.18 | 299 | 25.4 | -31.67 | -5.89 | -34.50 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 70.78 | -29.22 | 128 | 25.8 | -21.48 | -3.87 | -26.28 | 193 |
| 57 | Three white soldiers | momentum | 70.00 | -30.00 | 408 | 16.2 | -45.66 | -21.26 | -45.70 | 611 |
| 58 | EMA 9/21 cross · 1h | trend | 69.00 | -31.00 | 218 | 9.6 | -37.41 | -7.57 | -39.06 | 324 |
| 59 | Candlestick reversal · 1h | reversion | 69.00 | -31.00 | 345 | 27.8 | -38.29 | -7.89 | -38.49 | 546 |
| 60 | Max aggression: 1-day momentum | meta | 68.78 | -31.22 | 23 | 30.4 | -35.26 | -2.08 | -50.32 | 42 |
| 61 | VWAP momentum · 1h | momentum | 68.44 | -31.56 | 697 | 21.5 | -52.89 | -10.56 | -55.47 | 1220 |
| 62 | Agent (ML meta-label) | meta | 68.32 | -31.68 | 1302 | 20.4 | -13.55 | -2.45 | -16.57 | 287 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -44.88 | -98.97 | 5177 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.83 | -24.24 | -80.27 | 1401 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.70 | -47.91 | -93.70 | 2521 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.01 | -31.49 | -89.04 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -39.14 | -91.47 | 2327 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.79 | -31.99 | -90.80 | 2227 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.79 | -54.23 | -97.80 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -63.21 | -96.35 | 3386 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.19 | -33.72 | -93.30 | 2391 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.98 | -34.99 | -82.00 | 1682 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -51.65 | -99.48 | 5871 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.19 | -45.21 | -93.19 | 2616 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.52 | -36.63 | -95.52 | 3375 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -74.02 | -99.80 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.96 | -45.29 | -91.98 | 2278 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.90 | -26.62 | -74.91 | 1561 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -62.16 | -97.76 | 3545 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.59 | -98.66 | 4827 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.63 | -28.43 | -69.77 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -56.12 | -94.80 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.80 | -37.63 | -84.80 | 1799 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.49 | -99.61 | 6306 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.12 | -29.82 | -88.15 | 2228 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.54 | -19.09 | -76.65 | 1688 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -35.64 | -90.32 | 2232 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -49.69 | -96.45 | 3818 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.49 | -54.40 | -89.49 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.08 | -25.19 | -64.90 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.83 | -25.42 | -73.96 | 1270 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.64 | -18.59 | -77.03 | 1598 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -48.55 | -96.80 | 4238 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -104.91 | -99.93 | 8230 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T09:05 | Three white soldiers | buy | SOL-USD | 17.50 | — | entry signal |
| 2026-11-03T08:00 | MFI reversion · 1h | buy | BTC-USD | 10.91 | — | entry signal |
| 2026-11-03T08:00 | MFI reversion · 1h | sell | DOGE-USD | 6.74 | -0.08 | rebalance down |
| 2026-11-03T08:00 | Candlestick reversal · 1h | buy | ETH-USD | 7.67 | — | entry signal |
| 2026-11-03T08:00 | Candlestick reversal · 1h | buy | BTC-USD | 7.67 | — | entry signal |
| 2026-11-03T08:00 | Candlestick reversal · 1h | sell | XRP-USD | 3.84 | -0.02 | rebalance down |
| 2026-11-03T08:00 | Candlestick reversal · 1h | sell | DOGE-USD | 3.83 | -0.01 | rebalance down |
| 2026-11-03T08:00 | VWAP momentum · 1h | buy | XRP-USD | 17.12 | — | entry signal |
| 2026-11-03T08:00 | VWAP momentum · 1h | buy | ETH-USD | 17.12 | — | entry signal |
| 2026-11-03T08:00 | MACD zero-line · 1h | buy | XRP-USD | 19.41 | — | entry signal |
| 2026-11-03T07:00 | Ichimoku · 1h | sell | XRP-USD | 20.33 | -0.20 | exit signal |
| 2026-11-03T06:00 | Candlestick reversal · 1h | buy | XRP-USD | 3.83 | — | rebalance up |
| 2026-11-03T06:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.79 | — | rebalance up |
| 2026-11-03T06:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.68 | -0.05 | exit signal |
| 2026-11-03T06:00 | Candlestick reversal · 1h | sell | ETH-USD | 7.66 | -0.07 | exit signal |
| 2026-11-03T06:00 | Candlestick reversal · 1h | sell | BTC-USD | 7.64 | -0.09 | exit signal |
| 2026-11-03T06:00 | VWAP momentum · 1h | sell | XRP-USD | 17.03 | -0.12 | exit signal |
| 2026-11-03T05:00 | CCI reversion · 1h | buy | BTC-USD | 13.07 | — | entry |
| 2026-11-03T05:00 | CCI reversion · 1h | sell | XRP-USD | 13.08 | -0.05 | exit signal |
| 2026-11-03T05:00 | Ichimoku · 1h | buy | XRP-USD | 20.54 | — | entry signal |
| 2026-11-03T05:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 17.27 | — | entry signal |
| 2026-11-03T04:00 | VWAP momentum · 1h | buy | XRP-USD | 17.15 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 09:50:05.000125+00:00 -> 2026-11-03 10:00:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 09:50:05.000125+00:00 -> 2026-11-03 10:00:05.000125+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 09:50:05.000125+00:00 -> 2026-11-03 10:00:05.000125+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
