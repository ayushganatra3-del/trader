# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T13:10:05.000134+00:00 · 63195 ticks

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

Today: 10431 decisions in 2094 calls, $0.1459 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T13:10 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-17T13:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T13:10 | 5 / 0 / 0 | SOL-USD 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.03 | 18.03 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.73 | 3.73 | 0 | — | 5.51 | 1.52 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.62 | -3.38 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.62 | -8.15 | 157 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.82 | -6.18 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.66 | -8.34 | 47 | 42.6 | -8.37 | -1.64 | -14.79 | 59 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.56 | -8.44 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.62 | -12.38 | 67 | 20.9 | -10.38 | -3.84 | -16.34 | 78 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.67 | -13.33 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.10 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Parabolic SAR · 1h | trend | 83.40 | -16.60 | 181 | 28.2 | -22.75 | -6.13 | -24.87 | 214 |
| 27 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 28 | Keltner breakout · 1h | breakout | 80.58 | -19.42 | 121 | 25.6 | -18.70 | -4.14 | -25.84 | 157 |
| 29 | Donchian 55/20 · 1h | breakout | 80.56 | -19.44 | 76 | 13.2 | -24.82 | -6.44 | -29.04 | 84 |
| 30 | Connors RSI(2) · 1h | reversion | 80.31 | -19.69 | 213 | 39.9 | -14.53 | -6.42 | -14.88 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.38 | -5.18 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.10 | -21.90 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.30 | -22.70 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 76.09 | -23.91 | 2 | 0.0 | -14.12 | -1.95 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -31.24 | -8.80 | -31.74 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.92 | -25.08 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.74 | -25.26 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.30 | -25.70 | 186 | 22.0 | -24.40 | -5.21 | -31.89 | 235 |
| 40 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 41 | Supertrend · 1h | trend | 72.20 | -27.80 | 187 | 16.0 | -31.66 | -5.31 | -39.67 | 200 |
| 42 | MFI reversion · 1h | reversion | 72.15 | -27.85 | 420 | 34.3 | -25.78 | -3.65 | -29.33 | 163 |
| 43 | MACD zero-line · 1h | trend | 71.84 | -28.16 | 178 | 18.0 | -25.62 | -5.06 | -32.35 | 198 |
| 44 | RSI momentum · 1h | momentum | 71.48 | -28.52 | 175 | 14.3 | -31.20 | -5.64 | -38.07 | 202 |
| 45 | Heikin-Ashi · 1h | trend | 71.46 | -28.54 | 461 | 23.2 | -38.66 | -7.35 | -43.26 | 634 |
| 46 | Triple EMA stack · 1h | trend | 71.22 | -28.78 | 154 | 14.9 | -31.98 | -6.32 | -37.77 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.94 | -29.06 | 112 | 9.8 | -35.45 | -9.64 | -38.88 | 114 |
| 48 | ROC + volume · 1h | momentum | 70.58 | -29.43 | 405 | 28.4 | -28.30 | -4.65 | -37.95 | 355 |
| 49 | MACD cross · 1h | trend | 70.47 | -29.52 | 409 | 22.2 | -34.13 | -4.98 | -43.66 | 479 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.22 | -30.78 | 303 | 19.1 | -34.43 | -7.22 | -39.75 | 262 |
| 52 | CCI reversion · 1h | reversion | 68.00 | -32.00 | 378 | 42.1 | -40.10 | -6.49 | -42.07 | 457 |
| 53 | Donchian 20/10 · 1h | breakout | 67.65 | -32.35 | 158 | 18.4 | -31.09 | -5.25 | -39.27 | 208 |
| 54 | Bollinger reversion · 1h | reversion | 66.49 | -33.51 | 336 | 38.7 | -36.43 | -5.50 | -36.96 | 408 |
| 55 | Williams %R · 1h | reversion | 64.28 | -35.72 | 421 | 41.6 | -44.51 | -7.47 | -45.13 | 544 |
| 56 | EMA 9/21 cross · 1h | trend | 63.95 | -36.05 | 278 | 11.2 | -39.87 | -8.00 | -45.47 | 320 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -22.76 | -3.74 | -27.39 | 328 |
| 58 | Z-score reversion · 1h | reversion | 59.59 | -40.41 | 221 | 35.7 | -34.89 | -4.79 | -36.18 | 244 |
| 59 | RSI(14) reversion · 1h | reversion | 59.29 | -40.71 | 204 | 31.9 | -40.74 | -5.99 | -42.17 | 240 |
| 60 | VWAP momentum · 1h | momentum | 58.03 | -41.97 | 949 | 21.7 | -53.11 | -9.37 | -57.96 | 1208 |
| 61 | Candlestick reversal · 1h | reversion | 57.15 | -42.85 | 538 | 27.0 | -45.63 | -8.26 | -45.68 | 618 |
| 62 | Three white soldiers | momentum | 56.18 | -43.82 | 575 | 14.6 | -49.14 | -21.89 | -49.37 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -43.11 | -98.99 | 5294 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.30 | -25.57 | -81.70 | 1435 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.97 | -43.41 | -94.01 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.03 | -31.35 | -90.16 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -39.52 | -91.38 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.95 | -30.57 | -89.95 | 2142 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -47.67 | -97.95 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -51.76 | -96.44 | 3438 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.60 | -37.30 | -93.64 | 2270 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.79 | -33.30 | -82.89 | 1640 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.41 | -99.59 | 6044 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.95 | -40.64 | -92.02 | 2581 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.14 | -37.21 | -95.14 | 3345 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -66.45 | -99.80 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.35 | -43.23 | -92.39 | 2267 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.42 | -26.29 | -76.50 | 1653 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -58.26 | -97.62 | 3473 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -54.65 | -99.00 | 4941 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.44 | -26.98 | -68.56 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -54.42 | -94.68 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.37 | -36.84 | -84.52 | 1744 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -64.73 | -99.69 | 6372 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.45 | -29.69 | -90.56 | 2337 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.61 | -18.53 | -79.75 | 1814 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.98 | -35.29 | -91.04 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.49 | -44.98 | -97.49 | 3913 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -59.60 | -89.35 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.34 | -30.12 | -66.34 | 829 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.77 | -23.02 | -72.26 | 1249 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.22 | -17.47 | -80.50 | 1755 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -45.07 | -97.56 | 4353 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.06 | -99.94 | 8402 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T13:10 | MACD cross · 1h | sell | XRP-USD | 3.52 | -0.01 | rebalance down |
| 2026-11-17T13:00 | CCI reversion · 1h | buy | ETH-USD | 17.00 | — | entry signal |
| 2026-11-17T13:00 | Williams %R · 1h | sell | DOGE-USD | 6.45 | 0.03 | exit signal |
| 2026-11-17T13:00 | Bollinger reversion · 1h | sell | ETH-USD | 4.14 | -0.02 | exit signal |
| 2026-11-17T13:00 | Bollinger reversion · 1h | sell | DOGE-USD | 4.14 | -0.02 | exit signal |
| 2026-11-17T13:00 | Bollinger reversion · 1h | sell | BTC-USD | 4.14 | -0.02 | exit signal |
| 2026-11-17T13:00 | OBV trend · 1h | buy | SOL-USD | 17.30 | — | entry signal |
| 2026-11-17T13:00 | VWAP momentum · 1h | buy | ETH-USD | 7.24 | — | entry signal |
| 2026-11-17T13:00 | MACD cross · 1h | buy | DOGE-USD | 13.76 | — | entry signal |
| 2026-11-17T13:00 | MACD cross · 1h | buy | BTC-USD | 14.08 | — | entry signal |
| 2026-11-17T13:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 17.73 | — | entry signal |
| 2026-11-17T13:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 15.96 | — | entry signal |
| 2026-11-17T12:10 | Three white soldiers | sell | XRP-USD | 13.97 | -0.05 | exit signal |
| 2026-11-17T12:00 | CCI reversion · 1h | buy | DOGE-USD | 17.01 | — | entry signal |
| 2026-11-17T12:00 | CCI reversion · 1h | buy | BTC-USD | 17.01 | — | entry signal |
| 2026-11-17T12:00 | Bollinger reversion · 1h | buy | ETH-USD | 4.16 | — | entry signal |
| 2026-11-17T12:00 | Bollinger reversion · 1h | buy | DOGE-USD | 4.16 | — | entry signal |
| 2026-11-17T12:00 | Bollinger reversion · 1h | buy | BTC-USD | 4.16 | — | entry signal |
| 2026-11-17T12:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.72 | — | entry signal |
| 2026-11-17T12:00 | Bollinger breakout · 1h | buy | XRP-USD | 18.54 | — | entry signal |
| 2026-11-17T12:00 | Donchian 55/20 · 1h | buy | SOL-USD | 20.12 | — | entry signal |
| 2026-11-17T12:00 | Donchian 20/10 · 1h | buy | XRP-USD | 16.88 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | XRP-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | SOL-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | DOGE-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | BTC-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | Parabolic SAR · 1h | buy | XRP-USD | 20.81 | — | entry signal |
| 2026-11-17T12:00 | MACD cross · 1h | buy | XRP-USD | 17.60 | — | entry signal |
| 2026-11-17T11:20 | Three white soldiers | buy | XRP-USD | 14.02 | — | entry signal |
| 2026-11-17T11:15 | Three white soldiers | buy | BTC-USD | 14.03 | — | entry signal |
| 2026-11-17T11:00 | VWAP momentum · 1h | sell | SOL-USD | 14.42 | -0.08 | exit signal |
| 2026-11-17T11:00 | MACD zero-line · 1h | sell | XRP-USD | 17.71 | -0.32 | exit signal |
| 2026-11-17T11:00 | MACD cross · 1h | sell | XRP-USD | 14.12 | -0.13 | exit signal |
| 2026-11-17T11:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 15.58 | -0.37 | exit signal |
| 2026-11-17T10:10 | Donchian 20/10 · 1h | sell | ETH-USD | 16.43 | -0.53 | stop-loss |
| 2026-11-17T10:10 | Three white soldiers | sell | SOL-USD | 13.99 | -0.09 | exit signal |
| 2026-11-17T10:00 | Williams %R · 1h | buy | DOGE-USD | 6.41 | — | entry signal |
| 2026-11-17T10:00 | Parabolic SAR · 1h | sell | ETH-USD | 20.06 | -0.49 | exit signal |
| 2026-11-17T10:00 | MACD cross · 1h | sell | ETH-USD | 17.45 | -0.29 | exit signal |
| 2026-11-17T09:45 | Three white soldiers | sell | ETH-USD | 13.97 | -0.10 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 13:10:05.000134+00:00 -> 2026-11-17 13:20:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 13:10:05.000134+00:00 -> 2026-11-17 13:20:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
