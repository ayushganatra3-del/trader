# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T20:35:05.000132+00:00 · 75907 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £75.27 (-24.73%)

Closed trades 253, win rate 35.6%, fees £6.93, max drawdown -25.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.18 | -0.10 |

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

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 28260 decisions in 3231 calls, $0.3607 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T20:35 | 2 / 3 / 0 | DOGE-USD 17% |  |
| Breezy | 2026-11-27T20:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T20:35 | 5 / 0 / 0 | DOGE-USD 54% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.21 | 3.56 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.63 | 16.63 | 0 | — | 15.04 | 5.00 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 106.21 | 6.21 | 0 | — | 4.92 | 1.34 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.47 | -1.53 | 225 | 31.6 | 0.20 | 0.15 | -7.66 | 213 |
| 9 | Three white soldiers · 1h | momentum | 95.83 | -4.17 | 24 | 12.5 | -2.34 | -1.74 | -6.24 | 25 |
| 10 | Hold SPY | benchmark | 95.81 | -4.19 | 0 | — | -4.97 | -1.20 | -11.71 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 95.27 | -4.73 | 172 | 32.6 | -4.54 | -3.86 | -5.85 | 54 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.21 | -4.79 | 0 | — | -4.63 | -0.84 | -13.24 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 14 | Agent (rotation) | meta | 95.16 | -4.84 | 236 | 28.8 | 1.56 | 0.56 | -6.10 | 184 |
| 15 | Copy: Insider buying | copy | 94.74 | -5.26 | 64 | 42.2 | -1.48 | -0.12 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 90.67 | -9.33 | 117 | 23.9 | -8.36 | -4.77 | -10.58 | 31 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.60 | -9.40 | 0 | — | -10.32 | -2.15 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 88.11 | -11.89 | 490 | 33.9 | -7.93 | -2.32 | -15.30 | 553 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.14 | -15.86 | 20 | 20.0 | -14.90 | -3.29 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.62 | -6.09 | -17.80 | 80 |
| 25 | Opening range 15m | breakout | 79.86 | -20.14 | 618 | 31.9 | -17.41 | -4.71 | -24.20 | 679 |
| 26 | Connors RSI(2) · 1h | reversion | 78.52 | -21.48 | 228 | 41.2 | -14.58 | -6.56 | -14.81 | 63 |
| 27 | Volume breakout · 1h | breakout | 76.81 | -23.19 | 181 | 30.4 | -21.54 | -8.48 | -21.71 | 70 |
| 28 | Parabolic SAR · 1h | trend | 76.62 | -23.38 | 221 | 27.1 | -31.09 | -7.64 | -33.41 | 186 |
| 29 | Max aggression: 5-day momentum | meta | 76.50 | -23.50 | 27 | 37.0 | -51.07 | -2.45 | -67.33 | 21 |
| 30 | Agent (aggressive) | meta | 75.57 | -24.43 | 115 | 33.0 | -15.13 | -4.15 | -16.35 | 92 |
| 31 | Agent | meta | 75.27 | -24.73 | 253 | 35.6 | -27.35 | -6.08 | -27.66 | 210 |
| 32 | Donchian 55/20 · 1h | breakout | 73.55 | -26.45 | 91 | 13.2 | -30.59 | -8.04 | -31.23 | 82 |
| 33 | Keltner breakout · 1h | breakout | 73.07 | -26.93 | 147 | 23.8 | -26.29 | -6.41 | -27.60 | 151 |
| 34 | Ichimoku · 1h | trend | 72.92 | -27.09 | 119 | 15.1 | -29.37 | -7.38 | -30.50 | 100 |
| 35 | Daily: Momentum burst | daily | 71.69 | -28.31 | 31 | 16.1 | -31.61 | -4.23 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.33 | -28.67 | 274 | 19.7 | -37.62 | -6.92 | -39.97 | 281 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 70.23 | -29.77 | 3 | 0.0 | -22.00 | -2.56 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 69.16 | -30.84 | 3 | 0.0 | -29.25 | -5.13 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.93 | -31.07 | 418 | 40.7 | -30.02 | -2.96 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 68.37 | -31.62 | 225 | 18.7 | -38.24 | -7.23 | -41.51 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.74 | -32.26 | 220 | 23.2 | -29.95 | -7.72 | -31.73 | 211 |
| 42 | OBV trend · 1h | momentum | 66.16 | -33.84 | 332 | 19.6 | -40.23 | -9.61 | -40.67 | 216 |
| 43 | Max aggression: 1-day momentum | meta | 66.00 | -34.00 | 35 | 28.6 | -56.20 | -3.58 | -63.62 | 38 |
| 44 | EMA 20/50 cross · 1h | trend | 65.42 | -34.58 | 128 | 9.4 | -37.94 | -10.35 | -38.40 | 118 |
| 45 | Triple EMA stack · 1h | trend | 64.96 | -35.04 | 176 | 15.3 | -41.34 | -9.95 | -42.32 | 165 |
| 46 | MACD zero-line · 1h | trend | 64.87 | -35.13 | 206 | 16.5 | -35.05 | -8.97 | -37.39 | 190 |
| 47 | RSI momentum · 1h | momentum | 63.69 | -36.31 | 208 | 15.4 | -41.61 | -8.81 | -42.98 | 192 |
| 48 | MFI reversion · 1h | reversion | 63.54 | -36.46 | 529 | 33.8 | -31.80 | -4.60 | -38.15 | 194 |
| 49 | Donchian 20/10 · 1h | breakout | 63.04 | -36.96 | 188 | 17.0 | -37.65 | -8.00 | -40.84 | 198 |
| 50 | Heikin-Ashi · 1h | trend | 61.65 | -38.35 | 569 | 22.0 | -47.18 | -8.96 | -49.32 | 640 |
| 51 | ROC + volume · 1h | momentum | 61.42 | -38.58 | 477 | 26.8 | -38.37 | -7.28 | -39.94 | 340 |
| 52 | EMA 9/21 cross · 1h | trend | 59.76 | -40.24 | 316 | 12.3 | -43.67 | -9.57 | -46.70 | 312 |
| 53 | MACD cross · 1h | trend | 58.79 | -41.21 | 502 | 20.9 | -52.52 | -9.87 | -55.60 | 507 |
| 54 | Agent (ML meta-label) | meta | 55.43 | -44.57 | 2076 | 25.4 | -25.97 | -3.26 | -31.68 | 303 |
| 55 | CCI reversion · 1h | reversion | 53.74 | -46.26 | 469 | 38.6 | -50.43 | -7.86 | -55.11 | 496 |
| 56 | Bollinger reversion · 1h | reversion | 52.25 | -47.75 | 408 | 36.8 | -39.37 | -4.67 | -45.50 | 429 |
| 57 | VWAP momentum · 1h | momentum | 51.85 | -48.15 | 1128 | 21.4 | -60.10 | -12.40 | -61.44 | 1180 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -54.91 | -8.78 | -59.06 | 683 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.26 | -8.86 | -59.48 | 595 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -41.70 | -99.13 | 5340 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.28 | -29.80 | -83.33 | 1403 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.97 | -40.85 | -94.06 | 2386 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.93 | -28.46 | -90.15 | 1862 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.85 | -33.25 | -91.20 | 2205 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.24 | -25.53 | -88.39 | 1923 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.06 | -42.83 | -98.06 | 3362 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -45.94 | -96.88 | 3361 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.28 | -32.64 | -93.32 | 2087 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.81 | -33.10 | -82.07 | 1528 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -49.43 | -99.69 | 6233 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.61 | -34.92 | -92.66 | 2466 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.26 | -33.60 | -94.28 | 3126 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -55.95 | -99.81 | 6017 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.72 | -38.61 | -92.72 | 2224 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.74 | -18.23 | -51.05 | 651 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.73 | -22.39 | -77.99 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -50.49 | -97.64 | 3217 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -52.07 | -99.13 | 5060 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.13 | -22.51 | -69.58 | 1208 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -42.46 | -94.51 | 2654 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.23 | -5.72 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.80 | -30.67 | -84.36 | 1654 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -60.53 | -99.76 | 6468 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -29.70 | -91.55 | 2463 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.86 | -19.72 | -83.06 | 1954 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.14 | -31.00 | -91.23 | 2130 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -43.66 | -98.15 | 3996 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.88 | -41.36 | -89.98 | 2185 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.81 | -27.87 | -67.89 | 786 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.17 | -25.19 | -72.78 | 1158 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.30 | -18.52 | -84.52 | 1822 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.05 | -45.31 | -98.06 | 4366 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -78.64 | -99.94 | 8258 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -42.80 | -5.76 | -52.59 | 296 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-27T17:30 | EMA 20/50 cross · 1h | buy | META | 2.59 | — | entry signal |
| 2026-11-27T17:15 | Agent | buy | COIN | 15.13 | — | following OBV trend |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 20:35:05.000132+00:00 -> 2026-11-27 20:45:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
