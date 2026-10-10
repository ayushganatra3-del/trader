# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T07:55:05.000146+00:00 · 17662 ticks

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
| Copy: Insider buying | 2026-10-10 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 5970 decisions in 1194 calls, $0.0835 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T07:55 | 0 / 4 / 1 | SOL-USD 14%, NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T07:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T07:55 | 1 / 4 / 0 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |
| Bollinger reversion | TECL | 1.82 | +2.00% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -13.60 | -2.18 | -22.02 | 69 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.33 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.19 | -0.81 | 88 | 55.7 | -10.88 | -2.11 | -14.99 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.93 | -1.07 | 0 | — | 27.32 | 3.28 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.24 | -2.76 | 41 | 43.9 | 1.97 | 0.52 | -8.60 | 161 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.58 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 0.53 | 0.23 | -8.65 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.49 | -0.07 | -13.84 | 256 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.87 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.85 | -4.15 | 108 | 23.1 | -16.30 | -2.64 | -17.97 | 473 |
| 34 | Supertrend · 1h | trend | 95.19 | -4.81 | 52 | 13.5 | -0.20 | 0.17 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.14 | -5.86 | 35 | 25.7 | 24.09 | 3.28 | -8.68 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.70 | -2.02 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.55 | -0.67 | -9.03 | 154 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -4.63 | -0.76 | -13.27 | 431 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.80 | -4.97 | -23.49 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.58 | 0.63 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.87 | -8.13 | 67 | 29.9 | 6.53 | 1.00 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.79 | -8.21 | 119 | 47.9 | -25.07 | -4.32 | -27.27 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.80 | -0.88 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.26 | -9.74 | 114 | 30.7 | -28.56 | -5.62 | -30.34 | 522 |
| 51 | CCI reversion · 1h | reversion | 89.77 | -10.22 | 98 | 44.9 | -9.16 | -1.20 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.72 | -10.28 | 277 | 22.0 | -35.60 | -5.40 | -39.27 | 1286 |
| 53 | MACD zero-line · 1h | trend | 89.36 | -10.64 | 60 | 20.0 | -6.32 | -0.67 | -19.50 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.22 | -19.78 | 700 |
| 55 | Donchian 20/10 · 1h | breakout | 88.84 | -11.16 | 58 | 19.0 | -0.05 | 0.20 | -17.72 | 221 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.99 | -1.35 | -28.48 | 318 |
| 57 | Three white soldiers | momentum | 88.76 | -11.24 | 131 | 19.1 | -48.14 | -23.50 | -48.14 | 588 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.25 | -5.26 | -36.59 | 703 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.85 | -12.15 | 101 | 13.9 | -9.48 | -1.08 | -21.49 | 338 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.69 | -1.30 | -24.09 | 412 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -72.78 | -18.19 | -72.94 | 1493 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1667 |
| 65 | Squeeze breakout | breakout | 73.07 | -26.93 | 308 | 15.6 | -61.91 | -18.43 | -61.91 | 1222 |
| 66 | EMA 20/50 cross | trend | 72.03 | -27.97 | 311 | 20.9 | -77.21 | -15.37 | -77.37 | 1459 |
| 67 | Donchian 55/20 | breakout | 71.90 | -28.10 | 318 | 18.6 | -67.81 | -14.60 | -67.95 | 1296 |
| 68 | Volume breakout | breakout | 71.23 | -28.77 | 252 | 13.5 | -63.21 | -18.39 | -63.23 | 901 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.80 | -16.13 | -71.94 | 1436 |
| 70 | Supertrend | trend | 65.90 | -34.10 | 441 | 20.6 | -86.39 | -21.28 | -86.39 | 1923 |
| 71 | Keltner breakout | breakout | 64.52 | -35.48 | 430 | 14.9 | -84.14 | -28.42 | -84.20 | 1859 |
| 72 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.72 | -23.52 | -85.73 | 2094 |
| 73 | Ichimoku | trend | 61.41 | -38.59 | 393 | 9.9 | -81.81 | -23.69 | -81.81 | 1751 |
| 74 | MFI reversion | reversion | 61.13 | -38.87 | 490 | 22.0 | -87.67 | -28.48 | -87.67 | 2119 |
| 75 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 76 | AI bee: Bizzy | ai | 60.43 | -39.57 | 783 | 9.3 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.38 | -41.62 | 522 | 10.5 | -89.47 | -34.43 | -89.47 | 2126 |
| 78 | Donchian 20/10 | breakout | 58.13 | -41.87 | 605 | 18.8 | -90.80 | -26.41 | -90.80 | 2663 |
| 79 | Trend pullback | trend | 57.80 | -42.20 | 552 | 15.8 | -90.47 | -27.31 | -90.47 | 2304 |
| 80 | RSI momentum | momentum | 57.32 | -42.68 | 572 | 17.8 | -90.30 | -25.93 | -90.30 | 2379 |
| 81 | MACD zero-line | trend | 56.88 | -43.12 | 551 | 15.6 | -91.51 | -29.79 | -91.51 | 2359 |
| 82 | Triple EMA stack | trend | 56.16 | -43.84 | 592 | 16.2 | -93.12 | -30.90 | -93.12 | 2612 |
| 83 | Bollinger breakout | breakout | 53.61 | -46.39 | 633 | 14.8 | -93.53 | -33.79 | -93.53 | 2818 |
| 84 | Consensus | meta | 51.89 | -48.11 | 600 | 10.2 | -94.30 | -26.14 | -94.30 | 2689 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.85 | -98.68 | 5393 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -33.60 | -97.35 | 3541 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.41 | -37.26 | -96.41 | 3607 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.04 | -99.34 | 5690 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.17 | -31.72 | -96.17 | 3586 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.99 | -99.73 | 6202 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -39.43 | -97.34 | 3683 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.60 | -98.47 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.64 | -99.51 | 6145 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -33.87 | -95.85 | 3742 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.55 | -34.83 | -95.55 | 4082 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.40 | -99.90 | 8342 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T07:55 | Consensus | buy | BTC-USD | 12.98 | — | entry |
| 2026-10-10T07:55 | MACD zero-line | buy | BTC-USD | 14.23 | — | entry signal |
| 2026-10-10T07:55 | Triple EMA stack | buy | BTC-USD | 14.05 | — | entry signal |
| 2026-10-10T07:55 | EMA 20/50 cross | sell | XRP-USD | 14.46 | 0.08 | exit signal |
| 2026-10-10T07:52 | AI bee: Bizzy | buy | SOL-USD | 8.60 | — | Jev: buy (buy p=0.57) |
| 2026-10-10T07:50 | Trend pullback | buy | SOL-USD | 14.47 | — | entry signal |
| 2026-10-10T07:50 | Trend pullback | buy | ETH-USD | 14.47 | — | entry signal |
| 2026-10-10T07:50 | Supertrend | buy | BTC-USD | 16.49 | — | entry signal |
| 2026-10-10T07:45 | ADX DI cross | sell | XRP-USD | 14.54 | -0.09 | exit signal |
| 2026-10-10T07:40 | Trend pullback | buy | BTC-USD | 14.48 | — | entry signal |
| 2026-10-10T07:40 | ADX DI cross | buy | XRP-USD | 14.63 | — | entry |
| 2026-10-10T07:40 | ADX DI cross | buy | BTC-USD | 14.63 | — | entry signal |
| 2026-10-10T07:40 | Supertrend | sell | ETH-USD | 13.19 | -0.05 | exit signal |
| 2026-10-10T07:20 | Trend pullback | sell | SOL-USD | 14.41 | -0.10 | exit signal |
| 2026-10-10T07:20 | EMA 20/50 cross | buy | BTC-USD | 7.40 | — | rebalance up |
| 2026-10-10T07:20 | EMA 20/50 cross | sell | DOGE-USD | 14.49 | 0.14 | exit signal |
| 2026-10-10T07:15 | Donchian 55/20 | sell | BTC-USD | 17.99 | -0.13 | stop-loss |
| 2026-10-10T07:15 | Donchian 20/10 | sell | BTC-USD | 14.52 | -0.11 | stop-loss |
| 2026-10-10T07:15 | Trend pullback | buy | SOL-USD | 14.50 | — | entry signal |
| 2026-10-10T07:15 | Supertrend | sell | BTC-USD | 13.20 | -0.08 | exit signal |
| 2026-10-10T07:15 | Triple EMA stack | sell | BTC-USD | 11.26 | -0.07 | exit signal |
| 2026-10-10T07:10 | RSI momentum | sell | BTC-USD | 11.50 | -0.07 | exit signal |
| 2026-10-10T07:10 | Trend pullback | sell | BTC-USD | 14.52 | -0.09 | exit signal |
| 2026-10-10T07:05 | MFI reversion | buy | ETH-USD | 15.29 | — | entry signal |
| 2026-10-10T07:05 | Donchian 55/20 | sell | XRP-USD | 17.95 | -0.17 | stop-loss |
| 2026-10-10T07:05 | RSI momentum | sell | XRP-USD | 11.47 | -0.08 | exit signal |
| 2026-10-10T07:05 | Trend pullback | sell | XRP-USD | 11.63 | -0.08 | exit signal |
| 2026-10-10T07:05 | ADX DI cross | sell | XRP-USD | 14.58 | -0.07 | exit signal |
| 2026-10-10T07:05 | Supertrend | sell | XRP-USD | 16.47 | -0.11 | exit signal |
| 2026-10-10T07:00 | Squeeze breakout | sell | BTC-USD | 18.24 | -0.12 | stop-loss |
| 2026-10-10T07:00 | Keltner breakout | sell | BTC-USD | 16.13 | -0.10 | stop-loss |
| 2026-10-10T07:00 | Bollinger breakout | sell | BTC-USD | 13.41 | -0.09 | stop-loss |
| 2026-10-10T07:00 | Donchian 20/10 | sell | ETH-USD | 14.54 | -0.10 | exit signal |
| 2026-10-10T07:00 | RSI momentum | sell | ETH-USD | 11.49 | -0.07 | exit signal |
| 2026-10-10T07:00 | Trend pullback | sell | ETH-USD | 11.64 | -0.08 | exit signal |
| 2026-10-10T07:00 | Triple EMA stack | sell | XRP-USD | 11.25 | -0.05 | exit signal |
| 2026-10-10T07:00 | Triple EMA stack | sell | ETH-USD | 11.25 | -0.07 | exit signal |
| 2026-10-10T06:55 | Trend pullback | sell | SOL-USD | 14.47 | -0.11 | exit signal |
| 2026-10-10T06:54 | AI bee: Bizzy | sell | XRP-USD | 9.10 | -0.07 | Jev: sell (sell p=0.85) after 11 min |
| 2026-10-10T06:50 | Consensus | sell | XRP-USD | 12.90 | -0.11 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 07:55:05.000146+00:00 -> 2026-10-10 08:05:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
