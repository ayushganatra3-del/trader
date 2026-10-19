# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T01:56:05.000136+00:00 · 27852 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

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

Today: 1425 decisions in 285 calls, $0.0199 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T01:56 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-19T01:56 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T01:56 | 3 / 2 / 0 | ETH-USD 28% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | BITX | 2.21 | +2.15% | 7 |
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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.82 | 4.82 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.55 | -0.45 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.82 | -1.18 | 36 | 16.7 | -2.88 | -0.22 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.74 | -1.26 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.35 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 97.82 | -2.18 | 0 | — | 28.27 | 3.33 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -5.40 | -2.79 | -6.60 | 275 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -19.10 | -5.70 | -19.70 | 138 |
| 21 | Three white soldiers · 1h | momentum | 95.76 | -4.24 | 12 | 0.0 | 0.30 | 0.21 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.56 | -4.44 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.82 | -5.18 | 82 | 19.5 | 1.42 | 0.38 | -14.59 | 258 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 3.43 | 0.80 | -9.46 | 97 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.21 | -6.79 | 97 | 21.6 | -9.59 | -1.47 | -22.75 | 274 |
| 27 | Daily: Momentum burst | daily | 93.00 | -7.00 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.56 | -7.44 | 55 | 14.5 | -18.32 | -3.14 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.69 | -5.27 | -13.06 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.94 | -9.06 | 77 | 16.9 | -16.06 | -2.63 | -27.42 | 218 |
| 34 | Daily: Bullish score | daily | 90.66 | -9.34 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.33 | 1.11 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.36 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.05 | -9.95 | 81 | 16.0 | -16.66 | -1.94 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.53 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.10 | -10.90 | 52 | 23.1 | -8.12 | -0.98 | -27.05 | 203 |
| 41 | Supertrend · 1h | trend | 88.99 | -11.01 | 85 | 11.8 | -22.50 | -4.62 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.99 | -12.02 | 145 | 40.0 | -24.24 | -7.37 | -25.57 | 226 |
| 43 | MACD cross · 1h | trend | 87.70 | -12.30 | 181 | 21.5 | -21.27 | -3.50 | -30.63 | 461 |
| 44 | OBV trend · 1h | momentum | 87.64 | -12.36 | 170 | 18.2 | -16.67 | -1.92 | -33.85 | 317 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.32 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.45 | -14.55 | 82 | 15.9 | -23.55 | -4.66 | -23.96 | 216 |
| 49 | MFI reversion · 1h | reversion | 85.16 | -14.84 | 206 | 30.1 | -20.93 | -3.22 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.69 | -15.31 | 79 | 17.7 | 1.42 | 0.38 | -21.63 | 214 |
| 51 | Three white soldiers | momentum | 83.86 | -16.14 | 217 | 18.9 | -46.87 | -18.71 | -47.34 | 600 |
| 52 | Z-score reversion · 1h | reversion | 82.79 | -17.21 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.71 | -17.29 | 193 | 21.2 | -12.60 | -1.59 | -27.31 | 392 |
| 54 | Agent (ML meta-label) | meta | 82.21 | -17.80 | 655 | 18.0 | -15.01 | -2.58 | -16.50 | 374 |
| 55 | Heikin-Ashi · 1h | trend | 81.11 | -18.89 | 206 | 22.3 | -32.28 | -5.25 | -42.46 | 682 |
| 56 | EMA 9/21 cross · 1h | trend | 81.07 | -18.93 | 131 | 11.5 | -18.80 | -3.10 | -29.36 | 314 |
| 57 | Williams %R · 1h | reversion | 80.09 | -19.91 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 58 | VWAP momentum · 1h | momentum | 80.06 | -19.93 | 409 | 20.0 | -37.10 | -5.57 | -46.96 | 1252 |
| 59 | RSI(14) reversion · 1h | reversion | 80.02 | -19.98 | 74 | 20.3 | -14.79 | -2.62 | -22.27 | 169 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.26 | -2.63 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.34 | -6.53 | -37.22 | 547 |
| 63 | Volume breakout | breakout | 62.92 | -37.08 | 340 | 13.2 | -62.75 | -17.82 | -63.59 | 881 |
| 64 | ROC + volume | momentum | 62.55 | -37.45 | 565 | 21.9 | -75.70 | -17.47 | -77.84 | 1732 |
| 65 | Squeeze breakout | breakout | 61.71 | -38.29 | 444 | 14.4 | -62.87 | -17.72 | -64.82 | 1215 |
| 66 | Donchian 55/20 | breakout | 59.80 | -40.20 | 455 | 17.1 | -68.70 | -14.32 | -72.80 | 1284 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.53 | -16.47 | -74.62 | 1631 |
| 68 | EMA 20/50 cross | trend | 57.50 | -42.50 | 480 | 18.3 | -76.33 | -14.80 | -80.16 | 1436 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.88 | -15.31 | -73.40 | 1516 |
| 70 | Keltner breakout | breakout | 53.30 | -46.70 | 635 | 15.7 | -82.46 | -25.83 | -83.10 | 1816 |
| 71 | AI bee: Boozy | ai | 51.82 | -48.18 | 337 | 5.9 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -29.52 | -98.62 | 5327 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -29.56 | -93.50 | 2589 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.14 | -19.74 | -87.78 | 1910 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.06 | -23.81 | -90.90 | 2357 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.07 | -25.84 | -91.10 | 2294 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -31.64 | -97.48 | 3527 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -35.53 | -96.72 | 3611 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -26.77 | -94.59 | 2589 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.90 | -23.00 | -82.50 | 1724 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.31 | -99.39 | 5816 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.11 | -25.10 | -91.67 | 2639 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.05 | -31.27 | -96.05 | 3512 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.47 | -99.74 | 6237 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.54 | -28.65 | -91.68 | 2364 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.49 | -37.86 | -97.50 | 3658 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.15 | -98.49 | 4760 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.53 | -32.36 | -93.69 | 2808 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.71 | -99.53 | 6239 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.18 | -86.84 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.19 | -27.03 | -88.26 | 2174 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.08 | -95.89 | 3807 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.03 | -31.92 | -89.38 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -33.35 | -95.80 | 4149 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.06 | -99.90 | 8334 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T01:42 | AI bee: Boozy | buy | ETH-USD | 14.80 | — | Jev: buy (buy p=0.72) |
| 2026-10-19T01:23 | AI bee: Boozy | sell | ETH-USD | 14.80 | -0.06 | Jev: add (buy p=0.59) |
| 2026-10-19T01:20 | Squeeze breakout | buy | DOGE-USD | 15.43 | — | entry signal |
| 2026-10-19T01:15 | ROC + volume | buy | SOL-USD | 15.64 | — | entry signal |
| 2026-10-19T01:10 | Volume breakout | buy | DOGE-USD | 15.74 | — | entry signal |
| 2026-10-19T01:10 | Squeeze breakout | buy | SOL-USD | 15.44 | — | entry signal |
| 2026-10-19T01:10 | Keltner breakout | buy | SOL-USD | 13.31 | — | entry signal |
| 2026-10-19T01:08 | AI bee: Boozy | buy | ETH-USD | 14.86 | — | Jev: buy (buy p=0.71) |
| 2026-10-19T01:00 | Keltner breakout · 1h | buy | BTC-USD | 22.25 | — | entry signal |
| 2026-10-19T01:00 | Donchian 55/20 · 1h | buy | BTC-USD | 24.70 | — | entry signal |
| 2026-10-19T01:00 | Donchian 20/10 · 1h | buy | BTC-USD | 21.15 | — | entry signal |
| 2026-10-19T01:00 | VWAP momentum · 1h | buy | XRP-USD | 10.89 | — | rebalance up |
| 2026-10-19T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 13.24 | -0.05 | exit signal |
| 2026-10-19T01:00 | ADX DI cross · 1h | buy | DOGE-USD | 10.83 | — | entry |
| 2026-10-19T01:00 | ADX DI cross · 1h | sell | SOL-USD | 5.39 | -0.01 | rebalance down |
| 2026-10-19T01:00 | ADX DI cross · 1h | sell | BTC-USD | 5.44 | -0.00 | rebalance down |
| 2026-10-19T01:00 | MACD zero-line · 1h | buy | BTC-USD | 21.36 | — | entry signal |
| 2026-10-19T01:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 19.86 | — | entry signal |
| 2026-10-19T01:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 20.24 | — | entry signal |
| 2026-10-19T01:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 20.24 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 01:56:05.000136+00:00 -> 2026-10-19 02:06:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
