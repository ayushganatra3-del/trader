# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T00:25:05.000188+00:00 · 19612 ticks

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

Today: 315 decisions in 63 calls, $0.0044 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T00:25 | 1 / 3 / 1 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T00:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T00:25 | 2 / 2 / 1 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.44 | -2.25 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.07 | 2.07 | 14 | 57.1 | -15.28 | -2.49 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.11 | 0.11 | 0 | — | 30.39 | 3.57 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 89 | 55.1 | -9.47 | -1.80 | -14.61 | 339 |
| 19 | Donchian 55/20 · 1h | breakout | 99.11 | -0.89 | 28 | 14.3 | 12.92 | 1.61 | -16.96 | 113 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.30 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.13 | -6.51 | -25.39 | 167 |
| 27 | EMA 20/50 cross · 1h | trend | 96.68 | -3.32 | 40 | 12.5 | 5.39 | 0.80 | -19.85 | 138 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.86 | -2.41 | -9.94 | 257 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | 0.09 | 0.18 | -13.84 | 250 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.91 | -0.22 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.84 | -4.16 | 114 | 23.7 | -14.68 | -2.33 | -17.27 | 467 |
| 34 | Supertrend · 1h | trend | 95.38 | -4.62 | 53 | 13.2 | 0.56 | 0.26 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -10.04 | -1.58 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.43 | -6.57 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.19 | -0.37 | -9.03 | 144 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -3.50 | -0.45 | -12.68 | 431 |
| 42 | Bollinger reversion · 1h | reversion | 92.78 | -7.22 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 4.00 | 0.68 | -17.13 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.10 | -7.90 | 58 | 19.0 | 7.35 | 1.15 | -12.60 | 123 |
| 45 | Ichimoku · 1h | trend | 91.94 | -8.06 | 44 | 18.2 | -1.15 | 0.06 | -21.18 | 124 |
| 46 | Williams %R · 1h | reversion | 91.56 | -8.44 | 126 | 47.6 | -23.49 | -3.99 | -26.91 | 513 |
| 47 | Bollinger breakout · 1h | breakout | 91.25 | -8.75 | 72 | 27.8 | 5.69 | 0.89 | -13.62 | 289 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.36 | -0.94 | -26.47 | 243 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 118 | 33.1 | -25.88 | -4.99 | -27.96 | 506 |
| 51 | CCI reversion · 1h | reversion | 89.97 | -10.03 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 412 |
| 52 | VWAP momentum · 1h | momentum | 89.51 | -10.49 | 283 | 21.9 | -32.26 | -4.77 | -39.17 | 1276 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.94 | -1.47 | -28.57 | 325 |
| 55 | Donchian 20/10 · 1h | breakout | 88.67 | -11.33 | 60 | 18.3 | -1.10 | 0.07 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -29.89 | -4.98 | -36.60 | 699 |
| 57 | MACD zero-line · 1h | trend | 88.13 | -11.87 | 66 | 18.2 | -7.12 | -0.78 | -20.88 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.88 | -12.12 | 104 | 13.5 | -9.38 | -1.06 | -21.96 | 341 |
| 60 | Three white soldiers | momentum | 87.18 | -12.82 | 142 | 17.6 | -48.03 | -22.82 | -48.04 | 589 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -12.34 | -1.43 | -25.51 | 220 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.12 | -1.21 | -23.48 | 414 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.73 | -16.36 | -73.90 | 1677 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 373 | 27.3 | -72.44 | -17.91 | -72.46 | 1488 |
| 65 | Squeeze breakout | breakout | 71.09 | -28.91 | 333 | 15.6 | -61.88 | -17.77 | -62.22 | 1228 |
| 66 | Volume breakout | breakout | 70.40 | -29.60 | 267 | 14.2 | -62.31 | -17.62 | -62.56 | 904 |
| 67 | Donchian 55/20 | breakout | 70.19 | -29.81 | 337 | 18.7 | -67.33 | -14.20 | -67.48 | 1294 |
| 68 | EMA 20/50 cross | trend | 69.24 | -30.76 | 340 | 20.3 | -76.73 | -15.15 | -76.74 | 1457 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.16 | -15.78 | -71.22 | 1426 |
| 70 | Supertrend | trend | 63.47 | -36.53 | 469 | 20.3 | -85.88 | -20.70 | -85.96 | 1913 |
| 71 | Keltner breakout | breakout | 62.64 | -37.36 | 457 | 14.9 | -83.67 | -27.02 | -83.75 | 1852 |
| 72 | Ichimoku | trend | 60.38 | -39.62 | 411 | 10.5 | -81.56 | -22.79 | -81.75 | 1748 |
| 73 | AI bee: Boozy | ai | 60.23 | -39.77 | 257 | 5.1 | — | — | — | — |
| 74 | Z-score reversion | reversion | 58.98 | -41.02 | 514 | 22.2 | -85.39 | -22.92 | -85.39 | 2085 |
| 75 | MFI reversion | reversion | 58.35 | -41.65 | 524 | 20.8 | -87.58 | -27.94 | -87.61 | 2124 |
| 76 | AI bee: Bizzy | ai | 56.95 | -43.05 | 851 | 8.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.94 | -44.06 | 551 | 10.3 | -89.18 | -34.21 | -89.18 | 2116 |
| 78 | Donchian 20/10 | breakout | 54.96 | -45.04 | 644 | 18.3 | -90.79 | -25.70 | -90.82 | 2670 |
| 79 | Trend pullback | trend | 53.83 | -46.17 | 595 | 14.6 | -91.07 | -26.73 | -91.08 | 2342 |
| 80 | RSI momentum | momentum | 53.57 | -46.43 | 616 | 17.2 | -90.31 | -25.32 | -90.35 | 2387 |
| 81 | MACD zero-line | trend | 52.78 | -47.22 | 601 | 14.8 | -91.46 | -29.50 | -91.46 | 2366 |
| 82 | Triple EMA stack | trend | 52.39 | -47.61 | 641 | 15.6 | -93.17 | -29.67 | -93.17 | 2626 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.59 | -98.64 | 5386 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.33 | -32.79 | -97.33 | 3549 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -35.40 | -96.44 | 3620 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.21 | -25.39 | -94.21 | 2695 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.21 | -99.34 | 5686 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.44 | -31.56 | -96.44 | 3635 |
| 89 | Bollinger breakout | breakout | 50.25 | -49.75 | 680 | 14.6 | -93.48 | -32.48 | -93.50 | 2821 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.07 | -99.73 | 6204 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.44 | -97.36 | 3694 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.37 | -98.46 | 4705 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.44 | -99.52 | 6147 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.82 | -32.84 | -95.83 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.62 | -33.74 | -95.63 | 4083 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.89 | -99.90 | 8321 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T00:25 | Donchian 55/20 | buy | ETH-USD | 17.56 | — | entry signal |
| 2026-10-12T00:25 | Triple EMA stack | buy | DOGE-USD | 2.61 | — | rebalance up |
| 2026-10-12T00:25 | Triple EMA stack | sell | BTC-USD | 2.61 | -0.01 | rebalance down |
| 2026-10-12T00:20 | Bollinger breakout | sell | XRP-USD | 12.51 | -0.09 | exit signal |
| 2026-10-12T00:20 | MACD zero-line | sell | XRP-USD | 13.13 | -0.08 | exit signal |
| 2026-10-12T00:17 | EMA 20/50 cross | buy | DOGE-USD | 3.45 | — | rebalance up |
| 2026-10-12T00:17 | EMA 20/50 cross | sell | BTC-USD | 3.45 | -0.02 | rebalance down |
| 2026-10-12T00:15 | Bollinger breakout | buy | ETH-USD | 12.58 | — | entry signal |
| 2026-10-12T00:15 | MACD zero-line | buy | XRP-USD | 2.61 | — | rebalance up |
| 2026-10-12T00:15 | MACD zero-line | buy | DOGE-USD | 10.55 | — | rebalance up |
| 2026-10-12T00:15 | MACD zero-line | sell | SOL-USD | 13.16 | -0.08 | exit signal |
| 2026-10-12T00:15 | EMA 20/50 cross | buy | DOGE-USD | 3.54 | — | entry |
| 2026-10-12T00:15 | EMA 20/50 cross | sell | ETH-USD | 3.46 | -0.02 | rebalance down |
| 2026-10-12T00:13 | AI bee: Bizzy | sell | SOL-USD | 7.99 | -0.06 | Jev: sell (sell p=0.91) after 10 min |
| 2026-10-12T00:03 | AI bee: Bizzy | buy | SOL-USD | 8.05 | — | Jev: buy (buy p=0.56) |
| 2026-10-12T00:00 | Triple EMA stack | buy | DOGE-USD | 2.67 | — | entry signal |
| 2026-10-12T00:00 | Triple EMA stack | sell | ETH-USD | 2.62 | -0.01 | rebalance down |
| 2026-10-11T23:55 | Bollinger breakout | buy | BTC-USD | 12.59 | — | entry signal |
| 2026-10-11T23:55 | Donchian 55/20 | buy | BTC-USD | 17.57 | — | entry signal |
| 2026-10-11T23:52 | AI bee: Bizzy | sell | DOGE-USD | 8.83 | -0.05 | Jev: sell (sell p=0.59) after 12 min |
| 2026-10-11T23:50 | Trend pullback | buy | SOL-USD | 13.46 | — | entry signal |
| 2026-10-11T23:45 | Triple EMA stack | buy | SOL-USD | 13.11 | — | entry signal |
| 2026-10-11T23:40 | AI bee: Bizzy | buy | DOGE-USD | 8.88 | — | Jev: buy (buy p=0.62) |
| 2026-10-11T23:40 | Bollinger breakout | buy | XRP-USD | 12.60 | — | entry signal |
| 2026-10-11T23:40 | EMA 20/50 cross | buy | SOL-USD | 17.33 | — | entry signal |
| 2026-10-11T23:35 | RSI momentum | buy | XRP-USD | 13.40 | — | entry signal |
| 2026-10-11T23:35 | Triple EMA stack | buy | XRP-USD | 13.12 | — | entry signal |
| 2026-10-11T23:35 | EMA 20/50 cross | buy | XRP-USD | 17.34 | — | entry signal |
| 2026-10-11T23:30 | Trend pullback | buy | BTC-USD | 13.47 | — | entry signal |
| 2026-10-11T23:30 | Supertrend | buy | XRP-USD | 15.87 | — | entry signal |
| 2026-10-11T23:30 | MACD zero-line | buy | DOGE-USD | 2.67 | — | entry signal |
| 2026-10-11T23:30 | MACD zero-line | sell | XRP-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-11T23:25 | Trend pullback | buy | ETH-USD | 13.48 | — | entry signal |
| 2026-10-11T23:20 | ADX DI cross | sell | SOL-USD | 13.90 | -0.11 | exit signal |
| 2026-10-11T23:10 | MFI reversion | sell | DOGE-USD | 14.56 | -0.06 | exit signal |
| 2026-10-11T23:10 | EMA 20/50 cross | buy | BTC-USD | 17.35 | — | entry signal |
| 2026-10-11T23:05 | Z-score reversion | sell | DOGE-USD | 14.76 | -0.05 | exit signal |
| 2026-10-11T23:05 | Bollinger breakout | buy | DOGE-USD | 12.61 | — | entry signal |
| 2026-10-11T23:05 | Donchian 20/10 | buy | ETH-USD | 13.76 | — | entry signal |
| 2026-10-11T23:05 | Donchian 20/10 | buy | DOGE-USD | 13.76 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 00:25:05.000188+00:00 -> 2026-10-12 00:35:05.000188+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
