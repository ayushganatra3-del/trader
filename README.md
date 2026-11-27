# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T15:05:05.000124+00:00 · 75630 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.26 (-23.74%)

Closed trades 250, win rate 36.0%, fees £6.89, max drawdown -24.13%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.06 | -0.23 |
| SQQQ | 15.31 | +0.05 |

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

Today: 13497 decisions in 2400 calls, $0.1840 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T15:05 | 3 / 13 / 14 | cash |  |
| Breezy | 2026-11-27T15:05 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-27T15:05 | 5 / 21 / 4 | MSTR 64% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.30 | 16.30 | 0 | — | 14.93 | 4.96 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.41 | 5.41 | 0 | — | 4.31 | 1.20 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 102.52 | 2.52 | 43 | 27.9 | 0.06 | 0.20 | -14.70 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.81 | -2.19 | 222 | 31.1 | -0.39 | -0.03 | -7.66 | 207 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.17 | -4.83 | 171 | 32.7 | -4.56 | -3.89 | -5.63 | 52 |
| 11 | Hold SPY | benchmark | 94.55 | -5.45 | 0 | — | -6.04 | -1.52 | -11.71 | 1 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 94.45 | -5.55 | 0 | — | -5.22 | -0.97 | -13.24 | 1 |
| 13 | Agent (rotation) | meta | 94.25 | -5.75 | 233 | 28.3 | 0.48 | 0.24 | -6.10 | 179 |
| 14 | Three white soldiers · 1h | momentum | 93.84 | -6.16 | 24 | 12.5 | -4.66 | -6.09 | -6.57 | 26 |
| 15 | Copy: Insider buying | copy | 93.20 | -6.80 | 63 | 41.3 | -4.02 | -0.64 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.14 | -8.86 | 116 | 24.1 | -6.55 | -4.38 | -9.32 | 26 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.71 | -9.29 | 0 | — | -10.04 | -2.08 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -9.23 | -2.79 | -15.30 | 538 |
| 21 | Daily: Bullish score | daily | 85.42 | -14.58 | 20 | 20.0 | -13.55 | -3.00 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.41 | -6.03 | -17.45 | 79 |
| 25 | Opening range 15m | breakout | 79.13 | -20.87 | 616 | 32.0 | -18.19 | -5.00 | -24.20 | 664 |
| 26 | Connors RSI(2) · 1h | reversion | 78.74 | -21.26 | 226 | 40.7 | -14.29 | -6.53 | -14.47 | 62 |
| 27 | Volume breakout · 1h | breakout | 76.69 | -23.31 | 178 | 29.2 | -21.66 | -8.53 | -21.69 | 69 |
| 28 | Agent | meta | 76.26 | -23.74 | 250 | 36.0 | -26.33 | -5.82 | -26.89 | 208 |
| 29 | Parabolic SAR · 1h | trend | 75.30 | -24.70 | 221 | 27.1 | -32.07 | -8.06 | -33.18 | 181 |
| 30 | Agent (aggressive) | meta | 75.27 | -24.73 | 115 | 33.0 | -15.39 | -4.24 | -16.35 | 92 |
| 31 | Max aggression: 5-day momentum | meta | 72.87 | -27.13 | 27 | 37.0 | -53.31 | -2.67 | -67.33 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 72.73 | -27.27 | 91 | 13.2 | -31.18 | -8.13 | -31.21 | 77 |
| 33 | Ichimoku · 1h | trend | 72.02 | -27.98 | 119 | 15.1 | -30.19 | -7.57 | -30.49 | 100 |
| 34 | Keltner breakout · 1h | breakout | 71.77 | -28.23 | 147 | 23.8 | -27.49 | -6.71 | -27.60 | 146 |
| 35 | Daily: Momentum burst | daily | 70.78 | -29.22 | 31 | 16.1 | -32.41 | -4.39 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.87 | -30.13 | 273 | 19.8 | -39.36 | -7.55 | -40.43 | 277 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 68.36 | -31.64 | 3 | 0.0 | -23.93 | -2.90 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 68.20 | -31.80 | 3 | 0.0 | -30.07 | -5.27 | -36.10 | 1 |
| 39 | Supertrend · 1h | trend | 67.27 | -32.73 | 224 | 18.8 | -39.40 | -7.65 | -41.51 | 208 |
| 40 | Bollinger breakout · 1h | breakout | 67.09 | -32.91 | 220 | 23.2 | -30.50 | -7.89 | -31.66 | 206 |
| 41 | Stochastic reversion · 1h | reversion | 66.91 | -33.09 | 412 | 39.8 | -32.09 | -3.28 | -42.39 | 428 |
| 42 | OBV trend · 1h | momentum | 65.78 | -34.22 | 331 | 19.6 | -40.17 | -9.73 | -40.36 | 213 |
| 43 | EMA 20/50 cross · 1h | trend | 64.98 | -35.02 | 128 | 9.4 | -38.70 | -10.52 | -38.85 | 118 |
| 44 | MACD zero-line · 1h | trend | 63.92 | -36.08 | 206 | 16.5 | -35.95 | -9.54 | -37.39 | 188 |
| 45 | Triple EMA stack · 1h | trend | 63.89 | -36.11 | 174 | 14.9 | -41.49 | -10.30 | -41.63 | 162 |
| 46 | RSI momentum · 1h | momentum | 62.36 | -37.64 | 208 | 15.4 | -42.53 | -9.21 | -42.76 | 187 |
| 47 | MFI reversion · 1h | reversion | 62.28 | -37.72 | 528 | 33.7 | -33.21 | -4.91 | -38.15 | 194 |
| 48 | Donchian 20/10 · 1h | breakout | 61.60 | -38.40 | 188 | 17.0 | -38.90 | -8.53 | -40.84 | 195 |
| 49 | Heikin-Ashi · 1h | trend | 59.75 | -40.25 | 564 | 22.0 | -49.47 | -9.95 | -49.90 | 644 |
| 50 | ROC + volume · 1h | momentum | 59.74 | -40.27 | 477 | 26.8 | -40.78 | -7.89 | -40.85 | 332 |
| 51 | Max aggression: 1-day momentum | meta | 58.44 | -41.56 | 35 | 28.6 | -61.15 | -4.48 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.35 | -41.65 | 315 | 12.1 | -44.87 | -10.24 | -46.70 | 307 |
| 53 | MACD cross · 1h | trend | 56.80 | -43.20 | 502 | 20.9 | -54.04 | -10.65 | -55.66 | 506 |
| 54 | Agent (ML meta-label) | meta | 55.17 | -44.83 | 2074 | 25.4 | -24.39 | -3.18 | -29.09 | 294 |
| 55 | Bollinger reversion · 1h | reversion | 51.76 | -48.24 | 406 | 36.5 | -40.32 | -4.84 | -45.50 | 428 |
| 56 | CCI reversion · 1h | reversion | 51.71 | -48.29 | 467 | 38.3 | -52.25 | -8.60 | -55.11 | 494 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.67 | -9.64 | -59.72 | 687 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.99 | -9.16 | -59.48 | 594 |
| 59 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -43.72 | -99.15 | 5310 |
| 60 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.25 | -29.50 | -83.38 | 1400 |
| 61 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.12 | -42.52 | -94.12 | 2381 |
| 62 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.00 | -28.51 | -90.23 | 1856 |
| 63 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -36.81 | -91.28 | 2190 |
| 64 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.48 | -26.04 | -88.48 | 1913 |
| 65 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.08 | -43.25 | -98.08 | 3353 |
| 66 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -47.54 | -96.90 | 3340 |
| 67 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.34 | -33.13 | -93.34 | 2073 |
| 68 | VWAP momentum · 1h | momentum | 50.32 | -49.68 | 1117 | 21.2 | -61.16 | -13.16 | -61.75 | 1173 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.17 | -34.22 | -82.18 | 1520 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -51.14 | -99.69 | 6226 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -35.49 | -92.71 | 2438 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.41 | -34.37 | -94.42 | 3122 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -58.55 | -99.81 | 6014 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.74 | -38.83 | -92.76 | 2221 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.90 | -18.37 | -51.19 | 651 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.97 | -22.62 | -78.02 | 1599 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -51.57 | -97.67 | 3199 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -54.13 | -99.14 | 5053 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.53 | -22.72 | -69.53 | 1203 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -43.08 | -94.56 | 2635 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.55 | -6.38 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.40 | -32.53 | -84.43 | 1637 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -63.88 | -99.77 | 6450 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.49 | -29.70 | -91.63 | 2464 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.57 | -19.42 | -82.95 | 1948 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.32 | -31.81 | -91.49 | 2126 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.20 | -45.99 | -98.20 | 4002 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.99 | -42.02 | -90.11 | 2182 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.96 | -28.22 | -67.96 | 779 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.68 | -26.48 | -72.77 | 1146 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.75 | -19.01 | -84.75 | 1824 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.11 | -47.24 | -98.11 | 4360 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -80.91 | -99.94 | 8206 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -45.88 | -6.71 | -52.59 | 301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T15:05 | Triple EMA stack · 1h | buy | SOL-USD | 3.15 | — | rebalance up |
| 2026-11-27T15:00 | Connors RSI(2) · 1h | buy | XRP-USD | 19.73 | — | entry signal |
| 2026-11-27T15:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 19.73 | — | entry signal |
| 2026-11-27T15:00 | Volume breakout · 1h | sell | DOGE-USD | 18.82 | -0.38 | exit signal |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | buy | TNA | 4.62 | — | rebalance up |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | buy | PLTR | 4.56 | — | rebalance up |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | buy | META | 4.59 | — | rebalance up |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | buy | LABU | 4.80 | — | rebalance up |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | buy | IWM | 4.62 | — | rebalance up |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | buy | AAPL | 4.62 | — | rebalance up |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | sell | XRP-USD | 5.45 | -0.06 | exit signal |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | sell | SOL-USD | 5.53 | -0.14 | exit signal |
| 2026-11-27T15:00 | Donchian 20/10 · 1h | sell | DOGE-USD | 5.52 | -0.15 | exit signal |
| 2026-11-27T15:00 | OBV trend · 1h | buy | SQQQ | 7.99 | — | rebalance up |
| 2026-11-27T15:00 | OBV trend · 1h | buy | PLTR | 8.08 | — | rebalance up |
| 2026-11-27T15:00 | OBV trend · 1h | buy | AAPL | 8.16 | — | rebalance up |
| 2026-11-27T15:00 | OBV trend · 1h | sell | XRP-USD | 8.13 | -0.19 | exit signal |
| 2026-11-27T15:00 | OBV trend · 1h | sell | SOL-USD | 8.14 | -0.20 | exit signal |
| 2026-11-27T15:00 | OBV trend · 1h | sell | DOGE-USD | 8.11 | -0.23 | exit signal |
| 2026-11-27T15:00 | RSI momentum · 1h | buy | PLTR | 6.46 | — | rebalance up |
| 2026-11-27T15:00 | RSI momentum · 1h | buy | LABU | 6.85 | — | rebalance up |
| 2026-11-27T15:00 | RSI momentum · 1h | sell | XRP-USD | 9.38 | -0.06 | exit signal |
| 2026-11-27T15:00 | RSI momentum · 1h | sell | SOL-USD | 8.95 | 0.02 | exit signal |
| 2026-11-27T15:00 | RSI momentum · 1h | sell | ETH-USD | 8.80 | -0.30 | exit signal |
| 2026-11-27T15:00 | RSI momentum · 1h | sell | DOGE-USD | 9.03 | 0.08 | exit signal |
| 2026-11-27T15:00 | RSI momentum · 1h | sell | BTC-USD | 6.91 | -0.17 | exit signal |
| 2026-11-27T15:00 | VWAP momentum · 1h | buy | SPY | 1.84 | — | entry |
| 2026-11-27T15:00 | VWAP momentum · 1h | sell | DOGE-USD | 1.84 | -0.04 | exit signal |
| 2026-11-27T15:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.48 | -0.05 | exit signal |
| 2026-11-27T15:00 | Ichimoku · 1h | sell | XRP-USD | 17.98 | -0.30 | exit signal |
| 2026-11-27T15:00 | Ichimoku · 1h | sell | SOL-USD | 18.05 | -0.25 | exit signal |
| 2026-11-27T15:00 | Ichimoku · 1h | sell | DOGE-USD | 18.02 | -0.17 | exit signal |
| 2026-11-27T15:00 | ADX DI cross · 1h | buy | META | 5.09 | — | rebalance up |
| 2026-11-27T15:00 | ADX DI cross · 1h | sell | SOL-USD | 9.90 | -0.11 | exit signal |
| 2026-11-27T15:00 | Parabolic SAR · 1h | buy | TNA | 5.47 | — | rebalance up |
| 2026-11-27T15:00 | Parabolic SAR · 1h | buy | PLTR | 5.41 | — | rebalance up |
| 2026-11-27T15:00 | Parabolic SAR · 1h | buy | META | 5.41 | — | rebalance up |
| 2026-11-27T15:00 | Parabolic SAR · 1h | buy | IWM | 5.61 | — | rebalance up |
| 2026-11-27T15:00 | Parabolic SAR · 1h | buy | AAPL | 5.66 | — | rebalance up |
| 2026-11-27T15:00 | Parabolic SAR · 1h | sell | SOL-USD | 7.35 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 15:05:05.000124+00:00 -> 2026-11-27 15:15:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
