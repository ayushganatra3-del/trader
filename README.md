# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T01:25:05.000127+00:00 · 47844 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.52%)

Closed trades 146, win rate 37.7%, fees £4.05, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 1170 decisions in 234 calls, $0.0164 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T01:25 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-05T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T01:25 | 2 / 3 / 0 | ETH-USD 52% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.97 | 12.97 | 0 | — | 14.28 | 4.97 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.64 | 0.64 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.03 | -2.88 | -12.88 | 137 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.11 | -0.89 | 5 | 40.0 | 4.49 | 1.08 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.00 | -2.00 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.59 | -1.02 | -9.60 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.32 | -4.68 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.88 | -5.12 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 17 | Hold BTC | benchmark | 94.44 | -5.55 | 0 | — | -0.70 | 0.05 | -13.22 | 1 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.41 | -0.41 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Max aggression: 5-day momentum | meta | 91.25 | -8.75 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.80 | -9.20 | 103 | 22.3 | -16.33 | -6.04 | -17.67 | 78 |
| 23 | Parabolic SAR · 1h | trend | 89.91 | -10.09 | 155 | 27.1 | -15.30 | -3.39 | -19.35 | 246 |
| 24 | Copy: Insider buying | copy | 89.55 | -10.45 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.20 | -3.54 | -14.15 | 89 |
| 28 | Daily: Bullish score | daily | 87.01 | -12.98 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.82 | -13.18 | 249 | 47.8 | -20.46 | -3.86 | -24.97 | 383 |
| 30 | Donchian 55/20 · 1h | breakout | 86.68 | -13.32 | 62 | 12.9 | -13.08 | -2.78 | -19.91 | 105 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.13 | -13.87 | 1 | 0.0 | -6.85 | -0.99 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 85.07 | -14.93 | 155 | 18.1 | -18.23 | -3.26 | -22.68 | 278 |
| 34 | Volume breakout · 1h | breakout | 84.46 | -15.54 | 132 | 28.8 | -14.13 | -3.23 | -18.08 | 104 |
| 35 | MFI reversion · 1h | reversion | 84.40 | -15.60 | 324 | 34.3 | -13.81 | -2.09 | -18.47 | 153 |
| 36 | Keltner breakout · 1h | breakout | 83.65 | -16.35 | 94 | 24.5 | -20.15 | -4.13 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.38 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 81.99 | -18.01 | 85 | 12.9 | -20.40 | -4.32 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.38 | -18.62 | 148 | 25.0 | -18.10 | -3.67 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.94 | -19.06 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.39 | -20.61 | 92 | 10.9 | -18.57 | -3.26 | -27.87 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 78.80 | -21.20 | 375 | 22.7 | -40.55 | -8.48 | -43.89 | 678 |
| 44 | MACD zero-line · 1h | trend | 78.39 | -21.61 | 141 | 15.6 | -25.00 | -5.16 | -29.62 | 222 |
| 45 | MACD cross · 1h | trend | 78.05 | -21.95 | 311 | 23.2 | -30.67 | -5.98 | -33.62 | 475 |
| 46 | Z-score reversion · 1h | reversion | 77.99 | -22.01 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 77.82 | -22.18 | 147 | 12.9 | -29.41 | -5.30 | -32.06 | 232 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.56 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.90 | -23.10 | 233 | 40.3 | -28.20 | -5.52 | -30.68 | 367 |
| 50 | Williams %R · 1h | reversion | 76.64 | -23.36 | 290 | 47.6 | -33.15 | -5.96 | -34.67 | 525 |
| 51 | RSI momentum · 1h | momentum | 76.41 | -23.59 | 142 | 12.0 | -29.20 | -5.61 | -30.67 | 228 |
| 52 | Triple EMA stack · 1h | trend | 75.86 | -24.14 | 131 | 13.7 | -27.52 | -5.43 | -31.75 | 212 |
| 53 | OBV trend · 1h | momentum | 75.28 | -24.72 | 248 | 17.3 | -30.08 | -6.59 | -30.91 | 294 |
| 54 | Donchian 20/10 · 1h | breakout | 74.30 | -25.70 | 124 | 19.4 | -27.78 | -5.06 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.14 | -25.86 | 321 | 25.5 | -33.36 | -6.46 | -36.25 | 389 |
| 56 | RSI(14) reversion · 1h | reversion | 72.19 | -27.81 | 136 | 28.7 | -20.60 | -3.42 | -26.28 | 217 |
| 57 | EMA 9/21 cross · 1h | trend | 69.51 | -30.49 | 225 | 9.8 | -36.66 | -7.36 | -40.09 | 341 |
| 58 | VWAP momentum · 1h | momentum | 69.40 | -30.60 | 734 | 22.6 | -53.80 | -11.22 | -55.84 | 1223 |
| 59 | Candlestick reversal · 1h | reversion | 69.21 | -30.79 | 376 | 30.1 | -35.61 | -6.65 | -38.05 | 557 |
| 60 | Agent (ML meta-label) | meta | 69.20 | -30.80 | 1445 | 22.3 | -8.37 | -1.47 | -19.84 | 289 |
| 61 | Three white soldiers | momentum | 68.07 | -31.93 | 439 | 16.4 | -47.21 | -21.89 | -47.38 | 633 |
| 62 | Max aggression: 1-day momentum | meta | 66.59 | -33.41 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -45.13 | -98.94 | 5165 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.25 | -25.55 | -80.26 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -46.28 | -93.47 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.83 | -30.88 | -88.96 | 1898 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.86 | -38.49 | -90.88 | 2306 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.41 | -31.98 | -90.42 | 2221 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -52.25 | -97.69 | 3453 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -58.77 | -96.22 | 3385 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.83 | -34.25 | -93.85 | 2482 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.16 | -36.65 | -82.19 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.76 | -99.48 | 5877 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.92 | -42.87 | -92.92 | 2603 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -36.76 | -95.70 | 3426 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -70.72 | -99.79 | 6160 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.69 | -42.37 | -91.73 | 2257 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.16 | -26.46 | -75.16 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -61.02 | -97.76 | 3527 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -60.22 | -98.69 | 4825 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.85 | -28.65 | -70.54 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -52.86 | -94.73 | 2758 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.61 | -36.20 | -84.62 | 1785 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.01 | -99.62 | 6310 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.28 | -30.36 | -88.44 | 2241 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.43 | -18.90 | -76.92 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.69 | -36.78 | -90.69 | 2230 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -49.58 | -96.45 | 3831 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -51.73 | -89.23 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.36 | -27.51 | -65.51 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.80 | -25.29 | -73.81 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.49 | -18.27 | -77.27 | 1604 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.93 | -50.40 | -96.93 | 4248 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -91.96 | -99.93 | 8221 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T01:15 | Agent (ML meta-label) | buy | ETH-USD | 4.61 | — | entry |
| 2026-11-05T01:10 | Agent (ML meta-label) | sell | ETH-USD | 4.59 | -0.03 | selected signal exited |
| 2026-11-05T01:05 | Agent (ML meta-label) | buy | ETH-USD | 4.62 | — | entry |
| 2026-11-05T01:00 | Agent (ML meta-label) | sell | ETH-USD | 4.91 | -0.04 | selected signal exited |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | XRP-USD | 3.29 | 0.06 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | SOL-USD | 3.03 | -0.03 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | ETH-USD | 3.31 | 0.17 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.80 | 0.13 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | BTC-USD | 3.32 | 0.11 | exit signal |
| 2026-11-05T01:00 | MACD cross · 1h | sell | XRP-USD | 3.65 | 0.01 | exit signal |
| 2026-11-05T00:55 | Agent (ML meta-label) | buy | ETH-USD | 4.95 | — | entry |
| 2026-11-04T23:45 | Agent (ML meta-label) | sell | ETH-USD | 4.93 | -0.02 | selected signal exited |
| 2026-11-04T23:40 | Agent (ML meta-label) | buy | ETH-USD | 4.95 | — | entry |
| 2026-11-04T23:05 | Three white soldiers | sell | SOL-USD | 17.05 | -0.03 | exit signal |
| 2026-11-04T23:05 | Three white soldiers | sell | ETH-USD | 16.99 | -0.10 | exit signal |
| 2026-11-04T23:00 | VWAP momentum · 1h | buy | SOL-USD | 3.06 | — | entry signal |
| 2026-11-04T22:55 | Three white soldiers | sell | BTC-USD | 16.97 | -0.14 | stop-loss |
| 2026-11-04T22:45 | Three white soldiers | buy | BTC-USD | 17.11 | — | entry signal |
| 2026-11-04T22:20 | EMA 20/50 cross · 1h | sell | XRP-USD | 3.96 | 0.12 | rebalance down |
| 2026-11-04T22:20 | Three white soldiers | buy | SOL-USD | 17.09 | — | entry signal |
| 2026-11-04T22:20 | Three white soldiers | buy | ETH-USD | 17.09 | — | entry signal |
| 2026-11-04T21:15 | Agent (ML meta-label) | sell | ETH-USD | 5.31 | -0.02 | selected signal exited |
| 2026-11-04T21:05 | Agent (ML meta-label) | buy | ETH-USD | 5.33 | — | entry |
| 2026-11-04T21:00 | Parabolic SAR · 1h | sell | XRP-USD | 8.92 | 0.10 | exit signal |
| 2026-11-04T20:55 | Agent (rotation) | sell | UPRO | 3.12 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TSLA | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TQQQ | 31.06 | -0.34 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | SPY | 3.14 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSTR | 3.18 | 0.02 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSFT | 3.17 | 0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | GOOGL | 3.11 | -0.04 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | COIN | 2.44 | 0.00 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | BITX | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | AAPL | 3.13 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | MSFT | 24.25 | 0.19 | target is flat |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | GOOGL | 23.88 | -0.21 | target is flat |
| 2026-11-04T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 105.47 | -1.14 | target is flat |
| 2026-11-04T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 95.46 | -0.80 | target is flat |
| 2026-11-04T20:55 | Agent (aggressive) | sell | BITX | 42.49 | -0.26 | selected signal exited |
| 2026-11-04T20:55 | Agent | sell | BITX | 17.81 | -0.11 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 01:25:05.000127+00:00 -> 2026-11-05 01:35:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 01:25:05.000127+00:00 -> 2026-11-05 01:35:05.000127+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 01:25:05.000127+00:00 -> 2026-11-05 01:35:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
