# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T23:05:05.000108+00:00 · 76036 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £75.26 (-24.74%)

Closed trades 253, win rate 35.6%, fees £6.93, max drawdown -25.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.18 | -0.11 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-27 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-27)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 23.81 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.6, TSLA 6.2, SQQQ 6.0, LABU 3.9, META 3.7, PLTR 2.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 30195 decisions in 3618 calls, $0.3877 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T23:05 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-27T23:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T23:05 | 3 / 2 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.45 | +1.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.21 | 3.62 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.61 | 16.61 | 0 | — | 15.04 | 5.08 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 106.20 | 6.20 | 0 | — | 4.92 | 1.36 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.46 | -1.54 | 225 | 31.6 | 0.20 | 0.15 | -7.66 | 213 |
| 9 | Three white soldiers · 1h | momentum | 95.82 | -4.18 | 24 | 12.5 | -2.34 | -1.77 | -6.24 | 25 |
| 10 | Hold SPY | benchmark | 95.80 | -4.20 | 0 | — | -4.97 | -1.22 | -11.71 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 95.26 | -4.74 | 172 | 32.6 | -4.54 | -3.93 | -5.85 | 54 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.86 | -7.38 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 95.20 | -4.80 | 0 | — | -4.63 | -0.85 | -13.24 | 1 |
| 14 | Agent (rotation) | meta | 95.15 | -4.85 | 236 | 28.8 | 0.62 | 0.28 | -5.95 | 161 |
| 15 | Copy: Insider buying | copy | 94.72 | -5.28 | 64 | 42.2 | -1.48 | -0.12 | -14.79 | 70 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.59 | -9.41 | 0 | — | -10.32 | -2.18 | -17.03 | 1 |
| 17 | Trend pullback · 1h | trend | 90.58 | -9.42 | 117 | 23.9 | -8.48 | -4.90 | -10.61 | 31 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.47 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 88.10 | -11.90 | 490 | 33.9 | -7.93 | -2.35 | -15.30 | 553 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.94 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.44 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.13 | -15.87 | 20 | 20.0 | -14.90 | -3.35 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.01 | -6.08 | -17.05 | 79 |
| 25 | Opening range 15m | breakout | 79.86 | -20.14 | 618 | 31.9 | -17.41 | -4.79 | -24.20 | 679 |
| 26 | Connors RSI(2) · 1h | reversion | 78.44 | -21.56 | 228 | 41.2 | -14.60 | -6.65 | -14.74 | 60 |
| 27 | Volume breakout · 1h | breakout | 76.81 | -23.19 | 181 | 30.4 | -21.54 | -8.64 | -21.71 | 70 |
| 28 | Parabolic SAR · 1h | trend | 76.61 | -23.39 | 221 | 27.1 | -31.34 | -7.85 | -33.65 | 185 |
| 29 | Max aggression: 5-day momentum | meta | 76.50 | -23.50 | 27 | 37.0 | -51.07 | -2.49 | -67.33 | 21 |
| 30 | Agent (aggressive) | meta | 75.56 | -24.43 | 115 | 33.0 | -15.66 | -4.41 | -16.35 | 91 |
| 31 | Agent | meta | 75.26 | -24.74 | 253 | 35.6 | -27.58 | -6.26 | -27.63 | 203 |
| 32 | Donchian 55/20 · 1h | breakout | 73.49 | -26.51 | 91 | 13.2 | -30.63 | -8.20 | -31.23 | 82 |
| 33 | Keltner breakout · 1h | breakout | 73.06 | -26.94 | 147 | 23.8 | -26.29 | -6.52 | -27.60 | 151 |
| 34 | Ichimoku · 1h | trend | 72.91 | -27.09 | 119 | 15.1 | -29.53 | -7.55 | -30.65 | 101 |
| 35 | Daily: Momentum burst | daily | 71.69 | -28.31 | 31 | 16.1 | -31.57 | -4.30 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.32 | -28.68 | 274 | 19.7 | -37.25 | -6.98 | -39.61 | 279 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 70.22 | -29.78 | 3 | 0.0 | -22.00 | -2.60 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 69.20 | -30.80 | 3 | 0.0 | -29.33 | -5.24 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.93 | -31.07 | 418 | 40.7 | -30.00 | -3.01 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 68.37 | -31.63 | 225 | 18.7 | -38.20 | -7.35 | -41.52 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.73 | -32.27 | 220 | 23.2 | -29.95 | -7.87 | -31.73 | 211 |
| 42 | OBV trend · 1h | momentum | 66.08 | -33.91 | 333 | 19.5 | -39.74 | -9.70 | -40.13 | 214 |
| 43 | Max aggression: 1-day momentum | meta | 66.00 | -34.00 | 35 | 28.6 | -56.20 | -3.63 | -63.62 | 38 |
| 44 | EMA 20/50 cross · 1h | trend | 65.27 | -34.73 | 128 | 9.4 | -37.98 | -10.50 | -38.34 | 118 |
| 45 | Triple EMA stack · 1h | trend | 64.89 | -35.11 | 176 | 15.3 | -40.77 | -10.18 | -41.68 | 164 |
| 46 | MACD zero-line · 1h | trend | 64.86 | -35.14 | 206 | 16.5 | -35.11 | -9.15 | -37.39 | 190 |
| 47 | RSI momentum · 1h | momentum | 63.68 | -36.32 | 208 | 15.4 | -41.39 | -8.95 | -42.76 | 191 |
| 48 | MFI reversion · 1h | reversion | 63.53 | -36.47 | 529 | 33.8 | -31.80 | -4.68 | -38.15 | 194 |
| 49 | Donchian 20/10 · 1h | breakout | 63.03 | -36.97 | 188 | 17.0 | -37.65 | -8.15 | -40.84 | 198 |
| 50 | Heikin-Ashi · 1h | trend | 61.65 | -38.35 | 569 | 22.0 | -47.18 | -9.13 | -49.32 | 640 |
| 51 | ROC + volume · 1h | momentum | 61.42 | -38.59 | 477 | 26.8 | -38.18 | -7.35 | -39.86 | 339 |
| 52 | EMA 9/21 cross · 1h | trend | 59.70 | -40.30 | 317 | 12.6 | -43.65 | -9.77 | -46.70 | 312 |
| 53 | MACD cross · 1h | trend | 58.78 | -41.22 | 502 | 20.9 | -52.88 | -10.16 | -56.01 | 509 |
| 54 | Agent (ML meta-label) | meta | 55.43 | -44.57 | 2076 | 25.4 | -25.54 | -3.43 | -31.11 | 294 |
| 55 | CCI reversion · 1h | reversion | 53.72 | -46.28 | 469 | 38.6 | -50.32 | -7.99 | -55.11 | 496 |
| 56 | Bollinger reversion · 1h | reversion | 52.18 | -47.82 | 408 | 36.8 | -39.73 | -4.81 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.84 | -48.16 | 1128 | 21.4 | -60.11 | -12.69 | -61.44 | 1180 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.50 | -9.10 | -59.06 | 686 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.68 | -9.14 | -59.59 | 597 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -45.75 | -99.12 | 5334 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.20 | -31.49 | -83.33 | 1400 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.91 | -44.88 | -94.03 | 2380 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.94 | -30.13 | -90.15 | 1861 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.77 | -35.34 | -91.20 | 2201 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.20 | -26.62 | -88.35 | 1921 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.05 | -47.56 | -98.05 | 3361 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.79 | -51.51 | -96.88 | 3356 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.28 | -34.93 | -93.33 | 2089 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.65 | -35.25 | -81.90 | 1524 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -56.68 | -99.69 | 6236 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.59 | -37.43 | -92.64 | 2464 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.21 | -35.53 | -94.23 | 3120 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -66.83 | -99.81 | 6017 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.72 | -42.15 | -92.72 | 2224 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.78 | -18.84 | -51.05 | 653 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.73 | -23.27 | -77.99 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -58.31 | -97.63 | 3213 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -61.25 | -99.13 | 5065 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.19 | -23.46 | -69.60 | 1209 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.49 | -46.85 | -94.49 | 2652 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.23 | -5.82 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.69 | -32.31 | -84.29 | 1651 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.10 | -99.76 | 6470 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.54 | -31.53 | -91.55 | 2467 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.62 | -20.11 | -82.80 | 1951 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.13 | -32.93 | -91.22 | 2129 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -49.23 | -98.14 | 4001 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.87 | -45.71 | -89.98 | 2185 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.75 | -29.20 | -67.89 | 785 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.06 | -26.21 | -72.78 | 1156 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.32 | -19.13 | -84.52 | 1822 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.05 | -51.22 | -98.05 | 4369 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.69 | -99.94 | 8249 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -43.80 | -6.07 | -52.59 | 304 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T23:00 | Connors RSI(2) · 1h | buy | XRP-USD | 19.63 | — | entry signal |
| 2026-11-27T23:00 | Connors RSI(2) · 1h | buy | SOL-USD | 19.63 | — | entry signal |
| 2026-11-27T21:00 | OBV trend · 1h | sell | DOGE-USD | 15.95 | -0.13 | exit signal |
| 2026-11-27T21:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 6.57 | 0.12 | exit signal |
| 2026-11-27T20:00 | CCI reversion · 1h | buy | ETH-USD | 4.37 | — | entry signal |
| 2026-11-27T20:00 | CCI reversion · 1h | buy | BTC-USD | 4.48 | — | entry signal |
| 2026-11-27T20:00 | Triple EMA stack · 1h | buy | DOGE-USD | 5.39 | — | rebalance up |
| 2026-11-27T20:00 | Triple EMA stack · 1h | sell | SOL-USD | 10.82 | 0.11 | exit signal |
| 2026-11-27T19:00 | Connors RSI(2) · 1h | sell | XRP-USD | 19.89 | 0.16 | exit signal |
| 2026-11-27T18:03 | Copy: Insider buying | buy | COHR | 11.21 | — | entry |
| 2026-11-27T18:03 | Copy: Insider buying | sell | PAM | 11.21 | 0.23 | target is flat |
| 2026-11-27T18:01 | Agent | sell | SQQQ | 14.68 | -0.48 | selected signal exited |
| 2026-11-27T18:01 | Connors RSI(2) · 1h | sell | DOGE-USD | 20.04 | 0.31 | exit signal |
| 2026-11-27T18:01 | OBV trend · 1h | buy | DOGE-USD | 16.08 | — | entry signal |
| 2026-11-27T18:01 | Trend pullback · 1h | buy | DOGE-USD | 22.69 | — | entry signal |
| 2026-11-27T17:40 | Agent (rotation) | sell | TNA | 6.32 | 0.01 | selected signal exited |
| 2026-11-27T17:40 | Agent (rotation) | sell | IWM | 6.31 | 0.00 | selected signal exited |
| 2026-11-27T17:40 | Agent | sell | COIN | 15.02 | -0.11 | selected signal exited |
| 2026-11-27T17:40 | Gap and go | buy | TSLA | 4.97 | — | rebalance up |
| 2026-11-27T17:40 | Gap and go | buy | PLTR | 4.95 | — | rebalance up |
| 2026-11-27T17:40 | Gap and go | sell | TNA | 14.79 | 0.02 | stop-loss |
| 2026-11-27T17:40 | Gap and go | sell | IWM | 19.67 | 0.01 | stop-loss |
| 2026-11-27T17:30 | CCI reversion · 1h | sell | COIN | 4.43 | 0.04 | exit signal |
| 2026-11-27T17:30 | Donchian 55/20 · 1h | buy | LABU | 11.79 | — | entry signal |
| 2026-11-27T17:30 | Donchian 55/20 · 1h | sell | TSLA | 5.79 | 0.02 | rebalance down |
| 2026-11-27T17:30 | Donchian 55/20 · 1h | sell | AAPL | 6.00 | -0.01 | rebalance down |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | buy | UPRO | 6.97 | — | entry signal |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | buy | TSLA | 6.98 | — | entry |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | buy | SPY | 6.98 | — | entry signal |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | sell | TNA | 3.48 | 0.13 | rebalance down |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | sell | PLTR | 3.55 | 0.13 | rebalance down |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | sell | META | 3.38 | 0.09 | rebalance down |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | sell | LABU | 3.79 | 0.31 | rebalance down |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | sell | IWM | 3.37 | 0.04 | rebalance down |
| 2026-11-27T17:30 | Donchian 20/10 · 1h | sell | AAPL | 3.35 | 0.03 | rebalance down |
| 2026-11-27T17:30 | VWAP momentum · 1h | buy | LABU | 1.36 | — | entry |
| 2026-11-27T17:30 | VWAP momentum · 1h | buy | AAPL | 3.02 | — | entry signal |
| 2026-11-27T17:30 | VWAP momentum · 1h | sell | META | 4.39 | 0.24 | exit signal |
| 2026-11-27T17:30 | MACD zero-line · 1h | buy | UPRO | 9.79 | — | entry signal |
| 2026-11-27T17:30 | MACD zero-line · 1h | buy | SPY | 12.92 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 23:05:05.000108+00:00 -> 2026-11-27 23:15:05.000108+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
