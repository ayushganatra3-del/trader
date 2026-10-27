# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T14:35:05.000122+00:00 · 37965 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 111, win rate 38.7%, fees £3.41, max drawdown -11.45%.

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

Today: 14785 decisions in 2168 calls, $0.1957 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T14:35 | 2 / 23 / 5 | LABU 15% |  |
| Breezy | 2026-10-27T14:35 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-27T14:35 | 5 / 23 / 2 | ETHU 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.30 | +6.55% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |
| Candlestick reversal | LABU | 1.85 | +4.39% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.24 | 7.24 | 0 | — | 7.64 | 3.77 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.29 | 1.09 | -6.62 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.57 | 2.14 | -4.92 | 25 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.60 | 0.60 | 0 | — | 2.60 | 1.22 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.18 | -3.64 | -14.11 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.21 | -0.79 | 0 | — | 0.21 | 0.17 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 97.74 | -2.26 | 80 | 33.8 | 6.50 | 3.12 | -1.80 | 98 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.98 | -1.88 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 97.05 | -2.95 | 0 | — | -0.10 | 0.03 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.09 | -3.91 | 122 | 31.1 | -2.29 | -1.23 | -6.39 | 183 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 5.25 | 1.22 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.19 | -2.64 | -4.59 | 27 |
| 17 | Hold BTC | benchmark | 95.28 | -4.72 | 0 | — | 2.50 | 0.58 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.04 | -4.96 | 0 | — | -6.71 | -2.80 | -7.83 | 1 |
| 19 | Gap and go | momentum | 94.03 | -5.97 | 110 | 24.5 | 3.98 | 1.32 | -8.76 | 210 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Copy: Insider buying | copy | 93.44 | -6.56 | 27 | 37.0 | -19.63 | -3.84 | -22.94 | 63 |
| 22 | Donchian 55/20 · 1h | breakout | 92.66 | -7.34 | 49 | 16.3 | -15.11 | -3.36 | -16.70 | 98 |
| 23 | Opening range 30m | breakout | 92.32 | -7.68 | 272 | 34.2 | -11.08 | -3.38 | -17.21 | 579 |
| 24 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.74 | -2.04 | -16.91 | 1 |
| 25 | Daily: Momentum burst | daily | 91.17 | -8.83 | 13 | 15.4 | -18.65 | -3.63 | -19.44 | 39 |
| 26 | Squeeze breakout · 1h | breakout | 91.03 | -8.97 | 52 | 23.1 | -4.93 | -1.26 | -12.00 | 91 |
| 27 | Parabolic SAR · 1h | trend | 90.98 | -9.02 | 121 | 25.6 | -21.45 | -5.41 | -23.02 | 248 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 90.81 | -9.19 | 0 | — | -2.52 | -0.26 | -14.57 | 1 |
| 29 | Daily: Bullish score | daily | 90.79 | -9.21 | 11 | 18.2 | -6.08 | -0.71 | -14.40 | 14 |
| 30 | ADX DI cross · 1h | trend | 90.72 | -9.28 | 117 | 18.8 | -12.34 | -2.70 | -14.45 | 271 |
| 31 | Agent | meta | 89.98 | -10.02 | 111 | 38.7 | -10.51 | -6.62 | -12.47 | 216 |
| 32 | Max aggression: 5-day momentum | meta | 89.95 | -10.05 | 12 | 41.7 | -15.46 | -1.41 | -27.23 | 25 |
| 33 | Volume breakout · 1h | breakout | 89.23 | -10.77 | 105 | 23.8 | -13.46 | -2.81 | -15.93 | 109 |
| 34 | Stochastic reversion · 1h | reversion | 88.09 | -11.91 | 202 | 47.0 | -21.72 | -4.01 | -23.17 | 393 |
| 35 | Agent (aggressive) | meta | 88.08 | -11.92 | 55 | 36.4 | -11.23 | -3.70 | -14.77 | 97 |
| 36 | Bollinger breakout · 1h | breakout | 88.00 | -12.00 | 109 | 26.6 | -14.29 | -2.86 | -18.15 | 241 |
| 37 | Keltner breakout · 1h | breakout | 86.21 | -13.79 | 74 | 23.0 | -21.99 | -4.50 | -23.13 | 183 |
| 38 | Z-score reversion · 1h | reversion | 86.11 | -13.89 | 123 | 35.8 | -13.30 | -2.13 | -21.48 | 211 |
| 39 | Opening range 15m | breakout | 85.89 | -14.12 | 338 | 30.8 | -14.79 | -4.19 | -17.87 | 705 |
| 40 | Connors RSI(2) · 1h | reversion | 85.11 | -14.89 | 175 | 40.6 | -26.47 | -7.95 | -27.00 | 198 |
| 41 | Supertrend · 1h | trend | 84.80 | -15.20 | 114 | 14.0 | -26.00 | -5.45 | -28.00 | 223 |
| 42 | RSI momentum · 1h | momentum | 84.16 | -15.84 | 104 | 15.4 | -22.16 | -4.54 | -24.36 | 203 |
| 43 | EMA 20/50 cross · 1h | trend | 84.07 | -15.93 | 73 | 11.0 | -21.85 | -4.30 | -23.61 | 129 |
| 44 | MACD cross · 1h | trend | 83.64 | -16.36 | 244 | 22.1 | -30.47 | -6.30 | -31.77 | 479 |
| 45 | MFI reversion · 1h | reversion | 83.21 | -16.79 | 267 | 31.8 | -16.43 | -2.54 | -20.70 | 153 |
| 46 | Ichimoku · 1h | trend | 82.83 | -17.17 | 68 | 11.8 | -21.11 | -4.43 | -24.73 | 108 |
| 47 | Triple EMA stack · 1h | trend | 82.57 | -17.43 | 101 | 14.9 | -30.79 | -5.80 | -32.84 | 194 |
| 48 | CCI reversion · 1h | reversion | 81.71 | -18.29 | 226 | 45.1 | -24.77 | -3.54 | -28.08 | 466 |
| 49 | Williams %R · 1h | reversion | 81.67 | -18.33 | 231 | 46.8 | -36.03 | -6.20 | -36.63 | 537 |
| 50 | Bollinger reversion · 1h | reversion | 80.99 | -19.01 | 182 | 37.4 | -28.44 | -5.70 | -30.40 | 365 |
| 51 | Donchian 20/10 · 1h | breakout | 80.79 | -19.21 | 99 | 20.2 | -25.01 | -4.87 | -26.79 | 215 |
| 52 | MACD zero-line · 1h | trend | 80.61 | -19.39 | 111 | 15.3 | -23.42 | -4.94 | -24.87 | 220 |
| 53 | Agent (ML meta-label) | meta | 80.33 | -19.66 | 936 | 20.1 | -12.42 | -2.56 | -16.29 | 360 |
| 54 | OBV trend · 1h | momentum | 79.61 | -20.39 | 209 | 17.7 | -31.33 | -6.72 | -32.70 | 292 |
| 55 | RSI(14) reversion · 1h | reversion | 79.55 | -20.45 | 106 | 26.4 | -13.32 | -2.25 | -24.48 | 200 |
| 56 | ROC + volume · 1h | momentum | 77.96 | -22.04 | 258 | 25.6 | -31.32 | -6.08 | -33.46 | 380 |
| 57 | Three white soldiers | momentum | 77.73 | -22.27 | 311 | 19.0 | -44.35 | -20.37 | -44.79 | 606 |
| 58 | Heikin-Ashi · 1h | trend | 77.51 | -22.49 | 295 | 22.7 | -43.99 | -9.98 | -44.76 | 657 |
| 59 | Candlestick reversal · 1h | reversion | 77.09 | -22.91 | 278 | 28.8 | -33.58 | -6.34 | -34.21 | 566 |
| 60 | VWAP momentum · 1h | momentum | 76.08 | -23.92 | 566 | 21.7 | -48.93 | -10.69 | -50.64 | 1245 |
| 61 | EMA 9/21 cross · 1h | trend | 75.99 | -24.01 | 176 | 10.8 | -31.93 | -6.87 | -33.18 | 335 |
| 62 | Max aggression: 1-day momentum | meta | 69.41 | -30.59 | 20 | 30.0 | -40.28 | -2.75 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.34 | -45.66 | 777 | 22.1 | -74.58 | -26.57 | -75.02 | 1586 |
| 64 | Volume breakout | breakout | 53.15 | -46.85 | 468 | 12.6 | -63.25 | -26.68 | -63.51 | 810 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.86 | -42.18 | -98.88 | 5184 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.40 | -23.31 | -79.99 | 1415 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -43.61 | -93.76 | 2542 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.17 | -30.02 | -89.36 | 1922 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.35 | -36.24 | -91.53 | 2355 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.40 | -31.84 | -90.49 | 2174 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.84 | -49.09 | -97.89 | 3529 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -52.71 | -96.21 | 3392 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -35.90 | -94.04 | 2437 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.21 | -32.20 | -82.63 | 1692 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -51.99 | -99.42 | 5771 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -40.78 | -92.92 | 2636 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -38.15 | -95.42 | 3367 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.41 | -99.78 | 6163 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -44.24 | -92.35 | 2335 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.71 | -97.78 | 3592 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.87 | -98.67 | 4810 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.07 | -28.91 | -68.59 | 1191 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -54.33 | -94.64 | 2781 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.55 | -39.00 | -84.61 | 1825 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.40 | -99.61 | 6307 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.33 | -28.96 | -88.35 | 2236 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.67 | -18.93 | -77.07 | 1686 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.52 | -36.52 | -90.59 | 2278 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.27 | -47.17 | -96.29 | 3827 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.99 | -48.83 | -90.05 | 2132 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.47 | -23.64 | -73.09 | 1284 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.17 | -17.87 | -76.45 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.35 | -96.55 | 4204 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.19 | -99.92 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T14:35 | Agent (ML meta-label) | buy | TSLA | 16.07 | — | following Z-score reversion |
| 2026-10-27T14:35 | Agent (ML meta-label) | sell | IWM | 16.04 | 0.00 | selected signal exited |
| 2026-10-27T14:35 | MACD zero-line · 1h | buy | NVDA | 4.04 | — | rebalance up |
| 2026-10-27T14:35 | MACD zero-line · 1h | sell | PLTR | 4.04 | 0.00 | rebalance down |
| 2026-10-27T14:35 | Three white soldiers | buy | BITX | 19.43 | — | entry signal |
| 2026-10-27T14:35 | Opening range 30m | buy | TNA | 23.09 | — | entry signal |
| 2026-10-27T14:35 | Opening range 30m | buy | LABU | 23.09 | — | entry signal |
| 2026-10-27T14:35 | Opening range 30m | buy | BITX | 23.09 | — | entry signal |
| 2026-10-27T14:35 | Opening range 30m | buy | AAPL | 23.09 | — | entry signal |
| 2026-10-27T14:35 | Opening range 15m | buy | TNA | 21.47 | — | entry signal |
| 2026-10-27T14:35 | Opening range 15m | buy | LABU | 21.48 | — | entry signal |
| 2026-10-27T14:35 | Opening range 15m | buy | BITX | 21.48 | — | entry signal |
| 2026-10-27T14:35 | Opening range 15m | buy | AAPL | 21.48 | — | entry signal |
| 2026-10-27T14:35 | Opening range 15m | sell | SQQQ | 21.26 | -0.30 | stop-loss |
| 2026-10-27T14:35 | Gap and go | buy | TQQQ | 12.32 | — | entry signal |
| 2026-10-27T14:35 | Gap and go | buy | TNA | 15.68 | — | entry signal |
| 2026-10-27T14:35 | Gap and go | buy | TECL | 15.68 | — | entry signal |
| 2026-10-27T14:35 | Gap and go | sell | SOXL | 7.98 | 0.08 | rebalance down |
| 2026-10-27T14:35 | Gap and go | sell | AMD | 7.93 | 0.07 | rebalance down |
| 2026-10-27T14:35 | ROC + volume | buy | AMD | 2.73 | — | rebalance up |
| 2026-10-27T14:35 | ROC + volume | sell | LABU | 8.21 | 0.06 | target is flat |
| 2026-10-27T14:30 | Agent (ML meta-label) | buy | SOXL | 16.04 | — | entry |
| 2026-10-27T14:30 | Agent (ML meta-label) | buy | NVDA | 9.33 | — | rebalance up |
| 2026-10-27T14:30 | Agent (ML meta-label) | buy | IWM | 16.04 | — | entry |
| 2026-10-27T14:30 | Agent (ML meta-label) | sell | TQQQ | 16.02 | 0.12 | selected signal exited |
| 2026-10-27T14:30 | Agent (ML meta-label) | sell | QQQ | 12.05 | 0.01 | selected signal exited |
| 2026-10-27T14:30 | Agent (ML meta-label) | sell | AMD | 16.01 | 0.32 | selected signal exited |
| 2026-10-27T14:30 | MFI reversion · 1h | buy | GOOGL | 13.86 | — | entry signal |
| 2026-10-27T14:30 | MFI reversion · 1h | sell | LABU | 10.51 | 0.36 | exit signal |
| 2026-10-27T14:30 | CCI reversion · 1h | buy | LABU | 5.28 | — | rebalance up |
| 2026-10-27T14:30 | CCI reversion · 1h | buy | GOOGL | 5.35 | — | rebalance up |
| 2026-10-27T14:30 | CCI reversion · 1h | buy | ETHU | 11.64 | — | entry signal |
| 2026-10-27T14:30 | CCI reversion · 1h | sell | UPRO | 10.18 | 0.11 | exit signal |
| 2026-10-27T14:30 | CCI reversion · 1h | sell | SPY | 10.15 | 0.06 | exit signal |
| 2026-10-27T14:30 | Williams %R · 1h | buy | MSTR | 13.59 | — | entry signal |
| 2026-10-27T14:30 | Williams %R · 1h | sell | LABU | 10.24 | 0.26 | exit signal |
| 2026-10-27T14:30 | Williams %R · 1h | sell | AMZN | 10.20 | 0.01 | exit signal |
| 2026-10-27T14:30 | Stochastic reversion · 1h | buy | MSTR | 17.62 | — | entry signal |
| 2026-10-27T14:30 | Stochastic reversion · 1h | buy | META | 17.62 | — | entry signal |
| 2026-10-27T14:30 | Stochastic reversion · 1h | sell | LABU | 17.80 | 0.22 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 14:35:05.000122+00:00 -> 2026-10-27 14:45:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
