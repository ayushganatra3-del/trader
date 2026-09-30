# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-30T09:10:05.000125+00:00 · 6716 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £99.62 (-0.38%)

Closed trades 24, win rate 66.7%, fees £0.71, max drawdown -1.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 19.96 | -0.03 |

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

Today: 7200 decisions in 1440 calls, $0.1008 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-30T09:10 | 2 / 3 / 0 | ETH-USD 22%, SOL-USD 22% |  |
| Breezy | 2026-09-30T09:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-30T09:10 | 5 / 0 / 0 | SOL-USD 44%, ETH-USD 44% |  |

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
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 14.13 | 2.65 | -7.93 | 7 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Copy: Congress Democrats (NANC) | copy | 99.78 | -0.22 | 0 | — | 7.21 | 2.93 | -3.62 | 1 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.68 | -0.32 | 6 | 50.0 | 3.17 | 1.61 | -1.84 | 83 |
| 9 | Agent | meta | 99.62 | -0.38 | 24 | 66.7 | -10.10 | -6.72 | -10.75 | 219 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 99.44 | -0.56 | 0 | — | -0.09 | 0.03 | -7.65 | 1 |
| 11 | Agent (aggressive) | meta | 99.42 | -0.58 | 10 | 50.0 | -0.41 | -0.21 | -3.92 | 97 |
| 12 | Hold BTC | benchmark | 99.28 | -0.72 | 0 | — | 28.65 | 3.61 | -8.68 | 1 |
| 13 | Hold SPY | benchmark | 99.21 | -0.79 | 0 | — | 3.46 | 1.93 | -3.66 | 1 |
| 14 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.40 | -5.16 | 27 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.13 | -0.88 | 0 | — | -2.73 | -1.31 | -5.14 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 99.12 | -0.88 | 0 | — | -3.44 | -2.10 | -5.09 | 2 |
| 17 | VWAP reversion · 1h | reversion | 98.99 | -1.01 | 20 | 25.0 | -13.01 | -4.40 | -14.78 | 122 |
| 18 | RSI(14) reversion · 1h | reversion | 98.94 | -1.05 | 7 | 57.1 | 2.43 | 0.68 | -7.03 | 124 |
| 19 | Daily: Bullish score | daily | 98.78 | -1.22 | 2 | 0.0 | -1.05 | 0.05 | -12.76 | 13 |
| 20 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 21 | Z-score reversion · 1h | reversion | 98.67 | -1.33 | 10 | 50.0 | 5.16 | 1.23 | -8.60 | 153 |
| 22 | Copy: Insider buying | copy | 98.61 | -1.39 | 2 | 100.0 | -14.26 | -2.81 | -17.74 | 72 |
| 23 | Gap and go | momentum | 98.45 | -1.55 | 10 | 10.0 | 14.88 | 3.67 | -4.73 | 182 |
| 24 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | 0.10 | 0.20 | -15.21 | 47 |
| 25 | Williams %R · 1h | reversion | 98.29 | -1.71 | 40 | 45.0 | -17.80 | -3.29 | -19.41 | 488 |
| 26 | Stochastic reversion · 1h | reversion | 98.26 | -1.74 | 26 | 53.8 | -14.12 | -3.07 | -15.33 | 331 |
| 27 | Candlestick reversal · 1h | reversion | 98.20 | -1.80 | 25 | 20.0 | -28.10 | -6.90 | -28.74 | 494 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 98.16 | -1.84 | 0 | — | 23.27 | 3.44 | -6.29 | 1 |
| 29 | CCI reversion · 1h | reversion | 97.98 | -2.02 | 35 | 34.3 | 0.48 | 0.25 | -12.41 | 410 |
| 30 | Agent (rotation) | meta | 97.85 | -2.15 | 33 | 12.1 | -5.02 | -1.76 | -11.16 | 207 |
| 31 | Connors RSI(2) · 1h | reversion | 97.65 | -2.35 | 45 | 44.4 | -11.35 | -3.61 | -11.74 | 234 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 97.52 | -2.48 | 0 | — | -11.11 | -2.27 | -15.27 | 2 |
| 33 | EMA 20/50 cross · 1h | trend | 97.47 | -2.53 | 13 | 7.7 | 16.93 | 2.00 | -14.13 | 125 |
| 34 | Max aggression: 5-day momentum | meta | 97.42 | -2.58 | 2 | 50.0 | -8.57 | -0.44 | -29.56 | 29 |
| 35 | Opening range 30m | breakout | 97.17 | -2.83 | 37 | 13.5 | -9.10 | -2.61 | -14.21 | 560 |
| 36 | Squeeze breakout · 1h | breakout | 97.00 | -3.00 | 9 | 11.1 | 15.55 | 2.73 | -5.11 | 92 |
| 37 | Bollinger reversion · 1h | reversion | 97.00 | -3.00 | 22 | 27.3 | -17.53 | -4.88 | -18.15 | 312 |
| 38 | Max aggression: 1-day momentum | meta | 96.39 | -3.61 | 2 | 0.0 | -37.96 | -2.23 | -49.44 | 42 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 96.35 | -3.65 | 0 | — | -9.73 | -2.34 | -11.15 | 1 |
| 40 | Supertrend · 1h | trend | 96.28 | -3.72 | 18 | 5.6 | 1.93 | 0.46 | -16.43 | 194 |
| 41 | Agent (ML meta-label) | meta | 96.15 | -3.85 | 140 | 12.9 | 1.05 | 0.34 | -12.17 | 375 |
| 42 | Trend pullback · 1h | trend | 96.07 | -3.93 | 28 | 10.7 | -28.93 | -7.09 | -29.45 | 147 |
| 43 | MACD cross · 1h | trend | 95.85 | -4.15 | 40 | 10.0 | -18.50 | -3.13 | -21.39 | 460 |
| 44 | Parabolic SAR · 1h | trend | 95.64 | -4.36 | 26 | 11.5 | -7.96 | -0.99 | -18.82 | 293 |
| 45 | Donchian 55/20 · 1h | breakout | 95.58 | -4.42 | 12 | 0.0 | 4.54 | 0.79 | -16.96 | 112 |
| 46 | Opening range 15m | breakout | 95.57 | -4.43 | 48 | 12.5 | -10.72 | -2.85 | -16.91 | 684 |
| 47 | Three white soldiers | momentum | 95.17 | -4.83 | 44 | 18.2 | -50.28 | -27.84 | -50.33 | 607 |
| 48 | MFI reversion · 1h | reversion | 95.14 | -4.86 | 44 | 13.6 | -9.85 | -1.80 | -17.20 | 129 |
| 49 | Ichimoku · 1h | trend | 95.04 | -4.96 | 16 | 18.8 | 6.91 | 1.00 | -15.13 | 122 |
| 50 | Bollinger breakout · 1h | breakout | 94.79 | -5.21 | 17 | 5.9 | 8.30 | 1.26 | -10.10 | 282 |
| 51 | Volume breakout · 1h | breakout | 94.72 | -5.28 | 27 | 3.7 | 5.88 | 0.99 | -12.60 | 125 |
| 52 | RSI momentum · 1h | momentum | 94.09 | -5.91 | 24 | 4.2 | 1.60 | 0.42 | -15.29 | 207 |
| 53 | Keltner breakout · 1h | breakout | 94.02 | -5.98 | 10 | 0.0 | -0.05 | 0.22 | -18.68 | 214 |
| 54 | Donchian 20/10 · 1h | breakout | 94.02 | -5.99 | 16 | 12.5 | 6.99 | 1.08 | -12.78 | 213 |
| 55 | ADX DI cross · 1h | trend | 93.77 | -6.24 | 30 | 6.7 | -16.17 | -2.99 | -17.85 | 256 |
| 56 | MACD zero-line · 1h | trend | 93.73 | -6.27 | 21 | 4.8 | -5.81 | -0.63 | -14.64 | 223 |
| 57 | Triple EMA stack · 1h | trend | 93.72 | -6.28 | 30 | 6.7 | -6.78 | -0.63 | -22.58 | 226 |
| 58 | VWAP momentum · 1h | momentum | 93.43 | -6.57 | 103 | 12.6 | -35.08 | -5.31 | -35.63 | 1240 |
| 59 | Heikin-Ashi · 1h | trend | 92.57 | -7.43 | 45 | 11.1 | -26.24 | -3.97 | -30.59 | 671 |
| 60 | EMA 9/21 cross · 1h | trend | 92.55 | -7.45 | 45 | 11.1 | -4.43 | -0.41 | -16.92 | 309 |
| 61 | OBV trend · 1h | momentum | 92.22 | -7.78 | 54 | 7.4 | -12.73 | -1.39 | -25.19 | 316 |
| 62 | RSI(14) reversion | reversion | 90.79 | -9.21 | 120 | 34.2 | -71.04 | -21.16 | -71.11 | 1470 |
| 63 | ROC + volume · 1h | momentum | 89.24 | -10.76 | 53 | 5.7 | -4.59 | -0.37 | -19.49 | 405 |
| 64 | Squeeze breakout | breakout | 88.51 | -11.49 | 99 | 14.1 | -59.88 | -18.64 | -59.88 | 1192 |
| 65 | Volume breakout | breakout | 87.12 | -12.88 | 103 | 15.5 | -61.82 | -19.79 | -61.89 | 894 |
| 66 | ROC + volume | momentum | 86.68 | -13.32 | 151 | 18.5 | -72.06 | -17.62 | -72.06 | 1626 |
| 67 | Donchian 55/20 | breakout | 86.18 | -13.82 | 100 | 15.0 | -68.14 | -15.67 | -68.14 | 1300 |
| 68 | Keltner breakout | breakout | 85.24 | -14.76 | 150 | 13.3 | -84.74 | -34.09 | -84.74 | 1893 |
| 69 | Ichimoku | trend | 84.26 | -15.74 | 119 | 8.4 | -80.46 | -26.07 | -80.47 | 1742 |
| 70 | EMA 20/50 cross | trend | 84.01 | -15.99 | 135 | 14.8 | -79.15 | -17.76 | -79.15 | 1476 |
| 71 | VWAP reversion | reversion | 83.95 | -16.05 | 143 | 21.7 | -71.72 | -17.61 | -72.02 | 1402 |
| 72 | Z-score reversion | reversion | 83.65 | -16.34 | 193 | 30.6 | -84.58 | -27.48 | -84.60 | 2103 |
| 73 | AI bee: Boozy ⏸ | ai | 82.76 | -17.24 | 104 | 1.0 | — | — | — | — |
| 74 | AI bee: Bizzy ⏸ | ai | 82.73 | -17.27 | 288 | 9.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 80.12 | -19.88 | 189 | 19.0 | -88.11 | -35.37 | -88.15 | 2150 |
| 76 | Donchian 20/10 | breakout | 79.52 | -20.48 | 213 | 16.9 | -90.91 | -29.68 | -90.91 | 2674 |
| 77 | Supertrend | trend | 79.49 | -20.51 | 191 | 16.8 | -87.69 | -24.96 | -87.72 | 1962 |
| 78 | MACD zero-line | trend | 79.33 | -20.67 | 217 | 15.2 | -91.92 | -36.22 | -91.92 | 2360 |
| 79 | Bollinger breakout | breakout | 79.08 | -20.92 | 215 | 15.8 | -93.89 | -42.14 | -93.89 | 2863 |
| 80 | Trend pullback | trend | 78.55 | -21.45 | 174 | 16.7 | -90.58 | -33.23 | -90.58 | 2259 |
| 81 | Triple EMA stack | trend | 77.77 | -22.23 | 226 | 14.6 | -93.14 | -36.27 | -93.14 | 2621 |
| 82 | RSI momentum | momentum | 77.50 | -22.50 | 209 | 12.4 | -90.58 | -29.48 | -90.58 | 2383 |
| 83 | ADX DI cross | trend | 77.28 | -22.71 | 210 | 7.6 | -89.49 | -45.90 | -89.49 | 2116 |
| 84 | Connors RSI(2) | reversion | 76.96 | -23.05 | 243 | 16.9 | -96.29 | -39.22 | -96.29 | 3600 |
| 85 | Consensus | meta | 76.82 | -23.18 | 189 | 7.4 | -94.58 | -29.54 | -94.59 | 2644 |
| 86 | Stochastic reversion | reversion | 74.89 | -25.11 | 343 | 23.3 | -95.93 | -44.89 | -95.94 | 4058 |
| 87 | Candlestick reversal | reversion | 73.78 | -26.22 | 293 | 11.9 | -99.37 | -49.60 | -99.37 | 5596 |
| 88 | Bollinger reversion | reversion | 73.28 | -26.72 | 323 | 14.9 | -95.80 | -43.45 | -95.80 | 3687 |
| 89 | EMA 9/21 cross | trend | 73.20 | -26.80 | 301 | 15.9 | -97.47 | -41.93 | -97.47 | 3540 |
| 90 | OBV trend | momentum | 72.06 | -27.94 | 290 | 14.5 | -95.96 | -48.97 | -95.96 | 3552 |
| 91 | CCI reversion | reversion | 71.00 | -29.00 | 262 | 10.7 | -98.47 | -49.71 | -98.47 | 4704 |
| 92 | Parabolic SAR | trend | 70.85 | -29.15 | 281 | 12.5 | -97.00 | -55.05 | -97.00 | 3629 |
| 93 | MACD cross | trend | 68.99 | -31.01 | 295 | 12.9 | -99.72 | -65.26 | -99.72 | 6081 |
| 94 | VWAP momentum ⏸ | momentum | 68.71 | -31.29 | 409 | 9.3 | -98.57 | -36.43 | -98.57 | 5235 |
| 95 | Heikin-Ashi | trend | 68.59 | -31.41 | 252 | 3.2 | -99.89 | -78.38 | -99.89 | 8299 |
| 96 | Williams %R | reversion | 68.59 | -31.41 | 370 | 19.7 | -99.53 | -57.56 | -99.53 | 6114 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-30T09:10 | Williams %R | sell | SOL-USD | 17.15 | -0.04 | exit signal |
| 2026-09-30T09:10 | Stochastic reversion | sell | SOL-USD | 18.69 | -0.04 | exit signal |
| 2026-09-30T09:10 | Z-score reversion | sell | SOL-USD | 20.85 | -0.14 | exit signal |
| 2026-09-30T09:10 | Candlestick reversal | sell | XRP-USD | 18.57 | -0.02 | time stop |
| 2026-09-30T09:10 | OBV trend | buy | ETH-USD | 18.04 | — | entry signal |
| 2026-09-30T09:10 | OBV trend | buy | DOGE-USD | 18.04 | — | entry signal |
| 2026-09-30T09:10 | RSI momentum | buy | ETH-USD | 19.39 | — | entry signal |
| 2026-09-30T09:10 | Heikin-Ashi | buy | SOL-USD | 17.16 | — | entry signal |
| 2026-09-30T09:10 | Parabolic SAR | buy | BTC-USD | 17.73 | — | entry signal |
| 2026-09-30T09:10 | MACD cross | buy | BTC-USD | 3.50 | — | entry signal |
| 2026-09-30T09:10 | MACD cross | sell | SOL-USD | 3.46 | -0.01 | rebalance down |
| 2026-09-30T09:10 | Triple EMA stack | buy | ETH-USD | 19.47 | — | entry signal |
| 2026-09-30T09:10 | Triple EMA stack | buy | DOGE-USD | 19.47 | — | entry signal |
| 2026-09-30T09:10 | EMA 20/50 cross | buy | DOGE-USD | 21.02 | — | entry signal |
| 2026-09-30T09:05 | CCI reversion | buy | BTC-USD | 17.76 | — | entry signal |
| 2026-09-30T09:05 | Williams %R | sell | ETH-USD | 17.11 | -0.06 | exit signal |
| 2026-09-30T09:05 | Williams %R | sell | DOGE-USD | 17.13 | -0.05 | exit signal |
| 2026-09-30T09:05 | Candlestick reversal | buy | BTC-USD | 18.22 | — | entry signal |
| 2026-09-30T09:05 | Ichimoku | buy | XRP-USD | 21.08 | — | entry signal |
| 2026-09-30T09:05 | Parabolic SAR | buy | XRP-USD | 17.75 | — | entry signal |
| 2026-09-30T09:05 | Parabolic SAR | buy | DOGE-USD | 17.75 | — | entry signal |
| 2026-09-30T09:05 | MACD zero-line | buy | XRP-USD | 19.85 | — | entry signal |
| 2026-09-30T09:05 | MACD cross | buy | DOGE-USD | 17.26 | — | entry signal |
| 2026-09-30T09:05 | Triple EMA stack | buy | XRP-USD | 19.49 | — | entry signal |
| 2026-09-30T09:05 | EMA 20/50 cross | buy | XRP-USD | 21.05 | — | entry signal |
| 2026-09-30T09:05 | EMA 20/50 cross | buy | ETH-USD | 21.05 | — | entry signal |
| 2026-09-30T09:05 | EMA 9/21 cross | buy | XRP-USD | 18.31 | — | entry signal |
| 2026-09-30T09:00 | VWAP reversion | buy | BTC-USD | 20.97 | — | entry signal |
| 2026-09-30T09:00 | MACD cross | buy | ETH-USD | 17.24 | — | entry signal |
| 2026-09-30T09:00 | EMA 9/21 cross | buy | DOGE-USD | 18.31 | — | entry signal |
| 2026-09-30T08:55 | Candlestick reversal | sell | BTC-USD | 18.22 | -0.13 | exit signal |
| 2026-09-30T08:55 | MACD cross | buy | XRP-USD | 17.27 | — | entry signal |
| 2026-09-30T08:55 | MACD cross | buy | SOL-USD | 17.27 | — | entry signal |
| 2026-09-30T08:50 | Parabolic SAR | buy | ETH-USD | 17.76 | — | entry signal |
| 2026-09-30T08:50 | EMA 9/21 cross | buy | ETH-USD | 18.33 | — | entry signal |
| 2026-09-30T08:40 | Williams %R | buy | ETH-USD | 17.18 | — | entry signal |
| 2026-09-30T08:40 | Williams %R | buy | DOGE-USD | 17.18 | — | entry signal |
| 2026-09-30T08:40 | Williams %R | buy | BTC-USD | 17.18 | — | entry signal |
| 2026-09-30T08:40 | Candlestick reversal | buy | BTC-USD | 18.35 | — | entry signal |
| 2026-09-30T08:35 | Heikin-Ashi | sell | DOGE-USD | 17.06 | -0.14 | exit signal |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
