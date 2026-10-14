# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T13:25:05.000133+00:00 · 22500 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.12 (-4.88%)

Closed trades 64, win rate 46.9%, fees £2.37, max drawdown -5.38%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-13)

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 21.14 · VIX 15.27 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 9787 decisions in 1958 calls, $0.1369 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T13:25 | 0 / 3 / 2 | AMD 14% |  |
| Breezy | 2026-10-14T13:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T13:25 | 2 / 3 / 0 | COIN 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Three white soldiers | NVDA | 1.77 | +1.00% | 3 |
| ROC + volume | META | 1.74 | +2.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.06 | 3.06 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.12 | -2.70 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.76 | 1.76 | 18 | 50.0 | -15.67 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.66 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 100.99 | 0.99 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.36 | 0.36 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.79 | -0.21 | 0 | — | 4.59 | 1.77 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.78 | -0.22 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Timing: Nasdaq FTD · TQQQ | daily | 98.90 | -1.10 | 0 | — | -8.33 | -1.50 | -15.27 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.35 | -1.65 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 17 | Hold BTC | benchmark | 98.32 | -1.68 | 0 | — | 28.89 | 3.35 | -8.68 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.73 | -2.27 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.42 | -2.58 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.32 | -2.68 | 5 | 0.0 | 0.46 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.49 | -3.05 | -9.28 | 306 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | Stochastic reversion · 1h | reversion | 96.20 | -3.80 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 26 | ADX DI cross · 1h | trend | 96.00 | -4.00 | 66 | 18.2 | -11.82 | -2.19 | -14.81 | 255 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.73 | -4.27 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | EMA 20/50 cross · 1h | trend | 95.32 | -4.68 | 45 | 15.6 | 9.86 | 1.25 | -20.35 | 137 |
| 29 | Max aggression: 1-day momentum | meta | 95.31 | -4.69 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 30 | Z-score reversion · 1h | reversion | 95.18 | -4.82 | 52 | 44.2 | 2.58 | 0.64 | -8.60 | 158 |
| 31 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.34 | -4.71 | -8.52 | 234 |
| 32 | MACD cross · 1h | trend | 95.05 | -4.95 | 138 | 22.5 | -9.12 | -1.18 | -19.25 | 459 |
| 33 | Squeeze breakout · 1h | breakout | 93.93 | -6.07 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 34 | Supertrend · 1h | trend | 93.54 | -6.46 | 60 | 13.3 | 2.02 | 0.45 | -20.64 | 212 |
| 35 | Parabolic SAR · 1h | trend | 93.54 | -6.46 | 91 | 22.0 | 1.44 | 0.37 | -22.84 | 289 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -3.02 | -0.96 | -5.87 | 114 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.56 | 2.17 | -6.74 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.57 | -7.43 | 66 | 15.2 | 1.09 | 0.34 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.48 | -7.51 | 165 | 31.5 | -7.86 | -1.21 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.97 | -8.03 | 127 | 42.5 | -20.34 | -6.01 | -22.90 | 253 |
| 41 | Ichimoku · 1h | trend | 91.25 | -8.75 | 48 | 16.7 | 1.85 | 0.42 | -22.34 | 125 |
| 42 | RSI(14) reversion · 1h | reversion | 91.21 | -8.79 | 38 | 34.2 | 5.81 | 1.33 | -9.40 | 125 |
| 43 | Agent (ML meta-label) | meta | 91.02 | -8.98 | 485 | 18.1 | 2.21 | 0.53 | -11.82 | 369 |
| 44 | Volume breakout · 1h | breakout | 90.66 | -9.34 | 75 | 22.7 | 8.82 | 1.34 | -12.60 | 119 |
| 45 | Bollinger breakout · 1h | breakout | 90.65 | -9.35 | 77 | 28.6 | 7.25 | 1.07 | -14.21 | 278 |
| 46 | Triple EMA stack · 1h | trend | 90.50 | -9.50 | 72 | 15.3 | -7.47 | -0.57 | -32.27 | 239 |
| 47 | Bollinger reversion · 1h | reversion | 89.67 | -10.33 | 99 | 36.4 | -24.14 | -5.81 | -24.90 | 322 |
| 48 | Williams %R · 1h | reversion | 89.38 | -10.62 | 143 | 45.5 | -28.56 | -4.87 | -29.54 | 513 |
| 49 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.03 | -4.51 | -17.60 | 571 |
| 50 | CCI reversion · 1h | reversion | 88.41 | -11.59 | 122 | 44.3 | -9.47 | -1.23 | -14.42 | 416 |
| 51 | OBV trend · 1h | momentum | 88.05 | -11.95 | 159 | 18.2 | -9.41 | -0.78 | -33.87 | 319 |
| 52 | VWAP momentum · 1h | momentum | 87.15 | -12.85 | 334 | 22.8 | -33.17 | -4.91 | -40.83 | 1251 |
| 53 | MACD zero-line · 1h | trend | 87.03 | -12.97 | 72 | 16.7 | -22.64 | -4.41 | -22.67 | 230 |
| 54 | Donchian 20/10 · 1h | breakout | 86.95 | -13.05 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.71 | -13.29 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.66 | -13.34 | 49 | 20.4 | -8.10 | -0.87 | -26.76 | 214 |
| 57 | Heikin-Ashi · 1h | trend | 86.55 | -13.46 | 166 | 26.5 | -28.95 | -4.71 | -38.32 | 672 |
| 58 | EMA 9/21 cross · 1h | trend | 86.43 | -13.57 | 113 | 12.4 | -10.49 | -1.33 | -24.41 | 329 |
| 59 | Candlestick reversal · 1h | reversion | 86.09 | -13.91 | 145 | 30.3 | -28.37 | -5.50 | -28.59 | 468 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.82 | 698 |
| 61 | Three white soldiers | momentum | 85.44 | -14.56 | 169 | 17.8 | -47.79 | -21.88 | -48.03 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.28 | -14.72 | 173 | 20.2 | -8.96 | -1.02 | -24.87 | 399 |
| 63 | ROC + volume | momentum | 68.49 | -31.51 | 469 | 21.7 | -74.00 | -16.59 | -76.01 | 1680 |
| 64 | RSI(14) reversion | reversion | 66.65 | -33.35 | 464 | 27.4 | -73.62 | -16.93 | -73.75 | 1478 |
| 65 | Squeeze breakout | breakout | 66.32 | -33.68 | 386 | 15.0 | -62.91 | -18.07 | -63.12 | 1224 |
| 66 | Volume breakout | breakout | 66.14 | -33.86 | 304 | 13.8 | -62.58 | -17.47 | -62.88 | 894 |
| 67 | EMA 20/50 cross | trend | 63.40 | -36.60 | 405 | 19.5 | -77.10 | -15.03 | -77.62 | 1446 |
| 68 | Donchian 55/20 | breakout | 63.13 | -36.87 | 395 | 16.7 | -69.18 | -14.42 | -70.80 | 1285 |
| 69 | VWAP reversion | reversion | 61.10 | -38.90 | 498 | 25.3 | -72.65 | -15.32 | -72.71 | 1405 |
| 70 | AI bee: Boozy | ai | 59.68 | -40.32 | 272 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 57.08 | -42.92 | 561 | 19.3 | -85.93 | -20.28 | -85.93 | 1912 |
| 72 | Keltner breakout | breakout | 56.39 | -43.61 | 546 | 14.1 | -83.49 | -26.60 | -83.49 | 1849 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.29 | -22.74 | -82.30 | 1721 |
| 74 | AI bee: Bizzy | ai | 52.72 | -47.28 | 967 | 8.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.70 | -47.30 | 680 | 20.1 | -87.73 | -26.70 | -87.75 | 2106 |
| 76 | Z-score reversion | reversion | 51.77 | -48.23 | 630 | 22.9 | -85.88 | -21.69 | -85.89 | 2077 |
| 77 | ADX DI cross | trend | 50.67 | -49.33 | 658 | 10.3 | -89.23 | -33.34 | -89.23 | 2112 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.50 | -28.85 | -98.50 | 5301 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -29.43 | -93.55 | 2618 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.54 | -24.52 | -90.57 | 2375 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.64 | -26.23 | -91.64 | 2352 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -31.75 | -97.37 | 3532 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.59 | -34.88 | -96.59 | 3613 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.61 | -25.37 | -94.61 | 2645 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.35 | -99.38 | 5642 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.03 | -25.47 | -91.03 | 2634 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -30.38 | -96.37 | 3595 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.42 | -99.72 | 6153 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.60 | -29.06 | -91.60 | 2361 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.40 | -36.12 | -97.40 | 3672 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -34.86 | -98.50 | 4669 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.46 | -31.83 | -93.46 | 2800 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.92 | -99.54 | 6123 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -31.79 | -96.01 | 3739 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -33.27 | -95.74 | 4051 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.76 | -99.89 | 8211 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T13:25 | VWAP reversion | buy | SOL-USD | 9.19 | — | entry signal |
| 2026-10-14T13:25 | VWAP reversion | buy | ETH-USD | 12.24 | — | entry signal |
| 2026-10-14T13:25 | VWAP reversion | buy | DOGE-USD | 12.24 | — | entry signal |
| 2026-10-14T13:25 | VWAP reversion | sell | XRP-USD | 3.09 | -0.03 | rebalance down |
| 2026-10-14T13:25 | RSI(14) reversion | buy | XRP-USD | 16.70 | — | entry signal |
| 2026-10-14T13:25 | RSI(14) reversion | buy | DOGE-USD | 16.70 | — | entry signal |
| 2026-10-14T13:25 | RSI(14) reversion | buy | BTC-USD | 16.70 | — | entry signal |
| 2026-10-14T13:20 | VWAP reversion | buy | BTC-USD | 15.31 | — | entry signal |
| 2026-10-14T13:20 | VWAP reversion | sell | DOGE-USD | 15.23 | -0.19 | stop-loss |
| 2026-10-14T13:20 | RSI(14) reversion | sell | SOL-USD | 16.58 | -0.24 | stop-loss |
| 2026-10-14T13:20 | RSI(14) reversion | sell | DOGE-USD | 16.57 | -0.26 | stop-loss |
| 2026-10-14T13:15 | CCI reversion · 1h | sell | SOL-USD | 6.18 | -0.17 | stop-loss |
| 2026-10-14T13:15 | CCI reversion · 1h | sell | DOGE-USD | 6.20 | -0.15 | stop-loss |
| 2026-10-14T13:15 | Bollinger reversion · 1h | sell | SOL-USD | 1.54 | -0.04 | stop-loss |
| 2026-10-14T13:15 | Bollinger reversion · 1h | sell | ETH-USD | 10.99 | -0.25 | stop-loss |
| 2026-10-14T13:15 | VWAP reversion | buy | DOGE-USD | 9.18 | — | rebalance up |
| 2026-10-14T13:15 | VWAP reversion | sell | SOL-USD | 15.31 | -0.25 | stop-loss |
| 2026-10-14T13:15 | VWAP reversion | sell | ETH-USD | 12.26 | -0.18 | stop-loss |
| 2026-10-14T13:15 | VWAP reversion | sell | BTC-USD | 12.29 | -0.14 | stop-loss |
| 2026-10-14T13:15 | Z-score reversion | sell | BTC-USD | 12.87 | -0.16 | stop-loss |
| 2026-10-14T13:10 | VWAP reversion | buy | DOGE-USD | 6.24 | — | entry signal |
| 2026-10-14T13:10 | VWAP reversion | sell | ETH-USD | 3.13 | -0.03 | rebalance down |
| 2026-10-14T13:10 | VWAP reversion | sell | BTC-USD | 3.11 | -0.02 | rebalance down |
| 2026-10-14T13:10 | Z-score reversion | buy | XRP-USD | 12.99 | — | entry signal |
| 2026-10-14T13:10 | RSI(14) reversion | buy | SOL-USD | 16.82 | — | entry signal |
| 2026-10-14T13:10 | RSI(14) reversion | buy | DOGE-USD | 16.82 | — | entry signal |
| 2026-10-14T13:05 | VWAP reversion | buy | XRP-USD | 15.46 | — | entry signal |
| 2026-10-14T13:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.68 | -0.17 | stop-loss |
| 2026-10-14T13:00 | Candlestick reversal · 1h | sell | ETH-USD | 7.71 | -0.14 | stop-loss |
| 2026-10-14T13:00 | VWAP momentum · 1h | sell | XRP-USD | 7.14 | -0.13 | exit signal |
| 2026-10-14T13:00 | ADX DI cross · 1h | sell | SOL-USD | 13.44 | -0.34 | exit signal |
| 2026-10-14T13:00 | MACD zero-line · 1h | sell | XRP-USD | 20.50 | -0.26 | exit signal |
| 2026-10-14T13:00 | MACD cross · 1h | sell | XRP-USD | 7.85 | -0.13 | exit signal |
| 2026-10-14T13:00 | MACD cross · 1h | sell | SOL-USD | 7.77 | -0.18 | exit signal |
| 2026-10-14T13:00 | Triple EMA stack · 1h | sell | BTC-USD | 14.62 | -0.20 | exit signal |
| 2026-10-14T13:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 4.96 | -0.09 | exit signal |
| 2026-10-14T13:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 7.13 | -0.15 | exit signal |
| 2026-10-14T13:00 | VWAP reversion | sell | DOGE-USD | 15.39 | -0.21 | stop-loss |
| 2026-10-14T13:00 | Z-score reversion | sell | DOGE-USD | 12.88 | -0.17 | stop-loss |
| 2026-10-14T12:55 | VWAP reversion | buy | SOL-USD | 15.55 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 13:25:05.000133+00:00 -> 2026-10-14 13:35:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
