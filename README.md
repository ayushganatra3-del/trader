# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T19:55:05.000136+00:00 · 50020 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.30 (-11.70%)

Closed trades 151, win rate 37.1%, fees £4.31, max drawdown -12.11%.

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

Today: 34116 decisions in 3000 calls, $0.4240 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T19:55 | 1 / 11 / 19 | cash |  |
| Breezy | 2026-11-06T19:55 | 0 / 27 / 4 | cash |  |
| Boozy | 2026-11-06T19:55 | 4 / 25 / 2 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |
| Candlestick reversal · 1h | DOGE-USD | 1.64 | +5.59% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.18 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.78 | 12.79 | 0 | — | 13.55 | 4.64 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.93 | -0.07 | 120 | 47.5 | -11.29 | -2.55 | -14.31 | 152 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.69 | -0.31 | 0 | — | 2.67 | 0.85 | -6.60 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 4.51 | 2.31 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.45 | -6.50 | 21 |
| 12 | Hold SPY | benchmark | 95.04 | -4.96 | 0 | — | -3.93 | -1.44 | -6.18 | 1 |
| 13 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.75 | -4.87 | -10.36 | 169 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.29 | -0.34 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.34 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.78 | -7.22 | 7 | 42.9 | -9.49 | -0.89 | -18.69 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.24 | -7.76 | 0 | — | -7.11 | -2.15 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.23 | -7.77 | 107 | 23.4 | -15.58 | -5.66 | -17.86 | 82 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 91.14 | -8.86 | 0 | — | -6.85 | -2.03 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.37 | -10.63 | 369 | 32.8 | -16.28 | -5.26 | -17.56 | 588 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.25 | -3.57 | -14.68 | 86 |
| 23 | Daily: Bullish score | daily | 88.58 | -11.42 | 15 | 20.0 | -5.19 | -0.69 | -16.58 | 14 |
| 24 | Hold BTC | benchmark | 88.38 | -11.62 | 1 | 0.0 | -5.43 | -0.67 | -14.09 | 1 |
| 25 | Agent | meta | 88.30 | -11.70 | 151 | 37.1 | -13.66 | -7.29 | -14.12 | 206 |
| 26 | Copy: Insider buying | copy | 88.05 | -11.95 | 40 | 37.5 | -23.98 | -4.68 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.74 | -13.26 | 166 | 27.1 | -15.00 | -3.33 | -20.50 | 240 |
| 28 | Donchian 55/20 · 1h | breakout | 85.78 | -14.22 | 71 | 14.1 | -13.45 | -2.75 | -20.43 | 104 |
| 29 | Max aggression: 5-day momentum | meta | 84.54 | -15.46 | 17 | 47.1 | -33.10 | -2.12 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.60 | -5.59 | -18.68 | 98 |
| 31 | Opening range 15m | breakout | 82.27 | -17.73 | 458 | 29.9 | -21.20 | -6.29 | -21.40 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.00 | -18.00 | 260 | 46.9 | -26.01 | -3.86 | -29.25 | 393 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.70 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -20.47 | -6.82 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.51 | -4.68 | -24.50 | 173 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.22 | -19.78 | 2 | 0.0 | -12.30 | -1.61 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.39 | -20.61 | 173 | 18.5 | -24.58 | -4.12 | -27.04 | 262 |
| 38 | MFI reversion · 1h | reversion | 78.78 | -21.22 | 330 | 34.2 | -19.05 | -2.75 | -20.68 | 157 |
| 39 | Ichimoku · 1h | trend | 77.89 | -22.11 | 94 | 14.9 | -23.28 | -4.78 | -29.43 | 126 |
| 40 | Bollinger breakout · 1h | breakout | 77.78 | -22.22 | 166 | 23.5 | -23.57 | -4.92 | -27.12 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.86 | -23.14 | 286 | 46.2 | -30.40 | -4.99 | -31.74 | 467 |
| 42 | EMA 20/50 cross · 1h | trend | 75.96 | -24.04 | 102 | 10.8 | -24.67 | -4.49 | -30.58 | 134 |
| 43 | Heikin-Ashi · 1h | trend | 75.59 | -24.41 | 393 | 22.9 | -43.10 | -9.09 | -43.54 | 675 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.41 | -5.50 | -29.20 | 211 |
| 45 | Triple EMA stack · 1h | trend | 74.32 | -25.68 | 142 | 14.8 | -29.39 | -6.22 | -33.48 | 205 |
| 46 | Supertrend · 1h | trend | 73.58 | -26.43 | 166 | 13.3 | -30.89 | -5.42 | -34.80 | 218 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -28.08 | -5.36 | -32.60 | 219 |
| 48 | MACD cross · 1h | trend | 73.37 | -26.63 | 335 | 23.0 | -36.15 | -6.45 | -38.81 | 483 |
| 49 | Z-score reversion · 1h | reversion | 73.15 | -26.85 | 161 | 36.0 | -25.60 | -3.82 | -28.33 | 234 |
| 50 | Bollinger reversion · 1h | reversion | 73.02 | -26.98 | 250 | 40.0 | -31.06 | -5.30 | -34.52 | 375 |
| 51 | Williams %R · 1h | reversion | 72.40 | -27.60 | 314 | 44.9 | -37.45 | -6.06 | -39.70 | 534 |
| 52 | Daily: Momentum burst | daily | 72.17 | -27.82 | 26 | 11.5 | -36.04 | -5.07 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.45 | -28.55 | 140 | 20.0 | -30.14 | -5.59 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 70.99 | -29.01 | 272 | 18.0 | -30.59 | -6.57 | -33.62 | 287 |
| 55 | ROC + volume · 1h | momentum | 70.16 | -29.84 | 345 | 25.5 | -36.92 | -7.18 | -37.27 | 378 |
| 56 | EMA 9/21 cross · 1h | trend | 67.44 | -32.56 | 241 | 10.0 | -40.41 | -8.39 | -40.77 | 338 |
| 57 | VWAP momentum · 1h | momentum | 67.15 | -32.85 | 776 | 22.0 | -56.06 | -12.49 | -56.09 | 1233 |
| 58 | Agent (ML meta-label) | meta | 66.53 | -33.47 | 1531 | 22.9 | -10.30 | -1.50 | -21.94 | 338 |
| 59 | RSI(14) reversion · 1h | reversion | 66.39 | -33.61 | 142 | 27.5 | -28.60 | -4.48 | -31.54 | 219 |
| 60 | Three white soldiers | momentum | 65.93 | -34.07 | 456 | 16.0 | -47.74 | -22.28 | -47.74 | 637 |
| 61 | Candlestick reversal · 1h | reversion | 65.44 | -34.56 | 406 | 28.6 | -38.61 | -7.15 | -39.16 | 572 |
| 62 | Max aggression: 1-day momentum | meta | 61.77 | -38.23 | 26 | 26.9 | -43.40 | -2.76 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -46.54 | -98.93 | 5200 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.61 | -25.97 | -80.77 | 1427 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -48.51 | -93.47 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.21 | -32.20 | -89.33 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.82 | -40.49 | -90.90 | 2299 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.24 | -32.46 | -90.24 | 2195 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -55.75 | -97.72 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -59.26 | -96.31 | 3391 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.88 | -34.15 | -93.88 | 2452 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.54 | -36.88 | -82.56 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -55.78 | -99.52 | 5975 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.69 | -44.52 | -92.70 | 2601 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -38.05 | -95.68 | 3408 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.91 | -99.80 | 6182 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.82 | -44.29 | -91.87 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.36 | -26.38 | -75.47 | 1572 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -65.45 | -97.73 | 3506 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -62.58 | -98.79 | 4880 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.72 | -29.51 | -69.82 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -56.86 | -94.69 | 2745 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.17 | -38.39 | -85.23 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -74.47 | -99.64 | 6362 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.16 | -31.71 | -89.27 | 2288 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.58 | -19.64 | -77.79 | 1739 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.00 | -37.68 | -91.06 | 2230 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.57 | -53.03 | -96.60 | 3872 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.56 | -57.32 | -89.56 | 2169 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.38 | -29.01 | -66.38 | 805 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.51 | -24.83 | -73.78 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.04 | -17.78 | -78.59 | 1664 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.24 | -49.92 | -97.26 | 4327 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -121.06 | -99.93 | 8295 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T19:55 | Agent (ML meta-label) | buy | IWM | 3.42 | — | entry |
| 2026-11-06T19:55 | Agent (ML meta-label) | sell | BTC-USD | 3.42 | -0.02 | selected signal exited |
| 2026-11-06T19:40 | Agent (ML meta-label) | buy | UPRO | 1.32 | — | entry |
| 2026-11-06T19:40 | Agent (ML meta-label) | buy | TQQQ | 3.53 | — | entry |
| 2026-11-06T19:40 | Agent (ML meta-label) | sell | IWM | 3.91 | 0.00 | selected signal exited |
| 2026-11-06T19:40 | VWAP reversion · 1h | buy | NVDA | 24.98 | — | entry |
| 2026-11-06T19:35 | Agent (aggressive) | sell | AMZN | 41.87 | -0.27 | selected signal exited |
| 2026-11-06T19:35 | Agent | sell | AMZN | 17.57 | -0.11 | selected signal exited |
| 2026-11-06T19:31 | Agent (ML meta-label) | buy | BTC-USD | 3.44 | — | entry |
| 2026-11-06T19:31 | Agent (ML meta-label) | sell | LABU | 3.50 | 0.00 | selected signal exited |
| 2026-11-06T19:31 | MFI reversion · 1h | buy | ETHU | 4.63 | — | entry signal |
| 2026-11-06T19:31 | Candlestick reversal · 1h | buy | AMD | 5.94 | — | entry |
| 2026-11-06T19:31 | Candlestick reversal · 1h | sell | QQQ | 4.73 | -0.02 | target is flat |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | ETHU | 7.43 | — | entry signal |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | BTC-USD | 7.46 | — | entry |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | BITX | 7.46 | — | entry signal |
| 2026-11-06T19:31 | VWAP momentum · 1h | buy | AMD | 7.46 | — | entry signal |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | TNA | 6.01 | 0.04 | rebalance down |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | LABU | 5.90 | -0.02 | rebalance down |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | IWM | 6.01 | 0.01 | rebalance down |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | DOGE-USD | 5.91 | -0.01 | rebalance down |
| 2026-11-06T19:31 | VWAP momentum · 1h | sell | AAPL | 5.99 | -0.00 | rebalance down |
| 2026-11-06T19:31 | Heikin-Ashi · 1h | buy | TSLA | 6.26 | — | rebalance up |
| 2026-11-06T19:31 | Heikin-Ashi · 1h | buy | LABU | 3.92 | — | rebalance up |
| 2026-11-06T19:31 | Heikin-Ashi · 1h | buy | AMD | 6.17 | — | rebalance up |
| 2026-11-06T19:31 | Heikin-Ashi · 1h | sell | PLTR | 12.58 | -0.08 | exit signal |
| 2026-11-06T19:31 | Heikin-Ashi · 1h | sell | META | 12.57 | -0.09 | exit signal |
| 2026-11-06T19:31 | MACD cross · 1h | buy | QQQ | 3.55 | — | entry signal |
| 2026-11-06T19:31 | MACD cross · 1h | buy | NVDA | 5.24 | — | entry signal |
| 2026-11-06T19:31 | MACD cross · 1h | sell | SQQQ | 8.79 | -0.04 | exit signal |
| 2026-11-06T19:25 | OBV trend · 1h | sell | SQQQ | 17.64 | -0.17 | target is flat |
| 2026-11-06T19:20 | Agent (ML meta-label) | buy | LABU | 3.50 | — | entry |
| 2026-11-06T19:15 | MFI reversion · 1h | sell | ETHU | 4.63 | 0.00 | target is flat |
| 2026-11-06T19:10 | Agent (ML meta-label) | buy | MSTR | 4.37 | — | entry |
| 2026-11-06T19:10 | Agent (ML meta-label) | sell | META | 4.14 | 0.01 | selected signal exited |
| 2026-11-06T19:10 | Agent (ML meta-label) | sell | LABU | 4.13 | -0.03 | selected signal exited |
| 2026-11-06T19:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 16.88 | — | entry signal |
| 2026-11-06T19:00 | Opening range 30m | buy | LABU | 5.16 | — | rebalance up |
| 2026-11-06T19:00 | Opening range 30m | sell | SQQQ | 12.40 | -0.25 | stop-loss |
| 2026-11-06T18:55 | Three white soldiers | sell | XRP-USD | 16.39 | -0.15 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 19:55:05.000136+00:00 -> 2026-11-06 20:05:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 19:55:05.000136+00:00 -> 2026-11-06 20:05:05.000136+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 19:55:05.000136+00:00 -> 2026-11-06 20:05:05.000136+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
