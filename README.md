# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T17:27:05.000141+00:00 · 29749 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.04 (-8.96%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.61 | +0.33 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 27966 decisions in 2547 calls, $0.3490 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T17:27 | 8 / 16 / 4 | cash |  |
| Breezy | 2026-10-20T17:27 | 0 / 26 / 2 | cash |  |
| Boozy | 2026-10-20T17:27 | 5 / 22 / 1 | MSTR 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | BITX | 1.90 | +3.32% | 6 |
| VWAP reversion | ETHU | 1.90 | +4.27% | 5 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.64 | 5.64 | 0 | — | 7.14 | 3.39 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 101.78 | 1.78 | 9 | 44.4 | -12.37 | -0.82 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.04 | -0.96 | 0 | — | -0.07 | 0.00 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.91 | -1.09 | 59 | 35.6 | 2.39 | 1.37 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.89 | -1.11 | 0 | — | 0.27 | 0.19 | -5.15 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.47 | -1.53 | 3 | 33.3 | 4.69 | 1.07 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 14 | Hold BTC | benchmark | 97.76 | -2.24 | 0 | — | 20.70 | 2.73 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.24 | -2.76 | 0 | — | -3.70 | -1.38 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.82 | -2.16 | -5.83 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.92 | -3.08 | 0 | — | 0.03 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.25 | -3.75 | 40 | 15.0 | -18.34 | -3.62 | -22.00 | 103 |
| 19 | Agent (rotation) | meta | 96.21 | -3.79 | 114 | 31.6 | -7.14 | -3.26 | -9.02 | 303 |
| 20 | Trend pullback · 1h | trend | 95.54 | -4.46 | 90 | 23.3 | -20.42 | -6.12 | -20.75 | 133 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Copy: Insider buying | copy | 95.23 | -4.76 | 23 | 43.5 | -12.30 | -2.12 | -20.62 | 72 |
| 23 | ADX DI cross · 1h | trend | 94.73 | -5.27 | 89 | 18.0 | -11.92 | -2.17 | -15.37 | 258 |
| 24 | Daily: Momentum burst | daily | 94.48 | -5.52 | 6 | 16.7 | -6.30 | -0.81 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.29 | 1.37 | -6.51 | 198 |
| 26 | Opening range 30m | breakout | 92.53 | -7.47 | 208 | 29.3 | -13.01 | -3.74 | -17.26 | 565 |
| 27 | Parabolic SAR · 1h | trend | 91.81 | -8.19 | 105 | 21.9 | -18.33 | -3.96 | -21.51 | 273 |
| 28 | Daily: Bullish score | daily | 91.66 | -8.34 | 7 | 0.0 | -6.56 | -0.70 | -13.10 | 13 |
| 29 | Squeeze breakout · 1h | breakout | 91.64 | -8.36 | 46 | 21.7 | -3.41 | -0.75 | -11.34 | 98 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 91.33 | -8.67 | 0 | — | 1.46 | 0.39 | -14.37 | 1 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.25 | -2.32 | -16.91 | 1 |
| 32 | Agent | meta | 91.04 | -8.96 | 87 | 40.2 | -9.86 | -3.19 | -17.30 | 250 |
| 33 | Volume breakout · 1h | breakout | 90.79 | -9.21 | 84 | 22.6 | -12.30 | -2.21 | -15.57 | 108 |
| 34 | Bollinger breakout · 1h | breakout | 90.68 | -9.32 | 87 | 29.9 | -11.16 | -2.04 | -16.22 | 260 |
| 35 | Connors RSI(2) · 1h | reversion | 89.60 | -10.40 | 150 | 41.3 | -22.65 | -6.72 | -24.22 | 201 |
| 36 | RSI momentum · 1h | momentum | 89.18 | -10.82 | 83 | 15.7 | -20.51 | -4.03 | -26.37 | 216 |
| 37 | EMA 20/50 cross · 1h | trend | 88.80 | -11.20 | 62 | 12.9 | -19.00 | -3.51 | -21.33 | 131 |
| 38 | Opening range 15m | breakout | 88.67 | -11.33 | 256 | 25.8 | -17.55 | -4.65 | -20.98 | 700 |
| 39 | Supertrend · 1h | trend | 88.41 | -11.59 | 88 | 12.5 | -21.39 | -4.25 | -26.49 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 88.39 | -11.61 | 163 | 46.6 | -13.88 | -2.29 | -22.24 | 362 |
| 41 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -5.15 | -1.36 | -11.07 | 129 |
| 42 | Keltner breakout · 1h | breakout | 87.36 | -12.64 | 60 | 21.7 | -16.22 | -2.61 | -26.08 | 207 |
| 43 | Ichimoku · 1h | trend | 86.93 | -13.07 | 60 | 13.3 | -18.99 | -3.58 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.53 | -13.47 | 192 | 20.3 | -28.02 | -5.36 | -33.17 | 471 |
| 45 | Triple EMA stack · 1h | trend | 85.35 | -14.65 | 91 | 14.3 | -31.13 | -5.78 | -35.28 | 231 |
| 46 | Z-score reversion · 1h | reversion | 84.98 | -15.02 | 95 | 30.5 | -14.44 | -2.38 | -21.32 | 197 |
| 47 | Donchian 20/10 · 1h | breakout | 84.55 | -15.45 | 81 | 17.3 | -13.56 | -1.80 | -28.37 | 219 |
| 48 | MFI reversion · 1h | reversion | 84.38 | -15.62 | 215 | 30.7 | -14.33 | -2.22 | -20.43 | 144 |
| 49 | Agent (ML meta-label) | meta | 83.97 | -16.03 | 705 | 19.3 | -5.23 | -0.83 | -14.63 | 384 |
| 50 | OBV trend · 1h | momentum | 83.91 | -16.09 | 186 | 17.2 | -29.69 | -5.15 | -36.99 | 319 |
| 51 | MACD zero-line · 1h | trend | 83.67 | -16.33 | 89 | 14.6 | -25.27 | -5.02 | -26.35 | 224 |
| 52 | Three white soldiers | momentum | 82.67 | -17.33 | 249 | 19.7 | -46.56 | -17.74 | -47.79 | 615 |
| 53 | Bollinger reversion · 1h | reversion | 82.31 | -17.69 | 162 | 35.8 | -28.20 | -5.40 | -33.45 | 350 |
| 54 | Williams %R · 1h | reversion | 81.84 | -18.16 | 193 | 43.5 | -32.09 | -5.04 | -36.49 | 526 |
| 55 | ROC + volume · 1h | momentum | 81.66 | -18.34 | 199 | 21.6 | -25.53 | -4.30 | -34.45 | 397 |
| 56 | CCI reversion · 1h | reversion | 81.02 | -18.98 | 177 | 41.8 | -18.29 | -2.28 | -27.44 | 444 |
| 57 | Heikin-Ashi · 1h | trend | 80.62 | -19.38 | 229 | 21.0 | -41.46 | -8.63 | -46.11 | 680 |
| 58 | RSI(14) reversion · 1h | reversion | 80.00 | -20.00 | 83 | 22.9 | -15.30 | -2.77 | -23.28 | 175 |
| 59 | EMA 9/21 cross · 1h | trend | 79.59 | -20.41 | 143 | 10.5 | -29.25 | -6.09 | -30.10 | 323 |
| 60 | VWAP momentum · 1h | momentum | 78.01 | -21.99 | 447 | 20.6 | -42.30 | -6.87 | -50.30 | 1250 |
| 61 | Candlestick reversal · 1h | reversion | 77.49 | -22.51 | 220 | 28.2 | -33.40 | -5.91 | -37.01 | 544 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.39 | -1.57 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.99 | -38.01 | 620 | 23.2 | -77.04 | -19.71 | -78.73 | 1725 |
| 64 | Volume breakout | breakout | 61.70 | -38.30 | 376 | 14.1 | -63.13 | -18.79 | -64.25 | 872 |
| 65 | Squeeze breakout | breakout | 58.81 | -41.19 | 485 | 14.2 | -64.32 | -19.91 | -66.58 | 1208 |
| 66 | Donchian 55/20 | breakout | 58.42 | -41.58 | 491 | 18.3 | -70.44 | -17.50 | -73.50 | 1279 |
| 67 | RSI(14) reversion | reversion | 57.42 | -42.58 | 740 | 26.4 | -74.42 | -16.40 | -74.93 | 1615 |
| 68 | EMA 20/50 cross | trend | 56.07 | -43.93 | 535 | 19.1 | -76.88 | -15.81 | -80.87 | 1440 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.59 | -14.59 | -72.28 | 1498 |
| 70 | Keltner breakout | breakout | 50.70 | -49.30 | 700 | 16.9 | -82.61 | -25.30 | -83.82 | 1811 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -29.68 | -98.77 | 5333 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.79 | -33.16 | -93.85 | 2597 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.73 | -20.74 | -88.38 | 1900 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.44 | -25.20 | -91.32 | 2358 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.99 | -25.48 | -91.26 | 2255 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.55 | -33.08 | -97.64 | 3514 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -38.10 | -96.82 | 3600 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.31 | -27.86 | -94.42 | 2524 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.64 | -27.10 | -82.64 | 1699 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.71 | -99.38 | 5745 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.32 | -25.53 | -92.18 | 2621 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -31.39 | -95.92 | 3449 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -39.87 | -99.75 | 6197 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.55 | -28.84 | -91.66 | 2345 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -39.07 | -97.70 | 3615 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.34 | -98.50 | 4704 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.83 | -32.33 | -94.15 | 2802 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.59 | -99.53 | 6170 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.54 | -21.87 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.74 | -25.97 | -88.15 | 2137 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.28 | -95.98 | 3761 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.80 | -30.97 | -89.31 | 2119 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -32.87 | -95.83 | 4101 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.81 | -99.90 | 8275 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T17:25 | RSI(14) reversion | sell | AAPL | 14.29 | 0.02 | exit signal |
| 2026-10-20T17:25 | Squeeze breakout | buy | MSFT | 14.70 | — | entry signal |
| 2026-10-20T17:25 | ROC + volume | sell | BITX | 12.37 | -0.04 | target is flat |
| 2026-10-20T17:20 | MFI reversion · 1h | sell | PLTR | 8.77 | -0.00 | target is flat |
| 2026-10-20T17:20 | ROC + volume | buy | BITX | 3.10 | — | rebalance up |
| 2026-10-20T17:20 | ROC + volume | sell | SOL-USD | 3.10 | -0.02 | rebalance down |
| 2026-10-20T17:20 | EMA 20/50 cross | buy | MSFT | 4.67 | — | entry signal |
| 2026-10-20T17:18 | ROC + volume | buy | BITX | 3.10 | — | rebalance up |
| 2026-10-20T17:18 | ROC + volume | sell | XRP-USD | 3.10 | -0.02 | rebalance down |
| 2026-10-20T17:16 | MFI reversion · 1h | buy | PLTR | 1.95 | — | rebalance up |
| 2026-10-20T17:16 | MFI reversion · 1h | buy | GOOGL | 12.05 | — | entry |
| 2026-10-20T17:16 | MFI reversion · 1h | sell | UPRO | 14.00 | -0.05 | target is flat |
| 2026-10-20T17:16 | ROC + volume | buy | BITX | 3.10 | — | rebalance up |
| 2026-10-20T17:16 | ROC + volume | sell | ETH-USD | 3.10 | -0.02 | rebalance down |
| 2026-10-20T17:10 | Volume breakout · 1h | buy | AMZN | 22.34 | — | entry |
| 2026-10-20T17:10 | Squeeze breakout | buy | BTC-USD | 14.74 | — | entry signal |
| 2026-10-20T17:10 | Squeeze breakout | buy | BITX | 14.74 | — | entry signal |
| 2026-10-20T17:10 | ROC + volume | buy | BITX | 3.12 | — | entry signal |
| 2026-10-20T17:10 | ROC + volume | sell | DOGE-USD | 3.12 | -0.01 | rebalance down |
| 2026-10-20T17:00 | Squeeze breakout · 1h | buy | DOGE-USD | 22.94 | — | entry signal |
| 2026-10-20T17:00 | RSI momentum · 1h | buy | SOL-USD | 8.91 | — | entry signal |
| 2026-10-20T17:00 | VWAP momentum · 1h | buy | SOL-USD | 4.87 | — | entry signal |
| 2026-10-20T17:00 | EMA 20/50 cross | sell | NVDA | 4.30 | -0.02 | exit signal |
| 2026-10-20T16:56 | EMA 20/50 cross | sell | TQQQ | 4.64 | -0.03 | exit signal |
| 2026-10-20T16:50 | Donchian 55/20 · 1h | buy | AMZN | 4.82 | — | rebalance up |
| 2026-10-20T16:50 | ROC + volume | buy | XRP-USD | 15.59 | — | entry signal |
| 2026-10-20T16:50 | ROC + volume | buy | SOL-USD | 15.59 | — | entry signal |
| 2026-10-20T16:50 | ROC + volume | buy | ETH-USD | 15.59 | — | entry signal |
| 2026-10-20T16:50 | ROC + volume | buy | DOGE-USD | 15.59 | — | entry signal |
| 2026-10-20T16:41 | EMA 20/50 cross | buy | NVDA | 4.31 | — | entry signal |
| 2026-10-20T16:35 | Agent (ML meta-label) | buy | QQQ | 7.40 | — | entry |
| 2026-10-20T16:35 | EMA 20/50 cross | buy | TQQQ | 4.67 | — | entry signal |
| 2026-10-20T16:30 | Agent (ML meta-label) | sell | QQQ | 5.41 | -0.00 | selected signal exited |
| 2026-10-20T16:30 | Agent (ML meta-label) | sell | COIN | 1.99 | -0.00 | selected signal exited |
| 2026-10-20T16:30 | Bollinger reversion · 1h | buy | AAPL | 20.57 | — | entry signal |
| 2026-10-20T16:30 | VWAP momentum · 1h | sell | AMZN | 3.55 | -0.01 | exit signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | buy | TNA | 11.48 | — | entry signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | buy | MSTR | 11.48 | — | entry signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | buy | IWM | 11.48 | — | entry signal |
| 2026-10-20T16:30 | Heikin-Ashi · 1h | sell | TSLA | 8.51 | 0.09 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 17:27:05.000141+00:00 -> 2026-10-20 17:37:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
