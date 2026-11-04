# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T12:28:05.000143+00:00 · 47168 ticks

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

Today: 7347 decisions in 1470 calls, $0.1027 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T12:28 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-04T12:28 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T12:28 | 2 / 3 / 0 | ETH-USD 55% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.51 | 8.51 | 0 | — | 10.13 | 4.43 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.29 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 1.99 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.33 | -3.00 | -13.06 | 141 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.36 | -3.64 | 0 | — | -1.84 | -0.96 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.78 | 2.31 | -3.26 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.43 | -4.57 | 0 | — | -0.79 | -0.22 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.40 | -4.60 | 5 | 40.0 | 0.63 | 0.28 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 94.81 | -5.19 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.85 | -5.79 | -8.69 | 171 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.78 | -6.22 | 0 | — | -3.46 | -1.33 | -7.64 | 1 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -2.18 | -0.68 | -9.18 | 213 |
| 19 | Hold BTC | benchmark | 91.62 | -8.38 | 0 | — | -0.84 | 0.03 | -13.22 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.50 | -9.50 | 102 | 21.6 | -16.58 | -6.15 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.72 | -6.49 | -12.22 | 205 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.22 | -4.61 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.05 | -3.12 | -14.15 | 90 |
| 25 | Daily: Bullish score | daily | 88.27 | -11.73 | 14 | 21.4 | -7.60 | -1.05 | -14.82 | 15 |
| 26 | Copy: Insider buying | copy | 87.86 | -12.14 | 37 | 37.8 | -22.47 | -4.59 | -23.13 | 61 |
| 27 | Parabolic SAR · 1h | trend | 87.66 | -12.34 | 153 | 26.8 | -15.31 | -3.56 | -18.16 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 87.52 | -12.48 | 61 | 13.1 | -14.58 | -3.28 | -18.32 | 101 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 85.97 | -14.03 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.16 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.06 | -14.94 | 15 | 40.0 | -29.00 | -1.90 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 130 | 28.5 | -15.32 | -3.50 | -18.37 | 92 |
| 33 | Stochastic reversion · 1h | reversion | 84.37 | -15.63 | 242 | 47.1 | -23.25 | -4.67 | -25.31 | 387 |
| 34 | Connors RSI(2) · 1h | reversion | 83.80 | -16.20 | 191 | 40.8 | -19.70 | -6.55 | -20.18 | 131 |
| 35 | Keltner breakout · 1h | breakout | 83.80 | -16.20 | 90 | 23.3 | -20.83 | -4.35 | -22.24 | 164 |
| 36 | MFI reversion · 1h | reversion | 83.46 | -16.54 | 312 | 33.7 | -15.92 | -2.53 | -17.89 | 153 |
| 37 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.72 | -20.73 | 716 |
| 38 | ADX DI cross · 1h | trend | 82.49 | -17.51 | 153 | 17.6 | -20.31 | -3.99 | -22.30 | 261 |
| 39 | Ichimoku · 1h | trend | 81.21 | -18.79 | 84 | 13.1 | -18.19 | -3.70 | -25.58 | 118 |
| 40 | Bollinger breakout · 1h | breakout | 80.53 | -19.47 | 145 | 24.1 | -18.48 | -3.77 | -23.92 | 232 |
| 41 | EMA 20/50 cross · 1h | trend | 78.81 | -21.19 | 92 | 10.9 | -19.79 | -3.60 | -27.05 | 134 |
| 42 | CCI reversion · 1h | reversion | 78.56 | -21.44 | 268 | 44.8 | -24.87 | -3.84 | -27.71 | 455 |
| 43 | Bollinger reversion · 1h | reversion | 77.91 | -22.09 | 228 | 39.5 | -26.87 | -5.24 | -29.70 | 379 |
| 44 | Z-score reversion · 1h | reversion | 77.08 | -22.92 | 144 | 34.7 | -14.42 | -2.10 | -23.02 | 221 |
| 45 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.80 | -4.36 | -33.56 | 33 |
| 46 | Supertrend · 1h | trend | 76.64 | -23.36 | 145 | 12.4 | -30.59 | -5.60 | -31.91 | 223 |
| 47 | Williams %R · 1h | reversion | 76.39 | -23.61 | 282 | 46.8 | -36.06 | -6.47 | -37.32 | 530 |
| 48 | MACD cross · 1h | trend | 76.18 | -23.82 | 306 | 23.2 | -32.44 | -6.33 | -34.69 | 490 |
| 49 | MACD zero-line · 1h | trend | 76.05 | -23.95 | 141 | 15.6 | -27.10 | -6.09 | -28.75 | 216 |
| 50 | Triple EMA stack · 1h | trend | 75.33 | -24.67 | 130 | 13.8 | -30.02 | -5.94 | -32.26 | 206 |
| 51 | Heikin-Ashi · 1h | trend | 75.21 | -24.79 | 370 | 22.7 | -42.63 | -9.63 | -43.69 | 666 |
| 52 | RSI momentum · 1h | momentum | 75.13 | -24.87 | 141 | 12.1 | -30.50 | -6.00 | -31.05 | 218 |
| 53 | OBV trend · 1h | momentum | 74.64 | -25.36 | 245 | 17.1 | -30.84 | -6.68 | -32.31 | 295 |
| 54 | Donchian 20/10 · 1h | breakout | 73.89 | -26.11 | 123 | 19.5 | -28.07 | -5.12 | -31.45 | 206 |
| 55 | RSI(14) reversion · 1h | reversion | 72.55 | -27.45 | 130 | 26.2 | -20.26 | -3.78 | -26.28 | 200 |
| 56 | ROC + volume · 1h | momentum | 72.46 | -27.54 | 313 | 25.2 | -35.86 | -7.06 | -36.73 | 374 |
| 57 | Candlestick reversal · 1h | reversion | 70.42 | -29.58 | 361 | 28.5 | -34.09 | -6.48 | -37.45 | 545 |
| 58 | Agent (ML meta-label) | meta | 69.49 | -30.51 | 1372 | 21.8 | -11.16 | -1.98 | -17.89 | 267 |
| 59 | Max aggression: 1-day momentum | meta | 68.54 | -31.46 | 23 | 30.4 | -32.21 | -1.80 | -50.32 | 42 |
| 60 | Three white soldiers | momentum | 68.07 | -31.93 | 426 | 15.7 | -46.93 | -21.67 | -47.04 | 625 |
| 61 | VWAP momentum · 1h | momentum | 68.02 | -31.98 | 717 | 21.9 | -56.41 | -12.11 | -56.51 | 1230 |
| 62 | EMA 9/21 cross · 1h | trend | 67.67 | -32.33 | 224 | 9.4 | -38.85 | -7.95 | -40.34 | 334 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -42.87 | -98.98 | 5142 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.14 | -24.43 | -80.33 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -45.10 | -93.55 | 2511 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -30.24 | -89.11 | 1894 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -37.41 | -91.30 | 2315 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.73 | -31.70 | -90.73 | 2211 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -51.14 | -97.76 | 3451 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -56.46 | -96.30 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -33.42 | -93.76 | 2445 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.22 | -35.83 | -82.22 | 1654 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.81 | -99.49 | 5879 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -41.66 | -93.14 | 2618 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.37 | -36.65 | -95.37 | 3362 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.36 | -99.80 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -42.56 | -91.86 | 2254 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.75 | -26.28 | -75.42 | 1550 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -58.90 | -97.78 | 3509 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -60.87 | -98.70 | 4818 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.17 | -30.35 | -70.69 | 1209 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -51.45 | -94.91 | 2782 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.68 | -36.22 | -85.11 | 1791 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.70 | -99.63 | 6319 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.37 | -30.62 | -88.43 | 2248 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.97 | -19.29 | -77.04 | 1707 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.31 | -36.31 | -90.45 | 2232 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.54 | -51.64 | -96.54 | 3828 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -52.30 | -89.41 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.14 | -26.59 | -65.94 | 804 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.06 | -25.52 | -74.16 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.06 | -18.94 | -77.34 | 1612 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.97 | -52.16 | -96.98 | 4246 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.91 | -99.92 | 8200 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T11:30 | Donchian 55/20 · 1h | buy | XRP-USD | 20.89 | — | entry |
| 2026-11-04T11:30 | Donchian 20/10 · 1h | buy | XRP-USD | 18.22 | — | entry |
| 2026-11-04T11:30 | RSI momentum · 1h | buy | XRP-USD | 15.12 | — | entry |
| 2026-11-04T11:30 | RSI momentum · 1h | sell | ETH-USD | 3.90 | 0.02 | rebalance down |
| 2026-11-04T11:30 | RSI momentum · 1h | sell | BTC-USD | 3.77 | -0.00 | rebalance down |
| 2026-11-04T11:30 | ROC + volume · 1h | buy | XRP-USD | 18.22 | — | entry |
| 2026-11-04T11:30 | MACD zero-line · 1h | buy | SOL-USD | 19.18 | — | entry |
| 2026-11-04T11:30 | MACD zero-line · 1h | buy | DOGE-USD | 19.18 | — | entry |
| 2026-11-04T11:30 | MACD cross · 1h | buy | XRP-USD | 3.64 | — | entry |
| 2026-11-04T11:30 | Triple EMA stack · 1h | buy | BTC-USD | 3.86 | — | rebalance up |
| 2026-11-04T11:30 | Triple EMA stack · 1h | sell | XRP-USD | 3.86 | 0.02 | rebalance down |
| 2026-11-04T09:00 | Williams %R · 1h | sell | SOL-USD | 4.54 | -0.01 | exit signal |
| 2026-11-04T09:00 | Williams %R · 1h | sell | DOGE-USD | 1.95 | 0.04 | exit signal |
| 2026-11-04T09:00 | Keltner breakout · 1h | buy | ETH-USD | 20.98 | — | entry signal |
| 2026-11-04T09:00 | Bollinger breakout · 1h | buy | ETH-USD | 20.16 | — | entry signal |
| 2026-11-04T09:00 | Donchian 55/20 · 1h | buy | ETH-USD | 21.99 | — | entry signal |
| 2026-11-04T09:00 | Donchian 20/10 · 1h | buy | ETH-USD | 18.60 | — | entry signal |
| 2026-11-04T09:00 | Donchian 20/10 · 1h | buy | BTC-USD | 18.60 | — | entry signal |
| 2026-11-04T09:00 | ROC + volume · 1h | buy | ETH-USD | 18.21 | — | entry signal |
| 2026-11-04T09:00 | Supertrend · 1h | buy | SOL-USD | 2.12 | — | entry signal |
| 2026-11-04T09:00 | Supertrend · 1h | buy | DOGE-USD | 5.91 | — | entry signal |
| 2026-11-04T09:00 | MACD cross · 1h | buy | DOGE-USD | 3.82 | — | entry signal |
| 2026-11-04T09:00 | Triple EMA stack · 1h | buy | BTC-USD | 7.34 | — | entry signal |
| 2026-11-04T09:00 | Triple EMA stack · 1h | sell | ETH-USD | 3.86 | 0.01 | rebalance down |
| 2026-11-04T09:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 19.43 | — | entry signal |
| 2026-11-04T09:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 5.62 | — | entry signal |
| 2026-11-04T09:00 | Three white soldiers | sell | DOGE-USD | 16.89 | -0.17 | exit signal |
| 2026-11-04T08:20 | Bollinger reversion · 1h | sell | DOGE-USD | 2.13 | 0.02 | target is flat |
| 2026-11-04T08:20 | Three white soldiers | buy | DOGE-USD | 17.06 | — | entry |
| 2026-11-04T08:00 | RSI momentum · 1h | buy | ETH-USD | 18.85 | — | entry signal |
| 2026-11-04T08:00 | RSI momentum · 1h | buy | BTC-USD | 18.85 | — | entry signal |
| 2026-11-04T08:00 | ADX DI cross · 1h | buy | DOGE-USD | 6.50 | — | entry signal |
| 2026-11-04T08:00 | MACD cross · 1h | buy | SOL-USD | 4.02 | — | entry signal |
| 2026-11-04T07:00 | Z-score reversion · 1h | sell | SOL-USD | 3.96 | -0.01 | exit signal |
| 2026-11-04T07:00 | Heikin-Ashi · 1h | buy | BTC-USD | 9.40 | — | entry signal |
| 2026-11-04T07:00 | Heikin-Ashi · 1h | sell | XRP-USD | 9.33 | -0.07 | rebalance down |
| 2026-11-04T07:00 | MACD zero-line · 1h | buy | BTC-USD | 19.16 | — | entry signal |
| 2026-11-04T07:00 | MACD cross · 1h | buy | ETH-USD | 4.24 | — | entry signal |
| 2026-11-04T07:00 | MACD cross · 1h | buy | BTC-USD | 4.24 | — | entry signal |
| 2026-11-04T07:00 | Triple EMA stack · 1h | buy | ETH-USD | 18.84 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 12:28:05.000143+00:00 -> 2026-11-04 12:38:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 12:28:05.000143+00:00 -> 2026-11-04 12:38:05.000143+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 12:28:05.000143+00:00 -> 2026-11-04 12:38:05.000143+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
