# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T16:24:05.000169+00:00 · 20382 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.43 (-4.57%)

Closed trades 56, win rate 51.8%, fees £2.19, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AAPL | 19.11 | +0.01 |
| PLTR | 19.04 | -0.06 |
| TNA | 19.12 | +0.03 |

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

Today: 20253 decisions in 2373 calls, $0.2601 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T16:24 | 2 / 12 / 15 | cash |  |
| Breezy | 2026-10-12T16:24 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-12T16:24 | 1 / 26 / 2 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.78 | 2.78 | 0 | — | -0.26 | -0.07 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.32 | 2.32 | 14 | 57.1 | -12.33 | -2.02 | -20.64 | 71 |
| 3 | VWAP reversion · 1h | reversion | 102.29 | 2.29 | 39 | 41.0 | -8.32 | -2.52 | -13.79 | 118 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Hold SPY | benchmark | 101.44 | 1.44 | 0 | — | 0.98 | 0.62 | -3.66 | 1 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.28 | 1.28 | 0 | — | 1.57 | 0.77 | -3.62 | 1 |
| 7 | Timing: Nasdaq FTD · TQQQ | daily | 101.17 | 1.17 | 0 | — | -4.62 | -0.75 | -15.27 | 1 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.03 | 1.03 | 6 | 50.0 | 4.42 | 1.96 | -3.27 | 16 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.75 | 0.75 | 0 | — | -1.05 | -0.55 | -5.09 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 99.85 | -0.15 | 0 | — | -4.06 | -1.87 | -5.36 | 1 |
| 13 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.84 | -0.16 | 6 | 50.0 | -4.47 | -1.49 | -9.74 | 25 |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.82 | -0.18 | 0 | — | 2.64 | 1.06 | -5.18 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 10 | 30.0 | 3.94 | 1.25 | -7.55 | 43 |
| 16 | Hold BTC | benchmark | 99.16 | -0.84 | 0 | — | 30.05 | 3.53 | -8.68 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 4.88 | 2.37 | -1.95 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 19 | Max aggression: 1-day momentum | meta | 98.97 | -1.03 | 11 | 36.4 | -15.83 | -0.56 | -37.31 | 42 |
| 20 | Donchian 55/20 · 1h | breakout | 98.07 | -1.93 | 31 | 12.9 | 12.93 | 1.56 | -16.92 | 114 |
| 21 | Trend pullback · 1h | trend | 97.95 | -2.05 | 78 | 23.1 | -22.85 | -6.35 | -25.60 | 167 |
| 22 | Stochastic reversion · 1h | reversion | 97.85 | -2.15 | 96 | 53.1 | -10.97 | -2.12 | -13.74 | 333 |
| 23 | Daily: Bullish score | daily | 97.80 | -2.20 | 4 | 0.0 | 0.76 | 0.29 | -12.76 | 11 |
| 24 | Z-score reversion · 1h | reversion | 97.37 | -2.63 | 44 | 43.2 | 3.93 | 0.91 | -8.60 | 156 |
| 25 | Three white soldiers · 1h | momentum | 97.20 | -2.80 | 7 | 0.0 | -3.33 | -2.57 | -4.50 | 27 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 97.11 | -2.89 | 0 | — | 9.56 | 1.58 | -8.33 | 1 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.74 | -0.25 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.33 | -3.67 | 62 | 19.4 | 0.12 | 0.18 | -13.84 | 259 |
| 29 | Agent (rotation) | meta | 96.17 | -3.83 | 82 | 29.3 | -11.83 | -3.64 | -16.13 | 288 |
| 30 | MACD cross · 1h | trend | 96.14 | -3.85 | 120 | 24.2 | -13.34 | -2.19 | -17.32 | 468 |
| 31 | Parabolic SAR · 1h | trend | 95.83 | -4.17 | 83 | 21.7 | 1.75 | 0.41 | -21.52 | 291 |
| 32 | EMA 20/50 cross · 1h | trend | 95.77 | -4.23 | 44 | 13.6 | 5.99 | 0.86 | -23.39 | 134 |
| 33 | Agent | meta | 95.43 | -4.57 | 56 | 51.8 | -12.14 | -6.30 | -12.38 | 247 |
| 34 | Supertrend · 1h | trend | 94.65 | -5.35 | 58 | 13.8 | 0.96 | 0.31 | -18.27 | 212 |
| 35 | Gap and go | momentum | 93.92 | -6.08 | 58 | 12.1 | 8.51 | 2.17 | -6.20 | 202 |
| 36 | MFI reversion · 1h | reversion | 93.71 | -6.29 | 122 | 34.4 | -7.58 | -1.14 | -16.97 | 125 |
| 37 | Squeeze breakout · 1h | breakout | 93.67 | -6.33 | 39 | 23.1 | 3.99 | 0.89 | -9.37 | 105 |
| 38 | Agent (aggressive) | meta | 93.57 | -6.43 | 26 | 42.3 | -10.97 | -3.61 | -11.25 | 118 |
| 39 | Connors RSI(2) · 1h | reversion | 92.84 | -7.16 | 114 | 43.0 | -18.40 | -6.06 | -21.04 | 253 |
| 40 | Agent (ML meta-label) | meta | 92.72 | -7.28 | 421 | 18.5 | -5.02 | -0.85 | -13.89 | 424 |
| 41 | RSI(14) reversion · 1h | reversion | 92.66 | -7.34 | 30 | 30.0 | -5.35 | -1.05 | -9.03 | 141 |
| 42 | RSI momentum · 1h | momentum | 92.58 | -7.42 | 66 | 15.2 | 0.59 | 0.27 | -21.47 | 228 |
| 43 | Bollinger reversion · 1h | reversion | 92.07 | -7.93 | 82 | 37.8 | -21.72 | -5.18 | -23.37 | 317 |
| 44 | Volume breakout · 1h | breakout | 91.66 | -8.34 | 63 | 20.6 | 9.00 | 1.37 | -12.60 | 118 |
| 45 | Ichimoku · 1h | trend | 91.12 | -8.88 | 47 | 17.0 | 0.99 | 0.32 | -22.17 | 125 |
| 46 | Bollinger breakout · 1h | breakout | 91.02 | -8.98 | 74 | 28.4 | 8.54 | 1.23 | -13.96 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.90 | -9.10 | 71 | 15.5 | -7.59 | -0.68 | -27.26 | 238 |
| 48 | Williams %R · 1h | reversion | 90.19 | -9.81 | 130 | 46.9 | -26.01 | -4.42 | -27.33 | 505 |
| 49 | Opening range 30m | breakout | 89.91 | -10.09 | 150 | 22.0 | -15.28 | -4.63 | -15.63 | 567 |
| 50 | CCI reversion · 1h | reversion | 89.51 | -10.49 | 111 | 45.9 | -6.13 | -0.70 | -14.35 | 407 |
| 51 | Candlestick reversal · 1h | reversion | 88.79 | -11.21 | 126 | 31.7 | -27.61 | -5.34 | -28.45 | 493 |
| 52 | OBV trend · 1h | momentum | 88.67 | -11.33 | 150 | 18.7 | -7.62 | -0.67 | -27.93 | 322 |
| 53 | VWAP momentum · 1h | momentum | 88.43 | -11.57 | 301 | 23.3 | -32.96 | -4.91 | -40.06 | 1257 |
| 54 | Heikin-Ashi · 1h | trend | 88.20 | -11.80 | 149 | 28.2 | -29.89 | -4.95 | -37.33 | 690 |
| 55 | Donchian 20/10 · 1h | breakout | 87.90 | -12.10 | 63 | 17.5 | -0.30 | 0.17 | -19.17 | 214 |
| 56 | MACD zero-line · 1h | trend | 87.81 | -12.19 | 67 | 17.9 | -14.87 | -2.41 | -21.10 | 233 |
| 57 | EMA 9/21 cross · 1h | trend | 87.45 | -12.55 | 107 | 13.1 | -10.29 | -1.21 | -23.04 | 330 |
| 58 | Opening range 15m | breakout | 87.23 | -12.77 | 177 | 20.3 | -17.73 | -4.95 | -18.93 | 690 |
| 59 | Max aggression: 5-day momentum | meta | 87.13 | -12.87 | 7 | 28.6 | -15.22 | -1.13 | -34.64 | 28 |
| 60 | Keltner breakout · 1h | breakout | 86.90 | -13.10 | 45 | 20.0 | -10.89 | -1.18 | -26.55 | 216 |
| 61 | Three white soldiers | momentum | 86.72 | -13.29 | 148 | 16.9 | -48.54 | -23.26 | -48.70 | 590 |
| 62 | ROC + volume · 1h | momentum | 86.11 | -13.89 | 139 | 21.6 | -8.38 | -0.95 | -24.56 | 400 |
| 63 | ROC + volume | momentum | 72.95 | -27.05 | 415 | 22.7 | -72.83 | -16.44 | -74.36 | 1675 |
| 64 | RSI(14) reversion | reversion | 71.43 | -28.57 | 400 | 27.0 | -72.59 | -17.93 | -72.73 | 1484 |
| 65 | Squeeze breakout | breakout | 69.91 | -30.09 | 347 | 15.3 | -62.18 | -17.93 | -62.36 | 1223 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -62.14 | -17.64 | -62.29 | 899 |
| 67 | EMA 20/50 cross | trend | 68.07 | -31.93 | 351 | 19.7 | -76.20 | -14.94 | -76.22 | 1430 |
| 68 | Donchian 55/20 | breakout | 67.22 | -32.78 | 356 | 17.7 | -68.33 | -14.44 | -68.84 | 1293 |
| 69 | VWAP reversion | reversion | 66.47 | -33.52 | 420 | 26.0 | -70.90 | -15.57 | -71.04 | 1404 |
| 70 | Keltner breakout | breakout | 60.73 | -39.27 | 477 | 14.5 | -83.55 | -27.33 | -83.59 | 1848 |
| 71 | Supertrend | trend | 60.53 | -39.47 | 492 | 19.3 | -85.94 | -20.71 | -86.04 | 1902 |
| 72 | AI bee: Boozy | ai | 60.23 | -39.77 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.61 | -42.39 | 430 | 10.0 | -82.14 | -22.93 | -82.15 | 1743 |
| 74 | MFI reversion | reversion | 56.21 | -43.79 | 558 | 20.1 | -87.73 | -27.96 | -87.75 | 2103 |
| 75 | Z-score reversion | reversion | 56.16 | -43.84 | 540 | 21.5 | -85.54 | -22.88 | -85.58 | 2063 |
| 76 | AI bee: Bizzy | ai | 55.83 | -44.17 | 879 | 8.4 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.28 | -45.72 | 573 | 10.1 | -89.10 | -34.14 | -89.10 | 2099 |
| 78 | Donchian 20/10 | breakout | 52.48 | -47.52 | 667 | 17.7 | -90.83 | -25.61 | -90.89 | 2650 |
| 79 | MACD zero-line | trend | 51.45 | -48.55 | 618 | 14.6 | -91.37 | -29.09 | -91.43 | 2346 |
| 80 | RSI momentum | momentum | 51.03 | -48.97 | 644 | 16.6 | -90.52 | -25.56 | -90.54 | 2374 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -30.39 | -98.63 | 5390 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.38 | -26.81 | -91.38 | 2343 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.18 | -29.77 | -93.21 | 2612 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -32.74 | -97.35 | 3522 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -35.25 | -96.39 | 3603 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -25.71 | -94.41 | 2655 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.24 | -99.35 | 5615 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.34 | -96.37 | 3602 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.11 | -99.73 | 6135 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -37.47 | -97.34 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.37 | -98.48 | 4658 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.45 | -32.69 | -93.45 | 2801 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.46 | -99.52 | 6093 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.81 | -95.86 | 3716 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -33.87 | -95.68 | 4033 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.34 | -99.89 | 8238 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T16:20 | AI bee: Bizzy | sell | AMD | 8.75 | -0.02 | Jev: sell (sell p=0.51) after 12 min |
| 2026-10-12T16:20 | VWAP momentum · 1h | buy | PLTR | 4.45 | — | rebalance up |
| 2026-10-12T16:20 | VWAP momentum · 1h | sell | META | 4.45 | 0.00 | rebalance down |
| 2026-10-12T16:20 | MFI reversion | sell | SOXL | 11.24 | -0.01 | target is flat |
| 2026-10-12T16:20 | MACD zero-line | buy | ETH-USD | 2.94 | — | entry signal |
| 2026-10-12T16:20 | MACD zero-line | sell | BITX | 2.94 | -0.00 | rebalance down |
| 2026-10-12T16:15 | Volume breakout · 1h | buy | MSFT | 22.93 | — | entry |
| 2026-10-12T16:15 | ROC + volume · 1h | sell | TSLA | 7.16 | -0.02 | target is flat |
| 2026-10-12T16:15 | VWAP momentum · 1h | buy | PLTR | 4.42 | — | rebalance up |
| 2026-10-12T16:15 | VWAP momentum · 1h | sell | MSFT | 4.42 | 0.03 | rebalance down |
| 2026-10-12T16:15 | ROC + volume | sell | MSFT | 18.23 | -0.02 | target is flat |
| 2026-10-12T16:15 | ADX DI cross | buy | XRP-USD | 2.62 | — | entry |
| 2026-10-12T16:15 | ADX DI cross | buy | TQQQ | 3.39 | — | rebalance up |
| 2026-10-12T16:15 | ADX DI cross | sell | TECL | 6.01 | -0.02 | exit signal |
| 2026-10-12T16:15 | MACD zero-line | buy | BTC-USD | 6.84 | — | entry signal |
| 2026-10-12T16:14 | AI bee: Bizzy | sell | TECL | 7.70 | -0.02 | Jev: sell (sell p=0.61) after 15 min |
| 2026-10-12T16:10 | Agent | buy | PLTR | 19.10 | — | following VWAP momentum · 1h |
| 2026-10-12T16:10 | Volume breakout · 1h | sell | MSFT | 22.93 | -0.01 | target is flat |
| 2026-10-12T16:10 | ROC + volume · 1h | buy | PLTR | 6.63 | — | entry |
| 2026-10-12T16:10 | VWAP momentum · 1h | buy | PLTR | 8.86 | — | entry |
| 2026-10-12T16:10 | VWAP momentum · 1h | sell | SQQQ | 4.46 | -0.02 | rebalance down |
| 2026-10-12T16:10 | MFI reversion | buy | MSTR | 4.70 | — | rebalance up |
| 2026-10-12T16:10 | MFI reversion | buy | COIN | 4.74 | — | rebalance up |
| 2026-10-12T16:10 | MFI reversion | sell | GOOGL | 11.23 | -0.03 | exit signal |
| 2026-10-12T16:10 | Keltner breakout | sell | META | 15.19 | -0.01 | exit signal |
| 2026-10-12T16:10 | Donchian 20/10 | buy | TECL | 4.37 | — | entry signal |
| 2026-10-12T16:10 | Donchian 20/10 | sell | SPY | 4.37 | -0.00 | rebalance down |
| 2026-10-12T16:10 | RSI momentum | buy | BITX | 2.96 | — | entry signal |
| 2026-10-12T16:10 | RSI momentum | sell | MSFT | 2.96 | 0.01 | rebalance down |
| 2026-10-12T16:10 | ROC + volume | buy | MSFT | 18.24 | — | entry |
| 2026-10-12T16:10 | Ichimoku | buy | BITX | 14.41 | — | entry signal |
| 2026-10-12T16:10 | ADX DI cross | buy | TQQQ | 3.39 | — | entry signal |
| 2026-10-12T16:10 | ADX DI cross | buy | TECL | 6.04 | — | entry signal |
| 2026-10-12T16:10 | ADX DI cross | sell | BTC-USD | 2.99 | -0.02 | rebalance down |
| 2026-10-12T16:10 | MACD zero-line | buy | BITX | 10.30 | — | entry |
| 2026-10-12T16:10 | MACD zero-line | sell | PLTR | 8.55 | -0.04 | exit signal |
| 2026-10-12T16:10 | MACD zero-line | sell | AMZN | 8.58 | -0.03 | exit signal |
| 2026-10-12T16:09 | AI bee: Bizzy | sell | NANC | 10.07 | -0.02 | Jev: sell (sell p=0.80) after 4114 min |
| 2026-10-12T16:08 | AI bee: Bizzy | buy | AMD | 8.76 | — | Jev: buy (buy p=0.63) |
| 2026-10-12T16:06 | Donchian 20/10 | buy | NVDA | 2.63 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 16:24:05.000169+00:00 -> 2026-10-12 16:34:05.000169+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
