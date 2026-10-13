# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T16:55:05.000160+00:00 · 21535 ticks

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

Today: 24096 decisions in 2442 calls, $0.3045 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T16:55 | 2 / 13 / 16 | cash |  |
| Breezy | 2026-10-13T16:55 | 0 / 27 / 4 | cash |  |
| Boozy | 2026-10-13T16:55 | 0 / 29 / 2 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.18 | +2.49% | 5 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.47 | 3.47 | 0 | — | 2.62 | 1.30 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -8.89 | -2.64 | -13.79 | 115 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.43 | 1.43 | 11 | 36.4 | 5.63 | 1.73 | -7.55 | 43 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | Hold SPY | benchmark | 101.06 | 1.06 | 0 | — | 0.58 | 0.39 | -3.66 | 1 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.65 | 0.65 | 0 | — | 5.42 | 2.06 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.59 | 0.59 | 16 | 50.0 | -16.31 | -2.61 | -21.97 | 75 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.55 | 0.55 | 7 | 57.1 | -3.53 | -1.16 | -9.74 | 25 |
| 10 | Copy: Congress Democrats (NANC) | copy | 100.33 | 0.33 | 0 | — | 0.01 | 0.06 | -3.55 | 1 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.81 | -0.19 | 0 | — | -2.61 | -1.45 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.55 | -0.45 | 0 | — | 31.07 | 3.59 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.06 | -0.94 | 0 | — | -5.00 | -2.30 | -5.41 | 1 |
| 16 | Timing: Nasdaq FTD · TQQQ | daily | 98.82 | -1.18 | 0 | — | -9.03 | -1.65 | -15.27 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.93 | -2.07 | 82 | 25.6 | -22.86 | -6.43 | -25.58 | 172 |
| 20 | Donchian 55/20 · 1h | breakout | 97.68 | -2.32 | 31 | 12.9 | 7.14 | 1.00 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.42 | -2.58 | 5 | 0.0 | 0.38 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.72 | -3.29 | 87 | 31.0 | -10.74 | -3.85 | -12.52 | 272 |
| 23 | ADX DI cross · 1h | trend | 96.67 | -3.33 | 63 | 19.0 | -6.16 | -0.94 | -14.11 | 253 |
| 24 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.72 | -0.41 | -17.67 | 39 |
| 25 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 26 | Stochastic reversion · 1h | reversion | 96.22 | -3.77 | 107 | 51.4 | -14.39 | -2.81 | -16.53 | 345 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 96.09 | -3.91 | 0 | — | 7.59 | 1.30 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.75 | -4.25 | 128 | 24.2 | -12.46 | -1.97 | -19.81 | 462 |
| 29 | Max aggression: 1-day momentum | meta | 95.61 | -4.39 | 12 | 33.3 | -11.05 | -0.26 | -37.31 | 42 |
| 30 | EMA 20/50 cross · 1h | trend | 95.58 | -4.42 | 45 | 15.6 | 10.19 | 1.30 | -20.50 | 139 |
| 31 | Z-score reversion · 1h | reversion | 95.34 | -4.66 | 50 | 44.0 | 2.15 | 0.56 | -8.60 | 161 |
| 32 | Agent | meta | 95.07 | -4.93 | 61 | 47.5 | -8.95 | -4.64 | -9.81 | 240 |
| 33 | Supertrend · 1h | trend | 94.26 | -5.74 | 60 | 13.3 | -0.59 | 0.12 | -19.13 | 218 |
| 34 | Parabolic SAR · 1h | trend | 94.14 | -5.86 | 90 | 22.2 | 1.68 | 0.40 | -22.33 | 289 |
| 35 | Squeeze breakout · 1h | breakout | 93.93 | -6.07 | 40 | 22.5 | 4.73 | 1.04 | -9.46 | 102 |
| 36 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 7.57 | 1.94 | -6.98 | 203 |
| 37 | Agent (aggressive) | meta | 92.86 | -7.14 | 31 | 35.5 | -8.19 | -3.62 | -8.43 | 120 |
| 38 | RSI momentum · 1h | momentum | 92.69 | -7.31 | 66 | 15.2 | 3.48 | 0.61 | -22.33 | 226 |
| 39 | MFI reversion · 1h | reversion | 92.33 | -7.67 | 160 | 31.9 | -7.94 | -1.23 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 92.18 | -7.82 | 125 | 43.2 | -18.20 | -5.91 | -21.32 | 259 |
| 41 | Ichimoku · 1h | trend | 91.45 | -8.55 | 48 | 16.7 | 1.77 | 0.42 | -22.34 | 126 |
| 42 | Agent (ML meta-label) | meta | 91.39 | -8.62 | 471 | 17.6 | -4.10 | -0.59 | -14.65 | 401 |
| 43 | RSI(14) reversion · 1h | reversion | 91.30 | -8.70 | 37 | 32.4 | -4.25 | -0.75 | -9.40 | 147 |
| 44 | Volume breakout · 1h | breakout | 91.02 | -8.98 | 72 | 22.2 | 8.16 | 1.26 | -12.60 | 120 |
| 45 | Bollinger breakout · 1h | breakout | 90.95 | -9.05 | 75 | 28.0 | 7.54 | 1.11 | -14.21 | 278 |
| 46 | Triple EMA stack · 1h | trend | 90.84 | -9.16 | 71 | 15.5 | -8.94 | -0.76 | -33.26 | 241 |
| 47 | Bollinger reversion · 1h | reversion | 89.70 | -10.30 | 96 | 36.5 | -25.35 | -6.13 | -26.17 | 324 |
| 48 | CCI reversion · 1h | reversion | 89.04 | -10.96 | 117 | 45.3 | -9.77 | -1.28 | -14.42 | 412 |
| 49 | Williams %R · 1h | reversion | 89.04 | -10.96 | 143 | 45.5 | -27.20 | -4.58 | -29.48 | 509 |
| 50 | Opening range 30m | breakout | 88.39 | -11.61 | 160 | 21.2 | -15.85 | -4.76 | -17.46 | 578 |
| 51 | OBV trend · 1h | momentum | 88.29 | -11.71 | 154 | 18.2 | -7.30 | -0.63 | -27.69 | 326 |
| 52 | VWAP momentum · 1h | momentum | 87.77 | -12.23 | 322 | 23.3 | -32.57 | -4.81 | -40.47 | 1246 |
| 53 | MACD zero-line · 1h | trend | 87.73 | -12.27 | 68 | 17.6 | -22.23 | -4.35 | -23.05 | 228 |
| 54 | Donchian 20/10 · 1h | breakout | 87.32 | -12.68 | 64 | 17.2 | 1.40 | 0.37 | -19.51 | 217 |
| 55 | Three white soldiers | momentum | 87.06 | -12.94 | 157 | 17.8 | -47.51 | -21.97 | -48.13 | 592 |
| 56 | Keltner breakout · 1h | breakout | 87.05 | -12.95 | 46 | 19.6 | -7.21 | -0.75 | -26.75 | 213 |
| 57 | Max aggression: 5-day momentum | meta | 86.99 | -13.01 | 8 | 37.5 | -11.12 | -0.73 | -34.64 | 28 |
| 58 | EMA 9/21 cross · 1h | trend | 86.93 | -13.07 | 110 | 12.7 | -9.45 | -1.14 | -24.20 | 328 |
| 59 | Heikin-Ashi · 1h | trend | 86.82 | -13.18 | 159 | 27.7 | -30.23 | -5.00 | -38.07 | 678 |
| 60 | Candlestick reversal · 1h | reversion | 86.46 | -13.54 | 135 | 29.6 | -30.73 | -6.06 | -31.18 | 504 |
| 61 | Opening range 15m | breakout | 85.70 | -14.29 | 194 | 19.1 | -18.63 | -5.12 | -20.67 | 710 |
| 62 | ROC + volume · 1h | momentum | 85.70 | -14.30 | 169 | 20.7 | -8.56 | -0.97 | -25.29 | 394 |
| 63 | ROC + volume | momentum | 72.40 | -27.60 | 444 | 23.0 | -72.57 | -16.26 | -74.54 | 1672 |
| 64 | Squeeze breakout | breakout | 68.66 | -31.34 | 367 | 15.5 | -62.31 | -18.05 | -62.43 | 1219 |
| 65 | Volume breakout | breakout | 68.22 | -31.79 | 289 | 14.5 | -61.46 | -17.37 | -61.46 | 889 |
| 66 | EMA 20/50 cross | trend | 67.39 | -32.61 | 366 | 20.2 | -76.25 | -14.87 | -76.30 | 1434 |
| 67 | RSI(14) reversion | reversion | 67.32 | -32.68 | 454 | 27.1 | -74.18 | -17.38 | -74.50 | 1504 |
| 68 | Donchian 55/20 | breakout | 65.25 | -34.76 | 375 | 17.1 | -68.59 | -14.39 | -69.81 | 1279 |
| 69 | VWAP reversion | reversion | 62.96 | -37.04 | 474 | 25.3 | -72.08 | -15.45 | -72.19 | 1396 |
| 70 | Supertrend | trend | 60.58 | -39.42 | 514 | 19.8 | -85.59 | -20.15 | -85.77 | 1904 |
| 71 | AI bee: Boozy | ai | 60.15 | -39.85 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.84 | -40.16 | 506 | 15.0 | -83.15 | -26.56 | -83.27 | 1857 |
| 73 | Ichimoku | trend | 55.95 | -44.05 | 451 | 9.5 | -82.05 | -22.74 | -82.05 | 1724 |
| 74 | AI bee: Bizzy | ai | 54.21 | -45.79 | 927 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.77 | -46.23 | 645 | 20.0 | -87.84 | -27.74 | -87.91 | 2109 |
| 76 | Z-score reversion | reversion | 52.76 | -47.24 | 606 | 22.9 | -86.16 | -22.28 | -86.25 | 2088 |
| 77 | ADX DI cross | trend | 52.46 | -47.54 | 629 | 10.7 | -89.15 | -33.90 | -89.20 | 2118 |
| 78 | Donchian 20/10 | breakout | 51.61 | -48.39 | 709 | 17.6 | -90.62 | -25.19 | -90.67 | 2645 |
| 79 | MACD zero-line | trend | 50.93 | -49.07 | 653 | 15.0 | -91.19 | -28.64 | -91.22 | 2344 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -29.13 | -98.51 | 5320 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.15 | -29.30 | -93.15 | 2605 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.19 | -24.44 | -90.25 | 2370 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.44 | -26.76 | -91.44 | 2344 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.28 | -31.85 | -97.28 | 3517 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -35.11 | -96.37 | 3583 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -25.30 | -94.31 | 2628 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.30 | -99.36 | 5650 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -31.01 | -96.29 | 3587 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.38 | -99.72 | 6128 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -37.29 | -97.34 | 3666 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -36.31 | -98.54 | 4673 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.25 | -31.89 | -93.29 | 2796 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.19 | -99.54 | 6120 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -32.81 | -96.06 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.93 | -95.72 | 4046 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -45.57 | -99.89 | 8212 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T16:55 | MFI reversion | buy | SQQQ | 10.76 | — | entry signal |
| 2026-10-13T16:55 | MFI reversion | sell | TNA | 2.70 | 0.01 | rebalance down |
| 2026-10-13T16:55 | MFI reversion | sell | SPY | 2.70 | -0.00 | rebalance down |
| 2026-10-13T16:55 | Ichimoku | sell | XRP-USD | 4.65 | -0.03 | exit signal |
| 2026-10-13T16:55 | Ichimoku | sell | ETHU | 4.65 | -0.02 | exit signal |
| 2026-10-13T16:55 | Ichimoku | sell | ETH-USD | 2.88 | -0.02 | exit signal |
| 2026-10-13T16:55 | ADX DI cross | buy | IWM | 5.81 | — | entry |
| 2026-10-13T16:55 | ADX DI cross | sell | BITX | 5.81 | -0.01 | exit signal |
| 2026-10-13T16:50 | VWAP momentum · 1h | buy | SPY | 8.76 | — | entry |
| 2026-10-13T16:50 | VWAP momentum · 1h | sell | ETHU | 8.76 | -0.02 | target is flat |
| 2026-10-13T16:50 | MFI reversion | buy | SPY | 8.03 | — | rebalance up |
| 2026-10-13T16:50 | MFI reversion | sell | PLTR | 13.39 | -0.10 | stop-loss |
| 2026-10-13T16:50 | Donchian 20/10 | buy | UPRO | 4.69 | — | entry |
| 2026-10-13T16:50 | Donchian 20/10 | buy | TNA | 4.69 | — | entry signal |
| 2026-10-13T16:50 | Donchian 20/10 | buy | SPY | 4.69 | — | entry |
| 2026-10-13T16:50 | Donchian 20/10 | buy | IWM | 4.69 | — | entry signal |
| 2026-10-13T16:50 | Donchian 20/10 | sell | TQQQ | 2.66 | -0.00 | rebalance down |
| 2026-10-13T16:50 | Donchian 20/10 | sell | TECL | 2.68 | -0.00 | rebalance down |
| 2026-10-13T16:50 | Donchian 20/10 | sell | SOXL | 2.68 | 0.02 | rebalance down |
| 2026-10-13T16:50 | Donchian 20/10 | sell | QQQ | 2.68 | -0.00 | rebalance down |
| 2026-10-13T16:50 | Donchian 20/10 | sell | NVDA | 2.68 | -0.00 | rebalance down |
| 2026-10-13T16:50 | Donchian 20/10 | sell | COIN | 2.69 | -0.01 | rebalance down |
| 2026-10-13T16:50 | Donchian 20/10 | sell | AMD | 2.71 | 0.03 | rebalance down |
| 2026-10-13T16:50 | ROC + volume | buy | DOGE-USD | 18.11 | — | entry signal |
| 2026-10-13T16:50 | Ichimoku | sell | BITX | 4.67 | -0.00 | exit signal |
| 2026-10-13T16:50 | MACD zero-line | buy | UPRO | 4.38 | — | rebalance up |
| 2026-10-13T16:50 | MACD zero-line | sell | ETHU | 5.09 | -0.02 | exit signal |
| 2026-10-13T16:45 | Agent (ML meta-label) | sell | UPRO | 6.63 | -0.00 | selected signal exited |
| 2026-10-13T16:45 | MFI reversion | buy | SPY | 5.43 | — | entry |
| 2026-10-13T16:45 | MFI reversion | sell | META | 2.71 | 0.00 | rebalance down |
| 2026-10-13T16:45 | MFI reversion | sell | LABU | 2.72 | 0.01 | rebalance down |
| 2026-10-13T16:45 | RSI(14) reversion | sell | TNA | 16.63 | 0.11 | exit signal |
| 2026-10-13T16:45 | Three white soldiers | buy | TNA | 21.59 | — | entry signal |
| 2026-10-13T16:45 | Keltner breakout | buy | SPY | 2.49 | — | entry signal |
| 2026-10-13T16:45 | Ichimoku | buy | SOL-USD | 4.67 | — | entry |
| 2026-10-13T16:45 | Ichimoku | buy | ETHU | 4.67 | — | entry |
| 2026-10-13T16:45 | Ichimoku | buy | DOGE-USD | 4.67 | — | entry signal |
| 2026-10-13T16:45 | Ichimoku | buy | BITX | 4.67 | — | entry signal |
| 2026-10-13T16:45 | Ichimoku | sell | XRP-USD | 2.80 | -0.02 | rebalance down |
| 2026-10-13T16:45 | Ichimoku | sell | TQQQ | 3.34 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 16:55:05.000160+00:00 -> 2026-10-13 17:05:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
