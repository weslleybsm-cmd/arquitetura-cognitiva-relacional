# Copyright (c) 2026 weslleybsm-cmd
# Licensed under the MIT License.
# See the LICENSE file in the repository root for details.

"""AA-1 — Competicao (k-WTA) + normalizacao homeostatica.
Testa se Compatibilidade competitiva preserva diversidade de atratores
sob plasticidade continua. Resultado: pureza sobe, MAS colapso persiste
(os 4 'atratores' aprendidos sao efetivamente o mesmo padrao).
Teoria: ACR (Weslley B. S. de Morais). Experimento: colab. com Kimi (Moonshot AI)."""

import numpy as np

rng = np.random.default_rng(7)
N, S, K = 200, 8, 20
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

def run_v2(x0, W, U, lr=0.005, decay=1e-5, clip=2.0, noise=0.05):
    T = U.shape[0]; x = x0.copy(); X = np.zeros((T, N))
    target = np.linalg.norm(W, axis=0).copy()
    for t in range(T):
        x = kwta(np.tanh(W @ x + B @ U[t] + noise * rng.standard_normal(N)))
        if lr > 0:
            W = W + lr * np.outer(x, x); W *= (1 - decay)
            np.clip(W, -clip, clip, out=W)
            W = W * (target / (np.linalg.norm(W, axis=0) + 1e-9))
        X[t] = x
    return X, W

def cos(a, b): return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

if __name__ == "__main__":
    U, lab = env_stream(6000)
    X, W = run_v2(np.zeros(N), W0.copy(), U)
    att = np.array([X[lab == k].mean(axis=0) for k in range(n_obj)])
    pair = [cos(att[i], att[j]) for i in range(n_obj) for j in range(i+1, n_obj)]
    print("diversidade (1=distintos):", 1 - np.mean(pair))
