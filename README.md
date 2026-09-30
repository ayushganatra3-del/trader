# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T03:40:05.000116+00:00 · 6427 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.67 (-0.33%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 20.01 | +0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-09-30 | ETRA 12%, GME 12%, GRAB 12%, GSAT 12%, ADRX 12%, BBD 12%, ENHA 12%, CX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 22.07 · VIX 16.04 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 2865 decisions in 573 calls, $0.0402 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T03:40 | 2 / 3 / 0 | DOGE-USD 16%, SOL-USD 12% |  |
| Breezy | 2026-09-30T03:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T03:40 | 5 / 0 / 0 | SOL-USD 40%, ETH-USD 38% |  |

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
| 4 | Copy: Congress Democrats (NANC) | copy | 100.01 | 0.01 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.65 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.67 | -0.33 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Agent | meta | 99.67 | -0.33 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 11 | Hold BTC | benchmark | 99.66 | -0.34 | 0 | — | 29.81 | 3.73 | -8.68 | 1 |
| 12 | Agent (aggressive) | meta | 99.54 | -0.46 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.44 | -0.56 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.36 | -0.64 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.35 | -0.65 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.11 | -0.89 | 20 | 25.0 | -12.98 | -4.39 | -14.76 | 122 |
| 18 | Daily: Bullish score | daily | 99.01 | -0.99 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.00 | -1.00 | 7 | 57.1 | 1.65 | 0.50 | -7.03 | 126 |
| 20 | Z-score reversion · 1h | reversion | 98.85 | -1.15 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.82 | -1.18 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.52 | -1.48 | 40 | 45.0 | -17.75 | -3.28 | -19.41 | 488 |
| 24 | Candlestick reversal · 1h | reversion | 98.50 | -1.50 | 23 | 21.7 | -28.16 | -6.87 | -28.88 | 494 |
| 25 | Stochastic reversion · 1h | reversion | 98.49 | -1.51 | 26 | 53.8 | -14.09 | -3.06 | -15.28 | 331 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.39 | -1.61 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.21 | -1.79 | 35 | 34.3 | 0.50 | 0.25 | -12.41 | 410 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.83 | -2.17 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.75 | -2.25 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | Max aggression: 5-day momentum | meta | 97.65 | -2.35 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 34 | EMA 20/50 cross · 1h | trend | 97.64 | -2.36 | 13 | 7.7 | 16.56 | 1.97 | -14.13 | 126 |
| 35 | Bollinger reversion · 1h | reversion | 97.23 | -2.77 | 22 | 27.3 | -17.83 | -4.93 | -18.45 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.06 | -2.94 | 9 | 11.1 | 15.15 | 2.66 | -5.11 | 93 |
| 38 | Max aggression: 1-day momentum | meta | 96.62 | -3.38 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.58 | -3.42 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.51 | -3.49 | 18 | 5.6 | 1.96 | 0.47 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.43 | -3.57 | 139 | 12.9 | 3.14 | 0.69 | -11.55 | 379 |
| 42 | Trend pullback · 1h | trend | 96.24 | -3.76 | 28 | 10.7 | -28.93 | -7.09 | -29.45 | 147 |
| 43 | MACD cross · 1h | trend | 96.08 | -3.92 | 40 | 10.0 | -18.51 | -3.13 | -21.66 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.86 | -4.14 | 26 | 11.5 | -7.82 | -0.97 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.80 | -4.20 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 47 | MFI reversion · 1h | reversion | 95.49 | -4.51 | 44 | 13.6 | -9.63 | -1.76 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.32 | -27.90 | -50.38 | 608 |
| 49 | Ichimoku · 1h | trend | 95.16 | -4.84 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.89 | -5.11 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.26 | -5.75 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 53 | MACD zero-line · 1h | trend | 94.19 | -5.81 | 20 | 5.0 | -5.42 | -0.57 | -14.64 | 223 |
| 54 | Donchian 20/10 · 1h | breakout | 94.06 | -5.94 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.01 | 0.23 | -18.68 | 214 |
| 56 | ADX DI cross · 1h | trend | 93.99 | -6.01 | 30 | 6.7 | -16.13 | -2.98 | -17.81 | 255 |
| 57 | Triple EMA stack · 1h | trend | 93.82 | -6.18 | 30 | 6.7 | -6.79 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.65 | -6.35 | 103 | 12.6 | -34.83 | -5.26 | -35.33 | 1236 |
| 59 | EMA 9/21 cross · 1h | trend | 93.00 | -7.00 | 44 | 11.4 | -3.97 | -0.35 | -16.92 | 308 |
| 60 | Heikin-Ashi · 1h | trend | 92.68 | -7.32 | 45 | 11.1 | -26.43 | -4.01 | -30.59 | 672 |
| 61 | OBV trend · 1h | momentum | 92.44 | -7.56 | 54 | 7.4 | -13.09 | -1.44 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.07 | -21.19 | -71.11 | 1471 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 89.18 | -10.82 | 96 | 14.6 | -59.78 | -18.46 | -59.81 | 1193 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.99 | -19.88 | -62.05 | 897 |
| 66 | ROC + volume | momentum | 86.90 | -13.10 | 150 | 18.7 | -72.04 | -17.61 | -72.05 | 1628 |
| 67 | Donchian 55/20 | breakout | 86.49 | -13.51 | 99 | 15.2 | -68.25 | -15.66 | -68.25 | 1304 |
| 68 | EMA 20/50 cross | trend | 85.54 | -14.46 | 129 | 15.5 | -78.86 | -17.58 | -78.89 | 1471 |
| 69 | Ichimoku | trend | 85.31 | -14.69 | 114 | 8.8 | -80.47 | -25.85 | -80.51 | 1745 |
| 70 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.84 | -34.02 | -84.84 | 1898 |
| 71 | Z-score reversion | reversion | 84.60 | -15.40 | 184 | 32.1 | -84.45 | -27.17 | -84.47 | 2098 |
| 72 | VWAP reversion | reversion | 84.55 | -15.45 | 138 | 22.5 | -71.67 | -17.60 | -71.92 | 1401 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MACD zero-line | trend | 81.25 | -18.75 | 207 | 15.9 | -91.81 | -35.38 | -91.81 | 2357 |
| 76 | Supertrend | trend | 81.02 | -18.98 | 185 | 17.3 | -87.53 | -24.70 | -87.53 | 1958 |
| 77 | MFI reversion | reversion | 80.59 | -19.41 | 186 | 19.4 | -88.07 | -35.17 | -88.11 | 2153 |
| 78 | Donchian 20/10 | breakout | 80.33 | -19.67 | 209 | 17.2 | -90.92 | -29.42 | -90.92 | 2677 |
| 79 | Bollinger breakout | breakout | 79.93 | -20.07 | 210 | 16.2 | -93.91 | -41.34 | -93.91 | 2866 |
| 80 | RSI momentum | momentum | 79.04 | -20.95 | 202 | 12.9 | -90.47 | -29.03 | -90.48 | 2381 |
| 81 | Trend pullback | trend | 78.97 | -21.03 | 171 | 17.0 | -90.68 | -33.76 | -90.68 | 2266 |
| 82 | Triple EMA stack | trend | 78.94 | -21.05 | 221 | 14.9 | -93.11 | -35.76 | -93.12 | 2621 |
| 83 | ADX DI cross | trend | 78.67 | -21.33 | 200 | 8.0 | -89.42 | -45.04 | -89.42 | 2115 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.34 | -39.98 | -96.34 | 3611 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.61 | -29.62 | -94.62 | 2648 |
| 86 | Stochastic reversion | reversion | 75.58 | -24.42 | 333 | 23.7 | -95.91 | -44.45 | -95.91 | 4056 |
| 87 | Candlestick reversal | reversion | 75.49 | -24.51 | 276 | 12.7 | -99.35 | -48.52 | -99.36 | 5584 |
| 88 | EMA 9/21 cross | trend | 74.98 | -25.02 | 289 | 16.6 | -97.45 | -41.29 | -97.45 | 3541 |
| 89 | Bollinger reversion | reversion | 74.00 | -26.00 | 314 | 15.3 | -95.78 | -43.18 | -95.78 | 3684 |
| 90 | OBV trend | momentum | 73.67 | -26.33 | 282 | 14.9 | -95.92 | -47.69 | -95.92 | 3551 |
| 91 | Parabolic SAR | trend | 71.99 | -28.01 | 274 | 12.8 | -97.00 | -53.65 | -97.01 | 3632 |
| 92 | CCI reversion | reversion | 71.58 | -28.42 | 251 | 10.8 | -98.47 | -49.84 | -98.47 | 4703 |
| 93 | VWAP momentum | momentum | 71.24 | -28.76 | 387 | 9.8 | -98.49 | -35.70 | -98.49 | 5204 |
| 94 | MACD cross | trend | 70.93 | -29.07 | 281 | 13.5 | -99.72 | -63.11 | -99.72 | 6078 |
| 95 | Williams %R | reversion | 70.06 | -29.95 | 351 | 20.5 | -99.52 | -56.70 | -99.52 | 6111 |
| 96 | Heikin-Ashi | trend | 70.02 | -29.98 | 239 | 3.3 | -99.90 | -75.78 | -99.90 | 8301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T03:40 | CCI reversion | buy | XRP-USD | 17.93 | — | entry signal |
| 2026-09-30T03:40 | CCI reversion | buy | DOGE-USD | 17.93 | — | entry signal |
| 2026-09-30T03:40 | CCI reversion | buy | BTC-USD | 17.93 | — | entry signal |
| 2026-09-30T03:40 | Bollinger reversion | sell | SOL-USD | 18.47 | -0.07 | exit signal |
| 2026-09-30T03:40 | Bollinger reversion | sell | DOGE-USD | 18.50 | -0.03 | exit signal |
| 2026-09-30T03:40 | OBV trend | buy | SOL-USD | 18.43 | — | entry signal |
| 2026-09-30T03:40 | VWAP momentum | buy | XRP-USD | 17.85 | — | entry signal |
| 2026-09-30T03:40 | VWAP momentum | buy | SOL-USD | 17.85 | — | entry signal |
| 2026-09-30T03:40 | VWAP momentum | buy | ETH-USD | 17.85 | — | entry signal |
| 2026-09-30T03:40 | Trend pullback | buy | SOL-USD | 19.76 | — | entry signal |
| 2026-09-30T03:40 | ADX DI cross | buy | XRP-USD | 19.70 | — | entry signal |
| 2026-09-30T03:40 | ADX DI cross | buy | SOL-USD | 19.70 | — | entry signal |
| 2026-09-30T03:40 | Parabolic SAR | buy | SOL-USD | 18.01 | — | entry signal |
| 2026-09-30T03:40 | Triple EMA stack | buy | SOL-USD | 19.75 | — | entry signal |
| 2026-09-30T03:40 | EMA 9/21 cross | buy | SOL-USD | 18.77 | — | entry signal |
| 2026-09-30T03:40 | EMA 9/21 cross | buy | ETH-USD | 18.77 | — | entry signal |
| 2026-09-30T03:35 | Candlestick reversal | buy | BTC-USD | 18.86 | — | entry signal |
| 2026-09-30T03:35 | MACD cross | buy | ETH-USD | 17.74 | — | entry signal |
| 2026-09-30T03:35 | EMA 9/21 cross | sell | SOL-USD | 18.85 | -0.10 | exit signal |
| 2026-09-30T03:31 | Williams %R | buy | XRP-USD | 3.49 | — | rebalance up |
| 2026-09-30T03:31 | Williams %R | sell | ETH-USD | 3.49 | -0.02 | rebalance down |
| 2026-09-30T03:30 | CCI reversion | buy | SOL-USD | 17.94 | — | entry signal |
| 2026-09-30T03:30 | Williams %R | buy | XRP-USD | 10.47 | — | entry signal |
| 2026-09-30T03:30 | Williams %R | sell | SOL-USD | 3.49 | -0.02 | rebalance down |
| 2026-09-30T03:30 | Williams %R | sell | DOGE-USD | 3.49 | -0.02 | rebalance down |
| 2026-09-30T03:30 | Williams %R | sell | BTC-USD | 3.49 | -0.02 | rebalance down |
| 2026-09-30T03:30 | Candlestick reversal | buy | XRP-USD | 18.88 | — | entry signal |
| 2026-09-30T03:30 | Candlestick reversal | buy | DOGE-USD | 18.88 | — | entry signal |
| 2026-09-30T03:30 | MACD zero-line | sell | ETH-USD | 20.20 | -0.16 | exit signal |
| 2026-09-30T03:30 | MACD cross | sell | ETH-USD | 17.75 | -0.12 | exit signal |
| 2026-09-30T03:25 | Williams %R | buy | SOL-USD | 17.54 | — | entry signal |
| 2026-09-30T03:25 | Williams %R | buy | ETH-USD | 17.54 | — | entry signal |
| 2026-09-30T03:25 | Williams %R | buy | DOGE-USD | 17.54 | — | entry signal |
| 2026-09-30T03:25 | Williams %R | buy | BTC-USD | 17.54 | — | entry signal |
| 2026-09-30T03:25 | Stochastic reversion | buy | XRP-USD | 18.89 | — | entry signal |
| 2026-09-30T03:25 | VWAP reversion | buy | BTC-USD | 21.15 | — | entry signal |
| 2026-09-30T03:25 | Z-score reversion | buy | DOGE-USD | 21.15 | — | entry signal |
| 2026-09-30T03:25 | Z-score reversion | buy | BTC-USD | 21.15 | — | entry signal |
| 2026-09-30T03:25 | Bollinger reversion | buy | XRP-USD | 18.53 | — | entry signal |
| 2026-09-30T03:25 | Bollinger reversion | buy | SOL-USD | 18.53 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
