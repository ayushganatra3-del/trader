# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T21:40:05.000155+00:00 · 35922 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, IAM 12%, APLD 12%, BPRE 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 16363 decisions in 3278 calls, $0.2289 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T21:40 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-25T21:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T21:40 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | BITX | 2.56 | +2.84% | 15 |
| VWAP momentum | PLTR | 2.20 | +6.89% | 7 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.95 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.02 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.60 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.04 | -3.33 | -13.74 | 157 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 6.21 | 2.99 | -1.37 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.18 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.85 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.09 | -4.91 | 0 | — | 0.02 | 0.18 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.13 | -5.87 | 25 | 40.0 | -17.34 | -3.33 | -21.47 | 61 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.76 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -6.94 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.50 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.42 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 91.81 | -8.19 | 118 | 25.4 | -23.16 | -5.65 | -24.07 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.35 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.35 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.34 | -9.66 | 112 | 17.9 | -12.65 | -2.57 | -15.15 | 260 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.03 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -14.69 | -2.97 | -17.81 | 114 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.70 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.74 | -11.26 | 106 | 27.4 | -12.35 | -2.41 | -16.41 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.23 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.90 | -3.92 | -22.47 | 393 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -23.18 | -4.84 | -24.79 | 190 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -23.21 | -4.60 | -24.99 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.06 | -4.63 | -17.87 | 703 |
| 40 | RSI momentum · 1h | momentum | 85.45 | -14.55 | 101 | 15.8 | -21.54 | -4.56 | -23.32 | 216 |
| 41 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 42 | Supertrend · 1h | trend | 84.79 | -15.21 | 112 | 14.3 | -25.15 | -5.27 | -27.77 | 216 |
| 43 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 44 | MACD cross · 1h | trend | 83.56 | -16.44 | 228 | 22.8 | -24.22 | -4.82 | -27.50 | 466 |
| 45 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.38 | -5.20 | -28.32 | 211 |
| 46 | Z-score reversion · 1h | reversion | 83.41 | -16.59 | 110 | 33.6 | -15.59 | -2.62 | -21.48 | 204 |
| 47 | MFI reversion · 1h | reversion | 81.49 | -18.51 | 262 | 31.7 | -16.12 | -2.62 | -20.54 | 148 |
| 48 | Donchian 20/10 · 1h | breakout | 81.19 | -18.81 | 97 | 19.6 | -24.26 | -4.64 | -27.27 | 217 |
| 49 | MACD zero-line · 1h | trend | 81.16 | -18.84 | 106 | 15.1 | -22.09 | -4.59 | -25.51 | 219 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.75 | -6.93 | -32.97 | 304 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.00 | -6.37 | -36.54 | 536 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.40 | -6.51 | -31.80 | 372 |
| 53 | CCI reversion · 1h | reversion | 79.77 | -20.23 | 204 | 42.2 | -26.32 | -3.91 | -28.08 | 461 |
| 54 | Three white soldiers | momentum | 79.30 | -20.70 | 289 | 19.0 | -44.43 | -21.03 | -44.43 | 597 |
| 55 | Agent (ML meta-label) | meta | 79.29 | -20.71 | 875 | 18.7 | -15.87 | -3.46 | -16.34 | 352 |
| 56 | ROC + volume · 1h | momentum | 78.10 | -21.90 | 240 | 23.8 | -29.89 | -5.87 | -31.53 | 378 |
| 57 | Heikin-Ashi · 1h | trend | 78.00 | -22.00 | 279 | 22.9 | -43.68 | -10.04 | -44.10 | 658 |
| 58 | Candlestick reversal · 1h | reversion | 76.83 | -23.17 | 263 | 28.1 | -35.49 | -6.68 | -36.08 | 557 |
| 59 | RSI(14) reversion · 1h | reversion | 76.70 | -23.30 | 99 | 23.2 | -17.16 | -3.19 | -24.41 | 195 |
| 60 | EMA 9/21 cross · 1h | trend | 76.43 | -23.57 | 165 | 11.5 | -31.33 | -6.41 | -34.22 | 327 |
| 61 | VWAP momentum · 1h | momentum | 75.25 | -24.75 | 531 | 20.9 | -50.65 | -11.53 | -50.90 | 1233 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.95 | -44.05 | 725 | 22.1 | -74.81 | -27.64 | -75.12 | 1556 |
| 64 | Volume breakout | breakout | 54.75 | -45.26 | 442 | 12.4 | -62.63 | -26.39 | -62.92 | 791 |
| 65 | Donchian 55/20 | breakout | 51.96 | -48.04 | 580 | 19.0 | -72.16 | -24.13 | -72.27 | 1260 |
| 66 | Squeeze breakout | breakout | 51.74 | -48.26 | 573 | 13.8 | -67.44 | -29.23 | -67.52 | 1167 |
| 67 | EMA 20/50 cross | trend | 51.09 | -48.91 | 638 | 20.2 | -79.14 | -23.58 | -79.14 | 1416 |
| 68 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -45.45 | -98.82 | 5093 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.90 | -46.36 | -93.95 | 2526 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.03 | -30.97 | -89.11 | 1903 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.50 | -39.06 | -91.54 | 2327 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.41 | -29.86 | -90.43 | 2158 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -55.72 | -97.91 | 3517 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -61.53 | -96.26 | 3370 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.15 | -35.47 | -94.20 | 2467 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.12 | -36.64 | -83.13 | 1694 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -55.84 | -99.43 | 5782 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.46 | -42.36 | -92.60 | 2602 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -37.89 | -95.49 | 3379 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -83.40 | -99.78 | 6176 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -45.61 | -92.29 | 2336 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -65.46 | -97.67 | 3552 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -62.04 | -98.67 | 4797 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -59.82 | -94.68 | 2778 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.24 | -39.66 | -84.38 | 1792 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -69.45 | -99.60 | 6269 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.50 | -29.68 | -88.50 | 2235 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.27 | -20.37 | -78.27 | 1709 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.82 | -38.66 | -90.85 | 2277 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.33 | -49.55 | -96.33 | 3806 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.87 | -51.77 | -89.87 | 2118 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.79 | -18.25 | -76.94 | 1591 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.48 | -50.18 | -96.48 | 4187 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.17 | -99.92 | 8253 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T21:15 | EMA 20/50 cross | sell | SOL-USD | 12.75 | -0.05 | exit signal |
| 2026-10-25T21:15 | EMA 20/50 cross | sell | DOGE-USD | 10.23 | -0.00 | exit signal |
| 2026-10-25T21:05 | EMA 9/21 cross · 1h | buy | DOGE-USD | 2.97 | — | entry |
| 2026-10-25T21:00 | ROC + volume · 1h | buy | SOL-USD | 19.55 | — | entry signal |
| 2026-10-25T21:00 | ADX DI cross · 1h | sell | SOL-USD | 22.53 | -0.20 | exit signal |
| 2026-10-25T21:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 7.89 | — | rebalance up |
| 2026-10-25T21:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 10.86 | -0.11 | exit signal |
| 2026-10-25T20:50 | EMA 20/50 cross | sell | ETH-USD | 10.24 | -0.04 | exit signal |
| 2026-10-25T20:15 | Agent (ML meta-label) | sell | XRP-USD | 4.38 | -0.02 | selected signal exited |
| 2026-10-25T20:05 | Agent (ML meta-label) | buy | XRP-USD | 4.41 | — | entry |
| 2026-10-25T20:00 | Heikin-Ashi · 1h | sell | SOL-USD | 19.43 | -0.15 | exit signal |
| 2026-10-25T20:00 | Heikin-Ashi · 1h | sell | ETH-USD | 19.39 | -0.18 | exit signal |
| 2026-10-25T20:00 | ADX DI cross · 1h | sell | ETH-USD | 21.48 | -0.20 | exit signal |
| 2026-10-25T19:55 | EMA 20/50 cross | sell | XRP-USD | 12.77 | -0.09 | exit signal |
| 2026-10-25T19:40 | EMA 20/50 cross | buy | XRP-USD | 7.65 | — | rebalance up |
| 2026-10-25T19:40 | EMA 20/50 cross | sell | BTC-USD | 12.76 | -0.09 | exit signal |
| 2026-10-25T19:25 | Donchian 55/20 | sell | DOGE-USD | 13.03 | -0.06 | exit signal |
| 2026-10-25T19:10 | Donchian 55/20 | sell | SOL-USD | 13.03 | -0.06 | exit signal |
| 2026-10-25T19:10 | Donchian 55/20 | sell | ETH-USD | 13.01 | -0.07 | exit signal |
| 2026-10-25T19:00 | ADX DI cross · 1h | sell | BTC-USD | 22.54 | -0.17 | exit signal |
| 2026-10-25T19:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 1.69 | — | entry signal |
| 2026-10-25T19:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 8.52 | — | entry signal |
| 2026-10-25T19:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 4.24 | -0.03 | rebalance down |
| 2026-10-25T18:10 | Donchian 55/20 | sell | XRP-USD | 12.89 | -0.14 | stop-loss |
| 2026-10-25T18:05 | Squeeze breakout | sell | XRP-USD | 12.85 | -0.12 | exit signal |
| 2026-10-25T18:05 | ROC + volume | sell | SOL-USD | 13.93 | -0.10 | exit signal |
| 2026-10-25T18:00 | Heikin-Ashi · 1h | buy | ETH-USD | 19.57 | — | entry signal |
| 2026-10-25T18:00 | ADX DI cross · 1h | buy | ETH-USD | 21.68 | — | entry signal |
| 2026-10-25T18:00 | ADX DI cross · 1h | buy | BTC-USD | 22.71 | — | entry signal |
| 2026-10-25T18:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 10.96 | — | entry signal |
| 2026-10-25T18:00 | ROC + volume | sell | XRP-USD | 13.95 | -0.09 | exit signal |
| 2026-10-25T17:35 | Volume breakout | sell | BTC-USD | 13.62 | -0.09 | exit signal |
| 2026-10-25T17:25 | ROC + volume | buy | SOL-USD | 14.03 | — | entry signal |
| 2026-10-25T17:05 | ROC + volume | buy | XRP-USD | 14.03 | — | entry signal |
| 2026-10-25T17:00 | Z-score reversion · 1h | buy | ETH-USD | 1.25 | — | entry |
| 2026-10-25T17:00 | Z-score reversion · 1h | buy | DOGE-USD | 5.14 | — | rebalance up |
| 2026-10-25T17:00 | Z-score reversion · 1h | sell | BTC-USD | 6.38 | -0.04 | exit signal |
| 2026-10-25T17:00 | Heikin-Ashi · 1h | buy | SOL-USD | 19.58 | — | entry signal |
| 2026-10-25T17:00 | ADX DI cross · 1h | buy | SOL-USD | 22.73 | — | entry signal |
| 2026-10-25T17:00 | Parabolic SAR · 1h | buy | XRP-USD | 23.01 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 21:40:05.000155+00:00 -> 2026-10-25 21:50:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
