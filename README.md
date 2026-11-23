# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T18:15:05.000154+00:00 · 70852 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.86 (-21.14%)

Closed trades 240, win rate 35.8%, fees £6.50, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 25724 decisions in 2722 calls, $0.3258 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T18:15 | 6 / 14 / 10 | AMZN 16%, TNA 15%, META 14% |  |
| Breezy | 2026-11-23T18:15 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-23T18:15 | 6 / 21 / 3 | COIN 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 32.17 | 4.75 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.58 | 15.58 | 0 | — | 13.60 | 4.57 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.52 | 1.37 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.07 | 4.07 | 0 | — | 2.37 | 0.72 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.89 | -0.18 | -8.71 | 210 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.97 | -0.23 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.68 | -4.32 | 0 | — | -6.59 | -1.66 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.38 | -3.24 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.20 | -5.49 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.10 | -7.90 | 0 | — | -9.10 | -1.91 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.56 | -3.47 | -8.72 | 31 |
| 17 | VWAP reversion · 1h | reversion | 90.84 | -9.16 | 163 | 46.0 | -6.61 | -1.05 | -20.49 | 156 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.82 | -9.18 | 0 | — | -10.71 | -2.30 | -17.03 | 1 |
| 19 | Copy: Insider buying | copy | 89.15 | -10.85 | 57 | 40.4 | -18.50 | -3.62 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -16.25 | -3.36 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.99 | -13.01 | 9 | 44.4 | -10.66 | -0.55 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.71 | -13.29 | 457 | 33.3 | -12.88 | -4.30 | -14.52 | 542 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.48 | -3.96 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.11 | -6.24 | -17.90 | 71 |
| 25 | Connors RSI(2) · 1h | reversion | 80.88 | -19.12 | 219 | 40.6 | -13.23 | -5.61 | -14.31 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.62 | -19.38 | 203 | 28.1 | -27.69 | -7.48 | -30.07 | 190 |
| 27 | Agent | meta | 78.86 | -21.14 | 240 | 35.8 | -26.14 | -5.68 | -26.56 | 200 |
| 28 | Opening range 15m | breakout | 77.58 | -22.42 | 567 | 30.9 | -22.47 | -6.94 | -23.54 | 661 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -25.84 | -4.33 | -25.84 | 97 |
| 30 | Donchian 55/20 · 1h | breakout | 77.40 | -22.60 | 82 | 12.2 | -28.56 | -7.75 | -28.89 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.94 | -6.95 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -26.66 | -6.88 | -27.42 | 150 |
| 33 | Ichimoku · 1h | trend | 73.67 | -26.33 | 112 | 15.2 | -30.46 | -8.02 | -31.46 | 105 |
| 34 | Hold BTC | benchmark | 71.63 | -28.36 | 3 | 0.0 | -29.14 | -5.18 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 71.24 | -28.76 | 199 | 16.6 | -33.71 | -6.42 | -38.04 | 220 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.68 | -29.32 | 3 | 0.0 | -24.19 | -2.92 | -32.18 | 1 |
| 37 | Triple EMA stack · 1h | trend | 70.39 | -29.61 | 161 | 14.3 | -36.19 | -9.24 | -38.51 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 70.09 | -29.91 | 119 | 10.1 | -36.09 | -9.84 | -39.46 | 125 |
| 39 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -36.48 | -6.63 | -39.34 | 282 |
| 40 | Daily: Momentum burst | daily | 69.09 | -30.91 | 30 | 13.3 | -37.99 | -5.44 | -38.52 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.60 | -31.40 | 207 | 22.2 | -33.32 | -8.72 | -34.40 | 213 |
| 42 | OBV trend · 1h | momentum | 67.32 | -32.68 | 320 | 19.7 | -38.35 | -9.83 | -40.22 | 233 |
| 43 | Stochastic reversion · 1h | reversion | 67.12 | -32.88 | 392 | 40.6 | -36.11 | -3.90 | -44.44 | 437 |
| 44 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -33.96 | -9.11 | -34.22 | 209 |
| 45 | Max aggression: 5-day momentum | meta | 65.70 | -34.30 | 24 | 37.5 | -61.11 | -3.97 | -64.99 | 23 |
| 46 | RSI momentum · 1h | momentum | 65.50 | -34.50 | 188 | 13.8 | -39.07 | -8.82 | -40.66 | 203 |
| 47 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -46.87 | -9.48 | -47.64 | 632 |
| 48 | MFI reversion · 1h | reversion | 63.81 | -36.19 | 486 | 32.9 | -31.53 | -4.53 | -37.45 | 185 |
| 49 | Donchian 20/10 · 1h | breakout | 62.93 | -37.07 | 173 | 16.8 | -38.99 | -8.35 | -40.70 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.66 | -8.63 | -42.88 | 345 |
| 51 | EMA 9/21 cross · 1h | trend | 60.43 | -39.57 | 298 | 11.1 | -44.94 | -10.58 | -46.03 | 327 |
| 52 | Agent (ML meta-label) | meta | 59.87 | -40.13 | 2038 | 24.9 | -21.08 | -2.60 | -32.84 | 317 |
| 53 | MACD cross · 1h | trend | 59.28 | -40.72 | 464 | 20.9 | -48.80 | -9.33 | -50.60 | 517 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -53.21 | -3.85 | -54.71 | 38 |
| 55 | CCI reversion · 1h | reversion | 58.30 | -41.70 | 430 | 40.0 | -49.28 | -8.19 | -52.02 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 58.05 | -41.95 | 391 | 37.6 | -37.58 | -4.43 | -45.42 | 434 |
| 57 | Williams %R · 1h | reversion | 54.33 | -45.67 | 495 | 38.2 | -54.46 | -8.94 | -55.91 | 595 |
| 58 | VWAP momentum · 1h | momentum | 53.79 | -46.21 | 1049 | 21.8 | -57.71 | -13.19 | -58.43 | 1188 |
| 59 | RSI(14) reversion · 1h | reversion | 51.18 | -48.82 | 240 | 31.7 | -46.71 | -7.08 | -50.30 | 301 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.47 | -8.48 | -54.34 | 686 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -48.37 | -99.14 | 5331 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.93 | -32.65 | -84.56 | 1436 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.50 | -48.54 | -94.54 | 2423 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.88 | -31.47 | -91.06 | 1927 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.80 | -41.07 | -91.86 | 2256 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.43 | -27.61 | -89.56 | 1947 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -47.87 | -98.14 | 3413 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.98 | -51.38 | -97.00 | 3358 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -38.34 | -93.77 | 2157 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.27 | 647 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.33 | -34.80 | -83.41 | 1555 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.33 | -99.66 | 6298 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.18 | -39.77 | -93.19 | 2487 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.41 | -35.51 | -94.43 | 3158 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -61.30 | -99.82 | 6128 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.19 | -42.48 | -93.41 | 2262 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.45 | -24.03 | -78.85 | 1614 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -55.37 | -97.78 | 3284 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -57.34 | -99.18 | 5111 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.75 | -27.73 | -70.75 | 1194 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.96 | -48.18 | -94.96 | 2669 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.68 | -6.14 | -48.78 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.72 | -37.03 | -85.75 | 1682 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.59 | -99.76 | 6529 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.54 | -29.99 | -91.69 | 2460 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.90 | -19.67 | -82.91 | 1960 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.80 | -29.38 | -92.06 | 2170 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.15 | -47.36 | -98.15 | 4070 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.31 | -47.50 | -90.33 | 2200 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.54 | -30.00 | -68.55 | 798 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.19 | -28.42 | -74.42 | 1170 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.12 | -19.07 | -84.20 | 1846 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.99 | -48.20 | -98.00 | 4437 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.28 | -99.94 | 8282 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T18:10 | Agent (ML meta-label) | buy | BITX | 4.06 | — | entry |
| 2026-11-23T18:10 | Agent (aggressive) | sell | SQQQ | 38.39 | -0.76 | selected signal exited |
| 2026-11-23T18:10 | Agent | sell | SQQQ | 15.53 | -0.31 | selected signal exited |
| 2026-11-23T18:00 | Agent (ML meta-label) | sell | BITX | 4.06 | -0.02 | selected signal exited |
| 2026-11-23T18:00 | OBV trend · 1h | buy | XRP-USD | 5.12 | — | rebalance up |
| 2026-11-23T18:00 | OBV trend · 1h | buy | DOGE-USD | 4.98 | — | rebalance up |
| 2026-11-23T18:00 | OBV trend · 1h | sell | BTC-USD | 14.06 | 0.12 | exit signal |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | TSLA | 3.23 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | TNA | 3.01 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | META | 2.98 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | LABU | 2.99 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | IWM | 3.00 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | GOOGL | 2.98 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | AMZN | 2.98 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | buy | AMD | 3.01 | — | rebalance up |
| 2026-11-23T18:00 | VWAP momentum · 1h | sell | XRP-USD | 4.63 | 0.13 | exit signal |
| 2026-11-23T18:00 | VWAP momentum · 1h | sell | ETH-USD | 2.31 | 0.02 | exit signal |
| 2026-11-23T18:00 | VWAP momentum · 1h | sell | DOGE-USD | 2.29 | 0.08 | exit signal |
| 2026-11-23T18:00 | Ichimoku · 1h | sell | XRP-USD | 16.46 | 0.45 | exit signal |
| 2026-11-23T18:00 | Ichimoku · 1h | sell | SOL-USD | 19.75 | 0.78 | exit signal |
| 2026-11-23T18:00 | Parabolic SAR · 1h | buy | TSLA | 4.34 | — | rebalance up |
| 2026-11-23T18:00 | Parabolic SAR · 1h | buy | QQQ | 5.23 | — | rebalance up |
| 2026-11-23T18:00 | Parabolic SAR · 1h | buy | PLTR | 5.28 | — | rebalance up |
| 2026-11-23T18:00 | Parabolic SAR · 1h | buy | NVDA | 5.45 | — | rebalance up |
| 2026-11-23T18:00 | Parabolic SAR · 1h | buy | DOGE-USD | 5.42 | — | rebalance up |
| 2026-11-23T18:00 | Parabolic SAR · 1h | buy | AAPL | 5.22 | — | rebalance up |
| 2026-11-23T18:00 | Parabolic SAR · 1h | sell | XRP-USD | 9.36 | 0.25 | exit signal |
| 2026-11-23T18:00 | Parabolic SAR · 1h | sell | SOL-USD | 7.95 | 0.25 | exit signal |
| 2026-11-23T18:00 | Parabolic SAR · 1h | sell | BTC-USD | 8.02 | 0.08 | exit signal |
| 2026-11-23T17:55 | Agent (ML meta-label) | buy | BITX | 4.08 | — | entry |
| 2026-11-23T17:50 | Agent (rotation) | sell | TQQQ | 7.89 | -0.13 | selected signal exited |
| 2026-11-23T17:50 | Agent (rotation) | sell | LABU | 7.91 | -0.11 | selected signal exited |
| 2026-11-23T17:50 | Agent (aggressive) | buy | SQQQ | 39.15 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T17:50 | Agent | buy | SQQQ | 15.83 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T17:50 | Squeeze breakout · 1h | sell | DOGE-USD | 20.42 | -0.66 | stop-loss |
| 2026-11-23T17:50 | VWAP momentum · 1h | buy | TQQQ | 4.12 | — | entry |
| 2026-11-23T17:50 | VWAP momentum · 1h | buy | SPY | 4.12 | — | entry |
| 2026-11-23T17:50 | VWAP momentum · 1h | sell | NVDA | 4.07 | -0.07 | target is flat |
| 2026-11-23T17:50 | VWAP momentum · 1h | sell | COIN | 2.33 | -0.04 | target is flat |
| 2026-11-23T17:50 | Opening range 30m | buy | UPRO | 4.82 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 18:15:05.000154+00:00 -> 2026-11-23 18:25:05.000154+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
