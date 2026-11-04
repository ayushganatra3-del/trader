# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T16:25:05.000141+00:00 · 47362 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.73 (-10.27%)

Closed trades 144, win rate 38.2%, fees £4.01, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 16092 decisions in 2052 calls, $0.2088 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T16:25 | 1 / 4 / 25 | cash |  |
| Breezy | 2026-11-04T16:25 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-04T16:25 | 4 / 22 / 4 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 111.56 | 11.56 | 0 | — | 12.74 | 4.91 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.39 | 5.39 | 17 | 70.6 | 4.88 | 1.54 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.22 | 1.22 | 0 | — | 5.19 | 1.49 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.61 | -0.39 | 26 | 46.2 | -1.93 | -0.58 | -8.03 | 27 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.45 | -1.55 | 5 | 40.0 | 3.43 | 0.87 | -7.93 | 8 |
| 9 | Hold SPY | benchmark | 97.67 | -2.33 | 0 | — | -1.12 | -0.54 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 96.21 | -3.79 | 110 | 35.5 | 5.90 | 2.73 | -3.27 | 90 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.00 | -5.00 | 0 | — | -2.38 | -0.86 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Hold BTC | benchmark | 94.37 | -5.63 | 0 | — | -1.12 | -0.02 | -13.22 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.28 | -5.72 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 18 | Gap and go | momentum | 93.60 | -6.40 | 157 | 27.4 | -0.71 | -0.17 | -8.76 | 223 |
| 19 | Agent (rotation) | meta | 93.56 | -6.44 | 163 | 27.6 | -7.67 | -5.86 | -8.68 | 188 |
| 20 | Max aggression: 5-day momentum | meta | 91.89 | -8.11 | 16 | 43.8 | -23.24 | -1.32 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.94 | -9.06 | 103 | 22.3 | -16.46 | -6.09 | -17.40 | 78 |
| 23 | Parabolic SAR · 1h | trend | 90.13 | -9.87 | 154 | 26.6 | -13.86 | -3.11 | -18.16 | 244 |
| 24 | Agent | meta | 89.73 | -10.27 | 144 | 38.2 | -11.58 | -6.98 | -12.62 | 205 |
| 25 | Opening range 30m | breakout | 89.20 | -10.80 | 355 | 33.0 | -15.94 | -5.27 | -17.21 | 588 |
| 26 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.98 | -3.10 | -14.15 | 85 |
| 27 | Copy: Insider buying | copy | 88.14 | -11.86 | 37 | 37.8 | -22.54 | -4.61 | -23.56 | 63 |
| 28 | Donchian 55/20 · 1h | breakout | 87.01 | -12.99 | 62 | 12.9 | -14.31 | -3.09 | -19.86 | 107 |
| 29 | Daily: Bullish score | daily | 86.90 | -13.10 | 14 | 21.4 | -11.56 | -1.80 | -16.58 | 14 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -11.94 | -3.93 | -14.77 | 95 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.70 | -14.29 | 1 | 0.0 | -7.92 | -1.18 | -16.59 | 1 |
| 32 | Stochastic reversion · 1h | reversion | 85.31 | -14.69 | 248 | 47.6 | -22.23 | -4.39 | -25.47 | 385 |
| 33 | Volume breakout · 1h | breakout | 84.89 | -15.11 | 130 | 28.5 | -13.77 | -3.13 | -18.08 | 103 |
| 34 | ADX DI cross · 1h | trend | 84.58 | -15.42 | 155 | 18.1 | -18.46 | -3.42 | -22.34 | 271 |
| 35 | Keltner breakout · 1h | breakout | 83.97 | -16.03 | 92 | 22.8 | -22.15 | -4.61 | -24.27 | 184 |
| 36 | MFI reversion · 1h | reversion | 83.86 | -16.14 | 317 | 34.4 | -13.91 | -2.14 | -18.07 | 151 |
| 37 | Connors RSI(2) · 1h | reversion | 82.90 | -17.10 | 192 | 40.6 | -19.42 | -6.43 | -20.13 | 129 |
| 38 | Opening range 15m | breakout | 82.52 | -17.48 | 433 | 30.3 | -20.60 | -6.34 | -21.19 | 722 |
| 39 | Ichimoku · 1h | trend | 81.82 | -18.18 | 85 | 12.9 | -17.57 | -3.55 | -25.73 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 81.43 | -18.57 | 146 | 24.0 | -17.46 | -3.50 | -23.94 | 248 |
| 41 | CCI reversion · 1h | reversion | 79.73 | -20.27 | 277 | 46.2 | -22.83 | -3.43 | -27.71 | 455 |
| 42 | EMA 20/50 cross · 1h | trend | 78.93 | -21.07 | 92 | 10.9 | -19.69 | -3.59 | -28.14 | 130 |
| 43 | Heikin-Ashi · 1h | trend | 78.76 | -21.24 | 372 | 22.6 | -39.95 | -8.27 | -43.61 | 665 |
| 44 | MACD zero-line · 1h | trend | 78.35 | -21.65 | 141 | 15.6 | -25.73 | -5.43 | -30.14 | 220 |
| 45 | MACD cross · 1h | trend | 78.03 | -21.96 | 309 | 23.0 | -31.84 | -6.15 | -33.72 | 479 |
| 46 | Z-score reversion · 1h | reversion | 77.84 | -22.16 | 151 | 37.1 | -14.72 | -2.17 | -23.02 | 220 |
| 47 | Supertrend · 1h | trend | 77.74 | -22.26 | 147 | 12.9 | -27.19 | -5.13 | -30.19 | 237 |
| 48 | Bollinger reversion · 1h | reversion | 77.54 | -22.46 | 233 | 40.3 | -27.44 | -5.40 | -30.37 | 380 |
| 49 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.34 | -4.46 | -33.57 | 33 |
| 50 | RSI momentum · 1h | momentum | 76.58 | -23.42 | 142 | 12.0 | -29.44 | -5.75 | -31.76 | 227 |
| 51 | Williams %R · 1h | reversion | 76.04 | -23.96 | 289 | 47.4 | -36.30 | -6.52 | -37.21 | 533 |
| 52 | Triple EMA stack · 1h | trend | 75.80 | -24.20 | 131 | 13.7 | -28.93 | -5.86 | -32.11 | 208 |
| 53 | OBV trend · 1h | momentum | 75.11 | -24.89 | 248 | 17.3 | -30.13 | -6.58 | -30.97 | 291 |
| 54 | Donchian 20/10 · 1h | breakout | 74.44 | -25.56 | 124 | 19.4 | -27.12 | -4.89 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 73.95 | -26.05 | 314 | 25.5 | -34.51 | -6.75 | -36.94 | 385 |
| 56 | RSI(14) reversion · 1h | reversion | 72.15 | -27.85 | 136 | 28.7 | -21.29 | -3.71 | -26.28 | 215 |
| 57 | Agent (ML meta-label) | meta | 70.13 | -29.87 | 1393 | 22.0 | -6.26 | -1.16 | -16.92 | 281 |
| 58 | VWAP momentum · 1h | momentum | 69.90 | -30.10 | 720 | 22.1 | -54.97 | -11.30 | -56.36 | 1227 |
| 59 | Candlestick reversal · 1h | reversion | 69.64 | -30.36 | 374 | 30.2 | -35.41 | -6.79 | -38.34 | 562 |
| 60 | EMA 9/21 cross · 1h | trend | 69.62 | -30.39 | 225 | 9.8 | -36.98 | -7.45 | -40.27 | 339 |
| 61 | Three white soldiers | momentum | 67.87 | -32.13 | 432 | 16.2 | -46.90 | -21.53 | -47.11 | 628 |
| 62 | Max aggression: 1-day momentum | meta | 65.03 | -34.97 | 24 | 29.2 | -37.42 | -2.26 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.44 | -98.98 | 5167 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.08 | -24.27 | -80.29 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -44.38 | -93.51 | 2509 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.86 | -30.19 | -89.09 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.07 | -36.51 | -91.23 | 2312 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.42 | -31.91 | -90.42 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -49.82 | -97.76 | 3450 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -53.80 | -96.31 | 3359 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.43 | -32.59 | -93.56 | 2438 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.32 | -35.92 | -82.32 | 1643 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -54.15 | -99.49 | 5896 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.01 | -42.53 | -93.10 | 2617 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.47 | -36.91 | -95.48 | 3369 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.32 | -99.80 | 6155 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.69 | -40.95 | -91.86 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.91 | -26.77 | -75.03 | 1566 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -57.48 | -97.76 | 3492 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -61.11 | -98.70 | 4825 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.52 | -27.80 | -70.50 | 1200 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -52.14 | -94.88 | 2776 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.72 | -36.27 | -84.92 | 1794 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.31 | -99.63 | 6309 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.16 | -29.97 | -88.41 | 2255 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.50 | -18.93 | -76.90 | 1715 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -37.22 | -90.65 | 2239 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.47 | -50.05 | -96.53 | 3833 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.04 | -48.14 | -89.37 | 2137 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.24 | -27.10 | -65.72 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.79 | -24.66 | -74.12 | 1271 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.02 | -18.87 | -77.63 | 1621 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.97 | -51.86 | -96.99 | 4250 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.24 | -99.92 | 8194 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T16:25 | Agent (rotation) | sell | PLTR | 3.09 | -0.07 | selected signal exited |
| 2026-11-04T16:25 | Agent (rotation) | sell | GOOGL | 3.12 | -0.04 | selected signal exited |
| 2026-11-04T16:25 | Keltner breakout · 1h | sell | XRP-USD | 5.97 | -0.06 | stop-loss |
| 2026-11-04T16:25 | Bollinger breakout · 1h | sell | XRP-USD | 4.77 | -0.05 | stop-loss |
| 2026-11-04T16:25 | Opening range 30m | buy | COIN | 4.54 | — | rebalance up |
| 2026-11-04T16:25 | Opening range 30m | sell | PLTR | 8.79 | -0.19 | stop-loss |
| 2026-11-04T16:25 | Opening range 30m | sell | GOOGL | 8.86 | -0.12 | stop-loss |
| 2026-11-04T16:25 | Opening range 15m | sell | SPY | 5.91 | -0.03 | exit signal |
| 2026-11-04T16:25 | Gap and go | sell | AAPL | 23.35 | 0.06 | exit signal |
| 2026-11-04T16:15 | Agent (ML meta-label) | buy | UPRO | 5.86 | — | entry |
| 2026-11-04T16:15 | Agent (ML meta-label) | sell | TNA | 1.34 | 0.00 | selected signal exited |
| 2026-11-04T16:15 | Agent (ML meta-label) | sell | PLTR | 5.00 | -0.02 | selected signal exited |
| 2026-11-04T16:10 | Agent (ML meta-label) | buy | TNA | 1.33 | — | entry |
| 2026-11-04T16:10 | Agent (ML meta-label) | buy | PLTR | 5.02 | — | entry |
| 2026-11-04T16:10 | Agent (ML meta-label) | sell | AMZN | 6.35 | -0.06 | selected signal exited |
| 2026-11-04T16:05 | Agent (rotation) | sell | SPY | 2.26 | -0.01 | selected signal exited |
| 2026-11-04T16:05 | Agent (ML meta-label) | buy | TECL | 2.58 | — | entry |
| 2026-11-04T16:05 | Agent (ML meta-label) | buy | SPY | 3.66 | — | rebalance up |
| 2026-11-04T16:05 | Agent (ML meta-label) | sell | TQQQ | 6.24 | -0.17 | selected signal exited |
| 2026-11-04T16:05 | Candlestick reversal · 1h | sell | SOXL | 16.23 | -2.29 | stop-loss |
| 2026-11-04T16:05 | Three white soldiers | sell | AAPL | 13.66 | 0.08 | exit signal |
| 2026-11-04T16:05 | Opening range 30m | sell | SPY | 8.94 | -0.02 | exit signal |
| 2026-11-04T16:05 | Opening range 15m | sell | UPRO | 5.87 | -0.07 | stop-loss |
| 2026-11-04T16:00 | Agent (rotation) | sell | AMZN | 3.11 | -0.05 | selected signal exited |
| 2026-11-04T16:00 | MFI reversion · 1h | sell | DOGE-USD | 21.32 | 0.54 | exit signal |
| 2026-11-04T16:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 7.80 | — | entry signal |
| 2026-11-04T16:00 | EMA 20/50 cross · 1h | buy | AMZN | 6.17 | — | rebalance up |
| 2026-11-04T16:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 4.61 | 0.15 | rebalance down |
| 2026-11-04T16:00 | EMA 20/50 cross · 1h | sell | SQQQ | 4.79 | 0.09 | rebalance down |
| 2026-11-04T16:00 | EMA 20/50 cross · 1h | sell | BTC-USD | 4.56 | 0.08 | rebalance down |
| 2026-11-04T16:00 | Opening range 30m | buy | SPY | 8.95 | — | entry |
| 2026-11-04T16:00 | Opening range 30m | sell | AMZN | 8.83 | -0.15 | stop-loss |
| 2026-11-04T16:00 | Opening range 15m | sell | AMZN | 5.84 | -0.10 | exit signal |
| 2026-11-04T16:00 | Gap and go | sell | MSFT | 23.39 | -0.02 | exit signal |
| 2026-11-04T15:50 | Agent (rotation) | sell | UPRO | 3.13 | -0.03 | selected signal exited |
| 2026-11-04T15:50 | Williams %R · 1h | sell | SOXL | 10.34 | -1.16 | stop-loss |
| 2026-11-04T15:50 | Z-score reversion · 1h | sell | SOXL | 9.34 | -1.27 | stop-loss |
| 2026-11-04T15:50 | Bollinger reversion · 1h | sell | SOXL | 18.55 | -1.84 | stop-loss |
| 2026-11-04T15:50 | RSI(14) reversion · 1h | sell | SOXL | 11.33 | -1.49 | stop-loss |
| 2026-11-04T15:50 | Opening range 30m | buy | COIN | 8.15 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 16:25:05.000141+00:00 -> 2026-11-04 16:35:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 16:25:05.000141+00:00 -> 2026-11-04 16:35:05.000141+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 16:25:05.000141+00:00 -> 2026-11-04 16:35:05.000141+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
