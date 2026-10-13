# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T14:55:05.000165+00:00 · 21439 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.07 (-4.93%)

Closed trades 61, win rate 47.5%, fees £2.31, max drawdown -5.37%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-13 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 15444 decisions in 2154 calls, $0.2032 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T14:55 | 2 / 5 / 23 | cash |  |
| Breezy | 2026-10-13T14:55 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-13T14:55 | 0 / 27 / 3 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.35 | +3.18% | 4 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.23 | 3.23 | 0 | — | 2.03 | 1.03 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -8.74 | -2.59 | -13.79 | 115 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.29 | 1.29 | 0 | — | 5.77 | 2.15 | -5.18 | 1 |
| 6 | Hold SPY | benchmark | 101.04 | 1.04 | 0 | — | 0.59 | 0.40 | -3.66 | 1 |
| 7 | Copy: Insider buying | copy | 100.92 | 0.92 | 16 | 50.0 | -16.10 | -2.57 | -21.97 | 75 |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.77 | 0.77 | 11 | 36.4 | 4.88 | 1.52 | -7.55 | 43 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.66 | 0.66 | 0 | — | 1.10 | 0.55 | -3.62 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.90 | -0.10 | 7 | 57.1 | -4.22 | -1.40 | -9.74 | 25 |
| 13 | Hold BTC | benchmark | 99.73 | -0.27 | 0 | — | 31.29 | 3.61 | -8.68 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.68 | -0.32 | 0 | — | -2.63 | -1.45 | -5.09 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.12 | -0.88 | 0 | — | -5.00 | -2.30 | -5.41 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 98.50 | -1.50 | 45 | 33.3 | 3.24 | 1.88 | -1.32 | 74 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 98.34 | -1.67 | 0 | — | -9.09 | -1.65 | -15.27 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 98.23 | -1.77 | 31 | 12.9 | 12.24 | 1.47 | -18.79 | 115 |
| 20 | Trend pullback · 1h | trend | 98.14 | -1.86 | 82 | 25.6 | -22.84 | -6.38 | -25.67 | 173 |
| 21 | Daily: Bullish score | daily | 97.86 | -2.14 | 5 | 0.0 | 1.12 | 0.34 | -12.76 | 12 |
| 22 | ADX DI cross · 1h | trend | 97.17 | -2.83 | 63 | 19.0 | -1.67 | -0.13 | -13.99 | 252 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.65 | -0.40 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | Agent (rotation) | meta | 96.51 | -3.49 | 87 | 31.0 | -9.84 | -3.34 | -11.65 | 275 |
| 26 | Max aggression: 1-day momentum | meta | 96.34 | -3.66 | 12 | 33.3 | -10.44 | -0.22 | -37.31 | 42 |
| 27 | MACD cross · 1h | trend | 95.99 | -4.01 | 128 | 24.2 | -9.52 | -1.45 | -17.82 | 460 |
| 28 | EMA 20/50 cross · 1h | trend | 95.75 | -4.25 | 45 | 15.6 | 10.14 | 1.29 | -20.59 | 136 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 95.73 | -4.27 | 0 | — | 7.68 | 1.31 | -8.36 | 1 |
| 30 | Agent | meta | 95.07 | -4.93 | 61 | 47.5 | -8.86 | -4.56 | -9.41 | 234 |
| 31 | Z-score reversion · 1h | reversion | 95.07 | -4.93 | 49 | 42.9 | 1.80 | 0.49 | -8.60 | 158 |
| 32 | Stochastic reversion · 1h | reversion | 94.78 | -5.22 | 107 | 51.4 | -15.65 | -3.04 | -15.87 | 339 |
| 33 | Parabolic SAR · 1h | trend | 94.52 | -5.48 | 88 | 22.7 | 2.06 | 0.45 | -21.20 | 290 |
| 34 | Supertrend · 1h | trend | 94.48 | -5.52 | 60 | 13.3 | -1.61 | -0.01 | -20.04 | 217 |
| 35 | Squeeze breakout · 1h | breakout | 94.18 | -5.82 | 40 | 22.5 | 17.65 | 2.65 | -9.46 | 103 |
| 36 | Gap and go | momentum | 93.22 | -6.78 | 61 | 11.5 | 7.69 | 1.97 | -6.87 | 203 |
| 37 | RSI momentum · 1h | momentum | 93.01 | -7.00 | 66 | 15.2 | 3.29 | 0.59 | -21.82 | 227 |
| 38 | Agent (aggressive) | meta | 92.86 | -7.14 | 31 | 35.5 | -7.68 | -3.53 | -7.93 | 119 |
| 39 | MFI reversion · 1h | reversion | 92.70 | -7.30 | 155 | 31.6 | -7.80 | -1.21 | -16.97 | 128 |
| 40 | Ichimoku · 1h | trend | 91.80 | -8.20 | 48 | 16.7 | 2.09 | 0.45 | -22.34 | 126 |
| 41 | Bollinger breakout · 1h | breakout | 91.71 | -8.29 | 75 | 28.0 | 9.54 | 1.34 | -14.21 | 278 |
| 42 | Connors RSI(2) · 1h | reversion | 91.70 | -8.30 | 122 | 42.6 | -18.78 | -6.19 | -21.32 | 257 |
| 43 | Volume breakout · 1h | breakout | 91.63 | -8.37 | 72 | 22.2 | 8.81 | 1.34 | -12.60 | 120 |
| 44 | Agent (ML meta-label) | meta | 91.51 | -8.49 | 451 | 17.5 | -3.95 | -0.58 | -14.55 | 424 |
| 45 | RSI(14) reversion · 1h | reversion | 91.40 | -8.60 | 37 | 32.4 | -5.19 | -0.85 | -10.18 | 143 |
| 46 | Triple EMA stack · 1h | trend | 91.08 | -8.92 | 71 | 15.5 | -6.80 | -0.52 | -32.04 | 233 |
| 47 | Bollinger reversion · 1h | reversion | 89.22 | -10.78 | 96 | 36.5 | -26.11 | -6.30 | -26.52 | 319 |
| 48 | OBV trend · 1h | momentum | 88.85 | -11.15 | 151 | 18.5 | -6.85 | -0.57 | -27.73 | 322 |
| 49 | CCI reversion · 1h | reversion | 88.77 | -11.23 | 117 | 45.3 | -9.56 | -1.25 | -14.42 | 410 |
| 50 | Opening range 30m | breakout | 88.31 | -11.70 | 157 | 21.7 | -16.07 | -4.81 | -17.16 | 573 |
| 51 | VWAP momentum · 1h | momentum | 88.26 | -11.74 | 314 | 23.6 | -32.25 | -4.77 | -40.34 | 1244 |
| 52 | MACD zero-line · 1h | trend | 88.18 | -11.82 | 68 | 17.6 | -19.15 | -3.53 | -21.55 | 230 |
| 53 | Williams %R · 1h | reversion | 87.74 | -12.26 | 143 | 45.5 | -25.60 | -4.14 | -29.02 | 508 |
| 54 | Donchian 20/10 · 1h | breakout | 87.68 | -12.32 | 64 | 17.2 | -0.18 | 0.18 | -19.51 | 218 |
| 55 | Max aggression: 5-day momentum | meta | 87.65 | -12.35 | 8 | 37.5 | -10.51 | -0.67 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 87.54 | -12.46 | 46 | 19.6 | -10.17 | -1.16 | -26.77 | 218 |
| 57 | Heikin-Ashi · 1h | trend | 87.25 | -12.75 | 158 | 27.2 | -29.65 | -4.92 | -37.57 | 681 |
| 58 | EMA 9/21 cross · 1h | trend | 87.19 | -12.81 | 110 | 12.7 | -7.28 | -0.72 | -23.21 | 330 |
| 59 | Candlestick reversal · 1h | reversion | 86.66 | -13.34 | 135 | 29.6 | -29.55 | -5.83 | -30.17 | 489 |
| 60 | Three white soldiers | momentum | 86.47 | -13.53 | 156 | 17.3 | -47.89 | -22.74 | -48.13 | 587 |
| 61 | ROC + volume · 1h | momentum | 86.20 | -13.80 | 169 | 20.7 | -8.17 | -0.91 | -25.21 | 396 |
| 62 | Opening range 15m | breakout | 85.90 | -14.10 | 189 | 19.6 | -18.45 | -5.07 | -20.14 | 701 |
| 63 | ROC + volume | momentum | 72.98 | -27.02 | 435 | 23.0 | -72.62 | -16.13 | -74.80 | 1679 |
| 64 | Squeeze breakout | breakout | 68.65 | -31.35 | 362 | 15.2 | -62.47 | -18.19 | -62.51 | 1230 |
| 65 | Volume breakout | breakout | 68.38 | -31.62 | 288 | 14.6 | -61.47 | -17.42 | -61.47 | 890 |
| 66 | EMA 20/50 cross | trend | 67.46 | -32.54 | 365 | 20.3 | -76.10 | -14.82 | -76.17 | 1441 |
| 67 | RSI(14) reversion | reversion | 66.98 | -33.02 | 443 | 26.6 | -74.41 | -17.51 | -74.41 | 1499 |
| 68 | Donchian 55/20 | breakout | 65.65 | -34.34 | 371 | 17.3 | -68.34 | -14.31 | -69.57 | 1294 |
| 69 | VWAP reversion | reversion | 62.99 | -37.01 | 471 | 25.3 | -72.00 | -15.35 | -72.16 | 1392 |
| 70 | Supertrend | trend | 60.36 | -39.65 | 511 | 20.0 | -85.73 | -20.35 | -85.85 | 1900 |
| 71 | Keltner breakout | breakout | 60.11 | -39.89 | 498 | 15.3 | -83.07 | -26.46 | -83.10 | 1849 |
| 72 | AI bee: Boozy | ai | 59.79 | -40.21 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.46 | -43.54 | 442 | 9.7 | -82.13 | -22.70 | -82.14 | 1729 |
| 74 | MFI reversion | reversion | 53.89 | -46.11 | 635 | 19.8 | -87.79 | -27.81 | -87.80 | 2107 |
| 75 | AI bee: Bizzy | ai | 53.64 | -46.36 | 922 | 8.2 | — | — | — | — |
| 76 | ADX DI cross | trend | 52.75 | -47.25 | 621 | 10.5 | -89.14 | -34.01 | -89.16 | 2116 |
| 77 | Z-score reversion | reversion | 52.69 | -47.31 | 595 | 22.2 | -86.37 | -22.50 | -86.37 | 2090 |
| 78 | Donchian 20/10 | breakout | 51.85 | -48.15 | 701 | 17.8 | -90.62 | -25.16 | -90.66 | 2644 |
| 79 | MACD zero-line | trend | 51.16 | -48.84 | 643 | 15.1 | -91.21 | -28.66 | -91.28 | 2341 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -29.09 | -98.52 | 5325 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.06 | -29.07 | -93.06 | 2596 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.21 | -24.41 | -90.31 | 2366 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.37 | -26.50 | -91.42 | 2335 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.28 | -31.79 | -97.30 | 3509 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -34.54 | -96.33 | 3583 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.19 | -24.97 | -94.19 | 2629 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.42 | -99.36 | 5641 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.35 | -31.35 | -96.35 | 3599 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.48 | -99.72 | 6132 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -37.38 | -97.32 | 3658 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -36.39 | -98.54 | 4665 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.29 | -32.12 | -93.29 | 2801 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.26 | -99.54 | 6102 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.06 | -32.96 | -96.06 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.97 | -95.74 | 4030 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.04 | -99.89 | 8221 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T14:55 | Agent (ML meta-label) | buy | AAPL | 7.04 | — | entry |
| 2026-10-13T14:55 | Agent (ML meta-label) | sell | IWM | 7.05 | -0.01 | selected signal exited |
| 2026-10-13T14:55 | VWAP reversion | sell | SQQQ | 15.86 | 0.15 | exit signal |
| 2026-10-13T14:55 | Z-score reversion | buy | TNA | 8.78 | — | entry |
| 2026-10-13T14:55 | Z-score reversion | buy | IWM | 4.76 | — | rebalance up |
| 2026-10-13T14:55 | Z-score reversion | sell | TQQQ | 8.78 | -0.09 | stop-loss |
| 2026-10-13T14:55 | Z-score reversion | sell | QQQ | 8.82 | -0.03 | stop-loss |
| 2026-10-13T14:55 | Keltner breakout | buy | MSFT | 2.43 | — | rebalance up |
| 2026-10-13T14:55 | Keltner breakout | buy | BITX | 7.52 | — | entry |
| 2026-10-13T14:55 | Keltner breakout | sell | MSTR | 9.95 | -0.06 | stop-loss |
| 2026-10-13T14:55 | Opening range 30m | buy | TSLA | 13.92 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 30m | buy | NVDA | 4.97 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 30m | buy | ETHU | 4.98 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 30m | buy | BITX | 8.71 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 30m | buy | AMD | 4.99 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 30m | sell | TECL | 12.55 | -0.22 | stop-loss |
| 2026-10-13T14:55 | Opening range 30m | sell | SOXL | 12.47 | -0.37 | stop-loss |
| 2026-10-13T14:55 | Opening range 30m | sell | MSTR | 12.55 | -0.18 | stop-loss |
| 2026-10-13T14:55 | Opening range 15m | buy | TSLA | 10.69 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 15m | buy | NVDA | 6.48 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 15m | buy | META | 6.44 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 15m | buy | ETHU | 6.50 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 15m | buy | BITX | 6.48 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 15m | buy | AMD | 6.52 | — | rebalance up |
| 2026-10-13T14:55 | Opening range 15m | sell | TQQQ | 7.81 | -0.08 | stop-loss |
| 2026-10-13T14:55 | Opening range 15m | sell | TECL | 7.77 | -0.09 | stop-loss |
| 2026-10-13T14:55 | Opening range 15m | sell | SOXL | 11.89 | -0.35 | stop-loss |
| 2026-10-13T14:55 | Opening range 15m | sell | QQQ | 7.85 | -0.03 | stop-loss |
| 2026-10-13T14:55 | Opening range 15m | sell | MSTR | 7.78 | -0.09 | stop-loss |
| 2026-10-13T14:55 | Ichimoku | buy | SQQQ | 14.12 | — | entry signal |
| 2026-10-13T14:55 | Supertrend | buy | ETHU | 4.64 | — | entry |
| 2026-10-13T14:55 | Supertrend | sell | TECL | 5.41 | -0.06 | exit signal |
| 2026-10-13T14:55 | MACD zero-line | buy | ETHU | 6.30 | — | entry |
| 2026-10-13T14:55 | MACD zero-line | sell | MSTR | 6.30 | -0.05 | exit signal |
| 2026-10-13T14:51 | Z-score reversion | buy | IWM | 4.03 | — | entry signal |
| 2026-10-13T14:51 | Z-score reversion | sell | NVDA | 4.03 | 0.00 | rebalance down |
| 2026-10-13T14:45 | Agent (ML meta-label) | buy | IWM | 7.06 | — | following RSI momentum |
| 2026-10-13T14:45 | Agent (ML meta-label) | sell | AAPL | 7.03 | -0.02 | selected signal exited |
| 2026-10-13T14:45 | MFI reversion | buy | QQQ | 13.53 | — | entry signal |
| 2026-10-13T14:45 | Opening range 30m | buy | TSLA | 3.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 14:55:05.000165+00:00 -> 2026-10-13 15:05:05.000165+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
