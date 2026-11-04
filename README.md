# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T14:25:05.000153+00:00 · 47282 ticks

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

Today: 9057 decisions in 1812 calls, $0.1266 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T14:25 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-04T14:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T14:25 | 1 / 4 / 0 | ETH-USD 62% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.38 | 8.38 | 0 | — | 10.13 | 4.40 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.29 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 1.99 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.15 | -2.94 | -12.89 | 141 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 10 | Hold SPY | benchmark | 96.25 | -3.75 | 0 | — | -1.84 | -0.96 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 5.07 | 2.44 | -3.00 | 90 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.31 | -4.69 | 0 | — | -0.79 | -0.22 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.30 | -4.70 | 5 | 40.0 | 0.66 | 0.29 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 94.69 | -5.31 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.85 | -5.79 | -8.69 | 171 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.67 | -6.33 | 0 | — | -3.46 | -1.33 | -7.64 | 1 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -2.18 | -0.68 | -9.18 | 213 |
| 19 | Hold BTC | benchmark | 91.78 | -8.22 | 0 | — | -3.34 | -0.42 | -13.22 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.48 | -9.52 | 102 | 21.6 | -16.58 | -6.15 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.72 | -6.49 | -12.22 | 205 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.22 | -4.61 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.19 | -2.78 | -14.15 | 91 |
| 25 | Daily: Bullish score | daily | 88.22 | -11.78 | 14 | 21.4 | -7.60 | -1.05 | -14.82 | 15 |
| 26 | Copy: Insider buying | copy | 87.75 | -12.25 | 37 | 37.8 | -22.47 | -4.59 | -23.13 | 61 |
| 27 | Parabolic SAR · 1h | trend | 87.66 | -12.34 | 153 | 26.8 | -15.16 | -3.52 | -18.16 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 87.52 | -12.48 | 61 | 13.1 | -14.47 | -3.26 | -18.38 | 101 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 85.87 | -14.13 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.16 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 84.96 | -15.04 | 15 | 40.0 | -28.92 | -1.91 | -36.71 | 24 |
| 32 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 130 | 28.5 | -14.89 | -3.41 | -17.85 | 91 |
| 33 | Stochastic reversion · 1h | reversion | 84.31 | -15.69 | 242 | 47.1 | -23.27 | -4.68 | -25.33 | 386 |
| 34 | Connors RSI(2) · 1h | reversion | 83.77 | -16.23 | 191 | 40.8 | -19.70 | -6.55 | -20.18 | 131 |
| 35 | Keltner breakout · 1h | breakout | 83.77 | -16.23 | 90 | 23.3 | -22.83 | -4.85 | -22.89 | 164 |
| 36 | MFI reversion · 1h | reversion | 83.44 | -16.56 | 312 | 33.7 | -15.19 | -2.35 | -17.89 | 151 |
| 37 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.72 | -20.73 | 716 |
| 38 | ADX DI cross · 1h | trend | 82.45 | -17.55 | 154 | 17.5 | -20.12 | -3.92 | -22.30 | 261 |
| 39 | Ichimoku · 1h | trend | 81.08 | -18.92 | 84 | 13.1 | -18.24 | -3.71 | -25.58 | 121 |
| 40 | Bollinger breakout · 1h | breakout | 80.53 | -19.47 | 145 | 24.1 | -18.53 | -3.78 | -23.94 | 232 |
| 41 | EMA 20/50 cross · 1h | trend | 78.85 | -21.15 | 92 | 10.9 | -19.70 | -3.62 | -27.05 | 130 |
| 42 | CCI reversion · 1h | reversion | 78.46 | -21.54 | 268 | 44.8 | -24.83 | -3.83 | -27.71 | 455 |
| 43 | Bollinger reversion · 1h | reversion | 77.82 | -22.18 | 228 | 39.5 | -26.86 | -5.23 | -29.70 | 379 |
| 44 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.81 | -4.36 | -33.57 | 33 |
| 45 | Z-score reversion · 1h | reversion | 76.99 | -23.01 | 144 | 34.7 | -14.42 | -2.10 | -23.02 | 221 |
| 46 | Supertrend · 1h | trend | 76.60 | -23.40 | 145 | 12.4 | -30.25 | -5.54 | -31.73 | 222 |
| 47 | Williams %R · 1h | reversion | 76.31 | -23.69 | 282 | 46.8 | -36.39 | -6.51 | -37.64 | 530 |
| 48 | MACD zero-line · 1h | trend | 76.15 | -23.85 | 141 | 15.6 | -27.04 | -6.09 | -28.74 | 216 |
| 49 | MACD cross · 1h | trend | 76.14 | -23.86 | 306 | 23.2 | -32.92 | -6.50 | -33.85 | 484 |
| 50 | Triple EMA stack · 1h | trend | 75.35 | -24.65 | 130 | 13.8 | -28.35 | -5.60 | -32.26 | 201 |
| 51 | RSI momentum · 1h | momentum | 75.17 | -24.83 | 141 | 12.1 | -30.23 | -5.94 | -31.00 | 218 |
| 52 | Heikin-Ashi · 1h | trend | 75.10 | -24.90 | 372 | 22.6 | -42.76 | -9.68 | -43.70 | 666 |
| 53 | OBV trend · 1h | momentum | 74.62 | -25.38 | 245 | 17.1 | -31.08 | -6.83 | -31.29 | 290 |
| 54 | Donchian 20/10 · 1h | breakout | 73.95 | -26.05 | 123 | 19.5 | -27.92 | -5.09 | -31.49 | 206 |
| 55 | ROC + volume · 1h | momentum | 72.48 | -27.52 | 313 | 25.2 | -36.03 | -7.10 | -37.02 | 375 |
| 56 | RSI(14) reversion · 1h | reversion | 72.46 | -27.54 | 130 | 26.2 | -20.76 | -3.90 | -26.28 | 198 |
| 57 | Candlestick reversal · 1h | reversion | 70.33 | -29.67 | 361 | 28.5 | -33.15 | -6.25 | -36.55 | 539 |
| 58 | Agent (ML meta-label) | meta | 69.41 | -30.59 | 1372 | 21.8 | -5.73 | -1.08 | -15.79 | 251 |
| 59 | Max aggression: 1-day momentum | meta | 68.45 | -31.55 | 23 | 30.4 | -34.02 | -1.97 | -50.32 | 41 |
| 60 | Three white soldiers | momentum | 68.07 | -31.93 | 426 | 15.7 | -46.93 | -21.60 | -47.04 | 625 |
| 61 | VWAP momentum · 1h | momentum | 68.02 | -31.98 | 717 | 21.9 | -56.32 | -12.07 | -56.46 | 1227 |
| 62 | EMA 9/21 cross · 1h | trend | 67.70 | -32.30 | 224 | 9.4 | -38.60 | -7.87 | -40.37 | 334 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -43.67 | -98.98 | 5158 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.26 | -24.66 | -80.34 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -45.09 | -93.53 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -30.24 | -89.11 | 1894 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -37.43 | -91.30 | 2315 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.61 | -32.01 | -90.61 | 2204 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -51.35 | -97.76 | 3452 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -56.82 | -96.30 | 3376 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -33.09 | -93.62 | 2425 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.19 | -35.72 | -82.19 | 1651 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -54.13 | -99.49 | 5885 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.10 | -43.62 | -93.14 | 2617 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.39 | -36.68 | -95.39 | 3365 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.19 | -99.80 | 6180 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -42.56 | -91.86 | 2254 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.29 | -27.10 | -75.29 | 1545 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -58.36 | -97.77 | 3505 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -61.44 | -98.70 | 4823 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.52 | -31.39 | -70.65 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.91 | -54.96 | -94.92 | 2779 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.03 | -37.77 | -85.13 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -70.78 | -99.63 | 6319 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.36 | -30.62 | -88.43 | 2250 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.96 | -19.29 | -77.06 | 1708 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.32 | -36.28 | -90.46 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.55 | -51.72 | -96.55 | 3829 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -53.20 | -89.43 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.74 | -28.10 | -65.76 | 800 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.03 | -25.46 | -74.13 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.12 | -18.94 | -77.40 | 1611 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.97 | -52.22 | -96.98 | 4247 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.96 | -99.93 | 8204 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 14:25:05.000153+00:00 -> 2026-11-04 14:35:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 14:25:05.000153+00:00 -> 2026-11-04 14:35:05.000153+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 14:25:05.000153+00:00 -> 2026-11-04 14:35:05.000153+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
