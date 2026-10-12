# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T18:25:05.000156+00:00 · 20461 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.34 (-4.66%)

Closed trades 57, win rate 50.9%, fees £2.26, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AAPL | 19.07 | +0.00 |
| TNA | 19.06 | -0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 27312 decisions in 2610 calls, $0.3429 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T18:25 | 2 / 13 / 15 | META 15% |  |
| Breezy | 2026-10-12T18:25 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-12T18:25 | 0 / 28 / 2 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.72 | 2.72 | 0 | — | -0.48 | -0.17 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | VWAP reversion · 1h | reversion | 101.62 | 1.62 | 39 | 41.0 | -9.12 | -2.74 | -13.79 | 118 |
| 4 | Copy: Insider buying | copy | 101.59 | 1.59 | 14 | 57.1 | -13.03 | -2.15 | -20.64 | 71 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.49 | 1.49 | 6 | 50.0 | 4.91 | 2.18 | -3.27 | 17 |
| 6 | Hold SPY | benchmark | 101.35 | 1.35 | 0 | — | 0.82 | 0.53 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.06 | 1.06 | 0 | — | 1.27 | 0.63 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.69 | 0.69 | 6 | 50.0 | -3.74 | -1.23 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.57 | 0.57 | 0 | — | -1.10 | -0.57 | -5.09 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.49 | 0.48 | 10 | 30.0 | 4.73 | 1.48 | -7.55 | 43 |
| 11 | Timing: Nasdaq FTD · TQQQ | daily | 100.46 | 0.46 | 0 | — | -4.75 | -0.77 | -15.27 | 1 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.74 | -0.26 | 0 | — | 3.48 | 1.38 | -5.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.56 | -0.44 | 0 | — | -4.71 | -2.17 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 98.75 | -1.25 | 0 | — | 29.83 | 3.51 | -8.68 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 97.93 | -2.07 | 31 | 12.9 | 14.71 | 1.72 | -16.92 | 113 |
| 20 | Trend pullback · 1h | trend | 97.64 | -2.36 | 78 | 23.1 | -23.07 | -6.46 | -25.52 | 169 |
| 21 | Max aggression: 1-day momentum | meta | 97.45 | -2.56 | 11 | 36.4 | -17.20 | -0.66 | -37.31 | 42 |
| 22 | Daily: Bullish score | daily | 97.42 | -2.58 | 4 | 0.0 | 0.41 | 0.25 | -12.76 | 11 |
| 23 | Stochastic reversion · 1h | reversion | 97.21 | -2.79 | 96 | 53.1 | -11.63 | -2.25 | -13.89 | 337 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.86 | -3.14 | 0 | — | 9.05 | 1.50 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.80 | -3.20 | 44 | 43.2 | 3.62 | 0.85 | -8.60 | 158 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.53 | -0.22 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.41 | -3.60 | 62 | 19.4 | -7.80 | -1.34 | -14.13 | 253 |
| 29 | Agent (rotation) | meta | 96.38 | -3.62 | 82 | 29.3 | -14.18 | -4.57 | -18.72 | 311 |
| 30 | MACD cross · 1h | trend | 95.76 | -4.24 | 121 | 24.0 | -13.15 | -2.19 | -17.27 | 467 |
| 31 | EMA 20/50 cross · 1h | trend | 95.46 | -4.54 | 45 | 15.6 | 5.75 | 0.84 | -23.28 | 135 |
| 32 | Parabolic SAR · 1h | trend | 95.43 | -4.57 | 84 | 21.4 | 1.25 | 0.35 | -21.52 | 291 |
| 33 | Agent | meta | 95.34 | -4.66 | 57 | 50.9 | -10.12 | -4.96 | -10.42 | 255 |
| 34 | Supertrend · 1h | trend | 94.36 | -5.64 | 58 | 13.8 | 0.59 | 0.27 | -18.58 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.23 | 2.10 | -6.21 | 202 |
| 36 | Squeeze breakout · 1h | breakout | 93.62 | -6.38 | 39 | 23.1 | 4.29 | 0.93 | -9.46 | 104 |
| 37 | Agent (aggressive) | meta | 93.33 | -6.67 | 29 | 37.9 | -11.94 | -4.25 | -12.11 | 130 |
| 38 | MFI reversion · 1h | reversion | 93.01 | -6.99 | 136 | 32.4 | -8.33 | -1.27 | -16.95 | 128 |
| 39 | Connors RSI(2) · 1h | reversion | 92.48 | -7.52 | 114 | 43.0 | -18.77 | -6.19 | -21.04 | 254 |
| 40 | RSI momentum · 1h | momentum | 92.43 | -7.57 | 66 | 15.2 | -0.24 | 0.18 | -22.75 | 228 |
| 41 | Agent (ML meta-label) | meta | 92.28 | -7.72 | 426 | 18.3 | 0.53 | 0.24 | -13.83 | 399 |
| 42 | RSI(14) reversion · 1h | reversion | 91.95 | -8.04 | 30 | 30.0 | -0.27 | 0.05 | -9.03 | 132 |
| 43 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 67 | 19.4 | 8.98 | 1.37 | -12.60 | 117 |
| 44 | Bollinger reversion · 1h | reversion | 91.32 | -8.68 | 83 | 37.3 | -23.63 | -5.83 | -24.54 | 317 |
| 45 | Ichimoku · 1h | trend | 91.07 | -8.93 | 47 | 17.0 | 0.85 | 0.31 | -22.34 | 126 |
| 46 | Bollinger breakout · 1h | breakout | 90.89 | -9.11 | 74 | 28.4 | 8.32 | 1.20 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.57 | -9.43 | 71 | 15.5 | -7.54 | -0.68 | -26.94 | 239 |
| 48 | Opening range 30m | breakout | 89.70 | -10.30 | 152 | 21.7 | -15.53 | -4.69 | -15.92 | 569 |
| 49 | Williams %R · 1h | reversion | 89.59 | -10.41 | 131 | 46.6 | -26.26 | -4.44 | -27.54 | 504 |
| 50 | CCI reversion · 1h | reversion | 88.67 | -11.33 | 111 | 45.9 | -7.75 | -0.95 | -14.35 | 406 |
| 51 | VWAP momentum · 1h | momentum | 88.47 | -11.53 | 306 | 23.2 | -33.52 | -5.00 | -40.30 | 1254 |
| 52 | OBV trend · 1h | momentum | 88.44 | -11.56 | 150 | 18.7 | -8.75 | -0.79 | -28.73 | 324 |
| 53 | Candlestick reversal · 1h | reversion | 88.14 | -11.86 | 127 | 31.5 | -28.86 | -5.62 | -29.32 | 493 |
| 54 | MACD zero-line · 1h | trend | 87.93 | -12.07 | 67 | 17.9 | -19.84 | -3.59 | -21.38 | 232 |
| 55 | Heikin-Ashi · 1h | trend | 87.92 | -12.09 | 151 | 27.8 | -30.14 | -4.99 | -37.50 | 682 |
| 56 | Donchian 20/10 · 1h | breakout | 87.59 | -12.40 | 63 | 17.5 | -0.64 | 0.13 | -19.48 | 214 |
| 57 | Max aggression: 5-day momentum | meta | 87.21 | -12.79 | 7 | 28.6 | -15.22 | -1.13 | -34.64 | 28 |
| 58 | EMA 9/21 cross · 1h | trend | 87.16 | -12.84 | 107 | 13.1 | -10.97 | -1.30 | -23.35 | 332 |
| 59 | Opening range 15m | breakout | 86.92 | -13.07 | 180 | 20.0 | -18.08 | -5.00 | -19.41 | 692 |
| 60 | Keltner breakout · 1h | breakout | 86.71 | -13.29 | 45 | 20.0 | -12.30 | -1.44 | -26.77 | 216 |
| 61 | Three white soldiers | momentum | 86.54 | -13.46 | 152 | 17.1 | -48.68 | -23.38 | -48.68 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.62 | -14.38 | 151 | 20.5 | -9.11 | -1.05 | -24.83 | 400 |
| 63 | ROC + volume | momentum | 72.84 | -27.16 | 417 | 22.5 | -72.99 | -16.52 | -74.43 | 1673 |
| 64 | RSI(14) reversion | reversion | 70.80 | -29.20 | 404 | 26.7 | -72.64 | -17.74 | -72.67 | 1474 |
| 65 | Squeeze breakout | breakout | 69.91 | -30.09 | 347 | 15.3 | -62.06 | -17.89 | -62.07 | 1216 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -62.23 | -17.69 | -62.26 | 898 |
| 67 | EMA 20/50 cross | trend | 68.25 | -31.75 | 351 | 19.7 | -76.19 | -14.93 | -76.27 | 1430 |
| 68 | Donchian 55/20 | breakout | 67.07 | -32.93 | 357 | 17.6 | -68.04 | -14.27 | -68.90 | 1288 |
| 69 | VWAP reversion | reversion | 65.56 | -34.44 | 430 | 25.6 | -71.28 | -15.63 | -71.28 | 1403 |
| 70 | Keltner breakout | breakout | 60.72 | -39.28 | 478 | 14.6 | -83.58 | -27.38 | -83.58 | 1846 |
| 71 | Supertrend | trend | 60.33 | -39.67 | 496 | 19.2 | -86.00 | -20.74 | -86.01 | 1895 |
| 72 | AI bee: Boozy | ai | 59.78 | -40.22 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.40 | -42.60 | 432 | 10.0 | -82.21 | -22.89 | -82.22 | 1739 |
| 74 | Z-score reversion | reversion | 55.73 | -44.27 | 549 | 21.3 | -85.68 | -22.81 | -85.69 | 2064 |
| 75 | AI bee: Bizzy | ai | 55.68 | -44.32 | 881 | 8.4 | — | — | — | — |
| 76 | MFI reversion | reversion | 55.67 | -44.33 | 584 | 19.5 | -87.81 | -27.92 | -87.81 | 2112 |
| 77 | ADX DI cross | trend | 54.01 | -45.99 | 586 | 9.9 | -89.05 | -33.75 | -89.06 | 2095 |
| 78 | Donchian 20/10 | breakout | 52.21 | -47.79 | 673 | 17.5 | -90.85 | -25.62 | -90.88 | 2639 |
| 79 | MACD zero-line | trend | 51.21 | -48.79 | 626 | 14.4 | -91.44 | -29.31 | -91.45 | 2341 |
| 80 | RSI momentum | momentum | 50.64 | -49.36 | 651 | 16.6 | -90.52 | -25.33 | -90.53 | 2368 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -29.98 | -98.63 | 5338 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.34 | -26.53 | -91.35 | 2333 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.24 | -29.90 | -93.25 | 2608 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -32.48 | -97.35 | 3509 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.41 | -35.58 | -96.41 | 3598 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -25.33 | -94.27 | 2629 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.10 | -99.36 | 5640 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -31.02 | -96.32 | 3606 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.09 | -99.73 | 6149 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -37.29 | -97.34 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.27 | -98.50 | 4658 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.43 | -32.51 | -93.44 | 2791 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.09 | -99.53 | 6090 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.64 | -95.89 | 3716 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.80 | -95.70 | 4049 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.06 | -99.89 | 8211 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T18:25 | Agent (aggressive) | sell | AAPL | 46.65 | -0.02 | selected signal exited |
| 2026-10-12T18:25 | Agent | sell | AAPL | 19.07 | -0.01 | rebalance down |
| 2026-10-12T18:25 | MFI reversion · 1h | buy | BITX | 18.47 | — | entry |
| 2026-10-12T18:25 | MFI reversion · 1h | sell | QQQ | 18.47 | -0.02 | target is flat |
| 2026-10-12T18:25 | ROC + volume · 1h | buy | SPY | 6.59 | — | entry |
| 2026-10-12T18:25 | ROC + volume · 1h | sell | PLTR | 6.58 | -0.01 | target is flat |
| 2026-10-12T18:25 | MFI reversion | buy | SPY | 5.06 | — | entry |
| 2026-10-12T18:25 | MFI reversion | sell | ETHU | 3.13 | -0.00 | target is flat |
| 2026-10-12T18:25 | MFI reversion | sell | AAPL | 3.71 | -0.00 | exit signal |
| 2026-10-12T18:25 | VWAP reversion | buy | PLTR | 3.82 | — | entry |
| 2026-10-12T18:25 | VWAP reversion | sell | SOL-USD | 3.82 | -0.01 | rebalance down |
| 2026-10-12T18:25 | Z-score reversion | buy | ETH-USD | 3.33 | — | rebalance up |
| 2026-10-12T18:25 | Z-score reversion | sell | AMD | 4.00 | -0.00 | exit signal |
| 2026-10-12T18:25 | ROC + volume | sell | META | 18.19 | -0.02 | target is flat |
| 2026-10-12T18:20 | MFI reversion · 1h | buy | QQQ | 18.49 | — | entry |
| 2026-10-12T18:20 | MFI reversion · 1h | sell | NVDA | 4.66 | -0.01 | rebalance down |
| 2026-10-12T18:20 | Volume breakout · 1h | sell | MSFT | 22.88 | -0.05 | target is flat |
| 2026-10-12T18:20 | MFI reversion | buy | ETHU | 3.13 | — | entry |
| 2026-10-12T18:20 | Supertrend | sell | LABU | 15.07 | -0.02 | target is flat |
| 2026-10-12T18:19 | AI bee: Bizzy | buy | META | 8.54 | — | Jev: buy (buy p=0.61) |
| 2026-10-12T18:15 | Agent (ML meta-label) | buy | IWM | 5.01 | — | entry |
| 2026-10-12T18:15 | Agent (ML meta-label) | sell | AMD | 5.01 | -0.00 | selected signal exited |
| 2026-10-12T18:15 | MFI reversion · 1h | sell | BITX | 13.82 | -0.01 | target is flat |
| 2026-10-12T18:15 | ROC + volume · 1h | buy | TSLA | 6.59 | — | entry |
| 2026-10-12T18:15 | MFI reversion | buy | TSLA | 5.07 | — | entry |
| 2026-10-12T18:15 | VWAP reversion | buy | LABU | 1.30 | — | entry |
| 2026-10-12T18:15 | VWAP reversion | sell | TECL | 1.30 | 0.00 | target is flat |
| 2026-10-12T18:15 | Supertrend | buy | LABU | 15.08 | — | entry signal |
| 2026-10-12T18:15 | MACD zero-line | buy | NVDA | 12.80 | — | entry signal |
| 2026-10-12T18:10 | MFI reversion · 1h | buy | BITX | 13.83 | — | entry |
| 2026-10-12T18:10 | MFI reversion · 1h | sell | SOXL | 4.69 | 0.01 | rebalance down |
| 2026-10-12T18:10 | ROC + volume · 1h | sell | TSLA | 4.17 | -0.01 | target is flat |
| 2026-10-12T18:10 | ROC + volume · 1h | sell | SPY | 7.14 | -0.01 | target is flat |
| 2026-10-12T18:10 | MFI reversion | buy | TNA | 5.57 | — | entry |
| 2026-10-12T18:10 | MFI reversion | buy | IWM | 4.08 | — | rebalance up |
| 2026-10-12T18:10 | MFI reversion | buy | ETH-USD | 3.55 | — | rebalance up |
| 2026-10-12T18:10 | MFI reversion | sell | UPRO | 5.05 | -0.01 | stop-loss |
| 2026-10-12T18:10 | MFI reversion | sell | TSLA | 4.64 | -0.01 | target is flat |
| 2026-10-12T18:10 | MFI reversion | sell | SPY | 3.98 | -0.01 | target is flat |
| 2026-10-12T18:10 | MFI reversion | sell | PLTR | 4.00 | 0.00 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 18:25:05.000156+00:00 -> 2026-10-12 18:35:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
