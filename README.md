# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T03:40:05.000172+00:00 · 5265 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.98 (-0.02%)

Closed trades 17, win rate 70.6%, fees £0.52, max drawdown -1.39%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-28 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-28)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.13 · VIX 16.07 · last follow-through day 2026-08-04

Best bullish scores: MSTR 8.5, BITX 8.5, PLTR 8.5, ETHU 8.5, META 7.9, COIN 7.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 2800 decisions in 560 calls, $0.0393 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T03:40 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-09-29T03:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T03:40 | 3 / 2 / 0 | SOL-USD 30%, ETH-USD 28% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| CCI reversion | AMD | 2.04 | +3.07% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.36 | 1.36 | 1 | 100.0 | 12.70 | 2.77 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.70 | -0.30 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.69 | -0.31 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | RSI(14) reversion · 1h | reversion | 99.41 | -0.59 | 2 | 100.0 | 14.62 | 3.07 | -6.57 | 136 |
| 14 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 15 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 16 | Hold BTC | benchmark | 99.25 | -0.75 | 0 | — | 29.91 | 3.76 | -8.68 | 1 |
| 17 | Daily: Bullish score | daily | 99.19 | -0.81 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -3.36 | -2.74 | -5.16 | 28 |
| 19 | Connors RSI(2) · 1h | reversion | 99.06 | -0.94 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.04 | -0.96 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 99.03 | -0.97 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.93 | -1.07 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Stochastic reversion · 1h | reversion | 98.75 | -1.25 | 23 | 56.5 | -12.61 | -2.80 | -13.86 | 323 |
| 24 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 25 | Copy: Insider buying | copy | 98.53 | -1.47 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 26 | Williams %R · 1h | reversion | 98.46 | -1.53 | 30 | 50.0 | -18.48 | -3.41 | -20.04 | 488 |
| 27 | Z-score reversion · 1h | reversion | 98.46 | -1.54 | 4 | 25.0 | 3.23 | 0.82 | -8.60 | 155 |
| 28 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.88 | -2.76 | -11.75 | 233 |
| 29 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 30 | CCI reversion · 1h | reversion | 98.30 | -1.70 | 24 | 33.3 | 1.35 | 0.39 | -12.41 | 404 |
| 31 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.03 | -1.97 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.01 | -1.99 | 7 | 14.3 | 16.09 | 2.83 | -6.26 | 94 |
| 34 | Candlestick reversal · 1h | reversion | 97.95 | -2.05 | 12 | 16.7 | -25.20 | -5.95 | -25.98 | 484 |
| 35 | EMA 20/50 cross · 1h | trend | 97.85 | -2.15 | 8 | 12.5 | 15.67 | 1.87 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.69 | -2.31 | 11 | 9.1 | 4.74 | 0.83 | -16.43 | 195 |
| 37 | Bollinger reversion · 1h | reversion | 97.28 | -2.72 | 19 | 31.6 | -17.70 | -4.92 | -17.79 | 306 |
| 38 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 39 | Donchian 55/20 · 1h | breakout | 97.20 | -2.81 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.10 | -2.90 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.03 | -2.97 | 79 | 10.1 | 5.11 | 1.04 | -10.50 | 400 |
| 42 | Trend pullback · 1h | trend | 97.03 | -2.97 | 22 | 13.6 | -25.41 | -6.70 | -26.16 | 149 |
| 43 | Parabolic SAR · 1h | trend | 96.91 | -3.09 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 44 | MACD cross · 1h | trend | 96.84 | -3.16 | 31 | 9.7 | -16.50 | -2.80 | -20.79 | 455 |
| 45 | Bollinger breakout · 1h | breakout | 96.83 | -3.17 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 46 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.49 | -0.30 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.43 | -3.57 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 95.96 | -4.04 | 24 | 8.3 | -3.20 | -0.17 | -22.95 | 224 |
| 49 | Ichimoku · 1h | trend | 95.92 | -4.08 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 50 | EMA 9/21 cross · 1h | trend | 95.86 | -4.14 | 34 | 11.8 | 3.09 | 0.62 | -16.92 | 311 |
| 51 | ADX DI cross · 1h | trend | 95.84 | -4.16 | 25 | 8.0 | -11.80 | -2.22 | -15.42 | 249 |
| 52 | Three white soldiers | momentum | 95.78 | -4.22 | 34 | 11.8 | -51.85 | -28.47 | -51.85 | 621 |
| 53 | Donchian 20/10 · 1h | breakout | 95.78 | -4.22 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 54 | Max aggression: 1-day momentum | meta | 95.52 | -4.48 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | MFI reversion · 1h | reversion | 95.48 | -4.52 | 38 | 13.2 | -9.43 | -1.73 | -17.20 | 125 |
| 56 | OBV trend · 1h | momentum | 95.42 | -4.58 | 47 | 6.4 | -9.40 | -0.97 | -25.24 | 317 |
| 57 | Volume breakout · 1h | breakout | 95.16 | -4.84 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.11 | -4.89 | 7 | 0.0 | -0.48 | 0.14 | -18.68 | 221 |
| 59 | VWAP momentum · 1h | momentum | 95.03 | -4.97 | 82 | 7.3 | -33.37 | -4.97 | -33.96 | 1250 |
| 60 | Max aggression: 5-day momentum | meta | 95.02 | -4.98 | 1 | 0.0 | -1.42 | 0.23 | -29.56 | 29 |
| 61 | Heikin-Ashi · 1h | trend | 94.31 | -5.69 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | ROC + volume · 1h | momentum | 91.85 | -8.15 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.17 | -21.95 | -71.26 | 1473 |
| 64 | Squeeze breakout | breakout | 90.22 | -9.78 | 66 | 6.1 | -59.93 | -18.72 | -59.99 | 1182 |
| 65 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.92 | -17.85 | -72.35 | 1655 |
| 66 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.56 | -20.50 | -62.56 | 908 |
| 67 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.58 | -15.93 | -68.58 | 1327 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.48 | -26.30 | -80.48 | 1755 |
| 71 | EMA 20/50 cross | trend | 87.61 | -12.39 | 95 | 13.7 | -78.98 | -17.85 | -79.11 | 1483 |
| 72 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.95 | -35.04 | -84.95 | 1928 |
| 73 | Z-score reversion | reversion | 85.71 | -14.29 | 149 | 29.5 | -84.73 | -28.58 | -84.80 | 2089 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -70.38 | -16.49 | -71.75 | 1404 |
| 75 | MACD zero-line | trend | 84.39 | -15.61 | 154 | 15.6 | -91.53 | -35.91 | -91.70 | 2364 |
| 76 | Supertrend | trend | 83.97 | -16.03 | 142 | 15.5 | -87.33 | -24.88 | -87.40 | 1959 |
| 77 | RSI momentum | momentum | 83.85 | -16.15 | 145 | 11.0 | -90.44 | -30.06 | -90.44 | 2401 |
| 78 | Bollinger breakout | breakout | 83.83 | -16.17 | 158 | 14.6 | -93.95 | -42.19 | -93.96 | 2877 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.52 | -33.58 | -90.52 | 2282 |
| 80 | Triple EMA stack | trend | 82.99 | -17.01 | 169 | 13.6 | -93.08 | -37.12 | -93.08 | 2628 |
| 81 | Donchian 20/10 | breakout | 82.48 | -17.52 | 159 | 15.1 | -90.99 | -30.41 | -90.99 | 2690 |
| 82 | MFI reversion | reversion | 82.09 | -17.91 | 152 | 16.4 | -87.80 | -34.96 | -87.92 | 2169 |
| 83 | ADX DI cross | trend | 82.04 | -17.96 | 160 | 6.9 | -89.40 | -48.08 | -89.41 | 2130 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.36 | -40.96 | -96.36 | 3648 |
| 85 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.71 | -30.28 | -94.71 | 2658 |
| 86 | Candlestick reversal | reversion | 78.95 | -21.05 | 198 | 14.1 | -99.36 | -52.98 | -99.36 | 5566 |
| 87 | EMA 9/21 cross | trend | 78.59 | -21.41 | 221 | 13.6 | -97.41 | -42.98 | -97.42 | 3547 |
| 88 | OBV trend | momentum | 78.46 | -21.54 | 220 | 12.7 | -95.87 | -50.79 | -95.87 | 3564 |
| 89 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.94 | -49.07 | -95.95 | 4057 |
| 90 | Bollinger reversion | reversion | 77.28 | -22.72 | 243 | 12.8 | -95.81 | -46.82 | -95.81 | 3678 |
| 91 | Parabolic SAR | trend | 76.63 | -23.37 | 229 | 12.2 | -96.93 | -57.61 | -96.93 | 3650 |
| 92 | VWAP momentum | momentum | 76.40 | -23.60 | 289 | 9.3 | -98.45 | -36.92 | -98.46 | 5206 |
| 93 | CCI reversion | reversion | 75.62 | -24.38 | 169 | 5.9 | -98.47 | -53.23 | -98.47 | 4699 |
| 94 | MACD cross | trend | 75.19 | -24.81 | 185 | 8.1 | -99.70 | -67.83 | -99.71 | 6095 |
| 95 | Williams %R | reversion | 74.32 | -25.68 | 247 | 19.8 | -99.53 | -63.20 | -99.53 | 6089 |
| 96 | Heikin-Ashi | trend | 74.12 | -25.88 | 198 | 3.0 | -99.89 | -88.79 | -99.89 | 8323 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T03:40 | Candlestick reversal | sell | ETH-USD | 19.74 | -0.05 | exit signal |
| 2026-09-29T03:40 | VWAP momentum | sell | ETH-USD | 7.66 | -0.05 | exit signal |
| 2026-09-29T03:40 | MACD zero-line | buy | BTC-USD | 21.11 | — | entry signal |
| 2026-09-29T03:35 | VWAP reversion | sell | ETH-USD | 21.25 | -0.04 | exit signal |
| 2026-09-29T03:35 | Squeeze breakout | buy | BTC-USD | 22.58 | — | entry signal |
| 2026-09-29T03:35 | VWAP momentum | buy | ETH-USD | 7.71 | — | entry signal |
| 2026-09-29T03:35 | VWAP momentum | sell | XRP-USD | 3.89 | 0.00 | rebalance down |
| 2026-09-29T03:35 | VWAP momentum | sell | DOGE-USD | 3.82 | -0.02 | rebalance down |
| 2026-09-29T03:35 | MACD zero-line | buy | SOL-USD | 21.15 | — | entry signal |
| 2026-09-29T03:35 | MACD zero-line | buy | DOGE-USD | 21.15 | — | entry signal |
| 2026-09-29T03:35 | EMA 9/21 cross | buy | ETH-USD | 7.91 | — | entry signal |
| 2026-09-29T03:35 | EMA 9/21 cross | sell | XRP-USD | 3.93 | -0.02 | rebalance down |
| 2026-09-29T03:35 | EMA 9/21 cross | sell | SOL-USD | 3.93 | -0.02 | rebalance down |
| 2026-09-29T03:30 | Z-score reversion | sell | DOGE-USD | 21.47 | 0.12 | target is flat |
| 2026-09-29T03:30 | Z-score reversion | sell | BTC-USD | 17.16 | -0.06 | exit signal |
| 2026-09-29T03:30 | Three white soldiers | buy | BTC-USD | 23.97 | — | entry signal |
| 2026-09-29T03:30 | Donchian 20/10 | buy | BTC-USD | 20.65 | — | entry signal |
| 2026-09-29T03:30 | RSI momentum | buy | DOGE-USD | 20.98 | — | entry signal |
| 2026-09-29T03:30 | Heikin-Ashi | buy | XRP-USD | 14.86 | — | entry signal |
| 2026-09-29T03:30 | Heikin-Ashi | buy | ETH-USD | 14.87 | — | entry signal |
| 2026-09-29T03:30 | Heikin-Ashi | buy | DOGE-USD | 14.87 | — | entry signal |
| 2026-09-29T03:30 | Heikin-Ashi | buy | BTC-USD | 14.87 | — | entry signal |
| 2026-09-29T03:30 | Heikin-Ashi | sell | SOL-USD | 3.75 | 0.00 | rebalance down |
| 2026-09-29T03:30 | ADX DI cross | buy | ETH-USD | 12.35 | — | entry signal |
| 2026-09-29T03:30 | ADX DI cross | sell | XRP-USD | 4.12 | -0.00 | rebalance down |
| 2026-09-29T03:30 | ADX DI cross | sell | SOL-USD | 4.10 | -0.01 | rebalance down |
| 2026-09-29T03:30 | ADX DI cross | sell | DOGE-USD | 4.13 | -0.00 | rebalance down |
| 2026-09-29T03:30 | MACD zero-line | buy | XRP-USD | 21.17 | — | entry signal |
| 2026-09-29T03:30 | EMA 9/21 cross | buy | DOGE-USD | 19.70 | — | entry signal |
| 2026-09-29T03:30 | EMA 9/21 cross | buy | BTC-USD | 19.70 | — | entry signal |
| 2026-09-29T03:25 | CCI reversion | sell | ETH-USD | 15.14 | -0.08 | exit signal |
| 2026-09-29T03:25 | CCI reversion | sell | DOGE-USD | 19.01 | 0.03 | exit signal |
| 2026-09-29T03:25 | CCI reversion | sell | BTC-USD | 15.16 | -0.06 | exit signal |
| 2026-09-29T03:25 | Williams %R | sell | ETH-USD | 18.56 | -0.05 | exit signal |
| 2026-09-29T03:25 | Williams %R | sell | BTC-USD | 18.57 | -0.08 | exit signal |
| 2026-09-29T03:25 | Stochastic reversion | sell | BTC-USD | 19.54 | -0.07 | exit signal |
| 2026-09-29T03:25 | VWAP reversion | sell | SOL-USD | 21.38 | 0.04 | exit signal |
| 2026-09-29T03:25 | Z-score reversion | sell | XRP-USD | 21.61 | 0.10 | exit signal |
| 2026-09-29T03:25 | RSI(14) reversion | sell | XRP-USD | 23.19 | 0.11 | exit signal |
| 2026-09-29T03:25 | RSI(14) reversion | sell | BTC-USD | 18.54 | -0.09 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
