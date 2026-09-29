# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T22:10:05.000175+00:00 · 6155 ticks

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
| Copy: Insider buying | 2026-09-29 | ETRA 12%, GRAB 12%, GSAT 12%, BBD 12%, GME 12%, ENHA 12%, CX 12%, CRAFX 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-09-29)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.96 · VIX 16.02 · last follow-through day 2026-08-04

Best bullish scores: BITX 8.5, MSTR 8.5, PLTR 8.5, META 8.1, COIN 8.0, MSFT 7.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 38643 decisions in 3227 calls, $0.4787 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T22:10 | 2 / 1 / 2 | SOL-USD 23%, DOGE-USD 15% |  |
| Breezy | 2026-09-29T22:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T22:10 | 4 / 1 / 0 | SOL-USD 44%, DOGE-USD 42% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | AMD | 2.92 | +2.67% | 12 |
| Connors RSI(2) · 1h | COIN | 2.43 | +6.94% | 5 |
| Z-score reversion | MSFT | 2.27 | +1.52% | 4 |
| VWAP reversion | NVDA | 2.16 | +1.89% | 4 |
| Candlestick reversal | TQQQ | 2.10 | +4.61% | 9 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.02 | 1.02 | 2 | 50.0 | 13.82 | 3.01 | -7.55 | 43 |
| 2 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 1 | 100.0 | 0.30 | 0.46 | -1.49 | 18 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | 0.64 | 0.29 | -9.74 | 24 |
| 4 | Copy: Congress Democrats (NANC) | copy | 100.03 | 0.03 | 0 | — | 7.21 | 2.96 | -3.62 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.68 | -7.93 | 7 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Hold BTC | benchmark | 99.96 | -0.04 | 0 | — | 30.51 | 3.83 | -8.68 | 1 |
| 9 | Copy: Warren Buffett (BRK-B) | copy | 99.69 | -0.31 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.63 | -1.84 | 83 |
| 11 | Agent | meta | 99.67 | -0.33 | 24 | 66.7 | -10.10 | -6.78 | -10.75 | 219 |
| 12 | Agent (aggressive) | meta | 99.55 | -0.45 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 13 | Hold SPY | benchmark | 99.46 | -0.54 | 0 | — | 3.46 | 1.94 | -3.66 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.38 | -0.62 | 0 | — | -2.73 | -1.32 | -5.14 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 99.37 | -0.63 | 0 | — | -3.44 | -2.11 | -5.09 | 2 |
| 16 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 17 | VWAP reversion · 1h | reversion | 99.12 | -0.88 | 20 | 25.0 | -13.02 | -4.44 | -14.79 | 122 |
| 18 | Daily: Bullish score | daily | 99.03 | -0.97 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 19 | RSI(14) reversion · 1h | reversion | 99.01 | -0.99 | 7 | 57.1 | 4.97 | 1.31 | -7.03 | 119 |
| 20 | Z-score reversion · 1h | reversion | 98.86 | -1.14 | 10 | 50.0 | 5.16 | 1.24 | -8.60 | 153 |
| 21 | Copy: Insider buying | copy | 98.83 | -1.17 | 2 | 100.0 | -14.26 | -2.83 | -17.74 | 72 |
| 22 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 23 | Williams %R · 1h | reversion | 98.61 | -1.39 | 40 | 45.0 | -17.85 | -3.32 | -19.41 | 488 |
| 24 | Candlestick reversal · 1h | reversion | 98.61 | -1.39 | 21 | 23.8 | -27.18 | -6.78 | -28.00 | 490 |
| 25 | Stochastic reversion · 1h | reversion | 98.51 | -1.49 | 26 | 53.8 | -13.81 | -3.05 | -15.02 | 329 |
| 26 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.70 | -4.73 | 182 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 98.41 | -1.59 | 0 | — | 23.27 | 3.46 | -6.29 | 1 |
| 28 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 29 | CCI reversion · 1h | reversion | 98.23 | -1.77 | 35 | 34.3 | 0.42 | 0.24 | -12.41 | 410 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.78 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.84 | -2.16 | 45 | 44.4 | -11.35 | -3.64 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.76 | -2.23 | 0 | — | -11.11 | -2.29 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.72 | -2.28 | 12 | 8.3 | 16.62 | 1.99 | -14.13 | 126 |
| 34 | Max aggression: 5-day momentum | meta | 97.67 | -2.33 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Bollinger reversion · 1h | reversion | 97.25 | -2.75 | 22 | 27.3 | -17.85 | -4.97 | -18.47 | 313 |
| 36 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.63 | -14.21 | 560 |
| 37 | Squeeze breakout · 1h | breakout | 97.07 | -2.93 | 9 | 11.1 | 15.55 | 2.75 | -5.11 | 92 |
| 38 | Max aggression: 1-day momentum | meta | 96.64 | -3.36 | 2 | 0.0 | -37.96 | -2.25 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.59 | -3.41 | 0 | — | -9.73 | -2.36 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.57 | -3.43 | 18 | 5.6 | 2.01 | 0.48 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.47 | -3.53 | 139 | 12.9 | 2.63 | 0.61 | -11.34 | 381 |
| 42 | Trend pullback · 1h | trend | 96.25 | -3.75 | 28 | 10.7 | -28.75 | -7.09 | -29.59 | 147 |
| 43 | MACD cross · 1h | trend | 96.10 | -3.90 | 40 | 10.0 | -18.84 | -3.21 | -21.97 | 461 |
| 44 | Parabolic SAR · 1h | trend | 95.88 | -4.12 | 26 | 11.5 | -7.76 | -0.97 | -18.82 | 292 |
| 45 | Donchian 55/20 · 1h | breakout | 95.82 | -4.18 | 12 | 0.0 | 4.54 | 0.80 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.87 | -16.91 | 684 |
| 47 | MFI reversion · 1h | reversion | 95.47 | -4.53 | 44 | 13.6 | -9.71 | -1.79 | -17.20 | 128 |
| 48 | Three white soldiers | momentum | 95.34 | -4.66 | 43 | 18.6 | -50.24 | -28.40 | -50.38 | 607 |
| 49 | Ichimoku · 1h | trend | 95.16 | -4.84 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.90 | -5.10 | 17 | 5.9 | 8.30 | 1.27 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 1.00 | -12.60 | 125 |
| 52 | MACD zero-line · 1h | trend | 94.28 | -5.72 | 20 | 5.0 | -5.56 | -0.60 | -14.64 | 223 |
| 53 | RSI momentum · 1h | momentum | 94.27 | -5.73 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 54 | Donchian 20/10 · 1h | breakout | 94.06 | -5.94 | 16 | 12.5 | 6.99 | 1.09 | -12.78 | 213 |
| 55 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | 0.33 | 0.27 | -18.68 | 212 |
| 56 | ADX DI cross · 1h | trend | 94.00 | -6.00 | 30 | 6.7 | -16.34 | -3.05 | -18.02 | 256 |
| 57 | Triple EMA stack · 1h | trend | 93.83 | -6.17 | 30 | 6.7 | -6.73 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.67 | -6.33 | 103 | 12.6 | -34.77 | -5.30 | -35.20 | 1234 |
| 59 | EMA 9/21 cross · 1h | trend | 93.04 | -6.96 | 44 | 11.4 | -3.90 | -0.34 | -16.92 | 307 |
| 60 | Heikin-Ashi · 1h | trend | 92.69 | -7.31 | 45 | 11.1 | -26.43 | -4.04 | -30.59 | 672 |
| 61 | OBV trend · 1h | momentum | 92.46 | -7.54 | 54 | 7.4 | -13.07 | -1.45 | -25.19 | 317 |
| 62 | RSI(14) reversion | reversion | 90.93 | -9.07 | 118 | 34.7 | -71.12 | -21.65 | -71.21 | 1472 |
| 63 | Squeeze breakout | breakout | 89.86 | -10.14 | 92 | 15.2 | -59.57 | -18.50 | -59.92 | 1190 |
| 64 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -5.09 | -0.44 | -19.49 | 407 |
| 65 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 66 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 67 | ROC + volume | momentum | 87.31 | -12.69 | 148 | 18.9 | -72.10 | -17.89 | -72.16 | 1630 |
| 68 | Volume breakout | breakout | 87.23 | -12.77 | 102 | 15.7 | -62.10 | -20.25 | -62.21 | 899 |
| 69 | Donchian 55/20 | breakout | 87.22 | -12.78 | 96 | 15.6 | -67.97 | -15.69 | -68.05 | 1301 |
| 70 | EMA 20/50 cross | trend | 86.90 | -13.11 | 122 | 16.4 | -78.61 | -17.59 | -78.62 | 1470 |
| 71 | Ichimoku | trend | 86.01 | -13.99 | 110 | 9.1 | -80.32 | -26.20 | -80.34 | 1740 |
| 72 | Keltner breakout | breakout | 85.64 | -14.36 | 148 | 13.5 | -84.92 | -34.66 | -84.97 | 1901 |
| 73 | Z-score reversion | reversion | 85.08 | -14.92 | 180 | 32.8 | -84.37 | -27.64 | -84.41 | 2093 |
| 74 | VWAP reversion | reversion | 84.68 | -15.32 | 137 | 22.6 | -71.57 | -17.75 | -71.92 | 1398 |
| 75 | MACD zero-line | trend | 82.52 | -17.48 | 199 | 16.6 | -91.75 | -36.02 | -91.75 | 2355 |
| 76 | Supertrend | trend | 82.49 | -17.51 | 177 | 18.1 | -87.45 | -24.91 | -87.51 | 1960 |
| 77 | Donchian 20/10 | breakout | 81.37 | -18.63 | 203 | 17.7 | -90.95 | -29.69 | -90.96 | 2680 |
| 78 | MFI reversion | reversion | 81.22 | -18.78 | 182 | 19.8 | -88.04 | -36.23 | -88.06 | 2154 |
| 79 | Bollinger breakout | breakout | 81.14 | -18.86 | 202 | 16.8 | -93.91 | -42.20 | -93.92 | 2867 |
| 80 | RSI momentum | momentum | 80.28 | -19.72 | 195 | 13.3 | -90.34 | -29.53 | -90.35 | 2377 |
| 81 | Triple EMA stack | trend | 80.17 | -19.83 | 214 | 15.4 | -93.11 | -36.34 | -93.11 | 2624 |
| 82 | Trend pullback | trend | 79.54 | -20.46 | 168 | 17.3 | -90.91 | -35.30 | -90.91 | 2279 |
| 83 | ADX DI cross | trend | 79.37 | -20.63 | 196 | 8.2 | -89.42 | -47.09 | -89.42 | 2116 |
| 84 | Connors RSI(2) | reversion | 77.12 | -22.88 | 242 | 16.9 | -96.43 | -42.82 | -96.43 | 3629 |
| 85 | EMA 9/21 cross | trend | 76.84 | -23.16 | 277 | 17.3 | -97.42 | -42.26 | -97.42 | 3536 |
| 86 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.59 | -30.32 | -94.60 | 2646 |
| 87 | Candlestick reversal ⏸ | reversion | 76.19 | -23.81 | 268 | 12.7 | -99.35 | -51.09 | -99.35 | 5577 |
| 88 | Stochastic reversion | reversion | 76.05 | -23.95 | 327 | 24.2 | -95.93 | -47.08 | -95.94 | 4060 |
| 89 | OBV trend | momentum | 75.37 | -24.64 | 271 | 15.5 | -95.91 | -48.84 | -95.91 | 3550 |
| 90 | Bollinger reversion | reversion | 74.94 | -25.06 | 304 | 15.8 | -95.77 | -45.34 | -95.77 | 3684 |
| 91 | CCI reversion | reversion | 73.52 | -26.48 | 235 | 11.5 | -98.45 | -51.73 | -98.45 | 4696 |
| 92 | VWAP momentum ⏸ | momentum | 73.33 | -26.67 | 369 | 10.3 | -98.46 | -36.58 | -98.46 | 5194 |
| 93 | Parabolic SAR ⏸ | trend | 72.65 | -27.35 | 270 | 13.0 | -96.99 | -56.58 | -96.99 | 3631 |
| 94 | MACD cross ⏸ | trend | 71.95 | -28.05 | 272 | 14.0 | -99.71 | -67.49 | -99.71 | 6074 |
| 95 | Williams %R ⏸ | reversion | 71.59 | -28.41 | 340 | 21.2 | -99.52 | -60.97 | -99.52 | 6110 |
| 96 | Heikin-Ashi ⏸ | trend | 70.73 | -29.27 | 233 | 3.4 | -99.89 | -87.15 | -99.89 | 8302 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T22:10 | CCI reversion | sell | SOL-USD | 14.72 | -0.02 | exit signal |
| 2026-09-29T22:10 | Stochastic reversion | sell | BTC-USD | 18.96 | -0.07 | exit signal |
| 2026-09-29T22:10 | Triple EMA stack | buy | BTC-USD | 20.06 | — | entry signal |
| 2026-09-29T22:05 | CCI reversion | buy | ETH-USD | 7.26 | — | rebalance up |
| 2026-09-29T22:05 | CCI reversion | sell | DOGE-USD | 14.70 | 0.00 | exit signal |
| 2026-09-29T22:05 | Stochastic reversion | sell | XRP-USD | 19.00 | -0.07 | exit signal |
| 2026-09-29T22:05 | Bollinger reversion | sell | BTC-USD | 18.68 | -0.09 | exit signal |
| 2026-09-29T22:05 | Volume breakout | buy | DOGE-USD | 21.82 | — | entry signal |
| 2026-09-29T22:05 | Bollinger breakout | buy | SOL-USD | 20.31 | — | entry signal |
| 2026-09-29T22:05 | Bollinger breakout | buy | DOGE-USD | 20.31 | — | entry signal |
| 2026-09-29T22:05 | Donchian 20/10 | buy | SOL-USD | 20.37 | — | entry signal |
| 2026-09-29T22:05 | Donchian 20/10 | buy | DOGE-USD | 20.37 | — | entry signal |
| 2026-09-29T22:05 | OBV trend | buy | SOL-USD | 18.87 | — | entry signal |
| 2026-09-29T22:05 | OBV trend | buy | DOGE-USD | 18.87 | — | entry signal |
| 2026-09-29T22:05 | RSI momentum | buy | SOL-USD | 20.10 | — | entry signal |
| 2026-09-29T22:05 | RSI momentum | buy | DOGE-USD | 20.10 | — | entry signal |
| 2026-09-29T22:05 | MACD zero-line | buy | SOL-USD | 20.64 | — | entry signal |
| 2026-09-29T22:05 | Triple EMA stack | buy | SOL-USD | 20.09 | — | entry signal |
| 2026-09-29T22:05 | Triple EMA stack | buy | DOGE-USD | 20.09 | — | entry signal |
| 2026-09-29T22:05 | EMA 20/50 cross | buy | SOL-USD | 21.75 | — | entry signal |
| 2026-09-29T22:05 | EMA 20/50 cross | buy | DOGE-USD | 21.75 | — | entry signal |
| 2026-09-29T22:05 | EMA 9/21 cross | buy | SOL-USD | 19.22 | — | entry signal |
| 2026-09-29T22:00 | Candlestick reversal · 1h | buy | XRP-USD | 1.76 | — | entry |
| 2026-09-29T22:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.80 | — | entry |
| 2026-09-29T22:00 | Candlestick reversal · 1h | sell | BTC-USD | 7.56 | -0.01 | exit signal |
| 2026-09-29T22:00 | Trend pullback · 1h | sell | ETH-USD | 19.11 | -0.23 | exit signal |
| 2026-09-29T22:00 | Heikin-Ashi · 1h | sell | BTC-USD | 23.04 | -0.17 | exit signal |
| 2026-09-29T22:00 | CCI reversion | buy | ETH-USD | 11.17 | — | entry signal |
| 2026-09-29T22:00 | CCI reversion | sell | XRP-USD | 3.70 | -0.02 | rebalance down |
| 2026-09-29T22:00 | CCI reversion | sell | SOL-USD | 3.70 | -0.02 | rebalance down |
| 2026-09-29T22:00 | CCI reversion | sell | DOGE-USD | 3.76 | -0.01 | rebalance down |
| 2026-09-29T21:55 | EMA 9/21 cross | buy | DOGE-USD | 19.23 | — | entry signal |
| 2026-09-29T21:46 | CCI reversion | buy | BTC-USD | 18.28 | — | entry signal |
| 2026-09-29T21:40 | Bollinger reversion | buy | ETH-USD | 18.75 | — | entry signal |
| 2026-09-29T21:35 | MFI reversion | buy | ETH-USD | 20.29 | — | entry signal |
| 2026-09-29T21:35 | Bollinger reversion | buy | BTC-USD | 18.77 | — | entry signal |
| 2026-09-29T21:35 | RSI(14) reversion | buy | ETH-USD | 22.74 | — | entry signal |
| 2026-09-29T21:30 | MFI reversion | sell | ETH-USD | 20.17 | -0.22 | stop-loss |
| 2026-09-29T21:30 | CCI reversion | sell | ETH-USD | 18.28 | -0.18 | stop-loss |
| 2026-09-29T21:30 | Stochastic reversion | buy | ETH-USD | 19.03 | — | entry signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
