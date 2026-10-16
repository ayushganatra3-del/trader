# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T04:25:05.000161+00:00 · 24367 ticks

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

Today: 3282 decisions in 657 calls, $0.0460 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T04:25 | 0 / 4 / 1 | SOL-USD 16%, MSTR 15% |  |
| Breezy | 2026-10-16T04:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T04:25 | 3 / 2 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.97 | 4.97 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.97 | 3.98 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.05 | 0.05 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.17 | 0.74 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.83 | -0.17 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.80 | -0.20 | 58 | 39.7 | -11.19 | -3.15 | -13.80 | 126 |
| 11 | Copy: Insider buying | copy | 99.34 | -0.66 | 20 | 45.0 | -16.49 | -2.61 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.66 | -1.34 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.82 | -2.18 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.75 | -2.25 | 0 | — | 29.72 | 3.40 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.60 | -2.40 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 97.03 | -2.97 | 36 | 16.7 | 6.62 | 0.93 | -22.11 | 111 |
| 19 | Trend pullback · 1h | trend | 96.66 | -3.34 | 86 | 24.4 | -22.71 | -6.39 | -23.79 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.08 | -3.92 | 106 | 32.1 | -14.05 | -4.56 | -15.69 | 295 |
| 22 | Daily: Momentum burst | daily | 95.63 | -4.37 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.33 | -4.67 | 75 | 20.0 | -11.53 | -2.10 | -15.34 | 259 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 93.94 | -6.05 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.92 | 1.07 | -9.46 | 101 |
| 26 | Parabolic SAR · 1h | trend | 93.59 | -6.41 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.33 | 2.32 | -6.73 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.24 | -6.76 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.21 | -6.79 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.16 | -6.84 | 51 | 15.7 | -1.00 | 0.08 | -24.95 | 132 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.23 | -5.30 | -10.77 | 247 |
| 32 | MACD cross · 1h | trend | 92.74 | -7.26 | 154 | 22.1 | -12.83 | -1.71 | -26.23 | 457 |
| 33 | Max aggression: 5-day momentum | meta | 92.08 | -7.92 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 34 | Bollinger breakout · 1h | breakout | 91.97 | -8.03 | 79 | 30.4 | 6.45 | 1.00 | -14.21 | 273 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.40 | -8.60 | 74 | 13.5 | -1.75 | 0.01 | -28.77 | 213 |
| 38 | Stochastic reversion · 1h | reversion | 91.20 | -8.80 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 39 | RSI momentum · 1h | momentum | 91.20 | -8.80 | 73 | 17.8 | -0.70 | 0.14 | -26.67 | 224 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.28 | 0.35 | -22.64 | 121 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.67 | -3.21 | -9.57 | 122 |
| 42 | Triple EMA stack · 1h | trend | 90.17 | -9.83 | 77 | 16.9 | -7.26 | -0.55 | -32.05 | 234 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.01 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.72 | -10.28 | 194 | 30.9 | -16.02 | -2.78 | -18.75 | 142 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.44 | -11.56 | 73 | 35.6 | -10.16 | -1.82 | -17.27 | 178 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.92 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.88 | -12.12 | 165 | 18.8 | -10.68 | -0.90 | -34.85 | 316 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.90 | -4.32 | -21.41 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.14 | -12.86 | 568 | 18.5 | -2.87 | -0.34 | -14.89 | 404 |
| 51 | MACD zero-line · 1h | trend | 86.77 | -13.23 | 74 | 16.2 | -22.16 | -4.28 | -22.72 | 228 |
| 52 | VWAP momentum · 1h | momentum | 86.24 | -13.76 | 360 | 21.9 | -34.62 | -4.99 | -43.06 | 1257 |
| 53 | Heikin-Ashi · 1h | trend | 86.14 | -13.86 | 175 | 25.7 | -30.27 | -4.85 | -39.47 | 670 |
| 54 | Donchian 20/10 · 1h | breakout | 85.68 | -14.32 | 72 | 19.4 | -0.36 | 0.16 | -20.96 | 219 |
| 55 | ROC + volume · 1h | momentum | 85.63 | -14.37 | 184 | 22.3 | -9.09 | -1.11 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.38 | -14.62 | 203 | 19.2 | -47.56 | -18.70 | -48.89 | 604 |
| 57 | Bollinger reversion · 1h | reversion | 84.98 | -15.02 | 132 | 31.8 | -26.70 | -5.71 | -31.47 | 339 |
| 58 | EMA 9/21 cross · 1h | trend | 84.48 | -15.53 | 120 | 12.5 | -5.70 | -0.45 | -29.27 | 321 |
| 59 | Williams %R · 1h | reversion | 83.99 | -16.01 | 168 | 42.9 | -31.28 | -5.08 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.39 | -16.61 | 61 | 23.0 | -13.53 | -2.53 | -18.95 | 177 |
| 61 | CCI reversion · 1h | reversion | 83.35 | -16.65 | 143 | 42.7 | -15.04 | -1.92 | -23.38 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 80.19 | -19.81 | 185 | 25.9 | -33.07 | -6.16 | -34.48 | 526 |
| 63 | RSI(14) reversion | reversion | 66.33 | -33.67 | 576 | 28.5 | -73.30 | -16.06 | -74.07 | 1559 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.79 | -16.57 | -76.65 | 1698 |
| 65 | Volume breakout | breakout | 64.60 | -35.40 | 318 | 13.5 | -63.35 | -17.61 | -63.35 | 883 |
| 66 | Squeeze breakout | breakout | 64.35 | -35.65 | 421 | 15.0 | -62.78 | -17.27 | -63.44 | 1214 |
| 67 | Donchian 55/20 | breakout | 62.94 | -37.06 | 421 | 18.3 | -68.85 | -14.05 | -71.15 | 1278 |
| 68 | EMA 20/50 cross | trend | 61.40 | -38.60 | 437 | 19.9 | -77.23 | -14.81 | -78.49 | 1447 |
| 69 | AI bee: Boozy | ai | 58.39 | -41.61 | 282 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.77 | -42.23 | 590 | 24.4 | -73.05 | -15.03 | -73.09 | 1439 |
| 71 | Keltner breakout | breakout | 56.21 | -43.80 | 591 | 16.4 | -83.48 | -25.42 | -83.63 | 1847 |
| 72 | Supertrend | trend | 53.62 | -46.38 | 617 | 20.3 | -86.46 | -19.83 | -86.46 | 1917 |
| 73 | Ichimoku | trend | 53.07 | -46.93 | 534 | 11.8 | -81.97 | -22.03 | -81.97 | 1726 |
| 74 | AI bee: Bizzy | ai | 50.74 | -49.26 | 1047 | 9.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.59 | -28.26 | -98.59 | 5279 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -28.18 | -93.42 | 2584 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.53 | -23.65 | -90.56 | 2361 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.57 | -25.81 | -91.57 | 2321 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.48 | -30.74 | -97.48 | 3524 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.57 | -33.22 | -96.57 | 3579 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.42 | -24.48 | -94.42 | 2633 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -33.62 | -99.39 | 5723 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.22 | -24.52 | -91.22 | 2638 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.25 | -29.91 | -96.25 | 3556 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.04 | -99.73 | 6160 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -28.00 | -91.77 | 2367 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -35.53 | -97.46 | 3653 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -33.98 | -98.48 | 4685 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.57 | -30.87 | -93.57 | 2795 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -36.24 | -99.54 | 6172 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.04 | -21.37 | -86.24 | 2107 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.52 | -25.72 | -87.67 | 2112 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -30.64 | -95.98 | 3762 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -31.54 | -89.38 | 2106 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -31.58 | -95.77 | 4074 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.51 | -99.89 | 8225 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T04:25 | Supertrend | buy | SOL-USD | 13.42 | — | entry signal |
| 2026-10-16T04:23 | AI bee: Bizzy | buy | SOL-USD | 8.39 | — | Jev: buy (buy p=0.66) |
| 2026-10-16T04:20 | MACD zero-line · 1h | buy | DOGE-USD | 4.33 | — | entry |
| 2026-10-16T04:20 | MACD zero-line · 1h | sell | SOL-USD | 4.33 | -0.05 | rebalance down |
| 2026-10-16T04:20 | VWAP reversion | sell | ETH-USD | 14.42 | -0.03 | exit signal |
| 2026-10-16T04:00 | MFI reversion · 1h | sell | XRP-USD | 11.51 | -0.01 | exit signal |
| 2026-10-16T04:00 | MFI reversion · 1h | sell | DOGE-USD | 9.02 | 0.17 | exit signal |
| 2026-10-16T04:00 | ROC + volume · 1h | sell | XRP-USD | 14.21 | -0.18 | exit signal |
| 2026-10-16T04:00 | ROC + volume · 1h | sell | SOL-USD | 14.26 | -0.04 | exit signal |
| 2026-10-16T04:00 | ROC + volume · 1h | sell | ETH-USD | 14.36 | 0.14 | exit signal |
| 2026-10-16T04:00 | ROC + volume · 1h | sell | BTC-USD | 14.27 | -0.17 | exit signal |
| 2026-10-16T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.92 | — | entry signal |
| 2026-10-16T03:55 | VWAP reversion | sell | SOL-USD | 14.44 | -0.01 | exit signal |
| 2026-10-16T03:55 | Supertrend | buy | BTC-USD | 13.43 | — | entry signal |
| 2026-10-16T03:46 | VWAP reversion | buy | SOL-USD | 14.45 | — | entry signal |
| 2026-10-16T03:46 | VWAP reversion | buy | ETH-USD | 14.45 | — | entry signal |
| 2026-10-16T03:46 | VWAP reversion | buy | BTC-USD | 14.45 | — | entry signal |
| 2026-10-16T03:46 | RSI(14) reversion | buy | BTC-USD | 16.58 | — | entry signal |
| 2026-10-16T03:40 | VWAP reversion | sell | BTC-USD | 14.35 | -0.15 | stop-loss |
| 2026-10-16T03:40 | Supertrend | sell | XRP-USD | 13.32 | -0.18 | exit signal |
| 2026-10-16T03:40 | Supertrend | sell | DOGE-USD | 13.45 | -0.11 | exit signal |
| 2026-10-16T03:35 | Volume breakout | sell | DOGE-USD | 16.00 | -0.20 | stop-loss |
| 2026-10-16T03:35 | Squeeze breakout | sell | DOGE-USD | 15.98 | -0.14 | stop-loss |
| 2026-10-16T03:35 | Keltner breakout | sell | DOGE-USD | 13.93 | -0.16 | stop-loss |
| 2026-10-16T03:35 | Donchian 55/20 | sell | DOGE-USD | 15.60 | -0.18 | stop-loss |
| 2026-10-16T03:25 | Three white soldiers | sell | XRP-USD | 21.21 | -0.18 | exit signal |
| 2026-10-16T03:23 | AI bee: Bizzy | sell | DOGE-USD | 7.48 | -0.02 | Jev: sell (sell p=0.53) after 13 min |
| 2026-10-16T03:20 | Volume breakout | buy | DOGE-USD | 16.20 | — | entry signal |
| 2026-10-16T03:15 | Three white soldiers | buy | XRP-USD | 21.39 | — | entry signal |
| 2026-10-16T03:15 | Keltner breakout | buy | DOGE-USD | 14.09 | — | entry signal |
| 2026-10-16T03:15 | Donchian 55/20 | buy | DOGE-USD | 15.78 | — | entry signal |
| 2026-10-16T03:10 | AI bee: Bizzy | buy | DOGE-USD | 7.50 | — | Jev: buy (buy p=0.59) |
| 2026-10-16T03:05 | VWAP momentum · 1h | sell | DOGE-USD | 3.90 | -0.02 | target is flat |
| 2026-10-16T03:05 | Ichimoku | sell | DOGE-USD | 13.21 | -0.08 | target is flat |
| 2026-10-16T03:00 | MFI reversion · 1h | sell | ETH-USD | 8.98 | 0.09 | exit signal |
| 2026-10-16T03:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.92 | — | entry signal |
| 2026-10-16T02:54 | AI bee: Boozy | sell | ETH-USD | 16.93 | -0.15 | Jev: sell |
| 2026-10-16T02:50 | Ichimoku | buy | DOGE-USD | 13.29 | — | entry signal |
| 2026-10-16T02:40 | RSI(14) reversion | sell | SOL-USD | 16.60 | -0.05 | exit signal |
| 2026-10-16T02:40 | Squeeze breakout | buy | DOGE-USD | 16.12 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 04:25:05.000161+00:00 -> 2026-10-16 04:35:05.000161+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
