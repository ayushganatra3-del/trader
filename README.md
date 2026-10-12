# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T21:53:05.000158+00:00 · 20618 ticks

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
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.55 · VIX 15.24 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 33897 decisions in 3081 calls, $0.4235 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T21:53 | 0 / 3 / 2 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-12T21:53 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T21:53 | 1 / 4 / 0 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.93 | 2.93 | 0 | — | 1.61 | 0.84 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.07 | 2.07 | 16 | 50.0 | -12.87 | -2.14 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.44 | 1.44 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.11 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.52 | -2.85 | -13.79 | 118 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.23 | 1.23 | 0 | — | 1.71 | 0.84 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.66 | 0.66 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.64 | 0.64 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.31 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.44 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.14 | 0.14 | 0 | — | 3.58 | 1.41 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.38 | -0.62 | 0 | — | -4.89 | -2.27 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.66 | -1.80 | 78 |
| 17 | Hold BTC | benchmark | 98.92 | -1.08 | 0 | — | 29.42 | 3.49 | -8.68 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.80 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.25 | -1.75 | 31 | 12.9 | 12.04 | 1.46 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.15 | -1.85 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 98.02 | -1.98 | 11 | 36.4 | -16.71 | -0.63 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.89 | -2.11 | 78 | 23.1 | -23.01 | -6.47 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.63 | -4.53 | 27 |
| 24 | Stochastic reversion · 1h | reversion | 97.14 | -2.86 | 96 | 53.1 | -12.25 | -2.39 | -13.91 | 341 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 97.04 | -2.96 | 0 | — | 9.02 | 1.51 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.86 | -3.14 | 44 | 43.2 | 3.43 | 0.81 | -8.60 | 160 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.49 | -3.51 | 62 | 19.4 | -6.64 | -1.08 | -13.79 | 256 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.76 | -2.79 | -9.12 | 296 |
| 30 | MACD cross · 1h | trend | 95.86 | -4.14 | 125 | 24.0 | -11.00 | -1.72 | -17.79 | 459 |
| 31 | Parabolic SAR · 1h | trend | 95.37 | -4.63 | 86 | 22.1 | 1.20 | 0.35 | -21.52 | 291 |
| 32 | EMA 20/50 cross · 1h | trend | 95.36 | -4.64 | 45 | 15.6 | 4.87 | 0.75 | -23.71 | 136 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.96 | -3.86 | -8.72 | 232 |
| 34 | Supertrend · 1h | trend | 94.57 | -5.43 | 58 | 13.8 | 1.32 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.17 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.51 | -6.49 | 39 | 23.1 | 15.62 | 2.48 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.46 | -6.54 | 151 | 32.5 | -7.75 | -1.18 | -16.91 | 128 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.25 | -2.77 | -6.47 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.63 | -7.37 | 66 | 15.2 | -0.63 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.54 | -7.46 | 115 | 43.5 | -18.87 | -6.28 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.52 | -7.48 | 439 | 17.8 | 1.10 | 0.34 | -12.73 | 400 |
| 42 | RSI(14) reversion · 1h | reversion | 91.83 | -8.17 | 32 | 28.1 | 0.51 | 0.23 | -9.03 | 131 |
| 43 | Volume breakout · 1h | breakout | 91.73 | -8.27 | 70 | 20.0 | 9.08 | 1.39 | -12.60 | 117 |
| 44 | Bollinger reversion · 1h | reversion | 91.21 | -8.79 | 83 | 37.3 | -23.38 | -5.79 | -24.24 | 316 |
| 45 | Ichimoku · 1h | trend | 91.03 | -8.97 | 48 | 16.7 | 0.43 | 0.26 | -22.34 | 128 |
| 46 | Bollinger breakout · 1h | breakout | 90.88 | -9.12 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 71 | 15.5 | -6.99 | -0.60 | -27.17 | 236 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.74 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 89.06 | -10.94 | 112 | 45.5 | -10.73 | -1.45 | -14.35 | 409 |
| 50 | Williams %R · 1h | reversion | 88.97 | -11.03 | 133 | 45.9 | -26.49 | -4.42 | -28.24 | 507 |
| 51 | OBV trend · 1h | momentum | 88.73 | -11.27 | 150 | 18.7 | -12.46 | -1.19 | -34.14 | 317 |
| 52 | VWAP momentum · 1h | momentum | 88.26 | -11.74 | 311 | 23.2 | -33.03 | -4.95 | -40.22 | 1253 |
| 53 | Max aggression: 5-day momentum | meta | 88.11 | -11.89 | 7 | 28.6 | -14.35 | -1.05 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 88.11 | -11.89 | 128 | 31.2 | -29.08 | -5.61 | -29.19 | 500 |
| 55 | Donchian 20/10 · 1h | breakout | 87.73 | -12.27 | 63 | 17.5 | -0.60 | 0.13 | -19.51 | 214 |
| 56 | Heikin-Ashi · 1h | trend | 87.72 | -12.28 | 153 | 28.1 | -30.61 | -5.11 | -37.65 | 678 |
| 57 | MACD zero-line · 1h | trend | 87.61 | -12.39 | 67 | 17.9 | -21.66 | -4.04 | -21.73 | 234 |
| 58 | EMA 9/21 cross · 1h | trend | 87.12 | -12.88 | 108 | 13.0 | -8.22 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.07 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.66 | -13.34 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.46 | -13.54 | 153 | 17.0 | -48.61 | -23.66 | -48.61 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.54 | -14.46 | 164 | 20.1 | -9.07 | -1.05 | -25.01 | 401 |
| 63 | ROC + volume | momentum | 72.29 | -27.71 | 421 | 22.3 | -72.96 | -16.62 | -74.61 | 1658 |
| 64 | RSI(14) reversion | reversion | 70.74 | -29.26 | 416 | 26.7 | -72.64 | -17.95 | -72.67 | 1467 |
| 65 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.33 | -18.22 | -62.33 | 1223 |
| 66 | Volume breakout | breakout | 69.45 | -30.55 | 279 | 14.7 | -61.73 | -17.61 | -61.73 | 894 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 357 | 19.9 | -76.44 | -15.20 | -76.44 | 1431 |
| 68 | Donchian 55/20 | breakout | 66.63 | -33.37 | 360 | 17.5 | -68.25 | -14.42 | -69.10 | 1291 |
| 69 | VWAP reversion | reversion | 64.63 | -35.37 | 458 | 25.5 | -71.80 | -15.87 | -71.80 | 1402 |
| 70 | AI bee: Boozy | ai | 60.33 | -39.66 | 261 | 5.0 | — | — | — | — |
| 71 | Keltner breakout | breakout | 60.30 | -39.70 | 485 | 14.6 | -83.27 | -27.40 | -83.27 | 1836 |
| 72 | Supertrend | trend | 60.00 | -40.00 | 503 | 19.3 | -86.09 | -21.07 | -86.09 | 1893 |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.25 | -23.19 | -82.25 | 1734 |
| 74 | Z-score reversion | reversion | 55.80 | -44.20 | 563 | 22.2 | -85.66 | -23.22 | -85.69 | 2065 |
| 75 | AI bee: Bizzy | ai | 55.48 | -44.52 | 889 | 8.3 | — | — | — | — |
| 76 | MFI reversion | reversion | 55.35 | -44.65 | 619 | 19.5 | -87.90 | -28.39 | -87.94 | 2114 |
| 77 | ADX DI cross | trend | 53.41 | -46.59 | 599 | 10.0 | -89.09 | -34.51 | -89.09 | 2100 |
| 78 | Donchian 20/10 | breakout | 51.89 | -48.11 | 684 | 17.5 | -90.90 | -26.09 | -90.90 | 2644 |
| 79 | MACD zero-line | trend | 50.91 | -49.09 | 635 | 14.5 | -91.51 | -30.11 | -91.51 | 2347 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -30.83 | -98.61 | 5327 |
| 81 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.67 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.26 | -30.32 | -93.26 | 2601 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.58 | -25.70 | -90.58 | 2363 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -33.45 | -97.39 | 3523 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.41 | -36.28 | -96.41 | 3587 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -25.78 | -94.31 | 2627 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.13 | -99.36 | 5630 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -31.51 | -96.30 | 3592 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.43 | -99.73 | 6146 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.30 | -38.39 | -97.30 | 3655 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.24 | -98.50 | 4661 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.40 | -33.07 | -93.40 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.40 | -99.53 | 6107 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -33.53 | -95.90 | 3724 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -34.66 | -95.72 | 4050 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.18 | -99.89 | 8204 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T21:50 | Agent (rotation) | sell | SOL-USD | 7.83 | -0.18 | selected signal exited |
| 2026-10-12T21:50 | CCI reversion · 1h | buy | BTC-USD | 3.66 | — | entry |
| 2026-10-12T21:50 | CCI reversion · 1h | sell | ETH-USD | 3.66 | -0.07 | stop-loss |
| 2026-10-12T21:50 | Williams %R · 1h | buy | SOL-USD | 12.76 | — | entry |
| 2026-10-12T21:50 | Williams %R · 1h | buy | ETH-USD | 4.77 | — | rebalance up |
| 2026-10-12T21:50 | Williams %R · 1h | sell | DOGE-USD | 17.53 | -0.40 | stop-loss |
| 2026-10-12T21:50 | VWAP reversion · 1h | sell | SOL-USD | 25.00 | -0.58 | stop-loss |
| 2026-10-12T21:50 | Candlestick reversal · 1h | buy | BTC-USD | 10.00 | — | entry |
| 2026-10-12T21:50 | Candlestick reversal · 1h | sell | DOGE-USD | 10.00 | -0.19 | stop-loss |
| 2026-10-12T21:50 | VWAP reversion | buy | SOL-USD | 3.25 | — | rebalance up |
| 2026-10-12T21:50 | VWAP reversion | sell | XRP-USD | 16.13 | -0.25 | stop-loss |
| 2026-10-12T21:45 | Agent (rotation) | sell | XRP-USD | 7.83 | -0.18 | selected signal exited |
| 2026-10-12T21:45 | VWAP reversion · 1h | sell | XRP-USD | 25.00 | -0.58 | stop-loss |
| 2026-10-12T21:45 | RSI(14) reversion · 1h | buy | SOL-USD | 2.24 | — | entry |
| 2026-10-12T21:45 | RSI(14) reversion · 1h | sell | XRP-USD | 2.24 | -0.02 | stop-loss |
| 2026-10-12T21:45 | VWAP reversion | buy | XRP-USD | 3.30 | — | rebalance up |
| 2026-10-12T21:45 | VWAP reversion | sell | ETH-USD | 12.94 | -0.16 | stop-loss |
| 2026-10-12T21:45 | VWAP reversion | sell | DOGE-USD | 12.89 | -0.21 | stop-loss |
| 2026-10-12T21:45 | Donchian 55/20 | sell | BTC-USD | 16.58 | -0.17 | stop-loss |
| 2026-10-12T21:45 | EMA 20/50 cross | sell | BTC-USD | 16.88 | -0.15 | stop-loss |
| 2026-10-12T21:40 | MFI reversion | sell | DOGE-USD | 13.74 | -0.13 | stop-loss |
| 2026-10-12T21:40 | Ichimoku | sell | BTC-USD | 14.26 | -0.06 | exit signal |
| 2026-10-12T21:30 | MFI reversion | buy | DOGE-USD | 13.87 | — | entry signal |
| 2026-10-12T21:30 | ADX DI cross | sell | BTC-USD | 13.28 | -0.09 | exit signal |
| 2026-10-12T21:20 | ADX DI cross | buy | BTC-USD | 13.37 | — | entry signal |
| 2026-10-12T21:15 | Supertrend | sell | XRP-USD | 14.99 | -0.10 | exit signal |
| 2026-10-12T21:15 | Supertrend | sell | BTC-USD | 14.99 | -0.07 | exit signal |
| 2026-10-12T21:15 | EMA 20/50 cross | sell | DOGE-USD | 16.85 | -0.16 | stop-loss |
| 2026-10-12T21:10 | Donchian 20/10 | sell | BTC-USD | 10.39 | -0.04 | exit signal |
| 2026-10-12T21:10 | ROC + volume | sell | BTC-USD | 18.08 | -0.14 | stop-loss |
| 2026-10-12T21:10 | ADX DI cross | sell | BTC-USD | 13.40 | -0.05 | exit signal |
| 2026-10-12T21:05 | Three white soldiers | sell | BTC-USD | 21.56 | -0.08 | exit signal |
| 2026-10-12T21:05 | Volume breakout | sell | BTC-USD | 17.35 | -0.05 | exit signal |
| 2026-10-12T21:05 | Squeeze breakout | sell | SOL-USD | 13.88 | -0.09 | stop-loss |
| 2026-10-12T21:05 | Squeeze breakout | sell | BTC-USD | 13.93 | -0.04 | stop-loss |
| 2026-10-12T21:05 | Keltner breakout | sell | SOL-USD | 12.05 | -0.09 | stop-loss |
| 2026-10-12T21:05 | Keltner breakout | sell | BTC-USD | 12.10 | -0.03 | stop-loss |
| 2026-10-12T21:05 | Donchian 55/20 | sell | DOGE-USD | 16.56 | -0.19 | stop-loss |
| 2026-10-12T21:05 | ROC + volume | sell | XRP-USD | 18.08 | -0.13 | exit signal |
| 2026-10-12T21:05 | ROC + volume | sell | SOL-USD | 18.08 | -0.13 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 21:53:05.000158+00:00 -> 2026-10-12 22:03:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
