# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T19:34:05.000152+00:00 · 38182 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 114, win rate 39.5%, fees £3.48, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| META | 18.03 | +0.00 |
| PLTR | 18.07 | +0.06 |

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

Today: 34117 decisions in 2819 calls, $0.4212 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T19:34 | 4 / 16 / 10 | cash |  |
| Breezy | 2026-10-27T19:34 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-27T19:34 | 8 / 19 / 3 | COIN 57% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.19 | 7.19 | 0 | — | 8.23 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.69 | 6.69 | 14 | 71.4 | 3.99 | 1.31 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.02 | 5.02 | 20 | 50.0 | 7.71 | 2.52 | -4.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.78 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.13 | 1.12 | 0 | — | 2.10 | 1.20 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.92 | -3.89 | -14.07 | 150 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.61 | -0.39 | 0 | — | 0.13 | 0.12 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.91 | -1.09 | 83 | 34.9 | 8.22 | 3.81 | -2.29 | 98 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.73 | -2.27 | 14 | 21.4 | -3.20 | -4.33 | -4.04 | 22 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.71 | -2.29 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.32 | -2.06 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.45 | -3.55 | 122 | 31.1 | -1.84 | -1.04 | -6.39 | 173 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.02 | -3.98 | 0 | — | -5.80 | -2.38 | -7.83 | 1 |
| 16 | Gap and go | momentum | 95.76 | -4.24 | 116 | 28.4 | 3.81 | 1.29 | -8.76 | 207 |
| 17 | Hold BTC | benchmark | 95.75 | -4.25 | 0 | — | 2.51 | 0.49 | -9.28 | 1 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.77 | 1.02 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 20 | Opening range 30m | breakout | 93.92 | -6.08 | 272 | 34.2 | -9.18 | -2.71 | -17.21 | 592 |
| 21 | Donchian 55/20 · 1h | breakout | 93.69 | -6.31 | 49 | 16.3 | -12.87 | -2.87 | -15.40 | 97 |
| 22 | Trend pullback · 1h | trend | 93.63 | -6.37 | 96 | 22.9 | -21.93 | -7.02 | -22.19 | 116 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.59 | -7.41 | 0 | — | -2.80 | -0.30 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.27 | -7.73 | 121 | 25.6 | -20.29 | -5.03 | -23.02 | 248 |
| 25 | Copy: Insider buying | copy | 92.23 | -7.77 | 29 | 37.9 | -19.54 | -3.85 | -22.94 | 63 |
| 26 | Daily: Momentum burst | daily | 91.95 | -8.04 | 13 | 15.4 | -18.15 | -3.49 | -19.33 | 39 |
| 27 | ADX DI cross · 1h | trend | 91.79 | -8.21 | 120 | 18.3 | -14.51 | -3.18 | -16.24 | 272 |
| 28 | Daily: Bullish score | daily | 91.55 | -8.45 | 11 | 18.2 | -6.85 | -0.78 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.24 | -8.76 | 12 | 41.7 | -14.29 | -1.29 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.70 | -2.22 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 90.99 | -9.01 | 52 | 23.1 | -4.67 | -1.24 | -12.18 | 94 |
| 32 | Volume breakout · 1h | breakout | 90.12 | -9.88 | 108 | 25.9 | -11.59 | -2.39 | -16.00 | 116 |
| 33 | Agent | meta | 90.11 | -9.89 | 114 | 39.5 | -10.43 | -6.79 | -12.20 | 211 |
| 34 | Bollinger breakout · 1h | breakout | 88.91 | -11.09 | 109 | 26.6 | -11.95 | -2.35 | -18.15 | 247 |
| 35 | Agent (aggressive) | meta | 88.34 | -11.66 | 57 | 36.8 | -11.02 | -3.65 | -14.77 | 97 |
| 36 | Stochastic reversion · 1h | reversion | 87.76 | -12.24 | 205 | 47.3 | -21.39 | -4.01 | -22.58 | 389 |
| 37 | Opening range 15m | breakout | 87.37 | -12.63 | 338 | 30.8 | -14.06 | -3.98 | -17.87 | 714 |
| 38 | Keltner breakout · 1h | breakout | 87.24 | -12.76 | 74 | 23.0 | -19.26 | -3.73 | -23.13 | 187 |
| 39 | Z-score reversion · 1h | reversion | 86.78 | -13.22 | 125 | 36.0 | -12.82 | -2.05 | -21.48 | 211 |
| 40 | Supertrend · 1h | trend | 85.78 | -14.21 | 114 | 14.0 | -25.24 | -5.15 | -28.06 | 232 |
| 41 | Connors RSI(2) · 1h | reversion | 85.12 | -14.88 | 176 | 40.9 | -24.35 | -7.48 | -24.90 | 184 |
| 42 | RSI momentum · 1h | momentum | 85.11 | -14.89 | 104 | 15.4 | -21.05 | -4.27 | -23.95 | 212 |
| 43 | MACD cross · 1h | trend | 84.40 | -15.60 | 244 | 22.1 | -27.79 | -5.50 | -29.89 | 476 |
| 44 | EMA 20/50 cross · 1h | trend | 84.40 | -15.60 | 73 | 11.0 | -23.01 | -4.61 | -24.63 | 134 |
| 45 | Ichimoku · 1h | trend | 84.11 | -15.89 | 68 | 11.8 | -19.79 | -4.04 | -24.73 | 111 |
| 46 | Triple EMA stack · 1h | trend | 83.67 | -16.33 | 101 | 14.9 | -28.45 | -5.45 | -31.55 | 202 |
| 47 | MFI reversion · 1h | reversion | 83.52 | -16.48 | 274 | 32.1 | -16.13 | -2.51 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.46 | -17.54 | 230 | 45.2 | -24.50 | -3.52 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 81.98 | -18.02 | 99 | 20.2 | -24.20 | -4.66 | -26.49 | 221 |
| 50 | Williams %R · 1h | reversion | 81.93 | -18.07 | 232 | 47.0 | -35.19 | -6.01 | -36.10 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.32 | -18.68 | 111 | 15.3 | -23.44 | -5.00 | -24.88 | 229 |
| 52 | Agent (ML meta-label) | meta | 80.76 | -19.25 | 977 | 20.5 | -7.35 | -1.20 | -17.32 | 358 |
| 53 | Bollinger reversion · 1h | reversion | 80.73 | -19.27 | 182 | 37.4 | -29.16 | -6.02 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.52 | -19.48 | 209 | 17.7 | -30.99 | -6.55 | -33.04 | 297 |
| 55 | RSI(14) reversion · 1h | reversion | 80.40 | -19.59 | 107 | 27.1 | -16.46 | -2.87 | -24.48 | 195 |
| 56 | ROC + volume · 1h | momentum | 79.25 | -20.75 | 259 | 25.9 | -31.58 | -6.23 | -33.25 | 386 |
| 57 | Heikin-Ashi · 1h | trend | 78.39 | -21.61 | 298 | 22.8 | -43.22 | -9.59 | -44.60 | 671 |
| 58 | Three white soldiers | momentum | 77.36 | -22.64 | 321 | 19.0 | -44.39 | -21.47 | -45.10 | 608 |
| 59 | Candlestick reversal · 1h | reversion | 77.29 | -22.71 | 285 | 29.5 | -35.28 | -6.81 | -36.12 | 569 |
| 60 | VWAP momentum · 1h | momentum | 76.99 | -23.01 | 575 | 22.3 | -49.31 | -10.82 | -51.08 | 1239 |
| 61 | EMA 9/21 cross · 1h | trend | 76.66 | -23.34 | 176 | 10.8 | -30.38 | -6.48 | -32.35 | 338 |
| 62 | Max aggression: 1-day momentum | meta | 72.16 | -27.84 | 20 | 30.0 | -37.95 | -2.48 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.77 | -46.23 | 808 | 22.4 | -74.67 | -27.39 | -75.20 | 1575 |
| 64 | Volume breakout | breakout | 52.39 | -47.61 | 484 | 12.8 | -63.53 | -26.21 | -64.15 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -45.01 | -98.87 | 5106 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.20 | -23.65 | -80.04 | 1411 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.70 | -45.99 | -93.79 | 2542 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.09 | -30.74 | -89.25 | 1922 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -38.84 | -91.55 | 2346 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -32.39 | -90.21 | 2183 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -54.65 | -97.87 | 3510 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.13 | -59.57 | -96.18 | 3370 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -37.22 | -94.05 | 2459 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.36 | -34.25 | -82.60 | 1693 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -56.28 | -99.43 | 5770 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.78 | -44.85 | -92.98 | 2634 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -40.02 | -95.39 | 3384 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.40 | -99.78 | 6181 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -46.78 | -92.35 | 2319 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -67.94 | -97.78 | 3595 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.66 | -98.65 | 4788 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.52 | -30.18 | -68.76 | 1185 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -59.31 | -94.68 | 2774 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.28 | -40.00 | -84.59 | 1816 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -69.30 | -99.60 | 6297 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -29.41 | -88.27 | 2224 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.62 | -19.18 | -76.90 | 1679 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.48 | -37.71 | -90.62 | 2260 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -49.14 | -96.26 | 3810 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.07 | -51.46 | -90.09 | 2132 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.63 | -24.78 | -73.52 | 1275 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.23 | -18.20 | -76.42 | 1582 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.56 | -51.38 | -96.56 | 4197 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -114.77 | -99.92 | 8302 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T19:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 97.78 | — | entry |
| 2026-10-27T19:30 | Volume breakout · 1h | buy | TNA | 7.48 | — | entry |
| 2026-10-27T19:30 | Volume breakout · 1h | buy | TECL | 7.51 | — | entry |
| 2026-10-27T19:30 | Volume breakout · 1h | buy | SOXL | 7.51 | — | entry |
| 2026-10-27T19:30 | Volume breakout · 1h | buy | LABU | 7.51 | — | entry signal |
| 2026-10-27T19:30 | Volume breakout · 1h | buy | AMZN | 7.51 | — | entry signal |
| 2026-10-27T19:30 | Volume breakout · 1h | sell | TSLA | 5.38 | 0.03 | rebalance down |
| 2026-10-27T19:30 | Volume breakout · 1h | sell | TQQQ | 5.38 | 0.11 | rebalance down |
| 2026-10-27T19:30 | Volume breakout · 1h | sell | SPY | 5.38 | -0.00 | rebalance down |
| 2026-10-27T19:30 | Volume breakout · 1h | sell | QQQ | 5.34 | 0.04 | rebalance down |
| 2026-10-27T19:30 | Volume breakout · 1h | sell | NVDA | 5.33 | -0.02 | rebalance down |
| 2026-10-27T19:30 | Volume breakout · 1h | sell | ETH-USD | 5.28 | -0.05 | rebalance down |
| 2026-10-27T19:30 | Volume breakout · 1h | sell | AMD | 5.36 | 0.07 | rebalance down |
| 2026-10-27T19:30 | Heikin-Ashi · 1h | buy | XRP-USD | 4.36 | — | entry |
| 2026-10-27T19:30 | Heikin-Ashi · 1h | sell | ETHU | 4.59 | -0.03 | exit signal |
| 2026-10-27T19:30 | Supertrend · 1h | buy | GOOGL | 4.49 | — | entry signal |
| 2026-10-27T19:30 | Supertrend · 1h | sell | MSFT | 4.49 | 0.01 | rebalance down |
| 2026-10-27T19:30 | Volume breakout | sell | LABU | 13.07 | -0.08 | exit signal |
| 2026-10-27T19:25 | Squeeze breakout · 1h | buy | ETH-USD | 4.55 | — | rebalance up |
| 2026-10-27T19:25 | Squeeze breakout · 1h | sell | PLTR | 4.55 | -0.01 | rebalance down |
| 2026-10-27T19:25 | Volume breakout | sell | SOL-USD | 13.03 | -0.12 | exit signal |
| 2026-10-27T19:25 | ROC + volume | buy | SOXL | 13.46 | — | entry |
| 2026-10-27T19:21 | ROC + volume | buy | TSLA | 13.46 | — | entry signal |
| 2026-10-27T19:21 | ROC + volume | sell | SOXL | 13.48 | -0.02 | target is flat |
| 2026-10-27T19:21 | ROC + volume | sell | MSTR | 13.41 | -0.09 | exit signal |
| 2026-10-27T19:15 | CCI reversion · 1h | buy | ETHU | 4.14 | — | rebalance up |
| 2026-10-27T19:15 | Volume breakout | buy | GOOGL | 13.13 | — | entry signal |
| 2026-10-27T19:10 | Three white soldiers | buy | SPY | 19.35 | — | entry signal |
| 2026-10-27T19:10 | Volume breakout | buy | SOL-USD | 13.15 | — | entry signal |
| 2026-10-27T19:10 | Volume breakout | buy | LABU | 13.15 | — | entry |
| 2026-10-27T19:10 | ROC + volume | buy | SOXL | 13.50 | — | entry signal |
| 2026-10-27T19:10 | ROC + volume | buy | MSTR | 13.50 | — | entry signal |
| 2026-10-27T19:10 | ROC + volume | buy | LABU | 13.50 | — | entry |
| 2026-10-27T19:06 | Day trade: Stocks in Play ORB | buy | SOXL | 24.74 | — | entry |
| 2026-10-27T19:06 | Agent | buy | META | 18.02 | — | following VWAP reversion |
| 2026-10-27T19:06 | MFI reversion · 1h | sell | GOOGL | 20.85 | -0.02 | target is flat |
| 2026-10-27T19:06 | VWAP momentum · 1h | buy | AMZN | 3.85 | — | entry |
| 2026-10-27T19:06 | VWAP momentum · 1h | sell | PLTR | 3.86 | 0.01 | target is flat |
| 2026-10-27T19:06 | Gap and go | sell | SOXL | 23.98 | 0.08 | target is flat |
| 2026-10-27T19:06 | ROC + volume | sell | LABU | 13.51 | 0.02 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 19:34:05.000152+00:00 -> 2026-10-27 19:44:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
