# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-04T14:05:05.000124+00:00 · 11324 ticks

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

Today: 10559 decisions in 2113 calls, $0.1475 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-04T14:05 | 0 / 3 / 2 | AMZN 17%, COIN 17%, MSTR 16% |  |
| Breezy | 2026-10-04T14:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-04T14:05 | 1 / 4 / 0 | MSTR 65% |  |

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
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 102.05 | 2.05 | 0 | — | 2.82 | 0.86 | -7.93 | 7 |
| 3 | Hold BTC | benchmark | 101.87 | 1.87 | 0 | — | 33.27 | 4.08 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 101.03 | 1.03 | 25 | 36.0 | -9.08 | -2.95 | -14.05 | 112 |
| 5 | Copy: Congress Democrats (NANC) | copy | 100.94 | 0.94 | 0 | — | 4.22 | 1.91 | -3.62 | 1 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.86 | 0.86 | 0 | — | -1.93 | -1.08 | -5.09 | 2 |
| 7 | Candlestick reversal · 1h | reversion | 100.86 | 0.86 | 53 | 37.7 | -23.91 | -5.47 | -26.27 | 497 |
| 8 | RSI(14) reversion · 1h | reversion | 100.62 | 0.62 | 11 | 63.6 | 5.32 | 1.52 | -6.57 | 119 |
| 9 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | 1.92 | 1.14 | -3.66 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Bollinger reversion · 1h | reversion | 99.90 | -0.10 | 41 | 43.9 | -14.83 | -3.95 | -17.55 | 304 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 16 | 37.5 | 3.63 | 1.81 | -1.50 | 85 |
| 14 | Z-score reversion · 1h | reversion | 99.77 | -0.23 | 20 | 55.0 | 5.60 | 1.29 | -8.60 | 160 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -2.21 | -0.85 | -7.65 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 99.66 | -0.34 | 17 | 0.0 | 6.41 | 1.01 | -16.96 | 114 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 99.61 | -0.39 | 0 | — | -2.07 | -0.95 | -5.14 | 1 |
| 18 | Daily: Bullish score | daily | 99.46 | -0.54 | 3 | 0.0 | 1.72 | 0.43 | -12.76 | 14 |
| 19 | Agent | meta | 99.25 | -0.76 | 33 | 66.7 | -9.92 | -6.36 | -11.27 | 214 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 3 | 33.3 | -0.52 | -0.60 | -1.79 | 19 |
| 21 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.23 | -0.77 | 5 | 20.0 | 15.27 | 3.32 | -7.55 | 44 |
| 22 | Stochastic reversion · 1h | reversion | 99.02 | -0.98 | 45 | 60.0 | -8.07 | -1.66 | -9.82 | 327 |
| 23 | CCI reversion · 1h | reversion | 98.89 | -1.11 | 63 | 49.2 | 1.46 | 0.40 | -12.41 | 416 |
| 24 | Trend pullback · 1h | trend | 98.84 | -1.16 | 46 | 19.6 | -21.73 | -5.57 | -25.34 | 157 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 98.73 | -1.27 | 0 | — | 23.08 | 3.44 | -6.29 | 1 |
| 26 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.66 | -1.34 | 3 | 33.3 | -0.66 | -0.20 | -4.88 | 18 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.45 | -3.95 | 25 |
| 28 | Agent (aggressive) | meta | 98.23 | -1.77 | 15 | 53.3 | -0.90 | -0.43 | -4.23 | 100 |
| 29 | Agent (rotation) | meta | 97.92 | -2.08 | 52 | 23.1 | -3.92 | -1.48 | -8.80 | 223 |
| 30 | EMA 20/50 cross · 1h | trend | 97.78 | -2.22 | 25 | 8.0 | 13.58 | 1.70 | -14.40 | 136 |
| 31 | Daily: SMA 20/50 cross · AAPL | daily | 97.76 | -2.24 | 0 | — | 0.26 | 0.19 | -5.18 | 1 |
| 32 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 97.76 | -2.24 | 3 | 33.3 | -3.58 | -1.14 | -9.74 | 23 |
| 33 | Connors RSI(2) · 1h | reversion | 97.57 | -2.43 | 58 | 44.8 | -11.67 | -3.93 | -14.21 | 221 |
| 34 | Williams %R · 1h | reversion | 97.47 | -2.54 | 70 | 54.3 | -17.20 | -3.17 | -19.41 | 495 |
| 35 | Daily: Momentum burst | daily | 96.99 | -3.01 | 3 | 0.0 | -1.05 | 0.02 | -16.91 | 46 |
| 36 | Agent (ML meta-label) | meta | 96.72 | -3.28 | 206 | 17.5 | 4.76 | 0.99 | -11.50 | 368 |
| 37 | Parabolic SAR · 1h | trend | 96.44 | -3.56 | 47 | 17.0 | -5.81 | -0.65 | -19.70 | 304 |
| 38 | Gap and go | momentum | 96.22 | -3.78 | 34 | 8.8 | 11.67 | 2.83 | -4.73 | 199 |
| 39 | MFI reversion · 1h | reversion | 96.19 | -3.81 | 72 | 27.8 | -8.16 | -1.38 | -16.99 | 119 |
| 40 | Max aggression: 1-day momentum | meta | 96.12 | -3.88 | 5 | 40.0 | -25.95 | -1.41 | -40.19 | 42 |
| 41 | Supertrend · 1h | trend | 95.91 | -4.09 | 28 | 7.1 | 3.33 | 0.63 | -16.43 | 200 |
| 42 | Copy: Insider buying | copy | 95.82 | -4.18 | 6 | 50.0 | -18.81 | -3.72 | -21.08 | 73 |
| 43 | MACD cross · 1h | trend | 95.69 | -4.31 | 71 | 15.5 | -12.77 | -2.02 | -17.27 | 478 |
| 44 | ADX DI cross · 1h | trend | 95.67 | -4.33 | 41 | 12.2 | -4.61 | -0.62 | -13.84 | 267 |
| 45 | Squeeze breakout · 1h | breakout | 95.28 | -4.72 | 22 | 18.2 | 20.11 | 2.90 | -8.06 | 115 |
| 46 | Opening range 30m | breakout | 95.09 | -4.91 | 71 | 18.3 | -13.99 | -4.16 | -16.25 | 566 |
| 47 | Ichimoku · 1h | trend | 94.24 | -5.76 | 30 | 16.7 | 6.82 | 0.97 | -16.19 | 125 |
| 48 | RSI momentum · 1h | momentum | 93.98 | -6.01 | 40 | 2.5 | 1.53 | 0.40 | -16.65 | 231 |
| 49 | VWAP momentum · 1h | momentum | 93.29 | -6.71 | 178 | 21.9 | -39.76 | -6.29 | -40.17 | 1282 |
| 50 | Triple EMA stack · 1h | trend | 93.15 | -6.85 | 50 | 8.0 | -8.62 | -0.86 | -23.88 | 244 |
| 51 | Bollinger breakout · 1h | breakout | 93.09 | -6.91 | 38 | 15.8 | 6.24 | 0.99 | -12.06 | 297 |
| 52 | Opening range 15m | breakout | 92.97 | -7.03 | 88 | 17.0 | -16.46 | -4.63 | -19.13 | 696 |
| 53 | Volume breakout · 1h | breakout | 92.48 | -7.52 | 30 | 6.7 | 3.04 | 0.61 | -12.60 | 127 |
| 54 | EMA 9/21 cross · 1h | trend | 91.78 | -8.22 | 69 | 11.6 | -4.43 | -0.41 | -18.47 | 346 |
| 55 | Max aggression: 5-day momentum | meta | 91.29 | -8.71 | 5 | 40.0 | -21.37 | -1.91 | -29.56 | 30 |
| 56 | Three white soldiers | momentum | 90.97 | -9.03 | 76 | 14.5 | -49.57 | -26.46 | -49.83 | 593 |
| 57 | MACD zero-line · 1h | trend | 90.94 | -9.06 | 38 | 13.2 | -3.33 | -0.22 | -18.32 | 236 |
| 58 | Donchian 20/10 · 1h | breakout | 90.72 | -9.28 | 31 | 12.9 | -0.09 | 0.20 | -16.18 | 224 |
| 59 | Heikin-Ashi · 1h | trend | 90.31 | -9.69 | 94 | 23.4 | -32.65 | -5.78 | -33.92 | 688 |
| 60 | OBV trend · 1h | momentum | 89.45 | -10.55 | 97 | 11.3 | -12.26 | -1.34 | -26.45 | 336 |
| 61 | Keltner breakout · 1h | breakout | 88.29 | -11.71 | 22 | 0.0 | -11.12 | -1.31 | -23.19 | 212 |
| 62 | ROC + volume · 1h | momentum | 87.13 | -12.87 | 84 | 14.3 | -10.44 | -1.30 | -23.16 | 418 |
| 63 | RSI(14) reversion | reversion | 86.96 | -13.04 | 182 | 34.1 | -70.71 | -20.23 | -70.77 | 1429 |
| 64 | ROC + volume | momentum | 79.45 | -20.55 | 260 | 20.0 | -73.02 | -17.48 | -73.65 | 1658 |
| 65 | Donchian 55/20 | breakout | 79.40 | -20.60 | 192 | 16.7 | -68.78 | -15.63 | -68.79 | 1311 |
| 66 | VWAP reversion | reversion | 79.24 | -20.76 | 215 | 28.4 | -69.77 | -17.11 | -69.77 | 1361 |
| 67 | Squeeze breakout | breakout | 78.87 | -21.13 | 203 | 13.8 | -62.04 | -19.20 | -62.83 | 1231 |
| 68 | Volume breakout | breakout | 77.69 | -22.30 | 173 | 12.7 | -64.34 | -20.21 | -64.34 | 912 |
| 69 | EMA 20/50 cross | trend | 77.60 | -22.40 | 215 | 16.7 | -79.24 | -16.90 | -79.32 | 1489 |
| 70 | Z-score reversion | reversion | 76.05 | -23.95 | 291 | 29.2 | -85.08 | -26.70 | -85.10 | 2091 |
| 71 | MFI reversion | reversion | 74.01 | -25.99 | 286 | 21.0 | -87.72 | -32.93 | -87.76 | 2109 |
| 72 | Supertrend | trend | 72.53 | -27.47 | 293 | 19.1 | -87.45 | -23.56 | -87.50 | 1951 |
| 73 | AI bee: Bizzy | ai | 71.84 | -28.16 | 488 | 8.4 | — | — | — | — |
| 74 | Keltner breakout | breakout | 71.38 | -28.61 | 282 | 12.1 | -85.66 | -32.94 | -85.68 | 1903 |
| 75 | Ichimoku | trend | 69.87 | -30.13 | 257 | 8.2 | -82.58 | -26.35 | -82.63 | 1794 |
| 76 | ADX DI cross | trend | 69.70 | -30.30 | 320 | 9.7 | -89.57 | -40.31 | -89.57 | 2109 |
| 77 | AI bee: Boozy | ai | 68.28 | -31.72 | 194 | 4.1 | — | — | — | — |
| 78 | MACD zero-line | trend | 67.30 | -32.70 | 370 | 15.4 | -92.03 | -33.45 | -92.04 | 2386 |
| 79 | Donchian 20/10 | breakout | 67.20 | -32.80 | 386 | 17.4 | -91.26 | -28.81 | -91.29 | 2697 |
| 80 | RSI momentum | momentum | 65.67 | -34.33 | 365 | 14.5 | -91.00 | -28.37 | -91.00 | 2413 |
| 81 | Trend pullback | trend | 65.53 | -34.47 | 370 | 14.6 | -91.68 | -34.03 | -91.68 | 2366 |
| 82 | Triple EMA stack | trend | 64.58 | -35.42 | 413 | 14.5 | -93.75 | -35.17 | -93.75 | 2672 |
| 83 | Stochastic reversion | reversion | 64.03 | -35.97 | 566 | 23.7 | -95.65 | -40.80 | -95.68 | 4055 |
| 84 | Bollinger breakout | breakout | 63.54 | -36.46 | 402 | 13.9 | -94.21 | -39.51 | -94.23 | 2868 |
| 85 | Bollinger reversion | reversion | 63.09 | -36.91 | 536 | 17.0 | -95.68 | -39.93 | -95.68 | 3698 |
| 86 | Consensus | meta | 62.56 | -37.44 | 361 | 8.6 | -94.28 | -28.41 | -94.28 | 2626 |
| 87 | Connors RSI(2) | reversion | 59.99 | -40.01 | 490 | 16.5 | -96.58 | -39.11 | -96.58 | 3649 |
| 88 | EMA 9/21 cross | trend | 59.89 | -40.11 | 520 | 16.3 | -97.57 | -38.58 | -97.58 | 3589 |
| 89 | Candlestick reversal | reversion | 58.66 | -41.34 | 626 | 15.2 | -99.30 | -43.69 | -99.30 | 5632 |
| 90 | CCI reversion | reversion | 58.23 | -41.77 | 534 | 15.7 | -98.47 | -45.13 | -98.47 | 4727 |
| 91 | OBV trend | momentum | 58.11 | -41.89 | 575 | 13.9 | -96.42 | -44.61 | -96.43 | 3664 |
| 92 | VWAP momentum | momentum | 56.76 | -43.24 | 591 | 8.5 | -98.71 | -34.85 | -98.72 | 5367 |
| 93 | Parabolic SAR ⏸ | trend | 54.05 | -45.95 | 551 | 12.9 | -97.39 | -49.12 | -97.40 | 3705 |
| 94 | Williams %R | reversion | 53.48 | -46.52 | 661 | 20.3 | -99.50 | -49.88 | -99.50 | 6143 |
| 95 | MACD cross ⏸ | trend | 52.32 | -47.69 | 629 | 12.9 | -99.73 | -54.96 | -99.73 | 6203 |
| 96 | Heikin-Ashi ⏸ | trend | 51.40 | -48.60 | 586 | 8.5 | -99.90 | -63.83 | -99.90 | 8361 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-04T14:05 | Consensus | sell | XRP-USD | 15.61 | -0.10 | target is flat |
| 2026-10-04T14:05 | Candlestick reversal | sell | ETH-USD | 14.60 | -0.09 | exit signal |
| 2026-10-04T14:05 | Squeeze breakout | sell | XRP-USD | 19.62 | -0.16 | exit signal |
| 2026-10-04T14:05 | Bollinger breakout | sell | XRP-USD | 15.79 | -0.13 | exit signal |
| 2026-10-04T14:00 | AI bee: Bizzy | sell | DOGE-USD | 10.08 | -0.07 | Jev: sell (sell p=0.82) after 10 min |
| 2026-10-04T14:00 | ROC + volume · 1h | buy | DOGE-USD | 6.70 | — | entry signal |
| 2026-10-04T14:00 | Ichimoku | sell | XRP-USD | 17.40 | -0.13 | exit signal |
| 2026-10-04T14:00 | Ichimoku | sell | DOGE-USD | 17.40 | -0.12 | exit signal |
| 2026-10-04T14:00 | MACD zero-line | buy | BTC-USD | 16.84 | — | entry signal |
| 2026-10-04T13:50 | AI bee: Bizzy | buy | DOGE-USD | 10.15 | — | Jev: buy (buy p=0.56) |
| 2026-10-04T13:50 | Consensus | buy | ETH-USD | 15.61 | — | entry |
| 2026-10-04T13:50 | MFI reversion | buy | ETH-USD | 18.52 | — | entry signal |
| 2026-10-04T13:50 | Williams %R | sell | BTC-USD | 13.34 | -0.06 | exit signal |
| 2026-10-04T13:50 | Stochastic reversion | sell | BTC-USD | 16.00 | -0.07 | exit signal |
| 2026-10-04T13:50 | Squeeze breakout | buy | SOL-USD | 19.76 | — | entry signal |
| 2026-10-04T13:50 | Ichimoku | buy | DOGE-USD | 17.52 | — | entry signal |
| 2026-10-04T13:50 | Supertrend | buy | BTC-USD | 18.16 | — | entry signal |
| 2026-10-04T13:50 | Triple EMA stack | buy | BTC-USD | 16.18 | — | entry signal |
| 2026-10-04T13:50 | EMA 9/21 cross | buy | BTC-USD | 15.00 | — | entry signal |
| 2026-10-04T13:49 | AI bee: Boozy | sell | SOL-USD | 23.72 | -0.15 | Jev: buy |
| 2026-10-04T13:45 | Consensus | sell | ETH-USD | 15.61 | -0.10 | target is flat |
| 2026-10-04T13:40 | CCI reversion | sell | DOGE-USD | 14.54 | -0.06 | exit signal |
| 2026-10-04T13:40 | Candlestick reversal | sell | XRP-USD | 14.66 | -0.04 | take-profit |
| 2026-10-04T13:40 | Squeeze breakout | buy | XRP-USD | 19.78 | — | entry signal |
| 2026-10-04T13:40 | Bollinger breakout | buy | XRP-USD | 15.92 | — | entry signal |
| 2026-10-04T13:40 | Donchian 20/10 | buy | XRP-USD | 16.82 | — | entry signal |
| 2026-10-04T13:40 | Ichimoku | buy | XRP-USD | 17.53 | — | entry signal |
| 2026-10-04T13:35 | Williams %R | sell | XRP-USD | 13.36 | -0.05 | exit signal |
| 2026-10-04T13:35 | Bollinger reversion | sell | BTC-USD | 15.74 | -0.07 | exit signal |
| 2026-10-04T13:35 | Bollinger breakout | buy | SOL-USD | 15.93 | — | entry signal |
| 2026-10-04T13:35 | RSI momentum | buy | XRP-USD | 16.44 | — | entry signal |
| 2026-10-04T13:35 | Ichimoku | buy | SOL-USD | 17.54 | — | entry signal |
| 2026-10-04T13:33 | AI bee: Boozy | buy | SOL-USD | 23.87 | — | Jev: buy (buy p=0.69) |
| 2026-10-04T13:30 | Consensus | buy | BTC-USD | 15.20 | — | entry |
| 2026-10-04T13:30 | CCI reversion | sell | XRP-USD | 14.55 | -0.06 | exit signal |
| 2026-10-04T13:30 | Stochastic reversion | sell | SOL-USD | 15.98 | -0.06 | exit signal |
| 2026-10-04T13:30 | Bollinger reversion | sell | ETH-USD | 15.72 | -0.08 | exit signal |
| 2026-10-04T13:30 | OBV trend | buy | XRP-USD | 14.54 | — | entry signal |
| 2026-10-04T13:30 | Trend pullback | buy | BTC-USD | 16.39 | — | entry signal |
| 2026-10-04T13:30 | Triple EMA stack | buy | DOGE-USD | 16.17 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
