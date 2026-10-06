# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T23:55:05.000165+00:00 · 13985 ticks

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

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.15 · VIX 15.01 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.5, MSTR 7.5, AMD 7.3, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38744 decisions in 3346 calls, $0.4820 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T23:55 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-06T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-06T23:55 | 3 / 2 / 0 | MSTR 69% |  |

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
| 3 | Hold BTC | benchmark | 102.03 | 2.03 | 0 | — | 32.11 | 3.88 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.96 | 1.96 | 0 | — | 0.76 | 0.49 | -5.09 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.62 | 1.62 | 0 | — | 3.28 | 1.57 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.42 | 1.42 | 17 | 0.0 | 12.29 | 1.68 | -16.96 | 110 |
| 8 | Daily: Bullish score | daily | 101.33 | 1.33 | 3 | 0.0 | 5.96 | 0.99 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.07 | 1.07 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.33 | 0.33 | 68 | 38.2 | -21.13 | -4.82 | -23.37 | 487 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.88 | 1.87 | -1.59 | 85 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.01 | 0.01 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 15 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 16 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 17 | Stochastic reversion · 1h | reversion | 100.00 | -0.00 | 56 | 64.3 | -7.60 | -1.55 | -10.60 | 325 |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.06 | 0 | — | -3.61 | -1.76 | -5.14 | 1 |
| 20 | EMA 20/50 cross · 1h | trend | 99.85 | -0.15 | 30 | 6.7 | 7.28 | 1.08 | -17.11 | 139 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.63 | 1.33 | -6.57 | 116 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.47 | -2.90 | 21 |
| 23 | Connors RSI(2) · 1h | reversion | 99.28 | -0.72 | 74 | 44.6 | -11.03 | -3.98 | -14.77 | 217 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 99.23 | -0.77 | 0 | — | 18.30 | 2.78 | -6.29 | 1 |
| 25 | Trend pullback · 1h | trend | 98.81 | -1.19 | 66 | 24.2 | -20.74 | -6.11 | -24.41 | 166 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -0.17 | -0.04 | -4.23 | 102 |
| 27 | Daily: Momentum burst | daily | 98.38 | -1.62 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.71 | -4.92 | -9.35 | 222 |
| 30 | Z-score reversion · 1h | reversion | 98.28 | -1.72 | 23 | 52.2 | 3.80 | 0.92 | -8.60 | 151 |
| 31 | Bollinger reversion · 1h | reversion | 97.94 | -2.06 | 49 | 46.9 | -15.12 | -3.77 | -17.00 | 302 |
| 32 | Copy: Insider buying | copy | 97.94 | -2.06 | 11 | 54.5 | -15.61 | -2.88 | -21.08 | 73 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.47 | -2.53 | 0 | — | -0.63 | -0.16 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.21 | -2.79 | 63 | 28.6 | -3.27 | -0.79 | -10.76 | 279 |
| 35 | ADX DI cross · 1h | trend | 96.78 | -3.22 | 43 | 11.6 | -2.87 | -0.36 | -13.84 | 257 |
| 36 | Supertrend · 1h | trend | 96.70 | -3.30 | 33 | 9.1 | 1.91 | 0.45 | -16.43 | 212 |
| 37 | Agent (ML meta-label) | meta | 96.60 | -3.40 | 265 | 14.7 | 4.79 | 0.97 | -13.45 | 370 |
| 38 | Williams %R · 1h | reversion | 96.40 | -3.60 | 85 | 52.9 | -19.43 | -3.64 | -19.96 | 493 |
| 39 | Parabolic SAR · 1h | trend | 96.36 | -3.64 | 65 | 15.4 | -4.29 | -0.39 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.26 | -3.74 | 71 | 49.3 | 0.59 | 0.26 | -12.41 | 406 |
| 41 | MACD cross · 1h | trend | 95.65 | -4.35 | 90 | 20.0 | -13.03 | -2.10 | -17.27 | 465 |
| 42 | RSI momentum · 1h | momentum | 95.37 | -4.63 | 45 | 2.2 | 0.07 | 0.20 | -16.65 | 229 |
| 43 | MFI reversion · 1h | reversion | 95.06 | -4.94 | 75 | 28.0 | -9.68 | -1.67 | -16.99 | 118 |
| 44 | Squeeze breakout · 1h | breakout | 95.00 | -5.00 | 30 | 20.0 | 15.25 | 2.56 | -8.06 | 107 |
| 45 | Max aggression: 1-day momentum | meta | 94.94 | -5.06 | 7 | 42.9 | -23.54 | -1.22 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.82 | -5.18 | 34 | 14.7 | 2.42 | 0.50 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.50 | -5.50 | 57 | 10.5 | -9.70 | -0.96 | -24.82 | 253 |
| 48 | Bollinger breakout · 1h | breakout | 94.47 | -5.53 | 51 | 23.5 | 7.53 | 1.13 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 7.10 | 1.86 | -6.09 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.43 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.57 | -6.43 | 36 | 11.1 | 6.35 | 1.04 | -12.60 | 132 |
| 52 | EMA 9/21 cross · 1h | trend | 92.58 | -7.42 | 83 | 10.8 | -2.95 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.62 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.30 | -8.71 | 5 | 40.0 | -19.91 | -1.72 | -29.56 | 29 |
| 55 | MACD zero-line · 1h | trend | 91.22 | -8.78 | 50 | 18.0 | -4.53 | -0.41 | -18.32 | 244 |
| 56 | Donchian 20/10 · 1h | breakout | 91.21 | -8.79 | 42 | 14.3 | 2.46 | 0.51 | -16.18 | 223 |
| 57 | Three white soldiers | momentum | 90.87 | -9.13 | 102 | 19.6 | -49.52 | -25.20 | -49.68 | 592 |
| 58 | VWAP momentum · 1h | momentum | 90.65 | -9.35 | 229 | 22.7 | -36.83 | -5.66 | -36.99 | 1266 |
| 59 | OBV trend · 1h | momentum | 90.40 | -9.60 | 109 | 11.9 | -12.67 | -1.42 | -26.73 | 334 |
| 60 | Heikin-Ashi · 1h | trend | 89.91 | -10.09 | 116 | 25.0 | -31.13 | -5.35 | -34.35 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.64 | -10.36 | 30 | 6.7 | -10.61 | -1.23 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.24 | -12.76 | 112 | 16.1 | -9.46 | -1.14 | -23.04 | 416 |
| 63 | RSI(14) reversion | reversion | 85.39 | -14.61 | 226 | 31.9 | -71.73 | -19.66 | -71.98 | 1423 |
| 64 | Squeeze breakout | breakout | 77.21 | -22.79 | 252 | 15.5 | -62.48 | -19.06 | -62.60 | 1226 |
| 65 | VWAP reversion | reversion | 77.12 | -22.88 | 279 | 28.3 | -69.01 | -16.22 | -69.17 | 1377 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.95 | -17.84 | -73.95 | 1660 |
| 67 | Donchian 55/20 | breakout | 75.88 | -24.12 | 260 | 17.3 | -68.98 | -15.35 | -68.98 | 1305 |
| 68 | EMA 20/50 cross | trend | 74.08 | -25.92 | 268 | 18.3 | -78.55 | -16.26 | -78.55 | 1477 |
| 69 | Volume breakout | breakout | 73.30 | -26.70 | 212 | 12.3 | -65.66 | -19.58 | -65.66 | 928 |
| 70 | Z-score reversion | reversion | 70.76 | -29.24 | 359 | 27.3 | -84.92 | -25.29 | -84.92 | 2037 |
| 71 | MFI reversion | reversion | 69.64 | -30.36 | 358 | 20.9 | -87.11 | -30.62 | -87.11 | 2105 |
| 72 | Supertrend | trend | 69.03 | -30.97 | 362 | 19.9 | -87.20 | -22.47 | -87.22 | 1927 |
| 73 | Keltner breakout | breakout | 67.73 | -32.27 | 351 | 13.1 | -85.52 | -30.59 | -85.54 | 1886 |
| 74 | AI bee: Bizzy | ai | 67.08 | -32.92 | 615 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 66.52 | -33.48 | 322 | 9.0 | -82.29 | -24.96 | -82.30 | 1769 |
| 76 | AI bee: Boozy | ai | 65.97 | -34.03 | 219 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.19 | -35.81 | 404 | 9.2 | -89.65 | -37.28 | -89.66 | 2100 |
| 78 | MACD zero-line | trend | 62.57 | -37.43 | 459 | 15.3 | -91.57 | -31.17 | -91.58 | 2364 |
| 79 | Donchian 20/10 | breakout | 62.09 | -37.91 | 496 | 17.9 | -91.14 | -27.68 | -91.16 | 2667 |
| 80 | RSI momentum | momentum | 61.20 | -38.80 | 461 | 16.7 | -90.73 | -27.01 | -90.74 | 2384 |
| 81 | Trend pullback | trend | 59.91 | -40.09 | 493 | 15.4 | -91.46 | -30.75 | -91.46 | 2348 |
| 82 | Triple EMA stack | trend | 59.67 | -40.33 | 513 | 15.2 | -93.43 | -32.69 | -93.43 | 2634 |
| 83 | Bollinger breakout | breakout | 58.78 | -41.22 | 505 | 13.9 | -94.02 | -35.82 | -94.03 | 2824 |
| 84 | Stochastic reversion | reversion | 57.43 | -42.57 | 727 | 23.1 | -95.55 | -37.23 | -95.55 | 4040 |
| 85 | Bollinger reversion | reversion | 56.92 | -43.08 | 670 | 17.8 | -95.67 | -36.35 | -95.67 | 3677 |
| 86 | Consensus | meta | 56.90 | -43.10 | 492 | 10.0 | -94.68 | -27.31 | -94.68 | 2718 |
| 87 | EMA 9/21 cross | trend | 54.86 | -45.14 | 634 | 16.2 | -97.44 | -35.60 | -97.44 | 3551 |
| 88 | Connors RSI(2) | reversion | 53.60 | -46.40 | 681 | 20.1 | -96.59 | -35.41 | -96.59 | 3641 |
| 89 | OBV trend | momentum | 51.79 | -48.21 | 742 | 14.7 | -96.45 | -40.06 | -96.45 | 3606 |
| 90 | CCI reversion ⏸ | reversion | 51.31 | -48.69 | 705 | 17.2 | -98.45 | -40.35 | -98.45 | 4689 |
| 91 | Candlestick reversal ⏸ | reversion | 50.65 | -49.35 | 803 | 14.9 | -99.29 | -39.64 | -99.29 | 5615 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -31.92 | -98.69 | 5355 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -46.75 | -99.73 | 6132 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -42.57 | -97.42 | 3686 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -43.88 | -99.51 | 6095 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.31 | -99.90 | 8245 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T23:55 | Consensus | buy | SOL-USD | 14.23 | — | entry |
| 2026-10-06T23:55 | MFI reversion | buy | SOL-USD | 17.42 | — | entry signal |
| 2026-10-06T23:50 | Three white soldiers | buy | BTC-USD | 22.74 | — | entry signal |
| 2026-10-06T23:50 | Bollinger breakout | buy | ETH-USD | 14.71 | — | entry signal |
| 2026-10-06T23:45 | Stochastic reversion | sell | BTC-USD | 14.35 | -0.08 | exit signal |
| 2026-10-06T23:45 | Z-score reversion | buy | XRP-USD | 17.72 | — | entry signal |
| 2026-10-06T23:45 | Z-score reversion | sell | BTC-USD | 17.63 | -0.09 | exit signal |
| 2026-10-06T23:45 | Bollinger reversion | sell | BTC-USD | 14.18 | -0.07 | exit signal |
| 2026-10-06T23:45 | Keltner breakout | buy | DOGE-USD | 16.95 | — | entry signal |
| 2026-10-06T23:45 | MACD zero-line | buy | DOGE-USD | 15.65 | — | entry signal |
| 2026-10-06T23:44 | AI bee: Bizzy | sell | DOGE-USD | 9.50 | -0.04 | Jev: sell (sell p=0.51) after 14 min |
| 2026-10-06T23:40 | Z-score reversion | buy | BTC-USD | 17.73 | — | entry signal |
| 2026-10-06T23:40 | Bollinger reversion | buy | XRP-USD | 14.25 | — | entry signal |
| 2026-10-06T23:40 | Bollinger reversion | buy | BTC-USD | 14.25 | — | entry signal |
| 2026-10-06T23:40 | Squeeze breakout | buy | DOGE-USD | 19.31 | — | entry signal |
| 2026-10-06T23:40 | Bollinger breakout | buy | DOGE-USD | 14.72 | — | entry signal |
| 2026-10-06T23:40 | Donchian 20/10 | buy | DOGE-USD | 15.53 | — | entry signal |
| 2026-10-06T23:40 | RSI momentum | buy | DOGE-USD | 15.31 | — | entry signal |
| 2026-10-06T23:40 | Supertrend | buy | DOGE-USD | 17.27 | — | entry signal |
| 2026-10-06T23:40 | Triple EMA stack | buy | ETH-USD | 14.93 | — | entry signal |
| 2026-10-06T23:40 | EMA 9/21 cross | buy | ETH-USD | 13.73 | — | entry signal |
| 2026-10-06T23:40 | EMA 9/21 cross | buy | DOGE-USD | 13.73 | — | entry signal |
| 2026-10-06T23:37 | AI bee: Bizzy | sell | XRP-USD | 9.19 | -0.08 | Jev: sell (sell p=0.92) after 12 min |
| 2026-10-06T23:35 | CCI reversion | sell | XRP-USD | 12.75 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-06T23:35 | CCI reversion | sell | ETH-USD | 12.82 | -0.09 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-06T23:35 | CCI reversion | sell | BTC-USD | 12.82 | -0.10 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-06T23:35 | Stochastic reversion | sell | SOL-USD | 14.31 | -0.13 | stop-loss |
| 2026-10-06T23:35 | RSI momentum | sell | ETH-USD | 15.28 | -0.11 | exit signal |
| 2026-10-06T23:35 | Triple EMA stack | sell | ETH-USD | 14.85 | -0.11 | stop-loss |
| 2026-10-06T23:35 | EMA 9/21 cross | sell | ETH-USD | 13.66 | -0.10 | exit signal |
| 2026-10-06T23:30 | AI bee: Bizzy | buy | DOGE-USD | 9.54 | — | Jev: buy (buy p=0.57) |
| 2026-10-06T23:30 | CCI reversion | sell | DOGE-USD | 12.92 | -0.10 | exit signal |
| 2026-10-06T23:30 | Stochastic reversion | sell | ETH-USD | 14.37 | -0.08 | exit signal |
| 2026-10-06T23:30 | ADX DI cross | buy | DOGE-USD | 16.05 | — | entry signal |
| 2026-10-06T23:25 | AI bee: Bizzy | buy | XRP-USD | 9.27 | — | Jev: buy (buy p=0.55) |
| 2026-10-06T23:25 | CCI reversion | buy | XRP-USD | 12.86 | — | entry signal |
| 2026-10-06T23:25 | Stochastic reversion | buy | BTC-USD | 14.43 | — | entry |
| 2026-10-06T23:25 | Stochastic reversion | sell | XRP-USD | 14.38 | -0.09 | exit signal |
| 2026-10-06T23:25 | Stochastic reversion | sell | DOGE-USD | 14.38 | -0.10 | exit signal |
| 2026-10-06T23:25 | Bollinger reversion | buy | SOL-USD | 14.27 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 23:55:05.000165+00:00 -> 2026-10-07 00:05:05.000165+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
