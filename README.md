# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T02:56:05.000138+00:00 · 27904 ticks

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

Today: 2205 decisions in 441 calls, $0.0308 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T02:56 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-19T02:56 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T02:56 | 2 / 2 / 1 | ETH-USD 28% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.55 | -0.45 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.89 | -1.11 | 36 | 16.7 | -4.83 | -0.52 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.26 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.35 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 98.09 | -1.91 | 0 | — | 28.47 | 3.35 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -5.40 | -2.79 | -6.60 | 275 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.79 | 87 | 24.1 | -19.10 | -5.70 | -19.70 | 138 |
| 21 | Three white soldiers · 1h | momentum | 95.98 | -4.02 | 12 | 0.0 | 0.53 | 0.33 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 95.01 | -4.99 | 82 | 19.5 | -7.90 | -1.38 | -13.37 | 257 |
| 24 | Parabolic SAR · 1h | trend | 93.46 | -6.54 | 97 | 21.6 | -9.32 | -1.42 | -22.75 | 274 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 3.43 | 0.80 | -9.46 | 97 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.56 | -7.44 | 55 | 14.5 | -18.32 | -3.13 | -21.23 | 127 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.69 | -5.27 | -13.06 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.03 | -8.97 | 77 | 16.9 | -16.86 | -2.91 | -27.42 | 219 |
| 34 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.33 | 1.11 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.36 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.05 | -9.95 | 81 | 16.0 | -18.46 | -2.28 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.54 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.20 | -10.80 | 52 | 23.1 | -8.02 | -0.97 | -27.05 | 203 |
| 41 | Supertrend · 1h | trend | 89.06 | -10.94 | 85 | 11.8 | -22.34 | -4.58 | -26.38 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -24.24 | -7.37 | -25.57 | 226 |
| 43 | MACD cross · 1h | trend | 87.83 | -12.17 | 181 | 21.5 | -22.37 | -3.80 | -30.63 | 460 |
| 44 | OBV trend · 1h | momentum | 87.65 | -12.35 | 170 | 18.2 | -16.33 | -1.86 | -33.85 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.32 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.56 | -14.44 | 82 | 15.9 | -23.45 | -4.64 | -24.11 | 218 |
| 49 | MFI reversion · 1h | reversion | 85.32 | -14.68 | 206 | 30.1 | -20.79 | -3.19 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.84 | -15.16 | 79 | 17.7 | 1.58 | 0.39 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 83.80 | -16.20 | 217 | 18.9 | -46.91 | -18.75 | -47.34 | 602 |
| 52 | Z-score reversion · 1h | reversion | 82.78 | -17.21 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.68 | -17.32 | 193 | 21.2 | -12.67 | -1.60 | -27.41 | 393 |
| 54 | Agent (ML meta-label) | meta | 82.20 | -17.80 | 655 | 18.0 | -20.12 | -3.70 | -21.58 | 371 |
| 55 | Heikin-Ashi · 1h | trend | 81.32 | -18.68 | 206 | 22.3 | -32.09 | -5.21 | -42.46 | 682 |
| 56 | EMA 9/21 cross · 1h | trend | 81.17 | -18.83 | 131 | 11.5 | -18.88 | -3.12 | -29.40 | 317 |
| 57 | VWAP momentum · 1h | momentum | 80.23 | -19.77 | 409 | 20.0 | -36.87 | -5.50 | -46.96 | 1252 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 59 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.58 | -2.58 | -22.27 | 167 |
| 60 | Bollinger reversion · 1h | reversion | 79.87 | -20.13 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.24 | -2.62 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.34 | -6.53 | -37.22 | 543 |
| 63 | Volume breakout | breakout | 62.86 | -37.14 | 341 | 13.2 | -62.79 | -17.84 | -63.59 | 881 |
| 64 | ROC + volume | momentum | 62.60 | -37.40 | 566 | 22.1 | -75.68 | -17.46 | -77.84 | 1732 |
| 65 | Squeeze breakout | breakout | 61.44 | -38.56 | 446 | 14.3 | -62.96 | -17.84 | -64.95 | 1216 |
| 66 | Donchian 55/20 | breakout | 60.00 | -40.00 | 455 | 17.1 | -68.33 | -14.15 | -72.80 | 1280 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.49 | -16.45 | -74.57 | 1630 |
| 68 | EMA 20/50 cross | trend | 57.69 | -42.31 | 480 | 18.3 | -76.01 | -14.67 | -80.16 | 1433 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.81 | -15.28 | -73.33 | 1513 |
| 70 | Keltner breakout | breakout | 52.81 | -47.20 | 639 | 16.1 | -82.66 | -26.22 | -83.10 | 1821 |
| 71 | AI bee: Boozy | ai | 51.53 | -48.47 | 339 | 5.9 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -29.49 | -98.61 | 5323 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.35 | -29.43 | -93.50 | 2589 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.06 | -19.69 | -87.78 | 1908 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.99 | -23.68 | -90.90 | 2355 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.98 | -25.61 | -91.02 | 2293 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -31.49 | -97.45 | 3521 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.67 | -35.35 | -96.73 | 3612 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.35 | -26.62 | -94.68 | 2587 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.80 | -22.97 | -82.50 | 1721 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.32 | -99.39 | 5817 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.18 | -25.30 | -91.67 | 2644 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.05 | -31.33 | -96.05 | 3513 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.66 | -99.74 | 6241 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.50 | -28.65 | -91.64 | 2361 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -38.32 | -97.50 | 3660 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.19 | -98.48 | 4759 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.59 | -32.79 | -93.68 | 2811 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.72 | -99.53 | 6239 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.18 | -86.84 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.19 | -27.03 | -88.26 | 2174 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.09 | -95.89 | 3807 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.89 | -31.69 | -89.29 | 2108 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -33.37 | -95.79 | 4148 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.48 | -99.90 | 8338 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T02:50 | AI bee: Boozy | buy | ETH-USD | 14.57 | — | Jev: buy (buy p=0.74) |
| 2026-10-19T02:50 | Squeeze breakout | buy | XRP-USD | 15.39 | — | entry signal |
| 2026-10-19T02:50 | Squeeze breakout | buy | BTC-USD | 15.39 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | SOL-USD | 13.27 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | ETH-USD | 13.27 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | DOGE-USD | 13.27 | — | entry signal |
| 2026-10-19T02:50 | Keltner breakout | buy | BTC-USD | 13.27 | — | entry signal |
| 2026-10-19T02:45 | Three white soldiers | buy | ETH-USD | 20.97 | — | entry signal |
| 2026-10-19T02:45 | Three white soldiers | buy | BTC-USD | 20.97 | — | entry signal |
| 2026-10-19T02:30 | Squeeze breakout | sell | SOL-USD | 15.37 | -0.06 | stop-loss |
| 2026-10-19T02:30 | Keltner breakout | sell | SOL-USD | 13.26 | -0.05 | stop-loss |
| 2026-10-19T02:25 | Squeeze breakout | sell | DOGE-USD | 15.32 | -0.11 | stop-loss |
| 2026-10-19T02:25 | Keltner breakout | sell | ETH-USD | 13.27 | 0.19 | stop-loss |
| 2026-10-19T02:25 | Keltner breakout | sell | DOGE-USD | 10.65 | 0.22 | stop-loss |
| 2026-10-19T02:25 | Keltner breakout | sell | BTC-USD | 13.28 | 0.02 | exit signal |
| 2026-10-19T02:24 | AI bee: Boozy | sell | SOL-USD | 14.57 | -0.13 | Jev: sell (sell p=0.52) after 15 min |
| 2026-10-19T02:20 | Volume breakout | sell | DOGE-USD | 15.65 | -0.08 | exit signal |
| 2026-10-19T02:20 | ROC + volume | sell | BTC-USD | 12.56 | 0.05 | exit signal |
| 2026-10-19T02:09 | AI bee: Boozy | buy | SOL-USD | 14.70 | — | Jev: buy (buy p=0.73) |
| 2026-10-19T02:02 | RSI momentum · 1h | buy | SOL-USD | 4.54 | — | rebalance up |
| 2026-10-19T02:02 | RSI momentum · 1h | sell | XRP-USD | 4.54 | -0.01 | rebalance down |
| 2026-10-19T02:00 | Donchian 20/10 · 1h | buy | SOL-USD | 12.07 | — | entry signal |
| 2026-10-19T02:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 16.94 | — | entry signal |
| 2026-10-19T02:00 | Donchian 20/10 · 1h | sell | XRP-USD | 4.23 | -0.01 | rebalance down |
| 2026-10-19T02:00 | OBV trend · 1h | buy | BTC-USD | 21.91 | — | entry signal |
| 2026-10-19T02:00 | RSI momentum · 1h | buy | SOL-USD | 7.53 | — | entry signal |
| 2026-10-19T02:00 | RSI momentum · 1h | sell | BTC-USD | 4.55 | -0.01 | rebalance down |
| 2026-10-19T02:00 | ROC + volume · 1h | buy | ETH-USD | 20.68 | — | entry signal |
| 2026-10-19T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 2.36 | — | entry signal |
| 2026-10-19T02:00 | MACD zero-line · 1h | buy | XRP-USD | 21.36 | — | entry signal |
| 2026-10-19T02:00 | MACD zero-line · 1h | buy | SOL-USD | 21.36 | — | entry signal |
| 2026-10-19T02:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 23.14 | — | entry signal |
| 2026-10-19T02:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 6.33 | — | entry signal |
| 2026-10-19T02:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 13.51 | — | entry signal |
| 2026-10-19T02:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 6.36 | -0.01 | rebalance down |
| 2026-10-19T02:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 6.78 | 0.00 | rebalance down |
| 2026-10-19T02:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 6.70 | -0.02 | rebalance down |
| 2026-10-19T01:59 | AI bee: Boozy | sell | ETH-USD | 14.70 | -0.10 | Jev: sell |
| 2026-10-19T01:42 | AI bee: Boozy | buy | ETH-USD | 14.80 | — | Jev: buy (buy p=0.72) |
| 2026-10-19T01:23 | AI bee: Boozy | sell | ETH-USD | 14.80 | -0.06 | Jev: add (buy p=0.59) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 02:56:05.000138+00:00 -> 2026-10-19 03:06:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
