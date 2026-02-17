from .iyield_strategy import IYieldStrategy

class RegressiveTaxStrategy(IYieldStrategy):
    """
    Classe base para QUALQUER ativo que segue a tabela regressiva de 
    importo de renda (IR) para pessoas físicas, como CDB, LC, LCI, LCA, Debênture e Tesouro.
    """
    def calculate_IR(self, principal: float, gross_amount: float, days: int) -> float:
        '''Imposto de Renda segue a tabela regressiva
        @param principal: valor inicial investido
        @param gross_amount: valor bruto calculado
        @param days: número de dias da aplicação'''
        profit = gross_amount - principal
        
        if days <= 180: rate = 0.225
        elif days <= 360: rate = 0.20
        elif days <= 720: rate = 0.175
        else: rate = 0.15
        
        return profit * rate

    def calculate_IOF(self, principal: float, gross_amount: float, days: int) -> float:
        '''IOF(Imposto sobre operações financeiras) 
        incide sobre aplicações com menos de 30 dias.
        @param principal: valor inicial investido
        @param gross_amount: valor bruto calculado
        @param days: número de dias da aplicação'''
        if days >= 30: return 0.0
        
        profit = gross_amount - principal
        daily_rate = 0.0033
        return profit * daily_rate * (30 - days)