# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T09:04:05.000115+00:00 · 54406 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.80 (-13.20%)

Closed trades 163, win rate 35.0%, fees £4.99, max drawdown -13.60%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 6832 decisions in 1367 calls, $0.0956 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T09:04 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-10T09:04 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-10T09:04 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| VWAP momentum | TSLA | 1.44 | +2.06% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 18.87 | 3.78 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.24 | 12.24 | 0 | — | 13.79 | 4.66 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.93 | 11.93 | 31 | 29.0 | 20.12 | 3.01 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.55 | 1.55 | 126 | 36.5 | 10.08 | 3.80 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.03 | 1.03 | 0 | — | 4.81 | 1.38 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.82 | 0.82 | 7 | 42.9 | -0.93 | 0.19 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.67 | 1.09 | -9.06 | 239 |
| 11 | Agent (rotation) | meta | 98.07 | -1.93 | 177 | 28.2 | -3.44 | -1.36 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.16 | -3.11 | -12.16 | 150 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.33 | -3.67 | 0 | — | -1.49 | -0.45 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.73 | -5.27 | 0 | — | -3.54 | -0.88 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.65 | -7.35 | 0 | — | -4.02 | -1.05 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.49 | -7.51 | 108 | 23.1 | -13.74 | -5.12 | -17.96 | 79 |
| 20 | Copy: Insider buying | copy | 91.93 | -8.07 | 42 | 38.1 | -8.47 | -1.75 | -15.11 | 66 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 90.34 | -9.66 | 391 | 34.3 | -13.39 | -4.24 | -15.24 | 595 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.56 | -3.42 | -14.68 | 80 |
| 24 | Agent | meta | 86.80 | -13.20 | 163 | 35.0 | -13.62 | -7.01 | -14.09 | 203 |
| 25 | Hold BTC | benchmark | 86.56 | -13.44 | 1 | 0.0 | -5.85 | -0.76 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.07 | -13.93 | 15 | 20.0 | -10.31 | -1.57 | -17.42 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.44 | -14.56 | 167 | 26.9 | -11.32 | -2.03 | -21.29 | 227 |
| 28 | Agent (aggressive) | meta | 83.88 | -16.12 | 76 | 31.6 | -16.53 | -4.71 | -18.49 | 94 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 83.63 | -16.37 | 2 | 0.0 | -7.65 | -0.84 | -24.16 | 1 |
| 30 | Opening range 15m | breakout | 83.50 | -16.50 | 481 | 32.4 | -18.38 | -5.20 | -19.91 | 728 |
| 31 | Donchian 55/20 · 1h | breakout | 83.33 | -16.68 | 71 | 14.1 | -17.54 | -3.81 | -22.45 | 103 |
| 32 | Stochastic reversion · 1h | reversion | 83.08 | -16.92 | 279 | 48.4 | -23.06 | -3.38 | -27.13 | 386 |
| 33 | Keltner breakout · 1h | breakout | 81.85 | -18.15 | 107 | 23.4 | -22.13 | -4.45 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.28 | -18.72 | 145 | 27.6 | -14.82 | -3.34 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.56 | -19.44 | 205 | 40.0 | -19.67 | -6.55 | -19.99 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 79.70 | -20.30 | 401 | 22.7 | -39.78 | -7.37 | -43.08 | 675 |
| 37 | ADX DI cross · 1h | trend | 79.24 | -20.76 | 179 | 18.4 | -22.84 | -3.92 | -28.34 | 277 |
| 38 | Max aggression: 5-day momentum | meta | 79.24 | -20.76 | 18 | 44.4 | -39.47 | -2.63 | -45.81 | 25 |
| 39 | MFI reversion · 1h | reversion | 79.09 | -20.91 | 352 | 34.4 | -16.70 | -2.13 | -21.23 | 166 |
| 40 | CCI reversion · 1h | reversion | 78.79 | -21.21 | 320 | 45.9 | -21.62 | -3.28 | -30.29 | 456 |
| 41 | Ichimoku · 1h | trend | 77.01 | -22.99 | 96 | 15.6 | -29.76 | -8.45 | -29.87 | 120 |
| 42 | Bollinger breakout · 1h | breakout | 76.77 | -23.23 | 170 | 22.9 | -22.64 | -4.72 | -27.92 | 240 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -23.22 | -3.50 | -32.06 | 366 |
| 44 | MACD cross · 1h | trend | 75.00 | -25.00 | 351 | 22.5 | -32.87 | -5.40 | -39.46 | 483 |
| 45 | Z-score reversion · 1h | reversion | 74.98 | -25.02 | 179 | 37.4 | -21.43 | -3.09 | -27.66 | 226 |
| 46 | Williams %R · 1h | reversion | 74.69 | -25.31 | 337 | 46.9 | -35.13 | -5.67 | -38.19 | 542 |
| 47 | MACD zero-line · 1h | trend | 74.31 | -25.69 | 157 | 16.6 | -24.89 | -5.09 | -29.19 | 215 |
| 48 | EMA 20/50 cross · 1h | trend | 74.07 | -25.93 | 102 | 10.8 | -24.30 | -4.34 | -32.62 | 127 |
| 49 | Supertrend · 1h | trend | 73.20 | -26.80 | 167 | 13.2 | -29.05 | -4.98 | -34.92 | 226 |
| 50 | RSI momentum · 1h | momentum | 72.88 | -27.12 | 159 | 12.6 | -24.14 | -3.83 | -33.01 | 218 |
| 51 | Triple EMA stack · 1h | trend | 72.35 | -27.65 | 143 | 14.7 | -26.51 | -4.61 | -34.87 | 203 |
| 52 | ROC + volume · 1h | momentum | 71.66 | -28.34 | 349 | 25.5 | -35.91 | -6.67 | -38.89 | 380 |
| 53 | OBV trend · 1h | momentum | 71.59 | -28.41 | 274 | 18.2 | -27.05 | -4.99 | -34.09 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.36 | -29.64 | 142 | 19.7 | -29.88 | -5.49 | -35.64 | 207 |
| 55 | Daily: Momentum burst | daily | 70.35 | -29.65 | 26 | 11.5 | -39.31 | -5.63 | -39.66 | 31 |
| 56 | RSI(14) reversion · 1h | reversion | 68.29 | -31.71 | 162 | 31.5 | -29.16 | -4.25 | -33.86 | 245 |
| 57 | Max aggression: 1-day momentum | meta | 68.21 | -31.79 | 27 | 25.9 | -31.45 | -1.58 | -57.50 | 42 |
| 58 | Agent (ML meta-label) | meta | 67.48 | -32.52 | 1636 | 24.1 | -8.00 | -1.06 | -20.26 | 335 |
| 59 | VWAP momentum · 1h | momentum | 67.43 | -32.57 | 814 | 21.5 | -51.76 | -11.05 | -53.43 | 1236 |
| 60 | EMA 9/21 cross · 1h | trend | 65.42 | -34.58 | 248 | 9.7 | -38.84 | -7.65 | -40.15 | 337 |
| 61 | Candlestick reversal · 1h | reversion | 64.50 | -35.50 | 438 | 28.3 | -36.83 | -6.59 | -37.61 | 594 |
| 62 | Three white soldiers | momentum | 61.45 | -38.55 | 501 | 15.0 | -48.86 | -22.89 | -48.90 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -46.15 | -98.98 | 5261 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.84 | -26.18 | -79.84 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -45.54 | -93.21 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.13 | -31.71 | -89.16 | 1904 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.62 | -38.75 | -90.62 | 2314 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.12 | -31.09 | -90.17 | 2200 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -53.73 | -97.73 | 3465 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -57.00 | -96.32 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.73 | -31.71 | -93.81 | 2431 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.19 | -33.90 | -82.19 | 1675 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -55.10 | -99.54 | 5986 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.25 | -42.81 | -92.27 | 2605 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -36.29 | -95.51 | 3410 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.46 | -99.80 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -43.11 | -91.88 | 2265 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.09 | -24.13 | -75.28 | 1593 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -59.88 | -97.71 | 3523 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -62.07 | -98.86 | 4890 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.53 | -26.81 | -69.01 | 1216 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -52.75 | -94.54 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.38 | -36.04 | -84.38 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -71.49 | -99.65 | 6371 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.73 | -32.37 | -89.75 | 2278 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.26 | -19.85 | -78.28 | 1745 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.55 | -36.10 | -90.56 | 2209 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.80 | -50.94 | -96.80 | 3883 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -56.08 | -89.28 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.80 | -27.80 | -66.38 | 815 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -70.78 | -22.40 | -71.23 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.97 | -19.12 | -79.99 | 1694 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.82 | -97.27 | 4309 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -106.57 | -99.93 | 8317 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T09:00 | Candlestick reversal · 1h | buy | ETH-USD | 12.92 | — | entry signal |
| 2026-11-10T09:00 | Candlestick reversal · 1h | sell | DOGE-USD | 12.86 | -0.10 | time stop |
| 2026-11-10T09:00 | VWAP momentum · 1h | sell | BTC-USD | 2.14 | -0.02 | exit signal |
| 2026-11-10T08:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.65 | — | rebalance up |
| 2026-11-10T08:00 | Candlestick reversal · 1h | sell | XRP-USD | 9.23 | -0.05 | exit signal |
| 2026-11-10T08:00 | VWAP momentum · 1h | buy | BTC-USD | 2.16 | — | entry signal |
| 2026-11-10T08:00 | VWAP momentum · 1h | sell | XRP-USD | 2.16 | -0.02 | exit signal |
| 2026-11-10T07:00 | Candlestick reversal · 1h | buy | SOL-USD | 8.85 | — | rebalance up |
| 2026-11-10T07:00 | Candlestick reversal · 1h | sell | ETH-USD | 9.19 | -0.10 | exit signal |
| 2026-11-10T07:00 | Candlestick reversal · 1h | sell | BTC-USD | 9.21 | -0.07 | exit signal |
| 2026-11-10T07:00 | VWAP momentum · 1h | buy | XRP-USD | 2.18 | — | entry signal |
| 2026-11-10T06:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.75 | — | entry signal |
| 2026-11-10T06:00 | MACD cross · 1h | buy | SOL-USD | 3.58 | — | entry signal |
| 2026-11-10T06:00 | MACD cross · 1h | sell | BTC-USD | 5.11 | -0.05 | exit signal |
| 2026-11-10T06:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 4.09 | — | entry signal |
| 2026-11-10T06:00 | Three white soldiers | sell | BTC-USD | 15.27 | -0.12 | stop-loss |
| 2026-11-10T05:50 | Three white soldiers | buy | BTC-USD | 15.39 | — | entry signal |
| 2026-11-10T05:00 | Williams %R · 1h | buy | SOL-USD | 12.48 | — | entry signal |
| 2026-11-10T05:00 | Williams %R · 1h | buy | ETH-USD | 12.48 | — | entry signal |
| 2026-11-10T05:00 | Williams %R · 1h | buy | DOGE-USD | 12.48 | — | entry signal |
| 2026-11-10T04:40 | Three white soldiers | sell | ETH-USD | 15.32 | -0.13 | exit signal |
| 2026-11-10T04:40 | Three white soldiers | sell | BTC-USD | 15.34 | -0.12 | exit signal |
| 2026-11-10T04:30 | Three white soldiers | buy | ETH-USD | 15.46 | — | entry signal |
| 2026-11-10T04:30 | Three white soldiers | buy | BTC-USD | 15.46 | — | entry signal |
| 2026-11-10T04:01 | MACD cross · 1h | sell | SOL-USD | 4.43 | -0.08 | exit signal |
| 2026-11-10T04:01 | EMA 9/21 cross · 1h | sell | DOGE-USD | 6.48 | -0.08 | exit signal |
| 2026-11-10T03:01 | Agent (ML meta-label) | sell | XRP-USD | 6.05 | -0.03 | selected signal exited |
| 2026-11-10T02:25 | Agent (ML meta-label) | buy | XRP-USD | 6.08 | — | entry |
| 2026-11-10T02:20 | Agent (ML meta-label) | sell | XRP-USD | 5.15 | -0.05 | selected signal exited |
| 2026-11-10T02:15 | Agent (ML meta-label) | buy | XRP-USD | 5.20 | — | entry |
| 2026-11-10T02:05 | Agent (ML meta-label) | sell | XRP-USD | 5.17 | -0.04 | selected signal exited |
| 2026-11-10T02:00 | Agent (ML meta-label) | buy | XRP-USD | 5.21 | — | entry |
| 2026-11-10T02:00 | VWAP momentum · 1h | sell | XRP-USD | 3.54 | -0.02 | exit signal |
| 2026-11-10T02:00 | Heikin-Ashi · 1h | sell | BTC-USD | 4.94 | -0.05 | exit signal |
| 2026-11-10T01:00 | VWAP momentum · 1h | buy | XRP-USD | 3.56 | — | entry signal |
| 2026-11-10T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.96 | -0.04 | exit signal |
| 2026-11-10T00:20 | Three white soldiers | sell | XRP-USD | 15.36 | -0.12 | exit signal |
| 2026-11-10T00:10 | Three white soldiers | buy | XRP-USD | 15.49 | — | entry signal |
| 2026-11-10T00:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.99 | — | entry signal |
| 2026-11-09T23:05 | Three white soldiers | sell | XRP-USD | 15.50 | -0.08 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 09:04:05.000115+00:00 -> 2026-11-10 09:14:05.000115+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
