# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T23:25:05.000182+00:00 · 27733 ticks

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

Today: 17718 decisions in 3546 calls, $0.2478 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T23:25 | 2 / 3 / 0 | XRP-USD 15% |  |
| Breezy | 2026-10-18T23:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T23:25 | 4 / 1 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 2.34 | +2.45% | 9 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| VWAP reversion | ETHU | 1.80 | +2.34% | 5 |
| VWAP momentum · 1h | SQQQ | 1.77 | +10.81% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.55 | -0.45 | 64 | 39.1 | -11.34 | -3.28 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.92 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | -2.87 | -0.22 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.37 | -20.62 | 67 |
| 16 | Hold BTC | benchmark | 97.13 | -2.87 | 0 | — | 26.63 | 3.19 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -5.37 | -2.79 | -6.62 | 279 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -19.10 | -5.75 | -19.70 | 138 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.27 | -4.73 | 12 | 0.0 | -0.21 | -0.07 | -5.45 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.47 | -5.53 | 82 | 19.5 | -2.81 | -0.32 | -14.60 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 4.14 | 0.92 | -9.46 | 98 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.73 | -7.27 | 97 | 21.6 | -10.04 | -1.56 | -22.75 | 273 |
| 28 | EMA 20/50 cross · 1h | trend | 92.56 | -7.44 | 55 | 14.5 | -18.32 | -3.16 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.79 | -2.00 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.30 | -5.88 | -11.10 | 231 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.89 | -9.11 | 77 | 16.9 | -17.00 | -2.97 | -27.38 | 216 |
| 34 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.34 | 1.12 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.38 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.05 | -9.95 | 81 | 16.0 | -16.04 | -1.84 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.97 | -0.96 | -27.05 | 201 |
| 41 | Supertrend · 1h | trend | 88.83 | -11.17 | 85 | 11.8 | -22.81 | -4.74 | -26.38 | 212 |
| 42 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -24.24 | -7.43 | -25.57 | 226 |
| 43 | OBV trend · 1h | momentum | 87.64 | -12.36 | 170 | 18.2 | -16.92 | -1.99 | -33.85 | 317 |
| 44 | MACD cross · 1h | trend | 87.50 | -12.50 | 181 | 21.5 | -19.60 | -3.02 | -30.63 | 460 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.32 | 148 | 44.6 | -21.01 | -3.85 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.46 | -14.54 | 82 | 15.9 | -21.07 | -3.96 | -23.90 | 217 |
| 49 | Donchian 20/10 · 1h | breakout | 84.68 | -15.32 | 79 | 17.7 | 1.42 | 0.38 | -21.63 | 212 |
| 50 | MFI reversion · 1h | reversion | 84.66 | -15.34 | 206 | 30.1 | -21.40 | -3.33 | -23.01 | 148 |
| 51 | Three white soldiers | momentum | 83.86 | -16.14 | 217 | 18.9 | -46.87 | -18.97 | -47.34 | 600 |
| 52 | Z-score reversion · 1h | reversion | 82.79 | -17.21 | 90 | 31.1 | -16.60 | -2.92 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.71 | -17.29 | 193 | 21.2 | -12.97 | -1.67 | -27.31 | 393 |
| 54 | Agent (ML meta-label) | meta | 82.20 | -17.80 | 655 | 18.0 | -11.49 | -1.69 | -19.00 | 376 |
| 55 | EMA 9/21 cross · 1h | trend | 80.97 | -19.03 | 131 | 11.5 | -11.22 | -1.35 | -30.34 | 312 |
| 56 | Heikin-Ashi · 1h | trend | 80.95 | -19.05 | 206 | 22.3 | -32.42 | -5.33 | -42.19 | 678 |
| 57 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.32 | -5.81 | -36.90 | 533 |
| 58 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.91 | -2.67 | -22.27 | 170 |
| 59 | Bollinger reversion · 1h | reversion | 79.87 | -20.13 | 150 | 32.0 | -30.68 | -6.39 | -33.04 | 355 |
| 60 | VWAP momentum · 1h | momentum | 79.67 | -20.33 | 408 | 20.1 | -37.44 | -5.68 | -46.96 | 1252 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.53 | -2.69 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.39 | -6.59 | -37.22 | 546 |
| 63 | Volume breakout | breakout | 63.00 | -37.00 | 337 | 12.8 | -62.70 | -18.00 | -63.59 | 880 |
| 64 | ROC + volume | momentum | 62.64 | -37.36 | 561 | 21.6 | -75.66 | -17.67 | -77.84 | 1730 |
| 65 | Squeeze breakout | breakout | 61.75 | -38.25 | 444 | 14.4 | -62.77 | -17.92 | -64.76 | 1212 |
| 66 | Donchian 55/20 | breakout | 59.32 | -40.68 | 455 | 17.1 | -68.95 | -14.63 | -72.80 | 1284 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.64 | -16.75 | -74.73 | 1634 |
| 68 | EMA 20/50 cross | trend | 57.04 | -42.96 | 480 | 18.3 | -76.72 | -15.14 | -80.16 | 1440 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -73.46 | -15.67 | -73.97 | 1528 |
| 70 | Keltner breakout | breakout | 53.11 | -46.89 | 633 | 15.5 | -82.58 | -26.52 | -83.10 | 1817 |
| 71 | AI bee: Boozy | ai | 52.11 | -47.89 | 334 | 6.0 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -29.96 | -98.62 | 5315 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -30.59 | -93.50 | 2588 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.28 | -20.23 | -87.78 | 1912 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.15 | -24.48 | -90.90 | 2358 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.15 | -26.58 | -91.15 | 2296 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.42 | -32.76 | -97.48 | 3526 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -36.91 | -96.73 | 3610 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -26.60 | -94.44 | 2572 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.83 | -23.39 | -82.50 | 1722 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -37.60 | -99.40 | 5829 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.12 | -25.64 | -91.67 | 2637 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -32.37 | -96.11 | 3522 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.83 | -99.74 | 6236 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.57 | -29.30 | -91.71 | 2366 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -39.17 | -97.47 | 3651 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -37.32 | -98.52 | 4771 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -33.28 | -93.69 | 2805 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.24 | -99.54 | 6250 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.55 | -86.84 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.30 | -27.60 | -88.37 | 2180 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -33.00 | -95.94 | 3813 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -33.34 | -89.33 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.90 | -34.14 | -95.91 | 4161 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.71 | -99.90 | 8320 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T23:20 | ROC + volume | buy | XRP-USD | 3.13 | — | rebalance up |
| 2026-10-18T23:20 | ROC + volume | buy | BTC-USD | 3.15 | — | rebalance up |
| 2026-10-18T23:20 | ROC + volume | sell | ETH-USD | 12.42 | -0.08 | exit signal |
| 2026-10-18T23:10 | Three white soldiers | sell | XRP-USD | 21.19 | 0.30 | exit signal |
| 2026-10-18T23:10 | Volume breakout | buy | BTC-USD | 3.18 | — | rebalance up |
| 2026-10-18T23:10 | Volume breakout | sell | XRP-USD | 12.57 | -0.02 | exit signal |
| 2026-10-18T23:10 | Volume breakout | sell | ETH-USD | 12.51 | -0.08 | exit signal |
| 2026-10-18T23:05 | Keltner breakout | buy | BTC-USD | 2.66 | — | rebalance up |
| 2026-10-18T23:05 | Keltner breakout | sell | SOL-USD | 2.66 | 0.03 | rebalance down |
| 2026-10-18T23:00 | Stochastic reversion · 1h | sell | XRP-USD | 4.40 | 0.07 | exit signal |
| 2026-10-18T23:00 | Stochastic reversion · 1h | sell | SOL-USD | 4.37 | 0.05 | exit signal |
| 2026-10-18T23:00 | Stochastic reversion · 1h | sell | DOGE-USD | 4.21 | 0.11 | exit signal |
| 2026-10-18T23:00 | VWAP reversion · 1h | sell | SOL-USD | 8.47 | 0.15 | exit signal |
| 2026-10-18T23:00 | VWAP reversion · 1h | sell | DOGE-USD | 1.45 | 0.04 | exit signal |
| 2026-10-18T23:00 | Z-score reversion · 1h | buy | DOGE-USD | 11.75 | — | entry |
| 2026-10-18T23:00 | Z-score reversion · 1h | sell | BTC-USD | 11.75 | 0.03 | exit signal |
| 2026-10-18T23:00 | Bollinger reversion · 1h | sell | SOL-USD | 1.44 | 0.03 | exit signal |
| 2026-10-18T23:00 | Bollinger reversion · 1h | sell | BTC-USD | 7.27 | 0.01 | exit signal |
| 2026-10-18T23:00 | Three white soldiers · 1h | buy | SOL-USD | 23.84 | — | entry signal |
| 2026-10-18T23:00 | Three white soldiers · 1h | buy | ETH-USD | 23.84 | — | entry signal |
| 2026-10-18T23:00 | VWAP momentum · 1h | buy | XRP-USD | 5.08 | — | entry signal |
| 2026-10-18T23:00 | VWAP momentum · 1h | buy | SOL-USD | 13.30 | — | entry signal |
| 2026-10-18T23:00 | VWAP momentum · 1h | buy | ETH-USD | 13.30 | — | entry signal |
| 2026-10-18T23:00 | VWAP momentum · 1h | buy | DOGE-USD | 13.30 | — | entry signal |
| 2026-10-18T23:00 | VWAP momentum · 1h | buy | BTC-USD | 13.30 | — | entry signal |
| 2026-10-18T23:00 | ADX DI cross · 1h | buy | XRP-USD | 13.09 | — | entry signal |
| 2026-10-18T23:00 | ADX DI cross · 1h | buy | SOL-USD | 18.92 | — | entry signal |
| 2026-10-18T23:00 | ADX DI cross · 1h | buy | BTC-USD | 18.92 | — | entry signal |
| 2026-10-18T23:00 | Parabolic SAR · 1h | buy | XRP-USD | 22.52 | — | entry signal |
| 2026-10-18T23:00 | Parabolic SAR · 1h | buy | SOL-USD | 23.22 | — | entry signal |
| 2026-10-18T23:00 | Parabolic SAR · 1h | buy | BTC-USD | 23.22 | — | entry signal |
| 2026-10-18T23:00 | Supertrend · 1h | buy | DOGE-USD | 9.14 | — | entry signal |
| 2026-10-18T23:00 | Supertrend · 1h | buy | BTC-USD | 12.70 | — | entry signal |
| 2026-10-18T23:00 | MACD cross · 1h | buy | SOL-USD | 10.18 | — | entry signal |
| 2026-10-18T23:00 | MACD cross · 1h | buy | DOGE-USD | 14.59 | — | entry signal |
| 2026-10-18T22:05 | VWAP reversion | sell | XRP-USD | 10.73 | 0.16 | exit signal |
| 2026-10-18T22:05 | VWAP reversion | sell | SOL-USD | 8.03 | 0.12 | exit signal |
| 2026-10-18T22:05 | VWAP reversion | sell | ETH-USD | 10.70 | 0.14 | exit signal |
| 2026-10-18T22:05 | VWAP reversion | sell | DOGE-USD | 10.82 | 0.26 | exit signal |
| 2026-10-18T22:05 | VWAP reversion | sell | BTC-USD | 13.21 | 0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 23:25:05.000182+00:00 -> 2026-10-18 23:35:05.000182+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
