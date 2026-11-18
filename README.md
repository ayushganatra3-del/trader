# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T19:55:05.000259+00:00 · 64785 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.93 (-15.07%)

Closed trades 223, win rate 35.9%, fees £6.16, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 17.05 | +0.08 |
| TSLA | 17.03 | +0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-18 | PEPG 12%, FUN 12%, STWD 12%, LRN 12%, PSEC 12%, TEAM 12%, BH 12%, LILA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 34365 decisions in 3069 calls, $0.4283 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T19:55 | 10 / 14 / 5 | AMD 15% |  |
| Breezy | 2026-11-18T19:55 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-11-18T19:55 | 8 / 20 / 1 | COIN 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |
| OBV trend | SQQQ | 1.76 | +6.31% | 9 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.44 | 14.44 | 0 | — | 13.06 | 4.31 | -3.75 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 18.18 | 3.71 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.92 | 3.92 | 0 | — | 4.41 | 1.31 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.06 | 0.07 | 150 | 34.7 | -3.66 | -3.24 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 3.23 | 1.10 | -9.06 | 208 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.91 | -4.09 | 8 | 50.0 | -4.67 | -0.18 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.60 | -4.40 | 0 | — | -3.87 | -1.27 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.20 | -1.48 | -8.74 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.95 | -7.93 | -5.54 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.45 | -7.55 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.16 | -8.84 | 0 | — | -7.51 | -2.02 | -12.67 | 1 |
| 18 | Copy: Insider buying | copy | 90.68 | -9.32 | 52 | 40.4 | -9.84 | -1.98 | -14.79 | 64 |
| 19 | Trend pullback · 1h | trend | 90.32 | -9.68 | 113 | 23.9 | -12.85 | -7.04 | -13.33 | 58 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.25 | -3.30 | -18.48 | 148 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.16 | -12.85 | 17 | 17.6 | -5.16 | -0.82 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.03 | -8.99 | -16.08 | 70 |
| 24 | Agent | meta | 84.93 | -15.07 | 223 | 35.9 | -14.82 | -7.11 | -17.06 | 203 |
| 25 | Opening range 30m | breakout | 84.76 | -15.24 | 443 | 33.4 | -12.19 | -4.10 | -14.65 | 561 |
| 26 | Agent (aggressive) | meta | 83.53 | -16.47 | 104 | 33.7 | -15.49 | -4.08 | -19.74 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.64 | -18.36 | 188 | 28.2 | -24.35 | -6.72 | -27.42 | 200 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.41 | -6.41 | -14.73 | 86 |
| 29 | Keltner breakout · 1h | breakout | 79.94 | -20.06 | 124 | 25.8 | -24.90 | -6.69 | -27.39 | 154 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.07 | -5.20 | -21.17 | 73 |
| 31 | Max aggression: 5-day momentum | meta | 79.49 | -20.51 | 21 | 42.9 | -47.74 | -3.18 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 78.87 | -21.13 | 78 | 12.8 | -25.59 | -6.72 | -30.57 | 84 |
| 33 | Opening range 15m | breakout | 77.45 | -22.55 | 537 | 31.5 | -20.07 | -5.97 | -21.80 | 669 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.10 | -22.90 | 2 | 0.0 | -18.51 | -2.50 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.31 | -24.68 | 209 | 19.1 | -27.29 | -4.47 | -35.63 | 268 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 73.53 | -26.47 | 2 | 0.0 | -18.31 | -2.56 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.65 | -8.30 | -33.72 | 216 |
| 39 | Stochastic reversion · 1h | reversion | 72.74 | -27.26 | 351 | 42.5 | -34.56 | -5.27 | -35.58 | 426 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -39.80 | -2.44 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.77 | -28.23 | 191 | 16.2 | -32.19 | -5.44 | -39.50 | 202 |
| 42 | Triple EMA stack · 1h | trend | 70.82 | -29.18 | 156 | 14.7 | -30.89 | -6.20 | -37.36 | 174 |
| 43 | MFI reversion · 1h | reversion | 70.52 | -29.48 | 448 | 33.5 | -27.26 | -4.05 | -30.08 | 173 |
| 44 | RSI momentum · 1h | momentum | 70.41 | -29.59 | 179 | 14.5 | -30.56 | -5.52 | -37.62 | 199 |
| 45 | MACD zero-line · 1h | trend | 69.82 | -30.18 | 184 | 17.9 | -28.07 | -5.65 | -34.19 | 205 |
| 46 | Heikin-Ashi · 1h | trend | 69.70 | -30.30 | 474 | 23.0 | -44.78 | -9.85 | -45.84 | 631 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.37 | -30.64 | 116 | 10.3 | -36.37 | -9.32 | -40.37 | 119 |
| 49 | ROC + volume · 1h | momentum | 68.79 | -31.20 | 413 | 28.1 | -33.53 | -6.11 | -39.37 | 342 |
| 50 | OBV trend · 1h | momentum | 68.32 | -31.68 | 310 | 19.4 | -34.97 | -7.46 | -39.89 | 252 |
| 51 | MACD cross · 1h | trend | 67.45 | -32.55 | 417 | 22.3 | -40.90 | -6.68 | -46.63 | 494 |
| 52 | CCI reversion · 1h | reversion | 67.07 | -32.93 | 387 | 41.6 | -42.41 | -7.14 | -44.29 | 475 |
| 53 | Donchian 20/10 · 1h | breakout | 66.61 | -33.39 | 162 | 17.9 | -36.49 | -6.97 | -41.44 | 198 |
| 54 | Bollinger reversion · 1h | reversion | 63.73 | -36.27 | 348 | 37.9 | -38.89 | -5.93 | -39.58 | 417 |
| 55 | Williams %R · 1h | reversion | 63.46 | -36.54 | 437 | 40.7 | -46.94 | -8.23 | -47.60 | 572 |
| 56 | EMA 9/21 cross · 1h | trend | 62.95 | -37.05 | 284 | 11.3 | -40.26 | -7.87 | -46.26 | 322 |
| 57 | Agent (ML meta-label) | meta | 59.89 | -40.11 | 1940 | 24.5 | -27.13 | -5.37 | -29.04 | 291 |
| 58 | RSI(14) reversion · 1h | reversion | 58.78 | -41.22 | 206 | 32.0 | -42.91 | -6.47 | -44.19 | 270 |
| 59 | Z-score reversion · 1h | reversion | 57.41 | -42.59 | 227 | 35.2 | -36.98 | -5.12 | -39.63 | 258 |
| 60 | VWAP momentum · 1h | momentum | 55.12 | -44.88 | 982 | 21.6 | -56.59 | -11.06 | -60.34 | 1202 |
| 61 | Candlestick reversal · 1h | reversion | 55.05 | -44.95 | 552 | 26.4 | -47.32 | -8.70 | -48.62 | 638 |
| 62 | Three white soldiers | momentum | 54.64 | -45.36 | 589 | 14.4 | -49.66 | -21.86 | -50.71 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -42.66 | -99.04 | 5278 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.41 | -25.20 | -82.56 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.65 | -40.91 | -93.93 | 2458 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.86 | -30.70 | -90.36 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.00 | -37.80 | -91.48 | 2300 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -30.79 | -90.16 | 2077 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -46.93 | -97.94 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -52.98 | -96.43 | 3387 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -38.12 | -93.46 | 2200 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.51 | -34.48 | -82.85 | 1586 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.07 | -99.61 | 6109 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.94 | -43.54 | -92.16 | 2548 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.80 | -38.98 | -94.80 | 3224 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.44 | -99.81 | 6191 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.42 | -42.63 | -92.66 | 2267 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.21 | -27.38 | -76.60 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -61.65 | -97.72 | 3431 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.55 | -99.07 | 4969 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.23 | -28.68 | -70.15 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -55.68 | -94.67 | 2751 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.61 | -36.83 | -85.11 | 1733 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.51 | -99.70 | 6398 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.82 | -31.28 | -91.03 | 2362 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.09 | -19.08 | -80.50 | 1846 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.49 | -37.03 | -91.54 | 2165 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.59 | -46.64 | -97.61 | 3917 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -58.70 | -89.33 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.28 | -30.87 | -67.01 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.71 | -24.43 | -73.12 | 1218 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.61 | -18.37 | -81.89 | 1761 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -46.41 | -97.59 | 4333 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -115.66 | -99.94 | 8445 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T19:55 | Agent (ML meta-label) | buy | GOOGL | 3.33 | — | entry |
| 2026-11-18T19:55 | Agent (ML meta-label) | sell | SPY | 3.33 | -0.00 | selected signal exited |
| 2026-11-18T19:50 | Agent (ML meta-label) | buy | TECL | 4.53 | — | entry |
| 2026-11-18T19:50 | Agent (ML meta-label) | buy | AAPL | 6.28 | — | entry |
| 2026-11-18T19:50 | Agent (ML meta-label) | sell | SPY | 4.15 | -0.00 | rebalance down |
| 2026-11-18T19:46 | Agent (ML meta-label) | buy | SPY | 5.40 | — | rebalance up |
| 2026-11-18T19:46 | Agent (ML meta-label) | sell | TECL | 6.62 | -0.03 | selected signal exited |
| 2026-11-18T19:46 | Agent (ML meta-label) | sell | AAPL | 5.43 | -0.02 | selected signal exited |
| 2026-11-18T19:40 | Agent (ML meta-label) | buy | SPY | 2.09 | — | following Squeeze breakout |
| 2026-11-18T19:35 | Agent (ML meta-label) | buy | TSLA | 3.89 | — | rebalance up |
| 2026-11-18T19:35 | Agent (ML meta-label) | buy | TECL | 6.66 | — | entry |
| 2026-11-18T19:35 | Agent (ML meta-label) | sell | SPY | 6.64 | -0.01 | selected signal exited |
| 2026-11-18T19:35 | Agent (ML meta-label) | sell | IWM | 5.99 | -0.01 | selected signal exited |
| 2026-11-18T19:35 | Three white soldiers | sell | TECL | 13.58 | -0.10 | target is flat |
| 2026-11-18T19:30 | Agent | buy | TSLA | 17.01 | — | following Stochastic reversion |
| 2026-11-18T19:30 | CCI reversion · 1h | buy | BITX | 4.30 | — | entry |
| 2026-11-18T19:30 | CCI reversion · 1h | sell | AMD | 4.30 | 0.26 | exit signal |
| 2026-11-18T19:30 | Williams %R · 1h | buy | COIN | 1.22 | — | entry |
| 2026-11-18T19:30 | Williams %R · 1h | buy | BTC-USD | 2.77 | — | entry |
| 2026-11-18T19:30 | Williams %R · 1h | sell | GOOGL | 3.99 | 0.04 | exit signal |
| 2026-11-18T19:30 | Stochastic reversion · 1h | sell | GOOGL | 4.34 | 0.06 | exit signal |
| 2026-11-18T19:30 | VWAP momentum · 1h | buy | DOGE-USD | 6.91 | — | entry |
| 2026-11-18T19:30 | VWAP momentum · 1h | sell | UPRO | 4.24 | -0.05 | exit signal |
| 2026-11-18T19:30 | VWAP momentum · 1h | sell | TSLA | 4.26 | -0.03 | exit signal |
| 2026-11-18T19:30 | VWAP momentum · 1h | sell | TNA | 4.21 | -0.08 | exit signal |
| 2026-11-18T19:30 | VWAP momentum · 1h | sell | LABU | 4.19 | -0.10 | exit signal |
| 2026-11-18T19:30 | VWAP momentum · 1h | sell | IWM | 4.26 | -0.03 | exit signal |
| 2026-11-18T19:30 | VWAP momentum · 1h | sell | AAPL | 4.27 | -0.02 | exit signal |
| 2026-11-18T19:30 | MACD zero-line · 1h | buy | AMZN | 17.46 | — | entry signal |
| 2026-11-18T19:30 | Three white soldiers | buy | TECL | 13.69 | — | entry signal |
| 2026-11-18T19:25 | Agent (ML meta-label) | buy | TSLA | 2.77 | — | following Stochastic reversion |
| 2026-11-18T19:25 | Agent (ML meta-label) | buy | IWM | 4.74 | — | rebalance up |
| 2026-11-18T19:25 | Agent (ML meta-label) | sell | TECL | 7.52 | 0.04 | selected signal exited |
| 2026-11-18T19:20 | Agent (aggressive) | buy | SOXL | 41.67 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T19:20 | Agent | buy | SOXL | 16.97 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T19:15 | Agent (ML meta-label) | buy | IWM | 1.26 | — | entry |
| 2026-11-18T19:15 | Agent (ML meta-label) | buy | AAPL | 5.44 | — | entry |
| 2026-11-18T19:10 | Agent (ML meta-label) | buy | TECL | 7.47 | — | entry |
| 2026-11-18T19:10 | Agent (ML meta-label) | sell | TSLA | 2.72 | -0.01 | selected signal exited |
| 2026-11-18T19:10 | Agent (ML meta-label) | sell | IWM | 5.99 | -0.02 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 19:55:05.000259+00:00 -> 2026-11-18 20:05:05.000259+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 19:55:05.000259+00:00 -> 2026-11-18 20:05:05.000259+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
