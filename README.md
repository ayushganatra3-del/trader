# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T18:25:05.000162+00:00 · 21603 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.20 (-4.80%)

Closed trades 62, win rate 48.4%, fees £2.34, max drawdown -5.38%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| IWM | 19.03 | -0.02 |

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

Today: 30174 decisions in 2646 calls, $0.3756 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T18:25 | 4 / 10 / 16 | SOXL 14% |  |
| Breezy | 2026-10-13T18:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-13T18:25 | 1 / 27 / 2 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.22 | +2.54% | 5 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.41 | 3.41 | 0 | — | 2.29 | 1.15 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -8.83 | -2.62 | -13.79 | 116 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.37 | 1.37 | 11 | 36.4 | 5.53 | 1.70 | -7.55 | 43 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | Copy: Insider buying | copy | 101.19 | 1.19 | 16 | 50.0 | -15.94 | -2.54 | -21.97 | 75 |
| 7 | Hold SPY | benchmark | 101.11 | 1.11 | 0 | — | 0.56 | 0.38 | -3.66 | 1 |
| 8 | Copy: Congress Democrats (NANC) | copy | 100.53 | 0.53 | 0 | — | 0.37 | 0.22 | -3.55 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.49 | 0.49 | 7 | 57.1 | -3.63 | -1.20 | -9.74 | 25 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 100.31 | 0.31 | 0 | — | 5.31 | 2.04 | -5.18 | 1 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.82 | -0.18 | 0 | — | -2.64 | -1.46 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.21 | -0.79 | 0 | — | 30.74 | 3.57 | -8.68 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 16 | Timing: Nasdaq FTD · TQQQ | daily | 98.77 | -1.23 | 0 | — | -9.09 | -1.66 | -15.27 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.34 | -1.66 | 0 | — | -5.32 | -2.44 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.94 | -2.06 | 82 | 25.6 | -22.88 | -6.44 | -25.58 | 172 |
| 20 | Donchian 55/20 · 1h | breakout | 97.89 | -2.12 | 31 | 12.9 | 7.34 | 1.02 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.56 | -2.44 | 5 | 0.0 | 0.39 | 0.25 | -12.76 | 12 |
| 22 | ADX DI cross · 1h | trend | 96.79 | -3.21 | 63 | 19.0 | -6.04 | -0.95 | -13.66 | 250 |
| 23 | Agent (rotation) | meta | 96.70 | -3.30 | 87 | 31.0 | -10.15 | -3.65 | -12.09 | 267 |
| 24 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.73 | -0.41 | -17.67 | 39 |
| 25 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 26 | Stochastic reversion · 1h | reversion | 96.27 | -3.73 | 107 | 51.4 | -14.21 | -2.77 | -16.35 | 345 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 96.03 | -3.97 | 0 | — | 7.33 | 1.26 | -8.36 | 1 |
| 28 | Max aggression: 1-day momentum | meta | 95.73 | -4.27 | 12 | 33.3 | -10.99 | -0.25 | -37.31 | 42 |
| 29 | EMA 20/50 cross · 1h | trend | 95.50 | -4.50 | 45 | 15.6 | 10.83 | 1.37 | -19.84 | 138 |
| 30 | MACD cross · 1h | trend | 95.42 | -4.58 | 129 | 24.0 | -10.41 | -1.48 | -19.25 | 457 |
| 31 | Z-score reversion · 1h | reversion | 95.29 | -4.71 | 50 | 44.0 | 2.07 | 0.54 | -8.60 | 161 |
| 32 | Agent | meta | 95.20 | -4.80 | 62 | 48.4 | -11.26 | -6.29 | -12.16 | 240 |
| 33 | Parabolic SAR · 1h | trend | 94.04 | -5.96 | 90 | 22.2 | 1.54 | 0.39 | -22.47 | 289 |
| 34 | Squeeze breakout · 1h | breakout | 94.03 | -5.97 | 40 | 22.5 | 4.81 | 1.05 | -9.46 | 102 |
| 35 | Supertrend · 1h | trend | 94.01 | -5.99 | 60 | 13.3 | 2.67 | 0.53 | -19.21 | 216 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -6.94 | -3.07 | -8.42 | 115 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 7.57 | 1.94 | -6.98 | 203 |
| 38 | RSI momentum · 1h | momentum | 92.86 | -7.14 | 66 | 15.2 | 2.73 | 0.52 | -24.25 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.12 | -7.88 | 162 | 31.5 | -8.28 | -1.29 | -17.02 | 132 |
| 40 | Connors RSI(2) · 1h | reversion | 92.03 | -7.97 | 125 | 43.2 | -18.37 | -6.00 | -21.32 | 259 |
| 41 | Ichimoku · 1h | trend | 91.49 | -8.51 | 48 | 16.7 | 1.77 | 0.41 | -22.34 | 126 |
| 42 | Agent (ML meta-label) | meta | 91.19 | -8.80 | 478 | 17.6 | -4.42 | -0.70 | -13.48 | 393 |
| 43 | RSI(14) reversion · 1h | reversion | 91.17 | -8.83 | 37 | 32.4 | -5.78 | -1.16 | -9.40 | 153 |
| 44 | Bollinger breakout · 1h | breakout | 91.02 | -8.98 | 75 | 28.0 | 7.53 | 1.11 | -14.21 | 278 |
| 45 | Volume breakout · 1h | breakout | 90.99 | -9.01 | 73 | 23.3 | 8.08 | 1.25 | -12.60 | 120 |
| 46 | Triple EMA stack · 1h | trend | 90.85 | -9.15 | 71 | 15.5 | -7.77 | -0.62 | -32.61 | 240 |
| 47 | Bollinger reversion · 1h | reversion | 89.80 | -10.20 | 96 | 36.5 | -24.53 | -5.91 | -25.41 | 324 |
| 48 | Williams %R · 1h | reversion | 89.04 | -10.96 | 143 | 45.5 | -27.13 | -4.57 | -29.39 | 509 |
| 49 | CCI reversion · 1h | reversion | 88.68 | -11.32 | 117 | 45.3 | -10.05 | -1.33 | -14.42 | 412 |
| 50 | OBV trend · 1h | momentum | 88.39 | -11.62 | 156 | 17.9 | -7.32 | -0.63 | -27.70 | 326 |
| 51 | Opening range 30m | breakout | 88.20 | -11.80 | 162 | 21.0 | -16.05 | -4.81 | -17.60 | 578 |
| 52 | MACD zero-line · 1h | trend | 87.70 | -12.30 | 69 | 17.4 | -22.28 | -4.36 | -23.02 | 229 |
| 53 | VWAP momentum · 1h | momentum | 87.48 | -12.52 | 324 | 23.1 | -32.83 | -4.87 | -40.43 | 1246 |
| 54 | Donchian 20/10 · 1h | breakout | 87.24 | -12.76 | 65 | 16.9 | 1.30 | 0.36 | -19.51 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 87.10 | -12.90 | 8 | 37.5 | -11.06 | -0.72 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 87.00 | -13.00 | 47 | 19.1 | -8.63 | -0.94 | -26.76 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 86.78 | -13.22 | 110 | 12.7 | -9.48 | -1.14 | -24.20 | 327 |
| 58 | Heikin-Ashi · 1h | trend | 86.76 | -13.24 | 163 | 27.0 | -30.27 | -5.01 | -38.20 | 677 |
| 59 | Three white soldiers | momentum | 86.76 | -13.24 | 161 | 18.6 | -47.67 | -22.34 | -48.06 | 588 |
| 60 | Candlestick reversal · 1h | reversion | 86.37 | -13.63 | 138 | 30.4 | -30.98 | -6.08 | -31.49 | 502 |
| 61 | Opening range 15m | breakout | 85.60 | -14.40 | 198 | 18.7 | -18.75 | -5.15 | -20.82 | 710 |
| 62 | ROC + volume · 1h | momentum | 85.55 | -14.46 | 171 | 20.5 | -8.66 | -0.98 | -25.19 | 394 |
| 63 | ROC + volume | momentum | 72.17 | -27.83 | 448 | 22.8 | -72.46 | -16.19 | -74.52 | 1670 |
| 64 | Squeeze breakout | breakout | 68.51 | -31.49 | 368 | 15.8 | -62.23 | -17.94 | -62.28 | 1216 |
| 65 | Volume breakout | breakout | 68.17 | -31.83 | 290 | 14.5 | -61.42 | -17.33 | -61.50 | 891 |
| 66 | RSI(14) reversion | reversion | 67.36 | -32.64 | 456 | 27.2 | -73.74 | -17.12 | -74.08 | 1491 |
| 67 | EMA 20/50 cross | trend | 67.15 | -32.85 | 371 | 19.9 | -76.11 | -14.86 | -76.33 | 1431 |
| 68 | Donchian 55/20 | breakout | 65.04 | -34.96 | 377 | 17.0 | -68.60 | -14.38 | -69.93 | 1278 |
| 69 | VWAP reversion | reversion | 62.92 | -37.08 | 480 | 25.4 | -71.82 | -15.32 | -71.94 | 1391 |
| 70 | Supertrend | trend | 60.41 | -39.59 | 522 | 19.5 | -85.65 | -20.25 | -85.77 | 1909 |
| 71 | AI bee: Boozy | ai | 59.89 | -40.11 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.45 | -40.55 | 516 | 14.9 | -83.13 | -26.76 | -83.13 | 1854 |
| 73 | Ichimoku | trend | 55.72 | -44.28 | 459 | 9.4 | -82.13 | -22.79 | -82.24 | 1728 |
| 74 | AI bee: Bizzy | ai | 54.07 | -45.93 | 933 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.50 | -46.50 | 656 | 20.1 | -87.81 | -27.65 | -87.84 | 2111 |
| 76 | Z-score reversion | reversion | 52.73 | -47.27 | 608 | 23.0 | -86.11 | -22.14 | -86.19 | 2088 |
| 77 | ADX DI cross | trend | 52.21 | -47.79 | 640 | 10.5 | -89.15 | -33.83 | -89.17 | 2118 |
| 78 | Donchian 20/10 | breakout | 51.35 | -48.66 | 719 | 17.5 | -90.63 | -25.24 | -90.64 | 2639 |
| 79 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -29.22 | -98.50 | 5298 |
| 80 | MACD zero-line | trend | 50.50 | -49.50 | 665 | 15.0 | -91.26 | -28.79 | -91.26 | 2344 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.15 | -29.34 | -93.15 | 2597 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.48 | -90.23 | 2372 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.57 | -26.87 | -91.57 | 2349 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.27 | -31.82 | -97.28 | 3518 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -34.85 | -96.32 | 3566 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -25.75 | -94.47 | 2647 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.00 | -99.35 | 5645 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.31 | -31.02 | -96.31 | 3595 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.19 | -99.72 | 6144 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.27 | -97.36 | 3679 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -35.99 | -98.53 | 4675 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.28 | -31.95 | -93.28 | 2790 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.98 | -99.54 | 6123 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -32.39 | -96.01 | 3739 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -33.54 | -95.68 | 4042 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.55 | -99.89 | 8218 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T18:25 | AI bee: Bizzy | buy | SOXL | 7.64 | — | Jev: buy (buy p=0.57) |
| 2026-10-13T18:25 | MFI reversion | buy | LABU | 7.06 | — | entry signal |
| 2026-10-13T18:25 | MFI reversion | buy | ETHU | 8.92 | — | entry signal |
| 2026-10-13T18:25 | MFI reversion | sell | UPRO | 4.44 | 0.00 | rebalance down |
| 2026-10-13T18:25 | MFI reversion | sell | TECL | 4.48 | -0.00 | rebalance down |
| 2026-10-13T18:25 | MFI reversion | sell | MSTR | 4.44 | -0.02 | rebalance down |
| 2026-10-13T18:25 | Keltner breakout | sell | TECL | 9.90 | -0.02 | target is flat |
| 2026-10-13T18:25 | Ichimoku | buy | UPRO | 5.60 | — | rebalance up |
| 2026-10-13T18:25 | Ichimoku | sell | MSFT | 13.88 | -0.03 | exit signal |
| 2026-10-13T18:20 | AI bee: Bizzy | sell | TNA | 7.65 | -0.01 | Jev: sell (sell p=0.70) after 11 min |
| 2026-10-13T18:20 | Agent (ML meta-label) | buy | SOXL | 6.56 | — | entry |
| 2026-10-13T18:20 | Agent (ML meta-label) | sell | TECL | 6.56 | -0.02 | selected signal exited |
| 2026-10-13T18:20 | Keltner breakout · 1h | buy | SQQQ | 8.38 | — | rebalance up |
| 2026-10-13T18:20 | Keltner breakout · 1h | buy | META | 4.37 | — | rebalance up |
| 2026-10-13T18:20 | Keltner breakout · 1h | buy | AAPL | 4.45 | — | rebalance up |
| 2026-10-13T18:20 | Keltner breakout · 1h | sell | AMZN | 21.49 | -0.22 | stop-loss |
| 2026-10-13T18:20 | MFI reversion | buy | UPRO | 4.44 | — | rebalance up |
| 2026-10-13T18:20 | MFI reversion | buy | TECL | 2.68 | — | rebalance up |
| 2026-10-13T18:20 | MFI reversion | buy | MSTR | 4.48 | — | rebalance up |
| 2026-10-13T18:20 | MFI reversion | sell | AMZN | 8.91 | -0.04 | stop-loss |
| 2026-10-13T18:20 | VWAP reversion | sell | BITX | 15.66 | -0.00 | target is flat |
| 2026-10-13T18:20 | Volume breakout | sell | TNA | 17.01 | -0.04 | target is flat |
| 2026-10-13T18:20 | ROC + volume | sell | TNA | 18.00 | -0.04 | target is flat |
| 2026-10-13T18:20 | MACD zero-line | buy | TQQQ | 5.61 | — | entry |
| 2026-10-13T18:20 | MACD zero-line | buy | SOL-USD | 5.62 | — | entry signal |
| 2026-10-13T18:20 | MACD zero-line | buy | QQQ | 5.62 | — | entry |
| 2026-10-13T18:20 | MACD zero-line | sell | UPRO | 2.79 | -0.01 | rebalance down |
| 2026-10-13T18:20 | MACD zero-line | sell | TNA | 2.80 | -0.01 | rebalance down |
| 2026-10-13T18:20 | MACD zero-line | sell | SPY | 2.81 | -0.00 | rebalance down |
| 2026-10-13T18:20 | MACD zero-line | sell | PLTR | 2.82 | 0.01 | rebalance down |
| 2026-10-13T18:20 | MACD zero-line | sell | MSFT | 2.81 | -0.00 | rebalance down |
| 2026-10-13T18:20 | MACD zero-line | sell | IWM | 2.81 | 0.00 | rebalance down |
| 2026-10-13T18:15 | Agent (ML meta-label) | buy | TECL | 6.58 | — | entry |
| 2026-10-13T18:15 | Agent (ML meta-label) | sell | UPRO | 6.58 | -0.01 | selected signal exited |
| 2026-10-13T18:15 | MFI reversion | buy | TECL | 3.62 | — | rebalance up |
| 2026-10-13T18:15 | MFI reversion | sell | TNA | 8.92 | 0.05 | exit signal |
| 2026-10-13T18:15 | VWAP reversion | buy | BITX | 3.12 | — | rebalance up |
| 2026-10-13T18:15 | EMA 20/50 cross | buy | SOXL | 4.50 | — | entry signal |
| 2026-10-13T18:15 | EMA 20/50 cross | sell | AMD | 4.50 | 0.01 | rebalance down |
| 2026-10-13T18:10 | Agent (ML meta-label) | buy | UPRO | 6.58 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 18:25:05.000162+00:00 -> 2026-10-13 18:35:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
