# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T18:05:05.000107+00:00 · 75774 ticks

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

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 26265 decisions in 2832 calls, $0.3328 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T18:05 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-27T18:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T18:05 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.79 | 16.80 | 0 | — | 15.25 | 5.05 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 106.17 | 6.17 | 0 | — | 4.92 | 1.34 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.44 | -1.56 | 225 | 31.6 | 0.20 | 0.15 | -7.66 | 213 |
| 9 | Three white soldiers · 1h | momentum | 95.79 | -4.21 | 24 | 12.5 | -2.34 | -1.74 | -6.24 | 25 |
| 10 | Hold SPY | benchmark | 95.77 | -4.23 | 0 | — | -4.97 | -1.20 | -11.71 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 95.25 | -4.75 | 172 | 32.6 | -4.54 | -3.86 | -5.89 | 54 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 13 | Agent (rotation) | meta | 95.17 | -4.83 | 236 | 28.8 | 1.60 | 0.58 | -6.10 | 184 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.17 | -4.83 | 0 | — | -4.63 | -0.84 | -13.24 | 1 |
| 15 | Copy: Insider buying | copy | 94.82 | -5.18 | 64 | 42.2 | -1.37 | -0.10 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 90.61 | -9.39 | 117 | 23.9 | -8.42 | -4.78 | -10.59 | 31 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.42 | -9.58 | 0 | — | -10.46 | -2.19 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 88.07 | -11.93 | 490 | 33.9 | -8.05 | -2.36 | -15.30 | 553 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.13 | -15.87 | 20 | 20.0 | -14.90 | -3.29 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.42 | -6.03 | -17.45 | 79 |
| 25 | Opening range 15m | breakout | 79.83 | -20.17 | 618 | 31.9 | -17.51 | -4.75 | -24.20 | 679 |
| 26 | Connors RSI(2) · 1h | reversion | 78.51 | -21.49 | 227 | 41.0 | -14.58 | -6.56 | -14.76 | 63 |
| 27 | Volume breakout · 1h | breakout | 76.80 | -23.20 | 181 | 30.4 | -21.54 | -8.48 | -21.71 | 70 |
| 28 | Parabolic SAR · 1h | trend | 76.59 | -23.41 | 221 | 27.1 | -31.34 | -7.70 | -33.65 | 185 |
| 29 | Max aggression: 5-day momentum | meta | 75.96 | -24.04 | 27 | 37.0 | -51.40 | -2.49 | -67.33 | 21 |
| 30 | Agent (aggressive) | meta | 75.55 | -24.45 | 115 | 33.0 | -15.13 | -4.15 | -16.35 | 92 |
| 31 | Agent | meta | 75.26 | -24.74 | 253 | 35.6 | -27.35 | -6.08 | -27.66 | 210 |
| 32 | Donchian 55/20 · 1h | breakout | 73.41 | -26.59 | 91 | 13.2 | -30.69 | -8.06 | -31.23 | 82 |
| 33 | Keltner breakout · 1h | breakout | 72.96 | -27.04 | 147 | 23.8 | -26.37 | -6.43 | -27.60 | 151 |
| 34 | Ichimoku · 1h | trend | 72.78 | -27.22 | 119 | 15.1 | -29.49 | -7.41 | -30.50 | 100 |
| 35 | Daily: Momentum burst | daily | 71.56 | -28.44 | 31 | 16.1 | -31.72 | -4.26 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.23 | -28.77 | 274 | 19.7 | -37.47 | -6.91 | -39.78 | 280 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 70.20 | -29.80 | 3 | 0.0 | -22.00 | -2.56 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 69.17 | -30.83 | 3 | 0.0 | -29.06 | -5.08 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.92 | -31.08 | 418 | 40.7 | -30.00 | -2.96 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 68.35 | -31.65 | 225 | 18.7 | -38.29 | -7.25 | -41.51 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.71 | -32.29 | 220 | 23.2 | -29.95 | -7.72 | -31.73 | 211 |
| 42 | OBV trend · 1h | momentum | 66.10 | -33.90 | 332 | 19.6 | -40.25 | -9.62 | -40.66 | 216 |
| 43 | Max aggression: 1-day momentum | meta | 65.98 | -34.02 | 35 | 28.6 | -56.20 | -3.58 | -63.62 | 38 |
| 44 | EMA 20/50 cross · 1h | trend | 65.32 | -34.68 | 128 | 9.4 | -38.31 | -10.37 | -38.70 | 119 |
| 45 | Triple EMA stack · 1h | trend | 64.93 | -35.07 | 175 | 14.9 | -40.67 | -9.95 | -41.67 | 164 |
| 46 | MACD zero-line · 1h | trend | 64.84 | -35.16 | 206 | 16.5 | -35.13 | -8.97 | -37.39 | 190 |
| 47 | RSI momentum · 1h | momentum | 63.59 | -36.41 | 208 | 15.4 | -41.44 | -8.81 | -42.77 | 191 |
| 48 | MFI reversion · 1h | reversion | 63.52 | -36.48 | 529 | 33.8 | -31.80 | -4.60 | -38.15 | 194 |
| 49 | Donchian 20/10 · 1h | breakout | 62.96 | -37.04 | 188 | 17.0 | -37.69 | -8.02 | -40.84 | 198 |
| 50 | Heikin-Ashi · 1h | trend | 61.58 | -38.42 | 569 | 22.0 | -47.84 | -9.15 | -49.90 | 645 |
| 51 | ROC + volume · 1h | momentum | 61.36 | -38.65 | 477 | 26.8 | -38.40 | -7.29 | -39.94 | 340 |
| 52 | EMA 9/21 cross · 1h | trend | 59.66 | -40.34 | 316 | 12.3 | -44.06 | -9.72 | -46.70 | 313 |
| 53 | MACD cross · 1h | trend | 58.70 | -41.30 | 502 | 20.9 | -52.77 | -9.95 | -55.87 | 508 |
| 54 | Agent (ML meta-label) | meta | 55.42 | -44.58 | 2076 | 25.4 | -25.73 | -3.42 | -31.27 | 291 |
| 55 | CCI reversion · 1h | reversion | 53.72 | -46.28 | 469 | 38.6 | -50.42 | -7.86 | -55.11 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 52.25 | -47.75 | 408 | 36.8 | -39.82 | -4.74 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.82 | -48.18 | 1128 | 21.4 | -60.13 | -12.42 | -61.44 | 1179 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.92 | -9.06 | -59.20 | 689 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.47 | -8.91 | -59.48 | 596 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -42.45 | -99.15 | 5348 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.20 | -29.49 | -83.33 | 1401 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.03 | -41.18 | -94.12 | 2390 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.03 | -28.62 | -90.22 | 1868 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.94 | -33.62 | -91.26 | 2206 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.35 | -25.73 | -88.49 | 1928 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.07 | -43.15 | -98.09 | 3362 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -46.57 | -96.91 | 3361 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.33 | -32.67 | -93.37 | 2089 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.85 | -33.19 | -82.09 | 1528 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -49.83 | -99.69 | 6236 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.65 | -35.23 | -92.71 | 2466 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.38 | -34.19 | -94.40 | 3138 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -56.60 | -99.81 | 6023 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.74 | -38.73 | -92.75 | 2225 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.05 | -18.51 | -51.19 | 655 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.69 | -22.28 | -78.03 | 1614 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -50.72 | -97.66 | 3220 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -52.96 | -99.14 | 5069 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.19 | -22.59 | -69.59 | 1209 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -42.91 | -94.55 | 2655 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.32 | -5.75 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.89 | -30.95 | -84.48 | 1657 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -62.30 | -99.77 | 6476 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.50 | -29.66 | -91.55 | 2463 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.73 | -19.61 | -82.93 | 1954 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.29 | -31.75 | -91.40 | 2135 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -44.30 | -98.17 | 4004 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.03 | -42.52 | -90.10 | 2196 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.01 | -28.27 | -68.01 | 788 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.27 | -25.39 | -72.78 | 1159 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.41 | -18.65 | -84.63 | 1830 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.05 | -45.34 | -98.06 | 4365 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -80.99 | -99.94 | 8264 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -42.27 | -5.65 | -52.59 | 300 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-27T17:05 | Agent (rotation) | sell | META | 7.84 | -0.03 | selected signal exited |
| 2026-11-27T17:05 | Gap and go | buy | PLTR | 14.72 | — | rebalance up |
| 2026-11-27T17:05 | Gap and go | sell | META | 19.49 | -0.09 | stop-loss |
| 2026-11-27T17:00 | Triple EMA stack · 1h | sell | XRP-USD | 10.78 | -0.06 | exit signal |
| 2026-11-27T17:00 | EMA 9/21 cross · 1h | buy | SPY | 5.96 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 18:05:05.000107+00:00 -> 2026-11-27 18:15:05.000107+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
