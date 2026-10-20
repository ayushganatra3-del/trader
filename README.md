# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T20:25:05.000122+00:00 · 29904 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.86 (-9.14%)

Closed trades 90, win rate 41.1%, fees £2.98, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 17.46 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 39819 decisions in 3012 calls, $0.4884 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T20:25 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-20T20:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T20:25 | 5 / 0 / 0 | ETH-USD 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | BITX | 1.90 | +3.32% | 6 |
| VWAP reversion | ETHU | 1.90 | +4.27% | 5 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.97 | 5.97 | 0 | — | 8.17 | 3.83 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.66 | -2.08 | -13.79 | 134 |
| 6 | Max aggression: 5-day momentum | meta | 100.73 | 0.73 | 9 | 44.4 | -13.23 | -0.92 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.95 | -1.05 | 0 | — | 0.33 | 0.23 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 62 | 35.5 | 4.26 | 2.23 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.44 | -1.56 | 0 | — | -0.73 | -0.22 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.03 | -1.97 | 3 | 33.3 | 4.27 | 0.99 | -7.93 | 8 |
| 14 | Hold BTC | benchmark | 97.57 | -2.43 | 0 | — | 18.15 | 2.45 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.83 | -2.16 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.99 | -3.01 | 0 | — | -4.14 | -1.58 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.80 | -3.20 | 0 | — | 0.05 | 0.08 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.20 | -3.79 | 40 | 15.0 | -17.99 | -3.51 | -21.25 | 102 |
| 19 | Agent (rotation) | meta | 96.07 | -3.93 | 114 | 31.6 | -5.79 | -2.89 | -7.60 | 299 |
| 20 | Copy: Insider buying | copy | 96.06 | -3.94 | 25 | 40.0 | -12.02 | -2.07 | -20.62 | 72 |
| 21 | Trend pullback · 1h | trend | 95.69 | -4.31 | 90 | 23.3 | -20.92 | -6.26 | -21.38 | 133 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.56 | -5.43 | 89 | 18.0 | -13.82 | -2.61 | -16.12 | 253 |
| 24 | Daily: Momentum burst | daily | 94.09 | -5.92 | 6 | 16.7 | -6.95 | -0.93 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.71 | 1.50 | -6.51 | 196 |
| 26 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -13.39 | -3.90 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.69 | -8.31 | 105 | 21.9 | -18.31 | -3.95 | -21.51 | 273 |
| 28 | Squeeze breakout · 1h | breakout | 91.61 | -8.39 | 46 | 21.7 | -4.46 | -1.01 | -11.48 | 100 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.25 | -2.32 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.10 | -8.90 | 7 | 0.0 | -7.95 | -0.90 | -13.10 | 13 |
| 31 | Agent | meta | 90.86 | -9.14 | 90 | 41.1 | -10.43 | -5.53 | -14.19 | 239 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.76 | -9.23 | 0 | — | 0.92 | 0.30 | -14.37 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.58 | -9.42 | 84 | 22.6 | -12.71 | -2.27 | -14.57 | 106 |
| 34 | Bollinger breakout · 1h | breakout | 90.51 | -9.49 | 87 | 29.9 | -13.34 | -2.52 | -16.36 | 258 |
| 35 | Connors RSI(2) · 1h | reversion | 89.41 | -10.59 | 151 | 41.7 | -22.55 | -6.73 | -23.97 | 200 |
| 36 | RSI momentum · 1h | momentum | 89.21 | -10.79 | 83 | 15.7 | -24.51 | -4.77 | -25.37 | 217 |
| 37 | EMA 20/50 cross · 1h | trend | 88.51 | -11.49 | 62 | 12.9 | -19.24 | -3.54 | -21.39 | 132 |
| 38 | Opening range 15m | breakout | 88.26 | -11.74 | 270 | 29.3 | -17.72 | -4.78 | -20.79 | 699 |
| 39 | Supertrend · 1h | trend | 88.10 | -11.90 | 88 | 12.5 | -21.47 | -4.20 | -26.62 | 222 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -9.14 | -2.55 | -12.51 | 127 |
| 41 | Stochastic reversion · 1h | reversion | 87.75 | -12.25 | 164 | 47.0 | -14.69 | -2.45 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.25 | -12.75 | 60 | 21.7 | -19.19 | -3.48 | -26.64 | 206 |
| 43 | Ichimoku · 1h | trend | 86.80 | -13.20 | 60 | 13.3 | -19.10 | -3.60 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.22 | -13.78 | 193 | 20.2 | -26.36 | -5.01 | -33.71 | 468 |
| 45 | Triple EMA stack · 1h | trend | 85.21 | -14.79 | 91 | 14.3 | -32.81 | -5.93 | -35.36 | 229 |
| 46 | Donchian 20/10 · 1h | breakout | 84.56 | -15.44 | 81 | 17.3 | -20.02 | -3.26 | -28.55 | 222 |
| 47 | Z-score reversion · 1h | reversion | 84.49 | -15.51 | 96 | 30.2 | -14.29 | -2.35 | -21.32 | 195 |
| 48 | MFI reversion · 1h | reversion | 83.77 | -16.23 | 220 | 30.5 | -14.80 | -2.32 | -20.43 | 146 |
| 49 | OBV trend · 1h | momentum | 83.73 | -16.27 | 186 | 17.2 | -32.52 | -6.01 | -36.90 | 314 |
| 50 | Agent (ML meta-label) | meta | 83.64 | -16.36 | 711 | 19.1 | -1.64 | -0.13 | -15.64 | 388 |
| 51 | MACD zero-line · 1h | trend | 83.57 | -16.43 | 89 | 14.6 | -25.48 | -5.02 | -26.48 | 226 |
| 52 | Three white soldiers | momentum | 82.58 | -17.42 | 250 | 19.6 | -46.86 | -18.13 | -47.63 | 614 |
| 53 | Bollinger reversion · 1h | reversion | 82.22 | -17.78 | 162 | 35.8 | -29.42 | -5.70 | -32.84 | 347 |
| 54 | Williams %R · 1h | reversion | 81.37 | -18.63 | 195 | 43.6 | -30.70 | -4.75 | -36.49 | 524 |
| 55 | ROC + volume · 1h | momentum | 81.32 | -18.68 | 203 | 21.2 | -29.73 | -5.40 | -34.58 | 397 |
| 56 | CCI reversion · 1h | reversion | 80.74 | -19.26 | 178 | 41.6 | -18.24 | -2.28 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.16 | -19.84 | 232 | 20.7 | -44.03 | -9.36 | -47.30 | 671 |
| 58 | RSI(14) reversion · 1h | reversion | 79.56 | -20.44 | 83 | 22.9 | -15.38 | -2.71 | -23.28 | 184 |
| 59 | EMA 9/21 cross · 1h | trend | 79.53 | -20.47 | 143 | 10.5 | -29.35 | -6.12 | -30.12 | 326 |
| 60 | VWAP momentum · 1h | momentum | 77.60 | -22.40 | 463 | 19.9 | -45.28 | -8.14 | -50.53 | 1256 |
| 61 | Candlestick reversal · 1h | reversion | 77.37 | -22.63 | 226 | 28.8 | -36.53 | -6.69 | -38.83 | 540 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -27.91 | -1.54 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.60 | -38.40 | 628 | 23.1 | -77.87 | -21.80 | -78.44 | 1714 |
| 64 | Volume breakout | breakout | 61.59 | -38.41 | 377 | 14.1 | -63.33 | -19.13 | -64.07 | 871 |
| 65 | Squeeze breakout | breakout | 58.56 | -41.44 | 490 | 14.1 | -66.03 | -22.13 | -66.59 | 1203 |
| 66 | Donchian 55/20 | breakout | 57.80 | -42.20 | 503 | 19.3 | -70.51 | -17.46 | -73.50 | 1276 |
| 67 | RSI(14) reversion | reversion | 57.37 | -42.63 | 744 | 26.5 | -74.13 | -16.20 | -74.89 | 1623 |
| 68 | EMA 20/50 cross | trend | 55.65 | -44.35 | 551 | 19.4 | -76.88 | -15.63 | -80.87 | 1444 |
| 69 | VWAP reversion | reversion | 53.63 | -46.37 | 754 | 25.2 | -71.42 | -14.48 | -72.28 | 1500 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.78 | -31.04 | -98.78 | 5300 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -31.58 | -93.91 | 2599 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.65 | -20.37 | -88.38 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.29 | -24.59 | -91.32 | 2352 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.98 | -25.60 | -91.19 | 2249 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.55 | -33.03 | -97.65 | 3522 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.69 | -37.00 | -96.71 | 3564 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -28.11 | -94.46 | 2517 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.60 | -27.34 | -82.67 | 1706 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.88 | -99.38 | 5744 |
| 80 | Keltner breakout | breakout | 50.28 | -49.72 | 703 | 16.8 | -83.24 | -27.53 | -83.82 | 1802 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.69 | -27.25 | -92.26 | 2620 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.94 | -31.53 | -95.95 | 3460 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -40.95 | -99.75 | 6192 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.58 | -29.04 | -91.63 | 2353 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -38.26 | -97.66 | 3610 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.08 | -98.47 | 4709 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.06 | -34.73 | -94.07 | 2798 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.56 | -99.52 | 6188 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.61 | -22.00 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.80 | -26.23 | -87.99 | 2136 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -32.40 | -95.97 | 3767 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -32.78 | -89.37 | 2115 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -32.78 | -95.78 | 4109 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.35 | -99.91 | 8287 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T20:20 | Three white soldiers | sell | XRP-USD | 20.58 | -0.09 | exit signal |
| 2026-10-20T19:55 | Day trade: Stocks in Play ORB | sell | LABU | 24.57 | -0.15 | target is flat |
| 2026-10-20T19:55 | Day trade: Stocks in Play ORB | sell | IWM | 24.80 | 0.24 | target is flat |
| 2026-10-20T19:55 | Agent | sell | TSLA | 36.52 | 0.24 | selected signal exited |
| 2026-10-20T19:55 | MFI reversion · 1h | buy | IWM | 5.57 | — | entry |
| 2026-10-20T19:55 | VWAP reversion | sell | AAPL | 13.40 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | META | 14.43 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | COIN | 14.36 | 0.02 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | AAPL | 14.31 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Squeeze breakout | sell | SQQQ | 14.63 | -0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | UPRO | 4.90 | -0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TSLA | 5.14 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TQQQ | 5.09 | 0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TNA | 5.20 | 0.06 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TECL | 5.09 | 0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | SPY | 5.12 | -0.02 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | SOXL | 5.12 | 0.10 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | QQQ | 5.12 | -0.00 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | PLTR | 5.08 | -0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | NVDA | 5.11 | -0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | MSTR | 5.14 | 0.13 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | LABU | 5.28 | 0.14 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | IWM | 5.15 | 0.02 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | ETHU | 5.63 | 0.06 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | COIN | 4.66 | -0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | BITX | 5.07 | 0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | AMD | 5.10 | 0.02 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | UPRO | 6.23 | 0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TSLA | 6.25 | 0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TQQQ | 6.25 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TNA | 6.31 | 0.16 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | TECL | 6.29 | 0.07 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | SPY | 6.22 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | SOXL | 6.39 | 0.17 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | QQQ | 6.22 | 0.00 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | MSTR | 6.44 | 0.27 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | LABU | 6.52 | 0.42 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | IWM | 6.25 | 0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | ETHU | 6.36 | 0.16 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 15m | sell | COIN | 6.24 | 0.04 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 20:25:05.000122+00:00 -> 2026-10-20 20:35:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
