# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T01:25:05.000148+00:00 · 20787 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.28 (-4.72%)

Closed trades 59, win rate 49.2%, fees £2.28, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.55 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 990 decisions in 198 calls, $0.0140 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T01:25 | 0 / 4 / 1 | XRP-USD 15%, ETH-USD 15%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T01:25 | 2 / 3 / 0 | ETH-USD 23% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MFI reversion | AAPL | 1.97 | +0.65% | 6 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.91 | 2.91 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.05 | 2.05 | 16 | 50.0 | -12.87 | -2.12 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.42 | 1.42 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.21 | -2.74 | -13.79 | 118 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.21 | 1.21 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.65 | 0.65 | 0 | — | -5.03 | -0.82 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.62 | 0.62 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.12 | 0.12 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.36 | -0.64 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 18 | Donchian 55/20 · 1h | breakout | 98.24 | -1.76 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 19 | Hold BTC | benchmark | 98.16 | -1.84 | 0 | — | 27.97 | 3.30 | -8.68 | 1 |
| 20 | Daily: Bullish score | daily | 98.13 | -1.87 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 98.00 | -2.00 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.87 | -2.13 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.02 | -2.98 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Stochastic reversion · 1h | reversion | 96.70 | -3.30 | 100 | 51.0 | -12.45 | -2.37 | -13.91 | 346 |
| 26 | Z-score reversion · 1h | reversion | 96.70 | -3.30 | 45 | 42.2 | 3.18 | 0.76 | -8.60 | 160 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.48 | -3.52 | 62 | 19.4 | -5.74 | -0.90 | -13.79 | 252 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.56 | -2.71 | -8.94 | 304 |
| 30 | MACD cross · 1h | trend | 95.85 | -4.15 | 125 | 24.0 | -10.86 | -1.69 | -17.79 | 459 |
| 31 | Parabolic SAR · 1h | trend | 95.36 | -4.64 | 86 | 22.1 | 2.01 | 0.45 | -21.52 | 289 |
| 32 | EMA 20/50 cross · 1h | trend | 95.34 | -4.66 | 45 | 15.6 | 4.88 | 0.75 | -23.71 | 136 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.95 | -3.83 | -8.72 | 232 |
| 34 | Supertrend · 1h | trend | 94.56 | -5.44 | 58 | 13.8 | 1.33 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.50 | -6.50 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.46 | -6.54 | 151 | 32.5 | -8.21 | -1.25 | -16.91 | 129 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.24 | -2.74 | -6.45 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.61 | -7.39 | 66 | 15.2 | -0.62 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.52 | -7.48 | 115 | 43.5 | -18.87 | -6.23 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.51 | -7.50 | 439 | 17.8 | 1.00 | 0.32 | -11.47 | 390 |
| 42 | Volume breakout · 1h | breakout | 91.72 | -8.28 | 70 | 20.0 | 9.17 | 1.39 | -12.60 | 118 |
| 43 | RSI(14) reversion · 1h | reversion | 91.61 | -8.39 | 34 | 26.5 | 0.34 | 0.19 | -9.24 | 130 |
| 44 | Ichimoku · 1h | trend | 91.01 | -8.99 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.86 | -9.13 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 46 | Triple EMA stack · 1h | trend | 90.71 | -9.29 | 71 | 15.5 | -6.99 | -0.60 | -27.17 | 236 |
| 47 | Bollinger reversion · 1h | reversion | 90.35 | -9.65 | 88 | 35.2 | -24.07 | -5.84 | -24.28 | 315 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 89.01 | -10.99 | 113 | 45.1 | -9.84 | -1.30 | -14.35 | 406 |
| 50 | OBV trend · 1h | momentum | 88.71 | -11.29 | 150 | 18.7 | -12.46 | -1.18 | -34.14 | 317 |
| 51 | Williams %R · 1h | reversion | 88.48 | -11.52 | 136 | 44.9 | -26.86 | -4.42 | -28.65 | 507 |
| 52 | VWAP momentum · 1h | momentum | 88.25 | -11.75 | 311 | 23.2 | -32.93 | -4.89 | -40.22 | 1251 |
| 53 | Max aggression: 5-day momentum | meta | 88.10 | -11.90 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.97 | -12.03 | 130 | 30.8 | -28.52 | -5.42 | -29.05 | 496 |
| 55 | Heikin-Ashi · 1h | trend | 87.72 | -12.28 | 153 | 28.1 | -29.98 | -4.94 | -37.65 | 675 |
| 56 | Donchian 20/10 · 1h | breakout | 87.72 | -12.28 | 63 | 17.5 | -0.59 | 0.13 | -19.51 | 214 |
| 57 | MACD zero-line · 1h | trend | 87.60 | -12.40 | 67 | 17.9 | -21.06 | -3.90 | -21.53 | 232 |
| 58 | EMA 9/21 cross · 1h | trend | 87.11 | -12.89 | 108 | 13.0 | -8.23 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.65 | -13.35 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.37 | -13.63 | 153 | 17.0 | -48.35 | -23.21 | -48.35 | 588 |
| 62 | ROC + volume · 1h | momentum | 85.52 | -14.48 | 164 | 20.1 | -9.09 | -1.05 | -25.04 | 400 |
| 63 | ROC + volume | momentum | 72.00 | -28.00 | 421 | 22.3 | -72.98 | -16.46 | -74.68 | 1663 |
| 64 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.19 | -17.94 | -62.19 | 1221 |
| 65 | Volume breakout | breakout | 69.45 | -30.55 | 279 | 14.7 | -61.47 | -17.33 | -61.47 | 890 |
| 66 | RSI(14) reversion | reversion | 68.66 | -31.34 | 429 | 26.8 | -73.88 | -17.25 | -74.03 | 1486 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 357 | 19.9 | -76.37 | -15.00 | -76.37 | 1430 |
| 68 | Donchian 55/20 | breakout | 66.63 | -33.37 | 360 | 17.5 | -68.13 | -14.21 | -69.10 | 1289 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.09 | -15.47 | -73.12 | 1419 |
| 70 | AI bee: Boozy | ai | 60.27 | -39.73 | 261 | 5.0 | — | — | — | — |
| 71 | Keltner breakout | breakout | 60.24 | -39.76 | 485 | 14.6 | -83.23 | -26.79 | -83.23 | 1835 |
| 72 | Supertrend | trend | 59.75 | -40.24 | 503 | 19.3 | -86.10 | -20.80 | -86.10 | 1896 |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.19 | -22.73 | -82.19 | 1732 |
| 74 | AI bee: Bizzy | ai | 55.31 | -44.69 | 891 | 8.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 55.13 | -44.88 | 623 | 19.4 | -88.01 | -27.15 | -88.18 | 2125 |
| 76 | Z-score reversion | reversion | 54.57 | -45.43 | 573 | 22.0 | -86.32 | -22.42 | -86.48 | 2083 |
| 77 | ADX DI cross | trend | 53.30 | -46.70 | 599 | 10.0 | -89.15 | -33.69 | -89.15 | 2104 |
| 78 | Donchian 20/10 | breakout | 51.74 | -48.26 | 684 | 17.5 | -90.84 | -25.58 | -90.84 | 2642 |
| 79 | MACD zero-line | trend | 50.91 | -49.09 | 635 | 14.5 | -91.48 | -29.36 | -91.48 | 2344 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.56 | -29.87 | -98.58 | 5308 |
| 81 | Trend pullback | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.12 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.13 | -29.28 | -93.13 | 2590 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.48 | -25.10 | -90.48 | 2359 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -32.39 | -97.36 | 3517 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -34.91 | -96.34 | 3574 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.28 | -25.17 | -94.28 | 2626 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.94 | -99.38 | 5653 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -30.70 | -96.29 | 3591 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.46 | -99.73 | 6143 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.26 | -36.71 | -97.26 | 3647 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -35.93 | -98.55 | 4674 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.34 | -32.06 | -93.34 | 2790 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.75 | -99.55 | 6116 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.08 | -32.50 | -96.10 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.82 | -33.81 | -95.84 | 4057 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -44.56 | -99.89 | 8198 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T01:25 | MFI reversion | buy | XRP-USD | 2.75 | — | rebalance up |
| 2026-10-13T01:25 | MFI reversion | sell | DOGE-USD | 2.75 | 0.01 | rebalance down |
| 2026-10-13T01:22 | AI bee: Boozy | buy | ETH-USD | 14.21 | — | Jev: buy (buy p=0.77) |
| 2026-10-13T01:22 | AI bee: Bizzy | buy | ETH-USD | 8.29 | — | Jev: buy (buy p=0.60) |
| 2026-10-13T01:20 | Z-score reversion | sell | XRP-USD | 13.60 | 0.08 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | buy | SOL-USD | 3.47 | — | rebalance up |
| 2026-10-13T01:20 | RSI(14) reversion | sell | XRP-USD | 13.75 | 0.06 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | sell | ETH-USD | 13.73 | 0.04 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | sell | DOGE-USD | 13.76 | 0.07 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | sell | BTC-USD | 13.71 | 0.04 | take-profit |
| 2026-10-13T01:20 | Three white soldiers | buy | BTC-USD | 21.61 | — | entry signal |
| 2026-10-13T01:20 | Keltner breakout | buy | BTC-USD | 15.08 | — | entry signal |
| 2026-10-13T01:20 | Donchian 20/10 | buy | XRP-USD | 12.97 | — | entry signal |
| 2026-10-13T01:20 | Donchian 20/10 | buy | DOGE-USD | 12.97 | — | entry signal |
| 2026-10-13T01:20 | Donchian 20/10 | buy | BTC-USD | 12.97 | — | entry signal |
| 2026-10-13T01:20 | ROC + volume | buy | XRP-USD | 18.07 | — | entry signal |
| 2026-10-13T01:20 | ROC + volume | buy | ETH-USD | 18.07 | — | entry signal |
| 2026-10-13T01:20 | ROC + volume | buy | DOGE-USD | 18.07 | — | entry signal |
| 2026-10-13T01:20 | ROC + volume | buy | BTC-USD | 18.07 | — | entry signal |
| 2026-10-13T01:20 | ADX DI cross | buy | XRP-USD | 13.35 | — | entry signal |
| 2026-10-13T01:20 | ADX DI cross | buy | BTC-USD | 13.35 | — | entry signal |
| 2026-10-13T01:20 | Supertrend | buy | XRP-USD | 15.00 | — | entry signal |
| 2026-10-13T01:20 | Supertrend | buy | ETH-USD | 15.00 | — | entry signal |
| 2026-10-13T01:20 | Supertrend | buy | DOGE-USD | 15.00 | — | entry signal |
| 2026-10-13T01:20 | Supertrend | buy | BTC-USD | 15.00 | — | entry signal |
| 2026-10-13T01:15 | AI bee: Bizzy | buy | XRP-USD | 8.35 | — | Jev: buy (buy p=0.60) |
| 2026-10-13T01:10 | RSI(14) reversion | buy | XRP-USD | 3.42 | — | rebalance up |
| 2026-10-13T01:07 | RSI(14) reversion | sell | BTC-USD | 3.43 | -0.01 | rebalance down |
| 2026-10-13T01:05 | VWAP reversion | sell | SOL-USD | 15.73 | 0.02 | exit signal |
| 2026-10-13T01:05 | RSI(14) reversion | buy | XRP-USD | 10.28 | — | entry signal |
| 2026-10-13T01:05 | RSI(14) reversion | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-10-13T01:05 | RSI(14) reversion | buy | ETH-USD | 13.69 | — | entry signal |
| 2026-10-13T01:05 | RSI(14) reversion | buy | DOGE-USD | 13.69 | — | entry signal |
| 2026-10-13T01:00 | Stochastic reversion · 1h | buy | ETH-USD | 9.93 | — | entry signal |
| 2026-10-13T01:00 | Stochastic reversion · 1h | buy | DOGE-USD | 10.71 | — | entry signal |
| 2026-10-13T01:00 | Stochastic reversion · 1h | buy | BTC-USD | 10.71 | — | entry signal |
| 2026-10-13T01:00 | MFI reversion | buy | XRP-USD | 2.86 | — | entry signal |
| 2026-10-13T01:00 | MFI reversion | buy | SOL-USD | 10.90 | — | entry signal |
| 2026-10-13T01:00 | VWAP reversion | buy | SOL-USD | 15.71 | — | entry signal |
| 2026-10-13T00:55 | MFI reversion | buy | BTC-USD | 13.63 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 01:25:05.000148+00:00 -> 2026-10-13 01:35:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
