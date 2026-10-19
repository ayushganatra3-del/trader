# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T21:25:05.000109+00:00 · 28780 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, APLD 12%, FLSC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 18.40 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 35934 decisions in 3069 calls, $0.4452 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T21:25 | 2 / 2 / 1 | SOL-USD 16%, DOGE-USD 14% |  |
| Breezy | 2026-10-19T21:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T21:25 | 3 / 2 / 0 | ETH-USD 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |
| VWAP reversion | BITX | 1.52 | +2.60% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.86 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.09 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.16 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.08 | 5.08 | 0 | — | 5.36 | 2.60 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.07 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.97 | -0.03 | 0 | — | 2.38 | 1.01 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.22 | -0.78 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.05 | -3.91 | 21 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.35 | -1.65 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.70 | -2.17 | 63 |
| 13 | Donchian 55/20 · 1h | breakout | 97.71 | -2.29 | 36 | 16.7 | -11.12 | -2.07 | -18.86 | 100 |
| 14 | Hold BTC | benchmark | 97.56 | -2.44 | 0 | — | 26.66 | 3.19 | -8.68 | 1 |
| 15 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.15 | -0.80 | -5.10 | 288 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.41 | -2.59 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.29 | -5.83 | 1 |
| 18 | Trend pullback · 1h | trend | 96.53 | -3.47 | 88 | 23.9 | -19.67 | -5.82 | -20.57 | 137 |
| 19 | Copy: Insider buying | copy | 96.51 | -3.49 | 23 | 43.5 | -14.93 | -2.72 | -20.62 | 73 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.45 | -3.55 | 0 | — | -5.86 | -2.34 | -7.04 | 1 |
| 21 | Max aggression: 5-day momentum | meta | 95.48 | -4.52 | 8 | 37.5 | -20.05 | -1.70 | -34.64 | 26 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.91 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 93.70 | -6.30 | 88 | 18.2 | -14.55 | -2.67 | -16.51 | 259 |
| 24 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.54 | 2.18 | -6.51 | 199 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.97 | -7.03 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.05 | -7.95 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Parabolic SAR · 1h | trend | 91.91 | -8.09 | 102 | 22.5 | -14.22 | -2.72 | -24.65 | 267 |
| 29 | Volume breakout · 1h | breakout | 91.91 | -8.09 | 78 | 23.1 | -12.73 | -2.29 | -16.76 | 107 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.46 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.79 | -17.26 | 557 |
| 32 | Bollinger breakout · 1h | breakout | 90.80 | -9.20 | 84 | 28.6 | -8.66 | -1.46 | -16.89 | 256 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -6.19 | -2.22 | -18.06 | 251 |
| 34 | EMA 20/50 cross · 1h | trend | 90.51 | -9.49 | 58 | 13.8 | -18.92 | -3.40 | -21.31 | 126 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.15 | -9.86 | 0 | — | 0.78 | 0.29 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.96 | -10.04 | 79 | 16.5 | -19.09 | -3.09 | -30.20 | 212 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.62 | -23.86 | 205 |
| 38 | Ichimoku · 1h | trend | 88.80 | -11.20 | 55 | 14.5 | -17.45 | -3.31 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.34 | -11.66 | 152 | 46.1 | -17.09 | -2.98 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -5.42 | -1.41 | -20.91 | 126 |
| 41 | Keltner breakout · 1h | breakout | 87.73 | -12.27 | 56 | 23.2 | -11.96 | -1.69 | -26.96 | 201 |
| 42 | Triple EMA stack · 1h | trend | 87.73 | -12.27 | 85 | 15.3 | -22.51 | -3.35 | -32.98 | 230 |
| 43 | Supertrend · 1h | trend | 87.56 | -12.44 | 86 | 12.8 | -22.76 | -4.69 | -26.48 | 214 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.72 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 86.06 | -13.94 | 189 | 20.6 | -26.34 | -4.96 | -32.78 | 470 |
| 46 | OBV trend · 1h | momentum | 85.46 | -14.54 | 180 | 17.8 | -24.43 | -3.35 | -35.99 | 312 |
| 47 | Z-score reversion · 1h | reversion | 85.26 | -14.74 | 91 | 30.8 | -14.19 | -2.35 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.73 | -15.27 | 209 | 31.1 | -17.09 | -2.68 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.25 | -15.76 | 87 | 14.9 | -24.79 | -4.93 | -25.19 | 217 |
| 50 | Donchian 20/10 · 1h | breakout | 84.00 | -16.00 | 81 | 17.3 | -8.03 | -0.83 | -27.92 | 214 |
| 51 | Agent (ML meta-label) | meta | 83.90 | -16.10 | 681 | 18.8 | -11.26 | -2.02 | -16.21 | 349 |
| 52 | Bollinger reversion · 1h | reversion | 82.86 | -17.14 | 158 | 34.8 | -27.80 | -5.35 | -33.53 | 349 |
| 53 | Max aggression: 1-day momentum | meta | 82.61 | -17.39 | 15 | 33.3 | -15.83 | -0.60 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 82.52 | -17.48 | 231 | 19.0 | -47.27 | -18.95 | -47.56 | 603 |
| 55 | Williams %R · 1h | reversion | 82.05 | -17.95 | 182 | 42.9 | -33.23 | -5.32 | -36.50 | 531 |
| 56 | ROC + volume · 1h | momentum | 81.49 | -18.51 | 197 | 20.8 | -20.51 | -2.99 | -33.90 | 387 |
| 57 | CCI reversion · 1h | reversion | 80.74 | -19.26 | 163 | 39.3 | -17.87 | -2.25 | -27.44 | 442 |
| 58 | EMA 9/21 cross · 1h | trend | 80.31 | -19.69 | 135 | 11.1 | -29.20 | -6.09 | -29.53 | 314 |
| 59 | RSI(14) reversion · 1h | reversion | 80.19 | -19.81 | 75 | 21.3 | -20.45 | -3.67 | -25.21 | 170 |
| 60 | Heikin-Ashi · 1h | trend | 78.97 | -21.03 | 224 | 21.4 | -36.38 | -6.00 | -44.79 | 679 |
| 61 | VWAP momentum · 1h | momentum | 77.98 | -22.02 | 433 | 20.8 | -42.20 | -7.33 | -48.27 | 1244 |
| 62 | Candlestick reversal · 1h | reversion | 77.16 | -22.84 | 214 | 27.6 | -36.66 | -6.61 | -37.63 | 529 |
| 63 | ROC + volume | momentum | 61.91 | -38.09 | 594 | 22.4 | -75.91 | -18.01 | -78.08 | 1730 |
| 64 | Volume breakout | breakout | 61.54 | -38.46 | 358 | 13.1 | -62.63 | -18.00 | -64.20 | 876 |
| 65 | Squeeze breakout | breakout | 60.42 | -39.59 | 467 | 14.1 | -63.88 | -20.55 | -65.59 | 1203 |
| 66 | Donchian 55/20 | breakout | 59.10 | -40.90 | 475 | 18.5 | -67.96 | -13.71 | -72.83 | 1264 |
| 67 | RSI(14) reversion | reversion | 58.17 | -41.84 | 707 | 25.2 | -74.73 | -16.80 | -74.97 | 1601 |
| 68 | EMA 20/50 cross | trend | 56.77 | -43.23 | 512 | 19.9 | -75.10 | -13.60 | -80.29 | 1424 |
| 69 | VWAP reversion | reversion | 53.67 | -46.33 | 748 | 25.1 | -71.95 | -14.93 | -72.51 | 1499 |
| 70 | Keltner breakout | breakout | 51.12 | -48.88 | 672 | 16.2 | -82.39 | -25.40 | -83.49 | 1806 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -29.91 | -98.66 | 5272 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.05 | -28.18 | -93.70 | 2563 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -85.97 | -19.05 | -88.15 | 1894 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.78 | -22.71 | -91.10 | 2345 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.98 | -26.07 | -91.08 | 2260 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -31.37 | -97.55 | 3497 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -34.11 | -96.71 | 3567 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -28.45 | -94.45 | 2512 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.02 | -25.21 | -82.93 | 1696 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.99 | -99.37 | 5738 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.92 | -24.01 | -92.00 | 2623 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -32.33 | -96.12 | 3470 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.78 | -99.74 | 6188 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -30.01 | -91.69 | 2334 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.49 | -36.78 | -97.62 | 3627 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -37.31 | -98.46 | 4691 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -33.27 | -93.93 | 2800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.87 | -99.52 | 6157 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.64 | -86.86 | 2133 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.92 | -27.21 | -87.94 | 2135 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.82 | -32.89 | -95.83 | 3735 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.92 | -32.88 | -89.08 | 2094 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -34.09 | -95.72 | 4101 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.60 | -99.90 | 8280 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T21:25 | EMA 20/50 cross | buy | XRP-USD | 5.74 | — | entry signal |
| 2026-10-19T21:25 | EMA 20/50 cross | sell | SOL-USD | 2.85 | -0.01 | rebalance down |
| 2026-10-19T21:25 | EMA 20/50 cross | sell | DOGE-USD | 2.83 | -0.01 | rebalance down |
| 2026-10-19T21:20 | EMA 20/50 cross | buy | ETH-USD | 14.19 | — | entry signal |
| 2026-10-19T21:15 | VWAP reversion | sell | DOGE-USD | 10.76 | 0.03 | exit signal |
| 2026-10-19T21:15 | Volume breakout | buy | BTC-USD | 15.40 | — | entry signal |
| 2026-10-19T21:15 | Squeeze breakout | buy | BTC-USD | 15.12 | — | entry signal |
| 2026-10-19T21:15 | Donchian 55/20 | buy | SOL-USD | 14.80 | — | entry signal |
| 2026-10-19T21:15 | Donchian 55/20 | buy | BTC-USD | 14.80 | — | entry signal |
| 2026-10-19T21:15 | EMA 20/50 cross | buy | BTC-USD | 14.22 | — | entry signal |
| 2026-10-19T21:00 | OBV trend · 1h | buy | SOL-USD | 12.82 | — | entry signal |
| 2026-10-19T20:30 | EMA 20/50 cross | buy | SOL-USD | 14.21 | — | entry signal |
| 2026-10-19T20:15 | EMA 20/50 cross | buy | DOGE-USD | 14.22 | — | entry signal |
| 2026-10-19T20:00 | MFI reversion · 1h | buy | DOGE-USD | 21.14 | — | entry signal |
| 2026-10-19T20:00 | OBV trend · 1h | sell | XRP-USD | 12.82 | -0.09 | exit signal |
| 2026-10-19T20:00 | RSI momentum · 1h | sell | BTC-USD | 12.85 | -0.09 | exit signal |
| 2026-10-19T20:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 6.66 | — | rebalance up |
| 2026-10-19T20:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 6.63 | — | rebalance up |
| 2026-10-19T19:55 | Day trade: Stocks in Play ORB | sell | AMZN | 24.89 | 0.44 | target is flat |
| 2026-10-19T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 98.40 | -0.69 | target is flat |
| 2026-10-19T19:55 | Agent (ML meta-label) | buy | QQQ | 5.24 | — | entry |
| 2026-10-19T19:55 | Agent (aggressive) | sell | SQQQ | 88.03 | 0.49 | selected signal exited |
| 2026-10-19T19:55 | Agent | sell | SQQQ | 36.41 | 0.20 | selected signal exited |
| 2026-10-19T19:55 | Agent | sell | BITX | 18.01 | -0.09 | selected signal exited |
| 2026-10-19T19:55 | VWAP reversion | sell | MSTR | 8.93 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | VWAP reversion | sell | BITX | 10.71 | -0.05 | end-of-day flatten |
| 2026-10-19T19:55 | VWAP reversion | sell | AMD | 8.08 | 0.00 | end-of-day flatten |
| 2026-10-19T19:55 | RSI(14) reversion | sell | MSTR | 14.40 | -0.12 | end-of-day flatten |
| 2026-10-19T19:55 | Three white soldiers | sell | NVDA | 20.55 | -0.11 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | UPRO | 6.72 | -0.03 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | TSLA | 6.72 | -0.04 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | TQQQ | 6.67 | -0.07 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | TNA | 6.73 | -0.03 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | SPY | 6.74 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | QQQ | 6.73 | -0.03 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | NVDA | 6.72 | -0.04 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | GOOGL | 6.73 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | Squeeze breakout | sell | AMZN | 6.73 | -0.02 | end-of-day flatten |
| 2026-10-19T19:55 | Keltner breakout | sell | TECL | 10.20 | -0.12 | end-of-day flatten |
| 2026-10-19T19:55 | Keltner breakout | sell | SOXL | 10.08 | -0.23 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 21:25:05.000109+00:00 -> 2026-10-19 21:35:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
