# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T20:54:05.000131+00:00 · 50069 ticks

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

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 38.26 · VIX 28.18 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 38571 decisions in 3147 calls, $0.4760 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T20:54 | 2 / 7 / 21 | cash |  |
| Breezy | 2026-11-06T20:54 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-06T20:54 | 3 / 21 / 6 | MSTR 59% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |
| Candlestick reversal · 1h | DOGE-USD | 1.64 | +5.59% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.59 | 12.60 | 0 | — | 13.32 | 4.57 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.97 | -0.03 | 121 | 47.9 | -12.00 | -2.81 | -14.15 | 156 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.70 | -0.30 | 0 | — | 2.65 | 0.84 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Hold SPY | benchmark | 95.05 | -4.95 | 0 | — | -3.95 | -1.45 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.75 | -4.87 | -10.36 | 169 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.58 | -5.42 | 20 | 20.0 | -6.45 | -5.97 | -7.14 | 22 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.35 | -0.36 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.63 | -7.37 | 7 | 42.9 | -9.67 | -0.91 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.57 | -7.43 | 0 | — | -6.81 | -2.04 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.17 | -7.83 | 108 | 23.1 | -15.65 | -5.68 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 91.12 | -8.88 | 0 | — | -6.90 | -2.05 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.44 | -10.56 | 369 | 32.8 | -16.24 | -5.24 | -17.56 | 588 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.25 | -3.57 | -14.68 | 86 |
| 23 | Daily: Bullish score | daily | 88.64 | -11.36 | 15 | 20.0 | -5.13 | -0.68 | -16.58 | 14 |
| 24 | Hold BTC | benchmark | 88.58 | -11.42 | 1 | 0.0 | -5.44 | -0.64 | -14.09 | 1 |
| 25 | Agent | meta | 88.30 | -11.70 | 151 | 37.1 | -13.66 | -7.29 | -14.12 | 206 |
| 26 | Copy: Insider buying | copy | 88.09 | -11.91 | 40 | 37.5 | -23.98 | -4.68 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.80 | -13.20 | 166 | 27.1 | -14.95 | -3.32 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.84 | -14.16 | 71 | 14.1 | -13.40 | -2.74 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 84.77 | -15.23 | 17 | 47.1 | -32.95 | -2.10 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.60 | -5.59 | -18.68 | 98 |
| 31 | Opening range 15m | breakout | 82.29 | -17.71 | 458 | 29.9 | -21.21 | -6.29 | -21.40 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.21 | -17.79 | 260 | 46.9 | -25.96 | -3.85 | -29.25 | 394 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.70 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.68 | -24.50 | 173 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.55 | -19.45 | 2 | 0.0 | -11.97 | -1.55 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.44 | -20.57 | 174 | 18.4 | -25.01 | -4.21 | -27.04 | 262 |
| 38 | MFI reversion · 1h | reversion | 78.62 | -21.38 | 333 | 34.2 | -19.12 | -2.76 | -20.68 | 159 |
| 39 | Ichimoku · 1h | trend | 77.87 | -22.13 | 94 | 14.9 | -23.31 | -4.79 | -29.43 | 126 |
| 40 | Bollinger breakout · 1h | breakout | 77.78 | -22.22 | 166 | 23.5 | -23.58 | -4.92 | -27.12 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.88 | -23.12 | 286 | 46.2 | -30.76 | -5.05 | -32.12 | 468 |
| 42 | EMA 20/50 cross · 1h | trend | 76.00 | -24.00 | 102 | 10.8 | -24.63 | -4.49 | -30.58 | 134 |
| 43 | Heikin-Ashi · 1h | trend | 75.64 | -24.36 | 393 | 22.9 | -43.09 | -9.09 | -43.54 | 677 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.41 | -5.50 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.37 | -25.63 | 142 | 14.8 | -28.85 | -6.09 | -33.48 | 204 |
| 46 | Supertrend · 1h | trend | 73.65 | -26.35 | 166 | 13.3 | -30.52 | -5.34 | -34.80 | 217 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -28.11 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.34 | -26.66 | 335 | 23.0 | -36.28 | -6.47 | -38.81 | 485 |
| 49 | Z-score reversion · 1h | reversion | 73.18 | -26.82 | 162 | 35.8 | -25.62 | -3.83 | -28.33 | 234 |
| 50 | Bollinger reversion · 1h | reversion | 73.08 | -26.92 | 251 | 40.2 | -31.17 | -5.32 | -34.52 | 372 |
| 51 | Williams %R · 1h | reversion | 72.49 | -27.52 | 314 | 44.9 | -37.43 | -6.06 | -39.71 | 534 |
| 52 | Daily: Momentum burst | daily | 72.22 | -27.78 | 26 | 11.5 | -36.00 | -5.07 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.51 | -28.49 | 140 | 20.0 | -30.10 | -5.58 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 70.99 | -29.01 | 273 | 17.9 | -30.60 | -6.56 | -33.60 | 285 |
| 55 | ROC + volume · 1h | momentum | 70.01 | -29.99 | 346 | 25.4 | -37.07 | -7.22 | -37.28 | 379 |
| 56 | EMA 9/21 cross · 1h | trend | 67.41 | -32.59 | 241 | 10.0 | -40.44 | -8.40 | -40.77 | 338 |
| 57 | VWAP momentum · 1h | momentum | 67.26 | -32.74 | 776 | 22.0 | -56.15 | -12.50 | -56.15 | 1238 |
| 58 | Agent (ML meta-label) | meta | 66.58 | -33.42 | 1535 | 23.1 | -8.24 | -1.18 | -18.60 | 342 |
| 59 | RSI(14) reversion · 1h | reversion | 66.37 | -33.63 | 142 | 27.5 | -28.39 | -4.43 | -31.54 | 218 |
| 60 | Three white soldiers | momentum | 65.58 | -34.42 | 459 | 15.9 | -48.02 | -22.48 | -48.02 | 640 |
| 61 | Candlestick reversal · 1h | reversion | 65.53 | -34.47 | 406 | 28.6 | -38.05 | -7.02 | -38.66 | 570 |
| 62 | Max aggression: 1-day momentum | meta | 61.93 | -38.06 | 26 | 26.9 | -43.27 | -2.75 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -46.49 | -98.93 | 5220 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.66 | -25.95 | -80.83 | 1433 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -48.42 | -93.49 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.24 | -32.22 | -89.33 | 1911 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.84 | -40.49 | -90.90 | 2309 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.16 | -32.04 | -90.16 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -55.75 | -97.72 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -59.66 | -96.30 | 3397 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.89 | -33.96 | -93.90 | 2452 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.57 | -36.82 | -82.58 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -55.71 | -99.52 | 5986 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -44.51 | -92.70 | 2604 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -38.09 | -95.69 | 3409 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.88 | -99.80 | 6197 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -44.29 | -91.87 | 2280 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.55 | -25.93 | -75.66 | 1577 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -65.29 | -97.73 | 3513 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -62.77 | -98.78 | 4884 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.77 | -29.59 | -69.98 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -56.44 | -94.72 | 2752 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.15 | -38.31 | -85.23 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -74.86 | -99.64 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.18 | -31.75 | -89.27 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.82 | -19.62 | -78.03 | 1744 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.10 | -38.19 | -91.12 | 2222 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.57 | -53.08 | -96.60 | 3876 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.59 | -57.48 | -89.60 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.26 | -29.08 | -66.26 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.64 | -24.87 | -73.79 | 1270 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.03 | -17.78 | -78.58 | 1665 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -50.19 | -97.26 | 4330 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -121.48 | -99.93 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T20:50 | Agent (ML meta-label) | buy | LABU | 3.69 | — | entry |
| 2026-11-06T20:50 | Agent (ML meta-label) | sell | BTC-USD | 3.69 | -0.02 | selected signal exited |
| 2026-11-06T20:40 | MFI reversion · 1h | buy | ETHU | 6.56 | — | entry |
| 2026-11-06T20:40 | MFI reversion · 1h | sell | COIN | 7.15 | -0.01 | target is flat |
| 2026-11-06T20:40 | Three white soldiers | sell | COIN | 16.40 | -0.09 | exit signal |
| 2026-11-06T20:35 | Agent (ML meta-label) | buy | MSTR | 1.49 | — | entry |
| 2026-11-06T20:35 | Agent (ML meta-label) | buy | META | 3.71 | — | entry |
| 2026-11-06T20:35 | Agent (ML meta-label) | buy | BTC-USD | 3.71 | — | entry |
| 2026-11-06T20:35 | Agent (ML meta-label) | sell | SQQQ | 4.48 | 0.03 | selected signal exited |
| 2026-11-06T20:35 | Agent (ML meta-label) | sell | LABU | 3.96 | 0.03 | selected signal exited |
| 2026-11-06T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 95.31 | — | entry |
| 2026-11-06T20:30 | MFI reversion · 1h | buy | AAPL | 6.06 | — | entry signal |
| 2026-11-06T20:30 | MFI reversion · 1h | sell | NVDA | 6.13 | -0.00 | target is flat |
| 2026-11-06T20:30 | Stochastic reversion · 1h | buy | XRP-USD | 2.39 | — | entry |
| 2026-11-06T20:30 | Stochastic reversion · 1h | buy | UPRO | 4.86 | — | entry |
| 2026-11-06T20:30 | Stochastic reversion · 1h | buy | TQQQ | 4.86 | — | entry |
| 2026-11-06T20:30 | Stochastic reversion · 1h | buy | BITX | 4.86 | — | entry signal |
| 2026-11-06T20:30 | Stochastic reversion · 1h | sell | TECL | 4.15 | -0.02 | rebalance down |
| 2026-11-06T20:30 | Stochastic reversion · 1h | sell | SOXL | 4.22 | 0.01 | rebalance down |
| 2026-11-06T20:30 | Stochastic reversion · 1h | sell | MSTR | 4.38 | 0.09 | rebalance down |
| 2026-11-06T20:30 | Stochastic reversion · 1h | sell | COIN | 4.21 | 0.01 | rebalance down |
| 2026-11-06T20:30 | VWAP reversion · 1h | sell | COIN | 25.06 | 0.05 | exit signal |
| 2026-11-06T20:30 | Z-score reversion · 1h | sell | GOOGL | 4.30 | -0.03 | exit signal |
| 2026-11-06T20:30 | Bollinger reversion · 1h | sell | AMD | 5.33 | 0.18 | exit signal |
| 2026-11-06T20:30 | ROC + volume · 1h | buy | AMZN | 17.51 | — | entry signal |
| 2026-11-06T20:30 | ROC + volume · 1h | sell | SQQQ | 17.49 | -0.07 | exit signal |
| 2026-11-06T20:30 | Trend pullback · 1h | sell | AAPL | 23.06 | -0.07 | exit signal |
| 2026-11-06T20:30 | Heikin-Ashi · 1h | buy | TNA | 11.45 | — | entry signal |
| 2026-11-06T20:30 | Heikin-Ashi · 1h | buy | IWM | 15.19 | — | entry signal |
| 2026-11-06T20:30 | Heikin-Ashi · 1h | sell | LABU | 3.91 | 0.02 | rebalance down |
| 2026-11-06T20:30 | Heikin-Ashi · 1h | sell | AMD | 3.86 | 0.04 | rebalance down |
| 2026-11-06T20:30 | ADX DI cross · 1h | sell | GOOGL | 19.97 | -0.04 | exit signal |
| 2026-11-06T20:25 | MFI reversion · 1h | buy | NVDA | 6.13 | — | entry |
| 2026-11-06T20:25 | MFI reversion · 1h | buy | COIN | 7.16 | — | entry |
| 2026-11-06T20:25 | MFI reversion · 1h | buy | BITX | 7.16 | — | entry |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | XRP-USD | 3.97 | -0.08 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | SOL-USD | 4.17 | 0.02 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | ETH-USD | 4.12 | 0.00 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | BTC-USD | 4.10 | 0.00 | rebalance down |
| 2026-11-06T20:25 | MFI reversion · 1h | sell | AMZN | 4.09 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 20:54:05.000131+00:00 -> 2026-11-06 21:04:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 20:54:05.000131+00:00 -> 2026-11-06 21:04:05.000131+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 20:54:05.000131+00:00 -> 2026-11-06 21:04:05.000131+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
