# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T17:50:05.000122+00:00 · 45248 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.29 (-8.71%)

Closed trades 132, win rate 40.9%, fees £3.80, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.17 | -0.11 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BPRE 12%, ACN 12%, SCQCU 12%, NPB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 22416 decisions in 2628 calls, $0.2879 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T17:50 | 4 / 13 / 13 | cash |  |
| Breezy | 2026-11-02T17:50 | 0 / 22 / 8 | cash |  |
| Boozy | 2026-11-02T17:50 | 4 / 22 / 4 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Bollinger reversion | AMZN | 2.17 | +2.35% | 10 |
| Stochastic reversion | ETHU | 2.10 | +5.34% | 11 |
| Z-score reversion | BITX | 2.10 | +6.37% | 7 |
| Williams %R | MSTR | 2.00 | +3.35% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.50 | 8.50 | 0 | — | 10.11 | 4.53 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 5.93 | 1.92 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.35 | 2.35 | 24 | 45.8 | 2.60 | 0.99 | -5.32 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.72 | -1.28 | 99 | 45.5 | -13.27 | -3.67 | -13.28 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 97.74 | -2.26 | 0 | — | 1.14 | 0.52 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.23 | -2.77 | 0 | — | -0.39 | -0.15 | -3.94 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.85 | -1.96 | -5.83 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.92 | -3.08 | 103 | 35.0 | 3.67 | 1.86 | -2.46 | 94 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.88 | 0.95 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.10 | -4.90 | 0 | — | -5.22 | -1.98 | -6.49 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.65 | -5.35 | 0 | — | -1.57 | -0.54 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 17 | Agent (rotation) | meta | 94.10 | -5.90 | 143 | 30.1 | -6.91 | -4.80 | -9.58 | 143 |
| 18 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.16 | 1.06 | -8.76 | 215 |
| 19 | Agent | meta | 91.29 | -8.71 | 132 | 40.9 | -8.98 | -5.33 | -12.34 | 213 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.18 | -2.11 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 91.17 | -8.83 | 101 | 21.8 | -17.45 | -6.45 | -18.39 | 82 |
| 22 | Hold BTC | benchmark | 90.65 | -9.35 | 0 | — | -0.37 | 0.11 | -12.65 | 1 |
| 23 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.42 | -1.97 | -13.40 | 88 |
| 24 | Copy: Insider buying | copy | 89.03 | -10.97 | 34 | 35.3 | -21.68 | -4.38 | -23.10 | 62 |
| 25 | Opening range 30m | breakout | 88.98 | -11.02 | 331 | 33.2 | -13.49 | -4.10 | -17.21 | 585 |
| 26 | Daily: Bullish score | daily | 88.94 | -11.06 | 14 | 21.4 | -6.15 | -0.75 | -14.73 | 14 |
| 27 | Parabolic SAR · 1h | trend | 88.85 | -11.15 | 146 | 27.4 | -15.89 | -3.74 | -17.10 | 241 |
| 28 | Donchian 55/20 · 1h | breakout | 88.67 | -11.33 | 60 | 13.3 | -13.90 | -3.13 | -18.06 | 100 |
| 29 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.23 | -3.71 | -14.99 | 97 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 86.57 | -13.43 | 1 | 0.0 | -3.23 | -0.34 | -15.96 | 1 |
| 31 | Volume breakout · 1h | breakout | 84.89 | -15.11 | 128 | 28.9 | -17.24 | -3.87 | -18.68 | 98 |
| 32 | Stochastic reversion · 1h | reversion | 84.51 | -15.49 | 228 | 47.4 | -23.70 | -5.00 | -25.11 | 389 |
| 33 | Keltner breakout · 1h | breakout | 84.25 | -15.75 | 88 | 23.9 | -19.70 | -3.96 | -22.89 | 173 |
| 34 | Connors RSI(2) · 1h | reversion | 84.16 | -15.84 | 191 | 40.8 | -20.49 | -6.51 | -21.22 | 143 |
| 35 | Max aggression: 5-day momentum | meta | 83.55 | -16.45 | 15 | 40.0 | -33.59 | -2.39 | -37.35 | 26 |
| 36 | ADX DI cross · 1h | trend | 83.47 | -16.53 | 144 | 18.8 | -20.10 | -3.72 | -22.38 | 259 |
| 37 | MFI reversion · 1h | reversion | 83.16 | -16.84 | 299 | 32.8 | -16.42 | -2.64 | -18.35 | 144 |
| 38 | Opening range 15m | breakout | 81.81 | -18.18 | 405 | 30.4 | -18.78 | -5.46 | -20.70 | 717 |
| 39 | Bollinger breakout · 1h | breakout | 81.81 | -18.19 | 139 | 25.2 | -15.35 | -2.84 | -22.58 | 233 |
| 40 | Ichimoku · 1h | trend | 81.44 | -18.56 | 82 | 13.4 | -19.39 | -3.85 | -25.58 | 120 |
| 41 | CCI reversion · 1h | reversion | 79.65 | -20.35 | 258 | 45.7 | -26.43 | -4.15 | -28.55 | 444 |
| 42 | EMA 20/50 cross · 1h | trend | 78.33 | -21.66 | 90 | 11.1 | -22.84 | -4.49 | -27.27 | 128 |
| 43 | Supertrend · 1h | trend | 77.96 | -22.04 | 138 | 13.0 | -27.67 | -5.30 | -29.14 | 222 |
| 44 | Daily: Momentum burst | daily | 77.88 | -22.12 | 19 | 15.8 | -26.63 | -3.76 | -30.47 | 33 |
| 45 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.32 | -5.49 | -27.82 | 211 |
| 46 | Bollinger reversion · 1h | reversion | 77.61 | -22.39 | 209 | 39.2 | -30.07 | -6.26 | -30.50 | 372 |
| 47 | MACD cross · 1h | trend | 77.43 | -22.57 | 295 | 23.7 | -33.56 | -6.65 | -35.43 | 465 |
| 48 | Triple EMA stack · 1h | trend | 76.76 | -23.24 | 123 | 14.6 | -31.17 | -6.33 | -31.32 | 206 |
| 49 | Williams %R · 1h | reversion | 76.75 | -23.25 | 264 | 46.6 | -36.25 | -6.62 | -36.99 | 518 |
| 50 | RSI momentum · 1h | momentum | 76.71 | -23.29 | 135 | 12.6 | -30.43 | -5.82 | -30.57 | 213 |
| 51 | Z-score reversion · 1h | reversion | 76.46 | -23.54 | 137 | 34.3 | -15.50 | -2.34 | -22.55 | 207 |
| 52 | Heikin-Ashi · 1h | trend | 76.21 | -23.80 | 351 | 22.8 | -39.45 | -8.10 | -43.15 | 660 |
| 53 | OBV trend · 1h | momentum | 75.82 | -24.18 | 237 | 17.7 | -35.79 | -7.83 | -35.86 | 306 |
| 54 | Donchian 20/10 · 1h | breakout | 75.39 | -24.61 | 119 | 20.2 | -26.36 | -4.44 | -30.79 | 206 |
| 55 | ROC + volume · 1h | momentum | 74.53 | -25.47 | 299 | 25.4 | -29.59 | -5.03 | -34.34 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 71.44 | -28.56 | 125 | 26.4 | -21.03 | -3.83 | -26.17 | 199 |
| 57 | Three white soldiers | momentum | 70.45 | -29.55 | 404 | 16.1 | -45.51 | -21.20 | -45.88 | 618 |
| 58 | Candlestick reversal · 1h | reversion | 69.95 | -30.05 | 338 | 28.4 | -37.12 | -7.68 | -37.43 | 539 |
| 59 | VWAP momentum · 1h | momentum | 69.13 | -30.87 | 689 | 21.8 | -51.87 | -10.63 | -53.10 | 1225 |
| 60 | EMA 9/21 cross · 1h | trend | 69.07 | -30.93 | 216 | 9.7 | -36.87 | -6.79 | -40.41 | 328 |
| 61 | Agent (ML meta-label) | meta | 68.98 | -31.02 | 1251 | 20.9 | -20.48 | -4.08 | -21.48 | 316 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 68.78 | -31.22 | 23 | 30.4 | -35.24 | -2.08 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.45 | -98.95 | 5197 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.20 | -23.90 | -80.20 | 1406 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.76 | -44.16 | -93.76 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.96 | -31.52 | -88.98 | 1913 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.57 | -37.49 | -91.58 | 2336 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.92 | -32.15 | -90.92 | 2238 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -52.61 | -97.77 | 3473 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.35 | -57.63 | -96.35 | 3394 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -34.89 | -93.52 | 2422 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.31 | -33.69 | -82.31 | 1687 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -55.04 | -99.47 | 5829 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.02 | -43.55 | -93.04 | 2615 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.61 | -37.32 | -95.61 | 3395 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -75.34 | -99.79 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.94 | -44.20 | -91.97 | 2279 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.10 | -26.27 | -75.10 | 1570 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.17 | -97.76 | 3551 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -61.58 | -98.68 | 4804 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.21 | -28.06 | -69.21 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -53.91 | -94.72 | 2767 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.96 | -37.27 | -84.97 | 1809 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.02 | -99.62 | 6284 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.11 | -30.26 | -88.12 | 2201 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.97 | -19.61 | -76.97 | 1684 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.27 | -37.16 | -90.30 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -51.67 | -96.42 | 3792 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.63 | -53.49 | -89.67 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.15 | -25.19 | -64.67 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.35 | -25.52 | -74.35 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.03 | -18.76 | -76.13 | 1574 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.78 | -49.89 | -96.79 | 4221 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.30 | -99.92 | 8231 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T17:50 | Max aggression: 1-day momentum | sell | ETHU | 68.78 | -3.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | UPRO | 6.43 | — | entry |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | TQQQ | 6.45 | — | entry |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | TECL | 6.45 | — | entry |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | SOXL | 4.52 | — | entry |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | NVDA | 6.45 | — | entry |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | MSTR | 6.45 | — | following Williams %R |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | COIN | 6.45 | — | entry |
| 2026-11-02T17:50 | Agent (ML meta-label) | buy | BITX | 6.45 | — | following Z-score reversion |
| 2026-11-02T17:50 | Agent (ML meta-label) | sell | TSLA | 10.81 | -0.09 | rebalance down |
| 2026-11-02T17:50 | Agent (ML meta-label) | sell | SQQQ | 7.58 | 0.12 | rebalance down |
| 2026-11-02T17:50 | Agent (ML meta-label) | sell | ETHU | 10.74 | -0.18 | rebalance down |
| 2026-11-02T17:50 | ADX DI cross · 1h | buy | TSLA | 4.78 | — | rebalance up |
| 2026-11-02T17:50 | ADX DI cross · 1h | buy | TNA | 4.96 | — | rebalance up |
| 2026-11-02T17:50 | ADX DI cross · 1h | buy | SQQQ | 4.23 | — | rebalance up |
| 2026-11-02T17:50 | ADX DI cross · 1h | buy | IWM | 4.79 | — | rebalance up |
| 2026-11-02T17:50 | ADX DI cross · 1h | buy | AMZN | 4.81 | — | rebalance up |
| 2026-11-02T17:50 | ADX DI cross · 1h | sell | ETH-USD | 11.76 | -0.23 | stop-loss |
| 2026-11-02T17:50 | Parabolic SAR · 1h | sell | XRP-USD | 12.57 | -0.26 | stop-loss |
| 2026-11-02T17:45 | Agent (ML meta-label) | buy | TSLA | 3.48 | — | rebalance up |
| 2026-11-02T17:45 | Agent (ML meta-label) | buy | ETHU | 3.50 | — | rebalance up |
| 2026-11-02T17:45 | Agent (ML meta-label) | sell | TQQQ | 13.69 | -0.07 | selected signal exited |
| 2026-11-02T17:45 | Agent (ML meta-label) | sell | COIN | 2.31 | 0.00 | selected signal exited |
| 2026-11-02T17:45 | Agent (ML meta-label) | sell | BITX | 11.51 | -0.02 | selected signal exited |
| 2026-11-02T17:45 | RSI(14) reversion · 1h | buy | COIN | 8.65 | — | entry |
| 2026-11-02T17:45 | RSI(14) reversion · 1h | sell | TECL | 8.65 | -0.53 | stop-loss |
| 2026-11-02T17:45 | RSI momentum · 1h | buy | AMZN | 3.85 | — | rebalance up |
| 2026-11-02T17:40 | Agent (ML meta-label) | buy | COIN | 2.31 | — | entry |
| 2026-11-02T17:40 | Agent (ML meta-label) | buy | BITX | 11.53 | — | following Z-score reversion |
| 2026-11-02T17:40 | Agent (ML meta-label) | sell | GOOGL | 13.84 | -0.00 | selected signal exited |
| 2026-11-02T17:40 | Agent | buy | ETHU | 18.28 | — | following Stochastic reversion |
| 2026-11-02T17:35 | Day trade: Stocks in Play ORB | sell | UPRO | 24.11 | -0.22 | target is flat |
| 2026-11-02T17:35 | Day trade: Stocks in Play ORB | sell | IWM | 24.30 | -0.15 | target is flat |
| 2026-11-02T17:35 | Agent (ML meta-label) | buy | TQQQ | 13.76 | — | entry |
| 2026-11-02T17:35 | Agent (ML meta-label) | buy | GOOGL | 13.85 | — | entry |
| 2026-11-02T17:35 | Agent (ML meta-label) | sell | COIN | 13.83 | -0.10 | selected signal exited |
| 2026-11-02T17:35 | Agent (ML meta-label) | sell | BITX | 13.77 | -0.16 | selected signal exited |
| 2026-11-02T17:35 | Stochastic reversion · 1h | sell | DOGE-USD | 5.22 | -0.12 | stop-loss |
| 2026-11-02T17:35 | Candlestick reversal · 1h | buy | BITX | 3.50 | — | rebalance up |
| 2026-11-02T17:35 | EMA 9/21 cross · 1h | buy | TSLA | 3.52 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 17:50:05.000122+00:00 -> 2026-11-02 18:00:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
