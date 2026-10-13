# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T13:25:05.000174+00:00 · 21373 ticks

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
| Copy: Insider buying | 2026-10-13 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 9780 decisions in 1956 calls, $0.1369 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T13:25 | 0 / 5 / 0 | PLTR 15%, AMD 15%, SOL-USD 15% |  |
| Breezy | 2026-10-13T13:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T13:25 | 4 / 1 / 0 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.64 | 2.64 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 101.93 | 1.93 | 16 | 50.0 | -15.07 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.81 | -2.62 | -13.79 | 116 |
| 6 | Hold SPY | benchmark | 101.16 | 1.16 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.95 | 0.95 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.38 | 0.38 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.36 | 0.36 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 15 | Hold BTC | benchmark | 99.57 | -0.43 | 0 | — | 30.62 | 3.55 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 6.86 | 3.19 | -1.52 | 78 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.10 | -0.90 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.04 | -1.96 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 97.88 | -2.12 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.75 | -2.25 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.61 | -2.39 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.17 | -2.83 | 105 | 52.4 | -10.68 | -1.98 | -13.91 | 339 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 96.77 | -3.23 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 26 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 27 | Z-score reversion · 1h | reversion | 96.44 | -3.56 | 47 | 44.7 | 3.36 | 0.79 | -8.60 | 165 |
| 28 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -9.75 | -3.70 | -10.90 | 299 |
| 29 | ADX DI cross · 1h | trend | 96.15 | -3.85 | 63 | 19.0 | -5.47 | -0.85 | -13.79 | 251 |
| 30 | MACD cross · 1h | trend | 95.49 | -4.51 | 125 | 24.0 | -9.92 | -1.53 | -17.79 | 459 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 32 | Parabolic SAR · 1h | trend | 95.15 | -4.85 | 86 | 22.1 | 2.15 | 0.46 | -21.52 | 288 |
| 33 | EMA 20/50 cross · 1h | trend | 95.09 | -4.91 | 45 | 15.6 | 5.16 | 0.78 | -23.78 | 135 |
| 34 | Supertrend · 1h | trend | 94.31 | -5.69 | 58 | 13.8 | 1.10 | 0.33 | -19.13 | 217 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.38 | -6.62 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.20 | -6.80 | 151 | 32.5 | -7.11 | -1.05 | -16.91 | 129 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.37 | -7.63 | 66 | 15.2 | -0.71 | 0.12 | -23.02 | 230 |
| 40 | Connors RSI(2) · 1h | reversion | 92.28 | -7.72 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.26 | -7.74 | 439 | 17.8 | 0.20 | 0.17 | -12.85 | 403 |
| 42 | Volume breakout · 1h | breakout | 91.54 | -8.46 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 43 | RSI(14) reversion · 1h | reversion | 91.40 | -8.60 | 36 | 30.6 | -1.72 | -0.26 | -9.40 | 140 |
| 44 | Ichimoku · 1h | trend | 90.79 | -9.21 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.70 | -9.30 | 93 | 37.6 | -23.67 | -5.71 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.69 | -9.31 | 74 | 28.4 | 8.33 | 1.20 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.47 | -9.53 | 71 | 15.5 | -7.08 | -0.61 | -27.18 | 237 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 88.96 | -11.04 | 141 | 46.1 | -25.06 | -4.06 | -28.82 | 502 |
| 50 | CCI reversion · 1h | reversion | 88.77 | -11.23 | 114 | 45.6 | -9.96 | -1.31 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.48 | -11.52 | 150 | 18.7 | -12.48 | -1.18 | -34.15 | 318 |
| 52 | VWAP momentum · 1h | momentum | 88.01 | -11.98 | 311 | 23.2 | -32.70 | -4.84 | -40.29 | 1252 |
| 53 | Max aggression: 5-day momentum | meta | 87.87 | -12.13 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.82 | -12.18 | 130 | 30.8 | -28.76 | -5.47 | -29.02 | 500 |
| 55 | Donchian 20/10 · 1h | breakout | 87.48 | -12.52 | 63 | 17.5 | -0.69 | 0.12 | -19.51 | 215 |
| 56 | MACD zero-line · 1h | trend | 87.25 | -12.75 | 67 | 17.9 | -20.18 | -3.72 | -21.66 | 229 |
| 57 | Heikin-Ashi · 1h | trend | 87.02 | -12.97 | 158 | 27.2 | -30.39 | -5.03 | -38.02 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 86.76 | -13.24 | 109 | 12.8 | -7.30 | -0.74 | -23.22 | 330 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.42 | -13.58 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.16 | -23.13 | -48.16 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.30 | -14.70 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.38 | -15.90 | -74.72 | 1659 |
| 64 | Squeeze breakout | breakout | 69.22 | -30.78 | 356 | 15.4 | -62.07 | -17.94 | -62.07 | 1219 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.28 | -17.33 | -61.28 | 888 |
| 66 | EMA 20/50 cross | trend | 67.43 | -32.57 | 362 | 20.4 | -76.12 | -14.86 | -76.23 | 1429 |
| 67 | RSI(14) reversion | reversion | 66.94 | -33.06 | 442 | 26.5 | -74.30 | -17.47 | -74.34 | 1492 |
| 68 | Donchian 55/20 | breakout | 66.43 | -33.57 | 365 | 17.5 | -68.07 | -14.19 | -69.19 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -72.49 | -15.40 | -72.52 | 1413 |
| 70 | Keltner breakout | breakout | 60.63 | -39.37 | 492 | 15.4 | -82.87 | -25.92 | -83.05 | 1831 |
| 71 | Supertrend | trend | 60.24 | -39.76 | 510 | 20.0 | -85.71 | -20.31 | -85.87 | 1892 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.54 | -43.46 | 440 | 9.8 | -82.11 | -22.69 | -82.11 | 1728 |
| 74 | MFI reversion | reversion | 54.24 | -45.76 | 634 | 19.9 | -87.89 | -27.51 | -87.91 | 2113 |
| 75 | AI bee: Bizzy | ai | 54.22 | -45.78 | 914 | 8.2 | — | — | — | — |
| 76 | Z-score reversion | reversion | 53.04 | -46.96 | 590 | 21.9 | -86.29 | -22.48 | -86.32 | 2080 |
| 77 | ADX DI cross | trend | 52.72 | -47.28 | 618 | 10.5 | -89.12 | -33.91 | -89.19 | 2114 |
| 78 | Donchian 20/10 | breakout | 52.14 | -47.86 | 693 | 18.0 | -90.57 | -24.98 | -90.68 | 2638 |
| 79 | MACD zero-line | trend | 51.22 | -48.78 | 640 | 15.2 | -91.22 | -28.66 | -91.31 | 2341 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -28.92 | -98.52 | 5289 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.03 | -28.88 | -93.07 | 2589 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.36 | -90.34 | 2355 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.34 | -26.49 | -91.34 | 2329 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.26 | -31.64 | -97.29 | 3513 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -34.66 | -96.31 | 3576 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.32 | -25.31 | -94.32 | 2633 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.64 | -99.37 | 5639 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -31.48 | -96.39 | 3609 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.71 | -99.72 | 6137 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.29 | -37.12 | -97.29 | 3651 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -36.31 | -98.53 | 4668 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.23 | -31.79 | -93.23 | 2787 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.37 | -99.54 | 6111 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -32.93 | -96.05 | 3732 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.99 | -95.74 | 4044 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.88 | -99.89 | 8201 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T13:25 | Donchian 20/10 | buy | XRP-USD | 13.06 | — | entry signal |
| 2026-10-13T13:25 | Donchian 20/10 | buy | DOGE-USD | 13.06 | — | entry signal |
| 2026-10-13T13:25 | MACD zero-line | buy | SOL-USD | 12.82 | — | entry signal |
| 2026-10-13T13:25 | MACD zero-line | buy | ETH-USD | 12.82 | — | entry signal |
| 2026-10-13T13:12 | AI bee: Bizzy | buy | SOL-USD | 7.95 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T13:05 | AI bee: Bizzy | sell | XRP-USD | 7.95 | -0.08 | Jev: sell (sell p=0.82) after 11 min |
| 2026-10-13T13:05 | ADX DI cross | sell | SOL-USD | 13.09 | -0.12 | exit signal |
| 2026-10-13T13:05 | ADX DI cross | sell | ETH-USD | 13.12 | -0.10 | exit signal |
| 2026-10-13T13:05 | Supertrend | buy | XRP-USD | 3.00 | — | rebalance up |
| 2026-10-13T13:05 | Supertrend | sell | BTC-USD | 3.00 | -0.04 | rebalance down |
| 2026-10-13T13:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.84 | — | entry signal |
| 2026-10-13T12:54 | AI bee: Bizzy | buy | XRP-USD | 8.03 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T12:52 | Supertrend | buy | XRP-USD | 3.00 | — | rebalance up |
| 2026-10-13T12:52 | Supertrend | sell | ETH-USD | 3.00 | -0.03 | rebalance down |
| 2026-10-13T12:50 | Z-score reversion | sell | XRP-USD | 13.35 | 0.03 | exit signal |
| 2026-10-13T12:50 | Z-score reversion | sell | ETH-USD | 13.35 | -0.03 | exit signal |
| 2026-10-13T12:50 | RSI(14) reversion | sell | XRP-USD | 16.97 | 0.05 | take-profit |
| 2026-10-13T12:50 | Supertrend | buy | XRP-USD | 3.05 | — | entry signal |
| 2026-10-13T12:50 | Supertrend | sell | DOGE-USD | 3.05 | -0.02 | rebalance down |
| 2026-10-13T12:50 | MACD zero-line | buy | XRP-USD | 12.84 | — | entry signal |
| 2026-10-13T12:50 | MACD zero-line | buy | DOGE-USD | 12.84 | — | entry signal |
| 2026-10-13T12:40 | ADX DI cross | buy | SOL-USD | 13.21 | — | entry signal |
| 2026-10-13T12:30 | ADX DI cross | buy | ETH-USD | 13.22 | — | entry signal |
| 2026-10-13T12:30 | ADX DI cross | buy | DOGE-USD | 13.22 | — | entry signal |
| 2026-10-13T12:22 | AI bee: Bizzy | sell | XRP-USD | 7.55 | -0.07 | Jev: sell (sell p=0.90) after 12 min |
| 2026-10-13T12:15 | Z-score reversion | sell | DOGE-USD | 13.19 | -0.09 | stop-loss |
| 2026-10-13T12:15 | RSI(14) reversion | sell | DOGE-USD | 16.65 | -0.11 | stop-loss |
| 2026-10-13T12:15 | ADX DI cross | sell | ETH-USD | 13.15 | -0.09 | exit signal |
| 2026-10-13T12:10 | AI bee: Bizzy | buy | XRP-USD | 7.62 | — | Jev: buy (buy p=0.56) |
| 2026-10-13T12:10 | Z-score reversion | buy | DOGE-USD | 13.28 | — | entry |
| 2026-10-13T12:10 | RSI(14) reversion | buy | DOGE-USD | 16.76 | — | entry |
| 2026-10-13T12:10 | ADX DI cross | buy | ETH-USD | 13.24 | — | entry signal |
| 2026-10-13T12:05 | Z-score reversion | sell | DOGE-USD | 13.18 | -0.18 | stop-loss |
| 2026-10-13T12:05 | RSI(14) reversion | sell | DOGE-USD | 16.68 | -0.23 | stop-loss |
| 2026-10-13T12:05 | ADX DI cross | sell | ETH-USD | 10.59 | -0.12 | exit signal |
| 2026-10-13T12:00 | MFI reversion | sell | BTC-USD | 13.52 | -0.13 | stop-loss |
| 2026-10-13T11:55 | MFI reversion | sell | SOL-USD | 13.44 | -0.21 | stop-loss |
| 2026-10-13T11:55 | RSI(14) reversion | sell | SOL-USD | 16.66 | -0.26 | stop-loss |
| 2026-10-13T11:55 | ADX DI cross | sell | XRP-USD | 10.61 | -0.10 | exit signal |
| 2026-10-13T11:55 | ADX DI cross | sell | SOL-USD | 10.55 | -0.16 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 13:25:05.000174+00:00 -> 2026-10-13 13:35:05.000174+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
