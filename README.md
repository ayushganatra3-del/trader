# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T18:25:05.000151+00:00 · 19326 ticks

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

Today: 13095 decisions in 2619 calls, $0.1832 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T18:25 | 2 / 3 / 0 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-11T18:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T18:25 | 2 / 3 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.78 | +2.31% | 3 |

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
| 11 | Hold BTC | benchmark | 100.21 | 0.21 | 0 | — | 30.62 | 3.62 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.21 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.23 | -0.77 | 27 | 14.8 | 13.48 | 1.68 | -16.96 | 113 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.47 | -1.82 | -14.61 | 339 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.38 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.80 | -6.42 | -25.39 | 172 |
| 27 | EMA 20/50 cross · 1h | trend | 96.76 | -3.24 | 39 | 12.8 | 6.04 | 0.88 | -19.85 | 136 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.10 | -1.99 | -9.68 | 254 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -0.48 | 0.09 | -13.84 | 253 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.68 | -0.19 | -20.87 | 296 |
| 32 | MACD cross · 1h | trend | 95.95 | -4.05 | 113 | 23.9 | -14.86 | -2.38 | -17.27 | 468 |
| 33 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 34 | Supertrend · 1h | trend | 95.50 | -4.50 | 53 | 13.2 | 0.46 | 0.25 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -2.00 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.07 | -6.30 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.75 | -6.25 | 37 | 24.3 | 23.70 | 3.23 | -9.17 | 108 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.00 | -1.56 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.80 | -0.89 | -14.11 | 425 |
| 42 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.74 | -4.95 | -23.37 | 317 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.94 | 0.68 | -17.07 | 226 |
| 44 | Ichimoku · 1h | trend | 92.52 | -7.48 | 42 | 19.0 | -0.48 | 0.14 | -20.56 | 124 |
| 45 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 56 | 19.6 | 8.07 | 1.25 | -12.60 | 123 |
| 46 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.84 | -4.09 | -26.91 | 514 |
| 47 | Bollinger breakout · 1h | breakout | 91.51 | -8.48 | 70 | 28.6 | 6.37 | 0.98 | -13.17 | 289 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.16 | -0.92 | -26.38 | 241 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 118 | 33.1 | -25.87 | -5.02 | -27.95 | 505 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -6.92 | -0.85 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.52 | -10.48 | 283 | 21.9 | -32.76 | -4.90 | -39.17 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.61 | -1.44 | -28.57 | 323 |
| 55 | Donchian 20/10 · 1h | breakout | 88.72 | -11.28 | 59 | 18.6 | -0.76 | 0.11 | -17.81 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.11 | -5.05 | -36.60 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.62 | -11.38 | 64 | 18.8 | -6.50 | -0.70 | -20.33 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.89 | -12.11 | 104 | 13.5 | -9.35 | -1.07 | -21.69 | 342 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.10 | -23.37 | -48.11 | 590 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.30 | -1.30 | -25.35 | 218 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -9.23 | -1.09 | -23.33 | 412 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.73 | -16.57 | -73.90 | 1677 |
| 64 | RSI(14) reversion | reversion | 73.91 | -26.09 | 369 | 27.6 | -72.49 | -18.17 | -72.49 | 1487 |
| 65 | Squeeze breakout | breakout | 71.28 | -28.72 | 332 | 15.7 | -61.98 | -18.06 | -62.41 | 1230 |
| 66 | Donchian 55/20 | breakout | 70.82 | -29.18 | 333 | 18.0 | -67.18 | -14.24 | -67.50 | 1295 |
| 67 | Volume breakout | breakout | 70.40 | -29.60 | 267 | 14.2 | -62.44 | -17.88 | -62.69 | 906 |
| 68 | EMA 20/50 cross | trend | 70.16 | -29.84 | 335 | 19.4 | -76.71 | -15.22 | -77.04 | 1459 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.20 | -15.98 | -71.25 | 1427 |
| 70 | Supertrend | trend | 64.18 | -35.82 | 464 | 19.6 | -85.86 | -20.91 | -86.10 | 1914 |
| 71 | Keltner breakout | breakout | 62.64 | -37.36 | 457 | 14.9 | -83.72 | -27.78 | -83.79 | 1854 |
| 72 | Ichimoku | trend | 60.38 | -39.62 | 411 | 10.5 | -81.60 | -23.23 | -81.78 | 1750 |
| 73 | AI bee: Boozy | ai | 60.23 | -39.77 | 257 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.36 | -23.32 | -85.36 | 2082 |
| 75 | MFI reversion | reversion | 59.07 | -40.92 | 515 | 21.2 | -87.50 | -28.58 | -87.53 | 2119 |
| 76 | AI bee: Bizzy | ai | 57.33 | -42.67 | 844 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.44 | -43.56 | 546 | 10.3 | -89.23 | -35.13 | -89.30 | 2119 |
| 78 | Donchian 20/10 | breakout | 55.38 | -44.62 | 641 | 18.3 | -90.78 | -26.30 | -90.88 | 2670 |
| 79 | Trend pullback | trend | 54.72 | -45.28 | 587 | 14.8 | -91.00 | -27.19 | -91.00 | 2340 |
| 80 | RSI momentum | momentum | 54.01 | -45.99 | 612 | 16.8 | -90.28 | -25.78 | -90.40 | 2387 |
| 81 | MACD zero-line | trend | 53.21 | -46.79 | 597 | 14.9 | -91.47 | -30.35 | -91.55 | 2366 |
| 82 | Triple EMA stack | trend | 53.14 | -46.86 | 634 | 15.5 | -93.14 | -30.18 | -93.23 | 2623 |
| 83 | Bollinger breakout | breakout | 50.67 | -49.33 | 677 | 14.6 | -93.47 | -33.25 | -93.55 | 2820 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.67 | -31.65 | -98.69 | 5405 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.32 | -33.79 | -97.36 | 3547 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -36.12 | -96.47 | 3621 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.14 | -25.76 | -94.20 | 2691 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -38.00 | -99.34 | 5689 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.40 | -32.24 | -96.40 | 3629 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.95 | -99.73 | 6207 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.40 | -97.36 | 3694 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -38.01 | -98.46 | 4708 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.26 | -99.52 | 6148 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.82 | -34.08 | -95.82 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.59 | -34.96 | -95.59 | 4083 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.61 | -99.90 | 8324 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T18:25 | Triple EMA stack | sell | DOGE-USD | 10.64 | 0.12 | exit signal |
| 2026-10-11T18:20 | Donchian 20/10 | sell | SOL-USD | 11.13 | 0.16 | exit signal |
| 2026-10-11T18:20 | Trend pullback | buy | ETH-USD | 13.69 | — | entry signal |
| 2026-10-11T18:15 | RSI momentum | buy | ETH-USD | 2.72 | — | rebalance up |
| 2026-10-11T18:15 | RSI momentum | buy | DOGE-USD | 2.70 | — | rebalance up |
| 2026-10-11T18:15 | RSI momentum | buy | BTC-USD | 2.70 | — | rebalance up |
| 2026-10-11T18:15 | RSI momentum | sell | XRP-USD | 10.74 | 0.05 | exit signal |
| 2026-10-11T18:15 | Ichimoku | sell | SOL-USD | 15.19 | 0.22 | exit signal |
| 2026-10-11T18:15 | ADX DI cross | sell | XRP-USD | 14.15 | 0.10 | exit signal |
| 2026-10-11T18:10 | Trend pullback | buy | BTC-USD | 13.71 | — | entry signal |
| 2026-10-11T18:10 | Triple EMA stack | buy | SOL-USD | 5.13 | — | rebalance up |
| 2026-10-11T18:10 | Triple EMA stack | buy | ETH-USD | 2.68 | — | rebalance up |
| 2026-10-11T18:10 | Triple EMA stack | sell | XRP-USD | 10.61 | 0.10 | exit signal |
| 2026-10-11T18:05 | Trend pullback | buy | SOL-USD | 13.72 | — | entry signal |
| 2026-10-11T18:05 | Ichimoku | sell | BTC-USD | 15.00 | 0.03 | exit signal |
| 2026-10-11T18:00 | Squeeze breakout | sell | SOL-USD | 17.93 | 0.28 | stop-loss |
| 2026-10-11T18:00 | Squeeze breakout | sell | BTC-USD | 17.68 | 0.04 | stop-loss |
| 2026-10-11T18:00 | Keltner breakout | sell | SOL-USD | 12.55 | 0.12 | stop-loss |
| 2026-10-11T18:00 | Keltner breakout | sell | ETH-USD | 15.65 | 0.01 | stop-loss |
| 2026-10-11T18:00 | Keltner breakout | sell | DOGE-USD | 12.53 | 0.09 | exit signal |
| 2026-10-11T18:00 | Keltner breakout | sell | BTC-USD | 15.65 | -0.04 | stop-loss |
| 2026-10-11T18:00 | Bollinger breakout | sell | SOL-USD | 10.22 | 0.16 | stop-loss |
| 2026-10-11T18:00 | Bollinger breakout | sell | BTC-USD | 12.64 | 0.01 | stop-loss |
| 2026-10-11T18:00 | Donchian 55/20 | buy | DOGE-USD | 3.56 | — | rebalance up |
| 2026-10-11T18:00 | Donchian 55/20 | buy | BTC-USD | 7.07 | — | rebalance up |
| 2026-10-11T18:00 | Donchian 55/20 | sell | XRP-USD | 14.09 | 0.07 | exit signal |
| 2026-10-11T18:00 | Donchian 20/10 | buy | DOGE-USD | 2.80 | — | rebalance up |
| 2026-10-11T18:00 | Donchian 20/10 | buy | BTC-USD | 5.62 | — | rebalance up |
| 2026-10-11T18:00 | Donchian 20/10 | sell | XRP-USD | 11.14 | 0.10 | exit signal |
| 2026-10-11T18:00 | Donchian 20/10 | sell | ETH-USD | 13.79 | 0.08 | exit signal |
| 2026-10-11T18:00 | Ichimoku | sell | XRP-USD | 15.06 | 0.07 | exit signal |
| 2026-10-11T18:00 | Ichimoku | sell | ETH-USD | 15.09 | 0.10 | exit signal |
| 2026-10-11T17:55 | Trend pullback | buy | XRP-USD | 13.73 | — | entry signal |
| 2026-10-11T17:50 | Bollinger breakout | sell | ETH-USD | 12.70 | 0.08 | exit signal |
| 2026-10-11T17:45 | AI bee: Bizzy | sell | DOGE-USD | 8.80 | -0.06 | Jev: sell (sell p=0.90) after 10 min |
| 2026-10-11T17:45 | Keltner breakout | buy | ETH-USD | 3.16 | — | rebalance up |
| 2026-10-11T17:45 | Keltner breakout | sell | XRP-USD | 9.42 | -0.07 | exit signal |
| 2026-10-11T17:45 | ROC + volume | sell | ETH-USD | 18.70 | 0.02 | exit signal |
| 2026-10-11T17:44 | AI bee: Bizzy | sell | SOL-USD | 8.17 | -0.04 | Jev: sell (sell p=0.56) after 24 min |
| 2026-10-11T17:35 | AI bee: Bizzy | buy | DOGE-USD | 8.86 | — | Jev: buy (buy p=0.62) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 18:25:05.000151+00:00 -> 2026-10-11 18:35:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
