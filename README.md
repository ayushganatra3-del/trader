# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T05:25:05.000116+00:00 · 29162 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 3945 decisions in 789 calls, $0.0552 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T05:25 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-20T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T05:25 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.84 | +3.15% | 6 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.86 | 4.86 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.76 | -0.24 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.01 | -0.99 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.69 | -2.17 | 63 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.14 | -1.86 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.16 | -0.91 | -5.85 | 293 |
| 14 | Donchian 55/20 · 1h | breakout | 97.37 | -2.63 | 37 | 16.2 | -11.32 | -2.11 | -19.38 | 97 |
| 15 | Hold BTC | benchmark | 97.22 | -2.78 | 0 | — | 27.14 | 3.19 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.21 | -2.79 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 18 | Trend pullback · 1h | trend | 96.38 | -3.62 | 88 | 23.9 | -19.92 | -5.87 | -20.80 | 136 |
| 19 | Copy: Insider buying | copy | 96.31 | -3.69 | 23 | 43.5 | -11.55 | -1.97 | -20.62 | 70 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.24 | -3.76 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.28 | -4.72 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.54 | 2.17 | -6.51 | 199 |
| 24 | ADX DI cross · 1h | trend | 93.50 | -6.50 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.83 | -7.17 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 91.90 | -8.10 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.86 | -8.14 | 78 | 23.1 | -12.55 | -2.25 | -16.37 | 101 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 30 | Parabolic SAR · 1h | trend | 91.13 | -8.87 | 104 | 22.1 | -17.03 | -3.58 | -23.28 | 271 |
| 31 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 32 | Bollinger breakout · 1h | breakout | 90.75 | -9.25 | 84 | 28.6 | -9.11 | -1.54 | -16.89 | 253 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -16.12 | -6.07 | -20.42 | 281 |
| 34 | EMA 20/50 cross · 1h | trend | 90.11 | -9.88 | 59 | 13.6 | -19.23 | -3.44 | -21.31 | 127 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 89.96 | -10.04 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.65 | -10.35 | 80 | 16.2 | -20.35 | -3.48 | -30.28 | 212 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 38 | Ichimoku · 1h | trend | 88.59 | -11.41 | 56 | 14.3 | -17.63 | -3.33 | -18.10 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.16 | -11.84 | 152 | 46.1 | -17.09 | -2.96 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -17.44 | -4.00 | -23.55 | 137 |
| 41 | Keltner breakout · 1h | breakout | 87.69 | -12.31 | 56 | 23.2 | -11.96 | -1.67 | -26.96 | 201 |
| 42 | Supertrend · 1h | trend | 87.32 | -12.68 | 87 | 12.6 | -22.82 | -4.67 | -26.61 | 214 |
| 43 | Triple EMA stack · 1h | trend | 87.23 | -12.77 | 86 | 15.1 | -24.47 | -3.95 | -32.98 | 233 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 85.88 | -14.12 | 189 | 20.6 | -28.39 | -5.55 | -32.82 | 470 |
| 46 | OBV trend · 1h | momentum | 85.29 | -14.71 | 180 | 17.8 | -27.53 | -4.30 | -36.29 | 317 |
| 47 | Z-score reversion · 1h | reversion | 85.08 | -14.92 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.61 | -15.39 | 209 | 31.1 | -17.07 | -2.66 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.20 | -15.80 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Donchian 20/10 · 1h | breakout | 83.83 | -16.17 | 81 | 17.3 | -11.28 | -1.35 | -27.92 | 214 |
| 51 | Agent (ML meta-label) | meta | 83.72 | -16.28 | 681 | 18.8 | -10.04 | -1.71 | -16.04 | 368 |
| 52 | Bollinger reversion · 1h | reversion | 82.82 | -17.18 | 158 | 34.8 | -27.80 | -5.31 | -33.53 | 349 |
| 53 | Max aggression: 1-day momentum | meta | 82.44 | -17.56 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Williams %R · 1h | reversion | 81.88 | -18.12 | 182 | 42.9 | -33.27 | -5.29 | -36.50 | 531 |
| 55 | Three white soldiers | momentum | 81.85 | -18.15 | 235 | 18.7 | -47.49 | -18.66 | -47.87 | 605 |
| 56 | ROC + volume · 1h | momentum | 81.40 | -18.59 | 197 | 20.8 | -25.35 | -4.27 | -33.90 | 383 |
| 57 | CCI reversion · 1h | reversion | 80.57 | -19.43 | 163 | 39.3 | -17.88 | -2.23 | -27.44 | 443 |
| 58 | RSI(14) reversion · 1h | reversion | 80.02 | -19.98 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 79.91 | -20.09 | 136 | 11.0 | -29.45 | -6.11 | -29.93 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 78.73 | -21.27 | 226 | 21.2 | -41.71 | -8.92 | -45.14 | 683 |
| 61 | VWAP momentum · 1h | momentum | 77.82 | -22.18 | 433 | 20.8 | -43.33 | -7.61 | -48.46 | 1249 |
| 62 | Candlestick reversal · 1h | reversion | 77.00 | -23.00 | 214 | 27.6 | -36.74 | -6.58 | -37.63 | 530 |
| 63 | ROC + volume | momentum | 61.43 | -38.57 | 598 | 22.2 | -76.07 | -17.87 | -78.22 | 1727 |
| 64 | Volume breakout | breakout | 61.28 | -38.72 | 361 | 13.0 | -62.63 | -17.56 | -64.30 | 871 |
| 65 | Squeeze breakout | breakout | 59.72 | -40.28 | 474 | 13.9 | -63.94 | -19.54 | -65.98 | 1203 |
| 66 | Donchian 55/20 | breakout | 58.16 | -41.84 | 482 | 18.3 | -68.56 | -14.08 | -73.20 | 1270 |
| 67 | RSI(14) reversion | reversion | 57.56 | -42.44 | 715 | 25.2 | -74.63 | -16.53 | -74.73 | 1599 |
| 68 | EMA 20/50 cross | trend | 56.10 | -43.90 | 517 | 19.7 | -76.92 | -15.99 | -80.55 | 1422 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.68 | -14.60 | -72.51 | 1496 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -28.18 | -98.70 | 5263 |
| 71 | Keltner breakout | breakout | 50.52 | -49.48 | 678 | 16.1 | -82.50 | -24.45 | -83.70 | 1808 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.08 | -27.16 | -93.78 | 2562 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.60 | -20.43 | -88.26 | 1888 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.80 | -21.91 | -91.21 | 2345 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.19 | -26.13 | -91.19 | 2261 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.33 | -29.35 | -97.58 | 3487 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.52 | -32.73 | -96.79 | 3583 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.54 | -28.35 | -94.60 | 2506 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.81 | -23.73 | -82.95 | 1688 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.39 | -99.36 | 5722 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.01 | -23.59 | -92.11 | 2626 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.09 | -31.38 | -96.09 | 3468 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.01 | -99.74 | 6181 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -29.17 | -91.61 | 2329 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -34.26 | -97.66 | 3621 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -35.84 | -98.44 | 4680 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -31.12 | -94.03 | 2798 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -38.50 | -99.51 | 6148 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.81 | -22.31 | -86.85 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.85 | -26.57 | -87.88 | 2127 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -32.10 | -95.84 | 3737 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.65 | -30.49 | -89.17 | 2096 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -32.97 | -95.68 | 4096 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.59 | -99.90 | 8279 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T05:20 | Donchian 55/20 | sell | XRP-USD | 14.50 | -0.13 | exit signal |
| 2026-10-20T05:10 | Squeeze breakout | sell | ETH-USD | 14.86 | -0.10 | exit signal |
| 2026-10-20T05:10 | Keltner breakout | sell | BTC-USD | 12.55 | -0.10 | exit signal |
| 2026-10-20T05:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.78 | — | entry signal |
| 2026-10-20T05:00 | Parabolic SAR · 1h | buy | XRP-USD | 4.21 | — | entry signal |
| 2026-10-20T05:00 | Parabolic SAR · 1h | buy | ETH-USD | 18.25 | — | entry signal |
| 2026-10-20T04:50 | ROC + volume | sell | ETH-USD | 15.31 | -0.09 | exit signal |
| 2026-10-20T04:45 | ROC + volume | sell | SOL-USD | 15.30 | -0.11 | exit signal |
| 2026-10-20T04:10 | Three white soldiers | sell | DOGE-USD | 20.33 | -0.18 | target is flat |
| 2026-10-20T04:10 | Donchian 55/20 | sell | DOGE-USD | 14.48 | -0.13 | target is flat |
| 2026-10-20T04:05 | Three white soldiers | buy | DOGE-USD | 20.51 | — | entry signal |
| 2026-10-20T04:05 | Keltner breakout | buy | BTC-USD | 12.66 | — | entry signal |
| 2026-10-20T04:05 | Donchian 55/20 | buy | DOGE-USD | 14.61 | — | entry signal |
| 2026-10-20T04:00 | Parabolic SAR · 1h | buy | BTC-USD | 22.84 | — | entry signal |
| 2026-10-20T04:00 | Triple EMA stack · 1h | buy | XRP-USD | 21.42 | — | entry signal |
| 2026-10-20T04:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 22.57 | — | entry signal |
| 2026-10-20T04:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 8.07 | — | entry signal |
| 2026-10-20T04:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 4.00 | -0.01 | rebalance down |
| 2026-10-20T04:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 4.07 | -0.01 | rebalance down |
| 2026-10-20T04:00 | Donchian 55/20 | buy | BTC-USD | 14.62 | — | entry signal |
| 2026-10-20T03:55 | Donchian 55/20 | buy | XRP-USD | 14.63 | — | entry signal |
| 2026-10-20T03:50 | Donchian 55/20 | buy | ETH-USD | 14.64 | — | entry signal |
| 2026-10-20T03:35 | EMA 20/50 cross | buy | BTC-USD | 2.89 | — | entry |
| 2026-10-20T03:35 | EMA 20/50 cross | sell | SOL-USD | 2.80 | -0.02 | rebalance down |
| 2026-10-20T03:20 | EMA 20/50 cross | buy | ETH-USD | 14.03 | — | entry signal |
| 2026-10-20T03:10 | Squeeze breakout | buy | ETH-USD | 14.95 | — | entry signal |
| 2026-10-20T03:10 | ROC + volume | buy | ETH-USD | 15.40 | — | entry signal |
| 2026-10-20T03:10 | EMA 20/50 cross | buy | DOGE-USD | 14.07 | — | entry |
| 2026-10-20T03:05 | ROC + volume | buy | SOL-USD | 15.40 | — | entry signal |
| 2026-10-20T03:00 | EMA 20/50 cross | buy | XRP-USD | 14.08 | — | entry signal |
| 2026-10-20T02:50 | RSI(14) reversion | sell | ETH-USD | 14.39 | -0.02 | exit signal |
| 2026-10-20T02:50 | EMA 20/50 cross | buy | SOL-USD | 14.09 | — | entry signal |
| 2026-10-20T02:30 | RSI(14) reversion | sell | DOGE-USD | 11.53 | 0.02 | take-profit |
| 2026-10-20T02:05 | Three white soldiers | sell | DOGE-USD | 20.36 | -0.20 | exit signal |
| 2026-10-20T02:00 | Parabolic SAR · 1h | sell | SOL-USD | 22.59 | -0.21 | exit signal |
| 2026-10-20T02:00 | Parabolic SAR · 1h | sell | DOGE-USD | 22.72 | -0.26 | exit signal |
| 2026-10-20T02:00 | RSI(14) reversion | sell | BTC-USD | 14.40 | -0.03 | exit signal |
| 2026-10-20T01:55 | RSI(14) reversion | sell | SOL-USD | 14.40 | -0.01 | exit signal |
| 2026-10-20T01:46 | RSI(14) reversion | buy | SOL-USD | 2.89 | — | rebalance up |
| 2026-10-20T01:46 | RSI(14) reversion | buy | ETH-USD | 2.90 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 05:25:05.000116+00:00 -> 2026-10-20 05:35:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
