# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T06:55:05.000160+00:00 · 19949 ticks

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

Today: 5367 decisions in 1074 calls, $0.0752 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T06:55 | 3 / 2 / 0 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T06:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T06:55 | 5 / 0 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.26 | 3.26 | 37 | 43.2 | -7.53 | -2.27 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.52 | 2.52 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.20 | 2.20 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.00 | 2.00 | 14 | 57.1 | -12.39 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.32 | 1.32 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.24 | 1.24 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.08 | 1.08 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.43 | 0.43 | 0 | — | 30.91 | 3.62 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.75 | -0.25 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.68 | -0.32 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.25 | -0.75 | 28 | 14.3 | 13.20 | 1.63 | -16.96 | 114 |
| 19 | Stochastic reversion · 1h | reversion | 99.11 | -0.89 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.58 | -1.42 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.55 | -1.45 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.79 | -2.21 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.30 | -2.69 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.16 | -2.84 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.03 | -2.97 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | EMA 20/50 cross · 1h | trend | 96.73 | -3.27 | 40 | 12.5 | 6.31 | 0.90 | -19.85 | 136 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.92 | -2.30 | -10.19 | 268 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.29 | -3.71 | 58 | 20.7 | -0.37 | 0.10 | -13.84 | 252 |
| 31 | Parabolic SAR · 1h | trend | 96.25 | -3.75 | 82 | 22.0 | -1.97 | -0.09 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.84 | -4.16 | 115 | 23.5 | -14.68 | -2.33 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.67 | -4.33 | 53 | 13.2 | 2.46 | 0.51 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.48 | -6.52 | 119 | 34.5 | -10.04 | -1.58 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.41 | -6.59 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.08 | -6.92 | 26 | 26.9 | -2.00 | -0.33 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.01 | -6.99 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.81 | -7.19 | 392 | 18.4 | -4.01 | -0.57 | -13.94 | 429 |
| 42 | Bollinger reversion · 1h | reversion | 92.73 | -7.27 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.64 | -7.36 | 64 | 15.6 | 5.03 | 0.80 | -17.15 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.31 | -7.69 | 58 | 19.0 | 7.85 | 1.22 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 92.14 | -7.86 | 44 | 18.2 | -0.84 | 0.10 | -21.18 | 125 |
| 46 | Williams %R · 1h | reversion | 91.52 | -8.48 | 126 | 47.6 | -23.74 | -4.04 | -26.91 | 509 |
| 47 | Bollinger breakout · 1h | breakout | 91.20 | -8.80 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.67 | -9.33 | 69 | 15.9 | -8.40 | -0.82 | -26.49 | 241 |
| 50 | Candlestick reversal · 1h | reversion | 90.37 | -9.63 | 118 | 33.1 | -26.10 | -5.03 | -28.13 | 506 |
| 51 | CCI reversion · 1h | reversion | 89.93 | -10.07 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.46 | -10.54 | 284 | 21.8 | -32.15 | -4.76 | -39.17 | 1279 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.72 | -11.28 | 149 | 18.8 | -13.21 | -1.51 | -28.57 | 327 |
| 55 | Donchian 20/10 · 1h | breakout | 88.67 | -11.33 | 60 | 18.3 | -0.51 | 0.14 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.60 | -11.40 | 138 | 25.4 | -29.89 | -4.98 | -36.60 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.27 | -11.73 | 66 | 18.2 | -6.61 | -0.71 | -20.89 | 239 |
| 58 | EMA 9/21 cross · 1h | trend | 87.92 | -12.08 | 104 | 13.5 | -8.58 | -0.95 | -21.96 | 339 |
| 59 | Max aggression: 5-day momentum | meta | 87.91 | -12.09 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 60 | Keltner breakout · 1h | breakout | 87.04 | -12.96 | 43 | 18.6 | -11.93 | -1.38 | -25.86 | 220 |
| 61 | Three white soldiers | momentum | 86.80 | -13.20 | 147 | 17.0 | -48.21 | -23.10 | -48.24 | 593 |
| 62 | ROC + volume · 1h | momentum | 86.22 | -13.78 | 132 | 21.2 | -9.99 | -1.19 | -23.51 | 415 |
| 63 | ROC + volume | momentum | 74.15 | -25.84 | 400 | 23.0 | -73.00 | -16.56 | -74.10 | 1682 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 375 | 27.5 | -72.05 | -17.78 | -72.10 | 1482 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.22 | -18.04 | -62.23 | 1236 |
| 66 | Volume breakout | breakout | 69.88 | -30.12 | 271 | 14.0 | -62.52 | -17.83 | -62.54 | 907 |
| 67 | EMA 20/50 cross | trend | 68.73 | -31.27 | 346 | 19.9 | -76.72 | -15.21 | -76.78 | 1455 |
| 68 | Donchian 55/20 | breakout | 68.38 | -31.62 | 349 | 18.1 | -68.22 | -14.58 | -68.27 | 1303 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 405 | 25.9 | -71.11 | -15.76 | -71.18 | 1425 |
| 70 | Supertrend | trend | 62.62 | -37.38 | 479 | 19.8 | -85.95 | -20.92 | -86.02 | 1914 |
| 71 | Keltner breakout | breakout | 61.47 | -38.53 | 468 | 14.5 | -83.86 | -27.73 | -83.86 | 1858 |
| 72 | AI bee: Boozy | ai | 60.04 | -39.96 | 260 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 59.24 | -40.76 | 420 | 10.2 | -81.83 | -23.18 | -81.84 | 1753 |
| 74 | Z-score reversion | reversion | 58.93 | -41.07 | 516 | 22.1 | -85.05 | -22.69 | -85.06 | 2073 |
| 75 | MFI reversion | reversion | 58.29 | -41.72 | 525 | 20.8 | -87.46 | -27.77 | -87.50 | 2119 |
| 76 | AI bee: Bizzy | ai | 56.25 | -43.75 | 866 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.23 | -44.77 | 558 | 10.2 | -89.24 | -34.89 | -89.26 | 2122 |
| 78 | Donchian 20/10 | breakout | 53.73 | -46.27 | 656 | 18.0 | -90.89 | -26.16 | -90.89 | 2673 |
| 79 | RSI momentum | momentum | 52.21 | -47.79 | 631 | 16.8 | -90.57 | -25.95 | -90.57 | 2397 |
| 80 | MACD zero-line | trend | 52.13 | -47.87 | 610 | 14.6 | -91.49 | -29.76 | -91.50 | 2366 |
| 81 | Trend pullback | trend | 52.10 | -47.90 | 618 | 14.6 | -91.34 | -27.31 | -91.35 | 2362 |
| 82 | Triple EMA stack | trend | 51.25 | -48.76 | 655 | 15.3 | -93.34 | -30.41 | -93.34 | 2635 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -31.01 | -98.64 | 5390 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.35 | -97.36 | 3553 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -36.38 | -96.53 | 3635 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.28 | -25.56 | -94.28 | 2703 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.33 | -36.13 | -99.33 | 5677 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.50 | -31.86 | -96.50 | 3645 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.74 | -99.73 | 6205 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.05 | -97.36 | 3697 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.42 | -36.14 | -98.42 | 4698 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.57 | -33.18 | -93.57 | 2827 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -39.67 | -99.51 | 6146 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.73 | -32.76 | -95.73 | 3733 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.57 | -33.75 | -95.58 | 4082 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.80 | -99.89 | 8312 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T06:55 | RSI momentum | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-12T06:55 | RSI momentum | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-10-12T06:55 | Trend pullback | buy | SOL-USD | 10.37 | — | entry signal |
| 2026-10-12T06:55 | Trend pullback | sell | DOGE-USD | 2.61 | -0.02 | rebalance down |
| 2026-10-12T06:55 | Supertrend | buy | BTC-USD | 15.67 | — | entry signal |
| 2026-10-12T06:50 | Trend pullback | buy | DOGE-USD | 2.62 | — | rebalance up |
| 2026-10-12T06:50 | Trend pullback | sell | SOL-USD | 10.38 | -0.09 | exit signal |
| 2026-10-12T06:50 | Triple EMA stack | buy | BTC-USD | 12.81 | — | entry signal |
| 2026-10-12T06:35 | MFI reversion | buy | XRP-USD | 14.58 | — | entry signal |
| 2026-10-12T06:35 | Trend pullback | buy | XRP-USD | 10.47 | — | entry signal |
| 2026-10-12T06:35 | Trend pullback | buy | SOL-USD | 10.47 | — | entry signal |
| 2026-10-12T06:35 | Trend pullback | buy | ETH-USD | 10.47 | — | entry signal |
| 2026-10-12T06:35 | Trend pullback | buy | DOGE-USD | 10.47 | — | entry signal |
| 2026-10-12T06:35 | Trend pullback | buy | BTC-USD | 10.47 | — | entry signal |
| 2026-10-12T06:35 | ADX DI cross | buy | XRP-USD | 11.06 | — | entry signal |
| 2026-10-12T06:35 | ADX DI cross | buy | SOL-USD | 11.07 | — | entry signal |
| 2026-10-12T06:35 | ADX DI cross | buy | DOGE-USD | 11.07 | — | entry signal |
| 2026-10-12T06:35 | ADX DI cross | buy | BTC-USD | 11.07 | — | entry signal |
| 2026-10-12T06:35 | ADX DI cross | sell | ETH-USD | 2.77 | -0.01 | rebalance down |
| 2026-10-12T06:35 | Triple EMA stack | buy | ETH-USD | 12.82 | — | entry signal |
| 2026-10-12T06:30 | ADX DI cross | buy | ETH-USD | 13.83 | — | entry signal |
| 2026-10-12T06:25 | RSI momentum | sell | ETH-USD | 10.47 | -0.05 | exit signal |
| 2026-10-12T06:25 | Trend pullback | sell | ETH-USD | 10.47 | -0.09 | exit signal |
| 2026-10-12T06:25 | Triple EMA stack | sell | ETH-USD | 10.29 | -0.05 | exit signal |
| 2026-10-12T06:20 | Donchian 55/20 | sell | SOL-USD | 13.69 | -0.13 | exit signal |
| 2026-10-12T06:20 | Donchian 55/20 | sell | DOGE-USD | 17.02 | -0.13 | stop-loss |
| 2026-10-12T06:20 | Donchian 20/10 | sell | SOL-USD | 13.40 | -0.13 | exit signal |
| 2026-10-12T06:20 | RSI momentum | sell | BTC-USD | 10.47 | -0.09 | exit signal |
| 2026-10-12T06:20 | Trend pullback | sell | SOL-USD | 10.46 | -0.11 | exit signal |
| 2026-10-12T06:20 | Triple EMA stack | sell | SOL-USD | 10.25 | -0.07 | exit signal |
| 2026-10-12T06:20 | EMA 20/50 cross | sell | BTC-USD | 17.09 | -0.15 | stop-loss |
| 2026-10-12T06:15 | Donchian 55/20 | buy | DOGE-USD | 17.14 | — | entry |
| 2026-10-12T06:15 | RSI momentum | sell | SOL-USD | 10.46 | -0.05 | exit signal |
| 2026-10-12T06:15 | Supertrend | sell | SOL-USD | 12.54 | -0.04 | exit signal |
| 2026-10-12T06:15 | Triple EMA stack | sell | DOGE-USD | 10.28 | -0.03 | exit signal |
| 2026-10-12T06:15 | Triple EMA stack | sell | BTC-USD | 12.83 | -0.09 | exit signal |
| 2026-10-12T06:10 | Donchian 55/20 | sell | DOGE-USD | 13.70 | -0.13 | stop-loss |
| 2026-10-12T06:10 | Donchian 20/10 | sell | DOGE-USD | 10.76 | -0.06 | exit signal |
| 2026-10-12T06:10 | RSI momentum | sell | DOGE-USD | 13.07 | -0.08 | exit signal |
| 2026-10-12T06:10 | Trend pullback | sell | DOGE-USD | 13.08 | -0.13 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 06:55:05.000160+00:00 -> 2026-10-12 07:05:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
