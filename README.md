# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T01:10:05.000127+00:00 · 6295 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.67 (-0.33%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 20.02 | +0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, BBD 12%, ENHA 12%, CX 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 885 decisions in 177 calls, $0.0125 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T01:10 | 3 / 2 / 0 | SOL-USD 18%, XRP-USD 16% |  |
| Breezy | 2026-09-30T01:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T01:10 | 4 / 1 / 0 | SOL-USD 37%, DOGE-USD 35% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) · 1h | COIN | 2.58 | +7.21% | 6 |
| RSI(14) reversion · 1h | SOL-USD | 2.42 | +2.64% | 3 |
| Z-score reversion | MSFT | 2.34 | +2.58% | 5 |
| Williams %R | TQQQ | 2.04 | +2.09% | 14 |
| Candlestick reversal | TQQQ | 2.01 | +4.48% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.02 | 1.02 | 2 | 50.0 | 13.82 | 2.99 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | 0.64 | 0.29 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.05 | 0.05 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.65 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Hold BTC | benchmark | 99.81 | -0.19 | 0 | — | 29.47 | 3.70 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.70 | -0.29 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 11 | Agent | meta | 99.67 | -0.33 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 12 | Agent (aggressive) | meta | 99.55 | -0.45 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.48 | -0.52 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.39 | -0.61 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.38 | -0.61 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.13 | -0.87 | 20 | 25.0 | -12.97 | -4.39 | -14.74 | 122 |
| 18 | Daily: Bullish score | daily | 99.04 | -0.96 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 3.53 | 0.95 | -7.03 | 123 |
| 20 | Z-score reversion · 1h | reversion | 98.87 | -1.13 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.85 | -1.15 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.57 | -1.43 | 40 | 45.0 | -17.93 | -3.31 | -19.43 | 488 |
| 24 | Candlestick reversal · 1h | reversion | 98.54 | -1.46 | 23 | 21.7 | -27.73 | -6.80 | -28.47 | 492 |
| 25 | Stochastic reversion · 1h | reversion | 98.52 | -1.48 | 26 | 53.8 | -13.59 | -2.99 | -14.80 | 328 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.42 | -1.58 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.24 | -1.76 | 35 | 34.3 | 0.28 | 0.21 | -12.41 | 410 |
| 30 | Connors RSI(2) · 1h | reversion | 97.85 | -2.15 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 31 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.78 | -2.22 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.69 | -2.31 | 12 | 8.3 | 16.59 | 1.97 | -14.13 | 126 |
| 34 | Max aggression: 5-day momentum | meta | 97.68 | -2.32 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Bollinger reversion · 1h | reversion | 97.26 | -2.74 | 22 | 27.3 | -17.88 | -4.94 | -18.50 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.55 | 2.73 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.65 | -3.35 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.61 | -3.39 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.56 | -3.44 | 18 | 5.6 | 1.98 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.48 | -3.52 | 139 | 12.9 | -0.51 | 0.06 | -12.34 | 376 |
| 42 | Trend pullback · 1h | trend | 96.26 | -3.74 | 28 | 10.7 | -28.81 | -7.05 | -29.59 | 147 |
| 43 | MACD cross · 1h | trend | 96.11 | -3.89 | 40 | 10.0 | -18.65 | -3.15 | -21.73 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.89 | -4.11 | 26 | 11.5 | -7.76 | -0.96 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.83 | -4.17 | 12 | 0.0 | 4.53 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 47 | MFI reversion · 1h | reversion | 95.47 | -4.53 | 44 | 13.6 | -9.74 | -1.78 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.24 | -27.70 | -50.38 | 607 |
| 49 | Ichimoku · 1h | trend | 95.17 | -4.83 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.91 | -5.09 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.28 | -5.72 | 20 | 5.0 | -5.32 | -0.56 | -14.64 | 222 |
| 53 | RSI momentum · 1h | momentum | 94.28 | -5.72 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 94.07 | -5.93 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 56 | ADX DI cross · 1h | trend | 94.02 | -5.98 | 30 | 6.7 | -16.13 | -2.98 | -17.81 | 255 |
| 57 | Triple EMA stack · 1h | trend | 93.84 | -6.16 | 30 | 6.7 | -6.76 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.68 | -6.32 | 103 | 12.6 | -34.84 | -5.26 | -35.28 | 1235 |
| 59 | EMA 9/21 cross · 1h | trend | 93.04 | -6.96 | 44 | 11.4 | -4.09 | -0.36 | -16.92 | 308 |
| 60 | Heikin-Ashi · 1h | trend | 92.70 | -7.30 | 45 | 11.1 | -26.43 | -4.01 | -30.59 | 672 |
| 61 | OBV trend · 1h | momentum | 92.47 | -7.53 | 54 | 7.4 | -13.04 | -1.43 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.83 | -9.17 | 119 | 34.5 | -71.39 | -21.55 | -71.46 | 1477 |
| 63 | Squeeze breakout | breakout | 89.44 | -10.56 | 94 | 14.9 | -59.69 | -18.36 | -59.85 | 1192 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 65 | ROC + volume | momentum | 87.31 | -12.69 | 148 | 18.9 | -71.90 | -17.49 | -71.97 | 1626 |
| 66 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 67 | Donchian 55/20 | breakout | 87.04 | -12.96 | 97 | 15.5 | -68.04 | -15.52 | -68.05 | 1302 |
| 68 | EMA 20/50 cross | trend | 86.43 | -13.57 | 125 | 16.0 | -78.76 | -17.43 | -78.76 | 1470 |
| 69 | AI bee: Bizzy | ai | 85.73 | -14.27 | 251 | 10.8 | — | — | — | — |
| 70 | Ichimoku | trend | 85.53 | -14.47 | 113 | 8.8 | -80.44 | -25.75 | -80.44 | 1743 |
| 71 | Keltner breakout | breakout | 85.48 | -14.52 | 149 | 13.4 | -84.80 | -33.80 | -84.82 | 1897 |
| 72 | Z-score reversion | reversion | 84.86 | -15.14 | 181 | 32.6 | -84.40 | -27.06 | -84.43 | 2097 |
| 73 | VWAP reversion | reversion | 84.68 | -15.32 | 137 | 22.6 | -71.60 | -17.53 | -71.92 | 1397 |
| 74 | AI bee: Boozy | ai | 84.07 | -15.93 | 95 | 1.1 | — | — | — | — |
| 75 | MACD zero-line | trend | 81.93 | -18.07 | 203 | 16.3 | -91.75 | -34.89 | -91.75 | 2354 |
| 76 | Supertrend | trend | 81.65 | -18.35 | 182 | 17.6 | -87.44 | -24.50 | -87.44 | 1957 |
| 77 | Donchian 20/10 | breakout | 80.90 | -19.10 | 206 | 17.5 | -90.86 | -29.16 | -90.86 | 2675 |
| 78 | MFI reversion | reversion | 80.63 | -19.37 | 186 | 19.4 | -88.13 | -35.38 | -88.15 | 2155 |
| 79 | Bollinger breakout | breakout | 80.39 | -19.61 | 207 | 16.4 | -93.88 | -40.87 | -93.88 | 2864 |
| 80 | Triple EMA stack | trend | 79.69 | -20.31 | 218 | 15.1 | -93.06 | -35.25 | -93.06 | 2618 |
| 81 | RSI momentum | momentum | 79.60 | -20.40 | 199 | 13.1 | -90.40 | -28.77 | -90.41 | 2379 |
| 82 | Trend pullback | trend | 79.25 | -20.75 | 170 | 17.1 | -90.77 | -33.99 | -90.77 | 2271 |
| 83 | ADX DI cross | trend | 79.04 | -20.96 | 198 | 8.1 | -89.43 | -44.61 | -89.43 | 2115 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.39 | -40.56 | -96.39 | 3620 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.58 | -29.56 | -94.59 | 2645 |
| 86 | EMA 9/21 cross | trend | 75.83 | -24.16 | 284 | 16.9 | -97.43 | -40.67 | -97.43 | 3536 |
| 87 | Stochastic reversion | reversion | 75.70 | -24.30 | 332 | 23.8 | -95.95 | -44.98 | -95.96 | 4060 |
| 88 | Candlestick reversal | reversion | 75.66 | -24.34 | 272 | 12.5 | -99.36 | -48.80 | -99.36 | 5590 |
| 89 | OBV trend | momentum | 74.51 | -25.49 | 277 | 15.2 | -95.89 | -46.79 | -95.89 | 3548 |
| 90 | Bollinger reversion | reversion | 74.24 | -25.76 | 310 | 15.5 | -95.79 | -43.42 | -95.79 | 3684 |
| 91 | VWAP momentum | momentum | 72.59 | -27.41 | 375 | 10.1 | -98.46 | -35.10 | -98.46 | 5192 |
| 92 | Parabolic SAR | trend | 72.47 | -27.53 | 271 | 12.9 | -97.02 | -52.60 | -97.02 | 3634 |
| 93 | CCI reversion | reversion | 72.43 | -27.57 | 244 | 11.1 | -98.47 | -49.61 | -98.47 | 4701 |
| 94 | MACD cross | trend | 71.84 | -28.16 | 272 | 14.0 | -99.72 | -61.69 | -99.72 | 6077 |
| 95 | Williams %R | reversion | 70.66 | -29.34 | 347 | 20.7 | -99.53 | -56.53 | -99.53 | 6110 |
| 96 | Heikin-Ashi | trend | 70.57 | -29.43 | 233 | 3.4 | -99.89 | -74.35 | -99.89 | 8299 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T01:10 | Williams %R | sell | SOL-USD | 17.68 | -0.06 | exit signal |
| 2026-09-30T01:10 | Williams %R | sell | DOGE-USD | 17.71 | -0.05 | exit signal |
| 2026-09-30T01:10 | Stochastic reversion | sell | SOL-USD | 18.93 | -0.03 | exit signal |
| 2026-09-30T01:10 | Stochastic reversion | sell | DOGE-USD | 18.96 | -0.00 | exit signal |
| 2026-09-30T01:10 | Bollinger reversion | sell | ETH-USD | 18.55 | -0.11 | exit signal |
| 2026-09-30T01:10 | Candlestick reversal | buy | SOL-USD | 3.79 | — | rebalance up |
| 2026-09-30T01:10 | Candlestick reversal | buy | ETH-USD | 3.81 | — | rebalance up |
| 2026-09-30T01:10 | Candlestick reversal | buy | BTC-USD | 3.81 | — | rebalance up |
| 2026-09-30T01:10 | Candlestick reversal | sell | XRP-USD | 15.12 | -0.04 | exit signal |
| 2026-09-30T01:10 | Squeeze breakout | buy | XRP-USD | 22.38 | — | entry signal |
| 2026-09-30T01:10 | Bollinger breakout | buy | XRP-USD | 20.11 | — | entry signal |
| 2026-09-30T01:10 | Donchian 20/10 | buy | XRP-USD | 20.24 | — | entry signal |
| 2026-09-30T01:10 | RSI momentum | buy | XRP-USD | 19.92 | — | entry signal |
| 2026-09-30T01:10 | VWAP momentum | buy | ETH-USD | 18.16 | — | entry signal |
| 2026-09-30T01:10 | Heikin-Ashi | buy | XRP-USD | 17.68 | — | entry signal |
| 2026-09-30T01:10 | Heikin-Ashi | buy | SOL-USD | 17.68 | — | entry signal |
| 2026-09-30T01:10 | Heikin-Ashi | buy | DOGE-USD | 17.68 | — | entry signal |
| 2026-09-30T01:10 | ADX DI cross | buy | DOGE-USD | 19.77 | — | entry signal |
| 2026-09-30T01:10 | Supertrend | buy | XRP-USD | 20.43 | — | entry signal |
| 2026-09-30T01:10 | MACD cross | buy | SOL-USD | 17.99 | — | entry signal |
| 2026-09-30T01:10 | MACD cross | buy | ETH-USD | 17.99 | — | entry signal |
| 2026-09-30T01:10 | EMA 9/21 cross | buy | XRP-USD | 18.97 | — | entry signal |
| 2026-09-30T01:09 | AI bee: Bizzy | buy | XRP-USD | 13.73 | — | Jev: buy (buy p=0.64) |
| 2026-09-30T01:09 | AI bee: Bizzy | buy | SOL-USD | 15.87 | — | Jev: buy (buy p=0.74) |
| 2026-09-30T01:07 | AI bee: Bizzy | sell | XRP-USD | 15.40 | -0.11 | Jev: sell (buy p=0.10) |
| 2026-09-30T01:07 | AI bee: Bizzy | sell | SOL-USD | 19.47 | -0.14 | Jev: sell (buy p=0.17) |
| 2026-09-30T01:07 | AI bee: Bizzy | sell | DOGE-USD | 18.82 | -0.14 | Jev: sell (buy p=0.18) |
| 2026-09-30T01:06 | AI bee: Boozy | buy | DOGE-USD | 28.61 | — | Jev: buy (buy p=0.68) |
| 2026-09-30T01:06 | AI bee: Bizzy | buy | XRP-USD | 15.51 | — | Jev: buy (buy p=0.72) |
| 2026-09-30T01:06 | AI bee: Bizzy | buy | SOL-USD | 19.60 | — | Jev: buy (buy p=0.91) |
| 2026-09-30T01:06 | AI bee: Bizzy | buy | DOGE-USD | 18.96 | — | Jev: buy (buy p=0.88) |
| 2026-09-30T01:05 | AI bee: Boozy | sell | DOGE-USD | 29.36 | -0.16 | Jev: sell (buy p=0.39) |
| 2026-09-30T01:05 | AI bee: Bizzy | sell | XRP-USD | 19.99 | -0.11 | Jev: sell (buy p=0.15) |
| 2026-09-30T01:05 | AI bee: Bizzy | sell | DOGE-USD | 11.79 | -0.08 | Jev: sell (buy p=0.09) |
| 2026-09-30T01:05 | CCI reversion | buy | BTC-USD | 18.11 | — | entry signal |
| 2026-09-30T01:05 | CCI reversion | sell | XRP-USD | 14.57 | -0.05 | exit signal |
| 2026-09-30T01:05 | Z-score reversion | sell | XRP-USD | 21.17 | -0.10 | exit signal |
| 2026-09-30T01:05 | Bollinger reversion | sell | DOGE-USD | 18.55 | -0.11 | exit signal |
| 2026-09-30T01:05 | VWAP momentum | sell | ETH-USD | 18.07 | -0.12 | exit signal |
| 2026-09-30T01:05 | MACD cross | buy | DOGE-USD | 17.98 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
