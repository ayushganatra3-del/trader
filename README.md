# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T23:55:05.000143+00:00 · 19589 ticks

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

Today: 17040 decisions in 3408 calls, $0.2382 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T23:55 | 0 / 4 / 1 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-11T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T23:55 | 4 / 1 / 0 | COIN 76% |  |

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
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -15.28 | -2.51 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.08 | 0.08 | 0 | — | 30.41 | 3.60 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.21 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.71 | -1.87 | -14.61 | 340 |
| 19 | Donchian 55/20 · 1h | breakout | 99.11 | -0.89 | 28 | 14.3 | 12.91 | 1.62 | -16.96 | 113 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.38 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.73 | -6.39 | -25.39 | 172 |
| 27 | EMA 20/50 cross · 1h | trend | 96.68 | -3.32 | 40 | 12.5 | 5.73 | 0.85 | -19.85 | 137 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.23 | -2.10 | -9.70 | 259 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -0.49 | 0.09 | -13.84 | 253 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.89 | -0.22 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.84 | -4.16 | 114 | 23.7 | -15.06 | -2.42 | -17.27 | 468 |
| 34 | Supertrend · 1h | trend | 95.38 | -4.62 | 53 | 13.2 | 0.71 | 0.28 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -2.00 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.07 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.04 | -1.59 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.43 | -6.57 | 39 | 23.1 | 23.27 | 3.18 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.01 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.10 | -5.99 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -6.10 | -0.99 | -13.92 | 427 |
| 42 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.88 | -4.99 | -23.34 | 314 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.42 | 0.74 | -17.13 | 224 |
| 44 | Volume breakout · 1h | breakout | 92.08 | -7.92 | 58 | 19.0 | 7.32 | 1.16 | -12.60 | 123 |
| 45 | Ichimoku · 1h | trend | 91.93 | -8.07 | 44 | 18.2 | -1.16 | 0.06 | -21.18 | 124 |
| 46 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.78 | -4.08 | -26.91 | 514 |
| 47 | Bollinger breakout · 1h | breakout | 91.25 | -8.75 | 72 | 27.8 | 5.74 | 0.91 | -13.62 | 289 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.36 | -0.95 | -26.47 | 243 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 118 | 33.1 | -26.10 | -5.07 | -28.13 | 506 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -6.96 | -0.86 | -14.35 | 414 |
| 52 | VWAP momentum · 1h | momentum | 89.51 | -10.49 | 283 | 21.9 | -32.26 | -4.81 | -39.17 | 1276 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.95 | -1.48 | -28.57 | 325 |
| 55 | Donchian 20/10 · 1h | breakout | 88.68 | -11.32 | 60 | 18.3 | -1.11 | 0.07 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -29.89 | -5.01 | -36.60 | 699 |
| 57 | MACD zero-line · 1h | trend | 88.14 | -11.86 | 66 | 18.2 | -7.11 | -0.78 | -20.88 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.87 | -12.13 | 104 | 13.5 | -9.25 | -1.05 | -21.96 | 341 |
| 60 | Three white soldiers | momentum | 87.18 | -12.82 | 142 | 17.6 | -48.03 | -23.22 | -48.04 | 589 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -12.52 | -1.47 | -25.51 | 221 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.11 | -1.21 | -23.48 | 414 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.73 | -16.57 | -73.90 | 1677 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 373 | 27.3 | -72.47 | -18.16 | -72.49 | 1489 |
| 65 | Squeeze breakout | breakout | 71.09 | -28.91 | 333 | 15.6 | -62.00 | -18.10 | -62.34 | 1230 |
| 66 | Volume breakout | breakout | 70.40 | -29.60 | 267 | 14.2 | -62.31 | -17.86 | -62.56 | 904 |
| 67 | Donchian 55/20 | breakout | 70.24 | -29.77 | 337 | 18.7 | -67.30 | -14.34 | -67.48 | 1293 |
| 68 | EMA 20/50 cross | trend | 69.28 | -30.72 | 340 | 20.3 | -76.63 | -15.29 | -76.70 | 1456 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.16 | -15.97 | -71.22 | 1426 |
| 70 | Supertrend | trend | 63.47 | -36.53 | 469 | 20.3 | -85.88 | -21.03 | -85.96 | 1913 |
| 71 | Keltner breakout | breakout | 62.64 | -37.36 | 457 | 14.9 | -83.70 | -27.60 | -83.77 | 1853 |
| 72 | Ichimoku | trend | 60.38 | -39.62 | 411 | 10.5 | -81.59 | -23.22 | -81.77 | 1749 |
| 73 | AI bee: Boozy | ai | 60.23 | -39.77 | 257 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 58.98 | -41.02 | 514 | 22.2 | -85.39 | -23.32 | -85.39 | 2085 |
| 75 | MFI reversion | reversion | 58.35 | -41.65 | 524 | 20.8 | -87.59 | -28.61 | -87.63 | 2125 |
| 76 | AI bee: Bizzy | ai | 57.01 | -42.99 | 850 | 8.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.94 | -44.06 | 551 | 10.3 | -89.18 | -35.27 | -89.18 | 2116 |
| 78 | Donchian 20/10 | breakout | 54.95 | -45.05 | 644 | 18.3 | -90.78 | -26.23 | -90.81 | 2670 |
| 79 | Trend pullback | trend | 53.83 | -46.17 | 595 | 14.6 | -91.08 | -27.32 | -91.08 | 2342 |
| 80 | RSI momentum | momentum | 53.56 | -46.44 | 616 | 17.2 | -90.28 | -25.80 | -90.32 | 2385 |
| 81 | MACD zero-line | trend | 52.90 | -47.10 | 599 | 14.9 | -91.44 | -30.15 | -91.46 | 2366 |
| 82 | Triple EMA stack | trend | 52.43 | -47.57 | 641 | 15.6 | -93.20 | -30.43 | -93.20 | 2628 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -31.25 | -98.63 | 5384 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.33 | -33.77 | -97.34 | 3550 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -36.45 | -96.44 | 3621 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.18 | -25.90 | -94.18 | 2691 |
| 87 | Bollinger breakout | breakout | 50.32 | -49.68 | 679 | 14.6 | -93.51 | -33.39 | -93.54 | 2823 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.48 | -99.34 | 5688 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.44 | -32.39 | -96.44 | 3633 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.76 | -99.73 | 6207 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.67 | -97.37 | 3696 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -37.62 | -98.46 | 4705 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.00 | -99.52 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.83 | -33.79 | -95.83 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.62 | -34.77 | -95.63 | 4083 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.17 | -99.90 | 8319 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T23:55 | Bollinger breakout | buy | BTC-USD | 12.59 | — | entry signal |
| 2026-10-11T23:55 | Donchian 55/20 | buy | BTC-USD | 17.57 | — | entry signal |
| 2026-10-11T23:52 | AI bee: Bizzy | sell | DOGE-USD | 8.83 | -0.05 | Jev: sell (sell p=0.59) after 12 min |
| 2026-10-11T23:50 | Trend pullback | buy | SOL-USD | 13.46 | — | entry signal |
| 2026-10-11T23:45 | Triple EMA stack | buy | SOL-USD | 13.11 | — | entry signal |
| 2026-10-11T23:40 | AI bee: Bizzy | buy | DOGE-USD | 8.88 | — | Jev: buy (buy p=0.62) |
| 2026-10-11T23:40 | Bollinger breakout | buy | XRP-USD | 12.60 | — | entry signal |
| 2026-10-11T23:40 | EMA 20/50 cross | buy | SOL-USD | 17.33 | — | entry signal |
| 2026-10-11T23:35 | RSI momentum | buy | XRP-USD | 13.40 | — | entry signal |
| 2026-10-11T23:35 | Triple EMA stack | buy | XRP-USD | 13.12 | — | entry signal |
| 2026-10-11T23:35 | EMA 20/50 cross | buy | XRP-USD | 17.34 | — | entry signal |
| 2026-10-11T23:30 | Trend pullback | buy | BTC-USD | 13.47 | — | entry signal |
| 2026-10-11T23:30 | Supertrend | buy | XRP-USD | 15.87 | — | entry signal |
| 2026-10-11T23:30 | MACD zero-line | buy | DOGE-USD | 2.67 | — | entry signal |
| 2026-10-11T23:30 | MACD zero-line | sell | XRP-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-11T23:25 | Trend pullback | buy | ETH-USD | 13.48 | — | entry signal |
| 2026-10-11T23:20 | ADX DI cross | sell | SOL-USD | 13.90 | -0.11 | exit signal |
| 2026-10-11T23:10 | MFI reversion | sell | DOGE-USD | 14.56 | -0.06 | exit signal |
| 2026-10-11T23:10 | EMA 20/50 cross | buy | BTC-USD | 17.35 | — | entry signal |
| 2026-10-11T23:05 | Z-score reversion | sell | DOGE-USD | 14.76 | -0.05 | exit signal |
| 2026-10-11T23:05 | Bollinger breakout | buy | DOGE-USD | 12.61 | — | entry signal |
| 2026-10-11T23:05 | Donchian 20/10 | buy | ETH-USD | 13.76 | — | entry signal |
| 2026-10-11T23:05 | Donchian 20/10 | buy | DOGE-USD | 13.76 | — | entry signal |
| 2026-10-11T23:05 | Donchian 20/10 | buy | BTC-USD | 13.76 | — | entry signal |
| 2026-10-11T23:05 | RSI momentum | buy | ETH-USD | 13.42 | — | entry signal |
| 2026-10-11T23:05 | RSI momentum | buy | BTC-USD | 13.42 | — | entry signal |
| 2026-10-11T23:05 | ADX DI cross | buy | SOL-USD | 14.01 | — | entry signal |
| 2026-10-11T23:05 | Supertrend | buy | ETH-USD | 15.89 | — | entry signal |
| 2026-10-11T23:05 | Triple EMA stack | buy | BTC-USD | 13.13 | — | entry signal |
| 2026-10-11T23:05 | EMA 20/50 cross | buy | ETH-USD | 17.37 | — | entry signal |
| 2026-10-11T23:00 | Triple EMA stack | buy | ETH-USD | 13.14 | — | entry signal |
| 2026-10-11T22:55 | Three white soldiers | sell | DOGE-USD | 21.67 | -0.17 | exit signal |
| 2026-10-11T22:55 | ADX DI cross | sell | SOL-USD | 13.95 | -0.09 | exit signal |
| 2026-10-11T22:53 | AI bee: Bizzy | sell | DOGE-USD | 7.98 | -0.06 | Jev: sell (sell p=0.84) after 10 min |
| 2026-10-11T22:50 | ADX DI cross | buy | SOL-USD | 14.05 | — | entry signal |
| 2026-10-11T22:50 | ADX DI cross | sell | DOGE-USD | 13.96 | -0.10 | exit signal |
| 2026-10-11T22:45 | RSI(14) reversion | sell | ETH-USD | 18.44 | -0.03 | exit signal |
| 2026-10-11T22:45 | Three white soldiers | buy | DOGE-USD | 21.84 | — | entry signal |
| 2026-10-11T22:45 | ADX DI cross | buy | DOGE-USD | 14.06 | — | entry signal |
| 2026-10-11T22:43 | AI bee: Bizzy | buy | DOGE-USD | 8.04 | — | Jev: buy (buy p=0.56) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 23:55:05.000143+00:00 -> 2026-10-12 00:05:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
