# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T15:26:05.000143+00:00 · 21457 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.07 (-4.93%)

Closed trades 61, win rate 47.5%, fees £2.31, max drawdown -5.37%.

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

Today: 17070 decisions in 2208 calls, $0.2222 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T15:26 | 2 / 14 / 14 | cash |  |
| Breezy | 2026-10-13T15:26 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-13T15:26 | 2 / 24 / 4 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +2.94% | 4 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.65 | 3.65 | 0 | — | 2.67 | 1.32 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -8.89 | -2.64 | -13.79 | 115 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 101.34 | 1.34 | 0 | — | 6.44 | 2.38 | -5.18 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | Hold SPY | benchmark | 101.00 | 1.00 | 0 | — | 0.50 | 0.34 | -3.66 | 1 |
| 7 | Copy: Insider buying | copy | 100.94 | 0.94 | 16 | 50.0 | -15.94 | -2.54 | -21.97 | 75 |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.71 | 0.71 | 11 | 36.4 | 4.83 | 1.51 | -7.55 | 43 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.56 | 0.56 | 0 | — | 0.99 | 0.51 | -3.62 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Hold BTC | benchmark | 99.96 | -0.04 | 0 | — | 31.33 | 3.61 | -8.68 | 1 |
| 13 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.83 | -0.17 | 7 | 57.1 | -4.28 | -1.42 | -9.74 | 25 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 99.66 | -0.34 | 0 | — | -2.62 | -1.45 | -5.09 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.12 | -0.88 | 0 | — | -5.00 | -2.30 | -5.41 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 98.48 | -1.52 | 45 | 33.3 | 3.22 | 1.86 | -1.32 | 74 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 98.29 | -1.71 | 0 | — | -9.05 | -1.64 | -15.27 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 98.19 | -1.80 | 31 | 12.9 | 12.19 | 1.46 | -18.79 | 115 |
| 20 | Trend pullback · 1h | trend | 98.04 | -1.96 | 82 | 25.6 | -22.91 | -6.41 | -25.67 | 173 |
| 21 | Daily: Bullish score | daily | 98.00 | -2.00 | 5 | 0.0 | 1.22 | 0.35 | -12.76 | 12 |
| 22 | ADX DI cross · 1h | trend | 97.17 | -2.83 | 63 | 19.0 | -1.66 | -0.13 | -13.99 | 252 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.74 | -0.41 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | Agent (rotation) | meta | 96.49 | -3.52 | 87 | 31.0 | -11.07 | -3.44 | -12.84 | 271 |
| 26 | Max aggression: 1-day momentum | meta | 96.39 | -3.61 | 12 | 33.3 | -10.39 | -0.22 | -37.31 | 42 |
| 27 | MACD cross · 1h | trend | 96.20 | -3.80 | 128 | 24.2 | -9.08 | -1.37 | -17.82 | 459 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 95.81 | -4.19 | 0 | — | 7.44 | 1.27 | -8.36 | 1 |
| 29 | EMA 20/50 cross · 1h | trend | 95.79 | -4.21 | 45 | 15.6 | 10.20 | 1.30 | -20.59 | 136 |
| 30 | Z-score reversion · 1h | reversion | 95.31 | -4.69 | 49 | 42.9 | 2.06 | 0.54 | -8.60 | 158 |
| 31 | Agent | meta | 95.07 | -4.93 | 61 | 47.5 | -12.01 | -6.73 | -12.01 | 243 |
| 32 | Supertrend · 1h | trend | 94.74 | -5.26 | 60 | 13.3 | 0.66 | 0.28 | -19.12 | 219 |
| 33 | Stochastic reversion · 1h | reversion | 94.60 | -5.40 | 107 | 51.4 | -15.96 | -3.10 | -16.17 | 343 |
| 34 | Parabolic SAR · 1h | trend | 94.54 | -5.46 | 88 | 22.7 | 2.09 | 0.45 | -21.19 | 290 |
| 35 | Squeeze breakout · 1h | breakout | 94.06 | -5.94 | 40 | 22.5 | 4.84 | 1.06 | -9.46 | 102 |
| 36 | Gap and go | momentum | 93.32 | -6.68 | 61 | 11.5 | 7.80 | 2.00 | -6.92 | 203 |
| 37 | RSI momentum · 1h | momentum | 93.02 | -6.98 | 66 | 15.2 | 3.33 | 0.59 | -21.82 | 227 |
| 38 | Agent (aggressive) | meta | 92.86 | -7.14 | 31 | 35.5 | -9.08 | -4.04 | -9.08 | 120 |
| 39 | MFI reversion · 1h | reversion | 92.55 | -7.46 | 159 | 32.1 | -7.98 | -1.24 | -17.05 | 128 |
| 40 | Connors RSI(2) · 1h | reversion | 91.76 | -8.24 | 122 | 42.6 | -18.73 | -6.17 | -21.32 | 257 |
| 41 | Agent (ML meta-label) | meta | 91.69 | -8.31 | 456 | 17.3 | -3.64 | -0.50 | -15.29 | 396 |
| 42 | Ichimoku · 1h | trend | 91.66 | -8.34 | 48 | 16.7 | 1.94 | 0.43 | -22.34 | 126 |
| 43 | RSI(14) reversion · 1h | reversion | 91.63 | -8.38 | 37 | 32.4 | -6.10 | -1.04 | -9.97 | 147 |
| 44 | Volume breakout · 1h | breakout | 91.62 | -8.38 | 72 | 22.2 | 8.80 | 1.34 | -12.60 | 120 |
| 45 | Bollinger breakout · 1h | breakout | 91.54 | -8.46 | 75 | 28.0 | 8.55 | 1.23 | -14.21 | 279 |
| 46 | Triple EMA stack · 1h | trend | 91.08 | -8.92 | 71 | 15.5 | -6.79 | -0.52 | -32.04 | 233 |
| 47 | Bollinger reversion · 1h | reversion | 89.19 | -10.81 | 96 | 36.5 | -26.01 | -6.27 | -26.40 | 319 |
| 48 | CCI reversion · 1h | reversion | 89.06 | -10.94 | 117 | 45.3 | -9.56 | -1.25 | -14.42 | 411 |
| 49 | OBV trend · 1h | momentum | 88.88 | -11.12 | 151 | 18.5 | -6.67 | -0.55 | -27.73 | 322 |
| 50 | Opening range 30m | breakout | 88.45 | -11.55 | 157 | 21.7 | -15.88 | -4.77 | -17.31 | 574 |
| 51 | VWAP momentum · 1h | momentum | 88.42 | -11.58 | 315 | 23.5 | -31.83 | -4.67 | -40.47 | 1242 |
| 52 | MACD zero-line · 1h | trend | 88.13 | -11.87 | 68 | 17.6 | -19.35 | -3.57 | -21.55 | 231 |
| 53 | Donchian 20/10 · 1h | breakout | 87.79 | -12.21 | 64 | 17.2 | -0.07 | 0.20 | -19.51 | 218 |
| 54 | Max aggression: 5-day momentum | meta | 87.70 | -12.30 | 8 | 37.5 | -10.46 | -0.66 | -34.64 | 28 |
| 55 | Williams %R · 1h | reversion | 87.61 | -12.39 | 143 | 45.5 | -25.82 | -4.18 | -29.16 | 509 |
| 56 | Keltner breakout · 1h | breakout | 87.47 | -12.53 | 46 | 19.6 | -9.74 | -1.06 | -26.75 | 217 |
| 57 | Heikin-Ashi · 1h | trend | 87.33 | -12.67 | 159 | 27.7 | -30.43 | -5.04 | -38.13 | 681 |
| 58 | EMA 9/21 cross · 1h | trend | 87.16 | -12.84 | 110 | 12.7 | -7.60 | -0.76 | -23.21 | 330 |
| 59 | Candlestick reversal · 1h | reversion | 86.91 | -13.09 | 135 | 29.6 | -30.29 | -5.97 | -31.16 | 496 |
| 60 | Three white soldiers | momentum | 86.38 | -13.62 | 157 | 17.8 | -47.99 | -22.89 | -48.13 | 589 |
| 61 | ROC + volume · 1h | momentum | 86.26 | -13.74 | 169 | 20.7 | -8.12 | -0.90 | -25.26 | 396 |
| 62 | Opening range 15m | breakout | 85.87 | -14.13 | 191 | 19.4 | -18.57 | -5.10 | -20.34 | 704 |
| 63 | ROC + volume | momentum | 72.72 | -27.28 | 441 | 23.1 | -72.66 | -16.22 | -74.72 | 1675 |
| 64 | Squeeze breakout | breakout | 68.57 | -31.43 | 366 | 15.3 | -62.44 | -18.18 | -62.52 | 1225 |
| 65 | Volume breakout | breakout | 68.37 | -31.63 | 288 | 14.6 | -61.53 | -17.45 | -61.53 | 893 |
| 66 | EMA 20/50 cross | trend | 67.68 | -32.32 | 365 | 20.3 | -75.84 | -14.70 | -76.17 | 1435 |
| 67 | RSI(14) reversion | reversion | 66.88 | -33.12 | 445 | 26.7 | -74.36 | -17.46 | -74.36 | 1497 |
| 68 | Donchian 55/20 | breakout | 65.75 | -34.25 | 371 | 17.3 | -68.30 | -14.29 | -69.66 | 1294 |
| 69 | VWAP reversion | reversion | 62.90 | -37.10 | 471 | 25.3 | -72.17 | -15.46 | -72.23 | 1392 |
| 70 | Supertrend | trend | 60.40 | -39.60 | 511 | 20.0 | -85.73 | -20.35 | -85.85 | 1901 |
| 71 | AI bee: Boozy | ai | 60.37 | -39.63 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.98 | -40.02 | 502 | 15.1 | -83.12 | -26.58 | -83.15 | 1852 |
| 73 | Ichimoku | trend | 56.32 | -43.68 | 443 | 9.7 | -82.18 | -22.76 | -82.18 | 1729 |
| 74 | MFI reversion | reversion | 53.88 | -46.12 | 637 | 19.8 | -87.87 | -27.64 | -87.89 | 2107 |
| 75 | AI bee: Bizzy | ai | 53.64 | -46.36 | 922 | 8.2 | — | — | — | — |
| 76 | ADX DI cross | trend | 52.59 | -47.41 | 624 | 10.6 | -89.13 | -33.95 | -89.13 | 2115 |
| 77 | Z-score reversion | reversion | 52.59 | -47.41 | 596 | 22.1 | -86.32 | -22.38 | -86.32 | 2089 |
| 78 | Donchian 20/10 | breakout | 51.75 | -48.25 | 704 | 17.8 | -90.66 | -25.26 | -90.68 | 2645 |
| 79 | MACD zero-line | trend | 51.02 | -48.98 | 650 | 14.9 | -91.23 | -28.75 | -91.27 | 2340 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -29.02 | -98.51 | 5321 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.00 | -28.79 | -93.03 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.15 | -24.24 | -90.26 | 2364 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.38 | -26.57 | -91.39 | 2340 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.26 | -31.59 | -97.28 | 3503 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -34.36 | -96.29 | 3577 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.32 | -25.32 | -94.32 | 2644 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.40 | -99.36 | 5651 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.33 | -31.26 | -96.33 | 3593 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.61 | -99.72 | 6126 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -37.25 | -97.32 | 3656 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -36.37 | -98.54 | 4668 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.31 | -32.21 | -93.33 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.33 | -99.54 | 6115 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.06 | -32.90 | -96.06 | 3734 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -34.02 | -95.74 | 4040 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.91 | -99.89 | 8211 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T15:26 | Agent (ML meta-label) | sell | UPRO | 6.53 | -0.01 | selected signal exited |
| 2026-10-13T15:26 | Agent (ML meta-label) | sell | AAPL | 6.54 | -0.00 | selected signal exited |
| 2026-10-13T15:26 | Volume breakout | buy | COIN | 17.09 | — | entry signal |
| 2026-10-13T15:26 | Squeeze breakout | sell | META | 17.12 | 0.06 | exit signal |
| 2026-10-13T15:26 | Keltner breakout | buy | COIN | 3.08 | — | entry signal |
| 2026-10-13T15:26 | Keltner breakout | sell | BITX | 3.08 | 0.01 | rebalance down |
| 2026-10-13T15:26 | Opening range 15m | buy | ETHU | 4.15 | — | entry signal |
| 2026-10-13T15:26 | Opening range 15m | buy | BITX | 12.27 | — | entry signal |
| 2026-10-13T15:26 | Opening range 15m | sell | COIN | 5.03 | 0.04 | rebalance down |
| 2026-10-13T15:26 | Donchian 20/10 | buy | TSLA | 8.61 | — | entry signal |
| 2026-10-13T15:26 | Donchian 20/10 | buy | SQQQ | 8.63 | — | entry signal |
| 2026-10-13T15:26 | Donchian 20/10 | buy | COIN | 8.63 | — | entry signal |
| 2026-10-13T15:26 | Donchian 20/10 | sell | MSTR | 4.41 | 0.01 | rebalance down |
| 2026-10-13T15:26 | Donchian 20/10 | sell | META | 4.28 | 0.00 | rebalance down |
| 2026-10-13T15:26 | Donchian 20/10 | sell | ETH-USD | 4.32 | -0.01 | rebalance down |
| 2026-10-13T15:26 | ROC + volume | buy | COIN | 18.18 | — | entry signal |
| 2026-10-13T15:26 | Ichimoku | buy | GOOGL | 14.08 | — | entry signal |
| 2026-10-13T15:26 | ADX DI cross | buy | XRP-USD | 13.03 | — | entry signal |
| 2026-10-13T15:26 | ADX DI cross | buy | MSTR | 13.16 | — | entry signal |
| 2026-10-13T15:20 | VWAP momentum · 1h | buy | META | 5.12 | — | entry |
| 2026-10-13T15:20 | VWAP momentum · 1h | buy | ETHU | 5.96 | — | rebalance up |
| 2026-10-13T15:20 | VWAP momentum · 1h | sell | NVDA | 11.07 | -0.13 | target is flat |
| 2026-10-13T15:20 | MFI reversion | buy | PLTR | 13.37 | — | entry signal |
| 2026-10-13T15:20 | Z-score reversion | buy | TECL | 3.13 | — | entry signal |
| 2026-10-13T15:20 | RSI(14) reversion | sell | TSLA | 5.30 | 0.03 | exit signal |
| 2026-10-13T15:20 | Squeeze breakout | buy | META | 3.44 | — | rebalance up |
| 2026-10-13T15:20 | Squeeze breakout | sell | XRP-USD | 10.34 | -0.10 | exit signal |
| 2026-10-13T15:20 | Squeeze breakout | sell | ETH-USD | 13.61 | -0.11 | exit signal |
| 2026-10-13T15:20 | Squeeze breakout | sell | BTC-USD | 17.04 | -0.11 | exit signal |
| 2026-10-13T15:20 | Keltner breakout | buy | SQQQ | 4.94 | — | rebalance up |
| 2026-10-13T15:20 | Keltner breakout | buy | META | 4.89 | — | rebalance up |
| 2026-10-13T15:20 | Keltner breakout | buy | BITX | 7.49 | — | rebalance up |
| 2026-10-13T15:20 | Keltner breakout | buy | AAPL | 6.37 | — | rebalance up |
| 2026-10-13T15:20 | Keltner breakout | sell | XRP-USD | 7.93 | -0.08 | exit signal |
| 2026-10-13T15:20 | Keltner breakout | sell | SOL-USD | 9.93 | -0.11 | exit signal |
| 2026-10-13T15:20 | Opening range 15m | buy | COIN | 17.15 | — | entry |
| 2026-10-13T15:20 | Opening range 15m | sell | ETHU | 14.25 | -0.12 | exit signal |
| 2026-10-13T15:20 | Opening range 15m | sell | BITX | 14.28 | -0.07 | exit signal |
| 2026-10-13T15:20 | Donchian 20/10 | buy | MSTR | 5.60 | — | rebalance up |
| 2026-10-13T15:20 | Donchian 20/10 | buy | META | 5.53 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 15:26:05.000143+00:00 -> 2026-10-13 15:36:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
