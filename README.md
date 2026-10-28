# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T05:59:05.000133+00:00 · 38724 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 116, win rate 38.8%, fees £3.50, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 4527 decisions in 906 calls, $0.0633 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T05:59 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-28T05:59 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T05:59 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| VWAP momentum · 1h | LABU | 2.05 | +21.96% | 3 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.23 | 7.23 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.23 | 1.23 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.19 | -3.65 | -14.07 | 148 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.69 | -0.31 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.46 | 3.49 | -2.42 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.84 | -2.16 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.42 | -3.58 | 123 | 31.7 | -2.82 | -1.43 | -7.67 | 188 |
| 15 | Hold BTC | benchmark | 96.17 | -3.83 | 0 | — | 2.19 | 0.53 | -9.28 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.12 | -3.88 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.18 | 1.69 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.84 | -6.17 | 49 | 16.3 | -12.94 | -2.87 | -15.40 | 99 |
| 22 | Trend pullback · 1h | trend | 93.50 | -6.50 | 96 | 22.9 | -20.73 | -6.86 | -20.95 | 109 |
| 23 | Parabolic SAR · 1h | trend | 92.79 | -7.21 | 121 | 25.6 | -19.91 | -4.84 | -22.91 | 247 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.69 | -7.32 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 25 | ADX DI cross · 1h | trend | 92.17 | -7.83 | 120 | 18.3 | -13.99 | -3.01 | -15.89 | 271 |
| 26 | Daily: Momentum burst | daily | 92.03 | -7.97 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 91.94 | -8.06 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.42 | -8.58 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.34 | -8.66 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 91.15 | -8.85 | 52 | 23.1 | -4.45 | -1.16 | -12.21 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.36 | -9.64 | 112 | 26.8 | -12.75 | -2.65 | -16.02 | 105 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.02 | -6.38 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 89.08 | -10.92 | 109 | 26.6 | -11.24 | -2.17 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.94 | -12.06 | 205 | 47.3 | -20.83 | -3.84 | -22.35 | 389 |
| 37 | Keltner breakout · 1h | breakout | 87.42 | -12.58 | 74 | 23.0 | -18.85 | -3.61 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.07 | -12.94 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 85.99 | -14.01 | 114 | 14.0 | -23.68 | -4.78 | -26.59 | 232 |
| 41 | RSI momentum · 1h | momentum | 85.25 | -14.75 | 104 | 15.4 | -24.00 | -4.77 | -26.87 | 212 |
| 42 | Connors RSI(2) · 1h | reversion | 85.17 | -14.83 | 176 | 40.9 | -23.72 | -7.42 | -24.36 | 179 |
| 43 | EMA 20/50 cross · 1h | trend | 84.71 | -15.29 | 73 | 11.0 | -22.60 | -4.58 | -24.49 | 137 |
| 44 | MACD cross · 1h | trend | 84.51 | -15.49 | 244 | 22.1 | -27.57 | -5.34 | -29.94 | 476 |
| 45 | Ichimoku · 1h | trend | 84.21 | -15.79 | 68 | 11.8 | -19.72 | -3.99 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.84 | -16.16 | 101 | 14.9 | -28.13 | -5.33 | -31.19 | 205 |
| 47 | MFI reversion · 1h | reversion | 83.54 | -16.46 | 274 | 32.1 | -16.01 | -2.46 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.68 | -17.32 | 230 | 45.2 | -24.22 | -3.45 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.30 | -17.70 | 99 | 20.2 | -22.88 | -4.31 | -26.02 | 219 |
| 50 | Williams %R · 1h | reversion | 82.23 | -17.77 | 232 | 47.0 | -34.64 | -5.85 | -35.74 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.47 | -18.53 | 111 | 15.3 | -24.16 | -5.17 | -25.67 | 230 |
| 52 | Agent (ML meta-label) | meta | 80.93 | -19.07 | 982 | 20.6 | -7.58 | -1.29 | -18.48 | 352 |
| 53 | Bollinger reversion · 1h | reversion | 80.90 | -19.10 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.83 | -19.17 | 209 | 17.7 | -31.39 | -6.44 | -33.78 | 295 |
| 55 | RSI(14) reversion · 1h | reversion | 80.49 | -19.50 | 107 | 27.1 | -15.03 | -2.76 | -24.48 | 188 |
| 56 | ROC + volume · 1h | momentum | 79.45 | -20.55 | 259 | 25.9 | -29.65 | -5.59 | -32.05 | 379 |
| 57 | Heikin-Ashi · 1h | trend | 78.50 | -21.50 | 302 | 22.5 | -42.61 | -9.30 | -43.95 | 663 |
| 58 | Candlestick reversal · 1h | reversion | 77.50 | -22.50 | 285 | 29.5 | -38.93 | -7.71 | -39.69 | 553 |
| 59 | VWAP momentum · 1h | momentum | 77.15 | -22.85 | 579 | 22.6 | -49.78 | -10.89 | -50.91 | 1237 |
| 60 | EMA 9/21 cross · 1h | trend | 76.94 | -23.06 | 176 | 10.8 | -29.56 | -6.23 | -31.61 | 337 |
| 61 | Three white soldiers | momentum | 76.82 | -23.18 | 327 | 19.0 | -45.00 | -21.03 | -45.16 | 608 |
| 62 | Max aggression: 1-day momentum | meta | 72.66 | -27.34 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 52.59 | -47.41 | 821 | 22.0 | -75.02 | -27.09 | -75.34 | 1572 |
| 64 | Volume breakout | breakout | 51.29 | -48.71 | 496 | 12.5 | -64.21 | -26.17 | -64.71 | 812 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -43.03 | -98.86 | 5116 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.13 | -23.38 | -79.62 | 1411 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.69 | -45.38 | -93.69 | 2531 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.09 | -29.92 | -89.27 | 1917 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.57 | -37.83 | -91.61 | 2341 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -32.05 | -90.48 | 2201 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.84 | -51.46 | -97.87 | 3502 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -59.06 | -96.22 | 3390 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.12 | -36.94 | -94.12 | 2470 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.45 | -34.20 | -82.52 | 1692 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.53 | -99.42 | 5751 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.02 | -42.75 | -93.18 | 2640 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.39 | -38.43 | -95.39 | 3387 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -74.30 | -99.78 | 6174 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.35 | -44.29 | -92.45 | 2311 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -64.74 | -97.82 | 3592 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -57.04 | -98.65 | 4786 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.98 | -29.72 | -69.32 | 1188 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -55.79 | -94.81 | 2781 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -39.27 | -84.86 | 1817 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.58 | -99.61 | 6290 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.61 | -88.27 | 2222 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.38 | -18.71 | -76.79 | 1679 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.53 | -36.47 | -90.53 | 2264 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -46.51 | -96.25 | 3809 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.06 | -48.51 | -90.06 | 2130 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.25 | -24.88 | -73.50 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.24 | -17.96 | -76.49 | 1574 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.33 | -96.54 | 4191 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -99.82 | -99.92 | 8288 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T05:01 | VWAP momentum · 1h | sell | XRP-USD | 4.01 | -0.05 | exit signal |
| 2026-10-28T05:01 | Heikin-Ashi · 1h | sell | ETH-USD | 4.87 | -0.04 | exit signal |
| 2026-10-28T04:25 | ROC + volume | sell | DOGE-USD | 13.07 | -0.15 | stop-loss |
| 2026-10-28T04:10 | ROC + volume | sell | SOL-USD | 13.09 | -0.12 | stop-loss |
| 2026-10-28T04:00 | Heikin-Ashi · 1h | buy | ETH-USD | 4.91 | — | entry signal |
| 2026-10-28T03:55 | Volume breakout | sell | SOL-USD | 12.74 | -0.11 | exit signal |
| 2026-10-28T03:35 | Volume breakout | buy | SOL-USD | 12.85 | — | entry signal |
| 2026-10-28T03:35 | ROC + volume | buy | SOL-USD | 13.22 | — | entry signal |
| 2026-10-28T03:35 | ROC + volume | buy | DOGE-USD | 13.22 | — | entry signal |
| 2026-10-28T03:15 | ROC + volume | sell | ETH-USD | 13.20 | -0.09 | exit signal |
| 2026-10-28T02:45 | ROC + volume | sell | XRP-USD | 13.19 | -0.10 | stop-loss |
| 2026-10-28T02:45 | ROC + volume | sell | SOL-USD | 13.18 | -0.11 | exit signal |
| 2026-10-28T02:30 | Three white soldiers | sell | XRP-USD | 19.13 | -0.10 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | XRP-USD | 12.88 | -0.07 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | SOL-USD | 12.83 | -0.12 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | ETH-USD | 12.83 | -0.12 | exit signal |
| 2026-10-28T02:30 | Volume breakout | sell | BTC-USD | 12.85 | -0.09 | exit signal |
| 2026-10-28T02:20 | Volume breakout | buy | SOL-USD | 12.94 | — | entry signal |
| 2026-10-28T02:20 | Volume breakout | buy | ETH-USD | 12.94 | — | entry signal |
| 2026-10-28T02:20 | ROC + volume | buy | SOL-USD | 13.30 | — | entry signal |
| 2026-10-28T02:15 | Volume breakout | buy | BTC-USD | 12.94 | — | entry signal |
| 2026-10-28T02:15 | ROC + volume | buy | ETH-USD | 13.29 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | XRP-USD | 4.06 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | ETH-USD | 4.06 | — | entry signal |
| 2026-10-28T02:00 | VWAP momentum · 1h | buy | BTC-USD | 4.06 | — | entry signal |
| 2026-10-28T01:45 | Volume breakout · 1h | buy | ETH-USD | 9.63 | — | rebalance up |
| 2026-10-28T01:45 | Three white soldiers | buy | XRP-USD | 19.23 | — | entry signal |
| 2026-10-28T01:45 | Volume breakout | buy | XRP-USD | 12.95 | — | entry signal |
| 2026-10-28T01:45 | ROC + volume | buy | XRP-USD | 13.29 | — | entry signal |
| 2026-10-28T01:15 | Volume breakout · 1h | buy | ETH-USD | 5.39 | — | rebalance up |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | XRP-USD | 6.47 | 0.09 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | ETH-USD | 5.45 | 0.02 | exit signal |
| 2026-10-28T01:00 | VWAP momentum · 1h | sell | BTC-USD | 2.95 | 0.01 | exit signal |
| 2026-10-28T01:00 | Heikin-Ashi · 1h | sell | BTC-USD | 3.90 | -0.02 | exit signal |
| 2026-10-28T00:20 | ROC + volume | sell | DOGE-USD | 13.22 | -0.14 | stop-loss |
| 2026-10-28T00:05 | ROC + volume | sell | XRP-USD | 13.22 | -0.14 | stop-loss |
| 2026-10-28T00:00 | Donchian 55/20 · 1h | buy | XRP-USD | 3.96 | — | entry signal |
| 2026-10-28T00:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 18.74 | — | entry signal |
| 2026-10-27T23:50 | ROC + volume | buy | XRP-USD | 13.36 | — | entry signal |
| 2026-10-27T23:50 | ROC + volume | buy | DOGE-USD | 13.36 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 05:59:05.000133+00:00 -> 2026-10-28 06:09:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
