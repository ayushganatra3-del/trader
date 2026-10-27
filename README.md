# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T11:35:05.000154+00:00 · 37820 ticks

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
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 8632 decisions in 1733 calls, $0.1207 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T11:35 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-27T11:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T11:35 | 3 / 1 / 1 | ETH-USD 64% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.20 | +6.90% | 7 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.32% | 4 |
| Candlestick reversal | LABU | 1.85 | +4.39% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.16 | 8.16 | 0 | — | 8.51 | 4.26 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.48 | 1.14 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.57 | 5.57 | 21 | 33.3 | 10.57 | 2.73 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.20 | 2.01 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.87 | -3.26 | -14.02 | 151 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.16 | 0.16 | 0 | — | 2.80 | 1.29 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.94 | -1.06 | 0 | — | -0.04 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 7.97 | 3.31 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -4.13 | -4.73 | -4.49 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -1.99 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.70 | -3.30 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.19 | -3.81 | 121 | 31.4 | -1.91 | -1.09 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.06 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 95.06 | -4.94 | 0 | — | -6.95 | -2.93 | -7.83 | 1 |
| 18 | Hold BTC | benchmark | 94.83 | -5.17 | 0 | — | 1.69 | 0.45 | -9.28 | 1 |
| 19 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 5.01 | 1.64 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.97 | -3.34 | -17.21 | 577 |
| 22 | Copy: Insider buying | copy | 92.32 | -7.68 | 27 | 37.0 | -20.47 | -4.05 | -22.94 | 61 |
| 23 | Donchian 55/20 · 1h | breakout | 91.68 | -8.32 | 49 | 16.3 | -16.01 | -3.62 | -16.70 | 98 |
| 24 | Daily: Momentum burst | daily | 91.45 | -8.55 | 10 | 10.0 | -19.39 | -3.78 | -20.15 | 40 |
| 25 | Max aggression: 5-day momentum | meta | 91.28 | -8.72 | 11 | 45.5 | -15.58 | -1.42 | -27.80 | 25 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.16 | -16.91 | 1 |
| 27 | Squeeze breakout · 1h | breakout | 90.94 | -9.06 | 52 | 23.1 | -4.54 | -1.18 | -12.00 | 91 |
| 28 | Daily: Bullish score | daily | 90.71 | -9.29 | 11 | 18.2 | -6.77 | -0.82 | -14.40 | 13 |
| 29 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.89 | -6.82 | -12.54 | 214 |
| 30 | Parabolic SAR · 1h | trend | 89.96 | -10.04 | 121 | 25.6 | -21.91 | -5.59 | -22.00 | 247 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.45 | -10.55 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 32 | ADX DI cross · 1h | trend | 88.91 | -11.09 | 114 | 17.5 | -13.55 | -2.96 | -14.27 | 263 |
| 33 | Volume breakout · 1h | breakout | 88.63 | -11.37 | 104 | 23.1 | -14.20 | -3.00 | -15.93 | 111 |
| 34 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.03 | -3.27 | -14.77 | 95 |
| 35 | Stochastic reversion · 1h | reversion | 87.85 | -12.15 | 198 | 47.0 | -21.87 | -4.01 | -23.11 | 392 |
| 36 | Bollinger breakout · 1h | breakout | 87.24 | -12.76 | 109 | 26.6 | -14.22 | -2.84 | -17.92 | 239 |
| 37 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.53 | -4.11 | -17.87 | 704 |
| 38 | Keltner breakout · 1h | breakout | 85.62 | -14.38 | 74 | 23.0 | -21.48 | -4.24 | -23.13 | 185 |
| 39 | Connors RSI(2) · 1h | reversion | 85.11 | -14.89 | 174 | 40.2 | -26.47 | -7.95 | -26.96 | 198 |
| 40 | Z-score reversion · 1h | reversion | 84.88 | -15.12 | 116 | 33.6 | -14.54 | -2.39 | -21.48 | 211 |
| 41 | EMA 20/50 cross · 1h | trend | 84.31 | -15.69 | 73 | 11.0 | -21.89 | -4.32 | -23.33 | 130 |
| 42 | RSI momentum · 1h | momentum | 83.58 | -16.42 | 104 | 15.4 | -22.10 | -4.31 | -23.76 | 201 |
| 43 | Supertrend · 1h | trend | 82.97 | -17.03 | 114 | 14.0 | -27.65 | -5.91 | -28.20 | 223 |
| 44 | MACD cross · 1h | trend | 82.90 | -17.10 | 244 | 22.1 | -29.78 | -6.25 | -30.18 | 478 |
| 45 | MFI reversion · 1h | reversion | 82.67 | -17.33 | 263 | 31.6 | -17.22 | -2.70 | -20.70 | 153 |
| 46 | Ichimoku · 1h | trend | 82.25 | -17.75 | 68 | 11.8 | -21.80 | -4.56 | -24.73 | 109 |
| 47 | Triple EMA stack · 1h | trend | 81.68 | -18.32 | 101 | 14.9 | -29.46 | -5.87 | -30.81 | 203 |
| 48 | Bollinger reversion · 1h | reversion | 81.31 | -18.69 | 179 | 37.4 | -29.91 | -6.16 | -31.08 | 368 |
| 49 | Williams %R · 1h | reversion | 81.18 | -18.82 | 228 | 46.1 | -35.51 | -6.07 | -35.62 | 540 |
| 50 | CCI reversion · 1h | reversion | 81.18 | -18.82 | 222 | 44.6 | -25.79 | -3.71 | -28.06 | 466 |
| 51 | MACD zero-line · 1h | trend | 80.27 | -19.73 | 111 | 15.3 | -24.50 | -5.26 | -24.91 | 218 |
| 52 | Donchian 20/10 · 1h | breakout | 79.76 | -20.24 | 99 | 20.2 | -26.09 | -5.11 | -27.66 | 213 |
| 53 | OBV trend · 1h | momentum | 78.97 | -21.03 | 206 | 17.5 | -34.26 | -7.22 | -34.26 | 291 |
| 54 | Agent (ML meta-label) | meta | 78.88 | -21.12 | 924 | 19.4 | -10.91 | -2.04 | -16.03 | 366 |
| 55 | RSI(14) reversion · 1h | reversion | 78.29 | -21.70 | 100 | 24.0 | -18.26 | -2.95 | -24.48 | 207 |
| 56 | Three white soldiers | momentum | 78.20 | -21.80 | 307 | 19.2 | -44.03 | -20.21 | -44.48 | 602 |
| 57 | ROC + volume · 1h | momentum | 76.60 | -23.40 | 250 | 24.0 | -32.34 | -6.44 | -33.05 | 373 |
| 58 | Heikin-Ashi · 1h | trend | 76.52 | -23.48 | 290 | 22.1 | -45.03 | -10.35 | -45.06 | 657 |
| 59 | Candlestick reversal · 1h | reversion | 76.38 | -23.62 | 272 | 27.9 | -34.89 | -6.51 | -35.03 | 573 |
| 60 | EMA 9/21 cross · 1h | trend | 75.14 | -24.86 | 176 | 10.8 | -33.13 | -7.16 | -33.61 | 330 |
| 61 | VWAP momentum · 1h | momentum | 74.99 | -25.02 | 557 | 21.0 | -49.63 | -11.11 | -50.30 | 1237 |
| 62 | Max aggression: 1-day momentum | meta | 67.18 | -32.82 | 19 | 26.3 | -42.14 | -2.87 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.82 | -45.18 | 763 | 22.1 | -74.21 | -26.16 | -74.36 | 1568 |
| 64 | Volume breakout | breakout | 53.59 | -46.41 | 462 | 12.8 | -62.69 | -26.14 | -62.94 | 799 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -43.55 | -98.88 | 5148 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.97 | -22.48 | -79.57 | 1425 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -43.89 | -93.73 | 2533 |
| 68 | Squeeze breakout | breakout | 50.44 | -49.56 | 599 | 14.2 | -67.64 | -28.50 | -68.12 | 1177 |
| 69 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.12 | -29.60 | -89.32 | 1930 |
| 70 | Donchian 55/20 | breakout | 50.41 | -49.59 | 615 | 19.5 | -71.99 | -23.15 | -72.56 | 1276 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -36.45 | -91.47 | 2343 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.49 | -31.47 | -90.49 | 2161 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -51.53 | -97.89 | 3525 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -53.00 | -96.16 | 3374 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.10 | -36.38 | -94.10 | 2438 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.38 | -32.85 | -82.58 | 1687 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -54.11 | -99.44 | 5789 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -40.39 | -92.80 | 2619 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.77 | -95.43 | 3363 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.41 | -99.78 | 6166 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.26 | -44.64 | -92.26 | 2336 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -59.73 | -97.73 | 3576 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -59.99 | -98.69 | 4812 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -53.92 | -94.55 | 2770 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.29 | -38.47 | -84.30 | 1809 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -65.94 | -99.61 | 6309 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -28.89 | -88.31 | 2231 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.02 | -19.29 | -77.36 | 1705 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.71 | -37.17 | -90.72 | 2289 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.32 | -48.22 | -96.32 | 3835 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.08 | -50.24 | -90.08 | 2141 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.32 | -18.09 | -76.44 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.58 | -49.25 | -96.59 | 4208 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.07 | -99.92 | 8273 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-27T07:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 20.87 | -0.24 | exit signal |
| 2026-10-27T06:20 | Squeeze breakout | sell | XRP-USD | 12.55 | -0.12 | exit signal |
| 2026-10-27T06:05 | Three white soldiers | sell | XRP-USD | 19.50 | -0.17 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 11:35:05.000154+00:00 -> 2026-10-27 11:45:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
