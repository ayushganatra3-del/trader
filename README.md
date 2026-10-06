# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T01:00:05.000126+00:00 · 12927 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.68 (-1.32%)

Closed trades 35, win rate 62.9%, fees £1.21, max drawdown -1.91%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| DOGE-USD | 19.87 | +0.10 |
| SQQQ | 19.76 | +0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-05 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PAM 12%, GPUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-05)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.70 · VIX 15.52 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.8, AMD 7.6, TECL 7.6, MSTR 7.5, BITX 7.5, ETHU 7.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 870 decisions in 174 calls, $0.0122 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T01:00 | 1 / 3 / 1 | ETH-USD 14%, NANC 19%, MSTR 14% |  |
| Breezy | 2026-10-06T01:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-06T01:00 | 2 / 3 / 0 | ETH-USD 32% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion | AMZN | 1.94 | +0.87% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.03 | 5.03 | 0 | — | -4.61 | -0.74 | -15.27 | 2 |
| 2 | Hold BTC | benchmark | 102.85 | 2.85 | 0 | — | 33.01 | 3.97 | -8.68 | 1 |
| 3 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -7.74 | -2.39 | -14.05 | 114 |
| 4 | Copy: Cathie Wood (ARKK) | copy | 102.26 | 2.26 | 0 | — | 20.41 | 3.10 | -6.29 | 1 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 101.93 | 1.93 | 0 | — | -1.06 | -0.55 | -5.09 | 2 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 7 | Daily: Bullish score | daily | 101.63 | 1.63 | 3 | 0.0 | 4.13 | 0.74 | -12.76 | 12 |
| 8 | Copy: Congress Democrats (NANC) | copy | 101.48 | 1.48 | 0 | — | 2.00 | 0.99 | -3.62 | 1 |
| 9 | Hold SPY | benchmark | 100.95 | 0.95 | 0 | — | -0.01 | 0.04 | -3.66 | 1 |
| 10 | Candlestick reversal · 1h | reversion | 100.89 | 0.89 | 57 | 36.8 | -19.29 | -4.30 | -21.38 | 491 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.87 | 0.87 | 5 | 20.0 | 5.86 | 1.77 | -7.55 | 43 |
| 12 | Donchian 55/20 · 1h | breakout | 100.84 | 0.84 | 17 | 0.0 | 7.58 | 1.12 | -16.96 | 113 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 100.59 | 0.59 | 0 | — | -1.80 | -0.82 | -5.14 | 1 |
| 14 | Stochastic reversion · 1h | reversion | 100.46 | 0.46 | 50 | 62.0 | -8.70 | -1.80 | -11.62 | 327 |
| 15 | Bollinger reversion · 1h | reversion | 100.41 | 0.41 | 47 | 48.9 | -14.58 | -3.77 | -17.61 | 305 |
| 16 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.32 | 0.33 | 3 | 33.3 | 1.82 | 0.77 | -4.03 | 18 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 100.26 | 0.26 | 20 | 35.0 | 4.57 | 2.20 | -1.46 | 86 |
| 18 | Copy: Warren Buffett (BRK-B) | copy | 100.18 | 0.18 | 0 | — | -2.43 | -0.94 | -7.65 | 1 |
| 19 | Connors RSI(2) · 1h | reversion | 100.04 | 0.04 | 69 | 46.4 | -12.63 | -4.36 | -16.82 | 219 |
| 20 | RSI(14) reversion · 1h | reversion | 100.00 | 0.00 | 11 | 63.6 | 6.61 | 1.77 | -6.57 | 123 |
| 21 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 22 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 23 | Z-score reversion · 1h | reversion | 99.84 | -0.16 | 21 | 52.4 | 7.28 | 1.62 | -8.60 | 151 |
| 24 | EMA 20/50 cross · 1h | trend | 99.66 | -0.34 | 28 | 7.1 | 12.60 | 1.59 | -15.34 | 142 |
| 25 | Trend pullback · 1h | trend | 99.58 | -0.42 | 59 | 27.1 | -19.39 | -5.56 | -23.14 | 168 |
| 26 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.03 | -0.97 | 3 | 33.3 | -0.77 | -0.84 | -2.30 | 20 |
| 27 | CCI reversion · 1h | reversion | 99.01 | -0.98 | 66 | 48.5 | 1.50 | 0.40 | -12.41 | 410 |
| 28 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 98.96 | -1.04 | 3 | 33.3 | -6.13 | -2.16 | -9.74 | 24 |
| 29 | Williams %R · 1h | reversion | 98.93 | -1.07 | 76 | 55.3 | -18.98 | -3.53 | -21.09 | 499 |
| 30 | Copy: Insider buying | copy | 98.69 | -1.31 | 9 | 55.6 | -16.81 | -3.09 | -21.08 | 73 |
| 31 | Agent | meta | 98.68 | -1.32 | 35 | 62.9 | -9.21 | -6.01 | -9.84 | 227 |
| 32 | Agent (aggressive) | meta | 98.49 | -1.51 | 15 | 53.3 | 0.76 | 0.44 | -4.23 | 101 |
| 33 | Daily: Momentum burst | daily | 98.45 | -1.55 | 3 | 0.0 | -0.20 | 0.15 | -16.91 | 44 |
| 34 | Agent (rotation) | meta | 98.42 | -1.58 | 56 | 25.0 | 1.81 | 0.59 | -9.09 | 268 |
| 35 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 36 | Daily: SMA 20/50 cross · AAPL | daily | 97.73 | -2.27 | 0 | — | -0.30 | -0.03 | -5.18 | 1 |
| 37 | Agent (ML meta-label) | meta | 97.65 | -2.35 | 223 | 16.1 | -0.83 | 0.02 | -12.41 | 377 |
| 38 | ADX DI cross · 1h | trend | 97.38 | -2.62 | 41 | 12.2 | -2.84 | -0.33 | -13.84 | 260 |
| 39 | Supertrend · 1h | trend | 96.81 | -3.19 | 32 | 9.4 | 1.28 | 0.36 | -16.43 | 207 |
| 40 | Parabolic SAR · 1h | trend | 96.81 | -3.19 | 59 | 16.9 | -3.66 | -0.30 | -19.61 | 295 |
| 41 | MACD cross · 1h | trend | 96.38 | -3.62 | 81 | 19.8 | -7.45 | -1.01 | -17.27 | 473 |
| 42 | Squeeze breakout · 1h | breakout | 95.38 | -4.62 | 27 | 22.2 | 14.85 | 2.50 | -8.06 | 106 |
| 43 | RSI momentum · 1h | momentum | 95.37 | -4.63 | 45 | 2.2 | 1.01 | 0.33 | -16.65 | 224 |
| 44 | MFI reversion · 1h | reversion | 95.12 | -4.88 | 73 | 27.4 | -10.25 | -1.78 | -16.99 | 120 |
| 45 | Gap and go | momentum | 95.03 | -4.97 | 39 | 7.7 | 7.56 | 1.97 | -5.79 | 192 |
| 46 | Ichimoku · 1h | trend | 94.93 | -5.07 | 31 | 16.1 | 7.80 | 1.10 | -15.84 | 120 |
| 47 | Opening range 30m | breakout | 94.57 | -5.43 | 76 | 17.1 | -14.93 | -4.43 | -17.14 | 556 |
| 48 | Max aggression: 1-day momentum | meta | 94.57 | -5.43 | 6 | 33.3 | -27.72 | -1.54 | -39.72 | 42 |
| 49 | Triple EMA stack · 1h | trend | 94.39 | -5.62 | 56 | 10.7 | -7.96 | -0.79 | -24.00 | 250 |
| 50 | Bollinger breakout · 1h | breakout | 94.25 | -5.75 | 46 | 26.1 | 5.24 | 0.85 | -12.06 | 293 |
| 51 | Volume breakout · 1h | breakout | 93.56 | -6.44 | 32 | 9.4 | 5.32 | 0.91 | -12.60 | 130 |
| 52 | Opening range 15m | breakout | 92.91 | -7.09 | 93 | 16.1 | -17.69 | -5.23 | -18.88 | 677 |
| 53 | EMA 9/21 cross · 1h | trend | 92.72 | -7.28 | 76 | 11.8 | -2.10 | -0.09 | -18.47 | 341 |
| 54 | VWAP momentum · 1h | momentum | 91.90 | -8.10 | 195 | 22.1 | -38.49 | -5.96 | -38.94 | 1278 |
| 55 | MACD zero-line · 1h | trend | 91.87 | -8.13 | 43 | 18.6 | -1.33 | 0.02 | -18.32 | 244 |
| 56 | Max aggression: 5-day momentum | meta | 91.78 | -8.22 | 5 | 40.0 | -21.08 | -1.85 | -29.56 | 30 |
| 57 | Donchian 20/10 · 1h | breakout | 91.50 | -8.50 | 36 | 16.7 | 0.71 | 0.30 | -16.18 | 221 |
| 58 | Heikin-Ashi · 1h | trend | 90.55 | -9.45 | 102 | 24.5 | -31.76 | -5.50 | -34.14 | 704 |
| 59 | Three white soldiers | momentum | 90.36 | -9.64 | 91 | 18.7 | -49.64 | -25.57 | -49.68 | 586 |
| 60 | OBV trend · 1h | momentum | 90.36 | -9.64 | 102 | 10.8 | -12.53 | -1.38 | -26.78 | 332 |
| 61 | Keltner breakout · 1h | breakout | 89.03 | -10.97 | 30 | 6.7 | -13.86 | -1.67 | -23.31 | 228 |
| 62 | ROC + volume · 1h | momentum | 87.72 | -12.28 | 98 | 15.3 | -11.27 | -1.41 | -23.18 | 416 |
| 63 | RSI(14) reversion | reversion | 85.84 | -14.16 | 203 | 32.5 | -70.64 | -19.54 | -70.70 | 1418 |
| 64 | VWAP reversion | reversion | 78.68 | -21.32 | 240 | 29.6 | -69.35 | -16.39 | -69.62 | 1361 |
| 65 | Squeeze breakout | breakout | 78.04 | -21.96 | 229 | 14.0 | -62.42 | -19.05 | -62.42 | 1231 |
| 66 | Donchian 55/20 | breakout | 77.01 | -22.99 | 222 | 15.8 | -69.01 | -15.36 | -69.04 | 1298 |
| 67 | ROC + volume | momentum | 76.72 | -23.28 | 295 | 19.3 | -74.19 | -18.00 | -74.19 | 1656 |
| 68 | EMA 20/50 cross | trend | 75.61 | -24.39 | 243 | 16.9 | -78.78 | -16.28 | -78.99 | 1493 |
| 69 | Volume breakout | breakout | 74.47 | -25.53 | 200 | 12.0 | -65.00 | -19.51 | -65.00 | 926 |
| 70 | Z-score reversion | reversion | 74.13 | -25.87 | 323 | 28.8 | -84.77 | -25.14 | -84.78 | 2053 |
| 71 | MFI reversion | reversion | 71.83 | -28.17 | 317 | 21.5 | -87.07 | -30.71 | -87.09 | 2090 |
| 72 | Supertrend | trend | 71.62 | -28.38 | 320 | 19.4 | -87.00 | -22.45 | -87.13 | 1930 |
| 73 | AI bee: Bizzy | ai | 68.83 | -31.17 | 565 | 8.7 | — | — | — | — |
| 74 | Keltner breakout | breakout | 68.52 | -31.48 | 321 | 11.5 | -85.59 | -30.68 | -85.59 | 1889 |
| 75 | AI bee: Boozy | ai | 67.46 | -32.54 | 209 | 3.8 | — | — | — | — |
| 76 | Ichimoku | trend | 67.35 | -32.65 | 291 | 7.9 | -82.52 | -24.95 | -82.52 | 1764 |
| 77 | ADX DI cross | trend | 67.12 | -32.88 | 352 | 9.4 | -89.58 | -37.27 | -89.59 | 2100 |
| 78 | MACD zero-line | trend | 65.04 | -34.96 | 412 | 15.5 | -91.69 | -31.36 | -91.69 | 2377 |
| 79 | Donchian 20/10 | breakout | 64.14 | -35.86 | 436 | 17.0 | -91.26 | -27.76 | -91.26 | 2669 |
| 80 | RSI momentum | momentum | 62.95 | -37.05 | 408 | 13.5 | -90.70 | -27.08 | -90.71 | 2384 |
| 81 | Triple EMA stack | trend | 61.40 | -38.60 | 463 | 14.0 | -93.35 | -32.74 | -93.35 | 2637 |
| 82 | Trend pullback | trend | 61.40 | -38.60 | 437 | 15.3 | -91.47 | -31.43 | -91.47 | 2346 |
| 83 | Bollinger breakout | breakout | 60.63 | -39.37 | 454 | 13.2 | -94.07 | -35.88 | -94.07 | 2836 |
| 84 | Stochastic reversion | reversion | 59.93 | -40.07 | 648 | 23.0 | -95.59 | -37.50 | -95.59 | 4038 |
| 85 | Bollinger reversion | reversion | 59.60 | -40.40 | 596 | 17.6 | -95.65 | -36.59 | -95.65 | 3668 |
| 86 | Consensus | meta | 58.28 | -41.72 | 423 | 8.3 | -94.51 | -26.58 | -94.51 | 2665 |
| 87 | EMA 9/21 cross | trend | 56.83 | -43.17 | 574 | 15.3 | -97.46 | -35.72 | -97.46 | 3562 |
| 88 | Connors RSI(2) | reversion | 56.05 | -43.95 | 585 | 18.8 | -96.61 | -35.96 | -96.61 | 3625 |
| 89 | CCI reversion | reversion | 54.57 | -45.43 | 613 | 16.8 | -98.43 | -40.42 | -98.43 | 4682 |
| 90 | Candlestick reversal | reversion | 53.82 | -46.18 | 699 | 14.4 | -99.28 | -39.90 | -99.28 | 5605 |
| 91 | OBV trend | momentum | 53.49 | -46.51 | 662 | 13.7 | -96.44 | -40.67 | -96.44 | 3628 |
| 92 | VWAP momentum | momentum | 52.80 | -47.20 | 643 | 8.6 | -98.72 | -32.51 | -98.72 | 5326 |
| 93 | Parabolic SAR | trend | 51.66 | -48.34 | 609 | 14.1 | -97.40 | -42.66 | -97.40 | 3682 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -47.36 | -99.73 | 6151 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -44.20 | -99.50 | 6093 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.70 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T01:00 | AI bee: Bizzy | sell | SOL-USD | 9.83 | -0.05 | Jev: sell (sell p=0.71) after 11 min |
| 2026-10-06T01:00 | Agent (rotation) | sell | BTC-USD | 8.17 | -0.04 | rebalance down |
| 2026-10-06T01:00 | VWAP reversion · 1h | sell | BTC-USD | 25.63 | 0.03 | exit signal |
| 2026-10-06T01:00 | CCI reversion | buy | DOGE-USD | 13.66 | — | entry signal |
| 2026-10-06T01:00 | CCI reversion | sell | ETH-USD | 13.64 | -0.06 | exit signal |
| 2026-10-06T01:00 | Volume breakout | buy | ETH-USD | 18.48 | — | entry signal |
| 2026-10-06T01:00 | Squeeze breakout | buy | ETH-USD | 16.46 | — | entry signal |
| 2026-10-06T01:00 | Bollinger breakout | buy | ETH-USD | 10.01 | — | entry signal |
| 2026-10-06T01:00 | Donchian 20/10 | buy | ETH-USD | 11.17 | — | entry signal |
| 2026-10-06T01:00 | RSI momentum | buy | ETH-USD | 12.91 | — | entry signal |
| 2026-10-06T01:00 | VWAP momentum | buy | DOGE-USD | 2.68 | — | entry signal |
| 2026-10-06T01:00 | VWAP momentum | sell | ETH-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-06T01:00 | MACD zero-line | buy | ETH-USD | 1.40 | — | entry signal |
| 2026-10-06T00:58 | AI bee: Bizzy | buy | ETH-USD | 9.68 | — | Jev: buy (buy p=0.56) |
| 2026-10-06T00:55 | AI bee: Boozy | buy | ETH-USD | 21.53 | — | Jev: buy (buy p=0.69) |
| 2026-10-06T00:55 | Stochastic reversion | sell | ETH-USD | 14.90 | -0.09 | exit signal |
| 2026-10-06T00:55 | Stochastic reversion | sell | DOGE-USD | 14.76 | -0.08 | target is flat |
| 2026-10-06T00:55 | VWAP momentum | buy | XRP-USD | 13.22 | — | entry signal |
| 2026-10-06T00:55 | VWAP momentum | buy | BTC-USD | 13.22 | — | entry signal |
| 2026-10-06T00:50 | CCI reversion | sell | SOL-USD | 10.98 | -0.05 | exit signal |
| 2026-10-06T00:50 | Stochastic reversion | buy | DOGE-USD | 14.84 | — | entry signal |
| 2026-10-06T00:50 | Z-score reversion | buy | DOGE-USD | 18.54 | — | entry signal |
| 2026-10-06T00:50 | VWAP momentum | buy | SOL-USD | 13.23 | — | entry signal |
| 2026-10-06T00:50 | VWAP momentum | buy | ETH-USD | 13.23 | — | entry signal |
| 2026-10-06T00:50 | MACD zero-line | buy | SOL-USD | 16.27 | — | entry signal |
| 2026-10-06T00:50 | Triple EMA stack | buy | SOL-USD | 8.22 | — | entry signal |
| 2026-10-06T00:50 | EMA 9/21 cross | buy | SOL-USD | 6.38 | — | entry signal |
| 2026-10-06T00:49 | AI bee: Bizzy | buy | SOL-USD | 9.88 | — | Jev: buy (buy p=0.57) |
| 2026-10-06T00:45 | Z-score reversion | sell | DOGE-USD | 18.41 | -0.17 | target is flat |
| 2026-10-06T00:40 | MACD zero-line | sell | SOL-USD | 16.18 | -0.13 | exit signal |
| 2026-10-06T00:35 | CCI reversion | buy | ETH-USD | 5.52 | — | rebalance up |
| 2026-10-06T00:35 | CCI reversion | sell | DOGE-USD | 10.90 | -0.09 | target is flat |
| 2026-10-06T00:35 | Stochastic reversion | sell | DOGE-USD | 14.84 | -0.12 | target is flat |
| 2026-10-06T00:35 | Candlestick reversal | sell | DOGE-USD | 13.38 | -0.11 | target is flat |
| 2026-10-06T00:35 | VWAP momentum | sell | XRP-USD | 10.64 | -0.07 | exit signal |
| 2026-10-06T00:35 | VWAP momentum | sell | ETH-USD | 10.60 | -0.07 | exit signal |
| 2026-10-06T00:31 | AI bee: Bizzy | sell | XRP-USD | 9.71 | -0.07 | Jev: sell (sell p=0.79) after 11 min |
| 2026-10-06T00:30 | VWAP momentum | sell | SOL-USD | 13.23 | -0.09 | exit signal |
| 2026-10-06T00:30 | VWAP momentum | sell | DOGE-USD | 5.23 | -0.04 | exit signal |
| 2026-10-06T00:30 | VWAP momentum | sell | BTC-USD | 13.23 | -0.09 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 01:00:05.000126+00:00 -> 2026-10-06 01:10:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
