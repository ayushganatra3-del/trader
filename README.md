# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T08:05:05.000131+00:00 · 37644 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 110, win rate 39.1%, fees £3.39, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-26 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, RAPP 12%, THRM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 6010 decisions in 1205 calls, $0.0840 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T08:05 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-10-27T08:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T08:05 | 4 / 1 / 0 | ETH-USD 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.20 | +6.90% | 7 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 4 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.09 | 8.09 | 0 | — | 8.51 | 4.26 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.48 | 1.14 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.57 | 5.57 | 21 | 33.3 | 10.57 | 2.73 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.21 | 2.01 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.09 | -3.35 | -14.02 | 151 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.09 | 0.09 | 0 | — | 2.80 | 1.29 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.87 | -1.13 | 0 | — | -0.04 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 8.31 | 3.46 | -1.94 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -4.13 | -4.73 | -4.49 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -1.99 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.63 | -3.37 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.17 | -3.83 | 121 | 31.4 | -1.91 | -1.09 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.06 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 95.00 | -5.00 | 0 | — | -6.95 | -2.93 | -7.83 | 1 |
| 18 | Hold BTC | benchmark | 94.78 | -5.22 | 0 | — | 0.98 | 0.33 | -9.28 | 1 |
| 19 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 5.02 | 1.64 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.97 | -3.34 | -17.21 | 577 |
| 22 | Copy: Insider buying | copy | 92.26 | -7.74 | 27 | 37.0 | -20.46 | -4.05 | -22.94 | 61 |
| 23 | Donchian 55/20 · 1h | breakout | 91.63 | -8.37 | 49 | 16.3 | -16.01 | -3.62 | -16.70 | 98 |
| 24 | Daily: Momentum burst | daily | 91.39 | -8.61 | 10 | 10.0 | -19.39 | -3.78 | -20.15 | 40 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.16 | -16.91 | 1 |
| 26 | Max aggression: 5-day momentum | meta | 91.21 | -8.79 | 11 | 45.5 | -15.58 | -1.42 | -27.80 | 25 |
| 27 | Squeeze breakout · 1h | breakout | 90.92 | -9.08 | 52 | 23.1 | -4.54 | -1.18 | -12.00 | 91 |
| 28 | Daily: Bullish score | daily | 90.68 | -9.32 | 11 | 18.2 | -6.77 | -0.82 | -14.40 | 13 |
| 29 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.89 | -6.82 | -12.54 | 214 |
| 30 | Parabolic SAR · 1h | trend | 89.90 | -10.10 | 121 | 25.6 | -21.64 | -5.50 | -21.80 | 246 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.39 | -10.61 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 32 | ADX DI cross · 1h | trend | 88.85 | -11.15 | 114 | 17.5 | -13.16 | -2.87 | -14.27 | 262 |
| 33 | Volume breakout · 1h | breakout | 88.62 | -11.38 | 104 | 23.1 | -14.40 | -3.04 | -16.13 | 112 |
| 34 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.03 | -3.27 | -14.77 | 95 |
| 35 | Stochastic reversion · 1h | reversion | 87.80 | -12.20 | 198 | 47.0 | -21.86 | -4.00 | -23.11 | 392 |
| 36 | Bollinger breakout · 1h | breakout | 87.19 | -12.81 | 109 | 26.6 | -14.31 | -2.86 | -17.92 | 239 |
| 37 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.53 | -4.11 | -17.87 | 704 |
| 38 | Keltner breakout · 1h | breakout | 85.60 | -14.39 | 74 | 23.0 | -20.88 | -4.10 | -23.13 | 184 |
| 39 | Connors RSI(2) · 1h | reversion | 85.09 | -14.91 | 174 | 40.2 | -26.47 | -7.95 | -26.96 | 198 |
| 40 | Z-score reversion · 1h | reversion | 84.83 | -15.17 | 116 | 33.6 | -14.53 | -2.38 | -21.48 | 211 |
| 41 | EMA 20/50 cross · 1h | trend | 84.30 | -15.70 | 73 | 11.0 | -21.91 | -4.32 | -23.25 | 130 |
| 42 | RSI momentum · 1h | momentum | 83.52 | -16.48 | 104 | 15.4 | -22.10 | -4.31 | -23.76 | 201 |
| 43 | MACD cross · 1h | trend | 82.93 | -17.07 | 243 | 22.2 | -29.47 | -6.17 | -30.18 | 475 |
| 44 | Supertrend · 1h | trend | 82.91 | -17.09 | 114 | 14.0 | -27.65 | -5.91 | -28.20 | 223 |
| 45 | MFI reversion · 1h | reversion | 82.63 | -17.37 | 263 | 31.6 | -16.42 | -2.53 | -20.54 | 153 |
| 46 | Ichimoku · 1h | trend | 82.21 | -17.79 | 68 | 11.8 | -21.80 | -4.56 | -24.73 | 109 |
| 47 | Triple EMA stack · 1h | trend | 81.65 | -18.35 | 101 | 14.9 | -29.82 | -5.96 | -30.75 | 204 |
| 48 | Bollinger reversion · 1h | reversion | 81.25 | -18.75 | 179 | 37.4 | -29.91 | -6.16 | -31.08 | 368 |
| 49 | CCI reversion · 1h | reversion | 81.14 | -18.86 | 222 | 44.6 | -25.75 | -3.70 | -28.06 | 465 |
| 50 | Williams %R · 1h | reversion | 81.14 | -18.86 | 228 | 46.1 | -35.39 | -6.04 | -35.62 | 539 |
| 51 | MACD zero-line · 1h | trend | 80.42 | -19.58 | 110 | 15.5 | -23.92 | -5.11 | -24.91 | 217 |
| 52 | Donchian 20/10 · 1h | breakout | 79.76 | -20.24 | 99 | 20.2 | -26.01 | -5.10 | -27.53 | 213 |
| 53 | OBV trend · 1h | momentum | 78.91 | -21.09 | 206 | 17.5 | -34.32 | -7.23 | -34.32 | 291 |
| 54 | Agent (ML meta-label) | meta | 78.82 | -21.18 | 924 | 19.4 | -11.58 | -2.13 | -15.52 | 362 |
| 55 | RSI(14) reversion · 1h | reversion | 78.25 | -21.75 | 100 | 24.0 | -17.81 | -2.87 | -24.48 | 208 |
| 56 | Three white soldiers | momentum | 78.23 | -21.77 | 306 | 19.3 | -43.95 | -20.13 | -44.37 | 600 |
| 57 | ROC + volume · 1h | momentum | 76.55 | -23.45 | 250 | 24.0 | -32.48 | -6.48 | -32.97 | 373 |
| 58 | Heikin-Ashi · 1h | trend | 76.47 | -23.53 | 290 | 22.1 | -45.26 | -10.32 | -45.69 | 662 |
| 59 | Candlestick reversal · 1h | reversion | 76.32 | -23.68 | 272 | 27.9 | -35.09 | -6.49 | -35.45 | 573 |
| 60 | EMA 9/21 cross · 1h | trend | 75.18 | -24.82 | 175 | 10.9 | -32.95 | -7.07 | -33.77 | 331 |
| 61 | VWAP momentum · 1h | momentum | 75.01 | -24.99 | 557 | 21.0 | -49.56 | -11.07 | -50.15 | 1238 |
| 62 | Max aggression: 1-day momentum | meta | 67.13 | -32.87 | 19 | 26.3 | -42.14 | -2.87 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.05 | -44.95 | 761 | 22.2 | -74.09 | -26.08 | -74.15 | 1566 |
| 64 | Volume breakout | breakout | 54.02 | -45.98 | 457 | 12.9 | -62.62 | -25.85 | -62.74 | 800 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -43.98 | -98.89 | 5143 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.78 | -22.37 | -79.33 | 1419 |
| 67 | Squeeze breakout | breakout | 50.52 | -49.48 | 598 | 14.2 | -67.60 | -28.44 | -68.10 | 1178 |
| 68 | Donchian 55/20 | breakout | 50.49 | -49.51 | 615 | 19.5 | -71.94 | -23.09 | -72.51 | 1275 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.70 | -44.01 | -93.70 | 2531 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.16 | -30.19 | -89.20 | 1931 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.35 | -36.84 | -91.37 | 2341 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.67 | -30.70 | -90.68 | 2171 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -52.85 | -97.92 | 3528 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -52.65 | -96.12 | 3372 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.10 | -36.15 | -94.12 | 2443 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.22 | -32.22 | -82.58 | 1682 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -53.93 | -99.43 | 5788 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.64 | -41.00 | -92.74 | 2618 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -37.33 | -95.55 | 3382 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -73.69 | -99.78 | 6169 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.25 | -44.80 | -92.25 | 2335 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -62.33 | -97.75 | 3580 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -59.97 | -98.68 | 4811 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -54.39 | -94.54 | 2771 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.32 | -38.75 | -84.33 | 1809 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -65.61 | -99.61 | 6308 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.35 | -29.09 | -88.36 | 2232 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.73 | -19.00 | -77.09 | 1700 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.71 | -37.32 | -90.74 | 2292 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.29 | -47.79 | -96.29 | 3829 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.30 | -50.95 | -90.31 | 2152 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.08 | -18.00 | -76.13 | 1585 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.79 | -96.55 | 4205 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.66 | -99.92 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T08:00 | MACD cross · 1h | buy | ETH-USD | 5.18 | — | entry signal |
| 2026-10-27T07:55 | Volume breakout | buy | SOL-USD | 13.51 | — | entry signal |
| 2026-10-27T07:55 | Squeeze breakout | buy | XRP-USD | 12.64 | — | entry signal |
| 2026-10-27T07:55 | ROC + volume | buy | XRP-USD | 13.79 | — | entry signal |
| 2026-10-27T07:55 | ROC + volume | buy | SOL-USD | 13.79 | — | entry signal |
| 2026-10-27T07:50 | Volume breakout | buy | ETH-USD | 13.53 | — | entry signal |
| 2026-10-27T07:15 | Three white soldiers | sell | XRP-USD | 19.48 | -0.15 | exit signal |
| 2026-10-27T07:15 | Three white soldiers | sell | SOL-USD | 19.48 | -0.14 | exit signal |
| 2026-10-27T07:10 | Three white soldiers | buy | XRP-USD | 19.63 | — | entry signal |
| 2026-10-27T07:10 | Three white soldiers | buy | SOL-USD | 19.63 | — | entry signal |
| 2026-10-27T07:00 | Squeeze breakout · 1h | sell | XRP-USD | 22.48 | -0.32 | exit signal |
| 2026-10-27T07:00 | Bollinger breakout · 1h | sell | DOGE-USD | 21.57 | -0.10 | exit signal |
| 2026-10-27T07:00 | MACD cross · 1h | sell | ETH-USD | 4.82 | -0.07 | exit signal |
| 2026-10-27T07:00 | MACD cross · 1h | sell | DOGE-USD | 4.82 | -0.06 | exit signal |
| 2026-10-27T07:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 20.87 | -0.24 | exit signal |
| 2026-10-27T06:20 | Squeeze breakout | sell | XRP-USD | 12.55 | -0.12 | exit signal |
| 2026-10-27T06:05 | Three white soldiers | sell | XRP-USD | 19.50 | -0.17 | exit signal |
| 2026-10-27T06:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 21.11 | — | entry signal |
| 2026-10-27T05:50 | Three white soldiers | buy | XRP-USD | 19.67 | — | entry |
| 2026-10-27T05:50 | Squeeze breakout | buy | XRP-USD | 12.67 | — | entry signal |
| 2026-10-27T05:25 | Squeeze breakout | sell | DOGE-USD | 12.58 | -0.12 | stop-loss |
| 2026-10-27T05:05 | Squeeze breakout | buy | DOGE-USD | 12.70 | — | entry signal |
| 2026-10-27T05:00 | Volume breakout · 1h | sell | XRP-USD | 21.91 | -0.32 | exit signal |
| 2026-10-27T05:00 | Triple EMA stack · 1h | buy | XRP-USD | 20.38 | — | entry signal |
| 2026-10-27T03:00 | ROC + volume · 1h | sell | XRP-USD | 1.53 | -0.00 | exit signal |
| 2026-10-27T03:00 | ROC + volume · 1h | sell | DOGE-USD | 8.51 | -0.09 | exit signal |
| 2026-10-27T03:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 12.64 | -0.11 | exit signal |
| 2026-10-27T03:00 | MACD cross · 1h | sell | BTC-USD | 4.56 | -0.05 | exit signal |
| 2026-10-27T02:10 | Donchian 55/20 | sell | DOGE-USD | 10.13 | -0.03 | target is flat |
| 2026-10-27T02:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 12.75 | — | entry signal |
| 2026-10-27T02:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 21.12 | — | entry signal |
| 2026-10-27T02:00 | Donchian 55/20 | sell | XRP-USD | 12.59 | -0.09 | exit signal |
| 2026-10-27T01:26 | Squeeze breakout | sell | ETH-USD | 12.65 | -0.07 | stop-loss |
| 2026-10-27T01:26 | Squeeze breakout | sell | DOGE-USD | 12.69 | -0.04 | stop-loss |
| 2026-10-27T01:26 | Donchian 55/20 | buy | XRP-USD | 2.54 | — | rebalance up |
| 2026-10-27T01:26 | Donchian 55/20 | sell | SOL-USD | 12.59 | -0.12 | stop-loss |
| 2026-10-27T01:26 | Donchian 55/20 | sell | ETH-USD | 12.62 | -0.10 | exit signal |
| 2026-10-27T01:26 | Donchian 55/20 | sell | BTC-USD | 5.09 | -0.05 | stop-loss |
| 2026-10-27T01:26 | ROC + volume | sell | ETH-USD | 13.72 | -0.11 | stop-loss |
| 2026-10-27T01:00 | Squeeze breakout · 1h | buy | XRP-USD | 22.81 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 08:05:05.000131+00:00 -> 2026-10-27 08:15:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
