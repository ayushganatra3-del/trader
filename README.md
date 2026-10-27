# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T19:04:05.000142+00:00 · 38162 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.09 (-9.91%)

Closed trades 114, win rate 39.5%, fees £3.47, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.05 | +0.05 |

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

Today: 32341 decisions in 2759 calls, $0.4005 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T19:04 | 2 / 22 / 6 | PLTR 14% |  |
| Breezy | 2026-10-27T19:04 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-27T19:04 | 7 / 21 / 2 | COIN 65% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.30 | 7.30 | 0 | — | 8.64 | 4.23 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.54 | 6.54 | 14 | 71.4 | 3.81 | 1.25 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.87 | 4.87 | 20 | 50.0 | 7.53 | 2.45 | -4.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.94 | 0.94 | 0 | — | 1.98 | 0.95 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.92 | -3.86 | -14.07 | 150 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.54 | -0.46 | 0 | — | 0.21 | 0.17 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.91 | -1.09 | 83 | 34.9 | 7.15 | 3.41 | -1.80 | 98 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.76 | -2.24 | 0 | — | -0.91 | -0.34 | -5.99 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.28 | -2.08 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.34 | -3.66 | 122 | 31.1 | -2.47 | -1.40 | -6.39 | 186 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.04 | -3.96 | 0 | — | -5.80 | -2.36 | -7.83 | 1 |
| 16 | Gap and go | momentum | 95.74 | -4.26 | 115 | 27.8 | 5.99 | 1.92 | -8.76 | 210 |
| 17 | Hold BTC | benchmark | 95.73 | -4.27 | 0 | — | 2.25 | 0.54 | -9.28 | 1 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.97 | 0.96 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 20 | Opening range 30m | breakout | 93.80 | -6.20 | 272 | 34.2 | -9.55 | -2.82 | -17.21 | 593 |
| 21 | Donchian 55/20 · 1h | breakout | 93.61 | -6.39 | 49 | 16.3 | -12.96 | -2.87 | -15.40 | 97 |
| 22 | Trend pullback · 1h | trend | 93.57 | -6.43 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 116 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.83 | -7.17 | 0 | — | -1.72 | -0.11 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.23 | -7.77 | 121 | 25.6 | -20.32 | -5.00 | -23.02 | 247 |
| 25 | Copy: Insider buying | copy | 92.10 | -7.90 | 29 | 37.9 | -19.70 | -3.86 | -22.94 | 63 |
| 26 | Daily: Momentum burst | daily | 91.97 | -8.03 | 13 | 15.4 | -18.11 | -3.50 | -19.44 | 39 |
| 27 | ADX DI cross · 1h | trend | 91.77 | -8.23 | 120 | 18.3 | -14.14 | -3.07 | -15.78 | 271 |
| 28 | Daily: Bullish score | daily | 91.42 | -8.58 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.57 | -2.24 | -16.91 | 1 |
| 30 | Max aggression: 5-day momentum | meta | 91.12 | -8.88 | 12 | 41.7 | -14.43 | -1.29 | -27.23 | 25 |
| 31 | Squeeze breakout · 1h | breakout | 90.99 | -9.01 | 52 | 23.1 | -4.54 | -1.18 | -12.18 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.16 | -9.84 | 108 | 25.9 | -12.18 | -2.51 | -15.94 | 113 |
| 33 | Agent | meta | 90.09 | -9.91 | 114 | 39.5 | -11.04 | -7.07 | -12.20 | 221 |
| 34 | Bollinger breakout · 1h | breakout | 88.87 | -11.13 | 109 | 26.6 | -12.69 | -2.49 | -18.15 | 249 |
| 35 | Agent (aggressive) | meta | 88.29 | -11.71 | 57 | 36.8 | -10.60 | -3.48 | -14.77 | 97 |
| 36 | Stochastic reversion · 1h | reversion | 87.76 | -12.24 | 205 | 47.3 | -20.95 | -3.91 | -22.35 | 388 |
| 37 | Opening range 15m | breakout | 87.26 | -12.74 | 338 | 30.8 | -13.33 | -3.68 | -17.87 | 719 |
| 38 | Keltner breakout · 1h | breakout | 87.18 | -12.82 | 74 | 23.0 | -19.93 | -3.86 | -23.13 | 189 |
| 39 | Z-score reversion · 1h | reversion | 86.81 | -13.19 | 125 | 36.0 | -12.71 | -2.01 | -21.48 | 211 |
| 40 | Supertrend · 1h | trend | 85.73 | -14.27 | 114 | 14.0 | -24.08 | -4.91 | -26.88 | 229 |
| 41 | Connors RSI(2) · 1h | reversion | 85.17 | -14.83 | 176 | 40.9 | -24.30 | -7.40 | -24.90 | 184 |
| 42 | RSI momentum · 1h | momentum | 85.05 | -14.95 | 104 | 15.4 | -21.20 | -4.27 | -24.04 | 212 |
| 43 | EMA 20/50 cross · 1h | trend | 84.42 | -15.58 | 73 | 11.0 | -22.99 | -4.56 | -24.63 | 133 |
| 44 | MACD cross · 1h | trend | 84.36 | -15.64 | 244 | 22.1 | -27.81 | -5.46 | -29.89 | 475 |
| 45 | Ichimoku · 1h | trend | 84.03 | -15.97 | 68 | 11.8 | -19.89 | -4.04 | -24.73 | 111 |
| 46 | Triple EMA stack · 1h | trend | 83.59 | -16.41 | 101 | 14.9 | -28.53 | -5.43 | -31.55 | 202 |
| 47 | MFI reversion · 1h | reversion | 83.53 | -16.46 | 273 | 32.2 | -16.14 | -2.49 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.33 | -17.66 | 230 | 45.2 | -24.50 | -3.50 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 81.95 | -18.05 | 99 | 20.2 | -24.32 | -4.65 | -26.89 | 222 |
| 50 | Williams %R · 1h | reversion | 81.93 | -18.07 | 232 | 47.0 | -35.34 | -5.97 | -36.23 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.31 | -18.70 | 111 | 15.3 | -23.48 | -4.97 | -24.89 | 229 |
| 52 | Bollinger reversion · 1h | reversion | 80.73 | -19.27 | 182 | 37.4 | -29.17 | -5.97 | -30.19 | 364 |
| 53 | Agent (ML meta-label) | meta | 80.72 | -19.28 | 977 | 20.5 | -8.50 | -1.47 | -19.28 | 338 |
| 54 | OBV trend · 1h | momentum | 80.46 | -19.54 | 209 | 17.7 | -30.98 | -6.49 | -33.04 | 295 |
| 55 | RSI(14) reversion · 1h | reversion | 80.33 | -19.67 | 107 | 27.1 | -16.49 | -2.85 | -24.48 | 196 |
| 56 | ROC + volume · 1h | momentum | 79.19 | -20.81 | 259 | 25.9 | -31.49 | -6.15 | -33.22 | 385 |
| 57 | Heikin-Ashi · 1h | trend | 78.35 | -21.65 | 297 | 22.9 | -43.24 | -9.51 | -44.57 | 671 |
| 58 | Three white soldiers | momentum | 77.34 | -22.66 | 321 | 19.0 | -44.42 | -19.83 | -45.11 | 606 |
| 59 | Candlestick reversal · 1h | reversion | 77.23 | -22.77 | 285 | 29.5 | -35.48 | -6.79 | -36.13 | 571 |
| 60 | VWAP momentum · 1h | momentum | 76.95 | -23.05 | 574 | 22.1 | -49.12 | -10.63 | -51.06 | 1238 |
| 61 | EMA 9/21 cross · 1h | trend | 76.64 | -23.36 | 176 | 10.8 | -30.42 | -6.44 | -32.33 | 338 |
| 62 | Max aggression: 1-day momentum | meta | 72.12 | -27.88 | 20 | 30.0 | -37.99 | -2.47 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.97 | -46.03 | 805 | 22.4 | -74.86 | -26.22 | -75.36 | 1571 |
| 64 | Volume breakout | breakout | 52.60 | -47.40 | 482 | 12.9 | -63.20 | -25.57 | -63.83 | 805 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -41.81 | -98.87 | 5126 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.23 | -23.21 | -80.00 | 1413 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -43.42 | -93.79 | 2539 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.20 | -30.23 | -89.36 | 1923 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.44 | -37.24 | -91.58 | 2344 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.15 | -31.47 | -90.21 | 2181 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.84 | -48.51 | -97.89 | 3508 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -53.65 | -96.18 | 3368 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -36.14 | -94.06 | 2453 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.39 | -33.10 | -82.65 | 1690 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.17 | -99.42 | 5767 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.81 | -41.01 | -93.02 | 2628 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.39 | -38.42 | -95.39 | 3387 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.31 | -99.78 | 6168 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -44.32 | -92.35 | 2314 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -60.51 | -97.79 | 3596 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -56.69 | -98.65 | 4794 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.40 | -28.46 | -68.69 | 1175 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -53.29 | -94.69 | 2762 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -37.58 | -84.67 | 1816 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.08 | -99.61 | 6300 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.65 | -88.27 | 2224 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.75 | -19.02 | -77.00 | 1678 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -36.38 | -90.68 | 2261 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.22 | -46.14 | -96.24 | 3810 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.07 | -47.55 | -90.11 | 2139 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.08 | -24.59 | -73.64 | 1286 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.20 | -17.93 | -76.42 | 1581 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.28 | -96.55 | 4198 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -91.66 | -99.92 | 8305 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T19:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 104.92 | — | entry |
| 2026-10-27T19:00 | ROC + volume | buy | LABU | 13.49 | — | entry |
| 2026-10-27T18:48 | Copy: Insider buying | buy | PLUR | 11.52 | — | entry |
| 2026-10-27T18:45 | Copy: Insider buying | buy | RAPP | 11.52 | — | entry |
| 2026-10-27T18:45 | Copy: Insider buying | sell | PEP | 12.13 | 0.01 | target is flat |
| 2026-10-27T18:45 | Copy: Insider buying | sell | PAM | 11.28 | -0.84 | target is flat |
| 2026-10-27T18:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.92 | 0.68 | target is flat |
| 2026-10-27T18:30 | Candlestick reversal · 1h | buy | SQQQ | 7.67 | — | entry signal |
| 2026-10-27T18:30 | VWAP momentum · 1h | buy | TSLA | 2.31 | — | entry |
| 2026-10-27T18:30 | VWAP momentum · 1h | buy | TQQQ | 3.84 | — | entry |
| 2026-10-27T18:30 | VWAP momentum · 1h | buy | PLTR | 3.84 | — | entry |
| 2026-10-27T18:30 | VWAP momentum · 1h | sell | SPY | 3.34 | -0.00 | exit signal |
| 2026-10-27T18:30 | VWAP momentum · 1h | sell | MSTR | 3.33 | -0.02 | exit signal |
| 2026-10-27T18:30 | VWAP momentum · 1h | sell | MSFT | 3.33 | -0.01 | exit signal |
| 2026-10-27T18:30 | Heikin-Ashi · 1h | buy | ETH-USD | 1.36 | — | entry |
| 2026-10-27T18:30 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.91 | — | entry |
| 2026-10-27T18:30 | Heikin-Ashi · 1h | buy | BTC-USD | 3.91 | — | entry |
| 2026-10-27T18:30 | Heikin-Ashi · 1h | sell | NVDA | 4.59 | 0.00 | exit signal |
| 2026-10-27T18:30 | Heikin-Ashi · 1h | sell | AAPL | 4.60 | -0.01 | exit signal |
| 2026-10-27T18:30 | Supertrend · 1h | buy | XRP-USD | 1.73 | — | entry |
| 2026-10-27T18:30 | Supertrend · 1h | buy | UPRO | 5.04 | — | entry |
| 2026-10-27T18:30 | Supertrend · 1h | buy | TNA | 5.04 | — | entry |
| 2026-10-27T18:30 | Supertrend · 1h | buy | SPY | 5.04 | — | entry |
| 2026-10-27T18:30 | Supertrend · 1h | buy | AMZN | 5.04 | — | entry signal |
| 2026-10-27T18:30 | Supertrend · 1h | sell | TSLA | 4.50 | 0.12 | rebalance down |
| 2026-10-27T18:30 | Supertrend · 1h | sell | TQQQ | 4.49 | 0.11 | rebalance down |
| 2026-10-27T18:30 | Supertrend · 1h | sell | QQQ | 4.31 | 0.04 | rebalance down |
| 2026-10-27T18:30 | Supertrend · 1h | sell | NVDA | 4.28 | 0.02 | rebalance down |
| 2026-10-27T18:30 | Supertrend · 1h | sell | AAPL | 4.29 | 0.01 | rebalance down |
| 2026-10-27T18:30 | EMA 9/21 cross · 1h | buy | SOL-USD | 3.65 | — | entry |
| 2026-10-27T18:30 | EMA 9/21 cross · 1h | buy | AMZN | 3.65 | — | entry signal |
| 2026-10-27T18:30 | EMA 9/21 cross · 1h | sell | XRP-USD | 3.93 | 0.03 | rebalance down |
| 2026-10-27T18:30 | EMA 9/21 cross · 1h | sell | MSFT | 3.89 | -0.00 | rebalance down |
| 2026-10-27T18:16 | Three white soldiers | buy | TNA | 19.34 | — | entry signal |
| 2026-10-27T18:10 | Day trade: Stocks in Play ORB | sell | SOXL | 24.62 | -0.13 | target is flat |
| 2026-10-27T18:10 | Agent (aggressive) | buy | PLTR | 44.09 | — | following VWAP momentum |
| 2026-10-27T18:10 | Agent | buy | PLTR | 18.01 | — | following VWAP momentum |
| 2026-10-27T18:10 | MFI reversion · 1h | buy | GOOGL | 20.87 | — | entry |
| 2026-10-27T18:10 | Gap and go | buy | SOXL | 23.89 | — | entry |
| 2026-10-27T18:01 | Candlestick reversal · 1h | buy | GOOGL | 4.35 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 19:04:05.000142+00:00 -> 2026-10-27 19:14:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
