# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-07T00:20:05.000162+00:00 · 50241 ticks

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

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 225 decisions in 45 calls, $0.0031 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-07T00:20 | 1 / 4 / 0 | DOGE-USD 16% |  |
| Breezy | 2026-11-07T00:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-07T00:20 | 2 / 3 / 0 | ETH-USD 70% |  |

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
| 7 | VWAP reversion · 1h | reversion | 99.83 | -0.17 | 121 | 47.9 | -12.27 | -2.93 | -14.16 | 152 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.38 | -4.64 | -10.36 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.29 | -0.34 | -9.18 | 229 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.74 | -5.72 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.35 | -4.49 | -26.04 | 65 |
| 23 | Daily: Bullish score | daily | 88.75 | -11.25 | 15 | 20.0 | -5.01 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.25 | -3.55 | -14.68 | 86 |
| 25 | Hold BTC | benchmark | 88.63 | -11.37 | 1 | 0.0 | -5.39 | -0.73 | -14.09 | 1 |
| 26 | Agent | meta | 88.30 | -11.70 | 151 | 37.1 | -13.81 | -7.40 | -13.93 | 200 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -14.21 | -3.15 | -20.50 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -13.29 | -2.72 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.15 | -14.85 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.39 | -5.51 | -18.68 | 96 |
| 31 | Stochastic reversion · 1h | reversion | 82.12 | -17.88 | 260 | 46.9 | -25.99 | -3.85 | -29.25 | 394 |
| 32 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -17.02 | -3.85 | -21.73 | 101 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.66 | -24.50 | 173 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.36 | -20.64 | 175 | 18.3 | -24.85 | -4.17 | -27.04 | 261 |
| 38 | MFI reversion · 1h | reversion | 78.70 | -21.30 | 336 | 34.2 | -19.00 | -2.74 | -20.66 | 158 |
| 39 | Ichimoku · 1h | trend | 77.87 | -22.12 | 94 | 14.9 | -22.89 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.58 | -22.42 | 168 | 23.2 | -23.77 | -4.94 | -27.21 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.78 | -23.22 | 288 | 45.8 | -31.28 | -5.16 | -31.97 | 464 |
| 42 | EMA 20/50 cross · 1h | trend | 76.07 | -23.93 | 102 | 10.8 | -23.65 | -4.29 | -30.58 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.92 | -9.11 | -43.54 | 676 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.24 | -5.45 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -28.67 | -6.04 | -33.47 | 203 |
| 46 | Supertrend · 1h | trend | 73.62 | -26.38 | 166 | 13.3 | -30.11 | -5.24 | -34.80 | 216 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -28.09 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.34 | -26.66 | 335 | 23.0 | -36.26 | -6.47 | -38.81 | 485 |
| 49 | Z-score reversion · 1h | reversion | 73.16 | -26.84 | 162 | 35.8 | -25.28 | -3.77 | -28.10 | 233 |
| 50 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 251 | 40.2 | -31.28 | -5.37 | -34.52 | 372 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -37.50 | -6.14 | -39.70 | 535 |
| 52 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.93 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.65 | -28.36 | 140 | 20.0 | -29.94 | -5.53 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -30.10 | -6.36 | -34.09 | 286 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -37.94 | -7.46 | -38.14 | 382 |
| 56 | EMA 9/21 cross · 1h | trend | 67.30 | -32.70 | 242 | 9.9 | -40.42 | -8.37 | -40.61 | 337 |
| 57 | VWAP momentum · 1h | momentum | 67.17 | -32.83 | 777 | 22.1 | -55.84 | -12.28 | -55.85 | 1236 |
| 58 | Agent (ML meta-label) | meta | 66.38 | -33.62 | 1538 | 23.0 | -9.18 | -1.22 | -20.85 | 356 |
| 59 | RSI(14) reversion · 1h | reversion | 66.30 | -33.70 | 143 | 27.3 | -28.73 | -4.50 | -31.54 | 218 |
| 60 | Candlestick reversal · 1h | reversion | 65.48 | -34.52 | 407 | 28.5 | -38.14 | -7.06 | -38.71 | 571 |
| 61 | Three white soldiers | momentum | 65.22 | -34.78 | 462 | 15.8 | -48.22 | -22.41 | -48.27 | 643 |
| 62 | Max aggression: 1-day momentum | meta | 62.21 | -37.79 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -43.73 | -98.96 | 5230 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.76 | -25.08 | -80.78 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -44.69 | -93.53 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.31 | -31.04 | -89.31 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.89 | -38.22 | -90.89 | 2307 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.14 | -31.92 | -90.15 | 2190 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -50.93 | -97.74 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -53.01 | -96.34 | 3399 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.90 | -33.71 | -93.90 | 2451 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.65 | -34.72 | -82.65 | 1662 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -51.70 | -99.52 | 5977 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -41.93 | -92.78 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.71 | -37.54 | -95.71 | 3412 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -68.73 | -99.81 | 6202 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -41.48 | -91.95 | 2282 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.14 | -25.90 | -76.26 | 1589 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -59.37 | -97.75 | 3513 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -57.51 | -98.78 | 4885 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.08 | -28.60 | -70.08 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -51.68 | -94.75 | 2752 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.19 | -36.41 | -85.24 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -66.79 | -99.64 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.18 | -30.67 | -89.27 | 2291 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.63 | -19.32 | -77.82 | 1741 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.06 | -36.23 | -91.09 | 2238 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.57 | -50.01 | -96.58 | 3876 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.58 | -53.00 | -89.59 | 2169 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.50 | -28.24 | -66.55 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.55 | -24.03 | -73.56 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.18 | -17.64 | -78.66 | 1666 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -47.45 | -97.25 | 4329 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.44 | -99.93 | 8312 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-06T20:55 | MFI reversion · 1h | sell | PLTR | 4.64 | -0.03 | target is flat |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | BITX | 7.17 | 0.01 | target is flat |
| 2026-11-06T20:55 | MFI reversion · 1h | sell | AAPL | 6.03 | -0.03 | target is flat |
| 2026-11-06T20:55 | CCI reversion · 1h | buy | ETHU | 1.02 | — | entry |
| 2026-11-06T20:55 | CCI reversion · 1h | buy | COIN | 4.04 | — | entry |
| 2026-11-06T20:55 | CCI reversion · 1h | sell | XRP-USD | 5.06 | -0.08 | stop-loss |
| 2026-11-06T20:55 | Williams %R · 1h | buy | IWM | 4.52 | — | entry |
| 2026-11-06T20:55 | Williams %R · 1h | sell | XRP-USD | 5.40 | -0.14 | stop-loss |
| 2026-11-06T20:55 | RSI(14) reversion · 1h | buy | SOXL | 4.14 | — | entry |
| 2026-11-06T20:55 | RSI(14) reversion · 1h | sell | XRP-USD | 4.38 | -0.11 | stop-loss |
| 2026-11-06T20:55 | Candlestick reversal · 1h | buy | SOL-USD | 4.90 | — | entry |
| 2026-11-06T20:55 | Candlestick reversal · 1h | sell | QQQ | 4.67 | -0.02 | target is flat |
| 2026-11-06T20:55 | OBV trend · 1h | buy | AMZN | 17.75 | — | entry |
| 2026-11-06T20:55 | Opening range 30m | sell | TSLA | 12.80 | -0.07 | end-of-day flatten |
| 2026-11-06T20:55 | Opening range 30m | sell | TNA | 15.17 | 0.06 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-09 00:20:05.000162+00:00 -> 2026-11-07 00:30:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-09 00:20:05.000162+00:00 -> 2026-11-07 00:30:05.000162+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-09 00:20:05.000162+00:00 -> 2026-11-07 00:30:05.000162+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
