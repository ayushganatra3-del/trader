# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T04:40:05.000135+00:00 · 62745 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.11 (-13.89%)

Closed trades 203, win rate 36.5%, fees £5.77, max drawdown -15.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 3720 decisions in 744 calls, $0.0520 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T04:40 | 1 / 3 / 1 | SOL-USD 17% |  |
| Breezy | 2026-11-17T04:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T04:40 | 2 / 3 / 0 | ETH-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.55% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.98 | 17.98 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.66 | 3.65 | 0 | — | 5.47 | 1.51 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.58 | -3.42 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.62 | -8.15 | 157 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.78 | -6.22 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.62 | -8.38 | 47 | 42.6 | -10.04 | -2.01 | -14.95 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.52 | -8.48 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -10.76 | -3.99 | -16.01 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.63 | -13.37 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.11 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Parabolic SAR · 1h | trend | 83.35 | -16.66 | 180 | 28.3 | -22.78 | -6.14 | -24.65 | 213 |
| 27 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 28 | Keltner breakout · 1h | breakout | 80.57 | -19.43 | 121 | 25.6 | -18.83 | -4.16 | -25.84 | 158 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -24.61 | -6.13 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.28 | -19.72 | 213 | 39.9 | -14.54 | -6.43 | -14.88 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.94 | -5.37 | -22.48 | 86 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.06 | -21.93 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.27 | -22.73 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.97 | -24.03 | 2 | 0.0 | -14.66 | -2.04 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.03 | -8.26 | -31.55 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.88 | -25.12 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.73 | -25.27 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.19 | -25.82 | 185 | 22.2 | -24.78 | -5.31 | -31.78 | 237 |
| 40 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 41 | MFI reversion · 1h | reversion | 72.15 | -27.85 | 419 | 34.1 | -25.23 | -3.56 | -29.02 | 163 |
| 42 | MACD zero-line · 1h | trend | 72.02 | -27.98 | 176 | 18.2 | -25.41 | -5.01 | -31.93 | 197 |
| 43 | Supertrend · 1h | trend | 71.87 | -28.13 | 187 | 16.0 | -31.99 | -5.40 | -39.67 | 200 |
| 44 | Heikin-Ashi · 1h | trend | 71.78 | -28.22 | 459 | 23.3 | -39.07 | -7.45 | -43.26 | 637 |
| 45 | RSI momentum · 1h | momentum | 71.22 | -28.78 | 175 | 14.3 | -31.03 | -5.60 | -38.07 | 203 |
| 46 | Triple EMA stack · 1h | trend | 71.21 | -28.79 | 154 | 14.9 | -28.80 | -5.29 | -37.77 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.91 | -29.09 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | MACD cross · 1h | trend | 70.88 | -29.12 | 405 | 22.5 | -33.39 | -4.78 | -43.23 | 475 |
| 49 | ROC + volume · 1h | momentum | 70.57 | -29.43 | 405 | 28.4 | -28.49 | -4.69 | -37.95 | 356 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.19 | -30.81 | 303 | 19.1 | -30.68 | -5.75 | -39.29 | 259 |
| 52 | CCI reversion · 1h | reversion | 68.05 | -31.95 | 378 | 42.1 | -40.07 | -6.48 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.80 | -32.20 | 157 | 18.5 | -30.08 | -4.92 | -39.25 | 206 |
| 54 | Bollinger reversion · 1h | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.48 | -36.96 | 405 |
| 55 | Williams %R · 1h | reversion | 64.26 | -35.74 | 419 | 41.3 | -44.33 | -7.42 | -45.12 | 544 |
| 56 | EMA 9/21 cross · 1h | trend | 64.11 | -35.89 | 275 | 11.3 | -38.66 | -7.58 | -44.88 | 320 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -21.27 | -2.95 | -26.12 | 334 |
| 58 | Z-score reversion · 1h | reversion | 59.57 | -40.43 | 221 | 35.7 | -34.78 | -4.76 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.28 | -40.72 | 204 | 31.9 | -40.69 | -5.98 | -42.13 | 240 |
| 60 | VWAP momentum · 1h | momentum | 58.52 | -41.48 | 944 | 21.7 | -53.05 | -9.25 | -57.70 | 1212 |
| 61 | Candlestick reversal · 1h | reversion | 57.27 | -42.73 | 537 | 27.0 | -45.60 | -8.23 | -45.68 | 615 |
| 62 | Three white soldiers | momentum | 56.30 | -43.70 | 572 | 14.7 | -49.27 | -21.88 | -49.27 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -42.80 | -99.00 | 5292 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.33 | -25.39 | -81.42 | 1434 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.94 | -42.58 | -93.96 | 2509 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.89 | -30.69 | -89.98 | 1934 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -39.66 | -91.40 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.08 | -29.99 | -90.10 | 2154 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -46.29 | -97.91 | 3462 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -51.96 | -96.47 | 3441 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.58 | -37.28 | -93.59 | 2266 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -32.96 | -82.77 | 1636 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.77 | -99.59 | 6050 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.12 | -41.49 | -92.14 | 2585 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.24 | -35.83 | -95.24 | 3359 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.49 | -99.81 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.38 | -42.94 | -92.39 | 2264 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.56 | -26.03 | -76.58 | 1652 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -57.77 | -97.60 | 3468 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -53.14 | -98.99 | 4941 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.78 | -27.40 | -68.84 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -54.93 | -94.75 | 2759 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.66 | -37.36 | -84.68 | 1746 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -63.86 | -99.69 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.45 | -29.73 | -90.45 | 2332 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.73 | -18.59 | -79.76 | 1819 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.96 | -34.99 | -90.99 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.44 | -43.76 | -97.44 | 3901 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.24 | -57.87 | -89.24 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.52 | -29.82 | -66.52 | 829 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.03 | -23.10 | -72.09 | 1249 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.45 | -17.57 | -80.72 | 1759 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -44.70 | -97.57 | 4353 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.30 | -99.94 | 8392 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T04:00 | CCI reversion · 1h | sell | XRP-USD | 17.19 | 0.16 | exit signal |
| 2026-11-17T04:00 | Williams %R · 1h | sell | SOL-USD | 7.36 | 0.15 | exit signal |
| 2026-11-17T04:00 | Candlestick reversal · 1h | buy | BTC-USD | 7.16 | — | entry signal |
| 2026-11-17T04:00 | Bollinger breakout · 1h | buy | XRP-USD | 18.59 | — | entry signal |
| 2026-11-17T04:00 | Bollinger breakout · 1h | buy | SOL-USD | 18.59 | — | entry signal |
| 2026-11-17T04:00 | RSI momentum · 1h | buy | SOL-USD | 17.81 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | XRP-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | ETH-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | BTC-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | sell | SOL-USD | 7.52 | 0.09 | rebalance down |
| 2026-11-17T04:00 | Parabolic SAR · 1h | buy | SOL-USD | 20.85 | — | entry signal |
| 2026-11-17T04:00 | MACD zero-line · 1h | buy | XRP-USD | 18.03 | — | entry signal |
| 2026-11-17T04:00 | MACD cross · 1h | buy | ETH-USD | 14.21 | — | entry signal |
| 2026-11-17T04:00 | MACD cross · 1h | buy | BTC-USD | 14.21 | — | entry signal |
| 2026-11-17T04:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 7.55 | — | entry signal |
| 2026-11-17T04:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 10.72 | — | entry signal |
| 2026-11-17T04:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 10.72 | — | entry signal |
| 2026-11-17T04:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 5.49 | 0.04 | rebalance down |
| 2026-11-17T04:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.41 | 0.01 | rebalance down |
| 2026-11-17T03:00 | ROC + volume · 1h | sell | DOGE-USD | 17.26 | -0.35 | exit signal |
| 2026-11-17T03:00 | MACD zero-line · 1h | buy | SOL-USD | 18.01 | — | entry signal |
| 2026-11-17T03:00 | MACD zero-line · 1h | sell | ETH-USD | 17.97 | -0.16 | exit signal |
| 2026-11-17T03:00 | MACD zero-line · 1h | sell | BTC-USD | 17.84 | -0.33 | exit signal |
| 2026-11-17T03:00 | MACD cross · 1h | sell | ETH-USD | 14.10 | -0.19 | exit signal |
| 2026-11-17T03:00 | MACD cross · 1h | sell | BTC-USD | 14.08 | -0.14 | exit signal |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 5.31 | — | rebalance up |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.34 | — | rebalance up |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 10.61 | -0.21 | exit signal |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 10.59 | -0.15 | exit signal |
| 2026-11-17T02:15 | Three white soldiers | sell | XRP-USD | 14.01 | -0.14 | stop-loss |
| 2026-11-17T01:50 | Three white soldiers | sell | ETH-USD | 14.01 | -0.14 | stop-loss |
| 2026-11-17T01:45 | Three white soldiers | buy | XRP-USD | 14.14 | — | entry signal |
| 2026-11-17T01:45 | Three white soldiers | buy | ETH-USD | 14.14 | — | entry signal |
| 2026-11-17T01:00 | Bollinger breakout · 1h | sell | ETH-USD | 18.24 | -0.41 | exit signal |
| 2026-11-17T01:00 | VWAP momentum · 1h | buy | SOL-USD | 4.88 | — | rebalance up |
| 2026-11-17T01:00 | VWAP momentum · 1h | sell | ETH-USD | 9.69 | -0.09 | exit signal |
| 2026-11-17T01:00 | VWAP momentum · 1h | sell | BTC-USD | 9.68 | -0.09 | exit signal |
| 2026-11-17T01:00 | MACD zero-line · 1h | sell | DOGE-USD | 17.82 | -0.31 | exit signal |
| 2026-11-17T01:00 | MACD cross · 1h | buy | XRP-USD | 4.13 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 04:40:05.000135+00:00 -> 2026-11-17 04:50:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 04:40:05.000135+00:00 -> 2026-11-17 04:50:05.000135+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
