# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T20:06:05.000155+00:00 · 63546 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.63 (-15.37%)

Closed trades 217, win rate 35.5%, fees £6.04, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 36525 decisions in 3147 calls, $0.4538 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T20:06 | 0 / 13 / 18 | cash |  |
| Breezy | 2026-11-17T20:06 | 0 / 21 / 10 | cash |  |
| Boozy | 2026-11-17T20:06 | 3 / 21 / 7 | MSTR 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.42 | 17.42 | 0 | — | 15.54 | 5.42 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.10 | 12.11 | 24 | 62.5 | 17.67 | 3.54 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.83 | 2.83 | 0 | — | 5.35 | 1.48 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.99 | 2.21 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -2.98 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 38 | 39.5 | -2.00 | -0.33 | -9.74 | 35 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.00 | -5.00 | 8 | 50.0 | -5.20 | -0.26 | -18.69 | 6 |
| 12 | Hold SPY | benchmark | 94.98 | -5.02 | 0 | — | -4.31 | -1.40 | -6.90 | 1 |
| 13 | Agent (rotation) | meta | 94.26 | -5.74 | 197 | 29.9 | -3.63 | -1.24 | -9.44 | 157 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.21 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.18 | -7.82 | 0 | — | -8.40 | -2.20 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.48 | -7.89 | -9.65 | 23 |
| 17 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 18 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -11.35 | -5.42 | -13.38 | 60 |
| 19 | Copy: Congress Democrats (NANC) | copy | 90.15 | -9.85 | 0 | — | -8.65 | -2.34 | -12.67 | 1 |
| 20 | Copy: Insider buying | copy | 90.09 | -9.91 | 50 | 42.0 | -9.12 | -1.81 | -14.79 | 62 |
| 21 | Daily: Bullish score | daily | 87.51 | -12.49 | 17 | 17.6 | -4.58 | -0.70 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -14.50 | -4.97 | -19.20 | 77 |
| 24 | Opening range 30m | breakout | 86.53 | -13.47 | 438 | 33.6 | -8.88 | -2.78 | -14.11 | 570 |
| 25 | Agent | meta | 84.63 | -15.37 | 217 | 35.5 | -15.54 | -7.45 | -17.38 | 207 |
| 26 | Agent (aggressive) | meta | 81.95 | -18.05 | 102 | 33.3 | -17.76 | -4.90 | -20.39 | 100 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.23 | -7.18 | -27.99 | 203 |
| 28 | Max aggression: 5-day momentum | meta | 81.35 | -18.65 | 21 | 42.9 | -47.01 | -3.05 | -55.24 | 22 |
| 29 | Keltner breakout · 1h | breakout | 81.14 | -18.86 | 122 | 26.2 | -19.69 | -4.50 | -27.13 | 153 |
| 30 | Connors RSI(2) · 1h | reversion | 80.32 | -19.68 | 215 | 40.0 | -14.44 | -6.37 | -14.85 | 93 |
| 31 | Volume breakout · 1h | breakout | 80.08 | -19.91 | 162 | 28.4 | -15.33 | -4.73 | -22.20 | 79 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.51 | -29.47 | 83 |
| 33 | Opening range 15m | breakout | 78.42 | -21.58 | 533 | 31.5 | -15.92 | -4.23 | -21.37 | 680 |
| 34 | Max aggression: 1-day momentum | meta | 78.04 | -21.96 | 30 | 26.7 | -22.84 | -0.82 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 76.18 | -23.82 | 2 | 0.0 | -18.77 | -2.51 | -26.43 | 1 |
| 36 | ADX DI cross · 1h | trend | 75.41 | -24.59 | 208 | 19.2 | -26.87 | -4.28 | -35.42 | 262 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -28.72 | -8.32 | -29.33 | 109 |
| 38 | Hold BTC | benchmark | 74.37 | -25.63 | 2 | 0.0 | -16.51 | -2.35 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.06 | -5.68 | -33.32 | 221 |
| 40 | Stochastic reversion · 1h | reversion | 72.33 | -27.67 | 345 | 42.6 | -35.04 | -5.29 | -36.02 | 424 |
| 41 | Supertrend · 1h | trend | 71.76 | -28.24 | 189 | 15.9 | -31.99 | -5.40 | -39.67 | 200 |
| 42 | RSI momentum · 1h | momentum | 71.31 | -28.68 | 176 | 14.2 | -30.92 | -5.58 | -37.58 | 197 |
| 43 | Triple EMA stack · 1h | trend | 71.27 | -28.73 | 155 | 14.8 | -32.40 | -6.52 | -38.02 | 182 |
| 44 | MACD zero-line · 1h | trend | 70.92 | -29.08 | 181 | 17.7 | -26.75 | -5.31 | -33.31 | 202 |
| 45 | MFI reversion · 1h | reversion | 70.34 | -29.66 | 430 | 33.7 | -28.36 | -4.21 | -30.55 | 164 |
| 46 | EMA 20/50 cross · 1h | trend | 70.15 | -29.85 | 115 | 10.4 | -35.97 | -9.98 | -39.15 | 114 |
| 47 | Heikin-Ashi · 1h | trend | 69.94 | -30.06 | 466 | 23.0 | -42.76 | -8.97 | -44.75 | 632 |
| 48 | ROC + volume · 1h | momentum | 69.72 | -30.28 | 408 | 28.2 | -30.52 | -4.97 | -39.54 | 354 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 50 | MACD cross · 1h | trend | 69.18 | -30.82 | 413 | 22.3 | -39.29 | -6.36 | -44.56 | 472 |
| 51 | OBV trend · 1h | momentum | 68.60 | -31.40 | 306 | 19.0 | -35.30 | -7.53 | -39.68 | 254 |
| 52 | Donchian 20/10 · 1h | breakout | 67.57 | -32.43 | 159 | 18.2 | -32.40 | -5.42 | -40.92 | 201 |
| 53 | CCI reversion · 1h | reversion | 66.15 | -33.85 | 382 | 41.6 | -41.77 | -6.83 | -44.29 | 469 |
| 54 | Bollinger reversion · 1h | reversion | 63.70 | -36.30 | 344 | 37.8 | -38.72 | -5.81 | -39.42 | 414 |
| 55 | EMA 9/21 cross · 1h | trend | 63.39 | -36.61 | 280 | 11.1 | -40.43 | -7.60 | -47.20 | 323 |
| 56 | Williams %R · 1h | reversion | 62.34 | -37.66 | 430 | 40.7 | -46.24 | -7.86 | -46.88 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.05 | -39.95 | 1898 | 24.4 | -29.14 | -4.70 | -29.65 | 297 |
| 58 | RSI(14) reversion · 1h | reversion | 57.69 | -42.31 | 205 | 31.7 | -41.24 | -6.04 | -43.30 | 254 |
| 59 | VWAP momentum · 1h | momentum | 56.83 | -43.17 | 958 | 21.6 | -53.53 | -9.44 | -58.55 | 1188 |
| 60 | Z-score reversion · 1h | reversion | 56.65 | -43.35 | 224 | 35.3 | -37.89 | -5.22 | -39.23 | 255 |
| 61 | Three white soldiers | momentum | 55.09 | -44.91 | 584 | 14.6 | -49.62 | -21.49 | -50.22 | 660 |
| 62 | Candlestick reversal · 1h | reversion | 54.67 | -45.34 | 546 | 26.6 | -47.39 | -8.53 | -48.30 | 643 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -41.51 | -99.04 | 5259 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.81 | -25.06 | -82.09 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.06 | -39.66 | -94.07 | 2474 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.25 | -31.21 | -90.42 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.63 | -38.15 | -91.64 | 2301 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.87 | -30.53 | -89.90 | 2114 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.92 | -45.81 | -97.93 | 3483 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -51.05 | -96.53 | 3402 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.41 | -37.09 | -93.49 | 2224 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.21 | -31.84 | -83.21 | 1607 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.37 | -99.60 | 6086 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.15 | -40.62 | -92.16 | 2563 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.97 | -37.83 | -95.00 | 3296 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -64.69 | -99.81 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -42.05 | -92.48 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.54 | -25.52 | -76.57 | 1642 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -56.92 | -97.68 | 3431 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -53.75 | -99.02 | 4947 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.72 | -27.03 | -68.74 | 1225 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -52.55 | -94.63 | 2738 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.50 | -36.26 | -84.52 | 1717 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -64.44 | -99.70 | 6382 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.78 | -30.21 | -90.90 | 2358 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.69 | -18.59 | -79.95 | 1837 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.24 | -35.24 | -91.27 | 2163 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.56 | -44.54 | -97.57 | 3912 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -55.00 | -89.49 | 2167 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.12 | -29.76 | -66.12 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.25 | -22.75 | -72.51 | 1226 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.61 | -17.73 | -80.79 | 1725 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -44.94 | -97.60 | 4347 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.05 | -99.94 | 8434 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T20:05 | Agent (ML meta-label) | buy | SPY | 15.02 | — | entry |
| 2026-11-17T20:05 | Agent (ML meta-label) | buy | MSTR | 15.02 | — | entry |
| 2026-11-17T20:05 | Agent (ML meta-label) | sell | SQQQ | 15.00 | -0.02 | selected signal exited |
| 2026-11-17T20:00 | Agent (ML meta-label) | buy | SQQQ | 15.02 | — | entry |
| 2026-11-17T20:00 | Agent (ML meta-label) | sell | SPY | 10.21 | -0.02 | selected signal exited |
| 2026-11-17T20:00 | Z-score reversion · 1h | buy | COIN | 2.84 | — | entry |
| 2026-11-17T20:00 | Z-score reversion · 1h | sell | ETHU | 2.84 | -0.06 | rebalance down |
| 2026-11-17T20:00 | OBV trend · 1h | buy | SOL-USD | 17.16 | — | entry signal |
| 2026-11-17T20:00 | VWAP momentum · 1h | buy | XRP-USD | 14.15 | — | entry signal |
| 2026-11-17T20:00 | VWAP momentum · 1h | buy | SOL-USD | 14.24 | — | entry signal |
| 2026-11-17T20:00 | VWAP momentum · 1h | buy | DOGE-USD | 14.24 | — | entry signal |
| 2026-11-17T20:00 | Triple EMA stack · 1h | buy | SOL-USD | 17.83 | — | entry signal |
| 2026-11-17T19:56 | Agent (ML meta-label) | buy | SPY | 10.23 | — | entry |
| 2026-11-17T19:56 | Agent (ML meta-label) | sell | TSLA | 15.02 | -0.01 | selected signal exited |
| 2026-11-17T19:56 | Agent (aggressive) | sell | COIN | 40.90 | -0.16 | selected signal exited |
| 2026-11-17T19:56 | Agent | sell | COIN | 16.87 | -0.06 | selected signal exited |
| 2026-11-17T19:50 | Agent (ML meta-label) | buy | TSLA | 15.03 | — | entry |
| 2026-11-17T19:50 | Agent (ML meta-label) | sell | SQQQ | 15.07 | 0.05 | selected signal exited |
| 2026-11-17T19:45 | Agent (ML meta-label) | buy | SQQQ | 15.02 | — | entry |
| 2026-11-17T19:45 | Agent (ML meta-label) | sell | SPY | 3.06 | -0.00 | selected signal exited |
| 2026-11-17T19:45 | Agent (ML meta-label) | sell | MSTR | 15.02 | -0.00 | selected signal exited |
| 2026-11-17T19:40 | Agent (ML meta-label) | buy | SPY | 3.06 | — | entry |
| 2026-11-17T19:40 | Agent (ML meta-label) | buy | MSTR | 15.02 | — | entry |
| 2026-11-17T19:30 | Connors RSI(2) · 1h | buy | AAPL | 20.08 | — | entry signal |
| 2026-11-17T19:30 | Keltner breakout · 1h | buy | SQQQ | 20.24 | — | entry signal |
| 2026-11-17T19:30 | VWAP momentum · 1h | buy | SQQQ | 14.21 | — | entry signal |
| 2026-11-17T19:30 | MACD cross · 1h | buy | ETHU | 17.28 | — | entry signal |
| 2026-11-17T19:30 | MACD cross · 1h | buy | BITX | 17.28 | — | entry signal |
| 2026-11-17T19:15 | Agent (ML meta-label) | sell | SQQQ | 14.94 | -0.11 | selected signal exited |
| 2026-11-17T19:10 | Agent (ML meta-label) | buy | SQQQ | 15.04 | — | entry |
| 2026-11-17T19:10 | Agent (aggressive) | buy | COIN | 41.05 | — | following MACD cross |
| 2026-11-17T19:10 | Agent | buy | COIN | 16.94 | — | following MACD cross |
| 2026-11-17T19:10 | MFI reversion · 1h | buy | GOOGL | 7.05 | — | entry |
| 2026-11-17T19:07 | Agent (ML meta-label) | sell | SPY | 15.04 | -0.01 | selected signal exited |
| 2026-11-17T19:05 | Agent (ML meta-label) | buy | SPY | 15.05 | — | entry |
| 2026-11-17T19:05 | Agent (ML meta-label) | sell | SQQQ | 15.04 | -0.00 | selected signal exited |
| 2026-11-17T19:01 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 98.44 | — | entry |
| 2026-11-17T19:01 | Agent (ML meta-label) | buy | SQQQ | 15.05 | — | entry |
| 2026-11-17T19:01 | Agent | sell | BITX | 16.96 | 0.02 | selected signal exited |
| 2026-11-17T19:01 | MFI reversion · 1h | buy | SPY | 4.08 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 20:06:05.000155+00:00 -> 2026-11-17 20:16:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 20:06:05.000155+00:00 -> 2026-11-17 20:16:05.000155+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
