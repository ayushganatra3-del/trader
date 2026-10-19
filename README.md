# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T00:55:05.000134+00:00 · 27801 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.97 (-8.03%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.14 | -0.24 |
| SQQQ | 19.17 | +0.79 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, FLSC 12%, REF 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 660 decisions in 132 calls, $0.0093 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T00:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-19T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T00:55 | 3 / 2 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | BITX | 2.25 | +2.55% | 6 |
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.06 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.44 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.00 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.76 | 4.76 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.88 | -0.12 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.51 | -0.49 | 64 | 39.1 | -11.25 | -3.24 | -13.79 | 140 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.81 | -1.19 | 36 | 16.7 | -2.87 | -0.21 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.69 | -1.31 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.56 | -1.44 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.11 | -1.89 | 20 | 45.0 | -13.17 | -2.35 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 97.59 | -2.41 | 0 | — | 27.81 | 3.28 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.11 | -2.89 | 108 | 33.3 | -5.34 | -2.76 | -6.59 | 280 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.40 | -3.60 | 0 | — | -6.58 | -3.57 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.38 | -3.62 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.20 | -3.80 | 87 | 24.1 | -19.10 | -5.70 | -19.70 | 138 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.51 | -4.49 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.40 | -4.60 | 12 | 0.0 | -0.04 | 0.02 | -5.48 | 33 |
| 23 | ADX DI cross · 1h | trend | 94.65 | -5.36 | 82 | 19.5 | -6.54 | -1.08 | -14.49 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 3.26 | 0.78 | -9.46 | 97 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.95 | -7.05 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.91 | -7.09 | 97 | 21.6 | -9.86 | -1.52 | -22.75 | 274 |
| 28 | EMA 20/50 cross · 1h | trend | 92.55 | -7.45 | 55 | 14.5 | -18.32 | -3.14 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.13 | -7.87 | 38 | 31.6 | -5.81 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.97 | -8.03 | 77 | 39.0 | -8.96 | -5.32 | -13.12 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.78 | -9.22 | 77 | 16.9 | -16.17 | -2.65 | -27.42 | 218 |
| 34 | Daily: Bullish score | daily | 90.62 | -9.38 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.33 | 1.11 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.36 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.04 | -9.96 | 81 | 16.0 | -16.68 | -1.94 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.44 | -10.56 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.21 | -10.79 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.01 | -10.99 | 52 | 23.1 | -8.18 | -0.99 | -27.05 | 202 |
| 41 | Supertrend · 1h | trend | 88.88 | -11.12 | 85 | 11.8 | -22.69 | -4.67 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.95 | -12.05 | 145 | 40.0 | -24.24 | -7.37 | -25.57 | 226 |
| 43 | OBV trend · 1h | momentum | 87.62 | -12.38 | 170 | 18.2 | -17.21 | -2.03 | -33.85 | 317 |
| 44 | MACD cross · 1h | trend | 87.54 | -12.46 | 181 | 21.5 | -21.41 | -3.53 | -30.63 | 461 |
| 45 | Stochastic reversion · 1h | reversion | 86.66 | -13.34 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.91 | -14.10 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.46 | -14.54 | 82 | 15.9 | -21.19 | -3.96 | -24.00 | 217 |
| 49 | MFI reversion · 1h | reversion | 84.87 | -15.13 | 206 | 30.1 | -21.18 | -3.27 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.61 | -15.39 | 79 | 17.7 | 1.35 | 0.37 | -21.63 | 213 |
| 51 | Three white soldiers | momentum | 83.86 | -16.14 | 217 | 18.9 | -47.13 | -19.41 | -47.38 | 604 |
| 52 | Z-score reversion · 1h | reversion | 82.75 | -17.25 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.70 | -17.30 | 193 | 21.2 | -12.68 | -1.60 | -27.38 | 393 |
| 54 | Agent (ML meta-label) | meta | 82.17 | -17.83 | 655 | 18.0 | -10.85 | -1.60 | -20.56 | 371 |
| 55 | EMA 9/21 cross · 1h | trend | 80.96 | -19.04 | 131 | 11.5 | -11.09 | -1.31 | -30.34 | 312 |
| 56 | Heikin-Ashi · 1h | trend | 80.83 | -19.17 | 206 | 22.3 | -32.50 | -5.30 | -42.46 | 682 |
| 57 | Williams %R · 1h | reversion | 80.04 | -19.96 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 58 | RSI(14) reversion · 1h | reversion | 79.97 | -20.02 | 74 | 20.3 | -14.55 | -2.57 | -22.27 | 170 |
| 59 | VWAP momentum · 1h | momentum | 79.89 | -20.11 | 408 | 20.1 | -37.23 | -5.60 | -46.96 | 1252 |
| 60 | Bollinger reversion · 1h | reversion | 79.84 | -20.16 | 150 | 32.0 | -30.68 | -6.34 | -33.03 | 355 |
| 61 | CCI reversion · 1h | reversion | 78.99 | -21.01 | 161 | 38.5 | -20.38 | -2.65 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.07 | -23.93 | 205 | 25.4 | -35.84 | -6.46 | -36.73 | 546 |
| 63 | Volume breakout | breakout | 62.94 | -37.06 | 340 | 13.2 | -62.74 | -17.81 | -63.59 | 880 |
| 64 | ROC + volume | momentum | 62.54 | -37.46 | 565 | 21.9 | -75.71 | -17.48 | -77.85 | 1732 |
| 65 | Squeeze breakout | breakout | 61.75 | -38.25 | 444 | 14.4 | -62.77 | -17.68 | -64.76 | 1212 |
| 66 | Donchian 55/20 | breakout | 59.54 | -40.46 | 455 | 17.1 | -68.82 | -14.40 | -72.80 | 1284 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.74 | -16.60 | -74.83 | 1635 |
| 68 | EMA 20/50 cross | trend | 57.25 | -42.76 | 480 | 18.3 | -76.58 | -14.90 | -80.16 | 1439 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -73.19 | -15.44 | -73.71 | 1522 |
| 70 | Keltner breakout | breakout | 53.16 | -46.84 | 635 | 15.7 | -82.57 | -25.94 | -83.10 | 1817 |
| 71 | AI bee: Boozy | ai | 51.92 | -48.08 | 336 | 6.0 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -29.61 | -98.64 | 5333 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -29.73 | -93.50 | 2588 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.22 | -19.84 | -87.78 | 1912 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.12 | -23.93 | -90.90 | 2358 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.12 | -25.98 | -91.13 | 2296 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -31.78 | -97.48 | 3526 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.69 | -35.72 | -96.73 | 3613 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.11 | -26.33 | -94.47 | 2578 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.90 | -23.00 | -82.50 | 1724 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -36.34 | -99.40 | 5828 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.13 | -25.17 | -91.67 | 2638 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.08 | -31.40 | -96.08 | 3517 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.29 | -99.74 | 6234 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.57 | -28.64 | -91.70 | 2366 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -37.90 | -97.49 | 3656 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.14 | -98.50 | 4767 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.55 | -32.44 | -93.69 | 2806 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.76 | -99.54 | 6246 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.18 | -86.84 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.35 | -26.94 | -88.42 | 2178 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.08 | -95.89 | 3807 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.18 | -32.43 | -89.48 | 2114 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.84 | -33.33 | -95.84 | 4154 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.74 | -99.90 | 8328 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T00:45 | Parabolic SAR · 1h | buy | DOGE-USD | 4.65 | — | rebalance up |
| 2026-10-19T00:45 | Parabolic SAR · 1h | sell | SOL-USD | 4.65 | -0.00 | rebalance down |
| 2026-10-19T00:30 | ROC + volume | sell | XRP-USD | 12.51 | 0.04 | exit signal |
| 2026-10-19T00:30 | ROC + volume | sell | SOL-USD | 12.56 | 0.20 | exit signal |
| 2026-10-19T00:30 | ROC + volume | sell | ETH-USD | 12.34 | -0.08 | exit signal |
| 2026-10-19T00:30 | ROC + volume | sell | DOGE-USD | 12.55 | 0.21 | exit signal |
| 2026-10-19T00:24 | AI bee: Boozy | sell | ETH-USD | 14.86 | -0.12 | Jev: buy |
| 2026-10-19T00:20 | Keltner breakout | buy | BTC-USD | 5.26 | — | rebalance up |
| 2026-10-19T00:20 | Keltner breakout | sell | XRP-USD | 10.62 | 0.16 | stop-loss |
| 2026-10-19T00:20 | Keltner breakout | sell | SOL-USD | 10.56 | 0.11 | exit signal |
| 2026-10-19T00:15 | ROC + volume | buy | ETH-USD | 12.42 | — | entry signal |
| 2026-10-19T00:15 | ROC + volume | sell | XRP-USD | 3.16 | 0.01 | rebalance down |
| 2026-10-19T00:15 | ROC + volume | sell | BTC-USD | 3.13 | -0.00 | rebalance down |
| 2026-10-19T00:09 | AI bee: Boozy | buy | ETH-USD | 14.98 | — | Jev: buy (buy p=0.75) |
| 2026-10-19T00:05 | Volume breakout | sell | SOL-USD | 12.63 | 0.04 | time stop |
| 2026-10-19T00:05 | Volume breakout | sell | BTC-USD | 15.75 | -0.01 | time stop |
| 2026-10-19T00:00 | Stochastic reversion · 1h | sell | ETH-USD | 4.18 | 0.08 | exit signal |
| 2026-10-19T00:00 | Stochastic reversion · 1h | sell | BTC-USD | 5.12 | 0.03 | exit signal |
| 2026-10-19T00:00 | Z-score reversion · 1h | sell | DOGE-USD | 11.72 | -0.04 | exit signal |
| 2026-10-19T00:00 | Three white soldiers · 1h | buy | XRP-USD | 23.85 | — | entry signal |
| 2026-10-19T00:00 | Keltner breakout · 1h | buy | XRP-USD | 22.27 | — | entry signal |
| 2026-10-19T00:00 | Donchian 20/10 · 1h | buy | XRP-USD | 21.17 | — | entry signal |
| 2026-10-19T00:00 | RSI momentum · 1h | buy | XRP-USD | 22.72 | — | entry signal |
| 2026-10-19T00:00 | RSI momentum · 1h | buy | BTC-USD | 22.72 | — | entry signal |
| 2026-10-19T00:00 | Heikin-Ashi · 1h | buy | XRP-USD | 5.53 | — | entry signal |
| 2026-10-19T00:00 | Heikin-Ashi · 1h | buy | SOL-USD | 13.49 | — | entry signal |
| 2026-10-19T00:00 | Heikin-Ashi · 1h | buy | ETH-USD | 13.49 | — | entry signal |
| 2026-10-19T00:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 13.49 | — | entry signal |
| 2026-10-19T00:00 | Heikin-Ashi · 1h | buy | BTC-USD | 13.49 | — | entry signal |
| 2026-10-19T00:00 | Parabolic SAR · 1h | buy | DOGE-USD | 4.65 | — | entry signal |
| 2026-10-19T00:00 | Parabolic SAR · 1h | sell | BTC-USD | 4.65 | -0.01 | rebalance down |
| 2026-10-18T23:55 | Volume breakout | sell | DOGE-USD | 12.66 | 0.22 | time stop |
| 2026-10-18T23:48 | AI bee: Boozy | sell | ETH-USD | 14.98 | -0.08 | Jev: sell |
| 2026-10-18T23:33 | AI bee: Boozy | buy | ETH-USD | 15.06 | — | Jev: buy (buy p=0.72) |
| 2026-10-18T23:20 | ROC + volume | buy | XRP-USD | 3.13 | — | rebalance up |
| 2026-10-18T23:20 | ROC + volume | buy | BTC-USD | 3.15 | — | rebalance up |
| 2026-10-18T23:20 | ROC + volume | sell | ETH-USD | 12.42 | -0.08 | exit signal |
| 2026-10-18T23:10 | Three white soldiers | sell | XRP-USD | 21.19 | 0.30 | exit signal |
| 2026-10-18T23:10 | Volume breakout | buy | BTC-USD | 3.18 | — | rebalance up |
| 2026-10-18T23:10 | Volume breakout | sell | XRP-USD | 12.57 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 00:55:05.000134+00:00 -> 2026-10-19 01:05:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
