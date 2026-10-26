# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T19:10:05.000134+00:00 · 36979 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.19 (-9.81%)

Closed trades 108, win rate 38.9%, fees £3.37, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.03 | -0.01 |
| PLTR | 18.20 | +0.34 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-26 | PAM 12%, PEP 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 34809 decisions in 2862 calls, $0.4296 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T19:10 | 6 / 16 / 7 | cash |  |
| Breezy | 2026-10-26T19:10 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-26T19:10 | 7 / 21 / 1 | COIN 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Bollinger reversion | BITX | 2.12 | +2.39% | 13 |
| VWAP momentum | PLTR | 1.73 | +4.99% | 6 |
| Stochastic reversion | BITX | 1.67 | +3.43% | 12 |
| RSI(14) reversion | TSLA | 1.52 | +3.64% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.72 | 7.72 | 0 | — | 8.63 | 4.41 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.39 | 6.39 | 13 | 69.2 | 3.83 | 1.26 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 20 | 30.0 | 10.95 | 2.82 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.55 | 4.55 | 18 | 44.4 | 6.45 | 2.09 | -4.92 | 27 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.65 | -0.35 | 0 | — | 3.05 | 1.20 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -0.23 | -0.08 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.30 | -1.70 | 77 | 33.8 | 7.96 | 3.34 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.09 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.79 | -3.21 | 0 | — | 0.18 | 0.14 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.21 | -3.79 | 120 | 30.8 | -0.87 | -0.41 | -6.28 | 193 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.72 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.92 | -5.08 | 0 | — | -6.82 | -2.89 | -7.83 | 1 |
| 18 | Gap and go | momentum | 94.80 | -5.20 | 105 | 24.8 | 5.09 | 1.67 | -8.76 | 200 |
| 19 | Hold BTC | benchmark | 94.68 | -5.32 | 0 | — | 0.99 | 0.46 | -9.28 | 1 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -7.05 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.79 | -7.21 | 257 | 33.9 | -10.39 | -3.17 | -17.21 | 578 |
| 22 | Copy: Insider buying | copy | 92.17 | -7.83 | 27 | 37.0 | -17.30 | -3.32 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 91.62 | -8.38 | 49 | 16.3 | -15.89 | -3.62 | -16.47 | 98 |
| 24 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.08 | -2.18 | -16.91 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 91.19 | -8.81 | 51 | 23.5 | -2.66 | -0.63 | -11.68 | 92 |
| 26 | Daily: Momentum burst | daily | 91.01 | -8.99 | 10 | 10.0 | -20.03 | -3.86 | -20.67 | 40 |
| 27 | Max aggression: 5-day momentum | meta | 90.62 | -9.38 | 11 | 45.5 | -15.95 | -1.48 | -27.80 | 25 |
| 28 | Daily: Bullish score | daily | 90.57 | -9.43 | 11 | 18.2 | -6.74 | -0.82 | -14.40 | 13 |
| 29 | Agent | meta | 90.19 | -9.81 | 108 | 38.9 | -10.38 | -6.53 | -12.54 | 210 |
| 30 | Parabolic SAR · 1h | trend | 89.46 | -10.54 | 121 | 25.6 | -22.32 | -5.63 | -22.33 | 246 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.21 | -10.79 | 0 | — | -5.37 | -0.76 | -14.57 | 1 |
| 32 | Volume breakout · 1h | breakout | 89.05 | -10.95 | 103 | 23.3 | -12.61 | -2.64 | -15.73 | 111 |
| 33 | ADX DI cross · 1h | trend | 88.92 | -11.08 | 114 | 17.5 | -13.18 | -2.74 | -16.31 | 270 |
| 34 | Agent (aggressive) | meta | 88.61 | -11.39 | 53 | 37.7 | -9.99 | -3.28 | -14.77 | 95 |
| 35 | Stochastic reversion · 1h | reversion | 87.40 | -12.60 | 198 | 47.0 | -20.81 | -3.81 | -22.76 | 394 |
| 36 | Bollinger breakout · 1h | breakout | 87.35 | -12.65 | 107 | 27.1 | -12.26 | -2.39 | -17.52 | 238 |
| 37 | Opening range 15m | breakout | 86.38 | -13.62 | 323 | 30.3 | -15.02 | -4.28 | -17.87 | 718 |
| 38 | Keltner breakout · 1h | breakout | 85.71 | -14.29 | 74 | 23.0 | -22.02 | -4.47 | -23.38 | 186 |
| 39 | Connors RSI(2) · 1h | reversion | 85.01 | -14.99 | 173 | 40.5 | -26.48 | -8.03 | -26.96 | 198 |
| 40 | Z-score reversion · 1h | reversion | 84.84 | -15.16 | 116 | 33.6 | -14.37 | -2.37 | -21.48 | 210 |
| 41 | EMA 20/50 cross · 1h | trend | 84.40 | -15.60 | 72 | 11.1 | -22.07 | -4.44 | -23.47 | 126 |
| 42 | RSI momentum · 1h | momentum | 83.43 | -16.57 | 104 | 15.4 | -22.09 | -4.42 | -23.30 | 204 |
| 43 | MACD cross · 1h | trend | 83.02 | -16.98 | 237 | 22.8 | -29.13 | -6.15 | -29.90 | 473 |
| 44 | Supertrend · 1h | trend | 82.97 | -17.03 | 114 | 14.0 | -27.96 | -6.05 | -28.67 | 224 |
| 45 | MFI reversion · 1h | reversion | 82.36 | -17.64 | 263 | 31.6 | -16.24 | -2.54 | -20.70 | 154 |
| 46 | Ichimoku · 1h | trend | 82.30 | -17.70 | 67 | 11.9 | -22.41 | -4.68 | -24.50 | 110 |
| 47 | Triple EMA stack · 1h | trend | 81.60 | -18.40 | 101 | 14.9 | -30.57 | -6.25 | -30.58 | 209 |
| 48 | Bollinger reversion · 1h | reversion | 80.94 | -19.05 | 179 | 37.4 | -29.21 | -6.00 | -31.14 | 372 |
| 49 | CCI reversion · 1h | reversion | 80.92 | -19.08 | 217 | 43.3 | -24.53 | -3.49 | -28.06 | 467 |
| 50 | Williams %R · 1h | reversion | 80.79 | -19.21 | 228 | 46.1 | -35.04 | -6.02 | -35.60 | 542 |
| 51 | MACD zero-line · 1h | trend | 80.30 | -19.70 | 108 | 15.7 | -23.88 | -5.16 | -24.67 | 218 |
| 52 | Donchian 20/10 · 1h | breakout | 79.64 | -20.36 | 99 | 20.2 | -24.55 | -4.69 | -27.44 | 212 |
| 53 | Agent (ML meta-label) | meta | 78.89 | -21.11 | 922 | 19.3 | -18.12 | -3.64 | -19.75 | 370 |
| 54 | OBV trend · 1h | momentum | 78.89 | -21.11 | 206 | 17.5 | -33.09 | -6.99 | -33.41 | 304 |
| 55 | Three white soldiers | momentum | 78.79 | -21.21 | 300 | 19.3 | -44.09 | -20.70 | -44.09 | 600 |
| 56 | RSI(14) reversion · 1h | reversion | 78.20 | -21.80 | 100 | 24.0 | -17.17 | -3.16 | -24.48 | 199 |
| 57 | Heikin-Ashi · 1h | trend | 76.63 | -23.37 | 286 | 22.4 | -44.83 | -10.28 | -45.66 | 661 |
| 58 | ROC + volume · 1h | momentum | 76.56 | -23.44 | 247 | 23.9 | -30.43 | -6.01 | -32.22 | 380 |
| 59 | Candlestick reversal · 1h | reversion | 76.22 | -23.78 | 272 | 27.9 | -34.35 | -6.38 | -36.00 | 568 |
| 60 | VWAP momentum · 1h | momentum | 75.20 | -24.80 | 548 | 21.0 | -49.91 | -11.30 | -50.43 | 1244 |
| 61 | EMA 9/21 cross · 1h | trend | 75.18 | -24.82 | 173 | 11.0 | -32.02 | -6.53 | -35.09 | 332 |
| 62 | Max aggression: 1-day momentum | meta | 67.45 | -32.55 | 19 | 26.3 | -41.74 | -2.85 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.24 | -44.76 | 759 | 22.1 | -74.26 | -26.82 | -74.43 | 1572 |
| 64 | Volume breakout | breakout | 54.18 | -45.82 | 456 | 12.9 | -62.58 | -26.50 | -62.64 | 799 |
| 65 | Squeeze breakout | breakout | 51.22 | -48.78 | 589 | 14.4 | -67.20 | -28.42 | -67.82 | 1169 |
| 66 | Donchian 55/20 | breakout | 51.15 | -48.85 | 605 | 19.2 | -71.90 | -23.83 | -72.35 | 1276 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -45.52 | -98.91 | 5163 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.25 | -23.68 | -79.27 | 1427 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.88 | -47.42 | -93.91 | 2546 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.35 | -31.28 | -89.35 | 1938 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.33 | -38.58 | -91.36 | 2341 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.68 | -31.15 | -90.68 | 2169 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.96 | -56.19 | -97.96 | 3536 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -60.79 | -96.20 | 3377 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.18 | -37.35 | -94.21 | 2478 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.65 | -35.19 | -82.92 | 1698 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -56.81 | -99.43 | 5797 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -43.24 | -92.66 | 2614 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -38.52 | -95.55 | 3387 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -83.42 | -99.78 | 6171 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.50 | -46.74 | -92.50 | 2344 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -66.71 | -97.73 | 3574 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -61.86 | -98.64 | 4802 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -57.97 | -94.55 | 2766 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.44 | -39.85 | -84.45 | 1810 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -69.10 | -99.60 | 6309 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -29.72 | -88.44 | 2229 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.03 | -19.31 | -77.47 | 1708 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.78 | -38.43 | -90.80 | 2297 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.30 | -49.74 | -96.31 | 3837 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.29 | -50.95 | -90.29 | 2142 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.06 | -17.97 | -76.22 | 1585 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -50.40 | -96.54 | 4217 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -110.96 | -99.92 | 8270 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T19:10 | Agent (ML meta-label) | buy | SOXL | 8.77 | — | entry |
| 2026-10-26T19:10 | Agent (ML meta-label) | sell | TSLA | 8.78 | -0.00 | selected signal exited |
| 2026-10-26T19:05 | Agent (aggressive) | buy | BITX | 44.31 | — | following Bollinger reversion, Stochastic reversion |
| 2026-10-26T19:05 | Agent | buy | BITX | 18.04 | — | following Bollinger reversion, Stochastic reversion |
| 2026-10-26T19:05 | Three white soldiers | sell | MSFT | 19.66 | -0.05 | exit signal |
| 2026-10-26T19:00 | Candlestick reversal · 1h | buy | MSTR | 1.99 | — | entry |
| 2026-10-26T19:00 | Candlestick reversal · 1h | buy | MSFT | 6.35 | — | entry |
| 2026-10-26T19:00 | Candlestick reversal · 1h | sell | SOL-USD | 8.34 | -0.08 | exit signal |
| 2026-10-26T19:00 | ROC + volume · 1h | buy | TQQQ | 2.10 | — | entry |
| 2026-10-26T19:00 | ROC + volume · 1h | buy | TECL | 6.38 | — | entry |
| 2026-10-26T19:00 | ROC + volume · 1h | sell | BTC-USD | 8.48 | -0.11 | exit signal |
| 2026-10-26T19:00 | VWAP momentum · 1h | buy | ETHU | 4.70 | — | entry |
| 2026-10-26T19:00 | VWAP momentum · 1h | buy | COIN | 4.70 | — | entry |
| 2026-10-26T19:00 | VWAP momentum · 1h | sell | SOL-USD | 4.64 | -0.07 | exit signal |
| 2026-10-26T19:00 | VWAP momentum · 1h | sell | BTC-USD | 4.69 | -0.03 | exit signal |
| 2026-10-26T19:00 | Ichimoku · 1h | buy | XRP-USD | 8.27 | — | rebalance up |
| 2026-10-26T19:00 | Ichimoku · 1h | sell | SOL-USD | 13.63 | -0.34 | exit signal |
| 2026-10-26T19:00 | MACD zero-line · 1h | buy | XRP-USD | 11.80 | — | rebalance up |
| 2026-10-26T19:00 | MACD zero-line · 1h | sell | SOL-USD | 19.79 | -0.42 | exit signal |
| 2026-10-26T19:00 | MACD cross · 1h | buy | AMZN | 4.61 | — | entry |
| 2026-10-26T19:00 | MACD cross · 1h | sell | SOL-USD | 4.55 | -0.09 | exit signal |
| 2026-10-26T19:00 | EMA 9/21 cross · 1h | buy | TECL | 6.12 | — | entry |
| 2026-10-26T19:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 5.31 | -0.13 | exit signal |
| 2026-10-26T19:00 | ROC + volume | sell | TECL | 13.75 | -0.08 | target is flat |
| 2026-10-26T18:50 | ROC + volume | buy | TECL | 13.83 | — | entry |
| 2026-10-26T18:45 | Agent (aggressive) | sell | TSLA | 44.29 | -0.05 | selected signal exited |
| 2026-10-26T18:45 | Agent | sell | TSLA | 18.03 | -0.02 | selected signal exited |
| 2026-10-26T18:30 | Agent (ML meta-label) | buy | TSLA | 8.78 | — | following Connors RSI(2), RSI(14) reversion |
| 2026-10-26T18:30 | CCI reversion · 1h | buy | LABU | 4.48 | — | rebalance up |
| 2026-10-26T18:30 | CCI reversion · 1h | buy | GOOGL | 4.44 | — | rebalance up |
| 2026-10-26T18:30 | CCI reversion · 1h | sell | TECL | 4.97 | 0.29 | exit signal |
| 2026-10-26T18:30 | CCI reversion · 1h | sell | AMD | 4.87 | 0.13 | exit signal |
| 2026-10-26T18:30 | RSI momentum · 1h | buy | PLTR | 16.72 | — | entry signal |
| 2026-10-26T18:30 | RSI momentum · 1h | buy | MSFT | 16.73 | — | entry signal |
| 2026-10-26T18:30 | RSI momentum · 1h | sell | TSLA | 4.28 | -0.02 | rebalance down |
| 2026-10-26T18:30 | RSI momentum · 1h | sell | TNA | 4.21 | -0.04 | rebalance down |
| 2026-10-26T18:30 | RSI momentum · 1h | sell | IWM | 4.30 | -0.02 | rebalance down |
| 2026-10-26T18:30 | VWAP momentum · 1h | buy | BITX | 3.97 | — | entry signal |
| 2026-10-26T18:30 | VWAP momentum · 1h | sell | AMZN | 4.70 | -0.02 | exit signal |
| 2026-10-26T18:30 | Heikin-Ashi · 1h | buy | PLTR | 1.32 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 19:10:05.000134+00:00 -> 2026-10-26 19:20:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
