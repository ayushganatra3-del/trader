# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T10:10:05.000149+00:00 · 36531 ticks

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

Today: 7575 decisions in 1518 calls, $0.1060 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T10:10 | 0 / 3 / 1 | cash |  |
| Breezy | 2026-10-26T10:10 | 0 / 4 / 0 | cash |  |
| Boozy | 2026-10-26T10:10 | 3 / 1 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Bollinger reversion | BITX | 2.12 | +2.39% | 13 |
| VWAP momentum | PLTR | 1.73 | +4.99% | 6 |
| Stochastic reversion | BITX | 1.67 | +3.43% | 12 |
| RSI(14) reversion | TSLA | 1.52 | +3.64% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.71 | 6.71 | 0 | — | 7.97 | 3.95 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 2.30 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.01 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.03 | 1.03 | 0 | — | 3.44 | 1.81 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -10.94 | -2.98 | -13.74 | 153 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 5.84 | 2.80 | -1.76 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 98.04 | -1.96 | 0 | — | -0.72 | -0.41 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.01 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.20 | -3.80 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 192 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.89 | -4.11 | 0 | — | -0.88 | -0.38 | -5.99 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.27 | -4.73 | 0 | — | 1.30 | 0.55 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.74 | -5.26 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.35 | -5.65 | 25 | 40.0 | -16.03 | -3.05 | -21.73 | 58 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.81 | -6.19 | 95 | 23.2 | -21.52 | -6.94 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.20 | -6.80 | 48 | 16.7 | -15.03 | -3.38 | -15.99 | 96 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.21 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Daily: Momentum burst | daily | 91.89 | -8.11 | 10 | 10.0 | -17.52 | -3.70 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.60 | -8.40 | 119 | 25.2 | -23.06 | -5.68 | -23.76 | 253 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.06 | -0.72 | -11.55 | 91 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.18 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.39 | -9.61 | 112 | 17.9 | -12.65 | -2.57 | -15.15 | 260 |
| 30 | Daily: Bullish score | daily | 89.74 | -10.26 | 9 | 0.0 | -8.04 | -1.00 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.85 | -2.85 | -17.00 | 114 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 89.34 | -10.66 | 0 | — | -5.31 | -0.75 | -14.52 | 1 |
| 33 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.76 | -7.81 | -12.35 | 206 |
| 34 | Bollinger breakout · 1h | breakout | 88.79 | -11.21 | 106 | 27.4 | -12.35 | -2.41 | -16.41 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.36 | -12.64 | 186 | 45.2 | -20.97 | -3.94 | -22.47 | 392 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.57 | -4.29 | -14.77 | 93 |
| 37 | Keltner breakout · 1h | breakout | 86.36 | -13.64 | 73 | 23.3 | -23.30 | -4.88 | -25.03 | 191 |
| 38 | EMA 20/50 cross · 1h | trend | 86.23 | -13.78 | 71 | 11.3 | -23.05 | -4.69 | -23.35 | 136 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.44 | -17.87 | 703 |
| 40 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 41 | RSI momentum · 1h | momentum | 85.38 | -14.62 | 102 | 15.7 | -22.48 | -4.86 | -22.89 | 214 |
| 42 | Supertrend · 1h | trend | 84.55 | -15.45 | 113 | 14.2 | -26.24 | -5.76 | -27.09 | 215 |
| 43 | Ichimoku · 1h | trend | 83.96 | -16.04 | 65 | 12.3 | -24.15 | -5.05 | -24.49 | 109 |
| 44 | Triple EMA stack · 1h | trend | 83.64 | -16.36 | 98 | 15.3 | -28.01 | -5.69 | -28.19 | 211 |
| 45 | Z-score reversion · 1h | reversion | 83.49 | -16.51 | 113 | 33.6 | -15.77 | -2.66 | -21.48 | 206 |
| 46 | MACD cross · 1h | trend | 83.19 | -16.82 | 233 | 22.3 | -25.79 | -5.32 | -27.61 | 465 |
| 47 | MFI reversion · 1h | reversion | 81.64 | -18.36 | 262 | 31.7 | -17.45 | -2.79 | -20.71 | 150 |
| 48 | OBV trend · 1h | momentum | 81.27 | -18.73 | 203 | 17.2 | -31.62 | -6.89 | -32.91 | 303 |
| 49 | MACD zero-line · 1h | trend | 81.20 | -18.80 | 106 | 15.1 | -22.10 | -4.59 | -25.51 | 219 |
| 50 | Williams %R · 1h | reversion | 81.10 | -18.90 | 213 | 44.1 | -35.26 | -6.25 | -35.99 | 536 |
| 51 | Donchian 20/10 · 1h | breakout | 80.92 | -19.08 | 98 | 19.4 | -24.47 | -4.69 | -27.35 | 217 |
| 52 | Bollinger reversion · 1h | reversion | 80.36 | -19.64 | 171 | 34.5 | -30.25 | -6.17 | -31.39 | 374 |
| 53 | CCI reversion · 1h | reversion | 79.88 | -20.12 | 205 | 42.0 | -26.54 | -3.95 | -28.08 | 467 |
| 54 | Three white soldiers | momentum | 79.30 | -20.70 | 289 | 19.0 | -44.39 | -20.35 | -44.39 | 596 |
| 55 | Agent (ML meta-label) | meta | 79.25 | -20.75 | 881 | 18.6 | -17.98 | -3.51 | -20.46 | 344 |
| 56 | Heikin-Ashi · 1h | trend | 78.00 | -22.00 | 279 | 22.9 | -43.68 | -10.04 | -44.10 | 658 |
| 57 | ROC + volume · 1h | momentum | 77.93 | -22.07 | 241 | 23.7 | -29.92 | -5.89 | -31.53 | 378 |
| 58 | Candlestick reversal · 1h | reversion | 76.91 | -23.09 | 265 | 27.9 | -34.36 | -6.45 | -34.70 | 563 |
| 59 | RSI(14) reversion · 1h | reversion | 76.82 | -23.18 | 99 | 23.2 | -15.55 | -2.87 | -24.48 | 197 |
| 60 | EMA 9/21 cross · 1h | trend | 76.33 | -23.67 | 169 | 11.2 | -31.62 | -6.49 | -34.40 | 327 |
| 61 | VWAP momentum · 1h | momentum | 75.35 | -24.65 | 532 | 20.9 | -50.96 | -11.65 | -51.32 | 1238 |
| 62 | Max aggression: 1-day momentum | meta | 67.55 | -32.45 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.76 | -44.24 | 726 | 22.0 | -74.95 | -27.33 | -74.96 | 1555 |
| 64 | Volume breakout | breakout | 54.47 | -45.53 | 444 | 12.4 | -62.61 | -26.08 | -62.64 | 787 |
| 65 | Donchian 55/20 | breakout | 51.69 | -48.31 | 581 | 18.9 | -72.05 | -23.72 | -72.05 | 1262 |
| 66 | Squeeze breakout | breakout | 51.35 | -48.65 | 577 | 13.7 | -67.58 | -28.69 | -67.58 | 1169 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -45.41 | -98.92 | 5145 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.49 | -23.49 | -79.55 | 1427 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.97 | -46.09 | -93.99 | 2535 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -30.58 | -89.34 | 1916 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.50 | -38.14 | -91.53 | 2333 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.67 | -30.82 | -90.67 | 2172 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -53.76 | -97.93 | 3531 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -59.00 | -96.22 | 3368 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.16 | -35.71 | -94.22 | 2471 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.99 | -35.25 | -83.07 | 1698 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -55.41 | -99.44 | 5790 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -42.12 | -92.65 | 2610 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.88 | -95.50 | 3381 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -80.62 | -99.78 | 6187 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.42 | -44.70 | -92.43 | 2349 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -64.01 | -97.72 | 3565 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.72 | -61.53 | -98.72 | 4814 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -55.83 | -94.63 | 2776 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.30 | -39.26 | -84.31 | 1792 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -67.82 | -99.62 | 6291 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.46 | -29.52 | -88.49 | 2243 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.81 | -19.74 | -77.86 | 1704 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.87 | -37.79 | -90.87 | 2279 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -48.93 | -96.41 | 3826 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.03 | -51.10 | -90.04 | 2127 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.28 | -17.83 | -76.37 | 1596 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.50 | -48.87 | -96.51 | 4195 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -102.73 | -99.92 | 8257 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T10:00 | Agent (ML meta-label) | sell | DOGE-USD | 4.64 | -0.03 | selected signal exited |
| 2026-10-26T10:00 | Z-score reversion · 1h | buy | ETH-USD | 8.11 | — | entry |
| 2026-10-26T10:00 | Z-score reversion · 1h | sell | BTC-USD | 7.58 | 0.00 | exit signal |
| 2026-10-26T10:00 | Parabolic SAR · 1h | buy | BTC-USD | 22.92 | — | entry signal |
| 2026-10-26T10:00 | MACD cross · 1h | buy | SOL-USD | 9.26 | — | entry signal |
| 2026-10-26T10:00 | MACD cross · 1h | buy | ETH-USD | 9.26 | — | entry signal |
| 2026-10-26T10:00 | MACD cross · 1h | sell | DOGE-USD | 4.59 | -0.02 | rebalance down |
| 2026-10-26T09:55 | Agent (ML meta-label) | buy | DOGE-USD | 4.66 | — | entry |
| 2026-10-26T09:50 | Donchian 55/20 | buy | SOL-USD | 12.94 | — | entry signal |
| 2026-10-26T09:40 | ROC + volume | sell | XRP-USD | 13.91 | -0.07 | exit signal |
| 2026-10-26T09:20 | Donchian 55/20 | buy | DOGE-USD | 12.95 | — | entry signal |
| 2026-10-26T09:20 | ROC + volume | buy | DOGE-USD | 13.98 | — | entry signal |
| 2026-10-26T09:20 | ROC + volume | buy | BTC-USD | 13.98 | — | entry signal |
| 2026-10-26T09:00 | MFI reversion · 1h | buy | BTC-USD | 20.28 | — | entry signal |
| 2026-10-26T09:00 | MACD cross · 1h | buy | BTC-USD | 11.88 | — | entry signal |
| 2026-10-26T08:50 | Donchian 55/20 | buy | ETH-USD | 12.95 | — | entry signal |
| 2026-10-26T08:40 | Donchian 55/20 | buy | BTC-USD | 12.96 | — | entry signal |
| 2026-10-26T08:40 | ROC + volume | buy | XRP-USD | 13.99 | — | entry signal |
| 2026-10-26T08:40 | ROC + volume | buy | SOL-USD | 13.99 | — | entry signal |
| 2026-10-26T07:15 | Agent (ML meta-label) | sell | DOGE-USD | 4.37 | -0.03 | selected signal exited |
| 2026-10-26T07:05 | Agent (ML meta-label) | buy | DOGE-USD | 4.40 | — | entry |
| 2026-10-26T06:25 | Donchian 55/20 | sell | DOGE-USD | 12.87 | -0.12 | stop-loss |
| 2026-10-26T06:10 | Squeeze breakout | sell | DOGE-USD | 12.79 | -0.07 | stop-loss |
| 2026-10-26T06:10 | Squeeze breakout | sell | BTC-USD | 12.81 | -0.05 | exit signal |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | XRP-USD | 5.09 | -0.05 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | SOL-USD | 12.62 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | ETH-USD | 12.62 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | DOGE-USD | 10.11 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-26T06:10 | EMA 20/50 cross | sell | BTC-USD | 10.13 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-26T06:00 | Z-score reversion · 1h | buy | BTC-USD | 6.37 | — | rebalance up |
| 2026-10-26T06:00 | Z-score reversion · 1h | sell | DOGE-USD | 6.90 | -0.08 | exit signal |
| 2026-10-26T06:00 | VWAP momentum · 1h | buy | BTC-USD | 6.83 | — | entry signal |
| 2026-10-26T06:00 | MACD cross · 1h | buy | DOGE-USD | 13.86 | — | entry signal |
| 2026-10-26T05:40 | EMA 20/50 cross | buy | XRP-USD | 5.13 | — | entry signal |
| 2026-10-26T05:40 | EMA 20/50 cross | sell | DOGE-USD | 2.55 | -0.01 | rebalance down |
| 2026-10-26T05:40 | EMA 20/50 cross | sell | BTC-USD | 2.54 | -0.01 | rebalance down |
| 2026-10-26T05:25 | EMA 20/50 cross | buy | ETH-USD | 12.73 | — | entry signal |
| 2026-10-26T05:10 | Donchian 55/20 | buy | DOGE-USD | 12.99 | — | entry |
| 2026-10-26T05:10 | EMA 20/50 cross | buy | SOL-USD | 12.73 | — | entry signal |
| 2026-10-26T05:00 | CCI reversion · 1h | buy | BTC-USD | 3.35 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 10:10:05.000149+00:00 -> 2026-10-26 10:20:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
