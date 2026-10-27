# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T12:05:05.000153+00:00 · 37842 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 110, win rate 39.1%, fees £3.39, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 8962 decisions in 1799 calls, $0.1254 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T12:05 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-27T12:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T12:05 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.20 | +6.90% | 7 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 4 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.16 | 8.16 | 0 | — | 8.51 | 4.26 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.48 | 1.14 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.57 | 5.57 | 21 | 33.3 | 10.57 | 2.73 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.21 | 2.01 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.09 | -3.35 | -14.02 | 151 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.16 | 0.16 | 0 | — | 2.80 | 1.29 | -5.02 | 2 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.94 | -1.06 | 0 | — | -0.04 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 8.31 | 3.46 | -1.94 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -4.13 | -4.73 | -4.49 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -1.99 | -5.83 | 2 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.70 | -3.30 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.19 | -3.81 | 121 | 31.4 | -1.91 | -1.09 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.06 | -7.93 | 9 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 95.06 | -4.94 | 0 | — | -6.95 | -2.93 | -7.83 | 1 |
| 18 | Hold BTC | benchmark | 94.75 | -5.25 | 0 | — | 1.77 | 0.46 | -9.28 | 1 |
| 19 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 5.02 | 1.64 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.97 | -3.34 | -17.21 | 577 |
| 22 | Donchian 55/20 · 1h | breakout | 91.68 | -8.32 | 49 | 16.3 | -16.01 | -3.62 | -16.70 | 98 |
| 23 | Daily: Momentum burst | daily | 91.45 | -8.55 | 10 | 10.0 | -19.39 | -3.78 | -20.15 | 45 |
| 24 | Max aggression: 5-day momentum | meta | 91.28 | -8.72 | 11 | 45.5 | -15.58 | -1.42 | -27.80 | 25 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.16 | -16.91 | 2 |
| 26 | Squeeze breakout · 1h | breakout | 90.94 | -9.06 | 52 | 23.1 | -4.54 | -1.18 | -12.00 | 91 |
| 27 | Daily: Bullish score | daily | 90.71 | -9.29 | 11 | 18.2 | -6.77 | -0.82 | -14.40 | 16 |
| 28 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.89 | -6.82 | -12.54 | 214 |
| 29 | Parabolic SAR · 1h | trend | 89.96 | -10.04 | 121 | 25.6 | -21.91 | -5.59 | -22.00 | 247 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 89.45 | -10.55 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 31 | ADX DI cross · 1h | trend | 88.91 | -11.09 | 114 | 17.5 | -13.67 | -2.99 | -14.27 | 263 |
| 32 | Volume breakout · 1h | breakout | 88.63 | -11.37 | 104 | 23.1 | -14.40 | -3.04 | -16.13 | 112 |
| 33 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.03 | -3.27 | -14.77 | 95 |
| 34 | Stochastic reversion · 1h | reversion | 87.83 | -12.17 | 198 | 47.0 | -22.01 | -4.03 | -23.21 | 392 |
| 35 | Bollinger breakout · 1h | breakout | 87.24 | -12.76 | 109 | 26.6 | -14.34 | -2.87 | -17.92 | 239 |
| 36 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.53 | -4.11 | -17.87 | 704 |
| 37 | Keltner breakout · 1h | breakout | 85.62 | -14.38 | 74 | 23.0 | -20.89 | -4.12 | -23.13 | 183 |
| 38 | Connors RSI(2) · 1h | reversion | 85.11 | -14.89 | 174 | 40.2 | -26.47 | -7.95 | -26.96 | 198 |
| 39 | Z-score reversion · 1h | reversion | 84.87 | -15.13 | 116 | 33.6 | -14.56 | -2.39 | -21.48 | 211 |
| 40 | EMA 20/50 cross · 1h | trend | 84.31 | -15.69 | 73 | 11.0 | -21.88 | -4.32 | -23.33 | 130 |
| 41 | RSI momentum · 1h | momentum | 83.58 | -16.42 | 104 | 15.4 | -22.10 | -4.31 | -23.76 | 201 |
| 42 | Supertrend · 1h | trend | 82.97 | -17.03 | 114 | 14.0 | -27.65 | -5.91 | -28.20 | 223 |
| 43 | MACD cross · 1h | trend | 82.89 | -17.11 | 244 | 22.1 | -29.81 | -6.26 | -30.18 | 478 |
| 44 | MFI reversion · 1h | reversion | 82.66 | -17.34 | 263 | 31.6 | -16.45 | -2.54 | -20.54 | 153 |
| 45 | Ichimoku · 1h | trend | 82.25 | -17.75 | 68 | 11.8 | -21.80 | -4.56 | -24.73 | 109 |
| 46 | Triple EMA stack · 1h | trend | 81.68 | -18.32 | 101 | 14.9 | -29.46 | -5.87 | -30.81 | 203 |
| 47 | Bollinger reversion · 1h | reversion | 81.31 | -18.69 | 179 | 37.4 | -30.00 | -6.18 | -31.17 | 368 |
| 48 | Williams %R · 1h | reversion | 81.17 | -18.83 | 228 | 46.1 | -35.75 | -6.09 | -35.84 | 540 |
| 49 | CCI reversion · 1h | reversion | 81.16 | -18.84 | 222 | 44.6 | -25.83 | -3.72 | -28.06 | 466 |
| 50 | MACD zero-line · 1h | trend | 80.27 | -19.73 | 111 | 15.3 | -24.10 | -5.16 | -24.91 | 217 |
| 51 | Donchian 20/10 · 1h | breakout | 79.74 | -20.26 | 99 | 20.2 | -25.83 | -5.07 | -27.36 | 212 |
| 52 | OBV trend · 1h | momentum | 78.97 | -21.03 | 206 | 17.5 | -34.29 | -7.22 | -34.29 | 291 |
| 53 | Agent (ML meta-label) | meta | 78.88 | -21.12 | 924 | 19.4 | -8.33 | -1.38 | -15.84 | 359 |
| 54 | RSI(14) reversion · 1h | reversion | 78.28 | -21.72 | 100 | 24.0 | -17.65 | -2.83 | -24.48 | 208 |
| 55 | Three white soldiers | momentum | 78.20 | -21.80 | 307 | 19.2 | -43.97 | -20.15 | -44.41 | 601 |
| 56 | ROC + volume · 1h | momentum | 76.60 | -23.40 | 250 | 24.0 | -32.48 | -6.48 | -32.97 | 373 |
| 57 | Heikin-Ashi · 1h | trend | 76.52 | -23.48 | 290 | 22.1 | -45.03 | -10.35 | -45.06 | 657 |
| 58 | Candlestick reversal · 1h | reversion | 76.38 | -23.62 | 272 | 27.9 | -34.84 | -6.50 | -34.88 | 572 |
| 59 | EMA 9/21 cross · 1h | trend | 75.14 | -24.86 | 176 | 10.8 | -33.13 | -7.16 | -33.61 | 330 |
| 60 | VWAP momentum · 1h | momentum | 74.96 | -25.04 | 558 | 21.0 | -49.54 | -11.07 | -50.21 | 1239 |
| 61 | Max aggression: 1-day momentum | meta | 67.18 | -32.82 | 19 | 26.3 | -42.14 | -2.87 | -50.32 | 42 |
| 62 | ROC + volume | momentum | 54.79 | -45.21 | 764 | 22.1 | -74.01 | -25.92 | -74.16 | 1564 |
| 63 | Volume breakout | breakout | 53.59 | -46.41 | 462 | 12.8 | -62.76 | -26.08 | -63.01 | 801 |
| 64 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -43.69 | -98.89 | 5155 |
| 65 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.06 | -22.53 | -79.64 | 1426 |
| 66 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -43.83 | -93.74 | 2533 |
| 67 | Squeeze breakout | breakout | 50.44 | -49.56 | 599 | 14.2 | -67.66 | -28.53 | -68.14 | 1178 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.09 | -29.38 | -89.32 | 1929 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -36.48 | -91.47 | 2343 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.42 | -31.58 | -90.42 | 2158 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -51.58 | -97.89 | 3525 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.13 | -53.30 | -96.17 | 3379 |
| 73 | Donchian 55/20 | breakout | 50.36 | -49.64 | 616 | 19.5 | -72.02 | -23.18 | -72.59 | 1276 |
| 74 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.09 | -36.34 | -94.09 | 2442 |
| 75 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.39 | -32.89 | -82.58 | 1687 |
| 76 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -53.89 | -99.43 | 5788 |
| 77 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -40.52 | -92.82 | 2619 |
| 78 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.42 | -37.86 | -95.42 | 3361 |
| 79 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.80 | -99.78 | 6166 |
| 80 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -44.86 | -92.29 | 2336 |
| 81 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -59.84 | -97.74 | 3576 |
| 82 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -58.12 | -98.67 | 4807 |
| 83 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -53.94 | -94.54 | 2769 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.35 | -38.62 | -84.35 | 1809 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -65.76 | -99.61 | 6308 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -28.89 | -88.31 | 2231 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.04 | -19.30 | -77.38 | 1705 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.71 | -37.25 | -90.71 | 2288 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.29 | -47.65 | -96.30 | 3830 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.04 | -49.87 | -90.04 | 2138 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.15 | -17.95 | -76.40 | 1587 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.57 | -49.19 | -96.59 | 4208 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.09 | -99.92 | 8274 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T12:00 | VWAP momentum · 1h | sell | ETH-USD | 6.78 | -0.04 | exit signal |
| 2026-10-27T11:50 | ROC + volume | sell | SOL-USD | 13.64 | -0.08 | exit signal |
| 2026-10-27T11:45 | Donchian 55/20 | sell | XRP-USD | 12.49 | -0.13 | stop-loss |
| 2026-10-27T11:30 | Three white soldiers | sell | XRP-USD | 19.53 | -0.02 | exit signal |
| 2026-10-27T11:25 | Volume breakout | sell | SOL-USD | 13.35 | -0.11 | exit signal |
| 2026-10-27T11:20 | Volume breakout | sell | ETH-USD | 13.36 | -0.10 | exit signal |
| 2026-10-27T11:16 | Volume breakout | sell | BTC-USD | 13.39 | -0.08 | exit signal |
| 2026-10-27T11:05 | Donchian 55/20 | buy | XRP-USD | 12.62 | — | entry signal |
| 2026-10-27T11:00 | VWAP momentum · 1h | buy | XRP-USD | 6.38 | — | entry signal |
| 2026-10-27T11:00 | VWAP momentum · 1h | buy | ETH-USD | 6.82 | — | entry signal |
| 2026-10-27T11:00 | VWAP momentum · 1h | buy | BTC-USD | 6.82 | — | entry signal |
| 2026-10-27T11:00 | MACD cross · 1h | buy | XRP-USD | 4.88 | — | entry signal |
| 2026-10-27T11:00 | MACD cross · 1h | buy | BTC-USD | 4.88 | — | entry signal |
| 2026-10-27T10:50 | Volume breakout | buy | SOL-USD | 13.46 | — | entry signal |
| 2026-10-27T10:50 | Volume breakout | buy | ETH-USD | 13.46 | — | entry signal |
| 2026-10-27T10:50 | ROC + volume | buy | SOL-USD | 13.72 | — | entry signal |
| 2026-10-27T10:46 | Volume breakout | buy | BTC-USD | 13.47 | — | entry signal |
| 2026-10-27T10:35 | Three white soldiers | buy | XRP-USD | 19.56 | — | entry signal |
| 2026-10-27T10:00 | MACD zero-line · 1h | sell | XRP-USD | 20.15 | -0.01 | exit signal |
| 2026-10-27T10:00 | MACD cross · 1h | sell | XRP-USD | 4.52 | -0.01 | exit signal |
| 2026-10-27T10:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 8.30 | -0.06 | exit signal |
| 2026-10-27T08:50 | ROC + volume | sell | XRP-USD | 13.66 | -0.12 | exit signal |
| 2026-10-27T08:35 | Squeeze breakout | sell | XRP-USD | 12.52 | -0.11 | exit signal |
| 2026-10-27T08:35 | ROC + volume | sell | SOL-USD | 13.64 | -0.14 | stop-loss |
| 2026-10-27T08:30 | Volume breakout | sell | ETH-USD | 13.42 | -0.10 | exit signal |
| 2026-10-27T08:15 | Volume breakout | sell | SOL-USD | 13.39 | -0.12 | exit signal |
| 2026-10-27T08:00 | MACD cross · 1h | buy | ETH-USD | 5.18 | — | entry signal |
| 2026-10-27T07:55 | Volume breakout | buy | SOL-USD | 13.51 | — | entry signal |
| 2026-10-27T07:55 | Squeeze breakout | buy | XRP-USD | 12.64 | — | entry signal |
| 2026-10-27T07:55 | ROC + volume | buy | XRP-USD | 13.79 | — | entry signal |
| 2026-10-27T07:55 | ROC + volume | buy | SOL-USD | 13.79 | — | entry signal |
| 2026-10-27T07:50 | Volume breakout | buy | ETH-USD | 13.53 | — | entry signal |
| 2026-10-27T07:15 | Three white soldiers | sell | XRP-USD | 19.48 | -0.15 | exit signal |
| 2026-10-27T07:15 | Three white soldiers | sell | SOL-USD | 19.48 | -0.14 | exit signal |
| 2026-10-27T07:10 | Three white soldiers | buy | XRP-USD | 19.63 | — | entry signal |
| 2026-10-27T07:10 | Three white soldiers | buy | SOL-USD | 19.63 | — | entry signal |
| 2026-10-27T07:00 | Squeeze breakout · 1h | sell | XRP-USD | 22.48 | -0.32 | exit signal |
| 2026-10-27T07:00 | Bollinger breakout · 1h | sell | DOGE-USD | 21.57 | -0.10 | exit signal |
| 2026-10-27T07:00 | MACD cross · 1h | sell | ETH-USD | 4.82 | -0.07 | exit signal |
| 2026-10-27T07:00 | MACD cross · 1h | sell | DOGE-USD | 4.82 | -0.06 | exit signal |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
