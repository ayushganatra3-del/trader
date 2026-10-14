# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T12:55:05.000172+00:00 · 22472 ticks

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

Today: 9367 decisions in 1874 calls, $0.1310 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T12:55 | 0 / 4 / 1 | AMD 14% |  |
| Breezy | 2026-10-14T12:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T12:55 | 1 / 4 / 0 | COIN 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +3.06% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.06 | 3.06 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.06 | -2.68 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.76 | 1.76 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 100.99 | 0.99 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.36 | 0.36 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 99.78 | -0.22 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 99.78 | -0.22 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 14 | Timing: Nasdaq FTD · TQQQ | daily | 98.90 | -1.10 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 15 | Hold BTC | benchmark | 98.86 | -1.14 | 0 | — | 29.79 | 3.45 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.35 | -1.65 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.73 | -2.27 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.42 | -2.58 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.32 | -2.68 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.02 | -2.86 | -8.69 | 309 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | Stochastic reversion · 1h | reversion | 96.20 | -3.80 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 26 | ADX DI cross · 1h | trend | 96.10 | -3.90 | 65 | 18.5 | -11.57 | -2.13 | -14.81 | 251 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.73 | -4.27 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | EMA 20/50 cross · 1h | trend | 95.32 | -4.68 | 45 | 15.6 | 10.26 | 1.29 | -20.35 | 136 |
| 29 | Max aggression: 1-day momentum | meta | 95.31 | -4.69 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 30 | Z-score reversion · 1h | reversion | 95.28 | -4.72 | 52 | 44.2 | 2.70 | 0.66 | -8.60 | 158 |
| 31 | MACD cross · 1h | trend | 95.15 | -4.85 | 136 | 22.8 | -8.85 | -1.14 | -19.25 | 458 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.87 | -5.08 | -8.87 | 233 |
| 33 | Squeeze breakout · 1h | breakout | 93.93 | -6.07 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 34 | Supertrend · 1h | trend | 93.73 | -6.27 | 60 | 13.3 | 1.93 | 0.44 | -20.39 | 213 |
| 35 | Parabolic SAR · 1h | trend | 93.53 | -6.47 | 91 | 22.0 | 1.43 | 0.37 | -22.84 | 289 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.97 | -0.62 | -5.61 | 111 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.57 | -7.43 | 66 | 15.2 | 1.09 | 0.34 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.49 | -7.51 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.97 | -8.03 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.32 | -8.68 | 38 | 34.2 | 5.57 | 1.29 | -9.40 | 128 |
| 42 | Ichimoku · 1h | trend | 91.25 | -8.75 | 48 | 16.7 | 1.84 | 0.42 | -22.34 | 125 |
| 43 | Agent (ML meta-label) | meta | 91.02 | -8.98 | 485 | 18.1 | -0.75 | -0.00 | -13.10 | 375 |
| 44 | Volume breakout · 1h | breakout | 90.66 | -9.34 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 45 | Bollinger breakout · 1h | breakout | 90.65 | -9.35 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 46 | Triple EMA stack · 1h | trend | 90.58 | -9.42 | 71 | 15.5 | -7.57 | -0.58 | -32.27 | 240 |
| 47 | Bollinger reversion · 1h | reversion | 89.82 | -10.18 | 97 | 37.1 | -23.94 | -5.76 | -24.90 | 322 |
| 48 | Williams %R · 1h | reversion | 89.38 | -10.62 | 143 | 45.5 | -28.47 | -4.84 | -29.71 | 514 |
| 49 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 50 | CCI reversion · 1h | reversion | 88.64 | -11.36 | 120 | 45.0 | -10.11 | -1.33 | -14.42 | 419 |
| 51 | OBV trend · 1h | momentum | 88.05 | -11.95 | 159 | 18.2 | -9.88 | -0.83 | -33.87 | 322 |
| 52 | VWAP momentum · 1h | momentum | 87.19 | -12.81 | 333 | 22.8 | -33.14 | -4.91 | -40.82 | 1252 |
| 53 | MACD zero-line · 1h | trend | 87.14 | -12.86 | 71 | 16.9 | -22.57 | -4.39 | -22.71 | 230 |
| 54 | Donchian 20/10 · 1h | breakout | 86.95 | -13.05 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.71 | -13.29 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.66 | -13.34 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 57 | Heikin-Ashi · 1h | trend | 86.54 | -13.46 | 166 | 26.5 | -29.46 | -4.81 | -38.65 | 673 |
| 58 | EMA 9/21 cross · 1h | trend | 86.49 | -13.51 | 111 | 12.6 | -10.54 | -1.34 | -24.32 | 330 |
| 59 | Candlestick reversal · 1h | reversion | 86.20 | -13.80 | 143 | 30.8 | -29.69 | -5.76 | -30.01 | 475 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 61 | Three white soldiers | momentum | 85.44 | -14.56 | 169 | 17.8 | -47.84 | -21.96 | -48.07 | 584 |
| 62 | ROC + volume · 1h | momentum | 85.28 | -14.72 | 173 | 20.2 | -8.96 | -1.02 | -24.87 | 399 |
| 63 | ROC + volume | momentum | 68.49 | -31.51 | 469 | 21.7 | -74.02 | -16.60 | -76.03 | 1679 |
| 64 | RSI(14) reversion | reversion | 67.30 | -32.70 | 462 | 27.5 | -73.12 | -16.57 | -73.51 | 1470 |
| 65 | Squeeze breakout | breakout | 66.32 | -33.68 | 386 | 15.0 | -63.01 | -18.12 | -63.12 | 1225 |
| 66 | Volume breakout | breakout | 66.14 | -33.86 | 304 | 13.8 | -62.58 | -17.47 | -62.88 | 894 |
| 67 | EMA 20/50 cross | trend | 63.40 | -36.60 | 405 | 19.5 | -77.07 | -15.01 | -77.62 | 1445 |
| 68 | Donchian 55/20 | breakout | 63.13 | -36.87 | 395 | 16.7 | -69.18 | -14.42 | -70.80 | 1285 |
| 69 | VWAP reversion | reversion | 62.17 | -37.83 | 493 | 25.6 | -72.19 | -15.11 | -72.28 | 1401 |
| 70 | AI bee: Boozy | ai | 59.68 | -40.32 | 272 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 57.08 | -42.92 | 561 | 19.3 | -85.93 | -20.27 | -85.93 | 1913 |
| 72 | Keltner breakout | breakout | 56.39 | -43.61 | 546 | 14.1 | -83.51 | -26.64 | -83.51 | 1850 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.30 | -22.74 | -82.30 | 1721 |
| 74 | AI bee: Bizzy | ai | 52.72 | -47.28 | 967 | 8.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.70 | -47.30 | 680 | 20.1 | -87.64 | -26.67 | -87.66 | 2108 |
| 76 | Z-score reversion | reversion | 52.10 | -47.90 | 628 | 22.9 | -85.79 | -21.55 | -85.79 | 2078 |
| 77 | ADX DI cross | trend | 50.67 | -49.33 | 658 | 10.3 | -89.18 | -33.20 | -89.18 | 2109 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.51 | -28.91 | -98.51 | 5307 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -29.45 | -93.55 | 2618 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.54 | -24.52 | -90.57 | 2375 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.64 | -26.23 | -91.64 | 2352 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -31.86 | -97.38 | 3535 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.59 | -34.89 | -96.59 | 3607 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.56 | -25.21 | -94.56 | 2642 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.16 | -99.37 | 5645 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.06 | -25.51 | -91.06 | 2635 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -30.37 | -96.37 | 3596 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.41 | -99.72 | 6153 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.60 | -29.06 | -91.61 | 2361 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.40 | -36.12 | -97.40 | 3672 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -34.89 | -98.50 | 4670 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.50 | -31.99 | -93.50 | 2803 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.80 | -99.54 | 6124 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -31.43 | -95.94 | 3735 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -33.10 | -95.67 | 4045 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.76 | -99.89 | 8209 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T12:55 | VWAP reversion | buy | SOL-USD | 15.55 | — | entry signal |
| 2026-10-14T12:55 | Z-score reversion | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-10-14T12:45 | VWAP reversion | buy | BTC-USD | 15.56 | — | entry signal |
| 2026-10-14T12:40 | VWAP reversion | buy | ETH-USD | 15.59 | — | entry signal |
| 2026-10-14T12:40 | VWAP reversion | buy | DOGE-USD | 15.59 | — | entry signal |
| 2026-10-14T12:40 | Z-score reversion | buy | DOGE-USD | 13.05 | — | entry signal |
| 2026-10-14T12:35 | Three white soldiers | sell | ETH-USD | 21.09 | -0.36 | stop-loss |
| 2026-10-14T12:35 | Volume breakout | sell | XRP-USD | 16.46 | -0.29 | stop-loss |
| 2026-10-14T12:35 | Volume breakout | sell | DOGE-USD | 16.42 | -0.31 | stop-loss |
| 2026-10-14T12:35 | Volume breakout | sell | BTC-USD | 16.50 | -0.25 | stop-loss |
| 2026-10-14T12:35 | Squeeze breakout | sell | ETH-USD | 16.41 | -0.31 | stop-loss |
| 2026-10-14T12:35 | Squeeze breakout | sell | BTC-USD | 16.46 | -0.27 | stop-loss |
| 2026-10-14T12:35 | Keltner breakout | sell | XRP-USD | 11.27 | -0.20 | stop-loss |
| 2026-10-14T12:35 | Keltner breakout | sell | SOL-USD | 8.45 | -0.17 | stop-loss |
| 2026-10-14T12:35 | Keltner breakout | sell | ETH-USD | 11.27 | -0.19 | stop-loss |
| 2026-10-14T12:35 | Keltner breakout | sell | DOGE-USD | 11.26 | -0.20 | stop-loss |
| 2026-10-14T12:35 | Keltner breakout | sell | BTC-USD | 11.28 | -0.19 | stop-loss |
| 2026-10-14T12:35 | ROC + volume | sell | XRP-USD | 13.68 | -0.28 | stop-loss |
| 2026-10-14T12:35 | ROC + volume | sell | SOL-USD | 13.68 | -0.28 | stop-loss |
| 2026-10-14T12:35 | ROC + volume | sell | ETH-USD | 13.70 | -0.26 | stop-loss |
| 2026-10-14T12:35 | ROC + volume | sell | DOGE-USD | 13.71 | -0.26 | stop-loss |
| 2026-10-14T12:35 | ROC + volume | sell | BTC-USD | 13.71 | -0.25 | stop-loss |
| 2026-10-14T12:35 | Supertrend | sell | XRP-USD | 11.42 | -0.15 | exit signal |
| 2026-10-14T12:35 | Supertrend | sell | SOL-USD | 11.41 | -0.18 | exit signal |
| 2026-10-14T12:35 | Supertrend | sell | ETH-USD | 14.27 | -0.21 | exit signal |
| 2026-10-14T12:35 | Supertrend | sell | DOGE-USD | 8.56 | -0.15 | exit signal |
| 2026-10-14T12:35 | Supertrend | sell | BTC-USD | 11.42 | -0.17 | exit signal |
| 2026-10-14T12:35 | EMA 20/50 cross | sell | XRP-USD | 12.71 | -0.18 | stop-loss |
| 2026-10-14T12:35 | EMA 20/50 cross | sell | SOL-USD | 12.65 | -0.26 | stop-loss |
| 2026-10-14T12:35 | EMA 20/50 cross | sell | ETH-USD | 12.67 | -0.24 | stop-loss |
| 2026-10-14T12:35 | EMA 20/50 cross | sell | DOGE-USD | 12.66 | -0.26 | stop-loss |
| 2026-10-14T12:35 | EMA 20/50 cross | sell | BTC-USD | 12.71 | -0.21 | stop-loss |
| 2026-10-14T12:32 | ROC + volume | buy | XRP-USD | 6.94 | — | rebalance up |
| 2026-10-14T12:32 | ROC + volume | sell | SOL-USD | 3.49 | -0.02 | rebalance down |
| 2026-10-14T12:32 | ROC + volume | sell | DOGE-USD | 3.48 | -0.02 | rebalance down |
| 2026-10-14T12:30 | ROC + volume | buy | XRP-USD | 7.01 | — | entry signal |
| 2026-10-14T12:30 | ROC + volume | buy | ETH-USD | 13.96 | — | entry signal |
| 2026-10-14T12:30 | ROC + volume | buy | BTC-USD | 13.96 | — | entry signal |
| 2026-10-14T12:26 | AI bee: Boozy | sell | ETH-USD | 13.36 | -0.09 | Jev: buy |
| 2026-10-14T12:24 | AI bee: Bizzy | sell | SOL-USD | 7.48 | -0.07 | Jev: sell (sell p=0.74) after 11 min |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 12:55:05.000172+00:00 -> 2026-10-14 13:05:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
