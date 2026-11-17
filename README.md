# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T17:07:05.000140+00:00 · 63399 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £83.17 (-16.83%)

Closed trades 208, win rate 36.1%, fees £5.89, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 16.62 | -0.10 |
| SOXL | 32.68 | -0.69 |

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

Today: 23346 decisions in 2706 calls, $0.2996 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T17:07 | 10 / 18 / 2 | TNA 15% |  |
| Breezy | 2026-11-17T17:07 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-17T17:07 | 9 / 20 / 1 | COIN 67% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.16 | 17.16 | 0 | — | 12.73 | 4.23 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 24 | 62.5 | 18.31 | 3.63 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.93 | 2.93 | 0 | — | 5.33 | 1.47 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.16 | 2.15 | 36 | 41.7 | 0.78 | 0.30 | -9.64 | 33 |
| 6 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.63 | 2.12 | -9.06 | 224 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -2.71 | -2.27 | -4.31 | 71 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.21 | -4.79 | 8 | 50.0 | -3.83 | -0.10 | -18.69 | 6 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 95.13 | -4.87 | 0 | — | -4.15 | -1.31 | -6.90 | 1 |
| 13 | Agent (rotation) | meta | 94.46 | -5.54 | 197 | 29.9 | -1.20 | -0.35 | -8.15 | 159 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 91.95 | -8.05 | 0 | — | -8.67 | -2.26 | -8.69 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.03 | -8.97 | 47 | 42.6 | -9.26 | -1.84 | -14.79 | 62 |
| 18 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.11 | -9.89 | 0 | — | -8.53 | -2.30 | -12.67 | 1 |
| 21 | Daily: Bullish score | daily | 87.69 | -12.31 | 17 | 17.6 | -3.41 | -0.47 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -10.31 | -3.39 | -16.01 | 73 |
| 24 | Opening range 30m | breakout | 86.67 | -13.33 | 438 | 33.6 | -9.41 | -2.95 | -14.11 | 575 |
| 25 | Agent | meta | 83.17 | -16.83 | 208 | 36.1 | -17.24 | -7.48 | -17.54 | 203 |
| 26 | Max aggression: 5-day momentum | meta | 81.88 | -18.12 | 21 | 42.9 | -46.72 | -3.02 | -55.24 | 22 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.14 | -7.15 | -28.08 | 202 |
| 28 | Keltner breakout · 1h | breakout | 81.56 | -18.44 | 121 | 25.6 | -18.29 | -4.07 | -26.34 | 157 |
| 29 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.47 | -6.39 | -14.87 | 94 |
| 30 | Volume breakout · 1h | breakout | 80.22 | -19.78 | 162 | 28.4 | -15.60 | -4.91 | -22.00 | 81 |
| 31 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.40 | -6.63 | -29.47 | 84 |
| 32 | Agent (aggressive) | meta | 79.62 | -20.38 | 99 | 33.3 | -19.57 | -5.03 | -19.91 | 98 |
| 33 | Opening range 15m | breakout | 78.56 | -21.44 | 533 | 31.5 | -16.23 | -4.32 | -21.37 | 686 |
| 34 | Max aggression: 1-day momentum | meta | 78.55 | -21.45 | 30 | 26.7 | -22.42 | -0.79 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 75.98 | -24.02 | 2 | 0.0 | -16.02 | -1.99 | -26.43 | 1 |
| 36 | ADX DI cross · 1h | trend | 75.54 | -24.46 | 208 | 19.2 | -27.26 | -4.33 | -35.85 | 261 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.28 | -8.50 | -29.80 | 111 |
| 38 | Hold BTC | benchmark | 74.23 | -25.77 | 2 | 0.0 | -16.85 | -2.40 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 74.17 | -25.83 | 188 | 21.8 | -25.49 | -5.51 | -33.01 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 72.07 | -27.93 | 345 | 42.6 | -35.44 | -5.34 | -36.06 | 424 |
| 41 | Triple EMA stack · 1h | trend | 71.45 | -28.55 | 155 | 14.8 | -29.64 | -5.91 | -36.18 | 187 |
| 42 | RSI momentum · 1h | momentum | 71.20 | -28.80 | 176 | 14.2 | -30.22 | -5.45 | -37.27 | 198 |
| 43 | Supertrend · 1h | trend | 71.15 | -28.85 | 189 | 15.9 | -32.10 | -5.46 | -38.72 | 202 |
| 44 | MACD zero-line · 1h | trend | 71.05 | -28.95 | 181 | 17.7 | -26.45 | -5.24 | -32.82 | 199 |
| 45 | EMA 20/50 cross · 1h | trend | 70.28 | -29.72 | 115 | 10.4 | -35.94 | -9.89 | -39.00 | 114 |
| 46 | Heikin-Ashi · 1h | trend | 70.06 | -29.94 | 466 | 23.0 | -41.16 | -8.26 | -44.59 | 633 |
| 47 | MFI reversion · 1h | reversion | 70.00 | -30.00 | 424 | 34.0 | -26.68 | -3.83 | -30.42 | 165 |
| 48 | ROC + volume · 1h | momentum | 69.85 | -30.15 | 408 | 28.2 | -28.64 | -4.61 | -37.96 | 353 |
| 49 | MACD cross · 1h | trend | 69.44 | -30.56 | 413 | 22.3 | -37.45 | -5.90 | -44.43 | 473 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.77 | -31.23 | 306 | 19.0 | -35.02 | -7.46 | -39.92 | 261 |
| 52 | Donchian 20/10 · 1h | breakout | 67.46 | -32.54 | 159 | 18.2 | -30.91 | -5.25 | -39.11 | 206 |
| 53 | CCI reversion · 1h | reversion | 65.92 | -34.08 | 382 | 41.6 | -42.18 | -6.92 | -44.29 | 460 |
| 54 | Bollinger reversion · 1h | reversion | 63.91 | -36.09 | 344 | 37.8 | -39.22 | -5.92 | -39.92 | 407 |
| 55 | EMA 9/21 cross · 1h | trend | 63.09 | -36.91 | 280 | 11.1 | -40.62 | -8.11 | -45.81 | 320 |
| 56 | Williams %R · 1h | reversion | 62.22 | -37.78 | 430 | 40.7 | -46.58 | -7.92 | -46.97 | 550 |
| 57 | Agent (ML meta-label) | meta | 60.16 | -39.84 | 1886 | 24.5 | -21.91 | -3.51 | -26.40 | 323 |
| 58 | RSI(14) reversion · 1h | reversion | 58.34 | -41.66 | 205 | 31.7 | -41.91 | -6.21 | -42.95 | 242 |
| 59 | VWAP momentum · 1h | momentum | 57.17 | -42.83 | 957 | 21.6 | -53.39 | -9.56 | -58.19 | 1200 |
| 60 | Z-score reversion · 1h | reversion | 56.96 | -43.04 | 224 | 35.3 | -37.75 | -5.21 | -39.23 | 244 |
| 61 | Three white soldiers | momentum | 55.42 | -44.58 | 581 | 14.6 | -49.47 | -21.84 | -49.87 | 659 |
| 62 | Candlestick reversal · 1h | reversion | 54.13 | -45.87 | 546 | 26.6 | -48.28 | -8.58 | -48.92 | 618 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -43.11 | -99.02 | 5249 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.66 | -25.61 | -82.02 | 1401 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.06 | -42.62 | -94.06 | 2497 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.27 | -31.28 | -90.33 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -37.94 | -91.35 | 2301 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.82 | -30.52 | -89.83 | 2121 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -46.78 | -97.90 | 3443 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -53.78 | -96.57 | 3432 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -37.05 | -93.59 | 2223 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.98 | -32.11 | -83.06 | 1619 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -53.24 | -99.61 | 6080 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.95 | -40.72 | -92.00 | 2561 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.13 | -37.74 | -95.14 | 3328 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -65.33 | -99.81 | 6152 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.23 | -41.83 | -92.23 | 2247 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.89 | -26.13 | -75.90 | 1646 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -56.98 | -97.64 | 3456 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.04 | -55.17 | -99.04 | 4951 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.34 | -26.81 | -68.46 | 1224 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -52.86 | -94.58 | 2732 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.33 | -36.79 | -84.38 | 1736 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -66.15 | -99.70 | 6379 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.88 | -30.16 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.95 | -18.78 | -79.98 | 1835 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.23 | -34.73 | -91.33 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.59 | -44.99 | -97.59 | 3930 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -55.89 | -89.38 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.19 | -29.79 | -66.19 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.85 | -22.78 | -72.51 | 1232 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.76 | -17.80 | -80.90 | 1741 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.60 | -45.59 | -97.63 | 4360 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.05 | -99.94 | 8401 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T17:05 | Agent (ML meta-label) | buy | SPY | 12.59 | — | entry |
| 2026-11-17T17:05 | Williams %R · 1h | buy | SOXL | 6.50 | — | rebalance up |
| 2026-11-17T17:05 | Williams %R · 1h | sell | AAPL | 12.56 | -0.12 | stop-loss |
| 2026-11-17T17:05 | Stochastic reversion · 1h | sell | AAPL | 4.25 | -0.02 | stop-loss |
| 2026-11-17T17:00 | Agent (aggressive) | buy | COIN | 40.09 | — | following MACD cross |
| 2026-11-17T17:00 | Agent | buy | COIN | 16.72 | — | following MACD cross |
| 2026-11-17T17:00 | Supertrend · 1h | buy | XRP-USD | 7.54 | — | rebalance up |
| 2026-11-17T17:00 | Supertrend · 1h | buy | SQQQ | 7.04 | — | rebalance up |
| 2026-11-17T17:00 | Supertrend · 1h | buy | SOL-USD | 7.47 | — | rebalance up |
| 2026-11-17T17:00 | Supertrend · 1h | buy | DOGE-USD | 7.76 | — | rebalance up |
| 2026-11-17T17:00 | Supertrend · 1h | sell | ETH-USD | 9.89 | -0.36 | exit signal |
| 2026-11-17T17:00 | Supertrend · 1h | sell | BTC-USD | 11.65 | -0.37 | exit signal |
| 2026-11-17T17:00 | MACD zero-line · 1h | sell | SOL-USD | 17.93 | -0.08 | exit signal |
| 2026-11-17T17:00 | MACD cross · 1h | sell | SOL-USD | 14.18 | 0.01 | exit signal |
| 2026-11-17T16:50 | MFI reversion · 1h | buy | LABU | 5.20 | — | rebalance up |
| 2026-11-17T16:50 | MFI reversion · 1h | sell | GOOGL | 10.00 | -0.01 | target is flat |
| 2026-11-17T16:45 | MFI reversion · 1h | buy | LABU | 6.51 | — | entry |
| 2026-11-17T16:45 | MFI reversion · 1h | buy | GOOGL | 5.40 | — | rebalance up |
| 2026-11-17T16:45 | MFI reversion · 1h | sell | SPY | 3.95 | -0.04 | rebalance down |
| 2026-11-17T16:45 | MFI reversion · 1h | sell | COIN | 4.03 | -0.09 | rebalance down |
| 2026-11-17T16:45 | MFI reversion · 1h | sell | AMZN | 3.92 | -0.04 | rebalance down |
| 2026-11-17T16:40 | Agent (ML meta-label) | sell | SPY | 15.03 | -0.02 | selected signal exited |
| 2026-11-17T16:40 | Agent | sell | BITX | 16.65 | -0.14 | selected signal exited |
| 2026-11-17T16:35 | Agent (ML meta-label) | buy | SPY | 15.05 | — | entry |
| 2026-11-17T16:35 | Agent (ML meta-label) | sell | SQQQ | 15.14 | 0.12 | selected signal exited |
| 2026-11-17T16:30 | Williams %R · 1h | buy | SOXL | 6.10 | — | entry signal |
| 2026-11-17T16:30 | Williams %R · 1h | buy | QQQ | 10.48 | — | entry signal |
| 2026-11-17T16:30 | Williams %R · 1h | buy | NVDA | 10.48 | — | entry signal |
| 2026-11-17T16:30 | Williams %R · 1h | buy | AMD | 10.48 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | UPRO | 3.82 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | TQQQ | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | TECL | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | SPY | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | QQQ | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | PLTR | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | MSTR | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | buy | ETHU | 4.28 | — | entry signal |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | TSLA | 3.76 | 0.01 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | SOXL | 4.24 | 0.09 | rebalance down |
| 2026-11-17T16:30 | Stochastic reversion · 1h | sell | NVDA | 3.87 | 0.03 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 17:07:05.000140+00:00 -> 2026-11-17 17:17:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 17:07:05.000140+00:00 -> 2026-11-17 17:17:05.000140+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
