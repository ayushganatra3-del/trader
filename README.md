# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T15:57:05.000181+00:00 · 21487 ticks

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

Today: 19776 decisions in 2298 calls, $0.2539 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T15:57 | 4 / 23 / 3 | SOXL 14%, NVDA 14%, TECL 14%, AMD 14% |  |
| Breezy | 2026-10-13T15:57 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-13T15:57 | 3 / 26 / 1 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.64 | 3.64 | 0 | — | 2.71 | 1.34 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -8.74 | -2.59 | -13.79 | 115 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.94 | 0.94 | 0 | — | 6.12 | 2.29 | -5.18 | 1 |
| 6 | Hold SPY | benchmark | 100.94 | 0.94 | 0 | — | 0.43 | 0.30 | -3.66 | 1 |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.66 | 0.66 | 11 | 36.4 | 4.83 | 1.51 | -7.55 | 43 |
| 8 | Copy: Insider buying | copy | 100.60 | 0.60 | 16 | 50.0 | -16.33 | -2.61 | -21.97 | 75 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.35 | 0.35 | 0 | — | 0.83 | 0.43 | -3.62 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.79 | -0.21 | 7 | 57.1 | -4.28 | -1.42 | -9.74 | 25 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.64 | -0.36 | 0 | — | -2.56 | -1.41 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.51 | -0.49 | 0 | — | 30.94 | 3.58 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.08 | -0.92 | 0 | — | -5.00 | -2.30 | -5.41 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Timing: Nasdaq FTD · TQQQ | daily | 98.25 | -1.75 | 0 | — | -8.92 | -1.61 | -15.27 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Donchian 55/20 · 1h | breakout | 97.91 | -2.09 | 31 | 12.9 | 6.18 | 0.90 | -22.95 | 116 |
| 20 | Trend pullback · 1h | trend | 97.86 | -2.14 | 82 | 25.6 | -23.02 | -6.45 | -25.67 | 173 |
| 21 | Daily: Bullish score | daily | 97.62 | -2.38 | 5 | 0.0 | 0.87 | 0.31 | -12.76 | 12 |
| 22 | ADX DI cross · 1h | trend | 96.91 | -3.09 | 63 | 19.0 | -2.18 | -0.22 | -13.99 | 251 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.69 | -0.40 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | Agent (rotation) | meta | 96.47 | -3.53 | 87 | 31.0 | -11.67 | -4.43 | -13.41 | 273 |
| 26 | Max aggression: 1-day momentum | meta | 96.32 | -3.68 | 12 | 33.3 | -10.41 | -0.22 | -37.31 | 42 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.88 | -4.12 | 0 | — | 7.42 | 1.27 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.69 | -4.31 | 128 | 24.2 | -11.14 | -1.77 | -17.95 | 463 |
| 29 | EMA 20/50 cross · 1h | trend | 95.63 | -4.37 | 45 | 15.6 | 10.69 | 1.35 | -20.12 | 136 |
| 30 | Agent | meta | 95.07 | -4.93 | 61 | 47.5 | -9.88 | -5.06 | -9.88 | 243 |
| 31 | Z-score reversion · 1h | reversion | 94.87 | -5.13 | 50 | 44.0 | 1.59 | 0.45 | -8.60 | 158 |
| 32 | Stochastic reversion · 1h | reversion | 94.78 | -5.22 | 107 | 51.4 | -15.66 | -3.05 | -16.51 | 341 |
| 33 | Supertrend · 1h | trend | 94.30 | -5.70 | 60 | 13.3 | -0.18 | 0.18 | -20.06 | 216 |
| 34 | Parabolic SAR · 1h | trend | 94.25 | -5.75 | 90 | 22.2 | 0.64 | 0.28 | -23.12 | 288 |
| 35 | Squeeze breakout · 1h | breakout | 93.95 | -6.05 | 40 | 22.5 | 5.01 | 1.06 | -9.46 | 103 |
| 36 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 7.62 | 1.95 | -6.93 | 203 |
| 37 | Agent (aggressive) | meta | 92.86 | -7.14 | 31 | 35.5 | -8.07 | -3.58 | -8.07 | 115 |
| 38 | RSI momentum · 1h | momentum | 92.83 | -7.17 | 66 | 15.2 | 3.88 | 0.65 | -22.13 | 226 |
| 39 | MFI reversion · 1h | reversion | 92.36 | -7.64 | 159 | 32.1 | -8.29 | -1.29 | -17.08 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.73 | -8.27 | 123 | 42.3 | -18.70 | -6.16 | -21.32 | 259 |
| 41 | Ichimoku · 1h | trend | 91.43 | -8.57 | 48 | 16.7 | 1.73 | 0.41 | -22.34 | 126 |
| 42 | Agent (ML meta-label) | meta | 91.33 | -8.67 | 460 | 17.2 | -8.97 | -1.52 | -16.46 | 409 |
| 43 | Volume breakout · 1h | breakout | 91.20 | -8.80 | 72 | 22.2 | 8.36 | 1.29 | -12.60 | 120 |
| 44 | Bollinger breakout · 1h | breakout | 91.18 | -8.81 | 75 | 28.0 | 8.24 | 1.20 | -14.21 | 279 |
| 45 | RSI(14) reversion · 1h | reversion | 91.05 | -8.95 | 37 | 32.4 | -2.56 | -0.43 | -9.40 | 149 |
| 46 | Triple EMA stack · 1h | trend | 90.87 | -9.13 | 71 | 15.5 | -7.90 | -0.63 | -32.72 | 240 |
| 47 | Bollinger reversion · 1h | reversion | 89.30 | -10.70 | 96 | 36.5 | -26.07 | -6.30 | -26.55 | 319 |
| 48 | CCI reversion · 1h | reversion | 88.65 | -11.35 | 117 | 45.3 | -10.24 | -1.36 | -14.42 | 410 |
| 49 | OBV trend · 1h | momentum | 88.55 | -11.45 | 153 | 18.3 | -7.01 | -0.60 | -27.65 | 323 |
| 50 | Opening range 30m | breakout | 88.01 | -11.99 | 160 | 21.2 | -16.25 | -4.85 | -17.46 | 575 |
| 51 | MACD zero-line · 1h | trend | 87.91 | -12.09 | 68 | 17.6 | -19.42 | -3.59 | -21.55 | 231 |
| 52 | VWAP momentum · 1h | momentum | 87.83 | -12.17 | 318 | 23.6 | -32.60 | -4.82 | -40.47 | 1242 |
| 53 | Williams %R · 1h | reversion | 87.77 | -12.23 | 143 | 45.5 | -27.44 | -4.61 | -29.48 | 507 |
| 54 | Max aggression: 5-day momentum | meta | 87.64 | -12.36 | 8 | 37.5 | -10.48 | -0.67 | -34.64 | 28 |
| 55 | Donchian 20/10 · 1h | breakout | 87.49 | -12.51 | 64 | 17.2 | -0.37 | 0.16 | -19.51 | 218 |
| 56 | Keltner breakout · 1h | breakout | 87.23 | -12.77 | 46 | 19.6 | -7.13 | -0.71 | -26.75 | 217 |
| 57 | Heikin-Ashi · 1h | trend | 86.99 | -13.01 | 159 | 27.7 | -30.82 | -5.11 | -38.29 | 681 |
| 58 | EMA 9/21 cross · 1h | trend | 86.90 | -13.10 | 110 | 12.7 | -11.70 | -1.49 | -24.14 | 330 |
| 59 | Three white soldiers | momentum | 86.38 | -13.62 | 157 | 17.8 | -47.94 | -22.83 | -48.13 | 587 |
| 60 | Candlestick reversal · 1h | reversion | 86.24 | -13.76 | 135 | 29.6 | -31.20 | -6.18 | -31.56 | 497 |
| 61 | ROC + volume · 1h | momentum | 85.87 | -14.13 | 169 | 20.7 | -8.29 | -0.93 | -25.21 | 394 |
| 62 | Opening range 15m | breakout | 85.49 | -14.51 | 194 | 19.1 | -18.93 | -5.19 | -20.67 | 705 |
| 63 | ROC + volume | momentum | 72.56 | -27.45 | 441 | 23.1 | -72.76 | -16.29 | -74.74 | 1675 |
| 64 | Squeeze breakout | breakout | 68.45 | -31.55 | 366 | 15.3 | -62.57 | -18.21 | -62.57 | 1225 |
| 65 | Volume breakout | breakout | 68.22 | -31.79 | 289 | 14.5 | -61.62 | -17.49 | -61.62 | 892 |
| 66 | EMA 20/50 cross | trend | 67.22 | -32.78 | 365 | 20.3 | -76.10 | -14.86 | -76.20 | 1433 |
| 67 | RSI(14) reversion | reversion | 66.97 | -33.03 | 451 | 26.6 | -74.35 | -17.44 | -74.52 | 1500 |
| 68 | Donchian 55/20 | breakout | 65.17 | -34.83 | 374 | 17.1 | -68.75 | -14.46 | -69.81 | 1290 |
| 69 | VWAP reversion | reversion | 62.84 | -37.16 | 471 | 25.3 | -72.29 | -15.55 | -72.33 | 1395 |
| 70 | Supertrend | trend | 60.25 | -39.75 | 513 | 19.9 | -85.76 | -20.40 | -85.85 | 1902 |
| 71 | AI bee: Boozy | ai | 60.01 | -39.99 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.66 | -40.34 | 505 | 15.0 | -83.27 | -26.92 | -83.27 | 1854 |
| 73 | Ichimoku | trend | 56.22 | -43.78 | 443 | 9.7 | -82.21 | -22.79 | -82.21 | 1729 |
| 74 | MFI reversion | reversion | 53.68 | -46.32 | 638 | 19.7 | -87.93 | -27.77 | -87.95 | 2106 |
| 75 | AI bee: Bizzy | ai | 53.67 | -46.33 | 923 | 8.2 | — | — | — | — |
| 76 | Z-score reversion | reversion | 52.49 | -47.51 | 600 | 22.2 | -86.30 | -22.30 | -86.33 | 2090 |
| 77 | ADX DI cross | trend | 52.27 | -47.73 | 627 | 10.5 | -89.26 | -34.32 | -89.26 | 2126 |
| 78 | Donchian 20/10 | breakout | 51.46 | -48.54 | 707 | 17.7 | -90.72 | -25.42 | -90.72 | 2641 |
| 79 | MACD zero-line | trend | 50.89 | -49.11 | 651 | 15.1 | -91.23 | -28.79 | -91.25 | 2339 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.49 | -29.25 | -98.51 | 5312 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.09 | -29.16 | -93.09 | 2599 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.26 | -24.57 | -90.31 | 2365 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.40 | -26.64 | -91.40 | 2335 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.27 | -31.80 | -97.27 | 3501 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -34.54 | -96.29 | 3566 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -25.22 | -94.34 | 2622 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.38 | -99.36 | 5653 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -31.26 | -96.32 | 3590 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.56 | -99.72 | 6119 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.33 | -37.41 | -97.33 | 3658 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -36.39 | -98.54 | 4670 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.32 | -32.25 | -93.32 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.35 | -99.54 | 6129 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.07 | -32.89 | -96.07 | 3748 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -34.04 | -95.74 | 4053 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.93 | -99.89 | 8208 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T15:56 | AI bee: Bizzy | buy | TECL | 7.64 | — | Jev: buy (buy p=0.57) |
| 2026-10-13T15:55 | AI bee: Bizzy | buy | SOXL | 7.72 | — | Jev: buy (buy p=0.58) |
| 2026-10-13T15:55 | Agent (ML meta-label) | buy | UPRO | 7.61 | — | entry |
| 2026-10-13T15:55 | Agent (ML meta-label) | buy | IWM | 7.61 | — | following RSI momentum |
| 2026-10-13T15:55 | Agent (ML meta-label) | sell | TECL | 6.47 | -0.16 | selected signal exited |
| 2026-10-13T15:55 | MFI reversion · 1h | buy | TSLA | 23.09 | — | entry |
| 2026-10-13T15:55 | VWAP reversion | buy | IWM | 6.42 | — | entry signal |
| 2026-10-13T15:55 | VWAP reversion | sell | UPRO | 3.15 | 0.00 | rebalance down |
| 2026-10-13T15:55 | VWAP reversion | sell | SPY | 3.15 | -0.00 | rebalance down |
| 2026-10-13T15:55 | RSI(14) reversion | buy | TNA | 16.53 | — | entry signal |
| 2026-10-13T15:55 | RSI(14) reversion | buy | LABU | 3.37 | — | rebalance up |
| 2026-10-13T15:55 | RSI(14) reversion | buy | IWM | 16.75 | — | entry signal |
| 2026-10-13T15:55 | RSI(14) reversion | sell | NVDA | 16.75 | 0.04 | exit signal |
| 2026-10-13T15:55 | Opening range 30m | buy | NVDA | 22.00 | — | entry signal |
| 2026-10-13T15:55 | Opening range 15m | buy | NVDA | 4.36 | — | entry signal |
| 2026-10-13T15:55 | Opening range 15m | sell | AMD | 4.36 | 0.01 | rebalance down |
| 2026-10-13T15:55 | ADX DI cross | buy | NVDA | 13.07 | — | entry signal |
| 2026-10-13T15:50 | Agent (ML meta-label) | sell | UPRO | 7.60 | -0.01 | selected signal exited |
| 2026-10-13T15:50 | MFI reversion | buy | TNA | 2.68 | — | rebalance up |
| 2026-10-13T15:50 | MFI reversion | buy | NVDA | 5.28 | — | rebalance up |
| 2026-10-13T15:50 | MFI reversion | buy | ETHU | 2.68 | — | rebalance up |
| 2026-10-13T15:50 | MFI reversion | sell | IWM | 10.72 | -0.04 | stop-loss |
| 2026-10-13T15:50 | Z-score reversion | buy | TECL | 2.53 | — | entry signal |
| 2026-10-13T15:50 | Z-score reversion | buy | SPY | 7.49 | — | entry signal |
| 2026-10-13T15:50 | Z-score reversion | sell | NVDA | 3.03 | 0.00 | rebalance down |
| 2026-10-13T15:49 | AI bee: Bizzy | buy | NVDA | 7.71 | — | Jev: buy (buy p=0.58) |
| 2026-10-13T15:45 | Agent (ML meta-label) | buy | UPRO | 7.61 | — | entry |
| 2026-10-13T15:45 | Connors RSI(2) · 1h | sell | SPY | 15.26 | -0.01 | target is flat |
| 2026-10-13T15:45 | VWAP momentum · 1h | buy | SQQQ | 6.50 | — | rebalance up |
| 2026-10-13T15:45 | VWAP momentum · 1h | sell | ETHU | 8.78 | -0.06 | target is flat |
| 2026-10-13T15:45 | VWAP reversion | buy | SPY | 15.73 | — | entry signal |
| 2026-10-13T15:45 | RSI(14) reversion | buy | NVDA | 3.36 | — | rebalance up |
| 2026-10-13T15:45 | ADX DI cross | sell | TSLA | 13.15 | -0.02 | exit signal |
| 2026-10-13T15:45 | MACD zero-line | sell | COIN | 12.79 | 0.02 | exit signal |
| 2026-10-13T15:44 | AI bee: Bizzy | buy | AMD | 7.71 | — | Jev: buy (buy p=0.57) |
| 2026-10-13T15:44 | AI bee: Bizzy | sell | BRK-B | 7.62 | -0.02 | Jev: sell (sell p=0.59) after 11 min |
| 2026-10-13T15:40 | Day trade: Stocks in Play ORB | sell | TECL | 24.08 | -0.68 | target is flat |
| 2026-10-13T15:40 | Agent (ML meta-label) | sell | UPRO | 7.62 | -0.01 | selected signal exited |
| 2026-10-13T15:40 | Agent (ML meta-label) | sell | IWM | 6.38 | -0.01 | selected signal exited |
| 2026-10-13T15:40 | MFI reversion | buy | NVDA | 8.09 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 15:57:05.000181+00:00 -> 2026-10-13 16:07:05.000181+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
