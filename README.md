# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T22:25:05.000173+00:00 · 13923 ticks

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

Today: 37814 decisions in 3160 calls, $0.4690 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T22:25 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-06T22:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-06T22:25 | 0 / 4 / 1 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |
| VWAP reversion | TECL | 1.77 | +2.87% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.00 | 6.00 | 0 | — | 0.74 | 0.28 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.78 | -13.79 | 113 |
| 3 | Hold BTC | benchmark | 101.98 | 1.98 | 0 | — | 31.95 | 3.86 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.95 | 1.95 | 0 | — | 0.76 | 0.49 | -5.09 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.62 | 1.62 | 0 | — | 3.28 | 1.57 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.42 | 1.42 | 17 | 0.0 | 12.29 | 1.68 | -16.96 | 110 |
| 8 | Daily: Bullish score | daily | 101.33 | 1.33 | 3 | 0.0 | 5.96 | 0.99 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.06 | 1.06 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.32 | 0.32 | 68 | 38.2 | -21.04 | -4.78 | -23.37 | 486 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.91 | -1.59 | 84 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.01 | 0.01 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 15 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 16 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 17 | Stochastic reversion · 1h | reversion | 99.99 | -0.01 | 56 | 64.3 | -7.62 | -1.56 | -10.60 | 325 |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -3.61 | -1.76 | -5.14 | 1 |
| 20 | EMA 20/50 cross · 1h | trend | 99.88 | -0.12 | 29 | 6.9 | 7.31 | 1.09 | -17.11 | 139 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.09 | 1.18 | -6.57 | 116 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.47 | -2.90 | 21 |
| 23 | Connors RSI(2) · 1h | reversion | 99.27 | -0.72 | 74 | 44.6 | -11.03 | -3.98 | -14.77 | 217 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 99.22 | -0.78 | 0 | — | 18.30 | 2.78 | -6.29 | 1 |
| 25 | Trend pullback · 1h | trend | 98.86 | -1.14 | 66 | 24.2 | -20.91 | -6.18 | -24.41 | 167 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -0.17 | -0.04 | -4.23 | 102 |
| 27 | Daily: Momentum burst | daily | 98.38 | -1.62 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.71 | -4.92 | -9.35 | 222 |
| 30 | Z-score reversion · 1h | reversion | 98.26 | -1.74 | 23 | 52.2 | 3.78 | 0.92 | -8.60 | 151 |
| 31 | Copy: Insider buying | copy | 97.94 | -2.06 | 11 | 54.5 | -15.61 | -2.88 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.85 | -2.15 | 49 | 46.9 | -15.23 | -3.79 | -17.03 | 302 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.47 | -2.53 | 0 | — | -0.63 | -0.16 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.19 | -2.81 | 63 | 28.6 | 0.54 | 0.24 | -9.99 | 269 |
| 35 | ADX DI cross · 1h | trend | 96.77 | -3.23 | 43 | 11.6 | -3.01 | -0.38 | -13.84 | 257 |
| 36 | Supertrend · 1h | trend | 96.70 | -3.30 | 33 | 9.1 | 1.69 | 0.42 | -16.43 | 212 |
| 37 | Agent (ML meta-label) | meta | 96.60 | -3.40 | 265 | 14.7 | 4.94 | 1.01 | -13.19 | 385 |
| 38 | Williams %R · 1h | reversion | 96.38 | -3.62 | 85 | 52.9 | -19.44 | -3.64 | -19.95 | 493 |
| 39 | Parabolic SAR · 1h | trend | 96.37 | -3.63 | 65 | 15.4 | -4.27 | -0.39 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.25 | -3.75 | 71 | 49.3 | 0.53 | 0.25 | -12.41 | 406 |
| 41 | MACD cross · 1h | trend | 95.66 | -4.34 | 90 | 20.0 | -13.79 | -2.23 | -17.27 | 469 |
| 42 | RSI momentum · 1h | momentum | 95.37 | -4.63 | 45 | 2.2 | 0.09 | 0.21 | -16.65 | 229 |
| 43 | MFI reversion · 1h | reversion | 95.06 | -4.95 | 75 | 28.0 | -9.66 | -1.67 | -16.99 | 118 |
| 44 | Squeeze breakout · 1h | breakout | 95.00 | -5.00 | 30 | 20.0 | 14.84 | 2.49 | -8.06 | 109 |
| 45 | Max aggression: 1-day momentum | meta | 94.93 | -5.07 | 7 | 42.9 | -23.54 | -1.22 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.86 | -5.14 | 34 | 14.7 | 2.46 | 0.51 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.49 | -5.51 | 57 | 10.5 | -9.66 | -0.96 | -24.82 | 253 |
| 48 | Bollinger breakout · 1h | breakout | 94.47 | -5.53 | 51 | 23.5 | 7.53 | 1.13 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 7.12 | 1.87 | -6.07 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.43 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.56 | -6.44 | 36 | 11.1 | 6.25 | 1.03 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.58 | -7.42 | 83 | 10.8 | -2.95 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.62 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -19.91 | -1.72 | -29.56 | 29 |
| 55 | MACD zero-line · 1h | trend | 91.27 | -8.73 | 50 | 18.0 | -4.33 | -0.39 | -18.32 | 243 |
| 56 | Donchian 20/10 · 1h | breakout | 91.23 | -8.77 | 42 | 14.3 | 2.79 | 0.55 | -16.18 | 222 |
| 57 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.33 | -24.88 | -49.53 | 589 |
| 58 | VWAP momentum · 1h | momentum | 90.65 | -9.35 | 229 | 22.7 | -37.01 | -5.70 | -37.06 | 1269 |
| 59 | OBV trend · 1h | momentum | 90.41 | -9.59 | 109 | 11.9 | -12.66 | -1.42 | -26.73 | 334 |
| 60 | Heikin-Ashi · 1h | trend | 89.91 | -10.09 | 116 | 25.0 | -31.15 | -5.36 | -34.37 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.64 | -10.37 | 30 | 6.7 | -10.65 | -1.24 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.26 | -12.74 | 112 | 16.1 | -9.44 | -1.14 | -23.04 | 414 |
| 63 | RSI(14) reversion | reversion | 85.49 | -14.51 | 225 | 32.0 | -71.59 | -19.67 | -71.87 | 1421 |
| 64 | Squeeze breakout | breakout | 77.35 | -22.66 | 251 | 15.5 | -62.49 | -19.03 | -62.50 | 1226 |
| 65 | VWAP reversion | reversion | 77.15 | -22.85 | 278 | 28.4 | -69.04 | -16.24 | -69.16 | 1376 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.95 | -17.84 | -73.95 | 1655 |
| 67 | Donchian 55/20 | breakout | 75.96 | -24.04 | 259 | 17.4 | -68.94 | -15.34 | -68.94 | 1305 |
| 68 | EMA 20/50 cross | trend | 74.31 | -25.69 | 266 | 18.4 | -78.49 | -16.24 | -78.49 | 1477 |
| 69 | Volume breakout | breakout | 73.37 | -26.63 | 211 | 12.3 | -65.54 | -19.57 | -65.55 | 924 |
| 70 | Z-score reversion | reversion | 70.99 | -29.01 | 357 | 27.5 | -84.95 | -25.34 | -84.95 | 2039 |
| 71 | MFI reversion | reversion | 69.76 | -30.24 | 357 | 21.0 | -87.09 | -30.57 | -87.09 | 2098 |
| 72 | Supertrend | trend | 69.18 | -30.82 | 361 | 19.9 | -87.18 | -22.47 | -87.20 | 1926 |
| 73 | Keltner breakout | breakout | 67.86 | -32.14 | 350 | 13.1 | -85.49 | -30.57 | -85.51 | 1885 |
| 74 | AI bee: Bizzy | ai | 67.20 | -32.80 | 613 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 66.60 | -33.40 | 321 | 9.0 | -82.26 | -24.95 | -82.28 | 1769 |
| 76 | AI bee: Boozy | ai | 65.97 | -34.03 | 219 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.20 | -35.80 | 404 | 9.2 | -89.63 | -37.28 | -89.63 | 2098 |
| 78 | MACD zero-line | trend | 62.62 | -37.38 | 459 | 15.3 | -91.56 | -31.18 | -91.57 | 2363 |
| 79 | Donchian 20/10 | breakout | 62.27 | -37.73 | 494 | 18.0 | -91.17 | -27.73 | -91.17 | 2669 |
| 80 | RSI momentum | momentum | 61.38 | -38.62 | 459 | 16.8 | -90.70 | -27.02 | -90.71 | 2383 |
| 81 | Trend pullback | trend | 60.00 | -40.00 | 492 | 15.4 | -91.45 | -30.75 | -91.45 | 2348 |
| 82 | Triple EMA stack | trend | 59.96 | -40.04 | 510 | 15.3 | -93.40 | -32.70 | -93.40 | 2632 |
| 83 | Bollinger breakout | breakout | 58.93 | -41.07 | 504 | 13.9 | -94.03 | -35.85 | -94.03 | 2824 |
| 84 | Stochastic reversion | reversion | 57.79 | -42.21 | 722 | 23.3 | -95.52 | -37.19 | -95.52 | 4037 |
| 85 | Bollinger reversion | reversion | 57.26 | -42.74 | 666 | 17.9 | -95.65 | -36.25 | -95.66 | 3673 |
| 86 | Consensus | meta | 57.03 | -42.98 | 491 | 10.0 | -94.69 | -27.36 | -94.69 | 2719 |
| 87 | EMA 9/21 cross | trend | 55.16 | -44.84 | 631 | 16.3 | -97.44 | -35.61 | -97.44 | 3551 |
| 88 | Connors RSI(2) | reversion | 53.72 | -46.28 | 680 | 20.1 | -96.57 | -35.40 | -96.57 | 3639 |
| 89 | OBV trend | momentum | 51.98 | -48.02 | 740 | 14.7 | -96.46 | -40.03 | -96.46 | 3635 |
| 90 | CCI reversion | reversion | 51.69 | -48.31 | 700 | 17.3 | -98.44 | -40.29 | -98.44 | 4684 |
| 91 | Candlestick reversal ⏸ | reversion | 50.65 | -49.35 | 803 | 14.9 | -99.29 | -39.50 | -99.29 | 5616 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -32.15 | -98.72 | 5365 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -46.83 | -99.73 | 6129 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.41 | -42.53 | -97.41 | 3683 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -43.83 | -99.50 | 6089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.62 | -99.90 | 8245 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T22:25 | AI bee: Boozy | sell | SOL-USD | 20.27 | -0.14 | Jev: sell (sell p=0.52) after 16 min |
| 2026-10-06T22:25 | MACD zero-line | sell | BTC-USD | 15.57 | -0.11 | exit signal |
| 2026-10-06T22:25 | EMA 9/21 cross | sell | BTC-USD | 13.71 | -0.09 | exit signal |
| 2026-10-06T22:15 | AI bee: Bizzy | sell | SOL-USD | 9.43 | -0.05 | Jev: sell (sell p=0.57) after 11 min |
| 2026-10-06T22:15 | Bollinger breakout | sell | ETH-USD | 14.67 | -0.10 | exit signal |
| 2026-10-06T22:10 | CCI reversion | sell | BTC-USD | 12.88 | -0.06 | exit signal |
| 2026-10-06T22:10 | Squeeze breakout | buy | SOL-USD | 19.36 | — | entry signal |
| 2026-10-06T22:10 | Keltner breakout | buy | SOL-USD | 16.99 | — | entry signal |
| 2026-10-06T22:10 | Donchian 55/20 | buy | SOL-USD | 19.01 | — | entry signal |
| 2026-10-06T22:10 | Ichimoku | buy | SOL-USD | 16.67 | — | entry signal |
| 2026-10-06T22:10 | Triple EMA stack | buy | ETH-USD | 15.01 | — | entry signal |
| 2026-10-06T22:09 | AI bee: Boozy | buy | SOL-USD | 20.42 | — | Jev: buy (buy p=0.69) |
| 2026-10-06T22:05 | Bollinger reversion | sell | XRP-USD | 14.26 | -0.07 | exit signal |
| 2026-10-06T22:05 | Volume breakout | buy | SOL-USD | 18.36 | — | entry signal |
| 2026-10-06T22:05 | Bollinger breakout | buy | SOL-USD | 14.77 | — | entry signal |
| 2026-10-06T22:05 | Bollinger breakout | buy | ETH-USD | 14.77 | — | entry signal |
| 2026-10-06T22:05 | Donchian 20/10 | buy | SOL-USD | 15.58 | — | entry signal |
| 2026-10-06T22:05 | OBV trend | buy | ETH-USD | 13.01 | — | entry signal |
| 2026-10-06T22:05 | MACD zero-line | buy | BTC-USD | 15.68 | — | entry signal |
| 2026-10-06T22:05 | EMA 20/50 cross | buy | ETH-USD | 18.60 | — | entry signal |
| 2026-10-06T22:04 | AI bee: Bizzy | buy | SOL-USD | 9.48 | — | Jev: buy (buy p=0.56) |
| 2026-10-06T22:00 | Bollinger reversion · 1h | buy | DOGE-USD | 24.48 | — | entry signal |
| 2026-10-06T22:00 | Bollinger reversion | buy | XRP-USD | 14.33 | — | entry signal |
| 2026-10-06T22:00 | EMA 9/21 cross | buy | BTC-USD | 13.81 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 22:25:05.000173+00:00 -> 2026-10-06 22:35:05.000173+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
