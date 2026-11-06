# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T00:25:05.000139+00:00 · 49038 ticks

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
| Copy: Insider buying | 2026-11-05 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 38.26 · VIX 28.18 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 270 decisions in 54 calls, $0.0038 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T00:25 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-11-06T00:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T00:25 | 4 / 1 / 0 | ETH-USD 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| VWAP reversion | COIN | 1.83 | +4.26% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.69 | 11.69 | 0 | — | 13.22 | 4.50 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.05 | 0.61 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.29 | -0.71 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.22 | -1.78 | 107 | 45.8 | -13.68 | -3.31 | -14.36 | 148 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 13 | Agent (rotation) | meta | 95.13 | -4.87 | 175 | 28.0 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 15 | Hold SPY | benchmark | 93.88 | -6.12 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.09 | -1.39 | -18.69 | 8 |
| 17 | Trend pullback · 1h | trend | 92.13 | -7.87 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 90.71 | -9.29 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.05 | -9.95 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.06 | -10.95 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.65 | -14.68 | 86 |
| 24 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 25 | Hold BTC | benchmark | 88.29 | -11.71 | 1 | 0.0 | -4.84 | -0.60 | -13.74 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.59 | -12.41 | 166 | 27.1 | -15.02 | -3.30 | -20.02 | 242 |
| 27 | Donchian 55/20 · 1h | breakout | 86.65 | -13.36 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.48 | -13.52 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.75 | -17.25 | 144 | 27.8 | -16.20 | -3.64 | -21.39 | 103 |
| 33 | Keltner breakout · 1h | breakout | 82.00 | -18.00 | 106 | 23.6 | -22.02 | -4.53 | -24.41 | 176 |
| 34 | Stochastic reversion · 1h | reversion | 81.52 | -18.48 | 255 | 46.7 | -28.56 | -4.44 | -29.24 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.67 | -19.33 | 203 | 39.9 | -20.81 | -6.89 | -21.32 | 130 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -24.20 | -4.01 | -26.36 | 263 |
| 38 | Bollinger breakout · 1h | breakout | 79.19 | -20.81 | 165 | 23.6 | -22.43 | -4.64 | -26.52 | 247 |
| 39 | MFI reversion · 1h | reversion | 79.11 | -20.89 | 328 | 33.8 | -20.51 | -2.79 | -21.50 | 155 |
| 40 | Ichimoku · 1h | trend | 78.72 | -21.28 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.51 | -22.49 | 284 | 45.8 | -29.29 | -4.72 | -30.63 | 449 |
| 42 | Heikin-Ashi · 1h | trend | 77.13 | -22.87 | 385 | 23.1 | -42.47 | -8.86 | -44.25 | 674 |
| 43 | EMA 20/50 cross · 1h | trend | 76.58 | -23.42 | 102 | 10.8 | -22.75 | -4.07 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.05 | -24.95 | 142 | 14.8 | -29.93 | -6.27 | -33.06 | 209 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.31 | -5.43 | -29.20 | 211 |
| 46 | RSI momentum · 1h | momentum | 74.00 | -26.00 | 158 | 12.7 | -28.19 | -5.34 | -32.33 | 221 |
| 47 | Supertrend · 1h | trend | 73.93 | -26.07 | 166 | 13.3 | -29.83 | -5.14 | -34.26 | 217 |
| 48 | MACD cross · 1h | trend | 73.30 | -26.70 | 334 | 23.1 | -36.11 | -6.35 | -38.81 | 472 |
| 49 | Z-score reversion · 1h | reversion | 73.15 | -26.85 | 159 | 35.8 | -28.03 | -4.33 | -28.35 | 223 |
| 50 | Donchian 20/10 · 1h | breakout | 72.40 | -27.59 | 140 | 20.0 | -29.70 | -5.45 | -34.25 | 214 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.46 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 72.06 | -27.94 | 244 | 38.9 | -34.04 | -6.25 | -34.52 | 375 |
| 53 | Williams %R · 1h | reversion | 71.97 | -28.03 | 310 | 44.8 | -39.23 | -6.53 | -39.45 | 524 |
| 54 | ROC + volume · 1h | momentum | 71.60 | -28.40 | 344 | 25.6 | -36.49 | -7.07 | -37.64 | 384 |
| 55 | OBV trend · 1h | momentum | 71.32 | -28.68 | 266 | 17.3 | -33.02 | -6.97 | -33.98 | 297 |
| 56 | VWAP momentum · 1h | momentum | 68.61 | -31.39 | 757 | 22.3 | -55.07 | -12.03 | -56.33 | 1215 |
| 57 | EMA 9/21 cross · 1h | trend | 68.02 | -31.98 | 241 | 10.0 | -39.20 | -8.00 | -39.91 | 335 |
| 58 | Three white soldiers | momentum | 66.53 | -33.47 | 451 | 16.2 | -47.76 | -21.89 | -47.76 | 638 |
| 59 | RSI(14) reversion · 1h | reversion | 66.44 | -33.56 | 142 | 27.5 | -27.97 | -4.32 | -30.66 | 202 |
| 60 | Agent (ML meta-label) | meta | 65.10 | -34.90 | 1508 | 22.3 | -6.49 | -1.08 | -17.35 | 319 |
| 61 | Candlestick reversal · 1h | reversion | 65.02 | -34.98 | 395 | 28.6 | -38.73 | -7.14 | -39.04 | 563 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -44.19 | -98.89 | 5124 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.84 | -24.86 | -80.21 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -45.62 | -93.21 | 2489 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.92 | -30.41 | -89.09 | 1897 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.56 | -38.39 | -90.59 | 2284 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -32.05 | -90.56 | 2212 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -51.58 | -97.65 | 3434 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.07 | -56.40 | -96.07 | 3349 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -32.21 | -93.62 | 2421 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.61 | -35.78 | -81.68 | 1632 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.50 | -51.04 | -99.51 | 5935 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.50 | -42.29 | -92.51 | 2583 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.85 | -37.67 | -95.87 | 3424 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -65.25 | -99.79 | 6119 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -42.32 | -91.61 | 2250 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.82 | -26.43 | -74.89 | 1559 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -59.46 | -97.66 | 3488 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.77 | -57.07 | -98.77 | 4840 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -28.39 | -70.08 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.45 | -52.20 | -94.45 | 2735 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -36.54 | -84.73 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -66.69 | -99.64 | 6312 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.91 | -29.98 | -89.02 | 2262 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.49 | -19.22 | -77.77 | 1731 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.01 | -35.60 | -91.04 | 2224 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.53 | -49.21 | -96.56 | 3832 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -53.68 | -89.39 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.32 | -27.37 | -65.65 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.03 | -23.93 | -73.80 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.10 | -17.51 | -78.20 | 1646 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -47.22 | -97.25 | 4303 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -91.06 | -99.93 | 8205 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | DOGE-USD | 4.00 | — | entry |
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | BTC-USD | 4.00 | — | entry |
| 2026-11-06T00:00 | RSI(14) reversion · 1h | buy | SOL-USD | 16.60 | — | entry |
| 2026-11-06T00:00 | RSI(14) reversion · 1h | buy | BTC-USD | 16.60 | — | entry signal |
| 2026-11-06T00:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.41 | — | entry signal |
| 2026-11-06T00:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.41 | — | entry signal |
| 2026-11-06T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.41 | — | entry signal |
| 2026-11-06T00:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.41 | — | entry |
| 2026-11-05T23:15 | Agent | sell | DOGE-USD | 17.21 | -0.60 | selected signal exited |
| 2026-11-05T23:15 | CCI reversion · 1h | buy | BTC-USD | 18.86 | — | entry |
| 2026-11-05T23:15 | CCI reversion · 1h | sell | DOGE-USD | 18.85 | -0.66 | target is flat |
| 2026-11-05T23:15 | VWAP reversion · 1h | sell | XRP-USD | 9.56 | -0.29 | stop-loss |
| 2026-11-05T22:00 | CCI reversion · 1h | buy | SOL-USD | 19.48 | — | entry signal |
| 2026-11-05T21:00 | Agent | buy | DOGE-USD | 17.81 | — | following CCI reversion · 1h |
| 2026-11-05T21:00 | CCI reversion · 1h | buy | DOGE-USD | 19.51 | — | entry signal |
| 2026-11-05T20:56 | Agent (rotation) | sell | SQQQ | 33.49 | 2.40 | selected signal exited |
| 2026-11-05T20:56 | Day trade: Stocks in Play ORB | sell | SQQQ | 26.26 | 2.26 | target is flat |
| 2026-11-05T20:56 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.72 | 5.77 | target is flat |
| 2026-11-05T20:56 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 113.59 | 8.13 | target is flat |
| 2026-11-05T20:56 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 95.31 | -0.15 | target is flat |
| 2026-11-05T20:56 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 107.82 | 10.32 | target is flat |
| 2026-11-05T20:56 | Opening range 30m | sell | SQQQ | 23.26 | 1.05 | end-of-day flatten |
| 2026-11-05T20:56 | Opening range 15m | sell | SQQQ | 22.01 | 1.45 | end-of-day flatten |
| 2026-11-05T20:50 | OBV trend · 1h | buy | SQQQ | 17.78 | — | entry |
| 2026-11-05T20:40 | Agent (ML meta-label) | buy | LABU | 3.30 | — | following VWAP momentum · 1h |
| 2026-11-05T20:40 | Agent (ML meta-label) | sell | AAPL | 3.27 | 0.02 | rebalance down |
| 2026-11-05T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 95.46 | — | entry |
| 2026-11-05T20:30 | CCI reversion · 1h | buy | MSTR | 19.50 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 00:25:05.000139+00:00 -> 2026-11-06 00:35:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 00:25:05.000139+00:00 -> 2026-11-06 00:35:05.000139+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 00:25:05.000139+00:00 -> 2026-11-06 00:35:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
