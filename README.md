# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T17:05:05.000178+00:00 · 11473 ticks

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
| Copy: Insider buying | 2026-10-02 | SLBT 12%, KOD 12%, ADRX 12%, GME 12%, BPRE 12%, PAM 12%, CX 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-02)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.20 · VIX 15.31 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.7, PLTR 8.5, TECL 7.0, MSTR 7.0, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 12794 decisions in 2560 calls, $0.1788 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T17:05 | 1 / 2 / 2 | AMZN 17%, COIN 17%, MSTR 16% |  |
| Breezy | 2026-10-04T17:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T17:05 | 3 / 2 / 0 | MSTR 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.66 | +5.70% | 4 |
| Bollinger reversion · 1h | UPRO | 2.43 | +6.89% | 3 |
| RSI(14) reversion | SQQQ | 2.18 | +4.27% | 5 |
| Bollinger reversion · 1h | SPY | 2.00 | +1.40% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.94 | +3.45% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 102.18 | 2.18 | 0 | — | -7.04 | -1.27 | -15.27 | 2 |
| 2 | Hold BTC | benchmark | 102.06 | 2.06 | 0 | — | 33.32 | 4.08 | -8.68 | 1 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.68 | -5.41 | -26.03 | 494 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 4.95 | 1.42 | -6.57 | 117 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.82 | -3.95 | -17.54 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.77 | -0.23 | 20 | 55.0 | 6.18 | 1.41 | -8.60 | 158 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.41 | 1.01 | -16.96 | 114 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.36 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 45 | 60.0 | -8.07 | -1.66 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.83 | 0.46 | -12.41 | 412 |
| 24 | Trend pullback · 1h | trend | 98.83 | -1.18 | 47 | 21.3 | -21.71 | -5.56 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.94 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.71 | 1.72 | -14.40 | 136 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.51 | -2.49 | 59 | 44.1 | -11.73 | -3.95 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.14 | -3.16 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 1.30 | 0.38 | -12.47 | 359 |
| 37 | Parabolic SAR · 1h | trend | 96.42 | -3.58 | 48 | 16.7 | -5.47 | -0.60 | -19.70 | 303 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.63 | 2.82 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.49 | -1.45 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.93 | -4.07 | 28 | 7.1 | 3.34 | 0.63 | -16.43 | 202 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.79 | -4.21 | 71 | 15.5 | -12.32 | -1.94 | -17.27 | 477 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.60 | -0.61 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.30 | -4.70 | 22 | 18.2 | 19.99 | 2.88 | -8.06 | 117 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.99 | -6.01 | 40 | 2.5 | 1.81 | 0.44 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.31 | -6.69 | 178 | 21.9 | -39.54 | -6.25 | -40.07 | 1282 |
| 50 | Bollinger breakout · 1h | breakout | 93.16 | -6.84 | 38 | 15.8 | 6.36 | 1.01 | -12.06 | 297 |
| 51 | Triple EMA stack · 1h | trend | 93.15 | -6.85 | 50 | 8.0 | -8.09 | -0.79 | -23.88 | 244 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.07 | 0.61 | -12.60 | 128 |
| 54 | EMA 9/21 cross · 1h | trend | 91.80 | -8.20 | 69 | 11.6 | -3.77 | -0.32 | -18.47 | 342 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | MACD zero-line · 1h | trend | 90.95 | -9.05 | 38 | 13.2 | -3.20 | -0.21 | -18.32 | 236 |
| 57 | Donchian 20/10 · 1h | breakout | 90.82 | -9.18 | 31 | 12.9 | 0.02 | 0.22 | -16.18 | 224 |
| 58 | Three white soldiers | momentum | 90.81 | -9.19 | 77 | 14.3 | -49.60 | -26.51 | -49.92 | 593 |
| 59 | Heikin-Ashi · 1h | trend | 90.58 | -9.43 | 94 | 23.4 | -32.45 | -5.73 | -33.92 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.62 | -1.39 | -26.45 | 335 |
| 61 | Keltner breakout · 1h | breakout | 88.28 | -11.72 | 22 | 0.0 | -11.04 | -1.30 | -23.19 | 213 |
| 62 | ROC + volume · 1h | momentum | 87.20 | -12.80 | 84 | 14.3 | -10.16 | -1.26 | -23.16 | 418 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.70 | -20.22 | -70.76 | 1429 |
| 64 | ROC + volume | momentum | 79.32 | -20.68 | 261 | 19.9 | -73.11 | -17.54 | -73.74 | 1659 |
| 65 | Donchian 55/20 | breakout | 79.31 | -20.69 | 193 | 16.6 | -68.71 | -15.60 | -68.75 | 1312 |
| 66 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.99 | -17.26 | -69.99 | 1366 |
| 67 | Squeeze breakout | breakout | 78.77 | -21.23 | 204 | 13.7 | -62.07 | -19.12 | -62.91 | 1232 |
| 68 | Volume breakout | breakout | 77.69 | -22.30 | 173 | 12.7 | -64.29 | -20.16 | -64.29 | 911 |
| 69 | EMA 20/50 cross | trend | 77.61 | -22.39 | 217 | 16.6 | -79.16 | -16.83 | -79.24 | 1489 |
| 70 | Z-score reversion | reversion | 76.00 | -24.00 | 292 | 29.1 | -85.09 | -26.73 | -85.11 | 2091 |
| 71 | MFI reversion | reversion | 73.90 | -26.09 | 288 | 21.2 | -87.66 | -32.75 | -87.71 | 2113 |
| 72 | Supertrend | trend | 72.58 | -27.42 | 294 | 19.0 | -87.45 | -23.55 | -87.50 | 1953 |
| 73 | AI bee: Bizzy | ai | 71.52 | -28.48 | 493 | 8.3 | — | — | — | — |
| 74 | Keltner breakout | breakout | 70.94 | -29.06 | 285 | 11.9 | -85.76 | -33.00 | -85.78 | 1909 |
| 75 | ADX DI cross | trend | 69.68 | -30.32 | 320 | 9.7 | -89.60 | -40.50 | -89.62 | 2111 |
| 76 | Ichimoku | trend | 69.46 | -30.54 | 261 | 8.0 | -82.54 | -25.96 | -82.64 | 1794 |
| 77 | AI bee: Boozy | ai | 67.83 | -32.17 | 197 | 4.1 | — | — | — | — |
| 78 | MACD zero-line | trend | 66.77 | -33.23 | 375 | 15.2 | -92.04 | -33.39 | -92.05 | 2386 |
| 79 | Donchian 20/10 | breakout | 66.74 | -33.26 | 390 | 17.2 | -91.29 | -28.78 | -91.33 | 2701 |
| 80 | RSI momentum | momentum | 65.19 | -34.81 | 370 | 14.3 | -91.00 | -28.32 | -91.01 | 2415 |
| 81 | Trend pullback | trend | 64.76 | -35.24 | 378 | 14.3 | -91.78 | -34.15 | -91.79 | 2376 |
| 82 | Stochastic reversion | reversion | 63.94 | -36.06 | 569 | 23.6 | -95.65 | -40.78 | -95.68 | 4054 |
| 83 | Triple EMA stack | trend | 63.74 | -36.26 | 421 | 14.3 | -93.76 | -34.94 | -93.76 | 2672 |
| 84 | Bollinger reversion | reversion | 63.09 | -36.91 | 536 | 17.0 | -95.68 | -39.87 | -95.68 | 3697 |
| 85 | Bollinger breakout | breakout | 62.94 | -37.06 | 407 | 13.8 | -94.25 | -39.43 | -94.29 | 2871 |
| 86 | Consensus | meta | 61.63 | -38.37 | 371 | 8.6 | -94.30 | -28.22 | -94.30 | 2632 |
| 87 | EMA 9/21 cross | trend | 59.29 | -40.71 | 527 | 16.1 | -97.58 | -38.49 | -97.59 | 3590 |
| 88 | Connors RSI(2) | reversion | 59.21 | -40.79 | 500 | 16.2 | -96.63 | -39.28 | -96.63 | 3659 |
| 89 | Candlestick reversal | reversion | 58.10 | -41.90 | 632 | 15.0 | -99.30 | -44.00 | -99.30 | 5636 |
| 90 | CCI reversion | reversion | 58.07 | -41.93 | 537 | 15.6 | -98.47 | -45.10 | -98.47 | 4725 |
| 91 | OBV trend | momentum | 57.49 | -42.51 | 583 | 13.9 | -96.43 | -44.08 | -96.45 | 3664 |
| 92 | VWAP momentum | momentum | 56.73 | -43.27 | 594 | 8.4 | -98.72 | -34.91 | -98.72 | 5364 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.39 | -47.75 | -97.40 | 3708 |
| 94 | Williams %R | reversion | 53.06 | -46.94 | 670 | 20.0 | -99.50 | -49.98 | -99.50 | 6144 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -54.60 | -99.73 | 6201 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -63.55 | -99.90 | 8365 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T17:00 | Keltner breakout · 1h | buy | DOGE-USD | 7.36 | — | entry signal |
| 2026-10-04T17:00 | Parabolic SAR · 1h | buy | ETH-USD | 6.43 | — | entry signal |
| 2026-10-04T16:57 | AI bee: Boozy | sell | ETH-USD | 23.27 | -0.14 | Jev: sell |
| 2026-10-04T16:55 | CCI reversion | sell | SOL-USD | 14.48 | -0.07 | exit signal |
| 2026-10-04T16:54 | AI bee: Bizzy | sell | ETH-USD | 10.35 | -0.06 | Jev: sell (sell p=0.50) after 10 min |
| 2026-10-04T16:53 | Triple EMA stack | buy | XRP-USD | 3.18 | — | rebalance up |
| 2026-10-04T16:53 | Triple EMA stack | sell | BTC-USD | 3.18 | -0.01 | rebalance down |
| 2026-10-04T16:52 | Triple EMA stack | buy | XRP-USD | 3.18 | — | rebalance up |
| 2026-10-04T16:52 | Triple EMA stack | sell | ETH-USD | 3.18 | -0.01 | rebalance down |
| 2026-10-04T16:50 | Consensus | buy | XRP-USD | 2.97 | — | entry |
| 2026-10-04T16:50 | Williams %R | sell | XRP-USD | 13.26 | -0.06 | exit signal |
| 2026-10-04T16:50 | Williams %R | sell | SOL-USD | 13.28 | -0.05 | exit signal |
| 2026-10-04T16:50 | Williams %R | sell | BTC-USD | 13.27 | -0.05 | exit signal |
| 2026-10-04T16:50 | Keltner breakout | buy | ETH-USD | 17.77 | — | entry signal |
| 2026-10-04T16:50 | Keltner breakout | buy | BTC-USD | 17.77 | — | entry signal |
| 2026-10-04T16:50 | Bollinger breakout | buy | BTC-USD | 15.75 | — | entry signal |
| 2026-10-04T16:50 | Donchian 55/20 | buy | ETH-USD | 19.85 | — | entry signal |
| 2026-10-04T16:50 | Donchian 20/10 | buy | ETH-USD | 16.70 | — | entry signal |
| 2026-10-04T16:50 | RSI momentum | buy | SOL-USD | 16.33 | — | entry signal |
| 2026-10-04T16:50 | RSI momentum | buy | BTC-USD | 16.33 | — | entry signal |
| 2026-10-04T16:50 | Ichimoku | buy | BTC-USD | 17.38 | — | entry signal |
| 2026-10-04T16:50 | Supertrend | buy | BTC-USD | 14.05 | — | entry signal |
| 2026-10-04T16:50 | Supertrend | sell | ETH-USD | 3.64 | -0.01 | rebalance down |
| 2026-10-04T16:50 | MACD zero-line | buy | SOL-USD | 16.71 | — | entry signal |
| 2026-10-04T16:50 | Triple EMA stack | buy | XRP-USD | 6.41 | — | entry signal |
| 2026-10-04T16:50 | Triple EMA stack | buy | SOL-USD | 12.78 | — | entry signal |
| 2026-10-04T16:50 | Triple EMA stack | sell | DOGE-USD | 3.41 | 0.02 | rebalance down |
| 2026-10-04T16:50 | EMA 9/21 cross | buy | XRP-USD | 8.84 | — | entry signal |
| 2026-10-04T16:50 | EMA 9/21 cross | buy | SOL-USD | 11.88 | — | entry signal |
| 2026-10-04T16:50 | EMA 9/21 cross | sell | ETH-USD | 3.02 | -0.01 | rebalance down |
| 2026-10-04T16:45 | Consensus | buy | BTC-USD | 15.41 | — | entry |
| 2026-10-04T16:45 | Squeeze breakout | buy | ETH-USD | 19.70 | — | entry signal |
| 2026-10-04T16:44 | AI bee: Bizzy | buy | ETH-USD | 10.41 | — | Jev: buy (buy p=0.58) |
| 2026-10-04T16:42 | AI bee: Boozy | buy | ETH-USD | 23.41 | — | Jev: buy (buy p=0.68) |
| 2026-10-04T16:40 | MFI reversion | buy | XRP-USD | 18.48 | — | entry signal |
| 2026-10-04T16:40 | Bollinger breakout | buy | ETH-USD | 15.75 | — | entry signal |
| 2026-10-04T16:40 | OBV trend | buy | ETH-USD | 14.38 | — | entry signal |
| 2026-10-04T16:40 | OBV trend | buy | BTC-USD | 14.38 | — | entry signal |
| 2026-10-04T16:40 | RSI momentum | buy | ETH-USD | 16.33 | — | entry signal |
| 2026-10-04T16:35 | Consensus | buy | SOL-USD | 15.43 | — | entry |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
