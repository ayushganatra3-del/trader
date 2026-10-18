# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T01:25:05.000133+00:00 · 26622 ticks

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

Today: 1065 decisions in 213 calls, $0.0149 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T01:25 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-10-18T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T01:25 | 2 / 2 / 1 | SOL-USD 30% |  |

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
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.15 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.39 | -3.30 | -13.80 | 134 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -7.63 | -3.75 | -9.05 | 277 |
| 17 | Hold BTC | benchmark | 96.78 | -3.22 | 0 | — | 28.76 | 3.39 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -20.22 | -6.11 | -20.39 | 142 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.41 | -1.49 | -13.33 | 253 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.69 | 0.86 | -9.46 | 100 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -12.72 | -1.95 | -21.23 | 126 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -0.53 | 0.11 | -22.55 | 273 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.92 | -2.04 | -8.74 | 116 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.33 | -5.60 | -12.50 | 236 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.58 | -0.07 | -14.55 | 114 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.68 | 0.41 | -26.55 | 216 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.87 | 1.07 | -14.21 | 267 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.05 | -0.51 | -33.23 | 228 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -22.34 | -4.62 | -26.17 | 207 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.02 | -0.96 | -27.05 | 203 |
| 42 | MACD cross · 1h | trend | 88.13 | -11.87 | 177 | 22.0 | -15.95 | -2.11 | -29.52 | 460 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.24 | -7.73 | -25.57 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.92 | -0.61 | -34.04 | 316 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.55 | -13.45 | 142 | 43.7 | -20.96 | -3.83 | -22.11 | 368 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.75 | -4.49 | -23.64 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 2.19 | 0.47 | -21.63 | 212 |
| 50 | Three white soldiers | momentum | 84.36 | -15.64 | 211 | 19.0 | -47.05 | -19.14 | -47.83 | 598 |
| 51 | MFI reversion · 1h | reversion | 83.99 | -16.01 | 204 | 30.4 | -20.94 | -3.46 | -21.51 | 142 |
| 52 | Z-score reversion · 1h | reversion | 83.33 | -16.67 | 86 | 31.4 | -15.82 | -2.76 | -20.30 | 185 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.27 | -1.61 | -27.07 | 394 |
| 54 | Agent (ML meta-label) | meta | 82.43 | -17.57 | 649 | 18.2 | -13.26 | -2.00 | -20.80 | 391 |
| 55 | VWAP momentum · 1h | momentum | 81.71 | -18.29 | 398 | 20.6 | -37.60 | -5.75 | -45.23 | 1255 |
| 56 | EMA 9/21 cross · 1h | trend | 81.67 | -18.33 | 129 | 11.6 | -5.88 | -0.46 | -29.74 | 313 |
| 57 | Heikin-Ashi · 1h | trend | 81.55 | -18.45 | 201 | 22.9 | -32.05 | -5.25 | -41.72 | 675 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.81 | -36.60 | 531 |
| 59 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.51 | -2.58 | -21.70 | 162 |
| 60 | Bollinger reversion · 1h | reversion | 79.86 | -20.14 | 144 | 30.6 | -30.78 | -6.42 | -32.71 | 350 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.17 | -2.63 | -26.46 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.11 | -6.52 | -36.80 | 535 |
| 63 | Volume breakout | breakout | 63.30 | -36.70 | 329 | 13.1 | -63.37 | -18.29 | -63.38 | 882 |
| 64 | ROC + volume | momentum | 62.81 | -37.19 | 554 | 21.8 | -75.74 | -17.71 | -77.53 | 1720 |
| 65 | Squeeze breakout | breakout | 62.29 | -37.70 | 437 | 14.6 | -62.79 | -17.88 | -64.47 | 1213 |
| 66 | RSI(14) reversion | reversion | 60.91 | -39.09 | 667 | 25.5 | -74.22 | -16.56 | -74.33 | 1628 |
| 67 | Donchian 55/20 | breakout | 60.32 | -39.68 | 445 | 17.5 | -69.21 | -14.66 | -72.07 | 1283 |
| 68 | EMA 20/50 cross | trend | 57.72 | -42.28 | 470 | 18.7 | -77.20 | -15.31 | -79.76 | 1448 |
| 69 | VWAP reversion | reversion | 54.51 | -45.49 | 701 | 23.8 | -73.13 | -15.51 | -73.33 | 1511 |
| 70 | Keltner breakout | breakout | 53.46 | -46.54 | 620 | 15.8 | -83.27 | -26.97 | -83.27 | 1829 |
| 71 | AI bee: Boozy | ai | 53.15 | -46.85 | 322 | 6.2 | — | — | — | — |
| 72 | Ichimoku | trend | 50.69 | -49.31 | 567 | 11.5 | -82.15 | -23.41 | -82.19 | 1735 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -29.96 | -98.62 | 5316 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.63 | -30.74 | -93.64 | 2605 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.57 | -20.49 | -87.54 | 1916 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -25.00 | -90.69 | 2371 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.39 | -26.96 | -91.39 | 2313 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -32.69 | -97.47 | 3526 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -36.90 | -96.81 | 3629 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.13 | -26.82 | -94.35 | 2590 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.90 | -99.38 | 5819 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.39 | -25.97 | -91.42 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.14 | -32.06 | -96.14 | 3531 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.58 | -99.74 | 6236 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -29.61 | -91.79 | 2371 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -38.90 | -97.50 | 3664 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.91 | -98.48 | 4768 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.73 | -33.43 | -93.74 | 2812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.84 | -99.53 | 6243 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.40 | -86.77 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.01 | -27.21 | -88.03 | 2167 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -33.02 | -95.93 | 3818 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -33.96 | -89.33 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.84 | -34.01 | -95.86 | 4159 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.63 | -99.89 | 8309 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T01:20 | AI bee: Boozy | buy | SOL-USD | 16.14 | — | Jev: buy (buy p=0.71) |
| 2026-10-18T01:20 | Keltner breakout | buy | BTC-USD | 13.38 | — | entry signal |
| 2026-10-18T01:11 | AI bee: Boozy | sell | ETH-USD | 16.14 | -0.10 | Jev: sell |
| 2026-10-18T01:05 | Squeeze breakout | buy | SOL-USD | 15.58 | — | entry signal |
| 2026-10-18T01:05 | EMA 20/50 cross | sell | SOL-USD | 2.88 | -0.01 | rebalance down |
| 2026-10-18T01:01 | EMA 20/50 cross | buy | ETH-USD | 5.76 | — | rebalance up |
| 2026-10-18T01:01 | EMA 20/50 cross | sell | XRP-USD | 2.88 | -0.01 | rebalance down |
| 2026-10-18T01:01 | EMA 20/50 cross | sell | BTC-USD | 2.88 | -0.02 | rebalance down |
| 2026-10-18T01:00 | Bollinger reversion · 1h | buy | ETH-USD | 2.05 | — | entry |
| 2026-10-18T01:00 | Bollinger reversion · 1h | buy | DOGE-USD | 4.07 | — | rebalance up |
| 2026-10-18T01:00 | Bollinger reversion · 1h | sell | BTC-USD | 6.12 | -0.02 | exit signal |
| 2026-10-18T01:00 | EMA 20/50 cross | buy | ETH-USD | 2.94 | — | entry signal |
| 2026-10-18T01:00 | EMA 20/50 cross | buy | DOGE-USD | 11.54 | — | entry signal |
| 2026-10-18T00:55 | AI bee: Boozy | buy | ETH-USD | 16.24 | — | Jev: buy (buy p=0.72) |
| 2026-10-18T00:55 | Volume breakout | buy | BTC-USD | 15.83 | — | entry signal |
| 2026-10-18T00:55 | EMA 20/50 cross | buy | SOL-USD | 14.44 | — | entry signal |
| 2026-10-18T00:45 | EMA 20/50 cross | buy | XRP-USD | 14.45 | — | entry signal |
| 2026-10-18T00:40 | AI bee: Boozy | sell | ETH-USD | 16.24 | -0.09 | Jev: sell |
| 2026-10-18T00:25 | AI bee: Boozy | buy | ETH-USD | 16.34 | — | Jev: buy (buy p=0.72) |
| 2026-10-18T00:25 | EMA 20/50 cross | buy | BTC-USD | 14.46 | — | entry signal |
| 2026-10-18T00:20 | Ichimoku | buy | XRP-USD | 12.67 | — | entry signal |
| 2026-10-18T00:15 | VWAP reversion | sell | SOL-USD | 10.93 | 0.07 | exit signal |
| 2026-10-18T00:15 | VWAP reversion | sell | ETH-USD | 13.63 | 0.02 | exit signal |
| 2026-10-18T00:15 | VWAP reversion | sell | DOGE-USD | 10.93 | 0.06 | exit signal |
| 2026-10-18T00:15 | RSI(14) reversion | sell | XRP-USD | 15.19 | -0.02 | exit signal |
| 2026-10-18T00:10 | AI bee: Boozy | sell | ETH-USD | 16.34 | -0.13 | Jev: sell |
| 2026-10-18T00:00 | MACD cross · 1h | buy | XRP-USD | 7.73 | — | entry signal |
| 2026-10-18T00:00 | MACD cross · 1h | buy | BTC-USD | 17.63 | — | entry signal |
| 2026-10-17T23:55 | AI bee: Boozy | buy | ETH-USD | 16.46 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T23:55 | RSI(14) reversion | sell | SOL-USD | 15.23 | 0.02 | exit signal |
| 2026-10-17T23:55 | RSI(14) reversion | sell | ETH-USD | 15.25 | 0.03 | exit signal |
| 2026-10-17T23:55 | Squeeze breakout | buy | BTC-USD | 15.59 | — | entry signal |
| 2026-10-17T23:45 | RSI(14) reversion | sell | DOGE-USD | 12.22 | 0.06 | exit signal |
| 2026-10-17T23:10 | Three white soldiers | sell | ETH-USD | 20.96 | -0.17 | exit signal |
| 2026-10-17T23:00 | Bollinger reversion · 1h | buy | DOGE-USD | 2.58 | — | entry signal |
| 2026-10-17T23:00 | Bollinger reversion · 1h | buy | BTC-USD | 6.15 | — | entry signal |
| 2026-10-17T22:58 | AI bee: Boozy | sell | ETH-USD | 16.46 | -0.10 | Jev: buy |
| 2026-10-17T22:50 | VWAP reversion | buy | ETH-USD | 2.74 | — | rebalance up |
| 2026-10-17T22:50 | VWAP reversion | sell | XRP-USD | 10.89 | 0.08 | exit signal |
| 2026-10-17T22:50 | VWAP reversion | sell | BTC-USD | 10.85 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 01:25:05.000133+00:00 -> 2026-10-18 01:35:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
