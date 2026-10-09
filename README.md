# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T03:00:05.000141+00:00 · 16280 ticks

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

Today: 2070 decisions in 414 calls, $0.0290 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T03:00 | 0 / 4 / 1 | SOXL 15%, AMD 14% |  |
| Breezy | 2026-10-09T03:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T03:00 | 2 / 3 / 0 | ETH-USD 27% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 102.99 | 2.99 | 36 | 41.7 | -8.00 | -2.43 | -13.79 | 119 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.32 | 1.32 | 0 | — | -4.29 | -1.79 | -7.31 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 101.17 | 1.17 | 0 | — | -6.17 | -1.07 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.62 | 0.62 | 0 | — | -0.11 | -0.02 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.58 | 0.58 | 0 | — | 1.17 | 0.59 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.57 | 0.57 | 0 | — | -1.64 | -0.89 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -3.83 | -1.25 | -9.74 | 25 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.68 | -0.32 | 0 | — | 0.61 | 0.31 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.97 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.41 | -1.47 | -3.04 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.18 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.67 | -1.33 | 0 | — | -5.06 | -2.42 | -5.36 | 1 |
| 17 | Copy: Insider buying | copy | 98.38 | -1.62 | 12 | 50.0 | -15.22 | -2.65 | -21.08 | 75 |
| 18 | Stochastic reversion · 1h | reversion | 98.19 | -1.81 | 77 | 50.6 | -12.60 | -2.52 | -15.21 | 345 |
| 19 | Hold BTC | benchmark | 98.06 | -1.94 | 0 | — | 25.87 | 3.11 | -8.68 | 1 |
| 20 | Donchian 55/20 · 1h | breakout | 98.04 | -1.96 | 26 | 15.4 | 10.01 | 1.34 | -16.96 | 109 |
| 21 | Three white soldiers · 1h | momentum | 97.53 | -2.47 | 6 | 0.0 | -3.03 | -2.34 | -4.15 | 26 |
| 22 | Agent (rotation) | meta | 96.55 | -3.45 | 78 | 28.2 | 3.08 | 0.87 | -8.33 | 263 |
| 23 | ADX DI cross · 1h | trend | 96.53 | -3.47 | 54 | 22.2 | -4.53 | -0.64 | -13.84 | 249 |
| 24 | Trend pullback · 1h | trend | 96.53 | -3.47 | 78 | 23.1 | -23.34 | -6.55 | -25.53 | 170 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.28 | -3.72 | 0 | — | 8.88 | 1.50 | -8.33 | 1 |
| 26 | EMA 20/50 cross · 1h | trend | 96.12 | -3.88 | 36 | 11.1 | 0.50 | 0.28 | -20.52 | 135 |
| 27 | Daily: Momentum burst | daily | 95.97 | -4.03 | 4 | 0.0 | -4.75 | -0.57 | -17.67 | 40 |
| 28 | Z-score reversion · 1h | reversion | 95.94 | -4.06 | 36 | 38.9 | -0.59 | 0.00 | -8.60 | 168 |
| 29 | Agent | meta | 95.70 | -4.30 | 50 | 54.0 | -10.66 | -5.64 | -11.21 | 250 |
| 30 | Daily: Bullish score | daily | 95.70 | -4.30 | 3 | 0.0 | -1.35 | 0.02 | -12.76 | 10 |
| 31 | Parabolic SAR · 1h | trend | 95.09 | -4.91 | 82 | 22.0 | -5.24 | -0.55 | -20.80 | 291 |
| 32 | MACD cross · 1h | trend | 95.09 | -4.92 | 105 | 22.9 | -18.35 | -2.93 | -19.72 | 463 |
| 33 | Squeeze breakout · 1h | breakout | 94.87 | -5.13 | 34 | 26.5 | 15.40 | 2.52 | -8.14 | 102 |
| 34 | Supertrend · 1h | trend | 94.33 | -5.67 | 51 | 13.7 | -4.59 | -0.47 | -18.09 | 210 |
| 35 | Agent (aggressive) | meta | 94.25 | -5.75 | 22 | 45.5 | -10.08 | -3.61 | -10.37 | 116 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.31 | 1.87 | -6.52 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.36 | -6.64 | 102 | 41.2 | -18.29 | -6.02 | -20.97 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.08 | 0.21 | -19.98 | 119 |
| 39 | Agent (ML meta-label) | meta | 92.57 | -7.43 | 350 | 18.6 | -5.28 | -0.85 | -13.87 | 405 |
| 40 | Bollinger breakout · 1h | breakout | 92.53 | -7.47 | 65 | 30.8 | 6.44 | 0.98 | -12.06 | 285 |
| 41 | RSI momentum · 1h | momentum | 92.34 | -7.66 | 60 | 15.0 | 0.82 | 0.30 | -16.65 | 219 |
| 42 | RSI(14) reversion · 1h | reversion | 92.24 | -7.76 | 26 | 26.9 | -4.09 | -0.78 | -9.03 | 152 |
| 43 | Volume breakout · 1h | breakout | 92.11 | -7.89 | 45 | 17.8 | 6.47 | 1.04 | -12.60 | 121 |
| 44 | Bollinger reversion · 1h | reversion | 91.52 | -8.48 | 68 | 33.8 | -22.02 | -5.32 | -23.94 | 319 |
| 45 | Max aggression: 1-day momentum | meta | 91.23 | -8.77 | 9 | 33.3 | -23.96 | -1.22 | -37.31 | 43 |
| 46 | Triple EMA stack · 1h | trend | 91.19 | -8.81 | 68 | 16.2 | -10.85 | -1.19 | -25.80 | 236 |
| 47 | MFI reversion · 1h | reversion | 90.93 | -9.07 | 96 | 28.1 | -15.13 | -2.59 | -16.99 | 130 |
| 48 | Opening range 30m | breakout | 90.76 | -9.23 | 131 | 20.6 | -17.37 | -5.24 | -17.94 | 562 |
| 49 | Candlestick reversal · 1h | reversion | 90.53 | -9.47 | 97 | 29.9 | -29.50 | -5.82 | -30.81 | 499 |
| 50 | MACD zero-line · 1h | trend | 90.32 | -9.68 | 58 | 20.7 | -6.33 | -0.68 | -19.00 | 240 |
| 51 | Williams %R · 1h | reversion | 90.14 | -9.86 | 107 | 44.9 | -26.78 | -4.70 | -27.36 | 515 |
| 52 | Three white soldiers | momentum | 89.14 | -10.86 | 122 | 18.9 | -48.12 | -23.24 | -48.12 | 585 |
| 53 | Opening range 15m | breakout | 88.59 | -11.41 | 153 | 19.0 | -19.52 | -5.58 | -20.06 | 683 |
| 54 | EMA 9/21 cross · 1h | trend | 88.49 | -11.51 | 99 | 14.1 | -10.81 | -1.26 | -20.61 | 333 |
| 55 | Donchian 20/10 · 1h | breakout | 88.28 | -11.72 | 55 | 20.0 | -1.95 | -0.03 | -17.36 | 219 |
| 56 | OBV trend · 1h | momentum | 88.25 | -11.75 | 139 | 18.0 | -15.29 | -1.74 | -30.19 | 316 |
| 57 | VWAP momentum · 1h | momentum | 88.18 | -11.82 | 262 | 21.4 | -36.68 | -5.56 | -39.21 | 1265 |
| 58 | Keltner breakout · 1h | breakout | 87.63 | -12.37 | 41 | 19.5 | -11.06 | -1.27 | -24.35 | 225 |
| 59 | CCI reversion · 1h | reversion | 87.62 | -12.38 | 91 | 40.7 | -11.16 | -1.52 | -14.35 | 419 |
| 60 | Heikin-Ashi · 1h | trend | 87.53 | -12.47 | 133 | 25.6 | -32.61 | -5.54 | -36.34 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 128 | 21.1 | -10.45 | -1.26 | -23.15 | 407 |
| 62 | Max aggression: 5-day momentum | meta | 83.55 | -16.45 | 7 | 28.6 | -27.10 | -2.40 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.52 | -23.48 | 352 | 21.6 | -72.67 | -16.35 | -73.75 | 1644 |
| 64 | RSI(14) reversion | reversion | 75.62 | -24.38 | 339 | 28.0 | -73.44 | -18.38 | -73.64 | 1501 |
| 65 | Squeeze breakout | breakout | 74.35 | -25.65 | 277 | 15.2 | -62.10 | -18.13 | -62.10 | 1207 |
| 66 | Volume breakout | breakout | 72.28 | -27.72 | 225 | 13.3 | -63.60 | -18.18 | -63.60 | 900 |
| 67 | EMA 20/50 cross | trend | 72.19 | -27.81 | 288 | 18.4 | -77.43 | -15.37 | -77.56 | 1451 |
| 68 | Donchian 55/20 | breakout | 71.87 | -28.13 | 283 | 17.0 | -68.56 | -14.68 | -68.61 | 1282 |
| 69 | VWAP reversion | reversion | 68.60 | -31.40 | 379 | 25.3 | -71.95 | -16.05 | -72.24 | 1436 |
| 70 | Supertrend | trend | 67.39 | -32.61 | 414 | 20.3 | -86.73 | -21.14 | -86.96 | 1931 |
| 71 | Keltner breakout | breakout | 65.60 | -34.40 | 387 | 14.0 | -84.62 | -27.99 | -84.62 | 1852 |
| 72 | Ichimoku | trend | 63.62 | -36.38 | 355 | 9.3 | -81.73 | -23.20 | -81.73 | 1735 |
| 73 | AI bee: Bizzy | ai | 63.43 | -36.57 | 704 | 9.1 | — | — | — | — |
| 74 | MFI reversion | reversion | 62.36 | -37.64 | 447 | 20.8 | -88.00 | -28.44 | -88.02 | 2127 |
| 75 | Z-score reversion | reversion | 62.15 | -37.85 | 462 | 23.6 | -86.08 | -23.51 | -86.16 | 2097 |
| 76 | ADX DI cross | trend | 61.10 | -38.90 | 489 | 10.6 | -89.58 | -34.01 | -89.68 | 2133 |
| 77 | Donchian 20/10 | breakout | 60.08 | -39.92 | 548 | 18.6 | -90.95 | -25.89 | -90.97 | 2643 |
| 78 | AI bee: Boozy | ai | 59.99 | -40.02 | 239 | 5.4 | — | — | — | — |
| 79 | MACD zero-line | trend | 59.98 | -40.02 | 517 | 16.1 | -91.34 | -29.00 | -91.36 | 2350 |
| 80 | Trend pullback | trend | 59.59 | -40.41 | 507 | 15.8 | -90.52 | -26.71 | -90.56 | 2284 |
| 81 | RSI momentum | momentum | 58.98 | -41.02 | 515 | 17.9 | -90.27 | -25.17 | -90.33 | 2346 |
| 82 | Triple EMA stack | trend | 58.31 | -41.69 | 542 | 15.7 | -93.10 | -29.80 | -93.11 | 2591 |
| 83 | Bollinger breakout | breakout | 55.76 | -44.24 | 576 | 14.9 | -93.69 | -32.84 | -93.70 | 2807 |
| 84 | Consensus | meta | 54.28 | -45.72 | 542 | 10.1 | -94.23 | -25.16 | -94.23 | 2658 |
| 85 | Connors RSI(2) | reversion | 52.59 | -47.41 | 721 | 21.1 | -96.09 | -30.83 | -96.09 | 3539 |
| 86 | EMA 9/21 cross | trend | 52.54 | -47.46 | 697 | 16.5 | -97.31 | -32.23 | -97.33 | 3522 |
| 87 | Stochastic reversion | reversion | 50.98 | -49.02 | 863 | 22.9 | -95.69 | -33.64 | -95.73 | 4070 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.74 | -30.51 | -98.74 | 5351 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -35.78 | -96.32 | 3559 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -35.81 | -99.35 | 5667 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.24 | -99.73 | 6137 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.88 | -97.35 | 3636 |
| 93 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -36.42 | -98.51 | 4703 |
| 94 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.23 | -99.52 | 6121 |
| 95 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -33.09 | -95.92 | 3731 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.39 | -99.90 | 8243 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T03:00 | AI bee: Bizzy | sell | SOL-USD | 9.40 | -0.04 | Jev: sell (sell p=0.57) after 16 min |
| 2026-10-09T03:00 | Stochastic reversion · 1h | sell | XRP-USD | 8.33 | 0.33 | exit signal |
| 2026-10-09T02:55 | Consensus | buy | DOGE-USD | 5.51 | — | entry |
| 2026-10-09T02:55 | Consensus | sell | SOL-USD | 2.72 | -0.00 | rebalance down |
| 2026-10-09T02:55 | Consensus | sell | BTC-USD | 2.79 | -0.01 | rebalance down |
| 2026-10-09T02:55 | Volume breakout | buy | SOL-USD | 18.16 | — | entry signal |
| 2026-10-09T02:55 | Volume breakout | buy | ETH-USD | 18.16 | — | entry signal |
| 2026-10-09T02:55 | Volume breakout | buy | DOGE-USD | 18.16 | — | entry signal |
| 2026-10-09T02:55 | Volume breakout | buy | BTC-USD | 18.16 | — | entry signal |
| 2026-10-09T02:55 | Squeeze breakout | buy | XRP-USD | 18.62 | — | entry signal |
| 2026-10-09T02:55 | Keltner breakout | buy | SOL-USD | 16.46 | — | entry signal |
| 2026-10-09T02:55 | Keltner breakout | buy | ETH-USD | 16.46 | — | entry signal |
| 2026-10-09T02:55 | Keltner breakout | buy | BTC-USD | 16.46 | — | entry signal |
| 2026-10-09T02:55 | Bollinger breakout | buy | XRP-USD | 13.99 | — | entry signal |
| 2026-10-09T02:55 | Bollinger breakout | buy | ETH-USD | 13.99 | — | entry signal |
| 2026-10-09T02:55 | Donchian 55/20 | buy | DOGE-USD | 17.85 | — | entry signal |
| 2026-10-09T02:55 | Donchian 20/10 | buy | XRP-USD | 12.01 | — | entry signal |
| 2026-10-09T02:55 | Donchian 20/10 | buy | DOGE-USD | 12.06 | — | entry signal |
| 2026-10-09T02:55 | Donchian 20/10 | sell | SOL-USD | 3.07 | 0.00 | rebalance down |
| 2026-10-09T02:55 | Donchian 20/10 | sell | ETH-USD | 3.04 | -0.01 | rebalance down |
| 2026-10-09T02:55 | RSI momentum | buy | XRP-USD | 8.89 | — | entry signal |
| 2026-10-09T02:55 | RSI momentum | buy | DOGE-USD | 11.83 | — | entry signal |
| 2026-10-09T02:55 | RSI momentum | sell | SOL-USD | 3.02 | 0.00 | rebalance down |
| 2026-10-09T02:55 | Ichimoku | buy | XRP-USD | 15.93 | — | entry signal |
| 2026-10-09T02:50 | Consensus | buy | XRP-USD | 13.53 | — | entry |
| 2026-10-09T02:50 | Triple EMA stack | buy | XRP-USD | 8.79 | — | entry signal |
| 2026-10-09T02:50 | Triple EMA stack | sell | ETH-USD | 2.94 | -0.01 | rebalance down |
| 2026-10-09T02:50 | Triple EMA stack | sell | DOGE-USD | 2.93 | -0.01 | rebalance down |
| 2026-10-09T02:50 | Triple EMA stack | sell | BTC-USD | 2.92 | -0.01 | rebalance down |
| 2026-10-09T02:50 | EMA 9/21 cross | buy | XRP-USD | 10.48 | — | entry signal |
| 2026-10-09T02:50 | EMA 9/21 cross | sell | SOL-USD | 2.64 | -0.00 | rebalance down |
| 2026-10-09T02:50 | EMA 9/21 cross | sell | DOGE-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-09T02:49 | AI bee: Boozy | buy | ETH-USD | 16.13 | — | Jev: buy (buy p=0.74) |
| 2026-10-09T02:45 | Consensus | buy | SOL-USD | 13.59 | — | entry |
| 2026-10-09T02:45 | Consensus | buy | ETH-USD | 13.59 | — | entry |
| 2026-10-09T02:45 | Triple EMA stack | buy | SOL-USD | 14.54 | — | entry signal |
| 2026-10-09T02:45 | EMA 20/50 cross | buy | SOL-USD | 10.68 | — | entry signal |
| 2026-10-09T02:45 | EMA 20/50 cross | sell | DOGE-USD | 3.65 | 0.00 | rebalance down |
| 2026-10-09T02:44 | AI bee: Bizzy | buy | SOL-USD | 9.44 | — | Jev: buy (buy p=0.59) |
| 2026-10-09T02:40 | Stochastic reversion | buy | XRP-USD | 12.74 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 03:00:05.000141+00:00 -> 2026-10-09 03:10:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
