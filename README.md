# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T07:10:05.000149+00:00 · 5429 ticks

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

Today: 5260 decisions in 1052 calls, $0.0737 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T07:10 | 2 / 3 / 0 | DOGE-USD 16%, ETH-USD 13% |  |
| Breezy | 2026-09-29T07:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T07:10 | 5 / 0 / 0 | ETH-USD 40%, DOGE-USD 38% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |
| CCI reversion | AMD | 2.08 | +3.00% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.36 | 1.36 | 1 | 100.0 | 12.70 | 2.77 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.06 | 0.10 | -1.49 | 19 |
| 3 | Hold BTC | benchmark | 100.47 | 0.47 | 0 | — | 30.28 | 3.80 | -8.68 | 1 |
| 4 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 5 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 6 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 7 | RSI(14) reversion · 1h | reversion | 100.07 | 0.07 | 2 | 100.0 | 14.96 | 3.12 | -6.57 | 139 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.83 | -0.17 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.81 | -0.18 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.61 | -0.39 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.93 | -4.40 | -14.78 | 121 |
| 16 | Daily: Bullish score | daily | 99.32 | -0.68 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 17 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.05 | -4.73 | 190 |
| 18 | Z-score reversion · 1h | reversion | 99.25 | -0.75 | 5 | 40.0 | 3.83 | 0.95 | -8.60 | 155 |
| 19 | Stochastic reversion · 1h | reversion | 99.20 | -0.80 | 23 | 56.5 | -12.31 | -2.72 | -13.86 | 324 |
| 20 | Timing: Nasdaq FTD · QQQ | daily | 99.17 | -0.83 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 21 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 99.15 | -0.85 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 23 | Connors RSI(2) · 1h | reversion | 99.13 | -0.87 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 24 | Copy: Hedge-fund gurus (GURU) | copy | 99.06 | -0.94 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.71 | -1.29 | 31 | 51.6 | -17.63 | -3.22 | -19.79 | 489 |
| 27 | CCI reversion · 1h | reversion | 98.68 | -1.32 | 26 | 38.5 | 1.57 | 0.43 | -12.41 | 405 |
| 28 | Copy: Insider buying | copy | 98.64 | -1.36 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.32 | -2.59 | -11.75 | 233 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.29 | -1.71 | 12 | 16.7 | -26.02 | -6.07 | -26.58 | 494 |
| 32 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.16 | -1.84 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Supertrend · 1h | trend | 98.09 | -1.91 | 11 | 9.1 | 5.58 | 0.94 | -16.43 | 194 |
| 35 | Squeeze breakout · 1h | breakout | 98.04 | -1.96 | 7 | 14.3 | 15.96 | 2.81 | -6.26 | 94 |
| 36 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 8 | 12.5 | 15.62 | 1.87 | -14.36 | 125 |
| 37 | Bollinger reversion · 1h | reversion | 97.40 | -2.60 | 19 | 31.6 | -17.67 | -4.91 | -17.76 | 306 |
| 38 | MACD cross · 1h | trend | 97.35 | -2.65 | 31 | 9.7 | -15.95 | -2.70 | -20.52 | 459 |
| 39 | Donchian 55/20 · 1h | breakout | 97.29 | -2.71 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 40 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 41 | Timing: Nasdaq FTD · TQQQ | daily | 97.22 | -2.78 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 42 | Agent (ML meta-label) | meta | 97.15 | -2.85 | 79 | 10.1 | 4.71 | 0.97 | -10.90 | 394 |
| 43 | Trend pullback · 1h | trend | 97.13 | -2.87 | 22 | 13.6 | -25.81 | -6.85 | -26.39 | 148 |
| 44 | Parabolic SAR · 1h | trend | 96.99 | -3.01 | 20 | 15.0 | -5.61 | -0.64 | -18.82 | 301 |
| 45 | Bollinger breakout · 1h | breakout | 96.89 | -3.11 | 13 | 7.7 | 13.23 | 1.88 | -9.85 | 285 |
| 46 | Max aggression: 5-day momentum | meta | 96.52 | -3.48 | 1 | 0.0 | 0.01 | 0.35 | -29.56 | 29 |
| 47 | MACD zero-line · 1h | trend | 96.52 | -3.48 | 15 | 6.7 | -3.52 | -0.31 | -14.64 | 219 |
| 48 | RSI momentum · 1h | momentum | 96.46 | -3.54 | 20 | 5.0 | 1.53 | 0.41 | -15.29 | 213 |
| 49 | Triple EMA stack · 1h | trend | 96.05 | -3.95 | 24 | 8.3 | -2.80 | -0.12 | -22.95 | 223 |
| 50 | Ichimoku · 1h | trend | 95.94 | -4.06 | 11 | 9.1 | 8.13 | 1.14 | -15.13 | 120 |
| 51 | EMA 9/21 cross · 1h | trend | 95.93 | -4.07 | 34 | 11.8 | 3.03 | 0.61 | -16.92 | 311 |
| 52 | Three white soldiers | momentum | 95.91 | -4.09 | 37 | 10.8 | -51.71 | -28.37 | -52.21 | 626 |
| 53 | MFI reversion · 1h | reversion | 95.88 | -4.12 | 38 | 13.2 | -9.17 | -1.68 | -17.20 | 125 |
| 54 | Donchian 20/10 · 1h | breakout | 95.84 | -4.16 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 95.81 | -4.19 | 25 | 8.0 | -11.98 | -2.26 | -15.42 | 252 |
| 56 | Max aggression: 1-day momentum | meta | 95.65 | -4.35 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 57 | OBV trend · 1h | momentum | 95.48 | -4.52 | 47 | 6.4 | -9.59 | -1.00 | -25.24 | 317 |
| 58 | VWAP momentum · 1h | momentum | 95.36 | -4.64 | 82 | 7.3 | -31.76 | -4.68 | -34.09 | 1250 |
| 59 | Volume breakout · 1h | breakout | 95.19 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 60 | Keltner breakout · 1h | breakout | 95.14 | -4.86 | 7 | 0.0 | -0.48 | 0.14 | -18.68 | 221 |
| 61 | Heikin-Ashi · 1h | trend | 94.34 | -5.66 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | ROC + volume · 1h | momentum | 91.94 | -8.06 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.24 | -22.02 | -71.32 | 1474 |
| 64 | ROC + volume | momentum | 89.63 | -10.37 | 115 | 16.5 | -71.68 | -17.70 | -72.42 | 1656 |
| 65 | Squeeze breakout | breakout | 89.62 | -10.38 | 71 | 5.6 | -60.06 | -18.84 | -60.46 | 1185 |
| 66 | Donchian 55/20 | breakout | 89.14 | -10.86 | 77 | 11.7 | -68.22 | -15.74 | -68.54 | 1330 |
| 67 | Volume breakout | breakout | 89.01 | -10.99 | 76 | 9.2 | -62.13 | -20.24 | -62.47 | 908 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | EMA 20/50 cross | trend | 87.99 | -12.01 | 97 | 13.4 | -78.85 | -17.77 | -79.33 | 1487 |
| 71 | Ichimoku | trend | 87.87 | -12.13 | 85 | 8.2 | -80.26 | -25.90 | -80.36 | 1755 |
| 72 | Keltner breakout | breakout | 87.74 | -12.27 | 120 | 10.0 | -84.81 | -34.67 | -84.97 | 1929 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.70 | -28.55 | -84.77 | 2088 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.35 | -17.58 | -71.87 | 1418 |
| 75 | Supertrend | trend | 84.53 | -15.47 | 143 | 15.4 | -87.19 | -24.69 | -87.47 | 1964 |
| 76 | MACD zero-line | trend | 83.80 | -16.20 | 159 | 15.1 | -91.60 | -36.33 | -91.77 | 2365 |
| 77 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.50 | -33.62 | -90.50 | 2280 |
| 78 | Donchian 20/10 | breakout | 83.10 | -16.90 | 162 | 14.8 | -90.86 | -30.08 | -91.02 | 2688 |
| 79 | Bollinger breakout | breakout | 82.93 | -17.07 | 165 | 13.9 | -93.97 | -42.43 | -94.08 | 2879 |
| 80 | RSI momentum | momentum | 82.88 | -17.12 | 153 | 10.5 | -90.39 | -30.22 | -90.64 | 2403 |
| 81 | Triple EMA stack | trend | 82.74 | -17.26 | 173 | 13.3 | -92.91 | -36.91 | -93.07 | 2621 |
| 82 | MFI reversion | reversion | 82.15 | -17.86 | 153 | 17.0 | -87.80 | -34.92 | -87.92 | 2169 |
| 83 | ADX DI cross | trend | 81.43 | -18.57 | 167 | 6.6 | -89.36 | -48.11 | -89.48 | 2125 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.36 | -40.97 | -96.36 | 3648 |
| 85 | Consensus | meta | 79.45 | -20.55 | 157 | 7.0 | -94.78 | -30.55 | -94.80 | 2669 |
| 86 | EMA 9/21 cross | trend | 79.45 | -20.55 | 223 | 13.5 | -97.37 | -42.31 | -97.43 | 3548 |
| 87 | Candlestick reversal | reversion | 78.66 | -21.34 | 201 | 13.9 | -99.36 | -53.20 | -99.36 | 5567 |
| 88 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.94 | -49.05 | -95.95 | 4056 |
| 89 | OBV trend | momentum | 78.27 | -21.73 | 225 | 12.4 | -95.73 | -49.80 | -95.85 | 3557 |
| 90 | Bollinger reversion | reversion | 77.13 | -22.87 | 246 | 12.6 | -95.80 | -46.91 | -95.80 | 3677 |
| 91 | Parabolic SAR | trend | 75.93 | -24.07 | 237 | 11.8 | -96.92 | -57.95 | -96.96 | 3656 |
| 92 | VWAP momentum | momentum | 75.47 | -24.53 | 301 | 9.0 | -98.48 | -37.33 | -98.49 | 5218 |
| 93 | CCI reversion | reversion | 75.22 | -24.78 | 176 | 5.7 | -98.47 | -53.47 | -98.47 | 4700 |
| 94 | MACD cross | trend | 74.52 | -25.48 | 195 | 8.7 | -99.70 | -67.94 | -99.71 | 6097 |
| 95 | Williams %R | reversion | 74.01 | -25.99 | 256 | 19.5 | -99.53 | -63.72 | -99.53 | 6096 |
| 96 | Heikin-Ashi | trend | 72.11 | -27.89 | 220 | 3.2 | -99.89 | -91.96 | -99.89 | 8327 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T07:10 | RSI momentum | buy | XRP-USD | 4.12 | — | rebalance up |
| 2026-09-29T07:05 | Heikin-Ashi | sell | BTC-USD | 17.92 | -0.12 | exit signal |
| 2026-09-29T07:00 | Agent (ML meta-label) | buy | DOGE-USD | 1.78 | — | entry |
| 2026-09-29T07:00 | CCI reversion · 1h | sell | DOGE-USD | 8.35 | 0.12 | exit signal |
| 2026-09-29T07:00 | CCI reversion · 1h | sell | BTC-USD | 7.05 | 0.04 | exit signal |
| 2026-09-29T07:00 | Williams %R · 1h | buy | SOL-USD | 5.54 | — | entry |
| 2026-09-29T07:00 | Williams %R · 1h | sell | DOGE-USD | 5.54 | 0.07 | exit signal |
| 2026-09-29T07:00 | Z-score reversion · 1h | sell | BTC-USD | 16.53 | 0.02 | exit signal |
| 2026-09-29T07:00 | Bollinger breakout · 1h | buy | ETH-USD | 24.23 | — | entry signal |
| 2026-09-29T07:00 | RSI momentum · 1h | buy | ETH-USD | 24.12 | — | entry signal |
| 2026-09-29T07:00 | Ichimoku · 1h | buy | ETH-USD | 23.99 | — | entry signal |
| 2026-09-29T07:00 | ADX DI cross · 1h | buy | DOGE-USD | 23.97 | — | entry signal |
| 2026-09-29T07:00 | ADX DI cross · 1h | buy | BTC-USD | 23.97 | — | entry signal |
| 2026-09-29T07:00 | Parabolic SAR · 1h | buy | DOGE-USD | 16.17 | — | entry signal |
| 2026-09-29T07:00 | MACD zero-line · 1h | buy | ETH-USD | 24.14 | — | entry signal |
| 2026-09-29T07:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 19.01 | — | entry signal |
| 2026-09-29T07:00 | Heikin-Ashi | buy | BTC-USD | 18.04 | — | entry signal |
| 2026-09-29T06:55 | Heikin-Ashi | buy | DOGE-USD | 18.06 | — | entry signal |
| 2026-09-29T06:45 | Consensus | buy | SOL-USD | 3.97 | — | rebalance up |
| 2026-09-29T06:45 | Consensus | sell | BTC-USD | 11.84 | -0.06 | target is flat |
| 2026-09-29T06:45 | Heikin-Ashi | sell | BTC-USD | 14.44 | 0.00 | exit signal |
| 2026-09-29T06:40 | Heikin-Ashi | sell | SOL-USD | 18.02 | -0.02 | exit signal |
| 2026-09-29T06:30 | RSI momentum | sell | ETH-USD | 4.12 | 0.00 | rebalance down |
| 2026-09-29T06:30 | Heikin-Ashi | sell | XRP-USD | 14.42 | -0.00 | exit signal |
| 2026-09-29T06:27 | Consensus | buy | BTC-USD | 3.95 | — | rebalance up |
| 2026-09-29T06:27 | Consensus | sell | SOL-USD | 3.95 | -0.03 | rebalance down |
| 2026-09-29T06:25 | Consensus | buy | BTC-USD | 7.95 | — | entry |
| 2026-09-29T06:25 | Consensus | sell | ETH-USD | 3.99 | -0.02 | rebalance down |
| 2026-09-29T06:25 | Consensus | sell | DOGE-USD | 3.95 | -0.03 | rebalance down |
| 2026-09-29T06:25 | Heikin-Ashi | buy | SOL-USD | 3.62 | — | rebalance up |
| 2026-09-29T06:25 | Heikin-Ashi | buy | ETH-USD | 3.63 | — | rebalance up |
| 2026-09-29T06:25 | Heikin-Ashi | sell | DOGE-USD | 14.42 | -0.01 | exit signal |
| 2026-09-29T06:25 | Ichimoku | buy | XRP-USD | 17.54 | — | entry signal |
| 2026-09-29T06:25 | Ichimoku | buy | SOL-USD | 17.54 | — | entry signal |
| 2026-09-29T06:25 | Ichimoku | buy | ETH-USD | 17.54 | — | entry signal |
| 2026-09-29T06:25 | Ichimoku | buy | DOGE-USD | 17.54 | — | entry signal |
| 2026-09-29T06:25 | Ichimoku | buy | BTC-USD | 17.54 | — | entry signal |
| 2026-09-29T06:20 | Donchian 55/20 | buy | SOL-USD | 4.43 | — | rebalance up |
| 2026-09-29T06:20 | Donchian 55/20 | sell | ETH-USD | 4.43 | -0.00 | rebalance down |
| 2026-09-29T06:20 | ROC + volume | buy | XRP-USD | 8.91 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
