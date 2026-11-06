# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T00:55:05.000143+00:00 · 49058 ticks

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

Today: 570 decisions in 114 calls, $0.0080 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T00:55 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-06T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T00:55 | 2 / 2 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |
| VWAP reversion | GOOGL | 1.74 | +1.67% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.17 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.66 | 11.66 | 0 | — | 13.22 | 4.52 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.06 | 0.61 | -9.63 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.27 | -0.73 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.31 | -1.69 | 107 | 45.8 | -13.47 | -3.26 | -14.27 | 148 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 13 | Agent (rotation) | meta | 95.12 | -4.88 | 175 | 28.0 | -6.68 | -3.77 | -10.36 | 173 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 15 | Hold SPY | benchmark | 93.85 | -6.14 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.15 | -1.39 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.11 | -7.89 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 90.69 | -9.31 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.03 | -9.97 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.04 | -10.96 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.65 | -14.68 | 86 |
| 24 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 25 | Hold BTC | benchmark | 88.43 | -11.57 | 1 | 0.0 | -4.48 | -0.54 | -13.74 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.58 | -12.42 | 166 | 27.1 | -15.02 | -3.30 | -20.02 | 242 |
| 27 | Donchian 55/20 · 1h | breakout | 86.64 | -13.36 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.46 | -13.54 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.75 | -17.25 | 144 | 27.8 | -16.20 | -3.64 | -21.39 | 103 |
| 33 | Keltner breakout · 1h | breakout | 82.00 | -18.00 | 106 | 23.6 | -22.02 | -4.53 | -24.41 | 176 |
| 34 | Stochastic reversion · 1h | reversion | 81.60 | -18.40 | 255 | 46.7 | -28.48 | -4.42 | -29.24 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.66 | -19.34 | 203 | 39.9 | -20.81 | -6.89 | -21.32 | 130 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -24.20 | -4.01 | -26.36 | 263 |
| 38 | Bollinger breakout · 1h | breakout | 79.19 | -20.81 | 165 | 23.6 | -22.43 | -4.64 | -26.52 | 247 |
| 39 | MFI reversion · 1h | reversion | 79.11 | -20.89 | 328 | 33.8 | -21.52 | -2.88 | -22.50 | 152 |
| 40 | Ichimoku · 1h | trend | 78.72 | -21.28 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.59 | -22.41 | 284 | 45.8 | -29.19 | -4.70 | -30.63 | 449 |
| 42 | Heikin-Ashi · 1h | trend | 77.13 | -22.87 | 385 | 23.1 | -42.47 | -8.85 | -44.25 | 674 |
| 43 | EMA 20/50 cross · 1h | trend | 76.57 | -23.43 | 102 | 10.8 | -22.75 | -4.07 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.05 | -24.95 | 142 | 14.8 | -29.93 | -6.27 | -33.06 | 209 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.31 | -5.43 | -29.20 | 211 |
| 46 | RSI momentum · 1h | momentum | 73.99 | -26.01 | 158 | 12.7 | -28.19 | -5.34 | -32.33 | 221 |
| 47 | Supertrend · 1h | trend | 73.91 | -26.09 | 166 | 13.3 | -29.83 | -5.14 | -34.26 | 217 |
| 48 | MACD cross · 1h | trend | 73.30 | -26.70 | 334 | 23.1 | -36.11 | -6.35 | -38.81 | 472 |
| 49 | Z-score reversion · 1h | reversion | 73.21 | -26.80 | 159 | 35.8 | -27.97 | -4.32 | -28.35 | 223 |
| 50 | Donchian 20/10 · 1h | breakout | 72.40 | -27.60 | 140 | 20.0 | -29.70 | -5.45 | -34.25 | 214 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.45 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 72.11 | -27.89 | 244 | 38.9 | -34.00 | -6.24 | -34.52 | 375 |
| 53 | Williams %R · 1h | reversion | 71.97 | -28.03 | 310 | 44.8 | -39.24 | -6.53 | -39.45 | 524 |
| 54 | ROC + volume · 1h | momentum | 71.60 | -28.40 | 344 | 25.6 | -36.79 | -7.11 | -37.94 | 385 |
| 55 | OBV trend · 1h | momentum | 71.31 | -28.69 | 266 | 17.3 | -32.71 | -6.97 | -33.72 | 295 |
| 56 | VWAP momentum · 1h | momentum | 68.60 | -31.40 | 757 | 22.3 | -55.12 | -12.04 | -56.33 | 1214 |
| 57 | EMA 9/21 cross · 1h | trend | 68.01 | -31.99 | 241 | 10.0 | -39.20 | -8.00 | -39.91 | 335 |
| 58 | RSI(14) reversion · 1h | reversion | 66.52 | -33.48 | 142 | 27.5 | -27.87 | -4.30 | -30.66 | 202 |
| 59 | Three white soldiers | momentum | 66.42 | -33.58 | 451 | 16.2 | -48.01 | -22.12 | -48.06 | 639 |
| 60 | Candlestick reversal · 1h | reversion | 65.08 | -34.92 | 395 | 28.6 | -38.67 | -7.12 | -39.04 | 563 |
| 61 | Agent (ML meta-label) | meta | 65.08 | -34.92 | 1508 | 22.3 | -6.91 | -1.16 | -17.66 | 317 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -44.20 | -98.90 | 5132 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -24.78 | -80.27 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.20 | -45.73 | -93.22 | 2490 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.03 | -30.78 | -89.08 | 1897 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -38.38 | -90.62 | 2286 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -32.05 | -90.56 | 2212 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -51.24 | -97.64 | 3433 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.06 | -56.73 | -96.06 | 3346 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -32.26 | -93.59 | 2421 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.61 | -35.78 | -81.68 | 1632 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -51.29 | -99.51 | 5941 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.50 | -42.30 | -92.51 | 2585 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.85 | -37.66 | -95.87 | 3424 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -64.38 | -99.79 | 6116 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.59 | -42.12 | -91.61 | 2250 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.78 | -26.41 | -74.87 | 1565 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -58.99 | -97.65 | 3485 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.76 | -57.08 | -98.77 | 4838 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -28.39 | -70.08 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.45 | -52.34 | -94.46 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.72 | -36.69 | -84.74 | 1775 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -66.69 | -99.64 | 6312 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.90 | -29.94 | -89.02 | 2262 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.70 | -19.43 | -77.99 | 1737 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.21 | -34.98 | -91.22 | 2226 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.53 | -49.06 | -96.55 | 3830 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -53.55 | -89.41 | 2162 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.41 | -27.51 | -65.75 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -24.04 | -73.80 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.17 | -17.60 | -78.26 | 1651 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.23 | -47.16 | -97.25 | 4302 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -91.68 | -99.93 | 8202 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 00:55:05.000143+00:00 -> 2026-11-06 01:05:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 00:55:05.000143+00:00 -> 2026-11-06 01:05:05.000143+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 00:55:05.000143+00:00 -> 2026-11-06 01:05:05.000143+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
