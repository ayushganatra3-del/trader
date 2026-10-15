# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T14:25:05.000158+00:00 · 23704 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 14121 decisions in 2142 calls, $0.1886 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T14:25 | 0 / 12 / 18 | cash |  |
| Breezy | 2026-10-15T14:25 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-10-15T14:25 | 1 / 23 / 6 | ETHU 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.54 | +0.60% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.10 | 5.10 | 0 | — | 4.97 | 2.35 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.39 | 2.67 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.42 | -0.73 | -9.61 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.58 | 2.58 | 1 | 100.0 | 3.18 | 0.91 | -7.93 | 9 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.00 | 1.00 | 0 | — | 4.70 | 1.82 | -5.18 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 9 | VWAP reversion · 1h | reversion | 99.86 | -0.14 | 54 | 35.2 | -10.15 | -2.97 | -13.79 | 123 |
| 10 | Hold SPY | benchmark | 99.70 | -0.29 | 0 | — | -1.19 | -0.65 | -3.35 | 1 |
| 11 | Copy: Insider buying | copy | 99.63 | -0.37 | 20 | 45.0 | -16.47 | -2.63 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 97.93 | -2.07 | 0 | — | -1.84 | -0.74 | -4.45 | 1 |
| 14 | Donchian 55/20 · 1h | breakout | 97.89 | -2.11 | 36 | 16.7 | 7.36 | 1.01 | -22.11 | 112 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.40 | -2.60 | 0 | — | -5.78 | -3.16 | -6.38 | 1 |
| 17 | Trend pullback · 1h | trend | 97.01 | -2.99 | 86 | 24.4 | -24.48 | -7.20 | -25.52 | 165 |
| 18 | Hold BTC | benchmark | 96.89 | -3.11 | 0 | — | 28.88 | 3.34 | -8.68 | 1 |
| 19 | ADX DI cross · 1h | trend | 96.74 | -3.26 | 70 | 21.4 | -8.70 | -1.51 | -14.33 | 252 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.73 | -3.27 | 0 | — | -6.15 | -2.39 | -7.50 | 1 |
| 21 | Daily: Momentum burst | daily | 96.43 | -3.57 | 5 | 20.0 | -4.33 | -0.50 | -17.67 | 39 |
| 22 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.12 | -3.13 | -5.30 | 30 |
| 23 | Agent (rotation) | meta | 95.86 | -4.14 | 101 | 28.7 | -12.05 | -4.04 | -13.21 | 285 |
| 24 | Max aggression: 5-day momentum | meta | 95.27 | -4.73 | 8 | 37.5 | -4.42 | -0.09 | -34.64 | 26 |
| 25 | EMA 20/50 cross · 1h | trend | 94.00 | -6.00 | 50 | 16.0 | 0.90 | 0.31 | -24.19 | 129 |
| 26 | Parabolic SAR · 1h | trend | 93.93 | -6.07 | 93 | 22.6 | 1.50 | 0.38 | -22.73 | 285 |
| 27 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.61 | 1.00 | -9.46 | 103 |
| 28 | Gap and go | momentum | 93.37 | -6.63 | 65 | 12.3 | 8.94 | 2.25 | -6.78 | 201 |
| 29 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -9.32 | -4.05 | -9.91 | 251 |
| 30 | Supertrend · 1h | trend | 92.68 | -7.32 | 73 | 13.7 | 1.66 | 0.40 | -23.16 | 207 |
| 31 | Bollinger breakout · 1h | breakout | 92.65 | -7.35 | 78 | 29.5 | 8.84 | 1.27 | -14.21 | 276 |
| 32 | Daily: Bullish score | daily | 92.62 | -7.38 | 7 | 0.0 | -5.18 | -0.47 | -12.76 | 13 |
| 33 | RSI momentum · 1h | momentum | 92.51 | -7.49 | 73 | 17.8 | 2.18 | 0.46 | -24.95 | 224 |
| 34 | MACD cross · 1h | trend | 91.88 | -8.12 | 154 | 22.1 | -13.22 | -1.81 | -22.72 | 456 |
| 35 | Timing: Nasdaq FTD · TQQQ | daily | 91.79 | -8.21 | 0 | — | -17.58 | -3.32 | -19.22 | 1 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | 6.93 | 1.11 | -12.60 | 120 |
| 37 | Triple EMA stack · 1h | trend | 91.07 | -8.93 | 77 | 16.9 | -8.73 | -0.72 | -33.41 | 236 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 91.04 | -8.96 | 0 | — | 2.40 | 0.52 | -13.89 | 1 |
| 39 | Ichimoku · 1h | trend | 90.54 | -9.46 | 51 | 15.7 | -0.03 | 0.21 | -23.46 | 124 |
| 40 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -10.30 | -3.73 | -10.30 | 123 |
| 41 | Stochastic reversion · 1h | reversion | 89.73 | -10.27 | 127 | 44.1 | -18.76 | -3.48 | -20.41 | 357 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -16.01 | -0.57 | -37.31 | 43 |
| 43 | Opening range 30m | breakout | 89.11 | -10.89 | 169 | 23.1 | -14.03 | -4.18 | -17.60 | 560 |
| 44 | Connors RSI(2) · 1h | reversion | 89.09 | -10.91 | 139 | 39.6 | -23.14 | -6.91 | -24.89 | 248 |
| 45 | OBV trend · 1h | momentum | 88.83 | -11.17 | 164 | 18.9 | -11.88 | -1.03 | -36.08 | 319 |
| 46 | Keltner breakout · 1h | breakout | 88.36 | -11.63 | 51 | 21.6 | -6.38 | -0.64 | -26.75 | 212 |
| 47 | MACD zero-line · 1h | trend | 88.12 | -11.88 | 74 | 16.2 | -21.33 | -4.05 | -22.54 | 224 |
| 48 | MFI reversion · 1h | reversion | 88.03 | -11.97 | 183 | 29.0 | -18.24 | -3.15 | -19.41 | 139 |
| 49 | Donchian 20/10 · 1h | breakout | 86.85 | -13.15 | 72 | 19.4 | -0.21 | 0.17 | -20.38 | 216 |
| 50 | Z-score reversion · 1h | reversion | 86.40 | -13.60 | 70 | 32.9 | -12.48 | -2.15 | -17.27 | 168 |
| 51 | Heikin-Ashi · 1h | trend | 86.37 | -13.63 | 169 | 26.0 | -29.96 | -4.82 | -39.17 | 659 |
| 52 | ROC + volume · 1h | momentum | 86.30 | -13.70 | 179 | 21.2 | -10.65 | -1.42 | -25.27 | 395 |
| 53 | Agent (ML meta-label) | meta | 86.06 | -13.94 | 555 | 17.8 | -5.15 | -0.72 | -15.17 | 407 |
| 54 | VWAP momentum · 1h | momentum | 85.55 | -14.45 | 352 | 21.6 | -36.31 | -5.44 | -43.06 | 1236 |
| 55 | EMA 9/21 cross · 1h | trend | 85.17 | -14.82 | 120 | 12.5 | -9.12 | -1.01 | -26.86 | 321 |
| 56 | Opening range 15m | breakout | 84.76 | -15.24 | 216 | 20.4 | -19.22 | -5.29 | -21.40 | 701 |
| 57 | Three white soldiers | momentum | 83.74 | -16.26 | 187 | 16.0 | -48.68 | -21.57 | -48.92 | 599 |
| 58 | Bollinger reversion · 1h | reversion | 82.71 | -17.29 | 126 | 28.6 | -28.15 | -5.94 | -31.47 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 82.15 | -17.86 | 60 | 21.7 | -12.83 | -2.18 | -18.93 | 160 |
| 60 | CCI reversion · 1h | reversion | 81.72 | -18.28 | 137 | 40.1 | -18.89 | -2.47 | -23.38 | 419 |
| 61 | Williams %R · 1h | reversion | 81.67 | -18.33 | 162 | 41.4 | -33.78 | -5.56 | -34.95 | 508 |
| 62 | Candlestick reversal · 1h | reversion | 79.39 | -20.61 | 179 | 24.6 | -32.93 | -6.05 | -33.80 | 511 |
| 63 | ROC + volume | momentum | 66.50 | -33.50 | 490 | 21.2 | -74.41 | -16.64 | -76.53 | 1681 |
| 64 | RSI(14) reversion | reversion | 65.40 | -34.59 | 558 | 27.2 | -73.72 | -16.71 | -74.04 | 1567 |
| 65 | Volume breakout | breakout | 65.31 | -34.69 | 310 | 13.5 | -63.29 | -17.79 | -63.33 | 885 |
| 66 | Squeeze breakout | breakout | 64.37 | -35.63 | 403 | 14.6 | -63.01 | -17.56 | -63.39 | 1208 |
| 67 | Donchian 55/20 | breakout | 62.52 | -37.48 | 400 | 16.8 | -69.03 | -14.37 | -71.10 | 1268 |
| 68 | EMA 20/50 cross | trend | 60.96 | -39.04 | 420 | 18.8 | -77.47 | -15.10 | -78.49 | 1433 |
| 69 | VWAP reversion | reversion | 58.35 | -41.65 | 580 | 24.5 | -72.31 | -14.91 | -72.61 | 1431 |
| 70 | AI bee: Boozy | ai | 55.77 | -44.23 | 276 | 5.1 | — | — | — | — |
| 71 | Keltner breakout | breakout | 55.72 | -44.28 | 558 | 14.2 | -83.45 | -26.38 | -83.50 | 1836 |
| 72 | Supertrend | trend | 53.76 | -46.24 | 581 | 18.6 | -86.61 | -20.12 | -86.61 | 1896 |
| 73 | Ichimoku | trend | 53.18 | -46.82 | 492 | 9.8 | -81.99 | -22.28 | -82.07 | 1700 |
| 74 | AI bee: Bizzy | ai | 50.85 | -49.16 | 1011 | 8.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.87 | -98.65 | 5350 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -28.97 | -93.52 | 2563 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.65 | -24.12 | -90.73 | 2347 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.48 | -25.86 | -91.51 | 2325 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.49 | -31.56 | -97.49 | 3505 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.56 | -34.41 | -96.58 | 3560 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -24.57 | -94.44 | 2615 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -35.38 | -99.42 | 5753 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.21 | -25.10 | -91.23 | 2617 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.19 | -29.97 | -96.20 | 3543 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.51 | -99.73 | 6160 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -28.81 | -91.95 | 2355 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -36.35 | -97.46 | 3640 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -35.62 | -98.56 | 4696 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.49 | -31.34 | -93.54 | 2775 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -37.88 | -99.56 | 6175 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.44 | -21.82 | -86.54 | 2124 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.93 | -26.94 | -88.06 | 2133 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.10 | -31.91 | -96.14 | 3785 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.44 | -33.04 | -89.44 | 2108 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.85 | -32.81 | -95.91 | 4081 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.01 | -99.89 | 8203 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T14:25 | Agent (ML meta-label) | sell | META | 5.38 | 0.03 | selected signal exited |
| 2026-10-15T14:25 | Agent (ML meta-label) | sell | AAPL | 7.18 | -0.01 | selected signal exited |
| 2026-10-15T14:25 | MFI reversion · 1h | buy | IWM | 22.01 | — | entry |
| 2026-10-15T14:25 | RSI(14) reversion | sell | AMZN | 5.03 | 0.05 | take-profit |
| 2026-10-15T14:25 | Three white soldiers | sell | UPRO | 11.96 | -0.01 | target is flat |
| 2026-10-15T14:25 | Volume breakout | sell | LABU | 16.03 | -0.39 | stop-loss |
| 2026-10-15T14:25 | Keltner breakout | sell | LABU | 7.88 | 0.08 | stop-loss |
| 2026-10-15T14:25 | Opening range 30m | buy | SPY | 1.63 | — | entry |
| 2026-10-15T14:25 | Opening range 30m | buy | NVDA | 8.10 | — | entry |
| 2026-10-15T14:25 | Opening range 30m | sell | LABU | 9.73 | -0.24 | stop-loss |
| 2026-10-15T14:25 | Gap and go | sell | LABU | 23.27 | -0.17 | stop-loss |
| 2026-10-15T14:25 | Ichimoku | sell | LABU | 13.07 | -0.32 | stop-loss |
| 2026-10-15T14:25 | EMA 20/50 cross | buy | SOL-USD | 15.04 | — | entry signal |
| 2026-10-15T14:22 | AI bee: Bizzy | sell | GOOGL | 7.83 | -0.01 | Jev: sell (sell p=0.56) after 30 min |
| 2026-10-15T14:20 | Volume breakout · 1h | sell | SQQQ | 23.89 | 1.29 | target is flat |
| 2026-10-15T14:20 | RSI(14) reversion | buy | TSLA | 5.04 | — | entry |
| 2026-10-15T14:20 | RSI(14) reversion | sell | BITX | 5.11 | 0.14 | take-profit |
| 2026-10-15T14:20 | Three white soldiers | buy | UPRO | 11.97 | — | entry |
| 2026-10-15T14:20 | Keltner breakout | buy | ETH-USD | 7.99 | — | entry signal |
| 2026-10-15T14:20 | Keltner breakout | buy | BTC-USD | 8.00 | — | entry signal |
| 2026-10-15T14:20 | Keltner breakout | sell | TNA | 3.19 | 0.02 | rebalance down |
| 2026-10-15T14:20 | Keltner breakout | sell | SOL-USD | 3.21 | -0.01 | rebalance down |
| 2026-10-15T14:20 | Keltner breakout | sell | LABU | 3.17 | 0.08 | rebalance down |
| 2026-10-15T14:20 | Keltner breakout | sell | IWM | 3.21 | 0.00 | rebalance down |
| 2026-10-15T14:20 | Keltner breakout | sell | GOOGL | 3.21 | -0.00 | rebalance down |
| 2026-10-15T14:20 | Supertrend | buy | XRP-USD | 5.96 | — | entry |
| 2026-10-15T14:20 | Supertrend | buy | MSTR | 5.99 | — | entry signal |
| 2026-10-15T14:20 | Supertrend | buy | BITX | 5.99 | — | entry |
| 2026-10-15T14:20 | Supertrend | sell | SOL-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-15T14:20 | Supertrend | sell | MSFT | 2.96 | -0.02 | rebalance down |
| 2026-10-15T14:20 | Supertrend | sell | META | 3.01 | -0.00 | rebalance down |
| 2026-10-15T14:20 | Supertrend | sell | GOOGL | 2.99 | 0.03 | rebalance down |
| 2026-10-15T14:20 | Supertrend | sell | ETH-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-15T14:20 | Supertrend | sell | BTC-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-15T14:18 | AI bee: Boozy | buy | ETHU | 35.02 | — | Jev: buy (buy p=0.63) |
| 2026-10-15T14:18 | AI bee: Boozy | sell | COIN | 30.39 | 0.22 | Jev: add (buy p=0.50) |
| 2026-10-15T14:15 | AI bee: Bizzy | sell | LABU | 7.99 | -0.01 | Jev: sell (sell p=0.50) after 13 min |
| 2026-10-15T14:15 | Agent (ML meta-label) | buy | AAPL | 7.19 | — | following MFI reversion |
| 2026-10-15T14:15 | VWAP reversion | buy | AAPL | 14.62 | — | entry signal |
| 2026-10-15T14:15 | VWAP reversion | sell | XRP-USD | 14.66 | 0.15 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 14:25:05.000158+00:00 -> 2026-10-15 14:35:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
