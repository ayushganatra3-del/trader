# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T04:10:05.000169+00:00 · 72607 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.23 (-21.77%)

Closed trades 244, win rate 36.1%, fees £6.61, max drawdown -22.21%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.48 | -0.21 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | PLTR 12%, WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, COHR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 3225 decisions in 645 calls, $0.0452 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T04:10 | 2 / 2 / 1 | cash |  |
| Breezy | 2026-11-25T04:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T04:10 | 1 / 4 / 0 | ETH-USD 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| Bollinger reversion · 1h | ETH-USD | 1.78 | +4.64% | 7 |
| RSI(14) reversion · 1h | ETH-USD | 1.77 | +5.50% | 3 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.46 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.70 | 15.70 | 0 | — | 13.68 | 4.60 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.83 | 4.83 | 0 | — | 5.25 | 1.42 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | 0.00 | 0.09 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.39 | -3.61 | 229 | 28.4 | -1.63 | -0.48 | -7.61 | 142 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.69 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.37 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.46 | -5.54 | 0 | — | -6.20 | -1.57 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.08 | -5.92 | 20 | 10.0 | -4.59 | -7.39 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.74 | -7.26 | 0 | — | -7.92 | -1.59 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 92.54 | -7.46 | 61 | 41.0 | -6.79 | -1.22 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.12 | -8.88 | 116 | 24.1 | -8.21 | -4.01 | -11.12 | 40 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.67 | -10.34 | 0 | — | -11.39 | -2.44 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.74 | -11.13 | 24 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.46 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.03 | -13.96 | 168 | 45.8 | -11.69 | -2.14 | -20.49 | 154 |
| 21 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.24 | -13.73 | 543 |
| 22 | Daily: Bullish score | daily | 85.40 | -14.60 | 20 | 20.0 | -13.12 | -2.89 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.88 | -7.27 | -21.10 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.53 | -6.40 | -14.68 | 65 |
| 26 | Parabolic SAR · 1h | trend | 79.05 | -20.95 | 206 | 28.2 | -31.95 | -8.33 | -32.62 | 184 |
| 27 | Volume breakout · 1h | breakout | 78.44 | -21.56 | 169 | 27.8 | -21.81 | -6.52 | -23.66 | 71 |
| 28 | Agent | meta | 78.23 | -21.77 | 244 | 36.1 | -26.15 | -5.89 | -26.43 | 196 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.17 | -18.44 | 88 |
| 30 | Keltner breakout · 1h | breakout | 77.06 | -22.94 | 138 | 24.6 | -24.29 | -6.22 | -26.58 | 147 |
| 31 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -21.85 | -6.71 | -22.57 | 670 |
| 32 | Donchian 55/20 · 1h | breakout | 76.42 | -23.59 | 87 | 13.8 | -29.08 | -7.76 | -29.57 | 82 |
| 33 | Ichimoku · 1h | trend | 74.84 | -25.16 | 113 | 15.9 | -29.47 | -7.46 | -31.53 | 102 |
| 34 | ADX DI cross · 1h | trend | 70.64 | -29.36 | 260 | 19.2 | -37.36 | -7.04 | -38.94 | 293 |
| 35 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.76 | -36.38 | 24 |
| 36 | Bollinger breakout · 1h | breakout | 69.29 | -30.71 | 208 | 22.1 | -30.94 | -7.98 | -33.57 | 207 |
| 37 | Supertrend · 1h | trend | 68.94 | -31.06 | 207 | 18.4 | -36.58 | -7.18 | -37.75 | 208 |
| 38 | Triple EMA stack · 1h | trend | 68.52 | -31.48 | 169 | 15.4 | -39.09 | -9.89 | -39.47 | 172 |
| 39 | Hold BTC | benchmark | 68.43 | -31.57 | 3 | 0.0 | -29.98 | -5.36 | -36.10 | 1 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 68.06 | -31.94 | 3 | 0.0 | -25.78 | -3.19 | -32.18 | 1 |
| 41 | EMA 20/50 cross · 1h | trend | 67.86 | -32.14 | 124 | 9.7 | -38.33 | -10.21 | -39.50 | 112 |
| 42 | OBV trend · 1h | momentum | 66.67 | -33.33 | 323 | 19.8 | -39.04 | -9.73 | -40.06 | 226 |
| 43 | RSI momentum · 1h | momentum | 65.73 | -34.27 | 200 | 15.0 | -40.21 | -9.15 | -41.99 | 196 |
| 44 | Heikin-Ashi · 1h | trend | 64.72 | -35.28 | 543 | 21.9 | -48.71 | -9.96 | -49.70 | 627 |
| 45 | MACD zero-line · 1h | trend | 64.59 | -35.41 | 199 | 16.6 | -34.18 | -9.24 | -34.71 | 199 |
| 46 | Max aggression: 1-day momentum | meta | 64.19 | -35.81 | 34 | 26.5 | -55.97 | -4.13 | -60.68 | 38 |
| 47 | Stochastic reversion · 1h | reversion | 63.14 | -36.85 | 401 | 40.4 | -35.41 | -3.83 | -42.69 | 432 |
| 48 | ROC + volume · 1h | momentum | 63.09 | -36.91 | 456 | 27.0 | -41.01 | -7.97 | -42.69 | 338 |
| 49 | Donchian 20/10 · 1h | breakout | 62.36 | -37.63 | 181 | 17.7 | -40.61 | -8.97 | -42.28 | 194 |
| 50 | Max aggression: 5-day momentum | meta | 61.96 | -38.04 | 26 | 34.6 | -63.25 | -4.16 | -67.33 | 23 |
| 51 | EMA 9/21 cross · 1h | trend | 60.43 | -39.57 | 310 | 12.3 | -43.64 | -10.10 | -45.42 | 329 |
| 52 | MFI reversion · 1h | reversion | 59.52 | -40.48 | 509 | 32.0 | -33.29 | -4.93 | -35.63 | 185 |
| 53 | MACD cross · 1h | trend | 57.94 | -42.06 | 481 | 20.8 | -52.79 | -10.61 | -53.34 | 501 |
| 54 | Agent (ML meta-label) | meta | 56.69 | -43.31 | 2072 | 25.4 | -25.25 | -2.96 | -34.06 | 314 |
| 55 | CCI reversion · 1h | reversion | 55.92 | -44.08 | 446 | 39.2 | -51.89 | -8.81 | -52.59 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 55.45 | -44.55 | 392 | 37.5 | -39.94 | -4.81 | -45.42 | 425 |
| 57 | VWAP momentum · 1h | momentum | 53.51 | -46.49 | 1077 | 21.5 | -58.49 | -12.99 | -59.90 | 1174 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.91 | -8.53 | -53.26 | 689 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.17 | -9.31 | -56.58 | 593 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -48.19 | -99.15 | 5369 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.60 | -31.54 | -83.91 | 1411 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.34 | -47.07 | -94.42 | 2425 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.80 | -32.03 | -90.90 | 1898 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.63 | -39.35 | -91.76 | 2229 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.66 | -27.91 | -89.69 | 1958 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -47.23 | -98.18 | 3438 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.90 | -51.14 | -96.93 | 3373 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.90 | -34.44 | -92.94 | 2070 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.67 | -35.45 | -82.81 | 1532 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -55.62 | -99.69 | 6291 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.16 | -37.82 | -93.16 | 2495 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.24 | -34.82 | -94.25 | 3158 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -62.19 | -99.82 | 6101 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.13 | -42.82 | -93.20 | 2259 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.56 | -22.01 | -51.60 | 641 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.36 | -23.39 | -78.59 | 1610 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -54.65 | -97.75 | 3276 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -57.32 | -99.18 | 5147 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.33 | -27.02 | -71.61 | 1210 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.86 | -47.41 | -94.86 | 2670 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.79 | -6.53 | -48.57 | 281 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.96 | -35.66 | -85.27 | 1657 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -71.04 | -99.77 | 6543 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.63 | -31.01 | -91.67 | 2475 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.07 | -20.27 | -83.22 | 1955 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.93 | -31.10 | -91.97 | 2170 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.19 | -48.82 | -98.19 | 4079 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.40 | -47.37 | -90.40 | 2205 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.37 | -29.17 | -68.37 | 792 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.85 | -26.97 | -73.36 | 1157 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.46 | -19.24 | -84.59 | 1817 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -49.13 | -98.10 | 4427 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -90.49 | -99.94 | 8253 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.61 | -7.28 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-25T04:00 | VWAP reversion · 1h | sell | SOL-USD | 21.33 | -0.03 | exit signal |
| 2026-11-25T03:00 | MACD cross · 1h | buy | XRP-USD | 4.45 | — | entry signal |
| 2026-11-25T02:10 | CCI reversion · 1h | sell | ETH-USD | 2.43 | -0.10 | stop-loss |
| 2026-11-25T02:05 | MFI reversion · 1h | sell | BTC-USD | 3.91 | -0.07 | stop-loss |
| 2026-11-25T02:00 | MACD cross · 1h | sell | ETH-USD | 4.38 | -0.10 | exit signal |
| 2026-11-25T02:00 | MACD cross · 1h | sell | DOGE-USD | 3.57 | -0.06 | exit signal |
| 2026-11-25T02:00 | MACD cross · 1h | sell | BTC-USD | 4.39 | -0.08 | exit signal |
| 2026-11-25T01:50 | CCI reversion · 1h | sell | BTC-USD | 2.90 | -0.07 | stop-loss |
| 2026-11-25T01:35 | MFI reversion · 1h | sell | ETH-USD | 3.91 | -0.07 | stop-loss |
| 2026-11-25T01:35 | Stochastic reversion · 1h | sell | ETH-USD | 7.86 | -0.14 | stop-loss |
| 2026-11-25T01:00 | Heikin-Ashi · 1h | sell | SOL-USD | 16.02 | -0.11 | exit signal |
| 2026-11-25T00:05 | Agent | buy | ETH-USD | 15.69 | — | following Bollinger reversion · 1h, RSI(14) reversion · 1h |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | SOL-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | ETH-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | DOGE-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | MFI reversion · 1h | buy | BTC-USD | 3.98 | — | entry |
| 2026-11-25T00:00 | Heikin-Ashi · 1h | buy | SOL-USD | 16.13 | — | entry signal |
| 2026-11-25T00:00 | MACD cross · 1h | buy | SOL-USD | 2.73 | — | entry signal |
| 2026-11-25T00:00 | MACD cross · 1h | buy | DOGE-USD | 3.63 | — | entry signal |
| 2026-11-24T23:00 | MACD cross · 1h | buy | ETH-USD | 4.47 | — | entry signal |
| 2026-11-24T23:00 | MACD cross · 1h | buy | BTC-USD | 4.47 | — | entry signal |
| 2026-11-24T21:01 | CCI reversion · 1h | buy | SOL-USD | 3.30 | — | entry signal |
| 2026-11-24T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 89.28 | -1.31 | target is flat |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | SQQQ | 6.12 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | MSTR | 6.11 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | buy | ETHU | 6.07 | — | rebalance up |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | TECL | 8.15 | 0.04 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | MSFT | 8.12 | 0.00 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | COIN | 8.10 | -0.00 | selected signal exited |
| 2026-11-24T20:55 | Agent (ML meta-label) | sell | AMD | 8.12 | 0.01 | selected signal exited |
| 2026-11-24T20:55 | Opening range 30m | sell | TNA | 21.26 | -0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | MSFT | 21.14 | -0.08 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | LABU | 17.71 | 0.90 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 30m | sell | IWM | 21.31 | -0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | UPRO | 10.19 | -0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | TNA | 11.66 | 0.02 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | SPY | 10.92 | -0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | MSFT | 10.82 | 0.01 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | LABU | 11.29 | 0.57 | end-of-day flatten |
| 2026-11-24T20:55 | Opening range 15m | sell | IWM | 10.93 | -0.00 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-27 04:10:05.000169+00:00 -> 2026-11-25 04:20:05.000169+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
