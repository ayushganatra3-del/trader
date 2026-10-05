# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-05T13:35:05.000116+00:00 · 12501 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.25 (-0.76%)

Closed trades 33, win rate 66.7%, fees £1.04, max drawdown -1.59%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-05 | SLBT 12%, KOD 12%, ADRX 12%, GME 12%, BPRE 12%, PAM 12%, CX 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 10135 decisions in 2027 calls, $0.1422 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-05T13:35 | 0 / 2 / 3 | COIN 18%, AMZN 18%, MSTR 17% |  |
| Breezy | 2026-10-05T13:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-05T13:35 | 1 / 3 / 1 | MSTR 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.58 | +4.45% | 4 |
| VWAP reversion | AMZN | 1.94 | +0.87% | 3 |
| VWAP reversion | TECL | 1.77 | +2.87% | 3 |
| Z-score reversion | SQQQ | 1.74 | +3.40% | 6 |
| RSI(14) reversion | SQQQ | 1.71 | +3.09% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 103.27 | 3.27 | 0 | — | -6.21 | -1.09 | -15.27 | 2 |
| 2 | Hold BTC | benchmark | 102.94 | 2.94 | 0 | — | 34.08 | 4.11 | -8.68 | 1 |
| 3 | VWAP reversion · 1h | reversion | 102.70 | 2.70 | 25 | 36.0 | -7.69 | -2.39 | -14.05 | 112 |
| 4 | Daily: Bullish score | daily | 102.31 | 2.31 | 3 | 0.0 | 5.08 | 0.87 | -12.76 | 13 |
| 5 | Candlestick reversal · 1h | reversion | 101.95 | 1.95 | 53 | 37.7 | -21.11 | -4.70 | -24.04 | 483 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 7 | Timing: Nasdaq FTD · QQQ | daily | 101.34 | 1.34 | 0 | — | -1.63 | -0.89 | -5.09 | 2 |
| 8 | Copy: Congress Democrats (NANC) | copy | 101.12 | 1.12 | 0 | — | 4.22 | 1.90 | -3.62 | 1 |
| 9 | Stochastic reversion · 1h | reversion | 100.44 | 0.44 | 46 | 60.9 | -7.31 | -1.45 | -10.72 | 327 |
| 10 | RSI(14) reversion · 1h | reversion | 100.44 | 0.44 | 11 | 63.6 | 5.22 | 1.46 | -6.57 | 117 |
| 11 | Z-score reversion · 1h | reversion | 100.42 | 0.42 | 20 | 55.0 | 6.84 | 1.53 | -8.60 | 155 |
| 12 | Hold SPY | benchmark | 100.42 | 0.42 | 0 | — | 0.69 | 0.47 | -3.66 | 1 |
| 13 | Donchian 55/20 · 1h | breakout | 100.26 | 0.26 | 17 | 0.0 | 6.50 | 1.00 | -16.96 | 108 |
| 14 | Bollinger reversion · 1h | reversion | 100.19 | 0.19 | 42 | 42.9 | -14.71 | -3.84 | -17.84 | 302 |
| 15 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 16 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 17 | Trend pullback · 1h | trend | 99.89 | -0.11 | 51 | 23.5 | -17.80 | -5.19 | -22.16 | 159 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 4.35 | 2.11 | -1.46 | 82 |
| 19 | Copy: Warren Buffett (BRK-B) | copy | 99.87 | -0.14 | 0 | — | -2.21 | -0.84 | -7.65 | 1 |
| 20 | Connors RSI(2) · 1h | reversion | 99.85 | -0.15 | 64 | 45.3 | -12.75 | -4.45 | -16.84 | 221 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 99.78 | -0.22 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 22 | CCI reversion · 1h | reversion | 99.50 | -0.50 | 63 | 49.2 | 0.84 | 0.30 | -12.41 | 407 |
| 23 | EMA 20/50 cross · 1h | trend | 99.36 | -0.64 | 25 | 8.0 | 11.62 | 1.50 | -15.33 | 139 |
| 24 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.22 | -5.83 | -10.18 | 220 |
| 25 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.25 | -0.27 | -1.79 | 19 |
| 26 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.18 | -0.82 | 5 | 20.0 | 9.30 | 2.40 | -7.55 | 44 |
| 27 | Williams %R · 1h | reversion | 99.02 | -0.98 | 71 | 54.9 | -16.38 | -2.91 | -19.41 | 499 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.90 | -1.10 | 0 | — | 23.08 | 3.42 | -6.29 | 1 |
| 29 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 30 | Daily: SMA 20/50 cross · AAPL | daily | 98.60 | -1.40 | 0 | — | 2.25 | 0.92 | -5.18 | 1 |
| 31 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.43 | -3.95 | 25 |
| 32 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -3.80 | -1.95 | -6.07 | 104 |
| 33 | Agent (rotation) | meta | 97.99 | -2.01 | 53 | 24.5 | -0.51 | -0.09 | -9.73 | 264 |
| 34 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -6.06 | -2.19 | -9.74 | 22 |
| 35 | Daily: Momentum burst | daily | 97.51 | -2.49 | 3 | 0.0 | -0.35 | 0.13 | -16.91 | 45 |
| 36 | Agent (ML meta-label) | meta | 97.20 | -2.80 | 218 | 16.5 | 5.59 | 1.08 | -11.57 | 379 |
| 37 | Parabolic SAR · 1h | trend | 96.78 | -3.22 | 53 | 17.0 | -4.85 | -0.47 | -19.61 | 297 |
| 38 | ADX DI cross · 1h | trend | 96.54 | -3.46 | 41 | 12.2 | -4.17 | -0.51 | -13.84 | 254 |
| 39 | Supertrend · 1h | trend | 96.43 | -3.57 | 29 | 10.3 | 2.46 | 0.52 | -16.43 | 202 |
| 40 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 7.79 | 2.05 | -4.64 | 191 |
| 41 | MFI reversion · 1h | reversion | 96.17 | -3.83 | 72 | 27.8 | -8.94 | -1.53 | -16.99 | 119 |
| 42 | Copy: Insider buying | copy | 95.98 | -4.02 | 6 | 50.0 | -19.63 | -3.90 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.92 | -4.08 | 79 | 19.0 | -6.96 | -0.95 | -17.27 | 472 |
| 44 | Squeeze breakout · 1h | breakout | 95.25 | -4.75 | 27 | 22.2 | 11.89 | 2.03 | -8.06 | 115 |
| 45 | Max aggression: 1-day momentum | meta | 95.22 | -4.78 | 6 | 33.3 | -26.77 | -1.47 | -40.19 | 43 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -14.21 | -4.25 | -16.25 | 551 |
| 47 | RSI momentum · 1h | momentum | 94.93 | -5.07 | 41 | 2.4 | -0.80 | 0.09 | -16.65 | 231 |
| 48 | Ichimoku · 1h | trend | 94.34 | -5.66 | 30 | 16.7 | 6.12 | 0.92 | -15.84 | 122 |
| 49 | Triple EMA stack · 1h | trend | 94.11 | -5.89 | 51 | 9.8 | -8.68 | -0.83 | -24.62 | 242 |
| 50 | Bollinger breakout · 1h | breakout | 93.47 | -6.53 | 44 | 27.3 | 7.13 | 1.09 | -12.06 | 295 |
| 51 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -17.39 | -5.01 | -19.20 | 681 |
| 52 | Volume breakout · 1h | breakout | 92.78 | -7.22 | 31 | 9.7 | 3.53 | 0.67 | -12.60 | 130 |
| 53 | EMA 9/21 cross · 1h | trend | 92.38 | -7.62 | 70 | 12.9 | -3.44 | -0.27 | -18.47 | 344 |
| 54 | VWAP momentum · 1h | momentum | 92.20 | -7.80 | 186 | 22.6 | -38.95 | -6.04 | -38.95 | 1265 |
| 55 | Donchian 20/10 · 1h | breakout | 91.21 | -8.79 | 32 | 15.6 | -0.13 | 0.20 | -16.18 | 224 |
| 56 | MACD zero-line · 1h | trend | 90.92 | -9.08 | 42 | 16.7 | -2.46 | -0.11 | -18.32 | 237 |
| 57 | Three white soldiers | momentum | 90.65 | -9.35 | 78 | 14.1 | -49.84 | -26.51 | -49.85 | 578 |
| 58 | Max aggression: 5-day momentum | meta | 90.52 | -9.48 | 5 | 40.0 | -22.16 | -1.99 | -29.56 | 30 |
| 59 | Heikin-Ashi · 1h | trend | 90.12 | -9.88 | 99 | 25.3 | -32.47 | -5.68 | -34.14 | 683 |
| 60 | OBV trend · 1h | momentum | 89.92 | -10.08 | 98 | 11.2 | -13.82 | -1.58 | -26.78 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.40 | -11.60 | 27 | 7.4 | -13.60 | -1.68 | -23.21 | 225 |
| 62 | ROC + volume · 1h | momentum | 87.17 | -12.83 | 91 | 15.4 | -10.23 | -1.26 | -23.18 | 413 |
| 63 | RSI(14) reversion | reversion | 86.16 | -13.84 | 190 | 32.6 | -70.41 | -19.60 | -70.57 | 1420 |
| 64 | VWAP reversion | reversion | 78.74 | -21.26 | 222 | 27.9 | -69.48 | -16.71 | -69.65 | 1352 |
| 65 | Squeeze breakout | breakout | 78.34 | -21.66 | 212 | 13.7 | -63.18 | -19.64 | -63.26 | 1218 |
| 66 | Donchian 55/20 | breakout | 77.49 | -22.52 | 209 | 16.3 | -69.53 | -15.83 | -69.53 | 1293 |
| 67 | ROC + volume | momentum | 77.33 | -22.67 | 275 | 18.9 | -74.04 | -18.08 | -74.39 | 1657 |
| 68 | EMA 20/50 cross | trend | 76.02 | -23.98 | 231 | 17.7 | -79.14 | -16.70 | -79.14 | 1481 |
| 69 | Volume breakout | breakout | 75.89 | -24.11 | 188 | 11.7 | -64.73 | -20.04 | -64.73 | 918 |
| 70 | Z-score reversion | reversion | 74.90 | -25.10 | 304 | 28.0 | -84.85 | -25.69 | -84.87 | 2069 |
| 71 | MFI reversion | reversion | 72.32 | -27.68 | 302 | 20.2 | -87.56 | -31.73 | -87.58 | 2097 |
| 72 | Supertrend | trend | 71.26 | -28.74 | 310 | 19.7 | -87.41 | -23.17 | -87.41 | 1931 |
| 73 | AI bee: Bizzy | ai | 69.00 | -31.00 | 535 | 7.7 | — | — | — | — |
| 74 | Keltner breakout | breakout | 68.47 | -31.53 | 308 | 11.4 | -85.78 | -31.43 | -85.91 | 1887 |
| 75 | ADX DI cross | trend | 67.80 | -32.20 | 338 | 9.2 | -89.59 | -38.71 | -89.61 | 2089 |
| 76 | Ichimoku | trend | 67.68 | -32.32 | 277 | 7.9 | -82.93 | -25.91 | -82.94 | 1767 |
| 77 | AI bee: Boozy | ai | 67.11 | -32.89 | 209 | 3.8 | — | — | — | — |
| 78 | MACD zero-line | trend | 65.42 | -34.58 | 389 | 14.7 | -91.90 | -32.65 | -91.90 | 2368 |
| 79 | Donchian 20/10 | breakout | 64.58 | -35.42 | 411 | 16.8 | -91.37 | -28.23 | -91.48 | 2673 |
| 80 | RSI momentum | momentum | 63.02 | -36.98 | 394 | 14.0 | -91.04 | -28.21 | -91.04 | 2392 |
| 81 | Triple EMA stack | trend | 61.79 | -38.21 | 444 | 14.2 | -93.62 | -34.50 | -93.65 | 2643 |
| 82 | Trend pullback | trend | 61.35 | -38.65 | 414 | 13.8 | -91.49 | -32.45 | -91.49 | 2346 |
| 83 | Bollinger breakout | breakout | 61.02 | -38.98 | 428 | 13.6 | -94.17 | -37.48 | -94.22 | 2842 |
| 84 | Stochastic reversion | reversion | 60.89 | -39.11 | 608 | 22.0 | -95.64 | -39.74 | -95.65 | 4033 |
| 85 | Bollinger reversion | reversion | 60.28 | -39.72 | 565 | 16.1 | -95.68 | -38.50 | -95.68 | 3668 |
| 86 | Consensus | meta | 58.43 | -41.57 | 403 | 8.2 | -94.40 | -27.43 | -94.40 | 2627 |
| 87 | EMA 9/21 cross | trend | 57.02 | -42.98 | 556 | 15.8 | -97.58 | -38.11 | -97.58 | 3567 |
| 88 | Connors RSI(2) | reversion | 56.78 | -43.22 | 528 | 15.3 | -96.62 | -37.40 | -96.62 | 3625 |
| 89 | CCI reversion | reversion | 55.23 | -44.77 | 569 | 14.8 | -98.45 | -42.46 | -98.45 | 4683 |
| 90 | Candlestick reversal | reversion | 54.46 | -45.54 | 680 | 14.1 | -99.29 | -42.03 | -99.29 | 5618 |
| 91 | OBV trend | momentum | 53.88 | -46.12 | 622 | 13.7 | -96.49 | -43.75 | -96.49 | 3626 |
| 92 | VWAP momentum ⏸ | momentum | 53.60 | -46.40 | 634 | 8.7 | -98.72 | -33.89 | -98.73 | 5345 |
| 93 | Parabolic SAR | trend | 51.93 | -48.07 | 574 | 12.7 | -97.46 | -46.58 | -97.46 | 3670 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -51.45 | -99.73 | 6158 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -47.16 | -99.50 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -58.42 | -99.90 | 8272 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-05T13:35 | Max aggression: 1-day momentum | buy | BITX | 95.27 | — | entry |
| 2026-10-05T13:35 | Max aggression: 1-day momentum | sell | SOXL | 95.27 | -1.80 | target is flat |
| 2026-10-05T13:35 | Agent (rotation) | buy | TQQQ | 32.67 | — | entry |
| 2026-10-05T13:35 | Agent (rotation) | buy | META | 6.53 | — | entry |
| 2026-10-05T13:35 | Agent (rotation) | buy | LABU | 6.53 | — | entry |
| 2026-10-05T13:35 | Agent (rotation) | sell | COIN | 8.37 | 0.23 | selected signal exited |
| 2026-10-05T13:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | TQQQ | 99.23 | — | entry |
| 2026-10-05T13:35 | Agent (ML meta-label) | sell | DOGE-USD | 3.84 | -0.02 | selected signal exited |
| 2026-10-05T13:35 | Consensus | sell | ETH-USD | 14.52 | -0.12 | target is flat |
| 2026-10-05T13:35 | Daily: Connors RSI(2) · 3x ETFs | sell | TNA | 101.79 | 1.79 | target is flat |
| 2026-10-05T13:35 | Daily: Momentum burst | buy | TSLA | 24.38 | — | entry |
| 2026-10-05T13:35 | MFI reversion · 1h | buy | SPY | 24.05 | — | entry |
| 2026-10-05T13:35 | MFI reversion · 1h | buy | LABU | 24.05 | — | entry |
| 2026-10-05T13:35 | CCI reversion · 1h | buy | SOL-USD | 10.45 | — | entry |
| 2026-10-05T13:35 | CCI reversion · 1h | sell | META | 5.04 | 0.02 | rebalance down |
| 2026-10-05T13:35 | CCI reversion · 1h | sell | AAPL | 5.19 | 0.06 | rebalance down |
| 2026-10-05T13:35 | Williams %R · 1h | buy | XRP-USD | 6.23 | — | entry |
| 2026-10-05T13:35 | Williams %R · 1h | buy | SOL-USD | 11.02 | — | entry |
| 2026-10-05T13:35 | Williams %R · 1h | buy | ETH-USD | 11.02 | — | entry |
| 2026-10-05T13:35 | Williams %R · 1h | buy | BTC-USD | 11.02 | — | entry |
| 2026-10-05T13:35 | Williams %R · 1h | sell | MSTR | 5.73 | 0.15 | rebalance down |
| 2026-10-05T13:35 | Williams %R · 1h | sell | GOOGL | 5.63 | -0.01 | rebalance down |
| 2026-10-05T13:35 | Williams %R · 1h | sell | ETHU | 5.51 | 0.06 | rebalance down |
| 2026-10-05T13:35 | Williams %R · 1h | sell | BITX | 5.62 | 0.18 | rebalance down |
| 2026-10-05T13:35 | Williams %R · 1h | sell | AAPL | 16.80 | 0.21 | target is flat |
| 2026-10-05T13:35 | Stochastic reversion · 1h | buy | LABU | 5.15 | — | rebalance up |
| 2026-10-05T13:35 | Stochastic reversion · 1h | buy | GOOGL | 5.39 | — | rebalance up |
| 2026-10-05T13:35 | Stochastic reversion · 1h | buy | COIN | 5.15 | — | rebalance up |
| 2026-10-05T13:35 | Stochastic reversion · 1h | sell | AAPL | 9.93 | 0.14 | target is flat |
| 2026-10-05T13:35 | Connors RSI(2) · 1h | buy | ETH-USD | 24.98 | — | entry |
| 2026-10-05T13:35 | Connors RSI(2) · 1h | sell | MSTR | 25.59 | 1.05 | target is flat |
| 2026-10-05T13:35 | Candlestick reversal · 1h | buy | SOL-USD | 10.91 | — | entry |
| 2026-10-05T13:35 | Candlestick reversal · 1h | sell | LABU | 5.44 | 0.15 | rebalance down |
| 2026-10-05T13:35 | Candlestick reversal · 1h | sell | COIN | 5.45 | 0.15 | rebalance down |
| 2026-10-05T13:35 | Volume breakout · 1h | sell | QQQ | 9.33 | 0.01 | target is flat |
| 2026-10-05T13:35 | Squeeze breakout · 1h | sell | SOXL | 19.22 | 0.88 | stop-loss |
| 2026-10-05T13:35 | Bollinger breakout · 1h | sell | SOXL | 5.67 | 0.26 | stop-loss |
| 2026-10-05T13:35 | OBV trend · 1h | buy | DOGE-USD | 5.28 | — | entry |
| 2026-10-05T13:35 | OBV trend · 1h | buy | BTC-USD | 6.92 | — | entry |
| 2026-10-05T13:35 | OBV trend · 1h | sell | MSFT | 4.56 | 0.11 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-07 13:35:05.000116+00:00 -> 2026-10-05 13:45:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
