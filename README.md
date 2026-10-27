# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T21:31:05.000130+00:00 · 38291 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 116, win rate 38.8%, fees £3.50, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.96 · VIX 17.55 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 37252 decisions in 3146 calls, $0.4608 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T21:31 | 2 / 2 / 1 | BTC-USD 14% |  |
| Breezy | 2026-10-27T21:31 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T21:31 | 2 / 3 / 0 | BTC-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.30 | +6.55% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.14 | 7.14 | 0 | — | 8.22 | 4.05 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.25 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.76 | 2.88 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.78 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.15 | 1.15 | 0 | — | 2.52 | 1.19 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.92 | -3.89 | -14.07 | 150 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.61 | -0.39 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.09 | 3.42 | -1.80 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.76 | -2.24 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.57 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.06 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.39 | -3.61 | 123 | 31.7 | -2.82 | -1.44 | -7.67 | 188 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.04 | -3.96 | 0 | — | -5.83 | -2.39 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 95.90 | -4.10 | 0 | — | 2.06 | 0.51 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.02 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 4.95 | 1.63 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.77 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.71 | -6.29 | 49 | 16.3 | -12.89 | -2.87 | -15.40 | 97 |
| 22 | Trend pullback · 1h | trend | 93.46 | -6.54 | 96 | 22.9 | -22.59 | -7.19 | -22.69 | 114 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.61 | -7.39 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.39 | -7.61 | 121 | 25.6 | -20.24 | -5.01 | -23.02 | 248 |
| 25 | Daily: Momentum burst | daily | 91.98 | -8.03 | 13 | 15.4 | -17.98 | -3.50 | -19.23 | 39 |
| 26 | ADX DI cross · 1h | trend | 91.88 | -8.12 | 120 | 18.3 | -14.43 | -3.15 | -16.22 | 272 |
| 27 | Copy: Insider buying | copy | 91.87 | -8.13 | 29 | 37.9 | -19.85 | -3.93 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.35 | -8.65 | 11 | 18.2 | -6.76 | -0.82 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.27 | -8.73 | 12 | 41.7 | -14.31 | -1.29 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.22 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 90.84 | -9.16 | 52 | 23.1 | -4.72 | -1.24 | -12.21 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.32 | -9.68 | 112 | 26.8 | -11.71 | -2.42 | -16.00 | 112 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.41 | -6.78 | -12.20 | 208 |
| 34 | Bollinger breakout · 1h | breakout | 88.93 | -11.07 | 109 | 26.6 | -11.40 | -2.23 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.65 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.89 | -12.12 | 205 | 47.3 | -20.57 | -3.84 | -22.35 | 388 |
| 37 | Keltner breakout · 1h | breakout | 87.35 | -12.65 | 74 | 23.0 | -18.84 | -3.63 | -23.13 | 186 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -4.00 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.02 | -12.98 | 125 | 36.0 | -12.68 | -2.01 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 85.83 | -14.17 | 114 | 14.0 | -23.74 | -4.85 | -26.59 | 230 |
| 41 | Connors RSI(2) · 1h | reversion | 85.16 | -14.84 | 176 | 40.9 | -23.72 | -7.49 | -24.36 | 179 |
| 42 | RSI momentum · 1h | momentum | 85.13 | -14.87 | 104 | 15.4 | -24.08 | -4.84 | -26.87 | 211 |
| 43 | EMA 20/50 cross · 1h | trend | 84.37 | -15.63 | 73 | 11.0 | -22.94 | -4.69 | -24.49 | 136 |
| 44 | MACD cross · 1h | trend | 84.34 | -15.66 | 244 | 22.1 | -27.77 | -5.44 | -29.94 | 476 |
| 45 | Ichimoku · 1h | trend | 84.14 | -15.86 | 68 | 11.8 | -19.92 | -4.09 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.64 | -16.36 | 101 | 14.9 | -28.26 | -5.42 | -31.19 | 203 |
| 47 | MFI reversion · 1h | reversion | 83.50 | -16.50 | 274 | 32.1 | -16.17 | -2.51 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.61 | -17.39 | 230 | 45.2 | -24.28 | -3.48 | -28.06 | 462 |
| 49 | Williams %R · 1h | reversion | 82.16 | -17.84 | 232 | 47.0 | -34.74 | -5.92 | -35.80 | 536 |
| 50 | Donchian 20/10 · 1h | breakout | 82.05 | -17.95 | 99 | 20.2 | -23.01 | -4.39 | -26.02 | 219 |
| 51 | MACD zero-line · 1h | trend | 81.37 | -18.63 | 111 | 15.3 | -24.24 | -5.24 | -25.67 | 230 |
| 52 | Agent (ML meta-label) | meta | 80.86 | -19.14 | 982 | 20.6 | -8.35 | -1.53 | -16.51 | 345 |
| 53 | Bollinger reversion · 1h | reversion | 80.85 | -19.15 | 182 | 37.4 | -29.08 | -6.00 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.58 | -19.42 | 209 | 17.7 | -31.74 | -6.67 | -33.65 | 293 |
| 55 | RSI(14) reversion · 1h | reversion | 80.44 | -19.56 | 107 | 27.1 | -15.04 | -2.79 | -24.48 | 187 |
| 56 | ROC + volume · 1h | momentum | 79.38 | -20.62 | 259 | 25.9 | -31.30 | -6.18 | -32.59 | 383 |
| 57 | Heikin-Ashi · 1h | trend | 78.42 | -21.58 | 300 | 22.7 | -43.01 | -9.54 | -44.66 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.44 | -22.56 | 285 | 29.5 | -36.97 | -7.56 | -37.89 | 545 |
| 59 | VWAP momentum · 1h | momentum | 77.04 | -22.96 | 575 | 22.3 | -49.31 | -10.82 | -51.08 | 1238 |
| 60 | Three white soldiers | momentum | 76.92 | -23.08 | 326 | 19.0 | -45.28 | -21.39 | -45.30 | 609 |
| 61 | EMA 9/21 cross · 1h | trend | 76.69 | -23.31 | 176 | 10.8 | -29.69 | -6.33 | -31.61 | 337 |
| 62 | Max aggression: 1-day momentum | meta | 72.60 | -27.40 | 20 | 30.0 | -37.60 | -2.44 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.84 | -46.16 | 811 | 22.3 | -75.04 | -27.39 | -75.26 | 1567 |
| 64 | Volume breakout | breakout | 52.28 | -47.72 | 487 | 12.7 | -63.83 | -25.87 | -64.34 | 811 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -45.07 | -98.87 | 5103 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.28 | -23.95 | -79.87 | 1416 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.65 | -46.65 | -93.70 | 2531 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.10 | -30.68 | -89.25 | 1920 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.35 | -38.45 | -91.53 | 2334 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.24 | -32.64 | -90.28 | 2182 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -55.19 | -97.87 | 3508 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -60.31 | -96.10 | 3355 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.96 | -36.87 | -93.96 | 2454 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.36 | -34.56 | -82.52 | 1691 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -56.52 | -99.43 | 5767 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -45.02 | -93.02 | 2633 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -40.18 | -95.42 | 3387 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.43 | -99.78 | 6176 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.32 | -46.85 | -92.36 | 2320 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -67.80 | -97.80 | 3590 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.91 | -98.65 | 4789 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.86 | -30.07 | -68.88 | 1184 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -59.29 | -94.70 | 2772 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.41 | -40.03 | -84.55 | 1806 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -70.04 | -99.61 | 6297 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -29.41 | -88.27 | 2224 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.43 | -19.07 | -76.79 | 1681 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.60 | -38.15 | -90.63 | 2253 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -49.25 | -96.26 | 3811 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.09 | -51.26 | -90.09 | 2130 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.66 | -24.78 | -73.43 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.20 | -18.20 | -76.42 | 1580 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -51.32 | -96.56 | 4195 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -115.83 | -99.92 | 8286 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | XRP-USD | 4.32 | -0.03 | exit signal |
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | ETH-USD | 1.35 | -0.01 | exit signal |
| 2026-10-27T20:20 | Three white soldiers | sell | SOL-USD | 19.16 | -0.12 | exit signal |
| 2026-10-27T20:15 | Three white soldiers | sell | ETH-USD | 19.20 | -0.15 | exit signal |
| 2026-10-27T20:00 | OBV trend · 1h | buy | BTC-USD | 7.33 | — | entry signal |
| 2026-10-27T20:00 | OBV trend · 1h | sell | XRP-USD | 4.13 | 0.02 | rebalance down |
| 2026-10-27T20:00 | OBV trend · 1h | sell | DOGE-USD | 4.14 | -0.00 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 2.04 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 10.56 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 6.30 | 0.09 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 6.29 | 0.00 | rebalance down |
| 2026-10-27T20:00 | Three white soldiers | buy | SOL-USD | 19.28 | — | entry |
| 2026-10-27T19:55 | Agent (rotation) | sell | TQQQ | 32.22 | 0.12 | selected signal exited |
| 2026-10-27T19:55 | Day trade: Stocks in Play ORB | sell | TSLA | 24.98 | 0.40 | target is flat |
| 2026-10-27T19:55 | Day trade: Stocks in Play ORB | sell | AMD | 24.86 | 0.28 | target is flat |
| 2026-10-27T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.82 | -0.11 | target is flat |
| 2026-10-27T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 106.48 | 0.40 | target is flat |
| 2026-10-27T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 97.54 | -0.24 | target is flat |
| 2026-10-27T19:55 | Agent (ML meta-label) | buy | SOXL | 4.11 | — | rebalance up |
| 2026-10-27T19:55 | Agent (ML meta-label) | buy | META | 20.18 | — | following VWAP reversion |
| 2026-10-27T19:55 | Agent (aggressive) | sell | PLTR | 43.97 | -0.12 | selected signal exited |
| 2026-10-27T19:55 | Agent | sell | PLTR | 17.96 | -0.05 | selected signal exited |
| 2026-10-27T19:55 | Three white soldiers | sell | SPY | 19.33 | -0.02 | end-of-day flatten |
| 2026-10-27T19:55 | Three white soldiers | sell | SOL-USD | 19.17 | -0.14 | exit signal |
| 2026-10-27T19:55 | Volume breakout | sell | AAPL | 13.05 | -0.05 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | UPRO | 7.80 | 0.04 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | TQQQ | 7.83 | 0.07 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | TNA | 7.86 | 0.15 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | TECL | 7.84 | 0.08 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | SPY | 7.77 | 0.01 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | QQQ | 3.89 | 0.01 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | LABU | 7.91 | 0.39 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | IWM | 9.45 | 0.05 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | GOOGL | 7.81 | 0.04 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | ETHU | 2.24 | 0.02 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | BITX | 7.84 | 0.08 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | AMZN | 7.83 | 0.08 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 30m | sell | AAPL | 7.76 | 0.02 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 15m | sell | UPRO | 7.26 | 0.04 | end-of-day flatten |
| 2026-10-27T19:55 | Opening range 15m | sell | TQQQ | 7.29 | 0.07 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 21:31:05.000130+00:00 -> 2026-10-27 21:41:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
