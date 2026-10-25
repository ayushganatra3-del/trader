# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T17:40:05.000103+00:00 · 35721 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, IAM 12%, APLD 12%, BPRE 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 13353 decisions in 2676 calls, $0.1867 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T17:40 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-25T17:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T17:40 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | BITX | 2.56 | +2.84% | 15 |
| VWAP momentum | PLTR | 2.20 | +6.89% | 7 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.95 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.02 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.60 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -12.04 | -3.33 | -13.74 | 157 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 6.21 | 2.99 | -1.37 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.18 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.85 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.42 | -4.58 | 0 | — | 0.36 | 0.23 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.13 | -5.87 | 25 | 40.0 | -17.34 | -3.33 | -21.47 | 61 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.76 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -6.94 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.50 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.42 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 91.92 | -8.08 | 118 | 25.4 | -21.99 | -5.05 | -25.01 | 255 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.35 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.35 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.83 | -9.17 | 109 | 18.3 | -12.17 | -2.47 | -14.71 | 258 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.03 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -14.69 | -2.97 | -17.81 | 114 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.70 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.74 | -11.26 | 106 | 27.4 | -12.35 | -2.41 | -16.40 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.23 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.84 | -3.90 | -22.47 | 393 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.60 | -4.72 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -23.18 | -4.56 | -25.15 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.06 | -4.63 | -17.87 | 703 |
| 40 | RSI momentum · 1h | momentum | 85.55 | -14.45 | 101 | 15.8 | -21.17 | -4.45 | -23.32 | 216 |
| 41 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 42 | Supertrend · 1h | trend | 84.89 | -15.11 | 112 | 14.3 | -25.07 | -5.25 | -27.77 | 216 |
| 43 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 44 | MACD cross · 1h | trend | 83.76 | -16.24 | 228 | 22.8 | -24.27 | -4.84 | -27.39 | 466 |
| 45 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.51 | -5.24 | -28.32 | 211 |
| 46 | Z-score reversion · 1h | reversion | 83.44 | -16.56 | 110 | 33.6 | -15.49 | -2.60 | -21.48 | 204 |
| 47 | MFI reversion · 1h | reversion | 81.49 | -18.51 | 262 | 31.7 | -16.12 | -2.62 | -20.54 | 148 |
| 48 | Donchian 20/10 · 1h | breakout | 81.29 | -18.71 | 97 | 19.6 | -24.17 | -4.62 | -27.27 | 217 |
| 49 | MACD zero-line · 1h | trend | 81.16 | -18.84 | 106 | 15.1 | -22.09 | -4.59 | -25.51 | 219 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.58 | -6.87 | -32.97 | 304 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -35.79 | -6.32 | -36.33 | 536 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -32.14 | -6.69 | -32.46 | 373 |
| 53 | CCI reversion · 1h | reversion | 79.80 | -20.20 | 204 | 42.2 | -27.07 | -4.04 | -28.17 | 462 |
| 54 | Agent (ML meta-label) | meta | 79.31 | -20.69 | 874 | 18.8 | -18.25 | -3.89 | -19.62 | 363 |
| 55 | Three white soldiers | momentum | 79.30 | -20.70 | 289 | 19.0 | -44.43 | -21.03 | -44.43 | 597 |
| 56 | Heikin-Ashi · 1h | trend | 78.26 | -21.74 | 277 | 23.1 | -43.49 | -9.98 | -43.93 | 657 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -29.81 | -5.85 | -31.53 | 377 |
| 58 | Candlestick reversal · 1h | reversion | 76.85 | -23.15 | 263 | 28.1 | -35.04 | -6.62 | -35.71 | 555 |
| 59 | RSI(14) reversion · 1h | reversion | 76.81 | -23.19 | 99 | 23.2 | -16.84 | -3.13 | -24.41 | 193 |
| 60 | EMA 9/21 cross · 1h | trend | 76.74 | -23.26 | 164 | 11.6 | -30.78 | -6.26 | -34.03 | 323 |
| 61 | VWAP momentum · 1h | momentum | 75.27 | -24.73 | 531 | 20.9 | -50.50 | -11.48 | -50.74 | 1233 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 56.02 | -43.98 | 723 | 22.1 | -74.95 | -27.56 | -75.06 | 1559 |
| 64 | Volume breakout | breakout | 54.75 | -45.26 | 442 | 12.4 | -62.74 | -26.72 | -62.92 | 793 |
| 65 | Donchian 55/20 | breakout | 52.23 | -47.77 | 576 | 19.1 | -71.64 | -23.39 | -72.19 | 1261 |
| 66 | Squeeze breakout | breakout | 51.79 | -48.21 | 572 | 13.8 | -67.54 | -29.32 | -67.56 | 1169 |
| 67 | EMA 20/50 cross | trend | 51.46 | -48.54 | 633 | 20.2 | -78.94 | -23.34 | -79.27 | 1417 |
| 68 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -45.42 | -98.83 | 5101 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.82 | -45.23 | -93.95 | 2529 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.94 | -30.79 | -89.09 | 1903 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -38.12 | -91.54 | 2328 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.27 | -29.47 | -90.29 | 2150 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -55.39 | -97.90 | 3519 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.13 | -59.98 | -96.19 | 3368 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.14 | -35.60 | -94.17 | 2464 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.96 | -36.18 | -83.27 | 1696 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -54.92 | -99.42 | 5776 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.43 | -42.09 | -92.58 | 2604 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -37.99 | -95.44 | 3370 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -82.57 | -99.78 | 6176 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -45.49 | -92.31 | 2339 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -63.60 | -97.66 | 3553 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.45 | -98.65 | 4788 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -59.89 | -94.65 | 2781 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.21 | -39.76 | -84.30 | 1794 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -68.38 | -99.59 | 6257 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.41 | -29.57 | -88.42 | 2230 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.25 | -20.37 | -78.27 | 1711 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.76 | -38.48 | -90.80 | 2276 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.28 | -48.94 | -96.28 | 3797 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.75 | -51.22 | -89.81 | 2114 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.79 | -18.25 | -76.94 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.43 | -49.83 | -96.44 | 4181 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -113.20 | -99.92 | 8254 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T17:35 | Volume breakout | sell | BTC-USD | 13.62 | -0.09 | exit signal |
| 2026-10-25T17:25 | ROC + volume | buy | SOL-USD | 14.03 | — | entry signal |
| 2026-10-25T17:05 | ROC + volume | buy | XRP-USD | 14.03 | — | entry signal |
| 2026-10-25T17:00 | Z-score reversion · 1h | buy | ETH-USD | 1.25 | — | entry |
| 2026-10-25T17:00 | Z-score reversion · 1h | buy | DOGE-USD | 5.14 | — | rebalance up |
| 2026-10-25T17:00 | Z-score reversion · 1h | sell | BTC-USD | 6.38 | -0.04 | exit signal |
| 2026-10-25T17:00 | Heikin-Ashi · 1h | buy | SOL-USD | 19.58 | — | entry signal |
| 2026-10-25T17:00 | ADX DI cross · 1h | buy | SOL-USD | 22.73 | — | entry signal |
| 2026-10-25T17:00 | Parabolic SAR · 1h | buy | XRP-USD | 23.01 | — | entry signal |
| 2026-10-25T17:00 | MACD cross · 1h | buy | XRP-USD | 4.05 | — | entry signal |
| 2026-10-25T17:00 | Volume breakout | buy | BTC-USD | 13.71 | — | entry signal |
| 2026-10-25T17:00 | Squeeze breakout | buy | XRP-USD | 12.96 | — | entry signal |
| 2026-10-25T17:00 | Donchian 55/20 | buy | XRP-USD | 13.02 | — | entry signal |
| 2026-10-25T16:40 | Agent (ML meta-label) | sell | XRP-USD | 4.37 | -0.03 | selected signal exited |
| 2026-10-25T16:30 | Agent (ML meta-label) | buy | XRP-USD | 4.41 | — | entry |
| 2026-10-25T16:05 | Volume breakout | sell | XRP-USD | 13.65 | -0.12 | exit signal |
| 2026-10-25T16:05 | Volume breakout | sell | ETH-USD | 13.64 | -0.13 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | XRP-USD | 14.02 | -0.12 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | SOL-USD | 14.05 | -0.09 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | ETH-USD | 14.01 | -0.13 | exit signal |
| 2026-10-25T16:05 | ROC + volume | sell | DOGE-USD | 14.04 | -0.10 | exit signal |
| 2026-10-25T16:00 | VWAP reversion · 1h | sell | SOL-USD | 25.16 | 0.03 | exit signal |
| 2026-10-25T16:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.96 | — | entry |
| 2026-10-25T16:00 | VWAP momentum · 1h | sell | BTC-USD | 6.96 | -0.04 | exit signal |
| 2026-10-25T16:00 | MACD cross · 1h | buy | SOL-USD | 9.30 | — | entry signal |
| 2026-10-25T16:00 | Three white soldiers | sell | BTC-USD | 19.72 | -0.13 | exit signal |
| 2026-10-25T15:40 | Three white soldiers | buy | BTC-USD | 19.86 | — | entry signal |
| 2026-10-25T15:40 | Volume breakout | buy | XRP-USD | 13.77 | — | entry signal |
| 2026-10-25T15:40 | Volume breakout | buy | ETH-USD | 13.77 | — | entry signal |
| 2026-10-25T15:40 | Donchian 55/20 | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-25T15:40 | ROC + volume | buy | XRP-USD | 14.14 | — | entry signal |
| 2026-10-25T15:40 | ROC + volume | buy | ETH-USD | 14.14 | — | entry signal |
| 2026-10-25T15:40 | EMA 20/50 cross | buy | XRP-USD | 2.57 | — | rebalance up |
| 2026-10-25T15:40 | EMA 20/50 cross | sell | ETH-USD | 2.57 | -0.01 | rebalance down |
| 2026-10-25T15:35 | ROC + volume | buy | DOGE-USD | 14.14 | — | entry signal |
| 2026-10-25T15:25 | Three white soldiers | sell | ETH-USD | 19.77 | -0.15 | exit signal |
| 2026-10-25T15:25 | Three white soldiers | sell | BTC-USD | 19.81 | -0.12 | exit signal |
| 2026-10-25T15:25 | Volume breakout | sell | BTC-USD | 13.71 | -0.08 | exit signal |
| 2026-10-25T15:25 | Squeeze breakout | sell | SOL-USD | 12.95 | -0.08 | stop-loss |
| 2026-10-25T15:25 | Squeeze breakout | sell | ETH-USD | 12.93 | -0.10 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 17:40:05.000103+00:00 -> 2026-10-25 17:50:05.000103+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
