# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T16:53:05.000141+00:00 · 20399 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.45 (-4.55%)

Closed trades 57, win rate 50.9%, fees £2.20, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AAPL | 19.13 | +0.03 |
| TNA | 19.10 | +0.01 |

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

Today: 21771 decisions in 2424 calls, $0.2779 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T16:53 | 2 / 10 / 17 | META 16% |  |
| Breezy | 2026-10-12T16:53 | 0 / 20 / 9 | cash |  |
| Boozy | 2026-10-12T16:53 | 0 / 28 / 1 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | AAPL | 2.49 | +0.83% | 6 |
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.90 | 2.90 | 0 | — | -0.46 | -0.16 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.09 | 2.09 | 14 | 57.1 | -12.55 | -2.06 | -20.64 | 71 |
| 3 | VWAP reversion · 1h | reversion | 102.00 | 2.00 | 39 | 41.0 | -8.56 | -2.59 | -13.79 | 118 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Hold SPY | benchmark | 101.44 | 1.44 | 0 | — | 0.80 | 0.52 | -3.66 | 1 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.35 | 1.35 | 0 | — | 1.51 | 0.74 | -3.62 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.17 | 1.17 | 6 | 50.0 | 4.55 | 2.02 | -3.27 | 17 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.83 | 0.83 | 0 | — | -4.88 | -0.80 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.71 | 0.71 | 0 | — | -1.15 | -0.60 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.38 | 0.38 | 6 | 50.0 | -4.07 | -1.35 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.17 | 0.17 | 10 | 30.0 | 4.38 | 1.38 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.09 | 0 | — | 2.90 | 1.16 | -5.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.59 | -0.41 | 0 | — | -4.71 | -2.17 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 99.02 | -0.98 | 0 | — | 29.63 | 3.49 | -8.68 | 1 |
| 19 | Max aggression: 1-day momentum | meta | 98.44 | -1.56 | 11 | 36.4 | -16.38 | -0.60 | -37.31 | 42 |
| 20 | Donchian 55/20 · 1h | breakout | 97.94 | -2.06 | 31 | 12.9 | 12.69 | 1.54 | -16.92 | 114 |
| 21 | Trend pullback · 1h | trend | 97.90 | -2.10 | 78 | 23.1 | -22.99 | -6.41 | -25.60 | 168 |
| 22 | Stochastic reversion · 1h | reversion | 97.69 | -2.31 | 96 | 53.1 | -11.22 | -2.18 | -13.96 | 335 |
| 23 | Daily: Bullish score | daily | 97.65 | -2.35 | 4 | 0.0 | 0.58 | 0.27 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.15 | -2.85 | 44 | 43.2 | 3.58 | 0.84 | -8.60 | 158 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 96.95 | -3.05 | 0 | — | 9.37 | 1.55 | -8.33 | 1 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.63 | -0.23 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.38 | -3.62 | 62 | 19.4 | -8.37 | -1.44 | -14.05 | 258 |
| 29 | Agent (rotation) | meta | 96.30 | -3.70 | 82 | 29.3 | -12.02 | -3.69 | -15.94 | 294 |
| 30 | MACD cross · 1h | trend | 96.03 | -3.97 | 120 | 24.2 | -13.78 | -2.31 | -17.27 | 468 |
| 31 | Parabolic SAR · 1h | trend | 95.67 | -4.33 | 83 | 21.7 | 1.48 | 0.38 | -21.52 | 291 |
| 32 | EMA 20/50 cross · 1h | trend | 95.63 | -4.37 | 44 | 13.6 | 3.94 | 0.65 | -23.04 | 134 |
| 33 | Agent | meta | 95.45 | -4.55 | 57 | 50.9 | -10.81 | -5.95 | -11.01 | 242 |
| 34 | Supertrend · 1h | trend | 94.56 | -5.44 | 58 | 13.8 | 0.76 | 0.29 | -18.41 | 212 |
| 35 | Gap and go | momentum | 93.98 | -6.02 | 58 | 12.1 | 8.55 | 2.18 | -6.20 | 202 |
| 36 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 39 | 23.1 | 3.97 | 0.88 | -9.37 | 106 |
| 37 | MFI reversion · 1h | reversion | 93.57 | -6.43 | 124 | 34.7 | -7.91 | -1.20 | -16.99 | 127 |
| 38 | Agent (aggressive) | meta | 93.51 | -6.49 | 26 | 42.3 | -8.41 | -3.34 | -8.59 | 111 |
| 39 | Connors RSI(2) · 1h | reversion | 92.70 | -7.30 | 114 | 43.0 | -18.60 | -6.13 | -21.04 | 253 |
| 40 | Agent (ML meta-label) | meta | 92.58 | -7.42 | 424 | 18.4 | -1.84 | -0.22 | -13.07 | 395 |
| 41 | RSI momentum · 1h | momentum | 92.55 | -7.45 | 66 | 15.2 | 0.18 | 0.23 | -21.80 | 228 |
| 42 | RSI(14) reversion · 1h | reversion | 92.45 | -7.55 | 30 | 30.0 | -3.87 | -0.75 | -9.03 | 142 |
| 43 | Bollinger reversion · 1h | reversion | 91.84 | -8.16 | 82 | 37.8 | -21.89 | -5.24 | -23.25 | 318 |
| 44 | Volume breakout · 1h | breakout | 91.69 | -8.31 | 64 | 20.3 | 8.91 | 1.36 | -12.60 | 117 |
| 45 | Ichimoku · 1h | trend | 91.13 | -8.87 | 47 | 17.0 | 0.89 | 0.31 | -22.18 | 126 |
| 46 | Bollinger breakout · 1h | breakout | 91.06 | -8.94 | 74 | 28.4 | 8.52 | 1.23 | -13.96 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.83 | -9.17 | 71 | 15.5 | -7.72 | -0.69 | -27.29 | 237 |
| 48 | Williams %R · 1h | reversion | 90.02 | -9.98 | 130 | 46.9 | -26.21 | -4.44 | -27.31 | 507 |
| 49 | Opening range 30m | breakout | 89.96 | -10.04 | 151 | 21.9 | -15.28 | -4.63 | -15.68 | 568 |
| 50 | CCI reversion · 1h | reversion | 89.23 | -10.77 | 111 | 45.9 | -7.14 | -0.86 | -14.35 | 406 |
| 51 | Candlestick reversal · 1h | reversion | 88.60 | -11.40 | 126 | 31.7 | -28.31 | -5.53 | -28.95 | 501 |
| 52 | OBV trend · 1h | momentum | 88.59 | -11.41 | 150 | 18.7 | -8.17 | -0.71 | -28.83 | 321 |
| 53 | VWAP momentum · 1h | momentum | 88.54 | -11.46 | 304 | 23.0 | -32.95 | -4.91 | -40.08 | 1257 |
| 54 | Heikin-Ashi · 1h | trend | 88.23 | -11.77 | 149 | 28.2 | -29.50 | -4.91 | -36.88 | 686 |
| 55 | MACD zero-line · 1h | trend | 87.88 | -12.12 | 67 | 17.9 | -14.79 | -2.36 | -21.11 | 233 |
| 56 | Donchian 20/10 · 1h | breakout | 87.74 | -12.26 | 63 | 17.5 | -0.54 | 0.14 | -19.27 | 214 |
| 57 | EMA 9/21 cross · 1h | trend | 87.31 | -12.69 | 107 | 13.1 | -10.49 | -1.24 | -23.20 | 331 |
| 58 | Opening range 15m | breakout | 87.21 | -12.79 | 178 | 20.2 | -17.82 | -4.96 | -19.01 | 691 |
| 59 | Max aggression: 5-day momentum | meta | 87.12 | -12.88 | 7 | 28.6 | -15.33 | -1.14 | -34.64 | 28 |
| 60 | Keltner breakout · 1h | breakout | 86.86 | -13.14 | 45 | 20.0 | -11.04 | -1.20 | -26.55 | 216 |
| 61 | Three white soldiers | momentum | 86.54 | -13.46 | 152 | 17.1 | -48.68 | -23.38 | -48.68 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.98 | -14.02 | 139 | 21.6 | -9.18 | -1.06 | -24.60 | 401 |
| 63 | ROC + volume | momentum | 72.95 | -27.05 | 415 | 22.7 | -72.92 | -16.49 | -74.39 | 1673 |
| 64 | RSI(14) reversion | reversion | 71.19 | -28.81 | 401 | 26.9 | -72.61 | -17.83 | -72.61 | 1476 |
| 65 | Squeeze breakout | breakout | 69.91 | -30.09 | 347 | 15.3 | -62.19 | -17.84 | -62.40 | 1222 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -62.23 | -17.69 | -62.26 | 898 |
| 67 | EMA 20/50 cross | trend | 68.19 | -31.81 | 351 | 19.7 | -76.19 | -14.93 | -76.23 | 1430 |
| 68 | Donchian 55/20 | breakout | 67.27 | -32.73 | 356 | 17.7 | -68.18 | -14.39 | -68.84 | 1291 |
| 69 | VWAP reversion | reversion | 66.20 | -33.80 | 421 | 25.9 | -70.98 | -15.56 | -71.00 | 1396 |
| 70 | Keltner breakout | breakout | 60.72 | -39.28 | 478 | 14.6 | -83.53 | -27.27 | -83.59 | 1849 |
| 71 | Supertrend | trend | 60.43 | -39.58 | 494 | 19.2 | -85.96 | -20.69 | -86.07 | 1900 |
| 72 | AI bee: Boozy | ai | 60.09 | -39.91 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.49 | -42.52 | 431 | 10.0 | -82.19 | -22.91 | -82.19 | 1741 |
| 74 | MFI reversion | reversion | 56.09 | -43.91 | 559 | 20.0 | -87.72 | -27.82 | -87.76 | 2103 |
| 75 | Z-score reversion | reversion | 56.01 | -43.99 | 542 | 21.4 | -85.58 | -22.86 | -85.58 | 2062 |
| 76 | AI bee: Bizzy | ai | 55.82 | -44.18 | 879 | 8.4 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.05 | -45.95 | 583 | 9.9 | -89.06 | -33.65 | -89.15 | 2106 |
| 78 | Donchian 20/10 | breakout | 52.38 | -47.62 | 671 | 17.6 | -90.78 | -25.49 | -90.86 | 2645 |
| 79 | MACD zero-line | trend | 51.26 | -48.74 | 625 | 14.4 | -91.44 | -29.36 | -91.45 | 2342 |
| 80 | RSI momentum | momentum | 50.93 | -49.07 | 647 | 16.7 | -90.52 | -25.52 | -90.54 | 2373 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -30.38 | -98.63 | 5382 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.38 | -26.73 | -91.38 | 2339 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -29.83 | -93.23 | 2610 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -32.48 | -97.36 | 3520 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.39 | -35.27 | -96.41 | 3606 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -25.74 | -94.38 | 2638 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.17 | -99.35 | 5617 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -31.31 | -96.38 | 3610 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.10 | -99.73 | 6126 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.57 | -97.36 | 3675 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.36 | -98.49 | 4661 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.42 | -32.50 | -93.46 | 2796 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.42 | -99.53 | 6097 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.80 | -95.87 | 3718 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -33.88 | -95.69 | 4038 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.29 | -99.89 | 8227 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T16:50 | VWAP reversion | buy | LABU | 10.97 | — | entry |
| 2026-10-12T16:50 | VWAP reversion | sell | XRP-USD | 10.97 | -0.13 | stop-loss |
| 2026-10-12T16:50 | Z-score reversion | buy | SOL-USD | 2.18 | — | entry |
| 2026-10-12T16:50 | Z-score reversion | buy | AMZN | 4.67 | — | entry |
| 2026-10-12T16:50 | Z-score reversion | sell | XRP-USD | 5.01 | -0.06 | stop-loss |
| 2026-10-12T16:50 | Z-score reversion | sell | LABU | 1.84 | -0.02 | stop-loss |
| 2026-10-12T16:50 | RSI(14) reversion | sell | XRP-USD | 7.80 | -0.09 | stop-loss |
| 2026-10-12T16:50 | Three white soldiers | sell | AMD | 21.67 | 0.02 | exit signal |
| 2026-10-12T16:50 | Opening range 30m | sell | MSFT | 22.41 | -0.08 | stop-loss |
| 2026-10-12T16:50 | Opening range 15m | sell | MSFT | 21.73 | -0.08 | stop-loss |
| 2026-10-12T16:50 | Donchian 20/10 | buy | TECL | 2.63 | — | rebalance up |
| 2026-10-12T16:50 | Donchian 20/10 | sell | SPY | 8.75 | -0.01 | stop-loss |
| 2026-10-12T16:50 | Donchian 20/10 | sell | SOXL | 10.41 | -0.07 | exit signal |
| 2026-10-12T16:50 | Donchian 20/10 | sell | NVDA | 10.47 | -0.02 | exit signal |
| 2026-10-12T16:50 | RSI momentum | buy | META | 4.21 | — | rebalance up |
| 2026-10-12T16:50 | RSI momentum | buy | GOOGL | 4.22 | — | rebalance up |
| 2026-10-12T16:50 | RSI momentum | buy | ETHU | 4.25 | — | rebalance up |
| 2026-10-12T16:50 | RSI momentum | buy | BITX | 2.57 | — | rebalance up |
| 2026-10-12T16:50 | RSI momentum | sell | MSFT | 10.20 | 0.01 | exit signal |
| 2026-10-12T16:50 | Ichimoku | sell | ETHU | 14.34 | -0.06 | exit signal |
| 2026-10-12T16:50 | MACD zero-line | sell | BTC-USD | 12.78 | -0.09 | exit signal |
| 2026-10-12T16:50 | MACD zero-line | sell | BITX | 12.82 | -0.04 | exit signal |
| 2026-10-12T16:48 | AI bee: Bizzy | buy | META | 8.73 | — | Jev: buy (buy p=0.63) |
| 2026-10-12T16:46 | ADX DI cross | buy | SQQQ | 4.48 | — | rebalance up |
| 2026-10-12T16:46 | ADX DI cross | sell | SOXL | 4.47 | -0.01 | exit signal |
| 2026-10-12T16:46 | ADX DI cross | sell | MSFT | 8.08 | -0.02 | exit signal |
| 2026-10-12T16:46 | ADX DI cross | sell | AMD | 10.81 | -0.01 | exit signal |
| 2026-10-12T16:46 | MACD zero-line | buy | BTC-USD | 2.58 | — | rebalance up |
| 2026-10-12T16:46 | MACD zero-line | buy | BITX | 2.57 | — | rebalance up |
| 2026-10-12T16:46 | MACD zero-line | sell | TNA | 8.57 | -0.02 | exit signal |
| 2026-10-12T16:46 | MACD zero-line | sell | IWM | 8.59 | -0.01 | exit signal |
| 2026-10-12T16:46 | MACD zero-line | sell | ETH-USD | 8.52 | -0.06 | exit signal |
| 2026-10-12T16:40 | Agent (ML meta-label) | buy | IWM | 5.02 | — | entry |
| 2026-10-12T16:40 | Agent (ML meta-label) | sell | LABU | 5.02 | -0.08 | selected signal exited |
| 2026-10-12T16:40 | ROC + volume · 1h | buy | SPY | 5.17 | — | entry |
| 2026-10-12T16:40 | MFI reversion | buy | TNA | 5.64 | — | entry |
| 2026-10-12T16:40 | MFI reversion | sell | MSTR | 2.83 | -0.00 | rebalance down |
| 2026-10-12T16:40 | MFI reversion | sell | IWM | 2.81 | -0.00 | rebalance down |
| 2026-10-12T16:40 | RSI(14) reversion | buy | AMZN | 8.93 | — | entry signal |
| 2026-10-12T16:40 | ADX DI cross | buy | SOXL | 4.48 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 16:53:05.000141+00:00 -> 2026-10-12 17:03:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
