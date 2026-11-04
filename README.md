# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T20:25:05.000117+00:00 · 47575 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.59 (-10.41%)

Closed trades 145, win rate 37.9%, fees £4.04, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 17.91 | -0.01 |

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

Today: 35307 decisions in 2691 calls, $0.4332 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T20:25 | 1 / 17 / 12 | LABU 15% |  |
| Breezy | 2026-11-04T20:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-04T20:25 | 5 / 22 / 3 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.78 | 12.78 | 0 | — | 14.00 | 5.00 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.24 | 6.24 | 17 | 70.6 | 6.76 | 2.13 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.57 | 1.57 | 0 | — | 5.45 | 1.54 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.12 | -13.53 | 140 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.55 | -0.45 | 5 | 40.0 | 4.89 | 1.16 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.19 | -1.81 | 0 | — | -0.50 | -0.20 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.03 | -9.61 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.13 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.36 | -3.64 | 112 | 34.8 | 6.20 | 2.89 | -3.27 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.70 | -4.64 | -6.25 | 20 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.34 | -4.66 | 0 | — | -1.97 | -0.70 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.95 | -5.33 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.38 | -5.62 | 0 | — | -4.91 | -1.87 | -6.35 | 1 |
| 17 | Hold BTC | benchmark | 94.25 | -5.75 | 0 | — | -2.21 | -0.06 | -13.22 | 1 |
| 18 | Agent (rotation) | meta | 93.84 | -6.17 | 164 | 27.4 | -7.49 | -6.45 | -8.24 | 182 |
| 19 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -0.89 | -0.23 | -8.76 | 218 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Max aggression: 5-day momentum | meta | 91.08 | -8.91 | 16 | 43.8 | -23.99 | -1.41 | -36.71 | 25 |
| 22 | Trend pullback · 1h | trend | 90.73 | -9.27 | 103 | 22.3 | -16.36 | -6.10 | -17.67 | 78 |
| 23 | Parabolic SAR · 1h | trend | 90.26 | -9.74 | 154 | 26.6 | -14.99 | -3.36 | -19.35 | 245 |
| 24 | Copy: Insider buying | copy | 89.65 | -10.35 | 38 | 39.5 | -21.60 | -4.39 | -23.32 | 63 |
| 25 | Agent | meta | 89.59 | -10.41 | 145 | 37.9 | -11.90 | -7.20 | -12.78 | 212 |
| 26 | Opening range 30m | breakout | 89.34 | -10.66 | 356 | 32.9 | -15.27 | -5.07 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.20 | -3.57 | -14.15 | 89 |
| 28 | Daily: Bullish score | daily | 87.01 | -12.99 | 14 | 21.4 | -8.63 | -1.32 | -16.58 | 14 |
| 29 | Donchian 55/20 · 1h | breakout | 86.83 | -13.17 | 62 | 12.9 | -13.49 | -2.89 | -19.91 | 106 |
| 30 | Stochastic reversion · 1h | reversion | 86.83 | -13.17 | 249 | 47.8 | -20.47 | -3.90 | -24.97 | 383 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.94 | -14.06 | 1 | 0.0 | -7.13 | -1.05 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.49 | -14.51 | 70 | 31.4 | -12.32 | -4.10 | -14.77 | 97 |
| 33 | ADX DI cross · 1h | trend | 85.16 | -14.84 | 155 | 18.1 | -17.82 | -3.20 | -22.68 | 276 |
| 34 | Volume breakout · 1h | breakout | 84.82 | -15.18 | 132 | 28.8 | -13.89 | -3.19 | -18.08 | 103 |
| 35 | MFI reversion · 1h | reversion | 84.21 | -15.79 | 324 | 34.3 | -12.98 | -1.92 | -18.47 | 153 |
| 36 | Keltner breakout · 1h | breakout | 83.95 | -16.05 | 94 | 24.5 | -19.75 | -4.07 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.43 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.66 | -17.34 | 434 | 30.2 | -19.53 | -5.98 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 81.97 | -18.03 | 85 | 12.9 | -20.27 | -4.34 | -26.10 | 128 |
| 40 | Bollinger breakout · 1h | breakout | 81.52 | -18.48 | 148 | 25.0 | -18.02 | -3.69 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.91 | -19.09 | 278 | 46.4 | -22.08 | -3.20 | -27.71 | 450 |
| 42 | EMA 20/50 cross · 1h | trend | 79.31 | -20.69 | 92 | 10.9 | -19.03 | -3.38 | -27.87 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 79.06 | -20.94 | 372 | 22.6 | -40.35 | -8.44 | -43.89 | 676 |
| 44 | MACD zero-line · 1h | trend | 78.49 | -21.51 | 141 | 15.6 | -24.82 | -5.15 | -29.62 | 222 |
| 45 | MACD cross · 1h | trend | 78.19 | -21.81 | 310 | 22.9 | -30.48 | -5.98 | -33.62 | 473 |
| 46 | Z-score reversion · 1h | reversion | 78.16 | -21.84 | 152 | 37.5 | -15.46 | -2.28 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 78.01 | -22.00 | 147 | 12.9 | -29.32 | -5.33 | -32.06 | 232 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.29 | -33.57 | 33 |
| 49 | Williams %R · 1h | reversion | 76.78 | -23.22 | 290 | 47.6 | -33.16 | -6.01 | -34.64 | 525 |
| 50 | RSI momentum · 1h | momentum | 76.65 | -23.36 | 142 | 12.0 | -28.28 | -5.47 | -30.53 | 227 |
| 51 | Bollinger reversion · 1h | reversion | 76.47 | -23.53 | 233 | 40.3 | -28.69 | -5.69 | -30.69 | 369 |
| 52 | Triple EMA stack · 1h | trend | 75.96 | -24.04 | 131 | 13.7 | -27.53 | -5.48 | -31.75 | 210 |
| 53 | OBV trend · 1h | momentum | 75.36 | -24.64 | 248 | 17.3 | -29.26 | -6.40 | -30.85 | 291 |
| 54 | Donchian 20/10 · 1h | breakout | 74.54 | -25.46 | 124 | 19.4 | -27.60 | -5.06 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.25 | -25.75 | 321 | 25.5 | -33.51 | -6.57 | -36.19 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.00 | -28.00 | 136 | 28.7 | -20.20 | -3.36 | -26.28 | 218 |
| 57 | EMA 9/21 cross · 1h | trend | 69.69 | -30.31 | 225 | 9.8 | -36.67 | -7.44 | -40.09 | 341 |
| 58 | Agent (ML meta-label) | meta | 69.62 | -30.38 | 1440 | 22.4 | -8.07 | -1.44 | -19.94 | 296 |
| 59 | VWAP momentum · 1h | momentum | 69.60 | -30.40 | 727 | 22.3 | -53.22 | -11.01 | -55.70 | 1213 |
| 60 | Candlestick reversal · 1h | reversion | 69.44 | -30.56 | 376 | 30.1 | -35.15 | -6.57 | -37.87 | 554 |
| 61 | Three white soldiers | momentum | 68.34 | -31.66 | 436 | 16.5 | -46.79 | -21.97 | -47.18 | 631 |
| 62 | Max aggression: 1-day momentum | meta | 66.31 | -33.69 | 24 | 29.2 | -36.25 | -2.19 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -46.12 | -98.97 | 5157 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.11 | -25.41 | -80.23 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -47.23 | -93.42 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.91 | -31.31 | -89.10 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.92 | -38.27 | -91.06 | 2309 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.15 | -32.11 | -90.16 | 2207 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.68 | -53.31 | -97.71 | 3450 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -58.68 | -96.15 | 3350 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -34.46 | -93.59 | 2452 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.16 | -37.57 | -82.16 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -56.70 | -99.48 | 5875 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.89 | -42.94 | -92.99 | 2599 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.59 | -38.12 | -95.60 | 3407 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.04 | -99.79 | 6163 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -42.53 | -91.82 | 2255 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.41 | -26.75 | -74.43 | 1546 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -63.19 | -97.74 | 3522 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -64.19 | -98.70 | 4833 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.50 | -28.26 | -70.50 | 1196 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -54.43 | -94.79 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -37.09 | -84.66 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -75.00 | -99.62 | 6311 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -31.08 | -88.44 | 2242 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.47 | -19.24 | -76.92 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.37 | -36.72 | -90.39 | 2218 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.44 | -52.22 | -96.50 | 3837 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.14 | -53.45 | -89.25 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.28 | -28.00 | -65.56 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.54 | -25.23 | -73.79 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.73 | -18.72 | -77.54 | 1607 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.94 | -53.77 | -96.95 | 4255 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -115.18 | -99.93 | 8215 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T20:25 | Agent (ML meta-label) | sell | ETH-USD | 4.62 | -0.02 | selected signal exited |
| 2026-11-04T20:25 | MFI reversion · 1h | buy | NVDA | 4.23 | — | rebalance up |
| 2026-11-04T20:20 | Agent (ML meta-label) | buy | ETH-USD | 4.64 | — | entry |
| 2026-11-04T20:20 | Agent (ML meta-label) | sell | IWM | 5.36 | 0.00 | selected signal exited |
| 2026-11-04T20:10 | Agent (ML meta-label) | buy | SPY | 5.30 | — | entry |
| 2026-11-04T20:10 | Agent (ML meta-label) | buy | IWM | 5.36 | — | entry |
| 2026-11-04T20:10 | Agent (ML meta-label) | sell | XRP-USD | 5.32 | -0.02 | selected signal exited |
| 2026-11-04T20:10 | Agent (ML meta-label) | sell | ETH-USD | 5.33 | -0.02 | selected signal exited |
| 2026-11-04T20:10 | Agent (aggressive) | buy | BITX | 42.75 | — | following Z-score reversion |
| 2026-11-04T20:10 | Agent | buy | BITX | 17.92 | — | following Z-score reversion |
| 2026-11-04T20:05 | Agent (ML meta-label) | buy | XRP-USD | 5.34 | — | entry |
| 2026-11-04T20:05 | Agent (ML meta-label) | buy | UPRO | 5.35 | — | entry |
| 2026-11-04T20:05 | Agent (ML meta-label) | buy | TQQQ | 5.35 | — | entry |
| 2026-11-04T20:05 | Agent (ML meta-label) | buy | ETH-USD | 5.35 | — | entry |
| 2026-11-04T20:05 | Agent (ML meta-label) | buy | COIN | 5.35 | — | entry |
| 2026-11-04T20:05 | Agent (ML meta-label) | buy | BITX | 5.35 | — | following Z-score reversion |
| 2026-11-04T20:05 | Agent (ML meta-label) | sell | SQQQ | 4.55 | 0.02 | rebalance down |
| 2026-11-04T20:05 | Agent (ML meta-label) | sell | MSTR | 4.59 | -0.03 | rebalance down |
| 2026-11-04T20:05 | Agent (ML meta-label) | sell | MSFT | 4.60 | 0.02 | rebalance down |
| 2026-11-04T20:05 | Agent (ML meta-label) | sell | GOOGL | 4.59 | 0.00 | rebalance down |
| 2026-11-04T20:05 | Agent (ML meta-label) | sell | ETHU | 4.59 | -0.03 | rebalance down |
| 2026-11-04T20:05 | Agent (ML meta-label) | sell | AMZN | 4.58 | -0.01 | rebalance down |
| 2026-11-04T20:05 | Agent (ML meta-label) | sell | AAPL | 4.59 | -0.01 | rebalance down |
| 2026-11-04T20:00 | Day trade: Stocks in Play ORB | buy | GOOGL | 24.09 | — | entry |
| 2026-11-04T20:00 | Agent (ML meta-label) | buy | SQQQ | 3.55 | — | rebalance up |
| 2026-11-04T20:00 | Agent (ML meta-label) | buy | MSTR | 3.64 | — | rebalance up |
| 2026-11-04T20:00 | Agent (ML meta-label) | buy | MSFT | 3.54 | — | rebalance up |
| 2026-11-04T20:00 | Agent (ML meta-label) | buy | GOOGL | 9.94 | — | entry |
| 2026-11-04T20:00 | Agent (ML meta-label) | buy | ETHU | 3.66 | — | rebalance up |
| 2026-11-04T20:00 | Agent (ML meta-label) | buy | AMZN | 3.59 | — | rebalance up |
| 2026-11-04T20:00 | Agent (ML meta-label) | buy | AAPL | 3.60 | — | rebalance up |
| 2026-11-04T20:00 | Agent (ML meta-label) | sell | SOL-USD | 6.29 | -0.11 | selected signal exited |
| 2026-11-04T20:00 | Agent (ML meta-label) | sell | BITX | 6.33 | -0.05 | selected signal exited |
| 2026-11-04T20:00 | Agent (aggressive) | sell | BITX | 42.59 | -0.32 | selected signal exited |
| 2026-11-04T20:00 | Agent | sell | BITX | 17.81 | -0.13 | selected signal exited |
| 2026-11-04T20:00 | MFI reversion · 1h | buy | SPY | 20.96 | — | entry |
| 2026-11-04T20:00 | MFI reversion · 1h | sell | SOXL | 20.87 | -0.44 | target is flat |
| 2026-11-04T20:00 | MFI reversion · 1h | sell | AMZN | 21.08 | -0.10 | target is flat |
| 2026-11-04T20:00 | Volume breakout · 1h | buy | BTC-USD | 7.69 | — | entry |
| 2026-11-04T20:00 | Volume breakout · 1h | sell | XRP-USD | 6.99 | -0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 20:25:05.000117+00:00 -> 2026-11-04 20:35:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 20:25:05.000117+00:00 -> 2026-11-04 20:35:05.000117+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 20:25:05.000117+00:00 -> 2026-11-04 20:35:05.000117+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
