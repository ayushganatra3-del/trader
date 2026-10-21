# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T15:50:05.000131+00:00 · 30836 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.61 (-9.39%)

Closed trades 91, win rate 40.7%, fees £3.01, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 18.09 | -0.04 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.22 · VIX 17.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 18618 decisions in 2271 calls, $0.2400 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T15:50 | 4 / 20 / 6 | TECL 16% |  |
| Breezy | 2026-10-21T15:50 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-21T15:50 | 4 / 24 / 2 | MSTR 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Opening range 15m | TSLA | 2.24 | +2.47% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Bollinger reversion | ETHU | 1.75 | +6.35% | 14 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.46 | 6.46 | 0 | — | 8.72 | 4.06 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.54 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 5 | Max aggression: 5-day momentum | meta | 103.86 | 3.86 | 10 | 50.0 | -5.22 | -0.15 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.74 | 0.74 | 4 | 50.0 | 9.61 | 2.00 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.82 | -0.18 | 0 | — | 0.90 | 0.45 | -5.02 | 1 |
| 11 | Hold BTC | benchmark | 99.79 | -0.21 | 0 | — | 15.86 | 2.26 | -8.68 | 1 |
| 12 | Hold SPY | benchmark | 99.42 | -0.58 | 0 | — | 0.82 | 0.51 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.09 | -0.91 | 63 | 34.9 | 2.49 | 1.46 | -2.29 | 64 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.40 | -2.60 | 0 | — | 0.99 | 0.47 | -5.31 | 1 |
| 16 | Copy: Insider buying | copy | 97.25 | -2.75 | 25 | 40.0 | -10.91 | -1.84 | -20.62 | 72 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.11 | -1.77 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.89 | -3.11 | 0 | — | -4.22 | -1.61 | -7.04 | 1 |
| 19 | Agent (rotation) | meta | 96.52 | -3.48 | 114 | 31.6 | -6.43 | -3.27 | -8.49 | 286 |
| 20 | Donchian 55/20 · 1h | breakout | 96.42 | -3.58 | 40 | 15.0 | -14.09 | -2.82 | -16.01 | 102 |
| 21 | ADX DI cross · 1h | trend | 95.99 | -4.01 | 90 | 18.9 | -11.12 | -1.86 | -17.62 | 258 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | Daily: Momentum burst | daily | 95.48 | -4.52 | 6 | 16.7 | -9.15 | -1.33 | -20.58 | 38 |
| 24 | Trend pullback · 1h | trend | 95.05 | -4.95 | 91 | 24.2 | -20.41 | -6.21 | -20.50 | 132 |
| 25 | Gap and go | momentum | 94.51 | -5.49 | 84 | 16.7 | 5.97 | 1.85 | -7.13 | 207 |
| 26 | Parabolic SAR · 1h | trend | 93.81 | -6.20 | 108 | 23.1 | -15.40 | -3.27 | -19.76 | 274 |
| 27 | Opening range 30m | breakout | 93.77 | -6.23 | 225 | 32.4 | -10.67 | -2.99 | -17.26 | 568 |
| 28 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 46 | 21.7 | -1.80 | -0.33 | -11.48 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.50 | -6.50 | 0 | — | 2.81 | 0.59 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.82 | -7.18 | 87 | 29.9 | -9.33 | -1.64 | -15.70 | 259 |
| 31 | Daily: Bullish score | daily | 91.97 | -8.03 | 8 | 0.0 | -3.80 | -0.34 | -13.10 | 13 |
| 32 | Volume breakout · 1h | breakout | 91.28 | -8.72 | 89 | 23.6 | -12.16 | -2.15 | -14.02 | 109 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.26 | -1.93 | -16.91 | 1 |
| 34 | Agent | meta | 90.61 | -9.39 | 91 | 40.7 | -11.59 | -6.22 | -12.51 | 247 |
| 35 | Supertrend · 1h | trend | 90.53 | -9.47 | 88 | 12.5 | -20.32 | -3.85 | -26.73 | 224 |
| 36 | RSI momentum · 1h | momentum | 90.24 | -9.76 | 84 | 16.7 | -20.58 | -4.10 | -22.77 | 219 |
| 37 | Connors RSI(2) · 1h | reversion | 89.83 | -10.17 | 158 | 42.4 | -21.70 | -6.42 | -23.42 | 197 |
| 38 | Stochastic reversion · 1h | reversion | 89.46 | -10.54 | 168 | 47.6 | -12.84 | -2.06 | -22.24 | 363 |
| 39 | EMA 20/50 cross · 1h | trend | 89.32 | -10.68 | 62 | 12.9 | -20.85 | -3.80 | -23.86 | 137 |
| 40 | Opening range 15m | breakout | 88.54 | -11.46 | 273 | 28.9 | -16.24 | -4.34 | -19.78 | 705 |
| 41 | Keltner breakout · 1h | breakout | 88.52 | -11.48 | 61 | 23.0 | -18.08 | -3.34 | -25.75 | 205 |
| 42 | MACD cross · 1h | trend | 87.82 | -12.18 | 199 | 21.1 | -25.47 | -4.80 | -28.86 | 473 |
| 43 | Ichimoku · 1h | trend | 87.50 | -12.50 | 60 | 13.3 | -17.99 | -3.36 | -20.25 | 117 |
| 44 | Agent (aggressive) | meta | 87.48 | -12.52 | 45 | 35.6 | -10.48 | -3.18 | -12.37 | 129 |
| 45 | Z-score reversion · 1h | reversion | 86.75 | -13.26 | 101 | 33.7 | -11.55 | -1.79 | -21.32 | 195 |
| 46 | Donchian 20/10 · 1h | breakout | 86.42 | -13.58 | 83 | 19.3 | -20.15 | -3.69 | -29.59 | 224 |
| 47 | Triple EMA stack · 1h | trend | 85.94 | -14.06 | 91 | 14.3 | -29.25 | -5.38 | -31.00 | 224 |
| 48 | MFI reversion · 1h | reversion | 85.14 | -14.86 | 227 | 32.6 | -14.53 | -2.19 | -21.11 | 139 |
| 49 | Agent (ML meta-label) | meta | 85.12 | -14.88 | 718 | 19.6 | -7.06 | -1.12 | -16.27 | 374 |
| 50 | MACD zero-line · 1h | trend | 84.78 | -15.22 | 92 | 15.2 | -24.88 | -4.73 | -27.46 | 223 |
| 51 | OBV trend · 1h | momentum | 84.54 | -15.46 | 188 | 17.6 | -30.39 | -5.70 | -31.71 | 314 |
| 52 | ROC + volume · 1h | momentum | 83.39 | -16.61 | 211 | 23.7 | -25.88 | -4.62 | -32.93 | 387 |
| 53 | Three white soldiers | momentum | 82.76 | -17.24 | 253 | 19.8 | -45.97 | -17.76 | -46.93 | 609 |
| 54 | Williams %R · 1h | reversion | 82.54 | -17.46 | 198 | 44.4 | -30.38 | -4.64 | -36.50 | 518 |
| 55 | Bollinger reversion · 1h | reversion | 82.50 | -17.50 | 163 | 36.2 | -29.18 | -5.64 | -32.84 | 347 |
| 56 | CCI reversion · 1h | reversion | 82.23 | -17.77 | 185 | 43.2 | -19.94 | -2.57 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 81.82 | -18.18 | 235 | 20.9 | -43.87 | -9.38 | -47.28 | 684 |
| 58 | EMA 9/21 cross · 1h | trend | 81.35 | -18.65 | 143 | 10.5 | -26.57 | -5.16 | -29.63 | 325 |
| 59 | RSI(14) reversion · 1h | reversion | 81.10 | -18.90 | 84 | 23.8 | -13.94 | -2.45 | -23.28 | 174 |
| 60 | VWAP momentum · 1h | momentum | 79.37 | -20.63 | 472 | 21.2 | -44.43 | -7.96 | -51.48 | 1257 |
| 61 | Candlestick reversal · 1h | reversion | 78.98 | -21.02 | 228 | 29.4 | -34.84 | -5.99 | -38.51 | 544 |
| 62 | Max aggression: 1-day momentum | meta | 77.60 | -22.40 | 17 | 29.4 | -33.85 | -2.11 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 60.42 | -39.58 | 654 | 22.8 | -77.93 | -21.98 | -79.06 | 1730 |
| 64 | Volume breakout | breakout | 59.71 | -40.29 | 392 | 13.8 | -64.72 | -20.26 | -65.03 | 865 |
| 65 | RSI(14) reversion | reversion | 57.14 | -42.86 | 749 | 26.6 | -74.08 | -16.17 | -74.89 | 1604 |
| 66 | Donchian 55/20 | breakout | 56.88 | -43.12 | 521 | 18.6 | -71.60 | -18.65 | -74.04 | 1294 |
| 67 | Squeeze breakout | breakout | 56.88 | -43.12 | 512 | 13.7 | -66.70 | -22.64 | -67.80 | 1216 |
| 68 | EMA 20/50 cross | trend | 55.69 | -44.31 | 563 | 19.5 | -77.95 | -17.23 | -80.89 | 1449 |
| 69 | VWAP reversion | reversion | 53.92 | -46.08 | 760 | 25.5 | -71.02 | -14.26 | -72.15 | 1469 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.78 | -31.24 | -98.80 | 5322 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.80 | -32.68 | -94.23 | 2617 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.47 | -21.98 | -88.67 | 1908 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.83 | -25.87 | -91.71 | 2378 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.48 | -26.37 | -91.62 | 2274 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -33.90 | -97.77 | 3524 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.90 | -37.78 | -96.99 | 3610 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -27.88 | -94.65 | 2548 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.70 | -27.54 | -83.34 | 1734 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.96 | -99.38 | 5716 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.94 | -27.94 | -92.66 | 2636 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.95 | -31.62 | -95.97 | 3448 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.61 | -99.76 | 6194 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -29.45 | -91.89 | 2354 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -39.60 | -97.78 | 3622 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.28 | -98.48 | 4706 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.20 | -35.40 | -94.45 | 2807 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.41 | -27.99 | -84.44 | 1811 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.25 | -99.53 | 6166 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.74 | -22.21 | -87.01 | 2141 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.48 | -25.29 | -88.05 | 2138 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -32.89 | -95.95 | 3762 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -33.67 | -89.46 | 2117 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -33.57 | -95.77 | 4094 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.40 | -99.91 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T15:45 | Squeeze breakout | buy | SOXL | 13.92 | — | entry signal |
| 2026-10-21T15:45 | Squeeze breakout | buy | AMD | 14.20 | — | entry signal |
| 2026-10-21T15:40 | Agent (ML meta-label) | buy | ETHU | 2.42 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T15:40 | Three white soldiers | buy | TQQQ | 20.71 | — | entry signal |
| 2026-10-21T15:40 | Volume breakout | buy | TECL | 14.92 | — | entry signal |
| 2026-10-21T15:40 | Opening range 15m | buy | TECL | 1.39 | — | entry |
| 2026-10-21T15:40 | Opening range 15m | buy | SPY | 6.33 | — | entry |
| 2026-10-21T15:40 | Opening range 15m | buy | MSFT | 6.33 | — | entry signal |
| 2026-10-21T15:40 | Opening range 15m | sell | QQQ | 4.66 | 0.01 | rebalance down |
| 2026-10-21T15:40 | Opening range 15m | sell | META | 4.66 | 0.02 | rebalance down |
| 2026-10-21T15:40 | Opening range 15m | sell | BITX | 4.72 | 0.09 | rebalance down |
| 2026-10-21T15:35 | Agent (ML meta-label) | buy | IWM | 4.84 | — | rebalance up |
| 2026-10-21T15:35 | Agent (ML meta-label) | sell | ETHU | 7.26 | 0.21 | selected signal exited |
| 2026-10-21T15:35 | Volume breakout | buy | QQQ | 14.91 | — | entry signal |
| 2026-10-21T15:35 | Opening range 30m | buy | UPRO | 8.50 | — | entry |
| 2026-10-21T15:35 | Opening range 30m | buy | TECL | 8.52 | — | entry signal |
| 2026-10-21T15:35 | Opening range 30m | buy | SPY | 8.52 | — | entry |
| 2026-10-21T15:35 | Opening range 30m | buy | AAPL | 8.52 | — | entry |
| 2026-10-21T15:35 | Opening range 30m | sell | TQQQ | 4.80 | 0.03 | rebalance down |
| 2026-10-21T15:35 | Opening range 30m | sell | QQQ | 4.75 | 0.01 | rebalance down |
| 2026-10-21T15:35 | Opening range 30m | sell | PLTR | 4.86 | 0.04 | rebalance down |
| 2026-10-21T15:35 | Opening range 30m | sell | MSTR | 5.00 | 0.18 | rebalance down |
| 2026-10-21T15:35 | Opening range 30m | sell | ETHU | 5.02 | 0.13 | rebalance down |
| 2026-10-21T15:35 | Opening range 30m | sell | COIN | 4.81 | 0.03 | rebalance down |
| 2026-10-21T15:35 | Opening range 30m | sell | BITX | 4.81 | 0.06 | rebalance down |
| 2026-10-21T15:35 | ROC + volume | buy | TECL | 5.46 | — | entry signal |
| 2026-10-21T15:35 | ROC + volume | buy | SOL-USD | 5.50 | — | entry |
| 2026-10-21T15:35 | ROC + volume | buy | NVDA | 5.50 | — | entry |
| 2026-10-21T15:35 | ROC + volume | buy | AAPL | 5.50 | — | entry |
| 2026-10-21T15:35 | ROC + volume | sell | XRP-USD | 3.06 | -0.01 | rebalance down |
| 2026-10-21T15:35 | ROC + volume | sell | PLTR | 3.17 | 0.05 | rebalance down |
| 2026-10-21T15:35 | ROC + volume | sell | ETHU | 3.27 | 0.08 | rebalance down |
| 2026-10-21T15:35 | ROC + volume | sell | ETH-USD | 3.14 | 0.02 | rebalance down |
| 2026-10-21T15:35 | ROC + volume | sell | DOGE-USD | 3.14 | 0.02 | rebalance down |
| 2026-10-21T15:35 | ROC + volume | sell | BTC-USD | 3.04 | -0.01 | rebalance down |
| 2026-10-21T15:35 | ROC + volume | sell | BITX | 3.14 | 0.04 | rebalance down |
| 2026-10-21T15:31 | Agent (ML meta-label) | buy | IWM | 2.89 | — | entry |
| 2026-10-21T15:31 | Agent (ML meta-label) | buy | AMZN | 4.29 | — | rebalance up |
| 2026-10-21T15:31 | Agent (ML meta-label) | sell | COIN | 7.19 | 0.17 | selected signal exited |
| 2026-10-21T15:31 | Agent (aggressive) | buy | TSLA | 43.79 | — | following Opening range 30m, Opening range 15m |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 15:50:05.000131+00:00 -> 2026-10-21 16:00:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
