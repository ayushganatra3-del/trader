# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T01:55:05.000154+00:00 · 20809 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.28 (-4.72%)

Closed trades 59, win rate 49.2%, fees £2.28, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.55 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1320 decisions in 264 calls, $0.0186 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T01:55 | 1 / 4 / 0 | XRP-USD 15%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T01:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T01:55 | 5 / 0 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | AAPL | 1.77 | +1.13% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.92 | 2.92 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.21 | 2.21 | 16 | 50.0 | -12.86 | -2.12 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.43 | 1.43 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.21 | -2.74 | -13.79 | 118 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.22 | 1.22 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.65 | 0.65 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.63 | 0.63 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.12 | 0.12 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.36 | -0.64 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 18 | Hold BTC | benchmark | 98.55 | -1.45 | 0 | — | 28.76 | 3.38 | -8.68 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 98.24 | -1.76 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.14 | -1.86 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 98.01 | -1.99 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.88 | -2.12 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.03 | -2.97 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Stochastic reversion · 1h | reversion | 96.86 | -3.14 | 100 | 51.0 | -12.32 | -2.33 | -13.91 | 347 |
| 26 | Z-score reversion · 1h | reversion | 96.69 | -3.31 | 45 | 42.2 | 3.17 | 0.76 | -8.60 | 160 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.48 | -3.52 | 62 | 19.4 | -5.74 | -0.91 | -13.79 | 252 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.56 | -2.71 | -8.94 | 304 |
| 30 | MACD cross · 1h | trend | 95.85 | -4.15 | 125 | 24.0 | -10.87 | -1.69 | -17.79 | 459 |
| 31 | Parabolic SAR · 1h | trend | 95.36 | -4.64 | 86 | 22.1 | 2.00 | 0.44 | -21.52 | 289 |
| 32 | EMA 20/50 cross · 1h | trend | 95.34 | -4.66 | 45 | 15.6 | 4.87 | 0.75 | -23.71 | 136 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 34 | Supertrend · 1h | trend | 94.56 | -5.44 | 58 | 13.8 | 1.32 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.50 | -6.50 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.45 | -6.55 | 151 | 32.5 | -8.02 | -1.21 | -16.91 | 128 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.62 | -7.38 | 66 | 15.2 | -0.63 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.52 | -7.48 | 115 | 43.5 | -18.87 | -6.23 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.50 | -7.50 | 439 | 17.8 | -0.19 | 0.10 | -12.27 | 394 |
| 42 | Volume breakout · 1h | breakout | 91.72 | -8.28 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 43 | RSI(14) reversion · 1h | reversion | 91.61 | -8.39 | 34 | 26.5 | 0.35 | 0.19 | -9.24 | 130 |
| 44 | Ichimoku · 1h | trend | 91.02 | -8.98 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.87 | -9.13 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 46 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 71 | 15.5 | -6.99 | -0.60 | -27.17 | 236 |
| 47 | Bollinger reversion · 1h | reversion | 90.35 | -9.65 | 88 | 35.2 | -24.07 | -5.84 | -24.28 | 315 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 89.00 | -10.99 | 113 | 45.1 | -9.85 | -1.30 | -14.35 | 406 |
| 50 | OBV trend · 1h | momentum | 88.72 | -11.28 | 150 | 18.7 | -12.54 | -1.19 | -34.15 | 318 |
| 51 | Williams %R · 1h | reversion | 88.48 | -11.52 | 136 | 44.9 | -26.83 | -4.41 | -28.66 | 507 |
| 52 | VWAP momentum · 1h | momentum | 88.25 | -11.75 | 311 | 23.2 | -32.85 | -4.87 | -40.15 | 1249 |
| 53 | Max aggression: 5-day momentum | meta | 88.10 | -11.90 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.97 | -12.03 | 130 | 30.8 | -28.42 | -5.40 | -28.95 | 497 |
| 55 | Heikin-Ashi · 1h | trend | 87.72 | -12.28 | 153 | 28.1 | -29.97 | -4.94 | -37.65 | 675 |
| 56 | Donchian 20/10 · 1h | breakout | 87.72 | -12.28 | 63 | 17.5 | -0.60 | 0.13 | -19.51 | 214 |
| 57 | MACD zero-line · 1h | trend | 87.60 | -12.40 | 67 | 17.9 | -21.06 | -3.90 | -21.53 | 232 |
| 58 | EMA 9/21 cross · 1h | trend | 87.11 | -12.89 | 108 | 13.0 | -8.23 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.65 | -13.35 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.46 | -13.54 | 153 | 17.0 | -48.21 | -23.08 | -48.26 | 587 |
| 62 | ROC + volume · 1h | momentum | 85.53 | -14.47 | 164 | 20.1 | -9.21 | -1.07 | -25.13 | 397 |
| 63 | ROC + volume | momentum | 72.37 | -27.63 | 421 | 22.3 | -72.89 | -16.36 | -74.72 | 1661 |
| 64 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.25 | -17.96 | -62.25 | 1222 |
| 65 | Volume breakout | breakout | 69.45 | -30.55 | 279 | 14.7 | -61.51 | -17.37 | -61.51 | 891 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 430 | 27.0 | -73.94 | -17.27 | -74.12 | 1489 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 357 | 19.9 | -76.30 | -14.97 | -76.31 | 1428 |
| 68 | Donchian 55/20 | breakout | 66.63 | -33.37 | 360 | 17.5 | -68.13 | -14.21 | -69.10 | 1289 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.07 | -15.50 | -73.10 | 1422 |
| 70 | Keltner breakout | breakout | 60.30 | -39.70 | 485 | 14.6 | -83.22 | -26.74 | -83.23 | 1835 |
| 71 | AI bee: Boozy | ai | 60.29 | -39.71 | 262 | 5.0 | — | — | — | — |
| 72 | Supertrend | trend | 60.00 | -40.00 | 503 | 19.3 | -85.94 | -20.62 | -86.04 | 1893 |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.13 | -22.67 | -82.13 | 1730 |
| 74 | AI bee: Bizzy | ai | 55.36 | -44.64 | 892 | 8.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 55.33 | -44.67 | 625 | 19.7 | -87.98 | -26.96 | -88.19 | 2119 |
| 76 | Z-score reversion | reversion | 54.70 | -45.30 | 575 | 22.1 | -86.29 | -22.37 | -86.48 | 2083 |
| 77 | ADX DI cross | trend | 53.25 | -46.75 | 600 | 10.0 | -89.19 | -33.77 | -89.19 | 2108 |
| 78 | Donchian 20/10 | breakout | 51.91 | -48.09 | 684 | 17.5 | -90.81 | -25.49 | -90.84 | 2643 |
| 79 | MACD zero-line | trend | 50.84 | -49.16 | 635 | 14.5 | -91.45 | -29.36 | -91.46 | 2346 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.56 | -29.72 | -98.58 | 5307 |
| 81 | Trend pullback | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.12 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.10 | -29.19 | -93.11 | 2588 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.44 | -25.03 | -90.45 | 2360 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -32.36 | -97.36 | 3520 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -34.79 | -96.34 | 3575 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.29 | -25.17 | -94.29 | 2626 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.91 | -99.38 | 5643 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -30.70 | -96.29 | 3591 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.23 | -99.73 | 6144 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.26 | -36.65 | -97.26 | 3646 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -35.90 | -98.55 | 4671 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.33 | -32.03 | -93.34 | 2791 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.75 | -99.55 | 6116 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.08 | -32.51 | -96.09 | 3736 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -33.83 | -95.82 | 4053 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -44.29 | -99.89 | 8200 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T01:55 | ADX DI cross | buy | ETH-USD | 13.31 | — | entry signal |
| 2026-10-13T01:55 | ADX DI cross | buy | DOGE-USD | 13.33 | — | entry signal |
| 2026-10-13T01:50 | MACD zero-line | buy | ETH-USD | 12.72 | — | entry signal |
| 2026-10-13T01:50 | MACD zero-line | buy | DOGE-USD | 12.72 | — | entry signal |
| 2026-10-13T01:45 | MFI reversion | sell | ETH-USD | 13.76 | 0.07 | exit signal |
| 2026-10-13T01:45 | Z-score reversion | sell | ETH-USD | 10.98 | 0.08 | exit signal |
| 2026-10-13T01:45 | RSI(14) reversion | sell | SOL-USD | 17.24 | 0.09 | exit signal |
| 2026-10-13T01:42 | Supertrend | buy | SOL-USD | 2.99 | — | rebalance up |
| 2026-10-13T01:42 | Supertrend | sell | XRP-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-13T01:40 | Supertrend | buy | SOL-USD | 5.98 | — | rebalance up |
| 2026-10-13T01:40 | Supertrend | sell | DOGE-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-13T01:40 | Supertrend | sell | BTC-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-13T01:40 | MACD zero-line | buy | XRP-USD | 12.72 | — | entry signal |
| 2026-10-13T01:38 | AI bee: Boozy | sell | ETH-USD | 14.16 | -0.05 | Jev: add (buy p=0.56) |
| 2026-10-13T01:37 | AI bee: Bizzy | sell | ETH-USD | 8.25 | -0.03 | Jev: sell (sell p=0.50) after 15 min |
| 2026-10-13T01:35 | Z-score reversion | sell | BTC-USD | 10.93 | 0.02 | exit signal |
| 2026-10-13T01:35 | Donchian 20/10 | buy | ETH-USD | 12.95 | — | entry signal |
| 2026-10-13T01:35 | ADX DI cross | buy | BTC-USD | 13.32 | — | entry signal |
| 2026-10-13T01:35 | Supertrend | buy | SOL-USD | 3.01 | — | entry signal |
| 2026-10-13T01:35 | Supertrend | sell | ETH-USD | 3.01 | -0.01 | rebalance down |
| 2026-10-13T01:35 | MACD zero-line | buy | BTC-USD | 12.73 | — | entry signal |
| 2026-10-13T01:31 | MFI reversion | buy | XRP-USD | 8.13 | — | rebalance up |
| 2026-10-13T01:31 | MFI reversion | buy | SOL-USD | 2.77 | — | rebalance up |
| 2026-10-13T01:31 | MFI reversion | buy | DOGE-USD | 2.76 | — | rebalance up |
| 2026-10-13T01:31 | MFI reversion | sell | BTC-USD | 13.66 | 0.03 | exit signal |
| 2026-10-13T01:31 | ADX DI cross | sell | BTC-USD | 13.27 | -0.09 | exit signal |
| 2026-10-13T01:25 | MFI reversion | buy | XRP-USD | 2.75 | — | rebalance up |
| 2026-10-13T01:25 | MFI reversion | sell | DOGE-USD | 2.75 | 0.01 | rebalance down |
| 2026-10-13T01:22 | AI bee: Boozy | buy | ETH-USD | 14.21 | — | Jev: buy (buy p=0.77) |
| 2026-10-13T01:22 | AI bee: Bizzy | buy | ETH-USD | 8.29 | — | Jev: buy (buy p=0.60) |
| 2026-10-13T01:20 | Z-score reversion | sell | XRP-USD | 13.60 | 0.08 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | buy | SOL-USD | 3.47 | — | rebalance up |
| 2026-10-13T01:20 | RSI(14) reversion | sell | XRP-USD | 13.75 | 0.06 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | sell | ETH-USD | 13.73 | 0.04 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | sell | DOGE-USD | 13.76 | 0.07 | exit signal |
| 2026-10-13T01:20 | RSI(14) reversion | sell | BTC-USD | 13.71 | 0.04 | take-profit |
| 2026-10-13T01:20 | Three white soldiers | buy | BTC-USD | 21.61 | — | entry signal |
| 2026-10-13T01:20 | Keltner breakout | buy | BTC-USD | 15.08 | — | entry signal |
| 2026-10-13T01:20 | Donchian 20/10 | buy | XRP-USD | 12.97 | — | entry signal |
| 2026-10-13T01:20 | Donchian 20/10 | buy | DOGE-USD | 12.97 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 01:55:05.000154+00:00 -> 2026-10-13 02:05:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
