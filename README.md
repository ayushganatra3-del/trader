# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T02:55:05.000148+00:00 · 46813 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.19 (-9.81%)

Closed trades 143, win rate 38.5%, fees £3.99, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 2025 decisions in 405 calls, $0.0284 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T02:55 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-04T02:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T02:55 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.64 | 8.64 | 0 | — | 10.13 | 4.40 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.29 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 1.99 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.97 | -2.91 | -12.71 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.48 | -3.52 | 0 | — | -1.84 | -0.96 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.17 | 1.99 | -3.82 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.55 | -4.45 | 0 | — | -0.79 | -0.22 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.53 | -4.47 | 5 | 40.0 | 0.66 | 0.29 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 94.93 | -5.07 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.85 | -5.79 | -8.69 | 171 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.90 | -6.10 | 0 | — | -3.46 | -1.33 | -7.64 | 1 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -2.18 | -0.68 | -9.18 | 213 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 90.53 | -9.47 | 102 | 21.6 | -16.58 | -6.15 | -17.53 | 79 |
| 21 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.73 | -6.49 | -12.22 | 204 |
| 22 | Hold BTC | benchmark | 89.90 | -10.10 | 0 | — | -1.83 | -0.13 | -12.65 | 1 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.22 | -4.61 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.62 | -3.35 | -14.15 | 89 |
| 25 | Daily: Bullish score | daily | 88.32 | -11.68 | 14 | 21.4 | -7.60 | -1.05 | -14.82 | 15 |
| 26 | Donchian 55/20 · 1h | breakout | 88.01 | -11.99 | 61 | 13.1 | -14.86 | -3.35 | -18.06 | 100 |
| 27 | Copy: Insider buying | copy | 87.97 | -12.03 | 37 | 37.8 | -22.47 | -4.59 | -23.13 | 61 |
| 28 | Parabolic SAR · 1h | trend | 87.63 | -12.37 | 153 | 26.8 | -15.46 | -3.60 | -18.00 | 236 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.08 | -13.92 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.16 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.17 | -14.83 | 15 | 40.0 | -29.00 | -1.90 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 130 | 28.5 | -15.32 | -3.50 | -18.37 | 92 |
| 33 | Stochastic reversion · 1h | reversion | 84.44 | -15.56 | 242 | 47.1 | -23.25 | -4.67 | -25.31 | 387 |
| 34 | Keltner breakout · 1h | breakout | 83.95 | -16.05 | 90 | 23.3 | -21.22 | -4.45 | -22.20 | 164 |
| 35 | Connors RSI(2) · 1h | reversion | 83.82 | -16.18 | 191 | 40.8 | -19.70 | -6.55 | -20.18 | 131 |
| 36 | MFI reversion · 1h | reversion | 83.70 | -16.30 | 310 | 33.9 | -15.82 | -2.51 | -17.89 | 150 |
| 37 | ADX DI cross · 1h | trend | 82.57 | -17.43 | 153 | 17.6 | -19.80 | -3.83 | -22.27 | 256 |
| 38 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.72 | -20.73 | 716 |
| 39 | Ichimoku · 1h | trend | 81.24 | -18.77 | 84 | 13.1 | -17.75 | -3.59 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 80.65 | -19.35 | 145 | 24.1 | -18.45 | -3.76 | -23.80 | 231 |
| 41 | EMA 20/50 cross · 1h | trend | 78.67 | -21.33 | 92 | 10.9 | -18.93 | -3.37 | -27.05 | 131 |
| 42 | CCI reversion · 1h | reversion | 78.66 | -21.34 | 268 | 44.8 | -24.99 | -3.86 | -27.71 | 450 |
| 43 | Bollinger reversion · 1h | reversion | 77.97 | -22.03 | 226 | 38.9 | -27.19 | -5.32 | -29.70 | 375 |
| 44 | Z-score reversion · 1h | reversion | 77.14 | -22.86 | 142 | 34.5 | -14.60 | -2.13 | -23.02 | 218 |
| 45 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.81 | -4.36 | -33.57 | 33 |
| 46 | Supertrend · 1h | trend | 76.85 | -23.15 | 143 | 12.6 | -30.37 | -5.55 | -31.69 | 218 |
| 47 | MACD zero-line · 1h | trend | 76.66 | -23.34 | 141 | 15.6 | -26.40 | -5.91 | -28.29 | 213 |
| 48 | Williams %R · 1h | reversion | 76.40 | -23.60 | 279 | 46.6 | -36.31 | -6.54 | -37.32 | 525 |
| 49 | MACD cross · 1h | trend | 76.36 | -23.64 | 306 | 23.2 | -32.35 | -6.31 | -34.56 | 484 |
| 50 | Triple EMA stack · 1h | trend | 75.43 | -24.57 | 130 | 13.8 | -28.62 | -5.59 | -32.09 | 203 |
| 51 | Heikin-Ashi · 1h | trend | 75.40 | -24.60 | 370 | 22.7 | -42.74 | -9.67 | -43.46 | 662 |
| 52 | RSI momentum · 1h | momentum | 75.40 | -24.60 | 141 | 12.1 | -29.52 | -5.76 | -31.02 | 214 |
| 53 | OBV trend · 1h | momentum | 74.66 | -25.34 | 245 | 17.1 | -30.14 | -6.47 | -31.93 | 292 |
| 54 | Donchian 20/10 · 1h | breakout | 74.43 | -25.57 | 123 | 19.5 | -27.58 | -5.02 | -30.98 | 203 |
| 55 | ROC + volume · 1h | momentum | 72.84 | -27.16 | 313 | 25.2 | -35.55 | -6.99 | -36.43 | 372 |
| 56 | RSI(14) reversion · 1h | reversion | 72.64 | -27.36 | 130 | 26.2 | -20.79 | -3.91 | -26.28 | 196 |
| 57 | Candlestick reversal · 1h | reversion | 70.50 | -29.50 | 361 | 28.5 | -33.88 | -6.44 | -37.03 | 543 |
| 58 | Agent (ML meta-label) | meta | 69.58 | -30.42 | 1372 | 21.8 | -12.93 | -2.43 | -16.70 | 268 |
| 59 | Max aggression: 1-day momentum | meta | 68.62 | -31.38 | 23 | 30.4 | -32.21 | -1.80 | -50.32 | 42 |
| 60 | Three white soldiers | momentum | 68.41 | -31.59 | 423 | 15.8 | -46.74 | -21.36 | -46.82 | 623 |
| 61 | EMA 9/21 cross · 1h | trend | 68.05 | -31.95 | 222 | 9.5 | -38.46 | -7.86 | -39.96 | 329 |
| 62 | VWAP momentum · 1h | momentum | 67.99 | -32.01 | 717 | 21.9 | -56.46 | -12.13 | -56.47 | 1225 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.37 | -98.96 | 5152 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.69 | -23.23 | -80.57 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.31 | -42.07 | -93.52 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.71 | -29.20 | -89.17 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.89 | -34.62 | -91.20 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.96 | -32.08 | -90.96 | 2220 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -49.80 | -97.75 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -52.98 | -96.30 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -32.76 | -93.72 | 2427 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.61 | -32.97 | -82.24 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -54.71 | -99.49 | 5891 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.85 | -40.61 | -93.07 | 2612 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -37.52 | -95.45 | 3377 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.38 | -99.80 | 6181 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -42.22 | -91.84 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.40 | -25.68 | -75.06 | 1540 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -56.58 | -97.79 | 3512 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.71 | -62.16 | -98.71 | 4830 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.47 | -28.07 | -70.45 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -49.14 | -94.79 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.50 | -35.27 | -84.96 | 1785 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -72.21 | -99.63 | 6322 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.39 | -30.72 | -88.40 | 2246 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.19 | -19.53 | -77.19 | 1709 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.47 | -37.07 | -90.47 | 2236 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.55 | -52.09 | -96.55 | 3831 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -53.39 | -89.42 | 2125 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.18 | -26.92 | -65.71 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.07 | -23.21 | -74.29 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.05 | -18.93 | -77.15 | 1612 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.98 | -52.65 | -96.98 | 4250 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -91.47 | -99.92 | 8196 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T02:52 | EMA 9/21 cross · 1h | buy | XRP-USD | 5.18 | — | rebalance up |
| 2026-11-04T02:52 | EMA 9/21 cross · 1h | buy | BTC-USD | 5.13 | — | rebalance up |
| 2026-11-04T02:52 | EMA 9/21 cross · 1h | sell | ETH-USD | 11.27 | -0.21 | stop-loss |
| 2026-11-04T02:40 | EMA 20/50 cross · 1h | sell | ETH-USD | 19.43 | -0.45 | stop-loss |
| 2026-11-04T02:00 | RSI momentum · 1h | sell | ETH-USD | 18.85 | -0.22 | exit signal |
| 2026-11-04T02:00 | RSI momentum · 1h | sell | BTC-USD | 18.85 | -0.22 | exit signal |
| 2026-11-04T02:00 | VWAP momentum · 1h | sell | BTC-USD | 4.85 | -0.04 | exit signal |
| 2026-11-04T02:00 | Supertrend · 1h | buy | BTC-USD | 7.01 | — | entry |
| 2026-11-04T02:00 | Supertrend · 1h | sell | XRP-USD | 8.37 | -0.26 | exit signal |
| 2026-11-04T02:00 | Supertrend · 1h | sell | DOGE-USD | 6.90 | -0.18 | exit signal |
| 2026-11-04T02:00 | MACD cross · 1h | sell | SOL-USD | 4.47 | -0.11 | exit signal |
| 2026-11-04T02:00 | MACD cross · 1h | sell | DOGE-USD | 4.46 | -0.10 | exit signal |
| 2026-11-04T02:00 | MACD cross · 1h | sell | BTC-USD | 4.50 | -0.05 | exit signal |
| 2026-11-04T01:35 | EMA 9/21 cross · 1h | buy | ETH-USD | 4.77 | — | rebalance up |
| 2026-11-04T01:35 | EMA 9/21 cross · 1h | sell | DOGE-USD | 6.77 | -0.16 | stop-loss |
| 2026-11-04T01:00 | OBV trend · 1h | sell | XRP-USD | 18.70 | -0.08 | exit signal |
| 2026-11-04T01:00 | VWAP momentum · 1h | sell | XRP-USD | 4.82 | -0.00 | exit signal |
| 2026-11-04T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 4.84 | -0.00 | exit signal |
| 2026-11-04T01:00 | ADX DI cross · 1h | sell | SOL-USD | 9.15 | -0.13 | exit signal |
| 2026-11-04T01:00 | ADX DI cross · 1h | sell | DOGE-USD | 9.15 | -0.05 | exit signal |
| 2026-11-04T01:00 | ADX DI cross · 1h | sell | BTC-USD | 9.19 | -0.09 | exit signal |
| 2026-11-04T01:00 | Parabolic SAR · 1h | sell | XRP-USD | 21.75 | -0.38 | exit signal |
| 2026-11-04T01:00 | MACD zero-line · 1h | sell | XRP-USD | 19.19 | -0.02 | exit signal |
| 2026-11-04T01:00 | MACD zero-line · 1h | sell | ETH-USD | 19.22 | -0.20 | exit signal |
| 2026-11-04T01:00 | MACD cross · 1h | sell | XRP-USD | 4.45 | -0.10 | exit signal |
| 2026-11-04T01:00 | MACD cross · 1h | sell | ETH-USD | 4.49 | -0.07 | exit signal |
| 2026-11-04T00:35 | OBV trend · 1h | buy | XRP-USD | 3.77 | — | rebalance up |
| 2026-11-04T00:35 | RSI momentum · 1h | buy | ETH-USD | 3.78 | — | rebalance up |
| 2026-11-04T00:35 | RSI momentum · 1h | buy | BTC-USD | 3.80 | — | rebalance up |
| 2026-11-04T00:35 | RSI momentum · 1h | sell | DOGE-USD | 12.55 | -0.26 | stop-loss |
| 2026-11-04T00:35 | ROC + volume · 1h | sell | BTC-USD | 18.15 | -0.23 | stop-loss |
| 2026-11-04T00:35 | MACD zero-line · 1h | buy | XRP-USD | 3.89 | — | rebalance up |
| 2026-11-04T00:35 | MACD zero-line · 1h | buy | ETH-USD | 3.85 | — | rebalance up |
| 2026-11-04T00:35 | MACD zero-line · 1h | sell | SOL-USD | 11.43 | -0.30 | stop-loss |
| 2026-11-04T00:35 | MACD zero-line · 1h | sell | DOGE-USD | 12.74 | -0.26 | stop-loss |
| 2026-11-04T00:35 | MACD zero-line · 1h | sell | BTC-USD | 15.34 | -0.26 | stop-loss |
| 2026-11-04T00:35 | EMA 9/21 cross · 1h | sell | SOL-USD | 9.64 | -0.21 | stop-loss |
| 2026-11-04T00:25 | Bollinger breakout · 1h | sell | DOGE-USD | 16.08 | -0.25 | stop-loss |
| 2026-11-04T00:25 | Donchian 55/20 · 1h | sell | XRP-USD | 21.88 | -0.47 | stop-loss |
| 2026-11-04T00:25 | Donchian 20/10 · 1h | sell | XRP-USD | 18.17 | -0.39 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 02:55:05.000148+00:00 -> 2026-11-04 03:05:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 02:55:05.000148+00:00 -> 2026-11-04 03:05:05.000148+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 02:55:05.000148+00:00 -> 2026-11-04 03:05:05.000148+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
