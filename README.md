# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-08T05:50:05.000143+00:00 · 51764 ticks

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
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 4572 decisions in 915 calls, $0.0639 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-08T05:50 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-08T05:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-08T05:50 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 1.95 | +8.75% | 6 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.81 | -1.19 | 125 | 46.4 | -12.38 | -2.91 | -13.75 | 147 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.46 | 2.83 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -6.88 | -3.99 | -10.35 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.54 | -0.42 | -9.14 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.97 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.76 | -5.92 | -17.86 | 80 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -12.86 | -3.08 | -15.96 | 62 |
| 23 | Daily: Bullish score | daily | 88.76 | -11.23 | 15 | 20.0 | -5.00 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.50 | -3.29 | -14.68 | 83 |
| 25 | Hold BTC | benchmark | 88.44 | -11.55 | 1 | 0.0 | -5.27 | -0.52 | -14.09 | 1 |
| 26 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -14.32 | -7.67 | -14.33 | 197 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -13.50 | -2.98 | -20.50 | 236 |
| 28 | Donchian 55/20 · 1h | breakout | 85.95 | -14.05 | 71 | 14.1 | -12.74 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.23 | -5.45 | -18.65 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.01 | -17.99 | 262 | 46.6 | -25.09 | -3.70 | -29.25 | 392 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.62 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.37 | -20.63 | 175 | 18.3 | -24.07 | -4.02 | -27.04 | 261 |
| 38 | MFI reversion · 1h | reversion | 78.29 | -21.71 | 337 | 34.1 | -18.89 | -2.71 | -20.14 | 156 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.74 | -4.65 | -29.43 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.46 | -4.88 | -27.58 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.44 | -23.56 | 292 | 45.5 | -29.90 | -4.91 | -30.33 | 465 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -22.22 | -4.01 | -30.58 | 128 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -43.05 | -9.02 | -43.05 | 677 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.63 | -5.30 | -29.20 | 209 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -28.81 | -6.10 | -33.48 | 203 |
| 46 | Supertrend · 1h | trend | 73.63 | -26.37 | 166 | 13.3 | -29.81 | -5.18 | -34.80 | 215 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -28.14 | -5.36 | -32.60 | 219 |
| 48 | Z-score reversion · 1h | reversion | 72.91 | -27.09 | 164 | 35.4 | -25.20 | -3.76 | -27.66 | 227 |
| 49 | MACD cross · 1h | trend | 72.86 | -27.14 | 341 | 23.2 | -34.92 | -6.18 | -38.92 | 478 |
| 50 | Bollinger reversion · 1h | reversion | 72.71 | -27.29 | 254 | 39.8 | -30.89 | -5.28 | -33.80 | 371 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -36.81 | -5.95 | -38.53 | 534 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.92 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.47 | -28.53 | 141 | 19.9 | -29.91 | -5.54 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.83 | -6.15 | -34.11 | 285 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -38.35 | -7.44 | -39.25 | 382 |
| 56 | EMA 9/21 cross · 1h | trend | 67.14 | -32.85 | 243 | 9.9 | -38.67 | -7.96 | -39.07 | 332 |
| 57 | VWAP momentum · 1h | momentum | 66.61 | -33.39 | 789 | 21.8 | -55.32 | -12.10 | -55.32 | 1240 |
| 58 | Agent (ML meta-label) | meta | 66.34 | -33.66 | 1540 | 23.0 | -10.50 | -1.78 | -19.80 | 350 |
| 59 | RSI(14) reversion · 1h | reversion | 66.13 | -33.87 | 143 | 27.3 | -29.91 | -4.71 | -31.54 | 223 |
| 60 | Candlestick reversal · 1h | reversion | 65.10 | -34.90 | 416 | 28.1 | -38.62 | -7.16 | -38.62 | 582 |
| 61 | Three white soldiers | momentum | 63.73 | -36.27 | 478 | 15.3 | -49.16 | -22.78 | -49.16 | 649 |
| 62 | Max aggression: 1-day momentum | meta | 62.24 | -37.76 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.38 | -98.98 | 5246 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.83 | -25.93 | -80.83 | 1436 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -46.10 | -93.42 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.95 | -31.90 | -88.95 | 1904 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.69 | -39.35 | -90.73 | 2301 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.06 | -31.68 | -90.06 | 2188 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -53.88 | -97.74 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -55.17 | -96.29 | 3395 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -33.55 | -93.67 | 2437 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.17 | -33.96 | -82.24 | 1648 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -53.16 | -99.53 | 6002 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.58 | -42.95 | -92.59 | 2598 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -37.75 | -95.68 | 3411 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.14 | -99.80 | 6184 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -43.11 | -91.74 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.31 | -24.53 | -75.37 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.97 | -97.76 | 3513 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.82 | -61.24 | -98.82 | 4892 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.84 | -28.96 | -69.93 | 1203 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -52.60 | -94.59 | 2738 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.54 | -36.19 | -84.57 | 1752 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -70.87 | -99.65 | 6385 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.51 | -31.73 | -89.51 | 2304 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.33 | -19.71 | -78.34 | 1760 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.26 | -37.43 | -91.27 | 2235 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.76 | -51.30 | -96.76 | 3907 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.59 | -55.32 | -89.59 | 2170 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.34 | -28.05 | -65.42 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.97 | -23.97 | -73.03 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.75 | -18.48 | -78.75 | 1676 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.29 | -49.11 | -97.29 | 4335 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -104.09 | -99.93 | 8308 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-08T05:35 | Three white soldiers | sell | SOL-USD | 15.85 | -0.11 | exit signal |
| 2026-11-08T05:15 | Three white soldiers | buy | SOL-USD | 15.96 | — | entry signal |
| 2026-11-08T05:00 | VWAP momentum · 1h | sell | ETH-USD | 6.62 | -0.04 | exit signal |
| 2026-11-08T04:00 | VWAP reversion · 1h | sell | SOL-USD | 24.65 | -0.13 | exit signal |
| 2026-11-08T04:00 | VWAP reversion · 1h | sell | DOGE-USD | 24.60 | -0.18 | exit signal |
| 2026-11-08T04:00 | Z-score reversion · 1h | sell | BTC-USD | 5.22 | -0.01 | exit signal |
| 2026-11-08T04:00 | Bollinger reversion · 1h | buy | SOL-USD | 5.01 | — | entry |
| 2026-11-08T04:00 | Bollinger reversion · 1h | sell | BTC-USD | 4.36 | -0.01 | exit signal |
| 2026-11-08T03:55 | Three white soldiers | sell | SOL-USD | 15.87 | -0.12 | exit signal |
| 2026-11-08T03:50 | Three white soldiers | buy | SOL-USD | 15.99 | — | entry signal |
| 2026-11-08T03:00 | VWAP momentum · 1h | buy | ETH-USD | 6.67 | — | entry signal |
| 2026-11-08T03:00 | VWAP momentum · 1h | buy | BTC-USD | 6.67 | — | entry signal |
| 2026-11-08T02:50 | Stochastic reversion · 1h | buy | XRP-USD | 2.28 | — | entry |
| 2026-11-08T02:50 | Stochastic reversion · 1h | sell | DOGE-USD | 2.28 | -0.05 | target is flat |
| 2026-11-08T02:50 | Bollinger reversion · 1h | buy | ETH-USD | 4.85 | — | entry |
| 2026-11-08T02:50 | Bollinger reversion · 1h | sell | DOGE-USD | 5.49 | -0.12 | target is flat |
| 2026-11-08T02:50 | Candlestick reversal · 1h | buy | XRP-USD | 4.03 | — | entry |
| 2026-11-08T02:50 | Candlestick reversal · 1h | sell | DOGE-USD | 4.03 | -0.06 | target is flat |
| 2026-11-08T02:00 | VWAP momentum · 1h | sell | BTC-USD | 7.36 | -0.05 | exit signal |
| 2026-11-08T01:00 | VWAP momentum · 1h | buy | BTC-USD | 7.42 | — | entry signal |
| 2026-11-08T01:00 | VWAP momentum · 1h | sell | ETH-USD | 7.36 | -0.05 | exit signal |
| 2026-11-08T00:05 | Agent | sell | DOGE-USD | 17.41 | -0.12 | selected signal exited |
| 2026-11-08T00:00 | Agent | buy | DOGE-USD | 17.53 | — | following Candlestick reversal · 1h |
| 2026-11-08T00:00 | CCI reversion · 1h | buy | DOGE-USD | 3.48 | — | entry signal |
| 2026-11-08T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.10 | — | entry signal |
| 2026-11-08T00:00 | VWAP momentum · 1h | buy | ETH-USD | 7.42 | — | entry signal |
| 2026-11-08T00:00 | MACD cross · 1h | buy | ETH-USD | 5.61 | — | entry signal |
| 2026-11-07T23:05 | Agent | sell | DOGE-USD | 17.46 | -0.09 | selected signal exited |
| 2026-11-07T23:05 | Candlestick reversal · 1h | sell | DOGE-USD | 4.10 | -0.02 | target is flat |
| 2026-11-07T23:00 | CCI reversion · 1h | buy | ETH-USD | 3.82 | — | entry signal |
| 2026-11-07T23:00 | MACD cross · 1h | buy | BTC-USD | 6.08 | — | entry signal |
| 2026-11-07T22:00 | Agent | buy | DOGE-USD | 17.55 | — | following Candlestick reversal · 1h |
| 2026-11-07T22:00 | VWAP reversion · 1h | buy | SOL-USD | 24.78 | — | entry signal |
| 2026-11-07T22:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.78 | — | entry signal |
| 2026-11-07T22:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.12 | — | entry signal |
| 2026-11-07T22:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.93 | — | entry signal |
| 2026-11-07T21:20 | CCI reversion · 1h | sell | DOGE-USD | 3.76 | -0.07 | stop-loss |
| 2026-11-07T21:15 | CCI reversion · 1h | sell | SOL-USD | 3.95 | -0.09 | stop-loss |
| 2026-11-07T21:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.26 | -0.03 | exit signal |
| 2026-11-07T21:00 | MACD cross · 1h | sell | BTC-USD | 6.65 | -0.00 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-10 05:50:05.000143+00:00 -> 2026-11-08 06:00:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-10 05:50:05.000143+00:00 -> 2026-11-08 06:00:05.000143+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-10 05:50:05.000143+00:00 -> 2026-11-08 06:00:05.000143+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
