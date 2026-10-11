# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T16:55:05.000123+00:00 · 19251 ticks

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
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 11970 decisions in 2394 calls, $0.1674 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T16:55 | 0 / 4 / 1 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-11T16:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T16:55 | 3 / 2 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.78 | +2.31% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.44 | -2.26 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -15.28 | -2.51 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.32 | 0.32 | 0 | — | 30.91 | 3.65 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.21 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.28 | -0.72 | 27 | 14.8 | 13.79 | 1.71 | -16.96 | 112 |
| 19 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.86 | -1.90 | -14.61 | 340 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.38 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.00 | -6.51 | -25.39 | 173 |
| 27 | EMA 20/50 cross · 1h | trend | 96.83 | -3.17 | 39 | 12.8 | 6.14 | 0.89 | -19.85 | 133 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.10 | -1.99 | -9.68 | 254 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -0.06 | 0.15 | -13.84 | 252 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.62 | -0.18 | -20.87 | 296 |
| 32 | MACD cross · 1h | trend | 96.03 | -3.97 | 113 | 23.9 | -14.80 | -2.37 | -17.27 | 468 |
| 33 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.86 | -4.97 | -9.58 | 229 |
| 34 | Supertrend · 1h | trend | 95.63 | -4.37 | 53 | 13.2 | 0.62 | 0.27 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -2.00 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.07 | -6.30 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.88 | -6.12 | 37 | 24.3 | 23.87 | 3.25 | -9.17 | 108 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -9.89 | -1.55 | -17.79 | 128 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.67 | -0.86 | -13.00 | 419 |
| 42 | Ichimoku · 1h | trend | 92.78 | -7.22 | 42 | 19.0 | -0.17 | 0.18 | -20.56 | 124 |
| 43 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.74 | -4.95 | -23.37 | 317 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.43 | 0.74 | -17.07 | 225 |
| 45 | Volume breakout · 1h | breakout | 92.60 | -7.40 | 56 | 19.6 | 8.30 | 1.28 | -12.60 | 123 |
| 46 | Bollinger breakout · 1h | breakout | 91.57 | -8.43 | 70 | 28.6 | 6.27 | 0.97 | -13.17 | 290 |
| 47 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.84 | -4.09 | -26.91 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -8.99 | -0.90 | -26.38 | 239 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 118 | 33.1 | -26.45 | -5.16 | -28.48 | 510 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -6.92 | -0.85 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.53 | -10.47 | 283 | 21.9 | -32.63 | -4.87 | -39.17 | 1280 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.78 | -11.22 | 64 | 18.8 | -6.29 | -0.67 | -20.33 | 240 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.18 | -1.38 | -28.34 | 320 |
| 56 | Donchian 20/10 · 1h | breakout | 88.73 | -11.27 | 59 | 18.6 | -0.99 | 0.09 | -17.81 | 229 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -29.96 | -5.02 | -36.60 | 697 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.93 | -12.07 | 104 | 13.5 | -9.23 | -1.05 | -21.69 | 342 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.05 | -23.30 | -48.07 | 590 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.14 | -1.28 | -25.35 | 218 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -9.87 | -1.18 | -23.33 | 414 |
| 63 | ROC + volume | momentum | 75.27 | -24.73 | 390 | 22.6 | -72.54 | -16.40 | -73.90 | 1677 |
| 64 | RSI(14) reversion | reversion | 73.91 | -26.09 | 369 | 27.6 | -72.45 | -18.15 | -72.45 | 1486 |
| 65 | Squeeze breakout | breakout | 71.57 | -28.43 | 329 | 14.9 | -62.06 | -18.08 | -62.64 | 1235 |
| 66 | Donchian 55/20 | breakout | 71.13 | -28.87 | 332 | 17.8 | -67.03 | -14.14 | -67.50 | 1295 |
| 67 | Volume breakout | breakout | 70.73 | -29.27 | 264 | 13.6 | -62.35 | -17.78 | -62.78 | 907 |
| 68 | EMA 20/50 cross | trend | 70.39 | -29.61 | 335 | 19.4 | -76.62 | -15.16 | -77.02 | 1459 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.19 | -15.98 | -71.25 | 1426 |
| 70 | Supertrend | trend | 64.41 | -35.59 | 464 | 19.6 | -85.81 | -20.85 | -86.10 | 1914 |
| 71 | Keltner breakout | breakout | 63.03 | -36.97 | 452 | 14.4 | -83.65 | -27.63 | -83.84 | 1856 |
| 72 | Ichimoku | trend | 60.78 | -39.22 | 407 | 9.6 | -81.48 | -23.00 | -81.78 | 1750 |
| 73 | AI bee: Boozy | ai | 60.23 | -39.77 | 257 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.36 | -23.32 | -85.36 | 2082 |
| 75 | MFI reversion | reversion | 59.07 | -40.92 | 515 | 21.2 | -87.51 | -28.61 | -87.54 | 2120 |
| 76 | AI bee: Bizzy | ai | 57.43 | -42.57 | 842 | 8.8 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.62 | -43.38 | 545 | 10.1 | -89.18 | -35.02 | -89.27 | 2118 |
| 78 | Donchian 20/10 | breakout | 55.72 | -44.28 | 638 | 17.9 | -90.73 | -26.17 | -90.88 | 2672 |
| 79 | Trend pullback | trend | 54.94 | -45.06 | 587 | 14.8 | -91.00 | -27.17 | -91.00 | 2338 |
| 80 | RSI momentum | momentum | 54.25 | -45.75 | 611 | 16.7 | -90.28 | -25.85 | -90.45 | 2389 |
| 81 | MACD zero-line | trend | 53.47 | -46.53 | 594 | 14.5 | -91.41 | -30.18 | -91.53 | 2365 |
| 82 | Triple EMA stack | trend | 53.40 | -46.60 | 632 | 15.2 | -93.17 | -30.21 | -93.28 | 2627 |
| 83 | Bollinger breakout | breakout | 50.93 | -49.07 | 673 | 14.1 | -93.47 | -33.26 | -93.58 | 2825 |
| 84 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.67 | -31.65 | -98.70 | 5410 |
| 85 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -34.01 | -97.39 | 3554 |
| 86 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -36.39 | -96.52 | 3626 |
| 87 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.12 | -25.70 | -94.20 | 2691 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.88 | -99.34 | 5686 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -31.99 | -96.38 | 3623 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.67 | -99.73 | 6205 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -38.30 | -97.39 | 3695 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -38.06 | -98.46 | 4710 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.30 | -99.52 | 6148 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.83 | -34.19 | -95.83 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.59 | -34.96 | -95.59 | 4081 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.54 | -99.90 | 8325 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T16:55 | Keltner breakout | buy | XRP-USD | 3.14 | — | rebalance up |
| 2026-10-11T16:55 | Keltner breakout | sell | SOL-USD | 3.14 | 0.04 | rebalance down |
| 2026-10-11T16:53 | AI bee: Bizzy | sell | DOGE-USD | 8.11 | -0.03 | Jev: sell (sell p=0.76) after 11 min |
| 2026-10-11T16:50 | RSI momentum | buy | BTC-USD | 2.71 | — | rebalance up |
| 2026-10-11T16:50 | RSI momentum | sell | ETH-USD | 2.71 | 0.03 | rebalance down |
| 2026-10-11T16:50 | Triple EMA stack | buy | SOL-USD | 2.67 | — | rebalance up |
| 2026-10-11T16:50 | Triple EMA stack | sell | ETH-USD | 2.67 | 0.03 | rebalance down |
| 2026-10-11T16:45 | AI bee: Boozy | sell | ETH-USD | 14.47 | -0.08 | Jev: add (buy p=0.54) |
| 2026-10-11T16:42 | AI bee: Bizzy | buy | DOGE-USD | 8.15 | — | Jev: buy (buy p=0.57) |
| 2026-10-11T16:41 | AI bee: Bizzy | sell | ETH-USD | 8.52 | -0.06 | Jev: sell (sell p=0.53) after 12 min |
| 2026-10-11T16:40 | Keltner breakout | buy | XRP-USD | 6.34 | — | entry signal |
| 2026-10-11T16:40 | Keltner breakout | sell | ETH-USD | 3.18 | 0.02 | rebalance down |
| 2026-10-11T16:40 | Keltner breakout | sell | DOGE-USD | 3.16 | 0.03 | rebalance down |
| 2026-10-11T16:35 | Volume breakout | buy | SOL-USD | 10.54 | — | rebalance up |
| 2026-10-11T16:35 | Volume breakout | sell | XRP-USD | 14.10 | 0.09 | time stop |
| 2026-10-11T16:35 | Volume breakout | sell | DOGE-USD | 14.09 | 0.13 | time stop |
| 2026-10-11T16:29 | AI bee: Boozy | buy | ETH-USD | 14.55 | — | Jev: buy (buy p=0.78) |
| 2026-10-11T16:29 | AI bee: Bizzy | buy | ETH-USD | 8.58 | — | Jev: buy (buy p=0.60) |
| 2026-10-11T16:20 | Squeeze breakout | sell | XRP-USD | 17.78 | 0.11 | stop-loss |
| 2026-10-11T16:20 | Keltner breakout | buy | SOL-USD | 3.11 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | buy | ETH-USD | 3.17 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | buy | DOGE-USD | 3.16 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | buy | BTC-USD | 6.26 | — | rebalance up |
| 2026-10-11T16:20 | Keltner breakout | sell | XRP-USD | 12.54 | 0.08 | stop-loss |
| 2026-10-11T16:20 | Bollinger breakout | buy | ETH-USD | 2.56 | — | rebalance up |
| 2026-10-11T16:20 | Bollinger breakout | buy | BTC-USD | 2.58 | — | rebalance up |
| 2026-10-11T16:20 | Bollinger breakout | sell | XRP-USD | 10.11 | 0.06 | stop-loss |
| 2026-10-11T16:10 | AI bee: Bizzy | sell | SOL-USD | 8.13 | 0.01 | Jev: sell (sell p=0.55) after 21 min |
| 2026-10-11T16:08 | AI bee: Bizzy | sell | XRP-USD | 8.12 | -0.07 | Jev: sell (sell p=0.79) after 11 min |
| 2026-10-11T16:05 | AI bee: Boozy | sell | ETH-USD | 14.55 | -0.07 | Jev: sell |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | XRP-USD | 6.08 | 0.10 | exit signal |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | SOL-USD | 6.99 | 0.09 | exit signal |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | ETH-USD | 5.63 | 0.03 | exit signal |
| 2026-10-11T16:00 | CCI reversion · 1h | sell | DOGE-USD | 6.06 | 0.09 | exit signal |
| 2026-10-11T16:00 | Williams %R · 1h | sell | SOL-USD | 9.33 | 0.12 | exit signal |
| 2026-10-11T16:00 | Williams %R · 1h | sell | ETH-USD | 9.18 | 0.05 | exit signal |
| 2026-10-11T16:00 | Williams %R · 1h | sell | DOGE-USD | 9.25 | 0.12 | exit signal |
| 2026-10-11T16:00 | Bollinger reversion · 1h | sell | SOL-USD | 15.53 | 0.22 | take-profit |
| 2026-10-11T16:00 | Candlestick reversal · 1h | sell | XRP-USD | 5.03 | 0.07 | take-profit |
| 2026-10-11T16:00 | Candlestick reversal · 1h | sell | SOL-USD | 10.16 | 0.13 | take-profit |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 16:55:05.000123+00:00 -> 2026-10-11 17:05:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
