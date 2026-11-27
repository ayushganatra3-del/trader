# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T22:05:05.000131+00:00 · 75985 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £75.27 (-24.73%)

Closed trades 253, win rate 35.6%, fees £6.93, max drawdown -25.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.19 | -0.10 |

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

Today: 29430 decisions in 3465 calls, $0.3770 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T22:05 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-27T22:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T22:05 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.65 | 16.65 | 0 | — | 15.04 | 5.08 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 106.23 | 6.23 | 0 | — | 4.92 | 1.36 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.48 | -1.52 | 225 | 31.6 | 0.47 | 0.24 | -7.66 | 213 |
| 9 | Three white soldiers · 1h | momentum | 95.85 | -4.15 | 24 | 12.5 | -2.38 | -1.79 | -6.24 | 24 |
| 10 | Hold SPY | benchmark | 95.83 | -4.17 | 0 | — | -4.97 | -1.22 | -11.71 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 95.28 | -4.72 | 172 | 32.6 | -4.54 | -3.93 | -5.85 | 54 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.23 | -4.77 | 0 | — | -4.63 | -0.85 | -13.24 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.86 | -7.38 | 1 |
| 14 | Agent (rotation) | meta | 95.17 | -4.83 | 236 | 28.8 | 0.72 | 0.32 | -5.95 | 161 |
| 15 | Copy: Insider buying | copy | 94.75 | -5.25 | 64 | 42.2 | -1.48 | -0.12 | -14.79 | 70 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.62 | -9.38 | 0 | — | -10.32 | -2.18 | -17.03 | 1 |
| 17 | Trend pullback · 1h | trend | 90.55 | -9.46 | 117 | 23.9 | -8.50 | -4.89 | -10.59 | 31 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.47 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 88.13 | -11.87 | 490 | 33.9 | -7.99 | -2.38 | -15.30 | 553 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.94 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.44 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.14 | -15.86 | 20 | 20.0 | -14.90 | -3.35 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.42 | -6.13 | -17.45 | 79 |
| 25 | Opening range 15m | breakout | 79.88 | -20.12 | 618 | 31.9 | -17.00 | -4.70 | -23.78 | 679 |
| 26 | Connors RSI(2) · 1h | reversion | 78.52 | -21.48 | 228 | 41.2 | -14.52 | -6.64 | -14.66 | 58 |
| 27 | Volume breakout · 1h | breakout | 76.81 | -23.19 | 181 | 30.4 | -21.57 | -8.65 | -21.77 | 71 |
| 28 | Parabolic SAR · 1h | trend | 76.63 | -23.37 | 221 | 27.1 | -31.34 | -7.84 | -33.65 | 185 |
| 29 | Max aggression: 5-day momentum | meta | 76.52 | -23.48 | 27 | 37.0 | -51.07 | -2.49 | -67.33 | 21 |
| 30 | Agent (aggressive) | meta | 75.58 | -24.42 | 115 | 33.0 | -15.66 | -4.41 | -16.35 | 91 |
| 31 | Agent | meta | 75.27 | -24.73 | 253 | 35.6 | -27.58 | -6.26 | -27.63 | 203 |
| 32 | Donchian 55/20 · 1h | breakout | 73.48 | -26.52 | 91 | 13.2 | -30.66 | -8.20 | -31.23 | 82 |
| 33 | Keltner breakout · 1h | breakout | 73.08 | -26.92 | 147 | 23.8 | -26.29 | -6.52 | -27.60 | 151 |
| 34 | Ichimoku · 1h | trend | 72.92 | -27.08 | 119 | 15.1 | -29.37 | -7.52 | -30.50 | 100 |
| 35 | Daily: Momentum burst | daily | 71.70 | -28.30 | 31 | 16.1 | -31.57 | -4.30 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.34 | -28.66 | 274 | 19.7 | -37.62 | -7.04 | -39.97 | 281 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 70.25 | -29.75 | 3 | 0.0 | -22.00 | -2.60 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 69.12 | -30.88 | 3 | 0.0 | -29.42 | -5.22 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.94 | -31.06 | 418 | 40.7 | -30.00 | -3.01 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 68.39 | -31.61 | 225 | 18.7 | -38.22 | -7.36 | -41.52 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.75 | -32.25 | 220 | 23.2 | -29.95 | -7.87 | -31.73 | 211 |
| 42 | OBV trend · 1h | momentum | 66.10 | -33.90 | 333 | 19.5 | -39.72 | -9.69 | -40.13 | 215 |
| 43 | Max aggression: 1-day momentum | meta | 66.02 | -33.98 | 35 | 28.6 | -56.20 | -3.63 | -63.62 | 38 |
| 44 | EMA 20/50 cross · 1h | trend | 65.30 | -34.70 | 128 | 9.4 | -38.05 | -10.50 | -38.41 | 118 |
| 45 | MACD zero-line · 1h | trend | 64.88 | -35.12 | 206 | 16.5 | -35.13 | -9.15 | -37.39 | 190 |
| 46 | Triple EMA stack · 1h | trend | 64.88 | -35.12 | 176 | 15.3 | -40.77 | -10.19 | -41.70 | 164 |
| 47 | RSI momentum · 1h | momentum | 63.70 | -36.30 | 208 | 15.4 | -41.61 | -8.98 | -42.98 | 192 |
| 48 | MFI reversion · 1h | reversion | 63.55 | -36.45 | 529 | 33.8 | -32.32 | -4.78 | -37.91 | 194 |
| 49 | Donchian 20/10 · 1h | breakout | 63.05 | -36.95 | 188 | 17.0 | -37.65 | -8.15 | -40.84 | 198 |
| 50 | Heikin-Ashi · 1h | trend | 61.66 | -38.34 | 569 | 22.0 | -47.18 | -9.13 | -49.32 | 640 |
| 51 | ROC + volume · 1h | momentum | 61.43 | -38.56 | 477 | 26.8 | -38.15 | -7.32 | -39.85 | 341 |
| 52 | EMA 9/21 cross · 1h | trend | 59.70 | -40.30 | 317 | 12.6 | -43.72 | -9.79 | -46.70 | 312 |
| 53 | MACD cross · 1h | trend | 58.80 | -41.20 | 502 | 20.9 | -52.77 | -10.13 | -55.91 | 508 |
| 54 | Agent (ML meta-label) | meta | 55.44 | -44.56 | 2076 | 25.4 | -21.78 | -2.88 | -28.04 | 295 |
| 55 | CCI reversion · 1h | reversion | 53.73 | -46.27 | 469 | 38.6 | -50.33 | -7.99 | -55.11 | 496 |
| 56 | Bollinger reversion · 1h | reversion | 52.19 | -47.81 | 408 | 36.8 | -39.82 | -4.82 | -45.50 | 429 |
| 57 | VWAP momentum · 1h | momentum | 51.86 | -48.14 | 1128 | 21.4 | -60.37 | -12.64 | -61.66 | 1180 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.57 | -9.11 | -59.19 | 681 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.49 | -9.10 | -59.48 | 596 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -45.78 | -99.13 | 5340 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.33 | -31.63 | -83.34 | 1404 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.96 | -44.99 | -94.05 | 2384 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.95 | -30.13 | -90.15 | 1861 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.84 | -35.64 | -91.20 | 2204 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.20 | -26.62 | -88.35 | 1921 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.06 | -47.52 | -98.06 | 3361 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -51.70 | -96.87 | 3355 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.30 | -34.84 | -93.31 | 2093 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.65 | -35.25 | -81.90 | 1524 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -56.92 | -99.69 | 6232 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.57 | -37.68 | -92.61 | 2465 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.21 | -35.53 | -94.23 | 3120 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.13 | -99.81 | 6018 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.73 | -42.21 | -92.73 | 2225 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.55 | -18.32 | -51.05 | 650 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.64 | -23.23 | -77.90 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -58.61 | -97.64 | 3214 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -61.08 | -99.13 | 5062 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.13 | -23.40 | -69.58 | 1208 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.49 | -46.88 | -94.50 | 2652 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.23 | -5.82 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.74 | -32.40 | -84.31 | 1652 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.03 | -99.76 | 6468 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.50 | -31.44 | -91.55 | 2462 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.53 | -20.02 | -82.75 | 1945 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.08 | -32.57 | -91.18 | 2130 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -48.84 | -98.14 | 3996 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.92 | -45.91 | -89.98 | 2187 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.13 | -29.61 | -68.27 | 790 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.95 | -26.29 | -72.66 | 1156 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.33 | -19.14 | -84.52 | 1821 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -51.38 | -98.07 | 4368 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.38 | -99.94 | 8256 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -42.54 | -5.79 | -52.59 | 297 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-27T17:30 | MACD zero-line · 1h | sell | TNA | 3.51 | 0.13 | rebalance down |
| 2026-11-27T17:30 | MACD zero-line · 1h | sell | META | 3.53 | 0.14 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 22:05:05.000131+00:00 -> 2026-11-27 22:15:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
