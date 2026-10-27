# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T12:35:05.000163+00:00 · 37865 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 110, win rate 39.1%, fees £3.39, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 9304 decisions in 1868 calls, $0.1301 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T12:35 | 5 / 0 / 0 | XRP-USD 19%, BTC-USD 16% |  |
| Breezy | 2026-10-27T12:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T12:35 | 4 / 1 / 0 | ETH-USD 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.20 | +6.90% | 7 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 4 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.15 | 8.15 | 0 | — | 8.51 | 4.26 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.48 | 1.14 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.57 | 5.57 | 21 | 33.3 | 10.57 | 2.73 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.21 | 2.01 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.09 | -3.35 | -14.02 | 151 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.15 | 0.15 | 0 | — | 2.80 | 1.29 | -5.02 | 2 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.93 | -1.07 | 0 | — | -0.04 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 8.31 | 3.46 | -1.94 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -4.13 | -4.73 | -4.49 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -1.99 | -5.83 | 2 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.69 | -3.31 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.19 | -3.81 | 121 | 31.4 | -1.91 | -1.09 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.06 | -7.93 | 9 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Hold BTC | benchmark | 95.19 | -4.81 | 0 | — | 1.91 | 0.48 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.05 | -4.95 | 0 | — | -6.95 | -2.93 | -7.83 | 1 |
| 19 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 5.02 | 1.64 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.97 | -3.34 | -17.21 | 577 |
| 22 | Donchian 55/20 · 1h | breakout | 91.67 | -8.33 | 49 | 16.3 | -16.01 | -3.62 | -16.70 | 98 |
| 23 | Daily: Momentum burst | daily | 91.43 | -8.57 | 10 | 10.0 | -19.39 | -3.78 | -20.15 | 45 |
| 24 | Max aggression: 5-day momentum | meta | 91.26 | -8.74 | 11 | 45.5 | -15.58 | -1.42 | -27.80 | 25 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.16 | -16.91 | 2 |
| 26 | Squeeze breakout · 1h | breakout | 90.93 | -9.07 | 52 | 23.1 | -4.54 | -1.18 | -12.00 | 91 |
| 27 | Daily: Bullish score | daily | 90.70 | -9.30 | 11 | 18.2 | -6.77 | -0.82 | -14.40 | 16 |
| 28 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.89 | -6.82 | -12.54 | 214 |
| 29 | Parabolic SAR · 1h | trend | 89.95 | -10.05 | 121 | 25.6 | -21.91 | -5.59 | -22.00 | 247 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 89.44 | -10.56 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 31 | ADX DI cross · 1h | trend | 88.90 | -11.10 | 114 | 17.5 | -13.67 | -2.99 | -14.27 | 263 |
| 32 | Volume breakout · 1h | breakout | 88.63 | -11.37 | 104 | 23.1 | -14.40 | -3.04 | -16.13 | 112 |
| 33 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.03 | -3.27 | -14.77 | 95 |
| 34 | Stochastic reversion · 1h | reversion | 87.89 | -12.11 | 198 | 47.0 | -21.89 | -4.00 | -23.21 | 392 |
| 35 | Bollinger breakout · 1h | breakout | 87.23 | -12.77 | 109 | 26.6 | -14.32 | -2.86 | -17.92 | 239 |
| 36 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.53 | -4.11 | -17.87 | 704 |
| 37 | Keltner breakout · 1h | breakout | 85.62 | -14.38 | 74 | 23.0 | -20.87 | -4.11 | -23.13 | 183 |
| 38 | Connors RSI(2) · 1h | reversion | 85.11 | -14.89 | 174 | 40.2 | -26.47 | -7.95 | -26.96 | 198 |
| 39 | Z-score reversion · 1h | reversion | 84.90 | -15.10 | 116 | 33.6 | -14.48 | -2.37 | -21.48 | 211 |
| 40 | EMA 20/50 cross · 1h | trend | 84.46 | -15.54 | 73 | 11.0 | -21.74 | -4.28 | -23.33 | 130 |
| 41 | RSI momentum · 1h | momentum | 83.56 | -16.44 | 104 | 15.4 | -22.10 | -4.31 | -23.76 | 201 |
| 42 | MACD cross · 1h | trend | 82.97 | -17.03 | 244 | 22.1 | -29.74 | -6.24 | -30.18 | 478 |
| 43 | Supertrend · 1h | trend | 82.96 | -17.04 | 114 | 14.0 | -27.65 | -5.91 | -28.20 | 223 |
| 44 | MFI reversion · 1h | reversion | 82.78 | -17.22 | 263 | 31.6 | -16.30 | -2.51 | -20.54 | 153 |
| 45 | Ichimoku · 1h | trend | 82.24 | -17.76 | 68 | 11.8 | -21.80 | -4.56 | -24.73 | 109 |
| 46 | Triple EMA stack · 1h | trend | 81.82 | -18.18 | 101 | 14.9 | -29.33 | -5.83 | -30.81 | 203 |
| 47 | Bollinger reversion · 1h | reversion | 81.29 | -18.70 | 179 | 37.4 | -30.00 | -6.18 | -31.17 | 368 |
| 48 | CCI reversion · 1h | reversion | 81.25 | -18.75 | 222 | 44.6 | -25.67 | -3.69 | -28.06 | 466 |
| 49 | Williams %R · 1h | reversion | 81.22 | -18.78 | 228 | 46.1 | -35.64 | -6.07 | -35.84 | 540 |
| 50 | MACD zero-line · 1h | trend | 80.27 | -19.73 | 111 | 15.3 | -24.10 | -5.16 | -24.91 | 217 |
| 51 | Donchian 20/10 · 1h | breakout | 79.85 | -20.15 | 99 | 20.2 | -25.64 | -5.03 | -27.36 | 212 |
| 52 | OBV trend · 1h | momentum | 78.96 | -21.04 | 206 | 17.5 | -34.29 | -7.22 | -34.29 | 291 |
| 53 | Agent (ML meta-label) | meta | 78.86 | -21.14 | 924 | 19.4 | -9.04 | -1.56 | -15.48 | 364 |
| 54 | RSI(14) reversion · 1h | reversion | 78.35 | -21.65 | 100 | 24.0 | -17.57 | -2.82 | -24.48 | 208 |
| 55 | Three white soldiers | momentum | 78.08 | -21.92 | 307 | 19.2 | -44.05 | -20.21 | -44.48 | 603 |
| 56 | ROC + volume · 1h | momentum | 76.58 | -23.42 | 250 | 24.0 | -32.48 | -6.48 | -32.97 | 373 |
| 57 | Heikin-Ashi · 1h | trend | 76.51 | -23.50 | 290 | 22.1 | -45.03 | -10.35 | -45.06 | 657 |
| 58 | Candlestick reversal · 1h | reversion | 76.36 | -23.64 | 272 | 27.9 | -34.78 | -6.48 | -34.88 | 572 |
| 59 | EMA 9/21 cross · 1h | trend | 75.18 | -24.82 | 176 | 10.8 | -33.08 | -7.14 | -33.61 | 330 |
| 60 | VWAP momentum · 1h | momentum | 75.03 | -24.97 | 558 | 21.0 | -49.49 | -11.05 | -50.21 | 1239 |
| 61 | Max aggression: 1-day momentum | meta | 67.16 | -32.84 | 19 | 26.3 | -42.14 | -2.87 | -50.32 | 42 |
| 62 | ROC + volume | momentum | 54.75 | -45.25 | 764 | 22.1 | -74.03 | -25.95 | -74.18 | 1565 |
| 63 | Volume breakout | breakout | 53.52 | -46.48 | 462 | 12.8 | -62.80 | -26.13 | -63.06 | 803 |
| 64 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -43.88 | -98.90 | 5162 |
| 65 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.95 | -22.44 | -79.64 | 1426 |
| 66 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.69 | -43.62 | -93.74 | 2534 |
| 67 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.03 | -29.27 | -89.32 | 1929 |
| 68 | Squeeze breakout | breakout | 50.42 | -49.59 | 599 | 14.2 | -67.68 | -28.58 | -68.19 | 1180 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -36.28 | -91.47 | 2343 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.38 | -31.53 | -90.39 | 2157 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -50.80 | -97.89 | 3524 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -52.62 | -96.17 | 3378 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.10 | -36.39 | -94.10 | 2444 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.30 | -32.61 | -82.58 | 1687 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -53.42 | -99.43 | 5786 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.64 | -40.41 | -92.82 | 2621 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -37.85 | -95.41 | 3359 |
| 78 | Donchian 55/20 | breakout | 50.22 | -49.78 | 616 | 19.5 | -72.11 | -23.27 | -72.68 | 1281 |
| 79 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.84 | -99.78 | 6171 |
| 80 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -44.86 | -92.29 | 2336 |
| 81 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -59.97 | -97.74 | 3581 |
| 82 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.86 | -98.66 | 4806 |
| 83 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.54 | -54.02 | -94.56 | 2774 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -38.74 | -84.40 | 1814 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -65.09 | -99.61 | 6307 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -28.89 | -88.31 | 2231 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.11 | -19.35 | -77.44 | 1705 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.58 | -90.65 | 2285 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.29 | -47.68 | -96.30 | 3830 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.03 | -49.81 | -90.03 | 2137 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.16 | -17.96 | -76.40 | 1585 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.57 | -48.97 | -96.57 | 4207 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.53 | -99.92 | 8279 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T12:35 | Three white soldiers | buy | XRP-USD | 19.54 | — | entry signal |
| 2026-10-27T12:35 | Donchian 55/20 | buy | SOL-USD | 5.07 | — | entry signal |
| 2026-10-27T12:35 | Donchian 55/20 | buy | DOGE-USD | 10.06 | — | entry signal |
| 2026-10-27T12:35 | Donchian 55/20 | sell | XRP-USD | 2.52 | -0.01 | rebalance down |
| 2026-10-27T12:35 | ROC + volume | buy | XRP-USD | 13.70 | — | entry signal |
| 2026-10-27T12:30 | Three white soldiers | buy | ETH-USD | 19.55 | — | entry signal |
| 2026-10-27T12:30 | Volume breakout | buy | XRP-USD | 13.40 | — | entry signal |
| 2026-10-27T12:30 | Volume breakout | buy | ETH-USD | 13.40 | — | entry signal |
| 2026-10-27T12:30 | Donchian 55/20 | buy | ETH-USD | 12.58 | — | entry signal |
| 2026-10-27T12:30 | Donchian 55/20 | buy | BTC-USD | 12.58 | — | entry signal |
| 2026-10-27T12:25 | Squeeze breakout | buy | SOL-USD | 12.61 | — | entry signal |
| 2026-10-27T12:25 | Squeeze breakout | buy | ETH-USD | 12.61 | — | entry signal |
| 2026-10-27T12:25 | Donchian 55/20 | buy | XRP-USD | 12.59 | — | entry signal |
| 2026-10-27T12:00 | VWAP momentum · 1h | sell | ETH-USD | 6.78 | -0.04 | exit signal |
| 2026-10-27T11:50 | ROC + volume | sell | SOL-USD | 13.64 | -0.08 | exit signal |
| 2026-10-27T11:45 | Donchian 55/20 | sell | XRP-USD | 12.49 | -0.13 | stop-loss |
| 2026-10-27T11:30 | Three white soldiers | sell | XRP-USD | 19.53 | -0.02 | exit signal |
| 2026-10-27T11:25 | Volume breakout | sell | SOL-USD | 13.35 | -0.11 | exit signal |
| 2026-10-27T11:20 | Volume breakout | sell | ETH-USD | 13.36 | -0.10 | exit signal |
| 2026-10-27T11:16 | Volume breakout | sell | BTC-USD | 13.39 | -0.08 | exit signal |
| 2026-10-27T11:05 | Donchian 55/20 | buy | XRP-USD | 12.62 | — | entry signal |
| 2026-10-27T11:00 | VWAP momentum · 1h | buy | XRP-USD | 6.38 | — | entry signal |
| 2026-10-27T11:00 | VWAP momentum · 1h | buy | ETH-USD | 6.82 | — | entry signal |
| 2026-10-27T11:00 | VWAP momentum · 1h | buy | BTC-USD | 6.82 | — | entry signal |
| 2026-10-27T11:00 | MACD cross · 1h | buy | XRP-USD | 4.88 | — | entry signal |
| 2026-10-27T11:00 | MACD cross · 1h | buy | BTC-USD | 4.88 | — | entry signal |
| 2026-10-27T10:50 | Volume breakout | buy | SOL-USD | 13.46 | — | entry signal |
| 2026-10-27T10:50 | Volume breakout | buy | ETH-USD | 13.46 | — | entry signal |
| 2026-10-27T10:50 | ROC + volume | buy | SOL-USD | 13.72 | — | entry signal |
| 2026-10-27T10:46 | Volume breakout | buy | BTC-USD | 13.47 | — | entry signal |
| 2026-10-27T10:35 | Three white soldiers | buy | XRP-USD | 19.56 | — | entry signal |
| 2026-10-27T10:00 | MACD zero-line · 1h | sell | XRP-USD | 20.15 | -0.01 | exit signal |
| 2026-10-27T10:00 | MACD cross · 1h | sell | XRP-USD | 4.52 | -0.01 | exit signal |
| 2026-10-27T10:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 8.30 | -0.06 | exit signal |
| 2026-10-27T08:50 | ROC + volume | sell | XRP-USD | 13.66 | -0.12 | exit signal |
| 2026-10-27T08:35 | Squeeze breakout | sell | XRP-USD | 12.52 | -0.11 | exit signal |
| 2026-10-27T08:35 | ROC + volume | sell | SOL-USD | 13.64 | -0.14 | stop-loss |
| 2026-10-27T08:30 | Volume breakout | sell | ETH-USD | 13.42 | -0.10 | exit signal |
| 2026-10-27T08:15 | Volume breakout | sell | SOL-USD | 13.39 | -0.12 | exit signal |
| 2026-10-27T08:00 | MACD cross · 1h | buy | ETH-USD | 5.18 | — | entry signal |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
