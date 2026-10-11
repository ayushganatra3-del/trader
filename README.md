# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T12:25:05.000137+00:00 · 19042 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 8835 decisions in 1767 calls, $0.1236 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T12:25 | 0 / 1 / 4 | XRP-USD 14%, NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T12:25 | 2 / 2 / 1 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.44 | -2.26 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -15.29 | -2.51 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.16 | 2.41 | -1.64 | 87 |
| 17 | Hold BTC | benchmark | 99.33 | -0.67 | 0 | — | 27.64 | 3.31 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.41 | -1.80 | -14.61 | 340 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.68 | -6.37 | -25.39 | 171 |
| 27 | EMA 20/50 cross · 1h | trend | 96.71 | -3.29 | 39 | 12.8 | 4.98 | 0.77 | -19.85 | 136 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -5.57 | -2.00 | -8.33 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.63 | -0.09 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.82 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 33 | MACD cross · 1h | trend | 95.79 | -4.21 | 113 | 23.9 | -14.99 | -2.40 | -17.27 | 464 |
| 34 | Supertrend · 1h | trend | 95.10 | -4.90 | 53 | 13.2 | 0.16 | 0.21 | -18.22 | 209 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.90 | -2.25 | -6.77 | 103 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.96 | 2.05 | -6.38 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.85 | -6.15 | 37 | 24.3 | 23.27 | 3.18 | -8.95 | 108 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.49 | -1.65 | -17.79 | 126 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.84 | -0.51 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.84 | -0.54 | -13.20 | 426 |
| 42 | Ichimoku · 1h | trend | 92.81 | -7.19 | 42 | 19.0 | -0.09 | 0.19 | -20.11 | 120 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 5.04 | 0.81 | -17.07 | 220 |
| 44 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 45 | Bollinger reversion · 1h | reversion | 92.51 | -7.49 | 76 | 36.8 | -20.74 | -4.95 | -23.13 | 317 |
| 46 | Bollinger breakout · 1h | breakout | 91.61 | -8.39 | 70 | 28.6 | 5.97 | 0.93 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.15 | -8.85 | 123 | 46.3 | -24.18 | -4.17 | -26.91 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.47 | -0.84 | -26.38 | 237 |
| 50 | Candlestick reversal · 1h | reversion | 90.14 | -9.86 | 116 | 31.9 | -26.71 | -5.22 | -28.49 | 513 |
| 51 | CCI reversion · 1h | reversion | 89.58 | -10.42 | 101 | 44.6 | -8.10 | -1.04 | -14.35 | 417 |
| 52 | VWAP momentum · 1h | momentum | 89.46 | -10.54 | 283 | 21.9 | -33.65 | -5.06 | -39.28 | 1282 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.84 | -11.15 | 64 | 18.8 | -6.90 | -0.75 | -19.96 | 240 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.89 | -1.48 | -28.63 | 321 |
| 56 | Donchian 20/10 · 1h | breakout | 88.74 | -11.26 | 59 | 18.6 | -0.68 | 0.12 | -17.72 | 224 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.41 | -5.10 | -36.59 | 700 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.80 | -12.20 | 103 | 13.6 | -9.59 | -1.10 | -21.58 | 338 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.08 | -23.35 | -48.10 | 591 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.93 | -1.34 | -24.12 | 412 |
| 63 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.71 | -16.57 | -73.82 | 1670 |
| 64 | RSI(14) reversion | reversion | 73.91 | -26.09 | 369 | 27.6 | -72.97 | -18.46 | -72.97 | 1499 |
| 65 | Squeeze breakout | breakout | 70.75 | -29.25 | 327 | 14.7 | -62.45 | -18.45 | -62.46 | 1231 |
| 66 | Donchian 55/20 | breakout | 70.23 | -29.77 | 331 | 17.8 | -67.54 | -14.45 | -67.54 | 1292 |
| 67 | Volume breakout | breakout | 70.06 | -29.94 | 262 | 13.0 | -62.68 | -18.10 | -62.70 | 901 |
| 68 | EMA 20/50 cross | trend | 69.58 | -30.42 | 331 | 19.6 | -77.13 | -15.44 | -77.13 | 1460 |
| 69 | VWAP reversion | reversion | 67.82 | -32.18 | 402 | 25.9 | -71.71 | -16.17 | -71.74 | 1441 |
| 70 | Supertrend | trend | 63.51 | -36.49 | 461 | 19.7 | -86.22 | -21.39 | -86.22 | 1918 |
| 71 | Keltner breakout | breakout | 62.60 | -37.41 | 446 | 14.3 | -83.72 | -27.79 | -83.72 | 1849 |
| 72 | AI bee: Boozy | ai | 60.38 | -39.62 | 255 | 5.1 | — | — | — | — |
| 73 | Ichimoku | trend | 60.14 | -39.86 | 405 | 9.6 | -81.72 | -23.44 | -81.72 | 1747 |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.38 | -23.37 | -85.38 | 2084 |
| 75 | MFI reversion | reversion | 59.15 | -40.84 | 514 | 21.2 | -87.61 | -28.81 | -87.61 | 2120 |
| 76 | AI bee: Bizzy | ai | 57.87 | -42.13 | 832 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.36 | -43.64 | 543 | 10.1 | -89.40 | -35.75 | -89.40 | 2124 |
| 78 | Trend pullback | trend | 55.26 | -44.74 | 583 | 14.9 | -90.99 | -27.07 | -90.99 | 2338 |
| 79 | Donchian 20/10 | breakout | 55.01 | -44.99 | 634 | 18.0 | -90.85 | -26.46 | -90.85 | 2669 |
| 80 | RSI momentum | momentum | 53.87 | -46.13 | 605 | 16.9 | -90.35 | -25.98 | -90.35 | 2386 |
| 81 | Triple EMA stack | trend | 53.14 | -46.86 | 625 | 15.4 | -93.17 | -30.36 | -93.17 | 2618 |
| 82 | MACD zero-line | trend | 53.10 | -46.90 | 589 | 14.6 | -91.56 | -30.62 | -91.56 | 2369 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -31.72 | -98.68 | 5412 |
| 84 | Bollinger breakout | breakout | 50.46 | -49.54 | 667 | 14.1 | -93.54 | -33.57 | -93.54 | 2821 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -34.31 | -97.39 | 3554 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.41 | -36.19 | -96.41 | 3609 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -26.12 | -94.27 | 2688 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -38.12 | -99.35 | 5702 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -32.00 | -96.38 | 3624 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.54 | -99.73 | 6211 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -38.20 | -97.34 | 3682 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -38.27 | -98.47 | 4717 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.37 | -99.52 | 6155 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -34.48 | -95.88 | 3749 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.61 | -35.20 | -95.61 | 4088 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.68 | -99.90 | 8320 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T12:25 | Volume breakout | sell | BTC-USD | 17.44 | -0.11 | exit signal |
| 2026-10-11T12:20 | Triple EMA stack | buy | XRP-USD | 2.70 | — | entry signal |
| 2026-10-11T12:20 | Triple EMA stack | sell | BTC-USD | 2.65 | -0.02 | rebalance down |
| 2026-10-11T12:17 | AI bee: Bizzy | buy | XRP-USD | 8.33 | — | Jev: buy (buy p=0.58) |
| 2026-10-11T12:17 | EMA 20/50 cross | buy | XRP-USD | 3.47 | — | rebalance up |
| 2026-10-11T12:17 | EMA 20/50 cross | sell | SOL-USD | 3.47 | -0.02 | rebalance down |
| 2026-10-11T12:15 | Triple EMA stack | buy | DOGE-USD | 13.31 | — | entry signal |
| 2026-10-11T12:15 | EMA 20/50 cross | buy | XRP-USD | 3.54 | — | entry signal |
| 2026-10-11T12:15 | EMA 20/50 cross | sell | BTC-USD | 3.48 | -0.02 | rebalance down |
| 2026-10-11T12:12 | AI bee: Boozy | sell | ETH-USD | 14.62 | -0.09 | Jev: buy |
| 2026-10-11T12:10 | MACD zero-line | buy | XRP-USD | 2.65 | — | rebalance up |
| 2026-10-11T12:10 | MACD zero-line | sell | SOL-USD | 2.65 | -0.01 | rebalance down |
| 2026-10-11T12:10 | EMA 20/50 cross | buy | DOGE-USD | 17.44 | — | entry signal |
| 2026-10-11T12:07 | AI bee: Bizzy | sell | BTC-USD | 8.61 | -0.04 | Jev: sell (sell p=0.51) after 14 min |
| 2026-10-11T12:03 | AI bee: Bizzy | sell | SOL-USD | 8.89 | -0.05 | Jev: sell (sell p=0.67) after 13 min |
| 2026-10-11T12:00 | CCI reversion · 1h | buy | ETH-USD | 5.60 | — | entry signal |
| 2026-10-11T12:00 | VWAP momentum · 1h | buy | BTC-USD | 6.39 | — | entry signal |
| 2026-10-11T12:00 | Triple EMA stack | buy | SOL-USD | 13.31 | — | entry signal |
| 2026-10-11T11:59 | Keltner breakout | sell | DOGE-USD | 3.13 | -0.02 | rebalance down |
| 2026-10-11T11:57 | Keltner breakout | buy | SOL-USD | 6.26 | — | rebalance up |
| 2026-10-11T11:57 | Keltner breakout | sell | XRP-USD | 3.13 | -0.02 | rebalance down |
| 2026-10-11T11:57 | Keltner breakout | sell | BTC-USD | 3.13 | -0.02 | rebalance down |
| 2026-10-11T11:55 | AI bee: Boozy | buy | ETH-USD | 14.71 | — | Jev: buy (buy p=0.77) |
| 2026-10-11T11:55 | VWAP reversion | sell | XRP-USD | 16.93 | -0.03 | exit signal |
| 2026-10-11T11:55 | Keltner breakout | buy | SOL-USD | 3.17 | — | entry signal |
| 2026-10-11T11:55 | Keltner breakout | buy | ETH-USD | 12.55 | — | entry signal |
| 2026-10-11T11:55 | Donchian 55/20 | buy | ETH-USD | 17.57 | — | entry signal |
| 2026-10-11T11:55 | Ichimoku | sell | DOGE-USD | 14.98 | -0.09 | target is flat |
| 2026-10-11T11:55 | MACD zero-line | buy | XRP-USD | 5.35 | — | entry signal |
| 2026-10-11T11:55 | MACD zero-line | sell | ETH-USD | 2.66 | -0.01 | rebalance down |
| 2026-10-11T11:55 | MACD zero-line | sell | BTC-USD | 2.65 | -0.01 | rebalance down |
| 2026-10-11T11:55 | Triple EMA stack | buy | ETH-USD | 13.33 | — | entry signal |
| 2026-10-11T11:55 | EMA 20/50 cross | buy | SOL-USD | 17.46 | — | entry signal |
| 2026-10-11T11:55 | EMA 20/50 cross | buy | ETH-USD | 17.46 | — | entry signal |
| 2026-10-11T11:53 | AI bee: Bizzy | buy | BTC-USD | 8.65 | — | Jev: buy (buy p=0.60) |
| 2026-10-11T11:52 | RSI momentum | sell | BTC-USD | 2.70 | -0.01 | rebalance down |
| 2026-10-11T11:52 | Supertrend | sell | BTC-USD | 3.18 | -0.02 | rebalance down |
| 2026-10-11T11:50 | AI bee: Bizzy | buy | SOL-USD | 8.94 | — | Jev: buy (buy p=0.62) |
| 2026-10-11T11:50 | MFI reversion | sell | XRP-USD | 14.76 | -0.03 | exit signal |
| 2026-10-11T11:50 | Z-score reversion | sell | XRP-USD | 14.82 | -0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 12:25:05.000137+00:00 -> 2026-10-11 12:35:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
