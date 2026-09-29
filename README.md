# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T03:10:05.000191+00:00 · 5237 ticks

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

Today: 2380 decisions in 476 calls, $0.0335 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T03:10 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-09-29T03:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T03:10 | 3 / 2 / 0 | SOL-USD 34%, ETH-USD 32% |  |

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
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.71 | -0.29 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 11 | Copy: Congress Democrats (NANC) | copy | 99.70 | -0.30 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 12 | Hold SPY | benchmark | 99.49 | -0.51 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 13 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 14 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 17.00 | 4.20 | -4.73 | 191 |
| 15 | Daily: Bullish score | daily | 99.21 | -0.80 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 17 | RSI(14) reversion · 1h | reversion | 99.15 | -0.85 | 2 | 100.0 | 14.24 | 2.99 | -6.57 | 136 |
| 18 | Connors RSI(2) · 1h | reversion | 99.07 | -0.93 | 39 | 48.7 | -11.80 | -3.73 | -13.35 | 235 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 99.05 | -0.95 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 99.04 | -0.96 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 21 | Hold BTC | benchmark | 99.03 | -0.97 | 0 | — | 29.85 | 3.76 | -8.68 | 1 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 98.94 | -1.05 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 23 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 24 | Stochastic reversion · 1h | reversion | 98.69 | -1.31 | 23 | 56.5 | -12.69 | -2.82 | -13.85 | 323 |
| 25 | Copy: Insider buying | copy | 98.54 | -1.46 | 2 | 100.0 | -12.69 | -2.44 | -17.74 | 73 |
| 26 | Williams %R · 1h | reversion | 98.48 | -1.52 | 30 | 50.0 | -18.23 | -3.36 | -19.83 | 487 |
| 27 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.88 | -2.76 | -11.75 | 233 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 29 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 30 | CCI reversion · 1h | reversion | 98.19 | -1.80 | 24 | 33.3 | 1.23 | 0.37 | -12.41 | 404 |
| 31 | Z-score reversion · 1h | reversion | 98.16 | -1.83 | 4 | 25.0 | 2.96 | 0.76 | -8.60 | 155 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 98.05 | -1.95 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 33 | Squeeze breakout · 1h | breakout | 98.02 | -1.98 | 7 | 14.3 | 16.09 | 2.83 | -6.26 | 94 |
| 34 | Candlestick reversal · 1h | reversion | 97.88 | -2.12 | 12 | 16.7 | -25.26 | -5.97 | -25.98 | 484 |
| 35 | EMA 20/50 cross · 1h | trend | 97.86 | -2.14 | 8 | 12.5 | 15.67 | 1.87 | -14.36 | 125 |
| 36 | Supertrend · 1h | trend | 97.65 | -2.35 | 11 | 9.1 | 5.23 | 0.90 | -16.43 | 194 |
| 37 | Bollinger reversion · 1h | reversion | 97.29 | -2.71 | 19 | 31.6 | -17.70 | -4.92 | -17.79 | 306 |
| 38 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.13 | -2.75 | -16.14 | 692 |
| 39 | Donchian 55/20 · 1h | breakout | 97.20 | -2.79 | 8 | 0.0 | 4.42 | 0.78 | -16.96 | 113 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.11 | -2.89 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.05 | -2.95 | 79 | 10.1 | 2.55 | 0.61 | -10.59 | 389 |
| 42 | Trend pullback · 1h | trend | 97.04 | -2.96 | 22 | 13.6 | -25.41 | -6.70 | -26.16 | 149 |
| 43 | Parabolic SAR · 1h | trend | 96.92 | -3.08 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 44 | MACD cross · 1h | trend | 96.85 | -3.15 | 31 | 9.7 | -16.50 | -2.80 | -20.79 | 455 |
| 45 | Bollinger breakout · 1h | breakout | 96.84 | -3.16 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 46 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.49 | -0.30 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.44 | -3.56 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Triple EMA stack · 1h | trend | 95.97 | -4.03 | 24 | 8.3 | -3.20 | -0.17 | -22.95 | 224 |
| 49 | Ichimoku · 1h | trend | 95.92 | -4.08 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 50 | Three white soldiers | momentum | 95.87 | -4.13 | 34 | 11.8 | -51.81 | -28.38 | -51.81 | 620 |
| 51 | EMA 9/21 cross · 1h | trend | 95.87 | -4.13 | 34 | 11.8 | 3.09 | 0.62 | -16.92 | 311 |
| 52 | ADX DI cross · 1h | trend | 95.85 | -4.15 | 25 | 8.0 | -11.86 | -2.23 | -15.77 | 250 |
| 53 | Donchian 20/10 · 1h | breakout | 95.78 | -4.22 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 54 | Max aggression: 1-day momentum | meta | 95.54 | -4.46 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 55 | OBV trend · 1h | momentum | 95.43 | -4.57 | 47 | 6.4 | -9.40 | -0.97 | -25.24 | 317 |
| 56 | MFI reversion · 1h | reversion | 95.38 | -4.62 | 38 | 13.2 | -10.09 | -1.87 | -17.20 | 126 |
| 57 | Volume breakout · 1h | breakout | 95.16 | -4.84 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 58 | Keltner breakout · 1h | breakout | 95.11 | -4.89 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 59 | VWAP momentum · 1h | momentum | 95.04 | -4.96 | 82 | 7.3 | -33.44 | -4.98 | -33.96 | 1250 |
| 60 | Max aggression: 5-day momentum | meta | 94.44 | -5.56 | 1 | 0.0 | -2.03 | 0.18 | -29.56 | 29 |
| 61 | Heikin-Ashi · 1h | trend | 94.32 | -5.68 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | ROC + volume · 1h | momentum | 91.86 | -8.14 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.73 | -8.27 | 91 | 34.1 | -71.24 | -22.01 | -71.29 | 1478 |
| 64 | Squeeze breakout | breakout | 90.45 | -9.55 | 66 | 6.1 | -59.74 | -18.56 | -59.90 | 1178 |
| 65 | ROC + volume | momentum | 89.31 | -10.69 | 115 | 16.5 | -71.92 | -17.85 | -72.35 | 1655 |
| 66 | Volume breakout | breakout | 88.63 | -11.37 | 76 | 9.2 | -62.56 | -20.50 | -62.56 | 908 |
| 67 | Donchian 55/20 | breakout | 88.55 | -11.45 | 77 | 11.7 | -68.89 | -15.95 | -68.89 | 1331 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.48 | -26.30 | -80.48 | 1755 |
| 71 | EMA 20/50 cross | trend | 87.61 | -12.39 | 95 | 13.7 | -78.98 | -17.85 | -79.11 | 1483 |
| 72 | Keltner breakout | breakout | 87.49 | -12.51 | 120 | 10.0 | -84.94 | -35.03 | -84.94 | 1928 |
| 73 | Z-score reversion | reversion | 85.37 | -14.63 | 146 | 28.8 | -84.79 | -28.71 | -84.80 | 2089 |
| 74 | VWAP reversion | reversion | 85.18 | -14.82 | 103 | 13.6 | -70.41 | -16.51 | -71.75 | 1404 |
| 75 | MACD zero-line | trend | 84.66 | -15.34 | 154 | 15.6 | -91.51 | -35.78 | -91.67 | 2361 |
| 76 | RSI momentum | momentum | 84.06 | -15.94 | 145 | 11.0 | -90.39 | -29.95 | -90.40 | 2397 |
| 77 | Bollinger breakout | breakout | 84.00 | -16.00 | 158 | 14.6 | -93.94 | -42.03 | -93.95 | 2874 |
| 78 | Supertrend | trend | 83.97 | -16.03 | 142 | 15.5 | -87.33 | -24.88 | -87.40 | 1959 |
| 79 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.50 | -33.62 | -90.50 | 2280 |
| 80 | Triple EMA stack | trend | 82.99 | -17.01 | 169 | 13.6 | -93.08 | -37.12 | -93.08 | 2628 |
| 81 | Donchian 20/10 | breakout | 82.73 | -17.27 | 159 | 15.1 | -90.94 | -30.26 | -90.95 | 2686 |
| 82 | ADX DI cross | trend | 82.08 | -17.92 | 160 | 6.9 | -89.41 | -48.11 | -89.41 | 2127 |
| 83 | MFI reversion | reversion | 82.04 | -17.96 | 152 | 16.4 | -87.81 | -34.95 | -87.92 | 2171 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.36 | -40.95 | -96.36 | 3649 |
| 85 | Consensus | meta | 79.44 | -20.56 | 156 | 7.1 | -94.69 | -30.18 | -94.69 | 2656 |
| 86 | Candlestick reversal | reversion | 79.08 | -20.92 | 193 | 14.0 | -99.36 | -52.90 | -99.36 | 5566 |
| 87 | EMA 9/21 cross | trend | 78.91 | -21.09 | 221 | 13.6 | -97.41 | -42.89 | -97.42 | 3548 |
| 88 | OBV trend | momentum | 78.46 | -21.54 | 220 | 12.7 | -95.86 | -50.79 | -95.86 | 3564 |
| 89 | Stochastic reversion | reversion | 78.41 | -21.59 | 255 | 23.5 | -95.94 | -49.09 | -95.95 | 4057 |
| 90 | Bollinger reversion | reversion | 77.28 | -22.72 | 243 | 12.8 | -95.81 | -46.85 | -95.81 | 3678 |
| 91 | Parabolic SAR | trend | 76.69 | -23.31 | 229 | 12.2 | -96.94 | -57.74 | -96.94 | 3651 |
| 92 | VWAP momentum | momentum | 76.58 | -23.42 | 288 | 9.4 | -98.44 | -36.77 | -98.46 | 5203 |
| 93 | CCI reversion | reversion | 75.53 | -24.47 | 166 | 5.4 | -98.47 | -53.36 | -98.47 | 4699 |
| 94 | MACD cross | trend | 74.78 | -25.22 | 185 | 8.1 | -99.70 | -68.52 | -99.71 | 6094 |
| 95 | Williams %R | reversion | 74.40 | -25.61 | 242 | 20.2 | -99.53 | -63.13 | -99.53 | 6090 |
| 96 | Heikin-Ashi | trend | 74.22 | -25.78 | 198 | 3.0 | -99.89 | -88.39 | -99.89 | 8322 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T03:10 | Stochastic reversion | buy | BTC-USD | 19.62 | — | entry signal |
| 2026-09-29T03:10 | Heikin-Ashi | buy | SOL-USD | 18.57 | — | entry signal |
| 2026-09-29T03:05 | CCI reversion | buy | DOGE-USD | 3.91 | — | rebalance up |
| 2026-09-29T03:05 | CCI reversion | sell | XRP-USD | 15.10 | -0.04 | exit signal |
| 2026-09-29T03:05 | CCI reversion | sell | SOL-USD | 15.12 | -0.06 | exit signal |
| 2026-09-29T03:04 | AI bee: Bizzy | sell | XRP-USD | 19.31 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-29T03:04 | AI bee: Bizzy | sell | SOL-USD | 12.07 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-09-29T03:03 | AI bee: Bizzy | buy | XRP-USD | 19.42 | — | Jev: buy (buy p=0.88) |
| 2026-09-29T03:03 | AI bee: Bizzy | buy | SOL-USD | 12.14 | — | Jev: buy (buy p=0.55) |
| 2026-09-29T03:00 | Candlestick reversal · 1h | buy | XRP-USD | 8.16 | — | entry signal |
| 2026-09-29T03:00 | MACD cross · 1h | sell | ETH-USD | 16.09 | -0.14 | exit signal |
| 2026-09-29T03:00 | MACD cross · 1h | sell | DOGE-USD | 12.58 | -0.22 | exit signal |
| 2026-09-29T03:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 19.01 | -0.37 | exit signal |
| 2026-09-29T02:59 | AI bee: Bizzy | sell | SOL-USD | 13.17 | -0.08 | Jev: sell (buy p=0.18) |
| 2026-09-29T02:58 | AI bee: Bizzy | buy | SOL-USD | 13.25 | — | Jev: buy (buy p=0.60) |
| 2026-09-29T02:57 | AI bee: Bizzy | sell | XRP-USD | 10.99 | -0.07 | Jev: sell (buy p=0.12) |
| 2026-09-29T02:55 | AI bee: Bizzy | buy | XRP-USD | 11.05 | — | Jev: buy (buy p=0.50) |
| 2026-09-29T02:55 | Candlestick reversal | buy | SOL-USD | 19.77 | — | entry signal |
| 2026-09-29T02:55 | Heikin-Ashi | sell | XRP-USD | 18.60 | -0.10 | exit signal |
| 2026-09-29T02:55 | Heikin-Ashi | sell | SOL-USD | 18.57 | -0.12 | exit signal |
| 2026-09-29T02:55 | Heikin-Ashi | sell | ETH-USD | 18.57 | -0.13 | exit signal |
| 2026-09-29T02:55 | Heikin-Ashi | sell | DOGE-USD | 18.54 | -0.16 | exit signal |
| 2026-09-29T02:54 | AI bee: Bizzy | sell | XRP-USD | 13.00 | -0.05 | Jev: sell (buy p=0.38) |
| 2026-09-29T02:53 | AI bee: Bizzy | buy | XRP-USD | 13.05 | — | Jev: buy (buy p=0.59) |
| 2026-09-29T02:52 | MACD cross | buy | DOGE-USD | 7.46 | — | rebalance up |
| 2026-09-29T02:52 | MACD cross | sell | XRP-USD | 3.73 | -0.02 | rebalance down |
| 2026-09-29T02:52 | MACD cross | sell | SOL-USD | 3.73 | -0.02 | rebalance down |
| 2026-09-29T02:50 | AI bee: Bizzy | sell | DOGE-USD | 19.12 | -0.15 | Jev: sell (buy p=0.03) |
| 2026-09-29T02:50 | Heikin-Ashi | buy | XRP-USD | 18.70 | — | entry signal |
| 2026-09-29T02:50 | Heikin-Ashi | buy | SOL-USD | 18.70 | — | entry signal |
| 2026-09-29T02:50 | Heikin-Ashi | buy | ETH-USD | 18.70 | — | entry signal |
| 2026-09-29T02:50 | Heikin-Ashi | buy | DOGE-USD | 18.70 | — | entry signal |
| 2026-09-29T02:50 | MACD cross | buy | DOGE-USD | 3.87 | — | entry signal |
| 2026-09-29T02:50 | MACD cross | sell | BTC-USD | 3.87 | -0.03 | rebalance down |
| 2026-09-29T02:49 | AI bee: Bizzy | buy | DOGE-USD | 19.28 | — | Jev: buy (buy p=0.87) |
| 2026-09-29T02:48 | AI bee: Bizzy | sell | XRP-USD | 18.35 | -0.09 | Jev: sell (buy p=0.13) |
| 2026-09-29T02:48 | AI bee: Bizzy | sell | DOGE-USD | 11.29 | -0.04 | Jev: sell (buy p=0.21) |
| 2026-09-29T02:45 | CCI reversion | buy | DOGE-USD | 15.07 | — | entry signal |
| 2026-09-29T02:45 | CCI reversion | sell | XRP-USD | 3.83 | -0.01 | rebalance down |
| 2026-09-29T02:45 | CCI reversion | sell | SOL-USD | 3.80 | -0.02 | rebalance down |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
