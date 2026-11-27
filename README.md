# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T17:34:05.000136+00:00 · 75755 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £75.57 (-24.43%)

Closed trades 251, win rate 35.9%, fees £6.91, max drawdown -24.82%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 15.08 | -0.05 |
| MSFT | 15.12 | -0.16 |
| SQQQ | 14.98 | -0.17 |

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

Today: 24705 decisions in 2775 calls, $0.3145 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T17:34 | 6 / 11 / 13 | BRK-B 14% |  |
| Breezy | 2026-11-27T17:34 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-27T17:34 | 3 / 24 / 3 | COIN 52% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.52 | 16.52 | 0 | — | 14.98 | 4.98 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.96 | 5.96 | 0 | — | 4.71 | 1.29 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.42 | -1.58 | 223 | 30.9 | 0.22 | 0.16 | -7.66 | 213 |
| 9 | Hold SPY | benchmark | 95.53 | -4.47 | 0 | — | -5.20 | -1.27 | -11.71 | 1 |
| 10 | Three white soldiers · 1h | momentum | 95.31 | -4.69 | 24 | 12.5 | -2.82 | -2.45 | -6.24 | 25 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.10 | -4.90 | 0 | — | -4.70 | -0.85 | -13.24 | 1 |
| 13 | Agent (rotation) | meta | 95.09 | -4.91 | 234 | 28.2 | 1.31 | 0.49 | -6.10 | 184 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 94.98 | -5.02 | 172 | 32.6 | -4.80 | -4.11 | -5.85 | 54 |
| 15 | Copy: Insider buying | copy | 94.48 | -5.52 | 63 | 41.3 | -2.22 | -0.27 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 90.76 | -9.24 | 117 | 23.9 | -7.56 | -4.68 | -9.90 | 28 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.41 | -9.60 | 0 | — | -10.47 | -2.19 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 87.34 | -12.66 | 490 | 33.9 | -8.80 | -2.64 | -15.30 | 553 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.54 | -15.46 | 20 | 20.0 | -14.48 | -3.21 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.42 | -6.03 | -17.45 | 79 |
| 25 | Opening range 15m | breakout | 79.16 | -20.84 | 618 | 31.9 | -18.19 | -5.00 | -24.20 | 679 |
| 26 | Connors RSI(2) · 1h | reversion | 78.89 | -21.11 | 226 | 40.7 | -14.16 | -6.49 | -14.44 | 63 |
| 27 | Volume breakout · 1h | breakout | 76.75 | -23.25 | 181 | 30.4 | -21.60 | -8.50 | -21.71 | 70 |
| 28 | Parabolic SAR · 1h | trend | 76.34 | -23.66 | 221 | 27.1 | -31.52 | -7.78 | -33.65 | 185 |
| 29 | Max aggression: 5-day momentum | meta | 76.16 | -23.84 | 27 | 37.0 | -51.27 | -2.47 | -67.33 | 21 |
| 30 | Agent | meta | 75.57 | -24.43 | 251 | 35.9 | -27.04 | -6.01 | -27.40 | 210 |
| 31 | Agent (aggressive) | meta | 75.42 | -24.58 | 115 | 33.0 | -15.28 | -4.20 | -16.35 | 92 |
| 32 | Donchian 55/20 · 1h | breakout | 73.33 | -26.67 | 91 | 13.2 | -30.75 | -8.07 | -31.23 | 82 |
| 33 | Ichimoku · 1h | trend | 72.83 | -27.17 | 119 | 15.1 | -29.44 | -7.40 | -30.50 | 100 |
| 34 | Keltner breakout · 1h | breakout | 72.77 | -27.23 | 147 | 23.8 | -26.78 | -6.56 | -27.79 | 152 |
| 35 | Daily: Momentum burst | daily | 71.61 | -28.39 | 31 | 16.1 | -31.68 | -4.25 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.06 | -28.94 | 274 | 19.7 | -37.71 | -7.00 | -39.78 | 280 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 69.93 | -30.07 | 3 | 0.0 | -22.30 | -2.62 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 68.98 | -31.02 | 3 | 0.0 | -29.30 | -5.13 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.71 | -31.29 | 418 | 40.7 | -30.19 | -2.99 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 68.08 | -31.92 | 225 | 18.7 | -38.52 | -7.35 | -41.52 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.48 | -32.52 | 220 | 23.2 | -30.19 | -7.80 | -31.73 | 211 |
| 42 | OBV trend · 1h | momentum | 66.06 | -33.94 | 332 | 19.6 | -39.68 | -9.58 | -40.08 | 213 |
| 43 | EMA 20/50 cross · 1h | trend | 65.40 | -34.60 | 128 | 9.4 | -38.15 | -10.31 | -38.64 | 119 |
| 44 | Triple EMA stack · 1h | trend | 64.84 | -35.16 | 175 | 14.9 | -40.77 | -9.99 | -41.67 | 164 |
| 45 | MACD zero-line · 1h | trend | 64.57 | -35.42 | 206 | 16.5 | -35.41 | -9.17 | -37.39 | 190 |
| 46 | RSI momentum · 1h | momentum | 63.41 | -36.59 | 208 | 15.4 | -41.62 | -8.88 | -42.76 | 191 |
| 47 | MFI reversion · 1h | reversion | 63.29 | -36.71 | 529 | 33.8 | -32.07 | -4.66 | -38.15 | 194 |
| 48 | Max aggression: 1-day momentum | meta | 63.21 | -36.79 | 35 | 28.6 | -58.04 | -3.93 | -63.62 | 38 |
| 49 | Donchian 20/10 · 1h | breakout | 62.78 | -37.23 | 188 | 17.0 | -37.88 | -8.11 | -40.84 | 198 |
| 50 | Heikin-Ashi · 1h | trend | 61.24 | -38.76 | 569 | 22.0 | -48.21 | -9.36 | -49.90 | 645 |
| 51 | ROC + volume · 1h | momentum | 60.83 | -39.17 | 477 | 26.8 | -39.73 | -7.63 | -40.79 | 344 |
| 52 | EMA 9/21 cross · 1h | trend | 59.53 | -40.47 | 316 | 12.3 | -44.53 | -9.94 | -46.92 | 315 |
| 53 | MACD cross · 1h | trend | 58.28 | -41.72 | 502 | 20.9 | -53.06 | -10.13 | -55.83 | 509 |
| 54 | Agent (ML meta-label) | meta | 55.32 | -44.68 | 2076 | 25.4 | -24.12 | -3.08 | -29.79 | 293 |
| 55 | CCI reversion · 1h | reversion | 53.21 | -46.79 | 469 | 38.6 | -50.89 | -8.09 | -55.11 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 52.15 | -47.85 | 408 | 36.8 | -39.94 | -4.77 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.38 | -48.62 | 1128 | 21.4 | -60.30 | -12.63 | -61.80 | 1181 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.48 | -9.22 | -59.72 | 688 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.70 | -8.99 | -59.51 | 597 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -42.97 | -99.15 | 5342 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.26 | -29.61 | -83.36 | 1402 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.06 | -41.65 | -94.12 | 2390 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.07 | -28.79 | -90.23 | 1865 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.02 | -34.49 | -91.27 | 2202 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.45 | -25.94 | -88.50 | 1916 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.08 | -43.28 | -98.08 | 3362 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -46.94 | -96.91 | 3353 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.34 | -32.98 | -93.38 | 2085 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.77 | -32.91 | -82.09 | 1524 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -50.03 | -99.69 | 6228 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.67 | -35.34 | -92.69 | 2459 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.39 | -34.19 | -94.39 | 3124 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -56.65 | -99.81 | 6019 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.75 | -38.84 | -92.76 | 2226 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.04 | -18.50 | -51.19 | 654 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.52 | -22.02 | -78.03 | 1607 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -50.72 | -97.66 | 3207 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -52.96 | -99.14 | 5059 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.08 | -22.51 | -69.60 | 1205 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -42.60 | -94.55 | 2643 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.96 | -5.95 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.93 | -31.14 | -84.48 | 1651 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -62.44 | -99.77 | 6462 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.46 | -29.56 | -91.55 | 2463 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.77 | -19.64 | -83.06 | 1958 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.25 | -31.62 | -91.40 | 2129 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -44.18 | -98.17 | 3998 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.07 | -42.84 | -90.11 | 2191 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.99 | -28.26 | -67.99 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.56 | -26.08 | -72.79 | 1160 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.45 | -18.70 | -84.66 | 1829 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -45.83 | -98.08 | 4363 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -80.74 | -99.94 | 8259 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -44.98 | -6.34 | -52.59 | 303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-27T17:05 | Agent (rotation) | sell | META | 7.84 | -0.03 | selected signal exited |
| 2026-11-27T17:05 | Gap and go | buy | PLTR | 14.72 | — | rebalance up |
| 2026-11-27T17:05 | Gap and go | sell | META | 19.49 | -0.09 | stop-loss |
| 2026-11-27T17:00 | Triple EMA stack · 1h | sell | XRP-USD | 10.78 | -0.06 | exit signal |
| 2026-11-27T17:00 | EMA 9/21 cross · 1h | buy | SPY | 5.96 | — | entry |
| 2026-11-27T17:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 6.47 | 0.04 | exit signal |
| 2026-11-27T16:36 | Volume breakout · 1h | sell | META | 19.19 | 0.02 | target is flat |
| 2026-11-27T16:36 | Opening range 30m | buy | UPRO | 7.94 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | TQQQ | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | SPY | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | SOXL | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | QQQ | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | sell | TSLA | 4.52 | 0.03 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | TNA | 6.66 | 0.04 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | PLTR | 6.69 | 0.06 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | META | 6.59 | 0.03 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | IWM | 4.54 | 0.00 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | AMZN | 6.64 | 0.06 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 17:34:05.000136+00:00 -> 2026-11-27 17:44:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
