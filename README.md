# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T13:05:05.000184+00:00 · 37888 ticks

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
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 9649 decisions in 1937 calls, $0.1349 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T13:05 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-27T13:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T13:05 | 1 / 4 / 0 | ETH-USD 57% |  |

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
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.15 | 0.15 | 0 | — | 2.80 | 1.29 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.93 | -1.07 | 0 | — | -0.04 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 8.31 | 3.46 | -1.94 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -4.13 | -4.73 | -4.49 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -1.99 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.69 | -3.31 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.19 | -3.81 | 121 | 31.4 | -1.91 | -1.09 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.06 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Hold BTC | benchmark | 95.17 | -4.83 | 0 | — | 1.67 | 0.44 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.05 | -4.95 | 0 | — | -6.95 | -2.93 | -7.83 | 1 |
| 19 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 5.02 | 1.64 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.97 | -3.34 | -17.21 | 577 |
| 22 | Copy: Insider buying | copy | 92.31 | -7.69 | 27 | 37.0 | -20.46 | -4.05 | -22.94 | 61 |
| 23 | Donchian 55/20 · 1h | breakout | 91.67 | -8.33 | 49 | 16.3 | -16.01 | -3.62 | -16.70 | 98 |
| 24 | Daily: Momentum burst | daily | 91.43 | -8.57 | 10 | 10.0 | -19.39 | -3.78 | -20.15 | 40 |
| 25 | Max aggression: 5-day momentum | meta | 91.26 | -8.74 | 11 | 45.5 | -15.58 | -1.42 | -27.80 | 25 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.16 | -16.91 | 1 |
| 27 | Squeeze breakout · 1h | breakout | 90.93 | -9.07 | 52 | 23.1 | -4.54 | -1.18 | -12.00 | 91 |
| 28 | Daily: Bullish score | daily | 90.70 | -9.30 | 11 | 18.2 | -6.77 | -0.82 | -14.40 | 13 |
| 29 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.89 | -6.82 | -12.54 | 214 |
| 30 | Parabolic SAR · 1h | trend | 89.95 | -10.05 | 121 | 25.6 | -22.14 | -5.65 | -22.14 | 251 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.44 | -10.56 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 32 | ADX DI cross · 1h | trend | 88.90 | -11.10 | 114 | 17.5 | -13.55 | -2.96 | -14.38 | 266 |
| 33 | Volume breakout · 1h | breakout | 88.63 | -11.37 | 104 | 23.1 | -13.84 | -2.91 | -16.13 | 108 |
| 34 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.03 | -3.27 | -14.77 | 95 |
| 35 | Stochastic reversion · 1h | reversion | 87.90 | -12.10 | 199 | 46.7 | -21.89 | -4.00 | -23.21 | 392 |
| 36 | Bollinger breakout · 1h | breakout | 87.13 | -12.87 | 109 | 26.6 | -14.90 | -2.99 | -18.11 | 239 |
| 37 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.53 | -4.11 | -17.87 | 704 |
| 38 | Keltner breakout · 1h | breakout | 85.62 | -14.38 | 74 | 23.0 | -20.22 | -3.95 | -23.13 | 181 |
| 39 | Connors RSI(2) · 1h | reversion | 85.11 | -14.89 | 174 | 40.2 | -26.47 | -7.95 | -26.96 | 198 |
| 40 | Z-score reversion · 1h | reversion | 84.87 | -15.13 | 117 | 33.3 | -14.47 | -2.37 | -21.48 | 211 |
| 41 | EMA 20/50 cross · 1h | trend | 84.48 | -15.53 | 73 | 11.0 | -21.72 | -4.28 | -23.33 | 130 |
| 42 | RSI momentum · 1h | momentum | 83.56 | -16.44 | 104 | 15.4 | -22.16 | -4.32 | -23.76 | 202 |
| 43 | MACD cross · 1h | trend | 82.96 | -17.04 | 244 | 22.1 | -29.72 | -6.23 | -30.18 | 479 |
| 44 | Supertrend · 1h | trend | 82.96 | -17.04 | 114 | 14.0 | -27.68 | -5.92 | -28.20 | 224 |
| 45 | MFI reversion · 1h | reversion | 82.76 | -17.24 | 264 | 31.8 | -16.34 | -2.52 | -20.54 | 153 |
| 46 | Ichimoku · 1h | trend | 82.24 | -17.76 | 68 | 11.8 | -21.80 | -4.56 | -24.73 | 109 |
| 47 | Triple EMA stack · 1h | trend | 81.83 | -18.17 | 101 | 14.9 | -29.31 | -5.83 | -30.81 | 203 |
| 48 | Bollinger reversion · 1h | reversion | 81.29 | -18.70 | 179 | 37.4 | -30.00 | -6.18 | -31.17 | 368 |
| 49 | Williams %R · 1h | reversion | 81.22 | -18.78 | 229 | 46.3 | -35.66 | -6.07 | -35.84 | 540 |
| 50 | CCI reversion · 1h | reversion | 81.22 | -18.78 | 223 | 44.8 | -25.68 | -3.69 | -28.06 | 466 |
| 51 | MACD zero-line · 1h | trend | 80.27 | -19.73 | 111 | 15.3 | -24.10 | -5.16 | -24.91 | 217 |
| 52 | Donchian 20/10 · 1h | breakout | 79.86 | -20.14 | 99 | 20.2 | -25.47 | -5.02 | -26.49 | 209 |
| 53 | OBV trend · 1h | momentum | 78.96 | -21.04 | 206 | 17.5 | -34.38 | -7.24 | -34.38 | 292 |
| 54 | Agent (ML meta-label) | meta | 78.86 | -21.14 | 924 | 19.4 | -10.68 | -1.83 | -16.94 | 376 |
| 55 | RSI(14) reversion · 1h | reversion | 78.34 | -21.66 | 102 | 23.5 | -19.70 | -3.14 | -24.48 | 211 |
| 56 | Three white soldiers | momentum | 77.94 | -22.06 | 309 | 19.1 | -44.15 | -20.27 | -44.58 | 604 |
| 57 | ROC + volume · 1h | momentum | 76.58 | -23.42 | 250 | 24.0 | -31.92 | -6.33 | -32.96 | 372 |
| 58 | Heikin-Ashi · 1h | trend | 76.51 | -23.50 | 290 | 22.1 | -45.03 | -10.35 | -45.06 | 657 |
| 59 | Candlestick reversal · 1h | reversion | 76.36 | -23.64 | 272 | 27.9 | -35.76 | -6.58 | -35.86 | 575 |
| 60 | EMA 9/21 cross · 1h | trend | 75.14 | -24.86 | 176 | 10.8 | -33.14 | -7.16 | -33.61 | 332 |
| 61 | VWAP momentum · 1h | momentum | 74.99 | -25.01 | 558 | 21.0 | -49.13 | -10.85 | -50.21 | 1237 |
| 62 | Max aggression: 1-day momentum | meta | 67.16 | -32.84 | 19 | 26.3 | -42.14 | -2.87 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.49 | -45.51 | 766 | 22.1 | -74.18 | -26.15 | -74.33 | 1569 |
| 64 | Volume breakout | breakout | 53.27 | -46.73 | 466 | 12.7 | -62.98 | -26.28 | -63.23 | 806 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -42.74 | -98.88 | 5151 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.03 | -22.67 | -79.64 | 1428 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.69 | -43.67 | -93.74 | 2535 |
| 68 | Squeeze breakout | breakout | 50.46 | -49.54 | 599 | 14.2 | -67.64 | -28.51 | -68.19 | 1180 |
| 69 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.02 | -29.25 | -89.32 | 1929 |
| 70 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -36.29 | -91.47 | 2343 |
| 71 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.34 | -31.54 | -90.37 | 2155 |
| 72 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -50.75 | -97.89 | 3524 |
| 73 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.11 | -53.00 | -96.17 | 3380 |
| 74 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.14 | -36.61 | -94.14 | 2445 |
| 75 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.28 | -32.54 | -82.58 | 1687 |
| 76 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -53.16 | -99.43 | 5786 |
| 77 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -40.38 | -92.82 | 2621 |
| 78 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.86 | -95.40 | 3359 |
| 79 | Donchian 55/20 | breakout | 50.25 | -49.75 | 616 | 19.5 | -72.10 | -23.28 | -72.68 | 1281 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -69.83 | -99.78 | 6166 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -44.84 | -92.29 | 2336 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -59.92 | -97.74 | 3580 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -58.12 | -98.67 | 4807 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -54.35 | -94.58 | 2775 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.42 | -38.76 | -84.42 | 1814 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -65.09 | -99.61 | 6307 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -28.89 | -88.31 | 2231 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.73 | -19.01 | -77.07 | 1701 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.59 | -36.41 | -90.65 | 2284 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.29 | -47.66 | -96.29 | 3830 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -50.01 | -90.05 | 2138 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.13 | -17.92 | -76.40 | 1583 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.57 | -49.04 | -96.57 | 4207 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.75 | -99.92 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T13:05 | Three white soldiers | sell | XRP-USD | 19.43 | -0.10 | exit signal |
| 2026-10-27T13:05 | Three white soldiers | sell | ETH-USD | 19.46 | -0.09 | exit signal |
| 2026-10-27T13:05 | Volume breakout | buy | SOL-USD | 5.32 | — | rebalance up |
| 2026-10-27T13:05 | Volume breakout | sell | XRP-USD | 10.63 | -0.04 | exit signal |
| 2026-10-27T13:05 | Volume breakout | sell | ETH-USD | 10.66 | -0.05 | exit signal |
| 2026-10-27T13:05 | Volume breakout | sell | DOGE-USD | 10.65 | -0.07 | exit signal |
| 2026-10-27T13:05 | Volume breakout | sell | BTC-USD | 13.30 | -0.10 | exit signal |
| 2026-10-27T13:05 | ROC + volume | sell | XRP-USD | 10.87 | -0.06 | stop-loss |
| 2026-10-27T13:05 | ROC + volume | sell | DOGE-USD | 8.15 | -0.09 | stop-loss |
| 2026-10-27T13:00 | MFI reversion · 1h | sell | XRP-USD | 10.52 | 0.19 | exit signal |
| 2026-10-27T13:00 | CCI reversion · 1h | buy | DOGE-USD | 9.03 | — | entry |
| 2026-10-27T13:00 | CCI reversion · 1h | sell | ETH-USD | 10.18 | 0.07 | exit signal |
| 2026-10-27T13:00 | Williams %R · 1h | sell | ETH-USD | 10.24 | 0.07 | exit signal |
| 2026-10-27T13:00 | Stochastic reversion · 1h | sell | ETH-USD | 12.59 | 0.02 | exit signal |
| 2026-10-27T13:00 | Z-score reversion · 1h | buy | SOL-USD | 7.72 | — | entry |
| 2026-10-27T13:00 | Z-score reversion · 1h | sell | ETH-USD | 8.07 | -0.04 | exit signal |
| 2026-10-27T13:00 | RSI(14) reversion · 1h | sell | ETH-USD | 8.22 | -0.10 | exit signal |
| 2026-10-27T13:00 | RSI(14) reversion · 1h | sell | BTC-USD | 8.50 | -0.00 | exit signal |
| 2026-10-27T13:00 | Bollinger breakout · 1h | buy | ETH-USD | 7.03 | — | entry signal |
| 2026-10-27T13:00 | Bollinger breakout · 1h | buy | BTC-USD | 14.54 | — | entry signal |
| 2026-10-27T13:00 | VWAP momentum · 1h | buy | ETH-USD | 1.42 | — | entry signal |
| 2026-10-27T13:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.36 | — | entry signal |
| 2026-10-27T13:00 | MACD cross · 1h | buy | SOL-USD | 4.61 | — | entry signal |
| 2026-10-27T13:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 3.03 | — | entry signal |
| 2026-10-27T13:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 6.84 | — | entry signal |
| 2026-10-27T13:00 | Donchian 55/20 | buy | SOL-USD | 2.51 | — | rebalance up |
| 2026-10-27T13:00 | Donchian 55/20 | sell | ETH-USD | 2.51 | -0.01 | rebalance down |
| 2026-10-27T12:57 | ROC + volume | buy | DOGE-USD | 5.47 | — | rebalance up |
| 2026-10-27T12:57 | ROC + volume | sell | SOL-USD | 2.73 | -0.01 | rebalance down |
| 2026-10-27T12:57 | ROC + volume | sell | ETH-USD | 2.73 | -0.01 | rebalance down |
| 2026-10-27T12:55 | Volume breakout | buy | SOL-USD | 2.67 | — | rebalance up |
| 2026-10-27T12:55 | Volume breakout | sell | DOGE-USD | 2.67 | -0.01 | rebalance down |
| 2026-10-27T12:55 | ROC + volume | buy | DOGE-USD | 2.77 | — | entry signal |
| 2026-10-27T12:55 | ROC + volume | sell | XRP-USD | 2.77 | -0.00 | rebalance down |
| 2026-10-27T12:50 | Volume breakout | buy | SOL-USD | 5.41 | — | entry signal |
| 2026-10-27T12:50 | Volume breakout | sell | XRP-USD | 2.73 | 0.01 | rebalance down |
| 2026-10-27T12:50 | Volume breakout | sell | ETH-USD | 2.68 | -0.00 | rebalance down |
| 2026-10-27T12:50 | ROC + volume | buy | BTC-USD | 13.70 | — | entry signal |
| 2026-10-27T12:45 | Volume breakout | buy | BTC-USD | 13.40 | — | entry signal |
| 2026-10-27T12:40 | Three white soldiers | buy | SOL-USD | 19.54 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 13:05:05.000184+00:00 -> 2026-10-27 13:15:05.000184+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
