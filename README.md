# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T15:35:05.000154+00:00 · 38006 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.97 (-10.03%)

Closed trades 112, win rate 38.4%, fees £3.45, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 17.97 | -0.02 |
| PLTR | 18.04 | +0.06 |

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

Today: 18469 decisions in 2291 calls, $0.2386 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T15:35 | 1 / 16 / 13 | cash |  |
| Breezy | 2026-10-27T15:35 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-27T15:35 | 5 / 21 / 4 | COIN 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.30 | +6.55% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.54 | 7.54 | 0 | — | 8.03 | 4.00 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.80 | 5.80 | 14 | 71.4 | 3.02 | 1.01 | -6.62 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.56 | 4.56 | 19 | 47.4 | 6.88 | 2.23 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.00 | 1.00 | 0 | — | 2.87 | 1.33 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.45 | -0.56 | 0 | — | 0.63 | 0.41 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.30 | -1.70 | 81 | 34.6 | 6.85 | 3.28 | -1.80 | 98 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.44 | -2.56 | 0 | — | 0.13 | 0.12 | -5.99 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.06 | -1.93 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.14 | -3.86 | 122 | 31.1 | -3.38 | -1.79 | -6.39 | 192 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.74 | -4.26 | 0 | — | -6.01 | -2.47 | -7.83 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.89 | 1.15 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 18 | Hold BTC | benchmark | 95.36 | -4.64 | 0 | — | 2.63 | 0.60 | -9.28 | 1 |
| 19 | Gap and go | momentum | 94.83 | -5.17 | 111 | 25.2 | 4.89 | 1.60 | -8.76 | 210 |
| 20 | Trend pullback · 1h | trend | 93.47 | -6.54 | 96 | 22.9 | -21.94 | -7.00 | -22.19 | 116 |
| 21 | Opening range 30m | breakout | 93.19 | -6.81 | 272 | 34.2 | -10.11 | -3.04 | -17.21 | 591 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 49 | 16.3 | -15.29 | -3.37 | -17.32 | 98 |
| 23 | Copy: Insider buying | copy | 92.86 | -7.14 | 27 | 37.0 | -19.11 | -3.70 | -22.94 | 63 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 91.83 | -8.18 | 0 | — | -1.39 | -0.06 | -14.57 | 1 |
| 25 | Parabolic SAR · 1h | trend | 91.61 | -8.39 | 121 | 25.6 | -20.78 | -5.18 | -23.02 | 247 |
| 26 | Daily: Momentum burst | daily | 91.37 | -8.63 | 13 | 15.4 | -17.94 | -3.46 | -19.44 | 39 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.97 | -2.10 | -16.91 | 1 |
| 28 | Daily: Bullish score | daily | 91.21 | -8.79 | 11 | 18.2 | -5.28 | -0.58 | -14.40 | 14 |
| 29 | ADX DI cross · 1h | trend | 91.19 | -8.81 | 119 | 18.5 | -11.96 | -2.59 | -14.45 | 273 |
| 30 | Squeeze breakout · 1h | breakout | 91.08 | -8.92 | 52 | 23.1 | -4.87 | -1.24 | -12.00 | 92 |
| 31 | Max aggression: 5-day momentum | meta | 90.57 | -9.43 | 12 | 41.7 | -14.86 | -1.34 | -27.23 | 25 |
| 32 | Agent | meta | 89.97 | -10.03 | 112 | 38.4 | -11.12 | -7.03 | -12.47 | 221 |
| 33 | Volume breakout · 1h | breakout | 89.61 | -10.38 | 105 | 23.8 | -12.51 | -2.59 | -15.94 | 109 |
| 34 | Bollinger breakout · 1h | breakout | 88.28 | -11.72 | 109 | 26.6 | -13.36 | -2.66 | -18.15 | 247 |
| 35 | Agent (aggressive) | meta | 88.11 | -11.89 | 56 | 35.7 | -11.20 | -3.69 | -14.77 | 99 |
| 36 | Stochastic reversion · 1h | reversion | 87.93 | -12.07 | 203 | 47.3 | -21.38 | -3.98 | -22.74 | 393 |
| 37 | Opening range 15m | breakout | 86.69 | -13.31 | 338 | 30.8 | -13.86 | -3.88 | -17.87 | 717 |
| 38 | Z-score reversion · 1h | reversion | 86.39 | -13.61 | 124 | 36.3 | -13.04 | -2.08 | -21.48 | 211 |
| 39 | Keltner breakout · 1h | breakout | 86.28 | -13.72 | 74 | 23.0 | -19.62 | -3.84 | -23.13 | 183 |
| 40 | Supertrend · 1h | trend | 85.32 | -14.68 | 114 | 14.0 | -26.10 | -5.37 | -28.46 | 230 |
| 41 | Connors RSI(2) · 1h | reversion | 85.28 | -14.72 | 176 | 40.9 | -26.33 | -7.88 | -27.00 | 199 |
| 42 | RSI momentum · 1h | momentum | 84.67 | -15.33 | 104 | 15.4 | -21.49 | -4.39 | -24.07 | 209 |
| 43 | EMA 20/50 cross · 1h | trend | 84.01 | -15.99 | 73 | 11.0 | -22.52 | -4.47 | -24.31 | 130 |
| 44 | MACD cross · 1h | trend | 83.99 | -16.01 | 244 | 22.1 | -28.67 | -5.80 | -30.37 | 480 |
| 45 | Ichimoku · 1h | trend | 83.34 | -16.66 | 68 | 11.8 | -20.59 | -4.27 | -24.73 | 109 |
| 46 | MFI reversion · 1h | reversion | 83.31 | -16.69 | 270 | 32.2 | -16.25 | -2.51 | -20.70 | 153 |
| 47 | Triple EMA stack · 1h | trend | 83.03 | -16.97 | 101 | 14.9 | -28.04 | -5.40 | -30.72 | 205 |
| 48 | CCI reversion · 1h | reversion | 82.07 | -17.93 | 229 | 45.4 | -23.65 | -3.37 | -28.08 | 465 |
| 49 | Williams %R · 1h | reversion | 81.71 | -18.29 | 231 | 46.8 | -35.28 | -5.98 | -35.98 | 537 |
| 50 | Donchian 20/10 · 1h | breakout | 81.32 | -18.68 | 99 | 20.2 | -24.63 | -4.75 | -26.89 | 218 |
| 51 | Bollinger reversion · 1h | reversion | 80.88 | -19.12 | 182 | 37.4 | -28.44 | -5.71 | -30.40 | 365 |
| 52 | MACD zero-line · 1h | trend | 80.86 | -19.14 | 111 | 15.3 | -23.76 | -5.05 | -25.41 | 226 |
| 53 | Agent (ML meta-label) | meta | 80.39 | -19.61 | 953 | 20.7 | -9.48 | -1.83 | -16.49 | 352 |
| 54 | OBV trend · 1h | momentum | 79.93 | -20.07 | 209 | 17.7 | -31.14 | -6.62 | -32.77 | 296 |
| 55 | RSI(14) reversion · 1h | reversion | 79.76 | -20.24 | 106 | 26.4 | -16.02 | -2.98 | -24.48 | 187 |
| 56 | ROC + volume · 1h | momentum | 78.60 | -21.40 | 259 | 25.9 | -31.83 | -6.24 | -33.70 | 383 |
| 57 | Heikin-Ashi · 1h | trend | 77.70 | -22.30 | 295 | 22.7 | -44.16 | -9.93 | -45.12 | 660 |
| 58 | Three white soldiers | momentum | 77.66 | -22.34 | 315 | 19.0 | -44.40 | -20.24 | -44.89 | 605 |
| 59 | Candlestick reversal · 1h | reversion | 77.16 | -22.84 | 280 | 29.3 | -34.68 | -6.80 | -35.39 | 553 |
| 60 | VWAP momentum · 1h | momentum | 76.52 | -23.48 | 567 | 21.9 | -49.09 | -10.53 | -51.11 | 1247 |
| 61 | EMA 9/21 cross · 1h | trend | 76.32 | -23.68 | 176 | 10.8 | -30.89 | -6.70 | -32.50 | 337 |
| 62 | Max aggression: 1-day momentum | meta | 70.28 | -29.72 | 20 | 30.0 | -39.52 | -2.66 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.23 | -45.77 | 783 | 22.3 | -74.53 | -26.51 | -75.07 | 1593 |
| 64 | Volume breakout | breakout | 52.90 | -47.10 | 471 | 12.5 | -63.11 | -26.28 | -63.36 | 812 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -41.99 | -98.87 | 5172 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.29 | -23.20 | -80.00 | 1417 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -42.69 | -93.77 | 2526 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.22 | -30.24 | -89.36 | 1922 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -35.67 | -91.54 | 2345 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.41 | -31.78 | -90.49 | 2169 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -48.66 | -97.89 | 3525 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.11 | -51.59 | -96.23 | 3381 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -35.49 | -94.06 | 2451 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.06 | -31.55 | -82.63 | 1700 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -51.47 | -99.42 | 5760 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -40.87 | -92.92 | 2648 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -38.18 | -95.41 | 3364 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -70.41 | -99.78 | 6173 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.27 | -44.08 | -92.35 | 2324 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -58.69 | -97.78 | 3583 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.92 | -98.67 | 4791 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.95 | -28.76 | -68.59 | 1192 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -53.96 | -94.63 | 2788 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.44 | -38.73 | -84.57 | 1838 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.32 | -99.61 | 6303 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.32 | -28.91 | -88.35 | 2235 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.61 | -18.88 | -76.95 | 1684 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.55 | -36.56 | -90.62 | 2279 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.27 | -47.13 | -96.29 | 3821 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.02 | -49.31 | -90.06 | 2131 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.16 | -23.21 | -73.09 | 1294 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.10 | -17.81 | -76.40 | 1586 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.35 | -96.55 | 4190 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.40 | -99.92 | 8309 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T15:35 | Agent (ML meta-label) | buy | SOXL | 4.07 | — | rebalance up |
| 2026-10-27T15:35 | Agent (ML meta-label) | buy | NVDA | 4.02 | — | rebalance up |
| 2026-10-27T15:35 | Agent (ML meta-label) | buy | AMD | 6.67 | — | rebalance up |
| 2026-10-27T15:35 | Agent (ML meta-label) | sell | META | 5.34 | -0.01 | selected signal exited |
| 2026-10-27T15:35 | Agent (ML meta-label) | sell | GOOGL | 13.42 | -0.01 | selected signal exited |
| 2026-10-27T15:35 | CCI reversion · 1h | buy | GOOGL | 4.75 | — | rebalance up |
| 2026-10-27T15:35 | CCI reversion · 1h | buy | ETHU | 4.65 | — | rebalance up |
| 2026-10-27T15:35 | CCI reversion · 1h | buy | BITX | 6.17 | — | rebalance up |
| 2026-10-27T15:35 | CCI reversion · 1h | sell | LABU | 12.07 | 0.55 | target is flat |
| 2026-10-27T15:35 | Stochastic reversion · 1h | buy | MSTR | 4.42 | — | rebalance up |
| 2026-10-27T15:35 | OBV trend · 1h | buy | LABU | 11.39 | — | entry |
| 2026-10-27T15:35 | OBV trend · 1h | buy | AAPL | 11.42 | — | entry |
| 2026-10-27T15:35 | OBV trend · 1h | sell | XRP-USD | 4.53 | 0.00 | rebalance down |
| 2026-10-27T15:35 | OBV trend · 1h | sell | TSLA | 4.63 | 0.04 | rebalance down |
| 2026-10-27T15:35 | OBV trend · 1h | sell | TNA | 4.73 | 0.06 | rebalance down |
| 2026-10-27T15:35 | OBV trend · 1h | sell | IWM | 4.57 | 0.06 | rebalance down |
| 2026-10-27T15:35 | OBV trend · 1h | sell | DOGE-USD | 4.35 | -0.02 | rebalance down |
| 2026-10-27T15:35 | Ichimoku · 1h | buy | LABU | 12.37 | — | entry |
| 2026-10-27T15:35 | Ichimoku · 1h | sell | TNA | 4.34 | 0.06 | rebalance down |
| 2026-10-27T15:35 | Ichimoku · 1h | sell | IWM | 4.18 | 0.02 | rebalance down |
| 2026-10-27T15:35 | Supertrend · 1h | buy | IWM | 3.49 | — | entry |
| 2026-10-27T15:35 | Supertrend · 1h | buy | DOGE-USD | 5.33 | — | entry |
| 2026-10-27T15:35 | Supertrend · 1h | sell | SOXL | 4.48 | 0.27 | rebalance down |
| 2026-10-27T15:35 | Supertrend · 1h | sell | AMD | 4.34 | 0.20 | rebalance down |
| 2026-10-27T15:35 | Triple EMA stack · 1h | buy | LABU | 11.06 | — | entry |
| 2026-10-27T15:35 | Triple EMA stack · 1h | buy | AAPL | 7.77 | — | rebalance up |
| 2026-10-27T15:35 | Triple EMA stack · 1h | sell | XRP-USD | 6.83 | 0.09 | rebalance down |
| 2026-10-27T15:35 | Triple EMA stack · 1h | sell | TSLA | 5.39 | 0.12 | rebalance down |
| 2026-10-27T15:35 | Triple EMA stack · 1h | sell | PLTR | 6.60 | 0.01 | rebalance down |
| 2026-10-27T15:35 | EMA 20/50 cross · 1h | buy | LABU | 12.31 | — | entry |
| 2026-10-27T15:35 | EMA 20/50 cross · 1h | sell | XRP-USD | 4.58 | 0.05 | rebalance down |
| 2026-10-27T15:35 | EMA 20/50 cross · 1h | sell | PLTR | 4.34 | 0.01 | rebalance down |
| 2026-10-27T15:35 | EMA 9/21 cross · 1h | buy | LABU | 3.87 | — | entry |
| 2026-10-27T15:35 | EMA 9/21 cross · 1h | sell | AMD | 3.87 | 0.17 | rebalance down |
| 2026-10-27T15:35 | Volume breakout | buy | XRP-USD | 3.03 | — | rebalance up |
| 2026-10-27T15:35 | Volume breakout | buy | TSLA | 3.01 | — | rebalance up |
| 2026-10-27T15:35 | Volume breakout | buy | SPY | 3.00 | — | rebalance up |
| 2026-10-27T15:35 | Volume breakout | buy | ETH-USD | 3.04 | — | rebalance up |
| 2026-10-27T15:35 | Volume breakout | buy | DOGE-USD | 3.03 | — | rebalance up |
| 2026-10-27T15:35 | Volume breakout | sell | BTC-USD | 7.53 | -0.06 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 15:35:05.000154+00:00 -> 2026-10-27 15:45:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
