# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T13:45:05.000158+00:00 · 41440 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.67 (-8.33%)

Closed trades 122, win rate 40.2%, fees £3.62, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.33 | -0.01 |

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

Today: 10782 decisions in 1992 calls, $0.1486 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T13:45 | 0 / 11 / 19 | cash |  |
| Breezy | 2026-10-30T13:45 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-30T13:45 | 5 / 21 / 4 | COIN 59% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.94 | 6.94 | 0 | — | 8.29 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.78 | 2.21 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.25 | 1.25 | 24 | 29.2 | 8.18 | 2.10 | -5.53 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.58 | -0.42 | 0 | — | 2.94 | 1.27 | -5.02 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Hold SPY | benchmark | 97.65 | -2.35 | 0 | — | -0.77 | -0.38 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.57 | -2.43 | 94 | 36.2 | 6.70 | 3.16 | -1.98 | 94 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 96.68 | -3.32 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 15 | Agent (rotation) | meta | 95.52 | -4.48 | 128 | 31.2 | -2.81 | -1.83 | -7.82 | 163 |
| 16 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 4.72 | 1.55 | -8.76 | 202 |
| 17 | Copy: Congress Democrats (NANC) | copy | 95.06 | -4.94 | 0 | — | -2.42 | -0.94 | -5.99 | 1 |
| 18 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 19 | Copy: Insider buying | copy | 92.62 | -7.38 | 33 | 36.4 | -21.70 | -4.41 | -23.91 | 69 |
| 20 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.05 | -3.28 | -17.21 | 580 |
| 21 | Agent | meta | 91.67 | -8.33 | 122 | 40.2 | -9.48 | -5.58 | -12.21 | 219 |
| 22 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.17 | -7.34 | -21.50 | 99 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 24 | Donchian 55/20 · 1h | breakout | 91.04 | -8.96 | 54 | 14.8 | -15.11 | -3.41 | -16.05 | 102 |
| 25 | Hold BTC | benchmark | 90.68 | -9.32 | 0 | — | -1.89 | -0.14 | -12.47 | 1 |
| 26 | Parabolic SAR · 1h | trend | 90.57 | -9.43 | 137 | 28.5 | -18.93 | -4.41 | -20.28 | 250 |
| 27 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.17 | -1.97 | -12.70 | 94 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 89.18 | -10.81 | 0 | — | -2.43 | -0.22 | -14.57 | 1 |
| 29 | Daily: Bullish score | daily | 88.17 | -11.83 | 14 | 21.4 | -7.15 | -0.89 | -14.73 | 14 |
| 30 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Max aggression: 5-day momentum | meta | 86.22 | -13.78 | 14 | 42.9 | -32.88 | -2.53 | -32.88 | 25 |
| 32 | Volume breakout · 1h | breakout | 85.66 | -14.34 | 127 | 29.1 | -14.48 | -3.09 | -17.02 | 105 |
| 33 | Stochastic reversion · 1h | reversion | 85.25 | -14.75 | 221 | 47.5 | -17.91 | -3.10 | -23.39 | 381 |
| 34 | Keltner breakout · 1h | breakout | 84.83 | -15.17 | 86 | 24.4 | -24.71 | -4.89 | -25.54 | 189 |
| 35 | Connors RSI(2) · 1h | reversion | 84.40 | -15.60 | 186 | 40.9 | -20.46 | -6.51 | -21.56 | 158 |
| 36 | ADX DI cross · 1h | trend | 84.39 | -15.61 | 140 | 19.3 | -18.01 | -3.43 | -20.32 | 261 |
| 37 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -15.87 | -4.53 | -18.10 | 709 |
| 38 | Bollinger breakout · 1h | breakout | 83.16 | -16.84 | 132 | 26.5 | -16.31 | -3.00 | -21.37 | 244 |
| 39 | Ichimoku · 1h | trend | 83.07 | -16.93 | 75 | 10.7 | -19.70 | -3.96 | -24.73 | 117 |
| 40 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -21.93 | -3.42 | -24.45 | 35 |
| 41 | Supertrend · 1h | trend | 81.19 | -18.81 | 126 | 14.3 | -25.35 | -4.74 | -28.15 | 216 |
| 42 | EMA 20/50 cross · 1h | trend | 80.27 | -19.73 | 88 | 11.4 | -23.11 | -4.37 | -26.24 | 136 |
| 43 | MFI reversion · 1h | reversion | 80.18 | -19.82 | 292 | 31.8 | -19.16 | -3.02 | -20.24 | 152 |
| 44 | RSI momentum · 1h | momentum | 79.97 | -20.04 | 127 | 12.6 | -26.02 | -4.84 | -29.02 | 214 |
| 45 | CCI reversion · 1h | reversion | 79.93 | -20.07 | 246 | 46.3 | -26.17 | -4.03 | -28.85 | 450 |
| 46 | Williams %R · 1h | reversion | 79.22 | -20.78 | 252 | 47.2 | -34.86 | -6.15 | -35.34 | 528 |
| 47 | Triple EMA stack · 1h | trend | 79.12 | -20.88 | 117 | 13.7 | -29.93 | -5.70 | -32.23 | 208 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.37 | -4.90 | -27.15 | 214 |
| 49 | MACD cross · 1h | trend | 78.73 | -21.27 | 282 | 24.1 | -30.93 | -5.45 | -32.74 | 474 |
| 50 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -18.04 | -2.78 | -21.78 | 207 |
| 51 | OBV trend · 1h | momentum | 78.54 | -21.46 | 227 | 16.7 | -32.46 | -6.58 | -34.88 | 301 |
| 52 | Heikin-Ashi · 1h | trend | 78.18 | -21.82 | 333 | 23.7 | -42.01 | -9.12 | -42.16 | 667 |
| 53 | Bollinger reversion · 1h | reversion | 77.68 | -22.32 | 195 | 37.9 | -31.09 | -6.46 | -32.13 | 368 |
| 54 | Donchian 20/10 · 1h | breakout | 77.02 | -22.98 | 112 | 20.5 | -26.80 | -4.81 | -28.64 | 219 |
| 55 | ROC + volume · 1h | momentum | 75.73 | -24.27 | 290 | 25.9 | -31.11 | -5.48 | -32.40 | 388 |
| 56 | Three white soldiers | momentum | 74.32 | -25.68 | 365 | 17.8 | -44.51 | -20.61 | -44.54 | 612 |
| 57 | Agent (ML meta-label) | meta | 73.72 | -26.28 | 1126 | 20.8 | -13.61 | -2.48 | -18.63 | 356 |
| 58 | VWAP momentum · 1h | momentum | 73.26 | -26.74 | 637 | 22.9 | -52.37 | -11.12 | -52.61 | 1236 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -21.01 | -3.69 | -25.53 | 186 |
| 60 | Candlestick reversal · 1h | reversion | 73.08 | -26.92 | 308 | 29.5 | -35.19 | -6.89 | -35.50 | 540 |
| 61 | EMA 9/21 cross · 1h | trend | 71.86 | -28.14 | 202 | 9.9 | -34.79 | -6.74 | -35.61 | 335 |
| 62 | Max aggression: 1-day momentum | meta | 71.79 | -28.21 | 21 | 33.3 | -30.07 | -1.66 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -44.19 | -98.90 | 5196 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.07 | -23.62 | -79.07 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -44.52 | -93.53 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.66 | -30.39 | -88.66 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -36.93 | -91.14 | 2344 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.09 | -30.72 | -90.09 | 2234 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -50.31 | -97.70 | 3505 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -56.12 | -96.10 | 3385 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.87 | -34.84 | -93.87 | 2457 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.82 | -32.63 | -81.83 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -54.66 | -99.46 | 5806 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -42.80 | -92.88 | 2626 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -36.92 | -95.45 | 3453 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -73.14 | -99.78 | 6184 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -42.58 | -91.87 | 2300 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.32 | -27.44 | -75.32 | 1571 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -59.80 | -97.67 | 3573 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -60.15 | -98.65 | 4787 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -28.58 | -69.52 | 1211 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -52.72 | -94.75 | 2789 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.72 | -37.83 | -84.72 | 1815 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.67 | -99.61 | 6295 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.14 | -29.78 | -88.15 | 2213 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.11 | -19.56 | -77.27 | 1683 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.76 | -37.94 | -90.76 | 2243 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.29 | -50.71 | -96.29 | 3783 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.80 | -51.98 | -89.80 | 2133 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.65 | -25.65 | -64.65 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.72 | -25.61 | -73.72 | 1276 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.89 | -18.29 | -75.93 | 1555 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.71 | -50.34 | -96.71 | 4201 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -99.95 | -99.92 | 8295 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T13:45 | Day trade: Stocks in Play ORB | sell | SQQQ | 24.57 | 0.10 | target is flat |
| 2026-10-30T13:45 | Day trade: Stocks in Play ORB | sell | IWM | 24.40 | -0.07 | target is flat |
| 2026-10-30T13:45 | Agent (ML meta-label) | buy | XRP-USD | 8.16 | — | entry |
| 2026-10-30T13:45 | Agent | buy | PLTR | 18.34 | — | following Candlestick reversal |
| 2026-10-30T13:45 | Volume breakout · 1h | sell | TNA | 21.35 | -0.69 | target is flat |
| 2026-10-30T13:45 | Donchian 20/10 · 1h | buy | LABU | 4.04 | — | rebalance up |
| 2026-10-30T13:45 | RSI momentum · 1h | buy | LABU | 4.19 | — | rebalance up |
| 2026-10-30T13:45 | ROC + volume · 1h | sell | TNA | 18.87 | -0.15 | stop-loss |
| 2026-10-30T13:45 | MACD cross · 1h | buy | XRP-USD | 3.91 | — | rebalance up |
| 2026-10-30T13:45 | MACD cross · 1h | buy | SQQQ | 6.56 | — | rebalance up |
| 2026-10-30T13:45 | MACD cross · 1h | buy | ETH-USD | 6.53 | — | rebalance up |
| 2026-10-30T13:45 | MACD cross · 1h | buy | DOGE-USD | 6.58 | — | rebalance up |
| 2026-10-30T13:45 | MACD cross · 1h | sell | SOL-USD | 15.65 | -0.47 | stop-loss |
| 2026-10-30T13:45 | EMA 20/50 cross · 1h | buy | LABU | 4.17 | — | rebalance up |
| 2026-10-30T13:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 24.46 | — | entry |
| 2026-10-30T13:40 | Day trade: Stocks in Play ORB | buy | IWM | 24.46 | — | entry |
| 2026-10-30T13:40 | Day trade: Stocks in Play ORB | buy | AMZN | 24.46 | — | entry |
| 2026-10-30T13:40 | Day trade: Stocks in Play ORB | buy | AMD | 24.46 | — | entry |
| 2026-10-30T13:40 | Agent (ML meta-label) | buy | SOL-USD | 3.93 | — | rebalance up |
| 2026-10-30T13:40 | Agent (ML meta-label) | buy | ETH-USD | 6.07 | — | rebalance up |
| 2026-10-30T13:40 | Agent (ML meta-label) | sell | XRP-USD | 1.81 | -0.01 | selected signal exited |
| 2026-10-30T13:40 | Agent (ML meta-label) | sell | TSLA | 9.32 | -0.36 | selected signal exited |
| 2026-10-30T13:40 | Agent (ML meta-label) | sell | AAPL | 7.03 | -0.11 | selected signal exited |
| 2026-10-30T13:40 | Volume breakout · 1h | sell | AAPL | 21.58 | -0.46 | stop-loss |
| 2026-10-30T13:40 | Squeeze breakout · 1h | sell | IWM | 18.26 | 0.16 | stop-loss |
| 2026-10-30T13:40 | Keltner breakout · 1h | sell | IWM | 21.23 | -0.12 | stop-loss |
| 2026-10-30T13:40 | Bollinger breakout · 1h | sell | IWM | 17.25 | -0.08 | stop-loss |
| 2026-10-30T13:40 | Donchian 55/20 · 1h | buy | TNA | 4.66 | — | rebalance up |
| 2026-10-30T13:40 | Donchian 20/10 · 1h | buy | TNA | 3.97 | — | rebalance up |
| 2026-10-30T13:40 | Donchian 20/10 · 1h | buy | IWM | 3.97 | — | rebalance up |
| 2026-10-30T13:40 | Donchian 20/10 · 1h | sell | AAPL | 15.42 | -0.23 | stop-loss |
| 2026-10-30T13:40 | OBV trend · 1h | buy | SQQQ | 6.37 | — | rebalance up |
| 2026-10-30T13:40 | OBV trend · 1h | sell | AAPL | 9.88 | -0.21 | stop-loss |
| 2026-10-30T13:40 | RSI momentum · 1h | buy | TNA | 4.12 | — | rebalance up |
| 2026-10-30T13:40 | RSI momentum · 1h | buy | IWM | 4.12 | — | rebalance up |
| 2026-10-30T13:40 | RSI momentum · 1h | sell | AAPL | 16.01 | -0.13 | stop-loss |
| 2026-10-30T13:40 | ADX DI cross · 1h | sell | MSFT | 17.48 | -0.40 | stop-loss |
| 2026-10-30T13:40 | MACD zero-line · 1h | sell | AAPL | 19.68 | -0.28 | stop-loss |
| 2026-10-30T13:40 | MACD cross · 1h | buy | XRP-USD | 4.33 | — | rebalance up |
| 2026-10-30T13:40 | MACD cross · 1h | buy | SOL-USD | 5.90 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 13:45:05.000158+00:00 -> 2026-10-30 13:55:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
