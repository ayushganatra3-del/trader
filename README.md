# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-19T17:54:05.000146+00:00 · 65902 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.52 (-14.48%)

Closed trades 226, win rate 36.7%, fees £6.22, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 17.19 | +0.04 |
| SOXL | 16.93 | -0.20 |
| SQQQ | 17.18 | +0.11 |
| TSLA | 17.36 | +0.23 |

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

Today: 24795 decisions in 2772 calls, $0.3164 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-19T17:54 | 0 / 19 / 12 | cash |  |
| Breezy | 2026-11-19T17:54 | 0 / 26 / 5 | cash |  |
| Boozy | 2026-11-19T17:54 | 2 / 28 / 1 | COIN 62% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 118.44 | 18.45 | 25 | 64.0 | 26.63 | 4.62 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 113.72 | 13.72 | 0 | — | 11.02 | 3.78 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.47 | 3.47 | 0 | — | 4.29 | 1.22 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -3.88 | -3.45 | -4.83 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -3.56 | -0.69 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | 1.17 | 0.45 | -9.06 | 212 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 11 | Agent (rotation) | meta | 95.19 | -4.81 | 210 | 28.6 | -0.80 | -0.22 | -6.81 | 151 |
| 12 | Hold SPY | benchmark | 95.00 | -5.00 | 0 | — | -5.04 | -1.66 | -7.93 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.78 | -5.44 | 20 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 93.45 | -6.55 | 8 | 50.0 | -6.05 | -0.43 | -18.69 | 6 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.13 | -6.87 | 0 | — | -6.89 | -1.81 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.43 | -7.90 | -9.74 | 22 |
| 17 | Copy: Insider buying | copy | 91.05 | -8.95 | 52 | 40.4 | -9.18 | -1.80 | -14.79 | 67 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.89 | -9.11 | 0 | — | -9.64 | -2.73 | -12.67 | 1 |
| 19 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.67 | -3.74 | -18.48 | 149 |
| 20 | Trend pullback · 1h | trend | 88.97 | -11.03 | 115 | 23.5 | -14.98 | -7.40 | -15.90 | 55 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.11 | -12.89 | 17 | 17.6 | -10.37 | -2.34 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.27 | -9.17 | -16.27 | 71 |
| 24 | Opening range 30m | breakout | 85.77 | -14.23 | 448 | 33.5 | -12.11 | -4.11 | -14.66 | 561 |
| 25 | Agent | meta | 85.52 | -14.48 | 226 | 36.7 | -14.06 | -6.55 | -17.06 | 206 |
| 26 | Agent (aggressive) | meta | 83.56 | -16.44 | 105 | 34.3 | -15.85 | -4.11 | -19.98 | 100 |
| 27 | Connors RSI(2) · 1h | reversion | 80.71 | -19.29 | 216 | 40.3 | -14.55 | -6.46 | -15.33 | 77 |
| 28 | Parabolic SAR · 1h | trend | 80.62 | -19.38 | 194 | 27.8 | -28.23 | -8.70 | -29.47 | 199 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.45 | -5.37 | -21.50 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -25.45 | -6.73 | -28.32 | 151 |
| 31 | Donchian 55/20 · 1h | breakout | 78.55 | -21.45 | 79 | 12.7 | -25.89 | -6.79 | -30.74 | 84 |
| 32 | Opening range 15m | breakout | 76.76 | -23.24 | 546 | 31.7 | -20.93 | -6.23 | -23.54 | 674 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 76.09 | -23.91 | 2 | 0.0 | -20.20 | -2.86 | -26.57 | 1 |
| 34 | Hold BTC | benchmark | 73.95 | -26.05 | 2 | 0.0 | -22.64 | -3.63 | -28.91 | 1 |
| 35 | Max aggression: 5-day momentum ⏸ | meta | 73.75 | -26.25 | 22 | 40.9 | -49.19 | -3.20 | -57.68 | 22 |
| 36 | ADX DI cross · 1h | trend | 73.12 | -26.88 | 223 | 19.7 | -29.39 | -4.70 | -36.71 | 279 |
| 37 | Ichimoku · 1h | trend | 72.96 | -27.04 | 107 | 14.0 | -32.56 | -9.89 | -33.26 | 111 |
| 38 | Stochastic reversion · 1h | reversion | 72.38 | -27.62 | 356 | 42.1 | -35.43 | -5.43 | -36.60 | 427 |
| 39 | Supertrend · 1h | trend | 70.61 | -29.39 | 192 | 16.7 | -33.27 | -5.57 | -40.05 | 206 |
| 40 | MFI reversion · 1h | reversion | 70.45 | -29.55 | 462 | 33.8 | -28.68 | -4.30 | -31.13 | 172 |
| 41 | Bollinger breakout · 1h | breakout | 70.01 | -29.99 | 195 | 21.5 | -33.88 | -8.87 | -36.62 | 218 |
| 42 | Triple EMA stack · 1h | trend | 69.97 | -30.03 | 159 | 14.5 | -31.84 | -6.62 | -38.64 | 175 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.41 | -4.99 | -37.91 | 31 |
| 44 | EMA 20/50 cross · 1h | trend | 69.23 | -30.77 | 118 | 10.2 | -37.85 | -8.38 | -44.64 | 123 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -30.47 | -6.11 | -36.32 | 208 |
| 46 | CCI reversion · 1h | reversion | 67.79 | -32.21 | 396 | 41.9 | -41.82 | -6.97 | -44.29 | 481 |
| 47 | Heikin-Ashi · 1h | trend | 67.68 | -32.32 | 483 | 23.0 | -47.04 | -10.41 | -48.27 | 626 |
| 48 | RSI momentum · 1h | momentum | 67.55 | -32.45 | 183 | 14.2 | -35.46 | -6.79 | -41.42 | 203 |
| 49 | OBV trend · 1h | momentum | 67.12 | -32.88 | 315 | 19.4 | -35.61 | -8.10 | -40.61 | 246 |
| 50 | MACD cross · 1h | trend | 66.27 | -33.73 | 427 | 21.8 | -42.75 | -7.00 | -49.07 | 492 |
| 51 | Max aggression: 1-day momentum ⏸ | meta | 65.56 | -34.44 | 33 | 27.3 | -40.84 | -2.54 | -57.50 | 39 |
| 52 | ROC + volume · 1h | momentum | 65.50 | -34.50 | 428 | 27.8 | -38.96 | -6.91 | -43.86 | 342 |
| 53 | Donchian 20/10 · 1h | breakout | 64.61 | -35.39 | 165 | 17.6 | -36.82 | -7.17 | -42.86 | 191 |
| 54 | Williams %R · 1h | reversion | 62.72 | -37.28 | 446 | 40.6 | -47.64 | -8.43 | -48.59 | 577 |
| 55 | Bollinger reversion · 1h | reversion | 62.52 | -37.48 | 357 | 38.1 | -39.88 | -6.13 | -40.42 | 418 |
| 56 | EMA 9/21 cross · 1h | trend | 61.91 | -38.09 | 288 | 11.5 | -41.02 | -8.07 | -47.14 | 325 |
| 57 | Agent (ML meta-label) | meta | 59.21 | -40.79 | 1987 | 24.7 | -20.05 | -3.24 | -21.19 | 284 |
| 58 | RSI(14) reversion · 1h | reversion | 59.12 | -40.88 | 219 | 33.8 | -41.03 | -6.10 | -43.36 | 265 |
| 59 | Z-score reversion · 1h | reversion | 56.83 | -43.17 | 232 | 34.5 | -37.57 | -5.24 | -40.70 | 257 |
| 60 | Candlestick reversal · 1h | reversion | 55.78 | -44.22 | 571 | 27.0 | -48.45 | -8.99 | -49.22 | 653 |
| 61 | VWAP momentum · 1h | momentum | 54.77 | -45.23 | 1000 | 21.7 | -59.02 | -12.01 | -61.89 | 1204 |
| 62 | Three white soldiers | momentum | 53.62 | -46.38 | 599 | 14.5 | -51.17 | -23.22 | -51.21 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -48.11 | -99.10 | 5306 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.20 | -30.10 | -83.43 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.43 | -46.14 | -94.46 | 2480 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.58 | -35.50 | -90.62 | 1948 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.03 | -45.34 | -92.04 | 2298 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.66 | -30.56 | -90.67 | 2059 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.10 | -53.03 | -98.10 | 3466 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.77 | -53.56 | -96.79 | 3405 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -38.05 | -93.72 | 2203 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.75 | -35.84 | -83.77 | 1589 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.90 | -99.62 | 6157 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.87 | -46.26 | -92.87 | 2540 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.75 | -38.72 | -94.79 | 3190 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -76.17 | -99.83 | 6208 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.05 | -49.62 | -93.05 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.12 | -26.17 | -78.15 | 1654 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -61.06 | -97.83 | 3408 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.09 | -59.00 | -99.09 | 5005 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.60 | -29.89 | -70.60 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.93 | -57.22 | -94.93 | 2729 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.11 | -40.46 | -86.11 | 1731 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -72.76 | -99.71 | 6449 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -31.17 | -90.99 | 2396 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.04 | -19.17 | -80.37 | 1859 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.59 | -37.20 | -91.68 | 2173 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.69 | -47.86 | -97.71 | 3955 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.08 | -57.80 | -90.08 | 2178 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.49 | -32.17 | -67.49 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.37 | -28.87 | -74.52 | 1211 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.00 | -18.77 | -82.19 | 1787 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -46.16 | -97.61 | 4359 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.54 | -99.94 | 8423 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-19T17:45 | Three white soldiers | sell | BITX | 13.29 | -0.19 | stop-loss |
| 2026-11-19T17:41 | Agent (ML meta-label) | sell | TECL | 1.38 | -0.02 | selected signal exited |
| 2026-11-19T17:35 | Agent (ML meta-label) | buy | TECL | 1.40 | — | entry |
| 2026-11-19T17:35 | Agent (ML meta-label) | sell | AMZN | 1.40 | 0.00 | selected signal exited |
| 2026-11-19T17:35 | Three white soldiers | buy | DOGE-USD | 13.48 | — | entry signal |
| 2026-11-19T17:35 | Three white soldiers | buy | BITX | 13.48 | — | entry signal |
| 2026-11-19T17:30 | Agent (ML meta-label) | buy | AMZN | 1.40 | — | entry |
| 2026-11-19T17:30 | Williams %R · 1h | buy | TNA | 3.95 | — | entry signal |
| 2026-11-19T17:30 | Williams %R · 1h | buy | MSTR | 3.95 | — | entry signal |
| 2026-11-19T17:30 | Williams %R · 1h | buy | IWM | 3.95 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | MSTR | 6.20 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | IWM | 6.23 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | BITX | 6.23 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | buy | AAPL | 6.23 | — | entry signal |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | LABU | 5.03 | 0.10 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | ETHU | 5.03 | 0.04 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | ETH-USD | 3.09 | -0.02 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | COIN | 5.09 | 0.08 | rebalance down |
| 2026-11-19T17:30 | Candlestick reversal · 1h | sell | BTC-USD | 4.87 | -0.03 | rebalance down |
| 2026-11-19T17:30 | OBV trend · 1h | buy | SQQQ | 16.72 | — | entry signal |
| 2026-11-19T17:30 | ROC + volume · 1h | buy | GOOGL | 16.48 | — | entry signal |
| 2026-11-19T17:30 | ROC + volume · 1h | buy | AMZN | 16.48 | — | entry signal |
| 2026-11-19T17:30 | VWAP momentum · 1h | buy | SQQQ | 13.67 | — | entry signal |
| 2026-11-19T17:30 | VWAP momentum · 1h | buy | COIN | 13.67 | — | entry signal |
| 2026-11-19T17:30 | Trend pullback · 1h | buy | SQQQ | 22.16 | — | entry signal |
| 2026-11-19T17:30 | Heikin-Ashi · 1h | sell | MSFT | 16.92 | -0.15 | exit signal |
| 2026-11-19T17:30 | Heikin-Ashi · 1h | sell | GOOGL | 16.85 | -0.22 | exit signal |
| 2026-11-19T17:30 | Heikin-Ashi · 1h | sell | AMZN | 17.37 | 0.14 | exit signal |
| 2026-11-19T17:30 | Ichimoku · 1h | buy | SQQQ | 18.18 | — | entry signal |
| 2026-11-19T17:30 | ADX DI cross · 1h | buy | SQQQ | 14.61 | — | entry signal |
| 2026-11-19T17:30 | ADX DI cross · 1h | sell | NVDA | 14.61 | 0.02 | exit signal |
| 2026-11-19T17:30 | Parabolic SAR · 1h | buy | SQQQ | 20.09 | — | entry signal |
| 2026-11-19T17:30 | Parabolic SAR · 1h | sell | AMZN | 19.96 | 0.00 | exit signal |
| 2026-11-19T17:26 | Agent (aggressive) | buy | SOXL | 42.02 | — | following CCI reversion, Z-score reversion |
| 2026-11-19T17:26 | Agent | buy | SOXL | 17.13 | — | following CCI reversion, Z-score reversion |
| 2026-11-19T17:26 | MFI reversion · 1h | buy | BITX | 10.09 | — | entry |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | SOXL | 3.47 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | PLTR | 3.08 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | MSTR | 3.10 | — | rebalance up |
| 2026-11-19T17:20 | Agent (ML meta-label) | buy | LABU | 3.11 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-21 17:54:05.000146+00:00 -> 2026-11-19 18:04:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-21 17:54:05.000146+00:00 -> 2026-11-19 18:04:05.000146+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
