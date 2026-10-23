# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T02:15:05.000126+00:00 · 32537 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 98, win rate 39.8%, fees £3.14, max drawdown -10.53%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1890 decisions in 378 calls, $0.0264 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T02:15 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-23T02:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T02:15 | 2 / 3 / 0 | ETH-USD 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.17 | 7.17 | 0 | — | 8.93 | 4.33 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.95 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.32 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.78 | 0.78 | 0 | — | 4.24 | 1.82 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.32 | 0.32 | 82 | 43.9 | -10.26 | -2.74 | -13.79 | 142 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.30 | -0.70 | 10 | 50.0 | -16.15 | -1.26 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.04 | -4.06 | 22 |
| 12 | Hold SPY | benchmark | 98.15 | -1.85 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -1.99 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.54 | -3.46 | 118 | 31.4 | -3.72 | -1.62 | -7.58 | 234 |
| 15 | Hold BTC | benchmark | 95.99 | -4.01 | 0 | — | 3.14 | 0.64 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.75 | -4.25 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.02 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.40 | -4.60 | 0 | — | -4.72 | -1.75 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.15 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.23 | -5.77 | 25 | 40.0 | -13.46 | -2.31 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.75 | -6.25 | 95 | 23.2 | -22.28 | -6.89 | -22.80 | 120 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.73 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.04 | -6.96 | 48 | 16.7 | -18.51 | -3.75 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.92 | -7.08 | 115 | 26.1 | -16.86 | -3.72 | -20.59 | 263 |
| 26 | Daily: Momentum burst | daily | 92.53 | -7.47 | 8 | 12.5 | -16.39 | -2.90 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.45 | -7.55 | 103 | 19.4 | -10.31 | -1.99 | -12.90 | 252 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.76 | -11.76 | 95 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.13 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -12.23 | -5.11 | -12.77 | 247 |
| 31 | Daily: Bullish score | daily | 89.69 | -10.31 | 8 | 0.0 | -7.26 | -0.84 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.43 | -10.57 | 104 | 27.9 | -11.51 | -2.04 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.12 | -10.88 | 101 | 22.8 | -13.00 | -2.33 | -14.76 | 108 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.91 | -11.09 | 0 | — | -3.71 | -0.42 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -18.96 | -4.61 | -19.81 | 131 |
| 36 | EMA 20/50 cross · 1h | trend | 87.52 | -12.48 | 68 | 11.8 | -23.93 | -4.32 | -26.40 | 145 |
| 37 | Stochastic reversion · 1h | reversion | 87.17 | -12.83 | 179 | 45.3 | -16.32 | -2.68 | -22.24 | 388 |
| 38 | Supertrend · 1h | trend | 86.92 | -13.08 | 104 | 15.4 | -24.19 | -4.71 | -27.40 | 217 |
| 39 | RSI momentum · 1h | momentum | 86.64 | -13.36 | 96 | 16.7 | -20.68 | -3.90 | -22.88 | 213 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.26 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.21 | -13.79 | 73 | 23.3 | -23.38 | -4.52 | -24.29 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.05 | -14.95 | 168 | 39.9 | -26.16 | -7.09 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 84.69 | -15.31 | 216 | 23.1 | -27.59 | -5.06 | -29.35 | 468 |
| 44 | Triple EMA stack · 1h | trend | 84.34 | -15.66 | 96 | 15.6 | -27.10 | -5.02 | -29.22 | 214 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.72 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 83.07 | -16.93 | 104 | 33.7 | -14.01 | -2.04 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.66 | -17.34 | 93 | 20.4 | -24.80 | -4.47 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.24 | -17.76 | 198 | 17.7 | -29.52 | -5.53 | -31.71 | 299 |
| 49 | MACD zero-line · 1h | trend | 82.21 | -17.79 | 103 | 15.5 | -24.12 | -4.65 | -25.07 | 226 |
| 50 | Williams %R · 1h | reversion | 81.95 | -18.05 | 204 | 44.1 | -33.55 | -5.32 | -37.94 | 529 |
| 51 | MFI reversion · 1h | reversion | 81.95 | -18.05 | 245 | 31.4 | -18.76 | -2.86 | -21.11 | 147 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -45.39 | -18.14 | -45.39 | 600 |
| 53 | CCI reversion · 1h | reversion | 80.64 | -19.36 | 193 | 43.0 | -23.85 | -3.21 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.22 | -19.78 | 827 | 19.0 | -14.50 | -2.69 | -17.26 | 376 |
| 55 | Bollinger reversion · 1h | reversion | 80.06 | -19.94 | 168 | 35.1 | -31.11 | -5.96 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 79.97 | -20.03 | 260 | 23.5 | -43.26 | -9.25 | -44.09 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.70 | -20.30 | 233 | 24.0 | -28.37 | -5.09 | -28.88 | 381 |
| 58 | EMA 9/21 cross · 1h | trend | 78.16 | -21.84 | 155 | 11.6 | -33.67 | -6.34 | -34.19 | 333 |
| 59 | RSI(14) reversion · 1h | reversion | 77.71 | -22.29 | 90 | 23.3 | -22.95 | -4.13 | -24.19 | 195 |
| 60 | Candlestick reversal · 1h | reversion | 77.22 | -22.78 | 245 | 29.0 | -39.25 | -6.94 | -40.85 | 570 |
| 61 | VWAP momentum · 1h | momentum | 76.95 | -23.05 | 499 | 21.4 | -50.25 | -10.25 | -51.02 | 1237 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.83 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.79 | -41.21 | 693 | 23.1 | -79.36 | -22.17 | -79.58 | 1685 |
| 64 | Volume breakout | breakout | 57.99 | -42.01 | 410 | 13.4 | -65.42 | -20.87 | -65.51 | 854 |
| 65 | Donchian 55/20 | breakout | 55.45 | -44.55 | 546 | 19.8 | -72.79 | -20.47 | -72.80 | 1268 |
| 66 | Squeeze breakout | breakout | 54.49 | -45.51 | 539 | 14.3 | -68.57 | -24.37 | -68.57 | 1202 |
| 67 | EMA 20/50 cross | trend | 53.77 | -46.23 | 591 | 20.5 | -80.08 | -20.95 | -80.21 | 1446 |
| 68 | RSI(14) reversion | reversion | 53.11 | -46.89 | 808 | 26.0 | -76.99 | -17.23 | -77.07 | 1680 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -73.37 | -14.37 | -73.87 | 1522 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -32.89 | -98.91 | 5250 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.01 | -34.30 | -94.05 | 2554 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.65 | -24.69 | -88.68 | 1887 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.64 | -29.49 | -91.65 | 2339 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.76 | -24.77 | -90.88 | 2204 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -35.66 | -97.86 | 3498 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.94 | -37.73 | -96.96 | 3548 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -28.19 | -94.38 | 2541 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.26 | -28.33 | -83.26 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -36.01 | -99.49 | 5874 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.18 | -30.57 | -93.29 | 2624 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -30.19 | -95.67 | 3417 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -42.77 | -99.79 | 6197 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.31 | -32.00 | -92.35 | 2332 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -39.15 | -97.67 | 3573 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -37.57 | -98.66 | 4770 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.78 | -37.92 | -94.86 | 2792 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -29.37 | -84.72 | 1783 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -39.40 | -99.60 | 6228 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.02 | -23.39 | -88.13 | 2197 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.73 | -26.73 | -88.75 | 2175 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -33.60 | -96.30 | 3803 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.89 | -34.01 | -89.89 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -33.87 | -96.22 | 4133 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.89 | -99.91 | 8246 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T02:05 | Donchian 55/20 | sell | XRP-USD | 13.77 | -0.16 | stop-loss |
| 2026-10-23T02:05 | Donchian 55/20 | sell | SOL-USD | 13.83 | -0.15 | stop-loss |
| 2026-10-23T02:05 | EMA 20/50 cross | sell | BTC-USD | 8.04 | -0.07 | stop-loss |
| 2026-10-23T02:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.11 | -0.04 | exit signal |
| 2026-10-23T02:00 | MACD cross · 1h | buy | SOL-USD | 9.65 | — | entry |
| 2026-10-23T02:00 | MACD cross · 1h | sell | DOGE-USD | 4.88 | -0.00 | rebalance down |
| 2026-10-23T02:00 | MACD cross · 1h | sell | BTC-USD | 4.77 | -0.03 | rebalance down |
| 2026-10-23T02:00 | Volume breakout | sell | XRP-USD | 14.45 | -0.15 | exit signal |
| 2026-10-23T02:00 | Volume breakout | sell | ETH-USD | 14.48 | -0.12 | exit signal |
| 2026-10-23T02:00 | Volume breakout | sell | DOGE-USD | 14.45 | -0.15 | exit signal |
| 2026-10-23T02:00 | Donchian 55/20 | sell | BTC-USD | 13.86 | -0.13 | stop-loss |
| 2026-10-23T01:50 | Volume breakout | buy | XRP-USD | 14.60 | — | entry signal |
| 2026-10-23T01:50 | Volume breakout | buy | DOGE-USD | 14.60 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | XRP-USD | 13.93 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | SOL-USD | 13.99 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | BTC-USD | 13.99 | — | entry signal |
| 2026-10-23T01:45 | Volume breakout | buy | ETH-USD | 14.60 | — | entry signal |
| 2026-10-23T01:40 | Squeeze breakout | sell | DOGE-USD | 13.61 | -0.11 | target is flat |
| 2026-10-23T01:40 | Squeeze breakout | sell | BTC-USD | 13.62 | -0.11 | stop-loss |
| 2026-10-23T01:30 | EMA 20/50 cross | buy | BTC-USD | 2.68 | — | rebalance up |
| 2026-10-23T01:30 | EMA 20/50 cross | sell | SOL-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-23T01:25 | EMA 20/50 cross | buy | BTC-USD | 2.68 | — | rebalance up |
| 2026-10-23T01:25 | EMA 20/50 cross | sell | XRP-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-23T01:20 | Squeeze breakout | sell | ETH-USD | 13.63 | -0.10 | stop-loss |
| 2026-10-23T01:10 | Volume breakout | sell | XRP-USD | 14.50 | -0.14 | stop-loss |
| 2026-10-23T01:10 | Squeeze breakout | sell | XRP-USD | 13.59 | -0.13 | stop-loss |
| 2026-10-23T01:10 | Donchian 55/20 | sell | XRP-USD | 13.88 | -0.13 | stop-loss |
| 2026-10-23T01:05 | EMA 20/50 cross | buy | BTC-USD | 2.74 | — | entry signal |
| 2026-10-23T01:05 | EMA 20/50 cross | sell | DOGE-USD | 2.71 | -0.01 | rebalance down |
| 2026-10-23T01:00 | VWAP reversion · 1h | sell | SOL-USD | 14.40 | -0.12 | exit signal |
| 2026-10-23T01:00 | VWAP reversion · 1h | sell | ETH-USD | 14.38 | -0.02 | exit signal |
| 2026-10-23T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 14.39 | -0.08 | exit signal |
| 2026-10-23T01:00 | VWAP reversion · 1h | sell | BTC-USD | 14.36 | -0.07 | exit signal |
| 2026-10-23T01:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.15 | — | entry signal |
| 2026-10-23T00:50 | Volume breakout | buy | XRP-USD | 14.64 | — | entry signal |
| 2026-10-23T00:50 | Squeeze breakout | buy | XRP-USD | 13.72 | — | entry signal |
| 2026-10-23T00:50 | Squeeze breakout | buy | DOGE-USD | 13.72 | — | entry signal |
| 2026-10-23T00:50 | Donchian 55/20 | buy | XRP-USD | 14.01 | — | entry signal |
| 2026-10-23T00:50 | Donchian 55/20 | buy | DOGE-USD | 14.01 | — | entry signal |
| 2026-10-23T00:45 | RSI(14) reversion | sell | BTC-USD | 13.25 | -0.04 | take-profit |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 02:15:05.000126+00:00 -> 2026-10-23 02:25:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
