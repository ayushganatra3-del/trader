# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T21:25:05.000146+00:00 · 46565 ticks

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

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.74 · VIX 20.76 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 36939 decisions in 3087 calls, $0.4564 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T21:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-03T21:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T21:25 | 3 / 2 / 0 | ETH-USD 66% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.00 | 9.00 | 0 | — | 10.09 | 4.42 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.31 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 2.00 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.99 | -2.93 | -12.81 | 143 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.83 | -3.17 | 0 | — | -1.84 | -0.97 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.83 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.17 | 2.01 | -3.82 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.90 | -4.10 | 0 | — | -0.79 | -0.23 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.87 | -4.13 | 5 | 40.0 | 0.65 | 0.29 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.27 | -4.73 | 0 | — | -4.35 | -1.64 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.11 | -1.62 | -5.33 | 29 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.25 | -5.75 | 0 | — | -3.45 | -1.34 | -7.64 | 1 |
| 17 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.34 | -5.62 | -8.68 | 172 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -2.22 | -0.70 | -9.15 | 213 |
| 19 | Hold BTC | benchmark | 91.79 | -8.21 | 0 | — | 0.75 | 0.28 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.61 | -9.39 | 102 | 21.6 | -16.58 | -6.20 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.72 | -6.55 | -12.22 | 205 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.21 | -4.64 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 89.60 | -10.40 | 61 | 23.0 | -8.18 | -2.83 | -13.79 | 90 |
| 25 | Donchian 55/20 · 1h | breakout | 88.64 | -11.36 | 60 | 13.3 | -14.41 | -3.27 | -18.06 | 100 |
| 26 | Parabolic SAR · 1h | trend | 88.50 | -11.50 | 151 | 27.2 | -13.94 | -3.21 | -17.45 | 238 |
| 27 | Daily: Bullish score | daily | 88.48 | -11.52 | 14 | 21.4 | -7.60 | -1.06 | -14.82 | 15 |
| 28 | Copy: Insider buying | copy | 88.29 | -11.71 | 37 | 37.8 | -22.47 | -4.63 | -23.13 | 61 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.39 | -13.61 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.20 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.48 | -14.52 | 15 | 40.0 | -29.00 | -1.92 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.76 | -15.24 | 129 | 28.7 | -14.81 | -3.41 | -18.08 | 91 |
| 33 | Stochastic reversion · 1h | reversion | 84.64 | -15.37 | 242 | 47.1 | -23.25 | -4.71 | -25.31 | 387 |
| 34 | MFI reversion · 1h | reversion | 84.61 | -15.39 | 310 | 33.9 | -14.40 | -2.23 | -17.89 | 151 |
| 35 | Keltner breakout · 1h | breakout | 84.34 | -15.66 | 89 | 23.6 | -20.92 | -4.41 | -22.20 | 164 |
| 36 | Connors RSI(2) · 1h | reversion | 83.90 | -16.10 | 191 | 40.8 | -19.70 | -6.60 | -20.18 | 131 |
| 37 | ADX DI cross · 1h | trend | 83.16 | -16.84 | 150 | 18.0 | -19.48 | -3.82 | -21.89 | 255 |
| 38 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.77 | -20.73 | 716 |
| 39 | Bollinger breakout · 1h | breakout | 81.80 | -18.20 | 140 | 25.0 | -17.16 | -3.49 | -23.31 | 231 |
| 40 | Ichimoku · 1h | trend | 81.31 | -18.69 | 84 | 13.1 | -17.75 | -3.62 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 79.89 | -20.11 | 90 | 11.1 | -18.03 | -3.25 | -27.05 | 128 |
| 42 | CCI reversion · 1h | reversion | 78.95 | -21.05 | 268 | 44.8 | -24.99 | -3.89 | -27.71 | 450 |
| 43 | Bollinger reversion · 1h | reversion | 78.25 | -21.75 | 226 | 38.9 | -27.19 | -5.37 | -29.70 | 375 |
| 44 | MACD zero-line · 1h | trend | 78.11 | -21.89 | 136 | 15.4 | -25.11 | -5.59 | -27.55 | 213 |
| 45 | Supertrend · 1h | trend | 77.71 | -22.29 | 141 | 12.8 | -29.88 | -5.48 | -31.30 | 218 |
| 46 | Z-score reversion · 1h | reversion | 77.41 | -22.59 | 142 | 34.5 | -14.60 | -2.15 | -23.02 | 218 |
| 47 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.81 | -4.40 | -33.57 | 33 |
| 48 | MACD cross · 1h | trend | 77.02 | -22.98 | 301 | 23.6 | -32.19 | -6.33 | -34.56 | 484 |
| 49 | RSI momentum · 1h | momentum | 76.68 | -23.32 | 136 | 12.5 | -28.39 | -5.54 | -30.42 | 214 |
| 50 | Williams %R · 1h | reversion | 76.66 | -23.34 | 279 | 46.6 | -36.31 | -6.60 | -37.32 | 525 |
| 51 | Triple EMA stack · 1h | trend | 76.24 | -23.76 | 128 | 14.1 | -27.76 | -5.43 | -31.66 | 203 |
| 52 | Heikin-Ashi · 1h | trend | 75.61 | -24.39 | 370 | 22.7 | -40.80 | -8.82 | -43.46 | 666 |
| 53 | OBV trend · 1h | momentum | 75.60 | -24.40 | 242 | 17.4 | -29.26 | -6.28 | -31.40 | 291 |
| 54 | Donchian 20/10 · 1h | breakout | 75.52 | -24.48 | 120 | 20.0 | -27.48 | -5.05 | -30.44 | 205 |
| 55 | ROC + volume · 1h | momentum | 74.08 | -25.92 | 308 | 25.6 | -35.76 | -7.09 | -36.08 | 372 |
| 56 | RSI(14) reversion · 1h | reversion | 72.91 | -27.09 | 130 | 26.2 | -21.01 | -3.99 | -26.28 | 195 |
| 57 | Candlestick reversal · 1h | reversion | 70.76 | -29.24 | 361 | 28.5 | -33.74 | -6.44 | -37.04 | 542 |
| 58 | Agent (ML meta-label) | meta | 69.83 | -30.17 | 1372 | 21.8 | -13.58 | -2.65 | -18.69 | 284 |
| 59 | EMA 9/21 cross · 1h | trend | 69.25 | -30.75 | 219 | 9.6 | -37.52 | -7.66 | -39.23 | 329 |
| 60 | Max aggression: 1-day momentum | meta | 68.87 | -31.13 | 23 | 30.4 | -32.21 | -1.82 | -50.32 | 42 |
| 61 | Three white soldiers | momentum | 68.73 | -31.27 | 420 | 16.0 | -46.68 | -22.07 | -46.68 | 623 |
| 62 | VWAP momentum · 1h | momentum | 68.51 | -31.49 | 712 | 21.6 | -54.58 | -10.82 | -57.30 | 1230 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -44.04 | -98.93 | 5145 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.49 | -23.61 | -80.38 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -46.11 | -93.44 | 2520 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.69 | -30.52 | -89.07 | 1904 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.98 | -37.44 | -91.14 | 2322 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.73 | -33.04 | -90.83 | 2216 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -54.54 | -97.72 | 3470 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -59.98 | -96.31 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -34.35 | -93.55 | 2417 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.64 | -34.86 | -82.16 | 1665 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -56.35 | -99.48 | 5882 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -44.65 | -93.03 | 2624 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -38.53 | -95.38 | 3371 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -80.04 | -99.80 | 6183 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.80 | -45.64 | -91.82 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.66 | -26.64 | -75.08 | 1548 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -65.51 | -97.78 | 3522 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -65.24 | -98.68 | 4823 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.33 | -28.88 | -70.36 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -56.16 | -94.75 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.80 | -38.27 | -84.89 | 1796 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -74.90 | -99.61 | 6311 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.13 | -30.71 | -88.20 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.41 | -19.09 | -76.79 | 1695 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.18 | -38.38 | -90.19 | 2202 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -52.76 | -96.45 | 3817 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -57.09 | -89.42 | 2128 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.04 | -27.87 | -65.71 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.47 | -25.06 | -74.18 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.96 | -19.08 | -77.19 | 1597 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.84 | -52.76 | -96.85 | 4234 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.40 | -99.92 | 8209 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T21:20 | Three white soldiers | buy | SOL-USD | 17.20 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 21:25:05.000146+00:00 -> 2026-11-03 21:35:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 21:25:05.000146+00:00 -> 2026-11-03 21:35:05.000146+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 21:25:05.000146+00:00 -> 2026-11-03 21:35:05.000146+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
