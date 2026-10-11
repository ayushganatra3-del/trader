# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T18:55:05.000166+00:00 · 19354 ticks

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

Today: 13515 decisions in 2703 calls, $0.1890 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T18:55 | 2 / 3 / 0 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-11T18:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T18:55 | 4 / 1 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| MFI reversion | AAPL | 2.08 | +0.75% | 8 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.44 | -2.26 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -15.28 | -2.51 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Hold BTC | benchmark | 99.90 | -0.10 | 0 | — | 30.17 | 3.58 | -8.68 | 1 |
| 14 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.21 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.47 | -1.82 | -14.61 | 339 |
| 19 | Donchian 55/20 · 1h | breakout | 99.14 | -0.86 | 27 | 14.8 | 13.11 | 1.64 | -16.96 | 113 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.66 | -1.34 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.38 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.80 | -6.42 | -25.39 | 172 |
| 27 | EMA 20/50 cross · 1h | trend | 96.70 | -3.30 | 39 | 12.8 | 5.88 | 0.86 | -19.85 | 136 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.10 | -1.99 | -9.68 | 254 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -0.72 | 0.05 | -13.84 | 254 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.78 | -0.20 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.82 | -4.94 | -9.58 | 230 |
| 33 | MACD cross · 1h | trend | 95.85 | -4.15 | 113 | 23.9 | -14.95 | -2.40 | -17.27 | 468 |
| 34 | Supertrend · 1h | trend | 95.33 | -4.67 | 53 | 13.2 | 0.51 | 0.26 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -2.00 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.04 | 2.07 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.00 | -1.56 | -17.79 | 125 |
| 38 | Squeeze breakout · 1h | breakout | 93.43 | -6.58 | 39 | 23.1 | 23.27 | 3.18 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.85 | -0.89 | -14.64 | 419 |
| 42 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.74 | -4.95 | -23.37 | 317 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.72 | 0.65 | -17.07 | 226 |
| 44 | Volume breakout · 1h | breakout | 92.31 | -7.69 | 56 | 19.6 | 7.68 | 1.20 | -12.60 | 123 |
| 45 | Ichimoku · 1h | trend | 92.15 | -7.85 | 43 | 18.6 | -0.94 | 0.09 | -20.87 | 124 |
| 46 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.75 | -4.07 | -26.91 | 514 |
| 47 | Bollinger breakout · 1h | breakout | 91.36 | -8.64 | 71 | 28.2 | 5.82 | 0.92 | -13.52 | 289 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.29 | -0.94 | -26.38 | 241 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 118 | 33.1 | -25.87 | -5.02 | -27.95 | 505 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -6.92 | -0.85 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.50 | -10.50 | 283 | 21.9 | -32.82 | -4.91 | -39.17 | 1282 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.22 | -19.78 | 700 |
| 54 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.56 | -1.43 | -28.50 | 322 |
| 55 | Donchian 20/10 · 1h | breakout | 88.70 | -11.30 | 59 | 18.6 | -0.97 | 0.09 | -17.96 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.20 | -5.07 | -36.59 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.37 | -11.63 | 65 | 18.5 | -6.86 | -0.75 | -20.62 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.85 | -12.15 | 104 | 13.5 | -9.53 | -1.09 | -21.82 | 342 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.47 | -23.60 | -48.48 | 591 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -12.25 | -1.43 | -25.44 | 220 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -9.78 | -1.17 | -23.43 | 412 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.75 | -16.58 | -73.92 | 1679 |
| 64 | RSI(14) reversion | reversion | 73.86 | -26.14 | 369 | 27.6 | -72.47 | -18.16 | -72.47 | 1487 |
| 65 | Squeeze breakout | breakout | 71.28 | -28.72 | 332 | 15.7 | -61.99 | -18.07 | -62.43 | 1230 |
| 66 | Volume breakout | breakout | 70.40 | -29.60 | 267 | 14.2 | -62.40 | -17.84 | -62.65 | 905 |
| 67 | Donchian 55/20 | breakout | 70.29 | -29.71 | 337 | 18.7 | -67.44 | -14.39 | -67.50 | 1295 |
| 68 | EMA 20/50 cross | trend | 69.87 | -30.13 | 335 | 19.4 | -76.78 | -15.28 | -77.01 | 1459 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.25 | -15.96 | -71.30 | 1427 |
| 70 | Supertrend | trend | 63.62 | -36.38 | 469 | 20.3 | -85.99 | -21.03 | -86.10 | 1914 |
| 71 | Keltner breakout | breakout | 62.64 | -37.36 | 457 | 14.9 | -83.73 | -27.79 | -83.80 | 1854 |
| 72 | Ichimoku | trend | 60.38 | -39.62 | 411 | 10.5 | -81.60 | -23.23 | -81.78 | 1750 |
| 73 | AI bee: Boozy | ai | 60.23 | -39.77 | 257 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.35 | -23.30 | -85.35 | 2081 |
| 75 | MFI reversion | reversion | 59.07 | -40.92 | 515 | 21.2 | -87.50 | -28.48 | -87.54 | 2120 |
| 76 | AI bee: Bizzy | ai | 57.33 | -42.67 | 844 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.38 | -43.62 | 547 | 10.4 | -89.29 | -35.32 | -89.35 | 2122 |
| 78 | Donchian 20/10 | breakout | 55.20 | -44.80 | 643 | 18.4 | -90.79 | -26.32 | -90.86 | 2669 |
| 79 | Trend pullback | trend | 54.33 | -45.67 | 591 | 14.7 | -91.10 | -27.45 | -91.10 | 2342 |
| 80 | RSI momentum | momentum | 53.68 | -46.32 | 616 | 17.2 | -90.36 | -25.92 | -90.42 | 2388 |
| 81 | MACD zero-line | trend | 53.21 | -46.79 | 597 | 14.9 | -91.45 | -30.26 | -91.53 | 2365 |
| 82 | Triple EMA stack | trend | 52.97 | -47.03 | 637 | 15.7 | -93.18 | -30.28 | -93.24 | 2624 |
| 83 | Bollinger breakout | breakout | 50.67 | -49.33 | 677 | 14.6 | -93.49 | -33.29 | -93.57 | 2821 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.57 | -98.67 | 5402 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.92 | -97.36 | 3548 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -36.21 | -96.46 | 3620 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.18 | -25.97 | -94.19 | 2687 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.84 | -99.34 | 5686 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.43 | -32.44 | -96.43 | 3632 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.78 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.48 | -97.37 | 3695 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -38.16 | -98.47 | 4709 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.47 | -99.52 | 6152 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -34.18 | -95.85 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.64 | -35.06 | -95.64 | 4087 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.59 | -99.90 | 8322 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T18:55 | RSI(14) reversion | buy | XRP-USD | 18.48 | — | entry signal |
| 2026-10-11T18:50 | Squeeze breakout · 1h | sell | ETH-USD | 23.27 | -0.19 | stop-loss |
| 2026-10-11T18:50 | Squeeze breakout · 1h | sell | BTC-USD | 23.23 | -0.23 | stop-loss |
| 2026-10-11T18:50 | Bollinger breakout · 1h | buy | DOGE-USD | 11.34 | — | rebalance up |
| 2026-10-11T18:50 | Bollinger breakout · 1h | sell | BTC-USD | 11.34 | -0.11 | stop-loss |
| 2026-10-11T18:50 | Ichimoku · 1h | buy | SOL-USD | 4.64 | — | rebalance up |
| 2026-10-11T18:50 | Ichimoku · 1h | buy | DOGE-USD | 4.66 | — | rebalance up |
| 2026-10-11T18:50 | Ichimoku · 1h | sell | XRP-USD | 13.67 | -0.27 | stop-loss |
| 2026-10-11T18:50 | MACD zero-line · 1h | buy | SOL-USD | 3.91 | — | rebalance up |
| 2026-10-11T18:50 | MACD zero-line · 1h | buy | DOGE-USD | 4.50 | — | rebalance up |
| 2026-10-11T18:50 | MACD zero-line · 1h | sell | XRP-USD | 8.41 | -0.16 | stop-loss |
| 2026-10-11T18:50 | Donchian 55/20 | sell | SOL-USD | 14.11 | 0.09 | exit signal |
| 2026-10-11T18:50 | Donchian 55/20 | sell | ETH-USD | 17.56 | 0.02 | exit signal |
| 2026-10-11T18:50 | Donchian 55/20 | sell | DOGE-USD | 17.55 | 0.02 | exit signal |
| 2026-10-11T18:50 | Donchian 55/20 | sell | BTC-USD | 17.60 | -0.11 | exit signal |
| 2026-10-11T18:50 | Donchian 20/10 | sell | DOGE-USD | 13.75 | 0.04 | exit signal |
| 2026-10-11T18:50 | RSI momentum | sell | SOL-USD | 10.76 | 0.09 | exit signal |
| 2026-10-11T18:50 | RSI momentum | sell | ETH-USD | 13.41 | 0.00 | exit signal |
| 2026-10-11T18:50 | Trend pullback | sell | SOL-USD | 13.53 | -0.19 | stop-loss |
| 2026-10-11T18:50 | Trend pullback | sell | ETH-USD | 13.55 | -0.14 | stop-loss |
| 2026-10-11T18:50 | Trend pullback | sell | BTC-USD | 13.58 | -0.13 | stop-loss |
| 2026-10-11T18:50 | Supertrend | sell | SOL-USD | 15.85 | 0.12 | exit signal |
| 2026-10-11T18:50 | Supertrend | sell | ETH-USD | 15.89 | 0.05 | exit signal |
| 2026-10-11T18:50 | Supertrend | sell | DOGE-USD | 15.92 | 0.06 | exit signal |
| 2026-10-11T18:45 | Donchian 20/10 | sell | BTC-USD | 13.81 | -0.04 | exit signal |
| 2026-10-11T18:45 | RSI momentum | sell | DOGE-USD | 13.45 | 0.06 | exit signal |
| 2026-10-11T18:45 | RSI momentum | sell | BTC-USD | 13.45 | -0.05 | exit signal |
| 2026-10-11T18:45 | ADX DI cross | sell | ETH-USD | 14.14 | 0.10 | exit signal |
| 2026-10-11T18:45 | Supertrend | sell | BTC-USD | 15.94 | -0.06 | exit signal |
| 2026-10-11T18:45 | Triple EMA stack | sell | SOL-USD | 13.21 | -0.00 | exit signal |
| 2026-10-11T18:45 | Triple EMA stack | sell | ETH-USD | 13.25 | 0.05 | exit signal |
| 2026-10-11T18:45 | Triple EMA stack | sell | BTC-USD | 13.07 | 0.02 | exit signal |
| 2026-10-11T18:40 | Trend pullback | sell | XRP-USD | 13.59 | -0.15 | stop-loss |
| 2026-10-11T18:36 | Supertrend | buy | DOGE-USD | 3.22 | — | rebalance up |
| 2026-10-11T18:36 | Supertrend | buy | BTC-USD | 9.51 | — | rebalance up |
| 2026-10-11T18:36 | Supertrend | sell | XRP-USD | 12.75 | 0.10 | exit signal |
| 2026-10-11T18:25 | Triple EMA stack | sell | DOGE-USD | 10.64 | 0.12 | exit signal |
| 2026-10-11T18:20 | Donchian 20/10 | sell | SOL-USD | 11.13 | 0.16 | exit signal |
| 2026-10-11T18:20 | Trend pullback | buy | ETH-USD | 13.69 | — | entry signal |
| 2026-10-11T18:15 | RSI momentum | buy | ETH-USD | 2.72 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 18:55:05.000166+00:00 -> 2026-10-11 19:05:05.000166+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
