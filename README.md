# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T01:55:05.000140+00:00 · 19690 ticks

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

Today: 1485 decisions in 297 calls, $0.0208 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T01:55 | 4 / 1 / 0 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T01:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T01:55 | 4 / 1 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.25 | 3.25 | 37 | 43.2 | -7.44 | -2.25 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.46 | 2.46 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.14 | 2.14 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 101.95 | 1.95 | 14 | 57.1 | -15.28 | -2.49 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.27 | 1.26 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.18 | 1.18 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.02 | 1.02 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.69 | -0.31 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 14 | Hold BTC | benchmark | 99.65 | -0.35 | 0 | — | 30.01 | 3.53 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.63 | -0.37 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.06 | -0.94 | 89 | 55.1 | -10.03 | -1.93 | -14.61 | 338 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 20 | Donchian 55/20 · 1h | breakout | 98.89 | -1.11 | 28 | 14.3 | 12.79 | 1.59 | -16.96 | 113 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.53 | -1.47 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.49 | -1.51 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.73 | -2.27 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.29 | -2.71 | 7 | 0.0 | -3.28 | -2.51 | -4.32 | 28 |
| 25 | Z-score reversion · 1h | reversion | 97.13 | -2.87 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 96.98 | -3.02 | 78 | 23.1 | -23.13 | -6.51 | -25.39 | 167 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 28 | Agent (rotation) | meta | 96.66 | -3.34 | 80 | 30.0 | -6.15 | -2.07 | -9.46 | 260 |
| 29 | EMA 20/50 cross · 1h | trend | 96.48 | -3.52 | 40 | 12.5 | 4.81 | 0.74 | -19.85 | 139 |
| 30 | ADX DI cross · 1h | trend | 96.24 | -3.76 | 58 | 20.7 | -0.64 | 0.06 | -13.84 | 253 |
| 31 | Parabolic SAR · 1h | trend | 96.20 | -3.80 | 82 | 22.0 | -2.94 | -0.22 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.67 | -4.33 | 114 | 23.7 | -14.73 | -2.34 | -17.27 | 467 |
| 34 | Supertrend · 1h | trend | 95.15 | -4.85 | 53 | 13.2 | 0.59 | 0.27 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.43 | -6.57 | 119 | 34.5 | -9.72 | -1.52 | -17.79 | 127 |
| 38 | Squeeze breakout · 1h | breakout | 93.40 | -6.60 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.02 | -6.98 | 26 | 26.9 | -2.21 | -0.37 | -9.03 | 147 |
| 40 | Connors RSI(2) · 1h | reversion | 92.99 | -7.01 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.75 | -7.25 | 392 | 18.4 | -2.06 | -0.22 | -14.35 | 439 |
| 42 | Bollinger reversion · 1h | reversion | 92.68 | -7.32 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.59 | -7.41 | 64 | 15.6 | 4.27 | 0.71 | -17.15 | 225 |
| 44 | Volume breakout · 1h | breakout | 91.98 | -8.02 | 58 | 19.0 | 7.04 | 1.11 | -12.60 | 123 |
| 45 | Ichimoku · 1h | trend | 91.73 | -8.27 | 44 | 18.2 | -1.29 | 0.04 | -21.18 | 124 |
| 46 | Williams %R · 1h | reversion | 91.48 | -8.52 | 126 | 47.6 | -23.10 | -3.90 | -26.91 | 514 |
| 47 | Bollinger breakout · 1h | breakout | 91.16 | -8.84 | 72 | 27.8 | 5.83 | 0.91 | -13.62 | 288 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.62 | -9.38 | 69 | 15.9 | -9.49 | -0.96 | -26.49 | 243 |
| 50 | Candlestick reversal · 1h | reversion | 90.32 | -9.68 | 118 | 33.1 | -26.10 | -5.03 | -28.17 | 507 |
| 51 | CCI reversion · 1h | reversion | 89.89 | -10.11 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.38 | -10.62 | 283 | 21.9 | -31.80 | -4.68 | -39.17 | 1274 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.67 | -11.33 | 149 | 18.8 | -13.04 | -1.49 | -28.57 | 325 |
| 55 | Heikin-Ashi · 1h | trend | 88.55 | -11.45 | 138 | 25.4 | -30.03 | -5.01 | -36.60 | 702 |
| 56 | Donchian 20/10 · 1h | breakout | 88.54 | -11.46 | 60 | 18.3 | -1.21 | 0.06 | -18.15 | 228 |
| 57 | MACD zero-line · 1h | trend | 87.95 | -12.05 | 66 | 18.2 | -7.22 | -0.79 | -20.89 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.86 | -12.14 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.73 | -12.27 | 104 | 13.5 | -9.30 | -1.05 | -21.96 | 341 |
| 60 | Three white soldiers | momentum | 87.18 | -12.82 | 142 | 17.6 | -48.03 | -22.82 | -48.04 | 589 |
| 61 | Keltner breakout · 1h | breakout | 87.00 | -13.01 | 43 | 18.6 | -12.44 | -1.45 | -25.51 | 220 |
| 62 | ROC + volume · 1h | momentum | 86.17 | -13.83 | 132 | 21.2 | -10.36 | -1.24 | -23.48 | 414 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.73 | -16.36 | -73.90 | 1677 |
| 64 | RSI(14) reversion | reversion | 73.65 | -26.35 | 373 | 27.3 | -72.58 | -17.97 | -72.59 | 1492 |
| 65 | Squeeze breakout | breakout | 70.67 | -29.33 | 336 | 15.5 | -62.03 | -17.90 | -62.16 | 1230 |
| 66 | Volume breakout | breakout | 70.29 | -29.71 | 268 | 14.2 | -62.30 | -17.66 | -62.49 | 904 |
| 67 | Donchian 55/20 | breakout | 69.76 | -30.24 | 340 | 18.5 | -67.50 | -14.30 | -67.64 | 1295 |
| 68 | EMA 20/50 cross | trend | 68.83 | -31.17 | 343 | 20.1 | -76.87 | -15.25 | -76.88 | 1457 |
| 69 | VWAP reversion | reversion | 67.69 | -32.31 | 403 | 25.8 | -71.38 | -15.86 | -71.39 | 1431 |
| 70 | Supertrend | trend | 62.95 | -37.05 | 474 | 20.0 | -86.00 | -20.88 | -86.04 | 1914 |
| 71 | Keltner breakout | breakout | 62.24 | -37.76 | 460 | 14.8 | -83.75 | -27.29 | -83.75 | 1854 |
| 72 | Ichimoku | trend | 60.38 | -39.62 | 411 | 10.5 | -81.56 | -22.79 | -81.74 | 1749 |
| 73 | AI bee: Boozy | ai | 60.06 | -39.94 | 259 | 5.0 | — | — | — | — |
| 74 | Z-score reversion | reversion | 58.94 | -41.06 | 514 | 22.2 | -85.32 | -22.91 | -85.32 | 2083 |
| 75 | MFI reversion | reversion | 58.35 | -41.65 | 524 | 20.8 | -87.59 | -27.96 | -87.62 | 2125 |
| 76 | AI bee: Bizzy | ai | 56.80 | -43.20 | 854 | 8.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.89 | -44.11 | 552 | 10.3 | -89.19 | -34.26 | -89.19 | 2117 |
| 78 | Donchian 20/10 | breakout | 54.60 | -45.40 | 648 | 18.2 | -90.79 | -25.83 | -90.79 | 2668 |
| 79 | Trend pullback | trend | 53.27 | -46.73 | 602 | 14.5 | -91.17 | -27.07 | -91.17 | 2346 |
| 80 | RSI momentum | momentum | 53.17 | -46.83 | 621 | 17.1 | -90.35 | -25.51 | -90.35 | 2387 |
| 81 | MACD zero-line | trend | 52.63 | -47.37 | 604 | 14.7 | -91.47 | -29.58 | -91.48 | 2366 |
| 82 | Triple EMA stack | trend | 52.03 | -47.97 | 646 | 15.5 | -93.21 | -29.91 | -93.21 | 2625 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.84 | -98.65 | 5391 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -33.00 | -97.34 | 3547 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -35.67 | -96.45 | 3620 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.22 | -25.51 | -94.22 | 2695 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.46 | -99.35 | 5692 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.48 | -31.89 | -96.48 | 3639 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.44 | -99.73 | 6206 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.52 | -97.35 | 3692 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.36 | -98.46 | 4704 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.49 | -32.73 | -93.49 | 2820 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.73 | -99.52 | 6150 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -33.05 | -95.85 | 3747 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.64 | -33.90 | -95.64 | 4087 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.10 | -99.89 | 8313 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T01:55 | VWAP reversion | buy | XRP-USD | 16.95 | — | entry signal |
| 2026-10-12T01:55 | VWAP reversion | buy | DOGE-USD | 16.95 | — | entry signal |
| 2026-10-12T01:55 | Z-score reversion | buy | DOGE-USD | 14.75 | — | entry signal |
| 2026-10-12T01:55 | RSI(14) reversion | buy | XRP-USD | 18.44 | — | entry signal |
| 2026-10-12T01:55 | RSI(14) reversion | buy | BTC-USD | 18.44 | — | entry signal |
| 2026-10-12T01:50 | Three white soldiers · 1h | sell | BTC-USD | 24.10 | -0.30 | stop-loss |
| 2026-10-12T01:50 | Donchian 55/20 | sell | SOL-USD | 17.34 | -0.21 | stop-loss |
| 2026-10-12T01:50 | Donchian 55/20 | sell | ETH-USD | 17.39 | -0.17 | stop-loss |
| 2026-10-12T01:50 | Donchian 20/10 | sell | ETH-USD | 13.65 | -0.12 | exit signal |
| 2026-10-12T01:50 | Supertrend | sell | SOL-USD | 12.58 | -0.12 | exit signal |
| 2026-10-12T01:50 | Supertrend | sell | ETH-USD | 12.60 | -0.11 | exit signal |
| 2026-10-12T01:50 | Triple EMA stack | sell | SOL-USD | 10.38 | -0.10 | exit signal |
| 2026-10-12T01:50 | Triple EMA stack | sell | ETH-USD | 10.43 | -0.07 | exit signal |
| 2026-10-12T01:50 | EMA 20/50 cross | buy | SOL-USD | 3.45 | — | rebalance up |
| 2026-10-12T01:50 | EMA 20/50 cross | sell | BTC-USD | 13.75 | -0.13 | stop-loss |
| 2026-10-12T01:45 | Donchian 55/20 | sell | BTC-USD | 17.42 | -0.15 | exit signal |
| 2026-10-12T01:45 | Donchian 20/10 | sell | SOL-USD | 13.62 | -0.12 | exit signal |
| 2026-10-12T01:45 | RSI momentum | sell | SOL-USD | 10.63 | -0.08 | exit signal |
| 2026-10-12T01:45 | RSI momentum | sell | ETH-USD | 10.66 | -0.07 | exit signal |
| 2026-10-12T01:45 | Trend pullback | sell | SOL-USD | 13.37 | -0.10 | exit signal |
| 2026-10-12T01:45 | Trend pullback | sell | ETH-USD | 13.29 | -0.13 | stop-loss |
| 2026-10-12T01:45 | Supertrend | sell | DOGE-USD | 15.72 | -0.18 | exit signal |
| 2026-10-12T01:45 | Supertrend | sell | BTC-USD | 12.63 | -0.09 | exit signal |
| 2026-10-12T01:45 | Triple EMA stack | sell | BTC-USD | 10.42 | -0.08 | exit signal |
| 2026-10-12T01:40 | Squeeze breakout | sell | SOL-USD | 17.60 | -0.16 | exit signal |
| 2026-10-12T01:40 | Keltner breakout | sell | SOL-USD | 15.51 | -0.14 | exit signal |
| 2026-10-12T01:35 | RSI momentum | sell | BTC-USD | 10.66 | -0.07 | exit signal |
| 2026-10-12T01:35 | Trend pullback | sell | BTC-USD | 10.70 | -0.07 | exit signal |
| 2026-10-12T01:35 | EMA 20/50 cross | sell | DOGE-USD | 17.20 | -0.15 | target is flat |
| 2026-10-12T01:30 | Squeeze breakout | sell | ETH-USD | 17.63 | -0.14 | stop-loss |
| 2026-10-12T01:30 | Squeeze breakout | sell | BTC-USD | 17.64 | -0.13 | stop-loss |
| 2026-10-12T01:30 | Keltner breakout | sell | ETH-USD | 15.51 | -0.14 | stop-loss |
| 2026-10-12T01:30 | Keltner breakout | sell | BTC-USD | 15.54 | -0.12 | stop-loss |
| 2026-10-12T01:30 | Bollinger breakout | sell | SOL-USD | 12.47 | -0.08 | Kill switch: down 50% from peak |
| 2026-10-12T01:30 | Bollinger breakout | sell | ETH-USD | 12.50 | -0.08 | Kill switch: down 50% from peak |
| 2026-10-12T01:30 | Bollinger breakout | sell | BTC-USD | 12.50 | -0.09 | Kill switch: down 50% from peak |
| 2026-10-12T01:30 | Donchian 20/10 | sell | DOGE-USD | 13.63 | -0.13 | exit signal |
| 2026-10-12T01:30 | Donchian 20/10 | sell | BTC-USD | 13.67 | -0.09 | exit signal |
| 2026-10-12T01:30 | RSI momentum | sell | DOGE-USD | 13.28 | -0.13 | stop-loss |
| 2026-10-12T01:30 | Trend pullback | sell | DOGE-USD | 13.35 | -0.12 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 01:55:05.000140+00:00 -> 2026-10-12 02:05:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
