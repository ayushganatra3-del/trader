# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-31T14:25:05.000142+00:00 · 42625 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.52 (-8.48%)

Closed trades 130, win rate 40.8%, fees £3.76, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-30 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 10827 decisions in 2172 calls, $0.1512 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-31T14:25 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-31T14:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-31T14:25 | 2 / 3 / 0 | ETH-USD 50% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.83 | +1.03% | 6 |
| Candlestick reversal | LABU | 2.63 | +8.02% | 17 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Stochastic reversion | ETHU | 2.47 | +6.74% | 16 |
| Connors RSI(2) | SQQQ | 2.21 | +2.50% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.51 | 6.51 | 0 | — | 7.73 | 3.81 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.60 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.65 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.87 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.11 | 1.36 | -5.02 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.86 | -0.14 | 95 | 45.3 | -12.54 | -3.51 | -12.67 | 143 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.23 | 2.94 | -2.46 | 95 |
| 10 | Hold SPY | benchmark | 97.19 | -2.81 | 0 | — | -1.35 | -0.67 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.49 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.61 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.42 | -3.16 | -8.60 | 144 |
| 15 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.46 | 1.48 | -8.76 | 203 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -7.15 | -2.76 | -8.12 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.67 | -5.33 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -9.23 | -5.72 | -12.21 | 219 |
| 20 | Parabolic SAR · 1h | trend | 91.49 | -8.51 | 140 | 28.6 | -16.23 | -3.71 | -20.27 | 246 |
| 21 | Hold BTC | benchmark | 91.42 | -8.59 | 0 | — | -2.12 | 0.10 | -12.65 | 1 |
| 22 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -19.32 | -7.12 | -19.50 | 92 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.64 | -16.91 | 1 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.27 | -3.68 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.03 | -1.66 | -12.70 | 88 |
| 26 | Copy: Insider buying | copy | 89.48 | -10.52 | 34 | 35.3 | -23.06 | -4.70 | -23.73 | 68 |
| 27 | Donchian 55/20 · 1h | breakout | 89.34 | -10.66 | 57 | 14.0 | -16.81 | -3.73 | -17.83 | 103 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -0.84 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.44 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -10.51 | -3.48 | -15.04 | 95 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -15.72 | -3.25 | -19.27 | 105 |
| 32 | Stochastic reversion · 1h | reversion | 85.47 | -14.53 | 224 | 47.3 | -18.67 | -3.31 | -24.77 | 391 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -18.37 | -3.56 | -20.33 | 266 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.75 | -4.70 | -25.77 | 184 |
| 35 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.49 | -6.93 | -22.05 | 156 |
| 36 | Bollinger breakout · 1h | breakout | 83.33 | -16.67 | 132 | 26.5 | -15.96 | -2.96 | -21.61 | 241 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -4.98 | -19.32 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.65 | -3.47 | -30.47 | 35 |
| 39 | MFI reversion · 1h | reversion | 82.37 | -17.63 | 295 | 31.9 | -19.02 | -3.04 | -20.80 | 152 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | Supertrend · 1h | trend | 80.36 | -19.64 | 137 | 13.1 | -25.99 | -4.78 | -29.25 | 215 |
| 43 | CCI reversion · 1h | reversion | 80.10 | -19.90 | 252 | 46.0 | -26.76 | -4.20 | -28.60 | 447 |
| 44 | EMA 20/50 cross · 1h | trend | 80.09 | -19.91 | 88 | 11.4 | -22.94 | -4.34 | -26.95 | 135 |
| 45 | MACD cross · 1h | trend | 79.41 | -20.59 | 283 | 24.0 | -29.16 | -5.22 | -32.85 | 469 |
| 46 | Williams %R · 1h | reversion | 79.19 | -20.82 | 256 | 47.3 | -34.88 | -6.24 | -36.02 | 525 |
| 47 | RSI momentum · 1h | momentum | 79.11 | -20.89 | 130 | 13.1 | -26.32 | -4.76 | -30.14 | 213 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -23.20 | -4.67 | -27.15 | 210 |
| 49 | Z-score reversion · 1h | reversion | 78.40 | -21.60 | 131 | 34.4 | -17.79 | -2.78 | -22.55 | 213 |
| 50 | Heikin-Ashi · 1h | trend | 78.31 | -21.69 | 336 | 23.8 | -41.77 | -9.13 | -41.97 | 667 |
| 51 | Bollinger reversion · 1h | reversion | 78.09 | -21.91 | 199 | 37.7 | -31.72 | -6.75 | -32.94 | 377 |
| 52 | Triple EMA stack · 1h | trend | 78.04 | -21.96 | 120 | 15.0 | -30.25 | -5.63 | -33.25 | 206 |
| 53 | OBV trend · 1h | momentum | 77.91 | -22.09 | 232 | 17.7 | -32.75 | -6.64 | -36.05 | 298 |
| 54 | Donchian 20/10 · 1h | breakout | 75.97 | -24.03 | 116 | 20.7 | -26.51 | -4.66 | -29.81 | 216 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -29.13 | -5.16 | -32.80 | 379 |
| 56 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -28.37 | -1.52 | -50.32 | 42 |
| 57 | VWAP momentum · 1h | momentum | 73.27 | -26.73 | 648 | 22.7 | -51.63 | -11.01 | -51.84 | 1236 |
| 58 | RSI(14) reversion · 1h | reversion | 73.03 | -26.97 | 118 | 26.3 | -20.56 | -3.64 | -26.17 | 196 |
| 59 | Three white soldiers | momentum | 72.82 | -27.18 | 382 | 17.0 | -44.52 | -21.05 | -44.52 | 616 |
| 60 | Candlestick reversal · 1h | reversion | 71.75 | -28.25 | 325 | 28.0 | -36.31 | -7.14 | -37.11 | 555 |
| 61 | Agent (ML meta-label) | meta | 71.13 | -28.87 | 1190 | 20.8 | -17.57 | -3.05 | -17.62 | 351 |
| 62 | EMA 9/21 cross · 1h | trend | 70.94 | -29.06 | 206 | 10.2 | -34.94 | -6.64 | -36.69 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -44.58 | -98.84 | 5207 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.24 | -23.87 | -79.29 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -46.17 | -93.59 | 2535 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.60 | -30.84 | -88.61 | 1927 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.16 | -38.45 | -91.16 | 2346 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.09 | -31.77 | -90.09 | 2224 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -53.74 | -97.74 | 3522 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -61.26 | -96.21 | 3403 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.85 | -36.09 | -93.85 | 2458 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.00 | -34.08 | -82.00 | 1688 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -55.76 | -99.47 | 5922 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.83 | -44.16 | -92.87 | 2631 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -38.70 | -95.46 | 3461 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -80.92 | -99.78 | 6247 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -44.98 | -91.84 | 2305 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.29 | -27.21 | -75.55 | 1579 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -65.19 | -97.70 | 3576 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -62.82 | -98.67 | 4865 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.92 | -28.54 | -68.92 | 1211 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -55.60 | -94.69 | 2792 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.48 | -38.33 | -84.57 | 1811 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -72.27 | -99.62 | 6380 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.33 | -30.35 | -88.33 | 2257 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.77 | -19.59 | -77.92 | 1745 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.59 | -37.62 | -90.67 | 2260 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.40 | -51.25 | -96.40 | 3842 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.88 | -54.53 | -89.88 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.66 | -26.03 | -64.66 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.65 | -25.83 | -73.67 | 1274 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.89 | -18.71 | -77.06 | 1606 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.82 | -51.81 | -96.82 | 4269 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.67 | -99.92 | 8360 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-31T14:00 | Candlestick reversal · 1h | sell | XRP-USD | 8.92 | -0.05 | exit signal |
| 2026-10-31T13:55 | Three white soldiers | sell | SOL-USD | 18.12 | -0.15 | stop-loss |
| 2026-10-31T13:55 | Three white soldiers | sell | BTC-USD | 18.14 | -0.13 | exit signal |
| 2026-10-31T13:50 | Three white soldiers | buy | BTC-USD | 18.27 | — | entry signal |
| 2026-10-31T13:45 | Three white soldiers | buy | SOL-USD | 18.27 | — | entry signal |
| 2026-10-31T13:00 | Bollinger breakout · 1h | buy | ETH-USD | 20.85 | — | entry signal |
| 2026-10-31T13:00 | Donchian 20/10 · 1h | buy | ETH-USD | 19.01 | — | entry signal |
| 2026-10-31T13:00 | Three white soldiers | sell | DOGE-USD | 18.19 | -0.11 | exit signal |
| 2026-10-31T12:25 | Three white soldiers | buy | DOGE-USD | 18.30 | — | entry signal |
| 2026-10-31T12:00 | CCI reversion · 1h | buy | DOGE-USD | 7.66 | — | rebalance up |
| 2026-10-31T12:00 | CCI reversion · 1h | sell | BTC-USD | 16.00 | -0.00 | exit signal |
| 2026-10-31T12:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 17.74 | — | entry signal |
| 2026-10-31T11:45 | Agent (ML meta-label) | sell | SOL-USD | 3.08 | -0.01 | selected signal exited |
| 2026-10-31T11:40 | Agent (ML meta-label) | buy | SOL-USD | 3.09 | — | entry |
| 2026-10-31T10:00 | CCI reversion · 1h | buy | DOGE-USD | 12.39 | — | entry signal |
| 2026-10-31T10:00 | CCI reversion · 1h | sell | BTC-USD | 4.06 | -0.01 | rebalance down |
| 2026-10-31T10:00 | Candlestick reversal · 1h | buy | XRP-USD | 8.97 | — | entry signal |
| 2026-10-31T10:00 | VWAP momentum · 1h | buy | ETH-USD | 14.67 | — | entry signal |
| 2026-10-31T10:00 | VWAP momentum · 1h | buy | BTC-USD | 14.67 | — | entry signal |
| 2026-10-31T08:00 | Agent (ML meta-label) | sell | SOL-USD | 11.80 | -0.07 | selected signal exited |
| 2026-10-31T08:00 | Candlestick reversal · 1h | sell | DOGE-USD | 5.91 | -0.10 | exit signal |
| 2026-10-31T07:55 | Agent (ML meta-label) | buy | SOL-USD | 11.87 | — | entry |
| 2026-10-31T07:05 | Agent (ML meta-label) | sell | XRP-USD | 5.93 | -0.04 | selected signal exited |
| 2026-10-31T07:00 | Agent (ML meta-label) | sell | SOL-USD | 5.54 | -0.04 | selected signal exited |
| 2026-10-31T07:00 | Williams %R · 1h | buy | DOGE-USD | 6.74 | — | rebalance up |
| 2026-10-31T07:00 | Williams %R · 1h | sell | ETH-USD | 11.34 | 0.05 | exit signal |
| 2026-10-31T07:00 | Williams %R · 1h | sell | BTC-USD | 10.61 | 0.01 | exit signal |
| 2026-10-31T07:00 | Stochastic reversion · 1h | sell | ETH-USD | 4.47 | 0.02 | exit signal |
| 2026-10-31T07:00 | Stochastic reversion · 1h | sell | BTC-USD | 4.49 | -0.01 | exit signal |
| 2026-10-31T06:56 | Agent (ML meta-label) | buy | XRP-USD | 5.97 | — | entry |
| 2026-10-31T06:56 | Agent (ML meta-label) | buy | SOL-USD | 5.58 | — | entry |
| 2026-10-31T06:45 | Agent (ML meta-label) | sell | SOL-USD | 7.07 | -0.04 | selected signal exited |
| 2026-10-31T06:45 | Agent (ML meta-label) | sell | ETH-USD | 7.07 | -0.04 | selected signal exited |
| 2026-10-31T06:25 | Agent (ML meta-label) | buy | SOL-USD | 7.11 | — | entry |
| 2026-10-31T06:25 | Agent (ML meta-label) | buy | ETH-USD | 7.11 | — | entry |
| 2026-10-31T06:05 | Agent (ML meta-label) | sell | SOL-USD | 10.97 | -0.03 | selected signal exited |
| 2026-10-31T06:00 | Agent (ML meta-label) | buy | SOL-USD | 11.00 | — | entry |
| 2026-10-31T06:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.88 | — | entry signal |
| 2026-10-31T05:15 | Agent (ML meta-label) | sell | XRP-USD | 2.30 | -0.01 | selected signal exited |
| 2026-10-31T05:15 | Three white soldiers | sell | DOGE-USD | 18.21 | -0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-02 14:25:05.000142+00:00 -> 2026-10-31 14:35:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
