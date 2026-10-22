# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T16:15:05.000118+00:00 · 32036 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.48 (-9.52%)

Closed trades 94, win rate 40.4%, fees £3.06, max drawdown -10.18%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 17.96 | -0.17 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 22476 decisions in 2412 calls, $0.2861 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T16:15 | 6 / 18 / 4 | cash |  |
| Breezy | 2026-10-22T16:15 | 0 / 26 / 2 | cash |  |
| Boozy | 2026-10-22T16:15 | 7 / 21 / 0 | MSTR 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.87 | 7.87 | 0 | — | 10.40 | 4.64 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 12 | 66.7 | 1.13 | 0.42 | -7.48 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.27 | 3.27 | 15 | 46.7 | 5.60 | 1.80 | -4.90 | 24 |
| 5 | VWAP reversion · 1h | reversion | 102.23 | 2.23 | 75 | 48.0 | -8.69 | -2.36 | -13.79 | 135 |
| 6 | Max aggression: 5-day momentum | meta | 100.33 | 0.33 | 10 | 50.0 | -15.52 | -1.20 | -34.64 | 26 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.20 | 0.20 | 0 | — | 2.73 | 1.23 | -5.02 | 1 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.17 | -0.83 | 68 | 35.3 | 2.88 | 1.69 | -2.29 | 68 |
| 11 | Hold SPY | benchmark | 98.59 | -1.41 | 0 | — | -0.19 | -0.06 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.28 | -2.72 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -1.99 | -5.83 | 1 |
| 15 | Hold BTC | benchmark | 96.55 | -3.45 | 0 | — | 5.05 | 0.93 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 96.46 | -3.54 | 0 | — | -0.43 | -0.11 | -5.31 | 1 |
| 17 | Agent (rotation) | meta | 95.85 | -4.15 | 117 | 30.8 | -5.85 | -2.53 | -7.58 | 278 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.99 | 0.70 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.54 | -5.46 | 89 | 21.3 | 6.44 | 2.01 | -7.38 | 198 |
| 21 | Trend pullback · 1h | trend | 94.27 | -5.73 | 93 | 23.7 | -22.99 | -7.18 | -23.14 | 124 |
| 22 | Copy: Insider buying | copy | 93.93 | -6.07 | 25 | 40.0 | -14.01 | -2.39 | -20.62 | 72 |
| 23 | Daily: Momentum burst | daily | 93.42 | -6.58 | 8 | 12.5 | -15.47 | -2.73 | -20.58 | 39 |
| 24 | Opening range 30m | breakout | 93.37 | -6.63 | 237 | 35.0 | -10.62 | -3.00 | -17.26 | 558 |
| 25 | ADX DI cross · 1h | trend | 93.11 | -6.89 | 101 | 18.8 | -11.26 | -2.10 | -15.10 | 253 |
| 26 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -18.62 | -3.76 | -19.63 | 103 |
| 27 | Parabolic SAR · 1h | trend | 92.46 | -7.54 | 115 | 26.1 | -16.10 | -3.47 | -19.19 | 266 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.35 | -0.99 | -11.76 | 101 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.17 | -2.13 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.06 | -8.94 | 8 | 0.0 | -6.59 | -0.75 | -13.10 | 13 |
| 31 | Agent | meta | 90.48 | -9.52 | 94 | 40.4 | -20.50 | -6.30 | -25.06 | 288 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.13 | -9.87 | 0 | — | -4.05 | -0.48 | -14.37 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 89.37 | -10.63 | 103 | 28.2 | -11.85 | -2.11 | -15.91 | 258 |
| 34 | Stochastic reversion · 1h | reversion | 88.87 | -11.13 | 176 | 46.0 | -14.87 | -2.45 | -22.24 | 372 |
| 35 | Volume breakout · 1h | breakout | 88.75 | -11.25 | 101 | 22.8 | -11.83 | -2.11 | -12.86 | 106 |
| 36 | EMA 20/50 cross · 1h | trend | 88.15 | -11.85 | 67 | 11.9 | -24.15 | -4.55 | -26.19 | 145 |
| 37 | Supertrend · 1h | trend | 87.76 | -12.24 | 102 | 15.7 | -23.75 | -4.66 | -26.77 | 219 |
| 38 | RSI momentum · 1h | momentum | 87.55 | -12.45 | 94 | 17.0 | -20.10 | -3.96 | -21.61 | 218 |
| 39 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -20.29 | -4.94 | -25.62 | 148 |
| 40 | Opening range 15m | breakout | 86.91 | -13.10 | 297 | 30.6 | -16.35 | -4.40 | -18.82 | 703 |
| 41 | Keltner breakout · 1h | breakout | 85.86 | -14.14 | 73 | 23.3 | -23.89 | -4.59 | -24.42 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.75 | -14.25 | 168 | 39.9 | -25.71 | -7.16 | -25.76 | 204 |
| 43 | MACD cross · 1h | trend | 85.12 | -14.88 | 213 | 23.0 | -26.85 | -4.98 | -28.23 | 468 |
| 44 | Ichimoku · 1h | trend | 84.79 | -15.21 | 64 | 12.5 | -19.48 | -3.60 | -22.29 | 116 |
| 45 | Z-score reversion · 1h | reversion | 84.44 | -15.56 | 104 | 33.7 | -9.56 | -1.31 | -21.32 | 196 |
| 46 | Triple EMA stack · 1h | trend | 84.28 | -15.72 | 96 | 15.6 | -28.94 | -5.42 | -29.33 | 220 |
| 47 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 231 | 32.9 | -17.65 | -2.73 | -21.11 | 145 |
| 48 | Donchian 20/10 · 1h | breakout | 83.65 | -16.35 | 92 | 20.7 | -24.18 | -4.42 | -24.94 | 226 |
| 49 | Williams %R · 1h | reversion | 83.25 | -16.75 | 201 | 44.8 | -32.53 | -5.10 | -37.95 | 518 |
| 50 | MACD zero-line · 1h | trend | 82.59 | -17.41 | 101 | 14.9 | -24.67 | -4.71 | -25.84 | 226 |
| 51 | OBV trend · 1h | momentum | 82.30 | -17.70 | 196 | 17.9 | -31.97 | -6.12 | -32.23 | 307 |
| 52 | Three white soldiers | momentum | 82.17 | -17.83 | 263 | 20.2 | -44.68 | -17.86 | -45.15 | 598 |
| 53 | Agent (ML meta-label) | meta | 81.57 | -18.43 | 774 | 19.5 | -14.19 | -2.62 | -16.91 | 356 |
| 54 | CCI reversion · 1h | reversion | 81.39 | -18.61 | 191 | 43.5 | -21.96 | -2.91 | -27.44 | 442 |
| 55 | Bollinger reversion · 1h | reversion | 81.34 | -18.66 | 165 | 35.8 | -30.36 | -5.89 | -32.84 | 354 |
| 56 | ROC + volume · 1h | momentum | 80.05 | -19.95 | 230 | 24.3 | -28.10 | -5.11 | -28.27 | 378 |
| 57 | Heikin-Ashi · 1h | trend | 79.53 | -20.47 | 260 | 23.5 | -44.09 | -9.37 | -44.55 | 674 |
| 58 | RSI(14) reversion · 1h | reversion | 78.96 | -21.04 | 87 | 24.1 | -19.27 | -3.62 | -23.28 | 174 |
| 59 | Candlestick reversal · 1h | reversion | 78.76 | -21.24 | 235 | 30.2 | -35.60 | -6.03 | -38.20 | 556 |
| 60 | EMA 9/21 cross · 1h | trend | 78.54 | -21.46 | 154 | 11.7 | -31.12 | -5.80 | -31.99 | 336 |
| 61 | VWAP momentum · 1h | momentum | 76.31 | -23.69 | 499 | 21.4 | -50.72 | -10.31 | -50.95 | 1245 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -42.90 | -2.79 | -47.84 | 43 |
| 63 | ROC + volume | momentum | 59.65 | -40.35 | 684 | 23.4 | -77.73 | -21.25 | -79.18 | 1692 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.37 | -19.25 | -65.32 | 870 |
| 65 | Donchian 55/20 | breakout | 56.06 | -43.95 | 538 | 19.7 | -72.08 | -19.18 | -74.12 | 1273 |
| 66 | Squeeze breakout | breakout | 55.60 | -44.40 | 527 | 14.0 | -67.32 | -22.77 | -68.37 | 1201 |
| 67 | EMA 20/50 cross | trend | 54.38 | -45.62 | 581 | 20.3 | -79.20 | -20.19 | -80.54 | 1440 |
| 68 | RSI(14) reversion | reversion | 53.48 | -46.52 | 794 | 26.4 | -76.06 | -17.10 | -76.38 | 1665 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -72.73 | -14.52 | -73.05 | 1511 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -31.49 | -98.87 | 5303 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -32.43 | -94.36 | 2570 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.03 | -23.21 | -89.00 | 1900 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -27.31 | -91.95 | 2351 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.08 | -25.25 | -91.08 | 2222 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -34.41 | -97.91 | 3496 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -35.66 | -97.04 | 3563 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -28.11 | -94.47 | 2559 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.99 | -27.41 | -83.48 | 1719 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -36.94 | -99.47 | 5832 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.38 | -29.92 | -92.94 | 2616 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.71 | -30.54 | -95.74 | 3445 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -40.77 | -99.78 | 6157 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -29.24 | -92.13 | 2334 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -38.83 | -97.76 | 3589 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -38.27 | -98.63 | 4754 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.27 | -34.54 | -94.63 | 2785 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.32 | -27.05 | -84.51 | 1784 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -40.11 | -99.59 | 6220 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.72 | -23.49 | -87.82 | 2189 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.39 | -26.69 | -88.58 | 2192 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.20 | -33.84 | -96.23 | 3802 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.57 | -33.94 | -89.82 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.19 | -34.43 | -96.21 | 4132 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.36 | -99.91 | 8253 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T16:15 | Agent (ML meta-label) | buy | LABU | 4.23 | — | following Connors RSI(2) |
| 2026-10-22T16:15 | Agent (ML meta-label) | sell | MSFT | 4.23 | -0.00 | selected signal exited |
| 2026-10-22T16:10 | Agent (ML meta-label) | buy | TSLA | 10.09 | — | following Opening range 30m |
| 2026-10-22T16:10 | Agent (ML meta-label) | buy | MSTR | 12.90 | — | entry |
| 2026-10-22T16:10 | Agent (ML meta-label) | sell | MSFT | 9.36 | -0.01 | rebalance down |
| 2026-10-22T16:10 | Agent (ML meta-label) | sell | LABU | 13.63 | 0.04 | selected signal exited |
| 2026-10-22T16:10 | ROC + volume | buy | UPRO | 14.92 | — | entry signal |
| 2026-10-22T16:10 | ROC + volume | sell | META | 14.80 | -0.16 | stop-loss |
| 2026-10-22T16:05 | Opening range 15m | buy | TNA | 4.39 | — | rebalance up |
| 2026-10-22T16:05 | Opening range 15m | sell | MSTR | 4.39 | -0.02 | rebalance down |
| 2026-10-22T16:05 | EMA 20/50 cross | buy | SOL-USD | 13.62 | — | entry signal |
| 2026-10-22T16:00 | Agent (ML meta-label) | buy | SQQQ | 13.57 | — | entry |
| 2026-10-22T16:00 | Agent (ML meta-label) | buy | SPY | 13.59 | — | entry |
| 2026-10-22T16:00 | Agent (ML meta-label) | buy | MSFT | 13.59 | — | entry |
| 2026-10-22T16:00 | Agent (ML meta-label) | buy | IWM | 13.59 | — | entry |
| 2026-10-22T16:00 | Agent (ML meta-label) | sell | TSLA | 20.38 | 0.09 | selected signal exited |
| 2026-10-22T16:00 | Agent (ML meta-label) | sell | PLTR | 6.80 | 0.01 | rebalance down |
| 2026-10-22T16:00 | Agent (ML meta-label) | sell | MSTR | 20.37 | -0.11 | selected signal exited |
| 2026-10-22T16:00 | Agent (ML meta-label) | sell | LABU | 6.79 | 0.00 | rebalance down |
| 2026-10-22T16:00 | Stochastic reversion · 1h | buy | XRP-USD | 22.24 | — | entry signal |
| 2026-10-22T16:00 | Candlestick reversal · 1h | buy | XRP-USD | 4.65 | — | entry signal |
| 2026-10-22T16:00 | Candlestick reversal · 1h | buy | DOGE-USD | 15.77 | — | entry signal |
| 2026-10-22T16:00 | Opening range 15m | buy | TNA | 8.79 | — | entry signal |
| 2026-10-22T16:00 | Opening range 15m | buy | IWM | 17.39 | — | entry signal |
| 2026-10-22T16:00 | Opening range 15m | sell | SQQQ | 4.54 | 0.03 | rebalance down |
| 2026-10-22T15:55 | Agent (ML meta-label) | buy | TSLA | 6.77 | — | rebalance up |
| 2026-10-22T15:55 | Agent (ML meta-label) | buy | PLTR | 6.78 | — | rebalance up |
| 2026-10-22T15:55 | Agent (ML meta-label) | buy | MSTR | 6.78 | — | rebalance up |
| 2026-10-22T15:55 | Agent (ML meta-label) | buy | LABU | 6.78 | — | rebalance up |
| 2026-10-22T15:55 | Agent (ML meta-label) | sell | SQQQ | 13.52 | -0.06 | selected signal exited |
| 2026-10-22T15:55 | Agent (ML meta-label) | sell | SPY | 13.59 | -0.00 | selected signal exited |
| 2026-10-22T15:55 | ROC + volume | buy | META | 14.96 | — | entry signal |
| 2026-10-22T15:55 | ROC + volume | sell | SQQQ | 15.18 | 0.26 | exit signal |
| 2026-10-22T15:50 | Agent (ML meta-label) | buy | SQQQ | 13.58 | — | entry |
| 2026-10-22T15:50 | Agent (ML meta-label) | buy | SPY | 13.59 | — | entry |
| 2026-10-22T15:50 | Agent (ML meta-label) | buy | LABU | 13.59 | — | following Connors RSI(2) |
| 2026-10-22T15:50 | Agent (ML meta-label) | sell | TSLA | 6.83 | 0.03 | rebalance down |
| 2026-10-22T15:50 | Agent (ML meta-label) | sell | PLTR | 6.80 | 0.00 | rebalance down |
| 2026-10-22T15:50 | Agent (ML meta-label) | sell | MSTR | 6.72 | -0.06 | rebalance down |
| 2026-10-22T15:50 | ROC + volume | sell | AAPL | 14.96 | -0.02 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 16:15:05.000118+00:00 -> 2026-10-22 16:25:05.000118+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
