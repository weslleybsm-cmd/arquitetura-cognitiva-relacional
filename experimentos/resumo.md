
## Resultados dos experimentos (resumo)

| Versão | Regra de reorganização | Pureza | Diversidade | Reutilização | Conclusão |
|---|---|---|---|---|---|
| AA-0 | Hebb + decaimento | 77,8% | ~0 | 1.00 | Base ACR emerge; seleção colapsa |
| AA-1 | + k-WTA + homeostasia | 85,5% | ~0* | 1.00* | Métrica enganosa: colapso persistiu |
| AA-2 | BCM + novidade (bruta) | 16,7% | 0.000 | — | Arquitetura destruída (drift 253%) |
| **AA-2b** | **BCM + novidade (calibrada)** | 50,8% | **0.466** | 0.73–0.87 | **Diversidade real + reutilização** |

\* reutilização "perfeita" era artefato: os 4 atratores eram o mesmo padrão.

**Conclusão central:** a base da pirâmide ACR (relações distinguíveis → organizações estáveis →
história acumulada → reutilização) é computacionalmente realizável. O experimento revelou o
primeiro refinamento teórico exigido pela engenharia: **Compatibilidade possui dois polos**
(integração intra-organização × diferenciação inter-organizações). Detalhes: `RELATORIO_AA_0_AA2b.md`.

## Como rodar

```bash
pip install numpy scikit-learn matplotlib
python experimentos/aa2_prototipo.py
