# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T05:25:05.000134+00:00 · 19881 ticks

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

Today: 4350 decisions in 870 calls, $0.0609 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T05:25 | 0 / 1 / 4 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T05:25 | 2 / 2 / 1 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.26 | 3.26 | 37 | 43.2 | -7.53 | -2.27 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.49 | 2.49 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.17 | 2.17 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 101.98 | 1.98 | 14 | 57.1 | -12.39 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.29 | 1.29 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.21 | 1.21 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.05 | 1.05 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.35 | 0.35 | 0 | — | 31.12 | 3.64 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.72 | -0.28 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.66 | -0.34 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.26 | -0.74 | 28 | 14.3 | 13.26 | 1.64 | -16.96 | 114 |
| 19 | Stochastic reversion · 1h | reversion | 99.09 | -0.91 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.56 | -1.45 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.52 | -1.48 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.76 | -2.24 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.30 | -2.70 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.15 | -2.85 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.01 | -2.99 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | EMA 20/50 cross · 1h | trend | 96.72 | -3.28 | 40 | 12.5 | 6.37 | 0.91 | -19.85 | 136 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.49 | -2.09 | -10.17 | 263 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.27 | -3.73 | 58 | 20.7 | -0.58 | 0.07 | -13.84 | 253 |
| 31 | Parabolic SAR · 1h | trend | 96.23 | -3.77 | 82 | 22.0 | -1.97 | -0.09 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.84 | -4.16 | 115 | 23.5 | -14.63 | -2.32 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.67 | -4.33 | 53 | 13.2 | 2.04 | 0.45 | -18.22 | 208 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.45 | -6.54 | 119 | 34.5 | -10.04 | -1.58 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.40 | -6.60 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.05 | -6.95 | 26 | 26.9 | -2.19 | -0.37 | -9.03 | 144 |
| 40 | Connors RSI(2) · 1h | reversion | 93.00 | -7.00 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.78 | -7.22 | 392 | 18.4 | -3.00 | -0.41 | -12.84 | 425 |
| 42 | Bollinger reversion · 1h | reversion | 92.71 | -7.29 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.61 | -7.38 | 64 | 15.6 | 4.67 | 0.76 | -17.15 | 226 |
| 44 | Volume breakout · 1h | breakout | 92.23 | -7.77 | 58 | 19.0 | 7.79 | 1.21 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 92.16 | -7.84 | 44 | 18.2 | -0.81 | 0.10 | -21.18 | 125 |
| 46 | Williams %R · 1h | reversion | 91.50 | -8.50 | 126 | 47.6 | -23.78 | -4.05 | -26.91 | 510 |
| 47 | Bollinger breakout · 1h | breakout | 91.18 | -8.82 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.64 | -9.36 | 69 | 15.9 | -8.32 | -0.81 | -26.49 | 241 |
| 50 | Candlestick reversal · 1h | reversion | 90.34 | -9.66 | 118 | 33.1 | -26.33 | -5.08 | -28.36 | 507 |
| 51 | CCI reversion · 1h | reversion | 89.91 | -10.09 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.46 | -10.54 | 284 | 21.8 | -32.14 | -4.75 | -39.17 | 1279 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.69 | -11.31 | 149 | 18.8 | -13.20 | -1.51 | -28.57 | 327 |
| 55 | Donchian 20/10 · 1h | breakout | 88.66 | -11.34 | 60 | 18.3 | -0.48 | 0.15 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.58 | -11.42 | 138 | 25.4 | -29.88 | -4.98 | -36.60 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.31 | -11.69 | 66 | 18.2 | -6.54 | -0.70 | -20.89 | 239 |
| 58 | Max aggression: 5-day momentum | meta | 87.89 | -12.11 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.87 | -12.12 | 104 | 13.5 | -8.59 | -0.95 | -21.96 | 339 |
| 60 | Keltner breakout · 1h | breakout | 87.02 | -12.98 | 43 | 18.6 | -11.89 | -1.37 | -25.69 | 220 |
| 61 | Three white soldiers | momentum | 86.87 | -13.13 | 146 | 17.1 | -48.15 | -23.03 | -48.18 | 593 |
| 62 | ROC + volume · 1h | momentum | 86.19 | -13.80 | 132 | 21.2 | -10.00 | -1.19 | -23.48 | 415 |
| 63 | ROC + volume | momentum | 74.60 | -25.39 | 395 | 23.3 | -72.84 | -16.45 | -73.94 | 1682 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 375 | 27.5 | -72.29 | -17.88 | -72.34 | 1487 |
| 65 | Squeeze breakout | breakout | 70.58 | -29.42 | 338 | 15.4 | -62.14 | -17.98 | -62.23 | 1235 |
| 66 | Volume breakout | breakout | 69.88 | -30.12 | 271 | 14.0 | -62.52 | -17.83 | -62.54 | 907 |
| 67 | Donchian 55/20 | breakout | 68.99 | -31.01 | 343 | 18.4 | -68.00 | -14.52 | -68.03 | 1304 |
| 68 | EMA 20/50 cross | trend | 68.95 | -31.05 | 344 | 20.1 | -76.74 | -15.19 | -76.81 | 1457 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 405 | 25.9 | -71.09 | -15.75 | -71.15 | 1426 |
| 70 | Supertrend | trend | 62.99 | -37.01 | 475 | 20.0 | -85.92 | -20.84 | -86.08 | 1916 |
| 71 | Keltner breakout | breakout | 61.67 | -38.33 | 465 | 14.6 | -83.81 | -27.64 | -83.83 | 1859 |
| 72 | AI bee: Boozy | ai | 60.04 | -39.96 | 260 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 59.50 | -40.50 | 416 | 10.3 | -81.76 | -23.12 | -81.77 | 1754 |
| 74 | Z-score reversion | reversion | 58.93 | -41.07 | 516 | 22.1 | -85.05 | -22.69 | -85.06 | 2073 |
| 75 | MFI reversion | reversion | 58.32 | -41.68 | 525 | 20.8 | -87.51 | -27.85 | -87.55 | 2122 |
| 76 | AI bee: Bizzy | ai | 56.33 | -43.67 | 865 | 8.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.67 | -44.33 | 555 | 10.3 | -89.20 | -34.51 | -89.20 | 2118 |
| 78 | Donchian 20/10 | breakout | 54.13 | -45.87 | 651 | 18.1 | -90.82 | -26.00 | -90.83 | 2673 |
| 79 | Trend pullback | trend | 52.84 | -47.16 | 612 | 14.7 | -91.17 | -27.00 | -91.20 | 2349 |
| 80 | RSI momentum | momentum | 52.67 | -47.33 | 626 | 16.9 | -90.43 | -25.73 | -90.46 | 2395 |
| 81 | MACD zero-line | trend | 52.39 | -47.61 | 606 | 14.7 | -91.49 | -29.69 | -91.50 | 2368 |
| 82 | Triple EMA stack | trend | 51.68 | -48.32 | 650 | 15.4 | -93.27 | -30.15 | -93.28 | 2633 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -30.93 | -98.64 | 5389 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -33.22 | -97.37 | 3556 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -35.93 | -96.48 | 3630 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.21 | -25.38 | -94.21 | 2699 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.35 | -99.34 | 5684 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.51 | -32.12 | -96.51 | 3648 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -41.51 | -99.73 | 6205 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.83 | -97.37 | 3699 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.42 | -36.17 | -98.43 | 4698 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.53 | -33.03 | -93.54 | 2827 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.76 | -99.52 | 6149 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.74 | -32.79 | -95.74 | 3734 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.57 | -33.74 | -95.57 | 4080 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.55 | -99.89 | 8312 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T05:25 | Three white soldiers | sell | SOL-USD | 17.43 | -0.00 | exit signal |
| 2026-10-12T05:25 | Three white soldiers | sell | ETH-USD | 21.69 | -0.10 | exit signal |
| 2026-10-12T05:25 | Three white soldiers | sell | BTC-USD | 17.39 | -0.04 | exit signal |
| 2026-10-12T05:25 | Volume breakout | sell | ETH-USD | 17.40 | -0.13 | exit signal |
| 2026-10-12T05:25 | Volume breakout | sell | BTC-USD | 17.42 | -0.11 | exit signal |
| 2026-10-12T05:25 | Squeeze breakout | sell | XRP-USD | 17.60 | -0.07 | stop-loss |
| 2026-10-12T05:25 | Squeeze breakout | sell | ETH-USD | 17.60 | -0.07 | stop-loss |
| 2026-10-12T05:25 | Keltner breakout | buy | BTC-USD | 3.12 | — | rebalance up |
| 2026-10-12T05:25 | Keltner breakout | sell | XRP-USD | 12.30 | -0.05 | stop-loss |
| 2026-10-12T05:25 | Keltner breakout | sell | ETH-USD | 12.30 | -0.05 | stop-loss |
| 2026-10-12T05:25 | Ichimoku | buy | SOL-USD | 2.99 | — | rebalance up |
| 2026-10-12T05:25 | Ichimoku | sell | XRP-USD | 11.85 | -0.12 | stop-loss |
| 2026-10-12T05:20 | Three white soldiers | buy | ETH-USD | 4.36 | — | rebalance up |
| 2026-10-12T05:20 | Three white soldiers | buy | DOGE-USD | 4.40 | — | rebalance up |
| 2026-10-12T05:20 | Three white soldiers | sell | XRP-USD | 17.36 | -0.06 | exit signal |
| 2026-10-12T05:15 | ROC + volume | buy | DOGE-USD | 7.53 | — | entry signal |
| 2026-10-12T05:15 | ROC + volume | sell | SOL-USD | 3.80 | -0.00 | rebalance down |
| 2026-10-12T05:15 | ROC + volume | sell | ETH-USD | 3.73 | -0.01 | rebalance down |
| 2026-10-12T05:14 | AI bee: Bizzy | sell | SOL-USD | 8.51 | -0.05 | Jev: sell (sell p=0.58) after 11 min |
| 2026-10-12T05:10 | ROC + volume | buy | BTC-USD | 18.72 | — | entry signal |
| 2026-10-12T05:10 | Ichimoku | buy | XRP-USD | 11.97 | — | entry signal |
| 2026-10-12T05:10 | Ichimoku | buy | SOL-USD | 11.98 | — | entry signal |
| 2026-10-12T05:10 | Ichimoku | buy | DOGE-USD | 11.98 | — | entry signal |
| 2026-10-12T05:10 | Ichimoku | buy | BTC-USD | 11.98 | — | entry signal |
| 2026-10-12T05:10 | Ichimoku | sell | ETH-USD | 3.02 | -0.00 | rebalance down |
| 2026-10-12T05:03 | AI bee: Bizzy | buy | SOL-USD | 8.56 | — | Jev: buy (buy p=0.61) |
| 2026-10-12T05:00 | Ichimoku · 1h | buy | XRP-USD | 23.09 | — | entry signal |
| 2026-10-12T05:00 | MACD cross · 1h | buy | XRP-USD | 4.57 | — | entry signal |
| 2026-10-12T05:00 | MACD cross · 1h | buy | BTC-USD | 4.57 | — | entry signal |
| 2026-10-12T04:56 | AI bee: Bizzy | sell | XRP-USD | 8.96 | -0.01 | Jev: sell (sell p=0.54) after 26 min |
| 2026-10-12T04:55 | RSI momentum | buy | BTC-USD | 2.64 | — | rebalance up |
| 2026-10-12T04:55 | RSI momentum | sell | DOGE-USD | 2.64 | 0.00 | rebalance down |
| 2026-10-12T04:50 | AI bee: Bizzy | sell | ETH-USD | 10.73 | -0.04 | Jev: sell (sell p=0.52) after 17 min |
| 2026-10-12T04:50 | MFI reversion | sell | BTC-USD | 14.56 | -0.03 | exit signal |
| 2026-10-12T04:50 | Triple EMA stack | buy | BTC-USD | 7.78 | — | entry signal |
| 2026-10-12T04:50 | Triple EMA stack | sell | SOL-USD | 2.59 | -0.00 | rebalance down |
| 2026-10-12T04:50 | Triple EMA stack | sell | ETH-USD | 2.58 | -0.01 | rebalance down |
| 2026-10-12T04:50 | Triple EMA stack | sell | DOGE-USD | 2.61 | 0.00 | rebalance down |
| 2026-10-12T04:50 | EMA 20/50 cross | buy | BTC-USD | 17.25 | — | entry signal |
| 2026-10-12T04:47 | AI bee: Boozy | sell | ETH-USD | 14.29 | -0.02 | Jev: add (buy p=0.61) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 05:25:05.000134+00:00 -> 2026-10-12 05:35:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
