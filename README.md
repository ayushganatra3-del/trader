# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T15:40:05.000121+00:00 · 57092 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.77 (-14.23%)

Closed trades 182, win rate 35.2%, fees £5.42, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 17.44 | +0.36 |
| SQQQ | 17.05 | -0.04 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 17585 decisions in 2501 calls, $0.2320 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T15:40 | 9 / 16 / 5 | LABU 14% |  |
| Breezy | 2026-11-12T15:40 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-12T15:40 | 8 / 22 / 0 | MSTR 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.14 | +7.35% | 5 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.45 | 17.45 | 0 | — | 16.68 | 5.32 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.94 | 11.94 | 21 | 66.7 | 17.38 | 3.50 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.05 | 11.05 | 33 | 27.3 | 19.40 | 2.92 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.70 | 4.71 | 0 | — | 6.95 | 1.90 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.35 | 0.35 | 137 | 33.6 | 6.85 | 2.72 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.02 | 0.03 | 192 | 32.8 | 6.10 | 1.74 | -9.06 | 232 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.01 | 0.06 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.52 | -1.48 | 0 | — | -1.05 | -0.21 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.56 | -2.44 | 1 | 0.0 | -2.32 | -1.61 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.32 | -2.68 | 189 | 30.2 | -2.53 | -0.91 | -8.97 | 171 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.27 | -3.73 | 0 | — | -3.90 | -0.99 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.53 | -4.47 | 142 | 47.2 | -12.77 | -3.31 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 94.37 | -5.62 | 43 | 39.5 | -7.07 | -1.39 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.92 | -6.08 | 0 | — | -3.46 | -0.88 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 92.45 | -7.55 | 1 | 0.0 | -7.76 | -1.75 | -16.91 | 2 |
| 21 | Trend pullback · 1h | trend | 92.22 | -7.78 | 109 | 22.9 | -14.27 | -5.03 | -18.42 | 76 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -6.45 | -1.83 | -15.11 | 76 |
| 23 | Parabolic SAR · 1h | trend | 86.07 | -13.93 | 171 | 27.5 | -14.45 | -3.08 | -21.98 | 222 |
| 24 | Agent | meta | 85.77 | -14.23 | 182 | 35.2 | -15.06 | -7.54 | -15.60 | 210 |
| 25 | Opening range 30m | breakout | 85.44 | -14.56 | 417 | 32.9 | -10.90 | -3.50 | -14.11 | 591 |
| 26 | Daily: Bullish score | daily | 85.14 | -14.86 | 16 | 18.8 | -12.91 | -1.56 | -19.56 | 15 |
| 27 | Hold BTC | benchmark | 83.99 | -16.01 | 1 | 0.0 | -8.62 | -1.05 | -18.33 | 1 |
| 28 | Agent (aggressive) | meta | 83.59 | -16.41 | 89 | 33.7 | -16.78 | -4.69 | -18.51 | 101 |
| 29 | Donchian 55/20 · 1h | breakout | 83.25 | -16.75 | 73 | 13.7 | -23.01 | -4.87 | -29.68 | 93 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.83 | -18.17 | 2 | 0.0 | -9.47 | -1.01 | -24.16 | 1 |
| 31 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -28.66 | -1.55 | -45.81 | 24 |
| 32 | Connors RSI(2) · 1h | reversion | 80.94 | -19.06 | 209 | 40.2 | -19.89 | -6.72 | -20.32 | 120 |
| 33 | ADX DI cross · 1h | trend | 80.89 | -19.11 | 191 | 19.4 | -23.43 | -4.06 | -30.15 | 282 |
| 34 | Keltner breakout · 1h | breakout | 80.85 | -19.15 | 114 | 23.7 | -18.63 | -3.88 | -25.65 | 175 |
| 35 | Volume breakout · 1h | breakout | 80.14 | -19.86 | 155 | 27.7 | -13.81 | -3.23 | -21.11 | 91 |
| 36 | MFI reversion · 1h | reversion | 79.55 | -20.45 | 377 | 35.8 | -16.65 | -2.12 | -23.02 | 159 |
| 37 | Stochastic reversion · 1h | reversion | 79.42 | -20.58 | 297 | 47.5 | -26.28 | -3.89 | -26.97 | 394 |
| 38 | Heikin-Ashi · 1h | trend | 78.70 | -21.30 | 430 | 24.7 | -35.55 | -6.69 | -38.20 | 656 |
| 39 | Opening range 15m | breakout | 78.29 | -21.71 | 512 | 31.2 | -18.31 | -4.98 | -21.36 | 716 |
| 40 | MACD cross · 1h | trend | 76.59 | -23.41 | 370 | 21.9 | -30.10 | -4.40 | -39.89 | 465 |
| 41 | Bollinger breakout · 1h | breakout | 76.09 | -23.91 | 179 | 22.3 | -22.48 | -4.66 | -29.88 | 241 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -22.09 | -0.72 | -57.50 | 41 |
| 43 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 44 | MACD zero-line · 1h | trend | 74.88 | -25.12 | 164 | 17.1 | -21.55 | -4.09 | -30.69 | 210 |
| 45 | Supertrend · 1h | trend | 74.73 | -25.27 | 172 | 14.0 | -29.76 | -5.27 | -36.25 | 222 |
| 46 | RSI momentum · 1h | momentum | 74.41 | -25.59 | 162 | 13.6 | -25.91 | -4.04 | -36.41 | 216 |
| 47 | EMA 20/50 cross · 1h | trend | 73.91 | -26.09 | 105 | 10.5 | -25.05 | -4.22 | -35.74 | 120 |
| 48 | Daily: Momentum burst | daily | 73.45 | -26.55 | 27 | 11.1 | -35.24 | -4.78 | -38.17 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.02 | -26.98 | 147 | 14.3 | -25.64 | -4.22 | -36.50 | 204 |
| 50 | Bollinger reversion · 1h | reversion | 72.93 | -27.07 | 290 | 41.0 | -30.07 | -4.62 | -34.84 | 370 |
| 51 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -33.62 | -4.86 | -35.86 | 453 |
| 52 | ROC + volume · 1h | momentum | 72.25 | -27.75 | 385 | 27.8 | -31.72 | -5.95 | -38.34 | 377 |
| 53 | Donchian 20/10 · 1h | breakout | 71.35 | -28.65 | 145 | 19.3 | -28.81 | -5.27 | -35.87 | 210 |
| 54 | OBV trend · 1h | momentum | 71.22 | -28.79 | 283 | 19.1 | -27.71 | -4.81 | -37.08 | 283 |
| 55 | Williams %R · 1h | reversion | 68.17 | -31.83 | 358 | 45.5 | -39.27 | -6.29 | -39.34 | 527 |
| 56 | Z-score reversion · 1h | reversion | 67.75 | -32.25 | 199 | 38.2 | -27.25 | -3.77 | -28.98 | 233 |
| 57 | EMA 9/21 cross · 1h | trend | 66.69 | -33.31 | 257 | 9.7 | -34.69 | -6.64 | -41.66 | 337 |
| 58 | Agent (ML meta-label) | meta | 66.05 | -33.95 | 1765 | 24.8 | -6.06 | -0.69 | -19.60 | 361 |
| 59 | VWAP momentum · 1h | momentum | 66.02 | -33.98 | 883 | 22.3 | -51.79 | -10.72 | -51.90 | 1218 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -33.31 | -4.94 | -34.46 | 222 |
| 61 | Candlestick reversal · 1h | reversion | 62.68 | -37.32 | 467 | 28.5 | -41.68 | -7.49 | -42.07 | 576 |
| 62 | Three white soldiers | momentum | 59.36 | -40.64 | 526 | 14.8 | -48.99 | -22.73 | -48.99 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.40 | -99.00 | 5286 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.86 | -25.62 | -79.87 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -44.48 | -93.50 | 2510 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.53 | -32.43 | -89.66 | 1926 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.09 | -40.61 | -91.10 | 2324 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.95 | -31.53 | -89.97 | 2177 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -54.24 | -97.88 | 3455 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -55.13 | -96.29 | 3419 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -32.84 | -93.47 | 2339 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.11 | -34.34 | -83.11 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -55.67 | -99.58 | 6014 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -43.17 | -92.22 | 2600 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.13 | -95.45 | 3452 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -78.66 | -99.82 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.18 | -44.25 | -92.18 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.13 | -25.26 | -75.18 | 1626 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -58.35 | -97.61 | 3501 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.91 | -63.98 | -98.91 | 4920 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.37 | -26.95 | -68.54 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -57.73 | -94.77 | 2776 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.10 | -39.16 | -85.10 | 1785 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -76.84 | -99.66 | 6336 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.98 | -32.41 | -90.02 | 2316 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.79 | -20.19 | -78.88 | 1784 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.86 | -37.07 | -90.91 | 2186 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.92 | -53.27 | -96.94 | 3868 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.13 | -57.29 | -89.13 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.14 | -30.06 | -66.14 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.53 | -23.20 | -71.58 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.62 | -18.90 | -79.78 | 1721 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.35 | -49.87 | -97.37 | 4304 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.23 | -99.93 | 8338 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T15:40 | Agent (ML meta-label) | buy | QQQ | 3.17 | — | entry |
| 2026-11-12T15:40 | Agent (ML meta-label) | buy | IWM | 5.50 | — | entry |
| 2026-11-12T15:40 | Agent (ML meta-label) | sell | PLTR | 7.33 | -0.02 | selected signal exited |
| 2026-11-12T15:40 | Agent (ML meta-label) | sell | GOOGL | 1.35 | 0.00 | selected signal exited |
| 2026-11-12T15:35 | Agent (ML meta-label) | buy | GOOGL | 1.35 | — | entry |
| 2026-11-12T15:35 | Agent (ML meta-label) | buy | AMZN | 5.99 | — | following Supertrend |
| 2026-11-12T15:35 | Agent (ML meta-label) | sell | SPY | 7.34 | -0.01 | selected signal exited |
| 2026-11-12T15:35 | Three white soldiers | sell | NVDA | 14.72 | -0.17 | exit signal |
| 2026-11-12T15:35 | Opening range 15m | buy | TECL | 3.93 | — | rebalance up |
| 2026-11-12T15:35 | Opening range 15m | sell | UPRO | 3.93 | -0.01 | rebalance down |
| 2026-11-12T15:30 | Agent (ML meta-label) | buy | TQQQ | 7.33 | — | entry |
| 2026-11-12T15:30 | Agent (ML meta-label) | buy | SQQQ | 7.35 | — | following RSI momentum |
| 2026-11-12T15:30 | Agent (ML meta-label) | buy | PLTR | 7.35 | — | entry |
| 2026-11-12T15:30 | Agent (ML meta-label) | buy | MSTR | 7.35 | — | entry |
| 2026-11-12T15:30 | Agent (ML meta-label) | buy | MSFT | 7.35 | — | entry |
| 2026-11-12T15:30 | Agent (ML meta-label) | sell | TSLA | 9.14 | -0.04 | rebalance down |
| 2026-11-12T15:30 | Agent (ML meta-label) | sell | TECL | 6.13 | -0.05 | rebalance down |
| 2026-11-12T15:30 | Agent (ML meta-label) | sell | SPY | 9.19 | -0.00 | rebalance down |
| 2026-11-12T15:30 | Agent (ML meta-label) | sell | AMD | 5.87 | -0.00 | rebalance down |
| 2026-11-12T15:30 | Agent (aggressive) | buy | LABU | 41.36 | — | following MFI reversion |
| 2026-11-12T15:30 | Agent | buy | LABU | 17.08 | — | following MFI reversion |
| 2026-11-12T15:30 | MFI reversion · 1h | buy | MSFT | 19.94 | — | entry |
| 2026-11-12T15:30 | MFI reversion · 1h | sell | AAPL | 19.74 | 0.03 | exit signal |
| 2026-11-12T15:30 | Williams %R · 1h | buy | SQQQ | 8.48 | — | entry signal |
| 2026-11-12T15:30 | Williams %R · 1h | buy | MSFT | 8.54 | — | entry signal |
| 2026-11-12T15:30 | Williams %R · 1h | buy | AMZN | 8.54 | — | entry signal |
| 2026-11-12T15:30 | Williams %R · 1h | sell | XRP-USD | 5.02 | -0.06 | rebalance down |
| 2026-11-12T15:30 | Williams %R · 1h | sell | SOL-USD | 5.11 | -0.03 | rebalance down |
| 2026-11-12T15:30 | Williams %R · 1h | sell | ETHU | 4.92 | -0.27 | rebalance down |
| 2026-11-12T15:30 | Williams %R · 1h | sell | ETH-USD | 5.16 | -0.03 | rebalance down |
| 2026-11-12T15:30 | Williams %R · 1h | sell | DOGE-USD | 5.08 | -0.07 | rebalance down |
| 2026-11-12T15:30 | Stochastic reversion · 1h | buy | META | 10.32 | — | entry signal |
| 2026-11-12T15:30 | Connors RSI(2) · 1h | buy | TSLA | 20.23 | — | entry signal |
| 2026-11-12T15:30 | Connors RSI(2) · 1h | buy | IWM | 20.23 | — | entry signal |
| 2026-11-12T15:30 | Candlestick reversal · 1h | buy | MSTR | 11.15 | — | entry signal |
| 2026-11-12T15:30 | Candlestick reversal · 1h | sell | SQQQ | 4.24 | 0.12 | rebalance down |
| 2026-11-12T15:30 | Candlestick reversal · 1h | sell | ETHU | 3.24 | -0.06 | rebalance down |
| 2026-11-12T15:30 | Candlestick reversal · 1h | sell | ETH-USD | 3.67 | -0.01 | rebalance down |
| 2026-11-12T15:30 | Volume breakout · 1h | buy | AAPL | 20.04 | — | entry signal |
| 2026-11-12T15:30 | Keltner breakout · 1h | buy | AAPL | 5.01 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 15:40:05.000121+00:00 -> 2026-11-12 15:50:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
