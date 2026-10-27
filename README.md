# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T14:05:05.000167+00:00 · 37936 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 111, win rate 38.7%, fees £3.41, max drawdown -11.45%.

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

Today: 12187 decisions in 2081 calls, $0.1654 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T14:05 | 0 / 11 / 19 | cash |  |
| Breezy | 2026-10-27T14:05 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-27T14:05 | 2 / 21 / 7 | COIN 54% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.38 | 7.38 | 0 | — | 7.98 | 3.96 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 4.79 | 1.55 | -5.58 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.88 | 2.25 | -4.92 | 25 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.18 | -3.64 | -14.11 | 149 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.09 | 0 | — | 1.76 | 0.86 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.94 | -1.06 | 0 | — | -0.10 | -0.01 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.82 | -2.18 | 79 | 34.2 | 6.17 | 2.95 | -1.87 | 98 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.25 | -2.06 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.97 | -3.03 | 0 | — | -0.10 | 0.03 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 95.87 | -4.13 | 122 | 31.1 | -1.89 | -0.91 | -6.39 | 189 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.10 | 0.99 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.96 | -5.04 | 0 | — | -6.71 | -2.80 | -7.83 | 1 |
| 18 | Hold BTC | benchmark | 94.82 | -5.18 | 0 | — | 2.19 | 0.53 | -9.28 | 1 |
| 19 | Gap and go | momentum | 93.92 | -6.08 | 108 | 25.0 | 3.93 | 1.30 | -8.76 | 205 |
| 20 | Copy: Insider buying | copy | 93.76 | -6.24 | 27 | 37.0 | -19.26 | -3.74 | -22.94 | 63 |
| 21 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 22 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.79 | -3.28 | -17.21 | 574 |
| 23 | Donchian 55/20 · 1h | breakout | 92.27 | -7.73 | 49 | 16.3 | -15.41 | -3.45 | -16.70 | 98 |
| 24 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.48 | -2.22 | -16.91 | 1 |
| 25 | Daily: Momentum burst | daily | 91.05 | -8.95 | 13 | 15.4 | -19.13 | -3.73 | -19.61 | 39 |
| 26 | Squeeze breakout · 1h | breakout | 90.93 | -9.07 | 52 | 23.1 | -5.05 | -1.29 | -12.00 | 91 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 90.54 | -9.46 | 0 | — | -3.04 | -0.35 | -14.57 | 1 |
| 28 | Daily: Bullish score | daily | 90.37 | -9.63 | 11 | 18.2 | -6.55 | -0.78 | -14.40 | 14 |
| 29 | ADX DI cross · 1h | trend | 90.22 | -9.78 | 116 | 19.0 | -12.23 | -2.67 | -14.45 | 268 |
| 30 | Parabolic SAR · 1h | trend | 90.12 | -9.88 | 121 | 25.6 | -22.13 | -5.62 | -23.02 | 248 |
| 31 | Agent | meta | 89.98 | -10.02 | 111 | 38.7 | -10.70 | -6.76 | -12.47 | 216 |
| 32 | Max aggression: 5-day momentum | meta | 89.92 | -10.08 | 12 | 41.7 | -15.42 | -1.41 | -27.23 | 25 |
| 33 | Volume breakout · 1h | breakout | 89.09 | -10.91 | 105 | 23.8 | -13.60 | -2.84 | -15.90 | 106 |
| 34 | Agent (aggressive) | meta | 88.08 | -11.92 | 55 | 36.4 | -11.23 | -3.70 | -14.77 | 97 |
| 35 | Bollinger breakout · 1h | breakout | 87.51 | -12.49 | 109 | 26.6 | -14.69 | -2.95 | -18.15 | 239 |
| 36 | Stochastic reversion · 1h | reversion | 87.48 | -12.52 | 200 | 46.5 | -22.47 | -4.16 | -23.44 | 391 |
| 37 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.45 | -4.09 | -17.87 | 700 |
| 38 | Keltner breakout · 1h | breakout | 86.17 | -13.83 | 74 | 23.0 | -21.38 | -4.39 | -22.91 | 179 |
| 39 | Z-score reversion · 1h | reversion | 85.57 | -14.43 | 118 | 33.1 | -13.79 | -2.23 | -21.48 | 211 |
| 40 | Connors RSI(2) · 1h | reversion | 85.06 | -14.94 | 175 | 40.6 | -26.52 | -7.97 | -27.00 | 197 |
| 41 | Supertrend · 1h | trend | 84.23 | -15.77 | 114 | 14.0 | -26.44 | -5.61 | -28.00 | 223 |
| 42 | EMA 20/50 cross · 1h | trend | 83.99 | -16.01 | 73 | 11.0 | -23.47 | -4.68 | -25.20 | 131 |
| 43 | RSI momentum · 1h | momentum | 83.71 | -16.29 | 104 | 15.4 | -20.39 | -3.97 | -22.24 | 200 |
| 44 | MACD cross · 1h | trend | 83.11 | -16.89 | 244 | 22.1 | -28.46 | -5.90 | -29.40 | 481 |
| 45 | MFI reversion · 1h | reversion | 82.75 | -17.25 | 266 | 31.6 | -16.96 | -2.65 | -20.70 | 152 |
| 46 | Ichimoku · 1h | trend | 82.41 | -17.59 | 68 | 11.8 | -21.39 | -4.45 | -24.73 | 109 |
| 47 | Triple EMA stack · 1h | trend | 82.09 | -17.91 | 101 | 14.9 | -28.62 | -5.72 | -30.39 | 203 |
| 48 | CCI reversion · 1h | reversion | 81.03 | -18.97 | 224 | 44.6 | -25.87 | -3.72 | -28.08 | 465 |
| 49 | Williams %R · 1h | reversion | 80.98 | -19.02 | 229 | 46.3 | -36.26 | -6.32 | -36.30 | 537 |
| 50 | Bollinger reversion · 1h | reversion | 80.70 | -19.30 | 181 | 37.0 | -28.59 | -5.74 | -30.32 | 365 |
| 51 | MACD zero-line · 1h | trend | 80.35 | -19.64 | 111 | 15.3 | -24.03 | -5.16 | -25.05 | 219 |
| 52 | Donchian 20/10 · 1h | breakout | 80.27 | -19.73 | 99 | 20.2 | -25.10 | -4.93 | -26.49 | 209 |
| 53 | Agent (ML meta-label) | meta | 79.78 | -20.22 | 932 | 19.7 | -11.02 | -2.11 | -15.78 | 344 |
| 54 | OBV trend · 1h | momentum | 79.24 | -20.76 | 207 | 17.9 | -30.85 | -6.59 | -32.01 | 294 |
| 55 | RSI(14) reversion · 1h | reversion | 78.92 | -21.08 | 105 | 25.7 | -16.55 | -3.02 | -24.48 | 188 |
| 56 | Three white soldiers | momentum | 77.79 | -22.21 | 310 | 19.0 | -44.24 | -20.29 | -44.67 | 604 |
| 57 | ROC + volume · 1h | momentum | 77.54 | -22.46 | 256 | 25.4 | -31.23 | -6.07 | -33.27 | 371 |
| 58 | Heikin-Ashi · 1h | trend | 77.05 | -22.95 | 293 | 22.9 | -44.64 | -10.18 | -45.11 | 657 |
| 59 | Candlestick reversal · 1h | reversion | 76.57 | -23.43 | 277 | 28.9 | -33.45 | -6.25 | -34.54 | 553 |
| 60 | VWAP momentum · 1h | momentum | 75.65 | -24.35 | 561 | 21.2 | -49.24 | -10.83 | -50.69 | 1235 |
| 61 | EMA 9/21 cross · 1h | trend | 75.52 | -24.48 | 176 | 10.8 | -32.64 | -6.97 | -33.52 | 331 |
| 62 | Max aggression: 1-day momentum | meta | 68.76 | -31.24 | 20 | 30.0 | -40.79 | -2.82 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.90 | -46.10 | 774 | 22.0 | -74.61 | -26.57 | -74.76 | 1587 |
| 64 | Volume breakout | breakout | 53.20 | -46.80 | 467 | 12.6 | -62.92 | -26.10 | -63.16 | 805 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -42.96 | -98.88 | 5175 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.62 | -23.37 | -80.02 | 1422 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.73 | -43.87 | -93.77 | 2537 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.24 | -30.11 | -89.36 | 1920 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.40 | -36.36 | -91.53 | 2344 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.41 | -31.88 | -90.44 | 2163 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -50.65 | -97.89 | 3528 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -53.93 | -96.21 | 3386 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.09 | -36.11 | -94.09 | 2453 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.36 | -32.68 | -82.58 | 1686 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -52.70 | -99.43 | 5783 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -40.78 | -92.89 | 2632 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -38.24 | -95.41 | 3363 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -69.95 | -99.78 | 6165 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.31 | -44.42 | -92.34 | 2337 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.39 | -97.77 | 3582 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.84 | -98.66 | 4803 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.76 | -28.49 | -68.45 | 1189 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -55.05 | -94.65 | 2779 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -38.93 | -84.58 | 1816 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.76 | -99.61 | 6308 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.34 | -28.97 | -88.34 | 2235 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.68 | -18.95 | -77.09 | 1704 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.59 | -36.81 | -90.61 | 2277 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.29 | -47.37 | -96.29 | 3827 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.17 | -50.89 | -90.17 | 2144 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.41 | -23.50 | -72.97 | 1290 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.05 | -17.70 | -76.27 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.22 | -96.55 | 4206 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.63 | -99.92 | 8278 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T14:05 | Agent (ML meta-label) | buy | QQQ | 4.03 | — | rebalance up |
| 2026-10-27T14:05 | Agent (ML meta-label) | sell | AMD | 4.03 | 0.07 | rebalance down |
| 2026-10-27T14:01 | Agent (ML meta-label) | buy | QQQ | 8.00 | — | entry |
| 2026-10-27T14:01 | Agent (ML meta-label) | sell | TQQQ | 4.00 | 0.01 | rebalance down |
| 2026-10-27T14:01 | Agent (ML meta-label) | sell | AMZN | 4.01 | 0.00 | rebalance down |
| 2026-10-27T14:01 | MFI reversion · 1h | buy | NVDA | 4.19 | — | rebalance up |
| 2026-10-27T14:01 | MFI reversion · 1h | sell | GOOGL | 10.33 | -0.09 | target is flat |
| 2026-10-27T14:01 | OBV trend · 1h | buy | XRP-USD | 7.06 | — | rebalance up |
| 2026-10-27T14:01 | OBV trend · 1h | buy | TNA | 4.02 | — | rebalance up |
| 2026-10-27T14:01 | OBV trend · 1h | buy | PLTR | 4.07 | — | rebalance up |
| 2026-10-27T14:01 | OBV trend · 1h | buy | IWM | 3.98 | — | rebalance up |
| 2026-10-27T14:01 | OBV trend · 1h | sell | TSLA | 19.13 | 0.32 | target is flat |
| 2026-10-27T14:01 | VWAP momentum · 1h | sell | SOL-USD | 2.33 | -0.02 | exit signal |
| 2026-10-27T14:01 | ROC + volume | sell | TECL | 9.02 | 0.02 | target is flat |
| 2026-10-27T13:55 | Agent (rotation) | sell | TQQQ | 31.80 | -0.24 | selected signal exited |
| 2026-10-27T13:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 104.77 | -0.81 | target is flat |
| 2026-10-27T13:55 | Agent (ML meta-label) | buy | TQQQ | 8.57 | — | rebalance up |
| 2026-10-27T13:55 | Agent (ML meta-label) | buy | TNA | 8.53 | — | rebalance up |
| 2026-10-27T13:55 | Agent (ML meta-label) | buy | AMZN | 6.70 | — | rebalance up |
| 2026-10-27T13:55 | Agent (ML meta-label) | buy | AMD | 8.59 | — | rebalance up |
| 2026-10-27T13:55 | Agent (ML meta-label) | sell | QQQ | 11.42 | -0.05 | selected signal exited |
| 2026-10-27T13:55 | Agent (ML meta-label) | sell | META | 13.28 | -0.14 | selected signal exited |
| 2026-10-27T13:55 | Stochastic reversion · 1h | buy | SQQQ | 5.12 | — | rebalance up |
| 2026-10-27T13:55 | Stochastic reversion · 1h | buy | LABU | 4.83 | — | rebalance up |
| 2026-10-27T13:55 | Stochastic reversion · 1h | buy | GOOGL | 4.97 | — | rebalance up |
| 2026-10-27T13:55 | Stochastic reversion · 1h | buy | AMZN | 4.96 | — | rebalance up |
| 2026-10-27T13:55 | Stochastic reversion · 1h | buy | AAPL | 5.04 | — | rebalance up |
| 2026-10-27T13:55 | Stochastic reversion · 1h | sell | META | 12.34 | -0.32 | stop-loss |
| 2026-10-27T13:55 | Bollinger reversion · 1h | sell | META | 19.92 | -0.66 | stop-loss |
| 2026-10-27T13:55 | ROC + volume | buy | TQQQ | 8.99 | — | entry signal |
| 2026-10-27T13:55 | ROC + volume | buy | TECL | 9.00 | — | entry |
| 2026-10-27T13:55 | ROC + volume | buy | LABU | 9.00 | — | entry signal |
| 2026-10-27T13:55 | ROC + volume | sell | TSLA | 4.49 | 0.02 | rebalance down |
| 2026-10-27T13:55 | ROC + volume | sell | TNA | 13.43 | -0.08 | stop-loss |
| 2026-10-27T13:55 | ROC + volume | sell | SOXL | 4.56 | -0.01 | rebalance down |
| 2026-10-27T13:55 | ROC + volume | sell | AMD | 4.51 | -0.02 | rebalance down |
| 2026-10-27T13:50 | Day trade: Stocks in Play ORB | sell | GOOGL | 24.43 | -0.15 | target is flat |
| 2026-10-27T13:50 | Agent (ML meta-label) | sell | TSLA | 7.69 | -0.01 | selected signal exited |
| 2026-10-27T13:50 | Squeeze breakout | sell | UPRO | 5.55 | -0.04 | Kill switch: down 50% from peak |
| 2026-10-27T13:50 | Squeeze breakout | sell | TSLA | 5.62 | 0.03 | Kill switch: down 50% from peak |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 14:05:05.000167+00:00 -> 2026-10-27 14:15:05.000167+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
