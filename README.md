# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-09-29T06:10:05.000181+00:00 · 5378 ticks

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

Today: 4495 decisions in 899 calls, $0.0630 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-09-29T06:10 | 4 / 1 / 0 | SOL-USD 22%, BTC-USD 22%, ETH-USD 17%, DOGE-USD 16% |  |
| Breezy | 2026-09-29T06:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-09-29T06:10 | 5 / 0 / 0 | SOL-USD 44%, BTC-USD 43% |  |

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
| 3 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 5 | 60.0 | 2.50 | 1.29 | -2.47 | 91 |
| 4 | Agent (aggressive) | meta | 100.24 | 0.24 | 8 | 62.5 | 1.06 | 0.62 | -4.81 | 91 |
| 5 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.24 | 0.24 | 1 | 100.0 | -4.74 | -1.39 | -12.40 | 25 |
| 6 | Hold BTC | benchmark | 100.11 | 0.11 | 0 | — | 29.66 | 3.73 | -8.68 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.00 | 0.00 | 0 | — | 7.02 | 1.33 | -7.93 | 7 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent | meta | 99.98 | -0.02 | 17 | 70.6 | -8.27 | -4.98 | -9.84 | 203 |
| 11 | RSI(14) reversion · 1h | reversion | 99.87 | -0.13 | 2 | 100.0 | 15.15 | 3.17 | -6.57 | 136 |
| 12 | Copy: Warren Buffett (BRK-B) | copy | 99.81 | -0.19 | 0 | — | -1.17 | -0.43 | -7.65 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 99.80 | -0.20 | 0 | — | 8.06 | 3.08 | -3.62 | 1 |
| 14 | Hold SPY | benchmark | 99.59 | -0.41 | 0 | — | 4.05 | 2.09 | -3.66 | 1 |
| 15 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 20 | 25.0 | -12.87 | -4.39 | -14.72 | 121 |
| 16 | Gap and go | momentum | 99.30 | -0.70 | 6 | 16.7 | 16.36 | 4.05 | -4.73 | 190 |
| 17 | Daily: Bullish score | daily | 99.30 | -0.70 | 2 | 0.0 | -0.94 | 0.07 | -12.76 | 13 |
| 18 | Three white soldiers · 1h | momentum | 99.15 | -0.85 | 2 | 0.0 | -2.95 | -2.42 | -5.16 | 27 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 99.15 | -0.85 | 0 | — | -3.63 | -2.24 | -5.09 | 2 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 99.13 | -0.87 | 0 | — | -7.89 | -1.93 | -12.73 | 1 |
| 21 | Connors RSI(2) · 1h | reversion | 99.12 | -0.88 | 39 | 48.7 | -11.79 | -3.73 | -13.27 | 234 |
| 22 | Z-score reversion · 1h | reversion | 99.05 | -0.95 | 4 | 25.0 | 3.67 | 0.92 | -8.60 | 155 |
| 23 | Copy: Hedge-fund gurus (GURU) | copy | 99.04 | -0.96 | 0 | — | -1.97 | -0.91 | -5.14 | 1 |
| 24 | Stochastic reversion · 1h | reversion | 99.03 | -0.97 | 23 | 56.5 | -12.45 | -2.76 | -13.85 | 324 |
| 25 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.74 | -1.26 | 1 | 0.0 | -0.41 | -0.10 | -4.88 | 16 |
| 26 | Williams %R · 1h | reversion | 98.65 | -1.35 | 30 | 50.0 | -17.63 | -3.22 | -19.83 | 490 |
| 27 | Copy: Insider buying | copy | 98.62 | -1.38 | 2 | 100.0 | -14.51 | -2.89 | -17.74 | 72 |
| 28 | CCI reversion · 1h | reversion | 98.61 | -1.39 | 24 | 33.3 | 1.54 | 0.42 | -12.41 | 405 |
| 29 | Agent (rotation) | meta | 98.45 | -1.55 | 27 | 14.8 | -7.32 | -2.59 | -11.75 | 233 |
| 30 | Daily: Momentum burst | daily | 98.36 | -1.64 | 3 | 0.0 | -1.49 | -0.05 | -15.21 | 47 |
| 31 | Candlestick reversal · 1h | reversion | 98.21 | -1.79 | 12 | 16.7 | -25.81 | -6.03 | -26.26 | 490 |
| 32 | Opening range 30m | breakout | 98.20 | -1.80 | 31 | 12.9 | -9.01 | -2.59 | -13.54 | 562 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 98.14 | -1.86 | 0 | — | 25.09 | 3.62 | -6.29 | 1 |
| 34 | Squeeze breakout · 1h | breakout | 98.04 | -1.96 | 7 | 14.3 | 16.37 | 2.87 | -6.26 | 93 |
| 35 | Supertrend · 1h | trend | 97.95 | -2.05 | 11 | 9.1 | 5.45 | 0.92 | -16.43 | 194 |
| 36 | EMA 20/50 cross · 1h | trend | 97.94 | -2.06 | 8 | 12.5 | 15.62 | 1.87 | -14.36 | 125 |
| 37 | Bollinger reversion · 1h | reversion | 97.38 | -2.62 | 19 | 31.6 | -17.70 | -4.92 | -17.79 | 306 |
| 38 | Donchian 55/20 · 1h | breakout | 97.27 | -2.73 | 8 | 0.0 | 4.53 | 0.80 | -16.96 | 113 |
| 39 | Opening range 15m | breakout | 97.23 | -2.77 | 38 | 13.2 | -10.12 | -2.74 | -16.14 | 692 |
| 40 | Timing: Nasdaq FTD · TQQQ | daily | 97.20 | -2.80 | 0 | — | -11.60 | -2.41 | -15.27 | 2 |
| 41 | Agent (ML meta-label) | meta | 97.14 | -2.86 | 79 | 10.1 | 0.67 | 0.28 | -11.44 | 388 |
| 42 | MACD cross · 1h | trend | 97.12 | -2.88 | 31 | 9.7 | -16.10 | -2.72 | -20.52 | 458 |
| 43 | Trend pullback · 1h | trend | 97.12 | -2.88 | 22 | 13.6 | -25.74 | -6.83 | -26.36 | 148 |
| 44 | Parabolic SAR · 1h | trend | 96.99 | -3.01 | 20 | 15.0 | -5.60 | -0.64 | -18.82 | 300 |
| 45 | Bollinger breakout · 1h | breakout | 96.91 | -3.09 | 13 | 7.7 | 13.27 | 1.88 | -9.85 | 284 |
| 46 | MACD zero-line · 1h | trend | 96.55 | -3.45 | 15 | 6.7 | -3.46 | -0.30 | -14.64 | 218 |
| 47 | RSI momentum · 1h | momentum | 96.48 | -3.52 | 20 | 5.0 | 1.57 | 0.42 | -15.29 | 212 |
| 48 | Max aggression: 5-day momentum | meta | 96.07 | -3.93 | 1 | 0.0 | -0.43 | 0.31 | -29.56 | 29 |
| 49 | Triple EMA stack · 1h | trend | 96.04 | -3.96 | 24 | 8.3 | -2.82 | -0.12 | -22.95 | 223 |
| 50 | Ichimoku · 1h | trend | 95.97 | -4.03 | 11 | 9.1 | 8.17 | 1.14 | -15.13 | 119 |
| 51 | EMA 9/21 cross · 1h | trend | 95.94 | -4.06 | 34 | 11.8 | 3.08 | 0.62 | -16.92 | 310 |
| 52 | ADX DI cross · 1h | trend | 95.88 | -4.12 | 25 | 8.0 | -11.67 | -2.19 | -15.39 | 249 |
| 53 | Donchian 20/10 · 1h | breakout | 95.83 | -4.17 | 12 | 16.7 | 12.05 | 1.69 | -12.78 | 213 |
| 54 | MFI reversion · 1h | reversion | 95.77 | -4.23 | 38 | 13.2 | -9.25 | -1.69 | -17.20 | 125 |
| 55 | Max aggression: 1-day momentum | meta | 95.63 | -4.37 | 1 | 0.0 | -32.05 | -1.79 | -49.41 | 42 |
| 56 | OBV trend · 1h | momentum | 95.47 | -4.53 | 47 | 6.4 | -9.59 | -1.00 | -25.24 | 317 |
| 57 | Three white soldiers | momentum | 95.37 | -4.62 | 37 | 10.8 | -51.97 | -28.82 | -52.21 | 626 |
| 58 | Volume breakout · 1h | breakout | 95.18 | -4.82 | 25 | 4.0 | 6.26 | 1.05 | -12.60 | 126 |
| 59 | VWAP momentum · 1h | momentum | 95.16 | -4.84 | 82 | 7.3 | -31.96 | -4.72 | -34.09 | 1250 |
| 60 | Keltner breakout · 1h | breakout | 95.13 | -4.87 | 7 | 0.0 | -0.22 | 0.18 | -18.68 | 220 |
| 61 | Heikin-Ashi · 1h | trend | 94.33 | -5.67 | 35 | 11.4 | -22.62 | -3.37 | -29.24 | 678 |
| 62 | ROC + volume · 1h | momentum | 91.92 | -8.08 | 44 | 6.8 | -4.15 | -0.38 | -17.46 | 403 |
| 63 | RSI(14) reversion | reversion | 91.84 | -8.16 | 93 | 34.4 | -71.24 | -22.02 | -71.32 | 1474 |
| 64 | Squeeze breakout | breakout | 89.25 | -10.75 | 71 | 5.6 | -60.23 | -18.94 | -60.46 | 1185 |
| 65 | ROC + volume | momentum | 89.21 | -10.79 | 115 | 16.5 | -71.79 | -17.80 | -72.38 | 1655 |
| 66 | Donchian 55/20 | breakout | 88.68 | -11.32 | 77 | 11.7 | -68.39 | -15.87 | -68.54 | 1330 |
| 67 | Volume breakout | breakout | 88.48 | -11.52 | 76 | 9.2 | -62.43 | -20.52 | -62.47 | 909 |
| 68 | AI bee: Boozy ⏸ | ai | 88.30 | -11.70 | 66 | 1.5 | — | — | — | — |
| 69 | AI bee: Bizzy ⏸ | ai | 88.10 | -11.90 | 227 | 11.9 | — | — | — | — |
| 70 | Ichimoku | trend | 87.68 | -12.32 | 85 | 8.2 | -80.30 | -26.00 | -80.30 | 1750 |
| 71 | EMA 20/50 cross | trend | 87.57 | -12.43 | 97 | 13.4 | -79.00 | -17.86 | -79.30 | 1488 |
| 72 | Keltner breakout | breakout | 87.29 | -12.71 | 120 | 10.0 | -85.03 | -35.28 | -85.03 | 1933 |
| 73 | Z-score reversion | reversion | 85.70 | -14.30 | 150 | 30.0 | -84.73 | -28.59 | -84.80 | 2089 |
| 74 | VWAP reversion | reversion | 85.25 | -14.75 | 105 | 14.3 | -71.35 | -17.58 | -71.87 | 1417 |
| 75 | Supertrend | trend | 84.07 | -15.93 | 143 | 15.4 | -87.26 | -24.85 | -87.47 | 1964 |
| 76 | MACD zero-line | trend | 83.80 | -16.20 | 159 | 15.1 | -91.60 | -36.33 | -91.77 | 2365 |
| 77 | Trend pullback | trend | 83.19 | -16.81 | 140 | 15.7 | -90.50 | -33.62 | -90.50 | 2280 |
| 78 | Donchian 20/10 | breakout | 82.65 | -17.35 | 162 | 14.8 | -91.00 | -30.41 | -91.07 | 2693 |
| 79 | Bollinger breakout | breakout | 82.51 | -17.49 | 165 | 13.9 | -94.04 | -43.14 | -94.06 | 2882 |
| 80 | RSI momentum | momentum | 82.46 | -17.54 | 153 | 10.5 | -90.47 | -30.40 | -90.64 | 2404 |
| 81 | Triple EMA stack | trend | 82.35 | -17.65 | 173 | 13.3 | -92.99 | -37.29 | -93.07 | 2624 |
| 82 | MFI reversion | reversion | 82.15 | -17.86 | 153 | 17.0 | -87.80 | -34.93 | -87.92 | 2169 |
| 83 | ADX DI cross | trend | 81.43 | -18.57 | 167 | 6.6 | -89.48 | -49.08 | -89.48 | 2132 |
| 84 | Connors RSI(2) | reversion | 81.11 | -18.89 | 200 | 17.0 | -96.36 | -40.96 | -96.36 | 3648 |
| 85 | Consensus | meta | 79.26 | -20.74 | 156 | 7.1 | -94.71 | -30.27 | -94.71 | 2660 |
| 86 | EMA 9/21 cross | trend | 79.02 | -20.98 | 223 | 13.5 | -97.40 | -42.78 | -97.43 | 3550 |
| 87 | Candlestick reversal | reversion | 78.66 | -21.34 | 201 | 13.9 | -99.36 | -53.12 | -99.36 | 5564 |
| 88 | Stochastic reversion | reversion | 78.43 | -21.57 | 258 | 23.3 | -95.94 | -49.07 | -95.95 | 4057 |
| 89 | OBV trend | momentum | 77.89 | -22.11 | 225 | 12.4 | -95.84 | -51.39 | -95.87 | 3566 |
| 90 | Bollinger reversion | reversion | 77.13 | -22.87 | 246 | 12.6 | -95.81 | -46.96 | -95.81 | 3681 |
| 91 | Parabolic SAR | trend | 75.53 | -24.47 | 237 | 11.8 | -96.94 | -58.51 | -96.96 | 3656 |
| 92 | CCI reversion | reversion | 75.22 | -24.78 | 176 | 5.7 | -98.48 | -53.72 | -98.48 | 4706 |
| 93 | VWAP momentum | momentum | 75.07 | -24.93 | 301 | 9.0 | -98.50 | -37.52 | -98.51 | 5223 |
| 94 | MACD cross | trend | 74.12 | -25.88 | 195 | 8.7 | -99.71 | -68.94 | -99.71 | 6100 |
| 95 | Williams %R | reversion | 74.01 | -25.99 | 256 | 19.5 | -99.53 | -63.75 | -99.53 | 6097 |
| 96 | Heikin-Ashi | trend | 72.28 | -27.71 | 215 | 3.3 | -99.89 | -92.29 | -99.89 | 8328 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-09-29T06:10 | Consensus | buy | SOL-USD | 19.86 | — | entry |
| 2026-09-29T06:10 | Consensus | buy | ETH-USD | 19.86 | — | entry |
| 2026-09-29T06:10 | Consensus | buy | DOGE-USD | 19.86 | — | entry |
| 2026-09-29T06:10 | Volume breakout | buy | ETH-USD | 22.13 | — | entry signal |
| 2026-09-29T06:10 | Volume breakout | buy | DOGE-USD | 22.17 | — | entry signal |
| 2026-09-29T06:10 | Volume breakout | buy | BTC-USD | 22.17 | — | entry signal |
| 2026-09-29T06:10 | Squeeze breakout | buy | XRP-USD | 22.35 | — | entry signal |
| 2026-09-29T06:10 | Squeeze breakout | buy | SOL-USD | 22.35 | — | entry signal |
| 2026-09-29T06:10 | Keltner breakout | buy | XRP-USD | 13.13 | — | entry signal |
| 2026-09-29T06:10 | Keltner breakout | buy | SOL-USD | 17.50 | — | entry signal |
| 2026-09-29T06:10 | Keltner breakout | buy | ETH-USD | 17.50 | — | entry signal |
| 2026-09-29T06:10 | Keltner breakout | buy | DOGE-USD | 17.50 | — | entry signal |
| 2026-09-29T06:10 | Bollinger breakout | buy | XRP-USD | 12.40 | — | entry signal |
| 2026-09-29T06:10 | Bollinger breakout | buy | SOL-USD | 16.53 | — | entry signal |
| 2026-09-29T06:10 | Bollinger breakout | buy | DOGE-USD | 16.53 | — | entry signal |
| 2026-09-29T06:10 | Bollinger breakout | sell | BTC-USD | 4.14 | -0.01 | rebalance down |
| 2026-09-29T06:10 | Donchian 55/20 | buy | SOL-USD | 4.43 | — | rebalance up |
| 2026-09-29T06:10 | Donchian 55/20 | sell | DOGE-USD | 4.43 | -0.00 | rebalance down |
| 2026-09-29T06:10 | OBV trend | buy | ETH-USD | 3.89 | — | rebalance up |
| 2026-09-29T06:10 | OBV trend | sell | SOL-USD | 3.89 | 0.01 | rebalance down |
| 2026-09-29T06:10 | ROC + volume | buy | SOL-USD | 22.28 | — | entry signal |
| 2026-09-29T06:10 | ROC + volume | buy | ETH-USD | 22.35 | — | entry signal |
| 2026-09-29T06:10 | ROC + volume | buy | BTC-USD | 22.35 | — | entry signal |
| 2026-09-29T06:07 | RSI momentum | buy | XRP-USD | 8.21 | — | rebalance up |
| 2026-09-29T06:07 | RSI momentum | sell | DOGE-USD | 4.11 | -0.02 | rebalance down |
| 2026-09-29T06:07 | RSI momentum | sell | BTC-USD | 4.10 | -0.02 | rebalance down |
| 2026-09-29T06:05 | MFI reversion | sell | BTC-USD | 20.60 | 0.02 | exit signal |
| 2026-09-29T06:05 | Candlestick reversal | sell | ETH-USD | 19.63 | -0.05 | exit signal |
| 2026-09-29T06:05 | Volume breakout | buy | SOL-USD | 22.16 | — | entry signal |
| 2026-09-29T06:05 | Squeeze breakout | buy | ETH-USD | 22.34 | — | entry signal |
| 2026-09-29T06:05 | Keltner breakout | buy | BTC-USD | 21.87 | — | entry signal |
| 2026-09-29T06:05 | Bollinger breakout | buy | ETH-USD | 20.65 | — | entry signal |
| 2026-09-29T06:05 | RSI momentum | buy | XRP-USD | 4.17 | — | entry signal |
| 2026-09-29T06:05 | RSI momentum | buy | SOL-USD | 16.45 | — | entry signal |
| 2026-09-29T06:03 | Heikin-Ashi | buy | SOL-USD | 7.18 | — | rebalance up |
| 2026-09-29T06:03 | Heikin-Ashi | sell | DOGE-USD | 3.59 | -0.02 | rebalance down |
| 2026-09-29T06:03 | Heikin-Ashi | sell | BTC-USD | 3.59 | -0.02 | rebalance down |
| 2026-09-29T06:02 | Donchian 55/20 | buy | SOL-USD | 4.40 | — | rebalance up |
| 2026-09-29T06:02 | Donchian 55/20 | sell | XRP-USD | 4.40 | -0.02 | rebalance down |
| 2026-09-29T06:02 | Heikin-Ashi | buy | SOL-USD | 3.60 | — | rebalance up |

## Data problems on the last tick

- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
