"""
Minimal demo of the "Unicorn Edge" strategy from:
  Singha (2025) - Discovery of a 13-Sharpe OOS Factor:
  Drift Regimes Unlock Hidden Cross-Sectional Predictability

Timeline (no look-ahead):
  用T日收盘价计算信号 -> weights[T]
  weights[T] 在 T+1日收盘执行 -> 实现 ret[T+1]
  port_return[T+1] = sum(weights[T] * ret[T+1])

[ASSUMPTION] / [ISSUE] marked inline.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

# ============================================================
# 1. Synthetic price data
# ============================================================
N = 100  # stocks
T = 1260  # days (~5 years)

prices = np.zeros((T, N))
prices[0] = np.random.uniform(20, 200, N)

stock_drift = np.random.normal(0, 0.00015, N)
stock_vol = np.random.uniform(0.015, 0.025, N)
mkt = np.random.normal(0.0003, 0.008, T)

in_drift = np.zeros(N, dtype=bool)
for t in range(1, T):
    for i in range(N):
        in_drift[i] = (np.random.random() < 0.94) if in_drift[i] else (np.random.random() < 0.06)
        mu = (0.003 + stock_drift[i]) if in_drift[i] else (-0.0005 + stock_drift[i])
        sig = stock_vol[i] * (0.6 if in_drift[i] else 1.0)
        prices[t, i] = prices[t-1, i] * (1 + np.random.normal(mu, sig) + 0.3 * mkt[t])

# ret[t] = (P[t] - P[t-1]) / P[t-1], t=1..T-1
ret = np.zeros((T, N))
ret[1:] = np.diff(prices, axis=0) / prices[:-1]

dates = pd.bdate_range("2019-01-01", periods=T)
print(f"Data: {N} stocks, {T} days ({dates[0].date()} ~ {dates[-1].date()})")

# ============================================================
# 2. Signals (computed at each day t using data up to t)
# ============================================================
WARMUP = 63

value = np.full((T, N), np.nan)
reversal = np.full((T, N), np.nan)
regime = np.zeros((T, N))
edge = np.zeros((T, N))

for t in range(WARMUP, T):
    # Value: 1 - percentile_rank(price)
    rank = pd.Series(prices[t]).rank(pct=True).values
    value[t] = 1 - rank

    # Reversal: -sum(ret[t-9:t+1]) -> cross-sectional z-score
    r10 = ret[t-9:t+1].sum(axis=0)  # [ASSUMPTION] 10-day simple return sum
    rev_raw = -r10
    mu, std = rev_raw.mean(), rev_raw.std()
    reversal[t] = (rev_raw - mu) / std if std > 0 else 0

    # BASE
    base = 0.7 * value[t] + 0.3 * reversal[t]  # [ISSUE] different scales

    # Regime: >60% positive days in trailing 63d
    up = (ret[t-62:t+1] > 0).mean(axis=0)
    regime[t] = (up > 0.60).astype(float)

    # EDGE
    edge[t] = base * regime[t]

detected = regime[WARMUP:].mean()
print(f"Detected regime activation: {detected:.1%}")

# ============================================================
# 3. Portfolio weights at day t (applied to ret[t+1])
# ============================================================
# [ASSUMPTION] Rank active EDGE, top=long, bottom=short, equal-weight each side.
weights = np.zeros((T, N))

for t in range(WARMUP, T):
    active_idx = np.where(np.abs(edge[t]) > 1e-10)[0]
    n = len(active_idx)
    if n < 4:
        continue
    scores = edge[t, active_idx]
    order = np.argsort(scores)  # ascending
    mid = n // 2
    short_idx = active_idx[order[:mid]]
    long_idx = active_idx[order[mid:]]
    weights[t, long_idx] = 0.5 / len(long_idx)
    weights[t, short_idx] = -0.5 / len(short_idx)

# ============================================================
# 4. Portfolio returns: port_ret[t+1] = sum(w[t] * ret[t+1])
# ============================================================
port_ret = np.full(T, np.nan)
for t in range(WARMUP, T - 1):
    port_ret[t + 1] = np.nansum(weights[t] * ret[t + 1])

# ============================================================
# 5. Train / Test split
# ============================================================
TRAIN_END = T - 504  # last ~2yr = test

train = port_ret[WARMUP + 1:TRAIN_END + 1]
train = train[~np.isnan(train)]
test = port_ret[TRAIN_END + 1:T]
test = test[~np.isnan(test)]

train_vol = train.std() * np.sqrt(252)
cum_tr = np.cumprod(1 + train)
train_dd = ((cum_tr / np.maximum.accumulate(cum_tr)) - 1).min()

s_star = min(12.0 / train_vol, 15.0 / abs(train_dd)) if train_vol > 0 and train_dd != 0 else 1.0
print(f"Training ({len(train)} days): vol={train_vol:.1%}, maxDD={train_dd:.1%}, s*={s_star:.2f}")

# ============================================================
# 6. Turnover & TC (test period only)
# ============================================================
# turnover between day t and t+1: sum|w[t+1] - w[t]|
test_indices = np.arange(TRAIN_END, T - 1)
to_list = []
for k in range(len(test_indices) - 1):
    to_list.append(np.abs(weights[test_indices[k + 1]] - weights[test_indices[k]]).sum())
turnover = np.array(to_list)

# TC on day test_indices[k+1]: proportional to turnover from k to k+1
# Align: test returns start at TRAIN_END+1, turnover has len-1 entries
tc = np.zeros(len(test))
tc[1:] = 0.6e-4 * turnover  # [ASSUMPTION] 0.6bps on one-way turnover

test_after_tc = test - tc

# ============================================================
# 7. Metrics
# ============================================================
def show(r, label):
    cum = np.cumprod(1 + r)
    dd = cum / np.maximum.accumulate(cum) - 1
    ar = r.mean() * 252
    av = r.std() * np.sqrt(252)
    sr = ar / av if av > 0 else 0
    print(f"\n--- {label} ({len(r)} days) ---")
    print(f"  Ann Return:   {ar:>9.1%}")
    print(f"  Ann Vol:      {av:>9.1%}")
    print(f"  Sharpe:       {sr:>9.2f}")
    print(f"  Max DD:       {dd.min():>9.1%}")
    print(f"  Win Rate:     {(r > 0).mean():>9.1%}")
    print(f"  Final Wealth: {cum[-1]:>8.2f}x")

print(f"\n{'='*55}")
print(f"Test period: day {TRAIN_END}~{T-1} ({dates[TRAIN_END].date()} ~ {dates[T-1].date()})")
show(test_after_tc, "OOS raw (no leverage, s*=1)")
print(f"\n  s* = {s_star:.2f} (would scale returns by this factor)")
print(f"  Avg active stocks: {np.mean([np.sum(np.abs(edge[t]) > 1e-10) for t in range(TRAIN_END, T)]):.0f} / {N}")
print(f"  Avg daily turnover: {turnover.mean():.1%}")
