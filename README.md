# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T18:05:05.000139+00:00 · 53657 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.49 (-12.52%)

Closed trades 159, win rate 35.8%, fees £4.91, max drawdown -13.02%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.51 | -0.09 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 25329 decisions in 2835 calls, $0.3229 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T18:05 | 4 / 10 / 16 | cash |  |
| Breezy | 2026-11-09T18:05 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-09T18:05 | 4 / 25 / 1 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.64 | 16.64 | 19 | 68.4 | 16.71 | 3.48 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.49 | 11.49 | 0 | — | 12.57 | 4.34 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.05 | 11.05 | 30 | 26.7 | 18.99 | 2.94 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.16 | 3.15 | 30 | 43.3 | 2.88 | 0.80 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.97 | 0.97 | 0 | — | 4.49 | 1.32 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.93 | 0.93 | 123 | 35.0 | 9.27 | 3.83 | -2.27 | 89 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.32 | 0.32 | 7 | 42.9 | -1.67 | 0.11 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 97.92 | -2.08 | 179 | 29.1 | 2.83 | 0.91 | -9.06 | 241 |
| 11 | Agent (rotation) | meta | 97.54 | -2.46 | 176 | 27.8 | -3.04 | -1.34 | -9.58 | 161 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.55 | -3.45 | 0 | — | -1.93 | -0.55 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.27 | -5.73 | 0 | — | -3.86 | -1.03 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Trend pullback · 1h | trend | 92.65 | -7.35 | 108 | 23.1 | -13.60 | -5.10 | -17.86 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.64 | -7.36 | 0 | — | -4.45 | -1.20 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 89.97 | -10.03 | 377 | 32.4 | -14.65 | -4.71 | -15.99 | 598 |
| 22 | Copy: Insider buying | copy | 89.21 | -10.79 | 40 | 37.5 | -11.46 | -2.65 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.08 | -2.83 | -14.15 | 77 |
| 24 | Agent | meta | 87.49 | -12.52 | 159 | 35.8 | -13.40 | -7.01 | -13.91 | 203 |
| 25 | Hold BTC | benchmark | 86.84 | -13.16 | 1 | 0.0 | -5.10 | -0.60 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.33 | -13.67 | 15 | 20.0 | -9.72 | -1.40 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.69 | -14.31 | 167 | 26.9 | -11.24 | -2.04 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 84.33 | -15.68 | 75 | 32.0 | -15.72 | -4.45 | -18.49 | 94 |
| 29 | Donchian 55/20 · 1h | breakout | 83.76 | -16.24 | 71 | 14.1 | -16.30 | -3.43 | -21.91 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.56 | -16.44 | 2 | 0.0 | -8.77 | -0.99 | -24.16 | 1 |
| 31 | Opening range 15m | breakout | 83.18 | -16.82 | 466 | 30.5 | -19.23 | -5.54 | -20.97 | 735 |
| 32 | Stochastic reversion · 1h | reversion | 83.03 | -16.96 | 279 | 48.4 | -23.53 | -3.49 | -27.71 | 385 |
| 33 | Keltner breakout · 1h | breakout | 81.65 | -18.35 | 107 | 23.4 | -23.48 | -4.94 | -25.14 | 182 |
| 34 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.79 | -19.21 | 205 | 40.0 | -19.28 | -6.45 | -19.64 | 125 |
| 36 | Heikin-Ashi · 1h | trend | 79.57 | -20.43 | 397 | 22.9 | -38.50 | -7.26 | -41.86 | 681 |
| 37 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -38.91 | -2.61 | -44.97 | 25 |
| 38 | MFI reversion · 1h | reversion | 79.22 | -20.78 | 347 | 34.0 | -17.54 | -2.25 | -21.33 | 164 |
| 39 | ADX DI cross · 1h | trend | 79.13 | -20.87 | 179 | 18.4 | -25.59 | -4.32 | -28.65 | 272 |
| 40 | CCI reversion · 1h | reversion | 78.69 | -21.31 | 309 | 44.0 | -24.86 | -3.82 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 76.98 | -23.02 | 170 | 22.9 | -22.44 | -4.63 | -27.77 | 241 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.25 | -4.04 | -32.96 | 372 |
| 44 | MACD cross · 1h | trend | 75.05 | -24.95 | 349 | 22.6 | -33.55 | -5.50 | -39.64 | 485 |
| 45 | Williams %R · 1h | reversion | 75.01 | -24.99 | 335 | 46.9 | -34.47 | -5.46 | -37.62 | 543 |
| 46 | Z-score reversion · 1h | reversion | 74.89 | -25.11 | 176 | 36.4 | -20.58 | -2.98 | -27.66 | 228 |
| 47 | MACD zero-line · 1h | trend | 74.40 | -25.60 | 157 | 16.6 | -24.89 | -5.14 | -29.19 | 210 |
| 48 | EMA 20/50 cross · 1h | trend | 74.35 | -25.65 | 102 | 10.8 | -22.97 | -4.09 | -31.15 | 128 |
| 49 | Supertrend · 1h | trend | 73.22 | -26.78 | 167 | 13.2 | -31.08 | -5.77 | -34.46 | 236 |
| 50 | RSI momentum · 1h | momentum | 72.97 | -27.03 | 159 | 12.6 | -24.69 | -4.13 | -33.29 | 215 |
| 51 | Triple EMA stack · 1h | trend | 72.51 | -27.49 | 143 | 14.7 | -26.21 | -4.60 | -34.73 | 202 |
| 52 | OBV trend · 1h | momentum | 71.80 | -28.20 | 274 | 18.2 | -28.93 | -5.99 | -34.24 | 278 |
| 53 | ROC + volume · 1h | momentum | 71.39 | -28.61 | 349 | 25.5 | -36.90 | -7.00 | -39.39 | 387 |
| 54 | Daily: Momentum burst | daily | 70.54 | -29.46 | 26 | 11.5 | -38.23 | -5.40 | -39.42 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.37 | -29.63 | 142 | 19.7 | -31.98 | -5.95 | -35.64 | 210 |
| 56 | RSI(14) reversion · 1h | reversion | 67.97 | -32.03 | 160 | 30.6 | -31.23 | -4.74 | -34.44 | 247 |
| 57 | Agent (ML meta-label) | meta | 67.86 | -32.13 | 1591 | 23.8 | -10.87 | -1.95 | -19.90 | 340 |
| 58 | VWAP momentum · 1h | momentum | 67.53 | -32.47 | 807 | 21.7 | -51.87 | -11.14 | -53.62 | 1235 |
| 59 | Max aggression: 1-day momentum | meta | 66.93 | -33.07 | 27 | 25.9 | -32.90 | -1.75 | -57.50 | 42 |
| 60 | EMA 9/21 cross · 1h | trend | 65.54 | -34.47 | 247 | 9.7 | -40.17 | -7.75 | -41.71 | 331 |
| 61 | Candlestick reversal · 1h | reversion | 65.23 | -34.77 | 432 | 28.2 | -39.90 | -7.34 | -40.82 | 597 |
| 62 | Three white soldiers | momentum | 62.30 | -37.70 | 492 | 15.0 | -48.72 | -22.71 | -48.72 | 648 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.73 | -98.99 | 5272 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.00 | -26.40 | -80.06 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.23 | -46.63 | -93.30 | 2506 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -32.45 | -89.30 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.69 | -40.07 | -90.74 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -31.62 | -90.00 | 2183 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -54.94 | -97.71 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -57.74 | -96.29 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.58 | -32.69 | -93.64 | 2409 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.18 | -34.77 | -82.30 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -55.90 | -99.52 | 5969 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.35 | -43.17 | -92.53 | 2593 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.54 | -37.31 | -95.54 | 3404 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -75.58 | -99.80 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -44.14 | -91.78 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.47 | -24.83 | -75.87 | 1590 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -62.23 | -97.67 | 3502 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -63.54 | -98.84 | 4877 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.79 | -27.52 | -69.44 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -55.20 | -94.59 | 2733 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.94 | -37.11 | -85.00 | 1771 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.09 | -99.66 | 6368 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.63 | -32.70 | -89.67 | 2269 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.39 | -20.15 | -78.44 | 1747 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.58 | -36.56 | -90.70 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.75 | -52.65 | -96.79 | 3883 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -57.61 | -89.45 | 2153 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.01 | -29.05 | -66.26 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.43 | -23.34 | -72.00 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.58 | -19.11 | -79.73 | 1688 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -50.01 | -97.33 | 4320 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -108.50 | -99.93 | 8284 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T18:05 | Agent (ML meta-label) | buy | TECL | 2.17 | — | entry |
| 2026-11-09T18:05 | Agent (ML meta-label) | buy | AMD | 4.91 | — | entry |
| 2026-11-09T18:00 | Agent (ML meta-label) | buy | AAPL | 5.66 | — | entry |
| 2026-11-09T18:00 | Agent (ML meta-label) | sell | TECL | 5.65 | -0.02 | selected signal exited |
| 2026-11-09T18:00 | VWAP momentum · 1h | sell | XRP-USD | 3.50 | -0.05 | exit signal |
| 2026-11-09T18:00 | VWAP momentum · 1h | sell | SOL-USD | 3.02 | -0.05 | exit signal |
| 2026-11-09T18:00 | VWAP momentum · 1h | sell | ETH-USD | 1.46 | -0.01 | exit signal |
| 2026-11-09T18:00 | Heikin-Ashi · 1h | buy | COIN | 4.42 | — | entry |
| 2026-11-09T18:00 | Heikin-Ashi · 1h | sell | SOL-USD | 3.95 | -0.09 | exit signal |
| 2026-11-09T18:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.96 | -0.06 | exit signal |
| 2026-11-09T18:00 | Heikin-Ashi · 1h | sell | BTC-USD | 3.95 | -0.01 | exit signal |
| 2026-11-09T17:56 | Agent (ML meta-label) | buy | TECL | 3.67 | — | rebalance up |
| 2026-11-09T17:56 | Agent (ML meta-label) | sell | LABU | 5.08 | 0.01 | selected signal exited |
| 2026-11-09T17:56 | Agent (ML meta-label) | sell | AAPL | 5.65 | -0.01 | selected signal exited |
| 2026-11-09T17:56 | Three white soldiers | buy | LABU | 15.60 | — | entry signal |
| 2026-11-09T17:51 | Agent (ML meta-label) | buy | TECL | 2.00 | — | entry |
| 2026-11-09T17:51 | Agent (ML meta-label) | buy | LABU | 5.07 | — | following MFI reversion |
| 2026-11-09T17:51 | Agent (ML meta-label) | sell | GOOGL | 5.22 | 0.00 | selected signal exited |
| 2026-11-09T17:45 | Agent (ML meta-label) | buy | GOOGL | 5.22 | — | entry |
| 2026-11-09T17:40 | Opening range 30m | buy | COIN | 2.33 | — | entry |
| 2026-11-09T17:40 | Opening range 30m | sell | BITX | 2.33 | -0.02 | stop-loss |
| 2026-11-09T17:40 | Opening range 15m | buy | AAPL | 4.90 | — | entry |
| 2026-11-09T17:40 | Opening range 15m | sell | ETHU | 5.39 | -0.09 | exit signal |
| 2026-11-09T17:36 | Agent (ML meta-label) | buy | AAPL | 5.66 | — | entry |
| 2026-11-09T17:35 | Agent (ML meta-label) | buy | SPY | 3.50 | — | rebalance up |
| 2026-11-09T17:35 | Agent (ML meta-label) | sell | LABU | 5.81 | 0.03 | selected signal exited |
| 2026-11-09T17:35 | Agent (ML meta-label) | sell | AMD | 5.23 | 0.01 | selected signal exited |
| 2026-11-09T17:35 | Agent (ML meta-label) | sell | AAPL | 5.21 | -0.01 | selected signal exited |
| 2026-11-09T17:30 | Agent (ML meta-label) | buy | SPY | 2.68 | — | entry |
| 2026-11-09T17:30 | Agent (ML meta-label) | buy | BITX | 4.85 | — | entry |
| 2026-11-09T17:30 | MFI reversion · 1h | buy | UPRO | 3.56 | — | rebalance up |
| 2026-11-09T17:30 | MFI reversion · 1h | buy | NVDA | 4.43 | — | rebalance up |
| 2026-11-09T17:30 | MFI reversion · 1h | sell | PLTR | 7.99 | 0.26 | exit signal |
| 2026-11-09T17:30 | CCI reversion · 1h | sell | PLTR | 5.38 | 0.26 | exit signal |
| 2026-11-09T17:30 | Williams %R · 1h | buy | NVDA | 18.82 | — | entry signal |
| 2026-11-09T17:30 | Williams %R · 1h | buy | BITX | 18.82 | — | entry signal |
| 2026-11-09T17:30 | Williams %R · 1h | sell | MSFT | 18.98 | 0.07 | exit signal |
| 2026-11-09T17:30 | Stochastic reversion · 1h | buy | ETHU | 20.84 | — | entry signal |
| 2026-11-09T17:30 | Z-score reversion · 1h | buy | NVDA | 6.26 | — | entry signal |
| 2026-11-09T17:30 | Z-score reversion · 1h | buy | ETHU | 6.26 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 18:05:05.000139+00:00 -> 2026-11-09 18:15:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 18:05:05.000139+00:00 -> 2026-11-09 18:15:05.000139+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 18:05:05.000139+00:00 -> 2026-11-09 18:15:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
