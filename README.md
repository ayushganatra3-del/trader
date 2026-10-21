# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T03:25:05.000132+00:00 · 30257 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.86 (-9.14%)

Closed trades 90, win rate 41.1%, fees £2.98, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.22 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 2670 decisions in 534 calls, $0.0373 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T03:25 | 3 / 1 / 1 | cash |  |
| Breezy | 2026-10-21T03:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-21T03:25 | 2 / 2 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.77 | +3.00% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.11 | 6.11 | 0 | — | 8.23 | 3.84 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.74 | 0.74 | 9 | 44.4 | -13.29 | -0.93 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.02 | -0.98 | 0 | — | 0.33 | 0.23 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 62 | 35.5 | 4.20 | 2.21 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.51 | -1.49 | 0 | — | -0.73 | -0.22 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.09 | -1.91 | 3 | 33.3 | 4.26 | 0.99 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.84 | -2.16 | 0 | — | 18.92 | 2.55 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.83 | -2.16 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.98 | -3.02 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.84 | -3.16 | 0 | — | 0.02 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.31 | -3.69 | 40 | 15.0 | -14.48 | -2.90 | -15.92 | 99 |
| 19 | Copy: Insider buying | copy | 96.17 | -3.83 | 25 | 40.0 | -11.99 | -2.06 | -20.62 | 72 |
| 20 | Agent (rotation) | meta | 96.09 | -3.91 | 114 | 31.6 | -6.34 | -3.12 | -8.16 | 302 |
| 21 | Trend pullback · 1h | trend | 95.71 | -4.29 | 90 | 23.3 | -20.34 | -6.15 | -20.85 | 131 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.63 | -5.37 | 89 | 18.0 | -13.81 | -2.61 | -16.12 | 253 |
| 24 | Daily: Momentum burst | daily | 94.15 | -5.85 | 6 | 16.7 | -6.94 | -0.92 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.71 | 1.50 | -6.51 | 196 |
| 26 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -13.40 | -3.91 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.87 | -8.13 | 105 | 21.9 | -17.81 | -3.82 | -20.69 | 271 |
| 28 | Squeeze breakout · 1h | breakout | 91.71 | -8.29 | 46 | 21.7 | -3.35 | -0.74 | -11.48 | 98 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.25 | -2.32 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.17 | -8.83 | 7 | 0.0 | -7.95 | -0.90 | -13.10 | 13 |
| 31 | Agent | meta | 90.86 | -9.14 | 90 | 41.1 | -10.84 | -5.30 | -13.58 | 240 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.83 | -9.17 | 0 | — | 0.92 | 0.30 | -14.37 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.65 | -9.35 | 85 | 22.4 | -12.73 | -2.28 | -14.09 | 104 |
| 34 | Bollinger breakout · 1h | breakout | 90.61 | -9.39 | 87 | 29.9 | -12.80 | -2.40 | -16.36 | 258 |
| 35 | Connors RSI(2) · 1h | reversion | 89.36 | -10.64 | 151 | 41.7 | -22.19 | -6.62 | -23.77 | 196 |
| 36 | RSI momentum · 1h | momentum | 89.32 | -10.68 | 83 | 15.7 | -24.49 | -4.77 | -25.28 | 217 |
| 37 | EMA 20/50 cross · 1h | trend | 88.68 | -11.32 | 62 | 12.9 | -19.15 | -3.52 | -21.41 | 132 |
| 38 | Opening range 15m | breakout | 88.26 | -11.74 | 270 | 29.3 | -17.73 | -4.78 | -20.79 | 699 |
| 39 | Supertrend · 1h | trend | 88.21 | -11.79 | 88 | 12.5 | -21.43 | -4.19 | -26.62 | 222 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -12.34 | -2.80 | -19.91 | 121 |
| 41 | Stochastic reversion · 1h | reversion | 87.79 | -12.21 | 164 | 47.0 | -14.70 | -2.45 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.35 | -12.65 | 60 | 21.7 | -18.93 | -3.39 | -26.64 | 207 |
| 43 | Ichimoku · 1h | trend | 86.90 | -13.11 | 60 | 13.3 | -19.04 | -3.59 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.32 | -13.68 | 193 | 20.2 | -26.10 | -4.93 | -33.71 | 467 |
| 45 | Triple EMA stack · 1h | trend | 85.39 | -14.61 | 91 | 14.3 | -30.97 | -5.77 | -31.81 | 229 |
| 46 | Donchian 20/10 · 1h | breakout | 84.66 | -15.34 | 81 | 17.3 | -18.28 | -3.03 | -28.55 | 220 |
| 47 | Z-score reversion · 1h | reversion | 84.54 | -15.46 | 96 | 30.2 | -14.30 | -2.35 | -21.32 | 195 |
| 48 | MFI reversion · 1h | reversion | 83.90 | -16.10 | 220 | 30.5 | -15.01 | -2.36 | -20.43 | 140 |
| 49 | OBV trend · 1h | momentum | 83.90 | -16.10 | 186 | 17.2 | -35.58 | -6.04 | -35.72 | 317 |
| 50 | Agent (ML meta-label) | meta | 83.70 | -16.30 | 711 | 19.1 | -7.57 | -1.23 | -15.28 | 350 |
| 51 | MACD zero-line · 1h | trend | 83.67 | -16.33 | 89 | 14.6 | -25.45 | -5.01 | -26.48 | 226 |
| 52 | Three white soldiers | momentum | 82.36 | -17.64 | 252 | 19.4 | -47.00 | -18.36 | -47.63 | 616 |
| 53 | Bollinger reversion · 1h | reversion | 82.23 | -17.77 | 162 | 35.8 | -29.42 | -5.70 | -32.84 | 347 |
| 54 | Williams %R · 1h | reversion | 81.41 | -18.59 | 195 | 43.6 | -30.71 | -4.75 | -36.49 | 524 |
| 55 | ROC + volume · 1h | momentum | 81.39 | -18.61 | 208 | 22.6 | -29.33 | -5.43 | -34.11 | 392 |
| 56 | CCI reversion · 1h | reversion | 80.77 | -19.23 | 178 | 41.6 | -18.25 | -2.28 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.18 | -19.82 | 233 | 20.6 | -43.95 | -9.41 | -47.30 | 673 |
| 58 | RSI(14) reversion · 1h | reversion | 79.61 | -20.39 | 83 | 22.9 | -15.38 | -2.71 | -23.28 | 184 |
| 59 | EMA 9/21 cross · 1h | trend | 79.61 | -20.39 | 143 | 10.5 | -29.34 | -6.11 | -30.12 | 326 |
| 60 | VWAP momentum · 1h | momentum | 77.71 | -22.29 | 467 | 20.6 | -45.43 | -8.18 | -50.19 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 77.42 | -22.58 | 226 | 28.8 | -37.05 | -6.85 | -38.89 | 543 |
| 62 | Max aggression: 1-day momentum | meta | 77.11 | -22.89 | 17 | 29.4 | -27.91 | -1.54 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.21 | -38.79 | 632 | 22.9 | -77.51 | -21.59 | -78.40 | 1721 |
| 64 | Volume breakout | breakout | 60.99 | -39.01 | 382 | 13.9 | -63.75 | -19.66 | -64.14 | 867 |
| 65 | Squeeze breakout | breakout | 58.26 | -41.73 | 493 | 14.0 | -66.05 | -22.25 | -66.80 | 1204 |
| 66 | RSI(14) reversion | reversion | 57.37 | -42.63 | 745 | 26.6 | -74.24 | -16.28 | -74.89 | 1624 |
| 67 | Donchian 55/20 | breakout | 57.35 | -42.65 | 508 | 19.1 | -70.87 | -17.76 | -73.51 | 1279 |
| 68 | EMA 20/50 cross | trend | 55.56 | -44.44 | 555 | 19.6 | -78.00 | -17.07 | -80.87 | 1440 |
| 69 | VWAP reversion | reversion | 53.59 | -46.41 | 754 | 25.2 | -71.40 | -14.46 | -72.28 | 1489 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -30.03 | -98.77 | 5267 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.54 | -31.12 | -94.05 | 2597 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.43 | -21.96 | -88.48 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -24.82 | -91.50 | 2358 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.22 | -26.24 | -91.39 | 2255 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -33.97 | -97.71 | 3518 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.77 | -37.29 | -96.86 | 3602 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -28.09 | -94.43 | 2531 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.65 | -27.64 | -82.98 | 1709 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.19 | -99.38 | 5747 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.76 | -27.51 | -92.44 | 2626 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.98 | -31.67 | -95.98 | 3467 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -41.34 | -99.75 | 6189 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.56 | -29.16 | -91.68 | 2353 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -38.44 | -97.73 | 3614 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.02 | -98.46 | 4710 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.07 | -35.20 | -94.21 | 2801 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.22 | -27.61 | -83.94 | 1805 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.36 | -99.52 | 6189 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.71 | -22.18 | -87.01 | 2146 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.76 | -25.96 | -88.10 | 2138 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.43 | -95.95 | 3766 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.21 | -33.09 | -89.43 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.64 | -32.65 | -95.77 | 4107 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.90 | -99.91 | 8290 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T03:25 | VWAP reversion | buy | SOL-USD | 13.41 | — | entry signal |
| 2026-10-21T03:20 | Donchian 55/20 | sell | XRP-USD | 11.50 | -0.07 | exit signal |
| 2026-10-21T03:05 | EMA 20/50 cross | sell | XRP-USD | 11.20 | 0.13 | exit signal |
| 2026-10-21T03:00 | Connors RSI(2) · 1h | buy | BTC-USD | 22.36 | — | entry signal |
| 2026-10-21T03:00 | Volume breakout · 1h | sell | BTC-USD | 22.70 | -0.12 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | XRP-USD | 6.29 | 0.04 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | SOL-USD | 6.27 | 0.02 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | ETH-USD | 6.27 | 0.02 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | DOGE-USD | 6.28 | 0.03 | exit signal |
| 2026-10-21T03:00 | ROC + volume · 1h | sell | BTC-USD | 5.81 | -0.00 | exit signal |
| 2026-10-21T03:00 | VWAP momentum · 1h | sell | XRP-USD | 8.68 | 0.10 | exit signal |
| 2026-10-21T03:00 | VWAP momentum · 1h | sell | ETH-USD | 8.66 | 0.05 | exit signal |
| 2026-10-21T03:00 | VWAP momentum · 1h | sell | DOGE-USD | 8.67 | 0.08 | exit signal |
| 2026-10-21T03:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 7.90 | -0.05 | exit signal |
| 2026-10-21T02:45 | EMA 20/50 cross | sell | ETH-USD | 13.88 | -0.05 | exit signal |
| 2026-10-21T02:25 | EMA 20/50 cross | sell | BTC-USD | 13.91 | -0.01 | exit signal |
| 2026-10-21T02:20 | EMA 20/50 cross | sell | SOL-USD | 13.86 | -0.05 | exit signal |
| 2026-10-21T02:15 | Donchian 55/20 | sell | DOGE-USD | 11.50 | -0.06 | exit signal |
| 2026-10-21T02:05 | Volume breakout | sell | XRP-USD | 15.15 | -0.13 | exit signal |
| 2026-10-21T01:50 | Volume breakout | buy | XRP-USD | 15.28 | — | entry signal |
| 2026-10-21T01:45 | OBV trend · 1h | sell | SOL-USD | 4.76 | -0.01 | rebalance down |
| 2026-10-21T01:45 | OBV trend · 1h | sell | BTC-USD | 4.80 | -0.02 | rebalance down |
| 2026-10-21T01:10 | Squeeze breakout | sell | DOGE-USD | 14.46 | -0.14 | stop-loss |
| 2026-10-21T01:10 | Donchian 55/20 | sell | BTC-USD | 14.33 | -0.11 | stop-loss |
| 2026-10-21T01:00 | VWAP momentum · 1h | sell | BTC-USD | 8.65 | 0.03 | exit signal |
| 2026-10-21T01:00 | Volume breakout | sell | ETH-USD | 15.19 | -0.12 | exit signal |
| 2026-10-21T00:55 | Volume breakout | buy | ETH-USD | 15.31 | — | entry signal |
| 2026-10-21T00:46 | Squeeze breakout | buy | DOGE-USD | 14.60 | — | entry signal |
| 2026-10-20T23:30 | Donchian 55/20 | sell | SOL-USD | 14.33 | -0.14 | exit signal |
| 2026-10-20T23:10 | Squeeze breakout | sell | DOGE-USD | 14.49 | -0.15 | stop-loss |
| 2026-10-20T23:10 | Donchian 55/20 | buy | BTC-USD | 8.62 | — | rebalance up |
| 2026-10-20T23:10 | Donchian 55/20 | sell | ETH-USD | 14.31 | -0.13 | stop-loss |
| 2026-10-20T23:10 | ROC + volume | sell | DOGE-USD | 15.25 | -0.16 | stop-loss |
| 2026-10-20T23:05 | Keltner breakout | sell | DOGE-USD | 12.45 | -0.12 | Kill switch: down 50% from peak |
| 2026-10-20T23:05 | Keltner breakout | sell | BTC-USD | 12.53 | -0.05 | Kill switch: down 50% from peak |
| 2026-10-20T23:05 | ROC + volume | sell | SOL-USD | 15.35 | -0.07 | stop-loss |
| 2026-10-20T23:00 | Volume breakout | sell | DOGE-USD | 15.21 | -0.14 | exit signal |
| 2026-10-20T23:00 | Keltner breakout | sell | ETH-USD | 12.53 | -0.06 | exit signal |
| 2026-10-20T22:45 | Keltner breakout | sell | XRP-USD | 12.41 | -0.13 | stop-loss |
| 2026-10-20T22:45 | ROC + volume | sell | XRP-USD | 15.25 | -0.16 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 03:25:05.000132+00:00 -> 2026-10-21 03:35:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
