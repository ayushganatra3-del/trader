# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T17:26:05.000190+00:00 · 47404 ticks

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

Today: 19902 decisions in 2178 calls, $0.2532 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T17:26 | 12 / 14 / 5 | ARKK 17%, TNA 15%, LABU 15% |  |
| Breezy | 2026-11-04T17:26 | 0 / 29 / 2 | cash |  |
| Boozy | 2026-11-04T17:26 | 6 / 23 / 2 | MSTR 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 111.86 | 11.86 | 0 | — | 13.18 | 4.98 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.57 | 7.57 | 17 | 70.6 | 7.02 | 2.17 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.73 | 1.73 | 0 | — | 5.69 | 1.56 | -6.60 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.24 | 0.23 | 5 | 40.0 | 5.30 | 1.20 | -7.93 | 8 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.12 | -0.88 | 27 | 44.4 | -2.44 | -0.72 | -9.06 | 28 |
| 9 | Hold SPY | benchmark | 98.19 | -1.81 | 0 | — | -0.76 | -0.33 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.30 | -3.70 | 111 | 35.1 | 5.94 | 2.75 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.12 | -4.88 | 0 | — | -2.43 | -0.88 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Hold BTC | benchmark | 94.43 | -5.57 | 0 | — | -1.01 | 0.00 | -13.22 | 1 |
| 17 | Agent (rotation) | meta | 94.31 | -5.68 | 163 | 27.6 | -6.32 | -5.05 | -8.68 | 184 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.31 | -5.69 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 19 | Gap and go | momentum | 93.75 | -6.25 | 157 | 27.4 | -0.59 | -0.12 | -8.76 | 223 |
| 20 | Max aggression: 5-day momentum | meta | 91.90 | -8.10 | 16 | 43.8 | -23.26 | -1.32 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Parabolic SAR · 1h | trend | 90.56 | -9.44 | 154 | 26.6 | -13.36 | -2.88 | -18.39 | 243 |
| 23 | Trend pullback · 1h | trend | 90.40 | -9.60 | 103 | 22.3 | -16.96 | -6.30 | -17.97 | 79 |
| 24 | Agent | meta | 89.73 | -10.27 | 144 | 38.2 | -11.58 | -6.98 | -12.62 | 205 |
| 25 | Opening range 30m | breakout | 89.55 | -10.45 | 355 | 33.0 | -15.44 | -5.12 | -17.21 | 591 |
| 26 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.98 | -3.10 | -14.15 | 85 |
| 27 | Copy: Insider buying | copy | 88.63 | -11.37 | 37 | 37.8 | -22.10 | -4.49 | -23.56 | 63 |
| 28 | Donchian 55/20 · 1h | breakout | 86.91 | -13.09 | 62 | 12.9 | -14.43 | -3.11 | -19.85 | 107 |
| 29 | Daily: Bullish score | daily | 86.76 | -13.24 | 14 | 21.4 | -11.72 | -1.83 | -16.58 | 14 |
| 30 | Stochastic reversion · 1h | reversion | 86.65 | -13.35 | 248 | 47.6 | -20.46 | -3.88 | -24.90 | 385 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.91 | -14.09 | 1 | 0.0 | -7.99 | -1.20 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -11.94 | -3.93 | -14.77 | 95 |
| 33 | ADX DI cross · 1h | trend | 85.33 | -14.67 | 155 | 18.1 | -19.90 | -3.54 | -24.11 | 272 |
| 34 | Volume breakout · 1h | breakout | 85.18 | -14.82 | 130 | 28.5 | -13.49 | -3.06 | -18.08 | 104 |
| 35 | MFI reversion · 1h | reversion | 84.55 | -15.45 | 318 | 34.6 | -14.00 | -2.12 | -18.76 | 151 |
| 36 | Keltner breakout · 1h | breakout | 84.23 | -15.77 | 92 | 22.8 | -21.91 | -4.55 | -24.27 | 184 |
| 37 | Opening range 15m | breakout | 82.78 | -17.22 | 433 | 30.3 | -20.16 | -6.19 | -21.19 | 724 |
| 38 | Connors RSI(2) · 1h | reversion | 82.77 | -17.23 | 192 | 40.6 | -18.99 | -6.22 | -19.59 | 127 |
| 39 | Ichimoku · 1h | trend | 82.39 | -17.61 | 85 | 12.9 | -19.44 | -4.10 | -26.10 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 81.77 | -18.23 | 146 | 24.0 | -17.57 | -3.53 | -23.94 | 248 |
| 41 | CCI reversion · 1h | reversion | 80.61 | -19.39 | 277 | 46.2 | -22.36 | -3.32 | -27.71 | 456 |
| 42 | Heikin-Ashi · 1h | trend | 79.21 | -20.79 | 372 | 22.6 | -39.86 | -8.14 | -43.72 | 673 |
| 43 | EMA 20/50 cross · 1h | trend | 79.10 | -20.90 | 92 | 10.9 | -18.42 | -3.45 | -26.61 | 133 |
| 44 | MACD zero-line · 1h | trend | 78.82 | -21.18 | 141 | 15.6 | -24.69 | -5.18 | -29.61 | 219 |
| 45 | MACD cross · 1h | trend | 78.50 | -21.50 | 310 | 22.9 | -31.67 | -6.11 | -34.06 | 474 |
| 46 | Z-score reversion · 1h | reversion | 78.44 | -21.56 | 151 | 37.1 | -13.99 | -2.02 | -23.02 | 220 |
| 47 | Supertrend · 1h | trend | 78.20 | -21.80 | 147 | 12.9 | -26.59 | -4.97 | -30.19 | 237 |
| 48 | Bollinger reversion · 1h | reversion | 77.06 | -22.94 | 233 | 40.3 | -27.90 | -5.52 | -30.37 | 381 |
| 49 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.32 | -4.46 | -33.57 | 33 |
| 50 | RSI momentum · 1h | momentum | 76.90 | -23.10 | 142 | 12.0 | -28.28 | -5.44 | -30.64 | 224 |
| 51 | Williams %R · 1h | reversion | 76.69 | -23.31 | 289 | 47.4 | -35.90 | -6.40 | -37.28 | 534 |
| 52 | Triple EMA stack · 1h | trend | 75.99 | -24.01 | 131 | 13.7 | -28.94 | -5.71 | -32.12 | 209 |
| 53 | OBV trend · 1h | momentum | 75.55 | -24.45 | 248 | 17.3 | -29.92 | -6.53 | -31.18 | 293 |
| 54 | Donchian 20/10 · 1h | breakout | 74.75 | -25.25 | 124 | 19.4 | -26.94 | -4.87 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.45 | -25.55 | 317 | 25.2 | -34.04 | -6.62 | -36.90 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.77 | -27.23 | 136 | 28.7 | -18.90 | -3.20 | -26.28 | 209 |
| 57 | Agent (ML meta-label) | meta | 70.33 | -29.67 | 1406 | 22.2 | -14.05 | -2.77 | -20.16 | 285 |
| 58 | VWAP momentum · 1h | momentum | 69.92 | -30.08 | 723 | 22.1 | -54.91 | -11.33 | -56.26 | 1224 |
| 59 | EMA 9/21 cross · 1h | trend | 69.78 | -30.22 | 225 | 9.8 | -36.68 | -7.35 | -40.22 | 340 |
| 60 | Candlestick reversal · 1h | reversion | 69.47 | -30.53 | 376 | 30.1 | -36.04 | -6.82 | -38.82 | 559 |
| 61 | Three white soldiers | momentum | 68.19 | -31.81 | 433 | 16.2 | -47.31 | -22.06 | -47.62 | 632 |
| 62 | Max aggression: 1-day momentum | meta | 66.83 | -33.17 | 24 | 29.2 | -35.71 | -2.12 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -44.83 | -98.99 | 5189 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.08 | -24.38 | -80.26 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -43.89 | -93.44 | 2508 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -30.24 | -89.13 | 1911 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.97 | -36.23 | -91.16 | 2316 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.34 | -31.39 | -90.39 | 2202 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -49.02 | -97.74 | 3449 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -53.34 | -96.23 | 3359 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -32.70 | -93.55 | 2450 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.06 | -36.05 | -82.12 | 1642 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.77 | -99.49 | 5892 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -41.78 | -93.06 | 2609 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.52 | -36.97 | -95.53 | 3373 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -67.99 | -99.80 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -40.79 | -91.86 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.87 | -26.62 | -74.95 | 1575 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -55.46 | -97.75 | 3502 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -59.58 | -98.70 | 4827 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.64 | -28.02 | -70.61 | 1196 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -51.26 | -94.86 | 2764 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -36.13 | -84.93 | 1793 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.71 | -99.63 | 6319 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.16 | -29.83 | -88.50 | 2243 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.38 | -18.87 | -77.02 | 1712 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -37.00 | -90.63 | 2244 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.16 | -96.53 | 3836 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.08 | -48.98 | -89.31 | 2138 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.42 | -27.16 | -65.83 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -24.39 | -73.90 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.75 | -18.51 | -77.55 | 1617 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.95 | -51.71 | -96.99 | 4251 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.81 | -99.92 | 8193 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T17:20 | Agent (ML meta-label) | buy | TNA | 5.40 | — | entry |
| 2026-11-04T17:10 | Agent (ML meta-label) | sell | TNA | 5.03 | 0.02 | selected signal exited |
| 2026-11-04T17:10 | Agent (ML meta-label) | sell | GOOGL | 5.01 | -0.01 | selected signal exited |
| 2026-11-04T17:05 | Agent (ML meta-label) | buy | TNA | 5.01 | — | entry |
| 2026-11-04T17:05 | Agent (ML meta-label) | buy | GOOGL | 5.01 | — | entry |
| 2026-11-04T17:05 | Three white soldiers | buy | LABU | 16.95 | — | entry |
| 2026-11-04T17:05 | Three white soldiers | sell | GOOGL | 16.91 | -0.06 | exit signal |
| 2026-11-04T17:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 99.42 | — | entry |
| 2026-11-04T17:00 | Agent (ML meta-label) | sell | TNA | 5.05 | 0.02 | selected signal exited |
| 2026-11-04T17:00 | Agent (ML meta-label) | sell | AMD | 5.01 | 0.01 | selected signal exited |
| 2026-11-04T17:00 | MFI reversion · 1h | buy | COIN | 21.10 | — | entry |
| 2026-11-04T16:55 | Agent (rotation) | buy | UPRO | 3.15 | — | entry |
| 2026-11-04T16:55 | Agent (rotation) | buy | SPY | 3.15 | — | entry |
| 2026-11-04T16:55 | Agent (rotation) | buy | GOOGL | 3.15 | — | entry |
| 2026-11-04T16:55 | Agent (ML meta-label) | buy | AMD | 5.00 | — | following Supertrend |
| 2026-11-04T16:55 | Agent (ML meta-label) | sell | GOOGL | 5.00 | 0.00 | selected signal exited |
| 2026-11-04T16:55 | Three white soldiers | buy | SPY | 16.98 | — | entry |
| 2026-11-04T16:55 | Opening range 30m | buy | UPRO | 4.70 | — | entry signal |
| 2026-11-04T16:55 | Opening range 30m | buy | SPY | 8.98 | — | entry signal |
| 2026-11-04T16:55 | Opening range 30m | buy | GOOGL | 8.98 | — | entry signal |
| 2026-11-04T16:55 | Opening range 15m | buy | UPRO | 7.55 | — | entry signal |
| 2026-11-04T16:55 | Opening range 15m | buy | SPY | 7.55 | — | entry signal |
| 2026-11-04T16:50 | Agent (ML meta-label) | buy | GOOGL | 5.00 | — | entry |
| 2026-11-04T16:50 | Agent (ML meta-label) | sell | AMD | 5.00 | -0.03 | selected signal exited |
| 2026-11-04T16:50 | Three white soldiers | buy | META | 16.97 | — | entry signal |
| 2026-11-04T16:50 | Three white soldiers | buy | GOOGL | 16.97 | — | entry signal |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | UPRO | 5.01 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | TQQQ | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | TNA | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | SPY | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | IWM | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | BITX | 5.02 | — | following Z-score reversion |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | AMZN | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | AMD | 5.02 | — | following Supertrend |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | SQQQ | 6.57 | 0.05 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | MSTR | 5.05 | 0.01 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | MSFT | 5.04 | 0.02 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | ETHU | 5.04 | 0.01 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | COIN | 5.08 | 0.00 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | AAPL | 5.03 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 17:26:05.000190+00:00 -> 2026-11-04 17:36:05.000190+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 17:26:05.000190+00:00 -> 2026-11-04 17:36:05.000190+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 17:26:05.000190+00:00 -> 2026-11-04 17:36:05.000190+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
