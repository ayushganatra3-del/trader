# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T01:09:05.000095+00:00 · 73671 ticks

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

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 36.42 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 675 decisions in 135 calls, $0.0095 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T01:09 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-26T01:09 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T01:09 | 1 / 4 / 0 | ETH-USD 56% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.91 | 15.91 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.06 | 5.06 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | 0.39 | 0.21 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.46 | 0.55 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.06 | -5.94 | 0 | — | -6.75 | -1.73 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.65 | -6.35 | 23 | 8.7 | -5.20 | -7.49 | -6.57 | 25 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.28 | -6.71 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.12 | -6.88 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.56 | -8.44 | 116 | 24.1 | -7.45 | -4.36 | -10.99 | 34 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.16 | -10.84 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.29 | -3.14 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.81 | -14.19 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.69 | -15.31 | 173 | 44.5 | -12.89 | -2.37 | -20.49 | 155 |
| 23 | Squeeze breakout · 1h | breakout | 83.33 | -16.67 | 77 | 19.5 | -19.45 | -6.60 | -19.85 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -13.30 | -6.13 | -13.46 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.41 | -5.13 | -23.63 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.90 | -23.10 | 173 | 28.9 | -21.93 | -8.72 | -22.57 | 71 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.35 | -24.65 | 210 | 27.6 | -35.52 | -8.61 | -36.11 | 185 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 73.99 | -26.01 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.59 | -26.41 | 141 | 24.8 | -26.46 | -6.45 | -26.74 | 143 |
| 34 | Ichimoku · 1h | trend | 73.30 | -26.70 | 114 | 15.8 | -29.88 | -7.58 | -30.60 | 99 |
| 35 | Daily: Momentum burst | daily | 71.06 | -28.94 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.02 | -29.98 | 3 | 0.0 | -28.75 | -5.05 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.94 | -30.06 | 264 | 18.9 | -37.25 | -6.96 | -38.23 | 288 |
| 38 | Bollinger breakout · 1h | breakout | 68.40 | -31.60 | 209 | 22.5 | -31.09 | -7.96 | -31.80 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.83 | -32.17 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 66.87 | -33.13 | 221 | 17.6 | -40.33 | -7.98 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.64 | -33.36 | 411 | 39.9 | -32.96 | -3.44 | -42.70 | 439 |
| 42 | OBV trend · 1h | momentum | 66.42 | -33.58 | 325 | 19.7 | -42.15 | -10.35 | -42.35 | 224 |
| 43 | EMA 20/50 cross · 1h | trend | 65.88 | -34.12 | 126 | 9.5 | -38.01 | -10.47 | -38.21 | 112 |
| 44 | Triple EMA stack · 1h | trend | 65.09 | -34.91 | 172 | 15.1 | -43.12 | -10.52 | -43.18 | 171 |
| 45 | MACD zero-line · 1h | trend | 63.19 | -36.81 | 202 | 16.3 | -37.00 | -10.26 | -37.58 | 203 |
| 46 | MFI reversion · 1h | reversion | 62.65 | -37.35 | 518 | 32.4 | -32.50 | -4.80 | -38.04 | 197 |
| 47 | RSI momentum · 1h | momentum | 62.60 | -37.40 | 203 | 14.8 | -43.65 | -9.66 | -44.11 | 195 |
| 48 | Donchian 20/10 · 1h | breakout | 61.22 | -38.78 | 183 | 17.5 | -41.45 | -9.22 | -43.13 | 200 |
| 49 | ROC + volume · 1h | momentum | 60.92 | -39.08 | 465 | 26.7 | -40.50 | -7.85 | -41.16 | 338 |
| 50 | Heikin-Ashi · 1h | trend | 60.90 | -39.10 | 547 | 21.9 | -49.54 | -10.14 | -50.17 | 641 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.17 | -41.83 | 314 | 12.1 | -45.23 | -10.36 | -46.48 | 334 |
| 53 | MACD cross · 1h | trend | 57.30 | -42.70 | 492 | 20.3 | -54.07 | -10.94 | -55.74 | 512 |
| 54 | Agent (ML meta-label) | meta | 56.24 | -43.76 | 2074 | 25.4 | -24.45 | -3.32 | -30.91 | 326 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.13 | -8.97 | -55.52 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.97 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 50.99 | -49.01 | 1091 | 21.7 | -61.71 | -13.30 | -62.43 | 1188 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.91 | -9.34 | -59.31 | 693 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.32 | -9.37 | -59.57 | 607 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -46.26 | -99.16 | 5369 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.52 | -31.07 | -84.49 | 1428 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.20 | -45.39 | -94.39 | 2395 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.18 | -29.61 | -90.95 | 1881 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -38.77 | -91.75 | 2214 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.45 | -26.58 | -88.55 | 1915 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -46.09 | -98.22 | 3410 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -48.90 | -96.92 | 3341 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -92.94 | -34.42 | -92.94 | 2074 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.19 | -34.85 | -82.33 | 1508 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -53.49 | -99.70 | 6289 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -37.02 | -93.11 | 2473 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.12 | -34.79 | -94.12 | 3123 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -62.50 | -99.82 | 6071 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.97 | -41.70 | -93.23 | 2255 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.65 | -18.59 | -52.24 | 660 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.56 | -22.97 | -78.31 | 1603 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -54.44 | -97.72 | 3234 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.20 | -58.13 | -99.21 | 5126 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -23.08 | -70.66 | 1197 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -45.48 | -94.69 | 2651 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.20 | -34.07 | -84.50 | 1644 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -67.86 | -99.77 | 6529 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.57 | -30.62 | -91.95 | 2497 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.96 | -20.06 | -83.48 | 1969 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.74 | -32.69 | -91.93 | 2164 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.23 | -47.66 | -98.24 | 4055 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.25 | -44.98 | -90.70 | 2192 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.20 | -26.12 | -68.00 | 783 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.58 | -27.67 | -73.27 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.77 | -19.16 | -85.02 | 1823 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -48.32 | -98.12 | 4400 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -88.10 | -99.94 | 8282 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.53 | -6.88 | -52.53 | 295 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | XRP-USD | 4.27 | 0.04 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | SOL-USD | 4.28 | 0.05 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | ETH-USD | 4.24 | 0.02 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | DOGE-USD | 4.31 | 0.08 | exit signal |
| 2026-11-26T01:01 | VWAP momentum · 1h | sell | BTC-USD | 4.26 | 0.03 | exit signal |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | SOL-USD | 2.44 | — | entry |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.44 | — | entry |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.44 | — | entry |
| 2026-11-26T00:00 | Heikin-Ashi · 1h | buy | BTC-USD | 2.44 | — | entry |
| 2026-11-25T22:11 | Three white soldiers · 1h | buy | DOGE-USD | 5.33 | — | rebalance up |
| 2026-11-25T22:11 | ROC + volume · 1h | buy | DOGE-USD | 6.75 | — | entry |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | XRP-USD | 3.41 | 0.03 | rebalance down |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | SOL-USD | 3.42 | 0.03 | rebalance down |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | ETH-USD | 3.29 | -0.01 | rebalance down |
| 2026-11-25T22:11 | ROC + volume · 1h | sell | BTC-USD | 3.36 | 0.01 | rebalance down |
| 2026-11-25T22:00 | MACD zero-line · 1h | buy | BTC-USD | 7.88 | — | entry signal |
| 2026-11-25T22:00 | MACD zero-line · 1h | sell | XRP-USD | 7.85 | -0.05 | rebalance down |
| 2026-11-25T21:05 | Bollinger breakout · 1h | buy | BTC-USD | 3.43 | — | rebalance up |
| 2026-11-25T21:05 | Bollinger breakout · 1h | sell | DOGE-USD | 3.43 | 0.01 | rebalance down |
| 2026-11-25T21:00 | Bollinger breakout · 1h | buy | BTC-USD | 10.21 | — | entry signal |
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | XRP-USD | 3.40 | -0.01 | rebalance down |
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | SOL-USD | 3.41 | -0.01 | rebalance down |
| 2026-11-25T21:00 | Bollinger breakout · 1h | sell | ETH-USD | 3.40 | -0.01 | rebalance down |
| 2026-11-25T21:00 | RSI momentum · 1h | buy | BTC-USD | 7.08 | — | entry signal |
| 2026-11-25T21:00 | RSI momentum · 1h | sell | SOL-USD | 3.55 | -0.01 | rebalance down |
| 2026-11-25T21:00 | RSI momentum · 1h | sell | DOGE-USD | 3.53 | -0.01 | rebalance down |
| 2026-11-25T21:00 | MACD zero-line · 1h | buy | XRP-USD | 15.84 | — | entry signal |
| 2026-11-25T20:55 | Agent (ML meta-label) | buy | SQQQ | 14.06 | — | following Connors RSI(2), Z-score reversion, RSI(14) reversion |
| 2026-11-25T20:55 | Agent (aggressive) | sell | SQQQ | 37.46 | -0.91 | selected signal exited |
| 2026-11-25T20:55 | Agent | sell | SQQQ | 30.49 | -0.30 | selected signal exited |
| 2026-11-25T20:55 | Opening range 30m | sell | UPRO | 7.99 | 0.30 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | TQQQ | 8.18 | 0.49 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | TNA | 7.90 | 0.42 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | SPY | 7.76 | 0.07 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | QQQ | 7.82 | 0.12 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | PLTR | 7.90 | 0.30 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | META | 7.01 | 0.15 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | IWM | 7.73 | 0.11 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | ETHU | 7.92 | 0.30 | end-of-day flatten |
| 2026-11-25T20:55 | Opening range 30m | sell | COIN | 7.98 | 0.29 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 01:09:05.000095+00:00 -> 2026-11-26 01:19:05.000095+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
