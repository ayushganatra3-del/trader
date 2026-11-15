# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-15T16:40:05.000133+00:00 · 60846 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-14 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 12900 decisions in 2580 calls, $0.1802 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-15T16:40 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-15T16:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-15T16:40 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 3.27 | +5.62% | 11 |
| Bollinger reversion | TSLA | 2.67 | +2.69% | 7 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| Z-score reversion | TQQQ | 2.20 | +4.97% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.89 | 17.89 | 0 | — | 15.31 | 5.07 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.92 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.99 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.58 | 1.81 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 1.00 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 3.07 | 1.95 | -3.47 | 82 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.59 | 1.86 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.47 | 0.22 | -18.69 | 7 |
| 11 | Hold SPY | benchmark | 98.33 | -1.67 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.12 | 1 | 0.0 | -3.27 | -2.15 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.69 | -3.31 | 191 | 30.4 | -3.17 | -1.11 | -8.46 | 150 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.35 | -3.65 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.35 | -1.22 | -15.78 | 58 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.41 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.27 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.07 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -14.50 | -6.22 | -14.97 | 67 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -17.19 | -4.23 | -19.44 | 159 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.28 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.64 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.98 | -19.56 | 19 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.17 | -7.11 | -15.01 | 193 |
| 26 | Parabolic SAR · 1h | trend | 85.27 | -14.73 | 176 | 29.0 | -15.04 | -3.23 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -14.83 | -4.11 | -16.59 | 92 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.82 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.39 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -17.94 | -6.30 | -18.02 | 111 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.45 | -3.07 | -22.20 | 89 |
| 32 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.02 | -3.43 | -25.39 | 165 |
| 33 | Stochastic reversion · 1h | reversion | 78.85 | -21.14 | 314 | 46.5 | -26.70 | -3.98 | -28.40 | 411 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.92 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 76.97 | -23.03 | 407 | 35.1 | -22.29 | -2.89 | -26.60 | 174 |
| 36 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.59 | -50.62 | 22 |
| 37 | ADX DI cross · 1h | trend | 75.48 | -24.52 | 203 | 19.7 | -24.13 | -3.60 | -33.58 | 268 |
| 38 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -26.69 | -6.13 | -31.58 | 117 |
| 39 | Hold BTC | benchmark | 75.28 | -24.72 | 2 | 0.0 | -18.51 | -2.53 | -28.91 | 1 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.62 | -4.70 | -30.71 | 234 |
| 41 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -21.85 | -0.73 | -57.50 | 40 |
| 42 | Heikin-Ashi · 1h | trend | 74.30 | -25.70 | 450 | 23.8 | -37.66 | -6.94 | -40.36 | 666 |
| 43 | MACD zero-line · 1h | trend | 73.48 | -26.52 | 171 | 18.7 | -23.32 | -4.57 | -30.99 | 199 |
| 44 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.59 | -4.07 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.18 | -4.79 | -40.51 | 120 |
| 46 | MACD cross · 1h | trend | 71.68 | -28.32 | 393 | 23.2 | -31.95 | -4.76 | -41.23 | 478 |
| 47 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.47 | -4.56 | -38.65 | 201 |
| 48 | Supertrend · 1h | trend | 71.53 | -28.47 | 182 | 14.8 | -29.84 | -5.08 | -37.32 | 210 |
| 49 | ROC + volume · 1h | momentum | 71.18 | -28.82 | 399 | 28.8 | -29.68 | -5.31 | -37.90 | 361 |
| 50 | Bollinger reversion · 1h | reversion | 70.85 | -29.15 | 313 | 40.9 | -35.34 | -5.60 | -36.70 | 397 |
| 51 | CCI reversion · 1h | reversion | 69.97 | -30.03 | 357 | 42.3 | -37.59 | -6.02 | -39.14 | 475 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -28.50 | -4.99 | -38.36 | 271 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.10 | -4.64 | -37.81 | 35 |
| 54 | Donchian 20/10 · 1h | breakout | 69.23 | -30.77 | 153 | 19.0 | -29.93 | -5.35 | -37.58 | 204 |
| 55 | Williams %R · 1h | reversion | 66.08 | -33.92 | 403 | 42.2 | -44.25 | -7.42 | -45.15 | 551 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -20.41 | -3.39 | -24.22 | 337 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -37.16 | -7.48 | -43.16 | 324 |
| 58 | VWAP momentum · 1h | momentum | 62.50 | -37.50 | 917 | 22.2 | -52.45 | -10.41 | -53.34 | 1238 |
| 59 | RSI(14) reversion · 1h | reversion | 61.29 | -38.71 | 197 | 31.5 | -38.63 | -5.72 | -40.40 | 245 |
| 60 | Candlestick reversal · 1h | reversion | 60.85 | -39.15 | 507 | 27.4 | -44.47 | -8.47 | -44.62 | 614 |
| 61 | Z-score reversion · 1h | reversion | 60.22 | -39.78 | 215 | 35.3 | -34.19 | -4.76 | -35.69 | 238 |
| 62 | Three white soldiers | momentum | 58.45 | -41.55 | 551 | 15.1 | -48.86 | -21.10 | -49.26 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -43.20 | -99.01 | 5316 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.86 | -26.70 | -80.87 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -44.50 | -93.67 | 2525 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.83 | -32.26 | -89.99 | 1932 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.23 | -40.61 | -91.32 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.43 | -30.24 | -89.46 | 2164 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -49.92 | -97.88 | 3487 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -56.00 | -96.29 | 3453 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -32.57 | -93.48 | 2312 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.79 | -33.62 | -82.80 | 1648 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -53.97 | -99.61 | 6077 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.96 | -41.49 | -92.09 | 2622 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.07 | -35.79 | -95.09 | 3437 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -69.49 | -99.81 | 6168 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.28 | -42.24 | -92.40 | 2285 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.85 | -25.25 | -76.56 | 1668 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -58.07 | -97.52 | 3484 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -56.82 | -99.02 | 4971 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.79 | -27.29 | -68.95 | 1240 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -54.79 | -94.65 | 2798 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.64 | -36.39 | -84.95 | 1776 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -69.17 | -99.70 | 6401 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.11 | -30.30 | -91.11 | 2360 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.54 | -18.82 | -81.20 | 1835 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.24 | -36.14 | -91.26 | 2200 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -45.84 | -97.46 | 3925 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -57.11 | -89.33 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.13 | -29.68 | -66.25 | 827 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.34 | -22.89 | -71.37 | 1252 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.57 | -17.82 | -82.11 | 1768 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.66 | -46.48 | -97.68 | 4376 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -96.91 | -99.93 | 8445 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-15T15:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.77 | -0.05 | exit signal |
| 2026-11-15T15:00 | Heikin-Ashi · 1h | sell | BTC-USD | 6.09 | -0.11 | exit signal |
| 2026-11-15T15:00 | ADX DI cross · 1h | sell | XRP-USD | 18.69 | -0.35 | exit signal |
| 2026-11-15T15:00 | ADX DI cross · 1h | sell | BTC-USD | 18.72 | -0.31 | exit signal |
| 2026-11-15T14:00 | ADX DI cross · 1h | buy | BTC-USD | 19.03 | — | entry signal |
| 2026-11-15T13:00 | MFI reversion · 1h | buy | BTC-USD | 8.86 | — | entry |
| 2026-11-15T13:00 | MFI reversion · 1h | sell | XRP-USD | 8.86 | 0.37 | exit signal |
| 2026-11-15T13:00 | CCI reversion · 1h | sell | SOL-USD | 3.39 | 0.05 | exit signal |
| 2026-11-15T13:00 | ADX DI cross · 1h | buy | XRP-USD | 19.04 | — | entry signal |
| 2026-11-15T11:10 | Three white soldiers | sell | DOGE-USD | 14.53 | -0.11 | exit signal |
| 2026-11-15T11:00 | Williams %R · 1h | sell | DOGE-USD | 3.38 | 0.08 | exit signal |
| 2026-11-15T11:00 | Stochastic reversion · 1h | sell | DOGE-USD | 5.08 | 0.17 | exit signal |
| 2026-11-15T11:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.82 | — | entry signal |
| 2026-11-15T11:00 | Heikin-Ashi · 1h | buy | BTC-USD | 6.21 | — | entry signal |
| 2026-11-15T11:00 | Supertrend · 1h | buy | ETH-USD | 1.99 | — | entry signal |
| 2026-11-15T11:00 | Supertrend · 1h | buy | BTC-USD | 7.99 | — | entry signal |
| 2026-11-15T10:15 | Three white soldiers | buy | DOGE-USD | 14.64 | — | entry signal |
| 2026-11-15T10:00 | Williams %R · 1h | sell | SOL-USD | 3.30 | -0.00 | exit signal |
| 2026-11-15T10:00 | Williams %R · 1h | sell | ETH-USD | 3.38 | 0.08 | exit signal |
| 2026-11-15T10:00 | Stochastic reversion · 1h | sell | SOL-USD | 2.91 | 0.06 | exit signal |
| 2026-11-15T10:00 | Bollinger reversion · 1h | sell | DOGE-USD | 8.86 | 0.05 | exit signal |
| 2026-11-15T09:50 | Three white soldiers | sell | SOL-USD | 14.53 | -0.15 | exit signal |
| 2026-11-15T09:10 | Three white soldiers | buy | SOL-USD | 14.68 | — | entry signal |
| 2026-11-15T09:00 | Williams %R · 1h | sell | BTC-USD | 3.30 | -0.00 | exit signal |
| 2026-11-15T09:00 | Bollinger reversion · 1h | buy | DOGE-USD | 5.63 | — | rebalance up |
| 2026-11-15T09:00 | Bollinger reversion · 1h | sell | ETH-USD | 5.96 | 0.24 | exit signal |
| 2026-11-15T09:00 | Candlestick reversal · 1h | buy | SOL-USD | 2.81 | — | entry signal |
| 2026-11-15T09:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.81 | — | entry signal |
| 2026-11-15T07:00 | Candlestick reversal · 1h | buy | BTC-USD | 4.35 | — | entry signal |
| 2026-11-15T07:00 | Heikin-Ashi · 1h | sell | ETH-USD | 2.89 | -0.03 | exit signal |
| 2026-11-15T07:00 | Heikin-Ashi · 1h | sell | BTC-USD | 6.14 | -0.08 | exit signal |
| 2026-11-15T06:00 | Candlestick reversal · 1h | sell | BTC-USD | 3.35 | -0.04 | exit signal |
| 2026-11-15T06:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.92 | — | entry |
| 2026-11-15T06:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.92 | -0.04 | exit signal |
| 2026-11-15T06:00 | ADX DI cross · 1h | sell | XRP-USD | 18.75 | -0.39 | exit signal |
| 2026-11-15T05:00 | Williams %R · 1h | sell | XRP-USD | 3.49 | 0.19 | exit signal |
| 2026-11-15T05:00 | Candlestick reversal · 1h | sell | ETH-USD | 3.54 | -0.05 | exit signal |
| 2026-11-15T05:00 | Candlestick reversal · 1h | sell | DOGE-USD | 3.36 | -0.03 | exit signal |
| 2026-11-15T05:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.96 | — | entry signal |
| 2026-11-15T05:00 | Heikin-Ashi · 1h | buy | BTC-USD | 6.22 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-17 16:40:05.000133+00:00 -> 2026-11-15 16:50:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
