# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T02:55:05.000149+00:00 · 18600 ticks

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

Today: 2205 decisions in 441 calls, $0.0308 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T02:55 | 0 / 3 / 2 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T02:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T02:55 | 2 / 2 / 1 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -13.59 | -2.18 | -22.02 | 69 |
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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.22 | 2.44 | -1.58 | 86 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Hold BTC | benchmark | 99.30 | -0.70 | 0 | — | 27.50 | 3.29 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.97 | -1.93 | -14.61 | 342 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.89 | -6.47 | -25.39 | 172 |
| 27 | EMA 20/50 cross · 1h | trend | 96.71 | -3.29 | 39 | 12.8 | 5.49 | 0.82 | -19.85 | 134 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -7.23 | -2.56 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -2.64 | -0.25 | -13.84 | 262 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.71 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.85 | -4.15 | 111 | 24.3 | -15.20 | -2.44 | -17.84 | 467 |
| 34 | Supertrend · 1h | trend | 95.27 | -4.73 | 52 | 13.5 | -0.12 | 0.18 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.03 | -5.97 | 36 | 25.0 | 23.95 | 3.26 | -8.85 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.14 | -1.76 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.26 | -0.39 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.96 | -7.04 | 41 | 19.5 | 0.07 | 0.21 | -20.02 | 120 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.84 | -0.55 | -12.86 | 413 |
| 43 | Bollinger reversion · 1h | reversion | 92.79 | -7.21 | 74 | 37.8 | -20.57 | -4.90 | -23.37 | 314 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.62 | 0.64 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.76 | -8.24 | 68 | 29.4 | 6.36 | 0.98 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.63 | -8.37 | 120 | 47.5 | -24.29 | -4.19 | -26.91 | 513 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.48 | -0.84 | -26.38 | 235 |
| 50 | Candlestick reversal · 1h | reversion | 90.22 | -9.79 | 116 | 31.9 | -27.14 | -5.31 | -28.95 | 516 |
| 51 | CCI reversion · 1h | reversion | 89.75 | -10.25 | 100 | 45.0 | -8.31 | -1.07 | -14.35 | 414 |
| 52 | VWAP momentum · 1h | momentum | 89.65 | -10.35 | 280 | 22.1 | -33.85 | -5.10 | -39.30 | 1282 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.08 | -10.92 | 62 | 19.4 | -6.93 | -0.76 | -19.82 | 241 |
| 55 | Donchian 20/10 · 1h | breakout | 88.83 | -11.17 | 58 | 19.0 | -0.12 | 0.19 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.50 | -1.42 | -28.63 | 319 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.65 | -5.15 | -36.60 | 701 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.83 | -12.17 | 102 | 13.7 | -9.08 | -1.02 | -21.49 | 338 |
| 60 | Three white soldiers | momentum | 87.47 | -12.53 | 140 | 17.9 | -48.15 | -23.43 | -48.15 | 591 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.21 | -1.29 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.58 | -1.29 | -23.91 | 413 |
| 63 | RSI(14) reversion | reversion | 74.75 | -25.25 | 360 | 28.3 | -72.80 | -18.28 | -72.80 | 1493 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.68 | -16.55 | -73.79 | 1667 |
| 65 | Squeeze breakout | breakout | 71.28 | -28.72 | 323 | 14.9 | -62.48 | -18.38 | -62.49 | 1233 |
| 66 | Donchian 55/20 | breakout | 70.57 | -29.43 | 328 | 18.0 | -67.65 | -14.49 | -67.65 | 1294 |
| 67 | Volume breakout | breakout | 70.28 | -29.72 | 260 | 13.1 | -62.65 | -18.06 | -62.65 | 901 |
| 68 | EMA 20/50 cross | trend | 70.24 | -29.76 | 327 | 19.9 | -77.06 | -15.37 | -77.06 | 1457 |
| 69 | VWAP reversion | reversion | 68.15 | -31.85 | 396 | 26.0 | -71.75 | -16.14 | -71.83 | 1438 |
| 70 | Supertrend | trend | 64.72 | -35.28 | 451 | 20.2 | -86.08 | -21.17 | -86.09 | 1912 |
| 71 | Keltner breakout | breakout | 63.16 | -36.84 | 443 | 14.4 | -83.75 | -27.79 | -83.75 | 1848 |
| 72 | Ichimoku | trend | 60.51 | -39.49 | 402 | 9.7 | -81.71 | -23.41 | -81.71 | 1746 |
| 73 | AI bee: Boozy | ai | 60.46 | -39.54 | 254 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 60.27 | -39.73 | 496 | 23.0 | -85.74 | -23.62 | -85.74 | 2092 |
| 75 | MFI reversion | reversion | 60.20 | -39.80 | 501 | 21.6 | -87.65 | -28.53 | -87.66 | 2122 |
| 76 | AI bee: Bizzy | ai | 58.62 | -41.38 | 819 | 8.9 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.25 | -42.75 | 534 | 10.3 | -89.50 | -34.97 | -89.50 | 2129 |
| 78 | Donchian 20/10 | breakout | 56.16 | -43.84 | 624 | 18.3 | -90.83 | -26.25 | -90.84 | 2668 |
| 79 | Trend pullback | trend | 55.41 | -44.59 | 581 | 15.0 | -90.98 | -27.00 | -90.98 | 2338 |
| 80 | RSI momentum | momentum | 55.29 | -44.71 | 592 | 17.2 | -90.29 | -25.80 | -90.29 | 2381 |
| 81 | MACD zero-line | trend | 54.59 | -45.41 | 574 | 15.0 | -91.47 | -30.29 | -91.47 | 2363 |
| 82 | Triple EMA stack | trend | 53.70 | -46.30 | 620 | 15.5 | -93.24 | -30.49 | -93.24 | 2622 |
| 83 | Bollinger breakout | breakout | 51.49 | -48.51 | 657 | 14.3 | -93.50 | -33.30 | -93.51 | 2818 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.29 | -98.66 | 5394 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.57 | -97.34 | 3546 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -36.58 | -96.48 | 3616 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -26.22 | -94.32 | 2699 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.53 | -99.35 | 5697 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.86 | -96.37 | 3623 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.86 | -99.73 | 6203 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.41 | -97.36 | 3686 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.71 | -98.49 | 4719 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.68 | -99.51 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -33.91 | -95.89 | 3749 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.56 | -34.60 | -95.56 | 4079 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.72 | -99.90 | 8320 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T02:55 | MFI reversion | buy | DOGE-USD | 15.06 | — | entry signal |
| 2026-10-11T02:55 | ADX DI cross | sell | DOGE-USD | 14.29 | -0.09 | exit signal |
| 2026-10-11T02:45 | Keltner breakout | buy | BTC-USD | 15.80 | — | entry signal |
| 2026-10-11T02:45 | Donchian 55/20 | buy | BTC-USD | 17.66 | — | entry signal |
| 2026-10-11T02:40 | MACD zero-line | buy | XRP-USD | 13.61 | — | entry signal |
| 2026-10-11T02:40 | MACD zero-line | buy | SOL-USD | 13.68 | — | entry signal |
| 2026-10-11T02:35 | Z-score reversion | sell | XRP-USD | 15.05 | -0.06 | exit signal |
| 2026-10-11T02:35 | RSI(14) reversion | sell | XRP-USD | 18.66 | -0.07 | exit signal |
| 2026-10-11T02:35 | Donchian 55/20 | buy | ETH-USD | 17.67 | — | entry signal |
| 2026-10-11T02:34 | AI bee: Bizzy | sell | DOGE-USD | 8.12 | -0.06 | Jev: sell (sell p=0.88) after 11 min |
| 2026-10-11T02:30 | ADX DI cross | sell | XRP-USD | 14.26 | -0.10 | exit signal |
| 2026-10-11T02:26 | ADX DI cross | buy | XRP-USD | 14.35 | — | entry signal |
| 2026-10-11T02:26 | Triple EMA stack | buy | BTC-USD | 13.44 | — | entry signal |
| 2026-10-11T02:26 | EMA 20/50 cross | buy | BTC-USD | 17.58 | — | entry signal |
| 2026-10-11T02:23 | AI bee: Bizzy | buy | DOGE-USD | 8.17 | — | Jev: buy (buy p=0.56) |
| 2026-10-11T02:10 | Keltner breakout | sell | DOGE-USD | 15.70 | -0.13 | stop-loss |
| 2026-10-11T02:10 | Bollinger breakout | sell | DOGE-USD | 12.82 | -0.11 | stop-loss |
| 2026-10-11T02:10 | Ichimoku | sell | DOGE-USD | 15.03 | -0.13 | stop-loss |
| 2026-10-11T02:10 | MACD zero-line | sell | SOL-USD | 13.61 | -0.11 | stop-loss |
| 2026-10-11T02:10 | MACD zero-line | sell | DOGE-USD | 13.62 | -0.12 | stop-loss |
| 2026-10-11T02:05 | Three white soldiers | sell | DOGE-USD | 21.82 | -0.11 | exit signal |
| 2026-10-11T02:05 | Volume breakout | sell | DOGE-USD | 17.49 | -0.11 | exit signal |
| 2026-10-11T02:05 | Bollinger breakout | sell | SOL-USD | 12.83 | -0.10 | stop-loss |
| 2026-10-11T02:05 | RSI momentum | sell | SOL-USD | 13.75 | -0.11 | stop-loss |
| 2026-10-11T02:00 | CCI reversion · 1h | buy | DOGE-USD | 6.91 | — | entry signal |
| 2026-10-11T02:00 | Williams %R · 1h | buy | DOGE-USD | 12.67 | — | entry signal |
| 2026-10-11T02:00 | Bollinger reversion · 1h | buy | XRP-USD | 2.33 | — | entry signal |
| 2026-10-11T02:00 | Bollinger reversion · 1h | buy | DOGE-USD | 13.26 | — | entry signal |
| 2026-10-11T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.41 | — | entry signal |
| 2026-10-11T02:00 | Triple EMA stack | buy | DOGE-USD | 13.45 | — | entry signal |
| 2026-10-11T01:55 | Three white soldiers | sell | XRP-USD | 21.79 | -0.15 | exit signal |
| 2026-10-11T01:55 | ADX DI cross | sell | SOL-USD | 14.28 | -0.10 | exit signal |
| 2026-10-11T01:55 | EMA 20/50 cross | buy | DOGE-USD | 17.59 | — | entry signal |
| 2026-10-11T01:50 | MFI reversion | sell | DOGE-USD | 15.05 | -0.02 | exit signal |
| 2026-10-11T01:50 | Trend pullback | buy | ETH-USD | 13.86 | — | entry signal |
| 2026-10-11T01:50 | MACD zero-line | buy | SOL-USD | 13.72 | — | entry signal |
| 2026-10-11T01:50 | Triple EMA stack | buy | ETH-USD | 13.46 | — | entry signal |
| 2026-10-11T01:50 | EMA 20/50 cross | buy | ETH-USD | 17.60 | — | entry signal |
| 2026-10-11T01:47 | AI bee: Boozy | sell | ETH-USD | 14.71 | -0.09 | Jev: sell |
| 2026-10-11T01:45 | Donchian 55/20 | sell | DOGE-USD | 17.57 | -0.14 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 02:55:05.000149+00:00 -> 2026-10-11 03:05:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
