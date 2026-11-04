# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T13:26:05.000077+00:00 · 47225 ticks

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

Today: 8202 decisions in 1641 calls, $0.1147 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T13:26 | 3 / 2 / 0 | SOL-USD 14% |  |
| Breezy | 2026-11-04T13:26 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T13:26 | 2 / 3 / 0 | BTC-USD 59% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.48 | 8.48 | 0 | — | 10.13 | 4.40 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.29 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 1.99 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.97 | -2.91 | -12.71 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.34 | -3.66 | 0 | — | -1.84 | -0.96 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.47 | 2.12 | -3.54 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.40 | -4.60 | 0 | — | -0.79 | -0.22 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.39 | -4.61 | 5 | 40.0 | 0.66 | 0.29 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 94.78 | -5.21 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.85 | -5.79 | -8.69 | 171 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.76 | -6.25 | 0 | — | -3.46 | -1.33 | -7.64 | 1 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -2.18 | -0.68 | -9.18 | 213 |
| 19 | Hold BTC | benchmark | 91.88 | -8.12 | 0 | — | -2.02 | -0.18 | -13.22 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.50 | -9.50 | 102 | 21.6 | -16.58 | -6.15 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.73 | -6.49 | -12.22 | 204 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.22 | -4.61 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.14 | -3.16 | -14.15 | 90 |
| 25 | Daily: Bullish score | daily | 88.26 | -11.74 | 14 | 21.4 | -7.60 | -1.05 | -14.82 | 15 |
| 26 | Copy: Insider buying | copy | 87.84 | -12.16 | 37 | 37.8 | -22.47 | -4.59 | -23.13 | 61 |
| 27 | Parabolic SAR · 1h | trend | 87.73 | -12.27 | 153 | 26.8 | -15.19 | -3.53 | -18.16 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 87.57 | -12.43 | 61 | 13.1 | -14.50 | -3.26 | -18.38 | 101 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 85.95 | -14.05 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.16 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.04 | -14.96 | 15 | 40.0 | -29.00 | -1.90 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 130 | 28.5 | -15.32 | -3.50 | -18.37 | 92 |
| 33 | Stochastic reversion · 1h | reversion | 84.36 | -15.64 | 242 | 47.1 | -23.25 | -4.67 | -25.31 | 387 |
| 34 | Keltner breakout · 1h | breakout | 83.81 | -16.19 | 90 | 23.3 | -20.81 | -4.35 | -22.26 | 164 |
| 35 | Connors RSI(2) · 1h | reversion | 83.79 | -16.21 | 191 | 40.8 | -19.70 | -6.55 | -20.18 | 131 |
| 36 | MFI reversion · 1h | reversion | 83.48 | -16.52 | 312 | 33.7 | -16.10 | -2.56 | -17.89 | 152 |
| 37 | ADX DI cross · 1h | trend | 82.51 | -17.49 | 154 | 17.5 | -20.29 | -3.98 | -22.30 | 261 |
| 38 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.72 | -20.73 | 716 |
| 39 | Ichimoku · 1h | trend | 81.13 | -18.87 | 84 | 13.1 | -18.26 | -3.72 | -25.58 | 121 |
| 40 | Bollinger breakout · 1h | breakout | 80.54 | -19.46 | 145 | 24.1 | -18.55 | -3.78 | -23.94 | 232 |
| 41 | EMA 20/50 cross · 1h | trend | 78.90 | -21.10 | 92 | 10.9 | -19.80 | -3.62 | -27.05 | 134 |
| 42 | CCI reversion · 1h | reversion | 78.54 | -21.46 | 268 | 44.8 | -24.86 | -3.83 | -27.71 | 455 |
| 43 | Bollinger reversion · 1h | reversion | 77.89 | -22.11 | 228 | 39.5 | -26.86 | -5.23 | -29.70 | 379 |
| 44 | Z-score reversion · 1h | reversion | 77.06 | -22.94 | 144 | 34.7 | -14.42 | -2.10 | -23.02 | 221 |
| 45 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.81 | -4.36 | -33.57 | 33 |
| 46 | Supertrend · 1h | trend | 76.65 | -23.35 | 145 | 12.4 | -30.55 | -5.59 | -31.94 | 223 |
| 47 | Williams %R · 1h | reversion | 76.38 | -23.62 | 282 | 46.8 | -36.06 | -6.47 | -37.32 | 530 |
| 48 | MACD cross · 1h | trend | 76.19 | -23.81 | 306 | 23.2 | -32.42 | -6.32 | -34.69 | 490 |
| 49 | MACD zero-line · 1h | trend | 76.12 | -23.88 | 141 | 15.6 | -27.01 | -6.08 | -28.77 | 216 |
| 50 | Triple EMA stack · 1h | trend | 75.40 | -24.60 | 130 | 13.8 | -29.47 | -5.81 | -32.26 | 206 |
| 51 | RSI momentum · 1h | momentum | 75.21 | -24.79 | 141 | 12.1 | -29.96 | -5.86 | -30.54 | 217 |
| 52 | Heikin-Ashi · 1h | trend | 75.15 | -24.85 | 372 | 22.6 | -42.76 | -9.68 | -43.70 | 666 |
| 53 | OBV trend · 1h | momentum | 74.67 | -25.33 | 245 | 17.1 | -30.53 | -6.63 | -32.08 | 294 |
| 54 | Donchian 20/10 · 1h | breakout | 73.99 | -26.01 | 123 | 19.5 | -27.95 | -5.10 | -31.49 | 206 |
| 55 | RSI(14) reversion · 1h | reversion | 72.53 | -27.47 | 130 | 26.2 | -20.76 | -3.90 | -26.28 | 198 |
| 56 | ROC + volume · 1h | momentum | 72.50 | -27.50 | 313 | 25.2 | -35.81 | -7.05 | -36.78 | 374 |
| 57 | Candlestick reversal · 1h | reversion | 70.40 | -29.60 | 361 | 28.5 | -32.85 | -6.17 | -36.32 | 536 |
| 58 | Agent (ML meta-label) | meta | 69.47 | -30.53 | 1372 | 21.8 | -8.84 | -1.64 | -17.19 | 263 |
| 59 | Max aggression: 1-day momentum | meta | 68.52 | -31.48 | 23 | 30.4 | -32.21 | -1.80 | -50.32 | 42 |
| 60 | Three white soldiers | momentum | 68.07 | -31.93 | 426 | 15.7 | -46.93 | -21.60 | -47.04 | 625 |
| 61 | VWAP momentum · 1h | momentum | 68.05 | -31.95 | 717 | 21.9 | -56.38 | -12.10 | -56.51 | 1230 |
| 62 | EMA 9/21 cross · 1h | trend | 67.73 | -32.27 | 224 | 9.4 | -38.79 | -7.94 | -40.37 | 334 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -43.72 | -98.98 | 5141 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.22 | -24.60 | -80.33 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -45.08 | -93.55 | 2511 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -30.24 | -89.11 | 1894 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.24 | -37.51 | -91.32 | 2315 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.59 | -31.82 | -90.59 | 2204 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -51.14 | -97.76 | 3451 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -56.35 | -96.30 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.69 | -33.40 | -93.69 | 2440 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.20 | -35.77 | -82.20 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -53.99 | -99.49 | 5882 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.14 | -43.93 | -93.16 | 2618 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.37 | -36.61 | -95.37 | 3362 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.21 | -99.80 | 6177 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -42.56 | -91.86 | 2254 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.58 | -27.22 | -75.58 | 1548 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -58.74 | -97.78 | 3507 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -61.30 | -98.70 | 4823 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.52 | -31.44 | -70.64 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.89 | -54.70 | -94.90 | 2778 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.03 | -37.78 | -85.12 | 1789 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.56 | -99.63 | 6319 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.37 | -30.64 | -88.43 | 2250 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.99 | -19.32 | -77.08 | 1709 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.28 | -36.31 | -90.42 | 2231 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.54 | -51.64 | -96.55 | 3829 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -52.42 | -89.41 | 2132 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.83 | -28.27 | -65.83 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.06 | -25.52 | -74.16 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.87 | -18.79 | -77.16 | 1609 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.97 | -52.12 | -96.98 | 4247 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.50 | -99.92 | 8202 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T13:00 | Heikin-Ashi · 1h | sell | XRP-USD | 9.39 | -0.06 | exit signal |
| 2026-11-04T13:00 | Heikin-Ashi · 1h | sell | BTC-USD | 9.36 | -0.04 | exit signal |
| 2026-11-04T13:00 | Ichimoku · 1h | buy | XRP-USD | 19.37 | — | entry signal |
| 2026-11-04T13:00 | Ichimoku · 1h | buy | ETH-USD | 20.30 | — | entry signal |
| 2026-11-04T13:00 | Ichimoku · 1h | buy | BTC-USD | 20.30 | — | entry signal |
| 2026-11-04T13:00 | ADX DI cross · 1h | sell | DOGE-USD | 6.43 | -0.07 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 13:26:05.000077+00:00 -> 2026-11-04 13:36:05.000077+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 13:26:05.000077+00:00 -> 2026-11-04 13:36:05.000077+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 13:26:05.000077+00:00 -> 2026-11-04 13:36:05.000077+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
