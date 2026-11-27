# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T16:34:05.000130+00:00 · 75698 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £75.69 (-24.31%)

Closed trades 251, win rate 35.9%, fees £6.91, max drawdown -24.66%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.08 | -0.20 |
| SQQQ | 15.09 | -0.06 |

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

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 19611 decisions in 2604 calls, $0.2551 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T16:34 | 10 / 19 / 1 | PLTR 15% |  |
| Breezy | 2026-11-27T16:34 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-27T16:34 | 8 / 21 / 1 | COIN 69% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.21 | 3.56 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.29 | 16.29 | 0 | — | 14.78 | 4.92 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.62 | 5.62 | 0 | — | 4.40 | 1.22 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.36 | -1.64 | 222 | 31.1 | 0.19 | 0.15 | -7.66 | 213 |
| 9 | Three white soldiers · 1h | momentum | 95.46 | -4.54 | 24 | 12.5 | -3.07 | -2.51 | -6.52 | 26 |
| 10 | Hold SPY | benchmark | 95.30 | -4.70 | 0 | — | -5.41 | -1.33 | -11.71 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.03 | -4.96 | 0 | — | -4.74 | -0.86 | -13.24 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 94.88 | -5.12 | 172 | 32.6 | -4.89 | -4.18 | -5.85 | 54 |
| 14 | Agent (rotation) | meta | 94.78 | -5.22 | 233 | 28.3 | 0.98 | 0.39 | -6.10 | 184 |
| 15 | Copy: Insider buying | copy | 93.71 | -6.29 | 63 | 41.3 | -3.13 | -0.45 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 90.76 | -9.24 | 117 | 23.9 | -6.97 | -4.58 | -9.32 | 26 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.32 | -9.68 | 0 | — | -10.54 | -2.21 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Opening range 30m | breakout | 87.29 | -12.71 | 490 | 33.9 | -8.85 | -2.66 | -15.30 | 545 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.69 | -15.31 | 20 | 20.0 | -14.32 | -3.17 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.42 | -6.03 | -17.45 | 79 |
| 25 | Opening range 15m | breakout | 79.14 | -20.86 | 618 | 31.9 | -18.23 | -5.01 | -24.20 | 671 |
| 26 | Connors RSI(2) · 1h | reversion | 78.98 | -21.02 | 226 | 40.7 | -14.09 | -6.49 | -14.49 | 63 |
| 27 | Volume breakout · 1h | breakout | 76.64 | -23.36 | 180 | 30.0 | -21.63 | -8.52 | -21.72 | 71 |
| 28 | Parabolic SAR · 1h | trend | 76.26 | -23.74 | 221 | 27.1 | -31.29 | -7.75 | -33.18 | 183 |
| 29 | Agent | meta | 75.69 | -24.31 | 251 | 35.9 | -26.92 | -5.98 | -27.24 | 209 |
| 30 | Max aggression: 5-day momentum | meta | 75.60 | -24.40 | 27 | 37.0 | -51.62 | -2.51 | -67.33 | 21 |
| 31 | Agent (aggressive) | meta | 75.32 | -24.68 | 115 | 33.0 | -15.38 | -4.24 | -16.35 | 92 |
| 32 | Donchian 55/20 · 1h | breakout | 73.26 | -26.74 | 91 | 13.2 | -30.75 | -8.07 | -31.22 | 81 |
| 33 | Ichimoku · 1h | trend | 72.69 | -27.31 | 119 | 15.1 | -29.56 | -7.43 | -30.49 | 100 |
| 34 | Keltner breakout · 1h | breakout | 72.65 | -27.35 | 147 | 23.8 | -26.88 | -6.59 | -27.80 | 152 |
| 35 | Daily: Momentum burst | daily | 71.47 | -28.53 | 31 | 16.1 | -31.80 | -4.27 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 71.18 | -28.82 | 274 | 19.7 | -38.38 | -7.17 | -40.51 | 283 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 69.78 | -30.22 | 3 | 0.0 | -22.44 | -2.64 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 69.40 | -30.60 | 3 | 0.0 | -28.83 | -5.04 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.59 | -31.41 | 418 | 40.7 | -30.32 | -3.01 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 68.17 | -31.83 | 225 | 18.7 | -38.52 | -7.35 | -41.52 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.46 | -32.54 | 220 | 23.2 | -30.16 | -7.79 | -31.70 | 211 |
| 42 | OBV trend · 1h | momentum | 65.99 | -34.01 | 332 | 19.6 | -40.05 | -9.69 | -40.38 | 214 |
| 43 | EMA 20/50 cross · 1h | trend | 65.42 | -34.58 | 128 | 9.4 | -38.42 | -10.39 | -38.96 | 119 |
| 44 | Triple EMA stack · 1h | trend | 64.81 | -35.19 | 174 | 14.9 | -40.36 | -9.92 | -41.27 | 164 |
| 45 | MACD zero-line · 1h | trend | 64.58 | -35.41 | 206 | 16.5 | -35.36 | -9.15 | -37.39 | 188 |
| 46 | MFI reversion · 1h | reversion | 63.63 | -36.37 | 529 | 33.8 | -31.65 | -4.56 | -38.15 | 194 |
| 47 | RSI momentum · 1h | momentum | 63.24 | -36.76 | 208 | 15.4 | -41.77 | -8.94 | -42.76 | 191 |
| 48 | Max aggression: 1-day momentum | meta | 63.21 | -36.79 | 35 | 28.6 | -58.03 | -3.93 | -63.62 | 38 |
| 49 | Donchian 20/10 · 1h | breakout | 62.70 | -37.30 | 188 | 17.0 | -37.97 | -8.15 | -40.84 | 196 |
| 50 | Heikin-Ashi · 1h | trend | 61.19 | -38.81 | 569 | 22.0 | -48.25 | -9.38 | -49.90 | 645 |
| 51 | ROC + volume · 1h | momentum | 60.90 | -39.10 | 477 | 26.8 | -39.76 | -7.64 | -40.85 | 345 |
| 52 | EMA 9/21 cross · 1h | trend | 59.49 | -40.51 | 315 | 12.1 | -43.91 | -9.74 | -46.70 | 309 |
| 53 | MACD cross · 1h | trend | 58.31 | -41.69 | 502 | 20.9 | -53.04 | -10.12 | -55.83 | 508 |
| 54 | Agent (ML meta-label) | meta | 55.42 | -44.58 | 2076 | 25.4 | -24.54 | -3.15 | -29.92 | 301 |
| 55 | CCI reversion · 1h | reversion | 53.27 | -46.73 | 468 | 38.5 | -50.82 | -8.06 | -55.11 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 52.23 | -47.77 | 408 | 36.8 | -39.83 | -4.74 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.32 | -48.69 | 1127 | 21.3 | -60.44 | -12.67 | -61.80 | 1181 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.64 | -9.29 | -59.72 | 687 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.54 | -8.95 | -59.48 | 596 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -42.70 | -99.15 | 5331 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.20 | -29.32 | -83.38 | 1402 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.07 | -41.83 | -94.11 | 2386 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.05 | -28.72 | -90.23 | 1865 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.00 | -34.22 | -91.26 | 2196 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.40 | -25.88 | -88.44 | 1913 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.07 | -43.11 | -98.08 | 3359 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -46.74 | -96.90 | 3348 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.42 | -33.18 | -93.44 | 2086 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.83 | -33.13 | -82.17 | 1525 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -49.57 | -99.69 | 6223 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.65 | -35.20 | -92.70 | 2446 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.39 | -34.35 | -94.40 | 3123 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -57.25 | -99.81 | 6022 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.69 | -38.33 | -92.71 | 2221 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.91 | -18.38 | -51.19 | 652 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.53 | -22.10 | -77.98 | 1605 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -50.81 | -97.66 | 3202 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -53.28 | -99.14 | 5060 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.03 | -22.46 | -69.55 | 1204 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.49 | -42.46 | -94.56 | 2637 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.00 | -5.96 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.90 | -31.00 | -84.43 | 1649 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -62.76 | -99.77 | 6459 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.45 | -29.54 | -91.57 | 2468 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.51 | -19.36 | -82.81 | 1951 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.27 | -31.66 | -91.46 | 2130 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.16 | -44.49 | -98.18 | 3998 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.95 | -41.74 | -90.09 | 2185 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.99 | -28.26 | -67.99 | 781 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.54 | -26.17 | -72.77 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.49 | -18.74 | -84.72 | 1830 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -46.04 | -98.10 | 4360 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -80.03 | -99.94 | 8235 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -44.95 | -6.33 | -52.59 | 303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T16:30 | MFI reversion · 1h | buy | BITX | 3.90 | — | rebalance up |
| 2026-11-27T16:30 | MFI reversion · 1h | buy | AMZN | 3.82 | — | rebalance up |
| 2026-11-27T16:30 | MFI reversion · 1h | sell | QQQ | 5.25 | 0.21 | exit signal |
| 2026-11-27T16:30 | CCI reversion · 1h | sell | UPRO | 4.42 | 0.04 | exit signal |
| 2026-11-27T16:30 | Stochastic reversion · 1h | sell | MSTR | 17.26 | 1.20 | exit signal |
| 2026-11-27T16:30 | Stochastic reversion · 1h | sell | AMD | 17.32 | 0.77 | exit signal |
| 2026-11-27T16:30 | Bollinger reversion · 1h | sell | AMD | 13.20 | 0.15 | exit signal |
| 2026-11-27T16:30 | Donchian 55/20 · 1h | buy | META | 7.84 | — | entry signal |
| 2026-11-27T16:30 | Donchian 55/20 · 1h | sell | PLTR | 3.86 | 0.06 | rebalance down |
| 2026-11-27T16:30 | Donchian 55/20 · 1h | sell | DOGE-USD | 3.98 | -0.01 | rebalance down |
| 2026-11-27T16:30 | VWAP momentum · 1h | buy | GOOGL | 2.43 | — | entry signal |
| 2026-11-27T16:30 | VWAP momentum · 1h | buy | COIN | 2.85 | — | entry signal |
| 2026-11-27T16:30 | VWAP momentum · 1h | buy | AMD | 2.85 | — | entry signal |
| 2026-11-27T16:30 | VWAP momentum · 1h | sell | AAPL | 4.24 | 0.02 | exit signal |
| 2026-11-27T16:30 | Heikin-Ashi · 1h | buy | AMZN | 3.60 | — | entry signal |
| 2026-11-27T16:30 | Heikin-Ashi · 1h | sell | NVDA | 2.78 | 0.02 | exit signal |
| 2026-11-27T16:30 | Heikin-Ashi · 1h | sell | MSFT | 2.72 | -0.04 | exit signal |
| 2026-11-27T16:30 | Heikin-Ashi · 1h | sell | GOOGL | 2.74 | -0.02 | exit signal |
| 2026-11-27T16:30 | Heikin-Ashi · 1h | sell | ETHU | 2.67 | -0.09 | exit signal |
| 2026-11-27T16:30 | Heikin-Ashi · 1h | sell | BITX | 2.69 | -0.07 | exit signal |
| 2026-11-27T16:26 | Opening range 30m | buy | TNA | 5.78 | — | rebalance up |
| 2026-11-27T16:26 | Opening range 30m | buy | PLTR | 4.60 | — | rebalance up |
| 2026-11-27T16:26 | Opening range 30m | sell | AAPL | 14.49 | -0.08 | stop-loss |
| 2026-11-27T16:26 | Opening range 15m | sell | AAPL | 11.25 | -0.06 | stop-loss |
| 2026-11-27T16:11 | Volume breakout · 1h | buy | TSLA | 19.18 | — | entry |
| 2026-11-27T16:11 | Volume breakout · 1h | buy | META | 19.18 | — | entry |
| 2026-11-27T16:00 | Agent (ML meta-label) | sell | TSLA | 13.82 | -0.03 | selected signal exited |
| 2026-11-27T16:00 | Bollinger reversion · 1h | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-11-27T16:00 | Bollinger reversion · 1h | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-11-27T15:55 | Agent (rotation) | buy | PLTR | 5.17 | — | rebalance up |
| 2026-11-27T15:55 | Agent | buy | SQQQ | 15.15 | — | following Z-score reversion |
| 2026-11-27T15:55 | Opening range 30m | buy | PLTR | 9.89 | — | entry signal |
| 2026-11-27T15:55 | Opening range 30m | sell | TSLA | 4.91 | 0.03 | rebalance down |
| 2026-11-27T15:55 | Opening range 30m | sell | IWM | 4.96 | -0.01 | rebalance down |
| 2026-11-27T15:55 | Opening range 15m | buy | PLTR | 11.29 | — | entry signal |
| 2026-11-27T15:55 | Opening range 15m | buy | AAPL | 11.30 | — | entry |
| 2026-11-27T15:55 | Opening range 15m | sell | TSLA | 4.45 | 0.02 | rebalance down |
| 2026-11-27T15:55 | Opening range 15m | sell | TNA | 4.48 | -0.01 | rebalance down |
| 2026-11-27T15:55 | Opening range 15m | sell | META | 4.58 | 0.03 | rebalance down |
| 2026-11-27T15:55 | Opening range 15m | sell | IWM | 4.50 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 16:34:05.000130+00:00 -> 2026-11-27 16:44:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
