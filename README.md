# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T03:55:05.000138+00:00 · 26749 ticks

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
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 2970 decisions in 594 calls, $0.0415 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T03:55 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-18T03:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T03:55 | 2 / 3 / 0 | COIN 70% |  |

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
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.29 | -3.28 | -13.79 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Hold BTC | benchmark | 97.20 | -2.80 | 0 | — | 28.57 | 3.38 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -7.60 | -3.74 | -9.02 | 278 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -20.22 | -6.11 | -20.39 | 142 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.65 | -1.54 | -13.33 | 254 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.69 | 0.86 | -9.46 | 100 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.37 | 2.38 | -6.56 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.84 | -0.33 | -22.92 | 127 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -0.53 | 0.11 | -22.55 | 273 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.41 | -1.86 | -8.25 | 117 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.61 | -5.71 | -13.53 | 236 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.57 | -0.07 | -14.55 | 114 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.44 | 0.38 | -26.55 | 216 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.86 | 1.07 | -14.21 | 267 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.21 | -0.54 | -33.23 | 228 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -13.47 | -2.14 | -28.00 | 209 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.18 | -0.99 | -27.05 | 203 |
| 42 | MACD cross · 1h | trend | 88.21 | -11.79 | 177 | 22.0 | -15.61 | -2.04 | -29.51 | 462 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.24 | -7.73 | -25.57 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.76 | -0.60 | -33.87 | 316 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.57 | -13.43 | 142 | 43.7 | -20.93 | -3.83 | -22.11 | 368 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.78 | -4.50 | -23.64 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 2.18 | 0.47 | -21.63 | 212 |
| 50 | MFI reversion · 1h | reversion | 84.08 | -15.92 | 204 | 30.4 | -21.62 | -3.58 | -22.26 | 142 |
| 51 | Three white soldiers | momentum | 83.80 | -16.20 | 214 | 18.7 | -47.63 | -20.17 | -47.71 | 608 |
| 52 | Z-score reversion · 1h | reversion | 83.39 | -16.61 | 86 | 31.4 | -15.57 | -2.71 | -20.30 | 185 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.53 | -1.64 | -27.12 | 395 |
| 54 | Agent (ML meta-label) | meta | 82.43 | -17.57 | 649 | 18.2 | -11.65 | -1.71 | -18.67 | 387 |
| 55 | VWAP momentum · 1h | momentum | 81.91 | -18.09 | 398 | 20.6 | -37.38 | -5.70 | -45.40 | 1259 |
| 56 | Heikin-Ashi · 1h | trend | 81.75 | -18.25 | 201 | 22.9 | -31.92 | -5.22 | -41.90 | 679 |
| 57 | EMA 9/21 cross · 1h | trend | 81.64 | -18.36 | 129 | 11.6 | -6.55 | -0.56 | -30.11 | 315 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.81 | -36.60 | 531 |
| 59 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.44 | -2.57 | -21.70 | 162 |
| 60 | Bollinger reversion · 1h | reversion | 79.91 | -20.09 | 144 | 30.6 | -30.69 | -6.39 | -32.71 | 350 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.97 | -2.60 | -26.49 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.83 | -6.51 | -36.31 | 538 |
| 63 | Volume breakout | breakout | 63.08 | -36.92 | 331 | 13.0 | -63.50 | -18.40 | -63.50 | 884 |
| 64 | ROC + volume | momentum | 62.56 | -37.45 | 555 | 21.8 | -75.79 | -17.77 | -77.61 | 1724 |
| 65 | Squeeze breakout | breakout | 61.98 | -38.02 | 440 | 14.5 | -63.10 | -18.14 | -64.68 | 1217 |
| 66 | RSI(14) reversion | reversion | 60.91 | -39.09 | 667 | 25.5 | -74.25 | -16.58 | -74.36 | 1630 |
| 67 | Donchian 55/20 | breakout | 60.17 | -39.83 | 445 | 17.5 | -68.99 | -14.62 | -72.15 | 1283 |
| 68 | EMA 20/50 cross | trend | 58.02 | -41.98 | 470 | 18.7 | -77.12 | -15.23 | -79.76 | 1449 |
| 69 | VWAP reversion | reversion | 54.51 | -45.49 | 701 | 23.8 | -73.35 | -15.64 | -73.53 | 1519 |
| 70 | Keltner breakout | breakout | 53.05 | -46.95 | 623 | 15.7 | -83.38 | -27.29 | -83.38 | 1834 |
| 71 | AI bee: Boozy | ai | 52.66 | -47.34 | 328 | 6.1 | — | — | — | — |
| 72 | Ichimoku | trend | 50.64 | -49.36 | 568 | 11.4 | -81.99 | -23.38 | -82.25 | 1734 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.11 | -98.65 | 5334 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -30.69 | -93.59 | 2601 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.50 | -20.35 | -87.54 | 1916 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.43 | -24.85 | -90.71 | 2367 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.29 | -26.70 | -91.30 | 2308 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -32.70 | -97.47 | 3529 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -37.20 | -96.82 | 3635 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -25.89 | -94.33 | 2586 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.93 | -99.39 | 5822 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -25.97 | -91.42 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -31.81 | -96.11 | 3524 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.87 | -99.74 | 6238 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.80 | -29.81 | -91.80 | 2371 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -39.37 | -97.52 | 3668 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.97 | -98.48 | 4769 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.78 | -33.90 | -93.78 | 2817 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.94 | -99.53 | 6247 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.70 | -22.37 | -86.75 | 2170 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.15 | -27.21 | -88.16 | 2164 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.91 | -33.01 | -95.93 | 3817 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -34.26 | -89.40 | 2109 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.85 | -34.09 | -95.86 | 4163 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.38 | -99.89 | 8315 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T03:55 | AI bee: Boozy | sell | ETH-USD | 15.60 | -0.07 | Jev: buy |
| 2026-10-18T03:52 | Donchian 55/20 | buy | XRP-USD | 3.01 | — | rebalance up |
| 2026-10-18T03:52 | Donchian 55/20 | sell | SOL-USD | 3.01 | -0.01 | rebalance down |
| 2026-10-18T03:50 | Volume breakout | buy | SOL-USD | 15.79 | — | entry signal |
| 2026-10-18T03:50 | Squeeze breakout | buy | XRP-USD | 15.51 | — | entry signal |
| 2026-10-18T03:50 | Keltner breakout | buy | XRP-USD | 13.28 | — | entry signal |
| 2026-10-18T03:50 | Donchian 55/20 | buy | XRP-USD | 6.05 | — | entry signal |
| 2026-10-18T03:50 | Donchian 55/20 | buy | DOGE-USD | 12.06 | — | entry signal |
| 2026-10-18T03:50 | Donchian 55/20 | sell | BTC-USD | 3.01 | -0.01 | rebalance down |
| 2026-10-18T03:50 | ROC + volume | buy | SOL-USD | 15.66 | — | entry signal |
| 2026-10-18T03:45 | Keltner breakout | buy | SOL-USD | 13.28 | — | entry signal |
| 2026-10-18T03:45 | Donchian 55/20 | buy | SOL-USD | 15.07 | — | entry signal |
| 2026-10-18T03:40 | Three white soldiers | buy | SOL-USD | 20.95 | — | entry signal |
| 2026-10-18T03:40 | Ichimoku | buy | XRP-USD | 12.64 | — | entry signal |
| 2026-10-18T03:39 | AI bee: Boozy | buy | ETH-USD | 15.67 | — | Jev: buy (buy p=0.73) |
| 2026-10-18T03:32 | AI bee: Boozy | sell | BTC-USD | 15.67 | -0.12 | Jev: sell |
| 2026-10-18T03:15 | AI bee: Boozy | buy | BTC-USD | 15.79 | — | Jev: buy (buy p=0.74) |
| 2026-10-18T03:15 | AI bee: Boozy | sell | ETH-USD | 15.79 | -0.05 | Jev: add (buy p=0.65) |
| 2026-10-18T03:15 | Keltner breakout | buy | BTC-USD | 13.28 | — | entry signal |
| 2026-10-18T03:15 | Donchian 55/20 | buy | ETH-USD | 15.08 | — | entry signal |
| 2026-10-18T03:15 | ROC + volume | buy | ETH-USD | 15.66 | — | entry signal |
| 2026-10-18T03:10 | Heikin-Ashi · 1h | buy | BTC-USD | 4.08 | — | rebalance up |
| 2026-10-18T03:10 | Heikin-Ashi · 1h | sell | DOGE-USD | 4.08 | -0.01 | rebalance down |
| 2026-10-18T03:10 | Keltner breakout | buy | ETH-USD | 13.29 | — | entry signal |
| 2026-10-18T03:10 | Ichimoku | buy | SOL-USD | 12.66 | — | entry signal |
| 2026-10-18T03:10 | Ichimoku | buy | DOGE-USD | 12.66 | — | entry signal |
| 2026-10-18T03:05 | Ichimoku | buy | ETH-USD | 12.66 | — | entry signal |
| 2026-10-18T03:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.08 | — | entry signal |
| 2026-10-18T03:00 | Heikin-Ashi · 1h | sell | ETH-USD | 4.08 | -0.01 | rebalance down |
| 2026-10-18T03:00 | MACD cross · 1h | buy | DOGE-USD | 6.61 | — | entry signal |
| 2026-10-18T03:00 | MACD cross · 1h | sell | BTC-USD | 6.61 | -0.01 | rebalance down |
| 2026-10-18T03:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 20.42 | — | entry signal |
| 2026-10-18T02:59 | AI bee: Boozy | buy | ETH-USD | 15.83 | — | Jev: buy (buy p=0.76) |
| 2026-10-18T02:42 | AI bee: Boozy | sell | ETH-USD | 15.83 | -0.10 | Jev: sell |
| 2026-10-18T02:27 | AI bee: Boozy | buy | ETH-USD | 15.94 | — | Jev: buy (buy p=0.73) |
| 2026-10-18T02:05 | Squeeze breakout | sell | XRP-USD | 15.44 | -0.15 | exit signal |
| 2026-10-18T02:05 | ROC + volume | sell | SOL-USD | 15.55 | -0.16 | stop-loss |
| 2026-10-18T02:05 | Ichimoku | sell | XRP-USD | 12.63 | -0.04 | exit signal |
| 2026-10-18T02:00 | VWAP momentum · 1h | buy | XRP-USD | 11.18 | — | entry signal |
| 2026-10-18T02:00 | VWAP momentum · 1h | buy | SOL-USD | 16.34 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 03:55:05.000138+00:00 -> 2026-10-18 04:05:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
