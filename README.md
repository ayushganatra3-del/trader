# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T17:36:05.000135+00:00 · 38105 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.07 (-9.93%)

Closed trades 113, win rate 38.9%, fees £3.45, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.10 | +0.11 |

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

Today: 27268 decisions in 2588 calls, $0.3413 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T17:36 | 1 / 20 / 8 | cash |  |
| Breezy | 2026-10-27T17:36 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-10-27T17:36 | 4 / 24 / 1 | BITX 69% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.55 | 7.55 | 0 | — | 8.08 | 4.02 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.52 | 6.52 | 14 | 71.4 | 3.83 | 1.26 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.27 | 5.27 | 19 | 47.4 | 7.98 | 2.57 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.74 | 0.74 | 0 | — | 2.26 | 1.08 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.55 | -0.45 | 0 | — | 0.47 | 0.32 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.01 | -0.99 | 82 | 35.4 | 7.13 | 3.40 | -1.80 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.79 | -2.21 | 0 | — | 0.73 | 0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.17 | -2.01 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.27 | -3.73 | 122 | 31.1 | -2.35 | -1.33 | -6.39 | 180 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.01 | -3.99 | 0 | — | -5.80 | -2.36 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 95.88 | -4.12 | 0 | — | 2.61 | 0.60 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.40 | 1.05 | -7.93 | 8 |
| 18 | Gap and go | momentum | 95.62 | -4.38 | 114 | 27.2 | 5.98 | 1.91 | -8.76 | 210 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 20 | Opening range 30m | breakout | 93.75 | -6.25 | 272 | 34.2 | -9.54 | -2.82 | -17.21 | 593 |
| 21 | Donchian 55/20 · 1h | breakout | 93.59 | -6.41 | 49 | 16.3 | -13.01 | -2.93 | -15.45 | 97 |
| 22 | Trend pullback · 1h | trend | 93.48 | -6.52 | 96 | 22.9 | -21.95 | -7.01 | -22.19 | 116 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.76 | -7.24 | 0 | — | -1.24 | -0.03 | -14.57 | 1 |
| 24 | Copy: Insider buying | copy | 92.44 | -7.56 | 27 | 37.0 | -19.46 | -3.79 | -22.94 | 63 |
| 25 | Parabolic SAR · 1h | trend | 92.19 | -7.81 | 121 | 25.6 | -20.33 | -5.00 | -23.02 | 247 |
| 26 | Daily: Momentum burst | daily | 91.91 | -8.10 | 13 | 15.4 | -18.12 | -3.50 | -19.44 | 39 |
| 27 | ADX DI cross · 1h | trend | 91.78 | -8.21 | 120 | 18.3 | -13.94 | -3.02 | -15.77 | 270 |
| 28 | Daily: Bullish score | daily | 91.37 | -8.63 | 11 | 18.2 | -6.42 | -0.76 | -14.40 | 14 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.29 | -2.18 | -16.91 | 1 |
| 30 | Max aggression: 5-day momentum | meta | 91.05 | -8.95 | 12 | 41.7 | -14.46 | -1.29 | -27.23 | 25 |
| 31 | Squeeze breakout · 1h | breakout | 91.00 | -9.00 | 52 | 23.1 | -4.49 | -1.17 | -12.07 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.20 | -9.80 | 108 | 25.9 | -12.16 | -2.51 | -15.94 | 112 |
| 33 | Agent | meta | 90.07 | -9.93 | 113 | 38.9 | -11.27 | -7.07 | -12.47 | 221 |
| 34 | Bollinger breakout · 1h | breakout | 88.86 | -11.14 | 109 | 26.6 | -12.77 | -2.51 | -18.15 | 249 |
| 35 | Agent (aggressive) | meta | 88.25 | -11.75 | 56 | 35.7 | -10.51 | -3.44 | -14.77 | 96 |
| 36 | Stochastic reversion · 1h | reversion | 87.85 | -12.15 | 205 | 47.3 | -21.07 | -3.92 | -22.35 | 389 |
| 37 | Opening range 15m | breakout | 87.21 | -12.79 | 338 | 30.8 | -13.32 | -3.68 | -17.87 | 719 |
| 38 | Keltner breakout · 1h | breakout | 87.17 | -12.84 | 74 | 23.0 | -19.62 | -3.79 | -23.13 | 188 |
| 39 | Z-score reversion · 1h | reversion | 86.95 | -13.05 | 125 | 36.0 | -12.46 | -1.96 | -21.48 | 211 |
| 40 | Supertrend · 1h | trend | 85.74 | -14.26 | 114 | 14.0 | -25.48 | -5.15 | -28.23 | 230 |
| 41 | Connors RSI(2) · 1h | reversion | 85.15 | -14.85 | 176 | 40.9 | -24.37 | -7.42 | -24.94 | 197 |
| 42 | RSI momentum · 1h | momentum | 85.03 | -14.97 | 104 | 15.4 | -21.23 | -4.29 | -24.15 | 212 |
| 43 | MACD cross · 1h | trend | 84.36 | -15.63 | 244 | 22.1 | -26.61 | -4.99 | -28.72 | 473 |
| 44 | EMA 20/50 cross · 1h | trend | 84.25 | -15.75 | 73 | 11.0 | -22.97 | -4.67 | -24.49 | 133 |
| 45 | Ichimoku · 1h | trend | 83.91 | -16.09 | 68 | 11.8 | -19.98 | -4.07 | -24.73 | 111 |
| 46 | MFI reversion · 1h | reversion | 83.51 | -16.49 | 272 | 32.4 | -16.13 | -2.49 | -20.70 | 153 |
| 47 | Triple EMA stack · 1h | trend | 83.44 | -16.56 | 101 | 14.9 | -28.15 | -5.37 | -31.09 | 202 |
| 48 | CCI reversion · 1h | reversion | 82.56 | -17.44 | 230 | 45.2 | -23.26 | -3.29 | -28.08 | 465 |
| 49 | Williams %R · 1h | reversion | 82.12 | -17.88 | 232 | 47.0 | -35.04 | -5.92 | -36.10 | 536 |
| 50 | Donchian 20/10 · 1h | breakout | 81.92 | -18.08 | 99 | 20.2 | -24.22 | -4.62 | -26.91 | 222 |
| 51 | MACD zero-line · 1h | trend | 81.33 | -18.67 | 111 | 15.3 | -23.12 | -4.84 | -24.78 | 228 |
| 52 | Bollinger reversion · 1h | reversion | 80.81 | -19.19 | 182 | 37.4 | -29.08 | -5.94 | -30.19 | 364 |
| 53 | Agent (ML meta-label) | meta | 80.76 | -19.24 | 972 | 20.6 | -10.45 | -1.87 | -19.46 | 341 |
| 54 | RSI(14) reversion · 1h | reversion | 80.42 | -19.58 | 107 | 27.1 | -19.65 | -3.75 | -24.95 | 184 |
| 55 | OBV trend · 1h | momentum | 80.33 | -19.67 | 209 | 17.7 | -30.78 | -6.53 | -32.76 | 295 |
| 56 | ROC + volume · 1h | momentum | 79.16 | -20.84 | 259 | 25.9 | -31.12 | -6.04 | -33.31 | 385 |
| 57 | Heikin-Ashi · 1h | trend | 78.37 | -21.63 | 295 | 22.7 | -43.22 | -9.49 | -44.60 | 671 |
| 58 | Candlestick reversal · 1h | reversion | 77.44 | -22.56 | 284 | 29.6 | -33.90 | -6.54 | -34.84 | 551 |
| 59 | Three white soldiers | momentum | 77.35 | -22.65 | 321 | 19.0 | -44.56 | -20.14 | -45.09 | 606 |
| 60 | VWAP momentum · 1h | momentum | 76.96 | -23.04 | 570 | 22.3 | -49.07 | -10.59 | -51.33 | 1240 |
| 61 | EMA 9/21 cross · 1h | trend | 76.64 | -23.36 | 176 | 10.8 | -30.77 | -6.60 | -32.65 | 338 |
| 62 | Max aggression: 1-day momentum | meta | 72.08 | -27.92 | 20 | 30.0 | -38.01 | -2.47 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.07 | -45.93 | 804 | 22.4 | -74.41 | -26.06 | -75.05 | 1577 |
| 64 | Volume breakout | breakout | 52.60 | -47.40 | 482 | 12.9 | -62.91 | -25.38 | -63.54 | 807 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -42.23 | -98.87 | 5142 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.18 | -23.17 | -80.01 | 1414 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.63 | -42.54 | -93.80 | 2533 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.09 | -29.68 | -89.33 | 1925 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -37.15 | -91.59 | 2345 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.33 | -31.78 | -90.41 | 2180 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -48.76 | -97.89 | 3505 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -52.39 | -96.21 | 3383 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.08 | -35.97 | -94.09 | 2451 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.24 | -32.42 | -82.64 | 1686 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.19 | -99.42 | 5771 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.69 | -40.97 | -92.92 | 2629 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.42 | -38.42 | -95.42 | 3373 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -69.32 | -99.78 | 6166 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.25 | -43.59 | -92.37 | 2323 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -60.60 | -97.78 | 3591 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.93 | -98.67 | 4796 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.70 | -27.99 | -68.62 | 1179 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -54.47 | -94.63 | 2771 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.27 | -38.17 | -84.51 | 1824 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.09 | -99.61 | 6298 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -28.64 | -88.27 | 2225 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.95 | -19.23 | -77.16 | 1687 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.62 | -36.57 | -90.72 | 2276 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -46.92 | -96.28 | 3822 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.98 | -47.77 | -90.03 | 2127 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.95 | -24.52 | -73.50 | 1290 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.21 | -17.94 | -76.40 | 1584 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.27 | -96.55 | 4194 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.55 | -99.92 | 8305 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T17:35 | Agent (ML meta-label) | buy | UPRO | 16.05 | — | entry |
| 2026-10-27T17:35 | Agent (ML meta-label) | buy | PLTR | 16.16 | — | following VWAP momentum |
| 2026-10-27T17:35 | Agent (ML meta-label) | buy | NVDA | 16.16 | — | entry |
| 2026-10-27T17:35 | Agent (ML meta-label) | sell | SOXL | 4.08 | 0.08 | rebalance down |
| 2026-10-27T17:35 | Agent (ML meta-label) | sell | IWM | 20.18 | -0.01 | selected signal exited |
| 2026-10-27T17:35 | Volume breakout | sell | DOGE-USD | 13.06 | -0.12 | exit signal |
| 2026-10-27T17:30 | Agent (ML meta-label) | buy | SOXL | 4.05 | — | rebalance up |
| 2026-10-27T17:30 | Agent (ML meta-label) | buy | IWM | 8.08 | — | rebalance up |
| 2026-10-27T17:30 | Agent (ML meta-label) | sell | NVDA | 20.11 | -0.07 | selected signal exited |
| 2026-10-27T17:30 | Agent (ML meta-label) | sell | AMD | 16.13 | -0.03 | selected signal exited |
| 2026-10-27T17:30 | Stochastic reversion · 1h | buy | SQQQ | 21.98 | — | entry signal |
| 2026-10-27T17:30 | Bollinger reversion · 1h | buy | SQQQ | 20.22 | — | entry signal |
| 2026-10-27T17:30 | Candlestick reversal · 1h | buy | COIN | 12.91 | — | entry signal |
| 2026-10-27T17:30 | Candlestick reversal · 1h | sell | NVDA | 6.83 | -0.02 | exit signal |
| 2026-10-27T17:30 | Candlestick reversal · 1h | sell | MSFT | 11.01 | 0.00 | exit signal |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | SOL-USD | 3.20 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | PLTR | 3.35 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | MSTR | 3.35 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | MSFT | 3.35 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | sell | NVDA | 4.75 | 0.04 | exit signal |
| 2026-10-27T17:30 | VWAP momentum · 1h | sell | AMZN | 4.26 | 0.04 | target is flat |
| 2026-10-27T17:30 | VWAP momentum · 1h | sell | AAPL | 4.22 | 0.01 | exit signal |
| 2026-10-27T17:30 | ADX DI cross · 1h | buy | AMZN | 6.53 | — | entry |
| 2026-10-27T17:30 | ADX DI cross · 1h | sell | AAPL | 6.53 | -0.03 | exit signal |
| 2026-10-27T17:25 | Agent (ML meta-label) | buy | IWM | 12.11 | — | entry |
| 2026-10-27T17:25 | Agent (ML meta-label) | buy | AMD | 16.17 | — | entry |
| 2026-10-27T17:25 | Agent (ML meta-label) | sell | SOXL | 4.12 | 0.10 | rebalance down |
| 2026-10-27T17:25 | Stochastic reversion · 1h | buy | META | 4.40 | — | rebalance up |
| 2026-10-27T17:25 | Volume breakout | buy | DOGE-USD | 13.18 | — | entry signal |
| 2026-10-27T17:20 | ROC + volume | sell | AMZN | 13.51 | -0.03 | exit signal |
| 2026-10-27T17:15 | Agent (ML meta-label) | sell | AMD | 20.18 | -0.01 | selected signal exited |
| 2026-10-27T17:10 | ROC + volume | buy | ETHU | 13.52 | — | entry signal |
| 2026-10-27T17:07 | Agent (ML meta-label) | buy | AMD | 20.19 | — | entry |
| 2026-10-27T17:05 | Agent (ML meta-label) | sell | AMD | 20.17 | -0.02 | selected signal exited |
| 2026-10-27T17:01 | MFI reversion · 1h | sell | BTC-USD | 20.83 | 0.01 | exit signal |
| 2026-10-27T17:01 | Squeeze breakout · 1h | buy | ETH-USD | 13.72 | — | entry signal |
| 2026-10-27T17:01 | Squeeze breakout · 1h | buy | BTC-USD | 18.22 | — | entry signal |
| 2026-10-27T17:01 | Squeeze breakout · 1h | sell | XRP-USD | 4.57 | -0.01 | rebalance down |
| 2026-10-27T17:01 | Squeeze breakout · 1h | sell | IWM | 4.76 | 0.03 | rebalance down |
| 2026-10-27T16:55 | Agent (ML meta-label) | buy | NVDA | 4.04 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 17:36:05.000135+00:00 -> 2026-10-27 17:46:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
