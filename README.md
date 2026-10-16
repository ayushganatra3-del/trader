# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T10:25:05.000128+00:00 · 24669 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.85 (-7.14%)

Closed trades 76, win rate 39.5%, fees £2.65, max drawdown -7.57%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | GGR 12%, BORR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7792 decisions in 1559 calls, $0.1091 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T10:25 | 0 / 4 / 1 | MSTR 15% |  |
| Breezy | 2026-10-16T10:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T10:25 | 1 / 4 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.60 | 4.60 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.61 | 3.61 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 8 | VWAP reversion · 1h | reversion | 99.71 | -0.28 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 9 | Hold SPY | benchmark | 99.70 | -0.30 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.48 | -0.52 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 99.04 | -0.96 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.31 | -1.69 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.65 | -2.35 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Hold BTC | benchmark | 97.29 | -2.71 | 0 | — | 29.74 | 3.40 | -8.68 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.26 | -2.74 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.94 | -3.06 | 36 | 16.7 | 7.64 | 1.04 | -22.11 | 108 |
| 19 | Trend pullback · 1h | trend | 96.49 | -3.51 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.20 | -3.80 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.05 | -3.95 | 106 | 32.1 | -13.59 | -4.48 | -14.77 | 291 |
| 22 | Daily: Momentum burst | daily | 95.54 | -4.46 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.02 | -4.98 | 75 | 20.0 | -11.21 | -2.04 | -15.34 | 259 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.16 | 1.11 | -9.46 | 100 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 93.61 | -6.39 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 26 | Parabolic SAR · 1h | trend | 93.42 | -6.58 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.08 | -6.92 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 92.95 | -7.05 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.99 | -6.20 | -11.52 | 247 |
| 31 | EMA 20/50 cross · 1h | trend | 92.83 | -7.17 | 51 | 15.7 | -6.52 | -0.70 | -23.77 | 132 |
| 32 | MACD cross · 1h | trend | 92.48 | -7.52 | 155 | 21.9 | -12.21 | -1.61 | -26.23 | 455 |
| 33 | Bollinger breakout · 1h | breakout | 91.80 | -8.20 | 80 | 30.0 | 6.44 | 1.00 | -14.21 | 273 |
| 34 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 35 | Max aggression: 5-day momentum | meta | 91.75 | -8.25 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.13 | -8.87 | 74 | 13.5 | -1.73 | 0.01 | -28.77 | 214 |
| 38 | RSI momentum · 1h | momentum | 91.03 | -8.97 | 73 | 17.8 | 0.15 | 0.23 | -26.67 | 222 |
| 39 | Stochastic reversion · 1h | reversion | 90.88 | -9.12 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.18 | -3.01 | -9.08 | 123 |
| 42 | Triple EMA stack · 1h | trend | 89.88 | -10.12 | 77 | 16.9 | -7.70 | -0.60 | -32.08 | 235 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.60 | -10.40 | 195 | 31.3 | -16.46 | -2.82 | -19.82 | 140 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.14 | -11.86 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.57 | -12.43 | 165 | 18.8 | -10.86 | -0.92 | -34.78 | 317 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 86.88 | -13.12 | 568 | 18.5 | -1.88 | -0.15 | -14.62 | 402 |
| 51 | MACD zero-line · 1h | trend | 86.45 | -13.55 | 75 | 16.0 | -21.66 | -4.17 | -22.72 | 226 |
| 52 | VWAP momentum · 1h | momentum | 85.97 | -14.03 | 361 | 21.9 | -34.15 | -4.90 | -43.06 | 1257 |
| 53 | Heikin-Ashi · 1h | trend | 85.77 | -14.23 | 175 | 25.7 | -29.89 | -4.78 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 85.53 | -14.47 | 184 | 22.3 | -9.10 | -1.11 | -25.32 | 398 |
| 55 | Donchian 20/10 · 1h | breakout | 85.40 | -14.61 | 72 | 19.4 | -0.33 | 0.16 | -20.97 | 220 |
| 56 | Three white soldiers | momentum | 85.20 | -14.80 | 204 | 19.1 | -47.78 | -19.37 | -48.69 | 609 |
| 57 | Bollinger reversion · 1h | reversion | 84.68 | -15.32 | 132 | 31.8 | -26.66 | -5.70 | -31.47 | 338 |
| 58 | EMA 9/21 cross · 1h | trend | 84.27 | -15.73 | 120 | 12.5 | -5.54 | -0.43 | -29.27 | 322 |
| 59 | Williams %R · 1h | reversion | 83.69 | -16.31 | 168 | 42.9 | -31.21 | -5.06 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.10 | -16.90 | 62 | 24.2 | -12.66 | -2.36 | -18.95 | 175 |
| 61 | CCI reversion · 1h | reversion | 83.07 | -16.93 | 143 | 42.7 | -15.10 | -1.93 | -23.38 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 79.95 | -20.05 | 186 | 26.3 | -32.37 | -6.03 | -33.79 | 523 |
| 63 | RSI(14) reversion | reversion | 66.16 | -33.84 | 577 | 28.4 | -73.41 | -16.13 | -74.11 | 1562 |
| 64 | ROC + volume | momentum | 65.30 | -34.70 | 532 | 22.4 | -75.08 | -16.79 | -76.71 | 1705 |
| 65 | Volume breakout | breakout | 64.41 | -35.59 | 319 | 13.5 | -63.46 | -17.70 | -63.46 | 884 |
| 66 | Squeeze breakout | breakout | 63.76 | -36.24 | 425 | 14.8 | -63.03 | -17.45 | -63.72 | 1217 |
| 67 | Donchian 55/20 | breakout | 61.65 | -38.35 | 428 | 18.0 | -69.29 | -14.25 | -71.42 | 1282 |
| 68 | EMA 20/50 cross | trend | 60.62 | -39.38 | 442 | 19.7 | -77.30 | -14.88 | -78.70 | 1447 |
| 69 | AI bee: Boozy | ai | 58.02 | -41.98 | 285 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.73 | -42.27 | 591 | 24.4 | -72.61 | -14.83 | -72.65 | 1430 |
| 71 | Keltner breakout | breakout | 55.35 | -44.65 | 598 | 16.2 | -83.68 | -25.82 | -83.68 | 1852 |
| 72 | Supertrend | trend | 53.17 | -46.83 | 622 | 20.1 | -86.35 | -19.81 | -86.51 | 1911 |
| 73 | Ichimoku | trend | 52.44 | -47.56 | 541 | 11.8 | -82.02 | -22.14 | -82.02 | 1728 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.53 | -98.64 | 5296 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -28.63 | -93.52 | 2592 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.62 | -23.86 | -90.62 | 2365 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.74 | -26.04 | -91.74 | 2335 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -30.73 | -97.46 | 3521 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.71 | -34.17 | -96.71 | 3605 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -24.75 | -94.44 | 2633 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -33.54 | -99.38 | 5710 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.37 | -24.89 | -91.37 | 2646 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.28 | -29.96 | -96.28 | 3560 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.11 | -99.73 | 6156 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -28.08 | -91.77 | 2366 |
| 86 | AI bee: Bizzy | ai | 50.13 | -49.87 | 1062 | 8.9 | — | — | — | — |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -35.79 | -97.48 | 3656 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -33.91 | -98.45 | 4681 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.71 | -31.35 | -93.71 | 2804 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -36.35 | -99.53 | 6167 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.96 | -21.29 | -86.12 | 2104 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.54 | -25.66 | -87.64 | 2110 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -30.52 | -95.93 | 3760 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -31.75 | -89.29 | 2102 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -31.65 | -95.71 | 4072 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.74 | -99.89 | 8227 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T10:20 | RSI(14) reversion | buy | SOL-USD | 16.55 | — | entry signal |
| 2026-10-16T10:15 | VWAP reversion | buy | BTC-USD | 14.44 | — | entry signal |
| 2026-10-16T10:15 | RSI(14) reversion | buy | XRP-USD | 16.57 | — | entry signal |
| 2026-10-16T10:15 | RSI(14) reversion | buy | BTC-USD | 16.57 | — | entry signal |
| 2026-10-16T10:10 | Supertrend | sell | DOGE-USD | 10.63 | -0.08 | exit signal |
| 2026-10-16T10:10 | EMA 20/50 cross | sell | XRP-USD | 15.10 | -0.20 | stop-loss |
| 2026-10-16T10:05 | Donchian 55/20 | sell | SOL-USD | 15.28 | -0.23 | stop-loss |
| 2026-10-16T10:05 | Donchian 55/20 | sell | ETH-USD | 15.38 | -0.20 | stop-loss |
| 2026-10-16T10:05 | Ichimoku | sell | DOGE-USD | 13.03 | -0.14 | exit signal |
| 2026-10-16T10:05 | Supertrend | sell | XRP-USD | 13.29 | -0.14 | exit signal |
| 2026-10-16T10:05 | Supertrend | sell | SOL-USD | 10.65 | -0.06 | exit signal |
| 2026-10-16T10:05 | Supertrend | sell | ETH-USD | 13.31 | -0.09 | exit signal |
| 2026-10-16T10:00 | Candlestick reversal · 1h | sell | ETH-USD | 2.79 | 0.03 | exit signal |
| 2026-10-16T10:00 | Bollinger breakout · 1h | sell | BTC-USD | 22.72 | -0.38 | exit signal |
| 2026-10-16T10:00 | VWAP momentum · 1h | sell | BTC-USD | 3.28 | -0.03 | exit signal |
| 2026-10-16T10:00 | MACD zero-line · 1h | buy | XRP-USD | 4.15 | — | entry |
| 2026-10-16T10:00 | MACD zero-line · 1h | buy | DOGE-USD | 17.33 | — | rebalance up |
| 2026-10-16T10:00 | MACD zero-line · 1h | sell | BTC-USD | 21.48 | -0.32 | exit signal |
| 2026-10-16T10:00 | MACD cross · 1h | sell | BTC-USD | 7.62 | -0.07 | exit signal |
| 2026-10-16T10:00 | Triple EMA stack · 1h | buy | SOL-USD | 22.50 | — | entry signal |
| 2026-10-16T10:00 | Supertrend | buy | XRP-USD | 5.31 | — | rebalance up |
| 2026-10-16T10:00 | Supertrend | buy | ETH-USD | 2.69 | — | rebalance up |
| 2026-10-16T10:00 | Supertrend | sell | BTC-USD | 13.28 | -0.15 | exit signal |
| 2026-10-16T09:55 | EMA 20/50 cross | sell | BTC-USD | 15.10 | -0.14 | exit signal |
| 2026-10-16T09:40 | AI bee: Bizzy | sell | DOGE-USD | 7.08 | -0.03 | Jev: sell (sell p=0.67) after 10 min |
| 2026-10-16T09:35 | Squeeze breakout | sell | SOL-USD | 15.83 | -0.15 | exit signal |
| 2026-10-16T09:30 | AI bee: Bizzy | buy | DOGE-USD | 7.11 | — | Jev: buy (buy p=0.57) |
| 2026-10-16T09:11 | AI bee: Bizzy | sell | SOL-USD | 6.90 | -0.05 | Jev: sell (sell p=0.83) after 11 min |
| 2026-10-16T09:10 | Ichimoku | sell | XRP-USD | 13.08 | -0.11 | exit signal |
| 2026-10-16T09:10 | Ichimoku | sell | ETH-USD | 13.18 | -0.07 | exit signal |
| 2026-10-16T09:05 | Ichimoku | buy | DOGE-USD | 13.17 | — | entry signal |
| 2026-10-16T09:00 | AI bee: Bizzy | buy | SOL-USD | 6.94 | — | Jev: buy (buy p=0.55) |
| 2026-10-16T09:00 | MFI reversion · 1h | sell | SOL-USD | 9.01 | 0.32 | exit signal |
| 2026-10-16T09:00 | Heikin-Ashi · 1h | buy | SOL-USD | 6.61 | — | entry signal |
| 2026-10-16T09:00 | Heikin-Ashi · 1h | buy | ETH-USD | 6.61 | — | entry signal |
| 2026-10-16T08:50 | Squeeze breakout | buy | SOL-USD | 15.98 | — | entry signal |
| 2026-10-16T08:48 | AI bee: Bizzy | sell | DOGE-USD | 7.02 | -0.04 | Jev: sell (sell p=0.62) after 10 min |
| 2026-10-16T08:40 | Donchian 55/20 | buy | SOL-USD | 15.51 | — | entry signal |
| 2026-10-16T08:40 | Ichimoku | buy | XRP-USD | 13.19 | — | entry signal |
| 2026-10-16T08:38 | AI bee: Bizzy | buy | DOGE-USD | 7.05 | — | Jev: buy (buy p=0.56) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 10:25:05.000128+00:00 -> 2026-10-16 10:35:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
