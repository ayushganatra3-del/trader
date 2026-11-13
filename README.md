# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T19:40:05.000151+00:00 · 58565 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 36198 decisions in 3150 calls, $0.4502 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T19:40 | 10 / 11 / 8 | cash |  |
| Breezy | 2026-11-13T19:40 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-11-13T19:40 | 6 / 22 / 1 | MSTR 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| MFI reversion | LABU | 1.92 | +6.76% | 3 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.43 | 17.43 | 0 | — | 14.86 | 4.97 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 115.18 | 15.18 | 34 | 29.4 | 23.53 | 3.39 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.14 | 12.14 | 22 | 68.2 | 15.53 | 3.18 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.08 | 5.08 | 0 | — | 7.04 | 1.92 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.74 | 4.74 | 32 | 43.8 | 4.65 | 1.19 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.17 | 1.17 | 141 | 34.8 | 7.74 | 3.05 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.21 | -1.79 | 0 | — | -0.72 | -0.17 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.82 | -3.18 | 1 | 0.0 | -3.32 | -2.17 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.60 | -3.40 | 191 | 30.4 | -2.32 | -0.79 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.24 | -3.76 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 94.08 | -5.92 | 43 | 39.5 | -5.19 | -0.97 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.69 | -6.31 | 0 | — | -4.80 | -1.28 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 20 | Trend pullback · 1h | trend | 91.93 | -8.07 | 110 | 22.7 | -14.58 | -5.33 | -17.77 | 71 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.67 | -2.31 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.95 | -14.05 | 433 | 33.3 | -10.16 | -3.21 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.72 | -14.28 | 16 | 18.8 | -10.23 | -1.62 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.88 | -7.41 | -15.95 | 208 |
| 26 | Parabolic SAR · 1h | trend | 85.23 | -14.78 | 176 | 29.0 | -15.66 | -3.38 | -22.50 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.11 | -4.44 | -18.51 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.96 | -18.04 | 73 | 13.7 | -23.10 | -4.82 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.50 | -18.50 | 1 | 0.0 | -10.87 | -1.53 | -22.00 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.19 | -18.81 | 2 | 0.0 | -9.51 | -1.09 | -24.16 | 1 |
| 31 | Connors RSI(2) · 1h | reversion | 80.66 | -19.34 | 212 | 40.1 | -18.13 | -6.38 | -18.32 | 114 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Keltner breakout · 1h | breakout | 80.52 | -19.48 | 120 | 25.8 | -17.37 | -3.52 | -25.32 | 171 |
| 34 | Stochastic reversion · 1h | reversion | 79.79 | -20.21 | 303 | 47.5 | -25.86 | -3.78 | -28.24 | 402 |
| 35 | Opening range 15m | breakout | 78.40 | -21.60 | 526 | 31.2 | -17.39 | -4.67 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 77.93 | -22.07 | 399 | 35.3 | -22.48 | -2.92 | -27.13 | 171 |
| 37 | ADX DI cross · 1h | trend | 76.66 | -23.34 | 198 | 19.7 | -24.22 | -3.66 | -32.21 | 273 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -40.68 | -2.63 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 240 |
| 41 | Heikin-Ashi · 1h | trend | 74.91 | -25.09 | 443 | 24.2 | -37.98 | -7.07 | -39.26 | 664 |
| 42 | MACD cross · 1h | trend | 74.76 | -25.24 | 385 | 23.6 | -29.18 | -4.33 | -38.65 | 470 |
| 43 | Max aggression: 1-day momentum | meta | 74.72 | -25.27 | 29 | 27.6 | -20.33 | -0.62 | -57.50 | 41 |
| 44 | MACD zero-line · 1h | trend | 73.44 | -26.56 | 171 | 18.7 | -23.80 | -4.68 | -30.99 | 202 |
| 45 | RSI momentum · 1h | momentum | 72.67 | -27.33 | 171 | 14.0 | -26.96 | -4.15 | -37.92 | 209 |
| 46 | Supertrend · 1h | trend | 72.58 | -27.42 | 180 | 15.0 | -30.56 | -5.23 | -36.51 | 216 |
| 47 | EMA 20/50 cross · 1h | trend | 72.47 | -27.53 | 109 | 10.1 | -28.34 | -4.79 | -40.51 | 120 |
| 48 | Bollinger reversion · 1h | reversion | 72.13 | -27.87 | 302 | 41.7 | -33.00 | -5.16 | -35.72 | 383 |
| 49 | Triple EMA stack · 1h | trend | 71.73 | -28.27 | 151 | 14.6 | -28.24 | -4.67 | -38.65 | 205 |
| 50 | ROC + volume · 1h | momentum | 71.23 | -28.77 | 398 | 28.6 | -31.53 | -5.80 | -38.37 | 376 |
| 51 | CCI reversion · 1h | reversion | 71.23 | -28.77 | 346 | 43.4 | -37.45 | -5.87 | -38.71 | 470 |
| 52 | OBV trend · 1h | momentum | 69.81 | -30.19 | 298 | 19.1 | -30.49 | -5.38 | -38.15 | 277 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -33.15 | -4.51 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.33 | -30.67 | 153 | 19.0 | -30.22 | -5.42 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 68.02 | -31.98 | 383 | 43.6 | -42.34 | -6.91 | -44.04 | 543 |
| 56 | Z-score reversion · 1h | reversion | 65.63 | -34.37 | 204 | 37.3 | -30.37 | -4.30 | -31.55 | 237 |
| 57 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1851 | 24.8 | -20.16 | -2.88 | -24.49 | 345 |
| 58 | EMA 9/21 cross · 1h | trend | 64.81 | -35.19 | 266 | 11.3 | -37.98 | -7.70 | -43.16 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 64.53 | -35.48 | 186 | 32.8 | -36.13 | -5.32 | -38.24 | 240 |
| 60 | VWAP momentum · 1h | momentum | 62.69 | -37.31 | 913 | 22.2 | -52.78 | -10.68 | -53.44 | 1237 |
| 61 | Candlestick reversal · 1h | reversion | 62.13 | -37.87 | 486 | 28.4 | -44.99 | -8.32 | -46.12 | 605 |
| 62 | Three white soldiers | momentum | 58.34 | -41.66 | 542 | 14.6 | -49.50 | -22.28 | -49.51 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -44.57 | -99.01 | 5306 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.98 | -25.56 | -80.25 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -46.55 | -93.84 | 2543 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.22 | -31.56 | -89.28 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -41.47 | -91.31 | 2355 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.80 | -31.26 | -89.80 | 2197 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -52.09 | -97.89 | 3506 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -56.64 | -96.24 | 3432 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.77 | -33.10 | -93.78 | 2342 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -34.70 | -83.20 | 1662 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.57 | -99.57 | 6036 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -42.88 | -92.24 | 2635 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -37.15 | -95.41 | 3474 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.87 | -99.81 | 6172 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.25 | -42.97 | -92.29 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.66 | -25.95 | -75.85 | 1650 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -60.63 | -97.61 | 3517 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.05 | -98.89 | 4941 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.47 | -26.83 | -68.70 | 1254 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -56.81 | -94.76 | 2812 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.05 | -39.26 | -85.18 | 1791 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.80 | -99.66 | 6379 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.05 | -32.62 | -90.19 | 2327 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.51 | -20.17 | -78.89 | 1798 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.70 | -36.58 | -90.88 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.02 | -51.89 | -97.02 | 3887 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -58.39 | -89.49 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.36 | -30.57 | -66.38 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.35 | -23.03 | -71.43 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.00 | -19.28 | -80.41 | 1748 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.41 | -51.01 | -97.41 | 4352 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.43 | -99.93 | 8458 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T19:35 | Agent (ML meta-label) | buy | PLTR | 1.45 | — | following VWAP reversion |
| 2026-11-13T19:35 | Agent (ML meta-label) | buy | MSTR | 5.75 | — | entry |
| 2026-11-13T19:35 | Agent (ML meta-label) | sell | UPRO | 3.79 | -0.02 | selected signal exited |
| 2026-11-13T19:35 | Agent (ML meta-label) | sell | AMZN | 3.41 | -0.01 | selected signal exited |
| 2026-11-13T19:30 | MFI reversion · 1h | buy | COIN | 3.25 | — | entry signal |
| 2026-11-13T19:30 | MFI reversion · 1h | buy | BITX | 6.50 | — | entry |
| 2026-11-13T19:30 | MFI reversion · 1h | sell | META | 9.75 | 0.14 | exit signal |
| 2026-11-13T19:30 | CCI reversion · 1h | buy | MSTR | 3.39 | — | entry signal |
| 2026-11-13T19:30 | CCI reversion · 1h | buy | IWM | 3.39 | — | entry signal |
| 2026-11-13T19:30 | CCI reversion · 1h | buy | AMD | 3.39 | — | entry signal |
| 2026-11-13T19:30 | CCI reversion · 1h | sell | XRP-USD | 3.71 | -0.01 | rebalance down |
| 2026-11-13T19:30 | CCI reversion · 1h | sell | ETH-USD | 3.73 | -0.00 | rebalance down |
| 2026-11-13T19:30 | CCI reversion · 1h | sell | BTC-USD | 3.70 | -0.02 | rebalance down |
| 2026-11-13T19:30 | Connors RSI(2) · 1h | sell | AMZN | 20.10 | -0.16 | exit signal |
| 2026-11-13T19:30 | RSI momentum · 1h | buy | META | 18.14 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | UPRO | 3.26 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | TQQQ | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | TNA | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | TECL | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | SPY | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | SOXL | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | QQQ | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | PLTR | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | NVDA | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | MSTR | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | LABU | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | IWM | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | ETHU | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | COIN | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | buy | BITX | 3.31 | — | entry signal |
| 2026-11-13T19:30 | VWAP momentum · 1h | sell | TSLA | 12.39 | 0.04 | rebalance down |
| 2026-11-13T19:30 | VWAP momentum · 1h | sell | MSFT | 12.38 | 0.01 | rebalance down |
| 2026-11-13T19:30 | VWAP momentum · 1h | sell | META | 9.34 | 0.13 | rebalance down |
| 2026-11-13T19:30 | VWAP momentum · 1h | sell | DOGE-USD | 9.29 | 0.03 | rebalance down |
| 2026-11-13T19:30 | Heikin-Ashi · 1h | buy | MSFT | 18.74 | — | entry signal |
| 2026-11-13T19:30 | Heikin-Ashi · 1h | sell | SQQQ | 18.54 | -0.24 | exit signal |
| 2026-11-13T19:30 | Parabolic SAR · 1h | buy | META | 21.32 | — | entry signal |
| 2026-11-13T19:30 | Supertrend · 1h | buy | META | 4.04 | — | entry signal |
| 2026-11-13T19:30 | MACD zero-line · 1h | buy | META | 18.37 | — | entry signal |
| 2026-11-13T19:30 | MACD cross · 1h | buy | NVDA | 8.36 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 19:40:05.000151+00:00 -> 2026-11-13 19:50:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
