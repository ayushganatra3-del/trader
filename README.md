# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T13:27:05.000156+00:00 · 29542 ticks

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

Today: 9645 decisions in 1929 calls, $0.1350 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T13:27 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-20T13:27 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T13:27 | 1 / 4 / 0 | cash |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.78 | 4.78 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.69 | -0.32 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 98.93 | -1.07 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 2.57 | 1.40 | -2.63 | 63 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.07 | -1.93 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -1.51 | -0.58 | -5.85 | 290 |
| 14 | Donchian 55/20 · 1h | breakout | 97.22 | -2.78 | 37 | 16.2 | -11.42 | -2.13 | -19.38 | 97 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.13 | -2.87 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 17 | Hold BTC | benchmark | 96.54 | -3.46 | 0 | — | 24.13 | 2.98 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 96.32 | -3.68 | 88 | 23.9 | -20.10 | -5.95 | -20.55 | 136 |
| 19 | Copy: Insider buying | copy | 96.23 | -3.77 | 23 | 43.5 | -11.55 | -1.97 | -20.62 | 70 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.17 | -3.83 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.21 | -4.79 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.54 | 2.17 | -6.51 | 199 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 25 | ADX DI cross · 1h | trend | 93.43 | -6.57 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 26 | Daily: Momentum burst | daily | 92.78 | -7.22 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Volume breakout · 1h | breakout | 91.84 | -8.16 | 78 | 23.1 | -12.55 | -2.25 | -16.37 | 101 |
| 28 | Daily: Bullish score | daily | 91.84 | -8.16 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 30 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 31 | Parabolic SAR · 1h | trend | 90.77 | -9.23 | 105 | 21.9 | -20.36 | -4.54 | -22.26 | 270 |
| 32 | Bollinger breakout · 1h | breakout | 90.73 | -9.27 | 84 | 28.6 | -9.08 | -1.54 | -16.89 | 253 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -12.72 | -4.32 | -20.44 | 262 |
| 34 | EMA 20/50 cross · 1h | trend | 89.89 | -10.11 | 60 | 13.3 | -19.38 | -3.47 | -21.31 | 127 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 89.89 | -10.11 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 36 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.32 | -6.58 | -23.81 | 204 |
| 37 | RSI momentum · 1h | momentum | 89.21 | -10.79 | 82 | 15.9 | -25.74 | -4.99 | -26.11 | 212 |
| 38 | Ichimoku · 1h | trend | 88.49 | -11.51 | 57 | 14.0 | -17.74 | -3.35 | -18.21 | 114 |
| 39 | Stochastic reversion · 1h | reversion | 88.09 | -11.91 | 152 | 46.1 | -17.12 | -2.96 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -15.01 | -3.52 | -22.27 | 133 |
| 41 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 56 | 23.2 | -16.91 | -2.76 | -26.96 | 200 |
| 42 | Supertrend · 1h | trend | 87.03 | -12.97 | 88 | 12.5 | -22.99 | -4.72 | -26.61 | 214 |
| 43 | Triple EMA stack · 1h | trend | 86.73 | -13.27 | 88 | 14.8 | -25.78 | -4.35 | -33.14 | 233 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 85.81 | -14.19 | 189 | 20.6 | -28.29 | -5.53 | -32.90 | 470 |
| 46 | OBV trend · 1h | momentum | 85.08 | -14.92 | 181 | 17.7 | -29.91 | -5.14 | -36.63 | 317 |
| 47 | Z-score reversion · 1h | reversion | 85.01 | -14.99 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.40 | -15.60 | 209 | 31.1 | -17.23 | -2.69 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.18 | -15.81 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Agent (ML meta-label) | meta | 83.66 | -16.34 | 681 | 18.8 | -12.19 | -2.29 | -16.18 | 356 |
| 51 | Donchian 20/10 · 1h | breakout | 83.64 | -16.36 | 81 | 17.3 | -13.26 | -1.69 | -27.92 | 214 |
| 52 | Bollinger reversion · 1h | reversion | 82.81 | -17.19 | 158 | 34.8 | -27.82 | -5.31 | -33.53 | 352 |
| 53 | Max aggression: 1-day momentum | meta | 82.38 | -17.62 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 81.85 | -18.15 | 235 | 18.7 | -47.40 | -18.57 | -47.87 | 602 |
| 55 | Williams %R · 1h | reversion | 81.82 | -18.18 | 182 | 42.9 | -33.30 | -5.29 | -36.50 | 532 |
| 56 | ROC + volume · 1h | momentum | 81.37 | -18.63 | 197 | 20.8 | -24.83 | -4.13 | -33.90 | 382 |
| 57 | CCI reversion · 1h | reversion | 80.49 | -19.51 | 163 | 39.3 | -17.96 | -2.25 | -27.44 | 443 |
| 58 | RSI(14) reversion · 1h | reversion | 79.96 | -20.04 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 79.35 | -20.65 | 139 | 10.8 | -29.93 | -6.23 | -30.06 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 78.64 | -21.36 | 227 | 21.1 | -42.12 | -9.06 | -45.31 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.76 | -22.24 | 433 | 20.8 | -43.63 | -7.68 | -48.68 | 1249 |
| 62 | Candlestick reversal · 1h | reversion | 76.94 | -23.06 | 214 | 27.6 | -36.66 | -6.56 | -37.63 | 531 |
| 63 | ROC + volume | momentum | 61.28 | -38.72 | 599 | 22.2 | -76.08 | -17.79 | -78.28 | 1719 |
| 64 | Volume breakout | breakout | 60.94 | -39.05 | 364 | 12.9 | -62.54 | -17.18 | -64.45 | 863 |
| 65 | Squeeze breakout | breakout | 58.98 | -41.02 | 479 | 13.8 | -64.24 | -19.54 | -66.45 | 1207 |
| 66 | Donchian 55/20 | breakout | 57.64 | -42.36 | 486 | 18.1 | -70.19 | -16.76 | -73.45 | 1270 |
| 67 | RSI(14) reversion | reversion | 56.76 | -43.23 | 722 | 24.9 | -74.96 | -16.70 | -75.01 | 1607 |
| 68 | EMA 20/50 cross | trend | 55.35 | -44.65 | 524 | 19.5 | -77.61 | -16.49 | -80.84 | 1426 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.68 | -14.60 | -72.51 | 1496 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -28.65 | -98.75 | 5277 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -30.83 | -93.82 | 2563 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.88 | -20.92 | -88.37 | 1889 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.34 | -24.51 | -91.30 | 2346 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.99 | -25.61 | -91.17 | 2251 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.52 | -32.69 | -97.63 | 3495 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.69 | -35.69 | -96.84 | 3578 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -28.10 | -94.48 | 2498 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.05 | -24.62 | -83.02 | 1686 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.12 | -99.38 | 5739 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.17 | -24.47 | -92.16 | 2622 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -31.17 | -95.91 | 3445 |
| 82 | Keltner breakout | breakout | 50.23 | -49.77 | 680 | 16.0 | -82.95 | -26.23 | -83.80 | 1793 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -39.59 | -99.76 | 6189 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.69 | -29.45 | -91.69 | 2332 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -37.39 | -97.70 | 3619 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.40 | -98.49 | 4694 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.90 | -33.05 | -94.13 | 2790 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.98 | -99.53 | 6159 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.01 | -22.55 | -87.03 | 2143 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.93 | -26.67 | -87.99 | 2131 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -32.52 | -95.96 | 3751 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.88 | -31.68 | -89.26 | 2096 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.78 | -33.40 | -95.79 | 4105 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.30 | -99.90 | 8269 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T13:15 | Donchian 55/20 | sell | BTC-USD | 14.34 | -0.14 | stop-loss |
| 2026-10-20T13:05 | Volume breakout | sell | ETH-USD | 15.18 | -0.13 | exit signal |
| 2026-10-20T13:05 | Squeeze breakout | sell | DOGE-USD | 14.69 | -0.15 | stop-loss |
| 2026-10-20T13:05 | Squeeze breakout | sell | BTC-USD | 14.70 | -0.13 | exit signal |
| 2026-10-20T13:05 | Keltner breakout | sell | DOGE-USD | 12.47 | -0.13 | stop-loss |
| 2026-10-20T13:05 | Donchian 55/20 | sell | DOGE-USD | 14.36 | -0.15 | stop-loss |
| 2026-10-20T13:05 | EMA 20/50 cross | sell | DOGE-USD | 13.77 | -0.14 | stop-loss |
| 2026-10-20T13:05 | EMA 20/50 cross | sell | BTC-USD | 2.81 | -0.02 | exit signal |
| 2026-10-20T13:00 | Volume breakout | sell | DOGE-USD | 15.17 | -0.13 | exit signal |
| 2026-10-20T13:00 | EMA 20/50 cross | buy | BTC-USD | 2.83 | — | entry signal |
| 2026-10-20T13:00 | EMA 20/50 cross | sell | XRP-USD | 2.80 | -0.01 | rebalance down |
| 2026-10-20T12:45 | Squeeze breakout | buy | SOL-USD | 14.83 | — | entry signal |
| 2026-10-20T12:45 | Squeeze breakout | buy | BTC-USD | 14.83 | — | entry signal |
| 2026-10-20T12:45 | Donchian 55/20 | buy | BTC-USD | 14.48 | — | entry signal |
| 2026-10-20T12:45 | EMA 20/50 cross | buy | ETH-USD | 13.90 | — | entry signal |
| 2026-10-20T12:40 | EMA 20/50 cross | buy | SOL-USD | 13.89 | — | entry signal |
| 2026-10-20T12:25 | Volume breakout | buy | ETH-USD | 15.30 | — | entry signal |
| 2026-10-20T12:25 | Volume breakout | buy | DOGE-USD | 15.30 | — | entry signal |
| 2026-10-20T12:25 | Squeeze breakout | buy | ETH-USD | 14.84 | — | entry signal |
| 2026-10-20T12:25 | Squeeze breakout | buy | DOGE-USD | 14.84 | — | entry signal |
| 2026-10-20T12:25 | Keltner breakout | buy | ETH-USD | 12.60 | — | entry signal |
| 2026-10-20T12:25 | Keltner breakout | buy | DOGE-USD | 12.60 | — | entry signal |
| 2026-10-20T12:25 | Donchian 55/20 | buy | SOL-USD | 14.51 | — | entry signal |
| 2026-10-20T12:25 | Donchian 55/20 | buy | ETH-USD | 14.51 | — | entry signal |
| 2026-10-20T12:25 | Donchian 55/20 | buy | DOGE-USD | 14.51 | — | entry signal |
| 2026-10-20T12:25 | EMA 20/50 cross | buy | DOGE-USD | 13.91 | — | entry signal |
| 2026-10-20T12:10 | Squeeze breakout | sell | XRP-USD | 14.76 | -0.11 | stop-loss |
| 2026-10-20T12:10 | Keltner breakout | sell | XRP-USD | 12.51 | -0.12 | stop-loss |
| 2026-10-20T12:10 | ROC + volume | sell | XRP-USD | 15.21 | -0.15 | stop-loss |
| 2026-10-20T12:00 | Ichimoku · 1h | sell | DOGE-USD | 22.05 | -0.10 | exit signal |
| 2026-10-20T12:00 | EMA 20/50 cross | buy | XRP-USD | 13.91 | — | entry signal |
| 2026-10-20T11:40 | Keltner breakout | buy | XRP-USD | 12.63 | — | entry signal |
| 2026-10-20T11:40 | ROC + volume | buy | XRP-USD | 15.36 | — | entry signal |
| 2026-10-20T11:30 | Squeeze breakout | buy | XRP-USD | 14.87 | — | entry signal |
| 2026-10-20T11:25 | Squeeze breakout | sell | DOGE-USD | 14.83 | -0.10 | target is flat |
| 2026-10-20T11:20 | Squeeze breakout | sell | SOL-USD | 14.80 | -0.13 | exit signal |
| 2026-10-20T11:10 | Volume breakout | sell | DOGE-USD | 15.24 | -0.08 | target is flat |
| 2026-10-20T11:05 | RSI(14) reversion | sell | DOGE-USD | 14.17 | -0.05 | exit signal |
| 2026-10-20T11:05 | Volume breakout | buy | DOGE-USD | 15.32 | — | entry signal |
| 2026-10-20T11:05 | Squeeze breakout | buy | SOL-USD | 14.93 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 13:27:05.000156+00:00 -> 2026-10-20 13:37:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
