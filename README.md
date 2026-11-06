# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T23:50:05.000153+00:00 · 50220 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.30 (-11.70%)

Closed trades 151, win rate 37.1%, fees £4.31, max drawdown -12.11%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.50 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 41136 decisions in 3600 calls, $0.5110 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T23:50 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-06T23:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T23:50 | 2 / 3 / 0 | ETH-USD 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.49 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.80 | -0.20 | 121 | 47.9 | -11.91 | -2.78 | -14.25 | 151 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.27 | -4.22 | -10.36 | 169 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.11 | -0.97 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.74 | -5.72 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.35 | -4.49 | -26.04 | 65 |
| 23 | Daily: Bullish score | daily | 88.76 | -11.23 | 15 | 20.0 | -5.00 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.25 | -3.57 | -14.68 | 86 |
| 25 | Hold BTC | benchmark | 88.66 | -11.34 | 1 | 0.0 | -5.30 | -0.68 | -14.09 | 1 |
| 26 | Agent | meta | 88.30 | -11.70 | 151 | 37.1 | -13.95 | -7.49 | -14.10 | 205 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -14.84 | -3.29 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.95 | -14.05 | 71 | 14.1 | -13.28 | -2.72 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.60 | -5.59 | -18.68 | 98 |
| 31 | Stochastic reversion · 1h | reversion | 82.11 | -17.89 | 260 | 46.9 | -25.99 | -3.85 | -29.25 | 394 |
| 32 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -17.03 | -3.86 | -21.73 | 101 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.68 | -24.50 | 173 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.37 | -20.63 | 175 | 18.3 | -25.07 | -4.21 | -27.04 | 262 |
| 38 | MFI reversion · 1h | reversion | 78.68 | -21.32 | 336 | 34.2 | -19.23 | -2.79 | -20.96 | 156 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.89 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.58 | -22.42 | 168 | 23.2 | -23.77 | -4.96 | -27.21 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.78 | -23.22 | 288 | 45.8 | -31.28 | -5.16 | -31.97 | 464 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -24.14 | -4.39 | -30.58 | 133 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.92 | -9.02 | -43.54 | 676 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.12 | -5.42 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -28.94 | -6.10 | -33.48 | 203 |
| 46 | Supertrend · 1h | trend | 73.63 | -26.37 | 166 | 13.3 | -30.76 | -5.36 | -34.80 | 217 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -28.61 | -5.48 | -32.60 | 220 |
| 48 | MACD cross · 1h | trend | 73.33 | -26.68 | 335 | 23.0 | -36.38 | -6.49 | -38.81 | 486 |
| 49 | Z-score reversion · 1h | reversion | 73.15 | -26.85 | 162 | 35.8 | -25.29 | -3.77 | -28.10 | 233 |
| 50 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 251 | 40.2 | -31.28 | -5.37 | -34.52 | 372 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -37.50 | -6.08 | -39.71 | 535 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.92 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.66 | -28.34 | 140 | 20.0 | -29.93 | -5.55 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -30.54 | -6.49 | -33.83 | 288 |
| 55 | ROC + volume · 1h | momentum | 69.84 | -30.16 | 347 | 25.4 | -38.18 | -7.48 | -38.41 | 383 |
| 56 | EMA 9/21 cross · 1h | trend | 67.31 | -32.69 | 242 | 9.9 | -40.28 | -8.36 | -40.52 | 337 |
| 57 | VWAP momentum · 1h | momentum | 67.17 | -32.83 | 777 | 22.1 | -55.92 | -12.38 | -55.93 | 1237 |
| 58 | Agent (ML meta-label) | meta | 66.40 | -33.60 | 1537 | 23.0 | -11.30 | -1.57 | -21.93 | 339 |
| 59 | RSI(14) reversion · 1h | reversion | 66.29 | -33.71 | 143 | 27.3 | -28.74 | -4.51 | -31.54 | 218 |
| 60 | Candlestick reversal · 1h | reversion | 65.48 | -34.52 | 407 | 28.5 | -38.40 | -7.13 | -38.91 | 573 |
| 61 | Three white soldiers | momentum | 65.40 | -34.60 | 460 | 15.9 | -48.29 | -22.59 | -48.33 | 641 |
| 62 | Max aggression: 1-day momentum | meta | 62.24 | -37.76 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -46.53 | -98.95 | 5232 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.76 | -25.74 | -80.76 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.55 | -47.83 | -93.55 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.30 | -32.28 | -89.31 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.91 | -40.37 | -90.92 | 2309 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.14 | -31.95 | -90.15 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -55.05 | -97.73 | 3481 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -58.23 | -96.32 | 3393 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.87 | -34.24 | -93.87 | 2450 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.66 | -36.15 | -82.66 | 1661 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -55.71 | -99.51 | 5979 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -44.42 | -92.77 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.71 | -38.23 | -95.71 | 3412 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.89 | -99.80 | 6202 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -43.94 | -91.93 | 2281 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.37 | -26.35 | -76.45 | 1593 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -63.66 | -97.75 | 3511 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -63.17 | -98.78 | 4884 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.02 | -29.72 | -70.19 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -56.07 | -94.75 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.19 | -38.25 | -85.24 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -75.60 | -99.64 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.18 | -31.75 | -89.27 | 2291 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.58 | -19.65 | -77.79 | 1740 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.12 | -37.88 | -91.15 | 2240 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.56 | -53.20 | -96.58 | 3875 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.57 | -57.43 | -89.59 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.49 | -29.39 | -66.49 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -24.78 | -73.54 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.08 | -17.82 | -78.60 | 1667 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -50.33 | -97.25 | 4329 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -121.09 | -99.93 | 8306 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T23:35 | Three white soldiers | buy | ETH-USD | 16.36 | — | entry signal |
| 2026-11-06T23:20 | Three white soldiers | buy | XRP-USD | 16.37 | — | entry signal |
| 2026-11-06T23:00 | Agent (ML meta-label) | buy | BTC-USD | 3.91 | — | entry |
| 2026-11-06T23:00 | Agent (ML meta-label) | sell | DOGE-USD | 3.88 | -0.03 | selected signal exited |
| 2026-11-06T23:00 | CCI reversion · 1h | sell | ETH-USD | 5.15 | -0.02 | exit signal |
| 2026-11-06T23:00 | Bollinger breakout · 1h | sell | DOGE-USD | 19.23 | -0.29 | exit signal |
| 2026-11-06T23:00 | ROC + volume · 1h | sell | SOL-USD | 17.33 | -0.28 | exit signal |
| 2026-11-06T23:00 | VWAP momentum · 1h | buy | ETH-USD | 6.11 | — | entry |
| 2026-11-06T23:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.41 | -0.04 | exit signal |
| 2026-11-06T23:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 16.66 | -0.22 | exit signal |
| 2026-11-06T22:45 | Three white soldiers | sell | XRP-USD | 16.31 | -0.09 | exit signal |
| 2026-11-06T22:00 | VWAP reversion · 1h | buy | XRP-USD | 24.97 | — | entry signal |
| 2026-11-06T21:55 | Three white soldiers | buy | XRP-USD | 16.40 | — | entry signal |
| 2026-11-06T21:00 | Agent (ML meta-label) | buy | DOGE-USD | 3.91 | — | following Candlestick reversal · 1h |
| 2026-11-06T21:00 | Bollinger breakout · 1h | sell | SOL-USD | 19.22 | -0.33 | exit signal |
| 2026-11-06T21:00 | ADX DI cross · 1h | sell | DOGE-USD | 19.74 | -0.24 | exit signal |
| 2026-11-06T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 94.10 | -1.21 | target is flat |
| 2026-11-06T20:55 | Agent (ML meta-label) | sell | DOGE-USD | 4.11 | -0.05 | selected signal exited |
| 2026-11-06T20:55 | MFI reversion · 1h | buy | GOOGL | 8.73 | — | entry |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | PLTR | 4.64 | -0.03 | target is flat |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | BITX | 7.17 | 0.01 | target is flat |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | AAPL | 6.03 | -0.03 | target is flat |
| 2026-11-06T20:55 | CCI reversion · 1h | buy | ETHU | 1.02 | — | entry |
| 2026-11-06T20:55 | CCI reversion · 1h | buy | COIN | 4.04 | — | entry |
| 2026-11-06T20:55 | CCI reversion · 1h | sell | XRP-USD | 5.06 | -0.08 | stop-loss |
| 2026-11-06T20:55 | Williams %R · 1h | buy | IWM | 4.52 | — | entry |
| 2026-11-06T20:55 | Williams %R · 1h | sell | XRP-USD | 5.40 | -0.14 | stop-loss |
| 2026-11-06T20:55 | RSI(14) reversion · 1h | buy | SOXL | 4.14 | — | entry |
| 2026-11-06T20:55 | RSI(14) reversion · 1h | sell | XRP-USD | 4.38 | -0.11 | stop-loss |
| 2026-11-06T20:55 | Candlestick reversal · 1h | buy | SOL-USD | 4.90 | — | entry |
| 2026-11-06T20:55 | Candlestick reversal · 1h | sell | QQQ | 4.67 | -0.02 | target is flat |
| 2026-11-06T20:55 | OBV trend · 1h | buy | AMZN | 17.75 | — | entry |
| 2026-11-06T20:55 | Opening range 30m | sell | TSLA | 12.80 | -0.07 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | TNA | 15.17 | 0.06 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | MSFT | 12.70 | -0.06 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | LABU | 15.00 | 0.16 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | IWM | 12.85 | 0.01 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | AAPL | 13.48 | -0.05 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | TSLA | 11.72 | -0.01 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 15m | sell | TNA | 11.69 | 0.08 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 23:50:05.000153+00:00 -> 2026-11-07 00:00:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 23:50:05.000153+00:00 -> 2026-11-07 00:00:05.000153+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 23:50:05.000153+00:00 -> 2026-11-07 00:00:05.000153+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
