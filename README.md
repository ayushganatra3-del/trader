# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T15:15:05.000149+00:00 · 41502 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.82 (-8.18%)

Closed trades 125, win rate 40.8%, fees £3.67, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.28 | -0.10 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-29)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.18 · VIX 17.20 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, IWM 5.9, LABU 5.7, AAPL 5.2, SQQQ 4.9, PLTR 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 16422 decisions in 2178 calls, $0.2146 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T15:15 | 7 / 8 / 15 | cash |  |
| Breezy | 2026-10-30T15:15 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-30T15:15 | 8 / 15 / 7 | MSTR 83% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| VWAP reversion | SQQQ | 2.67 | +4.28% | 5 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.11 | 7.11 | 0 | — | 8.28 | 4.04 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.60 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.67 | 3.67 | 22 | 45.5 | 7.56 | 2.48 | -4.92 | 26 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 100.81 | 0.81 | 0 | — | 4.04 | 1.77 | -5.02 | 1 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.87 | -5.89 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.52 | -12.60 | 140 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.93 | -2.07 | 95 | 35.8 | 6.47 | 3.07 | -2.21 | 94 |
| 10 | Hold SPY | benchmark | 97.61 | -2.39 | 0 | — | -0.97 | -0.48 | -3.06 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.49 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.15 | -4.72 | 20 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 96.83 | -3.17 | 0 | — | -5.05 | -2.03 | -7.83 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 15 | Agent (rotation) | meta | 95.27 | -4.73 | 129 | 31.0 | -2.73 | -1.77 | -8.12 | 151 |
| 16 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.52 | -4.94 | 28 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.86 | -5.14 | 0 | — | -2.78 | -1.08 | -6.39 | 1 |
| 18 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.48 | -8.76 | 203 |
| 19 | Opening range 30m | breakout | 92.11 | -7.89 | 305 | 35.4 | -10.77 | -3.21 | -17.21 | 589 |
| 20 | Agent | meta | 91.82 | -8.18 | 125 | 40.8 | -9.15 | -5.36 | -12.21 | 222 |
| 21 | Hold BTC | benchmark | 91.75 | -8.25 | 0 | — | -0.85 | 0.04 | -12.47 | 1 |
| 22 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.11 | -7.49 | -21.17 | 98 |
| 23 | Parabolic SAR · 1h | trend | 91.42 | -8.58 | 139 | 28.1 | -18.11 | -4.16 | -20.27 | 250 |
| 24 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.64 | -16.91 | 1 |
| 25 | Donchian 55/20 · 1h | breakout | 90.72 | -9.28 | 54 | 14.8 | -15.72 | -3.55 | -17.32 | 103 |
| 26 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.42 | -2.05 | -12.70 | 94 |
| 27 | Daily: Bullish score | daily | 88.71 | -11.29 | 14 | 21.4 | -6.57 | -0.81 | -14.73 | 14 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 88.60 | -11.40 | 0 | — | -3.23 | -0.34 | -14.57 | 1 |
| 29 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.69 | -15.04 | 101 |
| 30 | Stochastic reversion · 1h | reversion | 86.03 | -13.97 | 221 | 47.5 | -17.29 | -3.03 | -23.72 | 381 |
| 31 | Volume breakout · 1h | breakout | 85.58 | -14.42 | 127 | 29.1 | -13.49 | -2.88 | -16.25 | 105 |
| 32 | Max aggression: 5-day momentum | meta | 85.17 | -14.83 | 14 | 42.9 | -34.07 | -2.58 | -36.20 | 25 |
| 33 | ADX DI cross · 1h | trend | 84.77 | -15.23 | 141 | 19.1 | -17.79 | -3.46 | -20.33 | 261 |
| 34 | Keltner breakout · 1h | breakout | 84.74 | -15.26 | 86 | 24.4 | -24.96 | -4.98 | -25.77 | 189 |
| 35 | Connors RSI(2) · 1h | reversion | 84.63 | -15.37 | 186 | 40.9 | -20.24 | -6.47 | -21.56 | 162 |
| 36 | Opening range 15m | breakout | 84.45 | -15.55 | 379 | 31.9 | -15.78 | -4.54 | -18.52 | 720 |
| 37 | Bollinger breakout · 1h | breakout | 83.08 | -16.92 | 132 | 26.5 | -16.41 | -3.04 | -21.61 | 245 |
| 38 | Ichimoku · 1h | trend | 82.60 | -17.40 | 78 | 14.1 | -20.27 | -4.09 | -24.80 | 117 |
| 39 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -23.39 | -3.47 | -26.56 | 35 |
| 40 | Supertrend · 1h | trend | 81.56 | -18.44 | 133 | 13.5 | -25.32 | -4.78 | -28.87 | 216 |
| 41 | CCI reversion · 1h | reversion | 80.89 | -19.11 | 246 | 46.3 | -25.54 | -3.96 | -28.85 | 448 |
| 42 | MFI reversion · 1h | reversion | 80.86 | -19.14 | 292 | 31.8 | -18.56 | -2.96 | -20.24 | 152 |
| 43 | EMA 20/50 cross · 1h | trend | 80.14 | -19.86 | 88 | 11.4 | -23.32 | -4.44 | -26.95 | 136 |
| 44 | Williams %R · 1h | reversion | 79.83 | -20.17 | 252 | 47.2 | -34.46 | -6.14 | -35.58 | 528 |
| 45 | MACD cross · 1h | trend | 79.71 | -20.29 | 282 | 24.1 | -30.01 | -5.40 | -32.86 | 473 |
| 46 | RSI momentum · 1h | momentum | 79.60 | -20.40 | 127 | 12.6 | -26.60 | -4.91 | -30.13 | 215 |
| 47 | Triple EMA stack · 1h | trend | 79.02 | -20.98 | 117 | 13.7 | -29.99 | -5.74 | -33.05 | 208 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.33 | -4.93 | -27.15 | 214 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -17.19 | -2.70 | -22.16 | 207 |
| 50 | Bollinger reversion · 1h | reversion | 78.49 | -21.51 | 195 | 37.9 | -30.67 | -6.47 | -32.42 | 365 |
| 51 | Heikin-Ashi · 1h | trend | 78.18 | -21.82 | 333 | 23.7 | -42.01 | -9.21 | -42.16 | 667 |
| 52 | OBV trend · 1h | momentum | 77.91 | -22.09 | 230 | 17.8 | -32.71 | -6.68 | -35.55 | 300 |
| 53 | Donchian 20/10 · 1h | breakout | 75.93 | -24.07 | 114 | 21.1 | -27.98 | -4.93 | -29.80 | 220 |
| 54 | ROC + volume · 1h | momentum | 75.79 | -24.21 | 291 | 25.8 | -29.72 | -5.14 | -31.91 | 384 |
| 55 | Three white soldiers | momentum | 74.25 | -25.75 | 368 | 17.7 | -44.41 | -20.83 | -44.47 | 613 |
| 56 | VWAP momentum · 1h | momentum | 73.97 | -26.03 | 638 | 22.9 | -51.96 | -11.13 | -52.79 | 1237 |
| 57 | Candlestick reversal · 1h | reversion | 73.70 | -26.30 | 309 | 29.4 | -34.27 | -6.79 | -35.12 | 547 |
| 58 | Agent (ML meta-label) | meta | 73.64 | -26.36 | 1141 | 20.9 | -13.24 | -2.18 | -20.40 | 354 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -19.84 | -3.53 | -25.90 | 190 |
| 60 | Max aggression: 1-day momentum | meta | 72.20 | -27.80 | 21 | 33.3 | -29.55 | -1.62 | -50.32 | 42 |
| 61 | EMA 9/21 cross · 1h | trend | 71.79 | -28.21 | 202 | 9.9 | -35.32 | -6.88 | -36.33 | 336 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -44.14 | -98.90 | 5241 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.18 | -24.09 | -79.18 | 1416 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -46.00 | -93.56 | 2539 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.60 | -30.87 | -88.67 | 1915 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -37.85 | -91.14 | 2348 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.07 | -31.61 | -90.07 | 2231 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -52.29 | -97.70 | 3509 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -58.91 | -96.12 | 3387 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -36.65 | -94.03 | 2472 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.80 | -33.58 | -81.89 | 1682 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -57.75 | -99.47 | 5839 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.92 | -44.26 | -92.94 | 2632 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -38.55 | -95.45 | 3453 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -79.59 | -99.78 | 6206 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -44.04 | -91.87 | 2307 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.49 | -28.05 | -75.54 | 1579 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -63.92 | -97.68 | 3571 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -63.59 | -98.67 | 4817 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.29 | -28.85 | -69.52 | 1212 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -55.29 | -94.76 | 2797 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -38.73 | -84.75 | 1820 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -73.40 | -99.61 | 6317 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.13 | -30.55 | -88.23 | 2239 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.34 | -19.92 | -77.46 | 1711 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.71 | -38.69 | -90.80 | 2258 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.32 | -53.04 | -96.33 | 3808 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.85 | -54.32 | -89.87 | 2142 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.99 | -26.44 | -64.99 | 831 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.72 | -25.90 | -73.72 | 1276 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.88 | -18.58 | -75.89 | 1560 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.72 | -52.72 | -96.74 | 4217 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -106.78 | -99.92 | 8316 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T15:15 | Agent (ML meta-label) | buy | LABU | 3.73 | — | rebalance up |
| 2026-10-30T15:15 | Agent (ML meta-label) | buy | ETH-USD | 3.69 | — | rebalance up |
| 2026-10-30T15:15 | Agent (ML meta-label) | sell | TSLA | 7.51 | -0.02 | selected signal exited |
| 2026-10-30T15:15 | Three white soldiers | sell | AAPL | 18.57 | -0.01 | exit signal |
| 2026-10-30T15:10 | Agent (ML meta-label) | buy | TSLA | 7.53 | — | entry |
| 2026-10-30T15:10 | Agent (ML meta-label) | sell | LABU | 3.77 | 0.06 | rebalance down |
| 2026-10-30T15:10 | Agent (ML meta-label) | sell | ETH-USD | 3.77 | 0.02 | rebalance down |
| 2026-10-30T15:10 | Opening range 30m | buy | MSTR | 11.53 | — | entry signal |
| 2026-10-30T15:10 | Opening range 30m | buy | GOOGL | 11.53 | — | entry signal |
| 2026-10-30T15:10 | Opening range 30m | buy | AMZN | 11.53 | — | entry signal |
| 2026-10-30T15:10 | Opening range 30m | sell | TSLA | 6.94 | 0.10 | rebalance down |
| 2026-10-30T15:10 | Opening range 30m | sell | META | 6.88 | 0.05 | rebalance down |
| 2026-10-30T15:10 | Opening range 30m | sell | ETHU | 11.36 | 0.16 | rebalance down |
| 2026-10-30T15:10 | Opening range 30m | sell | AAPL | 11.36 | -0.04 | rebalance down |
| 2026-10-30T15:10 | Opening range 15m | buy | MSTR | 10.56 | — | entry signal |
| 2026-10-30T15:10 | Opening range 15m | buy | GOOGL | 10.57 | — | entry signal |
| 2026-10-30T15:10 | Opening range 15m | buy | BITX | 10.57 | — | entry |
| 2026-10-30T15:10 | Opening range 15m | sell | TSLA | 6.64 | 0.15 | rebalance down |
| 2026-10-30T15:10 | Opening range 15m | sell | META | 6.46 | 0.05 | rebalance down |
| 2026-10-30T15:10 | Opening range 15m | sell | ETHU | 6.00 | 0.09 | rebalance down |
| 2026-10-30T15:10 | Opening range 15m | sell | AMZN | 6.38 | 0.04 | rebalance down |
| 2026-10-30T15:10 | Opening range 15m | sell | AAPL | 6.21 | -0.02 | rebalance down |
| 2026-10-30T15:05 | Opening range 30m | buy | BITX | 9.50 | — | entry signal |
| 2026-10-30T15:05 | Opening range 30m | sell | TSLA | 4.80 | 0.05 | rebalance down |
| 2026-10-30T15:05 | Opening range 30m | sell | META | 4.70 | 0.03 | rebalance down |
| 2026-10-30T15:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.67 | -1.14 | target is flat |
| 2026-10-30T15:00 | Agent (ML meta-label) | buy | SQQQ | 3.68 | — | rebalance up |
| 2026-10-30T15:00 | Agent (ML meta-label) | buy | ETH-USD | 3.69 | — | rebalance up |
| 2026-10-30T15:00 | Agent (ML meta-label) | sell | SOL-USD | 7.37 | -0.07 | selected signal exited |
| 2026-10-30T15:00 | Agent | buy | PLTR | 18.38 | — | following Candlestick reversal |
| 2026-10-30T15:00 | Candlestick reversal · 1h | buy | XRP-USD | 18.16 | — | entry signal |
| 2026-10-30T15:00 | Candlestick reversal · 1h | buy | BTC-USD | 18.32 | — | entry signal |
| 2026-10-30T14:55 | Agent (ML meta-label) | buy | SOL-USD | 3.72 | — | rebalance up |
| 2026-10-30T14:55 | Agent (ML meta-label) | sell | SQQQ | 3.72 | 0.09 | rebalance down |
| 2026-10-30T14:55 | Agent (aggressive) | sell | LABU | 43.52 | -0.15 | selected signal exited |
| 2026-10-30T14:55 | Agent | sell | LABU | 18.52 | 0.22 | selected signal exited |
| 2026-10-30T14:55 | Opening range 15m | buy | ETHU | 4.22 | — | rebalance up |
| 2026-10-30T14:55 | Opening range 15m | sell | AAPL | 4.22 | -0.00 | rebalance down |
| 2026-10-30T14:50 | Agent (rotation) | sell | SQQQ | 31.70 | -0.53 | selected signal exited |
| 2026-10-30T14:50 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 104.59 | -1.89 | target is flat |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
