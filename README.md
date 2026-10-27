# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T15:05:05.000203+00:00 · 37986 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.00 (-10.00%)

Closed trades 112, win rate 38.4%, fees £3.45, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 18.00 | +0.02 |
| PLTR | 18.04 | +0.05 |

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

Today: 16675 decisions in 2231 calls, $0.2177 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T15:05 | 9 / 18 / 3 | TECL 14%, AMZN 14% |  |
| Breezy | 2026-10-27T15:05 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-27T15:05 | 8 / 21 / 1 | COIN 71% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.24 | 7.24 | 0 | — | 7.44 | 3.67 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.29 | 1.09 | -6.62 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.42 | 4.42 | 19 | 47.4 | 6.63 | 2.15 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.05 | 1.05 | 0 | — | 2.84 | 1.32 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.18 | -3.64 | -14.11 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.42 | -0.58 | 0 | — | 0.47 | 0.32 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.04 | -1.96 | 80 | 33.8 | 6.75 | 3.23 | -2.29 | 98 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.14 | -1.99 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 97.05 | -2.95 | 0 | — | -0.10 | 0.03 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.24 | -3.76 | 122 | 31.1 | -2.14 | -1.15 | -6.39 | 183 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.57 | 1.08 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Hold BTC | benchmark | 95.37 | -4.63 | 0 | — | 2.42 | 0.57 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.04 | -4.96 | 0 | — | -6.71 | -2.80 | -7.83 | 1 |
| 19 | Gap and go | momentum | 94.49 | -5.51 | 111 | 25.2 | 4.30 | 1.42 | -8.76 | 210 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Copy: Insider buying | copy | 93.37 | -6.63 | 27 | 37.0 | -18.70 | -3.58 | -22.94 | 63 |
| 22 | Opening range 30m | breakout | 93.20 | -6.80 | 272 | 34.2 | -10.11 | -3.04 | -17.21 | 588 |
| 23 | Donchian 55/20 · 1h | breakout | 92.98 | -7.02 | 49 | 16.3 | -14.81 | -3.27 | -16.70 | 98 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 91.64 | -8.36 | 0 | — | -1.71 | -0.12 | -14.57 | 1 |
| 25 | Parabolic SAR · 1h | trend | 91.50 | -8.50 | 121 | 25.6 | -20.89 | -5.22 | -23.02 | 247 |
| 26 | Daily: Momentum burst | daily | 91.27 | -8.73 | 13 | 15.4 | -18.03 | -3.48 | -19.44 | 39 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.18 | -2.15 | -16.91 | 1 |
| 28 | Daily: Bullish score | daily | 91.15 | -8.85 | 11 | 18.2 | -5.27 | -0.58 | -14.40 | 14 |
| 29 | Squeeze breakout · 1h | breakout | 91.03 | -8.97 | 52 | 23.1 | -4.43 | -1.15 | -12.00 | 92 |
| 30 | ADX DI cross · 1h | trend | 90.97 | -9.03 | 119 | 18.5 | -12.07 | -2.63 | -14.45 | 271 |
| 31 | Max aggression: 5-day momentum | meta | 90.07 | -9.93 | 12 | 41.7 | -15.34 | -1.40 | -27.23 | 25 |
| 32 | Agent | meta | 90.00 | -10.00 | 112 | 38.4 | -11.27 | -7.09 | -12.47 | 223 |
| 33 | Volume breakout · 1h | breakout | 89.47 | -10.53 | 105 | 23.8 | -13.23 | -2.75 | -15.94 | 109 |
| 34 | Bollinger breakout · 1h | breakout | 88.24 | -11.76 | 109 | 26.6 | -13.98 | -2.78 | -18.15 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 88.12 | -11.88 | 202 | 47.0 | -21.52 | -3.94 | -23.06 | 394 |
| 36 | Agent (aggressive) | meta | 88.10 | -11.90 | 56 | 35.7 | -11.21 | -3.70 | -14.77 | 99 |
| 37 | Opening range 15m | breakout | 86.70 | -13.30 | 338 | 30.8 | -13.86 | -3.88 | -17.87 | 714 |
| 38 | Z-score reversion · 1h | reversion | 86.37 | -13.63 | 123 | 35.8 | -13.04 | -2.08 | -21.48 | 211 |
| 39 | Keltner breakout · 1h | breakout | 86.25 | -13.75 | 74 | 23.0 | -21.21 | -4.24 | -23.13 | 184 |
| 40 | Connors RSI(2) · 1h | reversion | 85.24 | -14.76 | 175 | 40.6 | -26.36 | -7.90 | -27.00 | 198 |
| 41 | Supertrend · 1h | trend | 85.16 | -14.84 | 114 | 14.0 | -26.23 | -5.42 | -28.46 | 225 |
| 42 | RSI momentum · 1h | momentum | 84.50 | -15.50 | 104 | 15.4 | -21.91 | -4.46 | -24.36 | 203 |
| 43 | EMA 20/50 cross · 1h | trend | 83.98 | -16.02 | 73 | 11.0 | -21.97 | -4.33 | -23.71 | 130 |
| 44 | MACD cross · 1h | trend | 83.93 | -16.07 | 244 | 22.1 | -30.16 | -6.20 | -31.77 | 480 |
| 45 | MFI reversion · 1h | reversion | 83.38 | -16.62 | 268 | 32.1 | -16.20 | -2.50 | -20.70 | 153 |
| 46 | Ichimoku · 1h | trend | 83.22 | -16.78 | 68 | 11.8 | -20.72 | -4.31 | -24.73 | 108 |
| 47 | Triple EMA stack · 1h | trend | 82.90 | -17.10 | 101 | 14.9 | -30.37 | -5.69 | -32.84 | 194 |
| 48 | CCI reversion · 1h | reversion | 82.16 | -17.84 | 227 | 44.9 | -24.79 | -3.51 | -28.06 | 467 |
| 49 | Williams %R · 1h | reversion | 81.80 | -18.20 | 231 | 46.8 | -35.89 | -6.16 | -36.67 | 537 |
| 50 | Donchian 20/10 · 1h | breakout | 81.10 | -18.90 | 99 | 20.2 | -24.72 | -4.78 | -26.79 | 215 |
| 51 | Bollinger reversion · 1h | reversion | 80.93 | -19.07 | 182 | 37.4 | -28.39 | -5.70 | -30.40 | 365 |
| 52 | MACD zero-line · 1h | trend | 80.83 | -19.17 | 111 | 15.3 | -23.13 | -4.88 | -24.74 | 221 |
| 53 | Agent (ML meta-label) | meta | 80.35 | -19.65 | 945 | 20.3 | -12.36 | -2.38 | -17.17 | 337 |
| 54 | OBV trend · 1h | momentum | 79.81 | -20.19 | 209 | 17.7 | -31.17 | -6.67 | -32.67 | 294 |
| 55 | RSI(14) reversion · 1h | reversion | 79.81 | -20.19 | 106 | 26.4 | -13.44 | -2.29 | -24.48 | 202 |
| 56 | ROC + volume · 1h | momentum | 78.47 | -21.52 | 259 | 25.9 | -31.57 | -6.17 | -33.33 | 382 |
| 57 | Three white soldiers | momentum | 77.74 | -22.26 | 314 | 19.1 | -44.26 | -20.25 | -44.80 | 603 |
| 58 | Heikin-Ashi · 1h | trend | 77.69 | -22.31 | 295 | 22.7 | -44.09 | -9.92 | -45.02 | 657 |
| 59 | Candlestick reversal · 1h | reversion | 77.18 | -22.82 | 279 | 29.0 | -34.37 | -6.56 | -35.12 | 570 |
| 60 | VWAP momentum · 1h | momentum | 76.42 | -23.58 | 567 | 21.9 | -48.64 | -10.54 | -50.61 | 1244 |
| 61 | EMA 9/21 cross · 1h | trend | 76.21 | -23.79 | 176 | 10.8 | -31.70 | -6.78 | -33.18 | 336 |
| 62 | Max aggression: 1-day momentum | meta | 69.87 | -30.13 | 20 | 30.0 | -39.88 | -2.71 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.47 | -45.53 | 782 | 22.4 | -74.36 | -26.33 | -74.98 | 1591 |
| 64 | Volume breakout | breakout | 53.13 | -46.87 | 469 | 12.6 | -63.28 | -26.72 | -63.55 | 813 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -41.98 | -98.87 | 5172 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.27 | -23.15 | -80.00 | 1416 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.63 | -43.14 | -93.76 | 2526 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.18 | -30.04 | -89.36 | 1928 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -36.50 | -91.55 | 2351 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.39 | -31.76 | -90.49 | 2171 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -48.67 | -97.89 | 3527 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -52.37 | -96.23 | 3400 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.13 | -36.45 | -94.14 | 2457 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.10 | -31.73 | -82.63 | 1700 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -51.26 | -99.42 | 5763 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -40.84 | -92.92 | 2645 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -38.13 | -95.42 | 3364 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -70.51 | -99.78 | 6167 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.31 | -44.66 | -92.35 | 2323 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.46 | -97.78 | 3586 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.49 | -98.66 | 4808 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.93 | -28.73 | -68.59 | 1189 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -53.88 | -94.63 | 2782 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.45 | -38.91 | -84.61 | 1829 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.40 | -99.61 | 6304 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.29 | -28.82 | -88.35 | 2235 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.66 | -18.93 | -77.03 | 1681 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.55 | -36.53 | -90.63 | 2283 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -46.88 | -96.28 | 3826 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.99 | -48.75 | -90.05 | 2139 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.16 | -23.21 | -73.09 | 1289 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.13 | -17.84 | -76.40 | 1589 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.23 | -96.55 | 4203 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.61 | -99.92 | 8301 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T15:05 | Agent (ML meta-label) | buy | TSLA | 6.70 | — | rebalance up |
| 2026-10-27T15:05 | Agent (ML meta-label) | buy | TNA | 6.69 | — | rebalance up |
| 2026-10-27T15:05 | Agent (ML meta-label) | buy | SOXL | 6.67 | — | rebalance up |
| 2026-10-27T15:05 | Agent (ML meta-label) | buy | AMZN | 6.69 | — | rebalance up |
| 2026-10-27T15:05 | Agent (ML meta-label) | sell | UPRO | 13.38 | 0.01 | selected signal exited |
| 2026-10-27T15:05 | Agent (ML meta-label) | sell | PLTR | 13.38 | 0.00 | selected signal exited |
| 2026-10-27T15:05 | Volume breakout | buy | AAPL | 13.29 | — | entry |
| 2026-10-27T15:05 | Opening range 30m | buy | ETHU | 2.22 | — | entry signal |
| 2026-10-27T15:05 | Opening range 15m | buy | ETHU | 2.07 | — | entry signal |
| 2026-10-27T15:05 | ROC + volume | buy | META | 13.62 | — | entry signal |
| 2026-10-27T15:05 | ROC + volume | buy | AAPL | 13.62 | — | entry |
| 2026-10-27T15:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 104.25 | — | entry |
| 2026-10-27T15:00 | Agent (ML meta-label) | buy | UPRO | 13.36 | — | entry |
| 2026-10-27T15:00 | Agent (ML meta-label) | buy | PLTR | 13.38 | — | following VWAP momentum |
| 2026-10-27T15:00 | Agent (ML meta-label) | sell | TSLA | 6.69 | 0.00 | rebalance down |
| 2026-10-27T15:00 | Agent (ML meta-label) | sell | TNA | 6.66 | 0.03 | rebalance down |
| 2026-10-27T15:00 | Agent (ML meta-label) | sell | SOXL | 6.66 | 0.02 | rebalance down |
| 2026-10-27T15:00 | Agent (ML meta-label) | sell | AMZN | 6.73 | 0.04 | rebalance down |
| 2026-10-27T15:00 | CCI reversion · 1h | buy | SOL-USD | 5.84 | — | rebalance up |
| 2026-10-27T15:00 | CCI reversion · 1h | sell | DOGE-USD | 8.99 | -0.05 | exit signal |
| 2026-10-27T15:00 | Squeeze breakout · 1h | buy | XRP-USD | 22.77 | — | entry signal |
| 2026-10-27T15:00 | OBV trend · 1h | buy | DOGE-USD | 11.82 | — | entry signal |
| 2026-10-27T15:00 | OBV trend · 1h | sell | TSLA | 4.00 | 0.01 | rebalance down |
| 2026-10-27T15:00 | ADX DI cross · 1h | buy | TQQQ | 4.08 | — | entry |
| 2026-10-27T15:00 | ADX DI cross · 1h | buy | SOXL | 9.09 | — | entry |
| 2026-10-27T15:00 | ADX DI cross · 1h | sell | ETH-USD | 4.97 | -0.01 | exit signal |
| 2026-10-27T15:00 | ADX DI cross · 1h | sell | BTC-USD | 8.20 | -0.02 | exit signal |
| 2026-10-27T15:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 21.02 | — | entry signal |
| 2026-10-27T15:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 3.83 | — | entry signal |
| 2026-10-27T15:00 | EMA 9/21 cross · 1h | sell | TSLA | 3.83 | 0.07 | rebalance down |
| 2026-10-27T15:00 | Volume breakout | sell | AAPL | 13.28 | -0.01 | target is flat |
| 2026-10-27T15:00 | Opening range 30m | buy | UPRO | 7.76 | — | entry signal |
| 2026-10-27T15:00 | Opening range 30m | buy | TQQQ | 7.76 | — | entry |
| 2026-10-27T15:00 | Opening range 30m | buy | TECL | 7.76 | — | entry |
| 2026-10-27T15:00 | Opening range 30m | buy | SPY | 7.76 | — | entry signal |
| 2026-10-27T15:00 | Opening range 30m | sell | TNA | 5.55 | 0.04 | rebalance down |
| 2026-10-27T15:00 | Opening range 30m | sell | LABU | 5.52 | 0.16 | rebalance down |
| 2026-10-27T15:00 | Opening range 30m | sell | GOOGL | 5.53 | -0.00 | rebalance down |
| 2026-10-27T15:00 | Opening range 30m | sell | BITX | 5.57 | -0.00 | rebalance down |
| 2026-10-27T15:00 | Opening range 30m | sell | AMZN | 5.55 | 0.00 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 15:05:05.000203+00:00 -> 2026-10-27 15:15:05.000203+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
