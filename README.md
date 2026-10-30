# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T04:45:05.000150+00:00 · 41002 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.68 (-8.32%)

Closed trades 122, win rate 40.2%, fees £3.61, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-29)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.18 · VIX 17.20 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, IWM 5.9, LABU 5.7, AAPL 5.2, SQQQ 4.9, PLTR 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 3390 decisions in 678 calls, $0.0475 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T04:45 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-10-30T04:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-30T04:45 | 3 / 2 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.23 | 2.03 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.23 | 6.23 | 0 | — | 7.59 | 3.72 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.04 | 1.04 | 0 | — | 4.35 | 1.89 | -5.02 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Hold SPY | benchmark | 98.94 | -1.06 | 0 | — | 0.56 | 0.37 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 7.05 | 3.33 | -1.98 | 90 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.74 | -2.52 | -5.83 | 1 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.03 | -2.96 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -5.09 | -5.81 | -5.22 | 22 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.76 | -3.24 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.20 | -2.06 | -7.40 | 174 |
| 17 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.33 | -4.76 | 27 |
| 18 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 5.27 | 1.72 | -8.76 | 204 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 93.44 | -6.57 | 0 | — | 2.42 | 0.57 | -14.57 | 1 |
| 20 | Copy: Insider buying | copy | 92.65 | -7.35 | 33 | 36.4 | -21.70 | -4.41 | -23.91 | 67 |
| 21 | Hold BTC | benchmark | 92.32 | -7.68 | 0 | — | 0.27 | 0.22 | -12.47 | 1 |
| 22 | Donchian 55/20 · 1h | breakout | 92.27 | -7.73 | 54 | 14.8 | -13.77 | -3.09 | -15.52 | 102 |
| 23 | Daily: Momentum burst | daily | 91.96 | -8.04 | 15 | 13.3 | -12.93 | -2.43 | -17.57 | 35 |
| 24 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.10 | -3.30 | -17.21 | 580 |
| 25 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.47 | -5.57 | -12.21 | 218 |
| 26 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.20 | -7.35 | -21.50 | 99 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.75 | -2.67 | -16.91 | 1 |
| 28 | Squeeze breakout · 1h | breakout | 90.61 | -9.39 | 56 | 23.2 | -4.98 | -1.35 | -12.65 | 93 |
| 29 | Daily: Bullish score | daily | 90.47 | -9.53 | 12 | 25.0 | -5.76 | -0.69 | -14.40 | 14 |
| 30 | Parabolic SAR · 1h | trend | 90.04 | -9.96 | 137 | 28.5 | -19.98 | -4.64 | -20.21 | 248 |
| 31 | ADX DI cross · 1h | trend | 89.45 | -10.55 | 137 | 19.7 | -15.07 | -3.02 | -16.59 | 260 |
| 32 | Stochastic reversion · 1h | reversion | 87.90 | -12.10 | 218 | 48.2 | -15.83 | -2.74 | -22.69 | 381 |
| 33 | Max aggression: 5-day momentum | meta | 87.67 | -12.33 | 14 | 42.9 | -14.69 | -1.27 | -27.23 | 25 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.66 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.60 | -13.40 | 124 | 29.8 | -14.65 | -3.12 | -17.33 | 107 |
| 36 | Bollinger breakout · 1h | breakout | 85.97 | -14.03 | 128 | 26.6 | -11.99 | -2.16 | -19.10 | 244 |
| 37 | Z-score reversion · 1h | reversion | 85.80 | -14.20 | 126 | 35.7 | -13.59 | -2.11 | -21.48 | 206 |
| 38 | Keltner breakout · 1h | breakout | 85.35 | -14.65 | 84 | 23.8 | -22.88 | -4.62 | -23.96 | 196 |
| 39 | Ichimoku · 1h | trend | 84.45 | -15.55 | 75 | 10.7 | -18.75 | -3.76 | -24.73 | 118 |
| 40 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -16.00 | -4.59 | -18.10 | 709 |
| 41 | Connors RSI(2) · 1h | reversion | 84.20 | -15.80 | 185 | 40.5 | -21.05 | -6.72 | -21.83 | 163 |
| 42 | Supertrend · 1h | trend | 83.74 | -16.26 | 126 | 14.3 | -23.64 | -4.52 | -26.18 | 218 |
| 43 | RSI momentum · 1h | momentum | 83.31 | -16.69 | 122 | 13.1 | -20.37 | -4.04 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.47 | -17.53 | 113 | 14.2 | -27.74 | -5.35 | -30.37 | 208 |
| 45 | MFI reversion · 1h | reversion | 82.08 | -17.92 | 288 | 32.3 | -15.73 | -2.46 | -19.58 | 153 |
| 46 | Williams %R · 1h | reversion | 81.80 | -18.20 | 249 | 47.8 | -33.46 | -5.89 | -34.73 | 529 |
| 47 | MACD cross · 1h | trend | 81.65 | -18.35 | 275 | 24.7 | -27.33 | -4.87 | -29.24 | 471 |
| 48 | EMA 20/50 cross · 1h | trend | 81.61 | -18.39 | 86 | 11.6 | -21.93 | -3.94 | -24.96 | 137 |
| 49 | CCI reversion · 1h | reversion | 81.54 | -18.46 | 245 | 46.5 | -21.60 | -3.04 | -28.07 | 451 |
| 50 | Bollinger reversion · 1h | reversion | 81.03 | -18.97 | 191 | 38.7 | -29.92 | -6.18 | -31.74 | 369 |
| 51 | Donchian 20/10 · 1h | breakout | 80.56 | -19.44 | 108 | 21.3 | -22.33 | -4.09 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.53 | -20.48 | 225 | 16.9 | -34.08 | -6.63 | -36.19 | 300 |
| 53 | MACD zero-line · 1h | trend | 79.11 | -20.89 | 129 | 16.3 | -24.19 | -4.86 | -26.72 | 213 |
| 54 | RSI(14) reversion · 1h | reversion | 78.41 | -21.59 | 113 | 26.5 | -20.97 | -3.84 | -24.99 | 207 |
| 55 | Heikin-Ashi · 1h | trend | 77.24 | -22.76 | 327 | 23.9 | -42.02 | -9.09 | -42.36 | 665 |
| 56 | Candlestick reversal · 1h | reversion | 76.85 | -23.15 | 304 | 29.9 | -34.58 | -6.87 | -36.08 | 548 |
| 57 | ROC + volume · 1h | momentum | 76.53 | -23.47 | 286 | 25.9 | -30.41 | -5.32 | -31.81 | 389 |
| 58 | Agent (ML meta-label) | meta | 76.39 | -23.61 | 1113 | 20.9 | -15.09 | -3.07 | -19.01 | 336 |
| 59 | Three white soldiers | momentum | 74.91 | -25.09 | 359 | 17.5 | -44.44 | -20.35 | -44.75 | 613 |
| 60 | EMA 9/21 cross · 1h | trend | 74.67 | -25.33 | 195 | 10.3 | -31.47 | -6.28 | -32.26 | 341 |
| 61 | VWAP momentum · 1h | momentum | 73.81 | -26.19 | 632 | 22.9 | -51.60 | -10.89 | -51.83 | 1241 |
| 62 | Max aggression: 1-day momentum | meta | 72.15 | -27.85 | 21 | 33.3 | -35.91 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -42.10 | -98.86 | 5188 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.67 | -23.17 | -78.75 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -43.95 | -93.53 | 2536 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.47 | -29.49 | -88.63 | 1911 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.11 | -36.49 | -91.23 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.48 | -31.55 | -90.48 | 2253 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -49.28 | -97.73 | 3505 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -55.61 | -96.14 | 3388 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.96 | -34.86 | -93.97 | 2471 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.09 | -33.38 | -82.09 | 1691 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -54.61 | -99.44 | 5778 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.81 | -41.10 | -92.94 | 2630 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -36.76 | -95.51 | 3464 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -69.18 | -99.78 | 6177 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -42.05 | -91.95 | 2304 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.00 | -26.87 | -75.11 | 1565 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -59.31 | -97.68 | 3575 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -59.05 | -98.63 | 4782 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.54 | -28.05 | -70.06 | 1210 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -51.36 | -94.80 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.72 | -37.53 | -84.81 | 1828 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -67.86 | -99.60 | 6288 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.04 | -29.57 | -88.18 | 2206 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.11 | -19.61 | -77.35 | 1678 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -37.36 | -90.68 | 2236 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -50.82 | -96.26 | 3776 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.76 | -50.48 | -89.90 | 2135 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.48 | -25.55 | -64.48 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.50 | -25.24 | -73.53 | 1279 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.88 | -18.33 | -75.92 | 1563 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.68 | -50.29 | -96.69 | 4191 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.22 | -99.92 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T04:05 | Three white soldiers | sell | ETH-USD | 14.90 | -0.06 | exit signal |
| 2026-10-30T04:05 | Three white soldiers | sell | DOGE-USD | 11.39 | -0.11 | exit signal |
| 2026-10-30T04:00 | Agent (ML meta-label) | buy | DOGE-USD | 9.09 | — | entry |
| 2026-10-30T04:00 | Agent (ML meta-label) | sell | ETH-USD | 8.67 | -0.05 | selected signal exited |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | XRP-USD | 11.99 | — | entry signal |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | SOL-USD | 16.31 | — | entry signal |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | DOGE-USD | 16.31 | — | entry signal |
| 2026-10-30T04:00 | CCI reversion · 1h | buy | BTC-USD | 16.31 | — | entry signal |
| 2026-10-30T04:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.57 | — | entry signal |
| 2026-10-30T04:00 | Z-score reversion · 1h | buy | BTC-USD | 12.26 | — | entry signal |
| 2026-10-30T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.33 | — | entry signal |
| 2026-10-30T04:00 | VWAP momentum · 1h | buy | BTC-USD | 14.76 | — | entry signal |
| 2026-10-30T03:55 | Agent (ML meta-label) | buy | ETH-USD | 8.72 | — | entry |
| 2026-10-30T03:55 | Agent (ML meta-label) | sell | DOGE-USD | 8.46 | -0.03 | selected signal exited |
| 2026-10-30T03:47 | Three white soldiers | buy | DOGE-USD | 3.73 | — | rebalance up |
| 2026-10-30T03:47 | Three white soldiers | sell | ETH-USD | 3.73 | -0.01 | rebalance down |
| 2026-10-30T03:45 | Three white soldiers | buy | DOGE-USD | 7.76 | — | entry signal |
| 2026-10-30T03:45 | Three white soldiers | sell | XRP-USD | 3.74 | -0.01 | rebalance down |
| 2026-10-30T03:45 | Three white soldiers | sell | SOL-USD | 4.02 | 0.07 | rebalance down |
| 2026-10-30T03:40 | Agent (ML meta-label) | buy | DOGE-USD | 8.49 | — | entry |
| 2026-10-30T03:40 | Three white soldiers | buy | BTC-USD | 18.47 | — | entry signal |
| 2026-10-30T03:36 | Three white soldiers | buy | XRP-USD | 18.71 | — | entry signal |
| 2026-10-30T03:36 | Three white soldiers | buy | ETH-USD | 18.71 | — | entry signal |
| 2026-10-30T03:25 | Agent (ML meta-label) | sell | DOGE-USD | 9.17 | 0.16 | selected signal exited |
| 2026-10-30T03:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 5.81 | — | entry signal |
| 2026-10-30T03:00 | RSI(14) reversion · 1h | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-10-30T02:20 | Three white soldiers | buy | SOL-USD | 18.63 | — | entry signal |
| 2026-10-30T02:05 | Agent (ML meta-label) | buy | DOGE-USD | 9.02 | — | entry |
| 2026-10-30T02:00 | Agent (ML meta-label) | sell | DOGE-USD | 9.02 | -0.03 | selected signal exited |
| 2026-10-30T01:25 | Agent (ML meta-label) | buy | DOGE-USD | 9.04 | — | entry |
| 2026-10-30T01:20 | Agent (ML meta-label) | sell | DOGE-USD | 9.04 | -0.06 | selected signal exited |
| 2026-10-30T01:05 | Agent (ML meta-label) | buy | DOGE-USD | 9.11 | — | entry |
| 2026-10-30T01:05 | Agent (ML meta-label) | sell | SOL-USD | 9.11 | -0.09 | selected signal exited |
| 2026-10-30T01:00 | Agent (ML meta-label) | buy | SOL-USD | 9.20 | — | entry |
| 2026-10-30T00:30 | Agent (ML meta-label) | sell | XRP-USD | 9.20 | -0.12 | selected signal exited |
| 2026-10-30T00:25 | Agent (ML meta-label) | buy | XRP-USD | 9.32 | — | entry |
| 2026-10-30T00:25 | VWAP reversion · 1h | sell | XRP-USD | 24.38 | -0.90 | stop-loss |
| 2026-10-30T00:25 | RSI(14) reversion · 1h | sell | XRP-USD | 6.26 | -0.08 | stop-loss |
| 2026-10-30T00:25 | RSI(14) reversion · 1h | sell | DOGE-USD | 12.59 | -0.62 | stop-loss |
| 2026-10-30T00:20 | VWAP reversion · 1h | sell | BTC-USD | 24.60 | -0.68 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 04:45:05.000150+00:00 -> 2026-10-30 04:55:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
