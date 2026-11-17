# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T16:38:05.000099+00:00 · 63371 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £83.67 (-16.33%)

Closed trades 207, win rate 36.2%, fees £5.88, max drawdown -16.71%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 16.68 | -0.11 |
| SOXL | 33.05 | -0.32 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 20799 decisions in 2622 calls, $0.2698 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T16:38 | 8 / 17 / 5 | cash |  |
| Breezy | 2026-11-17T16:38 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-17T16:38 | 6 / 23 / 1 | COIN 52% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.55% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| MFI reversion | BITX | 2.16 | +2.33% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.19 | 17.20 | 0 | — | 13.04 | 4.34 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.04 | 12.04 | 24 | 62.5 | 17.47 | 3.51 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.38 | 3.38 | 0 | — | 5.83 | 1.60 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.43 | 1.43 | 36 | 41.7 | 0.07 | 0.14 | -9.64 | 33 |
| 6 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.63 | 2.12 | -9.06 | 224 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -2.71 | -2.27 | -4.31 | 71 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.78 | -4.22 | 8 | 50.0 | -3.35 | -0.05 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.29 | -4.71 | 0 | — | -3.85 | -1.22 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.24 | -5.76 | 197 | 29.9 | -1.44 | -0.44 | -8.15 | 159 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.95 | -8.05 | 0 | — | -8.67 | -2.26 | -8.69 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 18 | Copy: Insider buying | copy | 90.95 | -9.05 | 47 | 42.6 | -9.54 | -1.89 | -14.79 | 62 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.06 | -9.94 | 0 | — | -8.58 | -2.31 | -12.67 | 1 |
| 21 | Daily: Bullish score | daily | 87.61 | -12.39 | 17 | 17.6 | -3.40 | -0.47 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -12.24 | -5.30 | -15.83 | 71 |
| 24 | Opening range 30m | breakout | 86.51 | -13.49 | 438 | 33.6 | -9.57 | -3.02 | -14.11 | 575 |
| 25 | Agent | meta | 83.67 | -16.33 | 207 | 36.2 | -17.29 | -7.09 | -17.65 | 206 |
| 26 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.32 | -7.19 | -28.08 | 203 |
| 27 | Keltner breakout · 1h | breakout | 81.41 | -18.59 | 121 | 25.6 | -17.33 | -3.60 | -26.47 | 157 |
| 28 | Max aggression: 5-day momentum | meta | 81.30 | -18.70 | 21 | 42.9 | -47.10 | -3.06 | -55.24 | 22 |
| 29 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.47 | -6.39 | -14.87 | 94 |
| 30 | Agent (aggressive) | meta | 80.32 | -19.68 | 99 | 33.3 | -18.87 | -4.98 | -19.41 | 97 |
| 31 | Volume breakout · 1h | breakout | 80.07 | -19.93 | 162 | 28.4 | -15.75 | -4.98 | -22.00 | 81 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.40 | -6.63 | -29.47 | 84 |
| 33 | Opening range 15m | breakout | 78.41 | -21.59 | 533 | 31.5 | -16.38 | -4.37 | -21.37 | 686 |
| 34 | Max aggression: 1-day momentum | meta | 77.99 | -22.01 | 30 | 26.7 | -22.97 | -0.83 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 76.04 | -23.96 | 2 | 0.0 | -15.86 | -1.97 | -26.43 | 1 |
| 36 | ADX DI cross · 1h | trend | 75.40 | -24.60 | 208 | 19.2 | -27.18 | -4.33 | -35.66 | 260 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.19 | -8.47 | -29.80 | 111 |
| 38 | Hold BTC | benchmark | 74.68 | -25.32 | 2 | 0.0 | -15.48 | -2.17 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 74.03 | -25.97 | 188 | 21.8 | -25.63 | -5.54 | -33.01 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 72.45 | -27.55 | 344 | 42.7 | -35.13 | -5.30 | -36.09 | 424 |
| 41 | Supertrend · 1h | trend | 71.52 | -28.48 | 187 | 16.0 | -31.72 | -5.37 | -38.72 | 202 |
| 42 | Triple EMA stack · 1h | trend | 71.31 | -28.69 | 155 | 14.8 | -30.05 | -6.02 | -36.18 | 187 |
| 43 | RSI momentum · 1h | momentum | 71.22 | -28.78 | 176 | 14.2 | -30.71 | -5.56 | -37.27 | 199 |
| 44 | MACD zero-line · 1h | trend | 71.06 | -28.94 | 180 | 17.8 | -26.43 | -5.23 | -32.79 | 199 |
| 45 | EMA 20/50 cross · 1h | trend | 70.14 | -29.86 | 115 | 10.4 | -36.05 | -9.92 | -39.00 | 114 |
| 46 | MFI reversion · 1h | reversion | 70.13 | -29.87 | 423 | 34.0 | -26.41 | -3.80 | -30.29 | 166 |
| 47 | Heikin-Ashi · 1h | trend | 69.93 | -30.07 | 466 | 23.0 | -41.26 | -8.28 | -44.59 | 633 |
| 48 | ROC + volume · 1h | momentum | 69.71 | -30.29 | 408 | 28.2 | -28.93 | -4.70 | -37.96 | 354 |
| 49 | MACD cross · 1h | trend | 69.45 | -30.55 | 412 | 22.1 | -35.20 | -5.16 | -44.40 | 476 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.64 | -31.36 | 306 | 19.0 | -35.26 | -7.53 | -39.92 | 261 |
| 52 | Donchian 20/10 · 1h | breakout | 67.48 | -32.52 | 159 | 18.2 | -30.71 | -5.14 | -39.11 | 206 |
| 53 | CCI reversion · 1h | reversion | 66.20 | -33.80 | 382 | 41.6 | -41.94 | -6.88 | -44.29 | 460 |
| 54 | Bollinger reversion · 1h | reversion | 64.19 | -35.81 | 344 | 37.8 | -38.98 | -5.90 | -39.95 | 407 |
| 55 | EMA 9/21 cross · 1h | trend | 63.23 | -36.77 | 280 | 11.1 | -40.50 | -8.09 | -45.77 | 320 |
| 56 | Williams %R · 1h | reversion | 62.57 | -37.44 | 429 | 40.8 | -46.22 | -7.86 | -46.56 | 550 |
| 57 | Agent (ML meta-label) | meta | 60.18 | -39.82 | 1885 | 24.5 | -21.87 | -3.75 | -26.03 | 319 |
| 58 | RSI(14) reversion · 1h | reversion | 58.39 | -41.61 | 205 | 31.7 | -41.86 | -6.20 | -42.95 | 242 |
| 59 | Z-score reversion · 1h | reversion | 57.12 | -42.88 | 224 | 35.3 | -37.58 | -5.19 | -39.23 | 244 |
| 60 | VWAP momentum · 1h | momentum | 57.07 | -42.93 | 957 | 21.6 | -53.48 | -9.58 | -58.20 | 1200 |
| 61 | Three white soldiers | momentum | 55.42 | -44.58 | 581 | 14.6 | -49.80 | -22.16 | -49.87 | 663 |
| 62 | Candlestick reversal · 1h | reversion | 54.49 | -45.51 | 546 | 26.6 | -48.31 | -8.69 | -48.41 | 618 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.87 | -99.02 | 5270 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.70 | -25.61 | -82.02 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.07 | -43.12 | -94.07 | 2500 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.29 | -31.73 | -90.35 | 1945 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -38.42 | -91.32 | 2302 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.84 | -30.52 | -89.84 | 2125 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -46.84 | -97.90 | 3446 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -53.95 | -96.56 | 3432 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.59 | -37.59 | -93.65 | 2234 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.98 | -32.11 | -83.06 | 1619 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.89 | -99.60 | 6072 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.95 | -40.78 | -92.00 | 2561 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.14 | -37.71 | -95.15 | 3328 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -65.20 | -99.80 | 6141 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.23 | -41.90 | -92.23 | 2248 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.12 | -26.18 | -76.21 | 1654 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -56.98 | -97.64 | 3456 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.03 | -54.96 | -99.04 | 4950 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.34 | -26.81 | -68.46 | 1224 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.54 | -52.78 | -94.57 | 2732 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.34 | -36.83 | -84.39 | 1737 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -65.02 | -99.70 | 6401 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.83 | -30.19 | -90.83 | 2356 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.45 | -18.27 | -79.75 | 1839 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.19 | -35.04 | -91.26 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.58 | -45.20 | -97.59 | 3938 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -59.29 | -89.54 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.14 | -29.92 | -66.14 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.97 | -22.80 | -72.51 | 1233 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.67 | -17.76 | -80.81 | 1757 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -45.15 | -97.63 | 4364 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.03 | -99.94 | 8399 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T16:35 | Agent (ML meta-label) | buy | SPY | 15.05 | — | entry |
| 2026-11-17T16:35 | Agent (ML meta-label) | sell | SQQQ | 15.14 | 0.12 | selected signal exited |
| 2026-11-17T16:30 | Williams %R · 1h | buy | SOXL | 6.10 | — | entry signal |
| 2026-11-17T16:30 | Williams %R · 1h | buy | QQQ | 10.48 | — | entry signal |
| 2026-11-17T16:30 | Williams %R · 1h | buy | NVDA | 10.48 | — | entry signal |
| 2026-11-17T16:30 | Williams %R · 1h | buy | AMD | 10.48 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | UPRO | 3.82 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | TQQQ | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | TECL | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | SPY | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | QQQ | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | PLTR | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | MSTR | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | ETHU | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | TSLA | 3.76 | 0.01 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | SOXL | 4.24 | 0.09 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | NVDA | 3.87 | 0.03 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | GOOGL | 3.71 | -0.00 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | COIN | 3.74 | -0.04 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | BITX | 3.78 | -0.04 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | AMZN | 3.68 | -0.02 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | AAPL | 3.69 | -0.00 | rebalance down |
| 2026-11-17T16:30 | Candlestick reversal · 1h | buy | TECL | 13.57 | — | entry signal |
| 2026-11-17T16:30 | Candlestick reversal · 1h | buy | SOXL | 13.74 | — | entry signal |
| 2026-11-17T16:30 | Candlestick reversal · 1h | buy | NVDA | 13.74 | — | entry signal |
| 2026-11-17T16:30 | Candlestick reversal · 1h | sell | BITX | 13.69 | -0.35 | exit signal |
| 2026-11-17T16:30 | VWAP momentum · 1h | sell | AAPL | 14.37 | -0.06 | exit signal |
| 2026-11-17T16:30 | ADX DI cross · 1h | sell | AAPL | 18.63 | -0.13 | exit signal |
| 2026-11-17T16:30 | EMA 20/50 cross · 1h | sell | AMD | 16.77 | -0.86 | exit signal |
| 2026-11-17T16:25 | Agent | buy | BITX | 16.79 | — | following MFI reversion |
| 2026-11-17T16:25 | Three white soldiers | sell | XRP-USD | 13.77 | -0.15 | exit signal |
| 2026-11-17T16:25 | Three white soldiers | sell | DOGE-USD | 13.80 | -0.12 | exit signal |
| 2026-11-17T16:20 | MFI reversion · 1h | buy | GOOGL | 4.62 | — | entry |
| 2026-11-17T16:11 | Three white soldiers | buy | XRP-USD | 13.92 | — | entry signal |
| 2026-11-17T16:11 | Three white soldiers | buy | DOGE-USD | 13.92 | — | entry signal |
| 2026-11-17T16:09 | Agent (ML meta-label) | buy | SQQQ | 15.02 | — | entry |
| 2026-11-17T16:06 | Agent | buy | SOXL | 16.58 | — | rebalance up |
| 2026-11-17T16:06 | Agent | sell | BITX | 16.93 | 0.13 | selected signal exited |
| 2026-11-17T16:06 | Three white soldiers | sell | SQQQ | 13.77 | -0.20 | stop-loss |
| 2026-11-17T16:01 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 101.39 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 16:38:05.000099+00:00 -> 2026-11-17 16:48:05.000099+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 16:38:05.000099+00:00 -> 2026-11-17 16:48:05.000099+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
