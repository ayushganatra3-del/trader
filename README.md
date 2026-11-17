# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T21:05:05.000130+00:00 · 63603 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.66 (-15.34%)

Closed trades 219, win rate 35.6%, fees £6.07, max drawdown -17.33%.

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

Today: 41181 decisions in 3318 calls, $0.5085 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T21:05 | 4 / 1 / 0 | ETH-USD 16%, XRP-USD 15% |  |
| Breezy | 2026-11-17T21:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T21:05 | 4 / 1 / 0 | ETH-USD 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.63 | 16.63 | 0 | — | 14.86 | 5.18 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.86 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.26 | 3.26 | 0 | — | 5.76 | 1.61 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.99 | 2.23 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.32 | -3.68 | 8 | 50.0 | -3.91 | -0.12 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.43 | -4.57 | 0 | — | -3.89 | -1.28 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.69 | -1.66 | -9.23 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.29 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.22 | -7.78 | 0 | — | -8.40 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.72 | -9.28 | 153 | 46.4 | -11.49 | -3.37 | -18.48 | 149 |
| 18 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -11.41 | -5.53 | -13.38 | 60 |
| 19 | Copy: Congress Democrats (NANC) | copy | 90.26 | -9.74 | 0 | — | -8.42 | -2.29 | -12.67 | 1 |
| 20 | Copy: Insider buying | copy | 89.96 | -10.04 | 50 | 42.0 | -9.36 | -1.87 | -14.79 | 62 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.08 | -12.92 | 17 | 17.6 | -4.97 | -0.78 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -15.77 | -6.33 | -19.02 | 76 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.86 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.20 | -7.35 | -16.95 | 199 |
| 26 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.05 | -7.20 | -27.99 | 202 |
| 28 | Keltner breakout · 1h | breakout | 80.72 | -19.28 | 122 | 26.2 | -18.79 | -4.00 | -27.13 | 153 |
| 29 | Connors RSI(2) · 1h | reversion | 80.40 | -19.60 | 215 | 40.0 | -14.37 | -6.39 | -14.85 | 93 |
| 30 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.57 | -29.47 | 83 |
| 31 | Max aggression: 5-day momentum | meta | 79.67 | -20.33 | 21 | 42.9 | -48.12 | -3.22 | -55.24 | 22 |
| 32 | Volume breakout · 1h | breakout | 79.66 | -20.34 | 162 | 28.4 | -15.78 | -4.95 | -22.20 | 79 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.31 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.43 | -23.57 | 2 | 0.0 | -18.45 | -2.48 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.43 | -23.57 | 30 | 26.7 | -24.46 | -0.95 | -57.50 | 39 |
| 36 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -28.72 | -8.40 | -29.33 | 109 |
| 37 | ADX DI cross · 1h | trend | 75.00 | -25.00 | 208 | 19.2 | -27.26 | -4.40 | -35.42 | 262 |
| 38 | Hold BTC | benchmark | 74.74 | -25.26 | 2 | 0.0 | -15.70 | -2.27 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.06 | -5.73 | -33.32 | 221 |
| 40 | Stochastic reversion · 1h | reversion | 73.20 | -26.80 | 345 | 42.6 | -34.29 | -5.22 | -36.02 | 424 |
| 41 | Supertrend · 1h | trend | 71.78 | -28.22 | 189 | 15.9 | -32.01 | -5.45 | -39.67 | 200 |
| 42 | RSI momentum · 1h | momentum | 71.06 | -28.94 | 176 | 14.2 | -31.17 | -5.69 | -37.58 | 197 |
| 43 | Triple EMA stack · 1h | trend | 71.01 | -28.99 | 155 | 14.8 | -32.50 | -6.61 | -38.02 | 182 |
| 44 | MFI reversion · 1h | reversion | 70.84 | -29.16 | 434 | 33.6 | -27.62 | -4.14 | -29.98 | 166 |
| 45 | MACD zero-line · 1h | trend | 70.53 | -29.47 | 181 | 17.7 | -27.14 | -5.42 | -33.31 | 202 |
| 46 | EMA 20/50 cross · 1h | trend | 69.76 | -30.24 | 115 | 10.4 | -36.31 | -10.17 | -39.15 | 114 |
| 47 | Heikin-Ashi · 1h | trend | 69.59 | -30.41 | 466 | 23.0 | -43.07 | -9.09 | -44.76 | 632 |
| 48 | MACD cross · 1h | trend | 69.51 | -30.49 | 413 | 22.3 | -39.10 | -6.38 | -44.56 | 473 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 50 | ROC + volume · 1h | momentum | 69.27 | -30.73 | 408 | 28.2 | -30.93 | -5.08 | -39.54 | 355 |
| 51 | OBV trend · 1h | momentum | 68.34 | -31.66 | 306 | 19.0 | -35.58 | -7.67 | -39.68 | 254 |
| 52 | Donchian 20/10 · 1h | breakout | 67.33 | -32.67 | 159 | 18.2 | -32.64 | -5.52 | -40.92 | 201 |
| 53 | CCI reversion · 1h | reversion | 67.09 | -32.91 | 382 | 41.6 | -41.04 | -6.76 | -44.29 | 471 |
| 54 | Bollinger reversion · 1h | reversion | 63.95 | -36.05 | 344 | 37.8 | -38.50 | -5.84 | -39.42 | 414 |
| 55 | EMA 9/21 cross · 1h | trend | 63.32 | -36.68 | 280 | 11.1 | -40.53 | -7.69 | -47.20 | 323 |
| 56 | Williams %R · 1h | reversion | 63.28 | -36.72 | 430 | 40.7 | -45.50 | -7.79 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.10 | -39.90 | 1906 | 24.3 | -25.65 | -4.97 | -26.67 | 299 |
| 58 | RSI(14) reversion · 1h | reversion | 58.43 | -41.57 | 205 | 31.7 | -40.32 | -5.92 | -43.29 | 257 |
| 59 | Z-score reversion · 1h | reversion | 57.30 | -42.70 | 224 | 35.3 | -37.48 | -5.22 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 56.78 | -43.22 | 959 | 21.7 | -53.48 | -9.52 | -58.52 | 1194 |
| 61 | Candlestick reversal · 1h | reversion | 55.37 | -44.63 | 546 | 26.6 | -46.77 | -8.55 | -48.30 | 646 |
| 62 | Three white soldiers | momentum | 55.07 | -44.93 | 585 | 14.5 | -49.74 | -21.82 | -50.33 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -43.19 | -99.04 | 5260 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.64 | -25.60 | -82.11 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.06 | -41.41 | -94.09 | 2476 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.22 | -32.17 | -90.43 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.62 | -39.83 | -91.66 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.91 | -31.45 | -89.94 | 2118 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -48.34 | -97.94 | 3490 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -55.41 | -96.51 | 3400 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.35 | -38.38 | -93.41 | 2220 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.23 | -32.86 | -83.26 | 1609 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.69 | -99.60 | 6081 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.20 | -42.24 | -92.24 | 2568 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.91 | -39.31 | -94.93 | 3294 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.22 | -99.81 | 6190 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.45 | -43.90 | -92.47 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.72 | -25.95 | -76.79 | 1643 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -61.92 | -97.69 | 3437 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -56.51 | -99.01 | 4954 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.79 | -27.73 | -68.90 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -56.52 | -94.68 | 2747 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.59 | -37.51 | -84.61 | 1721 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -69.42 | -99.70 | 6382 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -31.09 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.44 | -18.61 | -79.91 | 1834 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.24 | -36.27 | -91.31 | 2160 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.50 | -45.80 | -97.53 | 3904 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.43 | -59.58 | -89.50 | 2169 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.21 | -30.38 | -66.21 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.96 | -23.33 | -72.54 | 1225 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.50 | -17.87 | -80.74 | 1725 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -46.40 | -97.58 | 4343 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.65 | -99.94 | 8457 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T21:00 | ROC + volume · 1h | buy | DOGE-USD | 17.33 | — | entry signal |
| 2026-11-17T21:00 | MACD cross · 1h | buy | DOGE-USD | 3.00 | — | entry signal |
| 2026-11-17T20:55 | Agent (rotation) | sell | SQQQ | 31.47 | 0.17 | selected signal exited |
| 2026-11-17T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 98.59 | 0.15 | target is flat |
| 2026-11-17T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 111.39 | 0.61 | target is flat |
| 2026-11-17T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.65 | -0.23 | target is flat |
| 2026-11-17T20:55 | Agent (ML meta-label) | buy | TQQQ | 14.96 | — | entry |
| 2026-11-17T20:55 | Agent (ML meta-label) | sell | MSTR | 14.92 | -0.06 | selected signal exited |
| 2026-11-17T20:55 | Agent (ML meta-label) | sell | AMD | 14.94 | -0.04 | selected signal exited |
| 2026-11-17T20:55 | Agent | sell | SOXL | 17.04 | 0.10 | selected signal exited |
| 2026-11-17T20:55 | MFI reversion · 1h | buy | UPRO | 5.04 | — | entry |
| 2026-11-17T20:55 | MFI reversion · 1h | buy | TSLA | 10.08 | — | entry |
| 2026-11-17T20:55 | MFI reversion · 1h | sell | MSFT | 11.78 | -0.01 | target is flat |
| 2026-11-17T20:55 | Opening range 30m | sell | SQQQ | 21.97 | 0.45 | end-of-day flatten |
| 2026-11-17T20:55 | Opening range 15m | sell | SQQQ | 19.93 | 0.41 | end-of-day flatten |
| 2026-11-17T20:50 | Agent (ML meta-label) | buy | MSTR | 14.99 | — | entry |
| 2026-11-17T20:50 | Agent (ML meta-label) | buy | AMD | 14.99 | — | entry |
| 2026-11-17T20:50 | MFI reversion · 1h | buy | MSFT | 4.77 | — | rebalance up |
| 2026-11-17T20:50 | MFI reversion · 1h | sell | LABU | 8.11 | 0.08 | target is flat |
| 2026-11-17T20:50 | Three white soldiers | sell | NVDA | 13.75 | -0.02 | exit signal |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | TQQQ | 14.93 | -0.02 | selected signal exited |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | SQQQ | 11.99 | -0.00 | selected signal exited |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | MSTR | 14.98 | -0.03 | selected signal exited |
| 2026-11-17T20:45 | Agent (ML meta-label) | sell | AMD | 6.06 | -0.00 | selected signal exited |
| 2026-11-17T20:45 | Agent (aggressive) | sell | COIN | 40.80 | -0.18 | selected signal exited |
| 2026-11-17T20:45 | Agent | sell | COIN | 16.85 | -0.07 | selected signal exited |
| 2026-11-17T20:45 | VWAP momentum · 1h | buy | BITX | 6.31 | — | entry |
| 2026-11-17T20:40 | Agent (ML meta-label) | buy | AMD | 6.06 | — | entry |
| 2026-11-17T20:40 | Agent (ML meta-label) | sell | SQQQ | 3.01 | -0.00 | rebalance down |
| 2026-11-17T20:40 | Agent (ML meta-label) | sell | SPY | 3.05 | 0.01 | rebalance down |
| 2026-11-17T20:40 | MFI reversion · 1h | buy | MSFT | 7.02 | — | entry |
| 2026-11-17T20:40 | MFI reversion · 1h | buy | BITX | 10.11 | — | entry |
| 2026-11-17T20:40 | MFI reversion · 1h | sell | GOOGL | 7.01 | -0.04 | target is flat |
| 2026-11-17T20:40 | MFI reversion · 1h | sell | AMZN | 10.11 | 0.01 | target is flat |
| 2026-11-17T20:40 | VWAP reversion · 1h | sell | AAPL | 22.75 | 0.01 | target is flat |
| 2026-11-17T20:40 | VWAP momentum · 1h | sell | BITX | 6.33 | 0.01 | target is flat |
| 2026-11-17T20:35 | Agent (ML meta-label) | buy | TQQQ | 14.95 | — | entry |
| 2026-11-17T20:35 | Agent (ML meta-label) | buy | SQQQ | 15.00 | — | entry |
| 2026-11-17T20:35 | Agent (ML meta-label) | buy | MSTR | 15.00 | — | entry |
| 2026-11-17T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 91.88 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 21:05:05.000130+00:00 -> 2026-11-17 21:15:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 21:05:05.000130+00:00 -> 2026-11-17 21:15:05.000130+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
