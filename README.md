# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T03:54:05.000170+00:00 · 49213 ticks

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

Today: 2895 decisions in 579 calls, $0.0404 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T03:54 | 3 / 1 / 1 | cash |  |
| Breezy | 2026-11-06T03:54 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T03:54 | 3 / 2 / 0 | ETH-USD 54% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.73 | 11.73 | 0 | — | 13.22 | 4.50 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.05 | 0.61 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.33 | -0.67 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.24 | -1.76 | 111 | 44.1 | -13.59 | -3.31 | -14.16 | 150 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 13 | Agent (rotation) | meta | 95.14 | -4.86 | 175 | 28.0 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 15 | Hold SPY | benchmark | 93.92 | -6.08 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.09 | -1.39 | -18.69 | 8 |
| 17 | Trend pullback · 1h | trend | 92.16 | -7.84 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 90.75 | -9.25 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.09 | -9.91 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.07 | -10.93 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.55 | -14.68 | 86 |
| 24 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 25 | Hold BTC | benchmark | 88.01 | -11.99 | 1 | 0.0 | -5.00 | -0.62 | -13.74 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.60 | -12.40 | 166 | 27.1 | -14.67 | -3.22 | -20.02 | 241 |
| 27 | Donchian 55/20 · 1h | breakout | 86.65 | -13.35 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.51 | -13.49 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.76 | -17.24 | 144 | 27.8 | -16.20 | -3.64 | -21.39 | 103 |
| 33 | Keltner breakout · 1h | breakout | 82.01 | -17.99 | 106 | 23.6 | -22.14 | -4.56 | -24.41 | 177 |
| 34 | Stochastic reversion · 1h | reversion | 81.43 | -18.57 | 255 | 46.7 | -28.63 | -4.45 | -29.24 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.68 | -19.32 | 203 | 39.9 | -20.51 | -6.77 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -24.52 | -4.07 | -26.36 | 265 |
| 38 | Bollinger breakout · 1h | breakout | 79.20 | -20.80 | 165 | 23.6 | -22.45 | -4.64 | -26.52 | 247 |
| 39 | MFI reversion · 1h | reversion | 78.91 | -21.09 | 328 | 33.8 | -19.03 | -2.72 | -20.08 | 150 |
| 40 | Ichimoku · 1h | trend | 78.73 | -21.27 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.37 | -22.63 | 284 | 45.8 | -29.61 | -4.79 | -30.63 | 451 |
| 42 | Heikin-Ashi · 1h | trend | 77.01 | -22.99 | 385 | 23.1 | -43.29 | -9.12 | -43.91 | 674 |
| 43 | EMA 20/50 cross · 1h | trend | 76.58 | -23.42 | 102 | 10.8 | -22.75 | -4.07 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.06 | -24.94 | 142 | 14.8 | -29.58 | -6.19 | -33.06 | 207 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.31 | -5.43 | -29.20 | 211 |
| 46 | RSI momentum · 1h | momentum | 74.02 | -25.98 | 158 | 12.7 | -27.86 | -5.27 | -32.33 | 220 |
| 47 | Supertrend · 1h | trend | 73.95 | -26.05 | 166 | 13.3 | -29.83 | -5.14 | -34.26 | 217 |
| 48 | MACD cross · 1h | trend | 73.30 | -26.70 | 334 | 23.1 | -36.11 | -6.35 | -38.81 | 472 |
| 49 | Z-score reversion · 1h | reversion | 72.93 | -27.07 | 159 | 35.8 | -28.25 | -4.38 | -28.36 | 225 |
| 50 | Donchian 20/10 · 1h | breakout | 72.41 | -27.59 | 140 | 20.0 | -29.75 | -5.46 | -34.25 | 214 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.46 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 72.03 | -27.97 | 244 | 38.9 | -34.08 | -6.26 | -34.52 | 375 |
| 53 | Williams %R · 1h | reversion | 71.84 | -28.16 | 310 | 44.8 | -39.36 | -6.56 | -39.60 | 527 |
| 54 | ROC + volume · 1h | momentum | 71.61 | -28.39 | 344 | 25.6 | -36.68 | -7.13 | -37.60 | 383 |
| 55 | OBV trend · 1h | momentum | 71.34 | -28.66 | 266 | 17.3 | -32.86 | -6.93 | -34.09 | 295 |
| 56 | VWAP momentum · 1h | momentum | 68.24 | -31.76 | 758 | 22.3 | -55.57 | -12.23 | -56.28 | 1216 |
| 57 | EMA 9/21 cross · 1h | trend | 68.03 | -31.96 | 241 | 10.0 | -39.20 | -8.00 | -39.91 | 335 |
| 58 | Three white soldiers | momentum | 66.21 | -33.79 | 453 | 16.1 | -47.97 | -22.18 | -47.97 | 640 |
| 59 | RSI(14) reversion · 1h | reversion | 66.10 | -33.90 | 142 | 27.5 | -28.60 | -4.44 | -30.95 | 205 |
| 60 | Agent (ML meta-label) | meta | 65.12 | -34.88 | 1508 | 22.3 | -8.11 | -1.21 | -17.48 | 322 |
| 61 | Candlestick reversal · 1h | reversion | 64.98 | -35.02 | 395 | 28.6 | -38.92 | -7.19 | -39.18 | 564 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -45.26 | -98.92 | 5123 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.22 | -25.52 | -80.22 | 1404 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.31 | -47.19 | -93.31 | 2494 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.15 | -31.31 | -89.16 | 1897 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.63 | -39.02 | -90.70 | 2283 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.36 | -31.61 | -90.45 | 2206 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -52.74 | -97.65 | 3430 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -60.31 | -96.17 | 3359 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -32.47 | -93.63 | 2424 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.72 | -36.34 | -81.82 | 1633 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.50 | -50.67 | -99.50 | 5928 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.54 | -42.98 | -92.55 | 2583 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.79 | -37.15 | -95.82 | 3416 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -66.36 | -99.79 | 6113 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.57 | -42.42 | -91.57 | 2242 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.91 | -26.68 | -74.96 | 1562 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -60.72 | -97.66 | 3486 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.75 | -56.78 | -98.75 | 4833 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.28 | -28.32 | -70.08 | 1201 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -53.32 | -94.49 | 2737 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.80 | -37.10 | -84.80 | 1776 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -67.90 | -99.64 | 6315 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.89 | -29.91 | -88.97 | 2262 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.59 | -19.33 | -77.86 | 1736 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.95 | -35.77 | -90.96 | 2214 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.51 | -49.12 | -96.53 | 3831 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.42 | -54.73 | -89.42 | 2158 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.46 | -27.50 | -65.79 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.15 | -24.14 | -73.80 | 1256 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.24 | -17.54 | -78.30 | 1654 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -47.51 | -97.24 | 4304 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -92.23 | -99.93 | 8202 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | BTC-USD | 9.91 | -0.05 | exit signal |
| 2026-11-06T01:00 | Z-score reversion · 1h | buy | XRP-USD | 8.14 | — | entry signal |
| 2026-11-06T01:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.14 | — | entry signal |
| 2026-11-06T01:00 | RSI(14) reversion · 1h | buy | ETH-USD | 16.57 | — | entry signal |
| 2026-11-06T01:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 16.64 | — | entry signal |
| 2026-11-06T01:00 | VWAP momentum · 1h | buy | SOL-USD | 15.93 | — | entry signal |
| 2026-11-06T01:00 | VWAP momentum · 1h | buy | BTC-USD | 17.15 | — | entry signal |
| 2026-11-06T00:45 | Three white soldiers | buy | SOL-USD | 16.63 | — | entry signal |
| 2026-11-06T00:35 | Three white soldiers | buy | DOGE-USD | 16.63 | — | entry |
| 2026-11-06T00:05 | CCI reversion · 1h | buy | ETH-USD | 3.88 | — | entry |
| 2026-11-06T00:05 | CCI reversion · 1h | sell | SOL-USD | 3.88 | -0.03 | rebalance down |
| 2026-11-06T00:00 | Hold BTC | buy | BTC-USD | 88.43 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | XRP-USD | 5.82 | — | entry signal |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | SOL-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | ETH-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | DOGE-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | BTC-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Z-score reversion · 1h | buy | SOL-USD | 10.45 | — | entry |
| 2026-11-06T00:00 | Z-score reversion · 1h | buy | BTC-USD | 10.45 | — | entry |
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | SOL-USD | 4.00 | — | entry |
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | ETH-USD | 4.00 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 03:54:05.000170+00:00 -> 2026-11-06 04:04:05.000170+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 03:54:05.000170+00:00 -> 2026-11-06 04:04:05.000170+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 03:54:05.000170+00:00 -> 2026-11-06 04:04:05.000170+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
