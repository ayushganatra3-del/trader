# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T11:55:05.000152+00:00 · 19019 ticks

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

Today: 8490 decisions in 1698 calls, $0.1188 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T11:55 | 4 / 0 / 1 | SOL-USD 15%, BTC-USD 15%, NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T11:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T11:55 | 5 / 0 / 0 | ETH-USD 77% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.44 | -2.26 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -15.27 | -2.51 | -23.22 | 71 |
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
| 17 | Hold BTC | benchmark | 99.41 | -0.59 | 0 | — | 27.85 | 3.33 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.86 | -1.90 | -14.61 | 340 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.64 | -6.36 | -25.39 | 169 |
| 27 | EMA 20/50 cross · 1h | trend | 96.72 | -3.28 | 39 | 12.8 | 6.81 | 0.96 | -19.85 | 131 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -5.83 | -1.89 | -9.31 | 252 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.88 | -0.13 | -13.84 | 259 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.81 | -0.20 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.79 | -4.21 | 113 | 23.9 | -14.99 | -2.40 | -17.27 | 464 |
| 34 | Supertrend · 1h | trend | 95.12 | -4.88 | 53 | 13.2 | 0.22 | 0.22 | -18.22 | 209 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.85 | -6.15 | 37 | 24.3 | 23.83 | 3.25 | -8.95 | 106 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.38 | -1.63 | -17.79 | 129 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.19 | -0.37 | -9.03 | 152 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -1.64 | -0.15 | -13.04 | 426 |
| 42 | Ichimoku · 1h | trend | 92.81 | -7.19 | 42 | 19.0 | -0.09 | 0.19 | -20.11 | 120 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 5.06 | 0.81 | -17.07 | 220 |
| 44 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 45 | Bollinger reversion · 1h | reversion | 92.53 | -7.47 | 76 | 36.8 | -20.96 | -5.01 | -23.37 | 317 |
| 46 | Bollinger breakout · 1h | breakout | 91.61 | -8.39 | 70 | 28.6 | 6.05 | 0.94 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.18 | -8.82 | 123 | 46.3 | -24.35 | -4.20 | -26.91 | 516 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -7.63 | -0.73 | -26.38 | 234 |
| 50 | Candlestick reversal · 1h | reversion | 90.16 | -9.85 | 116 | 31.9 | -26.73 | -5.23 | -28.56 | 514 |
| 51 | CCI reversion · 1h | reversion | 89.61 | -10.39 | 101 | 44.6 | -8.05 | -1.03 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.48 | -10.52 | 283 | 21.9 | -33.62 | -5.05 | -39.30 | 1281 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.84 | -11.15 | 64 | 18.8 | -7.15 | -0.79 | -19.96 | 241 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.45 | -1.28 | -28.63 | 316 |
| 56 | Donchian 20/10 · 1h | breakout | 88.74 | -11.26 | 59 | 18.6 | -0.52 | 0.14 | -17.72 | 224 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.43 | -5.10 | -36.60 | 700 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.80 | -12.20 | 103 | 13.6 | -9.47 | -1.08 | -21.58 | 337 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.05 | -23.30 | -48.07 | 590 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.21 | -1.29 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.89 | -1.33 | -23.91 | 413 |
| 63 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.68 | -16.55 | -73.79 | 1667 |
| 64 | RSI(14) reversion | reversion | 73.91 | -26.09 | 369 | 27.6 | -72.96 | -18.46 | -72.96 | 1497 |
| 65 | Squeeze breakout | breakout | 70.76 | -29.24 | 327 | 14.7 | -62.46 | -18.44 | -62.47 | 1231 |
| 66 | Donchian 55/20 | breakout | 70.24 | -29.76 | 331 | 17.8 | -67.53 | -14.44 | -67.53 | 1292 |
| 67 | Volume breakout | breakout | 70.13 | -29.87 | 261 | 13.0 | -62.67 | -18.08 | -62.69 | 902 |
| 68 | EMA 20/50 cross | trend | 69.74 | -30.26 | 331 | 19.6 | -77.07 | -15.40 | -77.07 | 1458 |
| 69 | VWAP reversion | reversion | 67.84 | -32.16 | 402 | 25.9 | -71.81 | -16.22 | -71.86 | 1445 |
| 70 | Supertrend | trend | 63.56 | -36.44 | 461 | 19.7 | -86.21 | -21.38 | -86.22 | 1918 |
| 71 | Keltner breakout | breakout | 62.70 | -37.30 | 446 | 14.3 | -83.70 | -27.76 | -83.71 | 1849 |
| 72 | AI bee: Boozy | ai | 60.42 | -39.58 | 254 | 5.1 | — | — | — | — |
| 73 | Ichimoku | trend | 60.15 | -39.85 | 405 | 9.6 | -81.72 | -23.43 | -81.72 | 1747 |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.42 | -23.43 | -85.42 | 2085 |
| 75 | MFI reversion | reversion | 59.15 | -40.84 | 514 | 21.2 | -87.68 | -28.96 | -87.69 | 2125 |
| 76 | AI bee: Bizzy | ai | 57.97 | -42.03 | 830 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.36 | -43.64 | 543 | 10.1 | -89.39 | -35.73 | -89.39 | 2123 |
| 78 | Trend pullback | trend | 55.26 | -44.74 | 583 | 14.9 | -90.99 | -27.07 | -90.99 | 2338 |
| 79 | Donchian 20/10 | breakout | 55.06 | -44.94 | 634 | 18.0 | -90.84 | -26.44 | -90.85 | 2669 |
| 80 | RSI momentum | momentum | 53.91 | -46.09 | 605 | 16.9 | -90.34 | -25.97 | -90.35 | 2386 |
| 81 | Triple EMA stack | trend | 53.27 | -46.73 | 625 | 15.4 | -93.14 | -30.26 | -93.14 | 2615 |
| 82 | MACD zero-line | trend | 53.17 | -46.83 | 589 | 14.6 | -91.57 | -30.66 | -91.57 | 2370 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.60 | -98.66 | 5399 |
| 84 | Bollinger breakout | breakout | 50.50 | -49.50 | 667 | 14.1 | -93.54 | -33.54 | -93.54 | 2821 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -34.30 | -97.39 | 3554 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -36.27 | -96.43 | 3610 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.11 | -25.74 | -94.11 | 2677 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -38.16 | -99.35 | 5700 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -32.02 | -96.38 | 3625 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.59 | -99.73 | 6213 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -38.20 | -97.34 | 3682 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -38.29 | -98.48 | 4718 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.63 | -99.52 | 6160 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -34.61 | -95.91 | 3755 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.63 | -35.34 | -95.63 | 4090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.55 | -99.90 | 8321 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T11:55 | AI bee: Boozy | buy | ETH-USD | 14.71 | — | Jev: buy (buy p=0.77) |
| 2026-10-11T11:55 | VWAP reversion | sell | XRP-USD | 16.93 | -0.03 | exit signal |
| 2026-10-11T11:55 | Keltner breakout | buy | SOL-USD | 3.17 | — | entry signal |
| 2026-10-11T11:55 | Keltner breakout | buy | ETH-USD | 12.55 | — | entry signal |
| 2026-10-11T11:55 | Donchian 55/20 | buy | ETH-USD | 17.57 | — | entry signal |
| 2026-10-11T11:55 | Ichimoku | sell | DOGE-USD | 14.98 | -0.09 | target is flat |
| 2026-10-11T11:55 | MACD zero-line | buy | XRP-USD | 5.35 | — | entry signal |
| 2026-10-11T11:55 | MACD zero-line | sell | ETH-USD | 2.66 | -0.01 | rebalance down |
| 2026-10-11T11:55 | MACD zero-line | sell | BTC-USD | 2.65 | -0.01 | rebalance down |
| 2026-10-11T11:55 | Triple EMA stack | buy | ETH-USD | 13.33 | — | entry signal |
| 2026-10-11T11:55 | EMA 20/50 cross | buy | SOL-USD | 17.46 | — | entry signal |
| 2026-10-11T11:55 | EMA 20/50 cross | buy | ETH-USD | 17.46 | — | entry signal |
| 2026-10-11T11:53 | AI bee: Bizzy | buy | BTC-USD | 8.65 | — | Jev: buy (buy p=0.60) |
| 2026-10-11T11:52 | RSI momentum | sell | BTC-USD | 2.70 | -0.01 | rebalance down |
| 2026-10-11T11:52 | Supertrend | sell | BTC-USD | 3.18 | -0.02 | rebalance down |
| 2026-10-11T11:50 | AI bee: Bizzy | buy | SOL-USD | 8.94 | — | Jev: buy (buy p=0.62) |
| 2026-10-11T11:50 | MFI reversion | sell | XRP-USD | 14.76 | -0.03 | exit signal |
| 2026-10-11T11:50 | Z-score reversion | sell | XRP-USD | 14.82 | -0.04 | exit signal |
| 2026-10-11T11:50 | Volume breakout | buy | BTC-USD | 17.54 | — | entry signal |
| 2026-10-11T11:50 | Squeeze breakout | buy | ETH-USD | 17.70 | — | entry signal |
| 2026-10-11T11:50 | Keltner breakout | buy | XRP-USD | 15.71 | — | entry signal |
| 2026-10-11T11:50 | Keltner breakout | buy | DOGE-USD | 15.71 | — | entry signal |
| 2026-10-11T11:50 | Keltner breakout | buy | BTC-USD | 15.71 | — | entry signal |
| 2026-10-11T11:50 | Bollinger breakout | buy | XRP-USD | 10.13 | — | entry signal |
| 2026-10-11T11:50 | Bollinger breakout | buy | SOL-USD | 10.13 | — | entry signal |
| 2026-10-11T11:50 | Bollinger breakout | buy | ETH-USD | 10.13 | — | entry signal |
| 2026-10-11T11:50 | Bollinger breakout | buy | DOGE-USD | 10.13 | — | entry signal |
| 2026-10-11T11:50 | Bollinger breakout | buy | BTC-USD | 10.13 | — | entry signal |
| 2026-10-11T11:50 | Donchian 20/10 | buy | XRP-USD | 11.04 | — | entry signal |
| 2026-10-11T11:50 | Donchian 20/10 | buy | SOL-USD | 11.04 | — | entry signal |
| 2026-10-11T11:50 | Donchian 20/10 | buy | ETH-USD | 11.04 | — | entry signal |
| 2026-10-11T11:50 | Donchian 20/10 | buy | DOGE-USD | 11.04 | — | entry signal |
| 2026-10-11T11:50 | Donchian 20/10 | buy | BTC-USD | 11.04 | — | entry signal |
| 2026-10-11T11:50 | RSI momentum | buy | XRP-USD | 8.12 | — | entry signal |
| 2026-10-11T11:50 | RSI momentum | buy | SOL-USD | 10.80 | — | entry signal |
| 2026-10-11T11:50 | RSI momentum | buy | ETH-USD | 10.80 | — | entry signal |
| 2026-10-11T11:50 | RSI momentum | buy | DOGE-USD | 10.80 | — | entry signal |
| 2026-10-11T11:50 | Ichimoku | buy | SOL-USD | 15.07 | — | entry signal |
| 2026-10-11T11:50 | Ichimoku | buy | DOGE-USD | 15.07 | — | entry signal |
| 2026-10-11T11:50 | Supertrend | buy | XRP-USD | 9.58 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 11:55:05.000152+00:00 -> 2026-10-11 12:05:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
