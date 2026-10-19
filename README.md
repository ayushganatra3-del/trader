# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T01:25:05.000144+00:00 · 27824 ticks

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

Today: 1005 decisions in 201 calls, $0.0141 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T01:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-19T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T01:25 | 3 / 2 / 0 | COIN 71% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.76 | 4.76 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.88 | -0.12 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.51 | -0.49 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.79 | -1.21 | 36 | 16.7 | -2.89 | -0.22 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.69 | -1.31 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.56 | -1.44 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.11 | -1.89 | 20 | 45.0 | -13.17 | -2.35 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 97.74 | -2.26 | 0 | — | 28.11 | 3.31 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.11 | -2.89 | 108 | 33.3 | -5.40 | -2.79 | -6.60 | 275 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.40 | -3.60 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.38 | -3.62 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.20 | -3.80 | 87 | 24.1 | -19.10 | -5.70 | -19.70 | 138 |
| 21 | Three white soldiers · 1h | momentum | 95.62 | -4.38 | 12 | 0.0 | 0.18 | 0.15 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.51 | -4.49 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 94.71 | -5.29 | 82 | 19.5 | 1.33 | 0.37 | -14.59 | 258 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.94 | 1.03 | -9.46 | 101 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.08 | -6.92 | 97 | 21.6 | -9.68 | -1.48 | -22.75 | 274 |
| 27 | Daily: Momentum burst | daily | 92.95 | -7.05 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.55 | -7.45 | 55 | 14.5 | -18.32 | -3.14 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.13 | -7.87 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.97 | -8.03 | 77 | 39.0 | -8.69 | -5.27 | -13.06 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.87 | -9.13 | 77 | 16.9 | -16.09 | -2.64 | -27.42 | 218 |
| 34 | Daily: Bullish score | daily | 90.62 | -9.38 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.34 | 1.11 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.36 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.04 | -9.96 | 81 | 16.0 | -16.66 | -1.94 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.44 | -10.56 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.21 | -10.79 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.04 | -10.96 | 52 | 23.1 | -8.14 | -0.99 | -27.05 | 203 |
| 41 | Supertrend · 1h | trend | 88.93 | -11.07 | 85 | 11.8 | -22.56 | -4.64 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.95 | -12.05 | 145 | 40.0 | -24.24 | -7.37 | -25.57 | 226 |
| 43 | OBV trend · 1h | momentum | 87.62 | -12.38 | 170 | 18.2 | -16.67 | -1.92 | -33.85 | 317 |
| 44 | MACD cross · 1h | trend | 87.61 | -12.39 | 181 | 21.5 | -21.33 | -3.52 | -30.63 | 461 |
| 45 | Stochastic reversion · 1h | reversion | 86.66 | -13.34 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.91 | -14.10 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.44 | -14.56 | 82 | 15.9 | -23.56 | -4.66 | -23.96 | 216 |
| 49 | MFI reversion · 1h | reversion | 85.04 | -14.96 | 206 | 30.1 | -21.01 | -3.23 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.63 | -15.37 | 79 | 17.7 | 1.38 | 0.37 | -21.63 | 214 |
| 51 | Three white soldiers | momentum | 83.86 | -16.14 | 217 | 18.9 | -46.87 | -18.71 | -47.34 | 600 |
| 52 | Z-score reversion · 1h | reversion | 82.75 | -17.25 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.70 | -17.30 | 193 | 21.2 | -12.70 | -1.61 | -27.31 | 392 |
| 54 | Agent (ML meta-label) | meta | 82.17 | -17.83 | 655 | 18.0 | -10.84 | -1.62 | -19.69 | 387 |
| 55 | Heikin-Ashi · 1h | trend | 80.99 | -19.01 | 206 | 22.3 | -32.35 | -5.27 | -42.46 | 682 |
| 56 | EMA 9/21 cross · 1h | trend | 80.96 | -19.04 | 131 | 11.5 | -18.87 | -3.11 | -29.36 | 314 |
| 57 | Williams %R · 1h | reversion | 80.04 | -19.96 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 58 | RSI(14) reversion · 1h | reversion | 79.97 | -20.03 | 74 | 20.3 | -14.56 | -2.58 | -22.27 | 169 |
| 59 | VWAP momentum · 1h | momentum | 79.96 | -20.04 | 409 | 20.0 | -37.16 | -5.59 | -46.96 | 1252 |
| 60 | Bollinger reversion · 1h | reversion | 79.84 | -20.16 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 61 | CCI reversion · 1h | reversion | 78.99 | -21.01 | 161 | 38.5 | -20.32 | -2.64 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.07 | -23.93 | 205 | 25.4 | -36.33 | -6.53 | -37.22 | 547 |
| 63 | Volume breakout | breakout | 62.90 | -37.10 | 340 | 13.2 | -62.77 | -17.83 | -63.59 | 881 |
| 64 | ROC + volume | momentum | 62.50 | -37.50 | 565 | 21.9 | -75.71 | -17.49 | -77.84 | 1732 |
| 65 | Squeeze breakout | breakout | 61.65 | -38.35 | 444 | 14.4 | -62.83 | -17.74 | -64.82 | 1214 |
| 66 | Donchian 55/20 | breakout | 59.70 | -40.30 | 455 | 17.1 | -68.74 | -14.34 | -72.80 | 1284 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.64 | -16.54 | -74.73 | 1634 |
| 68 | EMA 20/50 cross | trend | 57.40 | -42.60 | 480 | 18.3 | -76.46 | -14.85 | -80.16 | 1438 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -73.09 | -15.40 | -73.61 | 1520 |
| 70 | Keltner breakout | breakout | 53.21 | -46.79 | 635 | 15.7 | -82.54 | -25.90 | -83.10 | 1818 |
| 71 | AI bee: Boozy | ai | 51.85 | -48.15 | 337 | 5.9 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -29.57 | -98.63 | 5329 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.37 | -29.63 | -93.50 | 2588 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.19 | -19.78 | -87.78 | 1912 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.07 | -23.84 | -90.90 | 2357 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.08 | -25.89 | -91.11 | 2295 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -31.68 | -97.48 | 3526 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -35.61 | -96.72 | 3609 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -26.77 | -94.59 | 2589 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.90 | -23.00 | -82.50 | 1724 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -36.35 | -99.40 | 5823 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.12 | -25.14 | -91.67 | 2639 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.07 | -31.35 | -96.07 | 3515 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.38 | -99.74 | 6236 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.58 | -28.64 | -91.71 | 2366 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -37.78 | -97.49 | 3656 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.16 | -98.49 | 4764 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -32.42 | -93.69 | 2808 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.76 | -99.54 | 6245 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.18 | -86.84 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.28 | -27.02 | -88.35 | 2179 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.09 | -95.89 | 3807 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.04 | -32.02 | -89.38 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -33.35 | -95.81 | 4150 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.00 | -99.90 | 8334 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-19T00:00 | Keltner breakout · 1h | buy | XRP-USD | 22.27 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 01:25:05.000144+00:00 -> 2026-10-19 01:35:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
