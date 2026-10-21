# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-21T16:51:05.000109+00:00 · 30886 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.64 (-9.36%)

Closed trades 91, win rate 40.7%, fees £3.01, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 18.12 | -0.01 |

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

Today: 23076 decisions in 2421 calls, $0.2920 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-21T16:51 | 10 / 16 / 3 | XRP-USD 15% |  |
| Breezy | 2026-10-21T16:51 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-10-21T16:51 | 5 / 23 / 1 | MSTR 80% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.43 | 6.43 | 0 | — | 8.72 | 4.06 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.83 | 4.83 | 13 | 53.8 | 7.19 | 2.36 | -3.41 | 21 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 5 | Max aggression: 5-day momentum | meta | 102.80 | 2.80 | 10 | 50.0 | -6.17 | -0.24 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.75 | 0.75 | 4 | 50.0 | 8.82 | 1.84 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold BTC | benchmark | 99.95 | -0.05 | 0 | — | 15.67 | 2.24 | -8.68 | 1 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.62 | -0.38 | 0 | — | 0.46 | 0.27 | -5.02 | 1 |
| 12 | Hold SPY | benchmark | 99.43 | -0.57 | 0 | — | 1.02 | 0.63 | -3.13 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.06 | -0.94 | 63 | 34.9 | 2.46 | 1.44 | -2.29 | 65 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.52 | -3.83 | -3.91 | 20 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.42 | -2.58 | 0 | — | 0.81 | 0.40 | -5.31 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.21 | -2.79 | 0 | — | -3.90 | -1.48 | -7.04 | 1 |
| 17 | Copy: Insider buying | copy | 97.20 | -2.80 | 25 | 40.0 | -10.94 | -1.84 | -20.62 | 72 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.35 | -1.91 | -5.83 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 96.64 | -3.36 | 41 | 17.1 | -13.95 | -2.78 | -16.01 | 103 |
| 20 | Agent (rotation) | meta | 96.28 | -3.72 | 115 | 31.3 | -5.24 | -2.72 | -7.41 | 275 |
| 21 | ADX DI cross · 1h | trend | 96.08 | -3.92 | 91 | 19.8 | -11.29 | -1.94 | -17.62 | 255 |
| 22 | Daily: Momentum burst | daily | 95.63 | -4.37 | 6 | 16.7 | -8.94 | -1.30 | -20.58 | 38 |
| 23 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 24 | Trend pullback · 1h | trend | 95.07 | -4.93 | 91 | 24.2 | -20.27 | -6.20 | -20.44 | 131 |
| 25 | Gap and go | momentum | 94.87 | -5.13 | 84 | 16.7 | 6.44 | 1.96 | -7.13 | 207 |
| 26 | Parabolic SAR · 1h | trend | 93.94 | -6.06 | 108 | 23.1 | -15.70 | -3.34 | -19.76 | 274 |
| 27 | Opening range 30m | breakout | 93.93 | -6.07 | 225 | 32.4 | -10.59 | -2.96 | -17.26 | 570 |
| 28 | Squeeze breakout · 1h | breakout | 93.81 | -6.19 | 46 | 21.7 | -0.69 | -0.07 | -11.48 | 98 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 93.41 | -6.59 | 0 | — | 3.28 | 0.66 | -14.37 | 1 |
| 30 | Bollinger breakout · 1h | breakout | 92.95 | -7.05 | 87 | 29.9 | -8.93 | -1.55 | -15.47 | 258 |
| 31 | Daily: Bullish score | daily | 92.04 | -7.96 | 8 | 0.0 | -3.44 | -0.29 | -13.10 | 13 |
| 32 | Volume breakout · 1h | breakout | 91.42 | -8.58 | 89 | 23.6 | -12.38 | -2.20 | -14.06 | 110 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.93 | -2.07 | -16.91 | 1 |
| 34 | Agent | meta | 90.64 | -9.36 | 91 | 40.7 | -11.13 | -6.36 | -11.44 | 230 |
| 35 | Supertrend · 1h | trend | 90.61 | -9.39 | 88 | 12.5 | -20.13 | -3.81 | -26.62 | 224 |
| 36 | RSI momentum · 1h | momentum | 90.26 | -9.74 | 84 | 16.7 | -19.74 | -3.86 | -21.74 | 218 |
| 37 | Connors RSI(2) · 1h | reversion | 89.83 | -10.17 | 158 | 42.4 | -21.70 | -6.42 | -23.42 | 197 |
| 38 | Stochastic reversion · 1h | reversion | 89.40 | -10.60 | 169 | 47.3 | -13.80 | -2.27 | -22.24 | 362 |
| 39 | EMA 20/50 cross · 1h | trend | 89.29 | -10.71 | 62 | 12.9 | -20.02 | -3.48 | -23.05 | 137 |
| 40 | Opening range 15m | breakout | 88.62 | -11.38 | 274 | 28.8 | -16.08 | -4.30 | -19.68 | 708 |
| 41 | Keltner breakout · 1h | breakout | 88.54 | -11.46 | 61 | 23.0 | -16.34 | -2.97 | -24.24 | 204 |
| 42 | MACD cross · 1h | trend | 87.88 | -12.12 | 199 | 21.1 | -23.29 | -4.36 | -26.96 | 468 |
| 43 | Agent (aggressive) | meta | 87.57 | -12.43 | 45 | 35.6 | -9.50 | -2.87 | -9.85 | 113 |
| 44 | Ichimoku · 1h | trend | 87.50 | -12.50 | 60 | 13.3 | -17.97 | -3.36 | -20.25 | 118 |
| 45 | Z-score reversion · 1h | reversion | 86.73 | -13.27 | 101 | 33.7 | -11.56 | -1.79 | -21.32 | 195 |
| 46 | Donchian 20/10 · 1h | breakout | 86.53 | -13.47 | 83 | 19.3 | -19.43 | -3.54 | -29.03 | 226 |
| 47 | Triple EMA stack · 1h | trend | 86.09 | -13.91 | 92 | 15.2 | -28.90 | -5.34 | -30.43 | 225 |
| 48 | MFI reversion · 1h | reversion | 85.14 | -14.86 | 227 | 32.6 | -14.49 | -2.20 | -21.11 | 140 |
| 49 | Agent (ML meta-label) | meta | 85.04 | -14.96 | 724 | 19.9 | -9.88 | -1.57 | -16.44 | 364 |
| 50 | MACD zero-line · 1h | trend | 84.85 | -15.15 | 92 | 15.2 | -22.86 | -4.38 | -25.89 | 223 |
| 51 | OBV trend · 1h | momentum | 84.50 | -15.50 | 188 | 17.6 | -30.95 | -5.81 | -32.24 | 313 |
| 52 | ROC + volume · 1h | momentum | 83.53 | -16.47 | 212 | 23.6 | -26.12 | -4.66 | -33.05 | 388 |
| 53 | Three white soldiers | momentum | 82.63 | -17.38 | 257 | 20.6 | -46.05 | -17.86 | -46.93 | 608 |
| 54 | Bollinger reversion · 1h | reversion | 82.50 | -17.50 | 163 | 36.2 | -29.18 | -5.64 | -32.84 | 348 |
| 55 | Williams %R · 1h | reversion | 82.49 | -17.51 | 199 | 44.7 | -31.55 | -4.90 | -36.58 | 516 |
| 56 | CCI reversion · 1h | reversion | 82.12 | -17.88 | 188 | 43.6 | -20.08 | -2.60 | -27.44 | 436 |
| 57 | Heikin-Ashi · 1h | trend | 81.88 | -18.12 | 236 | 21.2 | -42.89 | -9.14 | -46.42 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 81.44 | -18.56 | 143 | 10.5 | -26.46 | -5.10 | -29.77 | 328 |
| 59 | RSI(14) reversion · 1h | reversion | 81.10 | -18.90 | 84 | 23.8 | -12.58 | -2.17 | -23.28 | 173 |
| 60 | VWAP momentum · 1h | momentum | 79.50 | -20.50 | 474 | 21.1 | -45.15 | -8.22 | -51.91 | 1255 |
| 61 | Candlestick reversal · 1h | reversion | 78.87 | -21.13 | 228 | 29.4 | -34.14 | -5.82 | -37.91 | 546 |
| 62 | Max aggression: 1-day momentum | meta | 77.34 | -22.66 | 17 | 29.4 | -34.06 | -2.13 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 60.28 | -39.72 | 664 | 23.2 | -77.84 | -21.87 | -79.09 | 1728 |
| 64 | Volume breakout | breakout | 59.32 | -40.69 | 395 | 13.7 | -64.91 | -20.26 | -65.17 | 872 |
| 65 | RSI(14) reversion | reversion | 57.11 | -42.89 | 749 | 26.6 | -74.25 | -16.29 | -74.89 | 1620 |
| 66 | Donchian 55/20 | breakout | 56.99 | -43.01 | 521 | 18.6 | -71.74 | -18.93 | -74.04 | 1294 |
| 67 | Squeeze breakout | breakout | 56.62 | -43.38 | 513 | 13.6 | -66.88 | -22.80 | -67.80 | 1215 |
| 68 | EMA 20/50 cross | trend | 55.70 | -44.30 | 563 | 19.5 | -77.99 | -17.31 | -80.87 | 1449 |
| 69 | VWAP reversion | reversion | 53.90 | -46.10 | 760 | 25.5 | -71.14 | -14.34 | -72.15 | 1488 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.76 | -30.99 | -98.80 | 5305 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.82 | -32.78 | -94.24 | 2612 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.45 | -21.94 | -88.67 | 1908 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.75 | -25.54 | -91.71 | 2377 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.58 | -26.35 | -91.61 | 2275 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.62 | -33.74 | -97.77 | 3522 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -37.84 | -96.97 | 3610 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -27.87 | -94.58 | 2544 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.65 | -27.38 | -83.34 | 1731 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.85 | -99.38 | 5720 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.85 | -27.65 | -92.66 | 2639 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -31.46 | -95.94 | 3458 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -41.44 | -99.76 | 6171 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.65 | -29.36 | -91.89 | 2349 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -39.38 | -97.78 | 3634 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.15 | -98.48 | 4700 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.21 | -35.35 | -94.45 | 2816 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.33 | -27.83 | -84.44 | 1814 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.35 | -99.53 | 6163 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.80 | -22.34 | -87.01 | 2139 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.60 | -25.60 | -88.05 | 2137 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -32.64 | -95.93 | 3753 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -33.21 | -89.42 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.77 | -33.59 | -95.78 | 4083 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.28 | -99.91 | 8296 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-21T16:50 | Agent (ML meta-label) | sell | ETHU | 7.71 | -0.02 | selected signal exited |
| 2026-10-21T16:50 | ROC + volume | sell | TECL | 6.70 | 0.04 | exit signal |
| 2026-10-21T16:45 | Day trade: Stocks in Play ORB | buy | AMD | 24.78 | — | entry |
| 2026-10-21T16:45 | Agent (ML meta-label) | buy | ETHU | 7.73 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-21T16:45 | Opening range 15m | buy | UPRO | 5.20 | — | entry |
| 2026-10-21T16:45 | Opening range 15m | sell | TNA | 5.20 | -0.03 | exit signal |
| 2026-10-21T16:40 | Volume breakout | buy | UPRO | 14.89 | — | entry signal |
| 2026-10-21T16:40 | Volume breakout | buy | TNA | 14.89 | — | entry signal |
| 2026-10-21T16:40 | Volume breakout | buy | ETH-USD | 14.89 | — | entry signal |
| 2026-10-21T16:40 | Squeeze breakout | buy | BTC-USD | 13.76 | — | entry signal |
| 2026-10-21T16:40 | Opening range 15m | buy | TSLA | 3.03 | — | entry |
| 2026-10-21T16:40 | Opening range 15m | buy | TNA | 5.23 | — | entry signal |
| 2026-10-21T16:40 | Opening range 15m | buy | SOXL | 5.23 | — | entry signal |
| 2026-10-21T16:40 | Opening range 15m | buy | AMZN | 5.23 | — | entry signal |
| 2026-10-21T16:40 | Opening range 15m | sell | PLTR | 4.65 | 0.06 | rebalance down |
| 2026-10-21T16:40 | Opening range 15m | sell | MSTR | 4.79 | 0.23 | rebalance down |
| 2026-10-21T16:40 | Opening range 15m | sell | COIN | 4.71 | 0.09 | rebalance down |
| 2026-10-21T16:40 | Opening range 15m | sell | AAPL | 4.58 | 0.02 | rebalance down |
| 2026-10-21T16:40 | ROC + volume | buy | TQQQ | 6.71 | — | entry signal |
| 2026-10-21T16:40 | ROC + volume | buy | MSTR | 6.72 | — | entry signal |
| 2026-10-21T16:40 | ROC + volume | buy | COIN | 6.72 | — | entry signal |
| 2026-10-21T16:40 | ROC + volume | buy | BITX | 6.72 | — | entry signal |
| 2026-10-21T16:40 | ROC + volume | sell | UPRO | 5.34 | 0.02 | rebalance down |
| 2026-10-21T16:40 | ROC + volume | sell | TECL | 5.43 | 0.05 | rebalance down |
| 2026-10-21T16:40 | ROC + volume | sell | QQQ | 5.35 | 0.01 | rebalance down |
| 2026-10-21T16:40 | ROC + volume | sell | PLTR | 5.34 | 0.05 | rebalance down |
| 2026-10-21T16:40 | ROC + volume | sell | AMD | 5.41 | 0.04 | rebalance down |
| 2026-10-21T16:35 | Agent (ML meta-label) | buy | AMZN | 8.50 | — | entry |
| 2026-10-21T16:35 | Squeeze breakout | sell | SOXL | 13.76 | -0.16 | exit signal |
| 2026-10-21T16:35 | ROC + volume | buy | UPRO | 5.97 | — | rebalance up |
| 2026-10-21T16:35 | ROC + volume | buy | TECL | 6.58 | — | rebalance up |
| 2026-10-21T16:35 | ROC + volume | buy | QQQ | 6.01 | — | rebalance up |
| 2026-10-21T16:35 | ROC + volume | buy | PLTR | 6.54 | — | rebalance up |
| 2026-10-21T16:35 | ROC + volume | buy | AMD | 4.52 | — | rebalance up |
| 2026-10-21T16:35 | ROC + volume | sell | SOL-USD | 5.44 | -0.06 | exit signal |
| 2026-10-21T16:35 | ROC + volume | sell | ETHU | 5.46 | 0.09 | exit signal |
| 2026-10-21T16:35 | ROC + volume | sell | ETH-USD | 5.46 | 0.01 | exit signal |
| 2026-10-21T16:30 | Agent (rotation) | sell | TQQQ | 32.00 | -0.17 | selected signal exited |
| 2026-10-21T16:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.83 | -0.55 | target is flat |
| 2026-10-21T16:30 | Agent (ML meta-label) | sell | AMZN | 7.09 | 0.00 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-23 16:51:05.000109+00:00 -> 2026-10-21 17:01:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
