# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T16:40:05.000119+00:00 · 35668 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, IAM 12%, APLD 12%, BPRE 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 12558 decisions in 2517 calls, $0.1756 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T16:40 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-25T16:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T16:40 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | BITX | 2.56 | +2.84% | 15 |
| VWAP momentum | PLTR | 2.20 | +6.89% | 7 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.95 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.02 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.60 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.04 | -3.33 | -13.74 | 157 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 6.21 | 2.99 | -1.37 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.18 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.85 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.21 | -4.79 | 0 | — | 0.13 | 0.19 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.13 | -5.87 | 25 | 40.0 | -17.34 | -3.33 | -21.47 | 61 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.76 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -6.94 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.50 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.42 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -21.25 | -4.95 | -24.39 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.35 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.35 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.91 | -9.09 | 109 | 18.3 | -12.09 | -2.45 | -14.69 | 257 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.03 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -14.69 | -2.97 | -17.81 | 114 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.70 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.74 | -11.26 | 106 | 27.4 | -12.35 | -2.41 | -16.40 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.23 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.90 | -3.92 | -22.47 | 393 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -23.06 | -4.84 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -23.06 | -4.55 | -25.00 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.06 | -4.63 | -17.87 | 703 |
| 40 | RSI momentum · 1h | momentum | 85.45 | -14.55 | 101 | 15.8 | -21.55 | -4.56 | -23.32 | 216 |
| 41 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 42 | Supertrend · 1h | trend | 84.78 | -15.22 | 112 | 14.3 | -25.16 | -5.27 | -27.77 | 216 |
| 43 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 44 | MACD cross · 1h | trend | 83.59 | -16.41 | 228 | 22.8 | -24.39 | -4.87 | -27.39 | 465 |
| 45 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.52 | -5.24 | -28.27 | 211 |
| 46 | Z-score reversion · 1h | reversion | 83.46 | -16.54 | 109 | 33.9 | -15.59 | -2.62 | -21.48 | 204 |
| 47 | MFI reversion · 1h | reversion | 81.49 | -18.51 | 262 | 31.7 | -16.17 | -2.63 | -20.54 | 148 |
| 48 | Donchian 20/10 · 1h | breakout | 81.18 | -18.82 | 97 | 19.6 | -24.26 | -4.64 | -27.27 | 217 |
| 49 | MACD zero-line · 1h | trend | 81.16 | -18.84 | 106 | 15.1 | -22.09 | -4.59 | -25.51 | 219 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.65 | -6.89 | -32.94 | 304 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.23 | -6.42 | -36.69 | 536 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.86 | -6.61 | -32.19 | 372 |
| 53 | CCI reversion · 1h | reversion | 79.78 | -20.22 | 204 | 42.2 | -27.10 | -4.05 | -28.17 | 462 |
| 54 | Agent (ML meta-label) | meta | 79.31 | -20.69 | 874 | 18.8 | -17.61 | -3.72 | -19.06 | 348 |
| 55 | Three white soldiers | momentum | 79.30 | -20.70 | 289 | 19.0 | -44.43 | -21.03 | -44.43 | 597 |
| 56 | Heikin-Ashi · 1h | trend | 78.33 | -21.67 | 277 | 23.1 | -43.44 | -9.96 | -43.91 | 656 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -29.81 | -5.85 | -31.53 | 377 |
| 58 | Candlestick reversal · 1h | reversion | 76.84 | -23.16 | 263 | 28.1 | -36.60 | -6.90 | -37.16 | 560 |
| 59 | RSI(14) reversion · 1h | reversion | 76.70 | -23.30 | 99 | 23.2 | -15.47 | -2.85 | -24.41 | 193 |
| 60 | EMA 9/21 cross · 1h | trend | 76.67 | -23.33 | 164 | 11.6 | -30.84 | -6.27 | -34.03 | 323 |
| 61 | VWAP momentum · 1h | momentum | 75.24 | -24.76 | 531 | 20.9 | -50.92 | -11.66 | -50.92 | 1232 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 56.14 | -43.86 | 723 | 22.1 | -74.86 | -27.43 | -74.97 | 1555 |
| 64 | Volume breakout | breakout | 54.84 | -45.16 | 441 | 12.5 | -62.62 | -26.59 | -62.80 | 791 |
| 65 | Donchian 55/20 | breakout | 52.09 | -47.91 | 576 | 19.1 | -71.50 | -23.48 | -72.19 | 1259 |
| 66 | Squeeze breakout | breakout | 51.86 | -48.14 | 572 | 13.8 | -67.50 | -29.30 | -67.52 | 1168 |
| 67 | EMA 20/50 cross | trend | 51.23 | -48.77 | 633 | 20.2 | -79.10 | -23.46 | -79.39 | 1419 |
| 68 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.81 | -45.38 | -98.81 | 5093 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -45.70 | -93.95 | 2528 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.00 | -30.91 | -89.09 | 1903 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -38.37 | -91.54 | 2329 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.28 | -29.50 | -90.29 | 2150 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -55.46 | -97.90 | 3519 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -59.86 | -96.18 | 3361 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -35.33 | -94.09 | 2456 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.97 | -36.22 | -83.27 | 1696 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -54.92 | -99.42 | 5777 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.46 | -42.27 | -92.58 | 2603 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -38.00 | -95.44 | 3370 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -82.32 | -99.78 | 6169 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.33 | -45.49 | -92.33 | 2340 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -63.49 | -97.65 | 3550 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.49 | -98.65 | 4789 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -59.86 | -94.63 | 2776 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.16 | -39.77 | -84.23 | 1789 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -68.31 | -99.59 | 6257 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.41 | -29.57 | -88.42 | 2230 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.22 | -20.37 | -78.27 | 1710 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.77 | -38.61 | -90.81 | 2277 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.28 | -48.94 | -96.28 | 3797 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.92 | -51.35 | -89.92 | 2121 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.79 | -18.25 | -76.94 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.43 | -49.81 | -96.43 | 4179 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -112.84 | -99.92 | 8252 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T16:40 | Agent (ML meta-label) | sell | XRP-USD | 4.37 | -0.03 | selected signal exited |
| 2026-10-25T16:30 | Agent (ML meta-label) | buy | XRP-USD | 4.41 | — | entry |
| 2026-10-25T16:05 | Volume breakout | sell | XRP-USD | 13.65 | -0.12 | exit signal |
| 2026-10-25T16:05 | Volume breakout | sell | ETH-USD | 13.64 | -0.13 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | XRP-USD | 14.02 | -0.12 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | SOL-USD | 14.05 | -0.09 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | ETH-USD | 14.01 | -0.13 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | DOGE-USD | 14.04 | -0.10 | exit signal |
| 2026-10-25T16:00 | VWAP reversion · 1h | sell | SOL-USD | 25.16 | 0.03 | exit signal |
| 2026-10-25T16:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.96 | — | entry |
| 2026-10-25T16:00 | VWAP momentum · 1h | sell | BTC-USD | 6.96 | -0.04 | exit signal |
| 2026-10-25T16:00 | MACD cross · 1h | buy | SOL-USD | 9.30 | — | entry signal |
| 2026-10-25T16:00 | Three white soldiers | sell | BTC-USD | 19.72 | -0.13 | exit signal |
| 2026-10-25T15:40 | Three white soldiers | buy | BTC-USD | 19.86 | — | entry signal |
| 2026-10-25T15:40 | Volume breakout | buy | XRP-USD | 13.77 | — | entry signal |
| 2026-10-25T15:40 | Volume breakout | buy | ETH-USD | 13.77 | — | entry signal |
| 2026-10-25T15:40 | Donchian 55/20 | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-25T15:40 | ROC + volume | buy | XRP-USD | 14.14 | — | entry signal |
| 2026-10-25T15:40 | ROC + volume | buy | ETH-USD | 14.14 | — | entry signal |
| 2026-10-25T15:40 | EMA 20/50 cross | buy | XRP-USD | 2.57 | — | rebalance up |
| 2026-10-25T15:40 | EMA 20/50 cross | sell | ETH-USD | 2.57 | -0.01 | rebalance down |
| 2026-10-25T15:35 | ROC + volume | buy | DOGE-USD | 14.14 | — | entry signal |
| 2026-10-25T15:25 | Three white soldiers | sell | ETH-USD | 19.77 | -0.15 | exit signal |
| 2026-10-25T15:25 | Three white soldiers | sell | BTC-USD | 19.81 | -0.12 | exit signal |
| 2026-10-25T15:25 | Volume breakout | sell | BTC-USD | 13.71 | -0.08 | exit signal |
| 2026-10-25T15:25 | Squeeze breakout | sell | SOL-USD | 12.95 | -0.08 | stop-loss |
| 2026-10-25T15:25 | Squeeze breakout | sell | ETH-USD | 12.93 | -0.10 | stop-loss |
| 2026-10-25T15:25 | Squeeze breakout | sell | BTC-USD | 12.95 | -0.08 | stop-loss |
| 2026-10-25T15:25 | Donchian 55/20 | sell | BTC-USD | 12.99 | -0.10 | stop-loss |
| 2026-10-25T15:05 | Donchian 55/20 | buy | SOL-USD | 13.09 | — | entry signal |
| 2026-10-25T15:05 | Donchian 55/20 | buy | BTC-USD | 13.09 | — | entry signal |
| 2026-10-25T15:05 | ROC + volume | buy | SOL-USD | 14.14 | — | entry signal |
| 2026-10-25T15:05 | EMA 20/50 cross | buy | XRP-USD | 2.64 | — | entry signal |
| 2026-10-25T15:05 | EMA 20/50 cross | sell | DOGE-USD | 2.64 | 0.00 | rebalance down |
| 2026-10-25T15:00 | VWAP momentum · 1h | buy | BTC-USD | 7.00 | — | entry signal |
| 2026-10-25T15:00 | MACD cross · 1h | buy | ETH-USD | 10.47 | — | entry signal |
| 2026-10-25T15:00 | MACD cross · 1h | buy | DOGE-USD | 10.47 | — | entry signal |
| 2026-10-25T15:00 | MACD cross · 1h | buy | BTC-USD | 10.47 | — | entry signal |
| 2026-10-25T15:00 | EMA 20/50 cross | buy | SOL-USD | 12.80 | — | entry signal |
| 2026-10-25T15:00 | EMA 20/50 cross | buy | BTC-USD | 12.84 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 16:40:05.000119+00:00 -> 2026-10-25 16:50:05.000119+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
