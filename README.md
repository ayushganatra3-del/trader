# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T19:10:05.000138+00:00 · 57262 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.89 (-14.11%)

Closed trades 186, win rate 35.5%, fees £5.49, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 17.25 | +0.07 |
| SQQQ | 17.12 | -0.05 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 32807 decisions in 3008 calls, $0.4098 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T19:10 | 4 / 18 / 8 | cash |  |
| Breezy | 2026-11-12T19:10 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-12T19:10 | 8 / 21 / 1 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.36 | +7.92% | 5 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.48 | 17.48 | 0 | — | 15.95 | 5.29 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.41 | 13.41 | 21 | 66.7 | 19.76 | 3.89 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.51 | 12.51 | 33 | 27.3 | 20.79 | 3.08 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.45 | 4.45 | 0 | — | 6.54 | 1.80 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.89 | 0.89 | 137 | 33.6 | 7.32 | 2.87 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.70 | 1.90 | -9.06 | 232 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold SPY | benchmark | 98.81 | -1.19 | 0 | — | -0.10 | 0.05 | -6.18 | 1 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.51 | 0.06 | -18.69 | 5 |
| 12 | Agent (rotation) | meta | 98.30 | -1.70 | 190 | 30.5 | -1.61 | -0.54 | -8.93 | 169 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 98.07 | -1.93 | 1 | 0.0 | -1.95 | -1.32 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.75 | -3.25 | 0 | — | -3.56 | -0.90 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.43 | -4.57 | 142 | 47.2 | -12.83 | -3.32 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.07 | -4.93 | 43 | 39.5 | -6.51 | -1.27 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.70 | -5.30 | 0 | — | -3.04 | -0.77 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 93.66 | -6.34 | 1 | 0.0 | -6.68 | -1.45 | -16.91 | 2 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 21 | Trend pullback · 1h | trend | 92.07 | -7.93 | 109 | 22.9 | -13.15 | -4.58 | -17.88 | 74 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -7.51 | -2.38 | -14.89 | 75 |
| 23 | Parabolic SAR · 1h | trend | 86.49 | -13.51 | 171 | 27.5 | -13.68 | -2.91 | -21.98 | 221 |
| 24 | Opening range 30m | breakout | 86.21 | -13.79 | 419 | 32.7 | -10.29 | -3.27 | -14.11 | 604 |
| 25 | Agent | meta | 85.89 | -14.11 | 186 | 35.5 | -15.52 | -7.67 | -16.27 | 211 |
| 26 | Daily: Bullish score | daily | 84.91 | -15.09 | 16 | 18.8 | -10.51 | -1.62 | -19.56 | 15 |
| 27 | Agent (aggressive) | meta | 84.67 | -15.33 | 90 | 34.4 | -15.68 | -4.34 | -18.51 | 102 |
| 28 | Hold BTC | benchmark | 84.41 | -15.59 | 1 | 0.0 | -7.89 | -1.00 | -18.34 | 1 |
| 29 | Donchian 55/20 · 1h | breakout | 84.05 | -15.96 | 73 | 13.7 | -22.36 | -4.68 | -29.68 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.67 | -17.33 | 2 | 0.0 | -8.22 | -0.91 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.66 | -18.34 | 114 | 23.7 | -18.29 | -3.77 | -25.92 | 177 |
| 32 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -26.38 | -1.37 | -45.81 | 24 |
| 33 | ADX DI cross · 1h | trend | 81.13 | -18.87 | 191 | 19.4 | -20.99 | -3.40 | -29.55 | 267 |
| 34 | Connors RSI(2) · 1h | reversion | 81.09 | -18.91 | 210 | 40.5 | -18.04 | -6.16 | -18.87 | 118 |
| 35 | Volume breakout · 1h | breakout | 80.36 | -19.64 | 158 | 28.5 | -13.61 | -3.17 | -21.12 | 91 |
| 36 | MFI reversion · 1h | reversion | 80.08 | -19.92 | 381 | 36.0 | -18.03 | -2.28 | -23.02 | 163 |
| 37 | Stochastic reversion · 1h | reversion | 79.69 | -20.32 | 297 | 47.5 | -26.33 | -3.86 | -27.07 | 390 |
| 38 | Opening range 15m | breakout | 78.56 | -21.44 | 512 | 31.2 | -17.78 | -4.81 | -21.36 | 726 |
| 39 | Heikin-Ashi · 1h | trend | 77.85 | -22.15 | 432 | 24.8 | -35.92 | -6.72 | -38.20 | 658 |
| 40 | MACD cross · 1h | trend | 77.34 | -22.66 | 370 | 21.9 | -28.18 | -4.27 | -38.74 | 465 |
| 41 | Bollinger breakout · 1h | breakout | 76.31 | -23.69 | 179 | 22.3 | -22.20 | -4.59 | -29.92 | 241 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -19.82 | -0.58 | -57.50 | 41 |
| 43 | MACD zero-line · 1h | trend | 75.79 | -24.21 | 164 | 17.1 | -21.55 | -4.20 | -30.95 | 204 |
| 44 | Supertrend · 1h | trend | 75.67 | -24.33 | 172 | 14.0 | -28.47 | -5.13 | -35.51 | 218 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 46 | RSI momentum · 1h | momentum | 75.14 | -24.86 | 162 | 13.6 | -23.96 | -3.69 | -36.52 | 212 |
| 47 | EMA 20/50 cross · 1h | trend | 74.71 | -25.29 | 105 | 10.5 | -26.72 | -4.50 | -37.99 | 121 |
| 48 | Daily: Momentum burst | daily | 74.49 | -25.51 | 27 | 11.1 | -34.15 | -4.65 | -37.90 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.33 | -26.67 | 147 | 14.3 | -25.40 | -4.20 | -36.53 | 205 |
| 50 | ROC + volume · 1h | momentum | 73.20 | -26.80 | 385 | 27.8 | -30.69 | -5.66 | -38.31 | 378 |
| 51 | Bollinger reversion · 1h | reversion | 72.56 | -27.44 | 290 | 41.0 | -31.50 | -4.88 | -35.66 | 378 |
| 52 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -36.55 | -5.66 | -36.70 | 458 |
| 53 | Donchian 20/10 · 1h | breakout | 72.21 | -27.79 | 145 | 19.3 | -27.89 | -5.07 | -35.87 | 211 |
| 54 | OBV trend · 1h | momentum | 71.71 | -28.29 | 289 | 19.4 | -26.30 | -4.50 | -36.23 | 287 |
| 55 | Williams %R · 1h | reversion | 68.20 | -31.80 | 358 | 45.5 | -42.04 | -6.89 | -42.22 | 530 |
| 56 | Z-score reversion · 1h | reversion | 67.82 | -32.18 | 199 | 38.2 | -27.49 | -3.81 | -29.17 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 67.32 | -32.68 | 257 | 9.7 | -33.23 | -6.16 | -41.74 | 333 |
| 58 | VWAP momentum · 1h | momentum | 66.58 | -33.42 | 886 | 22.5 | -51.04 | -10.53 | -51.71 | 1218 |
| 59 | Agent (ML meta-label) | meta | 66.43 | -33.57 | 1808 | 24.9 | -13.30 | -1.66 | -21.04 | 342 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -35.71 | -5.20 | -35.79 | 245 |
| 61 | Candlestick reversal · 1h | reversion | 62.91 | -37.09 | 468 | 28.4 | -41.13 | -7.25 | -41.23 | 591 |
| 62 | Three white soldiers | momentum | 58.67 | -41.33 | 536 | 14.6 | -49.58 | -22.58 | -49.58 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -44.46 | -99.01 | 5279 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.18 | -26.11 | -80.18 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.79 | -46.54 | -93.79 | 2532 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.41 | -32.39 | -89.59 | 1932 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -41.43 | -91.22 | 2333 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.20 | -32.13 | -90.25 | 2218 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -53.85 | -97.89 | 3478 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -57.38 | -96.38 | 3431 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.45 | -32.31 | -93.46 | 2322 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.10 | -34.67 | -83.10 | 1655 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -55.66 | -99.57 | 5981 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.28 | -43.97 | -92.28 | 2605 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -37.12 | -95.43 | 3471 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -79.17 | -99.82 | 6140 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.41 | -44.22 | -92.41 | 2277 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.20 | -25.40 | -75.20 | 1620 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -60.40 | -97.66 | 3513 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -63.80 | -98.88 | 4902 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.52 | -27.07 | -68.52 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.78 | -58.81 | -94.78 | 2782 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.12 | -39.51 | -85.12 | 1790 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -76.92 | -99.66 | 6349 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.85 | -32.73 | -90.00 | 2295 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.84 | -19.91 | -78.33 | 1760 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.71 | -36.92 | -90.88 | 2189 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.86 | -52.45 | -96.87 | 3855 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.19 | -57.97 | -89.19 | 2152 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.28 | -30.44 | -66.28 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.52 | -23.19 | -71.63 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.06 | -18.89 | -79.36 | 1708 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.31 | -50.06 | -97.34 | 4301 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -117.34 | -99.93 | 8362 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T19:10 | Agent (ML meta-label) | sell | TSLA | 1.13 | -0.00 | selected signal exited |
| 2026-11-12T19:10 | Agent (ML meta-label) | sell | IWM | 3.90 | -0.01 | selected signal exited |
| 2026-11-12T19:05 | Agent (ML meta-label) | buy | TSLA | 1.13 | — | entry |
| 2026-11-12T19:01 | Agent (ML meta-label) | buy | SPY | 3.91 | — | entry |
| 2026-11-12T19:01 | Agent (ML meta-label) | buy | IWM | 3.91 | — | entry |
| 2026-11-12T19:01 | Agent (ML meta-label) | buy | AAPL | 3.91 | — | entry |
| 2026-11-12T19:01 | Agent (ML meta-label) | sell | TSLA | 3.91 | 0.00 | selected signal exited |
| 2026-11-12T19:01 | Candlestick reversal · 1h | sell | BTC-USD | 5.72 | -0.02 | exit signal |
| 2026-11-12T18:55 | Agent (ML meta-label) | sell | PLTR | 3.91 | -0.00 | selected signal exited |
| 2026-11-12T18:55 | Agent (ML meta-label) | sell | IWM | 3.90 | -0.01 | selected signal exited |
| 2026-11-12T18:55 | Agent | buy | SQQQ | 17.17 | — | following RSI momentum |
| 2026-11-12T18:55 | Agent | sell | AMD | 17.03 | -0.18 | selected signal exited |
| 2026-11-12T18:51 | Agent (ML meta-label) | buy | TSLA | 3.91 | — | entry |
| 2026-11-12T18:51 | Agent (ML meta-label) | buy | PLTR | 3.91 | — | entry |
| 2026-11-12T18:51 | Agent (ML meta-label) | buy | IWM | 3.91 | — | entry |
| 2026-11-12T18:51 | Agent (ML meta-label) | sell | SPY | 4.16 | -0.01 | selected signal exited |
| 2026-11-12T18:51 | Agent (ML meta-label) | sell | AAPL | 4.16 | -0.00 | selected signal exited |
| 2026-11-12T18:51 | Agent (aggressive) | buy | LABU | 42.25 | — | following MFI reversion |
| 2026-11-12T18:51 | Agent | buy | LABU | 17.18 | — | following MFI reversion |
| 2026-11-12T18:51 | Opening range 30m | sell | MSFT | 6.19 | -0.05 | stop-loss |
| 2026-11-12T18:45 | Agent (ML meta-label) | buy | SPY | 4.17 | — | entry |
| 2026-11-12T18:45 | Agent (ML meta-label) | buy | AAPL | 4.17 | — | entry |
| 2026-11-12T18:45 | Agent (ML meta-label) | sell | META | 4.16 | -0.01 | selected signal exited |
| 2026-11-12T18:45 | Agent (ML meta-label) | sell | IWM | 4.17 | -0.01 | selected signal exited |
| 2026-11-12T18:45 | MFI reversion · 1h | buy | SPY | 6.69 | — | entry |
| 2026-11-12T18:45 | MFI reversion · 1h | buy | MSFT | 4.12 | — | rebalance up |
| 2026-11-12T18:45 | MFI reversion · 1h | sell | SOXL | 6.16 | -0.02 | target is flat |
| 2026-11-12T18:45 | MFI reversion · 1h | sell | META | 8.90 | -0.02 | target is flat |
| 2026-11-12T18:45 | Volume breakout · 1h | sell | AAPL | 20.12 | 0.04 | target is flat |
| 2026-11-12T18:45 | OBV trend · 1h | buy | TNA | 8.99 | — | entry |
| 2026-11-12T18:45 | OBV trend · 1h | sell | SPY | 8.97 | -0.02 | target is flat |
| 2026-11-12T18:45 | VWAP momentum · 1h | buy | TSLA | 5.95 | — | entry |
| 2026-11-12T18:45 | VWAP momentum · 1h | sell | MSFT | 5.44 | 0.01 | target is flat |
| 2026-11-12T18:41 | Agent (ML meta-label) | buy | META | 4.17 | — | entry |
| 2026-11-12T18:40 | Agent (ML meta-label) | sell | TSLA | 1.90 | -0.00 | selected signal exited |
| 2026-11-12T18:35 | Agent (ML meta-label) | buy | IWM | 4.18 | — | entry |
| 2026-11-12T18:35 | Agent (ML meta-label) | sell | UPRO | 3.60 | 0.00 | selected signal exited |
| 2026-11-12T18:35 | Agent (ML meta-label) | sell | PLTR | 3.71 | 0.00 | selected signal exited |
| 2026-11-12T18:35 | Agent (ML meta-label) | sell | AAPL | 3.70 | -0.02 | selected signal exited |
| 2026-11-12T18:30 | Agent (ML meta-label) | buy | UPRO | 3.60 | — | following Gap and go |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 19:10:05.000138+00:00 -> 2026-11-12 19:20:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
