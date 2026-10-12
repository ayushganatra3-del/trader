# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T06:25:05.000152+00:00 · 19927 ticks

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

Today: 5040 decisions in 1008 calls, $0.0706 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T06:25 | 0 / 1 / 4 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T06:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T06:25 | 0 / 4 / 1 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | AAPL | 2.49 | +0.83% | 6 |
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.26 | 3.26 | 37 | 43.2 | -7.53 | -2.28 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.51 | 2.51 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.18 | 2.18 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 101.99 | 1.99 | 14 | 57.1 | -12.40 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.31 | 1.31 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.22 | 1.22 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.07 | 1.07 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Hold BTC | benchmark | 99.99 | -0.01 | 0 | — | 30.68 | 3.60 | -8.68 | 1 |
| 14 | Max aggression: 1-day momentum | meta | 99.73 | -0.27 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.67 | -0.33 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.13 | -0.87 | 28 | 14.3 | 12.95 | 1.61 | -16.96 | 114 |
| 19 | Stochastic reversion · 1h | reversion | 99.10 | -0.90 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.57 | -1.43 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.54 | -1.47 | 0 | — | 11.52 | 1.86 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.78 | -2.22 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.30 | -2.70 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.16 | -2.84 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.02 | -2.98 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.92 | -2.30 | -10.19 | 268 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 29 | EMA 20/50 cross · 1h | trend | 96.63 | -3.37 | 40 | 12.5 | 6.18 | 0.89 | -19.85 | 136 |
| 30 | ADX DI cross · 1h | trend | 96.28 | -3.72 | 58 | 20.7 | -0.37 | 0.10 | -13.84 | 252 |
| 31 | Parabolic SAR · 1h | trend | 96.24 | -3.76 | 82 | 22.0 | -2.08 | -0.11 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.07 | -5.05 | -9.83 | 230 |
| 33 | MACD cross · 1h | trend | 95.73 | -4.27 | 115 | 23.5 | -14.77 | -2.35 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.47 | -4.53 | 53 | 13.2 | 2.29 | 0.48 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.46 | -6.54 | 119 | 34.5 | -10.24 | -1.62 | -17.79 | 124 |
| 38 | Squeeze breakout · 1h | breakout | 93.41 | -6.59 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.06 | -6.94 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.00 | -7.00 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.79 | -7.21 | 392 | 18.4 | -2.39 | -0.25 | -14.35 | 427 |
| 42 | Bollinger reversion · 1h | reversion | 92.72 | -7.28 | 78 | 37.2 | -20.67 | -4.90 | -23.11 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.63 | -7.37 | 64 | 15.6 | 4.84 | 0.78 | -17.15 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.18 | -7.83 | 58 | 19.0 | 7.71 | 1.20 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 91.83 | -8.17 | 44 | 18.2 | -1.18 | 0.06 | -21.18 | 125 |
| 46 | Williams %R · 1h | reversion | 91.51 | -8.49 | 126 | 47.6 | -23.65 | -4.02 | -26.91 | 508 |
| 47 | Bollinger breakout · 1h | breakout | 91.19 | -8.81 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.65 | -9.35 | 69 | 15.9 | -8.57 | -0.84 | -26.49 | 241 |
| 50 | Candlestick reversal · 1h | reversion | 90.35 | -9.65 | 118 | 33.1 | -26.12 | -5.04 | -28.13 | 505 |
| 51 | CCI reversion · 1h | reversion | 89.92 | -10.08 | 105 | 46.7 | -7.02 | -0.86 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.42 | -10.58 | 284 | 21.8 | -32.26 | -4.78 | -39.18 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.18 | -19.78 | 700 |
| 54 | OBV trend · 1h | momentum | 88.70 | -11.30 | 149 | 18.8 | -13.16 | -1.50 | -28.50 | 326 |
| 55 | Donchian 20/10 · 1h | breakout | 88.63 | -11.37 | 60 | 18.3 | -0.66 | 0.13 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.59 | -11.41 | 138 | 25.4 | -29.93 | -4.99 | -36.59 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.17 | -11.83 | 66 | 18.2 | -6.70 | -0.72 | -20.89 | 239 |
| 58 | Max aggression: 5-day momentum | meta | 87.90 | -12.10 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.84 | -12.16 | 104 | 13.5 | -8.71 | -0.97 | -21.96 | 339 |
| 60 | Keltner breakout · 1h | breakout | 87.03 | -12.97 | 43 | 18.6 | -12.10 | -1.40 | -25.86 | 220 |
| 61 | Three white soldiers | momentum | 86.80 | -13.20 | 147 | 17.0 | -48.19 | -23.07 | -48.27 | 593 |
| 62 | ROC + volume · 1h | momentum | 86.21 | -13.79 | 132 | 21.2 | -10.02 | -1.20 | -23.65 | 415 |
| 63 | ROC + volume | momentum | 74.15 | -25.84 | 400 | 23.0 | -73.02 | -16.57 | -74.12 | 1684 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 375 | 27.5 | -72.12 | -17.81 | -72.17 | 1484 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.17 | -18.00 | -62.18 | 1234 |
| 66 | Volume breakout | breakout | 69.88 | -30.12 | 271 | 14.0 | -62.47 | -17.79 | -62.49 | 906 |
| 67 | EMA 20/50 cross | trend | 68.58 | -31.42 | 346 | 19.9 | -76.82 | -15.26 | -76.82 | 1456 |
| 68 | Donchian 55/20 | breakout | 68.38 | -31.62 | 349 | 18.1 | -68.30 | -14.61 | -68.30 | 1304 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 405 | 25.9 | -71.13 | -15.73 | -71.19 | 1424 |
| 70 | Supertrend | trend | 62.60 | -37.40 | 479 | 19.8 | -86.02 | -20.97 | -86.08 | 1915 |
| 71 | Keltner breakout | breakout | 61.47 | -38.53 | 468 | 14.5 | -83.87 | -27.73 | -83.87 | 1859 |
| 72 | AI bee: Boozy | ai | 60.04 | -39.96 | 260 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 59.24 | -40.76 | 420 | 10.2 | -81.83 | -23.18 | -81.84 | 1753 |
| 74 | Z-score reversion | reversion | 58.93 | -41.07 | 516 | 22.1 | -85.05 | -22.69 | -85.06 | 2073 |
| 75 | MFI reversion | reversion | 58.32 | -41.68 | 525 | 20.8 | -87.48 | -27.75 | -87.52 | 2122 |
| 76 | AI bee: Bizzy | ai | 56.25 | -43.75 | 866 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.34 | -44.66 | 558 | 10.2 | -89.30 | -34.85 | -89.30 | 2122 |
| 78 | Donchian 20/10 | breakout | 53.73 | -46.27 | 656 | 18.0 | -90.89 | -26.16 | -90.89 | 2673 |
| 79 | Trend pullback | trend | 52.33 | -47.67 | 617 | 14.6 | -91.26 | -27.20 | -91.27 | 2354 |
| 80 | RSI momentum | momentum | 52.29 | -47.72 | 631 | 16.8 | -90.51 | -25.87 | -90.51 | 2394 |
| 81 | MACD zero-line | trend | 52.13 | -47.87 | 610 | 14.6 | -91.52 | -29.82 | -91.52 | 2368 |
| 82 | Triple EMA stack | trend | 51.29 | -48.71 | 655 | 15.3 | -93.33 | -30.38 | -93.33 | 2633 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -31.06 | -98.64 | 5388 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.41 | -97.37 | 3554 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -36.25 | -96.50 | 3633 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.29 | -25.55 | -94.29 | 2699 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.23 | -99.34 | 5685 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.52 | -32.06 | -96.52 | 3649 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.68 | -99.73 | 6203 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -38.04 | -97.37 | 3697 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.41 | -35.99 | -98.42 | 4693 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.57 | -33.18 | -93.57 | 2827 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -39.58 | -99.51 | 6143 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.73 | -32.78 | -95.73 | 3733 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.58 | -33.82 | -95.58 | 4081 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.73 | -99.89 | 8311 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T06:25 | RSI momentum | sell | ETH-USD | 10.47 | -0.05 | exit signal |
| 2026-10-12T06:25 | Trend pullback | sell | ETH-USD | 10.47 | -0.09 | exit signal |
| 2026-10-12T06:25 | Triple EMA stack | sell | ETH-USD | 10.29 | -0.05 | exit signal |
| 2026-10-12T06:20 | Donchian 55/20 | sell | SOL-USD | 13.69 | -0.13 | exit signal |
| 2026-10-12T06:20 | Donchian 55/20 | sell | DOGE-USD | 17.02 | -0.13 | stop-loss |
| 2026-10-12T06:20 | Donchian 20/10 | sell | SOL-USD | 13.40 | -0.13 | exit signal |
| 2026-10-12T06:20 | RSI momentum | sell | BTC-USD | 10.47 | -0.09 | exit signal |
| 2026-10-12T06:20 | Trend pullback | sell | SOL-USD | 10.46 | -0.11 | exit signal |
| 2026-10-12T06:20 | Triple EMA stack | sell | SOL-USD | 10.25 | -0.07 | exit signal |
| 2026-10-12T06:20 | EMA 20/50 cross | sell | BTC-USD | 17.09 | -0.15 | stop-loss |
| 2026-10-12T06:15 | Donchian 55/20 | buy | DOGE-USD | 17.14 | — | entry |
| 2026-10-12T06:15 | RSI momentum | sell | SOL-USD | 10.46 | -0.05 | exit signal |
| 2026-10-12T06:15 | Supertrend | sell | SOL-USD | 12.54 | -0.04 | exit signal |
| 2026-10-12T06:15 | Triple EMA stack | sell | DOGE-USD | 10.28 | -0.03 | exit signal |
| 2026-10-12T06:15 | Triple EMA stack | sell | BTC-USD | 12.83 | -0.09 | exit signal |
| 2026-10-12T06:10 | Donchian 55/20 | sell | DOGE-USD | 13.70 | -0.13 | stop-loss |
| 2026-10-12T06:10 | Donchian 20/10 | sell | DOGE-USD | 10.76 | -0.06 | exit signal |
| 2026-10-12T06:10 | RSI momentum | sell | DOGE-USD | 13.07 | -0.08 | exit signal |
| 2026-10-12T06:10 | Trend pullback | sell | DOGE-USD | 13.08 | -0.13 | exit signal |
| 2026-10-12T06:10 | Trend pullback | sell | BTC-USD | 13.10 | -0.10 | exit signal |
| 2026-10-12T06:10 | ADX DI cross | sell | SOL-USD | 13.81 | -0.11 | exit signal |
| 2026-10-12T06:10 | ADX DI cross | sell | BTC-USD | 13.81 | -0.10 | exit signal |
| 2026-10-12T06:10 | Supertrend | sell | DOGE-USD | 12.57 | -0.01 | exit signal |
| 2026-10-12T06:05 | RSI momentum | buy | DOGE-USD | 2.64 | — | rebalance up |
| 2026-10-12T06:05 | RSI momentum | sell | XRP-USD | 10.45 | -0.05 | exit signal |
| 2026-10-12T06:05 | Trend pullback | buy | DOGE-USD | 2.65 | — | rebalance up |
| 2026-10-12T06:05 | Trend pullback | sell | XRP-USD | 7.87 | -0.07 | exit signal |
| 2026-10-12T06:05 | ADX DI cross | sell | XRP-USD | 13.79 | -0.13 | exit signal |
| 2026-10-12T06:04 | AI bee: Bizzy | sell | DOGE-USD | 8.24 | -0.08 | Jev: sell (sell p=0.84) after 10 min |
| 2026-10-12T05:54 | AI bee: Bizzy | buy | DOGE-USD | 8.31 | — | Jev: buy (buy p=0.59) |
| 2026-10-12T05:52 | Trend pullback | buy | XRP-USD | 2.63 | — | rebalance up |
| 2026-10-12T05:52 | Trend pullback | sell | ETH-USD | 2.63 | -0.01 | rebalance down |
| 2026-10-12T05:50 | Trend pullback | buy | XRP-USD | 5.31 | — | entry signal |
| 2026-10-12T05:50 | Trend pullback | buy | DOGE-USD | 10.55 | — | entry signal |
| 2026-10-12T05:50 | Trend pullback | sell | SOL-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-12T05:50 | ADX DI cross | buy | XRP-USD | 13.91 | — | entry signal |
| 2026-10-12T05:50 | ADX DI cross | buy | BTC-USD | 13.91 | — | entry signal |
| 2026-10-12T05:45 | ROC + volume | sell | SOL-USD | 18.55 | -0.10 | exit signal |
| 2026-10-12T05:45 | Trend pullback | buy | ETH-USD | 13.20 | — | entry signal |
| 2026-10-12T05:45 | Trend pullback | buy | BTC-USD | 13.20 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 06:25:05.000152+00:00 -> 2026-10-12 06:35:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
