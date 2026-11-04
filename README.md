# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T16:55:05.000136+00:00 · 47382 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.73 (-10.27%)

Closed trades 144, win rate 38.2%, fees £4.01, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 17898 decisions in 2112 calls, $0.2298 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T16:55 | 10 / 17 / 3 | TNA 17%, LABU 14% |  |
| Breezy | 2026-11-04T16:55 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-04T16:55 | 6 / 23 / 1 | COIN 79% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 111.84 | 11.84 | 0 | — | 13.05 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.94 | 7.94 | 17 | 70.6 | 7.38 | 2.26 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.76 | 1.76 | 0 | — | 5.72 | 1.57 | -6.60 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.48 | 0.48 | 5 | 40.0 | 5.42 | 1.22 | -7.93 | 8 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.42 | -0.58 | 27 | 44.4 | -2.14 | -0.64 | -8.23 | 27 |
| 9 | Hold SPY | benchmark | 98.25 | -1.75 | 0 | — | -0.65 | -0.27 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.33 | -3.67 | 111 | 35.1 | 5.98 | 2.77 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 94.98 | -5.02 | 0 | — | -2.44 | -0.89 | -7.64 | 1 |
| 15 | Hold BTC | benchmark | 94.70 | -5.30 | 0 | — | -0.85 | 0.03 | -13.22 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 17 | Agent (rotation) | meta | 94.50 | -5.50 | 163 | 27.6 | -6.03 | -4.75 | -8.68 | 183 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.31 | -5.69 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 19 | Gap and go | momentum | 94.16 | -5.84 | 157 | 27.4 | -0.16 | 0.03 | -8.76 | 223 |
| 20 | Max aggression: 5-day momentum | meta | 92.82 | -7.18 | 16 | 43.8 | -22.49 | -1.24 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Parabolic SAR · 1h | trend | 90.86 | -9.14 | 154 | 26.6 | -13.07 | -2.79 | -18.39 | 243 |
| 23 | Trend pullback · 1h | trend | 90.31 | -9.69 | 103 | 22.3 | -17.04 | -6.33 | -17.97 | 79 |
| 24 | Opening range 30m | breakout | 89.81 | -10.19 | 355 | 33.0 | -15.22 | -5.04 | -17.21 | 591 |
| 25 | Agent | meta | 89.73 | -10.27 | 144 | 38.2 | -11.58 | -6.98 | -12.62 | 205 |
| 26 | Copy: Insider buying | copy | 88.76 | -11.24 | 37 | 37.8 | -22.03 | -4.48 | -23.56 | 63 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.90 | -3.40 | -14.15 | 87 |
| 28 | Donchian 55/20 · 1h | breakout | 87.27 | -12.73 | 62 | 12.9 | -14.07 | -3.03 | -19.85 | 107 |
| 29 | Stochastic reversion · 1h | reversion | 86.72 | -13.28 | 248 | 47.6 | -20.33 | -3.85 | -24.84 | 384 |
| 30 | Daily: Bullish score | daily | 86.56 | -13.44 | 14 | 21.4 | -12.00 | -1.87 | -16.58 | 14 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.96 | -14.04 | 1 | 0.0 | -8.04 | -1.20 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -11.94 | -3.93 | -14.77 | 95 |
| 33 | Volume breakout · 1h | breakout | 85.58 | -14.42 | 130 | 28.5 | -13.12 | -2.95 | -18.08 | 104 |
| 34 | ADX DI cross · 1h | trend | 85.47 | -14.53 | 155 | 18.1 | -19.14 | -3.38 | -23.48 | 270 |
| 35 | Keltner breakout · 1h | breakout | 84.58 | -15.42 | 92 | 22.8 | -21.77 | -4.52 | -24.53 | 184 |
| 36 | MFI reversion · 1h | reversion | 84.52 | -15.48 | 318 | 34.6 | -14.01 | -2.13 | -18.76 | 150 |
| 37 | Opening range 15m | breakout | 83.01 | -17.00 | 433 | 30.3 | -19.93 | -6.10 | -21.19 | 724 |
| 38 | Ichimoku · 1h | trend | 82.67 | -17.33 | 85 | 12.9 | -19.19 | -4.02 | -26.10 | 125 |
| 39 | Connors RSI(2) · 1h | reversion | 82.57 | -17.43 | 192 | 40.6 | -19.19 | -6.31 | -19.59 | 127 |
| 40 | Bollinger breakout · 1h | breakout | 82.06 | -17.94 | 146 | 24.0 | -17.27 | -3.45 | -23.94 | 248 |
| 41 | CCI reversion · 1h | reversion | 80.85 | -19.15 | 277 | 46.2 | -22.27 | -3.30 | -27.71 | 456 |
| 42 | Heikin-Ashi · 1h | trend | 79.45 | -20.55 | 372 | 22.6 | -39.55 | -7.94 | -43.72 | 668 |
| 43 | EMA 20/50 cross · 1h | trend | 79.31 | -20.69 | 92 | 10.9 | -18.06 | -3.36 | -26.61 | 133 |
| 44 | MACD zero-line · 1h | trend | 79.14 | -20.86 | 141 | 15.6 | -24.46 | -5.07 | -29.63 | 219 |
| 45 | MACD cross · 1h | trend | 78.80 | -21.20 | 310 | 22.9 | -31.46 | -6.03 | -34.06 | 474 |
| 46 | Z-score reversion · 1h | reversion | 78.76 | -21.25 | 151 | 37.1 | -13.60 | -1.95 | -23.02 | 220 |
| 47 | Supertrend · 1h | trend | 78.49 | -21.51 | 147 | 12.9 | -26.69 | -4.98 | -30.19 | 237 |
| 48 | RSI momentum · 1h | momentum | 77.18 | -22.82 | 142 | 12.0 | -28.13 | -5.38 | -31.02 | 225 |
| 49 | Bollinger reversion · 1h | reversion | 77.17 | -22.82 | 233 | 40.3 | -27.68 | -5.45 | -30.26 | 381 |
| 50 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.29 | -4.46 | -33.57 | 33 |
| 51 | Williams %R · 1h | reversion | 76.71 | -23.29 | 289 | 47.4 | -35.81 | -6.40 | -37.21 | 534 |
| 52 | Triple EMA stack · 1h | trend | 76.18 | -23.82 | 131 | 13.7 | -28.54 | -5.61 | -32.12 | 209 |
| 53 | OBV trend · 1h | momentum | 75.81 | -24.19 | 248 | 17.3 | -29.76 | -6.47 | -30.90 | 293 |
| 54 | Donchian 20/10 · 1h | breakout | 75.04 | -24.95 | 124 | 19.4 | -26.66 | -4.81 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.67 | -25.33 | 317 | 25.2 | -33.83 | -6.56 | -36.90 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 73.04 | -26.96 | 136 | 28.7 | -19.10 | -3.23 | -26.28 | 208 |
| 57 | Agent (ML meta-label) | meta | 70.44 | -29.56 | 1402 | 22.0 | -5.90 | -1.07 | -17.98 | 283 |
| 58 | VWAP momentum · 1h | momentum | 70.25 | -29.75 | 723 | 22.1 | -54.55 | -11.15 | -56.15 | 1224 |
| 59 | EMA 9/21 cross · 1h | trend | 69.99 | -30.01 | 225 | 9.8 | -36.53 | -7.29 | -40.22 | 340 |
| 60 | Candlestick reversal · 1h | reversion | 69.47 | -30.53 | 376 | 30.1 | -36.19 | -6.87 | -38.96 | 561 |
| 61 | Three white soldiers | momentum | 67.90 | -32.10 | 432 | 16.2 | -47.24 | -21.88 | -47.38 | 630 |
| 62 | Max aggression: 1-day momentum | meta | 66.83 | -33.17 | 24 | 29.2 | -35.71 | -2.12 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.69 | -98.99 | 5185 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.96 | -24.03 | -80.27 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -44.04 | -93.47 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -30.02 | -89.13 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.97 | -35.82 | -91.19 | 2319 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.30 | -31.38 | -90.38 | 2197 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -48.91 | -97.75 | 3454 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -52.60 | -96.26 | 3364 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.48 | -32.78 | -93.61 | 2448 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.10 | -36.13 | -82.17 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.34 | -99.49 | 5905 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -41.38 | -93.08 | 2610 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.47 | -36.90 | -95.49 | 3371 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -67.72 | -99.80 | 6163 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.68 | -40.93 | -91.85 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.87 | -26.64 | -74.95 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -55.78 | -97.76 | 3502 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -59.09 | -98.70 | 4830 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.33 | -27.07 | -70.53 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -51.01 | -94.86 | 2767 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.63 | -35.79 | -84.90 | 1795 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.74 | -99.63 | 6313 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.07 | -29.53 | -88.45 | 2247 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.36 | -18.85 | -77.05 | 1722 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.52 | -36.83 | -90.63 | 2242 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -48.81 | -96.54 | 3836 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.07 | -48.03 | -89.37 | 2142 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.23 | -27.22 | -65.64 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.46 | -24.18 | -73.97 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.78 | -18.54 | -77.59 | 1619 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.93 | -51.33 | -96.99 | 4251 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.31 | -99.92 | 8199 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T16:55 | Agent (rotation) | buy | UPRO | 3.15 | — | entry |
| 2026-11-04T16:55 | Agent (rotation) | buy | SPY | 3.15 | — | entry |
| 2026-11-04T16:55 | Agent (rotation) | buy | GOOGL | 3.15 | — | entry |
| 2026-11-04T16:55 | Agent (ML meta-label) | buy | AMD | 5.00 | — | following Supertrend |
| 2026-11-04T16:55 | Agent (ML meta-label) | sell | GOOGL | 5.00 | 0.00 | selected signal exited |
| 2026-11-04T16:55 | Three white soldiers | buy | SPY | 16.98 | — | entry |
| 2026-11-04T16:55 | Opening range 30m | buy | UPRO | 4.70 | — | entry signal |
| 2026-11-04T16:55 | Opening range 30m | buy | SPY | 8.98 | — | entry signal |
| 2026-11-04T16:55 | Opening range 30m | buy | GOOGL | 8.98 | — | entry signal |
| 2026-11-04T16:55 | Opening range 15m | buy | UPRO | 7.55 | — | entry signal |
| 2026-11-04T16:55 | Opening range 15m | buy | SPY | 7.55 | — | entry signal |
| 2026-11-04T16:50 | Agent (ML meta-label) | buy | GOOGL | 5.00 | — | entry |
| 2026-11-04T16:50 | Agent (ML meta-label) | sell | AMD | 5.00 | -0.03 | selected signal exited |
| 2026-11-04T16:50 | Three white soldiers | buy | META | 16.97 | — | entry signal |
| 2026-11-04T16:50 | Three white soldiers | buy | GOOGL | 16.97 | — | entry signal |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | UPRO | 5.01 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | TQQQ | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | TNA | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | SPY | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | IWM | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | BITX | 5.02 | — | following Z-score reversion |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | AMZN | 5.02 | — | entry |
| 2026-11-04T16:45 | Agent (ML meta-label) | buy | AMD | 5.02 | — | following Supertrend |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | SQQQ | 6.57 | 0.05 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | MSTR | 5.05 | 0.01 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | MSFT | 5.04 | 0.02 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | ETHU | 5.04 | 0.01 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | COIN | 5.08 | 0.00 | rebalance down |
| 2026-11-04T16:45 | Agent (ML meta-label) | sell | AAPL | 5.03 | -0.01 | rebalance down |
| 2026-11-04T16:45 | EMA 20/50 cross · 1h | buy | MSFT | 3.98 | — | entry |
| 2026-11-04T16:45 | EMA 20/50 cross · 1h | sell | LABU | 3.98 | -0.08 | rebalance down |
| 2026-11-04T16:40 | Agent (ML meta-label) | buy | SQQQ | 5.15 | — | rebalance up |
| 2026-11-04T16:40 | Agent (ML meta-label) | sell | BITX | 10.06 | 0.02 | selected signal exited |
| 2026-11-04T16:40 | MFI reversion · 1h | sell | TSLA | 21.01 | 0.06 | target is flat |
| 2026-11-04T16:35 | Agent (ML meta-label) | buy | MSTR | 3.63 | — | rebalance up |
| 2026-11-04T16:35 | Agent (ML meta-label) | buy | MSFT | 3.60 | — | rebalance up |
| 2026-11-04T16:35 | Agent (ML meta-label) | buy | ETHU | 3.65 | — | rebalance up |
| 2026-11-04T16:35 | Agent (ML meta-label) | buy | COIN | 3.67 | — | rebalance up |
| 2026-11-04T16:35 | Agent (ML meta-label) | buy | BITX | 3.62 | — | rebalance up |
| 2026-11-04T16:35 | Agent (ML meta-label) | buy | AAPL | 3.65 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 16:55:05.000136+00:00 -> 2026-11-04 17:05:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 16:55:05.000136+00:00 -> 2026-11-04 17:05:05.000136+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 16:55:05.000136+00:00 -> 2026-11-04 17:05:05.000136+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
