# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T18:52:05.000140+00:00 · 65959 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.35 (-14.65%)

Closed trades 226, win rate 36.7%, fees £6.22, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 16.99 | -0.15 |
| SOXL | 16.68 | -0.45 |
| SQQQ | 17.48 | +0.42 |
| TSLA | 17.32 | +0.19 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-19 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, LRN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-18)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 33.12 · VIX 24.56 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 6.2, AMZN 6.2, TSLA 4.1, AMD 3.9, META 1.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 29952 decisions in 2943 calls, $0.3768 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T18:52 | 2 / 11 / 17 | cash |  |
| Breezy | 2026-11-19T18:52 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-19T18:52 | 4 / 22 / 4 | COIN 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| CCI reversion | SOXL | 2.51 | +21.97% | 16 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Stochastic reversion | TSLA | 1.98 | +4.51% | 13 |
| VWAP reversion | META | 1.90 | +2.79% | 4 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 120.53 | 20.53 | 25 | 64.0 | 29.27 | 4.67 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.16 | 14.16 | 0 | — | 11.74 | 3.91 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.32 | 3.32 | 0 | — | 3.82 | 1.16 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.23 | -3.79 | -4.99 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -3.26 | -0.62 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Agent (rotation) | meta | 95.77 | -4.23 | 210 | 28.6 | -0.98 | -0.27 | -7.49 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.63 | -5.37 | 0 | — | -5.47 | -1.80 | -7.96 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.19 | -6.81 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.22 | -7.78 | 8 | 50.0 | -7.53 | -0.56 | -18.69 | 6 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.79 | -9.21 | 0 | — | -9.86 | -2.79 | -12.73 | 1 |
| 18 | Copy: Insider buying | copy | 90.15 | -9.85 | 55 | 40.0 | -8.90 | -1.73 | -14.79 | 67 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.66 | -3.74 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 89.37 | -10.63 | 115 | 23.5 | -14.71 | -7.34 | -15.99 | 55 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.27 | -12.73 | 17 | 17.6 | -10.76 | -2.34 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.27 | -9.17 | -16.27 | 71 |
| 24 | Opening range 30m | breakout | 86.17 | -13.83 | 448 | 33.5 | -11.74 | -3.93 | -14.66 | 561 |
| 25 | Agent | meta | 85.35 | -14.65 | 226 | 36.7 | -14.30 | -6.68 | -17.14 | 207 |
| 26 | Agent (aggressive) | meta | 82.95 | -17.05 | 105 | 34.3 | -16.33 | -4.23 | -19.98 | 100 |
| 27 | Parabolic SAR · 1h | trend | 80.98 | -19.02 | 194 | 27.8 | -27.61 | -8.48 | -29.17 | 199 |
| 28 | Connors RSI(2) · 1h | reversion | 80.60 | -19.40 | 216 | 40.3 | -14.68 | -6.53 | -15.33 | 78 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.45 | -5.37 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -25.22 | -6.65 | -28.35 | 150 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -26.22 | -6.92 | -30.88 | 84 |
| 32 | Opening range 15m | breakout | 77.12 | -22.88 | 546 | 31.7 | -20.59 | -6.14 | -23.54 | 674 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 75.66 | -24.34 | 2 | 0.0 | -21.02 | -2.93 | -26.67 | 1 |
| 34 | Hold BTC | benchmark | 74.02 | -25.98 | 2 | 0.0 | -22.75 | -3.63 | -28.91 | 1 |
| 35 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -48.97 | -3.19 | -57.68 | 22 |
| 36 | Ichimoku · 1h | trend | 73.29 | -26.71 | 107 | 14.0 | -31.82 | -9.71 | -32.81 | 112 |
| 37 | ADX DI cross · 1h | trend | 72.92 | -27.08 | 225 | 20.0 | -29.88 | -4.77 | -36.82 | 279 |
| 38 | Stochastic reversion · 1h | reversion | 71.93 | -28.07 | 356 | 42.1 | -35.79 | -5.49 | -36.28 | 427 |
| 39 | Supertrend · 1h | trend | 70.55 | -29.45 | 195 | 16.9 | -33.42 | -5.60 | -40.05 | 206 |
| 40 | MFI reversion · 1h | reversion | 70.36 | -29.64 | 462 | 33.8 | -29.01 | -4.36 | -31.36 | 172 |
| 41 | Bollinger breakout · 1h | breakout | 70.01 | -29.99 | 195 | 21.5 | -33.87 | -8.87 | -36.62 | 218 |
| 42 | Triple EMA stack · 1h | trend | 69.97 | -30.03 | 161 | 14.3 | -32.44 | -6.94 | -38.93 | 171 |
| 43 | EMA 20/50 cross · 1h | trend | 69.60 | -30.40 | 118 | 10.2 | -37.82 | -8.31 | -44.85 | 122 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.38 | -4.99 | -37.91 | 31 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -30.45 | -6.10 | -36.31 | 206 |
| 46 | Heikin-Ashi · 1h | trend | 67.68 | -32.32 | 483 | 23.0 | -46.96 | -10.40 | -48.20 | 626 |
| 47 | CCI reversion · 1h | reversion | 67.58 | -32.42 | 397 | 42.1 | -42.00 | -7.02 | -44.29 | 481 |
| 48 | RSI momentum · 1h | momentum | 67.49 | -32.51 | 184 | 14.1 | -35.47 | -6.76 | -41.58 | 204 |
| 49 | OBV trend · 1h | momentum | 67.42 | -32.58 | 315 | 19.4 | -35.67 | -8.08 | -40.92 | 244 |
| 50 | MACD cross · 1h | trend | 65.82 | -34.17 | 427 | 21.8 | -43.29 | -7.09 | -49.07 | 493 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -41.74 | -2.62 | -57.50 | 39 |
| 52 | ROC + volume · 1h ⏸ | momentum | 64.82 | -35.18 | 431 | 27.6 | -39.92 | -6.99 | -44.41 | 342 |
| 53 | Donchian 20/10 · 1h | breakout | 64.61 | -35.39 | 165 | 17.6 | -37.01 | -7.20 | -43.04 | 191 |
| 54 | Bollinger reversion · 1h | reversion | 62.50 | -37.50 | 357 | 38.1 | -39.79 | -6.11 | -40.29 | 418 |
| 55 | Williams %R · 1h | reversion | 62.28 | -37.72 | 446 | 40.6 | -48.09 | -8.55 | -48.68 | 581 |
| 56 | EMA 9/21 cross · 1h | trend | 61.80 | -38.20 | 291 | 11.3 | -41.01 | -8.08 | -47.12 | 324 |
| 57 | Agent (ML meta-label) | meta | 59.07 | -40.93 | 1988 | 24.7 | -26.14 | -5.23 | -26.95 | 277 |
| 58 | RSI(14) reversion · 1h | reversion | 59.03 | -40.97 | 219 | 33.8 | -40.07 | -5.83 | -43.35 | 260 |
| 59 | Z-score reversion · 1h | reversion | 56.14 | -43.86 | 233 | 34.3 | -38.46 | -5.39 | -40.82 | 257 |
| 60 | Candlestick reversal · 1h | reversion | 55.73 | -44.27 | 573 | 27.1 | -48.70 | -9.10 | -49.35 | 654 |
| 61 | VWAP momentum · 1h | momentum | 54.62 | -45.38 | 1000 | 21.7 | -59.66 | -12.07 | -62.39 | 1201 |
| 62 | Three white soldiers | momentum | 52.98 | -47.02 | 608 | 14.3 | -51.66 | -23.04 | -51.66 | 668 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -48.45 | -99.13 | 5310 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.18 | -30.10 | -83.42 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.41 | -47.07 | -94.46 | 2473 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.54 | -35.21 | -90.59 | 1947 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.06 | -45.87 | -92.06 | 2299 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.53 | -30.57 | -90.58 | 2051 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.11 | -52.66 | -98.11 | 3476 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.75 | -53.91 | -96.77 | 3388 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -37.53 | -93.71 | 2202 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.74 | -35.90 | -83.76 | 1588 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.62 | -56.43 | -99.62 | 6172 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.85 | -46.66 | -92.85 | 2536 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.74 | -38.71 | -94.79 | 3186 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -75.75 | -99.83 | 6226 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.13 | -49.13 | -93.13 | 2269 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.11 | -26.48 | -78.16 | 1627 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.84 | -61.20 | -97.85 | 3399 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -59.51 | -99.10 | 5008 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.71 | -29.99 | -70.71 | 1225 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.91 | -57.80 | -94.91 | 2720 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.02 | -40.48 | -86.03 | 1723 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -73.44 | -99.71 | 6451 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.92 | -31.50 | -90.99 | 2397 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.21 | -19.36 | -80.34 | 1861 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.65 | -37.62 | -91.68 | 2181 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.70 | -47.99 | -97.72 | 3954 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.10 | -57.79 | -90.11 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.45 | -32.11 | -67.45 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.40 | -28.99 | -74.52 | 1207 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.98 | -18.81 | -82.02 | 1789 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.61 | -46.80 | -97.61 | 4360 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -117.82 | -99.94 | 8420 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T18:50 | ADX DI cross · 1h | buy | LABU | 3.73 | — | rebalance up |
| 2026-11-19T18:50 | Three white soldiers | sell | XRP-USD | 13.21 | -0.12 | exit signal |
| 2026-11-19T18:50 | Three white soldiers | sell | SOL-USD | 13.21 | -0.13 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | buy | XRP-USD | 5.68 | — | rebalance up |
| 2026-11-19T18:45 | Three white soldiers | buy | SOL-USD | 5.68 | — | rebalance up |
| 2026-11-19T18:45 | Three white soldiers | sell | UPRO | 7.54 | -0.05 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | sell | TNA | 7.57 | -0.06 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | sell | SPY | 7.60 | -0.02 | exit signal |
| 2026-11-19T18:45 | Three white soldiers | sell | IWM | 7.60 | -0.02 | exit signal |
| 2026-11-19T18:40 | ADX DI cross · 1h | buy | TSLA | 3.66 | — | rebalance up |
| 2026-11-19T18:40 | Three white soldiers | sell | NVDA | 7.61 | -0.02 | exit signal |
| 2026-11-19T18:35 | Three white soldiers | buy | UPRO | 7.59 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | buy | TNA | 7.63 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | buy | SPY | 7.63 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | buy | IWM | 7.63 | — | entry signal |
| 2026-11-19T18:35 | Three white soldiers | sell | XRP-USD | 5.69 | -0.03 | rebalance down |
| 2026-11-19T18:35 | Three white soldiers | sell | SOL-USD | 5.68 | -0.04 | rebalance down |
| 2026-11-19T18:35 | Three white soldiers | sell | NVDA | 5.73 | -0.01 | rebalance down |
| 2026-11-19T18:30 | Agent (ML meta-label) | sell | PLTR | 7.29 | -0.13 | selected signal exited |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | MSTR | 3.85 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | LABU | 3.95 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | ETHU | 4.00 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | buy | COIN | 3.71 | — | rebalance up |
| 2026-11-19T18:30 | CCI reversion · 1h | sell | SQQQ | 8.94 | 0.44 | exit signal |
| 2026-11-19T18:30 | Connors RSI(2) · 1h | buy | AMZN | 20.18 | — | entry signal |
| 2026-11-19T18:30 | Candlestick reversal · 1h | buy | SOL-USD | 7.01 | — | entry |
| 2026-11-19T18:30 | Candlestick reversal · 1h | sell | LABU | 6.14 | 0.04 | exit signal |
| 2026-11-19T18:30 | Candlestick reversal · 1h | sell | AAPL | 6.22 | -0.01 | exit signal |
| 2026-11-19T18:30 | RSI momentum · 1h | buy | SQQQ | 16.83 | — | entry signal |
| 2026-11-19T18:30 | VWAP momentum · 1h | buy | ETHU | 13.61 | — | entry signal |
| 2026-11-19T18:30 | VWAP momentum · 1h | buy | BITX | 13.73 | — | entry signal |
| 2026-11-19T18:30 | ADX DI cross · 1h | sell | PLTR | 14.43 | -0.15 | exit signal |
| 2026-11-19T18:30 | ADX DI cross · 1h | sell | AMZN | 14.37 | -0.14 | exit signal |
| 2026-11-19T18:30 | Supertrend · 1h | buy | SQQQ | 6.96 | — | rebalance up |
| 2026-11-19T18:30 | Supertrend · 1h | buy | SOL-USD | 7.53 | — | rebalance up |
| 2026-11-19T18:30 | Supertrend · 1h | buy | ETH-USD | 5.81 | — | rebalance up |
| 2026-11-19T18:30 | Supertrend · 1h | buy | BTC-USD | 7.54 | — | rebalance up |
| 2026-11-19T18:30 | Supertrend · 1h | sell | MSFT | 8.15 | -0.22 | exit signal |
| 2026-11-19T18:30 | Supertrend · 1h | sell | GOOGL | 9.83 | -0.30 | exit signal |
| 2026-11-19T18:30 | Supertrend · 1h | sell | AMZN | 9.86 | -0.11 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 18:52:05.000140+00:00 -> 2026-11-19 19:02:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 18:52:05.000140+00:00 -> 2026-11-19 19:02:05.000140+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
