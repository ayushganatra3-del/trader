# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T02:55:05.000127+00:00 · 19742 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 2265 decisions in 453 calls, $0.0317 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T02:55 | 0 / 4 / 1 | DOGE-USD 14%, NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T02:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T02:55 | 1 / 4 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.25 | 3.25 | 37 | 43.2 | -7.44 | -2.25 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.46 | 2.46 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.13 | 2.13 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 101.94 | 1.94 | 14 | 57.1 | -15.28 | -2.49 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.26 | 1.26 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.18 | 1.18 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.02 | 1.02 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.03 | 0.03 | 0 | — | 30.31 | 3.56 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.68 | -0.32 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.62 | -0.38 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 19 | Stochastic reversion · 1h | reversion | 99.05 | -0.95 | 89 | 55.1 | -9.77 | -1.87 | -14.61 | 337 |
| 20 | Donchian 55/20 · 1h | breakout | 99.04 | -0.96 | 28 | 14.3 | 13.07 | 1.62 | -16.96 | 113 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.52 | -1.48 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.49 | -1.51 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.73 | -2.27 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.29 | -2.71 | 7 | 0.0 | -3.28 | -2.51 | -4.32 | 28 |
| 25 | Z-score reversion · 1h | reversion | 97.13 | -2.87 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 96.97 | -3.03 | 78 | 23.1 | -23.13 | -6.51 | -25.39 | 167 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 28 | Agent (rotation) | meta | 96.66 | -3.34 | 80 | 30.0 | -6.60 | -2.32 | -9.69 | 258 |
| 29 | EMA 20/50 cross · 1h | trend | 96.58 | -3.42 | 40 | 12.5 | 5.02 | 0.77 | -19.85 | 139 |
| 30 | ADX DI cross · 1h | trend | 96.23 | -3.77 | 58 | 20.7 | -0.78 | 0.04 | -13.84 | 254 |
| 31 | Parabolic SAR · 1h | trend | 96.19 | -3.81 | 82 | 22.0 | -2.94 | -0.22 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.76 | -4.24 | 115 | 23.5 | -14.65 | -2.33 | -17.27 | 467 |
| 34 | Supertrend · 1h | trend | 95.40 | -4.59 | 53 | 13.2 | 0.32 | 0.23 | -18.22 | 212 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.42 | -6.58 | 119 | 34.5 | -10.04 | -1.58 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.40 | -6.60 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.02 | -6.98 | 26 | 26.9 | -1.81 | -0.28 | -9.03 | 146 |
| 40 | Connors RSI(2) · 1h | reversion | 92.99 | -7.01 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.75 | -7.25 | 392 | 18.4 | -4.43 | -0.69 | -13.62 | 429 |
| 42 | Bollinger reversion · 1h | reversion | 92.68 | -7.32 | 78 | 37.2 | -20.80 | -4.93 | -23.20 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.58 | -7.42 | 64 | 15.6 | 3.74 | 0.65 | -17.15 | 227 |
| 44 | Volume breakout · 1h | breakout | 92.10 | -7.90 | 58 | 19.0 | 7.66 | 1.19 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 91.98 | -8.02 | 44 | 18.2 | -0.99 | 0.08 | -21.18 | 124 |
| 46 | Williams %R · 1h | reversion | 91.48 | -8.52 | 126 | 47.6 | -23.54 | -4.00 | -26.91 | 512 |
| 47 | Bollinger breakout · 1h | breakout | 91.16 | -8.84 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.61 | -9.39 | 69 | 15.9 | -9.12 | -0.91 | -26.49 | 243 |
| 50 | Candlestick reversal · 1h | reversion | 90.32 | -9.68 | 118 | 33.1 | -26.10 | -5.03 | -28.13 | 506 |
| 51 | CCI reversion · 1h | reversion | 89.89 | -10.11 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.38 | -10.62 | 284 | 21.8 | -31.78 | -4.67 | -39.17 | 1274 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.66 | -11.34 | 149 | 18.8 | -12.97 | -1.48 | -28.57 | 325 |
| 55 | Donchian 20/10 · 1h | breakout | 88.57 | -11.43 | 60 | 18.3 | -0.58 | 0.14 | -18.15 | 227 |
| 56 | Heikin-Ashi · 1h | trend | 88.55 | -11.45 | 138 | 25.4 | -29.92 | -4.98 | -36.60 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.10 | -11.90 | 66 | 18.2 | -6.75 | -0.73 | -20.89 | 239 |
| 58 | Max aggression: 5-day momentum | meta | 87.86 | -12.14 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.79 | -12.21 | 104 | 13.5 | -8.61 | -0.96 | -21.96 | 339 |
| 60 | Three white soldiers | momentum | 87.18 | -12.82 | 142 | 17.6 | -48.03 | -22.82 | -48.04 | 589 |
| 61 | Keltner breakout · 1h | breakout | 86.99 | -13.01 | 43 | 18.6 | -11.90 | -1.37 | -25.51 | 218 |
| 62 | ROC + volume · 1h | momentum | 86.16 | -13.84 | 132 | 21.2 | -10.22 | -1.22 | -23.48 | 415 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.73 | -16.36 | -73.90 | 1677 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 375 | 27.5 | -72.75 | -17.93 | -72.80 | 1496 |
| 65 | Squeeze breakout | breakout | 70.67 | -29.33 | 336 | 15.5 | -62.03 | -17.90 | -62.16 | 1230 |
| 66 | Volume breakout | breakout | 70.12 | -29.88 | 269 | 14.1 | -62.39 | -17.74 | -62.49 | 905 |
| 67 | Donchian 55/20 | breakout | 69.41 | -30.59 | 341 | 18.5 | -67.66 | -14.38 | -67.82 | 1298 |
| 68 | EMA 20/50 cross | trend | 68.87 | -31.13 | 344 | 20.1 | -76.78 | -15.21 | -76.86 | 1458 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 405 | 25.9 | -71.32 | -15.83 | -71.38 | 1431 |
| 70 | Supertrend | trend | 62.73 | -37.27 | 474 | 20.0 | -86.05 | -20.95 | -86.11 | 1919 |
| 71 | Keltner breakout | breakout | 61.92 | -38.08 | 461 | 14.8 | -83.80 | -27.49 | -83.81 | 1856 |
| 72 | Ichimoku | trend | 60.16 | -39.84 | 411 | 10.5 | -81.59 | -22.86 | -81.70 | 1752 |
| 73 | AI bee: Boozy | ai | 60.06 | -39.94 | 259 | 5.0 | — | — | — | — |
| 74 | Z-score reversion | reversion | 58.93 | -41.07 | 516 | 22.1 | -85.11 | -22.76 | -85.12 | 2076 |
| 75 | MFI reversion | reversion | 58.35 | -41.65 | 524 | 20.8 | -87.57 | -27.94 | -87.61 | 2124 |
| 76 | AI bee: Bizzy | ai | 56.59 | -43.41 | 857 | 8.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.89 | -44.11 | 552 | 10.3 | -89.17 | -34.25 | -89.19 | 2119 |
| 78 | Donchian 20/10 | breakout | 54.32 | -45.68 | 649 | 18.2 | -90.80 | -25.93 | -90.81 | 2669 |
| 79 | Trend pullback | trend | 53.23 | -46.77 | 603 | 14.6 | -91.11 | -26.84 | -91.14 | 2347 |
| 80 | RSI momentum | momentum | 52.88 | -47.12 | 622 | 17.0 | -90.38 | -25.62 | -90.40 | 2391 |
| 81 | MACD zero-line | trend | 52.45 | -47.55 | 605 | 14.7 | -91.50 | -29.71 | -91.51 | 2368 |
| 82 | Triple EMA stack | trend | 51.88 | -48.12 | 647 | 15.5 | -93.21 | -29.98 | -93.22 | 2628 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.92 | -98.64 | 5390 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.10 | -97.35 | 3551 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -35.68 | -96.45 | 3623 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.19 | -25.29 | -94.19 | 2694 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.46 | -99.35 | 5692 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.46 | -31.79 | -96.46 | 3636 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.55 | -99.73 | 6210 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.59 | -97.35 | 3696 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.44 | -98.46 | 4709 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.52 | -32.92 | -93.53 | 2823 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.76 | -99.52 | 6155 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -33.06 | -95.85 | 3748 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.62 | -33.73 | -95.63 | 4086 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.39 | -99.89 | 8317 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T02:55 | Trend pullback | buy | ETH-USD | 13.32 | — | entry signal |
| 2026-10-12T02:50 | Volume breakout | sell | ETH-USD | 17.40 | -0.17 | exit signal |
| 2026-10-12T02:47 | AI bee: Bizzy | buy | DOGE-USD | 8.01 | — | Jev: buy (buy p=0.57) |
| 2026-10-12T02:44 | AI bee: Bizzy | sell | SOL-USD | 8.55 | -0.05 | Jev: sell (sell p=0.57) after 13 min |
| 2026-10-12T02:40 | Ichimoku | buy | SOL-USD | 15.10 | — | entry signal |
| 2026-10-12T02:40 | Ichimoku | buy | ETH-USD | 15.10 | — | entry signal |
| 2026-10-12T02:40 | Ichimoku | buy | DOGE-USD | 15.10 | — | entry signal |
| 2026-10-12T02:40 | Ichimoku | buy | BTC-USD | 15.10 | — | entry signal |
| 2026-10-12T02:31 | AI bee: Bizzy | buy | SOL-USD | 8.60 | — | Jev: buy (buy p=0.61) |
| 2026-10-12T02:30 | Trend pullback | buy | DOGE-USD | 13.31 | — | entry signal |
| 2026-10-12T02:30 | MACD zero-line | buy | BTC-USD | 13.12 | — | entry signal |
| 2026-10-12T02:29 | AI bee: Bizzy | sell | ETH-USD | 8.79 | -0.08 | Jev: sell (sell p=0.65) after 10 min |
| 2026-10-12T02:25 | Keltner breakout | sell | DOGE-USD | 15.39 | -0.17 | stop-loss |
| 2026-10-12T02:25 | Donchian 55/20 | sell | DOGE-USD | 17.25 | -0.19 | stop-loss |
| 2026-10-12T02:25 | Donchian 20/10 | sell | DOGE-USD | 13.50 | -0.15 | stop-loss |
| 2026-10-12T02:25 | RSI momentum | buy | XRP-USD | 2.66 | — | rebalance up |
| 2026-10-12T02:25 | RSI momentum | buy | SOL-USD | 2.65 | — | rebalance up |
| 2026-10-12T02:25 | RSI momentum | sell | DOGE-USD | 10.52 | -0.12 | stop-loss |
| 2026-10-12T02:25 | MACD zero-line | sell | DOGE-USD | 13.01 | -0.14 | stop-loss |
| 2026-10-12T02:25 | Triple EMA stack | buy | BTC-USD | 12.98 | — | entry signal |
| 2026-10-12T02:25 | Triple EMA stack | sell | DOGE-USD | 12.88 | -0.14 | stop-loss |
| 2026-10-12T02:25 | EMA 20/50 cross | sell | DOGE-USD | 17.09 | -0.19 | stop-loss |
| 2026-10-12T02:20 | VWAP reversion | sell | XRP-USD | 16.96 | 0.01 | exit signal |
| 2026-10-12T02:20 | Z-score reversion | sell | XRP-USD | 14.73 | -0.02 | exit signal |
| 2026-10-12T02:20 | RSI(14) reversion | sell | XRP-USD | 18.45 | 0.01 | take-profit |
| 2026-10-12T02:20 | RSI(14) reversion | sell | BTC-USD | 18.43 | -0.01 | take-profit |
| 2026-10-12T02:20 | Volume breakout | buy | ETH-USD | 17.57 | — | entry signal |
| 2026-10-12T02:20 | Keltner breakout | buy | SOL-USD | 15.56 | — | entry signal |
| 2026-10-12T02:20 | Keltner breakout | buy | ETH-USD | 15.56 | — | entry signal |
| 2026-10-12T02:20 | Keltner breakout | buy | DOGE-USD | 15.56 | — | entry signal |
| 2026-10-12T02:20 | Donchian 55/20 | buy | SOL-USD | 17.44 | — | entry signal |
| 2026-10-12T02:20 | Donchian 55/20 | buy | ETH-USD | 17.44 | — | entry signal |
| 2026-10-12T02:20 | Donchian 55/20 | buy | DOGE-USD | 17.44 | — | entry signal |
| 2026-10-12T02:20 | Donchian 20/10 | buy | SOL-USD | 13.65 | — | entry signal |
| 2026-10-12T02:20 | Donchian 20/10 | buy | ETH-USD | 13.65 | — | entry signal |
| 2026-10-12T02:20 | Donchian 20/10 | buy | DOGE-USD | 13.65 | — | entry signal |
| 2026-10-12T02:20 | RSI momentum | buy | XRP-USD | 10.63 | — | entry signal |
| 2026-10-12T02:20 | RSI momentum | buy | SOL-USD | 10.64 | — | entry signal |
| 2026-10-12T02:20 | RSI momentum | buy | DOGE-USD | 10.64 | — | entry signal |
| 2026-10-12T02:20 | RSI momentum | buy | BTC-USD | 10.64 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 02:55:05.000127+00:00 -> 2026-10-12 03:05:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
