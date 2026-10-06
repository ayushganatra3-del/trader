# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T21:55:05.000183+00:00 · 13900 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.29 (-1.71%)

Closed trades 37, win rate 62.2%, fees £1.28, max drawdown -2.16%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-06 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PAM 12%, BORR 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-06)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.09 · VIX 15.13 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, MSTR 7.5, AMD 7.3, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 37469 decisions in 3091 calls, $0.4641 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T21:55 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-06T21:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-06T21:55 | 0 / 3 / 2 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| Volume breakout | LABU | 1.81 | +2.37% | 3 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.00 | 6.00 | 0 | — | 0.74 | 0.28 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.78 | -13.79 | 113 |
| 3 | Hold BTC | benchmark | 101.98 | 1.99 | 0 | — | 32.08 | 3.88 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.95 | 1.95 | 0 | — | 0.76 | 0.49 | -5.09 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.62 | 1.62 | 0 | — | 3.28 | 1.57 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.42 | 1.42 | 17 | 0.0 | 12.29 | 1.68 | -16.96 | 110 |
| 8 | Daily: Bullish score | daily | 101.33 | 1.33 | 3 | 0.0 | 5.96 | 0.99 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.06 | 1.06 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.31 | 0.31 | 68 | 38.2 | -21.33 | -4.87 | -23.37 | 488 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.91 | -1.59 | 84 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.01 | 0.01 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 15 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 16 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 17 | Stochastic reversion · 1h | reversion | 99.99 | -0.01 | 56 | 64.3 | -7.95 | -1.63 | -10.86 | 326 |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -3.61 | -1.76 | -5.14 | 1 |
| 20 | EMA 20/50 cross · 1h | trend | 99.86 | -0.14 | 29 | 6.9 | 7.29 | 1.09 | -17.11 | 139 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 2.91 | 0.86 | -6.57 | 122 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.47 | -2.90 | 21 |
| 23 | Connors RSI(2) · 1h | reversion | 99.27 | -0.72 | 74 | 44.6 | -11.03 | -3.98 | -14.77 | 217 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 99.22 | -0.78 | 0 | — | 18.30 | 2.78 | -6.29 | 1 |
| 25 | Trend pullback · 1h | trend | 98.81 | -1.19 | 66 | 24.2 | -20.73 | -6.11 | -24.41 | 166 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -0.17 | -0.04 | -4.23 | 102 |
| 27 | Daily: Momentum burst | daily | 98.38 | -1.62 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.71 | -4.92 | -9.35 | 222 |
| 30 | Z-score reversion · 1h | reversion | 98.25 | -1.75 | 23 | 52.2 | 3.78 | 0.92 | -8.60 | 151 |
| 31 | Copy: Insider buying | copy | 97.94 | -2.06 | 11 | 54.5 | -15.61 | -2.88 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.92 | -2.08 | 49 | 46.9 | -15.16 | -3.78 | -17.03 | 301 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.47 | -2.53 | 0 | — | -0.63 | -0.16 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.19 | -2.81 | 63 | 28.6 | -1.47 | -0.30 | -10.40 | 270 |
| 35 | ADX DI cross · 1h | trend | 96.77 | -3.23 | 43 | 11.6 | -3.01 | -0.38 | -13.84 | 257 |
| 36 | Supertrend · 1h | trend | 96.69 | -3.31 | 33 | 9.1 | 1.74 | 0.42 | -16.43 | 212 |
| 37 | Agent (ML meta-label) | meta | 96.60 | -3.40 | 265 | 14.7 | 7.95 | 1.47 | -13.43 | 388 |
| 38 | Williams %R · 1h | reversion | 96.37 | -3.63 | 85 | 52.9 | -19.78 | -3.71 | -20.14 | 494 |
| 39 | Parabolic SAR · 1h | trend | 96.36 | -3.64 | 65 | 15.4 | -4.29 | -0.39 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.24 | -3.76 | 71 | 49.3 | 0.57 | 0.25 | -12.41 | 406 |
| 41 | MACD cross · 1h | trend | 95.64 | -4.36 | 90 | 20.0 | -13.83 | -2.24 | -17.27 | 469 |
| 42 | RSI momentum · 1h | momentum | 95.37 | -4.63 | 45 | 2.2 | -0.12 | 0.18 | -16.65 | 229 |
| 43 | MFI reversion · 1h | reversion | 95.06 | -4.95 | 75 | 28.0 | -10.21 | -1.78 | -16.99 | 120 |
| 44 | Squeeze breakout · 1h | breakout | 95.00 | -5.00 | 30 | 20.0 | 15.68 | 2.62 | -8.06 | 106 |
| 45 | Max aggression: 1-day momentum | meta | 94.93 | -5.07 | 7 | 42.9 | -23.54 | -1.22 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.82 | -5.17 | 34 | 14.7 | 2.42 | 0.51 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.49 | -5.51 | 57 | 10.5 | -9.72 | -0.96 | -24.82 | 253 |
| 48 | Bollinger breakout · 1h | breakout | 94.47 | -5.53 | 51 | 23.5 | 7.53 | 1.13 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 6.64 | 1.74 | -6.49 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.43 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.56 | -6.44 | 36 | 11.1 | 6.31 | 1.04 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.58 | -7.42 | 83 | 10.8 | -2.95 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.62 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -19.91 | -1.72 | -29.56 | 29 |
| 55 | MACD zero-line · 1h | trend | 91.23 | -8.78 | 50 | 18.0 | -4.58 | -0.42 | -18.32 | 244 |
| 56 | Donchian 20/10 · 1h | breakout | 91.21 | -8.79 | 42 | 14.3 | 2.45 | 0.51 | -16.18 | 223 |
| 57 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.33 | -24.88 | -49.53 | 589 |
| 58 | VWAP momentum · 1h | momentum | 90.65 | -9.35 | 229 | 22.7 | -37.11 | -5.72 | -37.12 | 1268 |
| 59 | OBV trend · 1h | momentum | 90.40 | -9.60 | 109 | 11.9 | -12.63 | -1.41 | -26.73 | 332 |
| 60 | Heikin-Ashi · 1h | trend | 89.91 | -10.09 | 116 | 25.0 | -31.15 | -5.36 | -34.37 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.64 | -10.37 | 30 | 6.7 | -10.61 | -1.23 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.24 | -12.76 | 112 | 16.1 | -9.21 | -1.10 | -23.04 | 412 |
| 63 | RSI(14) reversion | reversion | 85.46 | -14.54 | 225 | 32.0 | -71.69 | -19.80 | -71.96 | 1424 |
| 64 | Squeeze breakout | breakout | 77.44 | -22.57 | 251 | 15.5 | -62.40 | -18.99 | -62.42 | 1224 |
| 65 | VWAP reversion | reversion | 77.12 | -22.88 | 278 | 28.4 | -68.83 | -16.10 | -68.95 | 1382 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.79 | -17.78 | -73.79 | 1643 |
| 67 | Donchian 55/20 | breakout | 76.05 | -23.95 | 259 | 17.4 | -68.90 | -15.33 | -68.91 | 1304 |
| 68 | EMA 20/50 cross | trend | 74.33 | -25.67 | 266 | 18.4 | -78.48 | -16.24 | -78.49 | 1476 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.12 | -19.59 | -65.12 | 918 |
| 70 | Z-score reversion | reversion | 70.96 | -29.04 | 357 | 27.5 | -85.01 | -25.36 | -85.01 | 2041 |
| 71 | MFI reversion | reversion | 69.74 | -30.26 | 357 | 21.0 | -87.15 | -30.71 | -87.15 | 2098 |
| 72 | Supertrend | trend | 69.13 | -30.87 | 361 | 19.9 | -87.19 | -22.47 | -87.20 | 1926 |
| 73 | Keltner breakout | breakout | 67.94 | -32.06 | 350 | 13.1 | -85.48 | -30.55 | -85.49 | 1884 |
| 74 | AI bee: Bizzy | ai | 67.25 | -32.75 | 612 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 66.68 | -33.32 | 321 | 9.0 | -82.23 | -24.93 | -82.23 | 1767 |
| 76 | AI bee: Boozy | ai | 66.11 | -33.89 | 218 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.20 | -35.80 | 404 | 9.2 | -89.65 | -37.28 | -89.65 | 2099 |
| 78 | MACD zero-line | trend | 62.73 | -37.27 | 458 | 15.3 | -91.54 | -31.19 | -91.56 | 2362 |
| 79 | Donchian 20/10 | breakout | 62.32 | -37.68 | 494 | 18.0 | -91.16 | -27.73 | -91.16 | 2668 |
| 80 | RSI momentum | momentum | 61.34 | -38.66 | 459 | 16.8 | -90.71 | -27.02 | -90.71 | 2383 |
| 81 | Triple EMA stack | trend | 59.98 | -40.02 | 510 | 15.3 | -93.39 | -32.70 | -93.39 | 2631 |
| 82 | Trend pullback | trend | 59.96 | -40.04 | 492 | 15.4 | -91.45 | -30.75 | -91.45 | 2348 |
| 83 | Bollinger breakout | breakout | 59.08 | -40.92 | 503 | 13.9 | -94.01 | -35.84 | -94.01 | 2822 |
| 84 | Stochastic reversion | reversion | 57.76 | -42.24 | 722 | 23.3 | -95.52 | -37.20 | -95.52 | 4037 |
| 85 | Bollinger reversion | reversion | 57.31 | -42.69 | 665 | 17.9 | -95.65 | -36.25 | -95.65 | 3672 |
| 86 | Consensus | meta | 56.98 | -43.02 | 491 | 10.0 | -94.71 | -27.40 | -94.71 | 2727 |
| 87 | EMA 9/21 cross | trend | 55.21 | -44.79 | 630 | 16.3 | -97.44 | -35.61 | -97.44 | 3550 |
| 88 | Connors RSI(2) | reversion | 53.72 | -46.28 | 680 | 20.1 | -96.58 | -35.38 | -96.58 | 3640 |
| 89 | OBV trend | momentum | 51.99 | -48.01 | 740 | 14.7 | -96.47 | -39.99 | -96.47 | 3603 |
| 90 | CCI reversion | reversion | 51.68 | -48.32 | 699 | 17.3 | -98.44 | -40.33 | -98.44 | 4685 |
| 91 | Candlestick reversal ⏸ | reversion | 50.65 | -49.35 | 803 | 14.9 | -99.30 | -39.60 | -99.30 | 5620 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.73 | -32.37 | -98.73 | 5361 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -46.86 | -99.72 | 6128 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.41 | -42.57 | -97.41 | 3684 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -44.09 | -99.50 | 6093 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.60 | -99.90 | 8243 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T21:55 | Connors RSI(2) · 1h | sell | DOGE-USD | 24.39 | -0.53 | stop-loss |
| 2026-10-06T21:55 | Bollinger breakout | sell | ETH-USD | 14.72 | -0.09 | exit signal |
| 2026-10-06T21:55 | ADX DI cross | sell | ETH-USD | 16.00 | -0.07 | exit signal |
| 2026-10-06T21:55 | Supertrend | sell | XRP-USD | 17.18 | -0.18 | exit signal |
| 2026-10-06T21:55 | MACD zero-line | sell | ETH-USD | 15.68 | -0.10 | exit signal |
| 2026-10-06T21:45 | RSI momentum | buy | SOL-USD | 15.35 | — | entry signal |
| 2026-10-06T21:42 | AI bee: Bizzy | sell | SOL-USD | 9.65 | -0.05 | Jev: sell (sell p=0.62) after 12 min |
| 2026-10-06T21:35 | Bollinger reversion | sell | BTC-USD | 14.28 | -0.08 | exit signal |
| 2026-10-06T21:30 | AI bee: Bizzy | buy | SOL-USD | 9.70 | — | Jev: buy (buy p=0.58) |
| 2026-10-06T21:30 | CCI reversion | buy | BTC-USD | 12.95 | — | entry signal |
| 2026-10-06T21:30 | Trend pullback | buy | SOL-USD | 15.00 | — | entry signal |
| 2026-10-06T21:25 | Consensus | buy | SOL-USD | 14.26 | — | entry |
| 2026-10-06T21:25 | CCI reversion | buy | XRP-USD | 12.96 | — | entry signal |
| 2026-10-06T21:25 | Bollinger reversion | buy | BTC-USD | 14.36 | — | entry signal |
| 2026-10-06T21:25 | Connors RSI(2) | sell | SOL-USD | 13.38 | -0.07 | exit signal |
| 2026-10-06T21:20 | AI bee: Bizzy | sell | DOGE-USD | 10.50 | -0.10 | Jev: sell (sell p=0.93) after 11 min |
| 2026-10-06T21:20 | Consensus | sell | SOL-USD | 14.18 | -0.09 | target is flat |
| 2026-10-06T21:20 | Connors RSI(2) | buy | SOL-USD | 13.45 | — | entry signal |
| 2026-10-06T21:20 | Donchian 20/10 | sell | SOL-USD | 15.48 | -0.14 | exit signal |
| 2026-10-06T21:20 | RSI momentum | sell | SOL-USD | 15.27 | -0.13 | exit signal |
| 2026-10-06T21:20 | Ichimoku | sell | SOL-USD | 16.55 | -0.15 | exit signal |
| 2026-10-06T21:10 | Stochastic reversion | buy | XRP-USD | 14.47 | — | entry signal |
| 2026-10-06T21:10 | Bollinger reversion | buy | DOGE-USD | 14.37 | — | entry signal |
| 2026-10-06T21:10 | MACD zero-line | sell | SOL-USD | 15.70 | -0.09 | exit signal |
| 2026-10-06T21:10 | MACD zero-line | sell | BTC-USD | 15.66 | -0.12 | exit signal |
| 2026-10-06T21:10 | EMA 9/21 cross | sell | BTC-USD | 13.77 | -0.10 | exit signal |
| 2026-10-06T21:09 | AI bee: Bizzy | buy | DOGE-USD | 10.60 | — | Jev: buy (buy p=0.63) |
| 2026-10-06T21:05 | Bollinger breakout | sell | SOL-USD | 14.70 | -0.12 | exit signal |
| 2026-10-06T21:05 | MACD zero-line | sell | XRP-USD | 15.65 | -0.14 | exit signal |
| 2026-10-06T21:05 | EMA 9/21 cross | sell | XRP-USD | 13.73 | -0.13 | stop-loss |
| 2026-10-06T21:00 | Stochastic reversion | buy | DOGE-USD | 14.48 | — | entry signal |
| 2026-10-06T20:49 | AI bee: Boozy | sell | ETH-USD | 20.42 | -0.11 | Jev: add (buy p=0.53) |
| 2026-10-06T20:40 | Stochastic reversion | sell | BTC-USD | 11.60 | -0.05 | exit signal |
| 2026-10-06T20:40 | Bollinger breakout | buy | ETH-USD | 14.81 | — | entry signal |
| 2026-10-06T20:40 | RSI momentum | buy | ETH-USD | 15.39 | — | entry signal |
| 2026-10-06T20:40 | MACD zero-line | buy | ETH-USD | 15.78 | — | entry signal |
| 2026-10-06T20:40 | MACD zero-line | buy | BTC-USD | 15.78 | — | entry signal |
| 2026-10-06T20:35 | Donchian 20/10 | buy | ETH-USD | 15.61 | — | entry signal |
| 2026-10-06T20:34 | AI bee: Boozy | buy | ETH-USD | 20.53 | — | Jev: buy (buy p=0.71) |
| 2026-10-06T20:33 | AI bee: Bizzy | sell | SOL-USD | 9.70 | -0.07 | Jev: sell (sell p=0.73) after 11 min |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 21:55:05.000183+00:00 -> 2026-10-06 22:05:05.000183+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
