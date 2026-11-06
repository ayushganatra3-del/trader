# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T16:25:05.000138+00:00 · 49849 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.48 (-11.52%)

Closed trades 149, win rate 36.9%, fees £4.28, max drawdown -11.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 17.78 | +0.08 |

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

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 38.26 · VIX 28.18 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 18663 decisions in 2487 calls, $0.2436 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T16:25 | 7 / 22 / 2 | LABU 14% |  |
| Breezy | 2026-11-06T16:25 | 0 / 29 / 2 | cash |  |
| Boozy | 2026-11-06T16:25 | 6 / 24 / 1 | BITX 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.60 | 12.60 | 0 | — | 13.43 | 4.57 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.06 | 0.06 | 0 | — | 3.11 | 0.97 | -6.60 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.00 | 0.00 | 118 | 47.5 | -11.95 | -2.76 | -14.36 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.90 | -2.10 | 119 | 35.3 | 5.10 | 2.59 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Hold SPY | benchmark | 95.38 | -4.62 | 0 | — | -3.53 | -1.26 | -6.18 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 13 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Gap and go | momentum | 94.23 | -5.77 | 171 | 27.5 | -1.20 | -0.31 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 93.95 | -6.05 | 7 | 42.9 | -8.29 | -0.71 | -18.69 | 8 |
| 17 | Trend pullback · 1h | trend | 92.51 | -7.49 | 107 | 23.4 | -15.31 | -5.50 | -17.86 | 81 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.39 | -8.61 | 0 | — | -6.53 | -1.90 | -10.64 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 91.28 | -8.72 | 0 | — | -8.02 | -2.46 | -9.25 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.64 | -10.36 | 366 | 33.1 | -16.06 | -5.13 | -17.56 | 587 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.27 | -3.55 | -14.68 | 85 |
| 23 | Agent | meta | 88.48 | -11.52 | 149 | 36.9 | -14.12 | -7.51 | -14.62 | 212 |
| 24 | Hold BTC | benchmark | 88.37 | -11.63 | 1 | 0.0 | -5.74 | -0.74 | -14.09 | 1 |
| 25 | Daily: Bullish score | daily | 88.21 | -11.79 | 15 | 20.0 | -5.54 | -0.75 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 87.06 | -12.94 | 40 | 37.5 | -24.85 | -4.89 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.41 | -13.59 | 166 | 27.1 | -15.31 | -3.37 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.45 | -14.55 | 71 | 14.1 | -13.77 | -2.80 | -20.43 | 104 |
| 29 | Agent (aggressive) | meta | 84.44 | -15.56 | 72 | 30.6 | -18.37 | -5.45 | -19.08 | 100 |
| 30 | Max aggression: 5-day momentum | meta | 83.28 | -16.73 | 17 | 47.1 | -34.06 | -2.18 | -40.71 | 25 |
| 31 | Opening range 15m | breakout | 82.66 | -17.34 | 453 | 30.2 | -20.87 | -6.16 | -21.40 | 723 |
| 32 | Stochastic reversion · 1h | reversion | 82.14 | -17.86 | 260 | 46.9 | -25.83 | -3.78 | -29.25 | 392 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.71 | -3.67 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.04 | -18.96 | 204 | 40.2 | -20.48 | -6.76 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.58 | -24.50 | 172 |
| 36 | ADX DI cross · 1h | trend | 79.63 | -20.38 | 172 | 18.6 | -25.04 | -4.18 | -27.04 | 264 |
| 37 | MFI reversion · 1h | reversion | 79.21 | -20.79 | 329 | 34.0 | -19.50 | -2.54 | -22.82 | 154 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 79.14 | -20.86 | 2 | 0.0 | -13.43 | -1.80 | -24.16 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 78.00 | -22.00 | 166 | 23.5 | -23.34 | -4.84 | -27.04 | 247 |
| 40 | Ichimoku · 1h | trend | 77.68 | -22.32 | 94 | 14.9 | -23.50 | -4.79 | -29.43 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.26 | -22.74 | 286 | 46.2 | -30.17 | -4.90 | -31.70 | 462 |
| 42 | Heikin-Ashi · 1h | trend | 75.96 | -24.04 | 389 | 23.1 | -42.81 | -8.94 | -43.20 | 667 |
| 43 | EMA 20/50 cross · 1h | trend | 75.72 | -24.28 | 102 | 10.8 | -24.36 | -4.40 | -30.58 | 132 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.12 | -5.38 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.03 | -25.96 | 142 | 14.8 | -29.64 | -6.22 | -33.48 | 206 |
| 46 | MACD cross · 1h | trend | 73.59 | -26.41 | 334 | 23.1 | -36.05 | -6.36 | -38.81 | 477 |
| 47 | Supertrend · 1h | trend | 73.52 | -26.48 | 166 | 13.3 | -30.19 | -5.22 | -34.80 | 216 |
| 48 | Z-score reversion · 1h | reversion | 73.46 | -26.54 | 161 | 36.0 | -25.24 | -3.70 | -28.33 | 231 |
| 49 | RSI momentum · 1h | momentum | 73.35 | -26.65 | 158 | 12.7 | -28.19 | -5.34 | -32.60 | 219 |
| 50 | Bollinger reversion · 1h | reversion | 73.19 | -26.81 | 250 | 40.0 | -30.85 | -5.17 | -34.54 | 375 |
| 51 | Williams %R · 1h | reversion | 72.62 | -27.39 | 314 | 44.9 | -37.09 | -5.92 | -39.53 | 532 |
| 52 | Daily: Momentum burst | daily | 71.91 | -28.09 | 26 | 11.5 | -36.28 | -5.07 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.30 | -28.70 | 140 | 20.0 | -30.28 | -5.57 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 71.20 | -28.80 | 269 | 17.5 | -30.94 | -6.56 | -33.83 | 289 |
| 55 | ROC + volume · 1h | momentum | 70.09 | -29.91 | 345 | 25.5 | -37.89 | -7.41 | -37.89 | 380 |
| 56 | VWAP momentum · 1h | momentum | 67.59 | -32.41 | 763 | 22.3 | -55.97 | -12.37 | -56.18 | 1224 |
| 57 | EMA 9/21 cross · 1h | trend | 67.42 | -32.58 | 241 | 10.0 | -40.19 | -8.25 | -40.60 | 337 |
| 58 | Agent (ML meta-label) | meta | 66.70 | -33.30 | 1519 | 22.7 | -9.20 | -1.31 | -19.61 | 322 |
| 59 | RSI(14) reversion · 1h | reversion | 66.60 | -33.40 | 142 | 27.5 | -28.27 | -4.38 | -31.29 | 215 |
| 60 | Three white soldiers | momentum | 66.16 | -33.84 | 454 | 16.1 | -47.62 | -21.75 | -47.62 | 636 |
| 61 | Candlestick reversal · 1h | reversion | 65.50 | -34.50 | 401 | 28.7 | -37.93 | -6.90 | -38.72 | 563 |
| 62 | Max aggression: 1-day momentum | meta | 60.84 | -39.16 | 26 | 26.9 | -44.21 | -2.81 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -44.89 | -98.93 | 5160 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.48 | -25.63 | -80.72 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.39 | -47.03 | -93.42 | 2493 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.14 | -31.18 | -89.33 | 1904 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.79 | -39.45 | -90.87 | 2295 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.19 | -31.36 | -90.19 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -53.65 | -97.73 | 3445 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -58.25 | -96.25 | 3368 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.72 | -32.92 | -93.72 | 2434 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.12 | -36.74 | -82.32 | 1640 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -53.12 | -99.52 | 5953 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.64 | -43.38 | -92.68 | 2589 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -36.59 | -95.69 | 3407 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.43 | -99.80 | 6144 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.71 | -43.15 | -91.78 | 2254 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.59 | -26.99 | -75.60 | 1579 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -60.63 | -97.69 | 3480 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.79 | -59.55 | -98.79 | 4861 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.54 | -28.89 | -69.77 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -54.69 | -94.67 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.22 | -37.55 | -85.23 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.41 | -99.65 | 6338 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.26 | -31.03 | -89.29 | 2289 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.73 | -19.48 | -77.79 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.03 | -36.44 | -91.11 | 2233 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.61 | -51.16 | -96.62 | 3858 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -55.28 | -89.54 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.37 | -28.65 | -66.37 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.44 | -24.35 | -73.70 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.19 | -17.70 | -78.61 | 1660 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.32 | -97.28 | 4312 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.75 | -99.93 | 8243 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T16:21 | Agent (ML meta-label) | buy | DOGE-USD | 2.99 | — | entry |
| 2026-11-06T16:10 | Agent (ML meta-label) | sell | DOGE-USD | 2.99 | -0.03 | selected signal exited |
| 2026-11-06T16:10 | Gap and go | sell | TQQQ | 23.25 | -0.19 | exit signal |
| 2026-11-06T16:10 | Gap and go | sell | QQQ | 23.55 | -0.08 | exit signal |
| 2026-11-06T16:06 | Agent (ML meta-label) | buy | DOGE-USD | 3.02 | — | entry |
| 2026-11-06T16:00 | Agent | sell | DOGE-USD | 17.64 | -0.07 | selected signal exited |
| 2026-11-06T16:00 | Candlestick reversal · 1h | buy | BTC-USD | 6.56 | — | entry signal |
| 2026-11-06T16:00 | Candlestick reversal · 1h | sell | DOGE-USD | 5.56 | 0.15 | exit signal |
| 2026-11-06T16:00 | Bollinger breakout · 1h | buy | DOGE-USD | 19.52 | — | entry signal |
| 2026-11-06T16:00 | Opening range 15m | buy | PLTR | 7.49 | — | entry |
| 2026-11-06T16:00 | Opening range 15m | buy | META | 7.50 | — | entry |
| 2026-11-06T16:00 | Opening range 15m | buy | LABU | 7.50 | — | entry signal |
| 2026-11-06T16:00 | Opening range 15m | buy | AMZN | 7.50 | — | entry |
| 2026-11-06T16:00 | Opening range 15m | sell | UPRO | 4.35 | 0.00 | rebalance down |
| 2026-11-06T16:00 | Opening range 15m | sell | TSLA | 4.26 | 0.02 | rebalance down |
| 2026-11-06T16:00 | Opening range 15m | sell | TNA | 4.32 | 0.01 | rebalance down |
| 2026-11-06T16:00 | Opening range 15m | sell | SPY | 4.27 | -0.00 | rebalance down |
| 2026-11-06T16:00 | Opening range 15m | sell | MSFT | 4.27 | 0.01 | rebalance down |
| 2026-11-06T16:00 | Opening range 15m | sell | IWM | 4.26 | 0.00 | rebalance down |
| 2026-11-06T16:00 | Opening range 15m | sell | AAPL | 4.27 | 0.03 | rebalance down |
| 2026-11-06T15:55 | Agent | buy | DOGE-USD | 17.71 | — | following Candlestick reversal · 1h |
| 2026-11-06T15:55 | Gap and go | sell | AMD | 23.45 | -0.19 | exit signal |
| 2026-11-06T15:51 | Agent (ML meta-label) | sell | UPRO | 3.02 | 0.02 | selected signal exited |
| 2026-11-06T15:51 | OBV trend · 1h | sell | SQQQ | 17.92 | 0.19 | target is flat |
| 2026-11-06T15:51 | Opening range 30m | buy | META | 9.81 | — | entry signal |
| 2026-11-06T15:51 | Opening range 30m | buy | AMZN | 5.54 | — | rebalance up |
| 2026-11-06T15:51 | Opening range 30m | sell | TSLA | 5.02 | -0.04 | rebalance down |
| 2026-11-06T15:51 | Opening range 30m | sell | MSFT | 5.21 | 0.01 | rebalance down |
| 2026-11-06T15:51 | Opening range 30m | sell | IWM | 5.12 | -0.02 | rebalance down |
| 2026-11-06T15:51 | Gap and go | buy | TQQQ | 23.44 | — | entry signal |
| 2026-11-06T15:51 | Gap and go | buy | QQQ | 23.64 | — | entry signal |
| 2026-11-06T15:51 | Gap and go | buy | AMD | 23.64 | — | entry signal |
| 2026-11-06T15:45 | VWAP reversion · 1h | buy | NVDA | 24.97 | — | entry |
| 2026-11-06T15:45 | Opening range 30m | buy | AMZN | 7.25 | — | entry signal |
| 2026-11-06T15:45 | Opening range 30m | sell | TNA | 7.25 | -0.11 | rebalance down |
| 2026-11-06T15:40 | Agent (ML meta-label) | buy | UPRO | 2.99 | — | entry |
| 2026-11-06T15:35 | Opening range 15m | buy | UPRO | 4.23 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | TSLA | 4.60 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | TNA | 4.18 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | SPY | 4.17 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 16:25:05.000138+00:00 -> 2026-11-06 16:35:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 16:25:05.000138+00:00 -> 2026-11-06 16:35:05.000138+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 16:25:05.000138+00:00 -> 2026-11-06 16:35:05.000138+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
