# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T14:25:05.000163+00:00 · 21421 ticks

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

Today: 13818 decisions in 2100 calls, $0.1842 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T14:25 | 9 / 14 / 7 | cash |  |
| Breezy | 2026-10-13T14:25 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-13T14:25 | 8 / 21 / 1 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| VWAP reversion | PLTR | 1.89 | +2.20% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.98 | 2.98 | 0 | — | 1.85 | 0.95 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -8.89 | -2.64 | -13.79 | 115 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.62 | 1.62 | 11 | 36.4 | 5.82 | 1.77 | -7.55 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.43 | 1.43 | 0 | — | 6.04 | 2.23 | -5.18 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 7 | Copy: Insider buying | copy | 101.25 | 1.25 | 16 | 50.0 | -15.68 | -2.50 | -21.97 | 75 |
| 8 | Hold SPY | benchmark | 101.08 | 1.08 | 0 | — | 0.65 | 0.43 | -3.66 | 1 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.85 | 0.85 | 0 | — | 1.44 | 0.71 | -3.62 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.73 | 0.73 | 7 | 57.1 | -3.36 | -1.10 | -9.74 | 25 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Hold BTC | benchmark | 99.90 | -0.10 | 0 | — | 31.47 | 3.63 | -8.68 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.85 | -0.15 | 0 | — | -2.61 | -1.45 | -5.09 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.06 | -0.94 | 0 | — | -5.00 | -2.30 | -5.41 | 1 |
| 16 | Timing: Nasdaq FTD · TQQQ | daily | 98.95 | -1.05 | 0 | — | -9.00 | -1.64 | -15.27 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 98.85 | -1.15 | 45 | 33.3 | 3.62 | 2.11 | -1.32 | 74 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.54 | -1.46 | 31 | 12.9 | 12.65 | 1.50 | -18.79 | 113 |
| 20 | Trend pullback · 1h | trend | 98.35 | -1.66 | 82 | 25.6 | -22.66 | -6.31 | -25.67 | 170 |
| 21 | Daily: Bullish score | daily | 98.24 | -1.76 | 5 | 0.0 | 1.23 | 0.35 | -12.76 | 12 |
| 22 | ADX DI cross · 1h | trend | 97.22 | -2.78 | 63 | 19.0 | -5.26 | -0.81 | -13.66 | 253 |
| 23 | Agent (rotation) | meta | 96.77 | -3.23 | 87 | 31.0 | -10.43 | -3.24 | -12.13 | 268 |
| 24 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.93 | -0.44 | -17.67 | 39 |
| 25 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 26 | MACD cross · 1h | trend | 96.19 | -3.81 | 126 | 24.6 | -9.42 | -1.44 | -17.74 | 461 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.73 | -4.27 | 0 | — | 7.68 | 1.31 | -8.36 | 1 |
| 28 | EMA 20/50 cross · 1h | trend | 95.63 | -4.37 | 45 | 15.6 | 10.85 | 1.37 | -19.99 | 138 |
| 29 | Stochastic reversion · 1h | reversion | 95.48 | -4.52 | 107 | 51.4 | -13.33 | -2.55 | -14.88 | 339 |
| 30 | Z-score reversion · 1h | reversion | 95.45 | -4.55 | 49 | 42.9 | 1.54 | 0.44 | -8.60 | 159 |
| 31 | Max aggression: 1-day momentum | meta | 95.45 | -4.55 | 12 | 33.3 | -11.21 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.07 | -4.93 | 61 | 47.5 | -9.07 | -4.72 | -9.54 | 245 |
| 33 | Supertrend · 1h | trend | 94.66 | -5.34 | 58 | 13.8 | 3.14 | 0.58 | -19.02 | 216 |
| 34 | Parabolic SAR · 1h | trend | 94.55 | -5.45 | 88 | 22.7 | 1.30 | 0.36 | -21.86 | 288 |
| 35 | Squeeze breakout · 1h | breakout | 94.16 | -5.84 | 40 | 22.5 | 5.28 | 1.09 | -9.46 | 104 |
| 36 | Gap and go | momentum | 93.32 | -6.68 | 61 | 11.5 | 7.82 | 2.00 | -6.88 | 203 |
| 37 | RSI momentum · 1h | momentum | 93.05 | -6.95 | 66 | 15.2 | 0.77 | 0.30 | -22.67 | 229 |
| 38 | MFI reversion · 1h | reversion | 93.02 | -6.98 | 155 | 31.6 | -7.32 | -1.12 | -16.91 | 128 |
| 39 | Agent (aggressive) | meta | 92.86 | -7.14 | 31 | 35.5 | -9.06 | -4.10 | -9.08 | 118 |
| 40 | Volume breakout · 1h | breakout | 91.93 | -8.07 | 72 | 22.2 | 9.18 | 1.39 | -12.60 | 116 |
| 41 | RSI(14) reversion · 1h | reversion | 91.90 | -8.10 | 36 | 30.6 | -3.67 | -0.67 | -9.40 | 144 |
| 42 | Connors RSI(2) · 1h | reversion | 91.89 | -8.11 | 120 | 41.7 | -18.58 | -6.10 | -21.32 | 255 |
| 43 | Ichimoku · 1h | trend | 91.87 | -8.13 | 48 | 16.7 | 2.23 | 0.47 | -22.34 | 126 |
| 44 | Agent (ML meta-label) | meta | 91.77 | -8.23 | 448 | 17.6 | -0.45 | 0.06 | -12.34 | 407 |
| 45 | Bollinger breakout · 1h | breakout | 91.77 | -8.23 | 75 | 28.0 | 8.71 | 1.25 | -14.21 | 278 |
| 46 | Triple EMA stack · 1h | trend | 90.99 | -9.01 | 71 | 15.5 | -5.69 | -0.44 | -26.53 | 238 |
| 47 | Bollinger reversion · 1h | reversion | 89.32 | -10.68 | 96 | 36.5 | -25.86 | -6.25 | -26.37 | 319 |
| 48 | Opening range 30m | breakout | 89.13 | -10.87 | 154 | 22.1 | -15.25 | -4.58 | -16.60 | 572 |
| 49 | CCI reversion · 1h | reversion | 89.11 | -10.89 | 116 | 44.8 | -9.42 | -1.23 | -14.42 | 410 |
| 50 | OBV trend · 1h | momentum | 89.06 | -10.94 | 151 | 18.5 | -6.94 | -0.59 | -27.71 | 324 |
| 51 | VWAP momentum · 1h | momentum | 88.47 | -11.53 | 313 | 23.3 | -32.12 | -4.73 | -40.50 | 1242 |
| 52 | Williams %R · 1h | reversion | 88.25 | -11.75 | 143 | 45.5 | -25.72 | -4.21 | -28.82 | 502 |
| 53 | MACD zero-line · 1h | trend | 87.98 | -12.02 | 68 | 17.6 | -20.21 | -3.80 | -21.55 | 230 |
| 54 | Donchian 20/10 · 1h | breakout | 87.79 | -12.21 | 64 | 17.2 | -0.04 | 0.20 | -19.51 | 215 |
| 55 | Keltner breakout · 1h | breakout | 87.57 | -12.43 | 46 | 19.6 | -8.61 | -0.89 | -26.77 | 213 |
| 56 | EMA 9/21 cross · 1h | trend | 87.28 | -12.72 | 110 | 12.7 | -6.64 | -0.62 | -23.21 | 330 |
| 57 | Heikin-Ashi · 1h | trend | 87.21 | -12.79 | 158 | 27.2 | -30.21 | -4.99 | -38.02 | 679 |
| 58 | Candlestick reversal · 1h | reversion | 86.99 | -13.01 | 135 | 29.6 | -28.95 | -5.68 | -29.88 | 496 |
| 59 | Max aggression: 5-day momentum | meta | 86.84 | -13.16 | 8 | 37.5 | -11.28 | -0.74 | -34.64 | 28 |
| 60 | Opening range 15m | breakout | 86.62 | -13.38 | 184 | 20.1 | -17.80 | -4.88 | -19.72 | 700 |
| 61 | Three white soldiers | momentum | 86.45 | -13.55 | 156 | 17.3 | -47.89 | -22.75 | -48.13 | 587 |
| 62 | ROC + volume · 1h | momentum | 86.34 | -13.66 | 169 | 20.7 | -7.74 | -0.85 | -25.05 | 390 |
| 63 | ROC + volume | momentum | 73.27 | -26.73 | 430 | 22.8 | -72.34 | -15.98 | -74.65 | 1674 |
| 64 | Squeeze breakout | breakout | 68.70 | -31.30 | 362 | 15.2 | -62.38 | -18.16 | -62.47 | 1231 |
| 65 | Volume breakout | breakout | 68.38 | -31.62 | 288 | 14.6 | -61.47 | -17.42 | -61.47 | 890 |
| 66 | EMA 20/50 cross | trend | 67.70 | -32.30 | 365 | 20.3 | -75.93 | -14.75 | -76.17 | 1441 |
| 67 | RSI(14) reversion | reversion | 67.43 | -32.57 | 443 | 26.6 | -74.17 | -17.42 | -74.33 | 1505 |
| 68 | Donchian 55/20 | breakout | 66.01 | -33.99 | 369 | 17.3 | -68.28 | -14.30 | -69.48 | 1299 |
| 69 | VWAP reversion | reversion | 62.86 | -37.14 | 470 | 25.1 | -72.25 | -15.36 | -72.29 | 1394 |
| 70 | Supertrend | trend | 60.60 | -39.40 | 510 | 20.0 | -85.65 | -20.20 | -85.85 | 1900 |
| 71 | Keltner breakout | breakout | 60.37 | -39.63 | 497 | 15.3 | -83.01 | -26.30 | -83.10 | 1848 |
| 72 | AI bee: Boozy | ai | 59.79 | -40.21 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.56 | -43.44 | 441 | 9.8 | -82.12 | -22.71 | -82.15 | 1728 |
| 74 | MFI reversion | reversion | 54.10 | -45.90 | 635 | 19.8 | -87.86 | -27.47 | -87.89 | 2106 |
| 75 | AI bee: Bizzy | ai | 53.74 | -46.26 | 920 | 8.3 | — | — | — | — |
| 76 | Z-score reversion | reversion | 53.06 | -46.94 | 593 | 22.3 | -86.28 | -22.48 | -86.32 | 2088 |
| 77 | ADX DI cross | trend | 52.76 | -47.24 | 621 | 10.5 | -89.15 | -34.02 | -89.17 | 2121 |
| 78 | Donchian 20/10 | breakout | 52.10 | -47.90 | 699 | 17.9 | -90.56 | -24.97 | -90.66 | 2648 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 642 | 15.1 | -91.19 | -28.53 | -91.30 | 2345 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.50 | -29.05 | -98.54 | 5346 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.04 | -28.96 | -93.07 | 2600 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.21 | -24.38 | -90.34 | 2373 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.34 | -26.44 | -91.41 | 2333 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.27 | -31.62 | -97.29 | 3518 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -34.42 | -96.31 | 3586 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -25.13 | -94.28 | 2637 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.31 | -99.36 | 5656 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.35 | -31.37 | -96.35 | 3599 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.38 | -99.72 | 6131 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.31 | -37.38 | -97.32 | 3663 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -36.23 | -98.53 | 4667 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.25 | -31.92 | -93.29 | 2802 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.18 | -99.54 | 6111 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -32.85 | -96.04 | 3739 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -33.90 | -95.74 | 4039 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.90 | -99.89 | 8216 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T14:25 | Agent (ML meta-label) | sell | AAPL | 7.07 | 0.01 | selected signal exited |
| 2026-10-13T14:25 | Keltner breakout | buy | MSFT | 3.48 | — | entry signal |
| 2026-10-13T14:25 | Keltner breakout | sell | AAPL | 3.48 | 0.01 | rebalance down |
| 2026-10-13T14:25 | Opening range 30m | buy | MSTR | 12.74 | — | entry signal |
| 2026-10-13T14:25 | Opening range 30m | buy | ETHU | 12.74 | — | entry signal |
| 2026-10-13T14:25 | Opening range 30m | sell | TECL | 9.56 | -0.03 | rebalance down |
| 2026-10-13T14:25 | Opening range 30m | sell | SOXL | 9.45 | -0.08 | rebalance down |
| 2026-10-13T14:25 | Opening range 30m | sell | NVDA | 5.13 | -0.00 | rebalance down |
| 2026-10-13T14:25 | Opening range 30m | sell | AMD | 5.07 | -0.02 | rebalance down |
| 2026-10-13T14:21 | Z-score reversion | buy | TSLA | 7.03 | — | entry signal |
| 2026-10-13T14:21 | Z-score reversion | buy | LABU | 6.08 | — | rebalance up |
| 2026-10-13T14:21 | Z-score reversion | sell | TQQQ | 4.38 | -0.02 | rebalance down |
| 2026-10-13T14:21 | Z-score reversion | sell | SOXL | 4.32 | -0.04 | rebalance down |
| 2026-10-13T14:21 | Z-score reversion | sell | QQQ | 4.41 | -0.01 | rebalance down |
| 2026-10-13T14:21 | Squeeze breakout | buy | XRP-USD | 3.43 | — | rebalance up |
| 2026-10-13T14:21 | Squeeze breakout | sell | META | 3.43 | 0.02 | rebalance down |
| 2026-10-13T14:21 | Ichimoku | buy | META | 14.13 | — | entry signal |
| 2026-10-13T14:21 | Ichimoku | buy | AMZN | 14.13 | — | entry signal |
| 2026-10-13T14:15 | Agent (ML meta-label) | buy | AAPL | 7.06 | — | entry |
| 2026-10-13T14:15 | Agent (ML meta-label) | sell | SPY | 7.05 | -0.01 | selected signal exited |
| 2026-10-13T14:15 | Agent (aggressive) | sell | AMZN | 46.28 | -0.29 | selected signal exited |
| 2026-10-13T14:15 | Agent | sell | AMZN | 18.94 | -0.12 | selected signal exited |
| 2026-10-13T14:15 | Squeeze breakout · 1h | sell | GOOGL | 23.53 | -0.05 | stop-loss |
| 2026-10-13T14:15 | Keltner breakout · 1h | sell | GOOGL | 21.55 | -0.15 | stop-loss |
| 2026-10-13T14:15 | Bollinger breakout · 1h | sell | GOOGL | 22.87 | -0.05 | stop-loss |
| 2026-10-13T14:15 | ROC + volume · 1h | sell | ETHU | 21.63 | 0.01 | target is flat |
| 2026-10-13T14:15 | MFI reversion | buy | ETHU | 13.54 | — | entry signal |
| 2026-10-13T14:15 | Z-score reversion | buy | LABU | 2.76 | — | entry signal |
| 2026-10-13T14:15 | RSI(14) reversion | buy | TSLA | 3.56 | — | rebalance up |
| 2026-10-13T14:15 | RSI(14) reversion | buy | TNA | 7.51 | — | entry signal |
| 2026-10-13T14:15 | RSI(14) reversion | buy | IWM | 7.51 | — | entry signal |
| 2026-10-13T14:15 | RSI(14) reversion | sell | TQQQ | 3.66 | 0.00 | rebalance down |
| 2026-10-13T14:15 | RSI(14) reversion | sell | TECL | 3.78 | 0.04 | rebalance down |
| 2026-10-13T14:15 | RSI(14) reversion | sell | SOXL | 3.80 | 0.05 | rebalance down |
| 2026-10-13T14:15 | RSI(14) reversion | sell | QQQ | 3.65 | -0.00 | rebalance down |
| 2026-10-13T14:15 | RSI(14) reversion | sell | NVDA | 3.68 | 0.01 | rebalance down |
| 2026-10-13T14:15 | Squeeze breakout | buy | XRP-USD | 7.01 | — | entry signal |
| 2026-10-13T14:15 | Squeeze breakout | buy | ETH-USD | 13.72 | — | entry signal |
| 2026-10-13T14:15 | Squeeze breakout | sell | COIN | 3.57 | -0.00 | rebalance down |
| 2026-10-13T14:15 | Keltner breakout | buy | XRP-USD | 8.00 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 14:25:05.000163+00:00 -> 2026-10-13 14:35:05.000163+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
