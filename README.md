# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T23:55:05.000223+00:00 · 46676 ticks

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
| Copy: Insider buying | 2026-11-03 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.74 · VIX 20.76 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38604 decisions in 3420 calls, $0.4796 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T23:55 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-03T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T23:55 | 2 / 3 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.08 | 9.08 | 0 | — | 10.13 | 4.47 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.31 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 2.00 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.33 | -3.03 | -13.06 | 141 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.87 | -3.13 | 0 | — | -1.84 | -0.97 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.83 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.78 | 2.33 | -3.26 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.93 | -4.07 | 0 | — | -0.79 | -0.23 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.91 | -4.09 | 5 | 40.0 | 0.63 | 0.28 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.31 | -4.69 | 0 | — | -4.35 | -1.64 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.60 | -3.39 | -5.33 | 28 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.27 | -5.73 | 0 | — | -3.46 | -1.34 | -7.64 | 1 |
| 17 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.71 | -5.80 | -8.61 | 171 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -1.75 | -0.54 | -8.78 | 213 |
| 19 | Hold BTC | benchmark | 91.55 | -8.45 | 0 | — | 0.40 | 0.24 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.62 | -9.38 | 102 | 21.6 | -16.58 | -6.20 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.72 | -6.55 | -12.22 | 205 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.22 | -4.65 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 89.29 | -10.71 | 61 | 23.0 | -9.00 | -3.15 | -13.79 | 89 |
| 25 | Donchian 55/20 · 1h | breakout | 88.58 | -11.42 | 60 | 13.3 | -14.49 | -3.29 | -18.06 | 100 |
| 26 | Daily: Bullish score | daily | 88.49 | -11.51 | 14 | 21.4 | -7.60 | -1.06 | -14.82 | 15 |
| 27 | Parabolic SAR · 1h | trend | 88.37 | -11.63 | 151 | 27.2 | -14.12 | -3.26 | -17.47 | 238 |
| 28 | Copy: Insider buying | copy | 88.32 | -11.68 | 37 | 37.8 | -22.47 | -4.63 | -23.13 | 61 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.42 | -13.58 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.20 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.51 | -14.49 | 15 | 40.0 | -29.00 | -1.92 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.69 | -15.31 | 129 | 28.7 | -15.19 | -3.50 | -18.37 | 92 |
| 33 | Stochastic reversion · 1h | reversion | 84.66 | -15.34 | 242 | 47.1 | -23.25 | -4.71 | -25.31 | 387 |
| 34 | MFI reversion · 1h | reversion | 84.52 | -15.48 | 310 | 33.9 | -15.23 | -2.41 | -17.89 | 151 |
| 35 | Keltner breakout · 1h | breakout | 84.28 | -15.72 | 89 | 23.6 | -20.99 | -4.43 | -22.20 | 164 |
| 36 | Connors RSI(2) · 1h | reversion | 83.91 | -16.09 | 191 | 40.8 | -19.70 | -6.60 | -20.18 | 131 |
| 37 | ADX DI cross · 1h | trend | 83.10 | -16.90 | 150 | 18.0 | -19.45 | -3.79 | -21.89 | 256 |
| 38 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.77 | -20.73 | 716 |
| 39 | Bollinger breakout · 1h | breakout | 81.50 | -18.50 | 140 | 25.0 | -17.48 | -3.57 | -23.31 | 231 |
| 40 | Ichimoku · 1h | trend | 81.32 | -18.68 | 84 | 13.1 | -17.75 | -3.62 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 79.71 | -20.29 | 90 | 11.1 | -17.74 | -3.16 | -27.05 | 130 |
| 42 | CCI reversion · 1h | reversion | 78.97 | -21.03 | 268 | 44.8 | -24.99 | -3.89 | -27.71 | 450 |
| 43 | Bollinger reversion · 1h | reversion | 78.28 | -21.72 | 226 | 38.9 | -27.19 | -5.37 | -29.70 | 375 |
| 44 | MACD zero-line · 1h | trend | 77.86 | -22.14 | 136 | 15.4 | -25.35 | -5.67 | -27.55 | 213 |
| 45 | Supertrend · 1h | trend | 77.66 | -22.34 | 141 | 12.8 | -29.95 | -5.50 | -31.30 | 218 |
| 46 | Z-score reversion · 1h | reversion | 77.43 | -22.57 | 142 | 34.5 | -14.60 | -2.15 | -23.02 | 218 |
| 47 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.80 | -4.40 | -33.56 | 33 |
| 48 | MACD cross · 1h | trend | 76.96 | -23.04 | 301 | 23.6 | -32.25 | -6.35 | -34.56 | 484 |
| 49 | Williams %R · 1h | reversion | 76.68 | -23.32 | 279 | 46.6 | -36.31 | -6.60 | -37.32 | 525 |
| 50 | RSI momentum · 1h | momentum | 76.51 | -23.49 | 136 | 12.5 | -28.62 | -5.59 | -30.42 | 214 |
| 51 | Triple EMA stack · 1h | trend | 76.10 | -23.90 | 128 | 14.1 | -27.91 | -5.46 | -31.66 | 203 |
| 52 | Heikin-Ashi · 1h | trend | 75.63 | -24.37 | 370 | 22.7 | -40.81 | -8.82 | -43.46 | 666 |
| 53 | OBV trend · 1h | momentum | 75.50 | -24.50 | 242 | 17.4 | -29.61 | -6.37 | -31.52 | 293 |
| 54 | Donchian 20/10 · 1h | breakout | 75.26 | -24.74 | 120 | 20.0 | -27.70 | -5.10 | -30.44 | 205 |
| 55 | ROC + volume · 1h | momentum | 73.87 | -26.13 | 308 | 25.6 | -35.11 | -6.94 | -35.67 | 374 |
| 56 | RSI(14) reversion · 1h | reversion | 72.93 | -27.07 | 130 | 26.2 | -21.50 | -4.10 | -26.28 | 197 |
| 57 | Candlestick reversal · 1h | reversion | 70.79 | -29.21 | 361 | 28.5 | -33.90 | -6.50 | -37.05 | 542 |
| 58 | Agent (ML meta-label) | meta | 69.86 | -30.14 | 1372 | 21.8 | -11.07 | -2.26 | -16.44 | 261 |
| 59 | EMA 9/21 cross · 1h | trend | 69.11 | -30.89 | 219 | 9.6 | -37.67 | -7.70 | -39.23 | 329 |
| 60 | Max aggression: 1-day momentum | meta | 68.90 | -31.10 | 23 | 30.4 | -32.21 | -1.82 | -50.32 | 42 |
| 61 | VWAP momentum · 1h | momentum | 68.43 | -31.57 | 712 | 21.6 | -56.18 | -12.15 | -56.35 | 1225 |
| 62 | Three white soldiers | momentum | 68.41 | -31.59 | 423 | 15.8 | -46.86 | -21.99 | -46.86 | 624 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -43.67 | -98.92 | 5140 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.63 | -23.75 | -80.47 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -45.95 | -93.51 | 2520 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.73 | -30.28 | -89.16 | 1900 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.99 | -36.94 | -91.20 | 2318 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.94 | -33.07 | -90.98 | 2223 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -53.75 | -97.75 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -58.24 | -96.31 | 3375 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.65 | -33.60 | -93.70 | 2427 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.69 | -34.59 | -82.24 | 1661 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -56.34 | -99.48 | 5875 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -44.02 | -93.07 | 2619 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -38.87 | -95.43 | 3381 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -78.45 | -99.80 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -44.93 | -91.83 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.75 | -26.88 | -75.04 | 1552 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -64.63 | -97.79 | 3524 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -65.37 | -98.69 | 4823 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.47 | -28.80 | -70.45 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.55 | -94.79 | 2778 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.66 | -37.56 | -84.96 | 1790 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -74.96 | -99.61 | 6310 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.14 | -30.75 | -88.20 | 2240 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.32 | -19.08 | -76.72 | 1690 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.38 | -37.74 | -90.41 | 2246 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.46 | -52.93 | -96.46 | 3819 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -57.27 | -89.41 | 2126 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.16 | -27.59 | -65.71 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.25 | -24.31 | -74.26 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.91 | -19.10 | -77.15 | 1606 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.87 | -53.12 | -96.87 | 4236 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.20 | -99.92 | 8200 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T23:10 | Three white soldiers | sell | DOGE-USD | 17.03 | -0.13 | target is flat |
| 2026-11-03T23:05 | Three white soldiers | sell | ETH-USD | 17.04 | -0.12 | exit signal |
| 2026-11-03T23:01 | EMA 20/50 cross · 1h | buy | DOGE-USD | 4.05 | — | entry signal |
| 2026-11-03T23:01 | EMA 20/50 cross · 1h | sell | XRP-USD | 4.05 | 0.05 | rebalance down |
| 2026-11-03T23:01 | Three white soldiers | buy | DOGE-USD | 17.15 | — | entry signal |
| 2026-11-03T22:45 | Three white soldiers | buy | ETH-USD | 17.16 | — | entry signal |
| 2026-11-03T22:10 | MFI reversion · 1h | sell | DOGE-USD | 7.09 | 0.00 | rebalance down |
| 2026-11-03T22:10 | MFI reversion · 1h | sell | BTC-USD | 7.00 | -0.01 | rebalance down |
| 2026-11-03T21:50 | Three white soldiers | sell | SOL-USD | 17.06 | -0.14 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 23:55:05.000223+00:00 -> 2026-11-04 00:05:05.000223+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 23:55:05.000223+00:00 -> 2026-11-04 00:05:05.000223+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 23:55:05.000223+00:00 -> 2026-11-04 00:05:05.000223+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
