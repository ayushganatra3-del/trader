# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T14:16:05.000154+00:00 · 41461 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.53 (-8.47%)

Closed trades 123, win rate 39.8%, fees £3.65, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 18.30 | -0.01 |
| TSLA | 18.34 | +0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-29)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.18 · VIX 17.20 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, IWM 5.9, LABU 5.7, AAPL 5.2, SQQQ 4.9, PLTR 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 12696 decisions in 2055 calls, $0.1710 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T14:16 | 0 / 12 / 19 | cash |  |
| Breezy | 2026-10-30T14:16 | 0 / 24 / 7 | cash |  |
| Boozy | 2026-10-30T14:16 | 4 / 23 / 4 | COIN 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.81 | 6.81 | 0 | — | 8.15 | 3.96 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.78 | 2.21 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.96 | -0.04 | 0 | — | 3.33 | 1.45 | -5.02 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.59 | -2.42 | 95 | 35.8 | 6.14 | 2.87 | -2.08 | 94 |
| 10 | Hold SPY | benchmark | 97.45 | -2.55 | 0 | — | -0.97 | -0.48 | -3.00 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 96.68 | -3.32 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 15 | Agent (rotation) | meta | 95.63 | -4.37 | 128 | 31.2 | -2.69 | -1.76 | -7.82 | 164 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.21 | -4.79 | 0 | — | -2.26 | -0.89 | -5.99 | 1 |
| 17 | Gap and go | momentum | 95.05 | -4.95 | 123 | 29.3 | 4.70 | 1.55 | -8.76 | 203 |
| 18 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 19 | Copy: Insider buying | copy | 92.65 | -7.35 | 33 | 36.4 | -21.73 | -4.42 | -23.91 | 69 |
| 20 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.11 | -7.43 | -21.17 | 98 |
| 21 | Opening range 30m | breakout | 91.56 | -8.44 | 304 | 35.5 | -11.26 | -3.35 | -17.21 | 582 |
| 22 | Agent | meta | 91.53 | -8.47 | 123 | 39.8 | -9.62 | -5.67 | -12.21 | 221 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 24 | Parabolic SAR · 1h | trend | 90.75 | -9.26 | 138 | 28.3 | -18.65 | -4.32 | -20.27 | 249 |
| 25 | Hold BTC | benchmark | 90.40 | -9.60 | 0 | — | -2.02 | -0.16 | -12.47 | 1 |
| 26 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.41 | -2.03 | -12.70 | 93 |
| 27 | Donchian 55/20 · 1h | breakout | 89.98 | -10.02 | 54 | 14.8 | -16.10 | -3.59 | -17.03 | 102 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 89.31 | -10.69 | 0 | — | -2.30 | -0.20 | -14.57 | 1 |
| 29 | Daily: Bullish score | daily | 88.37 | -11.63 | 14 | 21.4 | -6.92 | -0.86 | -14.73 | 14 |
| 30 | Agent (aggressive) | meta | 87.39 | -12.61 | 62 | 35.5 | -11.12 | -3.67 | -15.04 | 102 |
| 31 | Volume breakout · 1h | breakout | 85.66 | -14.34 | 127 | 29.1 | -13.36 | -2.83 | -16.02 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 84.88 | -15.12 | 221 | 47.5 | -18.27 | -3.15 | -23.72 | 381 |
| 33 | Keltner breakout · 1h | breakout | 84.83 | -15.17 | 86 | 24.4 | -24.75 | -4.90 | -25.54 | 186 |
| 34 | ADX DI cross · 1h | trend | 84.69 | -15.31 | 140 | 19.3 | -17.40 | -3.33 | -20.33 | 261 |
| 35 | Connors RSI(2) · 1h | reversion | 84.40 | -15.60 | 186 | 40.9 | -20.46 | -6.51 | -21.56 | 158 |
| 36 | Opening range 15m | breakout | 83.85 | -16.15 | 378 | 32.0 | -16.45 | -4.71 | -18.44 | 714 |
| 37 | Max aggression: 5-day momentum | meta | 83.53 | -16.47 | 14 | 42.9 | -35.24 | -2.58 | -35.24 | 25 |
| 38 | Bollinger breakout · 1h | breakout | 83.16 | -16.84 | 132 | 26.5 | -16.80 | -3.10 | -21.36 | 244 |
| 39 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -23.29 | -3.44 | -25.77 | 35 |
| 40 | Ichimoku · 1h | trend | 82.08 | -17.92 | 75 | 10.7 | -20.64 | -4.12 | -24.73 | 117 |
| 41 | Supertrend · 1h | trend | 80.83 | -19.17 | 126 | 14.3 | -25.86 | -4.80 | -28.62 | 216 |
| 42 | MFI reversion · 1h | reversion | 80.28 | -19.72 | 292 | 31.8 | -17.84 | -2.83 | -20.24 | 152 |
| 43 | EMA 20/50 cross · 1h | trend | 79.78 | -20.22 | 88 | 11.4 | -23.64 | -4.46 | -26.78 | 136 |
| 44 | CCI reversion · 1h | reversion | 79.54 | -20.46 | 246 | 46.3 | -26.53 | -4.09 | -28.85 | 450 |
| 45 | RSI momentum · 1h | momentum | 78.99 | -21.01 | 127 | 12.6 | -27.00 | -4.88 | -29.89 | 214 |
| 46 | Williams %R · 1h | reversion | 78.93 | -21.07 | 252 | 47.2 | -35.24 | -6.22 | -35.60 | 528 |
| 47 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.33 | -4.89 | -27.15 | 214 |
| 48 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -18.43 | -2.82 | -22.16 | 207 |
| 49 | MACD cross · 1h | trend | 78.59 | -21.41 | 282 | 24.1 | -30.89 | -5.44 | -32.86 | 473 |
| 50 | Triple EMA stack · 1h | trend | 78.43 | -21.57 | 117 | 13.7 | -30.34 | -5.68 | -32.83 | 208 |
| 51 | Heikin-Ashi · 1h | trend | 78.18 | -21.82 | 333 | 23.7 | -42.01 | -9.12 | -42.16 | 667 |
| 52 | OBV trend · 1h | momentum | 77.48 | -22.52 | 228 | 17.1 | -34.22 | -6.81 | -36.56 | 299 |
| 53 | Bollinger reversion · 1h | reversion | 77.35 | -22.65 | 195 | 37.9 | -31.45 | -6.52 | -32.42 | 367 |
| 54 | Donchian 20/10 · 1h | breakout | 76.08 | -23.91 | 112 | 20.5 | -27.98 | -4.92 | -29.50 | 219 |
| 55 | ROC + volume · 1h | momentum | 75.80 | -24.20 | 291 | 25.8 | -30.74 | -5.43 | -32.51 | 386 |
| 56 | Three white soldiers | momentum | 74.32 | -25.68 | 365 | 17.8 | -44.43 | -20.56 | -44.46 | 611 |
| 57 | Agent (ML meta-label) | meta | 73.44 | -26.56 | 1129 | 20.8 | -9.73 | -1.50 | -16.63 | 347 |
| 58 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -20.84 | -3.59 | -25.90 | 195 |
| 59 | VWAP momentum · 1h | momentum | 72.98 | -27.02 | 638 | 22.9 | -52.55 | -11.16 | -52.79 | 1236 |
| 60 | Candlestick reversal · 1h | reversion | 72.86 | -27.14 | 309 | 29.4 | -35.30 | -6.97 | -35.42 | 549 |
| 61 | Max aggression: 1-day momentum | meta | 72.26 | -27.74 | 21 | 33.3 | -29.37 | -1.59 | -50.32 | 42 |
| 62 | EMA 9/21 cross · 1h | trend | 71.38 | -28.62 | 202 | 9.9 | -35.85 | -6.86 | -36.26 | 336 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -44.52 | -98.91 | 5225 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.12 | -23.69 | -79.12 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -44.52 | -93.53 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.69 | -30.48 | -88.69 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -36.93 | -91.14 | 2344 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.09 | -30.73 | -90.09 | 2232 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -50.46 | -97.71 | 3505 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.11 | -56.07 | -96.11 | 3387 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.00 | -35.19 | -94.00 | 2468 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.83 | -32.64 | -81.83 | 1682 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.70 | -99.47 | 5818 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -42.80 | -92.88 | 2626 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.47 | -37.11 | -95.47 | 3453 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.88 | -99.78 | 6183 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -42.57 | -91.87 | 2300 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.37 | -27.47 | -75.46 | 1575 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -60.64 | -97.68 | 3572 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -60.09 | -98.66 | 4809 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.39 | -28.72 | -69.59 | 1212 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -52.88 | -94.77 | 2790 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -37.86 | -84.73 | 1815 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.78 | -99.61 | 6301 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.22 | -29.93 | -88.22 | 2222 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.29 | -19.64 | -77.30 | 1693 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.80 | -37.84 | -90.80 | 2248 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.32 | -50.82 | -96.32 | 3805 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.84 | -52.11 | -89.84 | 2130 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.65 | -25.65 | -64.65 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.73 | -25.62 | -73.73 | 1276 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.96 | -18.28 | -76.00 | 1554 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.73 | -50.50 | -96.73 | 4212 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -99.30 | -99.92 | 8294 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T14:16 | Agent (rotation) | buy | SQQQ | 7.97 | — | entry |
| 2026-10-30T14:16 | Agent (ML meta-label) | buy | SOL-USD | 8.05 | — | entry |
| 2026-10-30T14:16 | Agent (aggressive) | buy | LABU | 43.71 | — | following Candlestick reversal |
| 2026-10-30T14:16 | Agent | buy | LABU | 18.31 | — | following Candlestick reversal |
| 2026-10-30T14:16 | Opening range 15m | sell | TQQQ | 12.46 | -0.24 | exit signal |
| 2026-10-30T14:16 | Opening range 15m | sell | QQQ | 16.78 | -0.11 | exit signal |
| 2026-10-30T14:16 | Gap and go | buy | SQQQ | 23.77 | — | entry signal |
| 2026-10-30T14:10 | Agent (ML meta-label) | buy | TSLA | 12.25 | — | following Z-score reversion |
| 2026-10-30T14:10 | Agent (ML meta-label) | sell | SOL-USD | 12.14 | -0.26 | selected signal exited |
| 2026-10-30T14:10 | Agent | sell | PLTR | 18.18 | -0.16 | selected signal exited |
| 2026-10-30T14:05 | Agent (ML meta-label) | sell | TSLA | 8.17 | 0.07 | selected signal exited |
| 2026-10-30T14:05 | Opening range 30m | buy | TSLA | 22.94 | — | entry signal |
| 2026-10-30T14:05 | Opening range 30m | buy | META | 22.94 | — | entry signal |
| 2026-10-30T14:00 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 100.34 | -1.44 | target is flat |
| 2026-10-30T14:00 | Agent | buy | TSLA | 18.32 | — | following Z-score reversion |
| 2026-10-30T14:00 | OBV trend · 1h | buy | TSLA | 6.21 | — | rebalance up |
| 2026-10-30T14:00 | OBV trend · 1h | buy | TNA | 6.60 | — | rebalance up |
| 2026-10-30T14:00 | OBV trend · 1h | buy | LABU | 6.74 | — | rebalance up |
| 2026-10-30T14:00 | OBV trend · 1h | buy | IWM | 6.52 | — | rebalance up |
| 2026-10-30T14:00 | OBV trend · 1h | sell | SQQQ | 15.74 | 0.50 | target is flat |
| 2026-10-30T14:00 | VWAP momentum · 1h | sell | SOL-USD | 18.23 | -0.22 | exit signal |
| 2026-10-30T14:00 | Opening range 15m | buy | TQQQ | 12.69 | — | entry signal |
| 2026-10-30T14:00 | Opening range 15m | buy | QQQ | 16.89 | — | entry signal |
| 2026-10-30T14:00 | Opening range 15m | buy | META | 16.89 | — | entry signal |
| 2026-10-30T14:00 | Opening range 15m | sell | TSLA | 4.27 | 0.01 | rebalance down |
| 2026-10-30T13:55 | Opening range 15m | buy | TSLA | 21.07 | — | entry signal |
| 2026-10-30T13:50 | Day trade: Stocks in Play ORB | sell | AMD | 24.13 | -0.33 | target is flat |
| 2026-10-30T13:50 | Agent (ML meta-label) | buy | TSLA | 8.10 | — | following Z-score reversion |
| 2026-10-30T13:50 | Agent (ML meta-label) | sell | XRP-USD | 8.10 | -0.07 | selected signal exited |
| 2026-10-30T13:50 | Candlestick reversal · 1h | sell | BTC-USD | 18.15 | -0.22 | stop-loss |
| 2026-10-30T13:50 | ROC + volume · 1h | sell | IWM | 18.91 | -0.14 | stop-loss |
| 2026-10-30T13:50 | Parabolic SAR · 1h | sell | IWM | 22.60 | -0.25 | stop-loss |
| 2026-10-30T13:50 | Opening range 15m | buy | AMZN | 21.09 | — | entry signal |
| 2026-10-30T13:45 | Day trade: Stocks in Play ORB | sell | SQQQ | 24.57 | 0.10 | target is flat |
| 2026-10-30T13:45 | Day trade: Stocks in Play ORB | sell | IWM | 24.40 | -0.07 | target is flat |
| 2026-10-30T13:45 | Agent (ML meta-label) | buy | XRP-USD | 8.16 | — | entry |
| 2026-10-30T13:45 | Agent | buy | PLTR | 18.34 | — | following Candlestick reversal |
| 2026-10-30T13:45 | Volume breakout · 1h | sell | TNA | 21.35 | -0.69 | target is flat |
| 2026-10-30T13:45 | Donchian 20/10 · 1h | buy | LABU | 4.04 | — | rebalance up |
| 2026-10-30T13:45 | RSI momentum · 1h | buy | LABU | 4.19 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 14:16:05.000154+00:00 -> 2026-10-30 14:26:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
