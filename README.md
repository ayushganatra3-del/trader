# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T17:05:05.000122+00:00 · 75727 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £75.67 (-24.33%)

Closed trades 251, win rate 35.9%, fees £6.91, max drawdown -24.82%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.10 | -0.19 |
| SQQQ | 15.06 | -0.10 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-27 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 22197 decisions in 2691 calls, $0.2853 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T17:05 | 2 / 16 / 12 | cash |  |
| Breezy | 2026-11-27T17:05 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-27T17:05 | 5 / 24 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.45 | +1.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.21 | 3.56 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.48 | 16.48 | 0 | — | 14.97 | 4.98 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.81 | 5.81 | 0 | — | 4.59 | 1.26 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 98.92 | -1.08 | 44 | 27.3 | -3.51 | -0.33 | -16.65 | 44 |
| 8 | Gap and go | momentum | 98.32 | -1.68 | 223 | 30.9 | 0.14 | 0.13 | -7.66 | 213 |
| 9 | Hold SPY | benchmark | 95.40 | -4.60 | 0 | — | -5.31 | -1.30 | -11.71 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 11 | Three white soldiers · 1h | momentum | 95.18 | -4.82 | 24 | 12.5 | -2.94 | -2.64 | -6.24 | 25 |
| 12 | Agent (rotation) | meta | 95.11 | -4.89 | 234 | 28.2 | 1.35 | 0.50 | -6.10 | 184 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 95.08 | -4.92 | 0 | — | -4.70 | -0.85 | -13.24 | 1 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 94.95 | -5.05 | 172 | 32.6 | -4.82 | -4.12 | -5.85 | 54 |
| 15 | Copy: Insider buying | copy | 94.64 | -5.36 | 63 | 41.3 | -2.02 | -0.23 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 90.76 | -9.24 | 117 | 23.9 | -7.56 | -4.68 | -9.90 | 28 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.49 | -9.51 | 0 | — | -10.37 | -2.16 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 87.14 | -12.86 | 490 | 33.9 | -9.04 | -2.72 | -15.30 | 553 |
| 21 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 22 | Daily: Bullish score | daily | 84.64 | -15.36 | 20 | 20.0 | -14.37 | -3.19 | -19.56 | 14 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.42 | -6.03 | -17.45 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 78.99 | -21.01 | 226 | 40.7 | -14.08 | -6.49 | -14.49 | 63 |
| 26 | Opening range 15m | breakout | 78.98 | -21.02 | 618 | 31.9 | -18.40 | -5.06 | -24.20 | 679 |
| 27 | Volume breakout · 1h | breakout | 76.74 | -23.26 | 181 | 30.4 | -21.59 | -8.50 | -21.70 | 70 |
| 28 | Parabolic SAR · 1h | trend | 76.28 | -23.72 | 221 | 27.1 | -31.55 | -7.80 | -33.65 | 184 |
| 29 | Max aggression: 5-day momentum | meta | 76.02 | -23.98 | 27 | 37.0 | -51.35 | -2.48 | -67.33 | 21 |
| 30 | Agent | meta | 75.67 | -24.33 | 251 | 35.9 | -26.94 | -5.99 | -27.40 | 209 |
| 31 | Agent (aggressive) | meta | 75.36 | -24.64 | 115 | 33.0 | -15.34 | -4.22 | -16.35 | 92 |
| 32 | Donchian 55/20 · 1h | breakout | 73.29 | -26.71 | 91 | 13.2 | -30.78 | -8.07 | -31.22 | 81 |
| 33 | Ichimoku · 1h | trend | 72.80 | -27.20 | 119 | 15.1 | -29.46 | -7.41 | -30.49 | 100 |
| 34 | Keltner breakout · 1h | breakout | 72.71 | -27.29 | 147 | 23.8 | -26.82 | -6.57 | -27.80 | 152 |
| 35 | Daily: Momentum burst | daily | 71.57 | -28.43 | 31 | 16.1 | -31.71 | -4.25 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 70.98 | -29.02 | 274 | 19.7 | -37.79 | -7.04 | -39.78 | 280 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 69.87 | -30.13 | 3 | 0.0 | -22.35 | -2.63 | -33.66 | 1 |
| 38 | Hold BTC | benchmark | 69.29 | -30.71 | 3 | 0.0 | -29.00 | -5.08 | -36.10 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 68.57 | -31.43 | 418 | 40.7 | -30.34 | -3.02 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 67.99 | -32.01 | 225 | 18.7 | -38.63 | -7.39 | -41.52 | 215 |
| 41 | Bollinger breakout · 1h | breakout | 67.42 | -32.58 | 220 | 23.2 | -30.20 | -7.81 | -31.70 | 211 |
| 42 | OBV trend · 1h | momentum | 66.06 | -33.95 | 332 | 19.6 | -39.79 | -9.62 | -40.20 | 214 |
| 43 | EMA 20/50 cross · 1h | trend | 65.47 | -34.53 | 128 | 9.4 | -38.05 | -10.27 | -38.64 | 118 |
| 44 | Triple EMA stack · 1h | trend | 64.85 | -35.15 | 175 | 14.9 | -40.74 | -9.98 | -41.67 | 164 |
| 45 | MACD zero-line · 1h | trend | 64.53 | -35.47 | 206 | 16.5 | -35.44 | -9.19 | -37.39 | 188 |
| 46 | RSI momentum · 1h | momentum | 63.37 | -36.62 | 208 | 15.4 | -41.64 | -8.89 | -42.76 | 191 |
| 47 | MFI reversion · 1h | reversion | 63.34 | -36.66 | 529 | 33.8 | -32.00 | -4.64 | -38.15 | 194 |
| 48 | Max aggression: 1-day momentum | meta | 62.92 | -37.08 | 35 | 28.6 | -58.22 | -3.97 | -63.62 | 38 |
| 49 | Donchian 20/10 · 1h | breakout | 62.73 | -37.27 | 188 | 17.0 | -37.91 | -8.12 | -40.84 | 196 |
| 50 | Heikin-Ashi · 1h | trend | 61.12 | -38.88 | 569 | 22.0 | -48.32 | -9.42 | -49.90 | 645 |
| 51 | ROC + volume · 1h | momentum | 60.73 | -39.27 | 477 | 26.8 | -39.49 | -7.59 | -40.48 | 343 |
| 52 | EMA 9/21 cross · 1h | trend | 59.51 | -40.49 | 316 | 12.3 | -44.54 | -9.95 | -46.92 | 312 |
| 53 | MACD cross · 1h | trend | 58.22 | -41.78 | 502 | 20.9 | -53.12 | -10.16 | -55.83 | 508 |
| 54 | Agent (ML meta-label) | meta | 55.37 | -44.63 | 2076 | 25.4 | -26.17 | -3.43 | -31.80 | 289 |
| 55 | CCI reversion · 1h | reversion | 53.11 | -46.89 | 468 | 38.5 | -51.00 | -8.13 | -55.11 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 52.21 | -47.79 | 408 | 36.8 | -39.86 | -4.75 | -45.50 | 430 |
| 57 | VWAP momentum · 1h | momentum | 51.27 | -48.73 | 1127 | 21.3 | -60.39 | -12.70 | -61.80 | 1180 |
| 58 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.67 | -9.30 | -59.72 | 688 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.57 | -8.95 | -59.48 | 596 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -42.98 | -99.15 | 5337 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.27 | -29.57 | -83.37 | 1403 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.07 | -41.93 | -94.11 | 2389 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.05 | -28.72 | -90.23 | 1865 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.03 | -34.57 | -91.26 | 2199 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.37 | -25.83 | -88.43 | 1913 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.08 | -43.24 | -98.08 | 3362 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -46.87 | -96.90 | 3349 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.33 | -32.86 | -93.36 | 2082 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.87 | -33.31 | -82.17 | 1526 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -50.02 | -99.69 | 6230 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.68 | -35.36 | -92.70 | 2459 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.36 | -34.21 | -94.36 | 3122 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -56.51 | -99.81 | 6019 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.75 | -38.91 | -92.75 | 2225 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.98 | -18.45 | -51.19 | 654 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.53 | -22.10 | -77.98 | 1606 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -50.87 | -97.65 | 3206 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.13 | -53.14 | -99.14 | 5060 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.07 | -22.50 | -69.54 | 1204 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -42.83 | -94.56 | 2642 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.14 | -6.00 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.93 | -31.10 | -84.43 | 1650 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -62.81 | -99.77 | 6460 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.44 | -29.48 | -91.55 | 2463 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.70 | -19.56 | -83.01 | 1956 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.23 | -31.49 | -91.40 | 2127 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.16 | -44.46 | -98.18 | 3998 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.04 | -42.63 | -90.09 | 2189 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.99 | -28.26 | -67.99 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.53 | -26.19 | -72.70 | 1159 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.45 | -18.69 | -84.68 | 1830 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -45.81 | -98.09 | 4359 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -80.19 | -99.94 | 8251 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -45.05 | -6.36 | -52.59 | 303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T17:05 | Agent (rotation) | sell | META | 7.84 | -0.03 | selected signal exited |
| 2026-11-27T17:05 | Gap and go | buy | PLTR | 14.72 | — | rebalance up |
| 2026-11-27T17:05 | Gap and go | sell | META | 19.49 | -0.09 | stop-loss |
| 2026-11-27T17:00 | Triple EMA stack · 1h | sell | XRP-USD | 10.78 | -0.06 | exit signal |
| 2026-11-27T17:00 | EMA 9/21 cross · 1h | buy | SPY | 5.96 | — | entry |
| 2026-11-27T17:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 6.47 | 0.04 | exit signal |
| 2026-11-27T16:36 | Volume breakout · 1h | sell | META | 19.19 | 0.02 | target is flat |
| 2026-11-27T16:36 | Opening range 30m | buy | UPRO | 7.94 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | TQQQ | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | SPY | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | SOXL | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | buy | QQQ | 7.95 | — | entry signal |
| 2026-11-27T16:36 | Opening range 30m | sell | TSLA | 4.52 | 0.03 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | TNA | 6.66 | 0.04 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | PLTR | 6.69 | 0.06 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | META | 6.59 | 0.03 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | IWM | 4.54 | 0.00 | rebalance down |
| 2026-11-27T16:36 | Opening range 30m | sell | AMZN | 6.64 | 0.06 | rebalance down |
| 2026-11-27T16:36 | Opening range 15m | buy | UPRO | 7.20 | — | entry signal |
| 2026-11-27T16:36 | Opening range 15m | buy | TQQQ | 7.21 | — | entry signal |
| 2026-11-27T16:36 | Opening range 15m | buy | SPY | 7.21 | — | entry signal |
| 2026-11-27T16:36 | Opening range 15m | buy | SOXL | 7.21 | — | entry signal |
| 2026-11-27T16:36 | Opening range 15m | buy | QQQ | 7.21 | — | entry signal |
| 2026-11-27T16:36 | Opening range 15m | sell | TSLA | 4.10 | 0.02 | rebalance down |
| 2026-11-27T16:36 | Opening range 15m | sell | TNA | 4.18 | 0.02 | rebalance down |
| 2026-11-27T16:36 | Opening range 15m | sell | PLTR | 4.22 | 0.05 | rebalance down |
| 2026-11-27T16:36 | Opening range 15m | sell | META | 4.06 | 0.02 | rebalance down |
| 2026-11-27T16:36 | Opening range 15m | sell | IWM | 4.11 | 0.00 | rebalance down |
| 2026-11-27T16:36 | Opening range 15m | sell | AMZN | 4.11 | 0.05 | rebalance down |
| 2026-11-27T16:30 | MFI reversion · 1h | buy | BITX | 3.90 | — | rebalance up |
| 2026-11-27T16:30 | MFI reversion · 1h | buy | AMZN | 3.82 | — | rebalance up |
| 2026-11-27T16:30 | MFI reversion · 1h | sell | QQQ | 5.25 | 0.21 | exit signal |
| 2026-11-27T16:30 | CCI reversion · 1h | sell | UPRO | 4.42 | 0.04 | exit signal |
| 2026-11-27T16:30 | Stochastic reversion · 1h | sell | MSTR | 17.26 | 1.20 | exit signal |
| 2026-11-27T16:30 | Stochastic reversion · 1h | sell | AMD | 17.32 | 0.77 | exit signal |
| 2026-11-27T16:30 | Bollinger reversion · 1h | sell | AMD | 13.20 | 0.15 | exit signal |
| 2026-11-27T16:30 | Donchian 55/20 · 1h | buy | META | 7.84 | — | entry signal |
| 2026-11-27T16:30 | Donchian 55/20 · 1h | sell | PLTR | 3.86 | 0.06 | rebalance down |
| 2026-11-27T16:30 | Donchian 55/20 · 1h | sell | DOGE-USD | 3.98 | -0.01 | rebalance down |
| 2026-11-27T16:30 | VWAP momentum · 1h | buy | GOOGL | 2.43 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 17:05:05.000122+00:00 -> 2026-11-27 17:15:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
