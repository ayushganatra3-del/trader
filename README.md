# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-07T02:20:05.000095+00:00 · 50347 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.29 (-11.71%)

Closed trades 151, win rate 37.1%, fees £4.36, max drawdown -12.16%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| DOGE-USD | 17.65 | -0.01 |

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

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 1812 decisions in 363 calls, $0.0252 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-07T02:20 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-11-07T02:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-07T02:20 | 3 / 1 / 1 | ETH-USD 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI(14) reversion | SQQQ | 2.31 | +7.36% | 4 |
| Z-score reversion | SQQQ | 1.94 | +4.38% | 7 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Candlestick reversal · 1h | DOGE-USD | 1.92 | +7.45% | 7 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.73 | -0.27 | 121 | 47.9 | -12.14 | -2.96 | -14.29 | 154 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.38 | -4.64 | -10.36 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.53 | -0.42 | -9.18 | 229 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.74 | -5.72 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Hold BTC | benchmark | 88.78 | -11.22 | 1 | 0.0 | -5.27 | -0.70 | -14.09 | 1 |
| 23 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.35 | -4.49 | -26.04 | 65 |
| 24 | Daily: Bullish score | daily | 88.75 | -11.25 | 15 | 20.0 | -5.01 | -0.66 | -16.58 | 14 |
| 25 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.25 | -3.55 | -14.68 | 86 |
| 26 | Agent | meta | 88.29 | -11.71 | 151 | 37.1 | -13.82 | -7.41 | -13.98 | 201 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -14.21 | -3.15 | -20.50 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -13.29 | -2.72 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.15 | -14.85 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.39 | -5.51 | -18.68 | 96 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.11 | -17.89 | 260 | 46.9 | -26.03 | -3.87 | -29.25 | 394 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -17.03 | -3.85 | -21.73 | 101 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.66 | -24.50 | 173 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.36 | -20.64 | 175 | 18.3 | -24.76 | -4.15 | -27.04 | 263 |
| 38 | MFI reversion · 1h | reversion | 78.74 | -21.26 | 336 | 34.2 | -18.92 | -2.72 | -20.66 | 158 |
| 39 | Ichimoku · 1h | trend | 77.87 | -22.12 | 94 | 14.9 | -22.89 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.55 | -22.45 | 168 | 23.2 | -23.80 | -4.95 | -27.27 | 248 |
| 41 | CCI reversion · 1h | reversion | 76.77 | -23.23 | 288 | 45.8 | -30.92 | -5.10 | -31.60 | 464 |
| 42 | EMA 20/50 cross · 1h | trend | 76.07 | -23.93 | 102 | 10.8 | -23.25 | -4.22 | -30.58 | 130 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.95 | -9.12 | -43.54 | 677 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.41 | -5.50 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -28.88 | -6.12 | -33.47 | 203 |
| 46 | Supertrend · 1h | trend | 73.62 | -26.38 | 166 | 13.3 | -30.11 | -5.24 | -34.80 | 216 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -28.09 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.38 | -26.62 | 335 | 23.0 | -36.61 | -6.53 | -38.81 | 485 |
| 49 | Z-score reversion · 1h | reversion | 73.17 | -26.83 | 162 | 35.8 | -25.27 | -3.77 | -28.10 | 233 |
| 50 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 251 | 40.2 | -30.89 | -5.29 | -34.15 | 372 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -37.42 | -6.08 | -39.35 | 534 |
| 52 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.93 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.71 | -28.29 | 140 | 20.0 | -29.88 | -5.52 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.45 | -6.21 | -34.09 | 284 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -37.94 | -7.46 | -38.14 | 382 |
| 56 | EMA 9/21 cross · 1h | trend | 67.30 | -32.70 | 242 | 9.9 | -40.05 | -8.32 | -40.18 | 336 |
| 57 | VWAP momentum · 1h | momentum | 67.10 | -32.90 | 779 | 22.1 | -55.79 | -12.31 | -55.88 | 1238 |
| 58 | RSI(14) reversion · 1h | reversion | 66.34 | -33.66 | 143 | 27.3 | -28.71 | -4.50 | -31.54 | 218 |
| 59 | Agent (ML meta-label) | meta | 66.34 | -33.66 | 1540 | 23.0 | -10.28 | -1.47 | -20.81 | 355 |
| 60 | Candlestick reversal · 1h | reversion | 65.48 | -34.52 | 408 | 28.7 | -37.83 | -6.98 | -38.52 | 570 |
| 61 | Three white soldiers | momentum | 65.12 | -34.88 | 463 | 15.8 | -48.31 | -22.53 | -48.36 | 644 |
| 62 | Max aggression: 1-day momentum | meta | 62.21 | -37.79 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.78 | -98.94 | 5224 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.71 | -25.02 | -80.76 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -44.93 | -93.48 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.27 | -30.99 | -89.30 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.79 | -38.30 | -90.80 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.14 | -31.92 | -90.16 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -51.27 | -97.74 | 3483 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -54.07 | -96.31 | 3402 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -33.55 | -93.76 | 2443 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.46 | -34.58 | -82.50 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -52.42 | -99.52 | 5982 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.74 | -42.11 | -92.74 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.70 | -37.62 | -95.70 | 3411 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.74 | -99.80 | 6201 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.97 | -41.71 | -91.97 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.30 | -25.44 | -76.30 | 1584 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -59.77 | -97.74 | 3510 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -57.76 | -98.78 | 4884 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.93 | -28.65 | -69.93 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -51.95 | -94.72 | 2751 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.14 | -36.69 | -85.14 | 1771 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -67.54 | -99.64 | 6379 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.18 | -30.71 | -89.27 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.70 | -19.32 | -77.89 | 1744 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.10 | -36.48 | -91.14 | 2234 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.57 | -50.13 | -96.58 | 3876 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.58 | -53.26 | -89.58 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.95 | -28.25 | -65.95 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.47 | -24.00 | -73.50 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.54 | -17.85 | -78.78 | 1668 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -47.45 | -97.24 | 4328 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.10 | -99.93 | 8316 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-07T02:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.04 | — | entry |
| 2026-11-07T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.42 | 0.00 | exit signal |
| 2026-11-07T02:00 | Bollinger breakout · 1h | buy | ETH-USD | 19.40 | — | entry signal |
| 2026-11-07T02:00 | VWAP momentum · 1h | buy | ETH-USD | 2.51 | — | entry signal |
| 2026-11-07T02:00 | VWAP momentum · 1h | buy | BTC-USD | 5.59 | — | entry signal |
| 2026-11-07T02:00 | Three white soldiers | buy | SOL-USD | 16.29 | — | entry signal |
| 2026-11-07T01:00 | Agent | buy | DOGE-USD | 17.66 | — | following Candlestick reversal · 1h |
| 2026-11-07T01:00 | CCI reversion · 1h | buy | XRP-USD | 4.04 | — | entry signal |
| 2026-11-07T01:00 | VWAP momentum · 1h | buy | SOL-USD | 6.72 | — | entry signal |
| 2026-11-07T01:00 | VWAP momentum · 1h | sell | ETH-USD | 6.08 | -0.03 | exit signal |
| 2026-11-07T01:00 | VWAP momentum · 1h | sell | BTC-USD | 7.44 | -0.02 | exit signal |
| 2026-11-07T00:51 | Agent (ML meta-label) | sell | BTC-USD | 3.88 | -0.02 | selected signal exited |
| 2026-11-07T00:45 | Agent (ML meta-label) | buy | BTC-USD | 3.90 | — | entry |
| 2026-11-07T00:30 | Three white soldiers | sell | ETH-USD | 16.21 | -0.11 | exit signal |
| 2026-11-07T00:21 | Agent (ML meta-label) | sell | BTC-USD | 4.02 | -0.02 | selected signal exited |
| 2026-11-07T00:15 | Three white soldiers | buy | ETH-USD | 16.32 | — | entry signal |
| 2026-11-07T00:10 | Agent (ML meta-label) | buy | BTC-USD | 4.05 | — | entry |
| 2026-11-07T00:05 | Agent (ML meta-label) | sell | BTC-USD | 3.88 | -0.02 | selected signal exited |
| 2026-11-07T00:00 | ROC + volume · 1h | sell | DOGE-USD | 17.40 | -0.22 | exit signal |
| 2026-11-07T00:00 | Three white soldiers | sell | ETH-USD | 16.25 | -0.11 | exit signal |
| 2026-11-06T23:55 | Three white soldiers | sell | XRP-USD | 16.26 | -0.12 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-09 02:20:05.000095+00:00 -> 2026-11-07 02:30:05.000095+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-09 02:20:05.000095+00:00 -> 2026-11-07 02:30:05.000095+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-09 02:20:05.000095+00:00 -> 2026-11-07 02:30:05.000095+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
