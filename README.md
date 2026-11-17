# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T06:41:05.000130+00:00 · 62854 ticks

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

Today: 5349 decisions in 1071 calls, $0.0748 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T06:41 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-17T06:41 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T06:41 | 3 / 2 / 0 | BTC-USD 58% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.93 | 17.93 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.61 | 3.61 | 0 | — | 5.47 | 1.51 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.53 | -3.46 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -2.82 | -0.97 | -8.15 | 158 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.74 | -6.26 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.58 | -8.42 | 47 | 42.6 | -8.37 | -1.64 | -14.79 | 59 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.48 | -8.52 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 22 | Squeeze breakout · 1h | breakout | 87.06 | -12.94 | 67 | 20.9 | -11.08 | -4.13 | -16.32 | 79 |
| 23 | Daily: Bullish score | daily | 86.61 | -13.39 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.11 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 82.96 | -17.04 | 180 | 28.3 | -23.12 | -6.25 | -24.73 | 213 |
| 28 | Keltner breakout · 1h | breakout | 80.56 | -19.44 | 121 | 25.6 | -18.42 | -3.95 | -25.84 | 158 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -24.61 | -6.13 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.27 | -19.73 | 213 | 39.9 | -14.54 | -6.43 | -14.88 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.94 | -5.37 | -22.48 | 86 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.03 | -21.97 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.23 | -22.77 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Ichimoku · 1h | trend | 75.15 | -24.85 | 100 | 15.0 | -31.17 | -8.78 | -31.74 | 116 |
| 36 | Hold BTC | benchmark | 75.13 | -24.87 | 2 | 0.0 | -15.41 | -2.17 | -28.91 | 1 |
| 37 | Max aggression: 1-day momentum | meta | 74.85 | -25.15 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 40 | Bollinger breakout · 1h | breakout | 73.77 | -26.23 | 185 | 22.2 | -25.01 | -5.36 | -31.87 | 235 |
| 41 | MFI reversion · 1h | reversion | 72.06 | -27.94 | 420 | 34.3 | -25.57 | -3.63 | -29.02 | 162 |
| 42 | MACD zero-line · 1h | trend | 71.37 | -28.63 | 176 | 18.2 | -26.06 | -5.16 | -32.32 | 198 |
| 43 | Heikin-Ashi · 1h | trend | 71.37 | -28.63 | 459 | 23.3 | -39.39 | -7.54 | -43.26 | 639 |
| 44 | Supertrend · 1h | trend | 71.33 | -28.67 | 187 | 16.0 | -32.53 | -5.53 | -39.67 | 200 |
| 45 | Triple EMA stack · 1h | trend | 71.21 | -28.79 | 154 | 14.9 | -28.48 | -5.17 | -37.77 | 192 |
| 46 | RSI momentum · 1h | momentum | 71.01 | -28.99 | 175 | 14.3 | -30.98 | -5.57 | -38.07 | 203 |
| 47 | EMA 20/50 cross · 1h | trend | 70.90 | -29.10 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | ROC + volume · 1h | momentum | 70.56 | -29.44 | 405 | 28.4 | -28.49 | -4.69 | -37.95 | 356 |
| 49 | MACD cross · 1h | trend | 70.26 | -29.74 | 405 | 22.5 | -33.98 | -4.89 | -43.44 | 476 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.18 | -30.82 | 303 | 19.1 | -31.00 | -5.90 | -39.29 | 259 |
| 52 | CCI reversion · 1h | reversion | 68.04 | -31.96 | 378 | 42.1 | -40.07 | -6.48 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.41 | -32.59 | 157 | 18.5 | -30.58 | -5.03 | -39.25 | 207 |
| 54 | Bollinger reversion · 1h | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.48 | -36.96 | 405 |
| 55 | Williams %R · 1h | reversion | 64.14 | -35.86 | 420 | 41.4 | -44.61 | -7.50 | -45.12 | 543 |
| 56 | EMA 9/21 cross · 1h | trend | 63.60 | -36.40 | 275 | 11.3 | -39.09 | -7.69 | -45.11 | 320 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -22.30 | -3.10 | -27.11 | 317 |
| 58 | Z-score reversion · 1h | reversion | 59.54 | -40.46 | 221 | 35.7 | -34.78 | -4.76 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.27 | -40.73 | 204 | 31.9 | -40.24 | -5.88 | -42.13 | 243 |
| 60 | VWAP momentum · 1h | momentum | 58.15 | -41.84 | 944 | 21.7 | -53.53 | -9.40 | -57.87 | 1209 |
| 61 | Candlestick reversal · 1h | reversion | 57.19 | -42.81 | 537 | 27.0 | -45.65 | -8.24 | -45.72 | 616 |
| 62 | Three white soldiers | momentum | 56.30 | -43.70 | 572 | 14.7 | -49.27 | -21.88 | -49.27 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.15 | -98.99 | 5279 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.33 | -25.62 | -81.60 | 1429 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.00 | -43.43 | -94.01 | 2511 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.98 | -31.19 | -90.03 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.45 | -40.31 | -91.46 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.11 | -30.00 | -90.12 | 2154 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -46.90 | -97.91 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -52.96 | -96.49 | 3443 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -37.21 | -93.56 | 2265 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.86 | -33.42 | -82.87 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.68 | -99.59 | 6050 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -41.65 | -92.10 | 2582 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.25 | -35.85 | -95.25 | 3356 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.01 | -99.81 | 6145 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.36 | -42.93 | -92.36 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.65 | -26.18 | -76.65 | 1653 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -59.41 | -97.63 | 3472 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.00 | -54.37 | -99.00 | 4941 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.85 | -27.51 | -68.85 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -55.37 | -94.72 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -37.62 | -84.71 | 1746 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -64.37 | -99.69 | 6372 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.45 | -29.73 | -90.45 | 2332 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.46 | -18.38 | -79.49 | 1809 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.98 | -35.19 | -90.99 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -44.29 | -97.45 | 3900 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -58.23 | -89.26 | 2152 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.52 | -30.01 | -66.52 | 829 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.22 | -23.37 | -72.23 | 1249 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.22 | -17.46 | -80.49 | 1753 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -45.41 | -97.58 | 4356 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.62 | -99.94 | 8393 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T06:00 | MFI reversion · 1h | sell | ETH-USD | 7.22 | 0.01 | exit signal |
| 2026-11-17T06:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.95 | — | entry signal |
| 2026-11-17T06:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.95 | — | entry signal |
| 2026-11-17T06:00 | Ichimoku · 1h | buy | ETH-USD | 18.84 | — | entry signal |
| 2026-11-17T05:00 | Williams %R · 1h | sell | XRP-USD | 7.25 | 0.08 | exit signal |
| 2026-11-17T05:00 | Squeeze breakout · 1h | buy | SOL-USD | 21.85 | — | entry signal |
| 2026-11-17T05:00 | Donchian 20/10 · 1h | buy | SOL-USD | 16.96 | — | entry signal |
| 2026-11-17T05:00 | MACD zero-line · 1h | buy | BTC-USD | 17.59 | — | entry signal |
| 2026-11-17T05:00 | MACD cross · 1h | buy | DOGE-USD | 3.44 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 06:41:05.000130+00:00 -> 2026-11-17 06:51:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 06:41:05.000130+00:00 -> 2026-11-17 06:51:05.000130+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
