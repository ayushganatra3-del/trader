# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-21T01:50:05.000134+00:00 · 67543 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.18 (-19.82%)

Closed trades 238, win rate 36.1%, fees £6.46, max drawdown -20.19%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-21 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 1470 decisions in 294 calls, $0.0206 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-21T01:50 | 2 / 3 / 0 | DOGE-USD 18% |  |
| Breezy | 2026-11-21T01:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-21T01:50 | 3 / 2 / 0 | ETH-USD 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.76 | +27.55% | 6 |
| Opening range 30m | SQQQ | 1.44 | +19.43% | 6 |
| Opening range 15m | SQQQ | 1.43 | +19.52% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.46 | 14.46 | 0 | — | 12.16 | 4.07 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.74 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.85 | -4.19 | -5.43 | 75 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.66 | 0.31 | -7.76 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.58 | -4.68 | -11.35 | 46 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.21 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -2.72 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -8.22 | -1.59 | -14.79 | 66 |
| 19 | VWAP reversion · 1h | reversion | 87.80 | -12.21 | 159 | 45.3 | -14.45 | -4.20 | -20.28 | 155 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.47 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.84 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.78 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -23.69 | -6.37 | -28.86 | 195 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.98 | -6.67 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.08 | -5.99 | -21.55 | 74 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -20.50 | -5.35 | -25.26 | 146 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.63 | -5.04 | -22.26 | 204 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.78 | -15.07 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -25.05 | -4.20 | -25.48 | 96 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 228 | 20.2 | -30.72 | -5.72 | -35.87 | 269 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.95 | -3.41 | -58.27 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.97 | -27.03 | 195 | 21.5 | -31.07 | -7.62 | -36.25 | 217 |
| 37 | Supertrend · 1h | trend | 72.93 | -27.07 | 198 | 16.7 | -33.54 | -6.53 | -37.64 | 199 |
| 38 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -31.58 | -7.38 | -37.24 | 170 |
| 39 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.75 | -9.72 | -40.64 | 122 |
| 40 | Heikin-Ashi · 1h | trend | 70.86 | -29.14 | 484 | 22.9 | -44.15 | -8.97 | -47.85 | 620 |
| 41 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 184 | 14.1 | -36.97 | -8.00 | -41.28 | 202 |
| 42 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 43 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -36.60 | -9.31 | -41.22 | 239 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | Hold BTC | benchmark | 68.28 | -31.72 | 3 | 0.0 | -26.99 | -4.46 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 165 | 17.6 | -35.35 | -6.72 | -43.26 | 193 |
| 49 | Stochastic reversion · 1h | reversion | 66.91 | -33.09 | 378 | 39.9 | -43.21 | -6.14 | -43.86 | 445 |
| 50 | ROC + volume · 1h | momentum | 66.42 | -33.58 | 431 | 27.6 | -37.34 | -6.52 | -43.62 | 343 |
| 51 | MFI reversion · 1h | reversion | 64.80 | -35.20 | 476 | 33.0 | -34.48 | -5.19 | -35.95 | 173 |
| 52 | EMA 9/21 cross · 1h | trend | 64.80 | -35.20 | 291 | 11.3 | -42.42 | -9.85 | -46.01 | 318 |
| 53 | MACD cross · 1h | trend | 63.03 | -36.97 | 444 | 20.9 | -49.70 | -9.92 | -51.09 | 496 |
| 54 | CCI reversion · 1h | reversion | 62.17 | -37.83 | 413 | 40.4 | -46.91 | -7.65 | -48.16 | 484 |
| 55 | Bollinger reversion · 1h | reversion | 58.21 | -41.79 | 377 | 36.6 | -44.26 | -6.66 | -45.16 | 444 |
| 56 | Williams %R · 1h | reversion | 57.50 | -42.50 | 470 | 38.5 | -52.79 | -8.67 | -53.06 | 582 |
| 57 | RSI(14) reversion · 1h | reversion | 55.32 | -44.68 | 225 | 32.9 | -42.64 | -6.17 | -46.29 | 276 |
| 58 | Agent (ML meta-label) | meta | 55.27 | -44.73 | 2005 | 24.6 | -30.49 | -5.59 | -32.32 | 313 |
| 59 | VWAP momentum · 1h | momentum | 55.14 | -44.86 | 1013 | 21.4 | -56.28 | -11.55 | -60.99 | 1199 |
| 60 | Z-score reversion · 1h | reversion | 51.99 | -48.01 | 242 | 33.1 | -43.89 | -6.05 | -46.40 | 270 |
| 61 | Three white soldiers | momentum | 51.39 | -48.61 | 621 | 14.0 | -52.63 | -22.31 | -52.96 | 670 |
| 62 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.70 | -9.56 | -53.95 | 680 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -47.24 | -99.16 | 5359 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.55 | -29.67 | -84.15 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.47 | -45.60 | -94.51 | 2458 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.16 | -33.25 | -91.39 | 1954 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.04 | -42.43 | -92.21 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.93 | -27.62 | -90.25 | 2025 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.25 | -47.08 | -98.25 | 3493 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.86 | -52.21 | -96.88 | 3404 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.90 | -39.57 | -94.00 | 2199 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.75 | -34.67 | -83.75 | 1589 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -51.90 | -99.66 | 6347 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.17 | -42.45 | -93.17 | 2538 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.56 | -36.59 | -94.60 | 3156 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -65.11 | -99.84 | 6288 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.56 | -43.50 | -93.57 | 2291 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.61 | -24.69 | -79.79 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.87 | -58.16 | -97.87 | 3390 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -55.08 | -99.14 | 5119 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.06 | -28.84 | -71.12 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.07 | -51.25 | -95.08 | 2734 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.71 | -37.95 | -85.93 | 1708 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -65.10 | -99.73 | 6558 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.50 | -30.73 | -91.60 | 2480 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.71 | -18.97 | -81.92 | 1943 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.71 | -31.93 | -92.72 | 2207 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.87 | -44.63 | -97.87 | 4046 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.40 | -49.68 | -90.48 | 2205 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.33 | -31.13 | -67.49 | 793 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.85 | -27.34 | -74.90 | 1205 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.17 | -18.90 | -83.48 | 1849 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.71 | -44.48 | -97.72 | 4441 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -93.51 | -99.94 | 8433 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-21T01:35 | Candlestick reversal · 1h | sell | XRP-USD | 12.68 | -0.14 | Kill switch: down 50% from peak |
| 2026-11-21T01:35 | Candlestick reversal · 1h | sell | ETH-USD | 12.72 | -0.10 | Kill switch: down 50% from peak |
| 2026-11-21T01:35 | Candlestick reversal · 1h | sell | DOGE-USD | 12.74 | -0.09 | Kill switch: down 50% from peak |
| 2026-11-21T01:20 | MFI reversion · 1h | buy | SOL-USD | 3.25 | — | rebalance up |
| 2026-11-21T01:15 | MFI reversion · 1h | buy | XRP-USD | 3.28 | — | rebalance up |
| 2026-11-21T01:15 | MFI reversion · 1h | buy | DOGE-USD | 3.25 | — | rebalance up |
| 2026-11-21T01:00 | VWAP reversion · 1h | buy | XRP-USD | 7.12 | — | rebalance up |
| 2026-11-21T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 14.87 | 0.03 | exit signal |
| 2026-11-21T01:00 | VWAP reversion · 1h | sell | BTC-USD | 14.63 | 0.03 | exit signal |
| 2026-11-21T01:00 | Z-score reversion · 1h | buy | ETH-USD | 8.67 | — | entry signal |
| 2026-11-21T01:00 | VWAP momentum · 1h | buy | SOL-USD | 13.66 | — | entry signal |
| 2026-11-21T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 13.81 | — | entry signal |
| 2026-11-21T01:00 | VWAP momentum · 1h | buy | BTC-USD | 13.81 | — | entry signal |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | buy | XRP-USD | 7.03 | — | rebalance up |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | buy | ETH-USD | 3.56 | — | rebalance up |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.55 | — | rebalance up |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | sell | SOL-USD | 14.14 | -0.06 | exit signal |
| 2026-11-21T00:00 | Hold BTC | buy | BTC-USD | 68.38 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | XRP-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | SOL-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | DOGE-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | BTC-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | XRP-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | SOL-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | ETH-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | DOGE-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | BTC-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | Williams %R · 1h | buy | XRP-USD | 11.53 | — | entry |
| 2026-11-21T00:00 | Williams %R · 1h | buy | SOL-USD | 11.53 | — | entry |
| 2026-11-21T00:00 | Williams %R · 1h | buy | ETH-USD | 11.53 | — | entry |
| 2026-11-21T00:00 | Williams %R · 1h | buy | DOGE-USD | 11.53 | — | entry |
| 2026-11-21T00:00 | Williams %R · 1h | buy | BTC-USD | 11.53 | — | entry |
| 2026-11-21T00:00 | Stochastic reversion · 1h | buy | ETH-USD | 4.18 | — | entry |
| 2026-11-21T00:00 | Stochastic reversion · 1h | buy | DOGE-USD | 4.18 | — | entry |
| 2026-11-21T00:00 | Stochastic reversion · 1h | buy | BTC-USD | 4.18 | — | entry |
| 2026-11-21T00:00 | Z-score reversion · 1h | buy | XRP-USD | 10.42 | — | entry |
| 2026-11-21T00:00 | Z-score reversion · 1h | buy | SOL-USD | 10.42 | — | entry |
| 2026-11-21T00:00 | Z-score reversion · 1h | buy | DOGE-USD | 10.42 | — | entry |
| 2026-11-21T00:00 | Z-score reversion · 1h | buy | BTC-USD | 10.42 | — | entry |
| 2026-11-21T00:00 | Bollinger reversion · 1h | buy | XRP-USD | 2.43 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-23 01:50:05.000134+00:00 -> 2026-11-21 02:00:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
