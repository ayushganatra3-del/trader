# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-15T05:10:05.000116+00:00 · 60255 ticks

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
| Copy: Insider buying | 2026-11-14 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 4035 decisions in 807 calls, $0.0564 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-15T05:10 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-15T05:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-15T05:10 | 2 / 3 / 0 | XRP-USD 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 3.27 | +5.62% | 11 |
| Bollinger reversion | TSLA | 2.67 | +2.69% | 7 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| Z-score reversion | TQQQ | 2.19 | +4.95% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.89 | 17.89 | 0 | — | 15.31 | 5.07 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.92 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.99 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.58 | 1.81 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 1.00 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 2.98 | 1.86 | -4.12 | 86 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.72 | 1.89 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.22 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.33 | -1.67 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.12 | 1 | 0.0 | -3.27 | -2.15 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.69 | -3.31 | 191 | 30.4 | -3.13 | -1.09 | -8.46 | 150 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.35 | -3.65 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.38 | -1.27 | -14.79 | 60 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.41 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.27 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -16.15 | -6.15 | -17.77 | 69 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -17.21 | -4.23 | -19.46 | 159 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.30 | -0.70 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.64 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.98 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.23 | -7.14 | -15.23 | 195 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.13 | -3.25 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -15.54 | -4.36 | -16.69 | 93 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.39 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -17.99 | -6.32 | -18.11 | 112 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -14.40 | -3.35 | -23.29 | 89 |
| 32 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.02 | -3.43 | -25.39 | 165 |
| 33 | Stochastic reversion · 1h | reversion | 78.76 | -21.24 | 312 | 46.2 | -27.63 | -4.10 | -28.51 | 413 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.92 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 77.20 | -22.80 | 406 | 35.0 | -22.58 | -2.90 | -26.93 | 174 |
| 36 | ADX DI cross · 1h | trend | 76.45 | -23.55 | 200 | 20.0 | -23.76 | -3.54 | -32.73 | 267 |
| 37 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 38 | Hold BTC | benchmark | 75.67 | -24.33 | 2 | 0.0 | -16.92 | -2.45 | -28.91 | 1 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -26.69 | -6.13 | -31.58 | 117 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.62 | -4.70 | -30.71 | 234 |
| 41 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -20.15 | -0.61 | -57.50 | 41 |
| 42 | Heikin-Ashi · 1h | trend | 74.57 | -25.43 | 445 | 24.0 | -37.23 | -6.76 | -39.61 | 663 |
| 43 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.31 | -4.57 | -30.99 | 199 |
| 44 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.64 | -4.08 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.26 | -4.77 | -40.51 | 120 |
| 46 | Supertrend · 1h | trend | 71.95 | -28.05 | 182 | 14.8 | -29.22 | -4.95 | -36.83 | 207 |
| 47 | MACD cross · 1h | trend | 71.88 | -28.12 | 393 | 23.2 | -31.74 | -4.72 | -40.54 | 478 |
| 48 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.17 | -4.47 | -38.65 | 201 |
| 49 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -29.74 | -5.33 | -37.65 | 367 |
| 50 | Bollinger reversion · 1h | reversion | 70.86 | -29.14 | 311 | 40.5 | -35.94 | -5.65 | -36.99 | 399 |
| 51 | CCI reversion · 1h | reversion | 69.99 | -30.02 | 356 | 42.1 | -38.78 | -6.14 | -39.04 | 479 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -28.63 | -4.99 | -38.37 | 270 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.12 | -4.64 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -29.93 | -5.35 | -37.58 | 204 |
| 55 | Williams %R · 1h | reversion | 65.98 | -34.02 | 399 | 42.1 | -44.66 | -7.45 | -45.18 | 552 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -25.61 | -4.55 | -27.40 | 334 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -36.96 | -7.42 | -43.16 | 323 |
| 58 | VWAP momentum · 1h | momentum | 62.52 | -37.48 | 917 | 22.2 | -52.40 | -10.38 | -53.23 | 1234 |
| 59 | RSI(14) reversion · 1h | reversion | 61.25 | -38.75 | 197 | 31.5 | -39.60 | -5.87 | -40.40 | 249 |
| 60 | Candlestick reversal · 1h | reversion | 60.90 | -39.10 | 506 | 27.5 | -45.77 | -8.63 | -45.90 | 616 |
| 61 | Z-score reversion · 1h | reversion | 60.41 | -39.59 | 215 | 35.3 | -33.99 | -4.73 | -34.69 | 238 |
| 62 | Three white soldiers | momentum | 58.71 | -41.29 | 549 | 15.1 | -48.88 | -20.64 | -49.45 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.07 | -42.40 | -99.09 | 5355 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.38 | -25.75 | -80.74 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.64 | -43.12 | -93.66 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.78 | -31.90 | -90.16 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -39.75 | -91.47 | 2349 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.22 | -29.48 | -89.25 | 2155 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -49.91 | -97.93 | 3500 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -52.79 | -96.20 | 3456 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.42 | -31.65 | -93.45 | 2313 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.70 | -32.45 | -82.83 | 1651 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -50.51 | -99.60 | 6062 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.07 | -40.90 | -92.18 | 2621 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.98 | -34.58 | -94.98 | 3418 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -63.65 | -99.82 | 6177 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -42.50 | -92.55 | 2292 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.90 | -24.94 | -76.53 | 1664 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -55.29 | -97.54 | 3499 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -52.59 | -99.00 | 4964 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.75 | -26.92 | -68.76 | 1247 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -52.32 | -94.69 | 2797 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.70 | -36.17 | -84.98 | 1777 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -63.83 | -99.69 | 6395 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.03 | -29.78 | -91.15 | 2354 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.50 | -18.78 | -81.20 | 1829 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.13 | -35.67 | -91.26 | 2200 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.35 | -43.51 | -97.38 | 3912 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -52.99 | -89.52 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.63 | -28.74 | -65.71 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.34 | -22.42 | -71.63 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.37 | -17.80 | -81.90 | 1761 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.59 | -43.91 | -97.65 | 4371 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -88.54 | -99.93 | 8449 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-15T05:00 | Williams %R · 1h | sell | XRP-USD | 3.49 | 0.19 | exit signal |
| 2026-11-15T05:00 | Candlestick reversal · 1h | sell | ETH-USD | 3.54 | -0.05 | exit signal |
| 2026-11-15T05:00 | Candlestick reversal · 1h | sell | DOGE-USD | 3.36 | -0.03 | exit signal |
| 2026-11-15T05:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.96 | — | entry signal |
| 2026-11-15T05:00 | Heikin-Ashi · 1h | buy | BTC-USD | 6.22 | — | entry signal |
| 2026-11-15T05:00 | ADX DI cross · 1h | buy | XRP-USD | 19.13 | — | entry signal |
| 2026-11-15T05:00 | MACD cross · 1h | buy | DOGE-USD | 4.56 | — | entry signal |
| 2026-11-15T05:00 | Three white soldiers | sell | XRP-USD | 15.01 | 0.48 | exit signal |
| 2026-11-15T04:30 | RSI(14) reversion · 1h | buy | SOL-USD | 6.20 | — | rebalance up |
| 2026-11-15T04:30 | RSI(14) reversion · 1h | sell | XRP-USD | 7.82 | 0.39 | take-profit |
| 2026-11-15T04:00 | Supertrend · 1h | buy | XRP-USD | 10.28 | — | entry signal |
| 2026-11-15T04:00 | MACD cross · 1h | buy | XRP-USD | 10.30 | — | entry signal |
| 2026-11-15T04:00 | MACD cross · 1h | buy | SOL-USD | 10.30 | — | entry signal |
| 2026-11-15T04:00 | MACD cross · 1h | buy | ETH-USD | 10.30 | — | entry signal |
| 2026-11-15T04:00 | MACD cross · 1h | buy | BTC-USD | 10.30 | — | entry signal |
| 2026-11-15T03:35 | Three white soldiers | sell | ETH-USD | 14.61 | 0.05 | exit signal |
| 2026-11-15T03:30 | Three white soldiers | sell | SOL-USD | 14.63 | 0.07 | exit signal |
| 2026-11-15T03:20 | Candlestick reversal · 1h | buy | ETH-USD | 3.59 | — | entry |
| 2026-11-15T03:20 | Candlestick reversal · 1h | sell | XRP-USD | 4.26 | 0.20 | take-profit |
| 2026-11-15T03:00 | CCI reversion · 1h | buy | SOL-USD | 3.33 | — | entry signal |
| 2026-11-15T03:00 | CCI reversion · 1h | buy | ETH-USD | 3.33 | — | entry signal |
| 2026-11-15T03:00 | CCI reversion · 1h | buy | DOGE-USD | 3.33 | — | entry signal |
| 2026-11-15T03:00 | CCI reversion · 1h | buy | BTC-USD | 3.33 | — | entry signal |
| 2026-11-15T03:00 | Williams %R · 1h | buy | SOL-USD | 3.30 | — | entry signal |
| 2026-11-15T03:00 | Williams %R · 1h | buy | BTC-USD | 3.30 | — | entry signal |
| 2026-11-15T03:00 | VWAP reversion · 1h | sell | XRP-USD | 23.69 | 0.85 | exit signal |
| 2026-11-15T03:00 | VWAP reversion · 1h | sell | ETH-USD | 23.30 | 0.45 | exit signal |
| 2026-11-15T03:00 | Z-score reversion · 1h | buy | XRP-USD | 10.09 | — | entry signal |
| 2026-11-15T03:00 | Z-score reversion · 1h | buy | SOL-USD | 10.09 | — | entry signal |
| 2026-11-15T03:00 | Z-score reversion · 1h | buy | ETH-USD | 10.09 | — | entry signal |
| 2026-11-15T03:00 | Z-score reversion · 1h | buy | DOGE-USD | 10.09 | — | entry signal |
| 2026-11-15T03:00 | Z-score reversion · 1h | buy | BTC-USD | 10.09 | — | entry signal |
| 2026-11-15T03:00 | RSI(14) reversion · 1h | buy | SOL-USD | 2.60 | — | entry signal |
| 2026-11-15T03:00 | RSI(14) reversion · 1h | buy | ETH-USD | 7.67 | — | entry signal |
| 2026-11-15T03:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 7.67 | — | entry signal |
| 2026-11-15T03:00 | RSI(14) reversion · 1h | buy | BTC-USD | 7.67 | — | entry signal |
| 2026-11-15T03:00 | RSI(14) reversion · 1h | sell | XRP-USD | 8.00 | 0.22 | rebalance down |
| 2026-11-15T03:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.39 | — | entry signal |
| 2026-11-15T03:00 | Candlestick reversal · 1h | buy | BTC-USD | 3.39 | — | entry signal |
| 2026-11-15T03:00 | VWAP momentum · 1h | buy | BTC-USD | 3.13 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-17 05:10:05.000116+00:00 -> 2026-11-15 05:20:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
