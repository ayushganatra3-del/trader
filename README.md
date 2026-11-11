# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T19:20:05.000130+00:00 · 56111 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 32703 decisions in 2919 calls, $0.4067 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T19:20 | 2 / 9 / 19 | cash |  |
| Breezy | 2026-11-11T19:20 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-11T19:20 | 4 / 22 / 4 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| MFI reversion | LABU | 1.66 | +5.37% | 3 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.23 | 16.23 | 20 | 70.0 | 17.73 | 3.56 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.31 | 15.31 | 0 | — | 14.68 | 4.86 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.64 | 3.64 | 31 | 45.2 | 3.73 | 0.98 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.62 | 3.62 | 0 | — | 6.07 | 1.68 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 5.70 | 1.61 | -9.06 | 240 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.78 | -0.21 | 133 | 34.6 | 10.40 | 3.58 | -3.22 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.56 | -1.44 | 0 | — | -0.74 | -0.18 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.29 | -1.71 | 187 | 30.5 | -2.42 | -0.85 | -9.46 | 160 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.16 | -3.84 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.66 | -5.34 | 0 | — | -3.31 | -0.83 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.12 | -5.88 | 43 | 39.5 | -7.16 | -1.44 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.59 | -3.30 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.60 | -8.40 | 109 | 22.9 | -16.27 | -5.70 | -18.84 | 80 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Max aggression: 5-day momentum | meta | 89.24 | -10.76 | 19 | 47.4 | -26.08 | -1.30 | -45.81 | 25 |
| 23 | Opening range 30m | breakout | 89.19 | -10.81 | 404 | 33.2 | -13.20 | -4.00 | -14.11 | 601 |
| 24 | Squeeze breakout · 1h | breakout | 88.57 | -11.43 | 64 | 21.9 | -7.61 | -2.64 | -14.29 | 74 |
| 25 | Hold BTC | benchmark | 87.13 | -12.87 | 1 | 0.0 | -4.34 | -0.51 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.51 | -13.49 | 168 | 26.8 | -14.17 | -2.98 | -21.98 | 225 |
| 27 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -15.34 | -7.72 | -15.70 | 203 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 84.98 | -15.02 | 2 | 0.0 | -5.55 | -0.53 | -24.16 | 1 |
| 29 | Daily: Bullish score | daily | 84.24 | -15.76 | 16 | 18.8 | -8.91 | -1.33 | -19.56 | 15 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -18.10 | -5.12 | -18.67 | 98 |
| 31 | Donchian 55/20 · 1h | breakout | 83.43 | -16.57 | 72 | 13.9 | -23.35 | -4.84 | -29.15 | 97 |
| 32 | ADX DI cross · 1h | trend | 82.91 | -17.09 | 185 | 18.9 | -19.80 | -3.02 | -30.93 | 267 |
| 33 | Max aggression: 1-day momentum | meta | 82.72 | -17.28 | 27 | 25.9 | -15.97 | -0.31 | -57.50 | 40 |
| 34 | Keltner breakout · 1h | breakout | 82.68 | -17.32 | 110 | 23.6 | -18.04 | -3.65 | -25.32 | 178 |
| 35 | Stochastic reversion · 1h | reversion | 81.95 | -18.05 | 292 | 48.3 | -24.32 | -3.47 | -27.17 | 394 |
| 36 | Volume breakout · 1h | breakout | 81.32 | -18.68 | 148 | 27.7 | -11.99 | -2.68 | -21.11 | 96 |
| 37 | Opening range 15m | breakout | 81.19 | -18.81 | 501 | 31.3 | -18.94 | -5.10 | -21.11 | 730 |
| 38 | Heikin-Ashi · 1h | trend | 80.60 | -19.40 | 417 | 24.5 | -37.10 | -6.86 | -40.59 | 670 |
| 39 | Connors RSI(2) · 1h | reversion | 80.19 | -19.81 | 208 | 39.9 | -20.78 | -6.92 | -21.17 | 123 |
| 40 | MFI reversion · 1h | reversion | 79.56 | -20.44 | 374 | 35.6 | -16.38 | -2.03 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.49 | -21.51 | 362 | 22.1 | -28.27 | -4.37 | -38.69 | 471 |
| 42 | CCI reversion · 1h | reversion | 77.94 | -22.06 | 332 | 45.2 | -27.11 | -4.11 | -31.08 | 450 |
| 43 | Bollinger breakout · 1h | breakout | 77.59 | -22.41 | 171 | 22.8 | -20.33 | -4.14 | -28.24 | 242 |
| 44 | MACD zero-line · 1h | trend | 76.19 | -23.81 | 160 | 16.9 | -20.82 | -4.01 | -31.12 | 211 |
| 45 | Bollinger reversion · 1h | reversion | 75.72 | -24.28 | 286 | 41.6 | -26.02 | -3.90 | -33.10 | 368 |
| 46 | Supertrend · 1h | trend | 75.53 | -24.47 | 168 | 13.1 | -29.75 | -5.16 | -36.25 | 225 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 48 | Daily: Momentum burst | daily | 75.27 | -24.73 | 27 | 11.1 | -31.68 | -4.10 | -38.23 | 33 |
| 49 | RSI momentum · 1h | momentum | 75.26 | -24.74 | 159 | 12.6 | -25.70 | -3.88 | -37.22 | 216 |
| 50 | EMA 20/50 cross · 1h | trend | 74.75 | -25.25 | 103 | 10.7 | -26.36 | -4.38 | -36.88 | 115 |
| 51 | Triple EMA stack · 1h | trend | 74.30 | -25.70 | 144 | 14.6 | -25.27 | -4.08 | -35.77 | 211 |
| 52 | ROC + volume · 1h | momentum | 73.43 | -26.57 | 376 | 27.7 | -32.93 | -5.86 | -38.60 | 384 |
| 53 | Donchian 20/10 · 1h | breakout | 72.56 | -27.43 | 142 | 19.7 | -28.10 | -5.05 | -35.62 | 211 |
| 54 | Williams %R · 1h | reversion | 72.25 | -27.75 | 353 | 46.2 | -35.97 | -5.57 | -37.03 | 528 |
| 55 | OBV trend · 1h | momentum | 71.93 | -28.07 | 279 | 18.6 | -26.09 | -4.61 | -35.28 | 286 |
| 56 | Z-score reversion · 1h | reversion | 71.32 | -28.68 | 197 | 38.6 | -22.90 | -3.12 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 68.77 | -31.23 | 175 | 32.6 | -25.51 | -3.59 | -32.54 | 229 |
| 58 | VWAP momentum · 1h | momentum | 68.35 | -31.65 | 857 | 22.6 | -52.62 | -10.91 | -54.66 | 1237 |
| 59 | EMA 9/21 cross · 1h | trend | 67.55 | -32.45 | 253 | 9.9 | -33.96 | -6.30 | -41.69 | 337 |
| 60 | Agent (ML meta-label) | meta | 66.80 | -33.20 | 1742 | 24.9 | -11.35 | -1.64 | -19.88 | 347 |
| 61 | Candlestick reversal · 1h | reversion | 65.10 | -34.90 | 460 | 28.9 | -37.92 | -6.93 | -40.36 | 577 |
| 62 | Three white soldiers | momentum | 60.35 | -39.65 | 519 | 14.8 | -49.18 | -22.19 | -49.37 | 657 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -44.28 | -99.04 | 5296 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.05 | -25.68 | -80.50 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -43.71 | -93.62 | 2529 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.37 | -31.32 | -89.51 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.09 | -39.17 | -91.31 | 2340 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.42 | -32.21 | -90.53 | 2214 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -51.29 | -97.80 | 3450 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -55.31 | -96.45 | 3442 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.43 | -32.16 | -93.43 | 2346 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.17 | -33.70 | -83.50 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -52.38 | -99.54 | 5940 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.14 | -41.29 | -92.35 | 2616 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -37.44 | -95.55 | 3461 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.52 | -99.80 | 6133 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.91 | -41.40 | -91.95 | 2265 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.24 | -23.77 | -75.59 | 1627 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -58.04 | -97.72 | 3535 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -60.44 | -98.84 | 4874 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.28 | -26.23 | -68.77 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -51.44 | -94.76 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.89 | -36.96 | -85.35 | 1799 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -71.47 | -99.64 | 6312 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.40 | -31.47 | -89.41 | 2282 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.46 | -19.52 | -77.62 | 1737 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -35.63 | -90.64 | 2163 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.72 | -50.97 | -96.72 | 3829 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.10 | -53.61 | -89.12 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.62 | -28.27 | -66.37 | 832 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.30 | -22.53 | -72.14 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.34 | -18.40 | -78.60 | 1685 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.20 | -48.17 | -97.20 | 4276 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -94.36 | -99.93 | 8362 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T19:20 | Agent (ML meta-label) | buy | TECL | 3.41 | — | rebalance up |
| 2026-11-11T19:20 | Agent (ML meta-label) | buy | AMD | 5.59 | — | rebalance up |
| 2026-11-11T19:20 | Agent (ML meta-label) | sell | TSLA | 10.03 | -0.03 | selected signal exited |
| 2026-11-11T19:20 | Agent (ML meta-label) | sell | TQQQ | 5.54 | -0.03 | selected signal exited |
| 2026-11-11T19:15 | Agent (ML meta-label) | buy | TQQQ | 5.57 | — | entry |
| 2026-11-11T19:15 | Agent (ML meta-label) | sell | AMD | 5.57 | -0.03 | rebalance down |
| 2026-11-11T19:15 | MFI reversion · 1h | sell | SQQQ | 20.04 | 0.09 | target is flat |
| 2026-11-11T19:10 | Agent (rotation) | sell | UPRO | 4.13 | 0.03 | selected signal exited |
| 2026-11-11T19:10 | Agent (rotation) | sell | NVDA | 6.55 | 0.04 | selected signal exited |
| 2026-11-11T19:10 | Agent (rotation) | sell | AMD | 8.41 | 0.26 | selected signal exited |
| 2026-11-11T19:10 | Agent (ML meta-label) | buy | TSLA | 10.06 | — | entry |
| 2026-11-11T19:10 | Agent (ML meta-label) | sell | AAPL | 3.39 | -0.01 | rebalance down |
| 2026-11-11T19:10 | Agent (aggressive) | sell | SQQQ | 41.85 | 0.33 | selected signal exited |
| 2026-11-11T19:10 | Agent (aggressive) | sell | COIN | 41.44 | -0.43 | selected signal exited |
| 2026-11-11T19:10 | Agent | sell | UPRO | 17.09 | -0.09 | selected signal exited |
| 2026-11-11T19:10 | Agent | sell | SQQQ | 34.66 | 0.18 | selected signal exited |
| 2026-11-11T19:10 | Agent | sell | COIN | 17.40 | 0.06 | selected signal exited |
| 2026-11-11T19:10 | Volume breakout · 1h | buy | TQQQ | 9.47 | — | entry |
| 2026-11-11T19:10 | Volume breakout · 1h | sell | SOXL | 4.61 | 0.19 | rebalance down |
| 2026-11-11T19:10 | Volume breakout · 1h | sell | AMD | 4.85 | 0.15 | rebalance down |
| 2026-11-11T19:10 | Gap and go | sell | UPRO | 25.05 | 0.03 | stop-loss |
| 2026-11-11T19:10 | Gap and go | sell | NVDA | 25.10 | 0.05 | stop-loss |
| 2026-11-11T19:10 | Gap and go | sell | AMD | 25.05 | 0.40 | stop-loss |
| 2026-11-11T19:05 | Agent (rotation) | sell | TECL | 6.68 | 0.17 | selected signal exited |
| 2026-11-11T19:05 | Agent (rotation) | sell | SOXL | 8.56 | 0.41 | selected signal exited |
| 2026-11-11T19:05 | Agent (rotation) | sell | QQQ | 4.68 | 0.03 | selected signal exited |
| 2026-11-11T19:05 | Agent (ML meta-label) | buy | AMD | 3.38 | — | rebalance up |
| 2026-11-11T19:05 | Agent (ML meta-label) | buy | AAPL | 5.58 | — | rebalance up |
| 2026-11-11T19:05 | Agent (ML meta-label) | sell | TSLA | 10.06 | -0.02 | selected signal exited |
| 2026-11-11T19:05 | Agent (ML meta-label) | sell | QQQ | 5.58 | -0.01 | selected signal exited |
| 2026-11-11T19:05 | Agent | buy | UPRO | 17.18 | — | following Gap and go |
| 2026-11-11T19:05 | MFI reversion · 1h | buy | SQQQ | 19.95 | — | entry |
| 2026-11-11T19:05 | Gap and go | buy | UPRO | 10.82 | — | rebalance up |
| 2026-11-11T19:05 | Gap and go | buy | NVDA | 10.92 | — | rebalance up |
| 2026-11-11T19:05 | Gap and go | buy | AMD | 10.57 | — | rebalance up |
| 2026-11-11T19:05 | Gap and go | sell | TQQQ | 14.36 | 0.26 | stop-loss |
| 2026-11-11T19:05 | Gap and go | sell | TECL | 10.13 | 0.25 | stop-loss |
| 2026-11-11T19:05 | Gap and go | sell | SOXL | 14.75 | 0.71 | stop-loss |
| 2026-11-11T19:05 | Gap and go | sell | QQQ | 14.17 | 0.08 | stop-loss |
| 2026-11-11T19:00 | Agent (ML meta-label) | buy | QQQ | 5.59 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 19:20:05.000130+00:00 -> 2026-11-11 19:30:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
