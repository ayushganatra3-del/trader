# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T13:55:05.000133+00:00 · 17964 ticks

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
| Copy: Insider buying | 2026-10-10 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 10492 decisions in 2099 calls, $0.1466 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T13:55 | 1 / 1 / 3 | SOL-USD 15%, XRP-USD 14%, NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T13:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T13:55 | 4 / 0 / 1 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| MFI reversion | AAPL | 1.96 | +0.72% | 7 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -13.60 | -2.18 | -22.02 | 69 |
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
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.33 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.17 | -0.82 | 89 | 55.1 | -10.63 | -2.07 | -14.61 | 344 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.98 | -1.02 | 0 | — | 26.52 | 3.19 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.66 | -1.34 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.25 | -2.75 | 41 | 43.9 | 1.98 | 0.52 | -8.60 | 161 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 5.72 | 0.84 | -19.85 | 132 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.51 | -0.07 | -13.84 | 256 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.78 | -0.20 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.83 | -5.49 | -10.38 | 243 |
| 33 | MACD cross · 1h | trend | 95.84 | -4.16 | 109 | 23.9 | -16.73 | -2.72 | -18.31 | 472 |
| 34 | Supertrend · 1h | trend | 95.22 | -4.78 | 52 | 13.5 | -0.18 | 0.17 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.09 | -5.91 | 35 | 25.7 | 24.03 | 3.27 | -8.76 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.68 | -2.56 | -7.39 | 112 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.95 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.37 | -1.80 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.24 | -0.38 | -9.03 | 148 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.70 | -0.85 | -13.43 | 408 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.36 | 0.61 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.66 | 1.20 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.82 | -8.18 | 67 | 29.9 | 6.47 | 0.99 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.76 | -8.24 | 120 | 47.5 | -24.48 | -4.22 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.28 | -0.81 | -26.38 | 234 |
| 50 | Candlestick reversal · 1h | reversion | 90.26 | -9.74 | 114 | 30.7 | -26.94 | -5.32 | -28.78 | 514 |
| 51 | CCI reversion · 1h | reversion | 89.76 | -10.24 | 99 | 44.4 | -8.59 | -1.11 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.69 | -10.31 | 278 | 22.3 | -34.58 | -5.22 | -39.24 | 1281 |
| 53 | MACD zero-line · 1h | trend | 89.19 | -10.81 | 61 | 19.7 | -6.56 | -0.70 | -19.70 | 241 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Donchian 20/10 · 1h | breakout | 88.83 | -11.17 | 58 | 19.0 | -0.08 | 0.20 | -17.72 | 221 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.89 | -1.34 | -28.66 | 318 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.36 | -5.28 | -36.59 | 704 |
| 58 | Three white soldiers | momentum | 88.31 | -11.69 | 134 | 18.7 | -47.86 | -23.36 | -47.87 | 589 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.84 | -12.16 | 101 | 13.9 | -9.22 | -1.04 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.71 | -1.31 | -24.12 | 409 |
| 63 | RSI(14) reversion | reversion | 75.28 | -24.72 | 355 | 28.7 | -72.89 | -18.29 | -72.97 | 1497 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -72.87 | -16.69 | -73.76 | 1670 |
| 65 | Squeeze breakout | breakout | 72.65 | -27.35 | 310 | 15.5 | -62.08 | -18.51 | -62.08 | 1226 |
| 66 | Donchian 55/20 | breakout | 71.77 | -28.23 | 319 | 18.5 | -67.58 | -14.52 | -67.67 | 1291 |
| 67 | EMA 20/50 cross | trend | 71.57 | -28.43 | 315 | 20.6 | -77.34 | -15.46 | -77.35 | 1461 |
| 68 | Volume breakout | breakout | 70.99 | -29.01 | 254 | 13.4 | -62.84 | -18.26 | -62.85 | 898 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.43 | -16.47 | -72.57 | 1446 |
| 70 | Supertrend | trend | 65.62 | -34.38 | 443 | 20.5 | -86.35 | -21.24 | -86.36 | 1919 |
| 71 | Keltner breakout | breakout | 64.17 | -35.83 | 433 | 14.8 | -83.98 | -28.35 | -83.98 | 1852 |
| 72 | Z-score reversion | reversion | 61.19 | -38.81 | 486 | 23.5 | -85.78 | -23.63 | -85.78 | 2097 |
| 73 | Ichimoku | trend | 61.02 | -38.98 | 397 | 9.8 | -81.74 | -23.52 | -81.74 | 1747 |
| 74 | AI bee: Boozy | ai | 60.87 | -39.13 | 250 | 5.2 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.61 | -39.39 | 496 | 21.8 | -87.64 | -28.44 | -87.64 | 2124 |
| 76 | AI bee: Bizzy | ai | 59.73 | -40.27 | 796 | 9.2 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.03 | -41.97 | 526 | 10.5 | -89.54 | -34.80 | -89.54 | 2129 |
| 78 | Donchian 20/10 | breakout | 57.33 | -42.67 | 611 | 18.7 | -90.87 | -26.57 | -90.87 | 2667 |
| 79 | RSI momentum | momentum | 56.57 | -43.43 | 578 | 17.6 | -90.36 | -26.06 | -90.36 | 2382 |
| 80 | Trend pullback | trend | 56.46 | -43.54 | 568 | 15.3 | -90.71 | -27.58 | -90.71 | 2319 |
| 81 | MACD zero-line | trend | 56.05 | -43.95 | 559 | 15.4 | -91.60 | -30.12 | -91.60 | 2366 |
| 82 | Triple EMA stack | trend | 55.07 | -44.94 | 604 | 15.9 | -93.20 | -31.06 | -93.21 | 2617 |
| 83 | Bollinger breakout | breakout | 52.82 | -47.18 | 640 | 14.7 | -93.55 | -33.87 | -93.55 | 2819 |
| 84 | Consensus | meta | 51.57 | -48.43 | 604 | 10.1 | -94.22 | -26.02 | -94.22 | 2684 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -31.18 | -98.71 | 5416 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -33.88 | -97.39 | 3550 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -37.64 | -96.46 | 3610 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.77 | -99.36 | 5704 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.27 | -32.18 | -96.27 | 3604 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -43.41 | -99.74 | 6210 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.20 | -97.35 | 3681 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.90 | -98.48 | 4717 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.95 | -99.51 | 6149 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -34.12 | -95.87 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.60 | -35.26 | -95.60 | 4086 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.72 | -99.90 | 8336 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T13:55 | Three white soldiers | sell | DOGE-USD | 21.97 | -0.15 | exit signal |
| 2026-10-10T13:55 | Trend pullback | sell | BTC-USD | 14.05 | -0.09 | exit signal |
| 2026-10-10T13:52 | AI bee: Bizzy | buy | XRP-USD | 8.58 | — | Jev: buy (buy p=0.57) |
| 2026-10-10T13:50 | Z-score reversion | sell | XRP-USD | 15.28 | -0.07 | exit signal |
| 2026-10-10T13:50 | RSI(14) reversion | sell | XRP-USD | 18.81 | -0.07 | exit signal |
| 2026-10-10T13:50 | Squeeze breakout | buy | XRP-USD | 18.19 | — | entry signal |
| 2026-10-10T13:50 | Squeeze breakout | buy | SOL-USD | 18.19 | — | entry signal |
| 2026-10-10T13:50 | Bollinger breakout | buy | XRP-USD | 13.23 | — | entry signal |
| 2026-10-10T13:50 | Bollinger breakout | buy | SOL-USD | 13.23 | — | entry signal |
| 2026-10-10T13:50 | Donchian 20/10 | buy | XRP-USD | 14.36 | — | entry signal |
| 2026-10-10T13:50 | Donchian 20/10 | buy | SOL-USD | 14.36 | — | entry signal |
| 2026-10-10T13:50 | RSI momentum | buy | XRP-USD | 14.16 | — | entry signal |
| 2026-10-10T13:50 | Trend pullback | buy | BTC-USD | 14.14 | — | entry signal |
| 2026-10-10T13:50 | MACD zero-line | buy | XRP-USD | 14.03 | — | entry signal |
| 2026-10-10T13:48 | AI bee: Bizzy | buy | SOL-USD | 9.10 | — | Jev: buy (buy p=0.61) |
| 2026-10-10T13:45 | Trend pullback | buy | SOL-USD | 14.14 | — | entry signal |
| 2026-10-10T13:45 | MACD zero-line | buy | DOGE-USD | 14.03 | — | entry |
| 2026-10-10T13:40 | AI bee: Boozy | sell | ETH-USD | 15.11 | -0.10 | Jev: sell |
| 2026-10-10T13:40 | Trend pullback | sell | BTC-USD | 14.08 | -0.09 | exit signal |
| 2026-10-10T13:40 | Triple EMA stack | sell | BTC-USD | 13.70 | -0.09 | exit signal |
| 2026-10-10T13:35 | Squeeze breakout | buy | ETH-USD | 18.21 | — | entry signal |
| 2026-10-10T13:34 | AI bee: Bizzy | sell | ETH-USD | 9.01 | -0.05 | Jev: sell (sell p=0.60) after 10 min |
| 2026-10-10T13:30 | Z-score reversion | sell | DOGE-USD | 15.27 | -0.08 | exit signal |
| 2026-10-10T13:30 | Three white soldiers | buy | DOGE-USD | 22.11 | — | entry signal |
| 2026-10-10T13:30 | Bollinger breakout | buy | ETH-USD | 13.24 | — | entry signal |
| 2026-10-10T13:30 | Triple EMA stack | buy | BTC-USD | 13.79 | — | entry signal |
| 2026-10-10T13:25 | RSI momentum | buy | SOL-USD | 14.16 | — | entry signal |
| 2026-10-10T13:25 | Triple EMA stack | buy | SOL-USD | 13.80 | — | entry signal |
| 2026-10-10T13:25 | EMA 20/50 cross | buy | SOL-USD | 17.90 | — | entry signal |
| 2026-10-10T13:24 | AI bee: Boozy | buy | ETH-USD | 15.22 | — | Jev: buy (buy p=0.75) |
| 2026-10-10T13:24 | AI bee: Bizzy | buy | ETH-USD | 9.06 | — | Jev: buy (buy p=0.61) |
| 2026-10-10T13:20 | Trend pullback | buy | ETH-USD | 14.17 | — | entry signal |
| 2026-10-10T13:20 | Trend pullback | buy | BTC-USD | 14.17 | — | entry signal |
| 2026-10-10T13:20 | Triple EMA stack | buy | ETH-USD | 13.81 | — | entry signal |
| 2026-10-10T13:16 | AI bee: Bizzy | sell | SOL-USD | 9.53 | -0.06 | Jev: sell (sell p=0.57) after 10 min |
| 2026-10-10T13:15 | Trend pullback | sell | ETH-USD | 14.15 | -0.10 | exit signal |
| 2026-10-10T13:15 | Triple EMA stack | sell | ETH-USD | 13.76 | -0.09 | exit signal |
| 2026-10-10T13:06 | AI bee: Bizzy | buy | SOL-USD | 9.60 | — | Jev: buy (buy p=0.64) |
| 2026-10-10T13:00 | MACD zero-line · 1h | buy | ETH-USD | 17.83 | — | rebalance up |
| 2026-10-10T13:00 | MACD zero-line · 1h | sell | DOGE-USD | 22.12 | -0.22 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 13:55:05.000133+00:00 -> 2026-10-10 14:05:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
