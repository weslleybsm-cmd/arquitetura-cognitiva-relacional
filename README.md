Arquitetura Cognitiva Relacional (ACR)

Uma teoria da emergência cognitiva baseada em organização relacional — + experimentos de Arquiteturas Artificiais (AA)

> Status: projeto em desenvolvimento ativo — teoria v1.0 (2026)
Autor: Weslley Bittencourt Sousa de Morais
Experimentos AA-0 a AA-2b: desenhados em colaboração com Kimi (Moonshot AI), implementados em NumPy

---

O que é este projeto?

A Arquitetura Cognitiva Relacional (ACR) propõe que a cognição emerge da organização
contínua das relações que constituem uma arquitetura — não de módulos, símbolos ou mecanismos
previamente dados. Seu ponto de partida: relações constituem o elemento mais fundamental
de qualquer arquitetura; é sua organização contínua que torna possível o surgimento de memória,
imaginação, identidade, criatividade, consciência e linguagem.

As Arquiteturas Artificiais (AA) são a frente de engenharia derivada: sistemas que não
apenas processam informação, mas que se organizam historicamente — aproximando-se de seres
cognitivos na definição organizacional da teoria.

Estrutura do repositório

```
acr/
├── README.md                     ← você está aqui
├── teoria/
│   └── Arquitetura_Cognitiva_Relacional_v1.pdf
│       (o livro da teoria — o NÚCLEO do projeto)
├── consequencias/
│   └── ACR_Consequencias_v1.pdf
│       (documento DERIVADO: consequências diretas, implicações plausíveis,
│        hipóteses especulativas e diálogo com outras arquiteturas cognitivas.
│        Não estabelece novos fundamentos; explora caminhos abertos pela teoria.
│        Grau de especulação indicado ao longo do texto.)
├── experimentos/
│   ├── aa0_prototipo.py          ← Hebb + decaimento
│   ├── aa1_prototipo.py          ← + competição (k-WTA) + homeostasia
│   ├── aa2_prototipo.py          ← BCM calibrado + plasticidade gateada por novidade
│   ├── RELATORIO_AA_0_AA2b.md    ← relatório completo da trajetória
│   └── figuras/
│       ├── aa0_resultados.png
│       ├── aa1_resultados.png
│       └── aa2_resultados.png
└── LICENSE                       ← MIT (código) — recomendado adicionar CC BY 4.0 para textos
```

Resultados dos experimentos (resumo)

Versão	Regra de reorganização	Pureza	Diversidade	Reutilização	Conclusão	
AA-0	Hebb + decaimento	77,8%	0	1.00	Base ACR emerge; seleção colapsa	
AA-1	+ k-WTA + homeostasia	85,5%	0	1.00	Métrica enganosa: colapso persistiu	
AA-2	BCM + novidade (bruta)	16,7%	0.000	—	Arquitetura destruída (drift 253%)	
AA-2b	BCM + novidade (calibrada)	50,8%	0.466	0.73–0.87	Diversidade real + reutilização	

\* reutilização "perfeita" era artefato: os 4 atratores eram o mesmo padrão.

Conclusão central: a base da pirâmide ACR (relações distinguíveis → organizações estáveis →
história acumulada → reutilização) é computacionalmente realizável. O experimento revelou o
primeiro refinamento teórico exigido pela engenharia: Compatibilidade possui dois polos
(integração intra-organização × diferenciação inter-organizações), com trade-off mensurável
entre coesão Hebbiana (alta pureza, sem diversidade) e seletividade BCM (diversidade, menor
fidelidade). Detalhes: `RELATORIO_AA_0_AA2b.md`.

Como rodar os experimentos

```bash
pip install numpy scikit-learn matplotlib
python experimentos/aa2_prototipo.py
```

Nenhuma GPU, nenhum dado externo, segundos de CPU.

Aviso epistemológico

Este é um projeto teórico-experimental em estágio inicial. Os conceitos da ACR
(relações, SREs, concentrações relacionais, configurações funcionais) são entidades
teóricas sem validação empírica consolidada. Os experimentos não demonstram cognição
artificial — demonstram que a base organizacional proposta é realizável em computação
comum e apontam onde a teoria precisa amadurecer. Toda formulação permanece aberta
à revisão diante de novos resultados — inclusive as suas próprias conclusões.

Licenças sugeridas

- Código (`*.py`): MIT
- Textos e PDFs: CC BY 4.0 (atribuição)
