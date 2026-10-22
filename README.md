# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T18:45:05.000147+00:00 · 32149 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.09 (-9.91%)

Closed trades 97, win rate 39.2%, fees £3.13, max drawdown -10.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.02 | +0.06 |

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

Today: 32631 decisions in 2751 calls, $0.4051 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T18:45 | 10 / 15 / 5 | COIN 15% |  |
| Breezy | 2026-10-22T18:45 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-22T18:45 | 10 / 18 / 2 | COIN 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.62 | 7.62 | 0 | — | 10.59 | 4.70 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.16 | 6.16 | 12 | 66.7 | 3.31 | 1.03 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.16 | 5.16 | 15 | 46.7 | 7.88 | 2.38 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.74 | 0.74 | 78 | 46.2 | -9.82 | -2.64 | -13.79 | 135 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.10 | 0.10 | 0 | — | 3.85 | 1.69 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 11 | Hold SPY | benchmark | 97.91 | -2.10 | 0 | — | -0.63 | -0.30 | -3.13 | 1 |
| 12 | Max aggression: 5-day momentum | meta | 97.44 | -2.56 | 10 | 50.0 | -17.69 | -1.41 | -34.64 | 26 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.38 | -1.93 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.40 | -3.60 | 117 | 30.8 | -8.19 | -4.67 | -9.03 | 258 |
| 15 | Hold BTC | benchmark | 95.89 | -4.11 | 0 | — | 4.91 | 0.90 | -8.68 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.28 | 0.75 | -7.93 | 8 |
| 17 | Copy: Congress Democrats (NANC) | copy | 95.58 | -4.42 | 0 | — | -0.87 | -0.28 | -5.45 | 1 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.88 | -5.12 | 0 | — | -5.22 | -1.90 | -7.17 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.41 | 2.00 | -7.38 | 198 |
| 21 | Copy: Insider buying | copy | 94.08 | -5.92 | 25 | 40.0 | -13.59 | -2.33 | -20.62 | 72 |
| 22 | Opening range 30m | breakout | 93.80 | -6.20 | 237 | 35.0 | -9.89 | -2.79 | -17.26 | 558 |
| 23 | Trend pullback · 1h | trend | 93.58 | -6.42 | 95 | 23.2 | -23.43 | -7.30 | -23.60 | 125 |
| 24 | Donchian 55/20 · 1h | breakout | 93.08 | -6.92 | 48 | 16.7 | -18.47 | -3.74 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.51 | -7.49 | 115 | 26.1 | -17.25 | -3.81 | -20.59 | 265 |
| 26 | ADX DI cross · 1h | trend | 92.19 | -7.80 | 103 | 19.4 | -9.83 | -1.87 | -12.90 | 250 |
| 27 | Daily: Momentum burst | daily | 91.80 | -8.20 | 8 | 12.5 | -16.87 | -2.96 | -20.58 | 39 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.17 | -0.94 | -11.76 | 99 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.92 | -2.08 | -16.91 | 1 |
| 30 | Agent | meta | 90.09 | -9.91 | 97 | 39.2 | -14.71 | -6.49 | -18.46 | 282 |
| 31 | Daily: Bullish score | daily | 89.76 | -10.24 | 8 | 0.0 | -6.86 | -0.78 | -13.31 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.47 | -10.53 | 104 | 27.9 | -11.44 | -2.03 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.16 | -10.84 | 101 | 22.8 | -10.93 | -1.93 | -12.44 | 105 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.45 | -11.55 | 0 | — | -5.56 | -0.70 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.72 | -12.28 | 46 | 34.8 | -18.33 | -4.45 | -26.82 | 138 |
| 36 | EMA 20/50 cross · 1h | trend | 87.35 | -12.65 | 68 | 11.8 | -23.38 | -4.24 | -25.26 | 142 |
| 37 | Stochastic reversion · 1h | reversion | 87.16 | -12.84 | 178 | 45.5 | -16.26 | -2.66 | -22.24 | 384 |
| 38 | Supertrend · 1h | trend | 86.79 | -13.21 | 104 | 15.4 | -24.36 | -4.72 | -27.31 | 219 |
| 39 | Opening range 15m | breakout | 86.49 | -13.51 | 301 | 30.2 | -16.38 | -4.40 | -18.65 | 702 |
| 40 | RSI momentum · 1h | momentum | 86.49 | -13.51 | 96 | 16.7 | -20.71 | -3.99 | -22.53 | 218 |
| 41 | Keltner breakout · 1h | breakout | 86.25 | -13.75 | 73 | 23.3 | -23.15 | -4.48 | -24.09 | 200 |
| 42 | Connors RSI(2) · 1h | reversion | 85.15 | -14.85 | 168 | 39.9 | -26.11 | -7.11 | -26.12 | 204 |
| 43 | MACD cross · 1h | trend | 84.78 | -15.22 | 215 | 23.3 | -28.11 | -5.07 | -29.52 | 466 |
| 44 | Triple EMA stack · 1h | trend | 84.12 | -15.88 | 96 | 15.6 | -29.17 | -5.47 | -29.84 | 222 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.72 | -23.02 | 116 |
| 46 | Z-score reversion · 1h | reversion | 83.33 | -16.67 | 104 | 33.7 | -13.64 | -2.00 | -21.32 | 196 |
| 47 | Donchian 20/10 · 1h | breakout | 82.82 | -17.18 | 93 | 20.4 | -24.64 | -4.46 | -25.38 | 226 |
| 48 | MFI reversion · 1h | reversion | 82.37 | -17.63 | 240 | 32.1 | -18.63 | -2.85 | -21.11 | 147 |
| 49 | MACD zero-line · 1h | trend | 82.17 | -17.83 | 102 | 15.7 | -25.49 | -4.82 | -26.63 | 226 |
| 50 | Three white soldiers | momentum | 82.16 | -17.84 | 263 | 20.2 | -44.88 | -17.94 | -45.15 | 597 |
| 51 | OBV trend · 1h | momentum | 81.88 | -18.12 | 198 | 17.7 | -32.67 | -6.19 | -33.09 | 306 |
| 52 | Williams %R · 1h | reversion | 81.75 | -18.25 | 204 | 44.1 | -33.61 | -5.33 | -37.96 | 523 |
| 53 | CCI reversion · 1h | reversion | 80.42 | -19.57 | 193 | 43.0 | -22.75 | -3.03 | -27.44 | 443 |
| 54 | Agent (ML meta-label) | meta | 80.15 | -19.85 | 808 | 19.1 | -16.27 | -2.87 | -18.44 | 379 |
| 55 | Bollinger reversion · 1h | reversion | 80.04 | -19.96 | 168 | 35.1 | -31.20 | -5.98 | -32.69 | 362 |
| 56 | Heikin-Ashi · 1h | trend | 79.87 | -20.13 | 260 | 23.5 | -43.46 | -9.27 | -44.22 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.45 | -20.55 | 231 | 24.2 | -28.91 | -5.20 | -29.17 | 378 |
| 58 | RSI(14) reversion · 1h | reversion | 77.85 | -22.15 | 90 | 23.3 | -20.58 | -3.86 | -23.32 | 180 |
| 59 | EMA 9/21 cross · 1h | trend | 77.79 | -22.21 | 155 | 11.6 | -32.15 | -6.07 | -32.94 | 330 |
| 60 | Candlestick reversal · 1h | reversion | 77.34 | -22.66 | 240 | 29.6 | -38.27 | -6.61 | -39.94 | 565 |
| 61 | VWAP momentum · 1h | momentum | 76.60 | -23.40 | 499 | 21.4 | -50.48 | -10.23 | -51.20 | 1232 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.54 | -2.82 | -48.38 | 43 |
| 63 | ROC + volume | momentum | 59.12 | -40.88 | 689 | 23.2 | -78.05 | -20.94 | -79.54 | 1674 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.30 | -19.27 | -65.26 | 855 |
| 65 | Donchian 55/20 | breakout | 56.28 | -43.72 | 538 | 19.7 | -72.88 | -20.29 | -74.13 | 1267 |
| 66 | Squeeze breakout | breakout | 55.23 | -44.77 | 529 | 14.0 | -67.26 | -22.84 | -68.30 | 1197 |
| 67 | EMA 20/50 cross | trend | 54.15 | -45.85 | 584 | 20.2 | -79.66 | -20.78 | -79.69 | 1436 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.31 | -16.76 | -76.70 | 1674 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -73.31 | -14.47 | -73.49 | 1518 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.81 | -31.01 | -98.89 | 5261 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.22 | -34.77 | -94.42 | 2564 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.37 | -24.53 | -89.09 | 1890 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.58 | -29.17 | -92.02 | 2344 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.97 | -24.94 | -91.04 | 2212 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.81 | -35.16 | -97.94 | 3486 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.97 | -37.95 | -97.09 | 3545 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -28.00 | -94.46 | 2550 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.16 | -28.01 | -83.57 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -36.32 | -99.49 | 5871 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.38 | -29.50 | -93.00 | 2612 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.65 | -30.24 | -95.68 | 3429 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -42.47 | -99.79 | 6177 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.18 | -31.95 | -92.18 | 2322 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -39.01 | -97.76 | 3585 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -37.72 | -98.65 | 4763 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.30 | -34.38 | -94.67 | 2781 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.16 | -27.23 | -84.39 | 1782 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -39.75 | -99.59 | 6223 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.00 | -23.58 | -88.07 | 2190 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.65 | -26.52 | -88.76 | 2194 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.23 | -33.70 | -96.27 | 3806 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.60 | -34.02 | -89.85 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -34.28 | -96.22 | 4137 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -44.76 | -99.91 | 8235 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T18:45 | Agent | sell | BITX | 18.00 | -0.04 | selected signal exited |
| 2026-10-22T18:45 | Three white soldiers | buy | COIN | 20.54 | — | entry signal |
| 2026-10-22T18:40 | Agent (ML meta-label) | buy | AMZN | 2.02 | — | entry |
| 2026-10-22T18:35 | Agent (ML meta-label) | buy | TQQQ | 5.00 | — | entry |
| 2026-10-22T18:35 | Agent (ML meta-label) | buy | QQQ | 5.00 | — | entry |
| 2026-10-22T18:35 | Agent (ML meta-label) | buy | GOOGL | 5.00 | — | entry |
| 2026-10-22T18:35 | Agent (ML meta-label) | sell | MSFT | 4.99 | -0.01 | selected signal exited |
| 2026-10-22T18:35 | Agent (ML meta-label) | sell | META | 5.00 | -0.01 | selected signal exited |
| 2026-10-22T18:35 | Agent (ML meta-label) | sell | AMZN | 5.31 | -0.05 | selected signal exited |
| 2026-10-22T18:35 | Squeeze breakout | sell | AAPL | 13.77 | -0.05 | exit signal |
| 2026-10-22T18:31 | Agent (ML meta-label) | buy | SOXL | 5.01 | — | entry |
| 2026-10-22T18:31 | Agent (ML meta-label) | buy | MSFT | 5.01 | — | entry |
| 2026-10-22T18:31 | Agent (ML meta-label) | buy | META | 5.01 | — | entry |
| 2026-10-22T18:31 | Agent (ML meta-label) | sell | TSLA | 5.64 | -0.03 | selected signal exited |
| 2026-10-22T18:31 | Agent (ML meta-label) | sell | ETH-USD | 4.69 | -0.04 | selected signal exited |
| 2026-10-22T18:31 | Bollinger reversion · 1h | buy | SOXL | 7.27 | — | entry signal |
| 2026-10-22T18:31 | Bollinger reversion · 1h | buy | META | 7.27 | — | entry signal |
| 2026-10-22T18:31 | Bollinger reversion · 1h | buy | AMD | 7.27 | — | entry signal |
| 2026-10-22T18:31 | Donchian 20/10 · 1h | sell | MSTR | 20.34 | -0.60 | exit signal |
| 2026-10-22T18:31 | RSI momentum · 1h | buy | AAPL | 5.27 | — | rebalance up |
| 2026-10-22T18:31 | RSI momentum · 1h | sell | MSTR | 10.67 | -0.51 | exit signal |
| 2026-10-22T18:31 | VWAP momentum · 1h | buy | TNA | 18.85 | — | entry signal |
| 2026-10-22T18:31 | VWAP momentum · 1h | buy | IWM | 19.17 | — | entry signal |
| 2026-10-22T18:31 | Trend pullback · 1h | sell | PLTR | 23.18 | -0.37 | exit signal |
| 2026-10-22T18:25 | Agent (ML meta-label) | buy | TSLA | 5.67 | — | following Opening range 30m |
| 2026-10-22T18:25 | Agent (ML meta-label) | sell | TQQQ | 5.35 | -0.01 | selected signal exited |
| 2026-10-22T18:25 | Agent (ML meta-label) | sell | MSFT | 2.52 | -0.00 | selected signal exited |
| 2026-10-22T18:25 | Agent (ML meta-label) | sell | GOOGL | 4.22 | -0.01 | selected signal exited |
| 2026-10-22T18:20 | Agent (ML meta-label) | buy | MSFT | 2.52 | — | entry |
| 2026-10-22T18:20 | Agent (ML meta-label) | buy | GOOGL | 4.23 | — | entry |
| 2026-10-22T18:20 | MFI reversion · 1h | buy | SOL-USD | 6.85 | — | rebalance up |
| 2026-10-22T18:20 | MFI reversion · 1h | buy | QQQ | 6.86 | — | rebalance up |
| 2026-10-22T18:20 | MFI reversion · 1h | buy | GOOGL | 20.64 | — | entry |
| 2026-10-22T18:20 | MFI reversion · 1h | buy | AMZN | 10.27 | — | rebalance up |
| 2026-10-22T18:20 | MFI reversion · 1h | sell | TECL | 13.84 | 0.07 | target is flat |
| 2026-10-22T18:20 | MFI reversion · 1h | sell | SOXL | 11.75 | -0.07 | target is flat |
| 2026-10-22T18:20 | MFI reversion · 1h | sell | AMD | 13.83 | -0.04 | target is flat |
| 2026-10-22T18:20 | Squeeze breakout | buy | AAPL | 13.82 | — | entry signal |
| 2026-10-22T18:15 | Agent (ML meta-label) | buy | MSTR | 5.34 | — | entry |
| 2026-10-22T18:15 | Agent (ML meta-label) | sell | QQQ | 3.25 | -0.01 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 18:45:05.000147+00:00 -> 2026-10-22 18:55:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
