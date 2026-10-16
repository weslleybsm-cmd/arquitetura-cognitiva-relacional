"""AA-0 — Prototipo rudimentar de Arquitetura Artificial baseado na ACR.
Substrato recorrente + reorganizacao continua (Hebb com decaimento).
Observaveis: SREs candidatos, Acumulacao, Reutilizacao, Selecao, Continuidade.
Teoria: ACR (Weslley B. S. de Morais). Experimento: colab. com Kimi (Moonshot AI)."""

import numpy as np
from sklearn.cluster import KMeans

rng = np.random.default_rng(7)

# 1. SUBSTRATO (relacoes da camada base)
N, S = 200, 8
W0 = (rng.random((N, N)) < 0.08) * rng.normal(0, 1.0, (N, N))
np.fill_diagonal(W0, 0)
W0 *= 0.85 / np.abs(np.linalg.eigvals(W0)).max()
B = rng.normal(0, 0.7, (N, S))

# 2. AMBIENTE: 4 objetos latentes
n_obj = 4
codes = (rng.random((n_obj, S)) < 0.35).astype(float)

def env_stream(T, hold=40, noise=0.05):
    u = np.zeros((T, S)); lab = np.zeros(T, int)
    o = rng.integers(0, n_obj)
    for t in range(T):
        if t % hold == 0 and rng.random() < 0.5:
            o = rng.integers(0, n_obj)
        lab[t] = o
        u[t] = codes[o] + noise * rng.standard_normal(S)
    return u, lab

# 3. DINAMICA + REORGANIZACAO CONTINUA
def run(x0, W, U, lr=0.0, decay=2e-5, clip=2.0, noise=0.05):
    T = U.shape[0]; x = x0.copy(); X = np.zeros((T, N))
    for t in range(T):
        x = np.tanh(W @ x + B @ U[t] + noise * rng.standard_normal(N))
        if lr > 0:
            W = W + lr * np.outer(x, x)
            W *= (1 - decay)
            np.clip(W, -clip, clip, out=W)
        X[t] = x
    return X, W

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

if __name__ == "__main__":
    U_learn, lab = env_stream(6000)
    X_learn, W_plastic = run(np.zeros(N), W0.copy(), U_learn, lr=0.01)
    attractors = np.array([X_learn[lab == k].mean(axis=0) for k in range(n_obj)])

    X_rest, _ = run(X_learn[-1].copy(), W_plastic, np.zeros((500, S)))
    X_rest_ctl, _ = run(X_learn[-1].copy(), W0, np.zeros((500, S)))

    def probe(W, k, steps=50, cue_noise=0.3):
        cue = codes[k] + cue_noise * rng.standard_normal(S)
        x = np.zeros(N)
        for _ in range(steps):
            x = np.tanh(W @ x + B @ cue + 0.05 * rng.standard_normal(N))
        return x

    print("reutilizacao plastico :", cos(probe(W_plastic, 0), attractors[0]))
    print("reutilizacao controle :", cos(probe(W0, 0), attractors[0]))
