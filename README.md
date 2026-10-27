# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T16:36:05.000076+00:00 · 38056 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 113, win rate 38.9%, fees £3.45, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.14 | +0.16 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 22939 decisions in 2441 calls, $0.2907 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T16:36 | 2 / 18 / 10 | cash |  |
| Breezy | 2026-10-27T16:36 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-27T16:36 | 6 / 20 / 4 | BITX 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.30 | +6.55% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.49 | 7.49 | 0 | — | 7.87 | 3.91 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.75 | 6.75 | 14 | 71.4 | 3.87 | 1.26 | -6.62 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.50 | 5.50 | 19 | 47.4 | 8.20 | 2.63 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.00 | 1.00 | 0 | — | 2.46 | 1.16 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.58 | -0.42 | 0 | — | 0.52 | 0.34 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.98 | -1.02 | 81 | 34.6 | 7.98 | 3.71 | -2.29 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.79 | -2.21 | 0 | — | 0.73 | 0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.02 | -1.90 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.42 | -3.58 | 122 | 31.1 | -2.20 | -1.24 | -6.39 | 180 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.02 | -3.98 | 0 | — | -5.80 | -2.36 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 95.73 | -4.26 | 0 | — | 2.23 | 0.54 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 5.06 | 1.18 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.46 | -4.54 | 112 | 25.9 | 5.35 | 1.74 | -8.76 | 210 |
| 20 | Opening range 30m | breakout | 93.71 | -6.29 | 272 | 34.2 | -9.62 | -2.85 | -17.21 | 593 |
| 21 | Trend pullback · 1h | trend | 93.59 | -6.41 | 96 | 22.9 | -21.86 | -6.97 | -22.19 | 116 |
| 22 | Donchian 55/20 · 1h | breakout | 93.47 | -6.53 | 49 | 16.3 | -13.12 | -2.96 | -15.45 | 97 |
| 23 | Copy: Insider buying | copy | 92.90 | -7.10 | 27 | 37.0 | -19.17 | -3.71 | -22.94 | 63 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.44 | -7.56 | 0 | — | -1.35 | -0.05 | -14.57 | 1 |
| 25 | Parabolic SAR · 1h | trend | 92.03 | -7.97 | 121 | 25.6 | -20.47 | -5.06 | -23.02 | 247 |
| 26 | Daily: Momentum burst | daily | 91.83 | -8.18 | 13 | 15.4 | -17.78 | -3.42 | -19.44 | 39 |
| 27 | ADX DI cross · 1h | trend | 91.79 | -8.21 | 119 | 18.5 | -10.95 | -2.32 | -14.45 | 274 |
| 28 | Daily: Bullish score | daily | 91.45 | -8.55 | 11 | 18.2 | -5.69 | -0.65 | -14.40 | 14 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.86 | -2.07 | -16.91 | 1 |
| 30 | Squeeze breakout · 1h | breakout | 91.15 | -8.85 | 52 | 23.1 | -4.83 | -1.23 | -12.00 | 93 |
| 31 | Max aggression: 5-day momentum | meta | 90.81 | -9.19 | 12 | 41.7 | -14.70 | -1.32 | -27.23 | 25 |
| 32 | Volume breakout · 1h | breakout | 90.30 | -9.70 | 105 | 23.8 | -11.82 | -2.42 | -16.00 | 115 |
| 33 | Agent | meta | 90.11 | -9.89 | 113 | 38.9 | -11.23 | -7.04 | -12.47 | 221 |
| 34 | Bollinger breakout · 1h | breakout | 88.85 | -11.15 | 109 | 26.6 | -12.90 | -2.54 | -18.15 | 249 |
| 35 | Agent (aggressive) | meta | 88.35 | -11.65 | 56 | 35.7 | -10.41 | -3.41 | -14.77 | 96 |
| 36 | Stochastic reversion · 1h | reversion | 87.98 | -12.02 | 205 | 47.3 | -21.32 | -3.93 | -22.71 | 394 |
| 37 | Opening range 15m | breakout | 87.18 | -12.82 | 338 | 30.8 | -13.39 | -3.70 | -17.87 | 719 |
| 38 | Keltner breakout · 1h | breakout | 87.14 | -12.87 | 74 | 23.0 | -21.70 | -4.34 | -23.28 | 189 |
| 39 | Z-score reversion · 1h | reversion | 86.82 | -13.18 | 125 | 36.0 | -12.60 | -1.99 | -21.48 | 211 |
| 40 | Supertrend · 1h | trend | 85.75 | -14.25 | 114 | 14.0 | -25.47 | -5.16 | -28.20 | 230 |
| 41 | Connors RSI(2) · 1h | reversion | 85.11 | -14.89 | 176 | 40.9 | -24.54 | -7.48 | -24.99 | 197 |
| 42 | RSI momentum · 1h | momentum | 85.03 | -14.97 | 104 | 15.4 | -21.40 | -4.33 | -24.34 | 209 |
| 43 | MACD cross · 1h | trend | 84.41 | -15.59 | 244 | 22.1 | -28.40 | -5.32 | -30.42 | 473 |
| 44 | EMA 20/50 cross · 1h | trend | 84.15 | -15.85 | 73 | 11.0 | -22.50 | -4.57 | -24.37 | 133 |
| 45 | Ichimoku · 1h | trend | 83.76 | -16.24 | 68 | 11.8 | -20.13 | -4.12 | -24.73 | 111 |
| 46 | MFI reversion · 1h | reversion | 83.63 | -16.37 | 271 | 32.5 | -16.08 | -2.48 | -20.70 | 153 |
| 47 | Triple EMA stack · 1h | trend | 83.38 | -16.62 | 101 | 14.9 | -28.58 | -5.46 | -31.33 | 203 |
| 48 | CCI reversion · 1h | reversion | 82.53 | -17.48 | 230 | 45.2 | -23.30 | -3.30 | -28.08 | 465 |
| 49 | Williams %R · 1h | reversion | 82.08 | -17.92 | 232 | 47.0 | -35.10 | -5.93 | -36.14 | 535 |
| 50 | Donchian 20/10 · 1h | breakout | 81.91 | -18.09 | 99 | 20.2 | -24.24 | -4.63 | -26.89 | 222 |
| 51 | MACD zero-line · 1h | trend | 81.31 | -18.69 | 111 | 15.3 | -23.82 | -5.10 | -25.57 | 230 |
| 52 | Bollinger reversion · 1h | reversion | 80.94 | -19.06 | 182 | 37.4 | -29.20 | -5.93 | -30.48 | 365 |
| 53 | Agent (ML meta-label) | meta | 80.89 | -19.11 | 963 | 20.8 | -8.08 | -1.48 | -18.07 | 332 |
| 54 | RSI(14) reversion · 1h | reversion | 80.34 | -19.66 | 107 | 27.1 | -18.38 | -3.48 | -24.48 | 188 |
| 55 | OBV trend · 1h | momentum | 80.23 | -19.77 | 209 | 17.7 | -30.93 | -6.59 | -32.72 | 297 |
| 56 | ROC + volume · 1h | momentum | 79.10 | -20.90 | 259 | 25.9 | -31.16 | -6.06 | -33.27 | 386 |
| 57 | Heikin-Ashi · 1h | trend | 78.32 | -21.68 | 295 | 22.7 | -43.26 | -9.52 | -44.65 | 667 |
| 58 | Candlestick reversal · 1h | reversion | 77.47 | -22.53 | 282 | 29.4 | -33.30 | -6.38 | -34.35 | 558 |
| 59 | Three white soldiers | momentum | 77.35 | -22.65 | 321 | 19.0 | -44.55 | -20.14 | -45.08 | 607 |
| 60 | VWAP momentum · 1h | momentum | 76.97 | -23.03 | 567 | 21.9 | -48.53 | -10.38 | -50.71 | 1242 |
| 61 | EMA 9/21 cross · 1h | trend | 76.65 | -23.35 | 176 | 10.8 | -30.77 | -6.62 | -32.69 | 338 |
| 62 | Max aggression: 1-day momentum | meta | 71.82 | -28.18 | 20 | 30.0 | -38.23 | -2.50 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.28 | -45.72 | 792 | 22.3 | -74.47 | -26.38 | -75.11 | 1592 |
| 64 | Volume breakout | breakout | 52.73 | -47.27 | 480 | 12.7 | -63.13 | -26.05 | -63.64 | 814 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -42.08 | -98.87 | 5149 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.15 | -23.06 | -79.95 | 1417 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.55 | -41.51 | -93.78 | 2531 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.19 | -30.18 | -89.36 | 1924 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -35.92 | -91.55 | 2343 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.39 | -31.73 | -90.49 | 2169 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -48.66 | -97.89 | 3508 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.06 | -50.71 | -96.20 | 3389 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -35.67 | -94.07 | 2454 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.10 | -30.95 | -82.79 | 1696 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.18 | -99.43 | 5766 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -41.29 | -92.92 | 2645 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.42 | -38.37 | -95.42 | 3371 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -70.80 | -99.78 | 6166 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.32 | -44.86 | -92.35 | 2322 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -58.92 | -97.76 | 3582 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.81 | -98.67 | 4792 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.68 | -28.30 | -68.58 | 1179 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.54 | -53.63 | -94.63 | 2782 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.24 | -37.81 | -84.56 | 1834 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.11 | -99.61 | 6282 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.23 | -28.61 | -88.27 | 2229 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.91 | -19.07 | -77.13 | 1694 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.52 | -36.28 | -90.65 | 2276 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -46.91 | -96.28 | 3820 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.04 | -47.97 | -90.09 | 2138 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.47 | -23.51 | -73.41 | 1292 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.19 | -17.92 | -76.40 | 1581 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.41 | -96.55 | 4190 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.50 | -99.92 | 8304 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T16:35 | Agent (ML meta-label) | buy | TSLA | 8.05 | — | following Z-score reversion |
| 2026-10-27T16:35 | Agent (ML meta-label) | buy | QQQ | 13.49 | — | entry |
| 2026-10-27T16:35 | Agent (ML meta-label) | buy | MSFT | 13.49 | — | following MACD zero-line |
| 2026-10-27T16:35 | Agent (ML meta-label) | buy | AMD | 13.49 | — | entry |
| 2026-10-27T16:35 | Agent (ML meta-label) | sell | IWM | 20.23 | -0.02 | selected signal exited |
| 2026-10-27T16:35 | Three white soldiers | sell | LABU | 19.23 | 0.01 | target is flat |
| 2026-10-27T16:35 | Volume breakout | sell | QQQ | 10.58 | 0.01 | exit signal |
| 2026-10-27T16:35 | Volume breakout | sell | PLTR | 13.16 | -0.06 | exit signal |
| 2026-10-27T16:35 | Volume breakout | sell | LABU | 13.15 | -0.11 | target is flat |
| 2026-10-27T16:30 | MFI reversion · 1h | sell | GOOGL | 20.97 | 0.15 | exit signal |
| 2026-10-27T16:30 | Williams %R · 1h | buy | META | 6.39 | — | rebalance up |
| 2026-10-27T16:30 | Williams %R · 1h | buy | ETHU | 6.00 | — | rebalance up |
| 2026-10-27T16:30 | Williams %R · 1h | buy | COIN | 6.14 | — | rebalance up |
| 2026-10-27T16:30 | Williams %R · 1h | buy | BITX | 6.15 | — | rebalance up |
| 2026-10-27T16:30 | Williams %R · 1h | sell | GOOGL | 10.26 | 0.07 | exit signal |
| 2026-10-27T16:30 | Stochastic reversion · 1h | sell | GOOGL | 17.77 | 0.16 | exit signal |
| 2026-10-27T16:30 | Bollinger reversion · 1h | buy | META | 20.24 | — | entry signal |
| 2026-10-27T16:30 | RSI(14) reversion · 1h | buy | GOOGL | 4.10 | — | rebalance up |
| 2026-10-27T16:30 | RSI(14) reversion · 1h | buy | COIN | 4.16 | — | rebalance up |
| 2026-10-27T16:30 | RSI(14) reversion · 1h | sell | AMZN | 16.12 | 0.28 | exit signal |
| 2026-10-27T16:30 | Squeeze breakout · 1h | buy | PLTR | 22.81 | — | entry signal |
| 2026-10-27T16:30 | Keltner breakout · 1h | buy | TQQQ | 10.88 | — | entry signal |
| 2026-10-27T16:30 | Keltner breakout · 1h | buy | TNA | 10.91 | — | entry signal |
| 2026-10-27T16:30 | Keltner breakout · 1h | buy | QQQ | 10.91 | — | entry signal |
| 2026-10-27T16:30 | Keltner breakout · 1h | buy | IWM | 10.91 | — | entry signal |
| 2026-10-27T16:30 | Keltner breakout · 1h | sell | TSLA | 11.13 | 0.29 | rebalance down |
| 2026-10-27T16:30 | Keltner breakout · 1h | sell | TECL | 10.47 | 0.09 | rebalance down |
| 2026-10-27T16:30 | Keltner breakout · 1h | sell | SOXL | 11.08 | 0.18 | rebalance down |
| 2026-10-27T16:30 | Keltner breakout · 1h | sell | AMD | 10.92 | 0.13 | rebalance down |
| 2026-10-27T16:30 | RSI momentum · 1h | buy | UPRO | 5.68 | — | entry signal |
| 2026-10-27T16:30 | RSI momentum · 1h | buy | TQQQ | 5.68 | — | entry |
| 2026-10-27T16:30 | RSI momentum · 1h | buy | SPY | 5.68 | — | entry |
| 2026-10-27T16:30 | RSI momentum · 1h | buy | QQQ | 5.68 | — | entry |
| 2026-10-27T16:30 | RSI momentum · 1h | buy | NVDA | 5.68 | — | entry signal |
| 2026-10-27T16:30 | RSI momentum · 1h | buy | LABU | 5.68 | — | entry |
| 2026-10-27T16:30 | RSI momentum · 1h | sell | XRP-USD | 4.83 | -0.00 | rebalance down |
| 2026-10-27T16:30 | RSI momentum · 1h | sell | TSLA | 4.92 | 0.13 | rebalance down |
| 2026-10-27T16:30 | RSI momentum · 1h | sell | TNA | 5.06 | 0.10 | rebalance down |
| 2026-10-27T16:30 | RSI momentum · 1h | sell | PLTR | 5.01 | 0.04 | rebalance down |
| 2026-10-27T16:30 | RSI momentum · 1h | sell | MSFT | 4.88 | 0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 16:36:05.000076+00:00 -> 2026-10-27 16:46:05.000076+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
