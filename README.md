# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T08:25:05.000134+00:00 · 49459 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.46 (-11.54%)

Closed trades 148, win rate 37.2%, fees £4.17, max drawdown -11.95%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 38.26 · VIX 28.18 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 6582 decisions in 1317 calls, $0.0920 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T08:25 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-06T08:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T08:25 | 3 / 2 / 0 | ETH-USD 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.17 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.96 | 11.96 | 0 | — | 13.22 | 4.52 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.06 | 0.61 | -9.63 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.53 | -0.47 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.34 | -1.66 | 111 | 44.1 | -13.64 | -3.31 | -14.25 | 149 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Agent (rotation) | meta | 95.20 | -4.80 | 175 | 28.0 | -6.68 | -3.77 | -10.36 | 173 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 14 | Hold SPY | benchmark | 94.11 | -5.89 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.15 | -1.39 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.30 | -7.70 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 90.93 | -9.07 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.27 | -9.73 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.17 | -10.83 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.65 | -14.68 | 86 |
| 24 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 25 | Hold BTC | benchmark | 87.99 | -12.01 | 1 | 0.0 | -5.39 | -0.68 | -13.78 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.64 | -12.36 | 166 | 27.1 | -14.67 | -3.22 | -20.02 | 241 |
| 27 | Donchian 55/20 · 1h | breakout | 86.70 | -13.30 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.69 | -13.31 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.80 | -17.20 | 144 | 27.8 | -15.84 | -3.55 | -21.39 | 101 |
| 33 | Keltner breakout · 1h | breakout | 82.06 | -17.95 | 106 | 23.6 | -21.54 | -4.42 | -24.41 | 173 |
| 34 | Stochastic reversion · 1h | reversion | 81.41 | -18.59 | 255 | 46.7 | -28.71 | -4.47 | -29.25 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.76 | -19.24 | 203 | 39.9 | -20.51 | -6.77 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -23.75 | -3.93 | -26.36 | 262 |
| 38 | Bollinger breakout · 1h | breakout | 79.24 | -20.76 | 165 | 23.6 | -22.07 | -4.55 | -26.52 | 245 |
| 39 | Ichimoku · 1h | trend | 78.77 | -21.23 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 40 | MFI reversion · 1h | reversion | 78.76 | -21.23 | 328 | 33.8 | -19.46 | -2.81 | -20.96 | 153 |
| 41 | CCI reversion · 1h | reversion | 77.52 | -22.48 | 284 | 45.8 | -29.76 | -4.82 | -30.70 | 451 |
| 42 | Heikin-Ashi · 1h | trend | 77.01 | -22.99 | 386 | 23.1 | -42.69 | -8.93 | -43.30 | 670 |
| 43 | EMA 20/50 cross · 1h | trend | 76.62 | -23.38 | 102 | 10.8 | -22.75 | -4.07 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.10 | -24.90 | 142 | 14.8 | -29.39 | -6.13 | -33.06 | 207 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.67 | -5.51 | -29.20 | 212 |
| 46 | RSI momentum · 1h | momentum | 74.09 | -25.91 | 158 | 12.7 | -27.86 | -5.27 | -32.33 | 220 |
| 47 | Supertrend · 1h | trend | 74.06 | -25.94 | 166 | 13.3 | -29.83 | -5.14 | -34.26 | 217 |
| 48 | MACD cross · 1h | trend | 73.27 | -26.73 | 334 | 23.1 | -36.32 | -6.40 | -38.81 | 477 |
| 49 | Z-score reversion · 1h | reversion | 72.87 | -27.13 | 160 | 35.6 | -28.69 | -4.46 | -28.88 | 226 |
| 50 | Donchian 20/10 · 1h | breakout | 72.45 | -27.55 | 140 | 20.0 | -29.12 | -5.32 | -34.25 | 212 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.45 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 72.05 | -27.95 | 244 | 38.9 | -34.09 | -6.26 | -34.52 | 375 |
| 53 | Williams %R · 1h | reversion | 71.87 | -28.13 | 310 | 44.8 | -39.37 | -6.56 | -39.71 | 528 |
| 54 | ROC + volume · 1h | momentum | 71.65 | -28.35 | 344 | 25.6 | -37.53 | -7.30 | -37.97 | 384 |
| 55 | OBV trend · 1h | momentum | 71.45 | -28.55 | 266 | 17.3 | -32.45 | -6.89 | -33.83 | 294 |
| 56 | VWAP momentum · 1h | momentum | 68.21 | -31.79 | 760 | 22.2 | -55.67 | -12.26 | -56.28 | 1216 |
| 57 | EMA 9/21 cross · 1h | trend | 68.11 | -31.89 | 241 | 10.0 | -39.26 | -8.01 | -39.93 | 335 |
| 58 | RSI(14) reversion · 1h | reversion | 66.21 | -33.79 | 142 | 27.5 | -28.38 | -4.40 | -31.29 | 204 |
| 59 | Three white soldiers | momentum | 66.21 | -33.79 | 453 | 16.1 | -47.84 | -21.95 | -47.84 | 635 |
| 60 | Agent (ML meta-label) | meta | 65.25 | -34.75 | 1508 | 22.3 | -9.53 | -1.27 | -20.83 | 326 |
| 61 | Candlestick reversal · 1h | reversion | 65.00 | -35.00 | 396 | 28.5 | -38.82 | -7.17 | -39.04 | 564 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.10 | -98.94 | 5138 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.21 | -25.46 | -80.27 | 1406 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.28 | -47.02 | -93.32 | 2488 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.11 | -31.19 | -89.16 | 1896 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.65 | -39.18 | -90.73 | 2282 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.24 | -31.11 | -90.33 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -53.28 | -97.69 | 3430 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -58.71 | -96.13 | 3344 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -32.11 | -93.54 | 2420 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.60 | -35.83 | -81.84 | 1629 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -52.62 | -99.51 | 5942 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.48 | -42.60 | -92.55 | 2577 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.73 | -36.45 | -95.75 | 3405 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -68.98 | -99.80 | 6127 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.62 | -42.93 | -91.64 | 2247 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.90 | -26.66 | -75.05 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -60.34 | -97.66 | 3478 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -59.15 | -98.77 | 4842 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.31 | -28.43 | -70.08 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.46 | -53.04 | -94.50 | 2731 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -36.56 | -84.79 | 1769 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -70.11 | -99.64 | 6317 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.08 | -30.64 | -89.10 | 2271 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.52 | -19.27 | -77.74 | 1732 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.03 | -36.22 | -91.06 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.59 | -51.06 | -96.59 | 3838 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -56.17 | -89.51 | 2162 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.49 | -27.61 | -65.85 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.40 | -24.44 | -73.80 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.53 | -17.94 | -78.62 | 1663 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -48.39 | -97.27 | 4306 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.20 | -99.93 | 8197 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T08:02 | MACD cross · 1h | sell | SOL-USD | 3.65 | -0.02 | rebalance down |
| 2026-11-06T08:00 | MACD cross · 1h | buy | ETH-USD | 14.65 | — | entry signal |
| 2026-11-06T08:00 | MACD cross · 1h | buy | BTC-USD | 14.65 | — | entry signal |
| 2026-11-06T08:00 | MACD cross · 1h | sell | DOGE-USD | 3.66 | -0.01 | rebalance down |
| 2026-11-06T07:00 | MFI reversion · 1h | buy | BTC-USD | 11.24 | — | entry signal |
| 2026-11-06T07:00 | MFI reversion · 1h | sell | XRP-USD | 4.38 | -0.05 | rebalance down |
| 2026-11-06T07:00 | MFI reversion · 1h | sell | SOL-USD | 4.50 | -0.02 | rebalance down |
| 2026-11-06T07:00 | MFI reversion · 1h | sell | ETH-USD | 4.50 | -0.02 | rebalance down |
| 2026-11-06T07:00 | MACD cross · 1h | buy | SOL-USD | 18.32 | — | entry signal |
| 2026-11-06T07:00 | MACD cross · 1h | buy | DOGE-USD | 18.32 | — | entry signal |
| 2026-11-06T06:20 | MFI reversion · 1h | sell | DOGE-USD | 6.41 | -0.09 | rebalance down |
| 2026-11-06T06:15 | Z-score reversion · 1h | sell | XRP-USD | 7.90 | -0.23 | stop-loss |
| 2026-11-06T06:00 | MFI reversion · 1h | buy | XRP-USD | 15.77 | — | entry signal |
| 2026-11-06T06:00 | MFI reversion · 1h | buy | SOL-USD | 15.77 | — | entry signal |
| 2026-11-06T06:00 | MFI reversion · 1h | buy | ETH-USD | 15.77 | — | entry signal |
| 2026-11-06T06:00 | Williams %R · 1h | buy | ETH-USD | 5.13 | — | entry signal |
| 2026-11-06T06:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.41 | — | entry signal |
| 2026-11-06T04:00 | Candlestick reversal · 1h | sell | SOL-USD | 5.41 | -0.00 | exit signal |
| 2026-11-06T04:00 | VWAP momentum · 1h | sell | SOL-USD | 15.74 | -0.19 | exit signal |
| 2026-11-06T04:00 | VWAP momentum · 1h | sell | DOGE-USD | 16.86 | -0.14 | exit signal |
| 2026-11-06T04:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.11 | -0.17 | exit signal |
| 2026-11-06T03:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.28 | — | entry signal |
| 2026-11-06T02:50 | MFI reversion · 1h | buy | DOGE-USD | 6.54 | — | rebalance up |
| 2026-11-06T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 17.00 | — | entry signal |
| 2026-11-06T02:00 | VWAP momentum · 1h | sell | BTC-USD | 17.00 | -0.16 | exit signal |
| 2026-11-06T01:45 | MFI reversion · 1h | buy | DOGE-USD | 4.42 | — | rebalance up |
| 2026-11-06T01:15 | MFI reversion · 1h | sell | DOGE-USD | 4.34 | -0.03 | rebalance down |
| 2026-11-06T01:05 | Three white soldiers | sell | SOL-USD | 16.46 | -0.18 | exit signal |
| 2026-11-06T01:05 | Three white soldiers | sell | DOGE-USD | 16.49 | -0.14 | exit signal |
| 2026-11-06T01:00 | MFI reversion · 1h | buy | DOGE-USD | 13.18 | — | entry signal |
| 2026-11-06T01:00 | CCI reversion · 1h | buy | ETH-USD | 1.34 | — | rebalance up |
| 2026-11-06T01:00 | CCI reversion · 1h | buy | DOGE-USD | 11.09 | — | entry signal |
| 2026-11-06T01:00 | CCI reversion · 1h | sell | SOL-USD | 4.51 | -0.00 | rebalance down |
| 2026-11-06T01:00 | CCI reversion · 1h | sell | BTC-USD | 7.93 | 0.05 | rebalance down |
| 2026-11-06T01:00 | Williams %R · 1h | buy | SOL-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | Williams %R · 1h | buy | DOGE-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | Williams %R · 1h | buy | BTC-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | SOL-USD | 9.92 | -0.04 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | ETH-USD | 9.87 | -0.12 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 9.82 | -0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 08:25:05.000134+00:00 -> 2026-11-06 08:35:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 08:25:05.000134+00:00 -> 2026-11-06 08:35:05.000134+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 08:25:05.000134+00:00 -> 2026-11-06 08:35:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
