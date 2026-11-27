# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T23:35:05.000133+00:00 · 76059 ticks

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

Today: 30540 decisions in 3687 calls, $0.3925 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T23:35 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-11-27T23:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T23:35 | 3 / 2 / 0 | ETH-USD 59% |  |

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
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 106.19 | 6.19 | 0 | — | 4.92 | 1.36 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.45 | -1.54 | 225 | 31.6 | 0.47 | 0.24 | -7.66 | 213 |
| 9 | Three white soldiers · 1h | momentum | 95.81 | -4.19 | 24 | 12.5 | -2.38 | -1.79 | -6.24 | 24 |
| 10 | Hold SPY | benchmark | 95.80 | -4.20 | 0 | — | -4.97 | -1.22 | -11.71 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 95.26 | -4.74 | 172 | 32.6 | -4.54 | -3.93 | -5.85 | 54 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.86 | -7.38 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 95.19 | -4.81 | 0 | — | -4.63 | -0.85 | -13.24 | 1 |
| 14 | Agent (rotation) | meta | 95.15 | -4.85 | 236 | 28.8 | 0.72 | 0.32 | -5.95 | 161 |
| 15 | Copy: Insider buying | copy | 94.72 | -5.28 | 64 | 42.2 | -1.48 | -0.12 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 90.60 | -9.40 | 117 | 23.9 | -8.47 | -4.90 | -10.61 | 31 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.59 | -9.41 | 0 | — | -10.32 | -2.18 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.47 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 88.10 | -11.90 | 490 | 33.9 | -7.99 | -2.38 | -15.30 | 553 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.94 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.44 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.13 | -15.87 | 20 | 20.0 | -14.90 | -3.35 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.02 | -6.08 | -17.05 | 79 |
| 25 | Opening range 15m | breakout | 79.85 | -20.15 | 618 | 31.9 | -17.00 | -4.70 | -23.78 | 679 |
| 26 | Connors RSI(2) · 1h | reversion | 78.43 | -21.57 | 228 | 41.2 | -14.61 | -6.65 | -14.76 | 60 |
| 27 | Volume breakout · 1h | breakout | 76.81 | -23.19 | 181 | 30.4 | -21.57 | -8.65 | -21.76 | 71 |
| 28 | Parabolic SAR · 1h | trend | 76.61 | -23.39 | 221 | 27.1 | -31.34 | -7.84 | -33.65 | 185 |
| 29 | Max aggression: 5-day momentum | meta | 76.49 | -23.51 | 27 | 37.0 | -51.07 | -2.49 | -67.33 | 21 |
| 30 | Agent (aggressive) | meta | 75.56 | -24.44 | 115 | 33.0 | -15.66 | -4.41 | -16.35 | 91 |
| 31 | Agent | meta | 75.26 | -24.74 | 253 | 35.6 | -27.58 | -6.26 | -27.63 | 203 |
| 32 | Donchian 55/20 · 1h | breakout | 73.50 | -26.50 | 91 | 13.2 | -30.62 | -8.19 | -31.22 | 82 |
| 33 | Keltner breakout · 1h | breakout | 73.06 | -26.94 | 147 | 23.8 | -26.29 | -6.52 | -27.60 | 151 |
| 34 | Ichimoku · 1h | trend | 72.91 | -27.09 | 119 | 15.1 | -29.52 | -7.54 | -30.64 | 101 |
| 35 | Daily: Momentum burst | daily | 71.69 | -28.31 | 31 | 16.1 | -31.57 | -4.30 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.32 | -28.68 | 274 | 19.7 | -37.25 | -6.98 | -39.61 | 279 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 70.22 | -29.78 | 3 | 0.0 | -22.00 | -2.60 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 69.22 | -30.78 | 3 | 0.0 | -29.31 | -5.23 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.92 | -31.07 | 418 | 40.7 | -30.21 | -3.04 | -42.39 | 429 |
| 40 | Supertrend · 1h | trend | 68.36 | -31.64 | 225 | 18.7 | -38.20 | -7.35 | -41.52 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.73 | -32.27 | 220 | 23.2 | -29.95 | -7.87 | -31.73 | 211 |
| 42 | OBV trend · 1h | momentum | 66.08 | -33.92 | 333 | 19.5 | -39.76 | -9.71 | -40.13 | 215 |
| 43 | Max aggression: 1-day momentum | meta | 65.99 | -34.01 | 35 | 28.6 | -56.20 | -3.63 | -63.62 | 38 |
| 44 | EMA 20/50 cross · 1h | trend | 65.28 | -34.72 | 128 | 9.4 | -37.98 | -10.50 | -38.34 | 118 |
| 45 | Triple EMA stack · 1h | trend | 64.90 | -35.09 | 176 | 15.3 | -40.76 | -10.18 | -41.68 | 164 |
| 46 | MACD zero-line · 1h | trend | 64.86 | -35.14 | 206 | 16.5 | -35.11 | -9.15 | -37.39 | 190 |
| 47 | RSI momentum · 1h | momentum | 63.68 | -36.32 | 208 | 15.4 | -41.39 | -8.95 | -42.76 | 191 |
| 48 | MFI reversion · 1h | reversion | 63.53 | -36.47 | 529 | 33.8 | -32.32 | -4.78 | -37.91 | 194 |
| 49 | Donchian 20/10 · 1h | breakout | 63.03 | -36.97 | 188 | 17.0 | -37.65 | -8.15 | -40.84 | 198 |
| 50 | Heikin-Ashi · 1h | trend | 61.65 | -38.35 | 569 | 22.0 | -47.18 | -9.13 | -49.32 | 640 |
| 51 | ROC + volume · 1h | momentum | 61.41 | -38.59 | 477 | 26.8 | -37.96 | -7.27 | -39.78 | 340 |
| 52 | EMA 9/21 cross · 1h | trend | 59.70 | -40.30 | 317 | 12.6 | -43.64 | -9.77 | -46.70 | 312 |
| 53 | MACD cross · 1h | trend | 58.78 | -41.22 | 502 | 20.9 | -52.88 | -10.16 | -56.01 | 509 |
| 54 | Agent (ML meta-label) | meta | 55.43 | -44.57 | 2076 | 25.4 | -25.10 | -3.13 | -31.75 | 303 |
| 55 | CCI reversion · 1h | reversion | 53.72 | -46.28 | 469 | 38.6 | -50.31 | -7.98 | -55.11 | 496 |
| 56 | Bollinger reversion · 1h | reversion | 52.20 | -47.80 | 408 | 36.8 | -39.99 | -4.85 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.84 | -48.16 | 1128 | 21.4 | -60.34 | -12.64 | -61.64 | 1180 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.32 | -9.06 | -59.19 | 682 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.81 | -9.18 | -59.65 | 598 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -45.75 | -99.12 | 5334 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.21 | -31.48 | -83.34 | 1401 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.91 | -44.94 | -94.04 | 2379 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.91 | -30.07 | -90.15 | 1860 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.77 | -35.33 | -91.19 | 2201 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.18 | -26.55 | -88.33 | 1921 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.05 | -47.37 | -98.05 | 3361 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -51.39 | -96.87 | 3353 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.32 | -34.86 | -93.34 | 2096 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.56 | -35.09 | -81.91 | 1525 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -56.85 | -99.69 | 6235 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.56 | -37.68 | -92.61 | 2464 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.20 | -35.54 | -94.22 | 3119 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.94 | -99.81 | 6018 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.68 | -41.95 | -92.68 | 2222 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.46 | -18.24 | -51.05 | 651 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.63 | -23.22 | -77.89 | 1616 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -58.80 | -97.65 | 3215 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -61.29 | -99.13 | 5064 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.06 | -23.35 | -69.51 | 1207 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.50 | -46.94 | -94.50 | 2652 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.23 | -5.82 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.69 | -32.15 | -84.26 | 1651 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -74.94 | -99.76 | 6466 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.53 | -31.51 | -91.55 | 2467 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.64 | -20.13 | -82.82 | 1954 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.08 | -32.61 | -91.18 | 2131 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -49.17 | -98.14 | 3999 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.90 | -45.98 | -89.98 | 2187 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.13 | -29.61 | -68.26 | 790 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.94 | -26.26 | -72.66 | 1156 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.30 | -19.11 | -84.51 | 1820 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.05 | -51.38 | -98.06 | 4367 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.60 | -99.94 | 8252 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -43.57 | -5.98 | -52.59 | 304 |

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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 23:35:05.000133+00:00 -> 2026-11-27 23:45:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
