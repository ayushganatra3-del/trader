# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T14:50:05.000131+00:00 · 66981 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.35 (-14.65%)

Closed trades 233, win rate 36.9%, fees £6.32, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.06 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-20 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 12900 decisions in 2304 calls, $0.1767 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T14:50 | 2 / 22 / 7 | cash |  |
| Breezy | 2026-11-20T14:50 | 0 / 25 / 6 | cash |  |
| Boozy | 2026-11-20T14:50 | 6 / 25 / 0 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.03 | +18.56% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.02 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.96 | 14.96 | 0 | — | 12.97 | 4.30 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.38 | 11.38 | 39 | 30.8 | 18.57 | 2.78 | -8.66 | 45 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.20 | 3.20 | 0 | — | 4.30 | 1.23 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.89 | -0.11 | 157 | 35.0 | -4.11 | -3.59 | -4.86 | 75 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.26 | -0.34 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 95.79 | -4.21 | 211 | 28.9 | -1.82 | -0.56 | -8.24 | 163 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.28 | -5.13 | 19 |
| 13 | Hold SPY | benchmark | 93.67 | -6.33 | 0 | — | -7.28 | -2.45 | -8.87 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.12 | -8.88 | 0 | — | -8.86 | -2.30 | -10.09 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.41 | -10.18 | 24 |
| 16 | Trend pullback · 1h | trend | 90.67 | -9.33 | 115 | 23.5 | -10.26 | -5.84 | -12.34 | 46 |
| 17 | VWAP reversion · 1h | reversion | 89.58 | -10.42 | 155 | 45.8 | -12.50 | -3.66 | -18.48 | 149 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 89.54 | -10.46 | 8 | 50.0 | -11.70 | -0.96 | -19.02 | 6 |
| 19 | Copy: Insider buying | copy | 88.99 | -11.01 | 55 | 40.0 | -6.98 | -1.33 | -14.79 | 66 |
| 20 | Copy: Congress Democrats (NANC) | copy | 88.71 | -11.29 | 0 | — | -11.86 | -3.31 | -14.12 | 1 |
| 21 | Daily: Bullish score | daily | 88.20 | -11.80 | 19 | 15.8 | -13.98 | -3.64 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.81 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.51 | -18.94 | 71 |
| 25 | Agent | meta | 85.35 | -14.65 | 233 | 36.9 | -13.67 | -6.22 | -16.34 | 211 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.34 | -3.94 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 82.16 | -17.84 | 194 | 27.8 | -26.24 | -7.85 | -28.86 | 196 |
| 28 | Connors RSI(2) · 1h | reversion | 80.07 | -19.93 | 218 | 40.4 | -15.51 | -6.92 | -15.67 | 71 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -17.09 | -5.95 | -21.55 | 74 |
| 30 | Donchian 55/20 · 1h | breakout | 79.32 | -20.68 | 79 | 12.7 | -26.84 | -8.38 | -27.93 | 82 |
| 31 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.32 | -5.99 | -25.33 | 144 |
| 32 | Opening range 15m | breakout | 77.32 | -22.68 | 547 | 31.8 | -21.23 | -6.47 | -23.60 | 659 |
| 33 | Ichimoku · 1h | trend | 74.35 | -25.65 | 107 | 14.0 | -30.08 | -9.05 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 73.47 | -26.54 | 226 | 20.4 | -27.24 | -4.09 | -35.87 | 277 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 73.09 | -26.91 | 2 | 0.0 | -25.72 | -3.71 | -28.95 | 1 |
| 36 | Hold BTC | benchmark | 72.33 | -27.67 | 2 | 0.0 | -24.92 | -4.11 | -29.74 | 1 |
| 37 | Triple EMA stack · 1h | trend | 70.85 | -29.15 | 161 | 14.3 | -34.71 | -9.05 | -36.70 | 170 |
| 38 | Bollinger breakout · 1h | breakout | 70.70 | -29.30 | 195 | 21.5 | -33.24 | -8.92 | -36.32 | 217 |
| 39 | Supertrend · 1h | trend | 70.57 | -29.43 | 198 | 16.7 | -32.77 | -5.41 | -39.93 | 204 |
| 40 | Max aggression: 5-day momentum | meta | 70.39 | -29.61 | 23 | 39.1 | -54.82 | -3.89 | -59.26 | 22 |
| 41 | EMA 20/50 cross · 1h | trend | 70.29 | -29.71 | 119 | 10.1 | -37.59 | -11.24 | -40.64 | 122 |
| 42 | Stochastic reversion · 1h | reversion | 69.66 | -30.34 | 363 | 41.3 | -37.74 | -5.69 | -39.28 | 424 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.14 | -37.91 | 31 |
| 44 | Heikin-Ashi · 1h | trend | 68.77 | -31.23 | 483 | 23.0 | -45.56 | -9.93 | -47.85 | 616 |
| 45 | RSI momentum · 1h | momentum | 68.46 | -31.54 | 184 | 14.1 | -38.74 | -8.76 | -41.77 | 202 |
| 46 | OBV trend · 1h | momentum | 68.40 | -31.60 | 315 | 19.4 | -38.48 | -10.49 | -41.22 | 240 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -29.44 | -6.70 | -33.76 | 204 |
| 48 | MFI reversion · 1h | reversion | 67.05 | -32.95 | 472 | 33.3 | -32.86 | -4.95 | -34.77 | 173 |
| 49 | CCI reversion · 1h | reversion | 65.71 | -34.29 | 399 | 41.9 | -43.87 | -7.39 | -45.19 | 478 |
| 50 | Donchian 20/10 · 1h | breakout | 65.24 | -34.76 | 165 | 17.6 | -36.51 | -6.96 | -43.26 | 192 |
| 51 | Max aggression: 1-day momentum | meta | 64.91 | -35.09 | 33 | 27.3 | -54.51 | -3.83 | -57.50 | 39 |
| 52 | ROC + volume · 1h | momentum | 64.82 | -35.18 | 431 | 27.6 | -37.92 | -6.62 | -43.31 | 341 |
| 53 | MACD cross · 1h | trend | 63.20 | -36.80 | 438 | 21.2 | -49.61 | -9.81 | -49.98 | 496 |
| 54 | EMA 9/21 cross · 1h | trend | 62.70 | -37.30 | 291 | 11.3 | -40.35 | -7.74 | -47.32 | 323 |
| 55 | Bollinger reversion · 1h | reversion | 60.88 | -39.12 | 362 | 37.8 | -41.18 | -6.31 | -41.84 | 419 |
| 56 | Williams %R · 1h | reversion | 59.63 | -40.37 | 455 | 39.8 | -48.61 | -8.41 | -49.46 | 578 |
| 57 | RSI(14) reversion · 1h | reversion | 57.03 | -42.97 | 221 | 33.5 | -40.50 | -5.81 | -44.32 | 270 |
| 58 | Agent (ML meta-label) | meta | 56.47 | -43.53 | 1999 | 24.7 | -25.36 | -4.59 | -27.58 | 299 |
| 59 | Z-score reversion · 1h | reversion | 53.90 | -46.10 | 237 | 33.8 | -41.03 | -5.75 | -43.66 | 263 |
| 60 | VWAP momentum · 1h | momentum | 53.88 | -46.12 | 1011 | 21.5 | -57.29 | -11.50 | -61.16 | 1196 |
| 61 | Three white soldiers | momentum | 52.55 | -47.45 | 612 | 14.2 | -51.42 | -22.77 | -51.63 | 660 |
| 62 | Candlestick reversal · 1h | reversion | 52.51 | -47.49 | 592 | 26.2 | -50.80 | -9.41 | -51.08 | 676 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -46.88 | -99.15 | 5329 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.49 | -29.75 | -83.99 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.41 | -44.80 | -94.42 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.07 | -34.18 | -91.15 | 1950 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.27 | -42.94 | -92.27 | 2293 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.12 | -28.64 | -90.21 | 2022 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.22 | -49.66 | -98.23 | 3489 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.76 | -51.22 | -96.76 | 3385 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -39.37 | -94.07 | 2216 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.64 | -34.76 | -83.64 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -57.07 | -99.65 | 6261 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.02 | -45.30 | -93.02 | 2530 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -36.10 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -69.00 | -99.84 | 6238 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.42 | -45.53 | -93.42 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.28 | -25.16 | -79.28 | 1639 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.85 | -57.28 | -97.85 | 3380 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -56.75 | -99.11 | 5032 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.79 | -29.15 | -70.79 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.93 | -54.09 | -94.93 | 2715 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.99 | -39.15 | -85.99 | 1704 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -70.63 | -99.72 | 6487 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.19 | -31.69 | -91.24 | 2426 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.61 | -19.38 | -80.69 | 1894 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.08 | -38.16 | -92.08 | 2183 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.74 | -46.59 | -97.74 | 4001 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.35 | -53.62 | -90.35 | 2184 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.51 | -31.56 | -67.51 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.37 | -28.26 | -74.89 | 1203 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.79 | -18.96 | -82.81 | 1808 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.63 | -45.80 | -97.65 | 4389 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.70 | -99.94 | 8410 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T14:50 | Day trade: Stocks in Play ORB | sell | TNA | 24.85 | -0.09 | target is flat |
| 2026-11-20T14:50 | Day trade: Stocks in Play ORB | sell | IWM | 24.90 | -0.05 | target is flat |
| 2026-11-20T14:50 | Agent | buy | TSLA | 17.07 | — | following Stochastic reversion, Bollinger reversion |
| 2026-11-20T14:50 | Opening range 15m | buy | MSFT | 19.33 | — | entry signal |
| 2026-11-20T14:45 | Agent (ML meta-label) | buy | SQQQ | 4.65 | — | rebalance up |
| 2026-11-20T14:45 | Agent (ML meta-label) | buy | LABU | 6.90 | — | rebalance up |
| 2026-11-20T14:45 | Agent (ML meta-label) | buy | ETHU | 6.96 | — | rebalance up |
| 2026-11-20T14:45 | Agent (ML meta-label) | buy | COIN | 6.99 | — | rebalance up |
| 2026-11-20T14:45 | Agent (ML meta-label) | sell | MSTR | 7.13 | -0.31 | selected signal exited |
| 2026-11-20T14:45 | Agent (ML meta-label) | sell | BITX | 7.11 | -0.33 | selected signal exited |
| 2026-11-20T14:45 | CCI reversion · 1h | sell | MSTR | 7.17 | -0.39 | stop-loss |
| 2026-11-20T14:45 | Williams %R · 1h | sell | COIN | 4.38 | -0.12 | stop-loss |
| 2026-11-20T14:45 | Z-score reversion · 1h | buy | XRP-USD | 2.72 | — | rebalance up |
| 2026-11-20T14:45 | Z-score reversion · 1h | buy | ETH-USD | 2.75 | — | rebalance up |
| 2026-11-20T14:45 | Z-score reversion · 1h | buy | BTC-USD | 2.71 | — | rebalance up |
| 2026-11-20T14:45 | Z-score reversion · 1h | sell | COIN | 9.25 | -0.35 | stop-loss |
| 2026-11-20T14:45 | RSI(14) reversion · 1h | buy | ETHU | 2.96 | — | rebalance up |
| 2026-11-20T14:45 | RSI(14) reversion · 1h | buy | BTC-USD | 5.55 | — | rebalance up |
| 2026-11-20T14:45 | RSI(14) reversion · 1h | sell | COIN | 11.38 | -0.45 | stop-loss |
| 2026-11-20T14:45 | RSI(14) reversion · 1h | sell | BITX | 14.15 | -0.68 | stop-loss |
| 2026-11-20T14:45 | Candlestick reversal · 1h | buy | ETHU | 2.81 | — | rebalance up |
| 2026-11-20T14:45 | Candlestick reversal · 1h | buy | BTC-USD | 3.36 | — | rebalance up |
| 2026-11-20T14:45 | Candlestick reversal · 1h | sell | MSTR | 4.58 | -0.11 | stop-loss |
| 2026-11-20T14:45 | Candlestick reversal · 1h | sell | BITX | 5.94 | -0.29 | stop-loss |
| 2026-11-20T14:40 | Day trade: Stocks in Play ORB | buy | TNA | 24.94 | — | entry |
| 2026-11-20T14:40 | Day trade: Stocks in Play ORB | buy | MSFT | 24.94 | — | entry |
| 2026-11-20T14:40 | Day trade: Stocks in Play ORB | buy | IWM | 24.94 | — | entry |
| 2026-11-20T14:40 | Day trade: Stocks in Play ORB | buy | GOOGL | 24.94 | — | entry |
| 2026-11-20T14:40 | Bollinger reversion · 1h | sell | TNA | 3.07 | -0.07 | rebalance down |
| 2026-11-20T14:40 | RSI(14) reversion · 1h | buy | BTC-USD | 2.94 | — | rebalance up |
| 2026-11-20T14:40 | RSI(14) reversion · 1h | sell | LABU | 2.94 | -0.09 | rebalance down |
| 2026-11-20T14:35 | Max aggression: 5-day momentum | buy | SQQQ | 71.09 | — | entry |
| 2026-11-20T14:35 | Max aggression: 5-day momentum | sell | SOL-USD | 71.09 | -2.65 | target is flat |
| 2026-11-20T14:35 | Max aggression: 1-day momentum | buy | SQQQ | 65.56 | — | entry |
| 2026-11-20T14:35 | Agent (rotation) | buy | SQQQ | 32.04 | — | following Connors RSI(2) |
| 2026-11-20T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 112.50 | — | entry |
| 2026-11-20T14:35 | Agent (ML meta-label) | buy | SQQQ | 3.18 | — | rebalance up |
| 2026-11-20T14:35 | Agent (ML meta-label) | sell | TQQQ | 6.87 | -0.43 | selected signal exited |
| 2026-11-20T14:35 | Agent (ML meta-label) | sell | SOXL | 6.32 | -1.53 | selected signal exited |
| 2026-11-20T14:35 | Daily: Bullish score | sell | SQQQ | 5.39 | 1.04 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 14:50:05.000131+00:00 -> 2026-11-20 15:00:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
