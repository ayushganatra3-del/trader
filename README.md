# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T21:55:05.000145+00:00 · 19498 ticks

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

Today: 15675 decisions in 3135 calls, $0.2192 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T21:55 | 0 / 4 / 1 | SOL-USD 14%, NANC 18%, COIN 15% |  |
| Breezy | 2026-10-11T21:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T21:55 | 4 / 1 / 0 | COIN 76% |  |

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
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -15.29 | -2.51 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Hold BTC | benchmark | 99.82 | -0.18 | 0 | — | 30.10 | 3.57 | -8.68 | 1 |
| 14 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.21 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.17 | -0.82 | 89 | 55.1 | -9.71 | -1.87 | -14.61 | 340 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Donchian 55/20 · 1h | breakout | 99.04 | -0.96 | 28 | 14.3 | 12.77 | 1.60 | -16.96 | 113 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.38 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.73 | -6.39 | -25.39 | 172 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.15 | -2.08 | -9.46 | 260 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.47 | -17.67 | 40 |
| 29 | EMA 20/50 cross · 1h | trend | 96.62 | -3.38 | 40 | 12.5 | 4.78 | 0.75 | -19.85 | 139 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -0.64 | 0.06 | -13.84 | 253 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.89 | -0.22 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.77 | -4.23 | 114 | 23.7 | -14.75 | -2.36 | -17.27 | 467 |
| 34 | Supertrend · 1h | trend | 95.23 | -4.77 | 53 | 13.2 | 0.42 | 0.25 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -2.00 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.07 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -9.93 | -1.56 | -17.79 | 123 |
| 38 | Squeeze breakout · 1h | breakout | 93.43 | -6.57 | 39 | 23.1 | 23.27 | 3.18 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.24 | -0.38 | -9.03 | 146 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.21 | -6.04 | -20.97 | 250 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.84 | -0.52 | -12.59 | 435 |
| 42 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.96 | -5.01 | -23.36 | 316 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.33 | 0.73 | -17.13 | 224 |
| 44 | Volume breakout · 1h | breakout | 92.00 | -8.00 | 58 | 19.0 | 7.23 | 1.15 | -12.60 | 123 |
| 45 | Ichimoku · 1h | trend | 91.80 | -8.20 | 44 | 18.2 | -1.32 | 0.04 | -21.18 | 124 |
| 46 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.78 | -4.08 | -26.91 | 514 |
| 47 | Bollinger breakout · 1h | breakout | 91.25 | -8.75 | 72 | 27.8 | 5.69 | 0.90 | -13.62 | 289 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.54 | -0.97 | -26.47 | 242 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.59 | 118 | 33.1 | -26.31 | -5.11 | -28.40 | 510 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -6.96 | -0.86 | -14.35 | 414 |
| 52 | VWAP momentum · 1h | momentum | 89.49 | -10.51 | 283 | 21.9 | -32.41 | -4.84 | -39.16 | 1277 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.22 | -19.78 | 700 |
| 54 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.73 | -1.45 | -28.50 | 323 |
| 55 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -29.87 | -5.01 | -36.59 | 699 |
| 56 | Donchian 20/10 · 1h | breakout | 88.66 | -11.34 | 60 | 18.3 | -1.19 | 0.06 | -18.15 | 228 |
| 57 | MACD zero-line · 1h | trend | 88.07 | -11.93 | 66 | 18.2 | -7.19 | -0.79 | -20.88 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.83 | -12.17 | 104 | 13.5 | -9.66 | -1.11 | -21.96 | 342 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -47.96 | -23.16 | -47.97 | 589 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -12.56 | -1.47 | -25.51 | 221 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.08 | -1.21 | -23.57 | 412 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.73 | -16.57 | -73.91 | 1678 |
| 64 | RSI(14) reversion | reversion | 73.79 | -26.21 | 370 | 27.6 | -72.57 | -18.22 | -72.59 | 1492 |
| 65 | Squeeze breakout | breakout | 71.09 | -28.91 | 333 | 15.6 | -62.07 | -18.15 | -62.41 | 1231 |
| 66 | Volume breakout | breakout | 70.40 | -29.60 | 267 | 14.2 | -62.44 | -17.88 | -62.69 | 906 |
| 67 | Donchian 55/20 | breakout | 70.29 | -29.71 | 337 | 18.7 | -67.47 | -14.39 | -67.52 | 1295 |
| 68 | EMA 20/50 cross | trend | 69.47 | -30.53 | 340 | 20.3 | -76.68 | -15.29 | -76.76 | 1453 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.20 | -15.95 | -71.26 | 1426 |
| 70 | Supertrend | trend | 63.62 | -36.38 | 469 | 20.3 | -85.93 | -21.03 | -86.05 | 1913 |
| 71 | Keltner breakout | breakout | 62.64 | -37.36 | 457 | 14.9 | -83.67 | -27.62 | -83.74 | 1852 |
| 72 | Ichimoku | trend | 60.38 | -39.62 | 411 | 10.5 | -81.59 | -23.22 | -81.77 | 1749 |
| 73 | AI bee: Boozy | ai | 60.23 | -39.77 | 257 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 59.07 | -40.93 | 509 | 22.4 | -85.37 | -23.31 | -85.39 | 2085 |
| 75 | MFI reversion | reversion | 58.40 | -41.60 | 520 | 21.0 | -87.60 | -28.61 | -87.63 | 2126 |
| 76 | AI bee: Bizzy | ai | 57.25 | -42.75 | 845 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.28 | -43.72 | 548 | 10.4 | -89.20 | -35.08 | -89.23 | 2117 |
| 78 | Donchian 20/10 | breakout | 55.06 | -44.94 | 644 | 18.3 | -90.76 | -26.20 | -90.81 | 2667 |
| 79 | Trend pullback | trend | 53.92 | -46.08 | 595 | 14.6 | -91.06 | -27.29 | -91.06 | 2339 |
| 80 | RSI momentum | momentum | 53.68 | -46.32 | 616 | 17.2 | -90.32 | -25.84 | -90.38 | 2386 |
| 81 | MACD zero-line | trend | 53.01 | -46.99 | 599 | 14.9 | -91.46 | -30.21 | -91.50 | 2365 |
| 82 | Triple EMA stack | trend | 52.56 | -47.44 | 641 | 15.6 | -93.24 | -30.41 | -93.24 | 2628 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -31.33 | -98.64 | 5392 |
| 84 | Bollinger breakout | breakout | 50.44 | -49.56 | 679 | 14.6 | -93.50 | -33.29 | -93.54 | 2821 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -33.83 | -97.35 | 3549 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -36.27 | -96.43 | 3620 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -26.22 | -94.30 | 2700 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.61 | -99.35 | 5701 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.46 | -32.48 | -96.46 | 3636 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.74 | -99.73 | 6201 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.59 | -97.36 | 3692 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.82 | -98.47 | 4711 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.08 | -99.52 | 6152 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.83 | -33.82 | -95.84 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.63 | -34.79 | -95.63 | 4085 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.22 | -99.90 | 8319 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T21:55 | MFI reversion | buy | SOL-USD | 14.62 | — | entry signal |
| 2026-10-11T21:55 | MFI reversion | buy | DOGE-USD | 14.62 | — | entry signal |
| 2026-10-11T21:50 | Z-score reversion | sell | BTC-USD | 2.95 | -0.02 | rebalance down |
| 2026-10-11T21:45 | AI bee: Bizzy | buy | SOL-USD | 8.32 | — | Jev: buy (buy p=0.58) |
| 2026-10-11T21:35 | Z-score reversion | buy | SOL-USD | 8.90 | — | entry signal |
| 2026-10-11T21:35 | Z-score reversion | buy | ETH-USD | 11.83 | — | entry signal |
| 2026-10-11T21:35 | Z-score reversion | buy | DOGE-USD | 11.83 | — | entry signal |
| 2026-10-11T21:35 | Z-score reversion | sell | XRP-USD | 2.95 | -0.01 | rebalance down |
| 2026-10-11T21:35 | RSI(14) reversion | buy | SOL-USD | 18.45 | — | entry signal |
| 2026-10-11T21:30 | MFI reversion | buy | ETH-USD | 14.63 | — | entry signal |
| 2026-10-11T21:30 | MFI reversion | buy | BTC-USD | 14.63 | — | entry signal |
| 2026-10-11T21:30 | Z-score reversion | buy | BTC-USD | 14.79 | — | entry signal |
| 2026-10-11T21:30 | RSI(14) reversion | buy | BTC-USD | 18.45 | — | entry signal |
| 2026-10-11T21:30 | EMA 20/50 cross | sell | DOGE-USD | 13.93 | 0.10 | exit signal |
| 2026-10-11T21:25 | Z-score reversion | buy | XRP-USD | 14.80 | — | entry signal |
| 2026-10-11T21:25 | RSI(14) reversion | buy | ETH-USD | 18.46 | — | entry signal |
| 2026-10-11T21:25 | EMA 20/50 cross | sell | ETH-USD | 17.27 | 0.01 | exit signal |
| 2026-10-11T21:20 | Volume breakout · 1h | buy | ETH-USD | 7.71 | — | rebalance up |
| 2026-10-11T21:20 | Volume breakout · 1h | sell | SOL-USD | 14.47 | -0.30 | stop-loss |
| 2026-10-11T21:20 | Volume breakout · 1h | sell | BTC-USD | 15.24 | -0.19 | stop-loss |
| 2026-10-11T21:20 | Bollinger breakout · 1h | sell | DOGE-USD | 22.19 | -0.24 | stop-loss |
| 2026-10-11T21:20 | Donchian 55/20 · 1h | buy | ETH-USD | 3.63 | — | entry |
| 2026-10-11T21:20 | Donchian 55/20 · 1h | buy | DOGE-USD | 10.39 | — | rebalance up |
| 2026-10-11T21:20 | Donchian 55/20 · 1h | sell | BTC-USD | 14.02 | -0.17 | stop-loss |
| 2026-10-11T21:20 | Donchian 20/10 · 1h | buy | DOGE-USD | 6.30 | — | entry |
| 2026-10-11T21:20 | Donchian 20/10 · 1h | sell | BTC-USD | 6.30 | -0.08 | stop-loss |
| 2026-10-11T21:20 | Ichimoku · 1h | sell | SOL-USD | 22.76 | -0.45 | stop-loss |
| 2026-10-11T21:20 | MACD zero-line · 1h | sell | SOL-USD | 21.26 | -0.42 | stop-loss |
| 2026-10-11T21:20 | MACD cross · 1h | sell | BTC-USD | 4.52 | -0.06 | stop-loss |
| 2026-10-11T21:20 | EMA 20/50 cross · 1h | buy | DOGE-USD | 8.31 | — | entry |
| 2026-10-11T21:20 | EMA 20/50 cross · 1h | sell | ETH-USD | 8.31 | -0.14 | stop-loss |
| 2026-10-11T21:20 | MFI reversion | sell | BTC-USD | 14.62 | -0.14 | stop-loss |
| 2026-10-11T21:20 | Z-score reversion | sell | XRP-USD | 14.68 | -0.16 | stop-loss |
| 2026-10-11T21:15 | MFI reversion | sell | SOL-USD | 14.58 | -0.17 | stop-loss |
| 2026-10-11T21:15 | Squeeze breakout | sell | XRP-USD | 17.63 | -0.18 | stop-loss |
| 2026-10-11T21:15 | Bollinger breakout | sell | XRP-USD | 12.54 | -0.13 | stop-loss |
| 2026-10-11T21:15 | Donchian 20/10 | sell | XRP-USD | 13.66 | -0.14 | stop-loss |
| 2026-10-11T21:15 | Trend pullback | sell | DOGE-USD | 13.44 | -0.11 | exit signal |
| 2026-10-11T21:15 | MACD zero-line | sell | DOGE-USD | 13.19 | -0.11 | exit signal |
| 2026-10-11T21:15 | Triple EMA stack | sell | DOGE-USD | 13.08 | -0.11 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 21:55:05.000145+00:00 -> 2026-10-11 22:05:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
