# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T14:55:05.000182+00:00 · 49787 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.48 (-11.52%)

Closed trades 148, win rate 37.2%, fees £4.18, max drawdown -11.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 17.71 | +0.01 |

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

Today: 13032 decisions in 2301 calls, $0.1779 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T14:55 | 1 / 14 / 16 | NANC 22% |  |
| Breezy | 2026-11-06T14:55 | 0 / 29 / 2 | cash |  |
| Boozy | 2026-11-06T14:55 | 4 / 25 / 2 | COIN 69% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 110.93 | 10.93 | 0 | — | 11.72 | 3.93 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.05 | 0.61 | -9.64 | 29 |
| 5 | VWAP reversion · 1h | reversion | 100.33 | 0.33 | 112 | 44.6 | -11.97 | -2.79 | -14.24 | 150 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.65 | -0.35 | 0 | — | 2.66 | 0.84 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.00 | -2.00 | 118 | 34.7 | 5.18 | 2.63 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Gap and go | momentum | 95.84 | -4.16 | 162 | 29.0 | 0.48 | 0.25 | -9.18 | 226 |
| 12 | Hold SPY | benchmark | 95.49 | -4.51 | 0 | — | -3.44 | -1.23 | -6.18 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 14 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 94.69 | -5.30 | 7 | 42.9 | -7.59 | -0.61 | -18.69 | 8 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.43 | -7.57 | 106 | 22.6 | -15.39 | -5.54 | -17.86 | 81 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.44 | -8.56 | 0 | — | -6.51 | -1.90 | -10.64 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 91.30 | -8.70 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.25 | -3.55 | -14.68 | 86 |
| 23 | Agent | meta | 88.48 | -11.52 | 148 | 37.2 | -14.19 | -7.56 | -14.62 | 212 |
| 24 | Hold BTC | benchmark | 88.32 | -11.69 | 1 | 0.0 | -5.54 | -0.71 | -13.78 | 1 |
| 25 | Daily: Bullish score | daily | 88.00 | -12.00 | 15 | 20.0 | -5.75 | -0.78 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 86.99 | -13.01 | 40 | 37.5 | -25.09 | -4.95 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.23 | -13.77 | 166 | 27.1 | -15.51 | -3.41 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.26 | -14.74 | 71 | 14.1 | -13.97 | -2.84 | -20.43 | 104 |
| 29 | Agent (aggressive) | meta | 84.28 | -15.72 | 72 | 30.6 | -18.54 | -5.52 | -19.08 | 100 |
| 30 | Opening range 15m | breakout | 83.28 | -16.72 | 446 | 30.7 | -20.20 | -5.97 | -21.31 | 717 |
| 31 | Stochastic reversion · 1h | reversion | 83.09 | -16.91 | 260 | 46.9 | -25.17 | -3.61 | -29.25 | 386 |
| 32 | Max aggression: 5-day momentum | meta | 82.56 | -17.44 | 17 | 47.1 | -34.65 | -2.23 | -40.71 | 25 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 144 | 27.8 | -17.25 | -3.88 | -21.73 | 101 |
| 34 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.64 | -24.50 | 173 |
| 35 | Connors RSI(2) · 1h | reversion | 80.82 | -19.18 | 204 | 40.2 | -20.70 | -6.85 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.02 | -19.98 | 2 | 0.0 | -12.48 | -1.63 | -24.16 | 1 |
| 37 | MFI reversion · 1h | reversion | 79.36 | -20.64 | 328 | 33.8 | -19.15 | -2.50 | -22.55 | 155 |
| 38 | ADX DI cross · 1h | trend | 79.35 | -20.65 | 171 | 18.1 | -25.28 | -4.23 | -27.04 | 263 |
| 39 | Bollinger breakout · 1h | breakout | 78.20 | -21.80 | 166 | 23.5 | -23.14 | -4.80 | -26.61 | 245 |
| 40 | Ichimoku · 1h | trend | 77.51 | -22.49 | 94 | 14.9 | -23.67 | -4.82 | -29.43 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.18 | -22.82 | 286 | 46.2 | -30.26 | -4.92 | -31.42 | 452 |
| 42 | EMA 20/50 cross · 1h | trend | 75.59 | -24.41 | 102 | 10.8 | -24.58 | -4.44 | -30.58 | 133 |
| 43 | Heikin-Ashi · 1h | trend | 75.56 | -24.44 | 388 | 22.9 | -43.65 | -9.18 | -43.65 | 670 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.12 | -5.38 | -29.20 | 210 |
| 45 | Z-score reversion · 1h | reversion | 73.99 | -26.01 | 160 | 35.6 | -24.49 | -3.51 | -28.32 | 225 |
| 46 | Triple EMA stack · 1h | trend | 73.88 | -26.12 | 142 | 14.8 | -29.96 | -6.29 | -33.47 | 206 |
| 47 | MACD cross · 1h | trend | 73.69 | -26.31 | 334 | 23.1 | -36.13 | -6.38 | -38.81 | 475 |
| 48 | Bollinger reversion · 1h | reversion | 73.37 | -26.62 | 249 | 39.8 | -30.72 | -5.13 | -34.52 | 375 |
| 49 | Supertrend · 1h | trend | 73.29 | -26.71 | 166 | 13.3 | -31.16 | -5.43 | -34.80 | 218 |
| 50 | Williams %R · 1h | reversion | 73.17 | -26.83 | 314 | 44.9 | -36.71 | -5.75 | -39.70 | 529 |
| 51 | RSI momentum · 1h | momentum | 73.12 | -26.88 | 158 | 12.7 | -28.43 | -5.38 | -32.60 | 219 |
| 52 | Daily: Momentum burst | daily | 71.75 | -28.25 | 26 | 11.5 | -36.42 | -5.10 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.28 | -28.72 | 140 | 20.0 | -30.31 | -5.57 | -34.66 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 268 | 17.2 | -31.14 | -6.62 | -33.72 | 290 |
| 55 | ROC + volume · 1h | momentum | 70.47 | -29.53 | 345 | 25.5 | -37.55 | -7.35 | -37.55 | 379 |
| 56 | VWAP momentum · 1h | momentum | 67.37 | -32.63 | 762 | 22.3 | -56.20 | -12.42 | -56.20 | 1216 |
| 57 | EMA 9/21 cross · 1h | trend | 67.21 | -32.79 | 241 | 10.0 | -40.10 | -8.25 | -40.24 | 335 |
| 58 | Agent (ML meta-label) | meta | 66.84 | -33.16 | 1512 | 22.5 | -9.13 | -1.26 | -22.48 | 336 |
| 59 | RSI(14) reversion · 1h | reversion | 66.70 | -33.30 | 142 | 27.5 | -28.20 | -4.36 | -31.29 | 205 |
| 60 | Three white soldiers | momentum | 66.21 | -33.79 | 453 | 16.1 | -47.63 | -21.79 | -47.64 | 637 |
| 61 | Candlestick reversal · 1h | reversion | 65.60 | -34.40 | 398 | 28.4 | -38.56 | -7.09 | -39.24 | 566 |
| 62 | Max aggression: 1-day momentum | meta | 60.32 | -39.68 | 26 | 26.9 | -44.70 | -2.85 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.01 | -98.95 | 5148 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.44 | -25.67 | -80.49 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -48.11 | -93.43 | 2495 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.05 | -30.91 | -89.16 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.68 | -39.24 | -90.73 | 2288 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.10 | -30.99 | -90.16 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.67 | -52.87 | -97.72 | 3440 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -60.08 | -96.22 | 3361 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -32.74 | -93.67 | 2433 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.82 | -36.48 | -81.82 | 1631 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -52.85 | -99.52 | 5946 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.55 | -43.13 | -92.65 | 2591 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.71 | -36.83 | -95.71 | 3403 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.01 | -99.80 | 6133 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.59 | -42.56 | -91.60 | 2248 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.94 | -26.54 | -75.26 | 1572 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -61.32 | -97.68 | 3481 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -59.03 | -98.78 | 4850 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.25 | -28.20 | -69.98 | 1201 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -53.79 | -94.61 | 2739 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -36.65 | -84.96 | 1775 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.58 | -99.65 | 6325 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.15 | -30.86 | -89.20 | 2281 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.64 | -19.40 | -77.75 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.06 | -36.32 | -91.13 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.60 | -51.02 | -96.61 | 3850 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -55.05 | -89.48 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.68 | -27.88 | -66.10 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.28 | -24.24 | -73.41 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.69 | -17.87 | -78.73 | 1664 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -48.52 | -97.28 | 4308 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.17 | -99.93 | 8221 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T14:55 | VWAP reversion · 1h | sell | TSLA | 12.58 | 0.18 | target is flat |
| 2026-11-06T14:55 | Gap and go | buy | TECL | 2.15 | — | entry |
| 2026-11-06T14:55 | Gap and go | buy | SOXL | 13.69 | — | entry |
| 2026-11-06T14:55 | Gap and go | sell | NVDA | 15.84 | -0.06 | exit signal |
| 2026-11-06T14:50 | Agent (ML meta-label) | sell | NVDA | 5.36 | 0.24 | selected signal exited |
| 2026-11-06T14:50 | ROC + volume · 1h | sell | SQQQ | 17.51 | -0.35 | stop-loss |
| 2026-11-06T14:50 | Three white soldiers | buy | SPY | 16.55 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | UPRO | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | TQQQ | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | TNA | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | TECL | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | SPY | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | SOXL | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | QQQ | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | PLTR | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | IWM | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | COIN | 7.61 | — | entry signal |
| 2026-11-06T14:50 | Opening range 15m | buy | AMD | 7.61 | — | entry signal |
| 2026-11-06T14:45 | Day trade: Stocks in Play ORB | sell | SQQQ | 24.32 | -0.12 | target is flat |
| 2026-11-06T14:45 | Agent (ML meta-label) | buy | TSLA | 4.45 | — | entry |
| 2026-11-06T14:45 | Agent (ML meta-label) | sell | MSFT | 5.01 | -0.12 | selected signal exited |
| 2026-11-06T14:45 | Agent (aggressive) | buy | AMZN | 42.12 | — | following OBV trend |
| 2026-11-06T14:45 | Agent | buy | AMZN | 17.69 | — | following OBV trend |
| 2026-11-06T14:45 | Copy: Cathie Wood (ARKK) | buy | ARKK | 80.06 | — | entry |
| 2026-11-06T14:45 | Trend pullback · 1h | sell | MSFT | 22.64 | -0.47 | stop-loss |
| 2026-11-06T14:45 | Gap and go | buy | TSLA | 15.89 | — | entry signal |
| 2026-11-06T14:45 | Gap and go | buy | NVDA | 15.90 | — | entry signal |
| 2026-11-06T14:45 | Gap and go | sell | TQQQ | 7.96 | 0.02 | rebalance down |
| 2026-11-06T14:45 | Gap and go | sell | QQQ | 7.90 | 0.00 | rebalance down |
| 2026-11-06T14:45 | Gap and go | sell | PLTR | 8.03 | 0.05 | rebalance down |
| 2026-11-06T14:45 | Gap and go | sell | AMD | 7.89 | 0.00 | rebalance down |
| 2026-11-06T14:40 | Day trade: Stocks in Play ORB | buy | UPRO | 24.44 | — | entry |
| 2026-11-06T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 24.44 | — | entry |
| 2026-11-06T14:40 | Day trade: Stocks in Play ORB | buy | SPY | 24.44 | — | entry |
| 2026-11-06T14:40 | Day trade: Stocks in Play ORB | buy | NVDA | 24.44 | — | entry |
| 2026-11-06T14:40 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 105.83 | -1.98 | target is flat |
| 2026-11-06T14:40 | Bollinger reversion · 1h | sell | NVDA | 5.18 | 0.03 | take-profit |
| 2026-11-06T14:40 | Keltner breakout · 1h | sell | SQQQ | 20.19 | -0.14 | stop-loss |
| 2026-11-06T14:40 | Bollinger breakout · 1h | sell | SQQQ | 19.50 | -0.14 | stop-loss |
| 2026-11-06T14:40 | Gap and go | buy | TQQQ | 23.79 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 14:55:05.000182+00:00 -> 2026-11-06 15:05:05.000182+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 14:55:05.000182+00:00 -> 2026-11-06 15:05:05.000182+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 14:55:05.000182+00:00 -> 2026-11-06 15:05:05.000182+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
