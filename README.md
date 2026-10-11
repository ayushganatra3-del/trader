# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T01:55:05.000146+00:00 · 18554 ticks

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

Today: 1515 decisions in 303 calls, $0.0212 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T01:55 | 0 / 1 / 4 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T01:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T01:55 | 1 / 3 / 1 | COIN 76% |  |

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
| 18 | Hold BTC | benchmark | 99.19 | -0.81 | 0 | — | 27.12 | 3.25 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.92 | -1.91 | -14.61 | 342 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.51 | -6.31 | -25.39 | 169 |
| 27 | EMA 20/50 cross · 1h | trend | 96.70 | -3.31 | 39 | 12.8 | 5.50 | 0.82 | -19.85 | 134 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -7.94 | -2.79 | -10.03 | 258 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -2.64 | -0.25 | -13.84 | 262 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.72 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.85 | -4.15 | 111 | 24.3 | -15.62 | -2.52 | -17.84 | 468 |
| 34 | Supertrend · 1h | trend | 95.26 | -4.74 | 52 | 13.5 | -0.16 | 0.17 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.01 | -5.99 | 36 | 25.0 | 23.92 | 3.26 | -8.85 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.19 | -1.77 | -17.79 | 131 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.92 | -0.53 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.94 | -7.06 | 41 | 19.5 | -0.14 | 0.18 | -20.02 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -2.07 | -0.23 | -12.40 | 401 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.28 | -4.83 | -23.18 | 312 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.17 | 0.71 | -17.07 | 222 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.73 | -8.27 | 68 | 29.4 | 6.30 | 0.97 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.68 | -8.32 | 120 | 47.5 | -24.16 | -4.16 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.49 | -0.84 | -26.38 | 235 |
| 50 | Candlestick reversal · 1h | reversion | 90.22 | -9.79 | 116 | 31.9 | -27.19 | -5.32 | -29.01 | 516 |
| 51 | CCI reversion · 1h | reversion | 89.78 | -10.22 | 100 | 45.0 | -8.30 | -1.07 | -14.35 | 413 |
| 52 | VWAP momentum · 1h | momentum | 89.68 | -10.32 | 280 | 22.1 | -33.81 | -5.09 | -39.30 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.07 | -10.93 | 62 | 19.4 | -7.01 | -0.77 | -19.82 | 241 |
| 55 | Donchian 20/10 · 1h | breakout | 88.84 | -11.16 | 58 | 19.0 | -0.25 | 0.18 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.50 | -1.42 | -28.63 | 319 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.65 | -5.15 | -36.60 | 701 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.82 | -12.18 | 102 | 13.7 | -9.05 | -1.02 | -21.49 | 337 |
| 60 | Three white soldiers | momentum | 87.56 | -12.44 | 139 | 18.0 | -48.01 | -23.25 | -48.01 | 590 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.59 | -1.29 | -23.91 | 413 |
| 63 | RSI(14) reversion | reversion | 74.79 | -25.21 | 359 | 28.4 | -72.82 | -18.27 | -72.84 | 1494 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.68 | -16.55 | -73.79 | 1667 |
| 65 | Squeeze breakout | breakout | 71.27 | -28.73 | 323 | 14.9 | -62.54 | -18.41 | -62.54 | 1233 |
| 66 | Donchian 55/20 | breakout | 70.69 | -29.31 | 328 | 18.0 | -67.60 | -14.46 | -67.60 | 1292 |
| 67 | Volume breakout | breakout | 70.36 | -29.64 | 259 | 13.1 | -62.61 | -18.03 | -62.62 | 901 |
| 68 | EMA 20/50 cross | trend | 70.30 | -29.70 | 327 | 19.9 | -77.17 | -15.43 | -77.17 | 1459 |
| 69 | VWAP reversion | reversion | 68.15 | -31.85 | 396 | 26.0 | -71.75 | -16.14 | -71.83 | 1437 |
| 70 | Supertrend | trend | 64.71 | -35.29 | 451 | 20.2 | -86.08 | -21.18 | -86.08 | 1912 |
| 71 | Keltner breakout | breakout | 63.28 | -36.72 | 442 | 14.5 | -83.73 | -27.73 | -83.73 | 1847 |
| 72 | Ichimoku | trend | 60.58 | -39.42 | 401 | 9.7 | -81.69 | -23.37 | -81.69 | 1746 |
| 73 | AI bee: Boozy | ai | 60.46 | -39.54 | 254 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 60.30 | -39.70 | 495 | 23.0 | -85.73 | -23.61 | -85.73 | 2092 |
| 75 | MFI reversion | reversion | 60.25 | -39.75 | 501 | 21.6 | -87.65 | -28.50 | -87.66 | 2121 |
| 76 | AI bee: Bizzy | ai | 58.68 | -41.32 | 818 | 8.9 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.41 | -42.59 | 532 | 10.3 | -89.34 | -34.92 | -89.34 | 2121 |
| 78 | Donchian 20/10 | breakout | 56.15 | -43.84 | 624 | 18.3 | -90.83 | -26.25 | -90.83 | 2668 |
| 79 | Trend pullback | trend | 55.40 | -44.60 | 581 | 15.0 | -90.98 | -27.01 | -90.98 | 2338 |
| 80 | RSI momentum | momentum | 55.33 | -44.67 | 591 | 17.3 | -90.29 | -25.79 | -90.29 | 2382 |
| 81 | MACD zero-line | trend | 54.80 | -45.20 | 572 | 15.0 | -91.47 | -30.18 | -91.47 | 2364 |
| 82 | Triple EMA stack | trend | 53.78 | -46.22 | 620 | 15.5 | -93.19 | -30.35 | -93.19 | 2618 |
| 83 | Bollinger breakout | breakout | 51.58 | -48.42 | 655 | 14.4 | -93.50 | -33.22 | -93.50 | 2818 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.16 | -98.66 | 5394 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.46 | -97.34 | 3544 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -36.56 | -96.48 | 3616 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -26.27 | -94.34 | 2700 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.48 | -99.36 | 5702 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.86 | -96.37 | 3623 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.75 | -99.73 | 6205 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.44 | -97.36 | 3686 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.69 | -98.49 | 4719 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.70 | -99.52 | 6150 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -33.91 | -95.89 | 3749 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.56 | -34.60 | -95.56 | 4079 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.39 | -99.90 | 8316 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-11T01:43 | AI bee: Bizzy | sell | ETH-USD | 8.18 | -0.05 | Jev: sell (sell p=0.66) after 10 min |
| 2026-10-11T01:40 | Three white soldiers | buy | XRP-USD | 21.94 | — | entry signal |
| 2026-10-11T01:40 | Donchian 55/20 | buy | DOGE-USD | 17.71 | — | entry signal |
| 2026-10-11T01:40 | Supertrend | buy | XRP-USD | 16.20 | — | entry signal |
| 2026-10-11T01:40 | MACD zero-line | buy | BTC-USD | 13.73 | — | entry signal |
| 2026-10-11T01:37 | AI bee: Bizzy | sell | DOGE-USD | 9.13 | -0.03 | Jev: sell (sell p=0.53) after 13 min |
| 2026-10-11T01:35 | Z-score reversion | sell | SOL-USD | 15.08 | -0.06 | exit signal |
| 2026-10-11T01:35 | Z-score reversion | sell | BTC-USD | 12.06 | -0.06 | exit signal |
| 2026-10-11T01:35 | Keltner breakout | buy | DOGE-USD | 15.83 | — | entry |
| 2026-10-11T01:35 | Bollinger breakout | buy | SOL-USD | 12.93 | — | entry signal |
| 2026-10-11T01:35 | Bollinger breakout | buy | DOGE-USD | 12.93 | — | entry |
| 2026-10-11T01:35 | Bollinger breakout | buy | BTC-USD | 12.93 | — | entry signal |
| 2026-10-11T01:35 | Donchian 20/10 | buy | ETH-USD | 14.07 | — | entry signal |
| 2026-10-11T01:35 | Donchian 20/10 | buy | BTC-USD | 14.07 | — | entry signal |
| 2026-10-11T01:35 | RSI momentum | buy | SOL-USD | 13.86 | — | entry signal |
| 2026-10-11T01:35 | RSI momentum | buy | BTC-USD | 13.86 | — | entry signal |
| 2026-10-11T01:35 | Ichimoku | buy | DOGE-USD | 15.16 | — | entry signal |
| 2026-10-11T01:35 | Supertrend | buy | ETH-USD | 16.22 | — | entry signal |
| 2026-10-11T01:35 | Supertrend | buy | BTC-USD | 16.22 | — | entry signal |
| 2026-10-11T01:35 | MACD zero-line | buy | DOGE-USD | 13.74 | — | entry signal |
| 2026-10-11T01:33 | AI bee: Bizzy | buy | ETH-USD | 8.24 | — | Jev: buy (buy p=0.56) |
| 2026-10-11T01:32 | AI bee: Boozy | buy | ETH-USD | 14.80 | — | Jev: buy (buy p=0.76) |
| 2026-10-11T01:30 | Z-score reversion | sell | DOGE-USD | 15.04 | -0.06 | exit signal |
| 2026-10-11T01:30 | RSI(14) reversion | sell | SOL-USD | 18.68 | -0.08 | exit signal |
| 2026-10-11T01:30 | RSI(14) reversion | sell | DOGE-USD | 18.66 | -0.07 | exit signal |
| 2026-10-11T01:30 | Volume breakout | buy | DOGE-USD | 17.60 | — | entry signal |
| 2026-10-11T01:30 | Squeeze breakout | buy | ETH-USD | 17.83 | — | entry signal |
| 2026-10-11T01:30 | Bollinger breakout | buy | ETH-USD | 12.94 | — | entry signal |
| 2026-10-11T01:30 | Donchian 20/10 | buy | DOGE-USD | 14.07 | — | entry signal |
| 2026-10-11T01:30 | RSI momentum | buy | ETH-USD | 13.88 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 01:55:05.000146+00:00 -> 2026-10-11 02:05:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
