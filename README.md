# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T18:55:05.000144+00:00 · 23903 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.93 (-7.07%)

Closed trades 75, win rate 40.0%, fees £2.63, max drawdown -7.49%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 31980 decisions in 2739 calls, $0.3973 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T18:55 | 6 / 21 / 2 | cash |  |
| Breezy | 2026-10-15T18:55 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-15T18:55 | 3 / 25 / 1 | COIN 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.56 | +0.42% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| VWAP reversion | PLTR | 1.50 | +3.07% | 7 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.48 | 4.48 | 0 | — | 4.53 | 2.16 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.06 | 4.06 | 1 | 100.0 | 4.82 | 1.27 | -7.93 | 9 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.03 | 1.80 | -3.27 | 19 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.05 | 2.05 | 9 | 66.7 | -3.80 | -1.19 | -9.61 | 27 |
| 5 | Copy: Insider buying | copy | 100.16 | 0.16 | 20 | 45.0 | -15.88 | -2.52 | -21.97 | 76 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.09 | 0.09 | 0 | — | 3.74 | 1.48 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.95 | -0.05 | 0 | — | -0.79 | -0.42 | -3.35 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 11 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 58 | 39.7 | -10.80 | -3.10 | -13.79 | 118 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.45 | -1.55 | 0 | — | -0.96 | -0.36 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 98.09 | -1.91 | 0 | — | 30.42 | 3.49 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.64 | -2.36 | 0 | — | -5.27 | -2.90 | -6.38 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Donchian 55/20 · 1h | breakout | 97.37 | -2.63 | 36 | 16.7 | 6.86 | 0.96 | -22.11 | 112 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 97.00 | -3.00 | 0 | — | -5.50 | -2.16 | -7.50 | 1 |
| 19 | Trend pullback · 1h | trend | 96.78 | -3.23 | 86 | 24.4 | -21.35 | -5.97 | -23.27 | 156 |
| 20 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.12 | -3.13 | -5.30 | 30 |
| 21 | ADX DI cross · 1h | trend | 96.02 | -3.98 | 70 | 21.4 | -10.16 | -1.84 | -15.22 | 252 |
| 22 | Daily: Momentum burst | daily | 95.94 | -4.06 | 5 | 20.0 | -4.48 | -0.53 | -17.67 | 39 |
| 23 | Agent (rotation) | meta | 95.65 | -4.35 | 105 | 31.4 | -13.63 | -4.67 | -14.71 | 290 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.17 | 1.12 | -9.46 | 101 |
| 25 | Parabolic SAR · 1h | trend | 93.70 | -6.30 | 93 | 22.6 | 3.11 | 0.58 | -22.05 | 281 |
| 26 | EMA 20/50 cross · 1h | trend | 93.43 | -6.57 | 51 | 15.7 | -0.96 | 0.09 | -23.29 | 132 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 93.40 | -6.60 | 0 | — | 4.95 | 0.90 | -13.89 | 1 |
| 28 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 8.94 | 2.25 | -6.78 | 202 |
| 29 | Max aggression: 5-day momentum | meta | 93.33 | -6.67 | 8 | 37.5 | -6.22 | -0.26 | -34.64 | 26 |
| 30 | Daily: Bullish score | daily | 93.24 | -6.76 | 7 | 0.0 | -4.25 | -0.35 | -12.76 | 13 |
| 31 | Agent | meta | 92.93 | -7.07 | 75 | 40.0 | -11.87 | -6.71 | -11.92 | 246 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 92.64 | -7.36 | 0 | — | -16.22 | -3.07 | -19.22 | 1 |
| 33 | MACD cross · 1h | trend | 92.51 | -7.49 | 154 | 22.1 | -13.08 | -1.78 | -24.60 | 460 |
| 34 | Bollinger breakout · 1h | breakout | 92.14 | -7.86 | 79 | 30.4 | 6.62 | 1.03 | -14.21 | 273 |
| 35 | RSI momentum · 1h | momentum | 91.77 | -8.23 | 73 | 17.8 | 0.75 | 0.30 | -26.08 | 223 |
| 36 | Supertrend · 1h | trend | 91.66 | -8.34 | 74 | 13.5 | -1.72 | 0.01 | -28.77 | 210 |
| 37 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -2.60 | -0.23 | -14.55 | 117 |
| 38 | Opening range 30m | breakout | 90.81 | -9.19 | 170 | 22.9 | -12.43 | -3.54 | -17.60 | 570 |
| 39 | Triple EMA stack · 1h | trend | 90.58 | -9.42 | 77 | 16.9 | -6.67 | -0.49 | -31.96 | 233 |
| 40 | Stochastic reversion · 1h | reversion | 90.53 | -9.47 | 128 | 44.5 | -16.22 | -3.03 | -19.84 | 350 |
| 41 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -7.21 | -2.73 | -7.47 | 121 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.20 | -6.91 | -24.94 | 245 |
| 44 | MFI reversion · 1h | reversion | 89.65 | -10.35 | 190 | 30.0 | -17.48 | -3.02 | -20.13 | 144 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -17.59 | -0.66 | -37.31 | 43 |
| 46 | OBV trend · 1h | momentum | 88.18 | -11.82 | 165 | 18.8 | -10.70 | -0.92 | -34.60 | 321 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.31 | -1.99 | -29.15 | 212 |
| 48 | Z-score reversion · 1h | reversion | 87.66 | -12.34 | 72 | 34.7 | -11.17 | -1.99 | -17.27 | 183 |
| 49 | MACD zero-line · 1h | trend | 87.60 | -12.40 | 74 | 16.2 | -21.42 | -4.13 | -22.26 | 225 |
| 50 | Agent (ML meta-label) | meta | 86.91 | -13.09 | 568 | 18.5 | -4.04 | -0.56 | -15.25 | 412 |
| 51 | Opening range 15m | breakout | 86.58 | -13.42 | 216 | 20.4 | -17.72 | -4.70 | -21.40 | 709 |
| 52 | Donchian 20/10 · 1h | breakout | 86.21 | -13.79 | 72 | 19.4 | 0.15 | 0.22 | -20.56 | 218 |
| 53 | ROC + volume · 1h | momentum | 86.15 | -13.85 | 180 | 21.7 | -8.54 | -1.03 | -25.31 | 398 |
| 54 | VWAP momentum · 1h | momentum | 86.10 | -13.90 | 354 | 21.8 | -35.13 | -5.17 | -43.06 | 1257 |
| 55 | Heikin-Ashi · 1h | trend | 85.97 | -14.03 | 170 | 26.5 | -30.23 | -4.89 | -39.15 | 671 |
| 56 | Three white soldiers | momentum | 85.61 | -14.39 | 196 | 18.4 | -47.54 | -19.03 | -48.92 | 600 |
| 57 | EMA 9/21 cross · 1h | trend | 84.78 | -15.22 | 120 | 12.5 | -5.43 | -0.42 | -29.09 | 319 |
| 58 | Bollinger reversion · 1h | reversion | 84.03 | -15.97 | 132 | 31.8 | -27.78 | -6.01 | -31.47 | 340 |
| 59 | Williams %R · 1h | reversion | 83.49 | -16.51 | 167 | 42.5 | -31.78 | -5.22 | -34.82 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 82.95 | -17.05 | 61 | 23.0 | -10.88 | -1.88 | -18.95 | 165 |
| 61 | CCI reversion · 1h | reversion | 82.94 | -17.06 | 141 | 41.8 | -15.92 | -2.05 | -23.38 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 79.97 | -20.03 | 182 | 25.3 | -32.41 | -5.99 | -33.65 | 520 |
| 63 | RSI(14) reversion | reversion | 66.68 | -33.32 | 570 | 28.8 | -73.23 | -16.16 | -74.13 | 1560 |
| 64 | ROC + volume | momentum | 66.14 | -33.86 | 516 | 22.1 | -74.70 | -16.91 | -76.47 | 1685 |
| 65 | Volume breakout | breakout | 65.01 | -34.99 | 313 | 13.4 | -63.54 | -17.88 | -63.54 | 890 |
| 66 | Squeeze breakout | breakout | 64.41 | -35.59 | 416 | 14.7 | -62.97 | -17.58 | -63.44 | 1213 |
| 67 | Donchian 55/20 | breakout | 63.57 | -36.43 | 403 | 17.4 | -68.79 | -14.15 | -71.15 | 1272 |
| 68 | EMA 20/50 cross | trend | 61.89 | -38.12 | 423 | 18.7 | -77.03 | -14.85 | -78.49 | 1441 |
| 69 | AI bee: Boozy | ai | 58.38 | -41.62 | 278 | 5.4 | — | — | — | — |
| 70 | VWAP reversion | reversion | 58.26 | -41.74 | 583 | 24.5 | -72.39 | -14.94 | -72.60 | 1428 |
| 71 | Keltner breakout | breakout | 56.08 | -43.92 | 578 | 15.2 | -83.37 | -26.21 | -83.49 | 1842 |
| 72 | Supertrend | trend | 54.72 | -45.27 | 591 | 19.1 | -86.30 | -19.88 | -86.59 | 1909 |
| 73 | Ichimoku | trend | 53.44 | -46.56 | 509 | 10.4 | -81.99 | -22.35 | -82.09 | 1713 |
| 74 | AI bee: Bizzy | ai | 50.97 | -49.03 | 1027 | 8.7 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.59 | -28.83 | -98.63 | 5311 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -28.51 | -93.47 | 2583 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.47 | -23.87 | -90.66 | 2354 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.59 | -26.18 | -91.60 | 2327 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -31.27 | -97.47 | 3514 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -33.89 | -96.59 | 3569 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -24.17 | -94.39 | 2612 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -34.79 | -99.40 | 5730 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.15 | -24.94 | -91.20 | 2626 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.19 | -30.22 | -96.19 | 3549 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.93 | -99.73 | 6153 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -28.54 | -91.85 | 2366 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -36.09 | -97.46 | 3649 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -35.16 | -98.53 | 4687 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.57 | -31.47 | -93.58 | 2788 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.41 | -99.55 | 6175 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.07 | -21.71 | -86.36 | 2102 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.42 | -26.09 | -87.79 | 2106 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.97 | -31.49 | -96.08 | 3766 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.37 | -32.68 | -89.47 | 2109 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -32.38 | -95.85 | 4077 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.49 | -99.89 | 8222 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T18:54 | AI bee: Bizzy | sell | MSTR | 7.20 | 0.02 | Jev: sell (sell p=0.57) after 25 min |
| 2026-10-15T18:50 | Ichimoku | buy | ETHU | 13.34 | — | entry signal |
| 2026-10-15T18:45 | MFI reversion · 1h | sell | ETHU | 11.24 | 0.06 | target is flat |
| 2026-10-15T18:45 | Keltner breakout | buy | COIN | 14.03 | — | entry signal |
| 2026-10-15T18:45 | Supertrend | buy | COIN | 3.65 | — | entry signal |
| 2026-10-15T18:41 | ROC + volume | sell | AMD | 16.56 | -0.05 | exit signal |
| 2026-10-15T18:35 | RSI(14) reversion | buy | AAPL | 16.67 | — | entry signal |
| 2026-10-15T18:35 | Supertrend | buy | NVDA | 2.86 | — | rebalance up |
| 2026-10-15T18:35 | Supertrend | sell | GOOGL | 2.60 | -0.01 | exit signal |
| 2026-10-15T18:30 | MFI reversion · 1h | sell | TNA | 9.91 | -0.02 | target is flat |
| 2026-10-15T18:30 | CCI reversion · 1h | buy | AMD | 2.40 | — | entry signal |
| 2026-10-15T18:30 | OBV trend · 1h | sell | AAPL | 21.76 | -0.20 | exit signal |
| 2026-10-15T18:30 | Ichimoku · 1h | sell | AAPL | 22.70 | -0.02 | exit signal |
| 2026-10-15T18:30 | VWAP reversion | buy | AAPL | 14.58 | — | entry signal |
| 2026-10-15T18:29 | AI bee: Bizzy | buy | MSTR | 7.18 | — | Jev: buy (buy p=0.56) |
| 2026-10-15T18:25 | MFI reversion · 1h | buy | TNA | 9.93 | — | entry |
| 2026-10-15T18:25 | Squeeze breakout | sell | IWM | 12.87 | -0.03 | exit signal |
| 2026-10-15T18:25 | Donchian 55/20 | buy | META | 5.76 | — | entry |
| 2026-10-15T18:25 | Donchian 55/20 | sell | SOL-USD | 6.28 | 0.05 | exit signal |
| 2026-10-15T18:25 | Supertrend | sell | SOL-USD | 3.02 | 0.04 | exit signal |
| 2026-10-15T18:21 | Agent (aggressive) | sell | META | 45.02 | -0.14 | selected signal exited |
| 2026-10-15T18:21 | Agent | sell | META | 18.57 | -0.06 | selected signal exited |
| 2026-10-15T18:21 | ROC + volume | sell | META | 16.56 | -0.03 | exit signal |
| 2026-10-15T18:21 | ROC + volume | sell | DOGE-USD | 16.49 | -0.12 | exit signal |
| 2026-10-15T18:21 | Ichimoku | sell | AMZN | 13.34 | -0.04 | exit signal |
| 2026-10-15T18:21 | Supertrend | sell | AMZN | 3.02 | 0.00 | exit signal |
| 2026-10-15T18:15 | ROC + volume | buy | META | 8.25 | — | rebalance up |
| 2026-10-15T18:15 | ROC + volume | buy | DOGE-USD | 7.10 | — | rebalance up |
| 2026-10-15T18:15 | ROC + volume | buy | AMD | 8.23 | — | rebalance up |
| 2026-10-15T18:15 | ROC + volume | sell | SOXL | 8.16 | -0.21 | stop-loss |
| 2026-10-15T18:15 | ROC + volume | sell | ETH-USD | 8.32 | -0.10 | exit signal |
| 2026-10-15T18:15 | ROC + volume | sell | COIN | 8.31 | -0.05 | stop-loss |
| 2026-10-15T18:15 | Ichimoku | buy | TNA | 8.00 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | buy | IWM | 8.02 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | buy | AMZN | 8.90 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | buy | AMD | 6.69 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | sell | XRP-USD | 4.45 | 0.04 | exit signal |
| 2026-10-15T18:15 | Ichimoku | sell | META | 4.45 | 0.00 | exit signal |
| 2026-10-15T18:15 | Ichimoku | sell | GOOGL | 5.35 | -0.01 | stop-loss |
| 2026-10-15T18:15 | Ichimoku | sell | DOGE-USD | 5.32 | -0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 18:55:05.000144+00:00 -> 2026-10-15 19:05:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
