import pytest
from strategies.cdb_strategy import CDBStrategy

def test_calculo_cdb_um_ano():
    """
    Testa se um CDB de 100% do CDI rende corretamente após 1 ano (252 dias úteis).
    """
    # 1. ARRANGE (Preparação)
    # Supondo taxa DI de 12% ao ano (definida no seu __init__ da estratégia)
    principal = 1000.00
    dias = 252
    percentual_cdi = 1.0 # 100%
    
    estrategia = CDBStrategy(percentage_of_cdi=percentual_cdi)

    # 2. ACT (Ação)
    resultado_bruto = estrategia.calculate_final_amount(principal, days=dias)
    
    # 3. ASSERT (Validação)
    # Se a taxa é 12% a.a., 1000 deve virar 1120.00
    # Usamos pytest.approx porque float nunca é exato
    assert resultado_bruto == pytest.approx(1120.00, rel=1e-2)

def test_imposto_regressivo_curto_prazo():
    """
    Testa se o imposto para menos de 180 dias é 22.5%
    """
    # Arrange
    estrategia = CDBStrategy(percentage_of_cdi=1.0)
    principal = 1000.00
    bruto_simulado = 1100.00 # Lucro de 100 reais
    dias = 100 # Menos de 180 dias
    
    # Act
    imposto = estrategia.calculate_taxes(principal, bruto_simulado, dias)
    
    # Assert
    # Lucro = 100. Taxa = 22.5%. Imposto deve ser 22.50
    assert imposto == pytest.approx(22.50, rel=1e-2)