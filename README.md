# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T17:09:05.000148+00:00 · 57162 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.12 (-13.88%)

Closed trades 184, win rate 35.3%, fees £5.45, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.35 | +0.21 |

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

Today: 23852 decisions in 2708 calls, $0.3051 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T17:09 | 10 / 12 / 8 | cash |  |
| Breezy | 2026-11-12T17:09 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-12T17:09 | 5 / 23 / 2 | COIN 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.47 | 17.47 | 0 | — | 16.32 | 5.31 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.28 | 14.29 | 21 | 66.7 | 20.78 | 4.05 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 113.38 | 13.38 | 33 | 27.3 | 21.82 | 3.18 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.80 | 1.86 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.49 | 1.49 | 137 | 33.6 | 8.02 | 3.06 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.61 | 0.61 | 192 | 32.8 | 6.63 | 1.88 | -9.06 | 233 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold SPY | benchmark | 98.99 | -1.01 | 0 | — | -0.67 | -0.07 | -6.18 | 1 |
| 11 | Agent (rotation) | meta | 98.87 | -1.14 | 189 | 30.2 | -1.00 | -0.30 | -8.93 | 169 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.85 | 0.06 | -18.69 | 5 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 98.28 | -1.72 | 1 | 0.0 | -1.66 | -1.09 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.34 | -3.66 | 0 | — | -3.90 | -0.99 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.36 | -4.64 | 142 | 47.2 | -12.86 | -3.33 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.06 | -4.95 | 43 | 39.5 | -6.38 | -1.24 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.66 | -5.34 | 0 | — | -2.79 | -0.69 | -10.64 | 1 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 94.38 | -5.62 | 1 | 0.0 | -5.89 | -1.22 | -16.91 | 2 |
| 19 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 21 | Trend pullback · 1h | trend | 92.23 | -7.77 | 109 | 22.9 | -13.51 | -4.69 | -18.42 | 75 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -7.23 | -2.29 | -14.89 | 74 |
| 23 | Opening range 30m | breakout | 86.67 | -13.33 | 418 | 32.8 | -9.75 | -3.05 | -14.11 | 603 |
| 24 | Parabolic SAR · 1h | trend | 86.66 | -13.34 | 171 | 27.5 | -13.22 | -2.79 | -21.98 | 220 |
| 25 | Agent | meta | 86.12 | -13.88 | 184 | 35.3 | -14.71 | -7.31 | -15.61 | 210 |
| 26 | Daily: Bullish score | daily | 84.78 | -15.22 | 16 | 18.8 | -11.84 | -1.64 | -19.56 | 15 |
| 27 | Agent (aggressive) | meta | 84.50 | -15.50 | 90 | 34.4 | -15.83 | -4.36 | -18.51 | 100 |
| 28 | Hold BTC | benchmark | 84.48 | -15.52 | 1 | 0.0 | -7.27 | -0.98 | -18.34 | 1 |
| 29 | Donchian 55/20 · 1h | breakout | 84.16 | -15.84 | 73 | 13.7 | -22.21 | -4.63 | -29.68 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.17 | -16.83 | 2 | 0.0 | -7.75 | -0.82 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.90 | -18.10 | 114 | 23.7 | -17.59 | -3.62 | -25.87 | 176 |
| 32 | ADX DI cross · 1h | trend | 81.48 | -18.52 | 191 | 19.4 | -20.65 | -3.32 | -29.85 | 269 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -25.73 | -1.31 | -45.81 | 24 |
| 34 | Connors RSI(2) · 1h | reversion | 81.17 | -18.83 | 210 | 40.5 | -19.69 | -6.63 | -20.32 | 120 |
| 35 | Volume breakout · 1h | breakout | 80.28 | -19.72 | 156 | 28.2 | -13.70 | -3.20 | -21.15 | 92 |
| 36 | MFI reversion · 1h | reversion | 80.25 | -19.75 | 378 | 36.0 | -17.05 | -2.17 | -23.02 | 164 |
| 37 | Stochastic reversion · 1h | reversion | 79.62 | -20.38 | 297 | 47.5 | -26.65 | -3.94 | -27.36 | 389 |
| 38 | Opening range 15m | breakout | 79.09 | -20.91 | 512 | 31.2 | -17.32 | -4.63 | -21.36 | 725 |
| 39 | Heikin-Ashi · 1h | trend | 78.16 | -21.84 | 431 | 24.6 | -35.93 | -6.75 | -38.20 | 656 |
| 40 | MACD cross · 1h | trend | 77.60 | -22.40 | 370 | 21.9 | -27.23 | -4.00 | -38.93 | 463 |
| 41 | Bollinger breakout · 1h | breakout | 76.48 | -23.52 | 179 | 22.3 | -22.10 | -4.59 | -29.88 | 242 |
| 42 | MACD zero-line · 1h | trend | 76.07 | -23.93 | 164 | 17.1 | -21.63 | -4.36 | -31.17 | 207 |
| 43 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -19.27 | -0.54 | -57.50 | 41 |
| 44 | Supertrend · 1h | trend | 75.93 | -24.07 | 172 | 14.0 | -29.58 | -5.24 | -36.13 | 225 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 46 | RSI momentum · 1h | momentum | 75.37 | -24.63 | 162 | 13.6 | -23.70 | -3.64 | -35.96 | 214 |
| 47 | Daily: Momentum burst | daily | 75.11 | -24.89 | 27 | 11.1 | -33.59 | -4.54 | -38.17 | 33 |
| 48 | EMA 20/50 cross · 1h | trend | 74.97 | -25.03 | 105 | 10.5 | -26.61 | -4.47 | -38.13 | 119 |
| 49 | Triple EMA stack · 1h | trend | 73.60 | -26.40 | 147 | 14.3 | -26.73 | -4.40 | -37.93 | 205 |
| 50 | ROC + volume · 1h | momentum | 73.50 | -26.50 | 385 | 27.8 | -30.82 | -5.74 | -38.37 | 377 |
| 51 | Bollinger reversion · 1h | reversion | 72.73 | -27.27 | 290 | 41.0 | -30.30 | -4.65 | -34.80 | 378 |
| 52 | Donchian 20/10 · 1h | breakout | 72.51 | -27.49 | 145 | 19.3 | -27.54 | -4.98 | -35.87 | 211 |
| 53 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -33.67 | -4.94 | -35.88 | 455 |
| 54 | OBV trend · 1h | momentum | 71.97 | -28.03 | 285 | 19.6 | -26.43 | -4.50 | -36.59 | 286 |
| 55 | Williams %R · 1h | reversion | 68.26 | -31.74 | 358 | 45.5 | -41.85 | -6.86 | -42.02 | 533 |
| 56 | Z-score reversion · 1h | reversion | 67.78 | -32.22 | 199 | 38.2 | -27.23 | -3.77 | -28.98 | 234 |
| 57 | EMA 9/21 cross · 1h | trend | 67.58 | -32.42 | 257 | 9.7 | -33.59 | -6.24 | -41.74 | 337 |
| 58 | VWAP momentum · 1h | momentum | 66.84 | -33.16 | 883 | 22.3 | -51.41 | -10.64 | -52.53 | 1221 |
| 59 | Agent (ML meta-label) | meta | 66.79 | -33.21 | 1781 | 25.0 | -17.82 | -2.33 | -24.54 | 344 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -34.13 | -4.68 | -35.13 | 246 |
| 61 | Candlestick reversal · 1h | reversion | 62.87 | -37.13 | 467 | 28.5 | -42.48 | -7.65 | -42.64 | 594 |
| 62 | Three white soldiers | momentum | 58.91 | -41.09 | 534 | 14.6 | -49.40 | -22.70 | -49.40 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.97 | -99.01 | 5277 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.01 | -25.98 | -80.05 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.62 | -45.61 | -93.64 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.40 | -32.18 | -89.67 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.01 | -40.02 | -91.05 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.99 | -31.21 | -90.16 | 2197 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -54.30 | -97.88 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -54.59 | -96.30 | 3422 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.52 | -32.67 | -93.53 | 2331 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.96 | -33.86 | -83.07 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.78 | -99.58 | 5995 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -43.39 | -92.24 | 2606 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -37.11 | -95.45 | 3460 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -78.90 | -99.82 | 6143 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.21 | -44.08 | -92.24 | 2273 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.15 | -25.32 | -75.22 | 1632 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -57.90 | -97.61 | 3506 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.87 | -64.09 | -98.89 | 4907 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.40 | -27.05 | -68.47 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -58.14 | -94.78 | 2788 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.14 | -39.36 | -85.18 | 1798 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.88 | -99.66 | 6334 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.79 | -32.32 | -89.97 | 2302 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.32 | -20.13 | -78.70 | 1774 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.69 | -36.86 | -90.87 | 2180 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.88 | -53.30 | -96.92 | 3857 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -57.32 | -89.15 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.21 | -30.27 | -66.21 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.28 | -22.95 | -71.45 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.35 | -19.00 | -79.66 | 1720 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.30 | -49.76 | -97.33 | 4294 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.01 | -99.93 | 8344 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T17:05 | Agent (ML meta-label) | sell | QQQ | 3.71 | 0.00 | selected signal exited |
| 2026-11-12T17:02 | Williams %R · 1h | buy | MSTR | 3.41 | — | rebalance up |
| 2026-11-12T17:02 | Williams %R · 1h | sell | SQQQ | 3.41 | -0.08 | rebalance down |
| 2026-11-12T17:00 | MFI reversion · 1h | buy | XRP-USD | 1.45 | — | entry signal |
| 2026-11-12T17:00 | MFI reversion · 1h | buy | NVDA | 10.04 | — | entry |
| 2026-11-12T17:00 | MFI reversion · 1h | sell | MSFT | 11.49 | 0.04 | target is flat |
| 2026-11-12T17:00 | Williams %R · 1h | buy | MSTR | 1.42 | — | entry |
| 2026-11-12T17:00 | Williams %R · 1h | buy | META | 4.88 | — | entry |
| 2026-11-12T17:00 | Williams %R · 1h | buy | LABU | 4.88 | — | entry |
| 2026-11-12T17:00 | Williams %R · 1h | buy | COIN | 4.88 | — | entry |
| 2026-11-12T17:00 | Williams %R · 1h | buy | BTC-USD | 4.88 | — | entry signal |
| 2026-11-12T17:00 | Williams %R · 1h | buy | BITX | 4.88 | — | entry |
| 2026-11-12T17:00 | Williams %R · 1h | sell | XRP-USD | 3.69 | -0.03 | rebalance down |
| 2026-11-12T17:00 | Williams %R · 1h | sell | SOL-USD | 3.68 | -0.00 | rebalance down |
| 2026-11-12T17:00 | Williams %R · 1h | sell | MSFT | 3.69 | 0.01 | rebalance down |
| 2026-11-12T17:00 | Williams %R · 1h | sell | ETHU | 3.69 | -0.18 | rebalance down |
| 2026-11-12T17:00 | Williams %R · 1h | sell | ETH-USD | 3.67 | -0.01 | rebalance down |
| 2026-11-12T17:00 | Williams %R · 1h | sell | DOGE-USD | 3.76 | -0.00 | rebalance down |
| 2026-11-12T17:00 | Williams %R · 1h | sell | AMZN | 3.66 | -0.00 | rebalance down |
| 2026-11-12T16:45 | Agent (ML meta-label) | buy | QQQ | 3.70 | — | entry |
| 2026-11-12T16:45 | Agent (ML meta-label) | sell | BITX | 4.14 | -0.05 | selected signal exited |
| 2026-11-12T16:45 | Volume breakout · 1h | buy | AAPL | 20.04 | — | entry |
| 2026-11-12T16:45 | OBV trend · 1h | buy | SPY | 3.79 | — | entry |
| 2026-11-12T16:40 | Agent (ML meta-label) | buy | SOXL | 3.48 | — | entry |
| 2026-11-12T16:40 | Agent (ML meta-label) | sell | PLTR | 3.48 | 0.00 | selected signal exited |
| 2026-11-12T16:40 | OBV trend · 1h | buy | TNA | 4.20 | — | rebalance up |
| 2026-11-12T16:40 | OBV trend · 1h | sell | SPY | 8.00 | 0.02 | target is flat |
| 2026-11-12T16:40 | ADX DI cross · 1h | buy | TQQQ | 4.12 | — | rebalance up |
| 2026-11-12T16:40 | ADX DI cross · 1h | sell | PLTR | 4.12 | 0.11 | rebalance down |
| 2026-11-12T16:40 | Three white soldiers | sell | MSTR | 14.69 | -0.06 | exit signal |
| 2026-11-12T16:40 | Three white soldiers | sell | DOGE-USD | 14.71 | -0.12 | exit signal |
| 2026-11-12T16:40 | Three white soldiers | sell | BTC-USD | 14.74 | -0.11 | exit signal |
| 2026-11-12T16:40 | Three white soldiers | sell | BITX | 14.77 | -0.05 | exit signal |
| 2026-11-12T16:40 | Opening range 30m | sell | ETHU | 6.12 | -0.13 | stop-loss |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | PLTR | 3.48 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | NVDA | 3.72 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | IWM | 3.72 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | buy | AAPL | 3.72 | — | entry |
| 2026-11-12T16:35 | Agent (ML meta-label) | sell | TQQQ | 3.78 | 0.08 | rebalance down |
| 2026-11-12T16:35 | Agent (ML meta-label) | sell | SQQQ | 3.47 | -0.08 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 17:09:05.000148+00:00 -> 2026-11-12 17:19:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
