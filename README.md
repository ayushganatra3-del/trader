# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T20:24:05.000127+00:00 · 46522 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.40 (-9.60%)

Closed trades 142, win rate 38.7%, fees £3.97, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-03 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 34560 decisions in 2958 calls, $0.4279 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T20:24 | 5 / 21 / 4 | AMZN 15%, TECL 15% |  |
| Breezy | 2026-11-03T20:24 | 0 / 30 / 0 | cash |  |
| Boozy | 2026-11-03T20:24 | 8 / 19 / 3 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| MACD zero-line | MSFT | 1.87 | +0.67% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.13 | 9.13 | 0 | — | 10.28 | 4.53 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.31 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 26 | 26.9 | 7.95 | 2.05 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.97 | -2.94 | -12.71 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.82 | -3.18 | 0 | — | -1.80 | -0.95 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.29 | -3.71 | 107 | 34.6 | 4.24 | 2.04 | -3.82 | 94 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.83 | -6.25 | 21 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.95 | -4.05 | 5 | 40.0 | 0.79 | 0.32 | -7.93 | 8 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 95.73 | -4.27 | 0 | — | -0.91 | -0.27 | -6.60 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.22 | -4.78 | 0 | — | -4.35 | -1.64 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.67 | -5.33 | 28 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.33 | -5.67 | 0 | — | -3.32 | -1.28 | -7.64 | 1 |
| 17 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.75 | -5.82 | -8.64 | 171 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -1.85 | -0.58 | -8.88 | 213 |
| 19 | Hold BTC | benchmark | 91.54 | -8.46 | 0 | — | 0.15 | 0.24 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.63 | -9.37 | 102 | 21.6 | -16.54 | -6.18 | -17.50 | 79 |
| 22 | Agent | meta | 90.40 | -9.60 | 142 | 38.7 | -10.56 | -6.45 | -12.22 | 204 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 341 | 32.6 | -14.17 | -4.63 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 89.22 | -10.78 | 61 | 23.0 | -8.57 | -2.98 | -13.79 | 90 |
| 25 | Copy: Insider buying | copy | 88.55 | -11.45 | 37 | 37.8 | -22.20 | -4.56 | -23.13 | 61 |
| 26 | Parabolic SAR · 1h | trend | 88.46 | -11.54 | 151 | 27.2 | -13.96 | -3.21 | -17.44 | 238 |
| 27 | Donchian 55/20 · 1h | breakout | 88.43 | -11.57 | 60 | 13.3 | -14.58 | -3.31 | -18.06 | 100 |
| 28 | Daily: Bullish score | daily | 88.42 | -11.58 | 14 | 21.4 | -7.64 | -1.07 | -14.82 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.42 | -13.58 | 1 | 0.0 | -6.38 | -0.91 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.33 | -13.67 | 68 | 32.4 | -12.14 | -4.07 | -14.77 | 93 |
| 31 | Max aggression: 5-day momentum | meta | 85.26 | -14.73 | 15 | 40.0 | -29.14 | -1.93 | -36.71 | 25 |
| 32 | Stochastic reversion · 1h | reversion | 84.66 | -15.34 | 241 | 46.9 | -23.20 | -4.69 | -25.33 | 387 |
| 33 | Volume breakout · 1h | breakout | 84.61 | -15.39 | 129 | 28.7 | -14.95 | -3.45 | -18.08 | 91 |
| 34 | MFI reversion · 1h | reversion | 84.41 | -15.59 | 308 | 33.4 | -14.67 | -2.29 | -17.89 | 150 |
| 35 | Keltner breakout · 1h | breakout | 84.14 | -15.86 | 89 | 23.6 | -21.09 | -4.45 | -22.20 | 164 |
| 36 | Connors RSI(2) · 1h | reversion | 83.90 | -16.10 | 191 | 40.8 | -19.68 | -6.60 | -20.18 | 131 |
| 37 | ADX DI cross · 1h | trend | 83.02 | -16.98 | 149 | 18.1 | -19.55 | -3.84 | -21.89 | 255 |
| 38 | Opening range 15m | breakout | 82.55 | -17.45 | 415 | 29.9 | -18.98 | -5.74 | -20.73 | 716 |
| 39 | Bollinger breakout · 1h | breakout | 81.38 | -18.62 | 140 | 25.0 | -17.54 | -3.58 | -23.31 | 231 |
| 40 | Ichimoku · 1h | trend | 81.26 | -18.74 | 84 | 13.1 | -17.79 | -3.63 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 79.68 | -20.32 | 90 | 11.1 | -18.19 | -3.29 | -27.05 | 128 |
| 42 | CCI reversion · 1h | reversion | 79.02 | -20.98 | 268 | 44.8 | -24.89 | -3.87 | -27.71 | 450 |
| 43 | Bollinger reversion · 1h | reversion | 78.21 | -21.79 | 226 | 38.9 | -27.19 | -5.37 | -29.70 | 375 |
| 44 | MACD zero-line · 1h | trend | 77.77 | -22.23 | 136 | 15.4 | -25.33 | -5.66 | -27.55 | 213 |
| 45 | Supertrend · 1h | trend | 77.62 | -22.38 | 141 | 12.8 | -29.89 | -5.48 | -31.30 | 217 |
| 46 | Z-score reversion · 1h | reversion | 77.37 | -22.63 | 142 | 34.5 | -14.60 | -2.15 | -23.02 | 218 |
| 47 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.80 | -4.40 | -33.56 | 33 |
| 48 | MACD cross · 1h | trend | 76.90 | -23.10 | 301 | 23.6 | -32.23 | -6.35 | -34.56 | 484 |
| 49 | Williams %R · 1h | reversion | 76.71 | -23.29 | 278 | 46.4 | -36.23 | -6.57 | -37.32 | 525 |
| 50 | RSI momentum · 1h | momentum | 76.44 | -23.56 | 136 | 12.5 | -28.35 | -5.52 | -30.43 | 214 |
| 51 | Triple EMA stack · 1h | trend | 76.05 | -23.95 | 126 | 14.3 | -27.88 | -5.45 | -31.60 | 202 |
| 52 | Heikin-Ashi · 1h | trend | 75.73 | -24.27 | 365 | 22.7 | -40.68 | -8.78 | -43.46 | 666 |
| 53 | OBV trend · 1h | momentum | 75.49 | -24.51 | 242 | 17.4 | -29.28 | -6.28 | -31.26 | 291 |
| 54 | Donchian 20/10 · 1h | breakout | 75.15 | -24.85 | 120 | 20.0 | -28.41 | -5.25 | -30.44 | 206 |
| 55 | ROC + volume · 1h | momentum | 73.83 | -26.17 | 304 | 25.7 | -35.86 | -7.10 | -36.39 | 374 |
| 56 | RSI(14) reversion · 1h | reversion | 72.86 | -27.14 | 130 | 26.2 | -21.02 | -4.00 | -26.28 | 195 |
| 57 | Candlestick reversal · 1h | reversion | 70.73 | -29.27 | 361 | 28.5 | -33.71 | -6.42 | -37.04 | 536 |
| 58 | Agent (ML meta-label) | meta | 69.69 | -30.31 | 1370 | 21.8 | -13.37 | -2.56 | -18.39 | 270 |
| 59 | EMA 9/21 cross · 1h | trend | 69.05 | -30.95 | 219 | 9.6 | -37.63 | -7.69 | -39.23 | 329 |
| 60 | Three white soldiers | momentum | 68.82 | -31.18 | 419 | 16.0 | -46.49 | -22.10 | -46.50 | 620 |
| 61 | Max aggression: 1-day momentum | meta | 68.70 | -31.30 | 23 | 30.4 | -32.34 | -1.83 | -50.32 | 42 |
| 62 | VWAP momentum · 1h | momentum | 68.35 | -31.65 | 708 | 21.5 | -54.64 | -10.84 | -57.30 | 1230 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -44.05 | -98.93 | 5152 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.45 | -23.63 | -80.34 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -46.30 | -93.42 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.72 | -30.85 | -89.04 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.85 | -36.42 | -91.10 | 2315 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.70 | -33.05 | -90.80 | 2214 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -54.66 | -97.71 | 3467 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -60.11 | -96.30 | 3368 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -34.51 | -93.55 | 2416 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.59 | -34.74 | -82.11 | 1661 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -55.95 | -99.47 | 5872 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.93 | -44.63 | -93.00 | 2619 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -38.52 | -95.38 | 3371 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -80.43 | -99.80 | 6174 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.88 | -46.22 | -91.89 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.57 | -26.63 | -75.02 | 1545 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -65.78 | -97.79 | 3523 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -65.13 | -98.68 | 4825 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -29.08 | -70.27 | 1201 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -56.27 | -94.73 | 2778 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -38.20 | -84.87 | 1793 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -74.83 | -99.62 | 6316 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.13 | -30.69 | -88.21 | 2240 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.36 | -19.15 | -76.73 | 1690 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.09 | -38.06 | -90.13 | 2207 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.46 | -52.71 | -96.47 | 3822 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -56.65 | -89.40 | 2124 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.97 | -27.84 | -65.65 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.41 | -25.05 | -74.11 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.98 | -19.06 | -77.19 | 1600 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.85 | -52.65 | -96.86 | 4238 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.17 | -99.92 | 8200 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T20:15 | Agent (ML meta-label) | buy | ETHU | 3.53 | — | rebalance up |
| 2026-11-03T20:15 | Three white soldiers | sell | NVDA | 17.24 | -0.04 | exit signal |
| 2026-11-03T20:15 | Three white soldiers | sell | ETH-USD | 17.10 | -0.17 | stop-loss |
| 2026-11-03T20:15 | Three white soldiers | sell | AMD | 17.21 | -0.06 | exit signal |
| 2026-11-03T20:10 | OBV trend · 1h | buy | LABU | 3.84 | — | rebalance up |
| 2026-11-03T20:10 | OBV trend · 1h | sell | IWM | 14.20 | -0.01 | target is flat |
| 2026-11-03T20:10 | Three white soldiers | buy | NVDA | 17.27 | — | entry signal |
| 2026-11-03T20:10 | Three white soldiers | buy | MSFT | 17.27 | — | entry signal |
| 2026-11-03T20:10 | Three white soldiers | buy | ETH-USD | 17.27 | — | entry signal |
| 2026-11-03T20:10 | Three white soldiers | buy | AMD | 17.27 | — | entry signal |
| 2026-11-03T20:05 | Agent (ML meta-label) | buy | TSLA | 5.84 | — | rebalance up |
| 2026-11-03T20:05 | Agent (ML meta-label) | buy | MSTR | 15.21 | — | rebalance up |
| 2026-11-03T20:05 | Agent (ML meta-label) | sell | GOOGL | 13.91 | -0.03 | selected signal exited |
| 2026-11-03T20:05 | Agent (ML meta-label) | sell | BITX | 13.99 | 0.03 | selected signal exited |
| 2026-11-03T20:00 | Agent (aggressive) | sell | LABU | 43.04 | -0.26 | selected signal exited |
| 2026-11-03T20:00 | Agent | sell | LABU | 17.97 | -0.14 | selected signal exited |
| 2026-11-03T20:00 | Copy: Insider buying | buy | RAPP | 8.97 | — | entry |
| 2026-11-03T20:00 | Copy: Insider buying | buy | BBTX | 10.07 | — | rebalance up |
| 2026-11-03T20:00 | Copy: Insider buying | sell | RENT | 8.42 | -2.56 | target is flat |
| 2026-11-03T20:00 | Copy: Insider buying | sell | FBK | 10.62 | 0.29 | target is flat |
| 2026-11-03T20:00 | Heikin-Ashi · 1h | buy | MSTR | 8.37 | — | rebalance up |
| 2026-11-03T20:00 | Heikin-Ashi · 1h | sell | XRP-USD | 6.35 | 0.07 | exit signal |
| 2026-11-03T20:00 | Heikin-Ashi · 1h | sell | SOL-USD | 6.34 | -0.02 | exit signal |
| 2026-11-03T20:00 | Heikin-Ashi · 1h | sell | ETH-USD | 6.33 | 0.00 | exit signal |
| 2026-11-03T20:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 6.34 | 0.01 | exit signal |
| 2026-11-03T20:00 | Heikin-Ashi · 1h | sell | BTC-USD | 6.35 | 0.00 | exit signal |
| 2026-11-03T19:57 | Agent (ML meta-label) | buy | MSTR | 2.24 | — | entry |
| 2026-11-03T19:57 | VWAP momentum · 1h | buy | LABU | 4.26 | — | entry |
| 2026-11-03T19:57 | VWAP momentum · 1h | sell | SPY | 4.26 | -0.01 | target is flat |
| 2026-11-03T19:57 | Opening range 15m | sell | TQQQ | 2.92 | -0.02 | stop-loss |
| 2026-11-03T19:55 | Agent (ML meta-label) | buy | GOOGL | 8.17 | — | rebalance up |
| 2026-11-03T19:55 | Agent (ML meta-label) | sell | MSTR | 10.41 | -0.08 | selected signal exited |
| 2026-11-03T19:55 | MFI reversion · 1h | buy | LABU | 2.94 | — | entry |
| 2026-11-03T19:55 | MFI reversion · 1h | buy | AMZN | 14.03 | — | entry |
| 2026-11-03T19:55 | MFI reversion · 1h | sell | TSLA | 16.80 | -0.09 | target is flat |
| 2026-11-03T19:55 | Candlestick reversal · 1h | sell | ETHU | 8.81 | -0.05 | target is flat |
| 2026-11-03T19:55 | OBV trend · 1h | buy | IWM | 14.20 | — | entry |
| 2026-11-03T19:55 | OBV trend · 1h | sell | TNA | 14.20 | -0.15 | target is flat |
| 2026-11-03T19:55 | ROC + volume · 1h | buy | AMZN | 7.36 | — | entry |
| 2026-11-03T19:55 | Opening range 30m | buy | AMZN | 8.00 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 20:24:05.000127+00:00 -> 2026-11-03 20:34:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 20:24:05.000127+00:00 -> 2026-11-03 20:34:05.000127+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 20:24:05.000127+00:00 -> 2026-11-03 20:34:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
