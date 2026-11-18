# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T15:01:05.000158+00:00 · 64559 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.66 (-15.34%)

Closed trades 219, win rate 35.6%, fees £6.07, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-18 | PEPG 12%, FUN 12%, STWD 12%, LRN 12%, PSEC 12%, TEAM 12%, BH 12%, LILA 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 14196 decisions in 2391 calls, $0.1923 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T15:01 | 8 / 20 / 2 | AMD 21%, TNA 17%, SOXL 17%, TECL 14% |  |
| Breezy | 2026-11-18T15:01 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-18T15:01 | 11 / 18 / 1 | COIN 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 115.62 | 15.62 | 0 | — | 13.25 | 4.77 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.38 | 12.38 | 37 | 32.4 | 19.49 | 2.93 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.80 | 4.80 | 0 | — | 6.88 | 1.55 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.25 | 0.25 | 150 | 34.7 | -3.45 | -3.01 | -4.83 | 70 |
| 6 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 97.16 | -2.84 | 8 | 50.0 | -3.54 | -0.03 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.96 | -4.04 | 0 | — | -3.81 | -1.25 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.90 | -6.10 | 198 | 30.3 | -4.38 | -1.55 | -8.80 | 148 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.00 | -6.34 | -6.42 | 23 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.59 | -7.41 | 0 | — | -7.15 | -1.88 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Insider buying | copy | 90.94 | -9.06 | 50 | 42.0 | -9.17 | -1.83 | -14.79 | 64 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.65 | -9.35 | 0 | — | -8.19 | -2.23 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -13.24 | -7.20 | -13.30 | 57 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.55 | -3.70 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.07 | -12.93 | 17 | 17.6 | -5.42 | -0.83 | -19.56 | 14 |
| 23 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.10 | -2.89 | -14.11 | 558 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.03 | -8.99 | -16.08 | 70 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.37 | -7.48 | -17.11 | 198 |
| 26 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.46 | -18.54 | 188 | 28.2 | -25.34 | -7.04 | -28.11 | 200 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.20 | -6.30 | -14.66 | 88 |
| 29 | Keltner breakout · 1h | breakout | 79.71 | -20.29 | 124 | 25.8 | -24.29 | -6.34 | -27.26 | 157 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -15.68 | -4.94 | -21.99 | 78 |
| 31 | Donchian 55/20 · 1h | breakout | 79.60 | -20.40 | 77 | 13.0 | -24.85 | -6.51 | -29.99 | 84 |
| 32 | Max aggression: 5-day momentum | meta | 78.63 | -21.37 | 21 | 42.9 | -48.27 | -3.24 | -55.24 | 21 |
| 33 | Opening range 15m | breakout | 78.54 | -21.46 | 534 | 31.6 | -15.95 | -4.27 | -21.37 | 672 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.01 | -22.99 | 2 | 0.0 | -18.23 | -2.43 | -26.43 | 1 |
| 35 | Ichimoku · 1h | trend | 74.95 | -25.05 | 101 | 14.9 | -28.61 | -8.36 | -29.95 | 111 |
| 36 | Hold BTC | benchmark | 74.55 | -25.45 | 2 | 0.0 | -17.29 | -2.39 | -28.91 | 1 |
| 37 | ADX DI cross · 1h | trend | 74.43 | -25.57 | 209 | 19.1 | -28.19 | -4.66 | -35.70 | 266 |
| 38 | Stochastic reversion · 1h | reversion | 73.59 | -26.41 | 347 | 42.4 | -33.82 | -5.12 | -35.65 | 425 |
| 39 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.04 | -7.97 | -33.93 | 223 |
| 40 | Supertrend · 1h | trend | 72.15 | -27.85 | 189 | 15.9 | -31.73 | -5.35 | -39.50 | 201 |
| 41 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -37.67 | -2.25 | -57.50 | 39 |
| 42 | Triple EMA stack · 1h | trend | 71.26 | -28.74 | 155 | 14.8 | -33.85 | -6.80 | -39.38 | 180 |
| 43 | RSI momentum · 1h | momentum | 70.87 | -29.13 | 176 | 14.2 | -30.34 | -5.50 | -37.13 | 198 |
| 44 | MFI reversion · 1h | reversion | 70.77 | -29.23 | 440 | 33.6 | -27.61 | -4.11 | -30.08 | 161 |
| 45 | MACD zero-line · 1h | trend | 69.88 | -30.12 | 183 | 17.5 | -28.15 | -5.70 | -34.23 | 203 |
| 46 | EMA 20/50 cross · 1h | trend | 69.65 | -30.35 | 115 | 10.4 | -35.89 | -9.19 | -39.86 | 117 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | Heikin-Ashi · 1h | trend | 68.95 | -31.05 | 474 | 23.0 | -44.96 | -9.84 | -45.38 | 639 |
| 49 | MACD cross · 1h | trend | 68.56 | -31.44 | 416 | 22.1 | -40.58 | -6.70 | -45.68 | 478 |
| 50 | ROC + volume · 1h | momentum | 68.49 | -31.51 | 412 | 28.2 | -33.87 | -6.09 | -39.92 | 356 |
| 51 | OBV trend · 1h | momentum | 68.41 | -31.59 | 308 | 19.2 | -35.96 | -7.71 | -39.97 | 256 |
| 52 | CCI reversion · 1h | reversion | 67.73 | -32.27 | 383 | 41.5 | -41.16 | -6.80 | -44.29 | 470 |
| 53 | Donchian 20/10 · 1h | breakout | 67.15 | -32.85 | 159 | 18.2 | -35.10 | -6.53 | -40.51 | 203 |
| 54 | Bollinger reversion · 1h | reversion | 64.37 | -35.62 | 345 | 37.7 | -38.30 | -5.80 | -39.50 | 413 |
| 55 | Williams %R · 1h | reversion | 64.21 | -35.79 | 430 | 40.7 | -46.06 | -7.97 | -47.53 | 564 |
| 56 | EMA 9/21 cross · 1h | trend | 63.46 | -36.54 | 282 | 11.0 | -39.70 | -7.77 | -45.86 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.11 | -39.89 | 1909 | 24.4 | -22.53 | -4.54 | -22.53 | 282 |
| 58 | RSI(14) reversion · 1h | reversion | 59.34 | -40.66 | 205 | 31.7 | -40.28 | -5.88 | -43.22 | 254 |
| 59 | Z-score reversion · 1h | reversion | 57.95 | -42.05 | 225 | 35.1 | -37.39 | -5.21 | -39.39 | 256 |
| 60 | VWAP momentum · 1h | momentum | 56.52 | -43.48 | 969 | 21.8 | -55.73 | -11.35 | -59.22 | 1198 |
| 61 | Candlestick reversal · 1h | reversion | 55.73 | -44.27 | 548 | 26.6 | -47.13 | -8.60 | -49.12 | 634 |
| 62 | Three white soldiers | momentum | 54.93 | -45.07 | 586 | 14.5 | -49.65 | -21.48 | -50.50 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.45 | -99.03 | 5311 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.19 | -25.53 | -82.35 | 1400 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -42.58 | -93.90 | 2451 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.00 | -31.84 | -90.25 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.99 | -39.50 | -91.34 | 2288 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.01 | -31.56 | -90.05 | 2112 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -48.22 | -97.90 | 3465 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -53.15 | -96.45 | 3381 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -38.93 | -93.54 | 2211 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.21 | -33.83 | -82.47 | 1580 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -54.27 | -99.61 | 6098 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.89 | -42.45 | -92.09 | 2549 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.92 | -39.50 | -94.92 | 3280 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.54 | -99.81 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.42 | -43.72 | -92.56 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.46 | -25.45 | -76.32 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -61.17 | -97.68 | 3423 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.20 | -99.06 | 4974 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.54 | -27.44 | -69.24 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -56.56 | -94.64 | 2750 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.31 | -37.75 | -84.59 | 1722 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -69.54 | -99.70 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.84 | -31.19 | -90.84 | 2368 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.06 | -18.82 | -80.13 | 1854 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.50 | -36.36 | -91.52 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.55 | -45.98 | -97.56 | 3920 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -57.55 | -89.32 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.23 | -30.01 | -66.95 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.16 | -23.00 | -72.81 | 1218 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.28 | -18.30 | -81.31 | 1737 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -46.09 | -97.59 | 4328 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -112.19 | -99.94 | 8441 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T15:00 | OBV trend · 1h | sell | SOL-USD | 17.44 | 0.27 | exit signal |
| 2026-11-18T15:00 | ROC + volume · 1h | buy | XRP-USD | 17.13 | — | entry signal |
| 2026-11-18T15:00 | Parabolic SAR · 1h | sell | XRP-USD | 20.68 | 0.29 | exit signal |
| 2026-11-18T15:00 | Parabolic SAR · 1h | sell | SOL-USD | 20.53 | 0.14 | exit signal |
| 2026-11-18T15:00 | Parabolic SAR · 1h | sell | DOGE-USD | 20.32 | -0.07 | exit signal |
| 2026-11-18T15:00 | Three white soldiers | buy | BTC-USD | 13.74 | — | entry signal |
| 2026-11-18T15:00 | Opening range 15m | buy | AMZN | 19.64 | — | entry signal |
| 2026-11-18T14:55 | Opening range 15m | buy | TNA | 19.57 | — | entry signal |
| 2026-11-18T14:55 | Opening range 15m | buy | IWM | 19.57 | — | entry signal |
| 2026-11-18T14:50 | Agent (ML meta-label) | sell | AMD | 15.21 | 0.13 | selected signal exited |
| 2026-11-18T14:50 | VWAP reversion · 1h | sell | AAPL | 22.50 | -0.00 | target is flat |
| 2026-11-18T14:45 | Max aggression: 1-day momentum | sell | SOXL | 71.77 | -3.96 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-18T14:45 | Agent (ML meta-label) | buy | AMD | 15.08 | — | entry |
| 2026-11-18T14:45 | CCI reversion · 1h | buy | ETH-USD | 2.38 | — | entry |
| 2026-11-18T14:45 | CCI reversion · 1h | buy | BTC-USD | 4.77 | — | entry |
| 2026-11-18T14:45 | CCI reversion · 1h | sell | COIN | 7.16 | -0.29 | stop-loss |
| 2026-11-18T14:45 | Z-score reversion · 1h | buy | MSFT | 2.75 | — | entry |
| 2026-11-18T14:45 | Z-score reversion · 1h | sell | COIN | 2.75 | -0.09 | stop-loss |
| 2026-11-18T14:40 | Day trade: Stocks in Play ORB | buy | TNA | 24.93 | — | entry |
| 2026-11-18T14:40 | Day trade: Stocks in Play ORB | buy | IWM | 24.93 | — | entry |
| 2026-11-18T14:40 | Agent (ML meta-label) | sell | AMD | 14.75 | -0.36 | selected signal exited |
| 2026-11-18T14:40 | MFI reversion · 1h | sell | MSTR | 17.54 | -0.16 | stop-loss |
| 2026-11-18T14:40 | VWAP reversion · 1h | sell | MSTR | 21.61 | -1.13 | stop-loss |
| 2026-11-18T14:40 | Volume breakout · 1h | sell | SQQQ | 20.02 | 0.12 | target is flat |
| 2026-11-18T14:35 | Max aggression: 1-day momentum | buy | SOXL | 75.73 | — | entry |
| 2026-11-18T14:35 | Max aggression: 1-day momentum | sell | SQQQ | 75.73 | 2.69 | target is flat |
| 2026-11-18T14:35 | Agent (rotation) | buy | SQQQ | 31.35 | — | following OBV trend |
| 2026-11-18T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 112.95 | — | entry |
| 2026-11-18T14:35 | Agent (ML meta-label) | buy | SQQQ | 15.10 | — | following OBV trend |
| 2026-11-18T14:35 | Agent (ML meta-label) | buy | SPY | 3.02 | — | rebalance up |
| 2026-11-18T14:35 | Agent (ML meta-label) | buy | AMD | 15.10 | — | entry |
| 2026-11-18T14:35 | Agent (ML meta-label) | sell | TQQQ | 15.44 | 0.47 | selected signal exited |
| 2026-11-18T14:35 | MFI reversion · 1h | buy | SPY | 7.50 | — | rebalance up |
| 2026-11-18T14:35 | MFI reversion · 1h | buy | QQQ | 5.79 | — | rebalance up |
| 2026-11-18T14:35 | MFI reversion · 1h | buy | MSTR | 17.69 | — | entry |
| 2026-11-18T14:35 | MFI reversion · 1h | buy | AMZN | 17.69 | — | entry |
| 2026-11-18T14:35 | MFI reversion · 1h | sell | UPRO | 5.13 | 0.09 | target is flat |
| 2026-11-18T14:35 | MFI reversion · 1h | sell | TSLA | 10.15 | 0.07 | target is flat |
| 2026-11-18T14:35 | MFI reversion · 1h | sell | ETHU | 11.59 | -0.24 | target is flat |
| 2026-11-18T14:35 | MFI reversion · 1h | sell | BITX | 9.94 | -0.17 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 15:01:05.000158+00:00 -> 2026-11-18 15:11:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 15:01:05.000158+00:00 -> 2026-11-18 15:11:05.000158+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
