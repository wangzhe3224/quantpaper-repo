"""
Replicate: Detecting Cross-Firm Momentum Effects via Shared Analyst Coverage — The Role of Leaders
Paper: 5587812 (Mao, Shi, Chen, Wan)

Standalone, instructional script using synthetic data. Demonstrates:
  1. Build analyst coverage networks
  2. Compute 5 weighting schemes (AH, Isr, MRX, Sor, SC)
  3. Construct connected-firm returns (CF Ret)
  4. Univariate portfolio analysis (decile sorts, long-short)
  5. Spanning tests
  6. Fama-MacBeth regressions
  7. SC characteristics analysis
  8. Leader-laggard bivariate sorts

Usage:
    conda activate quantfactor-ws
    python replicate_model.py
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.sparse import csr_matrix, lil_matrix
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import defaultdict
import os, warnings

warnings.filterwarnings("ignore")
np.random.seed(42)

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# =============================================================================
# 1. Synthetic Data Generation
# =============================================================================
print("=" * 70)
print("1. GENERATING SYNTHETIC DATA")
print("=" * 70)

N_STOCKS = 300
N_MONTHS = 120
N_ANALYSTS = 150
ANALYST_MIN_COV = 4
ANALYST_MAX_COV = 20

stock_ids = [f"S{i:04d}" for i in range(N_STOCKS)]
months = pd.date_range("2015-01-01", periods=N_MONTHS, freq="MS")

# Latent importance (power-law: a few hubs, many peripherals)
stock_importance = np.random.pareto(1.5, N_STOCKS) + 1
stock_importance /= stock_importance.sum()

# Analyst portfolios (importance-driven)
analyst_portfolios = {}
for a in range(N_ANALYSTS):
    n_cover = np.random.randint(ANALYST_MIN_COV, ANALYST_MAX_COV + 1)
    probs = stock_importance.copy()
    chosen = np.random.choice(N_STOCKS, size=n_cover, replace=False, p=probs / probs.sum())
    analyst_portfolios[a] = set(chosen)

# Analyst active windows (temporal variation)
analyst_start = np.random.randint(0, 24, N_ANALYSTS)
analyst_end = analyst_start + np.random.randint(60, N_MONTHS, N_ANALYSTS)
analyst_end = np.clip(analyst_end, 0, N_MONTHS)

# Build coverage as sparse bipartite matrices: stock-analyst
# coverage_mat[m] = sparse (N_STOCKS x N_ANALYSTS), 1 if analyst a covers stock s at month m
print("  Building coverage matrices...")
coverage_mats = []
for m in range(N_MONTHS):
    mat = lil_matrix((N_STOCKS, N_ANALYSTS), dtype=np.float64)
    for a in range(N_ANALYSTS):
        if analyst_start[a] <= m < analyst_end[a]:
            for s in analyst_portfolios[a]:
                mat[s, a] = 1.0
    coverage_mats.append(mat.tocsr())

# Stock characteristics
stock_sizes = np.exp(np.random.normal(15, 1.2, N_STOCKS))
market_beta = np.random.normal(1.0, 0.3, N_STOCKS)
inst_ownership = np.clip(0.3 + 0.4 * (stock_importance / stock_importance.max()) +
                          np.random.normal(0, 0.05, N_STOCKS), 0.05, 0.9)
turnover = np.clip(2.0 - 1.5 * (stock_importance / stock_importance.max()) +
                   np.random.normal(0, 0.3, N_STOCKS), 0.1, 10.0)

# Generate returns with embedded cross-firm momentum
raw_returns = np.zeros((N_MONTHS, N_STOCKS))
for m in range(N_MONTHS):
    mkt_ret = np.random.normal(0.008, 0.04)
    noise = np.random.normal(0, 0.08, N_STOCKS)
    raw_returns[m] = market_beta * mkt_ret + noise

# Embed momentum using lag-1 CF Ret^SC
print("  Embedding cross-firm momentum signal...")
for m in range(1, N_MONTHS):
    C_prev = coverage_mats[m - 1]  # (N_STOCKS x N_ANALYSTS) sparse
    n_cover = np.array(C_prev.sum(axis=1)).flatten()  # (N_STOCKS,)
    # Common analyst matrix: M = C @ C^T  -> (N_STOCKS x N_STOCKS)
    # But we only need weighted CF Ret for each stock
    # Use: peer returns weighted by SC of peer
    # SC_j = sum over all other stocks of |analysts(j) & analysts(other)|
    #       = sum_k M[j,k] = (C @ C^T @ 1)[j] - M[j,j]
    # But M[j,j] = n_cover[j], so SC_j = (C @ C^T @ 1)[j] - n_cover[j]

    # For speed: compute C @ C^T as sparse matrix
    CC = C_prev.dot(C_prev.T)  # sparse (N_STOCKS x N_STOCKS)
    # n_ij = CC[i,j];  n_i = n_cover[i];  n_j = n_cover[j]

    # SC = degree (sum of row) - diagonal = total connections minus self
    # Actually SC_j = sum_k!=j CC[j,k] = CC @ 1 - diag
    ones = np.ones(N_STOCKS)
    row_sums = np.array(CC.dot(ones)).flatten()
    sc_vals = row_sums - np.array(CC.diagonal())  # SC for each stock

    # For each stock s: CF Ret^SC = sum_j (SC_j / sum_k SC_k) * ret_j  for connected j
    # Connected = CC[s,j] > 0 and j != s
    # Precompute peer returns from previous month
    prev_rets = raw_returns[m - 1]  # (N_STOCKS,)

    for s in range(N_STOCKS):
        # Get connected peers (non-zero entries in row s of CC)
        row = CC.getrow(s)
        peers = row.indices
        peers = peers[peers != s]  # exclude self
        if len(peers) == 0:
            continue
        peer_sc = sc_vals[peers]
        total_sc = peer_sc.sum()
        if total_sc == 0:
            continue
        cf_ret = (peer_sc / total_sc * prev_rets[peers]).sum()
        raw_returns[m, s] += 0.3 * cf_ret

# Free sparse matrices we no longer need
del coverage_mats
import gc; gc.collect()

print(f"  Stocks: {N_STOCKS}, Months: {N_MONTHS}, Analysts: {N_ANALYSTS}")
print(f"  Date range: {months[0].strftime('%Y-%m')} to {months[-1].strftime('%Y-%m')}")

# =============================================================================
# 2. Precompute All CF Ret Values (vectorized per month)
# =============================================================================
print("\n" + "=" * 70)
print("2. PRECOMPUTING CF RET (all 5 weighting schemes)")
print("=" * 70)

# Rebuild coverage matrices (needed for weighting)
print("  Rebuilding coverage matrices for CF Ret computation...")
# Store only lagged coverage (month m-1 for predicting month m)
cov_counts_monthly = np.zeros((N_MONTHS, N_STOCKS), dtype=np.int32)
for m in range(N_MONTHS):
    for a in range(N_ANALYSTS):
        if analyst_start[a] <= m < analyst_end[a]:
            for s in analyst_portfolios[a]:
                cov_counts_monthly[m, s] += 1

# CF Ret arrays: (N_MONTHS, N_STOCKS, 5) — only months 1..N_MONTHS-1 valid
cf_ret_all = np.full((N_MONTHS, N_STOCKS, 5), np.nan)
SCHEMES = ["AH", "Isr", "MRX", "Sor", "SC"]
scheme_idx = {name: i for i, name in enumerate(SCHEMES)}

print("  Computing pairwise common analysts and weights...")
for m in range(1, N_MONTHS):
    if m % 20 == 0:
        print(f"    month {m}/{N_MONTHS}...")

    # Rebuild bipartite coverage for month m-1
    mat = lil_matrix((N_STOCKS, N_ANALYSTS), dtype=np.float64)
    for a in range(N_ANALYSTS):
        if analyst_start[a] <= m - 1 < analyst_end[a]:
            for s in analyst_portfolios[a]:
                mat[s, a] = 1.0
    C = mat.tocsr()

    # Common analyst matrix: CC = C @ C^T  (sparse)
    CC = C.dot(C.T)

    # Coverage counts
    n_cov = np.array(C.sum(axis=1)).flatten()  # (N_STOCKS,)
    n_cov_safe = np.maximum(n_cov, 1)

    # Extract as dense for speed (N_STOCKS=300 -> 300x300 = 90K entries, fine)
    CC_dense = CC.toarray()
    np.fill_diagonal(CC_dense, 0)  # exclude self

    # Masks: which stock pairs are connected
    connected = CC_dense > 0  # (N_STOCKS, N_STOCKS) boolean

    prev_rets = raw_returns[m - 1]  # (N_STOCKS,)

    # --- AH weights: w_ij = n_ij / sum_k n_ik ---
    row_sums = CC_dense.sum(axis=1, keepdims=True)
    row_sums_safe = np.where(row_sums > 0, row_sums, 1.0)
    w_ah = CC_dense / row_sums_safe
    cf_ah = (w_ah * prev_rets[np.newaxis, :]).sum(axis=1)  # weighted sum of peer returns
    cf_ret_all[m, :, scheme_idx["AH"]] = np.where(row_sums.flatten() > 0, cf_ah, np.nan)

    # --- Isr weights: w_ij = (n_ij / sqrt(n_i*n_j)) / sum ---
    n_i = n_cov_safe[:, np.newaxis]  # (N_STOCKS, 1)
    n_j = n_cov_safe[np.newaxis, :]  # (1, N_STOCKS)
    w_isr_raw = CC_dense / np.sqrt(n_i * n_j)
    row_sums_isr = w_isr_raw.sum(axis=1, keepdims=True)
    row_sums_isr_safe = np.where(row_sums_isr > 0, row_sums_isr, 1.0)
    w_isr = w_isr_raw / row_sums_isr_safe
    cf_isr = (w_isr * prev_rets[np.newaxis, :]).sum(axis=1)
    cf_ret_all[m, :, scheme_idx["Isr"]] = np.where(row_sums_isr.flatten() > 0, cf_isr, np.nan)

    # --- MRX weights: w_ij = (n_ij / (n_i+n_j-n_ij)) / sum ---
    denom_mrx = n_i + n_j - CC_dense
    denom_mrx = np.where(denom_mrx > 0, denom_mrx, 1.0)
    w_mrx_raw = CC_dense / denom_mrx
    row_sums_mrx = w_mrx_raw.sum(axis=1, keepdims=True)
    row_sums_mrx_safe = np.where(row_sums_mrx > 0, row_sums_mrx, 1.0)
    w_mrx = w_mrx_raw / row_sums_mrx_safe
    cf_mrx = (w_mrx * prev_rets[np.newaxis, :]).sum(axis=1)
    cf_ret_all[m, :, scheme_idx["MRX"]] = np.where(row_sums_mrx.flatten() > 0, cf_mrx, np.nan)

    # --- Sor weights: w_ij = (2*n_ij / (n_i+n_j)) / sum ---
    denom_sor = np.where((n_i + n_j) > 0, (n_i + n_j), 1.0)
    w_sor_raw = 2 * CC_dense / denom_sor
    row_sums_sor = w_sor_raw.sum(axis=1, keepdims=True)
    row_sums_sor_safe = np.where(row_sums_sor > 0, row_sums_sor, 1.0)
    w_sor = w_sor_raw / row_sums_sor_safe
    cf_sor = (w_sor * prev_rets[np.newaxis, :]).sum(axis=1)
    cf_ret_all[m, :, scheme_idx["Sor"]] = np.where(row_sums_sor.flatten() > 0, cf_sor, np.nan)

    # --- SC weights: w_ij = SC_j / sum_k SC_k ---
    # SC_j = sum_k CC[j,k] (number of analyst-shared connections for stock j)
    sc_vals = CC_dense.sum(axis=1)  # (N_STOCKS,)
    # Note: CC_dense has diagonal=0, so SC counts only cross-connections
    sc_safe = np.where(sc_vals > 0, sc_vals, 1.0)
    w_sc = sc_vals[np.newaxis, :] / (sc_vals[np.newaxis, :].sum(axis=1, keepdims=True) + 1e-10)
    # Only apply where connected
    w_sc_masked = w_sc * connected.astype(float)
    row_sums_sc = w_sc_masked.sum(axis=1, keepdims=True)
    row_sums_sc_safe = np.where(row_sums_sc > 0, row_sums_sc, 1.0)
    w_sc_norm = w_sc_masked / row_sums_sc_safe
    cf_sc = (w_sc_norm * prev_rets[np.newaxis, :]).sum(axis=1)
    cf_ret_all[m, :, scheme_idx["SC"]] = np.where(row_sums_sc.flatten() > 0, cf_sc, np.nan)

n_valid = np.sum(~np.isnan(cf_ret_all[1:, :, :]))
print(f"  CF Ret computed: {n_valid:,} valid observations")

# Stock filter: exclude stocks with zero coverage at month m-1
valid_mask = np.zeros((N_MONTHS, N_STOCKS), dtype=bool)
for m in range(1, N_MONTHS):
    valid_mask[m] = cov_counts_monthly[m - 1] > 0

# =============================================================================
# 3. Univariate Portfolio Analysis (Table 2)
# =============================================================================
print("\n" + "=" * 70)
print("3. UNIVARIATE PORTFOLIO ANALYSIS (Table 2)")
print("=" * 70)

from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant


def portfolio_analysis(scheme):
    """Sort into deciles by CF Ret, return stats."""
    si = scheme_idx[scheme]
    all_decile = {d: [] for d in range(10)}
    ls_rets = []

    for m in range(1, N_MONTHS):
        mask = valid_mask[m]
        vals = cf_ret_all[m, :, si]
        valid = mask & ~np.isnan(vals)
        indices = np.where(valid)[0]
        if len(indices) < 30:
            continue

        order = indices[np.argsort(-vals[indices])]  # descending: High CF Ret first
        n = len(order)
        ds = max(n // 10, 1)

        for d in range(10):
            s = d * ds
            e = s + ds if d < 9 else n
            stocks = order[s:e]
            if len(stocks) > 0:
                all_decile[d].append(raw_returns[m, stocks].mean())

        # Long-short
        hi = order[:ds]
        lo = order[9 * ds:]
        if len(hi) > 0 and len(lo) > 0:
            ls_rets.append(raw_returns[m, hi].mean() - raw_returns[m, lo].mean())

    results = {}
    for d in range(10):
        arr = np.array(all_decile[d]) * 100
        results[d] = {"mean": arr.mean(), "tstat": stats.ttest_1samp(arr, 0).statistic if len(arr) > 2 else 0}

    ls = np.array(ls_rets) * 100
    results["H-L"] = {"mean": ls.mean(), "tstat": stats.ttest_1samp(ls, 0).statistic if len(ls) > 2 else 0}

    # Simple SIM alpha via time-series regression on LS returns
    mkt_all = np.array([raw_returns[m].mean() for m in range(1, N_MONTHS)]) * 100
    n_ls = min(len(ls), len(mkt_all))
    if n_ls > 12:
        X = add_constant(mkt_all[:n_ls])
        try:
            reg = OLS(ls[:n_ls], X).fit()
            results["SIM_alpha"] = {"mean": float(reg.params[1]), "tstat": float(reg.tvalues[1])}
        except Exception:
            results["SIM_alpha"] = {"mean": np.nan, "tstat": 0}
    else:
        results["SIM_alpha"] = {"mean": np.nan, "tstat": 0}
    return results


print(f"\n{'Scheme':<8} {'High':>8} {'Low':>8} {'H-L':>8} {'H-L t':>8} {'SIM α':>8} {'SIM t':>8}")
print("-" * 64)
scheme_results = {}
for scheme in SCHEMES:
    r = portfolio_analysis(scheme)
    scheme_results[scheme] = r
    print(f"{scheme:<8} {r[0]['mean']:>7.3f} {r[9]['mean']:>7.3f} {r['H-L']['mean']:>7.3f} "
          f"{r['H-L']['tstat']:>7.2f} {r['SIM_alpha']['mean']:>7.3f} {r['SIM_alpha']['tstat']:>7.2f}")

# =============================================================================
# 4. Fama-MacBeth Regressions (Table 5)
# =============================================================================
print("\n" + "=" * 70)
print("4. FAMA-MACBETH REGRESSIONS (Table 5)")
print("=" * 70)


def fama_macbeth(schemes_list, with_controls=False):
    """FM regression with one or more CF Ret variables."""
    slopes = defaultdict(list)
    for m in range(1, N_MONTHS):
        mask = valid_mask[m]
        rows = []
        for s in range(N_STOCKS):
            if not mask[s]:
                continue
            row = {}
            ok = True
            for sc_name in schemes_list:
                v = cf_ret_all[m, s, scheme_idx[sc_name]]
                if np.isnan(v):
                    ok = False; break
                row[f"cf_{sc_name}"] = v
            if not ok:
                continue
            if with_controls:
                row["size"] = np.log(stock_sizes[s])
                row["turnover"] = turnover[s]
                row["inst"] = inst_ownership[s]
            row["ret"] = raw_returns[m, s]
            rows.append(row)
        if len(rows) < 30:
            continue
        df = pd.DataFrame(rows)
        X_cols = [c for c in df.columns if c != "ret"]
        X = add_constant(df[X_cols])
        try:
            reg = OLS(df["ret"], X).fit()
            for c in X_cols:
                if c != "const":
                    slopes[c].append(reg.params[c])
        except Exception:
            pass
    return {c: {"coef": np.mean(v), "tstat": stats.ttest_1samp(np.array(v), 0).statistic
                if len(v) > 2 else 0} for c, v in slopes.items()}


print(f"\n--- Univariate FM Regressions ---")
print(f"{'Variable':<16} {'Coef':>8} {'t-stat':>8}")
print("-" * 36)
fm_uni = {}
for scheme in SCHEMES:
    r = fama_macbeth([scheme])
    fm_uni[scheme] = r
    k = f"cf_{scheme}"
    print(f"{k:<16} {r[k]['coef']:>8.4f} {r[k]['tstat']:>8.2f}")

print(f"\n--- Bivariate FM: SC + alternative (with controls) ---")
print(f"{'Alt Scheme':<12} {'SC coef':>10} {'SC t':>8} {'Alt coef':>10} {'Alt t':>8}")
print("-" * 52)
for alt in ["AH", "Isr", "MRX", "Sor"]:
    r = fama_macbeth(["SC", alt], with_controls=True)
    sc_r = r.get("cf_SC", {"coef": 0, "tstat": 0})
    alt_r = r.get(f"cf_{alt}", {"coef": 0, "tstat": 0})
    print(f"{alt:<12} {sc_r['coef']:>10.4f} {sc_r['tstat']:>8.2f} {alt_r['coef']:>10.4f} {alt_r['tstat']:>8.2f}")

# =============================================================================
# 5. Spanning Tests (Table 4)
# =============================================================================
print("\n" + "=" * 70)
print("5. SPANNING TESTS (Table 4)")
print("=" * 70)

# Test: can CFMOM^SC explain the other CFMOM returns?
# Simple approach: regress LS returns of alternative on LS returns of SC
ls_series = {}
for scheme in SCHEMES:
    rets = []
    for m in range(1, N_MONTHS):
        si = scheme_idx[scheme]
        mask = valid_mask[m]
        vals = cf_ret_all[m, :, si]
        valid = mask & ~np.isnan(vals)
        indices = np.where(valid)[0]
        if len(indices) < 30:
            rets.append(np.nan); continue
        order = indices[np.argsort(-vals[indices])]
        n = len(order)
        ds = max(n // 10, 1)
        hi = raw_returns[m, order[:ds]].mean()
        lo = raw_returns[m, order[9 * ds:]].mean()
        rets.append(hi - lo)
    ls_series[scheme] = np.array(rets)

print(f"\n{'Test':<30} {'Alpha':>8} {'t-stat':>8}")
print("-" * 50)
# Regress LS_alt on LS_SC
for alt in ["AH", "Isr", "MRX", "Sor"]:
    y_raw = ls_series[alt]
    x_raw = ls_series["SC"]
    valid = ~np.isnan(y_raw) & ~np.isnan(x_raw)
    y = y_raw[valid] * 100
    X = add_constant(x_raw[valid] * 100)
    if len(y) > 12:
        try:
            reg = OLS(y, X).fit()
            print(f"  {alt} LS regressed on SC LS:  α={float(reg.params[0]):.3f}, t={float(reg.tvalues[0]):.2f}")
        except Exception as e:
            print(f"  {alt}: error ({e})")

# =============================================================================
# 6. SC Characteristics Analysis (Table 7)
# =============================================================================
print("\n" + "=" * 70)
print("6. SC CHARACTERISTICS (Table 7)")
print("=" * 70)

ref_m = N_MONTHS // 2
sc_ref = cov_counts_monthly[ref_m].astype(float)
sc_order = np.argsort(-sc_ref)
ds = N_STOCKS // 10

print(f"\n{'Characteristic':<18}", end="")
for d in range(10):
    print(f"{'D' + str(d + 1):>8}", end="")
print()
print("-" * 100)

chars = {
    "SC": sc_ref,
    "log(Size)": np.log(stock_sizes),
    "#Analysts": cov_counts_monthly[ref_m].astype(float),
    "Inst Own%": inst_ownership * 100,
    "Turnover": turnover,
}
for name, vals in chars.items():
    line = f"{name:<18}"
    for d in range(10):
        s = d * ds
        e = s + ds if d < 9 else N_STOCKS
        line += f"{vals[sc_order[s:e]].mean():>8.2f}"
    print(line)

# =============================================================================
# 7. Leader-Laggard Bivariate Sort (Table 8)
# =============================================================================
print("\n" + "=" * 70)
print("7. LEADER-LAGGARD ANALYSIS (Table 8)")
print("=" * 70)

print(f"\n{'SC Quintile':<20} {'H-L ret%':>10} {'t-stat':>8}")
print("-" * 42)

for sc_q in range(5):
    hl_list = []
    for m in range(1, N_MONTHS):
        mask = valid_mask[m]
        vals_sc = cov_counts_monthly[m - 1].astype(float)
        vals_cf = cf_ret_all[m, :, scheme_idx["SC"]]
        valid = mask & ~np.isnan(vals_cf)
        indices = np.where(valid)[0]
        if len(indices) < 50:
            continue
        # Sort by SC
        order = indices[np.argsort(-vals_sc[indices])]
        n = len(order)
        qs = n // 5
        s_start = sc_q * qs
        s_end = s_start + qs if sc_q < 4 else n
        group = order[s_start:s_end]
        if len(group) < 10:
            continue
        # Within group, sort by CF Ret^SC
        group_vals = vals_cf[group]
        inner_order = group[np.argsort(-group_vals)]
        qs2 = len(inner_order) // 5
        hi = inner_order[:qs2]
        lo = inner_order[4 * qs2:]
        if len(hi) > 0 and len(lo) > 0:
            hl_list.append(raw_returns[m, hi].mean() - raw_returns[m, lo].mean())
    hl = np.array(hl_list) * 100
    t = stats.ttest_1samp(hl, 0).statistic if len(hl) > 2 else 0
    label = f"SC Q{sc_q + 1} ({'High' if sc_q == 0 else 'Low' if sc_q == 4 else 'Mid'})"
    print(f"{label:<20} {hl.mean():>9.3f} {t:>8.2f}")

# =============================================================================
# 8. Figures
# =============================================================================
print("\n" + "=" * 70)
print("8. GENERATING FIGURES")
print("=" * 70)

colors = {"AH": "#e41a1c", "Isr": "#377eb8", "MRX": "#4daf4a", "Sor": "#984ea3", "SC": "#ff7f00"}

# --- Fig 1: Network ---
print("  Building network for visualization...")
mat_vis = lil_matrix((N_STOCKS, N_ANALYSTS), dtype=np.float64)
for a in range(N_ANALYSTS):
    if analyst_start[a] <= ref_m < analyst_end[a]:
        for s in analyst_portfolios[a]:
            mat_vis[s, a] = 1.0
C_vis = mat_vis.tocsr()
CC_vis = (C_vis.dot(C_vis.T)).toarray()
np.fill_diagonal(CC_vis, 0)
CC_vis = (CC_vis > 0).astype(int)

G = nx.from_numpy_array(CC_vis)
top30 = sorted(G.degree, key=lambda x: -x[1])[:30]
subG = G.subgraph([n for n, _ in top30])

fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.spring_layout(subG, seed=42, k=2.0)
deg = dict(subG.degree())
nx.draw_networkx(subG, pos, node_size=[deg[n] * 40 for n in subG.nodes()],
                node_color="steelblue", edge_color="lightgray", alpha=0.7, with_labels=False, ax=ax)
ax.set_title("Sample Analyst Coverage Network (top 30 connected stocks)", fontsize=12)
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig1_network.png"), dpi=150)
plt.close()
print("  Saved fig1_network.png")

# --- Fig 2: Decile returns ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
x = np.arange(10)
for scheme in SCHEMES:
    r = scheme_results[scheme]
    axes[0].plot(x, [r[d]["mean"] for d in range(10)], "-o", label=scheme,
                 color=colors[scheme], markersize=4)
axes[0].set_xlabel("Decile (1=High CF Ret, 10=Low)")
axes[0].set_ylabel("Mean Monthly Return (%)")
axes[0].set_title("Decile Portfolio Returns")
axes[0].legend(); axes[0].grid(alpha=0.3)

bars = axes[1].bar(SCHEMES, [scheme_results[s]["H-L"]["mean"] for s in SCHEMES],
                   color=[colors[s] for s in SCHEMES], alpha=0.8)
axes[1].set_ylabel("Long-Short Return (%)")
axes[1].set_title("Long-Short: High - Low")
axes[1].grid(axis="y", alpha=0.3)
for bar, s in zip(bars, SCHEMES):
    t = scheme_results[s]["H-L"]["tstat"]
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
                 f"t={t:.2f}", ha="center", fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig2_decile_returns.png"), dpi=150)
plt.close()
print("  Saved fig2_decile_returns.png")

# --- Fig 3: SC distribution ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(sc_ref, bins=40, color="steelblue", edgecolor="white", alpha=0.8)
axes[0].axvline(sc_ref.mean(), color="red", ls="--", label=f"Mean={sc_ref.mean():.0f}")
axes[0].set_xlabel("Strength Centrality"); axes[0].set_ylabel("Count")
axes[0].set_title("SC Distribution"); axes[0].legend()

axes[1].scatter(np.log(stock_sizes), sc_ref, s=12, alpha=0.5, c="steelblue")
axes[1].set_xlabel("log(Market Cap)"); axes[1].set_ylabel("SC")
corr = np.corrcoef(np.log(stock_sizes), sc_ref)[0, 1]
axes[1].text(0.05, 0.95, f"ρ = {corr:.3f}", transform=axes[1].transAxes, fontsize=11)
axes[1].set_title("SC vs Firm Size")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig3_sc_distribution.png"), dpi=150)
plt.close()
print("  Saved fig3_sc_distribution.png")

# --- Fig 4: Leader-laggard heatmap ---
fig, ax = plt.subplots(figsize=(8, 6))
heatmap = np.zeros((5, 5))
for sc_q in range(5):
    for cf_q in range(5):
        rets = []
        for m in range(1, N_MONTHS):
            mask = valid_mask[m]
            vals_sc = cov_counts_monthly[m - 1].astype(float)
            vals_cf = cf_ret_all[m, :, scheme_idx["SC"]]
            valid = mask & ~np.isnan(vals_cf)
            indices = np.where(valid)[0]
            if len(indices) < 50:
                continue
            order = indices[np.argsort(-vals_sc[indices])]
            n = len(order)
            qs = n // 5
            s1 = sc_q * qs; s2 = s1 + qs if sc_q < 4 else n
            group = order[s1:s2]
            if len(group) < 10:
                continue
            g_vals = vals_cf[group]
            inner = group[np.argsort(-g_vals)]
            qs2 = len(inner) // 5
            c1 = cf_q * qs2; c2 = c1 + qs2 if cf_q < 4 else len(inner)
            stocks = inner[c1:c2]
            if len(stocks) > 0:
                rets.append(raw_returns[m, stocks].mean() * 100)
        heatmap[sc_q, cf_q] = np.mean(rets) if rets else np.nan

im = ax.imshow(heatmap, cmap="RdYlGn", aspect="auto")
ax.set_xticks(range(5)); ax.set_xticklabels(["Q1\nHigh", "Q2", "Q3", "Q4", "Q5\nLow"])
ax.set_yticks(range(5)); ax.set_yticklabels([f"SC Q{i + 1}" for i in range(5)])
ax.set_title("Bivariate Sort: SC × CF Ret^SC — Mean Return (%)")
for i in range(5):
    for j in range(5):
        ax.text(j, i, f"{heatmap[i, j]:.2f}", ha="center", va="center", fontsize=11)
plt.colorbar(im, ax=ax, label="Return (%)")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig4_leader_laggard.png"), dpi=150)
plt.close()
print("  Saved fig4_leader_laggard.png")

# --- Fig 5: Network evolution ---
print("  Computing network evolution...")
fig, ax = plt.subplots(figsize=(12, 5))
sizes, ncomps = [], []
for m in range(0, N_MONTHS, 3):
    mat_e = lil_matrix((N_STOCKS, N_ANALYSTS), dtype=np.float64)
    for a in range(N_ANALYSTS):
        if analyst_start[a] <= m < analyst_end[a]:
            for s in analyst_portfolios[a]:
                mat_e[s, a] = 1.0
    CC_e = mat_e.tocsr().dot(mat_e.tocsr().T)
    CC_e_dense = CC_e.toarray()
    np.fill_diagonal(CC_e_dense, 0)
    G_e = nx.from_numpy_array((CC_e_dense > 0).astype(int))
    if G_e.number_of_nodes() > 0:
        lc = max(nx.connected_components(G_e), key=len)
        sizes.append(len(lc))
        ncomps.append(nx.number_connected_components(G_e))
    else:
        sizes.append(0); ncomps.append(0)

dates = months[::3][:len(sizes)]
ax2 = ax.twinx()
ax.bar(dates, ncomps, width=60, alpha=0.4, color="lightblue", label="# Components")
ax2.plot(dates, sizes, "r-o", ms=3, label="Largest Component")
ax.set_ylabel("# Components"); ax2.set_ylabel("Largest Component Size")
ax.set_title("Network Structure Evolution"); ax.legend(loc="upper left"); ax2.legend(loc="upper right")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig5_network_evolution.png"), dpi=150)
plt.close()
print("  Saved fig5_network_evolution.png")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
This script replicates the paper's core methodology with synthetic data.

KEY STEPS DEMONSTRATED:
  1. Analyst coverage network from bipartite stock-analyst matrix
  2. Five weighting schemes: AH, Isr, MRX, Sor, SC
  3. Connected-firm returns via matrix operations
  4. Decile portfolio analysis with long-short returns and t-stats
  5. Fama-MacBeth regressions (univariate + bivariate)
  6. Spanning tests between weighting schemes
  7. SC characteristics across deciles
  8. Leader-laggard bivariate dependent sorts

OUTPUT:
  figures/fig1_network.png          — Sample coverage network
  figures/fig2_decile_returns.png   — Decile returns by scheme
  figures/fig3_sc_distribution.png  — SC distribution & correlation
  figures/fig4_leader_laggard.png   — Bivariate sort heatmap
  figures/fig5_network_evolution.png — Network structure over time
""")
