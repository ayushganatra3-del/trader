# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T15:55:05.000134+00:00 · 49828 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.49 (-11.51%)

Closed trades 148, win rate 37.2%, fees £4.23, max drawdown -11.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 17.77 | +0.08 |
| DOGE-USD | 17.65 | -0.05 |

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

Today: 16764 decisions in 2424 calls, $0.2214 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T15:55 | 5 / 18 / 7 | cash |  |
| Breezy | 2026-11-06T15:55 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-06T15:55 | 6 / 24 / 0 | BITX 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |
| Connors RSI(2) | SOXL | 1.71 | +2.23% | 8 |
| Candlestick reversal · 1h | DOGE-USD | 1.64 | +5.59% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.21 | 12.21 | 0 | — | 13.04 | 4.44 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.39 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.05 | 0.13 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.08 | 0.08 | 0 | — | 3.14 | 0.97 | -6.60 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.94 | -0.06 | 118 | 47.5 | -12.34 | -2.88 | -14.46 | 148 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.97 | -2.03 | 119 | 35.3 | 5.16 | 2.62 | -3.32 | 94 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Hold SPY | benchmark | 95.40 | -4.60 | 0 | — | -3.51 | -1.25 | -6.18 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 13 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Gap and go | momentum | 94.43 | -5.57 | 169 | 27.8 | -1.01 | -0.25 | -9.18 | 229 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 93.70 | -6.30 | 7 | 42.9 | -8.53 | -0.74 | -18.73 | 8 |
| 17 | Trend pullback · 1h | trend | 92.50 | -7.50 | 107 | 23.4 | -15.31 | -5.50 | -17.86 | 81 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 91.28 | -8.72 | 0 | — | -8.02 | -2.46 | -9.25 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 91.13 | -8.87 | 0 | — | -6.80 | -1.99 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.57 | -10.43 | 366 | 33.1 | -16.20 | -5.19 | -17.56 | 586 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.26 | -3.55 | -14.68 | 86 |
| 23 | Agent | meta | 88.49 | -11.51 | 148 | 37.2 | -13.82 | -7.28 | -14.71 | 213 |
| 24 | Hold BTC | benchmark | 88.34 | -11.66 | 1 | 0.0 | -5.77 | -0.75 | -14.09 | 1 |
| 25 | Daily: Bullish score | daily | 88.28 | -11.72 | 15 | 20.0 | -5.47 | -0.74 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 86.99 | -13.01 | 40 | 37.5 | -25.01 | -4.93 | -26.04 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.47 | -13.53 | 166 | 27.1 | -14.63 | -3.22 | -20.50 | 239 |
| 28 | Donchian 55/20 · 1h | breakout | 85.51 | -14.49 | 71 | 14.1 | -13.71 | -2.79 | -20.43 | 104 |
| 29 | Agent (aggressive) | meta | 84.42 | -15.58 | 72 | 30.6 | -18.38 | -5.46 | -19.08 | 100 |
| 30 | Max aggression: 5-day momentum | meta | 83.51 | -16.49 | 17 | 47.1 | -33.88 | -2.17 | -40.71 | 25 |
| 31 | Opening range 15m | breakout | 82.58 | -17.42 | 453 | 30.2 | -20.93 | -6.18 | -21.38 | 722 |
| 32 | Stochastic reversion · 1h | reversion | 82.02 | -17.98 | 260 | 46.9 | -25.99 | -3.83 | -29.25 | 392 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.73 | -3.67 | -21.28 | 100 |
| 34 | Connors RSI(2) · 1h | reversion | 81.00 | -19.00 | 204 | 40.2 | -20.52 | -6.77 | -21.05 | 129 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.52 | -4.64 | -24.50 | 173 |
| 36 | ADX DI cross · 1h | trend | 79.67 | -20.33 | 172 | 18.6 | -24.95 | -4.17 | -27.04 | 264 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 79.49 | -20.51 | 2 | 0.0 | -13.03 | -1.73 | -24.16 | 1 |
| 38 | MFI reversion · 1h | reversion | 79.00 | -21.00 | 329 | 34.0 | -19.74 | -2.59 | -22.82 | 154 |
| 39 | Bollinger breakout · 1h | breakout | 78.05 | -21.95 | 166 | 23.5 | -23.28 | -4.83 | -26.82 | 246 |
| 40 | Ichimoku · 1h | trend | 77.73 | -22.27 | 94 | 14.9 | -23.45 | -4.78 | -29.43 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.13 | -22.87 | 286 | 46.2 | -30.29 | -4.92 | -31.70 | 462 |
| 42 | Heikin-Ashi · 1h | trend | 75.96 | -24.04 | 389 | 23.1 | -42.81 | -8.94 | -43.20 | 667 |
| 43 | EMA 20/50 cross · 1h | trend | 75.77 | -24.23 | 102 | 10.8 | -24.35 | -4.40 | -30.58 | 133 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.12 | -5.38 | -29.20 | 210 |
| 45 | Triple EMA stack · 1h | trend | 74.09 | -25.91 | 142 | 14.8 | -29.71 | -6.24 | -33.48 | 206 |
| 46 | Supertrend · 1h | trend | 73.57 | -26.43 | 166 | 13.3 | -30.55 | -5.30 | -34.80 | 217 |
| 47 | MACD cross · 1h | trend | 73.51 | -26.49 | 334 | 23.1 | -35.92 | -6.34 | -38.81 | 475 |
| 48 | RSI momentum · 1h | momentum | 73.39 | -26.61 | 158 | 12.7 | -28.15 | -5.33 | -32.60 | 219 |
| 49 | Z-score reversion · 1h | reversion | 73.25 | -26.75 | 161 | 36.0 | -25.40 | -3.74 | -28.32 | 231 |
| 50 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 250 | 40.0 | -31.08 | -5.26 | -34.52 | 375 |
| 51 | Williams %R · 1h | reversion | 72.42 | -27.58 | 314 | 44.9 | -37.41 | -5.99 | -39.71 | 533 |
| 52 | Daily: Momentum burst | daily | 71.95 | -28.05 | 26 | 11.5 | -36.24 | -5.07 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.35 | -28.65 | 140 | 20.0 | -30.22 | -5.56 | -34.69 | 213 |
| 54 | OBV trend · 1h | momentum | 71.19 | -28.81 | 269 | 17.5 | -31.08 | -6.60 | -33.72 | 290 |
| 55 | ROC + volume · 1h | momentum | 70.10 | -29.90 | 345 | 25.5 | -37.21 | -7.20 | -37.21 | 379 |
| 56 | VWAP momentum · 1h | momentum | 67.60 | -32.40 | 763 | 22.3 | -55.96 | -12.36 | -56.18 | 1224 |
| 57 | EMA 9/21 cross · 1h | trend | 67.46 | -32.54 | 241 | 10.0 | -39.87 | -8.19 | -40.24 | 335 |
| 58 | Agent (ML meta-label) | meta | 66.74 | -33.26 | 1518 | 22.7 | -6.39 | -0.94 | -18.08 | 327 |
| 59 | RSI(14) reversion · 1h | reversion | 66.51 | -33.49 | 142 | 27.5 | -28.37 | -4.40 | -31.29 | 215 |
| 60 | Three white soldiers | momentum | 66.16 | -33.84 | 454 | 16.1 | -47.62 | -21.75 | -47.62 | 636 |
| 61 | Candlestick reversal · 1h | reversion | 65.55 | -34.45 | 400 | 28.5 | -38.26 | -6.98 | -38.94 | 563 |
| 62 | Max aggression: 1-day momentum | meta | 61.01 | -38.99 | 26 | 26.9 | -44.05 | -2.79 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -44.82 | -98.93 | 5155 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.53 | -25.70 | -80.72 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -47.20 | -93.42 | 2493 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.16 | -31.22 | -89.33 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.80 | -39.46 | -90.87 | 2293 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.14 | -31.17 | -90.16 | 2193 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -53.66 | -97.73 | 3444 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -58.56 | -96.26 | 3365 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -32.80 | -93.68 | 2432 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.15 | -36.72 | -82.32 | 1640 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -52.93 | -99.52 | 5948 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -43.61 | -92.76 | 2590 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.70 | -36.77 | -95.71 | 3406 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.44 | -99.80 | 6143 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -43.22 | -91.78 | 2252 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.87 | -26.97 | -76.08 | 1580 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -60.83 | -97.69 | 3479 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.78 | -59.49 | -98.79 | 4857 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.62 | -29.00 | -69.77 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -54.57 | -94.70 | 2738 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.10 | -37.08 | -85.28 | 1776 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.46 | -99.65 | 6335 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.22 | -31.00 | -89.28 | 2289 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.72 | -19.46 | -77.79 | 1738 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.91 | -36.82 | -91.00 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.59 | -50.91 | -96.62 | 3856 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -55.26 | -89.52 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.26 | -28.54 | -66.53 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.44 | -24.35 | -73.70 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.30 | -17.78 | -78.62 | 1661 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -48.18 | -97.28 | 4310 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.81 | -99.93 | 8240 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T15:55 | Agent | buy | DOGE-USD | 17.71 | — | following Candlestick reversal · 1h |
| 2026-11-06T15:55 | Gap and go | sell | AMD | 23.45 | -0.19 | exit signal |
| 2026-11-06T15:51 | Agent (ML meta-label) | sell | UPRO | 3.02 | 0.02 | selected signal exited |
| 2026-11-06T15:51 | OBV trend · 1h | sell | SQQQ | 17.92 | 0.19 | target is flat |
| 2026-11-06T15:51 | Opening range 30m | buy | META | 9.81 | — | entry signal |
| 2026-11-06T15:51 | Opening range 30m | buy | AMZN | 5.54 | — | rebalance up |
| 2026-11-06T15:51 | Opening range 30m | sell | TSLA | 5.02 | -0.04 | rebalance down |
| 2026-11-06T15:51 | Opening range 30m | sell | MSFT | 5.21 | 0.01 | rebalance down |
| 2026-11-06T15:51 | Opening range 30m | sell | IWM | 5.12 | -0.02 | rebalance down |
| 2026-11-06T15:51 | Gap and go | buy | TQQQ | 23.44 | — | entry signal |
| 2026-11-06T15:51 | Gap and go | buy | QQQ | 23.64 | — | entry signal |
| 2026-11-06T15:51 | Gap and go | buy | AMD | 23.64 | — | entry signal |
| 2026-11-06T15:45 | VWAP reversion · 1h | buy | NVDA | 24.97 | — | entry |
| 2026-11-06T15:45 | Opening range 30m | buy | AMZN | 7.25 | — | entry signal |
| 2026-11-06T15:45 | Opening range 30m | sell | TNA | 7.25 | -0.11 | rebalance down |
| 2026-11-06T15:40 | Agent (ML meta-label) | buy | UPRO | 2.99 | — | entry |
| 2026-11-06T15:35 | Opening range 15m | buy | UPRO | 4.23 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | TSLA | 4.60 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | TNA | 4.18 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | SPY | 4.17 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | MSFT | 4.27 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | IWM | 4.15 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | buy | AAPL | 4.20 | — | rebalance up |
| 2026-11-06T15:35 | Opening range 15m | sell | PLTR | 7.44 | -0.17 | stop-loss |
| 2026-11-06T15:35 | Gap and go | sell | PLTR | 23.54 | -0.10 | stop-loss |
| 2026-11-06T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 101.66 | -2.06 | target is flat |
| 2026-11-06T15:30 | Agent (ML meta-label) | sell | UPRO | 2.98 | -0.03 | selected signal exited |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | UPRO | 5.03 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | TSLA | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | TQQQ | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | TECL | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | SPY | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | SOXL | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | QQQ | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | PLTR | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | NVDA | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | buy | AMD | 5.13 | — | entry signal |
| 2026-11-06T15:30 | CCI reversion · 1h | sell | XRP-USD | 9.99 | -0.06 | rebalance down |
| 2026-11-06T15:30 | CCI reversion · 1h | sell | MSTR | 10.28 | -0.12 | rebalance down |
| 2026-11-06T15:30 | CCI reversion · 1h | sell | ETH-USD | 10.27 | -0.13 | rebalance down |

## Data problems on the last tick

- GURU: yfinance: $GURU: possibly delisted; no price data found  (5m 2026-11-05 15:55:05.000134+00:00 -> 2026-11-06 16:05:05.000134+00:00); yahoo: cooling down after a rate limit
- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 15:55:05.000134+00:00 -> 2026-11-06 16:05:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 15:55:05.000134+00:00 -> 2026-11-06 16:05:05.000134+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 15:55:05.000134+00:00 -> 2026-11-06 16:05:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
