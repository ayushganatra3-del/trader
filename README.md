# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T18:44:05.000126+00:00 · 33355 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.28 (-10.72%)

Closed trades 101, win rate 38.6%, fees £3.20, max drawdown -11.13%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 17.84 | -0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 32586 decisions in 2832 calls, $0.4044 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T18:44 | 8 / 14 / 8 | cash |  |
| Breezy | 2026-10-23T18:44 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-23T18:44 | 4 / 21 / 5 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.33 | 6.33 | 0 | — | 7.77 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.54 | -3.21 | -13.74 | 152 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.51 | 0.51 | 0 | — | 3.09 | 1.46 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.21 | -0.79 | 73 | 34.2 | 5.31 | 2.60 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.91 | -2.09 | 0 | — | -0.67 | -0.36 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.35 | -3.65 | 0 | — | 1.30 | 0.39 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.03 | -3.97 | 120 | 30.8 | -2.43 | -1.42 | -6.22 | 195 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.77 | -4.23 | 0 | — | -0.83 | -0.29 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.83 | -5.17 | 0 | — | -6.26 | -2.67 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.81 | -5.18 | 25 | 40.0 | -14.21 | -2.70 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.68 | -6.32 | 95 | 23.2 | -21.61 | -7.11 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.22 | -6.78 | 242 | 34.7 | -10.93 | -3.41 | -17.21 | 562 |
| 23 | Donchian 55/20 · 1h | breakout | 93.08 | -6.92 | 48 | 16.7 | -16.16 | -3.67 | -17.44 | 98 |
| 24 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -15.42 | -1.43 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 91.98 | -8.03 | 118 | 25.4 | -21.02 | -4.99 | -24.17 | 254 |
| 26 | Daily: Momentum burst | daily | 91.69 | -8.31 | 10 | 10.0 | -17.60 | -3.42 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.16 | -8.84 | 108 | 18.5 | -11.69 | -2.40 | -14.53 | 255 |
| 30 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 31 | Daily: Bullish score | daily | 89.34 | -10.66 | 9 | 0.0 | -8.29 | -1.09 | -14.40 | 14 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 89.32 | -10.68 | 0 | — | -5.17 | -0.75 | -14.52 | 1 |
| 33 | Agent | meta | 89.28 | -10.72 | 101 | 38.6 | -11.00 | -7.60 | -11.72 | 206 |
| 34 | Bollinger breakout · 1h | breakout | 88.97 | -11.03 | 105 | 27.6 | -12.29 | -2.44 | -16.56 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.53 | -12.47 | 186 | 45.2 | -20.08 | -3.80 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 37 | Opening range 15m | breakout | 86.38 | -13.62 | 305 | 30.2 | -15.80 | -4.62 | -17.87 | 703 |
| 38 | EMA 20/50 cross · 1h | trend | 86.34 | -13.66 | 71 | 11.3 | -22.64 | -4.53 | -25.11 | 138 |
| 39 | Keltner breakout · 1h | breakout | 86.25 | -13.75 | 73 | 23.3 | -22.75 | -4.84 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 86.02 | -13.98 | 108 | 14.8 | -23.79 | -5.03 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.50 | -14.50 | 101 | 15.8 | -21.59 | -4.64 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.30 | -8.05 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 84.90 | -15.10 | 217 | 23.0 | -22.93 | -4.60 | -26.15 | 454 |
| 44 | Z-score reversion · 1h | reversion | 83.92 | -16.09 | 106 | 34.0 | -14.82 | -2.51 | -21.48 | 197 |
| 45 | Ichimoku · 1h | trend | 83.85 | -16.15 | 65 | 12.3 | -23.77 | -4.97 | -25.68 | 110 |
| 46 | Triple EMA stack · 1h | trend | 83.54 | -16.46 | 98 | 15.3 | -26.21 | -5.26 | -28.44 | 211 |
| 47 | MFI reversion · 1h | reversion | 82.00 | -18.00 | 257 | 31.9 | -17.66 | -2.90 | -20.54 | 144 |
| 48 | MACD zero-line · 1h | trend | 81.89 | -18.11 | 103 | 15.5 | -21.45 | -4.50 | -24.90 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 81.38 | -18.62 | 96 | 19.8 | -24.39 | -4.76 | -27.45 | 217 |
| 50 | Three white soldiers | momentum | 81.27 | -18.73 | 275 | 20.0 | -43.53 | -21.14 | -43.65 | 589 |
| 51 | OBV trend · 1h | momentum | 81.24 | -18.76 | 202 | 17.3 | -32.06 | -7.09 | -33.61 | 305 |
| 52 | Williams %R · 1h | reversion | 81.15 | -18.85 | 213 | 44.1 | -35.34 | -6.35 | -36.69 | 522 |
| 53 | Bollinger reversion · 1h | reversion | 80.36 | -19.64 | 171 | 34.5 | -31.03 | -6.49 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.26 | -19.74 | 198 | 42.9 | -26.49 | -4.00 | -28.17 | 451 |
| 55 | Agent (ML meta-label) | meta | 79.84 | -20.16 | 854 | 18.7 | -13.71 | -2.58 | -15.99 | 375 |
| 56 | Heikin-Ashi · 1h | trend | 78.82 | -21.18 | 269 | 23.0 | -43.11 | -10.14 | -43.80 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.16 | -21.84 | 239 | 23.8 | -30.94 | -6.22 | -32.05 | 380 |
| 58 | RSI(14) reversion · 1h | reversion | 78.03 | -21.97 | 91 | 23.1 | -15.04 | -2.78 | -23.51 | 186 |
| 59 | Candlestick reversal · 1h | reversion | 77.55 | -22.45 | 253 | 28.9 | -34.78 | -6.60 | -36.06 | 540 |
| 60 | EMA 9/21 cross · 1h | trend | 77.32 | -22.68 | 158 | 12.0 | -29.99 | -6.17 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 75.70 | -24.30 | 518 | 21.2 | -50.42 | -11.74 | -50.56 | 1216 |
| 62 | Max aggression: 1-day momentum | meta | 67.21 | -32.79 | 18 | 27.8 | -42.65 | -3.00 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.60 | -42.40 | 706 | 22.7 | -74.83 | -27.49 | -74.84 | 1546 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.77 | -26.32 | -60.77 | 765 |
| 65 | Squeeze breakout | breakout | 53.90 | -46.10 | 547 | 14.3 | -66.04 | -28.84 | -66.19 | 1139 |
| 66 | RSI(14) reversion | reversion | 53.34 | -46.66 | 821 | 26.4 | -76.41 | -19.63 | -76.81 | 1665 |
| 67 | Donchian 55/20 | breakout | 53.11 | -46.89 | 565 | 19.1 | -71.55 | -23.69 | -71.69 | 1251 |
| 68 | EMA 20/50 cross | trend | 51.95 | -48.05 | 615 | 20.0 | -78.81 | -23.90 | -79.10 | 1408 |
| 69 | VWAP reversion | reversion | 50.69 | -49.31 | 814 | 25.1 | -74.51 | -17.57 | -74.75 | 1545 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -45.05 | -98.66 | 5011 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.78 | -47.43 | -93.82 | 2508 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.35 | -30.40 | -88.50 | 1873 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -38.65 | -91.16 | 2301 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.37 | -31.56 | -90.40 | 2147 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.63 | -54.90 | -97.65 | 3445 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.97 | -61.89 | -95.99 | 3322 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -35.55 | -93.75 | 2427 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.66 | -36.40 | -82.70 | 1677 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -55.19 | -99.31 | 5652 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.15 | -42.38 | -92.21 | 2569 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -40.60 | -95.29 | 3349 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.72 | -99.74 | 6074 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.91 | -46.38 | -91.92 | 2304 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -65.84 | -97.51 | 3512 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -59.59 | -98.46 | 4704 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.15 | -60.14 | -94.17 | 2722 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.58 | -39.90 | -83.65 | 1767 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -66.46 | -99.53 | 6150 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.46 | -28.62 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.04 | -38.16 | -90.11 | 2223 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -47.65 | -95.88 | 3735 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -50.82 | -89.37 | 2077 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.01 | -48.16 | -96.06 | 4105 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.80 | -99.90 | 8114 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T18:40 | Three white soldiers | sell | TECL | 20.27 | -0.07 | exit signal |
| 2026-10-23T18:40 | Opening range 30m | buy | UPRO | 2.83 | — | entry |
| 2026-10-23T18:40 | Opening range 30m | buy | TNA | 4.80 | — | rebalance up |
| 2026-10-23T18:40 | Opening range 30m | sell | MSTR | 7.63 | -0.15 | stop-loss |
| 2026-10-23T18:35 | Agent | buy | BITX | 17.86 | — | following Stochastic reversion |
| 2026-10-23T18:30 | Agent (ML meta-label) | buy | IWM | 4.45 | — | entry |
| 2026-10-23T18:30 | Agent (ML meta-label) | buy | ETH-USD | 4.45 | — | entry |
| 2026-10-23T18:30 | Agent (ML meta-label) | sell | SPY | 1.32 | -0.00 | selected signal exited |
| 2026-10-23T18:30 | MFI reversion · 1h | buy | META | 20.52 | — | entry signal |
| 2026-10-23T18:30 | OBV trend · 1h | buy | IWM | 20.28 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | buy | LABU | 5.42 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | buy | IWM | 5.42 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | buy | AMD | 5.42 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | sell | BITX | 8.43 | -0.03 | exit signal |
| 2026-10-23T18:30 | Heikin-Ashi · 1h | sell | TECL | 19.87 | -0.01 | exit signal |
| 2026-10-23T18:30 | MACD cross · 1h | buy | MSFT | 5.38 | — | entry signal |
| 2026-10-23T18:30 | MACD cross · 1h | buy | AMD | 9.44 | — | entry signal |
| 2026-10-23T18:30 | MACD cross · 1h | sell | SOL-USD | 4.68 | -0.02 | rebalance down |
| 2026-10-23T18:25 | Donchian 55/20 | sell | MSTR | 13.25 | -0.12 | exit signal |
| 2026-10-23T18:16 | Agent (ML meta-label) | sell | IWM | 4.71 | -0.01 | selected signal exited |
| 2026-10-23T18:16 | Agent (ML meta-label) | sell | ETH-USD | 4.35 | -0.02 | selected signal exited |
| 2026-10-23T18:15 | Three white soldiers | buy | TECL | 20.33 | — | entry |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | TNA | 2.69 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | TECL | 2.71 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | MSFT | 2.66 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | IWM | 2.66 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | ETH-USD | 2.66 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | AMD | 2.68 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | sell | BITX | 4.25 | -0.03 | exit signal |
| 2026-10-23T18:05 | Agent (ML meta-label) | buy | SPY | 1.32 | — | entry |
| 2026-10-23T18:05 | Agent (ML meta-label) | buy | ETH-USD | 4.37 | — | entry |
| 2026-10-23T18:05 | VWAP momentum · 1h | sell | DOGE-USD | 8.41 | -0.07 | target is flat |
| 2026-10-23T18:00 | Agent (ML meta-label) | buy | IWM | 4.72 | — | entry |
| 2026-10-23T18:00 | Agent (ML meta-label) | sell | ETH-USD | 4.69 | -0.02 | selected signal exited |
| 2026-10-23T18:00 | VWAP momentum · 1h | buy | TECL | 8.43 | — | entry |
| 2026-10-23T18:00 | VWAP momentum · 1h | sell | BTC-USD | 8.43 | -0.05 | exit signal |
| 2026-10-23T18:00 | MACD cross · 1h | buy | SOL-USD | 4.49 | — | rebalance up |
| 2026-10-23T18:00 | MACD cross · 1h | sell | XRP-USD | 12.09 | -0.11 | exit signal |
| 2026-10-23T18:00 | Squeeze breakout | sell | SQQQ | 13.41 | -0.09 | exit signal |
| 2026-10-23T18:00 | ROC + volume | sell | SQQQ | 14.42 | -0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 18:44:05.000126+00:00 -> 2026-10-23 18:54:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
