# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-24T03:10:05.000122+00:00 · 33775 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 2445 decisions in 489 calls, $0.0342 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-24T03:10 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-10-24T03:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-24T03:10 | 1 / 4 / 0 | ETH-USD 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |
| RSI(14) reversion | TSLA | 1.70 | +3.99% | 7 |
| Opening range 30m | PLTR | 1.69 | +3.38% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.17 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.19 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.97 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.03 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.61 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.50 | 0.50 | 89 | 44.9 | -11.85 | -3.28 | -13.74 | 156 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 4.88 | 2.37 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.37 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.20 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.34 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 0.86 | -7.93 | 8 |
| 15 | Hold BTC | benchmark | 95.69 | -4.31 | 0 | — | 0.64 | 0.28 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.03 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.74 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.16 | -5.84 | 25 | 40.0 | -14.79 | -2.80 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.58 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -7.01 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.53 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.45 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.37 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -20.83 | -4.89 | -24.17 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.38 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.83 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.37 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.23 | -8.77 | 108 | 18.5 | -11.79 | -2.40 | -14.69 | 256 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.04 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -12.82 | -2.71 | -16.01 | 113 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.54 | -7.77 | -12.26 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.77 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 89.03 | -10.97 | 105 | 27.6 | -12.06 | -2.37 | -16.41 | 240 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.26 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.43 | -3.85 | -22.47 | 387 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.60 | -4.76 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -22.71 | -4.50 | -25.03 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.67 | -17.87 | 703 |
| 40 | Supertrend · 1h | trend | 85.63 | -14.37 | 109 | 14.7 | -24.13 | -5.06 | -26.68 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.62 | -14.38 | 101 | 15.8 | -21.39 | -4.55 | -23.32 | 215 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.99 | -26.96 | 196 |
| 43 | MACD cross · 1h | trend | 84.49 | -15.51 | 221 | 23.1 | -23.36 | -4.66 | -26.51 | 454 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.79 | -25.24 | 110 |
| 45 | Z-score reversion · 1h | reversion | 83.63 | -16.37 | 106 | 34.0 | -15.14 | -2.56 | -21.48 | 199 |
| 46 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.12 | -5.18 | -28.32 | 211 |
| 47 | MFI reversion · 1h | reversion | 81.96 | -18.05 | 258 | 31.8 | -17.37 | -2.79 | -20.54 | 145 |
| 48 | MACD zero-line · 1h | trend | 81.57 | -18.43 | 105 | 15.2 | -21.70 | -4.53 | -25.14 | 218 |
| 49 | Three white soldiers | momentum | 81.27 | -18.73 | 275 | 20.0 | -43.45 | -20.19 | -43.56 | 586 |
| 50 | Donchian 20/10 · 1h | breakout | 81.26 | -18.73 | 97 | 19.6 | -24.19 | -4.66 | -27.15 | 216 |
| 51 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.66 | -6.94 | -33.18 | 306 |
| 52 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -35.78 | -6.37 | -36.69 | 529 |
| 53 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.47 | -6.56 | -32.19 | 367 |
| 54 | CCI reversion · 1h | reversion | 79.94 | -20.06 | 199 | 42.7 | -26.68 | -4.00 | -28.17 | 452 |
| 55 | Agent (ML meta-label) | meta | 79.50 | -20.50 | 858 | 18.6 | -11.58 | -2.04 | -16.61 | 370 |
| 56 | Heikin-Ashi · 1h | trend | 78.64 | -21.36 | 271 | 22.9 | -43.24 | -10.07 | -43.93 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -30.20 | -6.01 | -31.38 | 379 |
| 58 | RSI(14) reversion · 1h | reversion | 77.40 | -22.60 | 92 | 22.8 | -15.63 | -2.89 | -23.51 | 187 |
| 59 | Candlestick reversal · 1h | reversion | 77.10 | -22.90 | 256 | 28.5 | -35.35 | -6.68 | -36.26 | 544 |
| 60 | EMA 9/21 cross · 1h | trend | 77.02 | -22.98 | 161 | 11.8 | -30.34 | -6.19 | -33.63 | 318 |
| 61 | VWAP momentum · 1h | momentum | 75.49 | -24.51 | 527 | 21.1 | -50.82 | -11.70 | -50.97 | 1222 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.95 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.58 | -42.42 | 706 | 22.7 | -74.94 | -26.97 | -74.98 | 1548 |
| 64 | Volume breakout | breakout | 57.01 | -42.99 | 418 | 13.2 | -61.09 | -25.67 | -61.09 | 765 |
| 65 | Squeeze breakout | breakout | 53.70 | -46.30 | 548 | 14.2 | -66.44 | -28.15 | -66.49 | 1148 |
| 66 | Donchian 55/20 | breakout | 53.11 | -46.89 | 565 | 19.1 | -71.48 | -23.15 | -71.62 | 1249 |
| 67 | RSI(14) reversion | reversion | 52.69 | -47.31 | 833 | 26.3 | -76.68 | -19.60 | -76.87 | 1674 |
| 68 | EMA 20/50 cross | trend | 51.87 | -48.13 | 622 | 20.1 | -78.86 | -23.46 | -79.15 | 1409 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -43.03 | -98.67 | 5021 |
| 70 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -44.97 | -93.81 | 2510 |
| 71 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.52 | -29.91 | -88.64 | 1880 |
| 72 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.14 | -37.42 | -91.20 | 2306 |
| 73 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.32 | -30.49 | -90.36 | 2147 |
| 74 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -51.89 | -97.73 | 3471 |
| 75 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.01 | -57.77 | -96.03 | 3327 |
| 76 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.66 | -34.19 | -93.71 | 2419 |
| 77 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.68 | -35.10 | -82.73 | 1681 |
| 78 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -52.17 | -99.35 | 5700 |
| 79 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.26 | -41.13 | -92.31 | 2579 |
| 80 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -38.80 | -95.29 | 3350 |
| 81 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -74.22 | -99.75 | 6100 |
| 82 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.06 | -44.09 | -92.07 | 2317 |
| 83 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -59.70 | -97.51 | 3515 |
| 84 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -56.63 | -98.50 | 4723 |
| 85 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 86 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.23 | -55.45 | -94.26 | 2734 |
| 87 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.64 | -38.13 | -83.70 | 1768 |
| 88 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -62.32 | -99.54 | 6177 |
| 89 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.69 | -28.57 | -87.73 | 2192 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.31 | -37.47 | -90.38 | 2243 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -45.93 | -95.97 | 3753 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.53 | -49.51 | -89.62 | 2090 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -74.76 | -17.53 | -74.90 | 1550 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.11 | -46.67 | -96.15 | 4126 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -95.58 | -99.90 | 8143 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-24T03:05 | Volume breakout | buy | SOL-USD | 14.27 | — | entry signal |
| 2026-10-24T03:05 | Squeeze breakout | buy | SOL-USD | 13.45 | — | entry signal |
| 2026-10-24T03:00 | MFI reversion · 1h | buy | XRP-USD | 20.51 | — | entry signal |
| 2026-10-24T03:00 | CCI reversion · 1h | buy | DOGE-USD | 4.00 | — | entry signal |
| 2026-10-24T03:00 | VWAP momentum · 1h | buy | BTC-USD | 6.86 | — | entry signal |
| 2026-10-24T02:25 | EMA 20/50 cross | buy | DOGE-USD | 12.98 | — | entry signal |
| 2026-10-24T02:10 | RSI(14) reversion | sell | XRP-USD | 13.16 | -0.06 | exit signal |
| 2026-10-24T02:10 | RSI(14) reversion | sell | SOL-USD | 13.17 | -0.05 | exit signal |
| 2026-10-24T02:00 | VWAP reversion · 1h | sell | XRP-USD | 25.01 | -0.22 | exit signal |
| 2026-10-24T02:00 | VWAP reversion · 1h | sell | SOL-USD | 25.02 | -0.21 | exit signal |
| 2026-10-24T02:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.00 | — | entry signal |
| 2026-10-24T01:55 | RSI(14) reversion | sell | ETH-USD | 10.57 | -0.02 | exit signal |
| 2026-10-24T01:55 | Squeeze breakout | buy | ETH-USD | 13.45 | — | entry signal |
| 2026-10-24T01:25 | ROC + volume | buy | DOGE-USD | 14.40 | — | entry signal |
| 2026-10-24T01:15 | RSI(14) reversion | sell | DOGE-USD | 10.58 | 0.02 | exit signal |
| 2026-10-24T00:20 | RSI(14) reversion | buy | SOL-USD | 2.63 | — | rebalance up |
| 2026-10-24T00:15 | RSI(14) reversion | buy | XRP-USD | 2.64 | — | rebalance up |
| 2026-10-24T00:00 | VWAP reversion · 1h | buy | XRP-USD | 25.23 | — | entry signal |
| 2026-10-24T00:00 | VWAP reversion · 1h | buy | SOL-USD | 25.23 | — | entry signal |
| 2026-10-24T00:00 | RSI(14) reversion · 1h | buy | XRP-USD | 9.69 | — | entry signal |
| 2026-10-23T23:51 | RSI(14) reversion | sell | BTC-USD | 10.49 | -0.02 | exit signal |
| 2026-10-23T23:20 | RSI(14) reversion | buy | BTC-USD | 10.51 | — | entry signal |
| 2026-10-23T23:20 | RSI(14) reversion | sell | DOGE-USD | 2.67 | -0.01 | rebalance down |
| 2026-10-23T23:15 | RSI(14) reversion | buy | DOGE-USD | 2.65 | — | rebalance up |
| 2026-10-23T23:15 | RSI(14) reversion | sell | BTC-USD | 10.49 | -0.10 | stop-loss |
| 2026-10-23T23:10 | CCI reversion · 1h | sell | XRP-USD | 4.65 | -0.16 | stop-loss |
| 2026-10-23T23:10 | RSI(14) reversion · 1h | sell | XRP-USD | 10.79 | -0.32 | stop-loss |
| 2026-10-23T23:05 | RSI(14) reversion | buy | XRP-USD | 10.59 | — | entry signal |
| 2026-10-23T23:05 | RSI(14) reversion | buy | SOL-USD | 10.59 | — | entry signal |
| 2026-10-23T23:05 | RSI(14) reversion | buy | ETH-USD | 10.59 | — | entry signal |
| 2026-10-23T23:05 | RSI(14) reversion | buy | DOGE-USD | 10.59 | — | entry signal |
| 2026-10-23T23:05 | RSI(14) reversion | buy | BTC-USD | 10.59 | — | entry signal |
| 2026-10-23T23:01 | VWAP reversion | sell | XRP-USD | 9.95 | -0.06 | Kill switch: down 50% from peak |
| 2026-10-23T23:01 | VWAP reversion | sell | SOL-USD | 9.95 | -0.06 | Kill switch: down 50% from peak |
| 2026-10-23T23:01 | VWAP reversion | sell | ETH-USD | 9.95 | -0.06 | Kill switch: down 50% from peak |
| 2026-10-23T23:01 | VWAP reversion | sell | DOGE-USD | 9.95 | -0.06 | Kill switch: down 50% from peak |
| 2026-10-23T23:01 | VWAP reversion | sell | BTC-USD | 9.95 | -0.06 | Kill switch: down 50% from peak |
| 2026-10-23T23:00 | Supertrend · 1h | sell | DOGE-USD | 21.00 | -0.72 | exit signal |
| 2026-10-23T23:00 | MACD cross · 1h | sell | ETH-USD | 11.94 | -0.16 | exit signal |
| 2026-10-23T23:00 | VWAP reversion | buy | XRP-USD | 10.01 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-26 03:10:05.000122+00:00 -> 2026-10-24 03:20:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
