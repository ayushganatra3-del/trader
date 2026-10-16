# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T17:25:05.000150+00:00 · 25015 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.89 (-8.11%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.19 | -0.18 |
| SQQQ | 19.03 | +0.66 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 27677 decisions in 2596 calls, $0.3475 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T17:25 | 7 / 16 / 7 | cash |  |
| Breezy | 2026-10-16T17:25 | 0 / 22 / 8 | cash |  |
| Boozy | 2026-10-16T17:25 | 1 / 26 / 3 | COIN 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.78 | 6.78 | 9 | 66.7 | 8.27 | 3.00 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.07 | 6.07 | 10 | 70.0 | 0.34 | 0.19 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.89 | 4.89 | 14 | 35.7 | 7.21 | 1.89 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.06 | 4.06 | 0 | — | 5.17 | 2.51 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.87 | -0.12 | 0 | — | 3.97 | 1.57 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.60 | -0.41 | 59 | 39.0 | -11.54 | -3.34 | -13.79 | 126 |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.29 | -0.71 | 1 | 100.0 | 0.44 | 0.22 | -7.93 | 9 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.76 | -3.91 | 20 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.65 | -1.34 | 51 | 31.4 | 1.87 | 1.04 | -2.96 | 69 |
| 12 | Donchian 55/20 · 1h | breakout | 98.63 | -1.37 | 36 | 16.7 | 8.82 | 1.18 | -22.12 | 109 |
| 13 | Hold SPY | benchmark | 98.62 | -1.38 | 0 | — | -1.54 | -0.84 | -3.23 | 1 |
| 14 | Copy: Insider buying | copy | 98.47 | -1.53 | 20 | 45.0 | -12.07 | -2.06 | -20.62 | 75 |
| 15 | Max aggression: 5-day momentum | meta | 98.00 | -2.00 | 8 | 37.5 | -17.78 | -1.47 | -34.64 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.25 | -2.75 | 0 | — | -4.87 | -1.95 | -7.50 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 97.17 | -2.83 | 0 | — | -1.84 | -0.74 | -4.50 | 1 |
| 18 | Agent (rotation) | meta | 96.65 | -3.35 | 107 | 32.7 | -9.96 | -3.42 | -13.23 | 298 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.56 | -3.44 | 0 | — | -6.45 | -3.52 | -6.67 | 1 |
| 20 | Trend pullback · 1h | trend | 96.20 | -3.80 | 87 | 24.1 | -21.64 | -6.43 | -22.37 | 152 |
| 21 | Hold BTC | benchmark | 95.92 | -4.08 | 0 | — | 27.91 | 3.26 | -8.68 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.60 | -5.40 | 81 | 19.8 | -8.97 | -1.60 | -13.33 | 258 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.56 | 0.82 | -9.46 | 101 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.31 | -6.78 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.16 | -6.84 | 95 | 22.1 | 3.23 | 0.59 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 93.13 | -6.87 | 5 | 20.0 | -7.04 | -0.93 | -19.89 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.76 | -7.24 | 54 | 14.8 | -4.34 | -0.39 | -22.92 | 129 |
| 29 | Agent | meta | 91.89 | -8.11 | 77 | 39.0 | -11.26 | -6.36 | -12.17 | 246 |
| 30 | Agent (aggressive) | meta | 91.80 | -8.20 | 38 | 31.6 | -6.94 | -2.45 | -9.83 | 124 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 32 | RSI momentum · 1h | momentum | 91.03 | -8.97 | 76 | 17.1 | 0.67 | 0.29 | -26.55 | 219 |
| 33 | Opening range 30m | breakout | 91.01 | -8.99 | 193 | 29.5 | -12.41 | -3.43 | -17.60 | 572 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.47 | 0.89 | -14.21 | 274 |
| 35 | Daily: Bullish score | daily | 90.41 | -9.59 | 7 | 0.0 | -6.21 | -0.61 | -12.93 | 13 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 37 | Triple EMA stack · 1h | trend | 90.20 | -9.80 | 80 | 16.2 | -8.74 | -0.70 | -33.23 | 235 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.86 | -10.14 | 0 | — | -19.37 | -3.69 | -20.01 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.58 | -10.42 | 0 | — | 0.24 | 0.21 | -13.89 | 1 |
| 40 | MACD cross · 1h | trend | 89.08 | -10.92 | 169 | 23.1 | -14.68 | -1.94 | -27.71 | 454 |
| 41 | Supertrend · 1h | trend | 89.04 | -10.96 | 79 | 12.7 | -4.05 | -0.26 | -30.09 | 213 |
| 42 | Keltner breakout · 1h | breakout | 88.92 | -11.08 | 52 | 23.1 | -9.54 | -1.18 | -27.05 | 210 |
| 43 | Connors RSI(2) · 1h | reversion | 88.01 | -11.99 | 144 | 40.3 | -24.90 | -7.41 | -25.74 | 243 |
| 44 | OBV trend · 1h | momentum | 87.94 | -12.06 | 168 | 18.5 | -8.94 | -0.73 | -33.94 | 320 |
| 45 | Stochastic reversion · 1h | reversion | 87.07 | -12.93 | 135 | 43.7 | -20.49 | -3.72 | -21.55 | 349 |
| 46 | Opening range 15m | breakout | 86.44 | -13.56 | 242 | 25.2 | -17.39 | -4.52 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.24 | -4.56 | -23.33 | 224 |
| 48 | Max aggression: 1-day momentum | meta | 84.86 | -15.14 | 14 | 35.7 | -11.82 | -0.31 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.84 | -15.16 | 78 | 17.9 | 0.71 | 0.29 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.72 | -15.28 | 207 | 18.8 | -47.86 | -19.97 | -48.52 | 609 |
| 51 | Z-score reversion · 1h | reversion | 84.51 | -15.49 | 82 | 32.9 | -14.39 | -2.55 | -18.68 | 180 |
| 52 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -21.53 | -3.61 | -21.81 | 142 |
| 53 | Heikin-Ashi · 1h | trend | 83.75 | -16.25 | 189 | 24.3 | -31.26 | -5.11 | -40.33 | 673 |
| 54 | VWAP momentum · 1h | momentum | 83.70 | -16.30 | 386 | 21.2 | -36.33 | -5.50 | -43.85 | 1253 |
| 55 | Agent (ML meta-label) | meta | 83.56 | -16.44 | 599 | 18.9 | -6.10 | -0.64 | -17.51 | 392 |
| 56 | ROC + volume · 1h | momentum | 82.90 | -17.10 | 191 | 21.5 | -12.48 | -1.65 | -26.33 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.16 | -17.84 | 126 | 11.9 | -7.31 | -0.66 | -29.65 | 320 |
| 58 | Williams %R · 1h | reversion | 80.82 | -19.18 | 180 | 42.2 | -34.06 | -5.58 | -35.16 | 524 |
| 59 | Bollinger reversion · 1h | reversion | 80.55 | -19.45 | 138 | 31.2 | -29.95 | -6.21 | -31.83 | 337 |
| 60 | RSI(14) reversion · 1h | reversion | 80.14 | -19.86 | 70 | 21.4 | -14.86 | -2.64 | -21.29 | 165 |
| 61 | CCI reversion · 1h | reversion | 79.74 | -20.26 | 158 | 39.2 | -18.69 | -2.43 | -24.55 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 76.32 | -23.68 | 201 | 25.4 | -35.01 | -6.29 | -35.50 | 519 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.50 | -18.21 | -63.50 | 895 |
| 64 | ROC + volume | momentum | 63.31 | -36.69 | 546 | 21.8 | -75.84 | -17.52 | -77.44 | 1720 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -63.00 | -17.84 | -63.91 | 1218 |
| 66 | RSI(14) reversion | reversion | 63.04 | -36.96 | 619 | 27.0 | -74.61 | -16.71 | -74.62 | 1601 |
| 67 | Donchian 55/20 | breakout | 61.38 | -38.62 | 434 | 17.7 | -69.23 | -14.49 | -71.81 | 1285 |
| 68 | EMA 20/50 cross | trend | 59.81 | -40.19 | 454 | 19.2 | -77.25 | -15.12 | -79.04 | 1451 |
| 69 | AI bee: Boozy | ai | 55.93 | -44.07 | 292 | 5.8 | — | — | — | — |
| 70 | VWAP reversion | reversion | 55.71 | -44.29 | 631 | 22.8 | -73.53 | -15.45 | -73.53 | 1487 |
| 71 | Keltner breakout | breakout | 54.66 | -45.34 | 606 | 16.0 | -83.55 | -26.68 | -83.66 | 1843 |
| 72 | Ichimoku | trend | 51.90 | -48.10 | 552 | 11.6 | -82.01 | -22.77 | -82.11 | 1733 |
| 73 | Supertrend | trend | 51.78 | -48.22 | 632 | 19.8 | -86.44 | -20.32 | -86.85 | 1910 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -29.40 | -98.64 | 5313 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -29.90 | -93.54 | 2602 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.53 | -24.54 | -90.58 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.82 | -27.13 | -91.83 | 2345 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -32.12 | -97.47 | 3530 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -36.00 | -96.74 | 3609 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.42 | -26.24 | -94.48 | 2626 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.90 | -99.41 | 5794 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.41 | -25.74 | -91.47 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.69 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.73 | -99.73 | 6191 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.10 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -37.51 | -97.47 | 3653 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.08 | -98.50 | 4724 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.68 | -32.72 | -93.72 | 2808 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.20 | -99.55 | 6225 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.65 | -22.19 | -86.65 | 2148 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.07 | -27.26 | -88.08 | 2135 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -32.24 | -96.01 | 3806 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -33.53 | -89.28 | 2104 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.88 | -33.59 | -95.88 | 4148 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.99 | -99.89 | 8263 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T17:25 | VWAP reversion | buy | XRP-USD | 2.21 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | UPRO | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | TQQQ | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | TNA | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | SOXL | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | SOL-USD | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | QQQ | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | NVDA | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | MSTR | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | MSFT | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | META | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | LABU | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | IWM | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | ETHU | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | ETH-USD | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | COIN | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | BTC-USD | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | buy | BITX | 2.23 | — | entry signal |
| 2026-10-16T17:25 | VWAP reversion | sell | TSLA | 5.71 | -0.01 | rebalance down |
| 2026-10-16T17:25 | VWAP reversion | sell | TECL | 5.74 | -0.00 | rebalance down |
| 2026-10-16T17:25 | VWAP reversion | sell | SPY | 5.74 | -0.01 | rebalance down |
| 2026-10-16T17:25 | VWAP reversion | sell | PLTR | 5.74 | -0.06 | rebalance down |
| 2026-10-16T17:25 | VWAP reversion | sell | GOOGL | 5.74 | -0.00 | rebalance down |
| 2026-10-16T17:25 | VWAP reversion | sell | AMZN | 5.73 | -0.01 | rebalance down |
| 2026-10-16T17:25 | VWAP reversion | sell | AAPL | 5.74 | -0.00 | rebalance down |
| 2026-10-16T17:25 | RSI(14) reversion | buy | NVDA | 12.61 | — | entry signal |
| 2026-10-16T17:25 | RSI(14) reversion | buy | MSTR | 12.61 | — | entry signal |
| 2026-10-16T17:25 | RSI(14) reversion | sell | TECL | 3.16 | -0.02 | rebalance down |
| 2026-10-16T17:25 | RSI(14) reversion | sell | LABU | 3.18 | -0.02 | rebalance down |
| 2026-10-16T17:25 | RSI(14) reversion | sell | GOOGL | 3.16 | -0.00 | rebalance down |
| 2026-10-16T17:20 | Agent (ML meta-label) | buy | TECL | 4.58 | — | rebalance up |
| 2026-10-16T17:20 | Agent (ML meta-label) | buy | SOXL | 4.85 | — | rebalance up |
| 2026-10-16T17:20 | Agent (ML meta-label) | buy | ETH-USD | 4.79 | — | rebalance up |
| 2026-10-16T17:20 | Agent (ML meta-label) | buy | AAPL | 4.76 | — | rebalance up |
| 2026-10-16T17:20 | Agent (ML meta-label) | sell | TNA | 5.24 | -0.11 | selected signal exited |
| 2026-10-16T17:20 | MFI reversion · 1h | sell | TNA | 20.68 | -1.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T17:20 | MFI reversion · 1h | sell | ETHU | 20.67 | -0.99 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-16T17:20 | CCI reversion · 1h | buy | SOXL | 4.41 | — | rebalance up |
| 2026-10-16T17:20 | CCI reversion · 1h | buy | NVDA | 4.38 | — | rebalance up |
| 2026-10-16T17:20 | CCI reversion · 1h | buy | IWM | 4.37 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 17:25:05.000150+00:00 -> 2026-10-16 17:35:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
