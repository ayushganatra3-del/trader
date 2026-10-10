# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T11:25:05.000125+00:00 · 17833 ticks

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

Today: 8527 decisions in 1706 calls, $0.1192 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T11:25 | 3 / 2 / 0 | NANC 17%, COIN 14% |  |
| Breezy | 2026-10-10T11:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T11:25 | 4 / 1 / 0 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |
| Bollinger reversion | TECL | 1.82 | +2.00% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.79 | -2.38 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -13.59 | -2.18 | -22.02 | 69 |
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
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.31 | 2.48 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.33 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -10.64 | -2.07 | -14.61 | 344 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.95 | -1.05 | 0 | — | 27.12 | 3.26 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 41 | 43.9 | 1.93 | 0.51 | -8.60 | 161 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 5.46 | 0.82 | -19.85 | 133 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.02 | 0.10 | -10.13 | 256 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.52 | -0.07 | -13.84 | 256 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.87 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.82 | -4.18 | 108 | 23.1 | -16.77 | -2.72 | -18.33 | 472 |
| 34 | Supertrend · 1h | trend | 95.16 | -4.84 | 52 | 13.5 | -0.25 | 0.16 | -18.22 | 211 |
| 35 | Squeeze breakout · 1h | breakout | 94.08 | -5.92 | 35 | 25.7 | 24.01 | 3.27 | -8.76 | 106 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.65 | 1.97 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.43 | -1.96 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.44 | -0.43 | -9.03 | 150 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.57 | -0.52 | -12.99 | 410 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.80 | -4.97 | -23.49 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.30 | 0.60 | -17.07 | 223 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 121 |
| 46 | Bollinger breakout · 1h | breakout | 91.81 | -8.19 | 67 | 29.9 | 6.46 | 0.99 | -12.90 | 285 |
| 47 | Williams %R · 1h | reversion | 91.76 | -8.24 | 120 | 47.5 | -24.46 | -4.22 | -26.91 | 511 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.70 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.24 | -9.76 | 114 | 30.7 | -27.50 | -5.43 | -29.30 | 519 |
| 51 | CCI reversion · 1h | reversion | 89.75 | -10.25 | 99 | 44.4 | -8.63 | -1.12 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.68 | -10.32 | 278 | 22.3 | -34.92 | -5.26 | -39.28 | 1282 |
| 53 | MACD zero-line · 1h | trend | 89.27 | -10.73 | 60 | 20.0 | -6.45 | -0.69 | -19.59 | 240 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Donchian 20/10 · 1h | breakout | 88.82 | -11.18 | 58 | 19.0 | -0.10 | 0.19 | -17.72 | 221 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.76 | -1.32 | -28.47 | 316 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.35 | -5.28 | -36.60 | 704 |
| 58 | Three white soldiers | momentum | 88.46 | -11.54 | 133 | 18.8 | -48.02 | -23.59 | -48.02 | 589 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.83 | -12.17 | 101 | 13.9 | -8.98 | -1.01 | -21.49 | 336 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.35 | -24.65 | 352 | 29.0 | -72.84 | -18.24 | -72.94 | 1496 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.04 | -16.74 | -73.92 | 1666 |
| 65 | Squeeze breakout | breakout | 73.07 | -26.93 | 308 | 15.6 | -61.90 | -18.43 | -61.90 | 1222 |
| 66 | Donchian 55/20 | breakout | 71.90 | -28.10 | 318 | 18.6 | -67.67 | -14.55 | -67.82 | 1292 |
| 67 | EMA 20/50 cross | trend | 71.70 | -28.30 | 314 | 20.7 | -77.30 | -15.44 | -77.30 | 1459 |
| 68 | Volume breakout | breakout | 71.11 | -28.89 | 253 | 13.4 | -63.24 | -18.44 | -63.24 | 902 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.04 | -16.32 | -72.18 | 1440 |
| 70 | Supertrend | trend | 65.75 | -34.25 | 442 | 20.6 | -86.32 | -21.20 | -86.35 | 1918 |
| 71 | Keltner breakout | breakout | 64.52 | -35.48 | 430 | 14.9 | -84.03 | -28.35 | -84.09 | 1855 |
| 72 | Z-score reversion | reversion | 61.25 | -38.75 | 483 | 23.6 | -85.76 | -23.60 | -85.77 | 2097 |
| 73 | Ichimoku | trend | 61.12 | -38.88 | 396 | 9.8 | -81.77 | -23.60 | -81.77 | 1748 |
| 74 | AI bee: Boozy | ai | 61.06 | -38.94 | 248 | 5.2 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.71 | -39.28 | 493 | 21.9 | -87.69 | -28.59 | -87.69 | 2120 |
| 76 | AI bee: Bizzy | ai | 60.15 | -39.85 | 789 | 9.3 | — | — | — | — |
| 77 | ADX DI cross | trend | 58.14 | -41.86 | 525 | 10.5 | -89.52 | -34.71 | -89.52 | 2128 |
| 78 | Donchian 20/10 | breakout | 57.68 | -42.32 | 609 | 18.7 | -90.81 | -26.45 | -90.82 | 2664 |
| 79 | Trend pullback | trend | 56.98 | -43.02 | 563 | 15.5 | -90.62 | -27.54 | -90.62 | 2312 |
| 80 | RSI momentum | momentum | 56.90 | -43.10 | 576 | 17.7 | -90.39 | -26.13 | -90.39 | 2382 |
| 81 | MACD zero-line | trend | 56.36 | -43.64 | 557 | 15.4 | -91.55 | -29.97 | -91.55 | 2361 |
| 82 | Triple EMA stack | trend | 55.42 | -44.58 | 601 | 16.0 | -93.23 | -31.25 | -93.23 | 2618 |
| 83 | Bollinger breakout | breakout | 53.23 | -46.77 | 637 | 14.8 | -93.54 | -33.89 | -93.54 | 2819 |
| 84 | Consensus | meta | 51.75 | -48.25 | 602 | 10.1 | -94.20 | -25.97 | -94.20 | 2684 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.83 | -98.69 | 5389 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.69 | -97.37 | 3542 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -37.84 | -96.49 | 3615 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.40 | -99.34 | 5689 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.24 | -32.08 | -96.24 | 3599 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.25 | -99.73 | 6206 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.40 | -97.35 | 3681 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.76 | -98.47 | 4715 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.82 | -99.51 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -34.11 | -95.87 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.58 | -35.16 | -95.59 | 4085 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.75 | -99.90 | 8341 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T11:25 | Ichimoku | sell | ETH-USD | 15.21 | -0.09 | exit signal |
| 2026-10-10T11:20 | MFI reversion | buy | DOGE-USD | 15.19 | — | entry signal |
| 2026-10-10T11:20 | Ichimoku | buy | ETH-USD | 15.30 | — | entry signal |
| 2026-10-10T11:15 | Trend pullback | sell | ETH-USD | 14.20 | -0.09 | exit signal |
| 2026-10-10T11:15 | Trend pullback | sell | BTC-USD | 14.19 | -0.09 | exit signal |
| 2026-10-10T11:15 | ADX DI cross | sell | XRP-USD | 14.46 | -0.11 | exit signal |
| 2026-10-10T11:15 | Triple EMA stack | sell | ETH-USD | 13.81 | -0.09 | exit signal |
| 2026-10-10T11:15 | Triple EMA stack | sell | BTC-USD | 13.80 | -0.09 | exit signal |
| 2026-10-10T11:10 | Three white soldiers | sell | XRP-USD | 22.01 | -0.14 | exit signal |
| 2026-10-10T11:05 | Triple EMA stack | buy | BTC-USD | 13.89 | — | entry signal |
| 2026-10-10T11:00 | Triple EMA stack | buy | ETH-USD | 13.90 | — | entry signal |
| 2026-10-10T10:59 | AI bee: Bizzy | sell | XRP-USD | 9.26 | -0.05 | Jev: sell (sell p=0.64) after 12 min |
| 2026-10-10T10:55 | Trend pullback | buy | BTC-USD | 14.28 | — | entry signal |
| 2026-10-10T10:50 | Z-score reversion | buy | SOL-USD | 15.33 | — | entry signal |
| 2026-10-10T10:50 | Three white soldiers | buy | XRP-USD | 22.15 | — | entry signal |
| 2026-10-10T10:50 | Trend pullback | buy | ETH-USD | 14.29 | — | entry signal |
| 2026-10-10T10:50 | ADX DI cross | buy | XRP-USD | 14.56 | — | entry signal |
| 2026-10-10T10:47 | AI bee: Bizzy | buy | XRP-USD | 9.31 | — | Jev: buy (buy p=0.62) |
| 2026-10-10T10:45 | MFI reversion | buy | XRP-USD | 15.20 | — | entry signal |
| 2026-10-10T10:45 | ADX DI cross | sell | BTC-USD | 14.49 | -0.09 | exit signal |
| 2026-10-10T10:40 | Z-score reversion | buy | XRP-USD | 15.35 | — | entry signal |
| 2026-10-10T10:40 | Z-score reversion | buy | DOGE-USD | 15.35 | — | entry signal |
| 2026-10-10T10:40 | RSI(14) reversion | buy | SOL-USD | 18.87 | — | entry signal |
| 2026-10-10T10:40 | RSI(14) reversion | buy | DOGE-USD | 18.87 | — | entry signal |
| 2026-10-10T10:35 | ADX DI cross | buy | BTC-USD | 14.58 | — | entry signal |
| 2026-10-10T10:30 | RSI(14) reversion | buy | XRP-USD | 18.88 | — | entry signal |
| 2026-10-10T10:30 | ADX DI cross | sell | BTC-USD | 14.55 | -0.08 | exit signal |
| 2026-10-10T10:25 | MFI reversion | sell | DOGE-USD | 15.12 | -0.12 | target is flat |
| 2026-10-10T10:25 | Trend pullback | sell | BTC-USD | 11.46 | -0.06 | exit signal |
| 2026-10-10T10:20 | MFI reversion | buy | DOGE-USD | 15.25 | — | entry signal |
| 2026-10-10T10:20 | MFI reversion | sell | XRP-USD | 15.15 | -0.13 | stop-loss |
| 2026-10-10T10:20 | Supertrend | sell | XRP-USD | 16.32 | -0.16 | exit signal |
| 2026-10-10T10:20 | Triple EMA stack | sell | BTC-USD | 11.13 | -0.06 | exit signal |
| 2026-10-10T10:20 | EMA 20/50 cross | sell | XRP-USD | 17.86 | -0.15 | stop-loss |
| 2026-10-10T10:16 | Triple EMA stack | sell | ETH-USD | 13.89 | -0.09 | exit signal |
| 2026-10-10T10:16 | EMA 20/50 cross | sell | SOL-USD | 14.36 | -0.06 | exit signal |
| 2026-10-10T10:10 | Donchian 20/10 | sell | ETH-USD | 14.42 | -0.10 | exit signal |
| 2026-10-10T10:10 | Donchian 20/10 | sell | BTC-USD | 14.42 | -0.10 | stop-loss |
| 2026-10-10T10:10 | RSI momentum | sell | ETH-USD | 14.21 | -0.10 | exit signal |
| 2026-10-10T10:10 | RSI momentum | sell | BTC-USD | 14.24 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 11:25:05.000125+00:00 -> 2026-10-10 11:35:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
