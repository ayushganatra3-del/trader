# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-07T11:50:05.000116+00:00 · 50841 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.95 (-12.05%)

Closed trades 153, win rate 36.6%, fees £4.57, max drawdown -12.52%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| DOGE-USD | 17.52 | -0.09 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 9201 decisions in 1845 calls, $0.1283 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-07T11:50 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-07T11:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-07T11:50 | 0 / 4 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI(14) reversion | SQQQ | 2.31 | +7.36% | 4 |
| Z-score reversion | SQQQ | 1.94 | +4.38% | 7 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Candlestick reversal · 1h | DOGE-USD | 1.92 | +7.45% | 7 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.49 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.16 | -0.84 | 122 | 47.5 | -13.19 | -3.16 | -14.37 | 152 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.38 | -4.64 | -10.36 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.56 | -0.43 | -9.18 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.98 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -16.31 | -6.00 | -17.86 | 81 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.46 | -4.41 | -26.45 | 64 |
| 23 | Daily: Bullish score | daily | 88.75 | -11.25 | 15 | 20.0 | -5.01 | -0.66 | -16.58 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.00 | -3.48 | -14.68 | 85 |
| 25 | Hold BTC | benchmark | 88.71 | -11.29 | 1 | 0.0 | -5.36 | -0.71 | -14.09 | 1 |
| 26 | Agent | meta | 87.95 | -12.05 | 153 | 36.6 | -14.03 | -7.54 | -14.21 | 202 |
| 27 | Parabolic SAR · 1h | trend | 86.90 | -13.10 | 166 | 27.1 | -14.07 | -3.12 | -20.50 | 238 |
| 28 | Donchian 55/20 · 1h | breakout | 85.94 | -14.06 | 71 | 14.1 | -12.75 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.15 | -14.85 | 17 | 47.1 | -32.62 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.37 | -5.50 | -18.65 | 96 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.04 | -17.95 | 261 | 46.7 | -26.04 | -3.87 | -29.25 | 396 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.78 | -3.80 | -21.73 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.38 | -6.78 | -20.94 | 128 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.69 | -4.72 | -24.50 | 173 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.36 | -20.64 | 175 | 18.3 | -23.80 | -3.97 | -27.04 | 260 |
| 38 | MFI reversion · 1h | reversion | 78.52 | -21.48 | 337 | 34.1 | -19.13 | -2.76 | -20.66 | 157 |
| 39 | Ichimoku · 1h | trend | 77.87 | -22.12 | 94 | 14.9 | -22.89 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.42 | -22.59 | 168 | 23.2 | -23.65 | -4.93 | -27.41 | 248 |
| 41 | CCI reversion · 1h | reversion | 76.62 | -23.38 | 290 | 45.9 | -31.38 | -5.19 | -31.96 | 468 |
| 42 | EMA 20/50 cross · 1h | trend | 76.07 | -23.93 | 102 | 10.8 | -23.33 | -4.23 | -30.58 | 130 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -43.45 | -9.21 | -43.48 | 678 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.59 | -5.29 | -29.20 | 209 |
| 45 | Triple EMA stack · 1h | trend | 74.45 | -25.55 | 142 | 14.8 | -28.65 | -6.03 | -33.47 | 203 |
| 46 | Supertrend · 1h | trend | 73.62 | -26.38 | 166 | 13.3 | -30.11 | -5.24 | -34.80 | 216 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -28.09 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.15 | -26.85 | 337 | 23.1 | -36.01 | -6.39 | -38.81 | 482 |
| 49 | Z-score reversion · 1h | reversion | 73.03 | -26.97 | 163 | 35.6 | -25.04 | -3.73 | -27.66 | 229 |
| 50 | Bollinger reversion · 1h | reversion | 72.98 | -27.02 | 251 | 40.2 | -31.28 | -5.37 | -34.52 | 374 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -37.81 | -6.16 | -39.63 | 536 |
| 52 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.93 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.60 | -28.40 | 140 | 20.0 | -29.78 | -5.51 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.15 | -6.14 | -34.09 | 284 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -37.51 | -7.36 | -38.03 | 380 |
| 56 | EMA 9/21 cross · 1h | trend | 67.25 | -32.75 | 242 | 9.9 | -39.30 | -8.13 | -39.40 | 334 |
| 57 | VWAP momentum · 1h | momentum | 66.91 | -33.09 | 782 | 22.0 | -55.57 | -12.33 | -55.59 | 1236 |
| 58 | Agent (ML meta-label) | meta | 66.34 | -33.66 | 1540 | 23.0 | -11.05 | -1.98 | -19.99 | 343 |
| 59 | RSI(14) reversion · 1h | reversion | 66.26 | -33.74 | 143 | 27.3 | -28.88 | -4.53 | -31.54 | 221 |
| 60 | Candlestick reversal · 1h | reversion | 65.35 | -34.65 | 411 | 28.5 | -38.75 | -7.22 | -39.04 | 577 |
| 61 | Three white soldiers | momentum | 64.57 | -35.43 | 469 | 15.6 | -48.67 | -22.97 | -48.70 | 650 |
| 62 | Max aggression: 1-day momentum | meta | 62.21 | -37.79 | 26 | 26.9 | -42.99 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.12 | -98.94 | 5227 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.79 | -25.63 | -80.82 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -47.02 | -93.52 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.26 | -31.62 | -89.26 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.81 | -39.48 | -90.81 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.15 | -32.21 | -90.15 | 2192 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -53.73 | -97.75 | 3483 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -57.01 | -96.32 | 3405 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.82 | -34.05 | -93.82 | 2445 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.45 | -35.10 | -82.45 | 1656 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -54.70 | -99.52 | 5978 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -43.54 | -92.70 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -38.03 | -95.69 | 3413 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.83 | -99.80 | 6195 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -42.67 | -91.87 | 2280 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.11 | -25.19 | -76.17 | 1576 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -63.28 | -97.75 | 3516 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.79 | -61.81 | -98.79 | 4890 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.73 | -29.39 | -69.73 | 1203 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.68 | -54.25 | -94.68 | 2748 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.95 | -37.26 | -84.95 | 1764 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -73.41 | -99.64 | 6380 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.09 | -31.48 | -89.11 | 2286 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.77 | -19.57 | -77.78 | 1749 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.14 | -37.74 | -91.15 | 2231 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.65 | -53.28 | -96.65 | 3888 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -55.11 | -89.54 | 2167 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.73 | -28.34 | -65.73 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.58 | -24.39 | -73.58 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.84 | -18.01 | -78.91 | 1676 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -49.90 | -97.28 | 4335 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -111.86 | -99.93 | 8313 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-07T11:40 | Three white soldiers | buy | SOL-USD | 16.16 | — | entry signal |
| 2026-11-07T11:35 | Three white soldiers | buy | BTC-USD | 16.17 | — | entry signal |
| 2026-11-07T11:15 | Three white soldiers | sell | DOGE-USD | 16.08 | -0.11 | target is flat |
| 2026-11-07T11:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.88 | — | entry signal |
| 2026-11-07T10:45 | Three white soldiers | buy | DOGE-USD | 16.20 | — | entry signal |
| 2026-11-07T10:00 | Three white soldiers · 1h | sell | XRP-USD | 23.31 | -0.22 | exit signal |
| 2026-11-07T10:00 | Candlestick reversal · 1h | sell | SOL-USD | 4.88 | -0.02 | exit signal |
| 2026-11-07T09:05 | Agent | buy | DOGE-USD | 17.61 | — | following Candlestick reversal · 1h |
| 2026-11-07T09:05 | Candlestick reversal · 1h | buy | DOGE-USD | 5.37 | — | entry |
| 2026-11-07T09:00 | CCI reversion · 1h | buy | DOGE-USD | 3.83 | — | entry signal |
| 2026-11-07T09:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.37 | -0.01 | exit signal |
| 2026-11-07T09:00 | Bollinger breakout · 1h | buy | BTC-USD | 19.39 | — | entry signal |
| 2026-11-07T08:50 | Three white soldiers | sell | XRP-USD | 16.20 | -0.04 | exit signal |
| 2026-11-07T08:05 | Agent | sell | DOGE-USD | 17.51 | -0.12 | selected signal exited |
| 2026-11-07T08:05 | Three white soldiers | sell | DOGE-USD | 16.11 | -0.12 | exit signal |
| 2026-11-07T08:00 | Agent | buy | DOGE-USD | 17.63 | — | following Candlestick reversal · 1h |
| 2026-11-07T08:00 | CCI reversion · 1h | sell | BTC-USD | 5.15 | 0.03 | exit signal |
| 2026-11-07T08:00 | Three white soldiers · 1h | buy | XRP-USD | 23.53 | — | entry signal |
| 2026-11-07T08:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 16.82 | — | entry signal |
| 2026-11-07T07:50 | Three white soldiers | buy | DOGE-USD | 16.23 | — | entry |
| 2026-11-07T07:45 | Three white soldiers | buy | XRP-USD | 16.23 | — | entry signal |
| 2026-11-07T07:30 | Three white soldiers | sell | XRP-USD | 16.22 | -0.02 | exit signal |
| 2026-11-07T07:00 | CCI reversion · 1h | buy | XRP-USD | 1.01 | — | entry signal |
| 2026-11-07T07:00 | VWAP momentum · 1h | buy | XRP-USD | 1.14 | — | entry signal |
| 2026-11-07T07:00 | VWAP momentum · 1h | buy | BTC-USD | 6.09 | — | entry signal |
| 2026-11-07T06:00 | CCI reversion · 1h | buy | SOL-USD | 4.04 | — | entry signal |
| 2026-11-07T06:00 | Stochastic reversion · 1h | buy | DOGE-USD | 2.32 | — | entry signal |
| 2026-11-07T06:00 | Bollinger reversion · 1h | buy | XRP-USD | 5.61 | — | entry signal |
| 2026-11-07T06:00 | Bollinger reversion · 1h | buy | DOGE-USD | 5.61 | — | entry signal |
| 2026-11-07T06:00 | VWAP momentum · 1h | buy | ETH-USD | 7.44 | — | entry signal |
| 2026-11-07T05:35 | Three white soldiers | buy | XRP-USD | 16.24 | — | entry signal |
| 2026-11-07T05:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.39 | — | entry signal |
| 2026-11-07T05:00 | VWAP momentum · 1h | sell | ETH-USD | 7.41 | -0.05 | exit signal |
| 2026-11-07T05:00 | MACD cross · 1h | sell | DOGE-USD | 6.57 | 0.01 | exit signal |
| 2026-11-07T04:05 | Three white soldiers | sell | SOL-USD | 16.16 | -0.10 | exit signal |
| 2026-11-07T04:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.00 | -0.04 | exit signal |
| 2026-11-07T04:00 | VWAP momentum · 1h | buy | ETH-USD | 4.95 | — | rebalance up |
| 2026-11-07T04:00 | VWAP momentum · 1h | sell | SOL-USD | 6.66 | -0.05 | exit signal |
| 2026-11-07T04:00 | VWAP momentum · 1h | sell | BTC-USD | 5.55 | -0.04 | exit signal |
| 2026-11-07T04:00 | Three white soldiers | buy | SOL-USD | 16.26 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-09 11:50:05.000116+00:00 -> 2026-11-07 12:00:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-09 11:50:05.000116+00:00 -> 2026-11-07 12:00:05.000116+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-09 11:50:05.000116+00:00 -> 2026-11-07 12:00:05.000116+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
