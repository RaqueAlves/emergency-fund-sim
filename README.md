# 💰 Emergency Fund Simulator

Um simulador de investimentos de Renda Fixa desenvolvido em Python. 

O objetivo deste projeto é projetar o crescimento de uma reserva financeira, calculando automaticamente juros compostos e descontos tributários (Imposto de Renda Regressivo) para diferentes tipos de ativos (CDB, LCI, LCA, Tesouro Direto).

## 🚀 Funcionalidades

- **Arquitetura Genérica:** Utiliza o padrão de projeto *Strategy* para desacoplar a regra de cálculo da definição do ativo.
- **Cálculo de Impostos:** Aplicação automática da Tabela Regressiva de IR baseada no tempo de investimento.
- **Simulação Realista:** Suporte a indexadores como CDI (com percentuais variáveis).
- **Cobertura de Testes:** Testes unitários com `pytest` para garantir a precisão matemática dos juros e impostos.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14.3
- **Testes:** Pytest
- **Conceitos:** POO, Design Patterns (Strategy), Clean Architecture.

## 📂 Estrutura do Projeto

```text
emergency-fund-sim/
├── src/
│   ├── models/       # Definição dos Ativos (ex: FixedIncomeAsset)
│   ├── strategies/   # Lógica de Cálculo (ex: CDBStrategy, IYieldStrategy)
│   └── main.py       # Ponto de entrada da aplicação
├── tests/            # Testes unitários
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação