# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T09:25:05.000184+00:00 · 18900 ticks

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

Today: 6705 decisions in 1341 calls, $0.0938 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T09:25 | 0 / 4 / 1 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T09:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T09:25 | 1 / 4 / 0 | COIN 76% |  |

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
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Hold BTC | benchmark | 99.22 | -0.78 | 0 | — | 27.32 | 3.27 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.86 | -1.90 | -14.61 | 340 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.84 | -6.44 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.70 | -3.30 | 39 | 12.8 | 5.26 | 0.80 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -7.12 | -2.54 | -10.13 | 256 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -2.28 | -0.19 | -13.84 | 260 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.82 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.79 | -4.21 | 113 | 23.9 | -15.31 | -2.46 | -17.64 | 466 |
| 34 | Supertrend · 1h | trend | 95.05 | -4.95 | 53 | 13.2 | 0.12 | 0.21 | -18.22 | 209 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.95 | 2.05 | -6.38 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.85 | -6.15 | 37 | 24.3 | 23.71 | 3.23 | -8.95 | 107 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.66 | -1.69 | -17.79 | 127 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.28 | -0.46 | -13.55 | 415 |
| 42 | Ichimoku · 1h | trend | 92.81 | -7.19 | 42 | 19.0 | -0.09 | 0.19 | -20.11 | 120 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.19 | 0.71 | -17.07 | 222 |
| 44 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 45 | Bollinger reversion · 1h | reversion | 92.51 | -7.49 | 76 | 36.8 | -21.01 | -5.02 | -23.37 | 317 |
| 46 | Bollinger breakout · 1h | breakout | 91.61 | -8.39 | 70 | 28.6 | 5.97 | 0.93 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.12 | -8.88 | 123 | 46.3 | -24.30 | -4.19 | -26.91 | 515 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -7.99 | -0.77 | -26.38 | 235 |
| 50 | Candlestick reversal · 1h | reversion | 90.12 | -9.88 | 116 | 31.9 | -26.63 | -5.21 | -28.40 | 514 |
| 51 | CCI reversion · 1h | reversion | 89.61 | -10.39 | 101 | 44.6 | -8.05 | -1.03 | -14.35 | 414 |
| 52 | VWAP momentum · 1h | momentum | 89.51 | -10.49 | 282 | 22.0 | -33.73 | -5.07 | -39.27 | 1283 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.84 | -11.15 | 64 | 18.8 | -7.26 | -0.80 | -19.96 | 241 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -13.20 | -1.52 | -28.62 | 322 |
| 56 | Donchian 20/10 · 1h | breakout | 88.74 | -11.26 | 59 | 18.6 | -0.65 | 0.13 | -17.72 | 224 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.41 | -5.10 | -36.59 | 700 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.80 | -12.20 | 102 | 13.7 | -9.77 | -1.12 | -21.57 | 338 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.51 | -23.65 | -48.51 | 592 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.21 | -1.29 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.83 | -1.33 | -24.05 | 413 |
| 63 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.69 | -16.56 | -73.80 | 1669 |
| 64 | RSI(14) reversion | reversion | 74.07 | -25.93 | 367 | 27.8 | -73.35 | -18.49 | -73.35 | 1505 |
| 65 | Squeeze breakout | breakout | 70.86 | -29.14 | 326 | 14.7 | -62.47 | -18.45 | -62.47 | 1231 |
| 66 | Donchian 55/20 | breakout | 70.30 | -29.70 | 331 | 17.8 | -67.51 | -14.43 | -67.51 | 1291 |
| 67 | Volume breakout | breakout | 70.17 | -29.83 | 261 | 13.0 | -62.64 | -18.06 | -62.66 | 901 |
| 68 | EMA 20/50 cross | trend | 69.88 | -30.12 | 331 | 19.6 | -77.02 | -15.37 | -77.02 | 1455 |
| 69 | VWAP reversion | reversion | 67.84 | -32.16 | 401 | 25.9 | -71.88 | -16.20 | -71.94 | 1443 |
| 70 | Supertrend | trend | 63.79 | -36.21 | 460 | 19.8 | -86.17 | -21.33 | -86.17 | 1913 |
| 71 | Keltner breakout | breakout | 62.86 | -37.14 | 446 | 14.3 | -83.82 | -27.98 | -83.82 | 1849 |
| 72 | AI bee: Boozy | ai | 60.46 | -39.54 | 254 | 5.1 | — | — | — | — |
| 73 | Ichimoku | trend | 60.28 | -39.72 | 404 | 9.7 | -81.71 | -23.41 | -81.71 | 1746 |
| 74 | Z-score reversion | reversion | 59.56 | -40.44 | 504 | 22.6 | -85.69 | -23.79 | -85.69 | 2092 |
| 75 | MFI reversion | reversion | 59.19 | -40.81 | 513 | 21.2 | -87.67 | -28.87 | -87.67 | 2122 |
| 76 | AI bee: Bizzy | ai | 58.16 | -41.84 | 827 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.41 | -43.59 | 542 | 10.1 | -89.42 | -35.76 | -89.42 | 2125 |
| 78 | Donchian 20/10 | breakout | 55.34 | -44.66 | 631 | 18.1 | -90.88 | -26.52 | -90.88 | 2669 |
| 79 | Trend pullback | trend | 55.26 | -44.74 | 583 | 14.9 | -91.01 | -27.10 | -91.01 | 2339 |
| 80 | RSI momentum | momentum | 54.14 | -45.86 | 603 | 16.9 | -90.30 | -25.90 | -90.31 | 2381 |
| 81 | MACD zero-line | trend | 53.62 | -46.38 | 584 | 14.7 | -91.51 | -30.58 | -91.51 | 2364 |
| 82 | Triple EMA stack | trend | 53.34 | -46.66 | 625 | 15.4 | -93.15 | -30.22 | -93.15 | 2614 |
| 83 | Bollinger breakout | breakout | 50.72 | -49.28 | 665 | 14.1 | -93.55 | -33.69 | -93.55 | 2820 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.67 | -31.61 | -98.67 | 5405 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -34.30 | -97.39 | 3552 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.40 | -36.08 | -96.40 | 3603 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.19 | -25.88 | -94.19 | 2682 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -38.13 | -99.36 | 5708 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -32.04 | -96.39 | 3626 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.55 | -99.73 | 6209 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.33 | -38.05 | -97.33 | 3680 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -38.28 | -98.48 | 4719 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.51 | -99.52 | 6158 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -34.51 | -95.94 | 3755 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.62 | -35.32 | -95.62 | 4090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.63 | -99.90 | 8323 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T09:25 | EMA 20/50 cross | sell | BTC-USD | 17.39 | -0.11 | exit signal |
| 2026-10-11T09:23 | AI bee: Bizzy | sell | SOL-USD | 8.72 | -0.08 | Jev: sell (sell p=0.91) after 10 min |
| 2026-10-11T09:20 | Bollinger breakout | sell | SOL-USD | 12.65 | -0.09 | exit signal |
| 2026-10-11T09:20 | Bollinger breakout | sell | ETH-USD | 12.64 | -0.09 | exit signal |
| 2026-10-11T09:19 | AI bee: Bizzy | sell | ETH-USD | 8.22 | -0.06 | Jev: sell (sell p=0.78) after 10 min |
| 2026-10-11T09:15 | MFI reversion | sell | SOL-USD | 14.77 | -0.07 | exit signal |
| 2026-10-11T09:15 | Donchian 20/10 | buy | DOGE-USD | 13.86 | — | entry |
| 2026-10-11T09:15 | RSI momentum | buy | DOGE-USD | 13.55 | — | entry |
| 2026-10-11T09:15 | Supertrend | buy | DOGE-USD | 15.96 | — | entry |
| 2026-10-11T09:15 | MACD zero-line | buy | SOL-USD | 13.42 | — | entry signal |
| 2026-10-11T09:13 | AI bee: Bizzy | buy | SOL-USD | 8.81 | — | Jev: buy (buy p=0.60) |
| 2026-10-11T09:10 | Bollinger breakout | buy | XRP-USD | 12.73 | — | entry signal |
| 2026-10-11T09:10 | Bollinger breakout | buy | ETH-USD | 12.73 | — | entry signal |
| 2026-10-11T09:10 | Donchian 20/10 | buy | SOL-USD | 13.88 | — | entry signal |
| 2026-10-11T09:10 | Donchian 20/10 | buy | ETH-USD | 13.88 | — | entry signal |
| 2026-10-11T09:10 | RSI momentum | buy | XRP-USD | 13.56 | — | entry signal |
| 2026-10-11T09:10 | ADX DI cross | buy | ETH-USD | 14.12 | — | entry signal |
| 2026-10-11T09:09 | AI bee: Bizzy | buy | ETH-USD | 8.27 | — | Jev: buy (buy p=0.57) |
| 2026-10-11T09:05 | Bollinger breakout | buy | SOL-USD | 12.74 | — | entry signal |
| 2026-10-11T09:00 | Trend pullback | sell | BTC-USD | 13.75 | -0.09 | exit signal |
| 2026-10-11T09:00 | ADX DI cross | sell | BTC-USD | 14.05 | -0.09 | exit signal |
| 2026-10-11T09:00 | MACD zero-line | buy | XRP-USD | 13.44 | — | entry signal |
| 2026-10-11T09:00 | MACD zero-line | buy | DOGE-USD | 13.44 | — | entry |
| 2026-10-11T09:00 | Triple EMA stack | sell | BTC-USD | 13.27 | -0.09 | exit signal |
| 2026-10-11T08:50 | Squeeze breakout | buy | DOGE-USD | 17.73 | — | entry signal |
| 2026-10-11T08:50 | Bollinger breakout | buy | DOGE-USD | 12.75 | — | entry signal |
| 2026-10-11T08:48 | AI bee: Bizzy | sell | DOGE-USD | 8.80 | -0.05 | Jev: sell (sell p=0.60) after 10 min |
| 2026-10-11T08:45 | Triple EMA stack | buy | BTC-USD | 13.36 | — | entry signal |
| 2026-10-11T08:40 | Trend pullback | buy | BTC-USD | 13.84 | — | entry signal |
| 2026-10-11T08:38 | AI bee: Bizzy | buy | DOGE-USD | 8.85 | — | Jev: buy (buy p=0.61) |
| 2026-10-11T08:35 | MFI reversion | sell | DOGE-USD | 14.73 | -0.10 | exit signal |
| 2026-10-11T08:35 | ADX DI cross | buy | BTC-USD | 14.14 | — | entry signal |
| 2026-10-11T08:30 | ADX DI cross | sell | BTC-USD | 14.08 | -0.08 | exit signal |
| 2026-10-11T08:20 | MFI reversion | buy | DOGE-USD | 14.83 | — | entry signal |
| 2026-10-11T08:05 | MFI reversion | buy | SOL-USD | 14.84 | — | entry signal |
| 2026-10-11T08:05 | ADX DI cross | buy | BTC-USD | 14.16 | — | entry signal |
| 2026-10-11T07:40 | Donchian 20/10 | sell | BTC-USD | 13.91 | -0.09 | exit signal |
| 2026-10-11T07:40 | RSI momentum | sell | BTC-USD | 13.69 | -0.09 | exit signal |
| 2026-10-11T07:40 | ADX DI cross | sell | BTC-USD | 14.23 | -0.08 | exit signal |
| 2026-10-11T07:40 | Triple EMA stack | sell | BTC-USD | 13.29 | -0.08 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 09:25:05.000184+00:00 -> 2026-10-11 09:35:05.000184+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
