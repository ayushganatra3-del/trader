# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T16:25:05.000148+00:00 · 19223 ticks

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

Today: 11550 decisions in 2310 calls, $0.1616 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T16:25 | 3 / 2 / 0 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-11T16:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T16:25 | 3 / 2 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| MFI reversion | AAPL | 2.03 | +0.79% | 6 |
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
| 11 | Hold BTC | benchmark | 100.11 | 0.11 | 0 | — | 30.72 | 3.63 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.21 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.20 | -0.80 | 27 | 14.8 | 13.51 | 1.68 | -16.96 | 112 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.86 | -1.90 | -14.61 | 340 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.38 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.00 | -6.50 | -25.39 | 173 |
| 27 | EMA 20/50 cross · 1h | trend | 96.81 | -3.19 | 39 | 12.8 | 6.11 | 0.89 | -19.85 | 133 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.10 | -1.99 | -9.68 | 254 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -0.44 | 0.09 | -13.84 | 253 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.73 | -0.19 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.82 | -4.94 | -9.58 | 230 |
| 33 | MACD cross · 1h | trend | 95.92 | -4.08 | 113 | 23.9 | -14.89 | -2.39 | -17.27 | 468 |
| 34 | Supertrend · 1h | trend | 95.43 | -4.57 | 53 | 13.2 | 0.38 | 0.24 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -2.00 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.04 | 2.07 | -6.30 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.68 | -6.32 | 37 | 24.3 | 23.61 | 3.22 | -9.17 | 108 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.28 | -1.62 | -17.79 | 126 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.45 | -0.80 | -14.60 | 420 |
| 42 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.54 | -4.90 | -23.18 | 317 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.24 | 0.72 | -17.07 | 225 |
| 44 | Ichimoku · 1h | trend | 92.43 | -7.57 | 42 | 19.0 | -0.57 | 0.13 | -20.56 | 124 |
| 45 | Volume breakout · 1h | breakout | 92.39 | -7.61 | 56 | 19.6 | 8.00 | 1.25 | -12.60 | 123 |
| 46 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.64 | -4.06 | -26.91 | 512 |
| 47 | Bollinger breakout · 1h | breakout | 91.49 | -8.52 | 70 | 28.6 | 5.98 | 0.93 | -13.17 | 290 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.03 | -0.91 | -26.38 | 239 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 118 | 33.1 | -26.20 | -5.10 | -28.23 | 509 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -6.92 | -0.85 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.51 | -10.49 | 283 | 21.9 | -32.77 | -4.90 | -39.14 | 1281 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.07 | -1.36 | -28.30 | 319 |
| 55 | Donchian 20/10 · 1h | breakout | 88.72 | -11.28 | 59 | 18.6 | -1.34 | 0.04 | -17.81 | 229 |
| 56 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -29.94 | -5.02 | -36.59 | 697 |
| 57 | MACD zero-line · 1h | trend | 88.56 | -11.44 | 64 | 18.8 | -6.55 | -0.71 | -20.33 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.87 | -12.13 | 104 | 13.5 | -9.43 | -1.08 | -21.69 | 342 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.42 | -23.53 | -48.45 | 591 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.62 | -1.34 | -25.35 | 219 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.11 | -1.22 | -23.33 | 414 |
| 63 | ROC + volume | momentum | 74.92 | -25.08 | 390 | 22.6 | -72.69 | -16.52 | -73.92 | 1679 |
| 64 | RSI(14) reversion | reversion | 73.91 | -26.09 | 369 | 27.6 | -72.54 | -18.22 | -72.54 | 1489 |
| 65 | Squeeze breakout | breakout | 71.34 | -28.66 | 329 | 14.9 | -62.21 | -18.22 | -62.68 | 1236 |
| 66 | Donchian 55/20 | breakout | 70.80 | -29.20 | 332 | 17.8 | -67.18 | -14.24 | -67.50 | 1295 |
| 67 | Volume breakout | breakout | 70.59 | -29.41 | 262 | 13.0 | -62.43 | -17.86 | -62.78 | 907 |
| 68 | EMA 20/50 cross | trend | 70.08 | -29.92 | 335 | 19.4 | -76.78 | -15.27 | -77.08 | 1460 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.25 | -15.96 | -71.30 | 1426 |
| 70 | Supertrend | trend | 64.10 | -35.90 | 464 | 19.6 | -85.88 | -20.92 | -86.10 | 1914 |
| 71 | Keltner breakout | breakout | 62.79 | -37.21 | 452 | 14.4 | -83.65 | -27.64 | -83.79 | 1853 |
| 72 | Ichimoku | trend | 60.52 | -39.48 | 407 | 9.6 | -81.56 | -23.15 | -81.78 | 1750 |
| 73 | AI bee: Boozy | ai | 60.30 | -39.70 | 256 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.36 | -23.32 | -85.36 | 2082 |
| 75 | MFI reversion | reversion | 59.07 | -40.92 | 515 | 21.2 | -87.52 | -28.53 | -87.55 | 2121 |
| 76 | AI bee: Bizzy | ai | 57.53 | -42.47 | 840 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.48 | -43.52 | 545 | 10.1 | -89.22 | -35.19 | -89.29 | 2119 |
| 78 | Donchian 20/10 | breakout | 55.46 | -44.54 | 638 | 17.9 | -90.77 | -26.27 | -90.88 | 2672 |
| 79 | Trend pullback | trend | 54.94 | -45.06 | 587 | 14.8 | -91.01 | -27.18 | -91.01 | 2339 |
| 80 | RSI momentum | momentum | 54.01 | -45.99 | 611 | 16.7 | -90.33 | -25.95 | -90.46 | 2390 |
| 81 | MACD zero-line | trend | 53.29 | -46.72 | 594 | 14.5 | -91.50 | -30.47 | -91.59 | 2371 |
| 82 | Triple EMA stack | trend | 53.18 | -46.81 | 632 | 15.2 | -93.19 | -30.42 | -93.28 | 2627 |
| 83 | Bollinger breakout | breakout | 50.71 | -49.29 | 673 | 14.1 | -93.50 | -33.42 | -93.58 | 2825 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -31.68 | -98.69 | 5410 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -34.00 | -97.38 | 3553 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -36.29 | -96.48 | 3620 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.19 | -25.91 | -94.25 | 2693 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -38.01 | -99.35 | 5695 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -31.99 | -96.38 | 3623 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.98 | -99.73 | 6208 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -38.15 | -97.37 | 3691 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -38.05 | -98.46 | 4710 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.30 | -99.52 | 6148 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.83 | -34.18 | -95.83 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.59 | -34.96 | -95.59 | 4081 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.63 | -99.90 | 8323 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T16:20 | Squeeze breakout | sell | XRP-USD | 17.78 | 0.11 | stop-loss |
| 2026-10-11T16:20 | Keltner breakout | buy | SOL-USD | 3.11 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | buy | ETH-USD | 3.17 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | buy | DOGE-USD | 3.16 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | buy | BTC-USD | 6.26 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | sell | XRP-USD | 12.54 | 0.08 | stop-loss |
| 2026-10-11T16:20 | Bollinger breakout | buy | ETH-USD | 2.56 | — | rebalance up |
| 2026-10-11T16:20 | Bollinger breakout | buy | BTC-USD | 2.58 | — | rebalance up |
| 2026-10-11T16:20 | Bollinger breakout | sell | XRP-USD | 10.11 | 0.06 | stop-loss |
| 2026-10-11T16:10 | AI bee: Bizzy | sell | SOL-USD | 8.13 | 0.01 | Jev: sell (sell p=0.55) after 21 min |
| 2026-10-11T16:08 | AI bee: Bizzy | sell | XRP-USD | 8.12 | -0.07 | Jev: sell (sell p=0.79) after 11 min |
| 2026-10-11T16:05 | AI bee: Boozy | sell | ETH-USD | 14.55 | -0.07 | Jev: sell |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | XRP-USD | 6.08 | 0.10 | exit signal |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | SOL-USD | 6.99 | 0.09 | exit signal |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | ETH-USD | 5.63 | 0.03 | exit signal |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | DOGE-USD | 6.06 | 0.09 | exit signal |
| 2026-10-11T16:00 | Williams %R · 1h | sell | SOL-USD | 9.33 | 0.12 | exit signal |
| 2026-10-11T16:00 | Williams %R · 1h | sell | ETH-USD | 9.18 | 0.05 | exit signal |
| 2026-10-11T16:00 | Williams %R · 1h | sell | DOGE-USD | 9.25 | 0.12 | exit signal |
| 2026-10-11T16:00 | Bollinger reversion · 1h | sell | SOL-USD | 15.53 | 0.22 | take-profit |
| 2026-10-11T16:00 | Candlestick reversal · 1h | sell | XRP-USD | 5.03 | 0.07 | take-profit |
| 2026-10-11T16:00 | Candlestick reversal · 1h | sell | SOL-USD | 10.16 | 0.13 | take-profit |
| 2026-10-11T16:00 | Volume breakout · 1h | buy | SOL-USD | 14.77 | — | entry signal |
| 2026-10-11T16:00 | Volume breakout · 1h | buy | ETH-USD | 15.43 | — | entry signal |
| 2026-10-11T16:00 | Volume breakout · 1h | buy | BTC-USD | 15.43 | — | entry signal |
| 2026-10-11T16:00 | Squeeze breakout · 1h | buy | ETH-USD | 23.46 | — | entry signal |
| 2026-10-11T16:00 | Squeeze breakout · 1h | buy | BTC-USD | 23.46 | — | entry signal |
| 2026-10-11T16:00 | Bollinger breakout · 1h | buy | DOGE-USD | 11.09 | — | entry signal |
| 2026-10-11T16:00 | Bollinger breakout · 1h | buy | BTC-USD | 11.45 | — | entry signal |
| 2026-10-11T16:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 9.54 | — | entry signal |
| 2026-10-11T16:00 | Donchian 55/20 · 1h | buy | BTC-USD | 14.19 | — | entry signal |
| 2026-10-11T16:00 | Donchian 20/10 · 1h | buy | BTC-USD | 6.38 | — | entry signal |
| 2026-10-11T16:00 | Ichimoku · 1h | buy | XRP-USD | 13.93 | — | entry signal |
| 2026-10-11T16:00 | Ichimoku · 1h | buy | SOL-USD | 18.56 | — | entry signal |
| 2026-10-11T16:00 | Ichimoku · 1h | buy | ETH-USD | 18.56 | — | entry signal |
| 2026-10-11T16:00 | Ichimoku · 1h | buy | DOGE-USD | 18.56 | — | entry signal |
| 2026-10-11T16:00 | Supertrend · 1h | buy | XRP-USD | 3.11 | — | entry signal |
| 2026-10-11T16:00 | Supertrend · 1h | buy | DOGE-USD | 7.35 | — | entry signal |
| 2026-10-11T16:00 | MACD zero-line · 1h | buy | XRP-USD | 8.57 | — | entry signal |
| 2026-10-11T16:00 | MACD zero-line · 1h | buy | SOL-USD | 17.77 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 16:25:05.000148+00:00 -> 2026-10-11 16:35:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
