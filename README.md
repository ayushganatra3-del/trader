# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T07:25:05.000206+00:00 · 19972 ticks

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

Today: 5712 decisions in 1143 calls, $0.0800 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T07:25 | 0 / 4 / 1 | SOL-USD 15%, NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T07:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T07:25 | 3 / 2 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| MFI reversion | AAPL | 2.06 | +0.67% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.26 | 3.26 | 37 | 43.2 | -7.53 | -2.28 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.52 | 2.52 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.20 | 2.20 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.00 | 2.00 | 14 | 57.1 | -12.40 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.32 | 1.32 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.24 | 1.24 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.08 | 1.08 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.44 | 0.44 | 0 | — | 30.94 | 3.62 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.75 | -0.25 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.68 | -0.32 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.31 | -0.69 | 28 | 14.3 | 13.32 | 1.65 | -16.96 | 114 |
| 19 | Stochastic reversion · 1h | reversion | 99.11 | -0.89 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.58 | -1.42 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.55 | -1.45 | 0 | — | 11.52 | 1.86 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.79 | -2.21 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.30 | -2.69 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.16 | -2.84 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.03 | -2.97 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | EMA 20/50 cross · 1h | trend | 96.75 | -3.25 | 40 | 12.5 | 6.38 | 0.91 | -19.85 | 136 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.92 | -2.30 | -10.19 | 268 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.29 | -3.71 | 58 | 20.7 | -0.11 | 0.15 | -13.84 | 251 |
| 31 | Parabolic SAR · 1h | trend | 96.25 | -3.75 | 82 | 22.0 | -1.94 | -0.09 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.88 | -4.12 | 115 | 23.5 | -14.64 | -2.32 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.74 | -4.26 | 53 | 13.2 | 2.53 | 0.51 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.48 | -6.52 | 119 | 34.5 | -9.93 | -1.55 | -17.79 | 123 |
| 38 | Squeeze breakout · 1h | breakout | 93.41 | -6.59 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.07 | -6.93 | 26 | 26.9 | -2.19 | -0.37 | -9.03 | 144 |
| 40 | Connors RSI(2) · 1h | reversion | 93.01 | -6.99 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.81 | -7.19 | 392 | 18.4 | -0.68 | 0.02 | -13.35 | 423 |
| 42 | Bollinger reversion · 1h | reversion | 92.73 | -7.27 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.64 | -7.36 | 64 | 15.6 | 5.11 | 0.81 | -17.15 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.34 | -7.66 | 58 | 19.0 | 7.89 | 1.22 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 92.28 | -7.72 | 44 | 18.2 | -0.69 | 0.12 | -21.18 | 125 |
| 46 | Williams %R · 1h | reversion | 91.52 | -8.48 | 126 | 47.6 | -23.63 | -4.02 | -26.91 | 508 |
| 47 | Bollinger breakout · 1h | breakout | 91.20 | -8.80 | 72 | 27.8 | 6.15 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.67 | -9.33 | 69 | 15.9 | -8.25 | -0.80 | -26.49 | 241 |
| 50 | Candlestick reversal · 1h | reversion | 90.36 | -9.63 | 118 | 33.1 | -25.87 | -4.99 | -27.95 | 505 |
| 51 | CCI reversion · 1h | reversion | 89.93 | -10.07 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.48 | -10.52 | 284 | 21.8 | -32.31 | -4.78 | -39.16 | 1279 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.18 | -19.78 | 700 |
| 54 | OBV trend · 1h | momentum | 88.72 | -11.28 | 149 | 18.8 | -12.59 | -1.43 | -28.50 | 325 |
| 55 | Donchian 20/10 · 1h | breakout | 88.69 | -11.31 | 60 | 18.3 | -0.53 | 0.14 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.60 | -11.40 | 138 | 25.4 | -29.85 | -4.97 | -36.59 | 702 |
| 57 | MACD zero-line · 1h | trend | 88.34 | -11.66 | 66 | 18.2 | -6.54 | -0.70 | -20.89 | 239 |
| 58 | EMA 9/21 cross · 1h | trend | 87.93 | -12.07 | 104 | 13.5 | -8.54 | -0.95 | -21.96 | 339 |
| 59 | Max aggression: 5-day momentum | meta | 87.91 | -12.09 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 60 | Keltner breakout · 1h | breakout | 87.04 | -12.96 | 43 | 18.6 | -11.87 | -1.37 | -25.86 | 220 |
| 61 | Three white soldiers | momentum | 86.80 | -13.20 | 147 | 17.0 | -48.59 | -23.32 | -48.61 | 594 |
| 62 | ROC + volume · 1h | momentum | 86.22 | -13.78 | 132 | 21.2 | -9.96 | -1.19 | -23.65 | 416 |
| 63 | ROC + volume | momentum | 74.10 | -25.90 | 400 | 23.0 | -73.02 | -16.58 | -74.12 | 1684 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 375 | 27.5 | -72.10 | -17.80 | -72.15 | 1484 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.17 | -18.00 | -62.18 | 1234 |
| 66 | Volume breakout | breakout | 69.88 | -30.12 | 271 | 14.0 | -62.48 | -17.82 | -62.50 | 906 |
| 67 | EMA 20/50 cross | trend | 68.79 | -31.21 | 346 | 19.9 | -76.62 | -15.16 | -76.71 | 1453 |
| 68 | Donchian 55/20 | breakout | 68.29 | -31.71 | 349 | 18.1 | -68.26 | -14.59 | -68.32 | 1304 |
| 69 | VWAP reversion | reversion | 67.74 | -32.26 | 405 | 25.9 | -71.16 | -15.75 | -71.22 | 1426 |
| 70 | Supertrend | trend | 62.53 | -37.47 | 479 | 19.8 | -85.98 | -20.96 | -86.03 | 1917 |
| 71 | Keltner breakout | breakout | 61.34 | -38.66 | 468 | 14.5 | -83.91 | -27.77 | -83.91 | 1861 |
| 72 | AI bee: Boozy | ai | 59.96 | -40.04 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 59.02 | -40.98 | 420 | 10.2 | -81.86 | -23.17 | -81.86 | 1756 |
| 74 | Z-score reversion | reversion | 58.93 | -41.07 | 516 | 22.1 | -85.05 | -22.69 | -85.06 | 2073 |
| 75 | MFI reversion | reversion | 58.31 | -41.69 | 525 | 20.8 | -87.45 | -27.72 | -87.49 | 2117 |
| 76 | AI bee: Bizzy | ai | 56.17 | -43.84 | 867 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.33 | -44.67 | 558 | 10.2 | -89.23 | -34.81 | -89.26 | 2122 |
| 78 | Donchian 20/10 | breakout | 53.65 | -46.35 | 656 | 18.0 | -90.89 | -26.18 | -90.90 | 2674 |
| 79 | Trend pullback | trend | 52.19 | -47.81 | 618 | 14.6 | -91.33 | -27.26 | -91.35 | 2362 |
| 80 | MACD zero-line | trend | 52.11 | -47.89 | 610 | 14.6 | -91.50 | -29.77 | -91.51 | 2367 |
| 81 | RSI momentum | momentum | 52.11 | -47.89 | 631 | 16.8 | -90.58 | -25.97 | -90.58 | 2400 |
| 82 | Triple EMA stack | trend | 51.19 | -48.81 | 655 | 15.3 | -93.35 | -30.44 | -93.35 | 2638 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -30.91 | -98.63 | 5390 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -33.31 | -97.36 | 3554 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -36.33 | -96.53 | 3639 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.24 | -25.48 | -94.24 | 2696 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.33 | -36.21 | -99.34 | 5686 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.50 | -31.86 | -96.50 | 3645 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.80 | -99.73 | 6208 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.03 | -97.36 | 3698 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.42 | -36.12 | -98.42 | 4697 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.55 | -33.17 | -93.55 | 2827 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -39.67 | -99.51 | 6146 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.72 | -32.74 | -95.73 | 3732 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.58 | -33.74 | -95.59 | 4084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.95 | -99.89 | 8314 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T07:25 | ROC + volume | buy | DOGE-USD | 18.54 | — | entry signal |
| 2026-10-12T07:22 | AI bee: Boozy | sell | ETH-USD | 14.21 | -0.08 | Jev: add (buy p=0.53) |
| 2026-10-12T07:20 | Donchian 20/10 | buy | DOGE-USD | 13.43 | — | entry |
| 2026-10-12T07:20 | Ichimoku | buy | XRP-USD | 14.78 | — | entry signal |
| 2026-10-12T07:20 | Ichimoku | buy | DOGE-USD | 14.78 | — | entry signal |
| 2026-10-12T07:20 | Triple EMA stack | buy | SOL-USD | 2.56 | — | rebalance up |
| 2026-10-12T07:20 | Triple EMA stack | sell | DOGE-USD | 2.56 | -0.01 | rebalance down |
| 2026-10-12T07:19 | AI bee: Bizzy | buy | SOL-USD | 8.56 | — | Jev: buy (buy p=0.61) |
| 2026-10-12T07:17 | AI bee: Bizzy | sell | ETH-USD | 8.07 | -0.05 | Jev: sell (sell p=0.50) after 13 min |
| 2026-10-12T07:17 | RSI momentum | buy | SOL-USD | 2.62 | — | rebalance up |
| 2026-10-12T07:17 | RSI momentum | sell | BTC-USD | 2.62 | -0.01 | rebalance down |
| 2026-10-12T07:15 | Donchian 55/20 | buy | ETH-USD | 17.10 | — | entry signal |
| 2026-10-12T07:15 | RSI momentum | buy | SOL-USD | 5.25 | — | entry signal |
| 2026-10-12T07:15 | RSI momentum | buy | DOGE-USD | 10.45 | — | entry signal |
| 2026-10-12T07:15 | RSI momentum | sell | ETH-USD | 2.62 | -0.01 | rebalance down |
| 2026-10-12T07:15 | Ichimoku | buy | BTC-USD | 14.81 | — | entry signal |
| 2026-10-12T07:15 | Supertrend | buy | DOGE-USD | 3.03 | — | entry signal |
| 2026-10-12T07:10 | Supertrend | buy | SOL-USD | 15.66 | — | entry signal |
| 2026-10-12T07:07 | AI bee: Boozy | buy | ETH-USD | 14.29 | — | Jev: buy (buy p=0.77) |
| 2026-10-12T07:05 | Keltner breakout | buy | ETH-USD | 15.36 | — | entry signal |
| 2026-10-12T07:05 | RSI momentum | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-10-12T07:05 | Supertrend | buy | XRP-USD | 15.67 | — | entry signal |
| 2026-10-12T07:05 | Triple EMA stack | buy | SOL-USD | 5.15 | — | entry signal |
| 2026-10-12T07:05 | Triple EMA stack | sell | ETH-USD | 2.57 | -0.01 | rebalance down |
| 2026-10-12T07:05 | Triple EMA stack | sell | BTC-USD | 2.56 | -0.01 | rebalance down |
| 2026-10-12T07:04 | AI bee: Bizzy | buy | ETH-USD | 8.12 | — | Jev: buy (buy p=0.58) |
| 2026-10-12T07:00 | Keltner breakout | buy | BTC-USD | 15.37 | — | entry signal |
| 2026-10-12T07:00 | Donchian 20/10 | buy | ETH-USD | 13.43 | — | entry signal |
| 2026-10-12T07:00 | Ichimoku | buy | ETH-USD | 14.81 | — | entry signal |
| 2026-10-12T07:00 | MACD zero-line | buy | XRP-USD | 13.03 | — | entry signal |
| 2026-10-12T07:00 | Triple EMA stack | buy | XRP-USD | 12.82 | — | entry signal |
| 2026-10-12T07:00 | Triple EMA stack | buy | DOGE-USD | 12.82 | — | entry signal |
| 2026-10-12T06:55 | RSI momentum | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-12T06:55 | RSI momentum | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-10-12T06:55 | Trend pullback | buy | SOL-USD | 10.37 | — | entry signal |
| 2026-10-12T06:55 | Trend pullback | sell | DOGE-USD | 2.61 | -0.02 | rebalance down |
| 2026-10-12T06:55 | Supertrend | buy | BTC-USD | 15.67 | — | entry signal |
| 2026-10-12T06:50 | Trend pullback | buy | DOGE-USD | 2.62 | — | rebalance up |
| 2026-10-12T06:50 | Trend pullback | sell | SOL-USD | 10.38 | -0.09 | exit signal |
| 2026-10-12T06:50 | Triple EMA stack | buy | BTC-USD | 12.81 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 07:25:05.000206+00:00 -> 2026-10-12 07:35:05.000206+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
