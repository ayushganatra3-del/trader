# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T20:55:05.000118+00:00 · 46543 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.19 (-9.81%)

Closed trades 143, win rate 38.5%, fees £3.99, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-03 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 36459 decisions in 3021 calls, $0.4501 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T20:55 | 2 / 13 / 15 | cash |  |
| Breezy | 2026-11-03T20:55 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-03T20:55 | 4 / 23 / 3 | COIN 81% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.99 | 8.99 | 0 | — | 10.08 | 4.41 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.31 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 2.00 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.99 | -2.93 | -12.81 | 143 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.80 | -3.20 | 0 | — | -1.87 | -0.99 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.83 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.17 | 2.01 | -3.82 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.89 | -4.11 | 0 | — | -0.80 | -0.23 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.85 | -4.15 | 5 | 40.0 | 0.62 | 0.28 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.27 | -4.73 | 0 | — | -4.35 | -1.64 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.26 | -1.83 | -5.33 | 29 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.25 | -5.75 | 0 | — | -3.45 | -1.34 | -7.64 | 1 |
| 17 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.34 | -5.62 | -8.68 | 172 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -2.22 | -0.70 | -9.15 | 213 |
| 19 | Hold BTC | benchmark | 91.75 | -8.25 | 0 | — | 0.35 | 0.27 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.59 | -9.41 | 102 | 21.6 | -16.59 | -6.20 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.71 | -6.54 | -12.22 | 205 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.21 | -4.64 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 89.36 | -10.64 | 61 | 23.0 | -8.89 | -3.11 | -13.79 | 89 |
| 25 | Copy: Insider buying | copy | 88.60 | -11.40 | 37 | 37.8 | -22.18 | -4.55 | -23.13 | 61 |
| 26 | Donchian 55/20 · 1h | breakout | 88.52 | -11.48 | 60 | 13.3 | -14.53 | -3.30 | -18.06 | 100 |
| 27 | Daily: Bullish score | daily | 88.47 | -11.53 | 14 | 21.4 | -7.61 | -1.06 | -14.82 | 15 |
| 28 | Parabolic SAR · 1h | trend | 88.32 | -11.68 | 151 | 27.2 | -14.13 | -3.26 | -17.45 | 238 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.48 | -13.52 | 1 | 0.0 | -6.36 | -0.90 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.50 | -4.19 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.42 | -14.58 | 15 | 40.0 | -29.04 | -1.92 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.65 | -15.35 | 129 | 28.7 | -14.93 | -3.44 | -18.08 | 91 |
| 33 | Stochastic reversion · 1h | reversion | 84.61 | -15.39 | 242 | 47.1 | -23.30 | -4.73 | -25.31 | 387 |
| 34 | MFI reversion · 1h | reversion | 84.56 | -15.44 | 310 | 33.9 | -14.45 | -2.24 | -17.89 | 151 |
| 35 | Keltner breakout · 1h | breakout | 84.21 | -15.79 | 89 | 23.6 | -21.04 | -4.44 | -22.20 | 164 |
| 36 | Connors RSI(2) · 1h | reversion | 83.91 | -16.09 | 191 | 40.8 | -19.68 | -6.60 | -20.18 | 131 |
| 37 | ADX DI cross · 1h | trend | 83.07 | -16.93 | 150 | 18.0 | -19.57 | -3.84 | -21.89 | 255 |
| 38 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.77 | -20.73 | 716 |
| 39 | Bollinger breakout · 1h | breakout | 81.56 | -18.44 | 140 | 25.0 | -17.39 | -3.54 | -23.31 | 231 |
| 40 | Ichimoku · 1h | trend | 81.30 | -18.70 | 84 | 13.1 | -17.76 | -3.62 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 79.72 | -20.28 | 90 | 11.1 | -18.21 | -3.30 | -27.05 | 128 |
| 42 | CCI reversion · 1h | reversion | 78.96 | -21.04 | 268 | 44.8 | -24.95 | -3.88 | -27.71 | 450 |
| 43 | Bollinger reversion · 1h | reversion | 78.25 | -21.75 | 226 | 38.9 | -27.19 | -5.37 | -29.70 | 375 |
| 44 | MACD zero-line · 1h | trend | 77.90 | -22.10 | 136 | 15.4 | -25.30 | -5.65 | -27.55 | 213 |
| 45 | Supertrend · 1h | trend | 77.59 | -22.41 | 141 | 12.8 | -29.95 | -5.50 | -31.30 | 217 |
| 46 | Z-score reversion · 1h | reversion | 77.44 | -22.56 | 142 | 34.5 | -14.56 | -2.14 | -23.02 | 218 |
| 47 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.81 | -4.40 | -33.57 | 33 |
| 48 | MACD cross · 1h | trend | 76.97 | -23.03 | 301 | 23.6 | -32.23 | -6.34 | -34.56 | 484 |
| 49 | Williams %R · 1h | reversion | 76.68 | -23.32 | 279 | 46.6 | -36.30 | -6.59 | -37.32 | 525 |
| 50 | RSI momentum · 1h | momentum | 76.51 | -23.49 | 136 | 12.5 | -28.29 | -5.50 | -30.42 | 214 |
| 51 | Triple EMA stack · 1h | trend | 76.08 | -23.92 | 128 | 14.1 | -27.91 | -5.46 | -31.65 | 203 |
| 52 | Heikin-Ashi · 1h | trend | 75.66 | -24.34 | 370 | 22.7 | -40.77 | -8.81 | -43.46 | 666 |
| 53 | OBV trend · 1h | momentum | 75.43 | -24.57 | 242 | 17.4 | -29.42 | -6.32 | -31.40 | 291 |
| 54 | Donchian 20/10 · 1h | breakout | 75.31 | -24.69 | 120 | 20.0 | -28.22 | -5.21 | -30.44 | 206 |
| 55 | ROC + volume · 1h | momentum | 73.92 | -26.08 | 308 | 25.6 | -35.82 | -7.11 | -36.40 | 373 |
| 56 | RSI(14) reversion · 1h | reversion | 72.95 | -27.05 | 130 | 26.2 | -20.97 | -3.98 | -26.28 | 195 |
| 57 | Candlestick reversal · 1h | reversion | 70.79 | -29.21 | 361 | 28.5 | -33.72 | -6.43 | -37.04 | 542 |
| 58 | Agent (ML meta-label) | meta | 69.86 | -30.14 | 1372 | 21.8 | -13.21 | -2.34 | -17.27 | 281 |
| 59 | EMA 9/21 cross · 1h | trend | 69.11 | -30.89 | 219 | 9.6 | -37.63 | -7.69 | -39.23 | 329 |
| 60 | Max aggression: 1-day momentum | meta | 68.82 | -31.18 | 23 | 30.4 | -32.26 | -1.82 | -50.32 | 42 |
| 61 | Three white soldiers | momentum | 68.80 | -31.20 | 420 | 16.0 | -46.63 | -22.09 | -46.63 | 622 |
| 62 | VWAP momentum · 1h | momentum | 68.45 | -31.55 | 712 | 21.6 | -54.62 | -10.84 | -57.30 | 1230 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -44.07 | -98.93 | 5144 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.50 | -23.60 | -80.38 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.34 | -46.12 | -93.44 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.74 | -30.88 | -89.05 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.92 | -36.94 | -91.12 | 2318 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.74 | -33.05 | -90.83 | 2216 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -54.79 | -97.72 | 3470 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -59.74 | -96.31 | 3374 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -34.35 | -93.53 | 2411 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.62 | -34.76 | -82.14 | 1663 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -56.16 | -99.48 | 5881 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -44.61 | -93.02 | 2621 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -38.53 | -95.38 | 3371 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -80.02 | -99.80 | 6183 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.88 | -46.14 | -91.89 | 2264 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.66 | -26.64 | -75.08 | 1548 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -65.79 | -97.80 | 3526 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -65.20 | -98.68 | 4828 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -28.89 | -70.31 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -56.38 | -94.76 | 2782 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.76 | -38.31 | -84.87 | 1793 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -74.89 | -99.61 | 6311 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.14 | -30.73 | -88.21 | 2240 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.36 | -19.10 | -76.74 | 1692 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.18 | -38.37 | -90.19 | 2202 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.46 | -52.80 | -96.46 | 3821 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -56.94 | -89.42 | 2126 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.04 | -27.87 | -65.71 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.64 | -25.50 | -74.16 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.99 | -19.08 | -77.19 | 1599 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.86 | -52.76 | -96.86 | 4238 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.49 | -99.92 | 8208 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T20:55 | Day trade: Stocks in Play ORB | sell | UPRO | 24.17 | 0.05 | target is flat |
| 2026-11-03T20:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 100.11 | -0.08 | target is flat |
| 2026-11-03T20:55 | Opening range 30m | sell | UPRO | 8.19 | -0.01 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | SPY | 8.18 | -0.01 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | PLTR | 6.14 | 0.13 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | MSTR | 8.15 | 0.04 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | MSFT | 8.34 | 0.15 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | META | 8.24 | 0.04 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | COIN | 8.03 | 0.06 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | BITX | 8.28 | 0.07 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 30m | sell | AMZN | 9.94 | -0.03 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | UPRO | 7.47 | -0.02 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | TNA | 7.38 | -0.06 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | SPY | 4.51 | -0.00 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | PLTR | 5.64 | 0.12 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | MSTR | 7.49 | 0.08 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | MSFT | 4.90 | 0.09 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | META | 7.58 | 0.06 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | IWM | 7.49 | -0.03 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | COIN | 7.39 | 0.11 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | BITX | 7.61 | 0.07 | end-of-day flatten |
| 2026-11-03T20:55 | Opening range 15m | sell | AMZN | 4.33 | -0.01 | end-of-day flatten |
| 2026-11-03T20:50 | Agent (ML meta-label) | buy | TSLA | 5.83 | — | rebalance up |
| 2026-11-03T20:50 | Agent (ML meta-label) | buy | SQQQ | 3.49 | — | rebalance up |
| 2026-11-03T20:50 | Agent (ML meta-label) | buy | MSTR | 5.80 | — | rebalance up |
| 2026-11-03T20:50 | Agent (ML meta-label) | buy | ETHU | 5.76 | — | rebalance up |
| 2026-11-03T20:50 | Agent (ML meta-label) | sell | GOOGL | 13.98 | 0.04 | selected signal exited |
| 2026-11-03T20:46 | Agent (aggressive) | sell | LABU | 42.66 | -0.50 | selected signal exited |
| 2026-11-03T20:46 | Agent | sell | LABU | 17.87 | -0.21 | selected signal exited |
| 2026-11-03T20:41 | MFI reversion · 1h | buy | PLTR | 4.15 | — | rebalance up |
| 2026-11-03T20:30 | Agent (ML meta-label) | buy | GOOGL | 4.71 | — | rebalance up |
| 2026-11-03T20:30 | Agent (ML meta-label) | sell | BITX | 11.61 | -0.01 | selected signal exited |
| 2026-11-03T20:30 | Williams %R · 1h | sell | BITX | 6.41 | 0.01 | exit signal |
| 2026-11-03T20:30 | Stochastic reversion · 1h | sell | BITX | 7.07 | 0.01 | exit signal |
| 2026-11-03T20:30 | Candlestick reversal · 1h | buy | PLTR | 2.70 | — | entry signal |
| 2026-11-03T20:30 | Candlestick reversal · 1h | buy | GOOGL | 5.44 | — | entry signal |
| 2026-11-03T20:30 | Candlestick reversal · 1h | buy | BITX | 5.44 | — | entry signal |
| 2026-11-03T20:30 | Candlestick reversal · 1h | sell | UPRO | 4.72 | -0.02 | rebalance down |
| 2026-11-03T20:30 | ROC + volume · 1h | buy | XRP-USD | 4.87 | — | rebalance up |
| 2026-11-03T20:30 | ROC + volume · 1h | buy | SOL-USD | 4.95 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 20:55:05.000118+00:00 -> 2026-11-03 21:05:05.000118+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 20:55:05.000118+00:00 -> 2026-11-03 21:05:05.000118+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 20:55:05.000118+00:00 -> 2026-11-03 21:05:05.000118+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
