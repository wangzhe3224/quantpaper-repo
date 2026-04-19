"""
demo.py — 最小化复现 Poh et al. (2020) 的核心方法
"Building Cross-Sectional Systematic Strategies by Learning to Rank"

对比三种分数计算方法 (对应论文第IV节):
  1. 启发式 (JT):  12个月累计收益 → 公式(5)
  2. MLP回归:      MSE损失训练     → 公式(10-11)
  3. LambdaMART:   成对排序损失    → 第IV-C节
"""

import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

try:
    from xgboost import XGBRanker
except ImportError:
    XGBRanker = None

np.random.seed(42)

# ══════════════════════════════════════════════
# 1. 合成数据 (模拟含动量效应的月度收益)
# ══════════════════════════════════════════════
N_STOCKS = 200
N_MONTHS = 300
TRAIN_WINDOW = 60  # 每5年重训练 (对应论文第V-B节)

returns = np.random.randn(N_MONTHS, N_STOCKS) * 0.06
for t in range(12, N_MONTHS):
    momentum = returns[t - 12:t].sum(axis=0)
    returns[t] += 0.01 * momentum  # 微弱动量溢价


# ══════════════════════════════════════════════
# 2. 特征工程 (对应论文第V-B节的预测因子)
# ══════════════════════════════════════════════
def make_features(ret, t):
    """特征: 过去3/6/12个月累计收益 → 公式(5)的变体"""
    cols = []
    for h in (3, 6, 12):
        cols.append(ret[t - h:t].sum(axis=0) if t >= h else np.zeros(N_STOCKS))
    return np.column_stack(cols)


def to_decile_labels(y):
    """收益 → 十分位标签 (0=最低, 9=最高), 用于LTR训练"""
    ranks = np.argsort(np.argsort(y))
    return (ranks * 10 // len(y)).astype(int)


# ══════════════════════════════════════════════
# 3. 组合构建 (对应论文公式 1-4)
# ══════════════════════════════════════════════
def long_short_return(scores, next_ret, long_pct=0.1, short_pct=0.1):
    """
    公式(3): 排名 → 公式(4): 选前10%做多、后10%做空 → 公式(1): 组合收益
    """
    n = len(scores)
    ranks = np.argsort(np.argsort(scores))  # 0=最低分
    long_ret = next_ret[ranks >= n - int(n * long_pct)].mean()
    short_ret = next_ret[ranks < int(n * short_pct)].mean()
    return long_ret - short_ret


# ══════════════════════════════════════════════
# 4. 滚动回测 (对应论文第V-B节: 每5年重调优)
# ══════════════════════════════════════════════
REBAL_START = 24  # 需要至少12个月来计算特征
perf = {"JT (启发式)": [], "MLP (MSE回归)": []}
if XGBRanker:
    perf["LambdaMART (LTR)"] = []

mlp, ltr_model = None, None
last_train = -999

for t in range(REBAL_START, N_MONTHS - 1):
    X = make_features(returns, t)
    y = returns[t + 1]

    # 方法1: 启发式 — 分数 = 12个月累计收益
    perf["JT (启发式)"].append(long_short_return(X[:, 2], y))

    # 每5年重训练
    if t - last_train >= TRAIN_WINDOW or mlp is None:
        last_train = t
        t0 = max(12, t - TRAIN_WINDOW)

        Xs, ys, labs, grps = [], [], [], []
        for s in range(t0, t):
            Xs.append(make_features(returns, s))
            ys.append(returns[s + 1])
            labs.append(to_decile_labels(returns[s + 1]))
            grps.append(N_STOCKS)

        X_all, y_all = np.vstack(Xs), np.concatenate(ys)
        lab_all = np.concatenate(labs)

        # 方法2: MLP — MSE回归 (公式11)
        mlp = MLPRegressor(
            hidden_layer_sizes=(128, 64), max_iter=200,
            early_stopping=True, validation_fraction=0.1, random_state=0,
        )
        mlp.fit(X_all, y_all)

        # 方法3: LambdaMART — 成对排序
        if XGBRanker:
            ltr_model = XGBRanker(
                objective="rank:pairwise", n_estimators=80,
                max_depth=4, learning_rate=0.1, random_state=0,
            )
            ltr_model.fit(X_all, lab_all, group=grps)

    perf["MLP (MSE回归)"].append(long_short_return(mlp.predict(X), y))

    if XGBRanker and ltr_model:
        perf["LambdaMART (LTR)"].append(long_short_return(ltr_model.predict(X), y))


# ══════════════════════════════════════════════
# 5. 绩效评估 (对应论文第V-C节)
# ══════════════════════════════════════════════
print(f"\n{'方法':<22} {'月均收益':>8} {'月波动':>8} {'年化夏普':>8} {'最大回撤':>8}")
print("─" * 60)

for name, rets in perf.items():
    r = np.array(rets)
    mu, sigma = r.mean(), r.std()
    sharpe = mu / sigma * np.sqrt(12)
    cum = np.cumprod(1 + r)
    peak = np.maximum.accumulate(cum)
    mdd = ((cum - peak) / peak).min()
    print(f"{name:<22} {mu:>+8.4f} {sigma:>8.4f} {sharpe:>8.3f} {mdd:>+8.2%}")

# 累计收益曲线 (对应论文图1)
plt.figure(figsize=(10, 5))
for name, rets in perf.items():
    plt.plot(np.cumprod(1 + np.array(rets)), label=name)
plt.title("Cumulative Returns - LTR vs Baselines (Synthetic Data)")
plt.xlabel("Rebalancing Month")
plt.ylabel("Cumulative Return")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("demo_output.png", dpi=150)
print("\n图表已保存: demo_output.png")
