# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-22T10:50:05.000127+00:00 · 69258 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.18 (-19.82%)

Closed trades 238, win rate 36.1%, fees £6.46, max drawdown -20.19%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-21 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 8580 decisions in 1716 calls, $0.1200 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-22T10:50 | 0 / 5 / 0 | cash |  |
| Breezy | 2026-11-22T10:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-22T10:50 | 2 / 3 / 0 | ETH-USD 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.73 | +27.25% | 5 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.56 | +8.27% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.49 | 14.49 | 0 | — | 12.18 | 4.63 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.12 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -3.14 | -2.96 | -3.73 | 72 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.53 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.76 | -4.20 | -10.56 | 37 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.38 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.24 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.87 | -7.54 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -14.13 | -2.75 | -18.60 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.90 | -12.10 | 161 | 45.3 | -14.56 | -4.21 | -20.40 | 157 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -4.00 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -4.01 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.80 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.56 | -15.44 | 194 | 27.8 | -22.91 | -6.14 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.43 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -19.82 | -9.62 | -20.09 | 67 |
| 28 | Keltner breakout · 1h | breakout | 80.23 | -19.77 | 126 | 26.2 | -21.79 | -6.29 | -24.03 | 138 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.49 | -4.95 | -21.26 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.50 | -3.95 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.69 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -26.88 | -7.25 | -31.39 | 105 |
| 34 | ADX DI cross · 1h | trend | 74.42 | -25.58 | 233 | 20.2 | -31.62 | -5.94 | -35.87 | 279 |
| 35 | Supertrend · 1h | trend | 73.92 | -26.08 | 198 | 16.7 | -32.63 | -6.27 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.96 | -3.42 | -58.28 | 39 |
| 37 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -31.50 | -7.52 | -36.09 | 165 |
| 38 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.64 | -9.59 | -40.41 | 121 |
| 39 | Bollinger breakout · 1h | breakout | 71.41 | -28.59 | 199 | 21.1 | -33.67 | -8.88 | -35.58 | 213 |
| 40 | Hold BTC | benchmark | 70.41 | -29.59 | 3 | 0.0 | -28.61 | -5.43 | -36.23 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.14 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -35.73 | -9.04 | -40.11 | 229 |
| 43 | Heikin-Ashi · 1h | trend | 70.17 | -29.83 | 492 | 23.4 | -44.43 | -9.44 | -46.74 | 611 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.41 | -37.91 | 31 |
| 45 | RSI momentum · 1h | momentum | 69.25 | -30.75 | 186 | 14.0 | -36.71 | -8.01 | -39.81 | 202 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.19 | -6.13 | -44.08 | 450 |
| 48 | MACD zero-line · 1h | trend | 66.39 | -33.61 | 195 | 16.9 | -34.40 | -9.54 | -34.78 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 66.02 | -33.98 | 170 | 17.1 | -40.58 | -9.14 | -42.59 | 195 |
| 50 | ROC + volume · 1h | momentum | 65.86 | -34.14 | 433 | 27.5 | -40.98 | -8.77 | -42.02 | 338 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -35.78 | -5.29 | -39.51 | 179 |
| 52 | EMA 9/21 cross · 1h | trend | 63.43 | -36.57 | 296 | 11.1 | -44.30 | -10.51 | -46.01 | 331 |
| 53 | MACD cross · 1h | trend | 62.12 | -37.88 | 451 | 21.5 | -49.01 | -9.68 | -50.62 | 504 |
| 54 | CCI reversion · 1h | reversion | 59.03 | -40.97 | 425 | 39.8 | -47.13 | -7.67 | -51.36 | 494 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.73 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.95 | -44.05 | 1025 | 21.7 | -58.51 | -13.56 | -60.39 | 1201 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -32.47 | -5.70 | -34.32 | 319 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.60 | -8.75 | -55.96 | 592 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.01 | -6.48 | -49.45 | 276 |
| 60 | Three white soldiers | momentum | 51.16 | -48.84 | 630 | 14.4 | -52.69 | -22.57 | -52.91 | 661 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.05 | -8.51 | -54.54 | 687 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -48.44 | -99.15 | 5353 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.12 | -35.03 | -84.59 | 1416 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.58 | -47.25 | -94.67 | 2458 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.76 | -31.65 | -91.43 | 1942 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.66 | -39.47 | -92.04 | 2279 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.24 | -28.33 | -89.24 | 1962 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -46.52 | -98.21 | 3476 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -52.02 | -96.88 | 3391 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.38 | -39.03 | -93.39 | 2160 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.43 | -34.92 | -83.50 | 1569 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -56.10 | -99.66 | 6343 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.62 | -38.32 | -92.92 | 2518 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.33 | -37.90 | -94.33 | 3120 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -65.61 | -99.84 | 6274 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.36 | -44.95 | -93.49 | 2277 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.11 | -23.73 | -79.51 | 1644 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -56.19 | -97.79 | 3358 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -60.14 | -99.17 | 5128 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.92 | -27.18 | -70.47 | 1223 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -47.41 | -94.80 | 2713 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.54 | -6.18 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.44 | -36.03 | -85.74 | 1701 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -74.10 | -99.76 | 6570 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.70 | -31.86 | -91.71 | 2494 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.03 | -20.16 | -83.15 | 1964 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.49 | -33.08 | -92.54 | 2199 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.07 | -48.40 | -98.08 | 4074 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.03 | -47.98 | -90.06 | 2211 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.24 | -30.66 | -67.27 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.75 | -26.82 | -74.90 | 1196 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.13 | -19.23 | -84.30 | 1867 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.88 | -48.17 | -97.88 | 4461 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.97 | -99.94 | 8406 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-22T10:00 | CCI reversion · 1h | buy | XRP-USD | 3.04 | — | rebalance up |
| 2026-11-22T10:00 | CCI reversion · 1h | buy | SOL-USD | 3.00 | — | rebalance up |
| 2026-11-22T10:00 | CCI reversion · 1h | buy | DOGE-USD | 2.99 | — | rebalance up |
| 2026-11-22T10:00 | CCI reversion · 1h | sell | ETH-USD | 11.87 | 0.29 | exit signal |
| 2026-11-22T10:00 | CCI reversion · 1h | sell | BTC-USD | 11.88 | 0.19 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | XRP-USD | 13.64 | 0.15 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | SOL-USD | 5.57 | 0.06 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | ETH-USD | 11.06 | 0.28 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | DOGE-USD | 13.71 | 0.26 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | BTC-USD | 11.05 | 0.30 | exit signal |
| 2026-11-22T10:00 | Stochastic reversion · 1h | sell | SOL-USD | 4.24 | 0.07 | exit signal |
| 2026-11-22T10:00 | Stochastic reversion · 1h | sell | ETH-USD | 4.89 | 0.13 | exit signal |
| 2026-11-22T10:00 | Stochastic reversion · 1h | sell | BTC-USD | 4.28 | 0.12 | exit signal |
| 2026-11-22T10:00 | Keltner breakout · 1h | buy | ETH-USD | 20.13 | — | entry signal |
| 2026-11-22T10:00 | Keltner breakout · 1h | buy | BTC-USD | 20.13 | — | entry signal |
| 2026-11-22T10:00 | Bollinger breakout · 1h | buy | ETH-USD | 17.92 | — | entry signal |
| 2026-11-22T10:00 | Bollinger breakout · 1h | buy | BTC-USD | 17.92 | — | entry signal |
| 2026-11-22T10:00 | Donchian 20/10 · 1h | buy | ETH-USD | 16.57 | — | entry signal |
| 2026-11-22T10:00 | Donchian 20/10 · 1h | buy | BTC-USD | 16.57 | — | entry signal |
| 2026-11-22T10:00 | RSI momentum · 1h | buy | ETH-USD | 14.57 | — | entry signal |
| 2026-11-22T10:00 | RSI momentum · 1h | buy | DOGE-USD | 17.38 | — | entry signal |
| 2026-11-22T10:00 | RSI momentum · 1h | buy | BTC-USD | 17.38 | — | entry signal |
| 2026-11-22T10:00 | ROC + volume · 1h | buy | ETH-USD | 16.50 | — | entry signal |
| 2026-11-22T10:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.59 | — | entry signal |
| 2026-11-22T10:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 17.59 | — | entry signal |
| 2026-11-22T10:00 | Parabolic SAR · 1h | buy | XRP-USD | 3.65 | — | entry signal |
| 2026-11-22T10:00 | Parabolic SAR · 1h | buy | SOL-USD | 14.15 | — | entry signal |
| 2026-11-22T10:00 | Parabolic SAR · 1h | buy | ETH-USD | 14.15 | — | entry signal |
| 2026-11-22T10:00 | Parabolic SAR · 1h | buy | DOGE-USD | 14.15 | — | entry signal |
| 2026-11-22T10:00 | Parabolic SAR · 1h | buy | BTC-USD | 14.15 | — | entry signal |
| 2026-11-22T10:00 | MACD zero-line · 1h | buy | SOL-USD | 16.66 | — | entry signal |
| 2026-11-22T10:00 | MACD zero-line · 1h | buy | DOGE-USD | 16.66 | — | entry signal |
| 2026-11-22T10:00 | MACD zero-line · 1h | buy | BTC-USD | 16.66 | — | entry signal |
| 2026-11-22T10:00 | MACD cross · 1h | buy | XRP-USD | 6.53 | — | entry signal |
| 2026-11-22T10:00 | MACD cross · 1h | buy | SOL-USD | 10.40 | — | entry signal |
| 2026-11-22T10:00 | MACD cross · 1h | buy | ETH-USD | 10.40 | — | entry signal |
| 2026-11-22T10:00 | MACD cross · 1h | buy | DOGE-USD | 10.40 | — | entry signal |
| 2026-11-22T10:00 | MACD cross · 1h | buy | BTC-USD | 10.40 | — | entry signal |
| 2026-11-22T10:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 2.35 | — | entry signal |
| 2026-11-22T10:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 10.61 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-24 10:50:05.000127+00:00 -> 2026-11-22 11:00:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
