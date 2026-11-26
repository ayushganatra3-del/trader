# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T19:05:05.000141+00:00 · 74566 ticks

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
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 14097 decisions in 2820 calls, $0.1967 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T19:05 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-26T19:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T19:05 | 1 / 4 / 0 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.66 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.02 | 16.02 | 0 | — | 14.88 | 4.95 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.15 | 5.15 | 0 | — | 6.08 | 1.18 | -6.60 | 1 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | 0.01 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.18 | -7.38 | 2 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.30 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.38 | 0.52 | -5.49 | 160 |
| 12 | Hold SPY | benchmark | 94.15 | -5.85 | 0 | — | -6.75 | -1.83 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.63 | -6.37 | 24 | 12.5 | -5.27 | -7.83 | -6.56 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.37 | -6.63 | 0 | — | -7.99 | -1.62 | -13.91 | 1 |
| 15 | Trend pullback · 1h | trend | 91.58 | -8.42 | 116 | 24.1 | -6.81 | -4.41 | -10.25 | 30 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.65 | -11.13 | 23 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.24 | -10.76 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.26 | -20.94 | 2 |
| 19 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -2.93 | -15.56 | 552 |
| 20 | Daily: Bullish score | daily | 85.83 | -14.16 | 20 | 20.0 | -13.31 | -3.13 | -19.56 | 18 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.02 | -2.42 | -20.49 | 155 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 23 | Squeeze breakout · 1h | breakout | 83.08 | -16.92 | 79 | 20.3 | -19.52 | -6.72 | -19.77 | 79 |
| 24 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.17 | -6.11 | -13.42 | 59 |
| 25 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.12 | -24.05 | 678 |
| 26 | Volume breakout · 1h | breakout | 76.83 | -23.17 | 174 | 29.3 | -22.18 | -8.87 | -22.46 | 69 |
| 27 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.17 | -6.12 | -27.61 | 195 |
| 28 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.78 | -4.63 | -18.54 | 92 |
| 29 | Parabolic SAR · 1h | trend | 75.42 | -24.58 | 212 | 28.3 | -34.58 | -8.46 | -35.15 | 183 |
| 30 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.69 | -29.10 | 73 |
| 31 | Max aggression: 5-day momentum | meta | 74.05 | -25.95 | 27 | 37.0 | -54.97 | -2.85 | -67.33 | 22 |
| 32 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -28.79 | -7.33 | -29.63 | 95 |
| 33 | Keltner breakout · 1h | breakout | 72.97 | -27.03 | 143 | 24.5 | -26.99 | -6.67 | -26.99 | 145 |
| 34 | Daily: Momentum burst | daily | 71.08 | -28.92 | 31 | 16.1 | -33.16 | -4.61 | -35.97 | 28 |
| 35 | ADX DI cross · 1h | trend | 69.98 | -30.02 | 268 | 19.8 | -36.82 | -6.91 | -38.08 | 287 |
| 36 | Hold BTC | benchmark | 69.89 | -30.11 | 3 | 0.0 | -28.25 | -4.97 | -36.10 | 1 |
| 37 | Bollinger breakout · 1h | breakout | 68.08 | -31.92 | 213 | 22.5 | -31.29 | -8.13 | -31.87 | 206 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 67.89 | -32.11 | 3 | 0.0 | -25.48 | -3.24 | -33.66 | 1 |
| 39 | Supertrend · 1h | trend | 67.07 | -32.93 | 221 | 17.6 | -40.20 | -8.01 | -42.10 | 210 |
| 40 | Stochastic reversion · 1h | reversion | 66.70 | -33.30 | 411 | 39.9 | -32.77 | -3.44 | -42.70 | 438 |
| 41 | OBV trend · 1h | momentum | 66.48 | -33.52 | 325 | 19.7 | -40.68 | -10.16 | -41.15 | 223 |
| 42 | EMA 20/50 cross · 1h | trend | 65.90 | -34.10 | 126 | 9.5 | -38.01 | -10.45 | -38.70 | 117 |
| 43 | Triple EMA stack · 1h | trend | 64.92 | -35.08 | 172 | 15.1 | -41.11 | -10.23 | -41.93 | 168 |
| 44 | MACD zero-line · 1h | trend | 63.09 | -36.91 | 206 | 16.5 | -37.02 | -10.38 | -37.32 | 200 |
| 45 | RSI momentum · 1h | momentum | 62.88 | -37.12 | 203 | 14.8 | -42.77 | -9.45 | -43.57 | 192 |
| 46 | MFI reversion · 1h | reversion | 62.70 | -37.30 | 520 | 32.7 | -32.25 | -4.79 | -38.15 | 193 |
| 47 | Donchian 20/10 · 1h | breakout | 61.38 | -38.62 | 183 | 17.5 | -40.86 | -9.09 | -42.84 | 199 |
| 48 | Heikin-Ashi · 1h | trend | 60.80 | -39.20 | 554 | 21.8 | -49.37 | -10.18 | -49.85 | 641 |
| 49 | ROC + volume · 1h | momentum | 60.52 | -39.48 | 472 | 26.9 | -40.35 | -7.90 | -41.14 | 335 |
| 50 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.67 | -63.62 | 39 |
| 51 | EMA 9/21 cross · 1h | trend | 58.40 | -41.60 | 314 | 12.1 | -44.78 | -10.28 | -46.16 | 330 |
| 52 | MACD cross · 1h | trend | 57.33 | -42.67 | 497 | 21.1 | -53.49 | -10.90 | -55.71 | 511 |
| 53 | Agent (ML meta-label) | meta | 56.27 | -43.73 | 2074 | 25.4 | -21.46 | -2.64 | -28.16 | 317 |
| 54 | CCI reversion · 1h | reversion | 52.51 | -47.49 | 463 | 37.8 | -52.41 | -8.86 | -55.31 | 500 |
| 55 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.86 | -5.02 | -45.49 | 431 |
| 56 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.99 | -9.21 | -58.37 | 690 |
| 57 | VWAP momentum · 1h | momentum | 50.72 | -49.28 | 1107 | 21.4 | -60.96 | -13.49 | -61.28 | 1193 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.15 | -9.41 | -59.57 | 606 |
| 59 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -48.86 | -99.18 | 5402 |
| 60 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.60 | -32.55 | -83.78 | 1423 |
| 61 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.24 | -48.27 | -94.26 | 2398 |
| 62 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.47 | -31.27 | -90.72 | 1887 |
| 63 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.57 | -41.08 | -91.57 | 2224 |
| 64 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.73 | -27.93 | -88.76 | 1929 |
| 65 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -49.25 | -98.19 | 3411 |
| 66 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -53.29 | -96.86 | 3347 |
| 67 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.29 | -36.38 | -93.29 | 2100 |
| 68 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.96 | -35.75 | -81.96 | 1504 |
| 69 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -55.70 | -99.69 | 6281 |
| 70 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -38.21 | -92.96 | 2471 |
| 71 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.28 | -36.26 | -94.28 | 3141 |
| 72 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -68.38 | -99.81 | 6067 |
| 73 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.09 | -43.35 | -93.09 | 2260 |
| 74 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.18 | -18.97 | -51.39 | 657 |
| 75 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.99 | -23.54 | -78.10 | 1604 |
| 76 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -59.14 | -97.70 | 3233 |
| 77 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -60.96 | -99.17 | 5114 |
| 78 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 79 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.82 | -22.78 | -69.94 | 1194 |
| 80 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -47.81 | -94.66 | 2656 |
| 81 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.49 | -51.25 | 291 |
| 82 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -35.31 | -84.54 | 1646 |
| 83 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -75.04 | -99.77 | 6516 |
| 84 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.47 | -31.13 | -91.80 | 2493 |
| 85 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.79 | -20.23 | -83.37 | 1975 |
| 86 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.44 | -32.84 | -91.83 | 2156 |
| 87 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -50.28 | -98.23 | 4052 |
| 88 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.35 | -47.46 | -90.46 | 2193 |
| 89 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.96 | -29.17 | -67.98 | 779 |
| 90 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.58 | -28.14 | -72.58 | 1149 |
| 91 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.61 | -19.48 | -85.00 | 1829 |
| 92 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -51.58 | -98.13 | 4403 |
| 93 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.55 | -99.94 | 8295 |
| 94 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 95 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.71 | -6.98 | -52.52 | 296 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T19:00 | VWAP momentum · 1h | buy | ETH-USD | 1.95 | — | entry signal |
| 2026-11-26T19:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.95 | — | entry signal |
| 2026-11-26T19:00 | ADX DI cross · 1h | buy | SOL-USD | 6.12 | — | entry signal |
| 2026-11-26T19:00 | ADX DI cross · 1h | buy | BTC-USD | 7.00 | — | entry signal |
| 2026-11-26T19:00 | Parabolic SAR · 1h | buy | SOL-USD | 12.58 | — | entry signal |
| 2026-11-26T18:00 | VWAP momentum · 1h | buy | XRP-USD | 2.11 | — | entry signal |
| 2026-11-26T17:00 | CCI reversion · 1h | buy | ETH-USD | 4.04 | — | entry signal |
| 2026-11-26T17:00 | ADX DI cross · 1h | buy | XRP-USD | 8.75 | — | entry signal |
| 2026-11-26T16:00 | Bollinger breakout · 1h | sell | BTC-USD | 17.07 | -0.03 | exit signal |
| 2026-11-26T16:00 | ROC + volume · 1h | sell | BTC-USD | 15.16 | -0.00 | exit signal |
| 2026-11-26T16:00 | VWAP momentum · 1h | buy | SOL-USD | 2.21 | — | entry signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | buy | DOGE-USD | 3.59 | — | rebalance up |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | XRP-USD | 6.38 | 0.12 | exit signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | SOL-USD | 6.36 | 0.03 | exit signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | ETH-USD | 6.34 | -0.00 | exit signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | BTC-USD | 6.39 | 0.05 | exit signal |
| 2026-11-26T16:00 | Parabolic SAR · 1h | sell | DOGE-USD | 9.62 | 0.23 | exit signal |
| 2026-11-26T16:00 | MACD zero-line · 1h | sell | ETH-USD | 15.67 | -0.13 | exit signal |
| 2026-11-26T16:00 | MACD cross · 1h | sell | ETH-USD | 4.07 | 0.07 | exit signal |
| 2026-11-26T15:55 | ROC + volume · 1h | sell | DOGE-USD | 15.10 | -0.04 | target is flat |
| 2026-11-26T15:55 | VWAP momentum · 1h | sell | DOGE-USD | 2.20 | -0.01 | target is flat |
| 2026-11-26T15:50 | ROC + volume · 1h | buy | DOGE-USD | 15.15 | — | entry |
| 2026-11-26T15:50 | VWAP momentum · 1h | buy | DOGE-USD | 2.21 | — | entry |
| 2026-11-26T15:35 | ROC + volume · 1h | sell | DOGE-USD | 15.08 | -0.07 | target is flat |
| 2026-11-26T15:35 | VWAP momentum · 1h | sell | DOGE-USD | 2.20 | -0.01 | target is flat |
| 2026-11-26T15:30 | ROC + volume · 1h | buy | DOGE-USD | 15.15 | — | entry |
| 2026-11-26T15:30 | VWAP momentum · 1h | buy | DOGE-USD | 2.21 | — | entry |
| 2026-11-26T15:10 | Squeeze breakout · 1h | sell | ETH-USD | 20.58 | -0.22 | stop-loss |
| 2026-11-26T15:10 | Keltner breakout · 1h | sell | DOGE-USD | 18.08 | -0.31 | stop-loss |
| 2026-11-26T15:10 | Bollinger breakout · 1h | sell | ETH-USD | 16.87 | -0.21 | stop-loss |
| 2026-11-26T15:10 | Bollinger breakout · 1h | sell | DOGE-USD | 13.58 | -0.02 | stop-loss |
| 2026-11-26T15:05 | Keltner breakout · 1h | sell | XRP-USD | 18.08 | -0.32 | stop-loss |
| 2026-11-26T15:05 | ROC + volume · 1h | sell | DOGE-USD | 15.06 | -0.11 | target is flat |
| 2026-11-26T15:05 | VWAP momentum · 1h | sell | DOGE-USD | 2.08 | -0.03 | target is flat |
| 2026-11-26T15:00 | Squeeze breakout · 1h | sell | XRP-USD | 20.90 | 0.10 | exit signal |
| 2026-11-26T15:00 | Bollinger breakout · 1h | buy | SOL-USD | 3.44 | — | rebalance up |
| 2026-11-26T15:00 | Bollinger breakout · 1h | buy | ETH-USD | 3.46 | — | rebalance up |
| 2026-11-26T15:00 | Bollinger breakout · 1h | buy | BTC-USD | 3.45 | — | rebalance up |
| 2026-11-26T15:00 | Bollinger breakout · 1h | sell | XRP-USD | 13.69 | 0.07 | exit signal |
| 2026-11-26T15:00 | ROC + volume · 1h | buy | DOGE-USD | 5.07 | — | rebalance up |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
