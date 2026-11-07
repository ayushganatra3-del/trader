# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-07T08:50:05.000133+00:00 · 50686 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.04 (-11.96%)

Closed trades 153, win rate 36.6%, fees £4.52, max drawdown -12.37%.

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

Today: 6882 decisions in 1380 calls, $0.0960 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-07T08:50 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-07T08:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-07T08:50 | 2 / 2 / 1 | ETH-USD 67% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.49 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.16 | -0.84 | 122 | 47.5 | -12.80 | -3.01 | -14.47 | 151 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -6.89 | -3.99 | -10.36 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.58 | -0.44 | -9.18 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 94.09 | -5.91 | 19 | 10.5 | -3.59 | -3.35 | -5.84 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.11 | -0.97 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -15.74 | -5.72 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Hold BTC | benchmark | 88.86 | -11.14 | 1 | 0.0 | -5.07 | -0.68 | -14.09 | 1 |
| 23 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -23.46 | -4.41 | -26.45 | 64 |
| 24 | Daily: Bullish score | daily | 88.76 | -11.23 | 15 | 20.0 | -5.00 | -0.66 | -16.58 | 14 |
| 25 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.54 | -3.67 | -14.68 | 86 |
| 26 | Agent | meta | 88.04 | -11.96 | 153 | 36.6 | -13.93 | -7.48 | -14.05 | 201 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -14.21 | -3.15 | -20.50 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 85.95 | -14.05 | 71 | 14.1 | -13.28 | -2.72 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.37 | -5.50 | -18.65 | 96 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.05 | -17.95 | 261 | 46.7 | -26.01 | -3.86 | -29.25 | 396 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.78 | -3.80 | -21.73 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.38 | -6.78 | -20.94 | 128 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.62 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.37 | -20.63 | 175 | 18.3 | -23.79 | -3.96 | -27.04 | 260 |
| 38 | MFI reversion · 1h | reversion | 78.58 | -21.42 | 337 | 34.1 | -19.40 | -2.82 | -20.96 | 157 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.89 | -4.69 | -29.43 | 125 |
| 40 | Bollinger breakout · 1h | breakout | 77.54 | -22.46 | 168 | 23.2 | -23.59 | -4.91 | -27.32 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.66 | -23.34 | 290 | 45.9 | -31.51 | -5.21 | -32.08 | 468 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -23.52 | -4.27 | -30.58 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -43.29 | -9.16 | -43.43 | 678 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.90 | -5.37 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -28.59 | -6.02 | -33.48 | 203 |
| 46 | Supertrend · 1h | trend | 73.63 | -26.37 | 166 | 13.3 | -30.10 | -5.24 | -34.80 | 216 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -28.11 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.19 | -26.81 | 337 | 23.1 | -36.48 | -6.50 | -38.81 | 485 |
| 49 | Z-score reversion · 1h | reversion | 73.06 | -26.94 | 163 | 35.6 | -25.01 | -3.72 | -27.66 | 229 |
| 50 | Bollinger reversion · 1h | reversion | 73.02 | -26.98 | 251 | 40.2 | -31.24 | -5.36 | -34.52 | 374 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -37.78 | -6.15 | -39.64 | 536 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.92 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.67 | -28.33 | 140 | 20.0 | -29.71 | -5.49 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -29.58 | -6.28 | -33.83 | 285 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -37.82 | -7.40 | -38.33 | 381 |
| 56 | EMA 9/21 cross · 1h | trend | 67.28 | -32.72 | 242 | 9.9 | -39.65 | -8.22 | -39.77 | 335 |
| 57 | VWAP momentum · 1h | momentum | 66.94 | -33.06 | 782 | 22.0 | -55.58 | -12.31 | -55.61 | 1237 |
| 58 | Agent (ML meta-label) | meta | 66.34 | -33.66 | 1540 | 23.0 | -11.40 | -1.77 | -20.27 | 329 |
| 59 | RSI(14) reversion · 1h | reversion | 66.30 | -33.70 | 143 | 27.3 | -28.80 | -4.52 | -31.54 | 219 |
| 60 | Candlestick reversal · 1h | reversion | 65.44 | -34.56 | 409 | 28.6 | -38.05 | -7.04 | -38.52 | 572 |
| 61 | Three white soldiers | momentum | 64.78 | -35.22 | 468 | 15.6 | -48.72 | -23.01 | -48.75 | 646 |
| 62 | Max aggression: 1-day momentum | meta | 62.24 | -37.76 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -45.77 | -98.94 | 5227 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.67 | -25.32 | -80.71 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -46.37 | -93.51 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.20 | -31.31 | -89.23 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.80 | -39.07 | -90.80 | 2307 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.14 | -32.18 | -90.14 | 2192 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -53.00 | -97.74 | 3483 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -55.72 | -96.29 | 3395 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.77 | -33.82 | -93.77 | 2444 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.41 | -35.03 | -82.41 | 1655 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.50 | -53.73 | -99.50 | 5971 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -43.08 | -92.71 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -37.93 | -95.68 | 3410 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.35 | -99.80 | 6194 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -42.46 | -91.88 | 2280 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.11 | -25.24 | -76.20 | 1578 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -62.50 | -97.74 | 3514 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -60.36 | -98.78 | 4883 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.78 | -29.24 | -69.80 | 1204 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -53.48 | -94.67 | 2749 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.98 | -37.10 | -85.00 | 1766 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -71.62 | -99.64 | 6377 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.22 | -31.19 | -89.23 | 2292 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.68 | -19.54 | -77.71 | 1744 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.19 | -37.65 | -91.19 | 2235 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.62 | -52.38 | -96.62 | 3882 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -53.41 | -89.52 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.80 | -28.38 | -65.80 | 801 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.44 | -24.17 | -73.46 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.71 | -18.17 | -78.76 | 1673 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -49.15 | -97.25 | 4329 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -107.12 | -99.93 | 8308 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-07T03:35 | CCI reversion · 1h | sell | XRP-USD | 3.93 | -0.11 | stop-loss |
| 2026-11-07T03:35 | Stochastic reversion · 1h | sell | XRP-USD | 2.32 | -0.06 | stop-loss |
| 2026-11-07T03:35 | VWAP reversion · 1h | sell | XRP-USD | 24.26 | -0.71 | stop-loss |
| 2026-11-07T03:20 | Z-score reversion · 1h | sell | XRP-USD | 4.18 | -0.10 | stop-loss |
| 2026-11-07T03:00 | Agent | sell | DOGE-USD | 17.52 | -0.14 | selected signal exited |
| 2026-11-07T02:35 | MFI reversion · 1h | sell | XRP-USD | 7.09 | -0.19 | stop-loss |
| 2026-11-07T02:35 | MACD cross · 1h | sell | XRP-USD | 6.53 | -0.19 | stop-loss |
| 2026-11-07T02:25 | Three white soldiers | sell | SOL-USD | 16.18 | -0.11 | exit signal |
| 2026-11-07T02:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.04 | — | entry |
| 2026-11-07T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.42 | 0.00 | exit signal |
| 2026-11-07T02:00 | Bollinger breakout · 1h | buy | ETH-USD | 19.40 | — | entry signal |
| 2026-11-07T02:00 | VWAP momentum · 1h | buy | ETH-USD | 2.51 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-09 08:50:05.000133+00:00 -> 2026-11-07 09:00:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-09 08:50:05.000133+00:00 -> 2026-11-07 09:00:05.000133+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-09 08:50:05.000133+00:00 -> 2026-11-07 09:00:05.000133+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
