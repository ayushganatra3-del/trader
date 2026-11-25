# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-25T02:40:05.000170+00:00 · 72522 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.21 (-21.79%)

Closed trades 244, win rate 36.1%, fees £6.61, max drawdown -22.21%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETH-USD | 15.46 | -0.23 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-24)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.36 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.8, AAPL 4.7, TSLA 3.3, LABU 2.2, GOOGL 0.8, META 0.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 1950 decisions in 390 calls, $0.0274 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-25T02:40 | 1 / 3 / 1 | XRP-USD 16% |  |
| Breezy | 2026-11-25T02:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-25T02:40 | 3 / 2 / 0 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.67 | 15.67 | 0 | — | 13.68 | 4.83 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.80 | 4.80 | 0 | — | 5.25 | 1.47 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.32 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.51 | -1.49 | 219 | 31.5 | -0.40 | -0.04 | -8.58 | 210 |
| 9 | Agent (rotation) | meta | 96.38 | -3.62 | 229 | 28.4 | -1.00 | -0.26 | -7.61 | 138 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.79 | -4.21 | 170 | 32.9 | -4.24 | -3.72 | -5.35 | 61 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.03 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.44 | -5.56 | 0 | — | -6.20 | -1.61 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 94.07 | -5.93 | 20 | 10.0 | -4.59 | -7.46 | -5.16 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.71 | -7.29 | 0 | — | -7.92 | -1.60 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.11 | -8.89 | 116 | 24.1 | -8.21 | -4.04 | -11.12 | 40 |
| 16 | Copy: Congress Democrats (NANC) | copy | 89.64 | -10.36 | 0 | — | -11.39 | -2.43 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.88 | -7.81 | -11.13 | 24 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.35 | -2.97 | -20.94 | 1 |
| 19 | VWAP reversion · 1h | reversion | 85.94 | -14.06 | 167 | 46.1 | -11.77 | -2.17 | -20.49 | 154 |
| 20 | Opening range 30m | breakout | 85.41 | -14.59 | 473 | 32.8 | -12.69 | -4.26 | -13.73 | 543 |
| 21 | Daily: Bullish score | daily | 85.39 | -14.61 | 20 | 20.0 | -13.12 | -3.07 | -19.56 | 14 |
| 22 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.10 | -7.43 | -21.38 | 75 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.53 | -6.46 | -14.68 | 65 |
| 25 | Parabolic SAR · 1h | trend | 79.03 | -20.97 | 206 | 28.2 | -32.02 | -8.43 | -32.69 | 184 |
| 26 | Volume breakout · 1h | breakout | 78.44 | -21.57 | 169 | 27.8 | -21.81 | -6.58 | -23.66 | 71 |
| 27 | Agent | meta | 78.21 | -21.79 | 244 | 36.1 | -26.16 | -5.94 | -26.43 | 196 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.13 | -4.20 | -18.44 | 88 |
| 29 | Keltner breakout · 1h | breakout | 77.05 | -22.95 | 138 | 24.6 | -24.63 | -6.37 | -26.91 | 148 |
| 30 | Opening range 15m | breakout | 76.71 | -23.29 | 592 | 30.7 | -22.28 | -6.94 | -22.99 | 670 |
| 31 | Donchian 55/20 · 1h | breakout | 76.41 | -23.59 | 87 | 13.8 | -29.08 | -7.83 | -29.57 | 82 |
| 32 | Ichimoku · 1h | trend | 74.84 | -25.16 | 113 | 15.9 | -29.47 | -7.53 | -31.53 | 102 |
| 33 | ADX DI cross · 1h | trend | 70.62 | -29.38 | 260 | 19.2 | -37.03 | -7.02 | -38.51 | 291 |
| 34 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -34.21 | -4.92 | -36.38 | 24 |
| 35 | Bollinger breakout · 1h | breakout | 69.29 | -30.71 | 208 | 22.1 | -30.94 | -8.05 | -33.57 | 207 |
| 36 | Supertrend · 1h | trend | 68.93 | -31.07 | 207 | 18.4 | -36.58 | -7.25 | -37.75 | 208 |
| 37 | Hold BTC | benchmark | 68.51 | -31.49 | 3 | 0.0 | -29.72 | -5.37 | -36.10 | 1 |
| 38 | Triple EMA stack · 1h | trend | 68.51 | -31.49 | 169 | 15.4 | -39.05 | -9.98 | -39.42 | 172 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 68.04 | -31.96 | 3 | 0.0 | -25.78 | -3.33 | -32.18 | 1 |
| 40 | EMA 20/50 cross · 1h | trend | 67.84 | -32.16 | 124 | 9.7 | -38.33 | -10.32 | -39.47 | 112 |
| 41 | OBV trend · 1h | momentum | 66.66 | -33.34 | 323 | 19.8 | -39.18 | -9.88 | -40.19 | 227 |
| 42 | RSI momentum · 1h | momentum | 65.72 | -34.28 | 200 | 15.0 | -40.24 | -9.24 | -42.02 | 196 |
| 43 | Heikin-Ashi · 1h | trend | 64.71 | -35.29 | 543 | 21.9 | -48.71 | -10.04 | -49.70 | 627 |
| 44 | MACD zero-line · 1h | trend | 64.58 | -35.42 | 199 | 16.6 | -34.05 | -9.28 | -34.71 | 198 |
| 45 | Max aggression: 1-day momentum | meta | 64.17 | -35.83 | 34 | 26.5 | -55.96 | -4.17 | -60.67 | 38 |
| 46 | Stochastic reversion · 1h | reversion | 63.10 | -36.90 | 401 | 40.4 | -35.43 | -3.86 | -42.69 | 432 |
| 47 | ROC + volume · 1h | momentum | 63.08 | -36.92 | 456 | 27.0 | -41.33 | -8.16 | -42.70 | 339 |
| 48 | Donchian 20/10 · 1h | breakout | 62.35 | -37.65 | 181 | 17.7 | -40.61 | -9.06 | -42.28 | 194 |
| 49 | Max aggression: 5-day momentum | meta | 61.94 | -38.05 | 26 | 34.6 | -63.25 | -4.19 | -67.33 | 23 |
| 50 | EMA 9/21 cross · 1h | trend | 60.41 | -39.59 | 310 | 12.3 | -43.93 | -10.30 | -45.78 | 330 |
| 51 | MFI reversion · 1h | reversion | 59.50 | -40.50 | 509 | 32.0 | -33.02 | -4.94 | -35.63 | 186 |
| 52 | MACD cross · 1h | trend | 57.92 | -42.09 | 481 | 20.8 | -52.85 | -10.75 | -53.39 | 499 |
| 53 | Agent (ML meta-label) | meta | 56.68 | -43.32 | 2072 | 25.4 | -27.08 | -3.33 | -34.24 | 314 |
| 54 | CCI reversion · 1h | reversion | 55.89 | -44.11 | 446 | 39.2 | -51.91 | -8.91 | -52.59 | 494 |
| 55 | Bollinger reversion · 1h | reversion | 55.36 | -44.64 | 392 | 37.5 | -39.95 | -4.85 | -45.42 | 424 |
| 56 | VWAP momentum · 1h | momentum | 53.50 | -46.50 | 1077 | 21.5 | -58.47 | -13.05 | -59.93 | 1177 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.58 | -8.76 | -53.79 | 694 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.14 | -9.39 | -56.57 | 591 |
| 59 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -48.48 | -99.14 | 5358 |
| 60 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.67 | -32.97 | -83.89 | 1412 |
| 61 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.44 | -47.87 | -94.44 | 2433 |
| 62 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.82 | -31.87 | -90.89 | 1898 |
| 63 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.69 | -40.03 | -91.73 | 2231 |
| 64 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.79 | -28.01 | -89.82 | 1963 |
| 65 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -46.89 | -98.18 | 3437 |
| 66 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -52.08 | -96.95 | 3378 |
| 67 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.93 | -36.12 | -92.97 | 2069 |
| 68 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.88 | -35.28 | -82.88 | 1537 |
| 69 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -55.63 | -99.68 | 6284 |
| 70 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.19 | -37.28 | -93.20 | 2496 |
| 71 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.29 | -35.74 | -94.30 | 3165 |
| 72 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -64.17 | -99.81 | 6101 |
| 73 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.09 | -42.34 | -93.16 | 2255 |
| 74 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.62 | -22.23 | -51.66 | 643 |
| 75 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.58 | -23.18 | -78.68 | 1614 |
| 76 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -56.18 | -97.75 | 3279 |
| 77 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -60.17 | -99.18 | 5147 |
| 78 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 79 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.30 | -26.79 | -71.59 | 1210 |
| 80 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.82 | -46.09 | -94.84 | 2670 |
| 81 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.79 | -6.58 | -48.57 | 281 |
| 82 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.03 | -35.37 | -85.25 | 1661 |
| 83 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -72.39 | -99.77 | 6545 |
| 84 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.65 | -31.47 | -91.67 | 2475 |
| 85 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.99 | -20.14 | -83.17 | 1952 |
| 86 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.97 | -32.44 | -92.01 | 2175 |
| 87 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.19 | -49.02 | -98.19 | 4079 |
| 88 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.31 | -45.74 | -90.33 | 2202 |
| 89 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.28 | -28.59 | -68.51 | 794 |
| 90 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.04 | -27.72 | -73.47 | 1158 |
| 91 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.39 | -19.21 | -84.48 | 1818 |
| 92 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -49.89 | -98.11 | 4431 |
| 93 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -88.38 | -99.94 | 8257 |
| 94 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 95 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.62 | -7.35 | -50.46 | 306 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-24T20:55 | Opening range 15m | sell | AAPL | 10.89 | 0.00 | end-of-day flatten |
| 2026-11-24T20:50 | Agent (ML meta-label) | buy | TECL | 8.11 | — | entry |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
