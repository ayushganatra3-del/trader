# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-29T17:15:05.000148+00:00 · 40456 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.42 (-8.58%)

Closed trades 119, win rate 39.5%, fees £3.55, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, RENT 12%, CTY 12%, ACN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-28)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 23.78 · VIX 16.91 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, MSFT 5.4, PLTR 5.0, AAPL 4.2, LABU 3.9, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 25908 decisions in 2601 calls, $0.3268 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-29T17:15 | 1 / 5 / 24 | cash |  |
| Breezy | 2026-10-29T17:15 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-29T17:15 | 4 / 21 / 5 | COIN 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.83 | +8.30% | 12 |
| VWAP momentum · 1h | LABU | 2.51 | +26.96% | 3 |
| VWAP reversion | SQQQ | 2.50 | +4.75% | 5 |
| MACD zero-line | MSFT | 2.39 | +0.71% | 6 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.05 | 7.05 | 0 | — | 7.80 | 3.77 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.05 | 1.97 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.39 | 1.40 | 0 | — | 4.58 | 1.97 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 101.12 | 1.12 | 93 | 46.2 | -11.31 | -3.11 | -12.63 | 141 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.89 | -1.11 | 0 | — | -0.21 | -0.07 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 7.05 | 3.33 | -1.98 | 90 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -4.59 | -5.34 | -4.72 | 21 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.15 | -2.85 | 0 | — | -0.42 | -0.12 | -5.99 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.10 | -2.90 | 0 | — | -4.83 | -1.91 | -7.83 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.72 | -2.50 | -5.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Hold BTC | benchmark | 95.69 | -4.31 | 0 | — | 3.81 | 0.80 | -9.28 | 1 |
| 17 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -2.37 | -1.58 | -7.46 | 175 |
| 18 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.33 | -4.76 | 27 |
| 19 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 5.00 | 1.64 | -8.76 | 204 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 93.97 | -6.03 | 0 | — | 2.29 | 0.55 | -14.57 | 1 |
| 21 | Copy: Insider buying | copy | 93.20 | -6.80 | 32 | 37.5 | -19.78 | -3.88 | -24.43 | 67 |
| 22 | Donchian 55/20 · 1h | breakout | 92.38 | -7.62 | 53 | 15.1 | -13.80 | -3.10 | -15.47 | 102 |
| 23 | Opening range 30m | breakout | 92.35 | -7.65 | 296 | 36.1 | -10.04 | -2.98 | -17.21 | 581 |
| 24 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -20.96 | -7.22 | -21.10 | 102 |
| 25 | Daily: Momentum burst | daily | 91.64 | -8.36 | 15 | 13.3 | -13.65 | -2.56 | -17.57 | 35 |
| 26 | Agent | meta | 91.42 | -8.58 | 119 | 39.5 | -8.77 | -5.19 | -12.20 | 209 |
| 27 | Parabolic SAR · 1h | trend | 91.25 | -8.75 | 132 | 28.8 | -18.62 | -4.42 | -19.69 | 248 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.67 | -2.65 | -16.91 | 1 |
| 29 | Squeeze breakout · 1h | breakout | 90.71 | -9.29 | 56 | 23.2 | -5.28 | -1.43 | -12.65 | 94 |
| 30 | Daily: Bullish score | daily | 89.94 | -10.06 | 12 | 25.0 | -7.03 | -0.89 | -14.40 | 14 |
| 31 | ADX DI cross · 1h | trend | 89.40 | -10.60 | 132 | 18.2 | -16.60 | -3.29 | -17.16 | 264 |
| 32 | Stochastic reversion · 1h | reversion | 87.79 | -12.21 | 217 | 47.9 | -16.86 | -3.14 | -22.29 | 380 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 87.67 | -12.33 | 14 | 42.9 | -15.38 | -1.34 | -27.23 | 25 |
| 34 | Volume breakout · 1h | breakout | 87.13 | -12.87 | 123 | 30.1 | -14.13 | -3.01 | -16.69 | 107 |
| 35 | Agent (aggressive) | meta | 86.92 | -13.08 | 60 | 35.0 | -9.13 | -2.89 | -14.77 | 98 |
| 36 | Z-score reversion · 1h | reversion | 86.68 | -13.32 | 125 | 36.0 | -11.96 | -1.83 | -21.48 | 205 |
| 37 | Bollinger breakout · 1h | breakout | 86.26 | -13.74 | 126 | 26.2 | -13.48 | -2.44 | -18.58 | 249 |
| 38 | Keltner breakout · 1h | breakout | 85.80 | -14.20 | 80 | 25.0 | -20.57 | -3.97 | -23.14 | 190 |
| 39 | Opening range 15m | breakout | 84.94 | -15.06 | 367 | 32.2 | -14.84 | -4.24 | -17.87 | 710 |
| 40 | Supertrend · 1h | trend | 84.60 | -15.40 | 120 | 13.3 | -22.14 | -4.40 | -25.12 | 231 |
| 41 | Ichimoku · 1h | trend | 84.57 | -15.43 | 71 | 11.3 | -18.71 | -3.75 | -24.73 | 118 |
| 42 | Connors RSI(2) · 1h | reversion | 83.71 | -16.29 | 185 | 40.5 | -21.34 | -6.82 | -21.67 | 163 |
| 43 | RSI momentum · 1h | momentum | 83.62 | -16.38 | 117 | 13.7 | -20.92 | -4.12 | -23.89 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.84 | -17.16 | 110 | 14.5 | -27.92 | -5.41 | -30.81 | 209 |
| 45 | MACD cross · 1h | trend | 82.72 | -17.28 | 268 | 24.6 | -27.62 | -5.04 | -28.79 | 477 |
| 46 | CCI reversion · 1h | reversion | 82.56 | -17.44 | 242 | 46.7 | -18.93 | -2.46 | -28.07 | 448 |
| 47 | EMA 20/50 cross · 1h | trend | 82.54 | -17.46 | 83 | 12.0 | -21.02 | -3.82 | -24.08 | 136 |
| 48 | MFI reversion · 1h | reversion | 82.24 | -17.76 | 286 | 32.2 | -15.00 | -2.31 | -19.60 | 152 |
| 49 | Williams %R · 1h | reversion | 81.47 | -18.54 | 248 | 47.6 | -33.11 | -5.89 | -34.90 | 528 |
| 50 | Bollinger reversion · 1h | reversion | 80.72 | -19.28 | 191 | 38.7 | -27.66 | -5.46 | -29.74 | 360 |
| 51 | Donchian 20/10 · 1h | breakout | 80.57 | -19.43 | 108 | 21.3 | -23.58 | -4.36 | -26.02 | 221 |
| 52 | RSI(14) reversion · 1h | reversion | 80.12 | -19.88 | 109 | 27.5 | -11.75 | -1.97 | -24.48 | 201 |
| 53 | OBV trend · 1h | momentum | 80.08 | -19.92 | 221 | 17.2 | -36.53 | -7.28 | -37.07 | 308 |
| 54 | MACD zero-line · 1h | trend | 79.91 | -20.09 | 122 | 14.8 | -21.89 | -4.40 | -24.62 | 214 |
| 55 | Agent (ML meta-label) | meta | 78.40 | -21.60 | 1070 | 20.9 | -12.15 | -2.31 | -17.53 | 356 |
| 56 | Heikin-Ashi · 1h | trend | 77.91 | -22.09 | 318 | 24.2 | -42.05 | -9.18 | -42.93 | 672 |
| 57 | ROC + volume · 1h | momentum | 77.54 | -22.46 | 276 | 26.4 | -29.95 | -5.54 | -31.11 | 392 |
| 58 | Candlestick reversal · 1h | reversion | 76.64 | -23.36 | 303 | 30.0 | -33.18 | -6.32 | -34.12 | 551 |
| 59 | VWAP momentum · 1h | momentum | 75.81 | -24.19 | 619 | 23.3 | -49.61 | -10.63 | -50.30 | 1234 |
| 60 | EMA 9/21 cross · 1h | trend | 74.93 | -25.07 | 189 | 10.6 | -32.49 | -6.56 | -33.33 | 343 |
| 61 | Three white soldiers | momentum | 74.65 | -25.35 | 353 | 17.6 | -44.97 | -21.01 | -44.98 | 610 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 72.15 | -27.85 | 21 | 33.3 | -36.04 | -2.17 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -44.67 | -98.92 | 5244 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.88 | -23.52 | -78.88 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.64 | -44.31 | -93.64 | 2547 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.83 | -30.77 | -88.83 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.39 | -38.31 | -91.39 | 2361 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.67 | -32.12 | -90.67 | 2267 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -52.52 | -97.78 | 3534 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -57.16 | -96.18 | 3394 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.22 | -35.76 | -94.22 | 2487 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.38 | -34.04 | -82.41 | 1704 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -53.73 | -99.41 | 5734 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -43.14 | -92.95 | 2640 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.56 | -37.27 | -95.57 | 3481 |
| 76 | ROC + volume | momentum | 50.19 | -49.81 | 878 | 21.8 | -74.60 | -27.36 | -74.63 | 1562 |
| 77 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.67 | -99.78 | 6178 |
| 78 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.15 | -45.30 | -92.19 | 2321 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -61.51 | -97.77 | 3604 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.59 | -59.24 | -98.59 | 4785 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.70 | -29.65 | -69.73 | 1217 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.82 | -55.51 | -94.83 | 2805 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.88 | -38.59 | -84.88 | 1832 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -67.84 | -99.58 | 6290 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.40 | -28.73 | -87.45 | 2187 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.07 | -19.28 | -76.32 | 1660 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.18 | -37.00 | -90.21 | 2232 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.07 | -50.42 | -96.09 | 3764 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.61 | -51.15 | -89.61 | 2126 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.51 | -25.88 | -64.51 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.50 | -25.34 | -73.50 | 1283 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.56 | -18.39 | -75.68 | 1574 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.56 | -51.32 | -96.59 | 4191 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.08 | -99.92 | 8292 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-29T17:15 | Opening range 30m | sell | UPRO | 9.23 | -0.10 | exit signal |
| 2026-10-29T17:15 | Opening range 30m | sell | SPY | 9.27 | -0.06 | exit signal |
| 2026-10-29T17:15 | Opening range 30m | sell | AMD | 6.46 | -0.11 | stop-loss |
| 2026-10-29T17:15 | Opening range 15m | sell | SPY | 1.49 | -0.01 | exit signal |
| 2026-10-29T17:10 | Three white soldiers · 1h | sell | BTC-USD | 23.48 | -0.39 | stop-loss |
| 2026-10-29T17:05 | Heikin-Ashi · 1h | sell | LABU | 3.91 | 0.10 | rebalance down |
| 2026-10-29T17:00 | Candlestick reversal · 1h | sell | XRP-USD | 19.09 | -0.11 | exit signal |
| 2026-10-29T17:00 | OBV trend · 1h | buy | BTC-USD | 8.93 | — | entry signal |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | buy | TSLA | 3.20 | — | entry |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | buy | SOL-USD | 7.11 | — | entry |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | buy | ETH-USD | 7.11 | — | entry signal |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | buy | BTC-USD | 7.11 | — | entry |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | sell | TNA | 3.99 | -0.03 | rebalance down |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | sell | SQQQ | 4.10 | -0.00 | rebalance down |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | sell | META | 4.18 | 0.03 | rebalance down |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | sell | IWM | 4.05 | -0.02 | rebalance down |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 4.11 | 0.01 | rebalance down |
| 2026-10-29T17:00 | Heikin-Ashi · 1h | sell | AAPL | 4.10 | 0.00 | rebalance down |
| 2026-10-29T17:00 | MACD zero-line · 1h | buy | SOL-USD | 10.05 | — | entry signal |
| 2026-10-29T17:00 | MACD zero-line · 1h | buy | ETH-USD | 10.05 | — | entry signal |
| 2026-10-29T17:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 8.28 | — | entry signal |
| 2026-10-29T16:51 | Agent (rotation) | sell | TNA | 8.02 | -0.02 | selected signal exited |
| 2026-10-29T16:51 | MFI reversion · 1h | buy | GOOGL | 20.58 | — | entry |
| 2026-10-29T16:51 | MFI reversion · 1h | sell | NVDA | 20.41 | -0.11 | target is flat |
| 2026-10-29T16:51 | Gap and go | sell | TNA | 23.74 | -0.05 | target is flat |
| 2026-10-29T16:46 | Agent (ML meta-label) | buy | IWM | 9.74 | — | entry |
| 2026-10-29T16:46 | Agent (ML meta-label) | sell | MSFT | 8.73 | -0.01 | selected signal exited |
| 2026-10-29T16:46 | Agent (ML meta-label) | sell | META | 1.01 | -0.00 | selected signal exited |
| 2026-10-29T16:45 | Agent (ML meta-label) | buy | META | 1.01 | — | entry |
| 2026-10-29T16:40 | Agent (ML meta-label) | buy | SQQQ | 8.84 | — | rebalance up |
| 2026-10-29T16:40 | Agent (ML meta-label) | sell | IWM | 9.85 | -0.02 | selected signal exited |
| 2026-10-29T16:35 | Agent (ML meta-label) | buy | SQQQ | 1.00 | — | following VWAP reversion |
| 2026-10-29T16:35 | Agent (ML meta-label) | buy | MSFT | 8.73 | — | following MACD zero-line |
| 2026-10-29T16:35 | Agent (ML meta-label) | sell | SOL-USD | 9.74 | -0.09 | selected signal exited |
| 2026-10-29T16:35 | ROC + volume | buy | META | 12.57 | — | entry signal |
| 2026-10-29T16:35 | ROC + volume | sell | SOL-USD | 12.51 | -0.10 | stop-loss |
| 2026-10-29T16:30 | Agent (ML meta-label) | buy | SOL-USD | 9.82 | — | entry |
| 2026-10-29T16:30 | Agent (ML meta-label) | buy | IWM | 9.87 | — | entry |
| 2026-10-29T16:30 | Agent (ML meta-label) | buy | ETHU | 9.87 | — | entry |
| 2026-10-29T16:30 | Agent (ML meta-label) | sell | XRP-USD | 5.89 | -0.05 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-31 17:15:05.000148+00:00 -> 2026-10-29 17:25:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
