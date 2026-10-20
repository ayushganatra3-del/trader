# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T02:25:05.000153+00:00 · 29007 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 1620 decisions in 324 calls, $0.0228 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T02:25 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-20T02:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T02:25 | 1 / 4 / 0 | ETH-USD 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| VWAP reversion | BITX | 1.77 | +3.00% | 6 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.01 | 5.01 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.09 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.15 | -0.85 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.28 | -1.72 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.69 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.59 | -0.96 | -4.94 | 303 |
| 14 | Donchian 55/20 · 1h | breakout | 97.35 | -2.65 | 37 | 16.2 | -12.61 | -2.40 | -19.38 | 98 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.35 | -2.65 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 17 | Hold BTC | benchmark | 96.89 | -3.11 | 0 | — | 26.36 | 3.12 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 96.48 | -3.52 | 88 | 23.9 | -19.92 | -5.87 | -20.80 | 136 |
| 19 | Copy: Insider buying | copy | 96.45 | -3.55 | 23 | 43.5 | -14.93 | -2.70 | -20.62 | 73 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.38 | -3.62 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.42 | -4.58 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.63 | -6.37 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.55 | 2.17 | -6.51 | 199 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.93 | -7.07 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.00 | -8.00 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.89 | -8.11 | 78 | 23.1 | -12.57 | -2.25 | -16.37 | 102 |
| 29 | Parabolic SAR · 1h | trend | 91.41 | -8.59 | 104 | 22.1 | -16.78 | -3.52 | -23.28 | 268 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 32 | Bollinger breakout · 1h | breakout | 90.78 | -9.22 | 84 | 28.6 | -9.11 | -1.54 | -16.89 | 253 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -12.55 | -6.52 | -15.35 | 269 |
| 34 | EMA 20/50 cross · 1h | trend | 90.32 | -9.68 | 59 | 13.6 | -19.11 | -3.41 | -21.31 | 126 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.09 | -9.91 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.62 | -10.38 | 80 | 16.2 | -20.25 | -3.43 | -30.28 | 212 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 38 | Ichimoku · 1h | trend | 88.59 | -11.41 | 56 | 14.3 | -17.63 | -3.33 | -18.10 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.28 | -11.72 | 152 | 46.1 | -17.12 | -2.96 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -10.40 | -2.29 | -15.81 | 133 |
| 41 | Keltner breakout · 1h | breakout | 87.72 | -12.28 | 56 | 23.2 | -11.96 | -1.67 | -26.96 | 201 |
| 42 | Triple EMA stack · 1h | trend | 87.36 | -12.64 | 86 | 15.1 | -28.08 | -5.11 | -29.46 | 232 |
| 43 | Supertrend · 1h | trend | 87.25 | -12.75 | 87 | 12.6 | -22.95 | -4.71 | -26.61 | 214 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 86.00 | -14.00 | 189 | 20.6 | -28.32 | -5.53 | -32.78 | 467 |
| 46 | OBV trend · 1h | momentum | 85.36 | -14.64 | 180 | 17.8 | -26.53 | -3.98 | -36.15 | 313 |
| 47 | Z-score reversion · 1h | reversion | 85.20 | -14.80 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.49 | -15.51 | 209 | 31.1 | -17.28 | -2.69 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.23 | -15.77 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Agent (ML meta-label) | meta | 83.84 | -16.16 | 681 | 18.8 | -10.09 | -1.72 | -16.21 | 351 |
| 51 | Donchian 20/10 · 1h | breakout | 83.80 | -16.20 | 81 | 17.3 | -11.44 | -1.37 | -27.92 | 214 |
| 52 | Bollinger reversion · 1h | reversion | 82.85 | -17.15 | 158 | 34.8 | -27.80 | -5.31 | -33.53 | 349 |
| 53 | Max aggression: 1-day momentum | meta | 82.56 | -17.44 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 82.03 | -17.98 | 234 | 18.8 | -47.76 | -19.33 | -48.14 | 609 |
| 55 | Williams %R · 1h | reversion | 82.00 | -18.00 | 182 | 42.9 | -33.32 | -5.30 | -36.49 | 531 |
| 56 | ROC + volume · 1h | momentum | 81.46 | -18.54 | 197 | 20.8 | -23.09 | -3.49 | -33.98 | 385 |
| 57 | CCI reversion · 1h | reversion | 80.66 | -19.34 | 163 | 39.3 | -17.93 | -2.24 | -27.44 | 442 |
| 58 | RSI(14) reversion · 1h | reversion | 80.14 | -19.86 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 79.91 | -20.09 | 136 | 11.0 | -29.51 | -6.13 | -29.93 | 315 |
| 60 | Heikin-Ashi · 1h | trend | 78.85 | -21.15 | 226 | 21.2 | -41.29 | -8.76 | -45.01 | 680 |
| 61 | VWAP momentum · 1h | momentum | 77.93 | -22.07 | 433 | 20.8 | -43.31 | -7.61 | -48.46 | 1246 |
| 62 | Candlestick reversal · 1h | reversion | 77.11 | -22.89 | 214 | 27.6 | -36.60 | -6.57 | -37.48 | 529 |
| 63 | ROC + volume | momentum | 61.62 | -38.38 | 596 | 22.3 | -76.01 | -17.82 | -78.16 | 1727 |
| 64 | Volume breakout | breakout | 61.28 | -38.72 | 361 | 13.0 | -62.67 | -17.65 | -64.30 | 872 |
| 65 | Squeeze breakout | breakout | 59.82 | -40.18 | 473 | 14.0 | -63.97 | -19.67 | -65.94 | 1205 |
| 66 | Donchian 55/20 | breakout | 58.58 | -41.42 | 480 | 18.3 | -68.42 | -14.03 | -73.07 | 1269 |
| 67 | RSI(14) reversion | reversion | 57.58 | -42.42 | 713 | 25.1 | -74.68 | -16.57 | -74.75 | 1601 |
| 68 | EMA 20/50 cross | trend | 56.34 | -43.66 | 517 | 19.7 | -75.19 | -13.45 | -80.44 | 1423 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.71 | -14.63 | -72.48 | 1496 |
| 70 | Keltner breakout | breakout | 50.62 | -49.38 | 677 | 16.1 | -82.45 | -24.29 | -83.66 | 1807 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.10 | -98.70 | 5275 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.06 | -27.40 | -93.73 | 2561 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -85.89 | -18.27 | -88.26 | 1891 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.80 | -22.15 | -91.16 | 2344 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.09 | -25.84 | -91.13 | 2260 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -29.93 | -97.58 | 3490 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.51 | -32.91 | -96.76 | 3581 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -27.98 | -94.47 | 2502 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.96 | -24.36 | -82.95 | 1694 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.60 | -99.36 | 5729 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.92 | -23.26 | -92.04 | 2621 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.07 | -31.20 | -96.07 | 3463 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -37.78 | -99.74 | 6190 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.66 | -29.22 | -91.66 | 2330 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.49 | -34.75 | -97.64 | 3623 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.30 | -98.46 | 4690 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.69 | -31.30 | -93.99 | 2798 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.68 | -99.52 | 6155 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.81 | -22.30 | -86.85 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.99 | -26.66 | -88.00 | 2130 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.32 | -95.86 | 3740 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.97 | -32.21 | -89.17 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.15 | -95.72 | 4099 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.64 | -99.90 | 8277 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T02:05 | Three white soldiers | sell | DOGE-USD | 20.36 | -0.20 | exit signal |
| 2026-10-20T02:00 | Parabolic SAR · 1h | sell | SOL-USD | 22.59 | -0.21 | exit signal |
| 2026-10-20T02:00 | Parabolic SAR · 1h | sell | DOGE-USD | 22.72 | -0.26 | exit signal |
| 2026-10-20T02:00 | RSI(14) reversion | sell | BTC-USD | 14.40 | -0.03 | exit signal |
| 2026-10-20T01:55 | RSI(14) reversion | sell | SOL-USD | 14.40 | -0.01 | exit signal |
| 2026-10-20T01:46 | RSI(14) reversion | buy | SOL-USD | 2.89 | — | rebalance up |
| 2026-10-20T01:46 | RSI(14) reversion | buy | ETH-USD | 2.90 | — | rebalance up |
| 2026-10-20T01:46 | RSI(14) reversion | buy | BTC-USD | 2.90 | — | rebalance up |
| 2026-10-20T01:46 | RSI(14) reversion | sell | XRP-USD | 11.53 | 0.01 | exit signal |
| 2026-10-20T01:46 | Three white soldiers | buy | DOGE-USD | 20.56 | — | entry |
| 2026-10-20T01:35 | VWAP reversion | sell | XRP-USD | 13.41 | -0.01 | exit signal |
| 2026-10-20T01:30 | VWAP reversion | sell | ETH-USD | 13.39 | -0.02 | exit signal |
| 2026-10-20T01:20 | VWAP reversion | buy | XRP-USD | 13.41 | — | entry signal |
| 2026-10-20T01:20 | RSI(14) reversion | buy | XRP-USD | 11.52 | — | entry signal |
| 2026-10-20T01:20 | RSI(14) reversion | buy | SOL-USD | 11.52 | — | entry signal |
| 2026-10-20T01:20 | RSI(14) reversion | buy | ETH-USD | 11.52 | — | entry signal |
| 2026-10-20T01:20 | RSI(14) reversion | buy | DOGE-USD | 11.52 | — | entry signal |
| 2026-10-20T01:20 | RSI(14) reversion | buy | BTC-USD | 11.52 | — | entry signal |
| 2026-10-20T01:15 | RSI momentum · 1h | buy | XRP-USD | 5.11 | — | rebalance up |
| 2026-10-20T01:15 | RSI momentum · 1h | buy | SOL-USD | 5.96 | — | rebalance up |
| 2026-10-20T01:15 | RSI momentum · 1h | sell | DOGE-USD | 14.80 | -0.30 | stop-loss |
| 2026-10-20T01:15 | VWAP reversion | buy | ETH-USD | 13.41 | — | entry signal |
| 2026-10-20T01:10 | Donchian 20/10 · 1h | buy | XRP-USD | 3.70 | — | rebalance up |
| 2026-10-20T01:10 | RSI(14) reversion | sell | XRP-USD | 14.34 | -0.20 | stop-loss |
| 2026-10-20T01:10 | RSI(14) reversion | sell | ETH-USD | 14.33 | -0.21 | stop-loss |
| 2026-10-20T01:10 | RSI(14) reversion | sell | BTC-USD | 14.36 | -0.16 | stop-loss |
| 2026-10-20T01:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.78 | -0.04 | exit signal |
| 2026-10-20T01:00 | Ichimoku · 1h | sell | XRP-USD | 22.21 | -0.36 | exit signal |
| 2026-10-20T01:00 | Supertrend · 1h | sell | BTC-USD | 7.91 | -0.04 | exit signal |
| 2026-10-20T01:00 | Triple EMA stack · 1h | sell | XRP-USD | 21.42 | -0.22 | exit signal |
| 2026-10-20T01:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 11.92 | — | rebalance up |
| 2026-10-20T01:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 4.01 | — | rebalance up |
| 2026-10-20T01:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 15.93 | -0.15 | exit signal |
| 2026-10-20T00:55 | EMA 20/50 cross | sell | SOL-USD | 11.30 | -0.06 | exit signal |
| 2026-10-20T00:46 | EMA 20/50 cross | sell | DOGE-USD | 11.30 | -0.08 | exit signal |
| 2026-10-20T00:40 | RSI(14) reversion | buy | BTC-USD | 14.52 | — | entry signal |
| 2026-10-20T00:30 | Donchian 55/20 · 1h | sell | BTC-USD | 24.38 | -0.32 | stop-loss |
| 2026-10-20T00:25 | RSI(14) reversion | buy | XRP-USD | 14.54 | — | entry signal |
| 2026-10-20T00:25 | RSI(14) reversion | buy | ETH-USD | 14.54 | — | entry signal |
| 2026-10-20T00:20 | EMA 20/50 cross · 1h | sell | BTC-USD | 18.21 | -0.26 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 02:25:05.000153+00:00 -> 2026-10-20 02:35:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
