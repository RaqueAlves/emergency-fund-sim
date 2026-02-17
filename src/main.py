from datetime import date
from models.fixed_income_asset import FixedIncomeAsset
from strategies.cdb_pos_fixado_strategy import CDBPosFixadoStrategy

def main():
    # 1. CRIAR A ESTRATÉGIA (O "Motor")
    # Configuro um CDB que rende 110% do CDI
    estrategia_cdb_top = CDBPosFixadoStrategy(percentage_of_cdi=1.10)

    # 2. CRIAR O ATIVO (A "Carcaça")
    # Conecto a estratégia dentro do ativo
    meu_investimento = FixedIncomeAsset(
        name="CDB Banco XP Turbo",
        iyield_strategy=estrategia_cdb_top,
        institute="XP Investimentos",
        min_contribution=1000.00, # A regra é mil...
        invested_amount=5000.00,  # ...mas eu coloquei 5 mil! <--- NOVO
        insurance_company="FGC",
        aplication_date=date(2025, 1, 1),
        due_date=date(2027, 1, 1),
        liquidity="No vencimento",
        venture="baixo"
    )

    # 3. RODAR A SIMULAÇÃO
    resultado = meu_investimento.simulate_current_status()
    
    print("-" * 30)
    print(f"Simulação do Ativo: {resultado['nome']}")
    print("-" * 30)
    print(f"Valor investido: R$ {resultado['valor_investido']}")
    print(f"Tempo investido: {resultado['dias_corridos']} dias")
    print(f"Taxa contratada: {resultado['rentabilidade']}")
    print(f"Valor Bruto:     R$ {resultado['valor_bruto']}")
    print(f"Impostos (IR/IOF): - R$ {resultado['impostos']}")
    print(f"Valor Líquido:   R$ {resultado['valor_liquido']}")
    print(f"Lucro Líquido:   R$ {resultado['lucro_liquido']}")
    print("-" * 30)

if __name__ == "__main__":
    main()