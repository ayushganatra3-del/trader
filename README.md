# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T16:59:05.000120+00:00 · 64647 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.48 (-15.52%)

Closed trades 219, win rate 35.6%, fees £6.10, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 16.70 | -0.23 |
| SQQQ | 17.01 | +0.08 |
| TSLA | 16.90 | -0.03 |

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

Today: 22098 decisions in 2655 calls, $0.2850 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T16:59 | 17 / 12 / 1 | cash |  |
| Breezy | 2026-11-18T16:59 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-18T16:59 | 7 / 22 / 1 | MSTR 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.92 | +5.04% | 13 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 115.33 | 15.33 | 0 | — | 13.06 | 4.58 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.73 | 3.73 | 0 | — | 4.74 | 1.24 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 8.02 | 2.24 | -9.06 | 212 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 150 | 34.7 | -3.86 | -3.45 | -4.83 | 70 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Hold SPY | benchmark | 95.26 | -4.74 | 0 | — | -4.66 | -1.53 | -6.91 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 94.77 | -5.23 | 8 | 50.0 | -6.30 | -0.30 | -18.69 | 6 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.18 | -1.47 | -8.74 | 148 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.00 | -6.34 | -6.42 | 23 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.49 | -7.51 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Copy: Insider buying | copy | 91.67 | -8.34 | 50 | 42.0 | -9.20 | -1.84 | -14.79 | 64 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.98 | -9.02 | 0 | — | -7.97 | -2.16 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.19 | -9.81 | 113 | 23.9 | -12.65 | -6.97 | -12.89 | 56 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.42 | -3.36 | -18.48 | 147 |
| 21 | Daily: Bullish score | daily | 87.69 | -12.31 | 17 | 17.6 | -4.97 | -0.73 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.03 | -8.99 | -16.08 | 70 |
| 24 | Opening range 30m | breakout | 85.09 | -14.91 | 442 | 33.5 | -10.43 | -3.30 | -14.16 | 563 |
| 25 | Agent | meta | 84.48 | -15.52 | 219 | 35.6 | -15.43 | -7.54 | -16.97 | 201 |
| 26 | Max aggression: 5-day momentum | meta | 81.35 | -18.65 | 21 | 42.9 | -46.54 | -3.04 | -55.24 | 21 |
| 27 | Parabolic SAR · 1h | trend | 81.30 | -18.70 | 188 | 28.2 | -24.37 | -6.90 | -26.97 | 202 |
| 28 | Agent (aggressive) | meta | 81.22 | -18.78 | 103 | 33.0 | -17.85 | -4.95 | -19.74 | 97 |
| 29 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.31 | -6.36 | -14.63 | 87 |
| 30 | Keltner breakout · 1h | breakout | 80.40 | -19.60 | 124 | 25.8 | -22.80 | -5.96 | -26.84 | 154 |
| 31 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -14.79 | -4.64 | -21.17 | 77 |
| 32 | Donchian 55/20 · 1h | breakout | 78.75 | -21.25 | 78 | 12.8 | -25.71 | -6.75 | -30.57 | 84 |
| 33 | Opening range 15m | breakout | 77.77 | -22.23 | 535 | 31.6 | -16.88 | -4.56 | -21.44 | 674 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.52 | -23.48 | 2 | 0.0 | -18.72 | -2.53 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 74.66 | -25.34 | 209 | 19.1 | -28.07 | -4.63 | -35.70 | 269 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.44 | -8.60 | -30.50 | 111 |
| 37 | Hold BTC | benchmark | 73.20 | -26.80 | 2 | 0.0 | -18.82 | -2.62 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.32 | -8.05 | -34.18 | 221 |
| 39 | Stochastic reversion · 1h | reversion | 71.98 | -28.02 | 350 | 42.3 | -35.40 | -5.41 | -35.58 | 426 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -41.87 | -2.61 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.69 | -28.31 | 189 | 15.9 | -32.34 | -5.46 | -39.50 | 202 |
| 42 | Triple EMA stack · 1h | trend | 71.10 | -28.90 | 155 | 14.8 | -31.35 | -6.31 | -37.28 | 177 |
| 43 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 178 | 14.6 | -30.93 | -5.59 | -37.80 | 198 |
| 44 | MACD zero-line · 1h | trend | 70.52 | -29.48 | 183 | 17.5 | -27.11 | -5.40 | -33.83 | 202 |
| 45 | MFI reversion · 1h | reversion | 69.90 | -30.10 | 443 | 33.6 | -28.13 | -4.21 | -30.08 | 164 |
| 46 | EMA 20/50 cross · 1h | trend | 69.70 | -30.30 | 116 | 10.3 | -36.02 | -9.27 | -40.11 | 117 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | Heikin-Ashi · 1h | trend | 68.84 | -31.16 | 474 | 23.0 | -45.59 | -10.08 | -45.78 | 635 |
| 49 | OBV trend · 1h | momentum | 68.71 | -31.29 | 310 | 19.4 | -35.43 | -7.59 | -39.85 | 255 |
| 50 | ROC + volume · 1h | momentum | 68.44 | -31.56 | 413 | 28.1 | -33.21 | -5.96 | -39.37 | 341 |
| 51 | MACD cross · 1h | trend | 66.97 | -33.03 | 416 | 22.1 | -41.46 | -6.74 | -46.35 | 484 |
| 52 | Donchian 20/10 · 1h | breakout | 66.96 | -33.04 | 161 | 18.0 | -35.32 | -6.59 | -41.18 | 199 |
| 53 | CCI reversion · 1h | reversion | 66.41 | -33.59 | 385 | 41.3 | -42.59 | -7.13 | -44.29 | 473 |
| 54 | Bollinger reversion · 1h | reversion | 63.58 | -36.42 | 346 | 37.6 | -39.17 | -5.99 | -39.60 | 413 |
| 55 | EMA 9/21 cross · 1h | trend | 63.08 | -36.92 | 283 | 11.0 | -40.49 | -7.97 | -46.48 | 322 |
| 56 | Williams %R · 1h | reversion | 62.85 | -37.15 | 436 | 40.6 | -47.38 | -8.33 | -47.60 | 563 |
| 57 | Agent (ML meta-label) | meta | 59.46 | -40.54 | 1917 | 24.5 | -24.43 | -4.63 | -24.43 | 288 |
| 58 | RSI(14) reversion · 1h | reversion | 58.26 | -41.74 | 206 | 32.0 | -41.84 | -6.27 | -43.36 | 250 |
| 59 | Z-score reversion · 1h | reversion | 57.05 | -42.95 | 226 | 35.0 | -37.65 | -5.24 | -39.62 | 253 |
| 60 | VWAP momentum · 1h | momentum | 55.76 | -44.24 | 975 | 21.7 | -55.72 | -11.18 | -59.24 | 1191 |
| 61 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.87 | -21.80 | -50.81 | 662 |
| 62 | Candlestick reversal · 1h | reversion | 54.63 | -45.37 | 552 | 26.4 | -47.85 | -8.83 | -48.28 | 638 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -43.74 | -99.04 | 5273 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.57 | -25.93 | -82.47 | 1401 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -41.88 | -93.94 | 2448 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.97 | -31.77 | -90.26 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.11 | -39.32 | -91.46 | 2284 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.08 | -31.52 | -90.10 | 2097 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -48.50 | -97.91 | 3462 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -53.76 | -96.43 | 3387 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.51 | -39.27 | -93.59 | 2211 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.51 | -34.78 | -82.76 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.52 | -99.61 | 6103 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.97 | -42.76 | -92.15 | 2539 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.93 | -39.38 | -94.95 | 3270 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.57 | -99.81 | 6171 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.48 | -44.03 | -92.62 | 2253 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.11 | -25.78 | -76.73 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -61.35 | -97.71 | 3424 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.08 | -58.35 | -99.08 | 4977 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.10 | -28.51 | -69.59 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -57.12 | -94.64 | 2744 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.49 | -38.28 | -84.84 | 1722 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.71 | -71.27 | -99.71 | 6391 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.06 | -31.47 | -91.06 | 2372 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.38 | -19.17 | -80.41 | 1850 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.61 | -37.10 | -91.61 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.61 | -46.41 | -97.61 | 3934 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -57.78 | -89.24 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.65 | -29.12 | -67.52 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.60 | -23.89 | -73.04 | 1217 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.90 | -18.39 | -81.90 | 1769 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.63 | -46.64 | -97.63 | 4336 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.86 | -99.94 | 8433 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T16:55 | Opening range 30m | buy | SQQQ | 21.28 | — | entry signal |
| 2026-11-18T16:50 | Agent (aggressive) | buy | SOXL | 40.89 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T16:50 | Agent | buy | SQQQ | 16.93 | — | following OBV trend |
| 2026-11-18T16:50 | Agent | buy | SOXL | 16.93 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T16:40 | Agent (ML meta-label) | sell | TSLA | 6.65 | -0.03 | selected signal exited |
| 2026-11-18T16:40 | Agent (ML meta-label) | sell | AAPL | 6.68 | -0.01 | selected signal exited |
| 2026-11-18T16:40 | CCI reversion · 1h | buy | TNA | 2.58 | — | entry |
| 2026-11-18T16:40 | CCI reversion · 1h | sell | ETH-USD | 2.33 | -0.05 | stop-loss |
| 2026-11-18T16:40 | Williams %R · 1h | sell | ETHU | 3.44 | -0.07 | stop-loss |
| 2026-11-18T16:40 | Williams %R · 1h | sell | ETH-USD | 1.75 | -0.04 | stop-loss |
| 2026-11-18T16:40 | Candlestick reversal · 1h | sell | ETHU | 2.86 | -0.17 | stop-loss |
| 2026-11-18T16:35 | Agent (ML meta-label) | buy | TECL | 6.64 | — | entry |
| 2026-11-18T16:35 | Agent (ML meta-label) | sell | IWM | 6.67 | -0.02 | selected signal exited |
| 2026-11-18T16:35 | MFI reversion · 1h | buy | ETHU | 11.72 | — | entry |
| 2026-11-18T16:30 | VWAP momentum · 1h | sell | TNA | 13.75 | -0.18 | exit signal |
| 2026-11-18T16:30 | VWAP momentum · 1h | sell | IWM | 14.04 | -0.06 | exit signal |
| 2026-11-18T16:30 | Heikin-Ashi · 1h | buy | AMZN | 17.24 | — | entry signal |
| 2026-11-18T16:30 | Heikin-Ashi · 1h | buy | AMD | 17.24 | — | entry signal |
| 2026-11-18T16:25 | VWAP momentum · 1h | sell | AMZN | 14.32 | 0.30 | target is flat |
| 2026-11-18T16:21 | Williams %R · 1h | buy | PLTR | 2.76 | — | entry |
| 2026-11-18T16:21 | Williams %R · 1h | buy | ETHU | 3.51 | — | entry |
| 2026-11-18T16:21 | Williams %R · 1h | sell | DOGE-USD | 3.14 | -0.06 | stop-loss |
| 2026-11-18T16:21 | Williams %R · 1h | sell | BTC-USD | 3.13 | -0.07 | stop-loss |
| 2026-11-18T16:21 | Stochastic reversion · 1h | sell | DOGE-USD | 4.50 | -0.10 | stop-loss |
| 2026-11-18T16:21 | Z-score reversion · 1h | buy | MSFT | 3.60 | — | rebalance up |
| 2026-11-18T16:21 | Z-score reversion · 1h | sell | ETHU | 4.17 | -0.28 | stop-loss |
| 2026-11-18T16:21 | Donchian 55/20 · 1h | sell | SOL-USD | 19.27 | -0.68 | stop-loss |
| 2026-11-18T16:21 | Ichimoku · 1h | sell | SOL-USD | 18.19 | -0.60 | stop-loss |
| 2026-11-18T16:21 | Opening range 15m | buy | SQQQ | 18.89 | — | entry signal |
| 2026-11-18T16:15 | Agent (rotation) | sell | AMZN | 7.83 | -0.01 | selected signal exited |
| 2026-11-18T16:15 | Agent (ML meta-label) | buy | SPY | 3.42 | — | rebalance up |
| 2026-11-18T16:15 | Agent (ML meta-label) | sell | ETHU | 3.43 | -0.02 | selected signal exited |
| 2026-11-18T16:15 | CCI reversion · 1h | buy | PLTR | 4.46 | — | entry |
| 2026-11-18T16:15 | CCI reversion · 1h | sell | BTC-USD | 4.71 | -0.06 | stop-loss |
| 2026-11-18T16:15 | Bollinger reversion · 1h | sell | BITX | 7.78 | -0.36 | stop-loss |
| 2026-11-18T16:15 | Candlestick reversal · 1h | sell | BITX | 2.85 | -0.08 | stop-loss |
| 2026-11-18T16:15 | Gap and go | sell | AMZN | 24.98 | -0.02 | exit signal |
| 2026-11-18T16:11 | Agent (ML meta-label) | buy | ETHU | 3.45 | — | entry |
| 2026-11-18T16:11 | Agent (ML meta-label) | sell | GOOGL | 3.45 | 0.00 | selected signal exited |
| 2026-11-18T16:11 | MFI reversion · 1h | sell | ETHU | 11.72 | -0.05 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 16:59:05.000120+00:00 -> 2026-11-18 17:09:05.000120+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 16:59:05.000120+00:00 -> 2026-11-18 17:09:05.000120+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
