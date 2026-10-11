# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T06:55:05.000151+00:00 · 18782 ticks

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

Today: 4935 decisions in 987 calls, $0.0690 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T06:55 | 1 / 2 / 2 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T06:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T06:55 | 3 / 2 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.56 | -2.30 | -13.79 | 118 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -15.29 | -2.51 | -23.22 | 71 |
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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.16 | 2.41 | -1.64 | 87 |
| 17 | Hold BTC | benchmark | 99.35 | -0.65 | 0 | — | 27.13 | 3.25 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 19 | Stochastic reversion · 1h | reversion | 99.17 | -0.82 | 89 | 55.1 | -9.97 | -1.93 | -14.61 | 342 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.45 | -6.28 | -25.39 | 169 |
| 27 | EMA 20/50 cross · 1h | trend | 96.72 | -3.29 | 39 | 12.8 | 5.58 | 0.83 | -19.85 | 134 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -7.84 | -2.76 | -10.88 | 258 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -2.48 | -0.22 | -13.84 | 261 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.78 | -0.20 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.79 | -4.21 | 113 | 23.9 | -15.24 | -2.45 | -17.63 | 466 |
| 34 | Supertrend · 1h | trend | 95.12 | -4.88 | 53 | 13.2 | 0.22 | 0.22 | -18.22 | 209 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.95 | 2.05 | -6.38 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.85 | -6.15 | 37 | 24.3 | 23.83 | 3.25 | -8.95 | 106 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.56 | -1.66 | -17.79 | 127 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -1.80 | -0.28 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.62 | -0.51 | -13.43 | 421 |
| 42 | Ichimoku · 1h | trend | 92.81 | -7.19 | 42 | 19.0 | -0.09 | 0.19 | -20.11 | 120 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.19 | 0.71 | -17.07 | 222 |
| 44 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 45 | Bollinger reversion · 1h | reversion | 92.54 | -7.46 | 76 | 36.8 | -20.94 | -5.00 | -23.37 | 317 |
| 46 | Bollinger breakout · 1h | breakout | 91.61 | -8.39 | 70 | 28.6 | 6.05 | 0.94 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.24 | -8.76 | 122 | 46.7 | -24.23 | -4.18 | -26.91 | 515 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.40 | -0.83 | -26.38 | 235 |
| 50 | Candlestick reversal · 1h | reversion | 90.21 | -9.79 | 116 | 31.9 | -26.65 | -5.21 | -28.56 | 513 |
| 51 | CCI reversion · 1h | reversion | 89.66 | -10.34 | 101 | 44.6 | -8.00 | -1.02 | -14.35 | 413 |
| 52 | VWAP momentum · 1h | momentum | 89.51 | -10.49 | 282 | 22.0 | -34.00 | -5.13 | -39.26 | 1284 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.22 | -19.78 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.84 | -11.15 | 64 | 18.8 | -7.22 | -0.80 | -19.96 | 241 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.32 | -1.40 | -28.62 | 319 |
| 56 | Donchian 20/10 · 1h | breakout | 88.74 | -11.26 | 59 | 18.6 | -0.52 | 0.14 | -17.72 | 224 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.64 | -5.15 | -36.59 | 701 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.82 | -12.18 | 102 | 13.7 | -9.41 | -1.07 | -21.57 | 337 |
| 60 | Three white soldiers | momentum | 87.42 | -12.58 | 140 | 17.9 | -48.13 | -23.42 | -48.14 | 592 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.21 | -1.29 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -11.14 | -1.37 | -24.12 | 412 |
| 63 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.71 | -16.57 | -73.82 | 1670 |
| 64 | RSI(14) reversion | reversion | 74.07 | -25.93 | 367 | 27.8 | -73.03 | -18.47 | -73.03 | 1499 |
| 65 | Squeeze breakout | breakout | 71.14 | -28.86 | 324 | 14.8 | -62.32 | -18.32 | -62.32 | 1229 |
| 66 | Donchian 55/20 | breakout | 70.37 | -29.64 | 330 | 17.9 | -67.48 | -14.41 | -67.48 | 1291 |
| 67 | Volume breakout | breakout | 70.23 | -29.77 | 260 | 13.1 | -62.59 | -18.03 | -62.61 | 900 |
| 68 | EMA 20/50 cross | trend | 69.96 | -30.04 | 330 | 19.7 | -77.10 | -15.41 | -77.11 | 1457 |
| 69 | VWAP reversion | reversion | 67.84 | -32.16 | 401 | 25.9 | -72.18 | -16.23 | -72.23 | 1450 |
| 70 | Supertrend | trend | 64.20 | -35.80 | 455 | 20.0 | -86.19 | -21.35 | -86.22 | 1917 |
| 71 | Keltner breakout | breakout | 63.02 | -36.98 | 444 | 14.4 | -83.71 | -27.76 | -83.71 | 1847 |
| 72 | AI bee: Boozy | ai | 60.46 | -39.54 | 254 | 5.1 | — | — | — | — |
| 73 | Ichimoku | trend | 60.43 | -39.57 | 402 | 9.7 | -81.70 | -23.40 | -81.70 | 1747 |
| 74 | Z-score reversion | reversion | 59.61 | -40.39 | 504 | 22.6 | -85.83 | -23.85 | -85.83 | 2095 |
| 75 | MFI reversion | reversion | 59.45 | -40.55 | 509 | 21.4 | -87.76 | -28.84 | -87.77 | 2127 |
| 76 | AI bee: Bizzy | ai | 58.35 | -41.65 | 824 | 8.9 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.78 | -43.22 | 538 | 10.2 | -89.40 | -35.54 | -89.40 | 2125 |
| 78 | Donchian 20/10 | breakout | 55.66 | -44.34 | 629 | 18.1 | -90.83 | -26.38 | -90.83 | 2666 |
| 79 | Trend pullback | trend | 55.35 | -44.66 | 582 | 14.9 | -90.99 | -27.04 | -90.99 | 2338 |
| 80 | RSI momentum | momentum | 54.59 | -45.41 | 598 | 17.1 | -90.33 | -25.99 | -90.33 | 2384 |
| 81 | MACD zero-line | trend | 53.98 | -46.02 | 581 | 14.8 | -91.53 | -30.60 | -91.53 | 2366 |
| 82 | Triple EMA stack | trend | 53.49 | -46.52 | 623 | 15.4 | -93.14 | -30.25 | -93.15 | 2614 |
| 83 | Bollinger breakout | breakout | 51.23 | -48.77 | 659 | 14.3 | -93.49 | -33.33 | -93.49 | 2816 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.67 | -31.59 | -98.67 | 5407 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -34.05 | -97.37 | 3549 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.40 | -36.12 | -96.40 | 3603 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.22 | -26.08 | -94.22 | 2685 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.82 | -99.35 | 5701 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -31.98 | -96.38 | 3625 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.31 | -99.73 | 6208 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.33 | -38.01 | -97.33 | 3680 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -38.27 | -98.50 | 4724 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.45 | -99.52 | 6161 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -34.43 | -95.95 | 3758 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.63 | -35.28 | -95.63 | 4091 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.11 | -99.90 | 8316 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T06:55 | AI bee: Bizzy | sell | BTC-USD | 8.29 | -0.05 | Jev: sell (sell p=0.63) after 10 min |
| 2026-10-11T06:55 | Ichimoku | buy | XRP-USD | 15.12 | — | entry signal |
| 2026-10-11T06:55 | MACD zero-line | buy | DOGE-USD | 13.51 | — | entry signal |
| 2026-10-11T06:53 | AI bee: Bizzy | sell | SOL-USD | 8.67 | -0.03 | Jev: sell (sell p=0.51) after 14 min |
| 2026-10-11T06:50 | VWAP reversion | sell | SOL-USD | 16.93 | -0.01 | exit signal |
| 2026-10-11T06:50 | Volume breakout | buy | BTC-USD | 17.57 | — | entry signal |
| 2026-10-11T06:50 | Squeeze breakout | buy | XRP-USD | 17.80 | — | entry signal |
| 2026-10-11T06:50 | Keltner breakout | buy | SOL-USD | 15.77 | — | entry signal |
| 2026-10-11T06:50 | Bollinger breakout | buy | XRP-USD | 12.84 | — | entry signal |
| 2026-10-11T06:50 | Bollinger breakout | buy | SOL-USD | 12.84 | — | entry signal |
| 2026-10-11T06:50 | Bollinger breakout | buy | DOGE-USD | 12.84 | — | entry signal |
| 2026-10-11T06:50 | Donchian 55/20 | buy | BTC-USD | 17.61 | — | entry signal |
| 2026-10-11T06:50 | Donchian 20/10 | buy | SOL-USD | 13.93 | — | entry signal |
| 2026-10-11T06:50 | RSI momentum | buy | XRP-USD | 13.62 | — | entry signal |
| 2026-10-11T06:50 | RSI momentum | buy | DOGE-USD | 13.68 | — | entry signal |
| 2026-10-11T06:50 | MACD zero-line | buy | SOL-USD | 13.52 | — | entry signal |
| 2026-10-11T06:45 | AI bee: Bizzy | buy | BTC-USD | 8.34 | — | Jev: buy (buy p=0.57) |
| 2026-10-11T06:45 | RSI(14) reversion | sell | SOL-USD | 18.51 | -0.05 | exit signal |
| 2026-10-11T06:45 | RSI momentum | buy | SOL-USD | 13.68 | — | entry signal |
| 2026-10-11T06:45 | Ichimoku | buy | SOL-USD | 15.13 | — | entry signal |
| 2026-10-11T06:45 | MACD zero-line | buy | XRP-USD | 13.53 | — | entry signal |
| 2026-10-11T06:40 | Z-score reversion | sell | SOL-USD | 14.87 | -0.09 | exit signal |
| 2026-10-11T06:40 | Three white soldiers | buy | BTC-USD | 21.87 | — | entry signal |
| 2026-10-11T06:40 | Bollinger breakout | buy | BTC-USD | 12.85 | — | entry signal |
| 2026-10-11T06:40 | ADX DI cross | buy | XRP-USD | 14.20 | — | entry signal |
| 2026-10-11T06:39 | AI bee: Bizzy | buy | SOL-USD | 8.71 | — | Jev: buy (buy p=0.60) |
| 2026-10-11T06:30 | MFI reversion | buy | XRP-USD | 14.88 | — | entry signal |
| 2026-10-11T06:30 | MFI reversion | buy | DOGE-USD | 14.88 | — | entry signal |
| 2026-10-11T06:10 | MACD zero-line | sell | BTC-USD | 13.52 | -0.08 | exit signal |
| 2026-10-11T05:55 | MACD zero-line | sell | DOGE-USD | 13.47 | -0.10 | exit signal |
| 2026-10-11T05:50 | RSI momentum | sell | ETH-USD | 13.67 | -0.11 | stop-loss |
| 2026-10-11T05:50 | MACD zero-line | sell | ETH-USD | 13.48 | -0.11 | stop-loss |
| 2026-10-11T05:45 | Donchian 20/10 | sell | XRP-USD | 13.88 | -0.12 | stop-loss |
| 2026-10-11T05:45 | RSI momentum | sell | XRP-USD | 13.66 | -0.12 | stop-loss |
| 2026-10-11T05:45 | ADX DI cross | sell | ETH-USD | 14.21 | -0.09 | exit signal |
| 2026-10-11T05:40 | ADX DI cross | sell | SOL-USD | 14.15 | -0.10 | exit signal |
| 2026-10-11T05:35 | AI bee: Bizzy | sell | SOL-USD | 8.16 | -0.05 | Jev: sell (sell p=0.81) after 11 min |
| 2026-10-11T05:30 | Supertrend | buy | ETH-USD | 3.20 | — | rebalance up |
| 2026-10-11T05:30 | Supertrend | sell | BTC-USD | 3.20 | -0.02 | rebalance down |
| 2026-10-11T05:30 | Triple EMA stack | buy | BTC-USD | 13.38 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 06:55:05.000151+00:00 -> 2026-10-11 07:05:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
