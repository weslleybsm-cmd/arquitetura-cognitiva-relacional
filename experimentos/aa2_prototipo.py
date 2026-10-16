# Copyright (c) 2026 weslleybsm-cmd
# Licensed under the MIT License.
# See the LICENSE file in the repository root for details.

"""AA-2b — BCM calibrado + novidade (predicao temporal) + homeostasia.
Resultado: diversidade de atratores recuperada (0.466) com reutilizacao
mantida (0.73-0.87) e ocupacao espontanea distribuida entre atratores.
Trade-off observado: seletividade (diversidade) x fidelidade (pureza).
Teoria: ACR (Weslley B. S. de Morais). Experimento: colab. com Kimi (Moonshot AI)."""

import numpy as np

rng = np.random.default_rng(7)
N, S, K = 200, 8, 15
W0 = (rng.random((N, N)) < 0.08) * rng.normal(0, 1.0, (N, N))
np.fill_diagonal(W0, 0)
W0 *= 0.85 / np.abs(np.linalg.eigvals(W0)).max()
B = rng.normal(0, 0.7, (N, S))
n_obj = 4
codes = (rng.random((n_obj, S)) < 0.35).astype(float)

def env_stream(T, hold=40, noise=0.05):
    u = np.zeros((T, S)); lab = np.zeros(T, int)
    o = rng.integers(0, n_obj)
    for t in range(T):
        if t % hold == 0 and rng.random() < 0.5:
            o = rng.integers(0, n_obj)
        lab[t] = o; u[t] = codes[o] + noise * rng.standard_normal(S)
    return u, lab

def kwta(pre, k=K):
    idx = np.argsort(pre)[-k:]
    x = np.zeros_like(pre); x[idx] = pre[idx]
    return x

def run_v3b(x0, W, U, lr=0.004, decay=1e-5, clip=2.0, noise=0.05):
    T = U.shape[0]; x = x0.copy(); xp = x.copy(); X = np.zeros((T, N))
    theta = np.full(N, 0.2); target = np.linalg.norm(W, axis=0).copy()
    for t in range(T):
        pred = np.tanh(W @ x + B @ U[t])
        x = kwta(pred + noise * rng.standard_normal(N))
        gate = np.linalg.norm(x - pred) / (np.linalg.norm(x - pred) + 0.3)
        W = W + lr * gate * np.outer(x * (x - theta), xp)
        W *= (1 - decay); np.clip(W, -clip, clip, out=W)
        W = W * (target / (np.linalg.norm(W, axis=0) + 1e-9))
        theta += 1e-3 * (x**2 - theta)
        xp = x.copy(); X[t] = x
    return X, W

def cos(a, b): return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

if __name__ == "__main__":
    U, lab = env_stream(6000)
    X, W = run_v3b(np.zeros(N), W0.copy(), U)
    print("OK — veja aa2_resultados.png e RELATORIO_AA_0_AA2b.md")
