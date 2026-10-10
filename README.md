# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T19:25:05.000180+00:00 · 18247 ticks

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

Today: 14737 decisions in 2948 calls, $0.2059 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T19:25 | 0 / 3 / 2 | SOL-USD 16%, NANC 17%, COIN 15% |  |
| Breezy | 2026-10-10T19:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T19:25 | 2 / 3 / 0 | COIN 75% |  |

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
| 18 | Hold BTC | benchmark | 99.21 | -0.79 | 0 | — | 27.07 | 3.25 | -8.68 | 1 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -10.80 | -2.10 | -14.73 | 344 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.28 | 0.38 | -8.60 | 159 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.81 | -3.19 | 38 | 13.2 | 5.98 | 0.87 | -19.85 | 132 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -0.30 | 0.04 | -10.38 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.91 | -0.13 | -13.84 | 258 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.81 | -0.20 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.88 | -4.12 | 110 | 24.5 | -15.92 | -2.58 | -17.84 | 469 |
| 34 | Supertrend · 1h | trend | 95.34 | -4.66 | 52 | 13.5 | -0.09 | 0.18 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.04 | -5.96 | 36 | 25.0 | 23.96 | 3.26 | -8.81 | 107 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.95 | 2.05 | -6.38 | 201 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.54 | -1.84 | -17.79 | 129 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.73 | -0.49 | -9.03 | 151 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.25 | -6.05 | -20.97 | 252 |
| 41 | Ichimoku · 1h | trend | 92.94 | -7.06 | 41 | 19.5 | -0.63 | 0.12 | -20.02 | 122 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.13 | -0.42 | -13.06 | 391 |
| 43 | Bollinger reversion · 1h | reversion | 92.85 | -7.15 | 74 | 37.8 | -20.85 | -4.99 | -23.54 | 316 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.42 | 0.62 | -17.07 | 224 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 7.46 | 1.17 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 91.74 | -8.26 | 68 | 29.4 | 6.33 | 0.98 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.72 | -8.28 | 120 | 47.5 | -24.43 | -4.22 | -26.91 | 512 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.71 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.24 | -9.76 | 115 | 31.3 | -27.72 | -5.45 | -29.55 | 519 |
| 51 | CCI reversion · 1h | reversion | 89.77 | -10.22 | 100 | 45.0 | -8.60 | -1.11 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.71 | -10.29 | 278 | 22.3 | -33.99 | -5.12 | -39.26 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 89.18 | -10.82 | 62 | 19.4 | -6.62 | -0.71 | -19.79 | 242 |
| 55 | Donchian 20/10 · 1h | breakout | 88.85 | -11.15 | 58 | 19.0 | -0.12 | 0.19 | -17.72 | 224 |
| 56 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -11.96 | -1.35 | -28.62 | 317 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.56 | -5.13 | -36.59 | 700 |
| 58 | Three white soldiers | momentum | 88.02 | -11.98 | 136 | 18.4 | -48.39 | -23.65 | -48.39 | 590 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.88 | -12.12 | 101 | 13.9 | -8.90 | -1.00 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.85 | -1.33 | -24.12 | 412 |
| 63 | RSI(14) reversion | reversion | 75.28 | -24.72 | 355 | 28.7 | -72.80 | -18.22 | -72.88 | 1494 |
| 64 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.92 | -16.73 | -73.81 | 1672 |
| 65 | Squeeze breakout | breakout | 71.82 | -28.18 | 318 | 15.1 | -62.52 | -18.60 | -62.55 | 1233 |
| 66 | EMA 20/50 cross | trend | 71.16 | -28.84 | 320 | 20.3 | -77.28 | -15.41 | -77.29 | 1461 |
| 67 | Donchian 55/20 | breakout | 71.15 | -28.85 | 324 | 18.2 | -67.44 | -14.41 | -67.45 | 1290 |
| 68 | Volume breakout | breakout | 70.50 | -29.50 | 258 | 13.2 | -63.08 | -18.41 | -63.08 | 906 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -72.17 | -16.35 | -72.31 | 1442 |
| 70 | Supertrend | trend | 65.34 | -34.66 | 447 | 20.4 | -86.32 | -21.19 | -86.34 | 1920 |
| 71 | Keltner breakout | breakout | 63.62 | -36.38 | 439 | 14.6 | -84.06 | -28.41 | -84.07 | 1856 |
| 72 | Z-score reversion | reversion | 61.19 | -38.81 | 486 | 23.5 | -85.58 | -23.29 | -85.58 | 2089 |
| 73 | Ichimoku | trend | 60.80 | -39.20 | 399 | 9.8 | -81.75 | -23.46 | -81.75 | 1748 |
| 74 | AI bee: Boozy | ai | 60.66 | -39.34 | 252 | 5.2 | — | — | — | — |
| 75 | MFI reversion | reversion | 60.53 | -39.47 | 497 | 21.7 | -87.63 | -28.38 | -87.64 | 2122 |
| 76 | AI bee: Bizzy | ai | 59.22 | -40.78 | 807 | 9.0 | — | — | — | — |
| 77 | ADX DI cross | trend | 57.69 | -42.31 | 529 | 10.4 | -89.52 | -34.65 | -89.52 | 2129 |
| 78 | Donchian 20/10 | breakout | 56.82 | -43.18 | 618 | 18.4 | -90.91 | -26.58 | -90.92 | 2670 |
| 79 | RSI momentum | momentum | 56.04 | -43.96 | 585 | 17.4 | -90.31 | -25.76 | -90.32 | 2381 |
| 80 | MACD zero-line | trend | 55.54 | -44.46 | 565 | 15.2 | -91.58 | -29.86 | -91.58 | 2365 |
| 81 | Trend pullback ⏸ | trend | 55.45 | -44.55 | 581 | 15.0 | -90.80 | -27.26 | -90.80 | 2326 |
| 82 | Triple EMA stack | trend | 54.67 | -45.33 | 610 | 15.7 | -93.15 | -30.53 | -93.16 | 2615 |
| 83 | Bollinger breakout | breakout | 52.22 | -47.78 | 649 | 14.5 | -93.60 | -33.86 | -93.61 | 2824 |
| 84 | Consensus | meta | 51.04 | -48.96 | 610 | 10.0 | -94.25 | -26.17 | -94.25 | 2689 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -31.04 | -98.71 | 5418 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -33.56 | -97.39 | 3550 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -36.64 | -96.44 | 3608 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.41 | -99.35 | 5699 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.30 | -31.89 | -96.30 | 3609 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.62 | -99.73 | 6208 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.87 | -97.36 | 3684 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.55 | -98.47 | 4714 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.48 | -99.51 | 6144 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -33.98 | -95.86 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.60 | -35.21 | -95.60 | 4087 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.85 | -99.90 | 8329 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T19:25 | MACD zero-line | buy | DOGE-USD | 13.89 | — | entry signal |
| 2026-10-10T19:21 | AI bee: Bizzy | buy | SOL-USD | 9.64 | — | Jev: buy (buy p=0.65) |
| 2026-10-10T19:21 | ADX DI cross | buy | XRP-USD | 14.43 | — | entry signal |
| 2026-10-10T19:15 | MFI reversion | sell | SOL-USD | 15.10 | -0.05 | exit signal |
| 2026-10-10T19:02 | AI bee: Boozy | sell | SOL-USD | 14.91 | -0.09 | Jev: sell (sell p=0.57) after 16 min |
| 2026-10-10T19:00 | AI bee: Bizzy | sell | ETH-USD | 8.52 | -0.06 | Jev: sell (sell p=0.52) after 10 min |
| 2026-10-10T19:00 | Williams %R · 1h | buy | XRP-USD | 15.29 | — | entry signal |
| 2026-10-10T18:55 | Triple EMA stack | buy | SOL-USD | 13.67 | — | entry signal |
| 2026-10-10T18:55 | EMA 20/50 cross | buy | SOL-USD | 17.80 | — | entry signal |
| 2026-10-10T18:50 | AI bee: Bizzy | buy | ETH-USD | 8.58 | — | Jev: buy (buy p=0.58) |
| 2026-10-10T18:50 | Keltner breakout | buy | SOL-USD | 15.92 | — | entry signal |
| 2026-10-10T18:50 | MACD zero-line | buy | SOL-USD | 13.90 | — | entry signal |
| 2026-10-10T18:46 | AI bee: Boozy | buy | SOL-USD | 15.00 | — | Jev: buy (buy p=0.75) |
| 2026-10-10T18:45 | MFI reversion | buy | XRP-USD | 15.15 | — | entry signal |
| 2026-10-10T18:45 | Squeeze breakout | buy | SOL-USD | 17.96 | — | entry signal |
| 2026-10-10T18:45 | Donchian 20/10 | buy | SOL-USD | 14.21 | — | entry signal |
| 2026-10-10T18:45 | RSI momentum | buy | SOL-USD | 14.01 | — | entry signal |
| 2026-10-10T18:45 | Supertrend | buy | SOL-USD | 16.34 | — | entry signal |
| 2026-10-10T18:40 | Consensus | buy | ETH-USD | 12.77 | — | entry |
| 2026-10-10T18:40 | Squeeze breakout | buy | ETH-USD | 17.97 | — | entry signal |
| 2026-10-10T18:40 | Donchian 20/10 | buy | ETH-USD | 14.22 | — | entry signal |
| 2026-10-10T18:40 | RSI momentum | buy | ETH-USD | 14.02 | — | entry signal |
| 2026-10-10T18:35 | Bollinger breakout | buy | SOL-USD | 13.05 | — | entry signal |
| 2026-10-10T18:29 | AI bee: Bizzy | sell | SOL-USD | 8.55 | -0.05 | Jev: sell (sell p=0.71) after 11 min |
| 2026-10-10T18:25 | Consensus | sell | BTC-USD | 12.71 | -0.08 | target is flat |
| 2026-10-10T18:25 | Donchian 20/10 | sell | BTC-USD | 11.39 | -0.06 | exit signal |
| 2026-10-10T18:25 | RSI momentum | sell | BTC-USD | 11.24 | -0.06 | exit signal |
| 2026-10-10T18:25 | Supertrend | sell | BTC-USD | 13.08 | -0.07 | exit signal |
| 2026-10-10T18:25 | Triple EMA stack | sell | BTC-USD | 13.72 | -0.07 | exit signal |
| 2026-10-10T18:23 | AI bee: Bizzy | sell | ETH-USD | 8.89 | -0.06 | Jev: sell (sell p=0.52) after 11 min |
| 2026-10-10T18:22 | Bollinger breakout | buy | ETH-USD | 13.06 | — | entry signal |
| 2026-10-10T18:22 | Ichimoku | buy | ETH-USD | 15.21 | — | entry signal |
| 2026-10-10T18:18 | AI bee: Bizzy | buy | SOL-USD | 8.60 | — | Jev: buy (buy p=0.58) |
| 2026-10-10T18:15 | Squeeze breakout | sell | BTC-USD | 17.88 | -0.13 | stop-loss |
| 2026-10-10T18:15 | Keltner breakout | sell | BTC-USD | 15.83 | -0.11 | stop-loss |
| 2026-10-10T18:15 | Bollinger breakout | sell | BTC-USD | 12.99 | -0.09 | stop-loss |
| 2026-10-10T18:15 | Ichimoku | sell | BTC-USD | 15.17 | -0.08 | exit signal |
| 2026-10-10T18:12 | AI bee: Bizzy | buy | ETH-USD | 8.95 | — | Jev: buy (buy p=0.60) |
| 2026-10-10T18:00 | Squeeze breakout · 1h | sell | DOGE-USD | 23.38 | -0.18 | exit signal |
| 2026-10-10T18:00 | Bollinger breakout · 1h | buy | ETH-USD | 4.37 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 19:25:05.000180+00:00 -> 2026-10-10 19:35:05.000180+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
