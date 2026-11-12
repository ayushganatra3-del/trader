# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T14:10:05.000109+00:00 · 57006 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 11193 decisions in 2244 calls, $0.1567 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T14:10 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-12T14:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-12T14:10 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.43 | 16.43 | 0 | — | 16.04 | 5.08 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.71 | 15.71 | 20 | 70.0 | 17.89 | 3.60 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.74 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.01 | 4.01 | 0 | — | 6.40 | 1.76 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 6.52 | 1.85 | -9.06 | 231 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.71 | -0.29 | 134 | 34.3 | 10.31 | 3.58 | -3.28 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | 0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.62 | -1.38 | 0 | — | -0.64 | -0.12 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.09 | -1.91 | 188 | 30.3 | -2.43 | -0.87 | -8.82 | 163 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.15 | -2.85 | 0 | — | -2.23 | -0.51 | -9.25 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 15 | Copy: Insider buying | copy | 95.58 | -4.42 | 43 | 39.5 | -5.77 | -1.11 | -15.11 | 67 |
| 16 | VWAP reversion · 1h | reversion | 95.53 | -4.47 | 142 | 47.2 | -12.77 | -3.31 | -13.44 | 155 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.50 | -5.50 | 0 | — | -3.37 | -0.85 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Trend pullback · 1h | trend | 91.75 | -8.25 | 109 | 22.9 | -12.37 | -4.63 | -16.41 | 74 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.88 | -11.12 | 404 | 33.2 | -12.12 | -3.50 | -14.11 | 597 |
| 23 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -4.89 | -0.99 | -17.04 | 78 |
| 24 | Max aggression: 5-day momentum | meta | 87.68 | -12.32 | 19 | 47.4 | -25.53 | -1.30 | -45.81 | 24 |
| 25 | Parabolic SAR · 1h | trend | 86.55 | -13.46 | 168 | 26.8 | -13.17 | -2.78 | -21.94 | 219 |
| 26 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -14.97 | -7.46 | -15.33 | 209 |
| 27 | Hold BTC | benchmark | 84.97 | -15.03 | 1 | 0.0 | -8.26 | -0.86 | -17.24 | 1 |
| 28 | Daily: Bullish score | daily | 84.43 | -15.57 | 16 | 18.8 | -9.89 | -1.69 | -19.56 | 18 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.25 | -15.74 | 2 | 0.0 | -6.49 | -0.62 | -24.16 | 1 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -16.78 | -4.70 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 82.99 | -17.01 | 72 | 13.9 | -22.99 | -4.88 | -29.34 | 92 |
| 32 | ADX DI cross · 1h | trend | 82.33 | -17.67 | 186 | 18.8 | -22.21 | -3.76 | -29.87 | 279 |
| 33 | Keltner breakout · 1h | breakout | 82.07 | -17.93 | 111 | 24.3 | -17.00 | -3.49 | -24.55 | 169 |
| 34 | Stochastic reversion · 1h | reversion | 81.90 | -18.10 | 293 | 48.1 | -24.84 | -3.66 | -27.08 | 394 |
| 35 | Max aggression: 1-day momentum | meta | 81.27 | -18.73 | 27 | 25.9 | -17.50 | -0.43 | -57.50 | 40 |
| 36 | Opening range 15m | breakout | 80.92 | -19.08 | 501 | 31.3 | -18.42 | -4.93 | -21.11 | 722 |
| 37 | Volume breakout · 1h | breakout | 80.84 | -19.16 | 149 | 27.5 | -13.25 | -3.06 | -21.11 | 91 |
| 38 | Connors RSI(2) · 1h | reversion | 80.32 | -19.68 | 208 | 39.9 | -20.27 | -6.81 | -20.74 | 121 |
| 39 | Heikin-Ashi · 1h | trend | 80.31 | -19.69 | 418 | 24.6 | -34.72 | -6.43 | -38.20 | 656 |
| 40 | MFI reversion · 1h | reversion | 79.20 | -20.80 | 375 | 35.5 | -16.30 | -2.10 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.05 | -21.95 | 367 | 22.1 | -27.75 | -4.02 | -39.83 | 464 |
| 42 | CCI reversion · 1h | reversion | 77.21 | -22.79 | 337 | 44.5 | -29.46 | -4.58 | -31.37 | 452 |
| 43 | Bollinger breakout · 1h | breakout | 77.02 | -22.98 | 176 | 22.2 | -21.58 | -4.59 | -28.24 | 240 |
| 44 | MACD zero-line · 1h | trend | 75.79 | -24.20 | 162 | 16.7 | -20.77 | -4.07 | -30.74 | 210 |
| 45 | Bollinger reversion · 1h | reversion | 75.69 | -24.31 | 286 | 41.6 | -28.43 | -4.37 | -34.84 | 370 |
| 46 | Supertrend · 1h | trend | 75.46 | -24.54 | 168 | 13.1 | -28.51 | -5.00 | -36.14 | 220 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 48 | RSI momentum · 1h | momentum | 75.01 | -24.99 | 159 | 12.6 | -25.99 | -3.94 | -37.48 | 215 |
| 49 | Daily: Momentum burst | daily | 74.87 | -25.13 | 27 | 11.1 | -33.19 | -4.55 | -38.23 | 36 |
| 50 | EMA 20/50 cross · 1h | trend | 74.49 | -25.51 | 103 | 10.7 | -27.12 | -4.60 | -37.26 | 117 |
| 51 | Triple EMA stack · 1h | trend | 74.14 | -25.86 | 144 | 14.6 | -25.03 | -4.13 | -35.90 | 205 |
| 52 | ROC + volume · 1h | momentum | 72.97 | -27.03 | 377 | 27.6 | -32.05 | -5.85 | -38.40 | 377 |
| 53 | Donchian 20/10 · 1h | breakout | 71.99 | -28.01 | 144 | 19.4 | -28.32 | -5.20 | -35.64 | 209 |
| 54 | OBV trend · 1h | momentum | 71.83 | -28.17 | 281 | 19.2 | -28.06 | -4.88 | -37.06 | 286 |
| 55 | Williams %R · 1h | reversion | 71.78 | -28.22 | 355 | 45.9 | -36.79 | -5.75 | -37.31 | 528 |
| 56 | Z-score reversion · 1h | reversion | 70.68 | -29.32 | 198 | 38.4 | -23.81 | -3.31 | -28.98 | 233 |
| 57 | RSI(14) reversion · 1h | reversion | 69.14 | -30.86 | 175 | 32.6 | -28.21 | -4.07 | -32.54 | 232 |
| 58 | VWAP momentum · 1h | momentum | 67.78 | -32.22 | 868 | 22.6 | -50.21 | -10.28 | -51.25 | 1218 |
| 59 | EMA 9/21 cross · 1h | trend | 67.25 | -32.75 | 255 | 9.8 | -33.01 | -6.23 | -41.65 | 335 |
| 60 | Agent (ML meta-label) | meta | 66.00 | -34.00 | 1754 | 24.7 | -6.42 | -0.70 | -19.55 | 345 |
| 61 | Candlestick reversal · 1h | reversion | 64.75 | -35.25 | 465 | 28.6 | -40.08 | -7.25 | -41.17 | 593 |
| 62 | Three white soldiers | momentum | 59.92 | -40.08 | 523 | 14.9 | -48.46 | -22.40 | -48.46 | 648 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -44.32 | -99.01 | 5260 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.78 | -25.49 | -79.78 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -43.74 | -93.46 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.45 | -32.33 | -89.45 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -40.36 | -91.13 | 2328 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.99 | -31.66 | -89.99 | 2183 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -54.08 | -97.88 | 3468 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -54.70 | -96.30 | 3429 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -32.94 | -93.53 | 2345 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.04 | -34.12 | -83.05 | 1656 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.56 | -99.57 | 6005 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.23 | -42.71 | -92.23 | 2604 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.51 | -95.46 | 3450 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -79.00 | -99.81 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.18 | -44.15 | -92.18 | 2269 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.08 | -25.02 | -75.30 | 1618 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -58.36 | -97.61 | 3501 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.05 | -98.88 | 4906 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.54 | -26.78 | -68.89 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -56.32 | -94.73 | 2776 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.90 | -38.40 | -84.91 | 1775 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -76.34 | -99.66 | 6352 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.89 | -32.66 | -89.90 | 2302 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.45 | -20.11 | -78.46 | 1763 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.82 | -36.87 | -90.83 | 2170 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.87 | -53.03 | -96.88 | 3856 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.15 | -57.29 | -89.15 | 2130 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.11 | -30.01 | -66.11 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.34 | -22.97 | -71.37 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.29 | -18.80 | -79.33 | 1709 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.32 | -49.59 | -97.34 | 4297 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.33 | -99.93 | 8359 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T14:00 | Williams %R · 1h | buy | ETH-USD | 5.90 | — | entry signal |
| 2026-11-12T14:00 | Williams %R · 1h | buy | DOGE-USD | 10.27 | — | entry signal |
| 2026-11-12T14:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.66 | — | entry signal |
| 2026-11-12T14:00 | Candlestick reversal · 1h | sell | XRP-USD | 3.34 | -0.00 | rebalance down |
| 2026-11-12T13:30 | Three white soldiers | sell | DOGE-USD | 14.90 | -0.11 | exit signal |
| 2026-11-12T13:25 | Three white soldiers | buy | DOGE-USD | 15.01 | — | entry signal |
| 2026-11-12T13:10 | Agent (ML meta-label) | buy | XRP-USD | 9.04 | — | entry |
| 2026-11-12T13:10 | Agent (ML meta-label) | sell | SOL-USD | 8.13 | -0.15 | selected signal exited |
| 2026-11-12T13:10 | CCI reversion · 1h | sell | SOL-USD | 3.44 | -0.06 | stop-loss |
| 2026-11-12T13:10 | CCI reversion · 1h | sell | DOGE-USD | 15.19 | -0.36 | stop-loss |
| 2026-11-12T13:10 | Williams %R · 1h | sell | XRP-USD | 10.09 | -0.38 | stop-loss |
| 2026-11-12T13:10 | Williams %R · 1h | sell | DOGE-USD | 6.07 | -0.29 | stop-loss |
| 2026-11-12T13:10 | Stochastic reversion · 1h | buy | XRP-USD | 11.13 | — | entry |
| 2026-11-12T13:10 | Stochastic reversion · 1h | sell | DOGE-USD | 11.03 | -0.73 | stop-loss |
| 2026-11-12T13:10 | VWAP reversion · 1h | sell | ETH-USD | 23.48 | -0.54 | stop-loss |
| 2026-11-12T13:10 | Z-score reversion · 1h | sell | XRP-USD | 17.07 | -0.78 | stop-loss |
| 2026-11-12T13:10 | Candlestick reversal · 1h | buy | XRP-USD | 10.49 | — | rebalance up |
| 2026-11-12T13:10 | Candlestick reversal · 1h | sell | SOL-USD | 12.81 | -0.26 | stop-loss |
| 2026-11-12T13:00 | VWAP reversion · 1h | buy | ETH-USD | 24.02 | — | entry signal |
| 2026-11-12T13:00 | Bollinger reversion · 1h | buy | BTC-USD | 3.47 | — | entry signal |
| 2026-11-12T13:00 | Candlestick reversal · 1h | buy | XRP-USD | 5.79 | — | entry signal |
| 2026-11-12T13:00 | Candlestick reversal · 1h | sell | SOL-USD | 3.24 | -0.03 | rebalance down |
| 2026-11-12T12:30 | Agent (ML meta-label) | buy | SOL-USD | 6.40 | — | rebalance up |
| 2026-11-12T12:30 | Agent (ML meta-label) | sell | BTC-USD | 7.32 | -0.08 | selected signal exited |
| 2026-11-12T12:30 | CCI reversion · 1h | buy | SOL-USD | 3.50 | — | entry |
| 2026-11-12T12:30 | CCI reversion · 1h | buy | DOGE-USD | 11.40 | — | rebalance up |
| 2026-11-12T12:30 | CCI reversion · 1h | sell | XRP-USD | 3.86 | -0.11 | stop-loss |
| 2026-11-12T12:30 | CCI reversion · 1h | sell | BTC-USD | 11.04 | -0.14 | stop-loss |
| 2026-11-12T12:30 | Candlestick reversal · 1h | buy | SOL-USD | 3.46 | — | rebalance up |
| 2026-11-12T12:30 | Candlestick reversal · 1h | sell | XRP-USD | 6.01 | -0.12 | stop-loss |
| 2026-11-12T12:00 | Agent (ML meta-label) | buy | SOL-USD | 1.87 | — | entry |
| 2026-11-12T12:00 | Agent (ML meta-label) | sell | DOGE-USD | 1.87 | -0.01 | selected signal exited |
| 2026-11-12T12:00 | Candlestick reversal · 1h | buy | SOL-USD | 8.07 | — | rebalance up |
| 2026-11-12T12:00 | Candlestick reversal · 1h | sell | DOGE-USD | 8.07 | -0.15 | target is flat |
| 2026-11-12T12:00 | VWAP momentum · 1h | sell | XRP-USD | 5.55 | -0.11 | exit signal |
| 2026-11-12T12:00 | MACD cross · 1h | sell | XRP-USD | 4.52 | -0.08 | exit signal |
| 2026-11-12T11:55 | Agent (ML meta-label) | buy | DOGE-USD | 1.88 | — | entry |
| 2026-11-12T11:55 | Agent (ML meta-label) | buy | BTC-USD | 3.55 | — | rebalance up |
| 2026-11-12T11:55 | Agent (ML meta-label) | sell | ETH-USD | 5.43 | -0.15 | selected signal exited |
| 2026-11-12T11:50 | CCI reversion · 1h | buy | DOGE-USD | 4.15 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 14:10:05.000109+00:00 -> 2026-11-12 14:20:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
