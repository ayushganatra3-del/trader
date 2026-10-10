# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T20:55:05.000178+00:00 · 18316 ticks

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

Today: 15772 decisions in 3155 calls, $0.2204 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T20:55 | 1 / 3 / 1 | DOGE-USD 15%, NANC 17%, COIN 15% |  |
| Breezy | 2026-10-10T20:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T20:55 | 3 / 2 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.14 | +1.01% | 5 |
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
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 18 | Hold BTC | benchmark | 99.28 | -0.72 | 0 | — | 27.04 | 3.25 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.17 | -0.82 | 89 | 55.1 | -10.63 | -2.07 | -14.61 | 344 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.82 | -3.18 | 38 | 13.2 | 5.99 | 0.87 | -19.85 | 132 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.88 | -0.13 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.65 | -0.18 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.88 | -4.12 | 110 | 24.5 | -15.79 | -2.55 | -17.84 | 469 |
| 34 | Supertrend · 1h | trend | 95.37 | -4.63 | 52 | 13.5 | -0.06 | 0.18 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.03 | -5.97 | 36 | 25.0 | 23.95 | 3.26 | -8.82 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.95 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.54 | -1.84 | -17.79 | 129 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.62 | -0.47 | -9.03 | 148 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Ichimoku · 1h | trend | 92.96 | -7.04 | 41 | 19.5 | -0.62 | 0.13 | -20.02 | 122 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.47 | -0.80 | -13.33 | 418 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.50 | 0.63 | -17.07 | 224 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Williams %R · 1h | reversion | 91.76 | -8.24 | 120 | 47.5 | -24.39 | -4.21 | -26.91 | 512 |
| 47 | Bollinger breakout · 1h | breakout | 91.75 | -8.24 | 68 | 29.4 | 6.34 | 0.98 | -12.90 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.66 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.25 | -9.76 | 115 | 31.3 | -27.70 | -5.44 | -29.50 | 517 |
| 51 | CCI reversion · 1h | reversion | 89.77 | -10.22 | 100 | 45.0 | -8.60 | -1.11 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 278 | 22.3 | -33.98 | -5.12 | -39.26 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.17 | -10.83 | 62 | 19.4 | -6.62 | -0.71 | -19.79 | 242 |
| 55 | Donchian 20/10 · 1h | breakout | 88.84 | -11.16 | 58 | 19.0 | -0.09 | 0.20 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.96 | -1.35 | -28.61 | 317 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.58 | -5.14 | -36.59 | 701 |
| 58 | Three white soldiers | momentum | 88.02 | -11.98 | 136 | 18.4 | -47.94 | -23.30 | -47.94 | 589 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.88 | -12.12 | 101 | 13.9 | -8.88 | -1.00 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.85 | -1.33 | -24.12 | 412 |
| 63 | RSI(14) reversion | reversion | 75.28 | -24.72 | 355 | 28.7 | -72.80 | -18.22 | -72.88 | 1494 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.78 | -16.63 | -73.80 | 1670 |
| 65 | Squeeze breakout | breakout | 71.39 | -28.61 | 322 | 14.9 | -62.57 | -18.42 | -62.57 | 1233 |
| 66 | EMA 20/50 cross | trend | 71.00 | -29.00 | 321 | 20.2 | -77.29 | -15.43 | -77.33 | 1462 |
| 67 | Donchian 55/20 | breakout | 70.96 | -29.04 | 325 | 18.2 | -67.53 | -14.44 | -67.53 | 1292 |
| 68 | Volume breakout | breakout | 70.45 | -29.55 | 258 | 13.2 | -62.71 | -18.12 | -62.72 | 901 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.25 | -16.38 | -72.39 | 1443 |
| 70 | Supertrend | trend | 65.24 | -34.76 | 448 | 20.3 | -86.35 | -21.23 | -86.36 | 1920 |
| 71 | Keltner breakout | breakout | 63.40 | -36.60 | 441 | 14.5 | -83.90 | -27.90 | -83.90 | 1850 |
| 72 | Z-score reversion | reversion | 61.19 | -38.81 | 486 | 23.5 | -85.53 | -23.23 | -85.53 | 2083 |
| 73 | Ichimoku | trend | 60.64 | -39.36 | 401 | 9.7 | -81.90 | -23.59 | -81.90 | 1751 |
| 74 | MFI reversion | reversion | 60.57 | -39.43 | 497 | 21.7 | -87.63 | -28.38 | -87.67 | 2122 |
| 75 | AI bee: Boozy | ai | 60.55 | -39.45 | 253 | 5.1 | — | — | — | — |
| 76 | AI bee: Bizzy | ai | 59.08 | -40.92 | 810 | 9.0 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.60 | -42.40 | 530 | 10.4 | -89.50 | -34.46 | -89.50 | 2128 |
| 78 | Donchian 20/10 | breakout | 56.48 | -43.52 | 622 | 18.3 | -90.83 | -26.21 | -90.84 | 2666 |
| 79 | RSI momentum | momentum | 55.75 | -44.25 | 588 | 17.3 | -90.36 | -25.80 | -90.37 | 2384 |
| 80 | Trend pullback ⏸ | trend | 55.45 | -44.55 | 581 | 15.0 | -90.85 | -27.21 | -90.85 | 2331 |
| 81 | MACD zero-line | trend | 55.33 | -44.67 | 568 | 15.1 | -91.61 | -29.92 | -91.62 | 2367 |
| 82 | Triple EMA stack | trend | 54.37 | -45.63 | 613 | 15.7 | -93.22 | -30.59 | -93.22 | 2620 |
| 83 | Bollinger breakout | breakout | 51.91 | -48.09 | 653 | 14.4 | -93.55 | -33.25 | -93.55 | 2819 |
| 84 | Consensus | meta | 50.85 | -49.15 | 612 | 10.0 | -94.25 | -26.15 | -94.25 | 2687 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.76 | -98.70 | 5411 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -33.26 | -97.38 | 3549 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -36.62 | -96.45 | 3608 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.40 | -99.35 | 5703 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -31.88 | -96.32 | 3613 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.58 | -99.74 | 6210 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -38.89 | -97.37 | 3688 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.58 | -98.47 | 4716 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.55 | -99.51 | 6148 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -34.01 | -95.87 | 3745 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.61 | -35.26 | -95.61 | 4090 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.25 | -99.90 | 8328 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T20:55 | ADX DI cross | buy | ETH-USD | 14.41 | — | entry signal |
| 2026-10-10T20:53 | AI bee: Bizzy | buy | DOGE-USD | 8.67 | — | Jev: buy (buy p=0.59) |
| 2026-10-10T20:50 | AI bee: Bizzy | sell | XRP-USD | 8.15 | -0.03 | Jev: sell (sell p=0.57) after 20 min |
| 2026-10-10T20:50 | Donchian 55/20 | buy | XRP-USD | 17.75 | — | entry signal |
| 2026-10-10T20:45 | Consensus | buy | XRP-USD | 12.73 | — | entry |
| 2026-10-10T20:45 | Consensus | buy | BTC-USD | 12.73 | — | entry |
| 2026-10-10T20:45 | Squeeze breakout | buy | XRP-USD | 17.86 | — | entry signal |
| 2026-10-10T20:45 | Keltner breakout | buy | XRP-USD | 15.86 | — | entry signal |
| 2026-10-10T20:45 | Triple EMA stack | buy | BTC-USD | 13.60 | — | entry signal |
| 2026-10-10T20:40 | Volume breakout | buy | XRP-USD | 17.62 | — | entry signal |
| 2026-10-10T20:40 | Bollinger breakout | buy | XRP-USD | 12.99 | — | entry signal |
| 2026-10-10T20:40 | Supertrend | buy | XRP-USD | 16.32 | — | entry signal |
| 2026-10-10T20:35 | Triple EMA stack | sell | BTC-USD | 13.57 | -0.09 | exit signal |
| 2026-10-10T20:30 | AI bee: Bizzy | buy | XRP-USD | 8.19 | — | Jev: buy (buy p=0.55) |
| 2026-10-10T20:30 | Consensus | sell | BTC-USD | 12.68 | -0.08 | target is flat |
| 2026-10-10T20:30 | Donchian 20/10 | sell | BTC-USD | 14.03 | -0.10 | stop-loss |
| 2026-10-10T20:30 | RSI momentum | sell | BTC-USD | 13.84 | -0.10 | stop-loss |
| 2026-10-10T20:30 | Triple EMA stack | buy | XRP-USD | 13.61 | — | entry signal |
| 2026-10-10T20:25 | MACD zero-line | sell | BTC-USD | 13.79 | -0.09 | exit signal |
| 2026-10-10T20:20 | Squeeze breakout | sell | XRP-USD | 17.84 | -0.12 | exit signal |
| 2026-10-10T20:20 | Bollinger breakout | sell | XRP-USD | 12.97 | -0.09 | exit signal |
| 2026-10-10T20:20 | Donchian 55/20 | sell | ETH-USD | 17.65 | -0.14 | stop-loss |
| 2026-10-10T20:20 | Donchian 20/10 | sell | SOL-USD | 14.12 | -0.08 | exit signal |
| 2026-10-10T20:20 | RSI momentum | sell | ETH-USD | 13.93 | -0.10 | exit signal |
| 2026-10-10T20:20 | Supertrend | sell | ETH-USD | 13.12 | -0.02 | exit signal |
| 2026-10-10T20:20 | Triple EMA stack | sell | ETH-USD | 13.63 | -0.08 | exit signal |
| 2026-10-10T20:15 | Squeeze breakout | sell | SOL-USD | 17.87 | -0.09 | exit signal |
| 2026-10-10T20:15 | Keltner breakout | sell | SOL-USD | 15.82 | -0.10 | exit signal |
| 2026-10-10T20:15 | Bollinger breakout | sell | SOL-USD | 13.00 | -0.05 | exit signal |
| 2026-10-10T20:15 | Donchian 20/10 | sell | ETH-USD | 14.13 | -0.09 | exit signal |
| 2026-10-10T20:15 | MACD zero-line | sell | SOL-USD | 13.82 | -0.08 | exit signal |
| 2026-10-10T20:10 | Consensus | sell | ETH-USD | 12.70 | -0.07 | target is flat |
| 2026-10-10T20:10 | Squeeze breakout | sell | ETH-USD | 17.88 | -0.10 | stop-loss |
| 2026-10-10T20:10 | Keltner breakout | sell | ETH-USD | 15.79 | -0.12 | stop-loss |
| 2026-10-10T20:10 | Bollinger breakout | sell | ETH-USD | 13.00 | -0.06 | stop-loss |
| 2026-10-10T20:10 | Ichimoku | sell | ETH-USD | 15.13 | -0.07 | exit signal |
| 2026-10-10T20:10 | EMA 20/50 cross | buy | XRP-USD | 17.76 | — | entry signal |
| 2026-10-10T20:05 | Donchian 20/10 | buy | BTC-USD | 14.13 | — | entry signal |
| 2026-10-10T20:05 | RSI momentum | buy | BTC-USD | 13.93 | — | entry signal |
| 2026-10-10T20:00 | Triple EMA stack | sell | DOGE-USD | 13.58 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 20:55:05.000178+00:00 -> 2026-10-10 21:05:05.000178+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
