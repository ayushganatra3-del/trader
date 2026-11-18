# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T18:26:05.000188+00:00 · 64724 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.83 (-15.17%)

Closed trades 223, win rate 35.9%, fees £6.14, max drawdown -17.33%.

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

Today: 28977 decisions in 2886 calls, $0.3653 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T18:26 | 6 / 18 / 6 | MSTR 16% |  |
| Breezy | 2026-11-18T18:26 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-18T18:26 | 5 / 24 / 1 | MSTR 79% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.96 | 14.96 | 0 | — | 12.78 | 4.41 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.27 | 4.27 | 0 | — | 5.34 | 1.39 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.50 | 0.50 | 150 | 34.7 | -3.26 | -2.78 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 7.96 | 2.22 | -9.06 | 214 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.62 | -3.38 | 8 | 50.0 | -4.04 | -0.10 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.83 | -4.17 | 0 | — | -4.08 | -1.33 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.20 | -1.48 | -8.74 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.26 | -8.34 | -5.84 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.48 | -7.52 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Insider buying | copy | 91.62 | -8.38 | 50 | 42.0 | -9.44 | -1.89 | -14.79 | 64 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.16 | -8.84 | 0 | — | -7.49 | -2.01 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.31 | -9.69 | 113 | 23.9 | -12.53 | -6.90 | -12.89 | 56 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.42 | -3.36 | -18.48 | 147 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.12 | -12.88 | 17 | 17.6 | -5.44 | -0.83 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.00 | -8.98 | -16.05 | 70 |
| 24 | Opening range 30m | breakout | 84.87 | -15.13 | 443 | 33.4 | -10.67 | -3.36 | -14.63 | 566 |
| 25 | Agent | meta | 84.83 | -15.17 | 223 | 35.9 | -15.16 | -7.36 | -17.06 | 201 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 104 | 33.7 | -15.70 | -4.17 | -19.74 | 97 |
| 27 | Parabolic SAR · 1h | trend | 81.69 | -18.31 | 188 | 28.2 | -24.31 | -6.72 | -27.42 | 200 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.31 | -6.36 | -14.63 | 87 |
| 29 | Keltner breakout · 1h | breakout | 79.84 | -20.16 | 124 | 25.8 | -25.43 | -6.94 | -28.03 | 156 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -15.63 | -5.02 | -21.17 | 77 |
| 31 | Max aggression: 5-day momentum | meta | 79.14 | -20.86 | 21 | 42.9 | -47.99 | -3.21 | -55.24 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 79.10 | -20.89 | 78 | 12.8 | -25.37 | -6.66 | -30.57 | 84 |
| 33 | Opening range 15m | breakout | 77.65 | -22.34 | 536 | 31.5 | -17.06 | -4.60 | -21.54 | 676 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.51 | -22.48 | 2 | 0.0 | -17.71 | -2.35 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.06 | -24.94 | 209 | 19.1 | -27.29 | -4.48 | -35.39 | 269 |
| 36 | Hold BTC | benchmark | 74.16 | -25.84 | 2 | 0.0 | -17.66 | -2.47 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 38 | Stochastic reversion · 1h | reversion | 73.12 | -26.88 | 350 | 42.3 | -34.17 | -5.19 | -35.59 | 426 |
| 39 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -31.09 | -8.37 | -34.15 | 218 |
| 40 | Supertrend · 1h | trend | 71.84 | -28.16 | 191 | 16.2 | -32.15 | -5.43 | -39.50 | 202 |
| 41 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -39.50 | -2.42 | -57.50 | 39 |
| 42 | Triple EMA stack · 1h | trend | 70.95 | -29.05 | 156 | 14.7 | -31.53 | -6.33 | -37.58 | 176 |
| 43 | MFI reversion · 1h | reversion | 70.73 | -29.27 | 447 | 33.6 | -26.95 | -3.99 | -30.08 | 171 |
| 44 | RSI momentum · 1h | momentum | 70.32 | -29.68 | 179 | 14.5 | -32.20 | -5.89 | -39.00 | 199 |
| 45 | MACD zero-line · 1h | trend | 69.83 | -30.17 | 184 | 17.9 | -27.77 | -5.55 | -33.89 | 202 |
| 46 | EMA 20/50 cross · 1h | trend | 69.49 | -30.51 | 116 | 10.3 | -36.46 | -9.43 | -40.47 | 116 |
| 47 | Heikin-Ashi · 1h | trend | 69.48 | -30.52 | 474 | 23.0 | -44.99 | -9.90 | -45.81 | 633 |
| 48 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 49 | ROC + volume · 1h | momentum | 68.57 | -31.43 | 413 | 28.1 | -34.11 | -6.24 | -39.35 | 342 |
| 50 | OBV trend · 1h | momentum | 68.30 | -31.70 | 310 | 19.4 | -35.49 | -7.59 | -40.30 | 253 |
| 51 | MACD cross · 1h | trend | 67.91 | -32.09 | 417 | 22.3 | -40.42 | -6.63 | -46.40 | 488 |
| 52 | CCI reversion · 1h | reversion | 67.39 | -32.61 | 386 | 41.5 | -42.08 | -7.06 | -44.29 | 473 |
| 53 | Donchian 20/10 · 1h | breakout | 66.53 | -33.47 | 162 | 17.9 | -36.72 | -6.99 | -41.57 | 199 |
| 54 | Bollinger reversion · 1h | reversion | 64.10 | -35.90 | 348 | 37.9 | -38.56 | -5.86 | -39.58 | 417 |
| 55 | Williams %R · 1h | reversion | 63.78 | -36.22 | 436 | 40.6 | -46.59 | -8.14 | -47.62 | 572 |
| 56 | EMA 9/21 cross · 1h | trend | 63.06 | -36.94 | 284 | 11.3 | -40.33 | -7.92 | -46.40 | 323 |
| 57 | Agent (ML meta-label) | meta | 60.15 | -39.85 | 1925 | 24.5 | -29.16 | -4.93 | -30.57 | 300 |
| 58 | RSI(14) reversion · 1h | reversion | 59.14 | -40.86 | 206 | 32.0 | -41.29 | -6.14 | -43.22 | 258 |
| 59 | Z-score reversion · 1h | reversion | 57.80 | -42.20 | 227 | 35.2 | -36.56 | -5.04 | -39.63 | 257 |
| 60 | VWAP momentum · 1h | momentum | 55.37 | -44.63 | 975 | 21.7 | -56.10 | -11.16 | -59.84 | 1203 |
| 61 | Candlestick reversal · 1h | reversion | 55.35 | -44.65 | 552 | 26.4 | -47.29 | -8.65 | -48.88 | 641 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.66 | -21.86 | -50.71 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -43.93 | -99.03 | 5284 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.51 | -25.85 | -82.56 | 1406 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.70 | -42.14 | -93.95 | 2459 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.89 | -31.54 | -90.31 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.99 | -38.46 | -91.44 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.06 | -90.10 | 2089 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -47.70 | -97.92 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -52.45 | -96.42 | 3379 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.60 | -39.05 | -93.60 | 2208 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.50 | -34.54 | -82.80 | 1590 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -55.13 | -99.61 | 6106 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.93 | -42.68 | -92.15 | 2555 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.87 | -39.36 | -94.89 | 3250 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.12 | -99.81 | 6195 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.38 | -42.93 | -92.66 | 2270 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.54 | -26.16 | -76.22 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -61.32 | -97.71 | 3427 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.05 | -58.36 | -99.07 | 4968 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.74 | -29.42 | -70.15 | 1236 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -57.30 | -94.69 | 2759 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -38.13 | -85.06 | 1736 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.05 | -99.70 | 6382 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.85 | -31.23 | -91.04 | 2370 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.85 | -18.89 | -80.35 | 1839 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.44 | -36.79 | -91.59 | 2167 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.57 | -46.36 | -97.60 | 3920 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.25 | -59.04 | -89.29 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.15 | -30.10 | -67.04 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.75 | -24.50 | -73.12 | 1219 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.51 | -18.36 | -81.88 | 1769 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -46.32 | -97.60 | 4324 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.81 | -99.94 | 8445 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T18:25 | MFI reversion · 1h | buy | TNA | 5.89 | — | entry |
| 2026-11-18T18:25 | MFI reversion · 1h | sell | ETHU | 5.91 | -0.03 | target is flat |
| 2026-11-18T18:15 | Agent (ML meta-label) | sell | AAPL | 6.01 | -0.01 | selected signal exited |
| 2026-11-18T18:10 | Agent | sell | SPY | 16.91 | -0.07 | selected signal exited |
| 2026-11-18T18:00 | Agent (ML meta-label) | buy | AAPL | 6.02 | — | entry |
| 2026-11-18T18:00 | MFI reversion · 1h | buy | ETH-USD | 4.70 | — | entry signal |
| 2026-11-18T18:00 | MFI reversion · 1h | buy | DOGE-USD | 5.89 | — | entry signal |
| 2026-11-18T18:00 | MFI reversion · 1h | buy | BTC-USD | 5.89 | — | entry signal |
| 2026-11-18T18:00 | MFI reversion · 1h | sell | MSTR | 7.08 | -0.01 | target is flat |
| 2026-11-18T18:00 | MFI reversion · 1h | sell | MSFT | 4.25 | -0.00 | rebalance down |
| 2026-11-18T18:00 | MFI reversion · 1h | sell | ETHU | 4.17 | -0.03 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | SOL-USD | 7.11 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | ETH-USD | 7.12 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | DOGE-USD | 7.12 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | BTC-USD | 7.12 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | UPRO | 5.64 | -0.03 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | TNA | 5.68 | 0.03 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | SPY | 5.71 | -0.00 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | MSFT | 5.74 | -0.01 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | IWM | 5.72 | 0.02 | rebalance down |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | UPRO | 3.94 | — | entry |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | SPY | 3.94 | — | entry |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | PLTR | 3.94 | — | entry |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | ETH-USD | 3.94 | — | entry signal |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | BTC-USD | 3.94 | — | entry signal |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | sell | TQQQ | 3.49 | 0.06 | rebalance down |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | sell | TNA | 3.46 | 0.04 | rebalance down |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | sell | QQQ | 3.43 | 0.03 | rebalance down |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | sell | NVDA | 3.28 | -0.09 | rebalance down |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | sell | IWM | 3.42 | 0.03 | rebalance down |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | sell | GOOGL | 3.36 | -0.00 | rebalance down |
| 2026-11-18T18:00 | Candlestick reversal · 1h | buy | SOL-USD | 1.98 | — | entry signal |
| 2026-11-18T17:55 | Agent (ML meta-label) | sell | TSLA | 2.16 | 0.00 | selected signal exited |
| 2026-11-18T17:55 | Agent (ML meta-label) | sell | AAPL | 4.63 | -0.00 | selected signal exited |
| 2026-11-18T17:50 | Agent (ML meta-label) | buy | TSLA | 2.16 | — | following Stochastic reversion |
| 2026-11-18T17:50 | Agent (ML meta-label) | sell | ETHU | 2.16 | -0.01 | selected signal exited |
| 2026-11-18T17:50 | MFI reversion · 1h | buy | QQQ | 7.08 | — | entry |
| 2026-11-18T17:50 | MFI reversion · 1h | buy | MSTR | 3.80 | — | rebalance up |
| 2026-11-18T17:50 | MFI reversion · 1h | buy | META | 7.08 | — | entry |
| 2026-11-18T17:50 | MFI reversion · 1h | sell | SPY | 4.73 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 18:26:05.000188+00:00 -> 2026-11-18 18:36:05.000188+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 18:26:05.000188+00:00 -> 2026-11-18 18:36:05.000188+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
