# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T14:15:05.000100+00:00 · 70669 ticks

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
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 10838 decisions in 2173 calls, $0.1514 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T14:15 | 4 / 1 / 0 | XRP-USD 17%, SOL-USD 15%, DOGE-USD 14% |  |
| Breezy | 2026-11-23T14:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T14:15 | 5 / 0 / 0 | ETH-USD 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.80% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.65 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.48 | 14.48 | 0 | — | 12.18 | 4.59 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.27 | -2.33 | -2.86 | 68 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.52 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.88 | -3.67 | -9.02 | 32 |
| 15 | Hold SPY | benchmark | 90.94 | -9.06 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 17 | Squeeze breakout · 1h | breakout | 89.73 | -10.27 | 70 | 20.0 | -15.38 | -6.55 | -18.96 | 76 |
| 18 | Copy: Insider buying | copy | 87.93 | -12.07 | 56 | 39.3 | -19.64 | -3.92 | -22.56 | 66 |
| 19 | VWAP reversion · 1h | reversion | 87.89 | -12.11 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 20 | Parabolic SAR · 1h | trend | 87.66 | -12.34 | 198 | 27.3 | -20.10 | -4.86 | -27.64 | 195 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 22 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 24 | Copy: Congress Democrats (NANC) | copy | 85.94 | -14.06 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 25 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 26 | Donchian 55/20 · 1h | breakout | 84.19 | -15.81 | 79 | 12.7 | -21.25 | -5.47 | -26.62 | 85 |
| 27 | Volume breakout · 1h | breakout | 81.53 | -18.47 | 163 | 28.8 | -17.98 | -7.67 | -20.03 | 72 |
| 28 | Keltner breakout · 1h | breakout | 80.93 | -19.07 | 128 | 25.8 | -20.99 | -5.95 | -23.49 | 142 |
| 29 | Ichimoku · 1h | trend | 80.50 | -19.50 | 109 | 13.8 | -23.31 | -5.39 | -31.41 | 110 |
| 30 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.48 | -4.90 | -21.26 | 199 |
| 31 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 32 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.51 | -3.92 | -18.44 | 91 |
| 33 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 34 | Supertrend · 1h | trend | 77.19 | -22.81 | 198 | 16.7 | -29.12 | -5.01 | -37.64 | 204 |
| 35 | Triple EMA stack · 1h | trend | 75.80 | -24.20 | 161 | 14.3 | -28.83 | -6.19 | -36.00 | 170 |
| 36 | EMA 20/50 cross · 1h | trend | 75.64 | -24.36 | 119 | 10.1 | -32.80 | -7.72 | -40.35 | 126 |
| 37 | ADX DI cross · 1h | trend | 74.97 | -25.03 | 234 | 20.1 | -30.56 | -5.61 | -35.87 | 276 |
| 38 | Bollinger breakout · 1h | breakout | 73.80 | -26.20 | 201 | 20.9 | -29.97 | -7.22 | -34.65 | 213 |
| 39 | Hold BTC | benchmark | 73.53 | -26.47 | 3 | 0.0 | -26.63 | -4.47 | -36.21 | 1 |
| 40 | Max aggression: 1-day momentum | meta | 73.03 | -26.97 | 33 | 27.3 | -43.18 | -3.10 | -50.47 | 37 |
| 41 | OBV trend · 1h | momentum | 72.61 | -27.39 | 318 | 19.5 | -33.90 | -7.94 | -40.14 | 236 |
| 42 | RSI momentum · 1h | momentum | 71.75 | -28.25 | 187 | 13.9 | -33.98 | -6.78 | -39.84 | 205 |
| 43 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 44 | Heikin-Ashi · 1h | trend | 69.97 | -30.03 | 500 | 23.2 | -44.56 | -9.30 | -46.64 | 617 |
| 45 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 47 | Donchian 20/10 · 1h | breakout | 68.54 | -31.46 | 171 | 17.0 | -36.95 | -7.66 | -41.69 | 196 |
| 48 | ROC + volume · 1h | momentum | 67.16 | -32.84 | 436 | 27.3 | -38.72 | -7.79 | -40.84 | 340 |
| 49 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 388 | 40.2 | -43.59 | -6.15 | -44.19 | 448 |
| 50 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -34.75 | -9.53 | -35.09 | 210 |
| 51 | EMA 9/21 cross · 1h | trend | 65.84 | -34.16 | 298 | 11.1 | -41.25 | -8.72 | -46.01 | 330 |
| 52 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.46 | -5.02 | -38.38 | 178 |
| 53 | MACD cross · 1h | trend | 63.45 | -36.55 | 461 | 21.0 | -47.52 | -8.86 | -49.85 | 510 |
| 54 | CCI reversion · 1h | reversion | 59.00 | -41.00 | 429 | 40.1 | -46.83 | -7.50 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.67 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 57.62 | -42.38 | 1031 | 21.6 | -56.69 | -12.15 | -59.79 | 1195 |
| 57 | Agent (ML meta-label) | meta | 55.13 | -44.87 | 2023 | 24.6 | -34.28 | -6.47 | -36.80 | 333 |
| 58 | Williams %R · 1h | reversion | 54.96 | -45.04 | 487 | 38.4 | -53.67 | -8.68 | -55.86 | 590 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.22 | -6.48 | -49.45 | 274 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.41 | -8.51 | -54.80 | 688 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -47.48 | -99.15 | 5368 |
| 62 | Three white soldiers | momentum | 50.61 | -49.39 | 636 | 14.3 | -52.19 | -22.42 | -52.35 | 657 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.03 | -32.90 | -84.72 | 1427 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.65 | -50.65 | -94.72 | 2460 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.75 | -30.56 | -91.12 | 1949 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.70 | -40.48 | -91.84 | 2283 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.46 | -27.89 | -89.56 | 1968 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -48.70 | -98.19 | 3472 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.91 | -54.27 | -96.99 | 3399 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -38.89 | -93.69 | 2199 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.44 | -35.74 | -83.73 | 1565 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.80 | -99.66 | 6342 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -40.46 | -93.11 | 2526 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.26 | -35.65 | -94.33 | 3128 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -63.11 | -99.83 | 6247 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.36 | -43.89 | -93.51 | 2286 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.91 | -24.67 | -79.33 | 1639 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -57.45 | -97.83 | 3354 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -56.34 | -99.18 | 5135 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.98 | -28.38 | -71.29 | 1228 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.00 | -50.22 | -95.08 | 2726 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.77 | -6.18 | -49.04 | 269 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.69 | -37.61 | -85.93 | 1702 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -68.69 | -99.76 | 6568 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.62 | -30.59 | -91.73 | 2500 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.09 | -19.89 | -83.18 | 1973 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.89 | -28.98 | -92.21 | 2190 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.11 | -47.01 | -98.11 | 4080 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.22 | -48.15 | -90.41 | 2226 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.20 | -30.73 | -68.63 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.99 | -27.60 | -74.50 | 1195 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.81 | -18.66 | -83.90 | 1862 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.95 | -47.41 | -97.95 | 4469 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -93.14 | -99.94 | 8385 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T14:00 | Volume breakout · 1h | buy | XRP-USD | 5.33 | — | entry signal |
| 2026-11-23T14:00 | Volume breakout · 1h | buy | SOL-USD | 13.61 | — | entry signal |
| 2026-11-23T14:00 | Volume breakout · 1h | buy | ETH-USD | 13.61 | — | entry signal |
| 2026-11-23T14:00 | Volume breakout · 1h | buy | DOGE-USD | 13.61 | — | entry signal |
| 2026-11-23T14:00 | Volume breakout · 1h | buy | BTC-USD | 13.61 | — | entry signal |
| 2026-11-23T14:00 | Squeeze breakout · 1h | buy | ETH-USD | 12.22 | — | entry signal |
| 2026-11-23T14:00 | Squeeze breakout · 1h | buy | DOGE-USD | 17.98 | — | entry signal |
| 2026-11-23T14:00 | Squeeze breakout · 1h | buy | BTC-USD | 17.98 | — | entry signal |
| 2026-11-23T14:00 | Squeeze breakout · 1h | sell | SOL-USD | 5.53 | 0.32 | rebalance down |
| 2026-11-23T14:00 | Keltner breakout · 1h | buy | XRP-USD | 5.41 | — | entry signal |
| 2026-11-23T14:00 | Keltner breakout · 1h | buy | ETH-USD | 13.51 | — | entry signal |
| 2026-11-23T14:00 | Keltner breakout · 1h | buy | DOGE-USD | 13.51 | — | entry signal |
| 2026-11-23T14:00 | Keltner breakout · 1h | buy | BTC-USD | 13.51 | — | entry signal |
| 2026-11-23T14:00 | Keltner breakout · 1h | sell | SOL-USD | 7.59 | 0.40 | rebalance down |
| 2026-11-23T14:00 | Donchian 55/20 · 1h | buy | ETH-USD | 5.07 | — | entry signal |
| 2026-11-23T14:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 14.04 | — | entry signal |
| 2026-11-23T14:00 | Donchian 55/20 · 1h | buy | BTC-USD | 14.04 | — | entry signal |
| 2026-11-23T14:00 | Donchian 55/20 · 1h | sell | XRP-USD | 7.40 | 0.32 | rebalance down |
| 2026-11-23T14:00 | Donchian 55/20 · 1h | sell | SOL-USD | 7.74 | 0.45 | rebalance down |
| 2026-11-23T14:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 11.41 | — | entry signal |
| 2026-11-23T14:00 | Donchian 20/10 · 1h | sell | SOL-USD | 6.16 | 0.36 | rebalance down |
| 2026-11-23T14:00 | Donchian 20/10 · 1h | sell | BTC-USD | 5.83 | 0.22 | rebalance down |
| 2026-11-23T14:00 | OBV trend · 1h | buy | ETH-USD | 1.20 | — | entry signal |
| 2026-11-23T14:00 | OBV trend · 1h | buy | DOGE-USD | 4.57 | — | rebalance up |
| 2026-11-23T14:00 | OBV trend · 1h | sell | XRP-USD | 5.76 | 0.25 | rebalance down |
| 2026-11-23T14:00 | ROC + volume · 1h | buy | SOL-USD | 4.56 | — | entry signal |
| 2026-11-23T14:00 | ROC + volume · 1h | buy | DOGE-USD | 11.20 | — | entry signal |
| 2026-11-23T14:00 | ROC + volume · 1h | buy | BTC-USD | 11.20 | — | entry signal |
| 2026-11-23T14:00 | ROC + volume · 1h | sell | XRP-USD | 4.73 | 0.25 | rebalance down |
| 2026-11-23T14:00 | ROC + volume · 1h | sell | ETH-USD | 5.93 | 0.24 | rebalance down |
| 2026-11-23T14:00 | MACD cross · 1h | buy | ETH-USD | 4.34 | — | entry signal |
| 2026-11-23T14:00 | MACD cross · 1h | buy | BTC-USD | 10.57 | — | entry signal |
| 2026-11-23T14:00 | MACD cross · 1h | sell | XRP-USD | 5.50 | 0.28 | rebalance down |
| 2026-11-23T14:00 | MACD cross · 1h | sell | DOGE-USD | 5.48 | 0.24 | rebalance down |
| 2026-11-23T13:35 | Three white soldiers | sell | SOL-USD | 12.63 | -0.03 | exit signal |
| 2026-11-23T13:05 | Three white soldiers | buy | SOL-USD | 12.66 | — | entry signal |
| 2026-11-23T13:00 | Heikin-Ashi · 1h | sell | SOL-USD | 17.34 | 0.00 | exit signal |
| 2026-11-23T13:00 | Ichimoku · 1h | buy | SOL-USD | 3.89 | — | rebalance up |
| 2026-11-23T13:00 | Ichimoku · 1h | buy | DOGE-USD | 15.10 | — | rebalance up |
| 2026-11-23T13:00 | Ichimoku · 1h | sell | ETH-USD | 19.18 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 14:15:05.000100+00:00 -> 2026-11-23 14:25:05.000100+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
