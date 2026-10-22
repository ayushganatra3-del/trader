# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T07:50:05.000163+00:00 · 31624 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

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

Today: 5880 decisions in 1176 calls, $0.0824 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T07:50 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-22T07:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T07:50 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.92 | 5.92 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.40 | 1.40 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.13 | 0.13 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.52 | -0.48 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.30 | -0.70 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.40 | -2.60 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 16 | Hold BTC | benchmark | 96.98 | -3.02 | 0 | — | 4.16 | 0.80 | -8.68 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 96.96 | -3.04 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.59 | -3.41 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.74 | -4.26 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 21 | ADX DI cross · 1h | trend | 95.37 | -4.62 | 92 | 19.6 | -10.11 | -1.83 | -16.14 | 258 |
| 22 | Daily: Momentum burst | daily | 94.83 | -5.17 | 6 | 16.7 | -9.30 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.81 | -5.19 | 92 | 23.9 | -20.40 | -6.36 | -20.58 | 129 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 94.18 | -5.82 | 45 | 17.8 | -16.06 | -3.29 | -17.13 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.83 | -7.17 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.77 | -7.22 | 113 | 25.7 | -16.62 | -3.68 | -19.79 | 272 |
| 29 | Squeeze breakout · 1h | breakout | 92.47 | -7.53 | 50 | 24.0 | -2.55 | -0.55 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.11 | -7.88 | 8 | 0.0 | -2.44 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 91.95 | -8.05 | 93 | 30.1 | -10.27 | -1.86 | -14.43 | 259 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -15.83 | -6.53 | -16.82 | 260 |
| 34 | Volume breakout · 1h | breakout | 90.31 | -9.69 | 95 | 24.2 | -13.59 | -2.39 | -13.64 | 108 |
| 35 | Supertrend · 1h | trend | 89.58 | -10.42 | 93 | 15.1 | -21.06 | -4.21 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.05 | -10.95 | 89 | 18.0 | -17.99 | -3.59 | -20.65 | 219 |
| 37 | Stochastic reversion · 1h | reversion | 88.87 | -11.13 | 169 | 47.3 | -14.35 | -2.36 | -22.24 | 368 |
| 38 | EMA 20/50 cross · 1h | trend | 88.31 | -11.69 | 63 | 12.7 | -21.55 | -3.72 | -23.57 | 142 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Keltner breakout · 1h | breakout | 87.62 | -12.38 | 67 | 23.9 | -20.71 | -4.02 | -22.53 | 199 |
| 41 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -16.75 | -4.63 | -20.48 | 132 |
| 42 | MACD cross · 1h | trend | 87.37 | -12.63 | 202 | 22.3 | -23.77 | -4.50 | -26.95 | 467 |
| 43 | Z-score reversion · 1h | reversion | 86.74 | -13.26 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 44 | Connors RSI(2) · 1h | reversion | 86.72 | -13.28 | 164 | 40.9 | -24.71 | -7.18 | -24.71 | 202 |
| 45 | Ichimoku · 1h | trend | 86.45 | -13.55 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.35 | -14.65 | 87 | 20.7 | -23.77 | -4.40 | -28.56 | 229 |
| 47 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.02 | -21.11 | 141 |
| 48 | Triple EMA stack · 1h | trend | 85.11 | -14.89 | 94 | 16.0 | -27.32 | -5.07 | -27.78 | 221 |
| 49 | MACD zero-line · 1h | trend | 84.43 | -15.57 | 92 | 15.2 | -23.42 | -4.56 | -26.06 | 228 |
| 50 | Agent (ML meta-label) | meta | 84.11 | -15.89 | 740 | 20.0 | -10.48 | -1.91 | -16.57 | 346 |
| 51 | OBV trend · 1h | momentum | 83.45 | -16.55 | 191 | 18.3 | -30.66 | -5.74 | -31.54 | 306 |
| 52 | ROC + volume · 1h | momentum | 82.70 | -17.30 | 218 | 23.9 | -28.68 | -5.03 | -32.98 | 386 |
| 53 | Williams %R · 1h | reversion | 82.55 | -17.45 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.06 | -18.05 | -45.66 | 602 |
| 55 | Bollinger reversion · 1h | reversion | 82.16 | -17.84 | 163 | 36.2 | -29.44 | -5.70 | -32.84 | 350 |
| 56 | CCI reversion · 1h | reversion | 82.08 | -17.92 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.37 | -18.63 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | RSI(14) reversion · 1h | reversion | 80.84 | -19.16 | 85 | 24.7 | -16.91 | -2.89 | -24.99 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 80.67 | -19.33 | 145 | 11.7 | -26.79 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 78.93 | -21.07 | 231 | 30.3 | -38.29 | -7.03 | -41.40 | 538 |
| 61 | VWAP momentum · 1h | momentum | 78.92 | -21.08 | 483 | 22.2 | -48.55 | -9.73 | -52.94 | 1252 |
| 62 | Max aggression: 1-day momentum | meta | 77.06 | -22.94 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.93 | -22.16 | -78.97 | 1701 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.16 | -19.31 | -64.95 | 858 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.03 | -19.18 | -74.04 | 1276 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.04 | -22.78 | -67.93 | 1201 |
| 67 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.87 | -19.22 | -80.87 | 1437 |
| 68 | RSI(14) reversion | reversion | 54.55 | -45.45 | 779 | 26.6 | -75.50 | -17.05 | -75.70 | 1628 |
| 69 | VWAP reversion | reversion | 52.68 | -47.32 | 775 | 25.7 | -71.71 | -14.46 | -72.15 | 1477 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -32.42 | -98.86 | 5305 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.95 | -33.22 | -94.26 | 2582 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.04 | -23.78 | -88.71 | 1894 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -28.28 | -91.74 | 2358 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.14 | -25.34 | -91.24 | 2256 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -35.68 | -97.83 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -36.53 | -96.99 | 3595 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.56 | -28.19 | -94.58 | 2554 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.08 | -27.85 | -83.42 | 1727 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -37.80 | -99.44 | 5763 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.28 | -30.24 | -92.73 | 2619 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.84 | -30.76 | -95.84 | 3462 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.34 | -99.77 | 6154 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.86 | -30.70 | -91.92 | 2337 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -39.02 | -97.73 | 3618 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.59 | -38.20 | -98.59 | 4722 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.23 | -35.08 | -94.46 | 2790 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.33 | -27.61 | -84.44 | 1789 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.57 | -40.60 | -99.57 | 6205 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.55 | -23.38 | -87.59 | 2162 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.27 | -27.14 | -88.30 | 2149 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.15 | -34.00 | -96.15 | 3778 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.60 | -34.30 | -89.60 | 2102 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.09 | -34.82 | -96.10 | 4106 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.17 | -99.91 | 8283 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T07:50 | Agent (ML meta-label) | buy | XRP-USD | 9.35 | — | entry |
| 2026-10-22T07:35 | VWAP reversion | buy | BTC-USD | 7.80 | — | entry signal |
| 2026-10-22T07:35 | VWAP reversion | sell | SOL-USD | 2.64 | -0.02 | rebalance down |
| 2026-10-22T07:35 | VWAP reversion | sell | DOGE-USD | 2.65 | -0.02 | rebalance down |
| 2026-10-22T07:25 | Agent (ML meta-label) | sell | XRP-USD | 3.37 | -0.02 | selected signal exited |
| 2026-10-22T07:10 | EMA 20/50 cross · 1h | sell | BTC-USD | 8.65 | -0.14 | stop-loss |
| 2026-10-22T07:10 | VWAP reversion | buy | ETH-USD | 10.63 | — | rebalance up |
| 2026-10-22T07:10 | VWAP reversion | sell | BTC-USD | 13.15 | -0.11 | stop-loss |
| 2026-10-22T07:10 | RSI(14) reversion | sell | BTC-USD | 13.56 | -0.11 | stop-loss |
| 2026-10-22T07:05 | Agent (ML meta-label) | sell | XRP-USD | 6.01 | -0.04 | rebalance down |
| 2026-10-22T07:00 | Bollinger reversion · 1h | buy | DOGE-USD | 20.58 | — | entry signal |
| 2026-10-22T07:00 | Connors RSI(2) · 1h | sell | BTC-USD | 21.73 | -0.38 | stop-loss |
| 2026-10-22T07:00 | Donchian 55/20 · 1h | sell | BTC-USD | 23.42 | -0.40 | exit signal |
| 2026-10-22T07:00 | OBV trend · 1h | sell | BTC-USD | 7.45 | -0.12 | exit signal |
| 2026-10-22T06:55 | Agent (ML meta-label) | buy | XRP-USD | 9.44 | — | entry |
| 2026-10-22T06:55 | RSI(14) reversion | buy | BTC-USD | 13.68 | — | entry signal |
| 2026-10-22T06:50 | Agent (ML meta-label) | sell | XRP-USD | 9.31 | -0.05 | selected signal exited |
| 2026-10-22T06:45 | VWAP reversion | buy | ETH-USD | 2.58 | — | entry signal |
| 2026-10-22T06:40 | VWAP reversion | buy | SOL-USD | 13.26 | — | entry signal |
| 2026-10-22T06:40 | VWAP reversion | buy | DOGE-USD | 13.26 | — | entry signal |
| 2026-10-22T06:40 | VWAP reversion | buy | BTC-USD | 13.26 | — | entry signal |
| 2026-10-22T06:40 | RSI(14) reversion | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-10-22T06:35 | Agent (ML meta-label) | buy | XRP-USD | 9.36 | — | entry |
| 2026-10-22T06:35 | VWAP reversion | sell | SOL-USD | 13.24 | -0.14 | stop-loss |
| 2026-10-22T06:35 | RSI(14) reversion | sell | ETH-USD | 10.96 | -0.13 | stop-loss |
| 2026-10-22T06:30 | VWAP reversion | buy | SOL-USD | 2.74 | — | rebalance up |
| 2026-10-22T06:30 | VWAP reversion | sell | ETH-USD | 10.65 | -0.13 | stop-loss |
| 2026-10-22T06:30 | VWAP reversion | sell | DOGE-USD | 10.60 | -0.09 | stop-loss |
| 2026-10-22T06:30 | VWAP reversion | sell | BTC-USD | 10.62 | -0.13 | stop-loss |
| 2026-10-22T06:30 | RSI(14) reversion | sell | SOL-USD | 13.64 | -0.17 | stop-loss |
| 2026-10-22T06:30 | RSI(14) reversion | sell | BTC-USD | 13.70 | -0.15 | stop-loss |
| 2026-10-22T06:25 | Agent (ML meta-label) | sell | XRP-USD | 9.30 | -0.08 | selected signal exited |
| 2026-10-22T06:05 | Agent (ML meta-label) | buy | XRP-USD | 9.38 | — | entry |
| 2026-10-22T06:00 | Agent (ML meta-label) | sell | XRP-USD | 9.57 | -0.07 | selected signal exited |
| 2026-10-22T06:00 | VWAP reversion | buy | SOL-USD | 10.63 | — | entry signal |
| 2026-10-22T06:00 | VWAP reversion | buy | DOGE-USD | 10.69 | — | entry |
| 2026-10-22T06:00 | VWAP reversion | sell | BTC-USD | 2.68 | -0.02 | rebalance down |
| 2026-10-22T05:55 | VWAP reversion | sell | SOL-USD | 13.28 | -0.17 | stop-loss |
| 2026-10-22T05:55 | VWAP reversion | sell | DOGE-USD | 5.36 | -0.06 | stop-loss |
| 2026-10-22T05:45 | RSI(14) reversion | sell | DOGE-USD | 13.72 | -0.18 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 07:50:05.000163+00:00 -> 2026-10-22 08:00:05.000163+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
