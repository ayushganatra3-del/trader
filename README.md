# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T10:05:05.000176+00:00 · 74108 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.44 (-23.56%)

Closed trades 250, win rate 36.0%, fees £6.87, max drawdown -24.09%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 7230 decisions in 1446 calls, $0.1009 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T10:05 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-26T10:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T10:05 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.45 | +1.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.63 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.03 | 16.03 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.16 | 5.16 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | 0.39 | 0.21 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.46 | 0.55 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.15 | -5.85 | 0 | — | -6.75 | -1.73 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.63 | -6.37 | 24 | 12.5 | -5.32 | -7.73 | -6.57 | 25 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.38 | -6.62 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.21 | -6.79 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.58 | -8.42 | 116 | 24.1 | -7.40 | -4.36 | -10.99 | 32 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.25 | -10.75 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.29 | -3.14 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.84 | -14.16 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.87 | -2.37 | -20.49 | 156 |
| 23 | Squeeze breakout · 1h | breakout | 83.70 | -16.30 | 77 | 19.5 | -19.23 | -6.47 | -19.91 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.28 | -6.11 | -13.46 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.41 | -5.13 | -23.63 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.83 | -23.17 | 174 | 29.3 | -22.21 | -8.80 | -22.48 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.59 | -24.41 | 210 | 27.6 | -34.18 | -8.21 | -35.47 | 182 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.06 | -25.94 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.58 | -26.42 | 141 | 24.8 | -26.28 | -6.41 | -26.51 | 144 |
| 34 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -28.79 | -7.26 | -29.63 | 95 |
| 35 | Daily: Momentum burst | daily | 71.08 | -28.92 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.34 | -29.66 | 3 | 0.0 | -28.74 | -5.04 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 70.18 | -29.82 | 264 | 18.9 | -37.31 | -6.97 | -38.45 | 288 |
| 38 | Bollinger breakout · 1h | breakout | 68.84 | -31.16 | 209 | 22.5 | -30.72 | -7.80 | -31.81 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.89 | -32.11 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.03 | -32.97 | 221 | 17.6 | -40.21 | -7.94 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.70 | -33.30 | 411 | 39.9 | -32.82 | -3.42 | -42.70 | 439 |
| 42 | OBV trend · 1h | momentum | 66.48 | -33.52 | 325 | 19.7 | -41.07 | -10.20 | -41.32 | 225 |
| 43 | EMA 20/50 cross · 1h | trend | 65.90 | -34.10 | 126 | 9.5 | -37.70 | -10.37 | -37.97 | 116 |
| 44 | Triple EMA stack · 1h | trend | 64.97 | -35.03 | 172 | 15.1 | -42.00 | -10.26 | -42.50 | 172 |
| 45 | MACD zero-line · 1h | trend | 63.39 | -36.61 | 202 | 16.3 | -36.71 | -10.11 | -37.58 | 202 |
| 46 | RSI momentum · 1h | momentum | 62.88 | -37.12 | 203 | 14.8 | -43.43 | -9.57 | -44.10 | 194 |
| 47 | MFI reversion · 1h | reversion | 62.71 | -37.29 | 520 | 32.7 | -33.29 | -4.95 | -37.91 | 195 |
| 48 | Donchian 20/10 · 1h | breakout | 61.40 | -38.60 | 183 | 17.5 | -40.93 | -9.03 | -42.86 | 199 |
| 49 | ROC + volume · 1h | momentum | 61.13 | -38.87 | 465 | 26.7 | -40.14 | -7.74 | -41.18 | 336 |
| 50 | Heikin-Ashi · 1h | trend | 60.82 | -39.18 | 553 | 21.9 | -49.35 | -10.07 | -49.85 | 640 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.38 | -41.62 | 314 | 12.1 | -45.47 | -10.32 | -46.84 | 333 |
| 53 | MACD cross · 1h | trend | 57.43 | -42.57 | 492 | 20.3 | -53.60 | -10.80 | -55.57 | 510 |
| 54 | Agent (ML meta-label) | meta | 56.27 | -43.73 | 2074 | 25.4 | -20.28 | -2.61 | -28.06 | 326 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.11 | -8.96 | -55.49 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.97 | -45.50 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.35 | -8.93 | -58.40 | 680 |
| 58 | VWAP momentum · 1h | momentum | 50.88 | -49.12 | 1099 | 21.6 | -61.72 | -13.38 | -62.19 | 1194 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.27 | -9.35 | -59.57 | 606 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -48.89 | -99.15 | 5388 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.70 | -31.71 | -84.17 | 1427 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.31 | -47.19 | -94.32 | 2399 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.26 | -29.94 | -90.82 | 1880 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.44 | -39.90 | -91.55 | 2218 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.44 | -26.79 | -88.45 | 1915 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -47.53 | -98.20 | 3412 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.87 | -51.73 | -96.87 | 3345 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.13 | -35.52 | -93.13 | 2090 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.11 | -35.44 | -82.11 | 1507 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -53.65 | -99.69 | 6280 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -37.59 | -93.04 | 2468 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.23 | -35.29 | -94.23 | 3137 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -64.95 | -99.82 | 6072 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.99 | -42.28 | -93.18 | 2254 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.04 | -18.32 | -51.64 | 656 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.89 | -23.47 | -78.27 | 1600 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -56.85 | -97.73 | 3235 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -58.82 | -99.19 | 5118 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -23.29 | -70.48 | 1196 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -47.17 | -94.62 | 2649 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.38 | -34.59 | -84.46 | 1642 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -69.00 | -99.77 | 6522 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.45 | -30.18 | -91.80 | 2493 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.96 | -20.07 | -83.44 | 1970 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.50 | -31.84 | -91.81 | 2155 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -47.84 | -98.22 | 4051 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.41 | -47.11 | -90.61 | 2197 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.29 | -29.77 | -68.29 | 779 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.48 | -27.60 | -72.58 | 1148 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.85 | -19.29 | -85.04 | 1826 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -48.79 | -98.10 | 4399 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -101.67 | -99.94 | 8292 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.24 | -6.82 | -52.53 | 291 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T10:05 | VWAP momentum · 1h | sell | DOGE-USD | 1.95 | -0.01 | target is flat |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | ETH-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T09:00 | VWAP reversion · 1h | sell | ETH-USD | 21.18 | 0.01 | exit signal |
| 2026-11-26T09:00 | Connors RSI(2) · 1h | sell | DOGE-USD | 20.01 | 0.02 | exit signal |
| 2026-11-26T08:00 | VWAP reversion · 1h | buy | ETH-USD | 21.17 | — | entry signal |
| 2026-11-26T07:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 19.99 | — | entry signal |
| 2026-11-26T07:00 | Three white soldiers · 1h | sell | DOGE-USD | 18.80 | 0.21 | exit signal |
| 2026-11-26T07:00 | Volume breakout · 1h | sell | DOGE-USD | 19.21 | 0.08 | exit signal |
| 2026-11-26T07:00 | VWAP momentum · 1h | sell | XRP-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | XRP-USD | 2.40 | -0.03 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | SOL-USD | 2.43 | -0.00 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | BTC-USD | 2.43 | -0.01 | exit signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | buy | ETH-USD | 5.33 | — | entry signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | sell | DOGE-USD | 5.33 | -0.06 | rebalance down |
| 2026-11-26T06:25 | VWAP momentum · 1h | sell | DOGE-USD | 2.11 | -0.01 | target is flat |
| 2026-11-26T06:25 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.42 | -0.01 | target is flat |
| 2026-11-26T06:20 | VWAP momentum · 1h | buy | DOGE-USD | 2.12 | — | entry |
| 2026-11-26T06:20 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.43 | — | entry |
| 2026-11-26T06:05 | VWAP momentum · 1h | sell | DOGE-USD | 1.95 | -0.02 | target is flat |
| 2026-11-26T06:05 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.44 | 0.01 | target is flat |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | SOL-USD | 1.94 | -0.02 | exit signal |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | BTC-USD | 1.95 | -0.02 | exit signal |
| 2026-11-26T05:00 | MFI reversion · 1h | sell | SOL-USD | 4.81 | 0.18 | exit signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | SOL-USD | 6.49 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | sell | XRP-USD | 3.30 | 0.00 | rebalance down |
| 2026-11-26T04:00 | VWAP momentum · 1h | sell | SOL-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.44 | — | entry signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | sell | ETH-USD | 2.43 | -0.01 | exit signal |
| 2026-11-26T04:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 3.75 | — | entry signal |
| 2026-11-26T04:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 3.75 | -0.01 | rebalance down |
| 2026-11-26T03:00 | MFI reversion · 1h | sell | BTC-USD | 5.16 | 0.15 | exit signal |
| 2026-11-26T03:00 | VWAP momentum · 1h | sell | BTC-USD | 1.95 | -0.02 | exit signal |
| 2026-11-26T02:20 | ROC + volume · 1h | buy | DOGE-USD | 3.34 | — | rebalance up |
| 2026-11-26T02:20 | ROC + volume · 1h | buy | BTC-USD | 3.37 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 10:05:05.000176+00:00 -> 2026-11-26 10:15:05.000176+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
