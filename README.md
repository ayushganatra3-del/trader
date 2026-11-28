# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-28T11:35:05.000119+00:00 · 76703 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £75.26 (-24.74%)

Closed trades 253, win rate 35.6%, fees £6.93, max drawdown -25.09%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.18 | -0.11 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-27 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-27)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 33.34 · VIX 23.81 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.6, TSLA 6.2, SQQQ 6.0, LABU 3.9, META 3.7, PLTR 2.9

### AI bees (Jev: typesafe/jev-1.13)

Today: 9399 decisions in 1881 calls, $0.1314 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-28T11:35 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-28T11:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-28T11:35 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Triple EMA stack | AMD | 1.76 | +10.39% | 4 |
| Connors RSI(2) | TNA | 1.75 | +0.78% | 6 |
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| Opening range 30m | AMD | 1.64 | +5.77% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.21 | 3.62 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.61 | 16.61 | 0 | — | 15.04 | 5.08 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.12 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 106.19 | 6.19 | 0 | — | 4.92 | 1.36 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.45 | -1.54 | 225 | 31.6 | 0.20 | 0.15 | -7.66 | 213 |
| 9 | Three white soldiers · 1h | momentum | 95.81 | -4.19 | 24 | 12.5 | -2.31 | -1.74 | -6.24 | 25 |
| 10 | Hold SPY | benchmark | 95.80 | -4.20 | 0 | — | -4.97 | -1.22 | -11.71 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 95.26 | -4.74 | 172 | 32.6 | -4.54 | -3.93 | -5.85 | 54 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.86 | -7.38 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 95.19 | -4.81 | 0 | — | -4.63 | -0.85 | -13.24 | 1 |
| 14 | Agent (rotation) | meta | 95.15 | -4.85 | 236 | 28.8 | 1.63 | 0.60 | -5.01 | 157 |
| 15 | Copy: Insider buying | copy | 94.72 | -5.28 | 64 | 42.2 | -0.62 | 0.04 | -14.79 | 69 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.59 | -9.41 | 0 | — | -10.32 | -2.18 | -17.03 | 1 |
| 17 | Trend pullback · 1h | trend | 90.22 | -9.78 | 118 | 23.7 | -5.81 | -4.12 | -7.66 | 23 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.47 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 88.10 | -11.90 | 490 | 33.9 | -7.93 | -2.35 | -15.30 | 553 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.94 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.56 | -15.44 | 174 | 44.8 | -13.19 | -2.46 | -20.49 | 153 |
| 22 | Daily: Bullish score | daily | 84.13 | -15.87 | 20 | 20.0 | -14.90 | -3.35 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.01 | -6.08 | -17.05 | 79 |
| 25 | Opening range 15m | breakout | 79.85 | -20.15 | 618 | 31.9 | -17.41 | -4.79 | -24.20 | 679 |
| 26 | Connors RSI(2) · 1h | reversion | 78.05 | -21.95 | 230 | 41.3 | -14.97 | -6.84 | -15.22 | 61 |
| 27 | Volume breakout · 1h | breakout | 76.81 | -23.19 | 181 | 30.4 | -21.66 | -8.68 | -21.70 | 69 |
| 28 | Parabolic SAR · 1h | trend | 76.61 | -23.39 | 221 | 27.1 | -30.11 | -7.50 | -32.36 | 181 |
| 29 | Max aggression: 5-day momentum | meta | 76.49 | -23.51 | 27 | 37.0 | -51.07 | -2.49 | -67.33 | 21 |
| 30 | Agent (aggressive) | meta | 75.56 | -24.44 | 115 | 33.0 | -14.83 | -4.16 | -15.34 | 83 |
| 31 | Agent | meta | 75.26 | -24.74 | 253 | 35.6 | -27.16 | -6.14 | -27.16 | 192 |
| 32 | Keltner breakout · 1h | breakout | 73.06 | -26.94 | 147 | 23.8 | -26.29 | -6.52 | -27.60 | 151 |
| 33 | Donchian 55/20 · 1h | breakout | 73.06 | -26.95 | 93 | 12.9 | -30.36 | -8.11 | -30.69 | 81 |
| 34 | Ichimoku · 1h | trend | 72.91 | -27.09 | 119 | 15.1 | -28.33 | -7.21 | -29.43 | 98 |
| 35 | Daily: Momentum burst | daily | 71.69 | -28.31 | 31 | 16.1 | -31.57 | -4.30 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.32 | -28.68 | 274 | 19.7 | -36.89 | -6.91 | -39.61 | 278 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 70.22 | -29.78 | 3 | 0.0 | -22.00 | -2.60 | -33.66 | 1 |
| 38 | Stochastic reversion · 1h | reversion | 68.90 | -31.10 | 418 | 40.7 | -29.56 | -2.95 | -42.39 | 428 |
| 39 | Hold BTC | benchmark | 68.40 | -31.60 | 3 | 0.0 | -30.69 | -5.39 | -36.10 | 1 |
| 40 | Supertrend · 1h | trend | 68.36 | -31.64 | 225 | 18.7 | -38.20 | -7.35 | -41.52 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.73 | -32.27 | 220 | 23.2 | -29.95 | -7.87 | -31.73 | 211 |
| 42 | Max aggression: 1-day momentum | meta | 65.99 | -34.01 | 35 | 28.6 | -56.20 | -3.63 | -63.62 | 38 |
| 43 | OBV trend · 1h | momentum | 65.70 | -34.30 | 336 | 19.3 | -39.49 | -9.95 | -39.49 | 214 |
| 44 | EMA 20/50 cross · 1h | trend | 64.95 | -35.05 | 129 | 9.3 | -37.56 | -10.64 | -37.67 | 116 |
| 45 | MACD zero-line · 1h | trend | 64.86 | -35.14 | 206 | 16.5 | -35.00 | -9.11 | -37.58 | 189 |
| 46 | Triple EMA stack · 1h | trend | 64.77 | -35.23 | 177 | 15.3 | -40.08 | -10.00 | -40.80 | 162 |
| 47 | RSI momentum · 1h | momentum | 63.68 | -36.32 | 208 | 15.4 | -40.91 | -8.85 | -42.16 | 189 |
| 48 | MFI reversion · 1h | reversion | 63.45 | -36.55 | 529 | 33.8 | -31.87 | -4.69 | -38.15 | 195 |
| 49 | Donchian 20/10 · 1h | breakout | 63.03 | -36.97 | 188 | 17.0 | -37.68 | -8.15 | -40.87 | 198 |
| 50 | Heikin-Ashi · 1h | trend | 61.58 | -38.42 | 571 | 21.9 | -46.95 | -9.06 | -49.05 | 640 |
| 51 | ROC + volume · 1h | momentum | 61.41 | -38.59 | 477 | 26.8 | -38.38 | -7.39 | -40.02 | 339 |
| 52 | EMA 9/21 cross · 1h | trend | 59.65 | -40.35 | 318 | 12.9 | -43.70 | -9.79 | -46.72 | 312 |
| 53 | MACD cross · 1h | trend | 58.78 | -41.22 | 502 | 20.9 | -50.98 | -9.67 | -55.13 | 501 |
| 54 | Agent (ML meta-label) | meta | 55.43 | -44.57 | 2076 | 25.4 | -19.58 | -2.44 | -26.72 | 317 |
| 55 | CCI reversion · 1h | reversion | 53.63 | -46.37 | 469 | 38.6 | -49.49 | -7.78 | -55.11 | 493 |
| 56 | Bollinger reversion · 1h | reversion | 51.92 | -48.08 | 408 | 36.8 | -39.14 | -4.70 | -45.50 | 427 |
| 57 | VWAP momentum · 1h | momentum | 51.84 | -48.16 | 1128 | 21.4 | -58.94 | -12.32 | -60.30 | 1178 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.00 | -9.00 | -59.06 | 687 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -54.94 | -8.96 | -59.48 | 592 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.09 | -43.49 | -99.10 | 5340 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.34 | -31.24 | -83.34 | 1401 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.80 | -43.08 | -93.85 | 2371 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.80 | -29.46 | -89.92 | 1854 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.75 | -34.68 | -91.08 | 2198 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.04 | -26.19 | -88.19 | 1916 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.04 | -45.97 | -98.04 | 3357 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -49.46 | -96.84 | 3359 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.05 | -34.83 | -93.06 | 2075 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.23 | -33.82 | -81.51 | 1512 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.70 | -56.57 | -99.70 | 6253 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.53 | -36.40 | -92.55 | 2458 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.19 | -35.43 | -94.21 | 3116 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -65.09 | -99.81 | 6023 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.61 | -40.74 | -92.63 | 2218 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.97 | -18.94 | -50.77 | 650 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.45 | -22.80 | -77.69 | 1605 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -53.74 | -97.54 | 3195 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -58.52 | -99.13 | 5065 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.90 | -22.97 | -69.30 | 1204 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.38 | -44.56 | -94.38 | 2640 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.34 | -5.85 | -51.27 | 285 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.70 | -32.01 | -84.23 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.20 | -99.76 | 6466 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.64 | -31.45 | -91.64 | 2466 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.18 | -20.36 | -83.19 | 1963 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.22 | -32.85 | -91.22 | 2132 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.17 | -48.38 | -98.17 | 4010 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.78 | -43.64 | -89.78 | 2177 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.49 | -28.54 | -67.49 | 778 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.12 | -25.91 | -72.55 | 1156 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.70 | -19.41 | -84.70 | 1833 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.04 | -49.46 | -98.04 | 4362 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -102.28 | -99.94 | 8250 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -43.41 | -6.01 | -52.60 | 299 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-28T11:00 | Stochastic reversion · 1h | buy | DOGE-USD | 17.23 | — | entry signal |
| 2026-11-28T10:50 | Donchian 55/20 · 1h | sell | DOGE-USD | 12.07 | -0.13 | stop-loss |
| 2026-11-28T10:45 | Donchian 55/20 · 1h | buy | DOGE-USD | 12.20 | — | entry |
| 2026-11-28T10:40 | Donchian 55/20 · 1h | sell | DOGE-USD | 14.36 | -0.30 | stop-loss |
| 2026-11-28T10:00 | VWAP reversion · 1h | buy | XRP-USD | 21.17 | — | entry signal |
| 2026-11-28T09:00 | OBV trend · 1h | sell | SOL-USD | 10.84 | -0.25 | exit signal |
| 2026-11-28T09:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 10.83 | -0.14 | exit signal |
| 2026-11-28T06:00 | Connors RSI(2) · 1h | buy | XRP-USD | 19.63 | — | entry signal |
| 2026-11-28T06:00 | Connors RSI(2) · 1h | buy | SOL-USD | 19.63 | — | entry signal |
| 2026-11-28T06:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 19.63 | — | entry signal |
| 2026-11-28T06:00 | Trend pullback · 1h | sell | DOGE-USD | 22.16 | -0.53 | exit signal |
| 2026-11-28T05:00 | OBV trend · 1h | sell | DOGE-USD | 4.72 | -0.05 | target is flat |
| 2026-11-28T05:00 | Triple EMA stack · 1h | sell | DOGE-USD | 16.05 | -0.01 | exit signal |
| 2026-11-28T05:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 6.58 | 0.14 | exit signal |
| 2026-11-28T04:40 | OBV trend · 1h | buy | DOGE-USD | 4.78 | — | entry |
| 2026-11-28T04:30 | OBV trend · 1h | sell | DOGE-USD | 4.78 | -0.03 | target is flat |
| 2026-11-28T04:05 | OBV trend · 1h | buy | DOGE-USD | 4.81 | — | entry |
| 2026-11-28T04:05 | OBV trend · 1h | sell | SOL-USD | 4.81 | -0.06 | rebalance down |
| 2026-11-28T04:00 | Heikin-Ashi · 1h | sell | XRP-USD | 3.21 | -0.03 | exit signal |
| 2026-11-28T04:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.21 | -0.04 | exit signal |
| 2026-11-28T02:00 | Connors RSI(2) · 1h | sell | SOL-USD | 19.69 | 0.06 | exit signal |
| 2026-11-28T02:00 | OBV trend · 1h | buy | SOL-USD | 15.95 | — | entry signal |
| 2026-11-28T02:00 | Heikin-Ashi · 1h | buy | XRP-USD | 3.24 | — | entry signal |
| 2026-11-28T02:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.24 | — | entry signal |
| 2026-11-28T00:00 | MFI reversion · 1h | buy | XRP-USD | 5.61 | — | entry signal |
| 2026-11-28T00:00 | Connors RSI(2) · 1h | sell | XRP-USD | 19.59 | -0.04 | exit signal |
| 2026-11-27T23:00 | Connors RSI(2) · 1h | buy | XRP-USD | 19.63 | — | entry signal |
| 2026-11-27T23:00 | Connors RSI(2) · 1h | buy | SOL-USD | 19.63 | — | entry signal |
| 2026-11-27T21:00 | OBV trend · 1h | sell | DOGE-USD | 15.95 | -0.13 | exit signal |
| 2026-11-27T21:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 6.57 | 0.12 | exit signal |
| 2026-11-27T20:00 | CCI reversion · 1h | buy | ETH-USD | 4.37 | — | entry signal |
| 2026-11-27T20:00 | CCI reversion · 1h | buy | BTC-USD | 4.48 | — | entry signal |
| 2026-11-27T20:00 | Triple EMA stack · 1h | buy | DOGE-USD | 5.39 | — | rebalance up |
| 2026-11-27T20:00 | Triple EMA stack · 1h | sell | SOL-USD | 10.82 | 0.11 | exit signal |
| 2026-11-27T19:00 | Connors RSI(2) · 1h | sell | XRP-USD | 19.89 | 0.16 | exit signal |
| 2026-11-27T18:03 | Copy: Insider buying | buy | COHR | 11.21 | — | entry |
| 2026-11-27T18:03 | Copy: Insider buying | sell | PAM | 11.21 | 0.23 | target is flat |
| 2026-11-27T18:01 | Agent | sell | SQQQ | 14.68 | -0.48 | selected signal exited |
| 2026-11-27T18:01 | Connors RSI(2) · 1h | sell | DOGE-USD | 20.04 | 0.31 | exit signal |
| 2026-11-27T18:01 | OBV trend · 1h | buy | DOGE-USD | 16.08 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-30 11:35:05.000119+00:00 -> 2026-11-28 11:45:05.000119+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
