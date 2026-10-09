# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T06:00:05.000113+00:00 · 16427 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.70 (-4.30%)

Closed trades 50, win rate 54.0%, fees £2.06, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 19.13 | -0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BORR 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 4275 decisions in 855 calls, $0.0598 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T06:00 | 0 / 2 / 3 | SOXL 15%, AMD 15% |  |
| Breezy | 2026-10-09T06:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T06:00 | 1 / 4 / 0 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 102.99 | 2.99 | 36 | 41.7 | -8.00 | -2.43 | -13.79 | 119 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.33 | 1.33 | 0 | — | -4.29 | -1.79 | -7.31 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 101.18 | 1.18 | 0 | — | -6.17 | -1.07 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.63 | 0.63 | 0 | — | -0.11 | -0.02 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.59 | 0.59 | 0 | — | 1.17 | 0.59 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.58 | 0.58 | 0 | — | -1.64 | -0.89 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -3.83 | -1.25 | -9.74 | 25 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.69 | -0.31 | 0 | — | 0.61 | 0.31 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.97 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.41 | -1.47 | -3.04 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.18 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.68 | -1.32 | 0 | — | -5.06 | -2.42 | -5.36 | 1 |
| 17 | Copy: Insider buying | copy | 98.39 | -1.61 | 12 | 50.0 | -15.88 | -2.79 | -21.08 | 71 |
| 18 | Hold BTC | benchmark | 98.34 | -1.66 | 0 | — | 26.28 | 3.15 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 98.18 | -1.82 | 81 | 53.1 | -12.64 | -2.53 | -15.21 | 345 |
| 20 | Donchian 55/20 · 1h | breakout | 98.04 | -1.96 | 26 | 15.4 | 10.01 | 1.34 | -16.96 | 109 |
| 21 | Three white soldiers · 1h | momentum | 97.53 | -2.47 | 6 | 0.0 | -3.03 | -2.34 | -4.15 | 26 |
| 22 | Agent (rotation) | meta | 96.55 | -3.45 | 78 | 28.2 | 0.48 | 0.23 | -7.43 | 261 |
| 23 | ADX DI cross · 1h | trend | 96.53 | -3.47 | 54 | 22.2 | -4.41 | -0.62 | -13.84 | 248 |
| 24 | Trend pullback · 1h | trend | 96.53 | -3.47 | 78 | 23.1 | -23.34 | -6.56 | -25.53 | 168 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.29 | -3.71 | 0 | — | 8.88 | 1.50 | -8.33 | 1 |
| 26 | EMA 20/50 cross · 1h | trend | 96.13 | -3.87 | 36 | 11.1 | 0.51 | 0.28 | -20.52 | 135 |
| 27 | Z-score reversion · 1h | reversion | 96.04 | -3.96 | 36 | 38.9 | -0.49 | 0.02 | -8.60 | 168 |
| 28 | Daily: Momentum burst | daily | 95.98 | -4.02 | 4 | 0.0 | -4.75 | -0.57 | -17.67 | 40 |
| 29 | Daily: Bullish score | daily | 95.71 | -4.29 | 3 | 0.0 | -1.35 | 0.02 | -12.76 | 10 |
| 30 | Agent | meta | 95.70 | -4.30 | 50 | 54.0 | -9.27 | -5.20 | -9.83 | 247 |
| 31 | MACD cross · 1h | trend | 95.13 | -4.87 | 105 | 22.9 | -17.59 | -2.79 | -18.84 | 460 |
| 32 | Parabolic SAR · 1h | trend | 95.10 | -4.90 | 82 | 22.0 | -5.24 | -0.55 | -20.80 | 291 |
| 33 | Squeeze breakout · 1h | breakout | 94.87 | -5.13 | 34 | 26.5 | 15.40 | 2.52 | -8.14 | 102 |
| 34 | Supertrend · 1h | trend | 94.34 | -5.66 | 51 | 13.7 | -4.54 | -0.46 | -18.09 | 210 |
| 35 | Agent (aggressive) | meta | 94.25 | -5.75 | 22 | 45.5 | -6.32 | -2.99 | -6.68 | 109 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.31 | 1.87 | -6.52 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.37 | -6.63 | 102 | 41.2 | -18.29 | -6.02 | -20.97 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.08 | 0.21 | -19.98 | 119 |
| 39 | Bollinger breakout · 1h | breakout | 92.53 | -7.47 | 65 | 30.8 | 6.44 | 0.98 | -12.06 | 285 |
| 40 | Agent (ML meta-label) | meta | 92.47 | -7.53 | 354 | 18.6 | -6.04 | -1.01 | -13.25 | 399 |
| 41 | RSI momentum · 1h | momentum | 92.35 | -7.65 | 60 | 15.0 | 1.31 | 0.36 | -16.65 | 218 |
| 42 | RSI(14) reversion · 1h | reversion | 92.25 | -7.75 | 26 | 26.9 | -4.01 | -0.76 | -9.03 | 154 |
| 43 | Volume breakout · 1h | breakout | 92.11 | -7.89 | 45 | 17.8 | 6.47 | 1.04 | -12.60 | 121 |
| 44 | Bollinger reversion · 1h | reversion | 91.53 | -8.47 | 68 | 33.8 | -22.05 | -5.33 | -23.94 | 319 |
| 45 | Max aggression: 1-day momentum | meta | 91.24 | -8.76 | 9 | 33.3 | -23.96 | -1.22 | -37.31 | 43 |
| 46 | Triple EMA stack · 1h | trend | 91.19 | -8.81 | 68 | 16.2 | -10.64 | -1.16 | -25.80 | 235 |
| 47 | MFI reversion · 1h | reversion | 91.00 | -9.00 | 96 | 28.1 | -14.88 | -2.53 | -16.99 | 128 |
| 48 | Opening range 30m | breakout | 90.76 | -9.23 | 131 | 20.6 | -17.37 | -5.24 | -17.94 | 562 |
| 49 | Candlestick reversal · 1h | reversion | 90.40 | -9.60 | 100 | 30.0 | -30.41 | -5.99 | -31.59 | 505 |
| 50 | MACD zero-line · 1h | trend | 90.32 | -9.68 | 58 | 20.7 | -6.37 | -0.68 | -19.00 | 240 |
| 51 | Williams %R · 1h | reversion | 90.15 | -9.85 | 107 | 44.9 | -26.80 | -4.70 | -27.36 | 515 |
| 52 | Three white soldiers | momentum | 89.14 | -10.86 | 122 | 18.9 | -48.41 | -23.33 | -48.41 | 586 |
| 53 | Opening range 15m | breakout | 88.59 | -11.41 | 153 | 19.0 | -19.52 | -5.58 | -20.06 | 683 |
| 54 | EMA 9/21 cross · 1h | trend | 88.49 | -11.51 | 99 | 14.1 | -10.80 | -1.26 | -20.61 | 333 |
| 55 | Donchian 20/10 · 1h | breakout | 88.29 | -11.71 | 55 | 20.0 | -1.95 | -0.03 | -17.36 | 219 |
| 56 | OBV trend · 1h | momentum | 88.25 | -11.75 | 139 | 18.0 | -15.38 | -1.75 | -30.34 | 318 |
| 57 | VWAP momentum · 1h | momentum | 88.19 | -11.81 | 262 | 21.4 | -36.59 | -5.54 | -39.17 | 1264 |
| 58 | Keltner breakout · 1h | breakout | 87.64 | -12.37 | 41 | 19.5 | -11.23 | -1.30 | -24.35 | 225 |
| 59 | CCI reversion · 1h | reversion | 87.63 | -12.37 | 91 | 40.7 | -10.92 | -1.48 | -14.35 | 418 |
| 60 | Heikin-Ashi · 1h | trend | 87.54 | -12.46 | 133 | 25.6 | -32.44 | -5.50 | -36.32 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 128 | 21.1 | -10.70 | -1.30 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 83.55 | -16.45 | 7 | 28.6 | -27.10 | -2.40 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.28 | -23.72 | 354 | 21.5 | -72.76 | -16.41 | -73.75 | 1645 |
| 64 | RSI(14) reversion | reversion | 75.62 | -24.38 | 339 | 28.0 | -73.55 | -18.46 | -73.75 | 1504 |
| 65 | Squeeze breakout | breakout | 74.33 | -25.66 | 279 | 15.1 | -62.07 | -18.15 | -62.07 | 1206 |
| 66 | EMA 20/50 cross | trend | 72.35 | -27.65 | 288 | 18.4 | -77.32 | -15.28 | -77.50 | 1449 |
| 67 | Donchian 55/20 | breakout | 72.09 | -27.91 | 283 | 17.0 | -68.37 | -14.57 | -68.55 | 1280 |
| 68 | Volume breakout | breakout | 71.89 | -28.11 | 230 | 13.0 | -63.79 | -18.32 | -63.79 | 900 |
| 69 | VWAP reversion | reversion | 68.60 | -31.40 | 379 | 25.3 | -72.10 | -16.10 | -72.39 | 1439 |
| 70 | Supertrend | trend | 67.39 | -32.61 | 415 | 20.2 | -86.68 | -21.10 | -86.92 | 1929 |
| 71 | Keltner breakout | breakout | 65.23 | -34.77 | 392 | 13.8 | -84.68 | -28.17 | -84.68 | 1853 |
| 72 | Ichimoku | trend | 63.09 | -36.91 | 359 | 9.2 | -81.78 | -23.27 | -81.78 | 1735 |
| 73 | AI bee: Bizzy | ai | 63.00 | -37.00 | 711 | 9.0 | — | — | — | — |
| 74 | MFI reversion | reversion | 62.36 | -37.64 | 447 | 20.8 | -87.98 | -28.39 | -88.00 | 2125 |
| 75 | Z-score reversion | reversion | 62.15 | -37.85 | 462 | 23.6 | -86.04 | -23.46 | -86.12 | 2095 |
| 76 | ADX DI cross | trend | 60.86 | -39.14 | 492 | 10.6 | -89.60 | -34.13 | -89.65 | 2136 |
| 77 | MACD zero-line | trend | 59.92 | -40.08 | 519 | 16.0 | -91.31 | -28.92 | -91.32 | 2347 |
| 78 | Donchian 20/10 | breakout | 59.76 | -40.24 | 553 | 18.4 | -90.98 | -25.99 | -90.98 | 2643 |
| 79 | AI bee: Boozy | ai | 59.75 | -40.25 | 242 | 5.4 | — | — | — | — |
| 80 | Trend pullback | trend | 59.61 | -40.39 | 507 | 15.8 | -90.49 | -26.59 | -90.53 | 2283 |
| 81 | RSI momentum | momentum | 58.69 | -41.31 | 518 | 17.8 | -90.30 | -25.26 | -90.33 | 2348 |
| 82 | Triple EMA stack | trend | 57.99 | -42.01 | 546 | 15.6 | -93.12 | -29.91 | -93.12 | 2591 |
| 83 | Bollinger breakout | breakout | 55.44 | -44.56 | 582 | 14.8 | -93.68 | -32.97 | -93.68 | 2805 |
| 84 | Consensus | meta | 53.67 | -46.33 | 553 | 9.9 | -94.30 | -25.57 | -94.30 | 2660 |
| 85 | EMA 9/21 cross | trend | 52.29 | -47.71 | 701 | 16.4 | -97.31 | -32.32 | -97.31 | 3523 |
| 86 | Connors RSI(2) | reversion | 52.06 | -47.94 | 726 | 20.9 | -96.10 | -30.95 | -96.10 | 3544 |
| 87 | Stochastic reversion | reversion | 50.96 | -49.04 | 865 | 23.0 | -95.68 | -33.64 | -95.71 | 4068 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -30.28 | -98.72 | 5343 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -35.71 | -96.29 | 3554 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -35.78 | -99.35 | 5669 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.22 | -99.73 | 6131 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.93 | -97.35 | 3634 |
| 93 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.35 | -98.50 | 4701 |
| 94 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.19 | -99.52 | 6118 |
| 95 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -33.07 | -95.91 | 3730 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.80 | -99.90 | 8239 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T06:00 | Consensus | sell | DOGE-USD | 13.47 | -0.06 | target is flat |
| 2026-10-09T06:00 | Stochastic reversion · 1h | sell | SOL-USD | 8.26 | 0.23 | exit signal |
| 2026-10-09T06:00 | Stochastic reversion · 1h | sell | ETH-USD | 8.20 | 0.17 | exit signal |
| 2026-10-09T06:00 | Stochastic reversion · 1h | sell | DOGE-USD | 8.33 | 0.30 | exit signal |
| 2026-10-09T06:00 | Connors RSI(2) | buy | DOGE-USD | 13.03 | — | entry signal |
| 2026-10-09T06:00 | Keltner breakout | sell | DOGE-USD | 16.26 | -0.12 | stop-loss |
| 2026-10-09T06:00 | Bollinger breakout | sell | DOGE-USD | 13.82 | -0.10 | stop-loss |
| 2026-10-09T06:00 | ROC + volume | sell | DOGE-USD | 18.95 | -0.17 | stop-loss |
| 2026-10-09T05:55 | AI bee: Bizzy | sell | DOGE-USD | 8.68 | -0.08 | Jev: sell (sell p=0.90) after 10 min |
| 2026-10-09T05:55 | Agent (ML meta-label) | buy | XRP-USD | 5.78 | — | entry |
| 2026-10-09T05:55 | Consensus | sell | XRP-USD | 13.38 | -0.13 | target is flat |
| 2026-10-09T05:55 | Connors RSI(2) | buy | XRP-USD | 13.03 | — | entry signal |
| 2026-10-09T05:55 | Keltner breakout | sell | XRP-USD | 16.21 | -0.16 | stop-loss |
| 2026-10-09T05:55 | Bollinger breakout | sell | XRP-USD | 13.78 | -0.13 | stop-loss |
| 2026-10-09T05:55 | Ichimoku | sell | XRP-USD | 15.75 | -0.14 | exit signal |
| 2026-10-09T05:55 | ADX DI cross | sell | SOL-USD | 15.15 | -0.09 | exit signal |
| 2026-10-09T05:50 | Connors RSI(2) | buy | SOL-USD | 13.06 | — | entry signal |
| 2026-10-09T05:50 | Connors RSI(2) | buy | BTC-USD | 13.06 | — | entry signal |
| 2026-10-09T05:50 | Volume breakout | sell | XRP-USD | 17.85 | -0.16 | exit signal |
| 2026-10-09T05:50 | Ichimoku | sell | ETH-USD | 15.76 | -0.13 | exit signal |
| 2026-10-09T05:45 | AI bee: Bizzy | buy | DOGE-USD | 8.76 | — | Jev: buy (buy p=0.56) |
| 2026-10-09T05:45 | Consensus | sell | SOL-USD | 13.41 | -0.08 | target is flat |
| 2026-10-09T05:45 | Consensus | sell | ETH-USD | 13.42 | -0.08 | target is flat |
| 2026-10-09T05:45 | ROC + volume | buy | DOGE-USD | 19.11 | — | entry signal |
| 2026-10-09T05:40 | Consensus | buy | SOL-USD | 13.49 | — | entry |
| 2026-10-09T05:40 | Consensus | buy | ETH-USD | 13.50 | — | entry |
| 2026-10-09T05:40 | Ichimoku | buy | XRP-USD | 15.88 | — | entry signal |
| 2026-10-09T05:40 | Ichimoku | buy | SOL-USD | 15.88 | — | entry signal |
| 2026-10-09T05:40 | Ichimoku | buy | ETH-USD | 15.88 | — | entry signal |
| 2026-10-09T05:40 | Ichimoku | buy | DOGE-USD | 15.88 | — | entry signal |
| 2026-10-09T05:39 | AI bee: Bizzy | sell | XRP-USD | 9.12 | -0.04 | Jev: sell (sell p=0.50) after 11 min |
| 2026-10-09T05:35 | Consensus | buy | XRP-USD | 13.51 | — | entry |
| 2026-10-09T05:35 | Volume breakout | buy | XRP-USD | 18.01 | — | entry signal |
| 2026-10-09T05:35 | Keltner breakout | buy | XRP-USD | 16.37 | — | entry signal |
| 2026-10-09T05:35 | Bollinger breakout | buy | XRP-USD | 13.91 | — | entry signal |
| 2026-10-09T05:30 | Consensus | sell | ETH-USD | 13.45 | -0.08 | target is flat |
| 2026-10-09T05:30 | Stochastic reversion | sell | ETH-USD | 12.72 | -0.02 | exit signal |
| 2026-10-09T05:28 | AI bee: Bizzy | buy | XRP-USD | 9.17 | — | Jev: buy (buy p=0.58) |
| 2026-10-09T05:20 | Consensus | buy | ETH-USD | 13.52 | — | entry |
| 2026-10-09T05:20 | Keltner breakout | buy | DOGE-USD | 16.38 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 06:00:05.000113+00:00 -> 2026-10-09 06:10:05.000113+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
