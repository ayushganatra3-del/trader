# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T00:55:05.000145+00:00 · 19633 ticks

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

Today: 630 decisions in 126 calls, $0.0088 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T00:55 | 2 / 3 / 0 | SOL-USD 15%, NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T00:55 | 3 / 2 / 0 | COIN 76% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.27 | 3.27 | 37 | 43.2 | -7.44 | -2.25 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.54 | 2.54 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.22 | 2.22 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.02 | 2.02 | 14 | 57.1 | -15.28 | -2.49 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.34 | 1.34 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.26 | 1.26 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.10 | 1.10 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Hold BTC | benchmark | 100.22 | 0.23 | 0 | — | 30.62 | 3.59 | -8.68 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Max aggression: 1-day momentum | meta | 99.77 | -0.23 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.70 | -0.30 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Stochastic reversion · 1h | reversion | 99.13 | -0.87 | 89 | 55.1 | -9.71 | -1.86 | -14.61 | 340 |
| 19 | Donchian 55/20 · 1h | breakout | 99.06 | -0.94 | 28 | 14.3 | 12.96 | 1.61 | -16.96 | 113 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.60 | -1.40 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.57 | -1.43 | 0 | — | 11.52 | 1.87 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.81 | -2.19 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.61 | -2.39 | 6 | 0.0 | -3.00 | -2.30 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.18 | -2.82 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.05 | -2.95 | 78 | 23.1 | -23.13 | -6.51 | -25.39 | 167 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.86 | -2.41 | -9.94 | 257 |
| 28 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 29 | EMA 20/50 cross · 1h | trend | 96.65 | -3.35 | 40 | 12.5 | 5.43 | 0.81 | -19.85 | 138 |
| 30 | ADX DI cross · 1h | trend | 96.31 | -3.69 | 58 | 20.7 | 0.09 | 0.18 | -13.84 | 250 |
| 31 | Parabolic SAR · 1h | trend | 96.27 | -3.73 | 82 | 22.0 | -2.90 | -0.22 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.12 | -5.08 | -9.83 | 229 |
| 33 | MACD cross · 1h | trend | 95.82 | -4.18 | 114 | 23.7 | -14.66 | -2.33 | -17.27 | 467 |
| 34 | Supertrend · 1h | trend | 95.40 | -4.60 | 53 | 13.2 | 0.61 | 0.27 | -18.22 | 211 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.05 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.50 | -6.50 | 119 | 34.5 | -10.04 | -1.58 | -17.79 | 126 |
| 38 | Squeeze breakout · 1h | breakout | 93.42 | -6.58 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.10 | -6.91 | 26 | 26.9 | -2.19 | -0.37 | -9.03 | 144 |
| 40 | Connors RSI(2) · 1h | reversion | 93.01 | -6.99 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.83 | -7.17 | 392 | 18.4 | -4.23 | -0.58 | -12.85 | 424 |
| 42 | Bollinger reversion · 1h | reversion | 92.74 | -7.25 | 78 | 37.2 | -20.86 | -4.95 | -23.26 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.66 | -7.34 | 64 | 15.6 | 4.04 | 0.69 | -17.13 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.11 | -7.89 | 58 | 19.0 | 7.40 | 1.16 | -12.60 | 123 |
| 45 | Ichimoku · 1h | trend | 91.94 | -8.06 | 44 | 18.2 | -1.11 | 0.07 | -21.18 | 124 |
| 46 | Williams %R · 1h | reversion | 91.53 | -8.47 | 126 | 47.6 | -23.49 | -3.99 | -26.91 | 513 |
| 47 | Bollinger breakout · 1h | breakout | 91.22 | -8.78 | 72 | 27.8 | 5.74 | 0.90 | -13.62 | 289 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.69 | -9.31 | 69 | 15.9 | -9.32 | -0.94 | -26.47 | 243 |
| 50 | Candlestick reversal · 1h | reversion | 90.38 | -9.62 | 118 | 33.1 | -25.88 | -4.99 | -27.96 | 506 |
| 51 | CCI reversion · 1h | reversion | 89.94 | -10.06 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 412 |
| 52 | VWAP momentum · 1h | momentum | 89.48 | -10.52 | 283 | 21.9 | -32.23 | -4.76 | -39.17 | 1276 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.19 | -19.81 | 700 |
| 54 | OBV trend · 1h | momentum | 88.73 | -11.27 | 149 | 18.8 | -12.93 | -1.47 | -28.57 | 325 |
| 55 | Donchian 20/10 · 1h | breakout | 88.63 | -11.37 | 60 | 18.3 | -1.08 | 0.07 | -18.15 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.62 | -11.38 | 138 | 25.4 | -29.89 | -4.98 | -36.60 | 699 |
| 57 | MACD zero-line · 1h | trend | 88.09 | -11.90 | 66 | 18.2 | -7.13 | -0.78 | -20.88 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.93 | -12.07 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.86 | -12.14 | 104 | 13.5 | -9.35 | -1.06 | -21.96 | 341 |
| 60 | Three white soldiers | momentum | 87.18 | -12.82 | 142 | 17.6 | -48.03 | -22.82 | -48.04 | 589 |
| 61 | Keltner breakout · 1h | breakout | 87.06 | -12.94 | 43 | 18.6 | -12.30 | -1.43 | -25.51 | 220 |
| 62 | ROC + volume · 1h | momentum | 86.24 | -13.76 | 132 | 21.2 | -10.07 | -1.20 | -23.48 | 414 |
| 63 | ROC + volume | momentum | 74.87 | -25.13 | 395 | 23.3 | -72.73 | -16.36 | -73.90 | 1677 |
| 64 | RSI(14) reversion | reversion | 73.76 | -26.24 | 373 | 27.3 | -72.39 | -17.90 | -72.41 | 1487 |
| 65 | Squeeze breakout | breakout | 70.94 | -29.06 | 333 | 15.6 | -62.03 | -17.89 | -62.29 | 1232 |
| 66 | Volume breakout | breakout | 70.35 | -29.65 | 267 | 14.2 | -62.33 | -17.65 | -62.56 | 905 |
| 67 | Donchian 55/20 | breakout | 70.18 | -29.82 | 337 | 18.7 | -67.32 | -14.20 | -67.48 | 1295 |
| 68 | EMA 20/50 cross | trend | 69.30 | -30.70 | 340 | 20.3 | -76.69 | -15.13 | -76.73 | 1457 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.15 | -15.78 | -71.21 | 1425 |
| 70 | Supertrend | trend | 63.54 | -36.46 | 469 | 20.3 | -85.86 | -20.66 | -85.96 | 1913 |
| 71 | Keltner breakout | breakout | 62.48 | -37.52 | 457 | 14.9 | -83.72 | -27.14 | -83.75 | 1855 |
| 72 | Ichimoku | trend | 60.38 | -39.62 | 411 | 10.5 | -81.56 | -22.79 | -81.75 | 1748 |
| 73 | AI bee: Boozy | ai | 60.17 | -39.83 | 258 | 5.0 | — | — | — | — |
| 74 | Z-score reversion | reversion | 58.98 | -41.02 | 514 | 22.2 | -85.39 | -22.92 | -85.39 | 2085 |
| 75 | MFI reversion | reversion | 58.35 | -41.65 | 524 | 20.8 | -87.58 | -27.94 | -87.61 | 2124 |
| 76 | AI bee: Bizzy | ai | 56.83 | -43.17 | 853 | 8.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 55.89 | -44.11 | 552 | 10.3 | -89.19 | -34.25 | -89.19 | 2116 |
| 78 | Donchian 20/10 | breakout | 54.94 | -45.06 | 644 | 18.3 | -90.77 | -25.69 | -90.80 | 2670 |
| 79 | Trend pullback | trend | 53.75 | -46.25 | 596 | 14.6 | -91.09 | -26.80 | -91.09 | 2344 |
| 80 | RSI momentum | momentum | 53.54 | -46.46 | 616 | 17.2 | -90.28 | -25.31 | -90.32 | 2387 |
| 81 | MACD zero-line | trend | 52.75 | -47.25 | 602 | 14.8 | -91.46 | -29.50 | -91.47 | 2366 |
| 82 | Triple EMA stack | trend | 52.44 | -47.56 | 641 | 15.6 | -93.15 | -29.60 | -93.16 | 2625 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.65 | -98.64 | 5388 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.33 | -32.74 | -97.33 | 3549 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -35.45 | -96.43 | 3621 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.22 | -25.44 | -94.22 | 2697 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -36.23 | -99.34 | 5687 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.44 | -31.60 | -96.44 | 3634 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.22 | -99.73 | 6206 |
| 90 | Bollinger breakout | breakout | 50.13 | -49.87 | 681 | 14.5 | -93.50 | -32.57 | -93.50 | 2823 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.44 | -97.36 | 3695 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.37 | -98.46 | 4705 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.47 | -99.52 | 6148 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.83 | -32.83 | -95.83 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.62 | -33.74 | -95.63 | 4083 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.01 | -99.90 | 8320 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T00:55 | Trend pullback | buy | DOGE-USD | 8.04 | — | rebalance up |
| 2026-10-12T00:55 | Trend pullback | sell | XRP-USD | 13.37 | -0.09 | exit signal |
| 2026-10-12T00:53 | AI bee: Bizzy | sell | ETH-USD | 8.42 | -0.04 | Jev: sell (sell p=0.55) after 24 min |
| 2026-10-12T00:52 | RSI momentum | buy | DOGE-USD | 2.68 | — | rebalance up |
| 2026-10-12T00:52 | RSI momentum | sell | BTC-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-12T00:50 | Squeeze breakout | buy | SOL-USD | 17.76 | — | entry signal |
| 2026-10-12T00:50 | Keltner breakout | buy | SOL-USD | 15.65 | — | entry signal |
| 2026-10-12T00:50 | Keltner breakout | buy | ETH-USD | 15.65 | — | entry signal |
| 2026-10-12T00:50 | Bollinger breakout | buy | DOGE-USD | 12.53 | — | entry signal |
| 2026-10-12T00:50 | RSI momentum | buy | DOGE-USD | 2.73 | — | entry signal |
| 2026-10-12T00:50 | RSI momentum | sell | ETH-USD | 2.69 | -0.01 | rebalance down |
| 2026-10-12T00:48 | AI bee: Boozy | sell | ETH-USD | 14.42 | -0.05 | Jev: add (buy p=0.60) |
| 2026-10-12T00:47 | AI bee: Bizzy | buy | SOL-USD | 8.42 | — | Jev: buy (buy p=0.59) |
| 2026-10-12T00:45 | AI bee: Bizzy | sell | BTC-USD | 7.89 | -0.05 | Jev: sell (sell p=0.54) after 13 min |
| 2026-10-12T00:45 | Volume breakout | buy | ETH-USD | 17.60 | — | entry signal |
| 2026-10-12T00:45 | Bollinger breakout | buy | SOL-USD | 12.55 | — | entry signal |
| 2026-10-12T00:45 | Donchian 55/20 | buy | SOL-USD | 17.55 | — | entry signal |
| 2026-10-12T00:45 | Donchian 20/10 | buy | SOL-USD | 13.74 | — | entry signal |
| 2026-10-12T00:44 | Trend pullback | buy | DOGE-USD | 2.68 | — | rebalance up |
| 2026-10-12T00:44 | Trend pullback | sell | BTC-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-12T00:42 | Squeeze breakout | buy | ETH-USD | 17.76 | — | entry signal |
| 2026-10-12T00:42 | Keltner breakout | buy | BTC-USD | 15.66 | — | entry signal |
| 2026-10-12T00:42 | RSI momentum | buy | SOL-USD | 13.40 | — | entry signal |
| 2026-10-12T00:42 | Trend pullback | buy | DOGE-USD | 2.75 | — | entry signal |
| 2026-10-12T00:42 | Trend pullback | sell | ETH-USD | 2.70 | -0.01 | rebalance down |
| 2026-10-12T00:35 | Bollinger breakout | sell | DOGE-USD | 12.51 | -0.09 | exit signal |
| 2026-10-12T00:35 | Trend pullback | buy | XRP-USD | 13.46 | — | entry signal |
| 2026-10-12T00:35 | ADX DI cross | sell | XRP-USD | 13.99 | -0.08 | exit signal |
| 2026-10-12T00:35 | MACD zero-line | sell | DOGE-USD | 13.13 | -0.10 | exit signal |
| 2026-10-12T00:32 | AI bee: Boozy | buy | ETH-USD | 14.47 | — | Jev: buy (buy p=0.76) |
| 2026-10-12T00:32 | AI bee: Bizzy | buy | BTC-USD | 7.93 | — | Jev: buy (buy p=0.56) |
| 2026-10-12T00:30 | Squeeze breakout | buy | BTC-USD | 17.77 | — | entry signal |
| 2026-10-12T00:29 | AI bee: Bizzy | buy | ETH-USD | 8.47 | — | Jev: buy (buy p=0.59) |
| 2026-10-12T00:25 | Donchian 55/20 | buy | ETH-USD | 17.56 | — | entry signal |
| 2026-10-12T00:25 | Triple EMA stack | buy | DOGE-USD | 2.61 | — | rebalance up |
| 2026-10-12T00:25 | Triple EMA stack | sell | BTC-USD | 2.61 | -0.01 | rebalance down |
| 2026-10-12T00:20 | Bollinger breakout | sell | XRP-USD | 12.51 | -0.09 | exit signal |
| 2026-10-12T00:20 | MACD zero-line | sell | XRP-USD | 13.13 | -0.08 | exit signal |
| 2026-10-12T00:17 | EMA 20/50 cross | buy | DOGE-USD | 3.45 | — | rebalance up |
| 2026-10-12T00:17 | EMA 20/50 cross | sell | BTC-USD | 3.45 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 00:55:05.000145+00:00 -> 2026-10-12 01:05:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
