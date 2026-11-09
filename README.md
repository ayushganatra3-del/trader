# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T20:35:05.000148+00:00 · 53772 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.87 (-13.13%)

Closed trades 160, win rate 35.6%, fees £4.97, max drawdown -13.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.38 | -0.12 |
| SQQQ | 17.30 | -0.14 |
| TSLA | 17.57 | +0.08 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 35730 decisions in 3180 calls, $0.4442 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T20:35 | 0 / 23 / 7 | cash |  |
| Breezy | 2026-11-09T20:35 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-09T20:35 | 5 / 23 / 2 | COIN 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 118.39 | 18.39 | 19 | 68.4 | 19.70 | 3.89 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.76 | 12.76 | 0 | — | 14.21 | 4.81 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.71 | 12.71 | 30 | 26.7 | 20.96 | 3.09 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.70 | 4.70 | 30 | 43.3 | 4.58 | 1.16 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 102.30 | 2.30 | 123 | 35.0 | 10.81 | 3.81 | -2.27 | 89 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.81 | 1.81 | 7 | 42.9 | -0.04 | 0.29 | -18.69 | 8 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 101.21 | 1.21 | 0 | — | 4.90 | 1.41 | -6.60 | 1 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 99.19 | -0.81 | 181 | 29.8 | 4.32 | 1.23 | -9.06 | 239 |
| 11 | Agent (rotation) | meta | 98.59 | -1.41 | 176 | 27.8 | -2.95 | -1.08 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -13.08 | -3.39 | -13.08 | 151 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.67 | -3.33 | 0 | — | -1.23 | -0.35 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.58 | -5.42 | 0 | — | -3.79 | -0.98 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.84 | -6.16 | 21 | 19.0 | -7.56 | -6.48 | -8.04 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.89 | -7.11 | 0 | — | -3.86 | -1.01 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.68 | -7.32 | 108 | 23.1 | -13.60 | -5.09 | -17.96 | 79 |
| 20 | Copy: Insider buying | copy | 91.67 | -8.33 | 42 | 38.1 | -9.88 | -2.12 | -16.06 | 63 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 91.10 | -8.90 | 378 | 32.3 | -12.71 | -3.94 | -15.24 | 595 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.56 | -3.45 | -14.68 | 80 |
| 24 | Agent | meta | 86.87 | -13.13 | 160 | 35.6 | -13.64 | -7.08 | -14.10 | 205 |
| 25 | Hold BTC | benchmark | 86.66 | -13.34 | 1 | 0.0 | -5.23 | -0.61 | -15.58 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.02 | -13.97 | 167 | 26.9 | -10.87 | -1.96 | -21.29 | 227 |
| 27 | Daily: Bullish score | daily | 85.85 | -14.15 | 15 | 20.0 | -10.55 | -1.62 | -17.42 | 14 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 84.20 | -15.80 | 2 | 0.0 | -7.11 | -0.76 | -24.16 | 1 |
| 29 | Agent (aggressive) | meta | 84.04 | -15.96 | 75 | 32.0 | -16.37 | -4.70 | -18.49 | 94 |
| 30 | Opening range 15m | breakout | 84.00 | -16.00 | 466 | 30.5 | -17.85 | -4.98 | -19.91 | 728 |
| 31 | Donchian 55/20 · 1h | breakout | 83.32 | -16.68 | 71 | 14.1 | -18.24 | -4.01 | -22.45 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 83.10 | -16.90 | 279 | 48.4 | -24.03 | -3.57 | -28.05 | 387 |
| 33 | Keltner breakout · 1h | breakout | 82.55 | -17.45 | 107 | 23.4 | -21.55 | -4.31 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.46 | -18.54 | 145 | 27.6 | -14.83 | -3.37 | -21.11 | 96 |
| 35 | Connors RSI(2) · 1h | reversion | 80.36 | -19.64 | 205 | 40.0 | -19.89 | -6.68 | -19.99 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 80.26 | -19.74 | 400 | 22.8 | -39.29 | -7.16 | -43.08 | 674 |
| 37 | ADX DI cross · 1h | trend | 79.77 | -20.23 | 179 | 18.4 | -21.93 | -3.77 | -28.34 | 274 |
| 38 | MFI reversion · 1h | reversion | 79.39 | -20.61 | 351 | 34.5 | -16.51 | -2.11 | -21.23 | 166 |
| 39 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -40.12 | -2.69 | -45.81 | 25 |
| 40 | CCI reversion · 1h | reversion | 79.10 | -20.90 | 319 | 45.8 | -23.96 | -3.66 | -30.29 | 462 |
| 41 | Ichimoku · 1h | trend | 77.66 | -22.34 | 96 | 15.6 | -29.11 | -8.38 | -29.33 | 119 |
| 42 | Bollinger breakout · 1h | breakout | 76.89 | -23.11 | 170 | 22.9 | -22.54 | -4.73 | -27.87 | 240 |
| 43 | MACD cross · 1h | trend | 75.62 | -24.38 | 349 | 22.6 | -32.65 | -5.29 | -39.46 | 485 |
| 44 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.14 | -4.01 | -32.87 | 373 |
| 45 | Z-score reversion · 1h | reversion | 75.40 | -24.60 | 179 | 37.4 | -19.90 | -2.82 | -27.66 | 228 |
| 46 | MACD zero-line · 1h | trend | 75.03 | -24.97 | 157 | 16.6 | -24.13 | -4.91 | -29.19 | 213 |
| 47 | Williams %R · 1h | reversion | 74.97 | -25.03 | 337 | 46.9 | -36.05 | -5.89 | -39.28 | 540 |
| 48 | EMA 20/50 cross · 1h | trend | 74.06 | -25.94 | 102 | 10.8 | -24.50 | -4.41 | -32.62 | 127 |
| 49 | Supertrend · 1h | trend | 73.72 | -26.29 | 167 | 13.2 | -28.79 | -4.96 | -34.92 | 226 |
| 50 | RSI momentum · 1h | momentum | 73.39 | -26.61 | 159 | 12.6 | -23.03 | -3.67 | -33.01 | 218 |
| 51 | Triple EMA stack · 1h | trend | 72.61 | -27.39 | 143 | 14.7 | -25.99 | -4.54 | -34.87 | 203 |
| 52 | ROC + volume · 1h | momentum | 72.41 | -27.59 | 349 | 25.5 | -35.67 | -6.65 | -38.89 | 384 |
| 53 | OBV trend · 1h | momentum | 71.93 | -28.07 | 274 | 18.2 | -26.69 | -4.94 | -34.09 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.69 | -29.31 | 142 | 19.7 | -29.59 | -5.47 | -35.64 | 207 |
| 55 | Daily: Momentum burst | daily | 70.19 | -29.81 | 26 | 11.5 | -39.48 | -5.71 | -39.66 | 31 |
| 56 | Max aggression: 1-day momentum | meta | 69.31 | -30.70 | 27 | 25.9 | -30.41 | -1.49 | -57.50 | 42 |
| 57 | RSI(14) reversion · 1h | reversion | 68.60 | -31.40 | 162 | 31.5 | -30.57 | -4.51 | -34.37 | 247 |
| 58 | Agent (ML meta-label) | meta | 68.11 | -31.89 | 1629 | 24.1 | -8.36 | -1.09 | -19.82 | 330 |
| 59 | VWAP momentum · 1h | momentum | 67.94 | -32.06 | 810 | 21.6 | -51.78 | -11.10 | -53.55 | 1236 |
| 60 | EMA 9/21 cross · 1h | trend | 65.94 | -34.06 | 247 | 9.7 | -37.97 | -7.53 | -40.15 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 64.87 | -35.13 | 434 | 28.6 | -37.79 | -6.90 | -38.45 | 592 |
| 62 | Three white soldiers | momentum | 62.31 | -37.69 | 494 | 15.2 | -48.60 | -22.79 | -48.60 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -45.84 | -98.97 | 5257 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.72 | -26.44 | -79.77 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.16 | -45.92 | -93.30 | 2520 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.01 | -32.16 | -89.09 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.60 | -39.90 | -90.72 | 2321 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.51 | -90.11 | 2193 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -54.42 | -97.65 | 3457 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -57.39 | -96.27 | 3419 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.65 | -32.31 | -93.71 | 2431 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.86 | -33.74 | -82.22 | 1674 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -56.04 | -99.53 | 5960 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.23 | -43.00 | -92.44 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.48 | -37.50 | -95.49 | 3404 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.20 | -99.79 | 6155 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.68 | -44.03 | -91.68 | 2257 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.16 | -24.75 | -75.70 | 1597 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -61.53 | -97.66 | 3520 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -63.62 | -98.84 | 4877 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.32 | -26.38 | -69.27 | 1219 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -55.06 | -94.51 | 2758 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -37.69 | -84.66 | 1784 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.38 | -99.65 | 6365 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.60 | -32.63 | -89.67 | 2271 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.42 | -20.18 | -78.44 | 1743 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.46 | -36.68 | -90.59 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.68 | -96.81 | 3876 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.34 | -58.80 | -89.34 | 2142 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.12 | -29.15 | -66.38 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -70.92 | -22.46 | -71.87 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.67 | -19.18 | -79.67 | 1680 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -49.86 | -97.32 | 4309 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.07 | -99.93 | 8312 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T20:35 | Agent (ML meta-label) | sell | BITX | 2.29 | -0.02 | selected signal exited |
| 2026-11-09T20:35 | Agent | sell | COIN | 17.29 | -0.13 | rebalance down |
| 2026-11-09T20:31 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 94.10 | — | entry |
| 2026-11-09T20:31 | CCI reversion · 1h | buy | XRP-USD | 6.35 | — | rebalance up |
| 2026-11-09T20:31 | CCI reversion · 1h | buy | NVDA | 9.92 | — | entry signal |
| 2026-11-09T20:31 | CCI reversion · 1h | buy | MSTR | 4.82 | — | rebalance up |
| 2026-11-09T20:31 | CCI reversion · 1h | buy | ETH-USD | 6.32 | — | rebalance up |
| 2026-11-09T20:31 | CCI reversion · 1h | buy | COIN | 5.81 | — | rebalance up |
| 2026-11-09T20:31 | CCI reversion · 1h | buy | BTC-USD | 6.12 | — | rebalance up |
| 2026-11-09T20:31 | CCI reversion · 1h | buy | BITX | 4.92 | — | rebalance up |
| 2026-11-09T20:31 | CCI reversion · 1h | sell | UPRO | 5.31 | 0.29 | exit signal |
| 2026-11-09T20:31 | CCI reversion · 1h | sell | TQQQ | 5.63 | 0.50 | exit signal |
| 2026-11-09T20:31 | CCI reversion · 1h | sell | TECL | 5.68 | 0.56 | exit signal |
| 2026-11-09T20:31 | CCI reversion · 1h | sell | SPY | 5.20 | 0.08 | exit signal |
| 2026-11-09T20:31 | CCI reversion · 1h | sell | SOXL | 6.46 | 1.33 | exit signal |
| 2026-11-09T20:31 | Z-score reversion · 1h | buy | XRP-USD | 4.21 | — | rebalance up |
| 2026-11-09T20:31 | Z-score reversion · 1h | buy | TSLA | 3.87 | — | rebalance up |
| 2026-11-09T20:31 | Z-score reversion · 1h | buy | SOL-USD | 4.19 | — | rebalance up |
| 2026-11-09T20:31 | Z-score reversion · 1h | buy | ETH-USD | 4.17 | — | rebalance up |
| 2026-11-09T20:31 | Z-score reversion · 1h | sell | UPRO | 6.34 | 0.15 | exit signal |
| 2026-11-09T20:31 | Z-score reversion · 1h | sell | SPY | 5.30 | 0.08 | exit signal |
| 2026-11-09T20:31 | Z-score reversion · 1h | sell | QQQ | 5.37 | 0.15 | exit signal |
| 2026-11-09T20:31 | RSI(14) reversion · 1h | buy | XRP-USD | 4.24 | — | rebalance up |
| 2026-11-09T20:31 | RSI(14) reversion · 1h | buy | BITX | 9.82 | — | entry signal |
| 2026-11-09T20:31 | RSI(14) reversion · 1h | sell | UPRO | 8.59 | 0.28 | exit signal |
| 2026-11-09T20:31 | RSI(14) reversion · 1h | sell | TQQQ | 8.63 | 0.48 | exit signal |
| 2026-11-09T20:31 | Volume breakout · 1h | buy | META | 20.37 | — | entry signal |
| 2026-11-09T20:31 | Donchian 55/20 · 1h | buy | META | 20.82 | — | entry signal |
| 2026-11-09T20:31 | Donchian 20/10 · 1h | buy | META | 17.68 | — | entry signal |
| 2026-11-09T20:31 | VWAP momentum · 1h | buy | TSLA | 2.82 | — | entry signal |
| 2026-11-09T20:31 | VWAP momentum · 1h | buy | NVDA | 3.24 | — | entry signal |
| 2026-11-09T20:31 | VWAP momentum · 1h | buy | MSTR | 3.24 | — | entry signal |
| 2026-11-09T20:31 | VWAP momentum · 1h | buy | ETHU | 3.24 | — | entry signal |
| 2026-11-09T20:31 | VWAP momentum · 1h | buy | BITX | 3.24 | — | entry signal |
| 2026-11-09T20:31 | Ichimoku · 1h | buy | TNA | 19.42 | — | entry signal |
| 2026-11-09T20:31 | Ichimoku · 1h | buy | LABU | 19.42 | — | entry signal |
| 2026-11-09T20:31 | Ichimoku · 1h | buy | IWM | 19.42 | — | entry signal |
| 2026-11-09T20:31 | Triple EMA stack · 1h | buy | META | 18.16 | — | entry signal |
| 2026-11-09T20:29 | Copy: Insider buying | buy | MDGL | 3.52 | — | entry |
| 2026-11-09T20:29 | Copy: Insider buying | buy | KOD | 11.45 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 20:35:05.000148+00:00 -> 2026-11-09 20:45:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 20:35:05.000148+00:00 -> 2026-11-09 20:45:05.000148+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 20:35:05.000148+00:00 -> 2026-11-09 20:45:05.000148+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
