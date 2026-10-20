# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T04:25:05.000145+00:00 · 29111 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 3180 decisions in 636 calls, $0.0445 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T04:25 | 1 / 0 / 4 | cash |  |
| Breezy | 2026-10-20T04:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T04:25 | 2 / 3 / 0 | ETH-USD 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.84 | +3.15% | 6 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.90 | 4.89 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.80 | -0.20 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.04 | -0.96 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.69 | -2.17 | 63 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.18 | -1.82 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -2.59 | -0.96 | -4.94 | 303 |
| 14 | Donchian 55/20 · 1h | breakout | 97.45 | -2.55 | 37 | 16.2 | -11.26 | -2.10 | -19.38 | 97 |
| 15 | Hold BTC | benchmark | 97.43 | -2.57 | 0 | — | 27.21 | 3.20 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.24 | -2.76 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 18 | Trend pullback · 1h | trend | 96.40 | -3.60 | 88 | 23.9 | -19.92 | -5.87 | -20.80 | 136 |
| 19 | Copy: Insider buying | copy | 96.34 | -3.66 | 23 | 43.5 | -14.93 | -2.70 | -20.62 | 73 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.28 | -3.72 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.31 | -4.68 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.54 | 2.17 | -6.51 | 199 |
| 24 | ADX DI cross · 1h | trend | 93.53 | -6.47 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.85 | -7.15 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 91.92 | -8.08 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.87 | -8.13 | 78 | 23.1 | -12.55 | -2.25 | -16.37 | 101 |
| 29 | Parabolic SAR · 1h | trend | 91.30 | -8.70 | 104 | 22.1 | -16.84 | -3.53 | -23.28 | 269 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 32 | Bollinger breakout · 1h | breakout | 90.76 | -9.24 | 84 | 28.6 | -9.11 | -1.54 | -16.89 | 253 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -13.82 | -5.84 | -18.49 | 265 |
| 34 | EMA 20/50 cross · 1h | trend | 90.19 | -9.81 | 59 | 13.6 | -19.19 | -3.43 | -21.31 | 127 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 89.99 | -10.01 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.75 | -10.25 | 80 | 16.2 | -20.07 | -3.40 | -30.28 | 212 |
| 37 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 38 | Ichimoku · 1h | trend | 88.59 | -11.41 | 56 | 14.3 | -17.63 | -3.33 | -18.10 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.19 | -11.81 | 152 | 46.1 | -17.08 | -2.95 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -17.80 | -4.07 | -23.55 | 155 |
| 41 | Keltner breakout · 1h | breakout | 87.69 | -12.31 | 56 | 23.2 | -11.96 | -1.67 | -26.96 | 201 |
| 42 | Supertrend · 1h | trend | 87.44 | -12.56 | 87 | 12.6 | -22.76 | -4.66 | -26.61 | 214 |
| 43 | Triple EMA stack · 1h | trend | 87.35 | -12.65 | 86 | 15.1 | -25.53 | -4.33 | -32.98 | 233 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 85.91 | -14.09 | 189 | 20.6 | -28.35 | -5.54 | -32.78 | 469 |
| 46 | OBV trend · 1h | momentum | 85.36 | -14.64 | 180 | 17.8 | -27.47 | -4.29 | -36.28 | 317 |
| 47 | Z-score reversion · 1h | reversion | 85.11 | -14.89 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.72 | -15.28 | 209 | 31.1 | -16.98 | -2.64 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.21 | -15.79 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Donchian 20/10 · 1h | breakout | 83.94 | -16.06 | 81 | 17.3 | -11.20 | -1.34 | -27.92 | 214 |
| 51 | Agent (ML meta-label) | meta | 83.75 | -16.25 | 681 | 18.8 | -11.33 | -2.01 | -16.04 | 353 |
| 52 | Bollinger reversion · 1h | reversion | 82.83 | -17.17 | 158 | 34.8 | -27.80 | -5.31 | -33.53 | 349 |
| 53 | Max aggression: 1-day momentum | meta | 82.47 | -17.53 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Williams %R · 1h | reversion | 81.91 | -18.09 | 182 | 42.9 | -33.27 | -5.29 | -36.50 | 531 |
| 55 | Three white soldiers | momentum | 81.85 | -18.15 | 235 | 18.7 | -47.49 | -18.66 | -47.87 | 605 |
| 56 | ROC + volume · 1h | momentum | 81.42 | -18.58 | 197 | 20.8 | -25.33 | -4.26 | -33.90 | 384 |
| 57 | CCI reversion · 1h | reversion | 80.61 | -19.39 | 163 | 39.3 | -17.85 | -2.23 | -27.44 | 443 |
| 58 | RSI(14) reversion · 1h | reversion | 80.05 | -19.95 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 80.03 | -19.97 | 136 | 11.0 | -29.36 | -6.09 | -29.93 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 78.77 | -21.23 | 226 | 21.2 | -41.58 | -8.88 | -45.01 | 680 |
| 61 | VWAP momentum · 1h | momentum | 77.85 | -22.15 | 433 | 20.8 | -43.28 | -7.60 | -48.46 | 1249 |
| 62 | Candlestick reversal · 1h | reversion | 77.03 | -22.97 | 214 | 27.6 | -36.73 | -6.57 | -37.63 | 530 |
| 63 | ROC + volume | momentum | 61.55 | -38.45 | 596 | 22.3 | -76.03 | -17.83 | -78.22 | 1727 |
| 64 | Volume breakout | breakout | 61.28 | -38.72 | 361 | 13.0 | -62.67 | -17.65 | -64.30 | 872 |
| 65 | Squeeze breakout | breakout | 59.79 | -40.21 | 473 | 14.0 | -63.93 | -19.57 | -65.98 | 1204 |
| 66 | Donchian 55/20 | breakout | 58.30 | -41.70 | 481 | 18.3 | -68.49 | -14.04 | -73.15 | 1270 |
| 67 | RSI(14) reversion | reversion | 57.56 | -42.44 | 715 | 25.2 | -74.75 | -16.62 | -74.81 | 1604 |
| 68 | EMA 20/50 cross | trend | 56.24 | -43.77 | 517 | 19.7 | -76.55 | -15.59 | -80.55 | 1424 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.74 | -14.64 | -72.51 | 1498 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -28.41 | -98.70 | 5267 |
| 71 | Keltner breakout | breakout | 50.58 | -49.42 | 677 | 16.1 | -82.46 | -24.32 | -83.68 | 1808 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.08 | -27.52 | -93.76 | 2565 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -85.84 | -18.21 | -88.26 | 1893 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.82 | -22.15 | -91.21 | 2348 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.13 | -25.96 | -91.15 | 2259 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.33 | -29.61 | -97.58 | 3492 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.52 | -32.84 | -96.79 | 3585 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.58 | -28.39 | -94.63 | 2510 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.88 | -24.04 | -82.95 | 1690 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.56 | -99.36 | 5728 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.90 | -23.07 | -92.08 | 2624 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.07 | -31.20 | -96.07 | 3462 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -36.98 | -99.74 | 6182 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.60 | -29.10 | -91.62 | 2330 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -34.61 | -97.65 | 3625 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -36.03 | -98.45 | 4685 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -31.23 | -94.03 | 2800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -38.55 | -99.51 | 6151 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.81 | -22.31 | -86.85 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.85 | -26.56 | -87.88 | 2128 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -32.24 | -95.85 | 3738 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.87 | -31.78 | -89.17 | 2093 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.68 | -33.03 | -95.70 | 4097 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.59 | -99.90 | 8279 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T04:10 | Three white soldiers | sell | DOGE-USD | 20.33 | -0.18 | target is flat |
| 2026-10-20T04:10 | Donchian 55/20 | sell | DOGE-USD | 14.48 | -0.13 | target is flat |
| 2026-10-20T04:05 | Three white soldiers | buy | DOGE-USD | 20.51 | — | entry signal |
| 2026-10-20T04:05 | Keltner breakout | buy | BTC-USD | 12.66 | — | entry signal |
| 2026-10-20T04:05 | Donchian 55/20 | buy | DOGE-USD | 14.61 | — | entry signal |
| 2026-10-20T04:00 | Parabolic SAR · 1h | buy | BTC-USD | 22.84 | — | entry signal |
| 2026-10-20T04:00 | Triple EMA stack · 1h | buy | XRP-USD | 21.42 | — | entry signal |
| 2026-10-20T04:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 22.57 | — | entry signal |
| 2026-10-20T04:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 8.07 | — | entry signal |
| 2026-10-20T04:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 4.00 | -0.01 | rebalance down |
| 2026-10-20T04:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 4.07 | -0.01 | rebalance down |
| 2026-10-20T04:00 | Donchian 55/20 | buy | BTC-USD | 14.62 | — | entry signal |
| 2026-10-20T03:55 | Donchian 55/20 | buy | XRP-USD | 14.63 | — | entry signal |
| 2026-10-20T03:50 | Donchian 55/20 | buy | ETH-USD | 14.64 | — | entry signal |
| 2026-10-20T03:35 | EMA 20/50 cross | buy | BTC-USD | 2.89 | — | entry |
| 2026-10-20T03:35 | EMA 20/50 cross | sell | SOL-USD | 2.80 | -0.02 | rebalance down |
| 2026-10-20T03:20 | EMA 20/50 cross | buy | ETH-USD | 14.03 | — | entry signal |
| 2026-10-20T03:10 | Squeeze breakout | buy | ETH-USD | 14.95 | — | entry signal |
| 2026-10-20T03:10 | ROC + volume | buy | ETH-USD | 15.40 | — | entry signal |
| 2026-10-20T03:10 | EMA 20/50 cross | buy | DOGE-USD | 14.07 | — | entry |
| 2026-10-20T03:05 | ROC + volume | buy | SOL-USD | 15.40 | — | entry signal |
| 2026-10-20T03:00 | EMA 20/50 cross | buy | XRP-USD | 14.08 | — | entry signal |
| 2026-10-20T02:50 | RSI(14) reversion | sell | ETH-USD | 14.39 | -0.02 | exit signal |
| 2026-10-20T02:50 | EMA 20/50 cross | buy | SOL-USD | 14.09 | — | entry signal |
| 2026-10-20T02:30 | RSI(14) reversion | sell | DOGE-USD | 11.53 | 0.02 | take-profit |
| 2026-10-20T02:05 | Three white soldiers | sell | DOGE-USD | 20.36 | -0.20 | exit signal |
| 2026-10-20T02:00 | Parabolic SAR · 1h | sell | SOL-USD | 22.59 | -0.21 | exit signal |
| 2026-10-20T02:00 | Parabolic SAR · 1h | sell | DOGE-USD | 22.72 | -0.26 | exit signal |
| 2026-10-20T02:00 | RSI(14) reversion | sell | BTC-USD | 14.40 | -0.03 | exit signal |
| 2026-10-20T01:55 | RSI(14) reversion | sell | SOL-USD | 14.40 | -0.01 | exit signal |
| 2026-10-20T01:46 | RSI(14) reversion | buy | SOL-USD | 2.89 | — | rebalance up |
| 2026-10-20T01:46 | RSI(14) reversion | buy | ETH-USD | 2.90 | — | rebalance up |
| 2026-10-20T01:46 | RSI(14) reversion | buy | BTC-USD | 2.90 | — | rebalance up |
| 2026-10-20T01:46 | RSI(14) reversion | sell | XRP-USD | 11.53 | 0.01 | exit signal |
| 2026-10-20T01:46 | Three white soldiers | buy | DOGE-USD | 20.56 | — | entry |
| 2026-10-20T01:35 | VWAP reversion | sell | XRP-USD | 13.41 | -0.01 | exit signal |
| 2026-10-20T01:30 | VWAP reversion | sell | ETH-USD | 13.39 | -0.02 | exit signal |
| 2026-10-20T01:20 | VWAP reversion | buy | XRP-USD | 13.41 | — | entry signal |
| 2026-10-20T01:20 | RSI(14) reversion | buy | XRP-USD | 11.52 | — | entry signal |
| 2026-10-20T01:20 | RSI(14) reversion | buy | SOL-USD | 11.52 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 04:25:05.000145+00:00 -> 2026-10-20 04:35:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
