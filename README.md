# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T20:25:05.000141+00:00 · 48844 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.06 (-10.94%)

Closed trades 147, win rate 37.4%, fees £4.06, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-05 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 38931 decisions in 3234 calls, $0.4829 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T20:25 | 16 / 9 / 5 | cash |  |
| Breezy | 2026-11-05T20:25 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-05T20:25 | 12 / 15 / 3 | COIN 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.21 | 13.21 | 18 | 66.7 | 16.12 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.93 | 11.93 | 0 | — | 13.59 | 4.70 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.45 | 7.45 | 28 | 25.0 | 16.15 | 2.73 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.37 | 3.37 | 28 | 42.9 | 1.73 | 0.54 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.49 | -0.51 | 0 | — | 3.28 | 1.03 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.94 | -1.06 | 106 | 46.2 | -12.99 | -3.28 | -13.91 | 143 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.68 | -2.32 | 116 | 34.5 | 4.85 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.57 | -5.30 | -6.27 | 20 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.40 | -4.60 | 0 | — | -3.49 | -1.30 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.04 | 0.10 | -9.18 | 218 |
| 14 | Agent (rotation) | meta | 95.08 | -4.92 | 174 | 27.6 | -6.67 | -3.79 | -10.36 | 173 |
| 15 | Hold SPY | benchmark | 94.17 | -5.83 | 0 | — | -4.05 | -1.57 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 17 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -11.24 | -1.28 | -17.84 | 8 |
| 18 | Trend pullback · 1h | trend | 92.06 | -7.94 | 105 | 22.9 | -15.26 | -5.53 | -17.86 | 80 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.44 | -9.56 | 0 | — | -6.83 | -2.12 | -10.50 | 1 |
| 21 | Opening range 30m | breakout | 89.82 | -10.18 | 365 | 32.9 | -16.00 | -5.16 | -17.56 | 579 |
| 22 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -13.61 | -7.78 | -14.01 | 210 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.71 | -3.74 | -14.68 | 88 |
| 24 | Daily: Bullish score | daily | 88.55 | -11.45 | 14 | 21.4 | -4.94 | -0.66 | -16.58 | 14 |
| 25 | Hold BTC ⏸ | benchmark | 88.43 | -11.57 | 1 | 0.0 | -5.07 | -0.57 | -13.41 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.21 | -12.79 | 166 | 27.1 | -15.99 | -3.51 | -20.02 | 244 |
| 27 | Donchian 55/20 · 1h | breakout | 86.25 | -13.74 | 71 | 14.1 | -12.85 | -2.62 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.22 | -13.78 | 40 | 37.5 | -25.18 | -5.00 | -26.03 | 65 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -30.88 | -1.91 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.58 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.60 | -16.40 | 445 | 30.6 | -19.88 | -5.92 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.39 | -17.61 | 144 | 27.8 | -14.04 | -3.22 | -18.40 | 96 |
| 33 | Keltner breakout · 1h | breakout | 81.64 | -18.36 | 106 | 23.6 | -22.82 | -4.74 | -24.41 | 179 |
| 34 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -27.37 | -4.51 | -28.61 | 384 |
| 35 | Connors RSI(2) · 1h | reversion | 80.58 | -19.42 | 202 | 40.1 | -20.94 | -6.99 | -21.42 | 131 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -14.48 | -2.02 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -24.53 | -4.06 | -26.36 | 261 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -17.00 | -2.55 | -18.76 | 152 |
| 39 | Bollinger breakout · 1h | breakout | 78.85 | -21.15 | 165 | 23.6 | -23.79 | -4.96 | -26.52 | 250 |
| 40 | Ichimoku · 1h | trend | 78.38 | -21.62 | 94 | 14.9 | -24.11 | -4.92 | -28.82 | 130 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -28.75 | -4.71 | -30.63 | 443 |
| 42 | Heikin-Ashi · 1h | trend | 76.79 | -23.21 | 385 | 23.1 | -42.70 | -8.96 | -44.25 | 674 |
| 43 | EMA 20/50 cross · 1h | trend | 76.30 | -23.70 | 102 | 10.8 | -22.84 | -4.11 | -30.17 | 131 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.31 | -5.47 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.72 | -25.28 | 142 | 14.8 | -30.78 | -6.49 | -33.06 | 211 |
| 46 | Supertrend · 1h | trend | 73.74 | -26.26 | 166 | 13.3 | -29.94 | -5.19 | -34.26 | 217 |
| 47 | RSI momentum · 1h | momentum | 73.60 | -26.40 | 158 | 12.7 | -29.64 | -5.63 | -32.33 | 224 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -36.37 | -6.39 | -38.81 | 472 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -26.19 | -4.31 | -26.79 | 221 |
| 50 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -35.22 | -4.96 | -37.28 | 30 |
| 51 | Donchian 20/10 · 1h | breakout | 72.09 | -27.91 | 140 | 20.0 | -31.02 | -5.75 | -34.25 | 218 |
| 52 | Bollinger reversion · 1h ⏸ | reversion | 72.03 | -27.97 | 244 | 38.9 | -33.06 | -6.35 | -33.56 | 373 |
| 53 | Williams %R · 1h ⏸ | reversion | 71.97 | -28.03 | 310 | 44.8 | -37.85 | -6.59 | -38.89 | 524 |
| 54 | ROC + volume · 1h | momentum | 71.37 | -28.63 | 341 | 25.8 | -36.45 | -7.15 | -37.62 | 382 |
| 55 | OBV trend · 1h | momentum | 71.15 | -28.85 | 265 | 17.4 | -34.34 | -7.16 | -34.52 | 299 |
| 56 | VWAP momentum · 1h | momentum | 68.22 | -31.78 | 757 | 22.3 | -56.19 | -12.31 | -56.98 | 1213 |
| 57 | EMA 9/21 cross · 1h | trend | 67.65 | -32.35 | 241 | 10.0 | -39.50 | -8.11 | -39.91 | 335 |
| 58 | Three white soldiers | momentum | 66.53 | -33.47 | 451 | 16.2 | -47.76 | -22.30 | -47.76 | 638 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -27.32 | -4.37 | -29.88 | 203 |
| 60 | Agent (ML meta-label) | meta | 65.38 | -34.62 | 1508 | 22.3 | -8.07 | -1.63 | -17.54 | 319 |
| 61 | Candlestick reversal · 1h ⏸ | reversion | 64.98 | -35.02 | 395 | 28.6 | -38.63 | -7.25 | -39.20 | 558 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -41.52 | -2.57 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.57 | -98.94 | 5126 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.82 | -25.36 | -80.21 | 1406 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.31 | -48.78 | -93.31 | 2497 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.82 | -31.60 | -88.94 | 1894 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -39.96 | -90.57 | 2283 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.67 | -33.44 | -90.75 | 2229 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.65 | -55.93 | -97.66 | 3436 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.11 | -59.93 | -96.11 | 3336 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.69 | -34.28 | -93.75 | 2420 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.68 | -37.38 | -81.68 | 1634 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.50 | -56.56 | -99.51 | 5934 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.49 | -43.98 | -92.57 | 2584 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.88 | -39.51 | -95.91 | 3432 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -77.78 | -99.79 | 6127 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.64 | -44.62 | -91.65 | 2252 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.86 | -27.02 | -74.93 | 1542 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -65.63 | -97.70 | 3497 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.75 | -64.70 | -98.77 | 4839 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.40 | -29.16 | -70.08 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -56.73 | -94.53 | 2743 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -38.02 | -84.73 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -77.19 | -99.64 | 6309 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.89 | -31.55 | -89.08 | 2260 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.40 | -19.64 | -77.78 | 1725 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.16 | -36.91 | -91.20 | 2209 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.52 | -53.04 | -96.58 | 3828 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.34 | -57.16 | -89.34 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.96 | -27.46 | -65.63 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -24.51 | -73.80 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.44 | -17.98 | -77.68 | 1646 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.18 | -52.60 | -97.24 | 4298 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.02 | -99.93 | 8199 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T20:06 | Agent (ML meta-label) | buy | MSTR | 4.68 | — | entry |
| 2026-11-05T20:06 | Agent (ML meta-label) | sell | TQQQ | 1.03 | -0.01 | selected signal exited |
| 2026-11-05T20:06 | Agent (ML meta-label) | sell | SOXL | 4.60 | -0.10 | selected signal exited |
| 2026-11-05T20:06 | Three white soldiers | sell | SOXL | 16.40 | -0.38 | exit signal |
| 2026-11-05T20:06 | Three white soldiers | sell | IWM | 16.74 | -0.05 | exit signal |
| 2026-11-05T20:06 | Three white soldiers | sell | ETHU | 16.71 | -0.12 | exit signal |
| 2026-11-05T20:06 | Three white soldiers | sell | AMZN | 16.66 | -0.14 | stop-loss |
| 2026-11-05T20:00 | OBV trend · 1h | buy | MSFT | 17.84 | — | entry |
| 2026-11-05T20:00 | ROC + volume · 1h | buy | AAPL | 17.71 | — | entry |
| 2026-11-05T20:00 | VWAP momentum · 1h | sell | AMZN | 17.15 | 0.11 | target is flat |
| 2026-11-05T19:55 | Three white soldiers | buy | SOXL | 3.36 | — | rebalance up |
| 2026-11-05T19:55 | Three white soldiers | buy | ETHU | 13.44 | — | rebalance up |
| 2026-11-05T19:55 | Three white soldiers | sell | SPY | 16.81 | 0.01 | target is flat |
| 2026-11-05T19:50 | Three white soldiers | buy | ETHU | 3.39 | — | entry |
| 2026-11-05T19:50 | Three white soldiers | sell | SOXL | 3.39 | 0.01 | rebalance down |
| 2026-11-05T19:45 | Agent (ML meta-label) | buy | TQQQ | 1.04 | — | entry |
| 2026-11-05T19:45 | Agent (ML meta-label) | buy | SOXL | 4.70 | — | following Connors RSI(2) |
| 2026-11-05T19:45 | Agent (ML meta-label) | sell | SQQQ | 4.94 | -0.08 | selected signal exited |
| 2026-11-05T19:45 | Three white soldiers | buy | SPY | 16.80 | — | entry signal |
| 2026-11-05T19:45 | Three white soldiers | buy | SOXL | 16.80 | — | entry signal |
| 2026-11-05T19:45 | Three white soldiers | buy | IWM | 16.80 | — | entry signal |
| 2026-11-05T19:45 | Three white soldiers | buy | AMZN | 16.80 | — | entry signal |
| 2026-11-05T19:30 | Agent (ML meta-label) | buy | SQQQ | 5.03 | — | entry |
| 2026-11-05T19:30 | Agent (ML meta-label) | buy | AMD | 5.03 | — | entry |
| 2026-11-05T19:30 | VWAP momentum · 1h | buy | AMZN | 17.04 | — | entry signal |
| 2026-11-05T19:25 | Agent (ML meta-label) | buy | AAPL | 6.53 | — | entry |
| 2026-11-05T19:25 | Agent (ML meta-label) | sell | SQQQ | 6.53 | 0.00 | selected signal exited |
| 2026-11-05T19:20 | Agent (ML meta-label) | sell | GOOGL | 5.40 | -0.02 | selected signal exited |
| 2026-11-05T19:20 | Agent (ML meta-label) | sell | AAPL | 5.44 | -0.01 | selected signal exited |
| 2026-11-05T19:15 | Agent (ML meta-label) | buy | GOOGL | 5.42 | — | entry |
| 2026-11-05T19:15 | Agent (ML meta-label) | buy | AAPL | 5.46 | — | entry |
| 2026-11-05T19:15 | VWAP reversion · 1h | buy | XRP-USD | 4.93 | — | rebalance up |
| 2026-11-05T19:15 | VWAP reversion · 1h | sell | ETH-USD | 4.93 | -0.05 | rebalance down |
| 2026-11-05T19:10 | Agent (ML meta-label) | buy | SQQQ | 6.53 | — | entry |
| 2026-11-05T19:10 | Agent (ML meta-label) | sell | AAPL | 7.25 | 0.00 | selected signal exited |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | SOL-USD | 10.26 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | PLTR | 10.34 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | META | 10.33 | -0.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | LABU | 10.25 | -0.22 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-05T19:05 | Bollinger reversion · 1h | sell | ETH-USD | 10.28 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 20:25:05.000141+00:00 -> 2026-11-05 20:35:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 20:25:05.000141+00:00 -> 2026-11-05 20:35:05.000141+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 20:25:05.000141+00:00 -> 2026-11-05 20:35:05.000141+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
