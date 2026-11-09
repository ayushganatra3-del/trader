# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T14:40:05.000116+00:00 · 53506 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.54 (-12.46%)

Closed trades 156, win rate 35.9%, fees £4.84, max drawdown -12.87%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 11910 decisions in 2382 calls, $0.1666 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T14:40 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-09T14:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-09T14:40 | 1 / 4 / 0 | SOL-USD 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 13.20 | 2.87 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.72 | 11.72 | 0 | — | 13.03 | 4.43 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.88 | 6.88 | 30 | 26.7 | 14.53 | 2.43 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | -1.29 | -0.18 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.10 | 1.10 | 0 | — | 4.63 | 1.35 | -6.60 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 97.28 | -2.72 | 121 | 34.7 | 5.60 | 2.90 | -2.27 | 88 |
| 9 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.54 | -3.46 | 7 | 42.9 | -5.36 | -0.35 | -18.69 | 8 |
| 12 | Hold SPY | benchmark | 95.58 | -4.42 | 0 | — | -3.05 | -0.96 | -6.18 | 1 |
| 13 | Agent (rotation) | meta | 95.48 | -4.52 | 176 | 27.8 | -7.75 | -4.44 | -12.12 | 179 |
| 14 | Gap and go | momentum | 94.21 | -5.79 | 172 | 27.9 | -1.07 | -0.26 | -9.06 | 237 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Trend pullback · 1h | trend | 93.28 | -6.72 | 108 | 23.1 | -13.05 | -4.78 | -17.86 | 78 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 91.67 | -8.34 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.36 | -9.64 | 0 | — | -7.19 | -2.11 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -15.17 | -4.92 | -15.99 | 580 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.13 | -2.83 | -14.15 | 80 |
| 23 | Copy: Insider buying | copy | 88.34 | -11.66 | 40 | 37.5 | -13.63 | -3.33 | -16.06 | 63 |
| 24 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -13.09 | -6.79 | -13.52 | 198 |
| 25 | Daily: Bullish score | daily | 87.34 | -12.66 | 15 | 20.0 | -8.15 | -1.23 | -16.58 | 14 |
| 26 | Hold BTC | benchmark | 86.41 | -13.59 | 1 | 0.0 | -5.86 | -0.68 | -15.58 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.65 | -14.35 | 166 | 27.1 | -11.34 | -2.05 | -20.98 | 220 |
| 28 | Donchian 55/20 · 1h | breakout | 84.67 | -15.33 | 71 | 14.1 | -13.90 | -2.85 | -20.86 | 103 |
| 29 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -16.05 | -4.57 | -18.49 | 92 |
| 30 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -20.27 | -5.98 | -20.93 | 717 |
| 31 | Stochastic reversion · 1h | reversion | 81.76 | -18.24 | 268 | 46.3 | -26.22 | -3.94 | -28.84 | 392 |
| 32 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -15.95 | -3.62 | -21.11 | 96 |
| 33 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -19.04 | -6.36 | -19.64 | 124 |
| 34 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.90 | -4.72 | -25.08 | 174 |
| 35 | Max aggression: 5-day momentum | meta | 80.31 | -19.69 | 17 | 47.1 | -36.14 | -2.40 | -42.04 | 25 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.08 | -19.92 | 2 | 0.0 | -12.03 | -1.62 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 78.80 | -21.20 | 178 | 18.5 | -25.22 | -4.14 | -28.38 | 262 |
| 38 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 39 | MFI reversion · 1h | reversion | 77.57 | -22.43 | 345 | 33.6 | -18.61 | -2.44 | -21.29 | 163 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -21.95 | -4.53 | -27.58 | 242 |
| 41 | Heikin-Ashi · 1h | trend | 77.06 | -22.94 | 394 | 23.1 | -40.22 | -8.22 | -41.90 | 668 |
| 42 | CCI reversion · 1h | reversion | 76.49 | -23.51 | 306 | 43.5 | -30.14 | -4.89 | -30.80 | 470 |
| 43 | EMA 20/50 cross · 1h | trend | 75.17 | -24.83 | 102 | 10.8 | -22.25 | -3.90 | -30.91 | 127 |
| 44 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.80 | -5.11 | -29.18 | 207 |
| 45 | Bollinger reversion · 1h | reversion | 73.78 | -26.22 | 263 | 39.2 | -29.60 | -4.95 | -33.98 | 374 |
| 46 | Supertrend · 1h | trend | 73.45 | -26.55 | 166 | 13.3 | -31.91 | -5.82 | -34.53 | 224 |
| 47 | Triple EMA stack · 1h | trend | 73.37 | -26.63 | 142 | 14.8 | -25.35 | -4.26 | -34.47 | 195 |
| 48 | RSI momentum · 1h | momentum | 73.36 | -26.64 | 158 | 12.7 | -26.53 | -4.93 | -33.05 | 210 |
| 49 | MACD cross · 1h | trend | 73.31 | -26.69 | 349 | 22.6 | -34.08 | -5.95 | -39.51 | 481 |
| 50 | Williams %R · 1h | reversion | 73.29 | -26.71 | 318 | 44.7 | -34.13 | -5.37 | -36.22 | 538 |
| 51 | Z-score reversion · 1h | reversion | 73.03 | -26.97 | 170 | 34.1 | -22.98 | -3.47 | -27.66 | 228 |
| 52 | OBV trend · 1h | momentum | 71.80 | -28.20 | 274 | 18.2 | -28.83 | -6.01 | -34.01 | 273 |
| 53 | Daily: Momentum burst | daily | 71.28 | -28.72 | 26 | 11.5 | -37.15 | -5.29 | -38.64 | 31 |
| 54 | ROC + volume · 1h | momentum | 70.62 | -29.38 | 349 | 25.5 | -37.71 | -7.29 | -39.42 | 378 |
| 55 | Donchian 20/10 · 1h | breakout | 70.42 | -29.58 | 141 | 19.9 | -30.23 | -5.60 | -35.35 | 209 |
| 56 | Agent (ML meta-label) | meta | 66.89 | -33.11 | 1551 | 23.1 | -5.60 | -0.90 | -17.19 | 338 |
| 57 | EMA 9/21 cross · 1h | trend | 66.61 | -33.39 | 246 | 9.8 | -37.58 | -7.51 | -39.14 | 326 |
| 58 | RSI(14) reversion · 1h | reversion | 66.50 | -33.49 | 151 | 26.5 | -28.60 | -4.33 | -32.60 | 238 |
| 59 | VWAP momentum · 1h | momentum | 65.66 | -34.34 | 801 | 21.6 | -53.98 | -11.90 | -53.98 | 1231 |
| 60 | Candlestick reversal · 1h | reversion | 64.65 | -35.35 | 429 | 28.0 | -37.95 | -7.14 | -38.18 | 590 |
| 61 | Three white soldiers | momentum | 62.47 | -37.53 | 488 | 15.0 | -48.85 | -22.62 | -48.86 | 646 |
| 62 | Max aggression: 1-day momentum | meta | 60.47 | -39.53 | 27 | 25.9 | -39.38 | -2.39 | -57.50 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -45.74 | -99.00 | 5289 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.30 | -26.28 | -80.31 | 1430 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -47.13 | -93.42 | 2504 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.47 | -32.29 | -89.55 | 1912 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.97 | -40.01 | -90.98 | 2307 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.67 | -90.03 | 2184 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -54.96 | -97.75 | 3477 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.39 | -58.15 | -96.39 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.64 | -32.47 | -93.69 | 2410 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.34 | -35.16 | -82.40 | 1649 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.87 | -99.54 | 5983 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -44.36 | -92.70 | 2602 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -37.42 | -95.57 | 3393 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -74.34 | -99.80 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.97 | -43.92 | -91.97 | 2274 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.37 | -24.76 | -76.37 | 1588 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -62.34 | -97.73 | 3498 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.47 | -98.85 | 4899 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.51 | -29.24 | -69.51 | 1204 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -55.00 | -94.68 | 2738 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.14 | -37.16 | -85.14 | 1766 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -76.03 | -99.66 | 6390 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.70 | -32.53 | -89.76 | 2310 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.51 | -20.13 | -78.58 | 1754 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.69 | -36.84 | -90.78 | 2214 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.81 | -53.02 | -96.82 | 3901 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.62 | -57.88 | -89.64 | 2165 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.14 | -29.12 | -66.24 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.24 | -24.18 | -72.24 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.46 | -19.03 | -79.73 | 1687 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.33 | -50.74 | -97.34 | 4335 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -110.75 | -99.93 | 8280 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T14:40 | Day trade: Stocks in Play ORB | buy | TNA | 24.33 | — | entry |
| 2026-11-09T14:40 | Day trade: Stocks in Play ORB | buy | SOXL | 24.33 | — | entry |
| 2026-11-09T14:40 | Day trade: Stocks in Play ORB | buy | ETHU | 24.33 | — | entry |
| 2026-11-09T14:40 | Agent (ML meta-label) | buy | TECL | 4.18 | — | entry |
| 2026-11-09T14:40 | Agent (ML meta-label) | sell | SPY | 3.49 | 0.00 | selected signal exited |
| 2026-11-09T14:40 | Agent (ML meta-label) | sell | BITX | 4.79 | -0.32 | selected signal exited |
| 2026-11-09T14:40 | Agent (ML meta-label) | sell | AAPL | 3.35 | 0.07 | selected signal exited |
| 2026-11-09T14:40 | Williams %R · 1h | buy | TSLA | 1.74 | — | entry |
| 2026-11-09T14:40 | Williams %R · 1h | buy | TNA | 4.58 | — | entry |
| 2026-11-09T14:40 | Williams %R · 1h | sell | MSTR | 6.32 | -0.21 | stop-loss |
| 2026-11-09T14:40 | Bollinger reversion · 1h | sell | IWM | 5.26 | 0.11 | take-profit |
| 2026-11-09T14:40 | Candlestick reversal · 1h | buy | ETH-USD | 3.46 | — | rebalance up |
| 2026-11-09T14:40 | Candlestick reversal · 1h | sell | BITX | 5.22 | -0.23 | stop-loss |
| 2026-11-09T14:40 | Ichimoku · 1h | sell | SQQQ | 18.37 | -1.19 | stop-loss |
| 2026-11-09T14:40 | EMA 20/50 cross · 1h | buy | SQQQ | 3.76 | — | rebalance up |
| 2026-11-09T14:40 | Gap and go | buy | UPRO | 11.78 | — | entry signal |
| 2026-11-09T14:40 | Gap and go | buy | TQQQ | 11.78 | — | entry signal |
| 2026-11-09T14:40 | Gap and go | buy | TNA | 11.78 | — | entry signal |
| 2026-11-09T14:40 | Gap and go | buy | TECL | 11.78 | — | entry signal |
| 2026-11-09T14:40 | Gap and go | buy | SOXL | 11.78 | — | entry signal |
| 2026-11-09T14:40 | Gap and go | buy | META | 11.78 | — | entry signal |
| 2026-11-09T14:40 | Gap and go | buy | IWM | 11.78 | — | entry signal |
| 2026-11-09T14:40 | Gap and go | buy | AMZN | 11.78 | — | entry signal |
| 2026-11-09T14:35 | Max aggression: 1-day momentum | buy | SOXL | 59.31 | — | entry |
| 2026-11-09T14:35 | Max aggression: 1-day momentum | sell | SQQQ | 59.31 | -2.89 | target is flat |
| 2026-11-09T14:35 | Agent (rotation) | buy | TQQQ | 31.67 | — | entry |
| 2026-11-09T14:35 | Agent (rotation) | buy | AAPL | 31.67 | — | entry |
| 2026-11-09T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | TQQQ | 105.83 | — | entry |
| 2026-11-09T14:35 | Agent (ML meta-label) | buy | SQQQ | 3.27 | — | following RSI(14) reversion |
| 2026-11-09T14:35 | Agent (ML meta-label) | buy | SPY | 3.48 | — | entry |
| 2026-11-09T14:35 | Agent (ML meta-label) | buy | SOL-USD | 3.71 | — | entry |
| 2026-11-09T14:35 | Agent (ML meta-label) | buy | QQQ | 3.71 | — | entry |
| 2026-11-09T14:35 | Agent (ML meta-label) | buy | DOGE-USD | 3.71 | — | entry |
| 2026-11-09T14:35 | Agent (ML meta-label) | buy | BTC-USD | 1.35 | — | entry |
| 2026-11-09T14:35 | Agent (ML meta-label) | sell | NVDA | 1.37 | -0.15 | selected signal exited |
| 2026-11-09T14:35 | Agent (ML meta-label) | sell | META | 3.82 | 0.11 | selected signal exited |
| 2026-11-09T14:35 | Agent (ML meta-label) | sell | LABU | 3.65 | -0.04 | selected signal exited |
| 2026-11-09T14:35 | Agent (ML meta-label) | sell | IWM | 3.45 | 0.03 | selected signal exited |
| 2026-11-09T14:35 | Agent (ML meta-label) | sell | GOOGL | 4.20 | 0.07 | selected signal exited |
| 2026-11-09T14:35 | Agent (ML meta-label) | sell | ETHU | 2.68 | -0.31 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 14:40:05.000116+00:00 -> 2026-11-09 14:50:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 14:40:05.000116+00:00 -> 2026-11-09 14:50:05.000116+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 14:40:05.000116+00:00 -> 2026-11-09 14:50:05.000116+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
