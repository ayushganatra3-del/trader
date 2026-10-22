# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T15:45:05.000168+00:00 · 32007 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.44 (-9.56%)

Closed trades 94, win rate 40.4%, fees £3.06, max drawdown -10.18%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 17.93 | -0.21 |

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

Today: 19881 decisions in 2325 calls, $0.2558 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T15:45 | 3 / 5 / 21 | cash |  |
| Breezy | 2026-10-22T15:45 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-10-22T15:45 | 3 / 21 / 5 | MSTR 61% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.68 | 7.68 | 0 | — | 10.02 | 4.50 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.01 | 5.01 | 12 | 66.7 | 1.87 | 0.63 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.03 | 4.03 | 15 | 46.7 | 6.37 | 2.02 | -4.90 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.08 | 2.08 | 75 | 48.0 | -8.82 | -2.40 | -13.79 | 135 |
| 6 | Max aggression: 5-day momentum | meta | 100.28 | 0.28 | 10 | 50.0 | -15.57 | -1.21 | -34.64 | 26 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.17 | 0.17 | 0 | — | 2.66 | 1.20 | -5.02 | 1 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.23 | -0.77 | 68 | 35.3 | 2.94 | 1.72 | -2.29 | 68 |
| 11 | Hold SPY | benchmark | 98.35 | -1.65 | 0 | — | -0.43 | -0.19 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.28 | -2.72 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.66 | -2.10 | -5.83 | 1 |
| 15 | Hold BTC | benchmark | 96.45 | -3.55 | 0 | — | 4.77 | 0.88 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 96.24 | -3.76 | 0 | — | -0.76 | -0.24 | -5.31 | 1 |
| 17 | Agent (rotation) | meta | 96.07 | -3.93 | 117 | 30.8 | -5.63 | -2.46 | -7.58 | 278 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.40 | 0.59 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.72 | -5.28 | 89 | 21.3 | 6.64 | 2.07 | -7.38 | 198 |
| 21 | Trend pullback · 1h | trend | 94.32 | -5.68 | 93 | 23.7 | -22.95 | -7.17 | -23.10 | 124 |
| 22 | Copy: Insider buying | copy | 93.86 | -6.13 | 25 | 40.0 | -14.07 | -2.40 | -20.62 | 72 |
| 23 | Opening range 30m | breakout | 93.54 | -6.46 | 237 | 35.0 | -10.46 | -2.95 | -17.26 | 558 |
| 24 | ADX DI cross · 1h | trend | 93.17 | -6.83 | 101 | 18.8 | -13.17 | -2.49 | -15.18 | 256 |
| 25 | Daily: Momentum burst | daily | 93.08 | -6.92 | 8 | 12.5 | -16.46 | -2.93 | -20.58 | 39 |
| 26 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -18.62 | -3.76 | -19.64 | 103 |
| 27 | Parabolic SAR · 1h | trend | 92.35 | -7.65 | 115 | 26.1 | -16.20 | -3.49 | -19.19 | 266 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.17 | -0.96 | -11.76 | 101 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.68 | -2.24 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 90.80 | -9.20 | 8 | 0.0 | -6.79 | -0.78 | -13.10 | 13 |
| 31 | Agent | meta | 90.44 | -9.56 | 94 | 40.4 | -19.32 | -6.35 | -23.57 | 285 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.11 | -9.89 | 0 | — | -4.04 | -0.48 | -14.37 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 89.45 | -10.55 | 103 | 28.2 | -11.82 | -2.10 | -15.89 | 258 |
| 34 | Volume breakout · 1h | breakout | 88.92 | -11.08 | 101 | 22.8 | -12.52 | -2.24 | -13.70 | 106 |
| 35 | Stochastic reversion · 1h | reversion | 88.83 | -11.17 | 176 | 46.0 | -14.94 | -2.46 | -22.24 | 371 |
| 36 | EMA 20/50 cross · 1h | trend | 88.11 | -11.89 | 67 | 11.9 | -23.94 | -4.50 | -26.20 | 143 |
| 37 | Supertrend · 1h | trend | 87.68 | -12.32 | 102 | 15.7 | -23.83 | -4.67 | -26.77 | 219 |
| 38 | RSI momentum · 1h | momentum | 87.47 | -12.54 | 94 | 17.0 | -20.11 | -3.95 | -21.61 | 218 |
| 39 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -14.05 | -3.85 | -19.23 | 133 |
| 40 | Opening range 15m | breakout | 87.08 | -12.92 | 297 | 30.6 | -16.20 | -4.36 | -18.82 | 701 |
| 41 | Keltner breakout · 1h | breakout | 86.01 | -13.98 | 73 | 23.3 | -22.94 | -4.40 | -23.62 | 200 |
| 42 | Connors RSI(2) · 1h | reversion | 85.71 | -14.29 | 168 | 39.9 | -25.74 | -7.16 | -25.74 | 204 |
| 43 | MACD cross · 1h | trend | 85.18 | -14.82 | 213 | 23.0 | -26.81 | -4.98 | -28.23 | 468 |
| 44 | Ichimoku · 1h | trend | 84.78 | -15.22 | 64 | 12.5 | -19.91 | -3.71 | -22.29 | 117 |
| 45 | Triple EMA stack · 1h | trend | 84.41 | -15.59 | 96 | 15.6 | -28.95 | -5.43 | -29.30 | 220 |
| 46 | Z-score reversion · 1h | reversion | 84.35 | -15.65 | 104 | 33.7 | -9.65 | -1.32 | -21.32 | 196 |
| 47 | MFI reversion · 1h | reversion | 83.91 | -16.09 | 231 | 32.9 | -17.40 | -2.70 | -21.11 | 144 |
| 48 | Donchian 20/10 · 1h | breakout | 83.73 | -16.27 | 92 | 20.7 | -24.13 | -4.41 | -24.85 | 226 |
| 49 | Williams %R · 1h | reversion | 82.98 | -17.02 | 201 | 44.8 | -32.76 | -5.15 | -37.96 | 518 |
| 50 | MACD zero-line · 1h | trend | 82.55 | -17.45 | 101 | 14.9 | -24.87 | -4.76 | -25.84 | 226 |
| 51 | OBV trend · 1h | momentum | 82.48 | -17.52 | 196 | 17.9 | -32.19 | -6.16 | -32.59 | 308 |
| 52 | Three white soldiers | momentum | 82.17 | -17.83 | 263 | 20.2 | -44.68 | -17.86 | -45.15 | 598 |
| 53 | Agent (ML meta-label) | meta | 81.61 | -18.39 | 768 | 19.4 | -14.04 | -2.60 | -16.37 | 351 |
| 54 | CCI reversion · 1h | reversion | 81.29 | -18.71 | 191 | 43.5 | -22.22 | -2.96 | -27.44 | 442 |
| 55 | Bollinger reversion · 1h | reversion | 81.23 | -18.77 | 165 | 35.8 | -30.37 | -5.88 | -32.75 | 354 |
| 56 | ROC + volume · 1h | momentum | 80.10 | -19.90 | 230 | 24.3 | -28.47 | -5.14 | -28.63 | 378 |
| 57 | Heikin-Ashi · 1h | trend | 79.67 | -20.33 | 260 | 23.5 | -45.76 | -9.46 | -45.80 | 676 |
| 58 | RSI(14) reversion · 1h | reversion | 78.86 | -21.14 | 87 | 24.1 | -19.39 | -3.64 | -23.28 | 173 |
| 59 | Candlestick reversal · 1h | reversion | 78.70 | -21.30 | 235 | 30.2 | -35.28 | -5.95 | -38.19 | 553 |
| 60 | EMA 9/21 cross · 1h | trend | 78.49 | -21.51 | 154 | 11.7 | -31.00 | -5.76 | -32.02 | 336 |
| 61 | VWAP momentum · 1h | momentum | 76.45 | -23.55 | 499 | 21.4 | -50.60 | -10.33 | -50.85 | 1246 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.13 | -2.80 | -47.84 | 43 |
| 63 | ROC + volume | momentum | 59.90 | -40.10 | 681 | 23.3 | -77.72 | -21.22 | -79.23 | 1694 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.50 | -19.37 | -65.38 | 872 |
| 65 | Donchian 55/20 | breakout | 56.16 | -43.84 | 538 | 19.7 | -71.91 | -18.64 | -74.21 | 1274 |
| 66 | Squeeze breakout | breakout | 55.60 | -44.40 | 527 | 14.0 | -67.37 | -23.18 | -68.25 | 1202 |
| 67 | EMA 20/50 cross | trend | 54.45 | -45.55 | 581 | 20.3 | -79.00 | -20.08 | -80.38 | 1442 |
| 68 | RSI(14) reversion | reversion | 53.37 | -46.62 | 794 | 26.4 | -76.50 | -17.33 | -76.50 | 1677 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -72.91 | -14.51 | -73.06 | 1516 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -31.54 | -98.87 | 5293 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.82 | -31.84 | -94.30 | 2570 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.01 | -23.16 | -88.98 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.20 | -27.30 | -91.88 | 2348 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.07 | -25.21 | -91.08 | 2223 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -33.69 | -97.91 | 3494 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -35.38 | -97.04 | 3560 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.52 | -27.96 | -94.53 | 2566 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.98 | -27.38 | -83.47 | 1717 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -37.18 | -99.47 | 5843 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.35 | -29.93 | -92.92 | 2614 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.74 | -30.65 | -95.77 | 3449 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -40.70 | -99.78 | 6164 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -29.20 | -92.12 | 2328 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -38.83 | -97.75 | 3589 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -38.22 | -98.63 | 4754 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.25 | -34.38 | -94.62 | 2782 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.37 | -27.37 | -84.51 | 1784 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -40.17 | -99.59 | 6224 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.75 | -23.49 | -87.81 | 2190 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.54 | -26.84 | -88.69 | 2191 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.21 | -33.87 | -96.23 | 3807 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.52 | -33.75 | -89.81 | 2106 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.20 | -34.42 | -96.21 | 4133 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.62 | -99.91 | 8242 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T15:40 | Agent (ML meta-label) | buy | TSLA | 6.84 | — | rebalance up |
| 2026-10-22T15:40 | Agent (ML meta-label) | buy | PLTR | 6.85 | — | rebalance up |
| 2026-10-22T15:40 | Agent (ML meta-label) | buy | MSTR | 6.80 | — | rebalance up |
| 2026-10-22T15:40 | Agent (ML meta-label) | sell | TNA | 13.60 | -0.00 | selected signal exited |
| 2026-10-22T15:40 | Agent (ML meta-label) | sell | SQQQ | 13.61 | -0.01 | selected signal exited |
| 2026-10-22T15:40 | Agent (ML meta-label) | sell | IWM | 13.71 | -0.02 | selected signal exited |
| 2026-10-22T15:40 | ROC + volume | buy | AAPL | 14.98 | — | entry signal |
| 2026-10-22T15:35 | Agent (ML meta-label) | buy | TNA | 13.60 | — | entry |
| 2026-10-22T15:35 | Agent (ML meta-label) | buy | SQQQ | 8.83 | — | rebalance up |
| 2026-10-22T15:35 | Agent (ML meta-label) | sell | LABU | 10.77 | -0.06 | selected signal exited |
| 2026-10-22T15:35 | Agent (ML meta-label) | sell | AAPL | 11.65 | -0.02 | selected signal exited |
| 2026-10-22T15:30 | Agent (ML meta-label) | buy | SQQQ | 4.79 | — | entry |
| 2026-10-22T15:30 | Agent (ML meta-label) | buy | AAPL | 11.67 | — | entry |
| 2026-10-22T15:30 | Agent (ML meta-label) | sell | TNA | 16.46 | 0.04 | selected signal exited |
| 2026-10-22T15:30 | CCI reversion · 1h | sell | SQQQ | 13.65 | 0.09 | exit signal |
| 2026-10-22T15:30 | Williams %R · 1h | buy | TNA | 13.78 | — | entry signal |
| 2026-10-22T15:30 | Williams %R · 1h | buy | MSFT | 13.84 | — | entry signal |
| 2026-10-22T15:30 | Williams %R · 1h | buy | IWM | 13.84 | — | entry signal |
| 2026-10-22T15:30 | Williams %R · 1h | sell | SOL-USD | 6.74 | -0.04 | rebalance down |
| 2026-10-22T15:30 | Williams %R · 1h | sell | ETH-USD | 6.80 | -0.08 | rebalance down |
| 2026-10-22T15:30 | Williams %R · 1h | sell | DOGE-USD | 6.68 | -0.11 | rebalance down |
| 2026-10-22T15:30 | Z-score reversion · 1h | buy | MSFT | 21.10 | — | entry signal |
| 2026-10-22T15:30 | Bollinger reversion · 1h | buy | SPY | 12.25 | — | entry signal |
| 2026-10-22T15:30 | Bollinger reversion · 1h | buy | GOOGL | 16.25 | — | entry signal |
| 2026-10-22T15:30 | Bollinger reversion · 1h | sell | DOGE-USD | 4.10 | -0.06 | rebalance down |
| 2026-10-22T15:30 | Bollinger reversion · 1h | sell | BTC-USD | 4.11 | -0.03 | rebalance down |
| 2026-10-22T15:30 | Connors RSI(2) · 1h | buy | TSLA | 21.45 | — | entry signal |
| 2026-10-22T15:30 | VWAP momentum · 1h | buy | AAPL | 19.11 | — | entry signal |
| 2026-10-22T15:30 | VWAP momentum · 1h | sell | TSLA | 19.07 | -0.01 | exit signal |
| 2026-10-22T15:30 | VWAP momentum · 1h | sell | MSTR | 19.10 | -0.11 | exit signal |
| 2026-10-22T15:30 | Heikin-Ashi · 1h | buy | SQQQ | 19.92 | — | entry signal |
| 2026-10-22T15:30 | MACD zero-line · 1h | buy | TSLA | 4.29 | — | rebalance up |
| 2026-10-22T15:30 | MACD zero-line · 1h | buy | PLTR | 4.18 | — | rebalance up |
| 2026-10-22T15:30 | MACD zero-line · 1h | sell | TNA | 16.59 | -0.08 | exit signal |
| 2026-10-22T15:30 | MACD zero-line · 1h | sell | IWM | 16.55 | -0.01 | exit signal |
| 2026-10-22T15:30 | MACD cross · 1h | buy | TSLA | 6.43 | — | rebalance up |
| 2026-10-22T15:30 | MACD cross · 1h | buy | SQQQ | 17.04 | — | entry signal |
| 2026-10-22T15:30 | MACD cross · 1h | buy | PLTR | 6.39 | — | rebalance up |
| 2026-10-22T15:30 | MACD cross · 1h | buy | MSTR | 10.47 | — | rebalance up |
| 2026-10-22T15:30 | MACD cross · 1h | buy | AAPL | 10.46 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 15:45:05.000168+00:00 -> 2026-10-22 15:55:05.000168+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
