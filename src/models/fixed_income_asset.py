from typing import Literal
from datetime import date
from strategies.iyield_strategy import IYieldStrategy

class FixedIncomeAsset:
    '''Classe para ativos de renda fixa.
        @param name: nome do ativo
        @param iyield_strategy: estratégia de rendimento do ativo
        @param institute: instituição financeira emissora do ativo
        @param min_contribution: valor mínimo de contribuição para investir no ativo
        @insurance_company: seguradora do ativo (se houver)
        @param aplication_date: data de início das aplicações
        @param due_date: data de vencimento do ativo
        @param liquidity: liquidez do ativo (diária ou no vencimento)
        @param venture: nível de risco do ativo (alto, médio, baixo ou baixíssimo)'''

    def __init__(
        self, 
        name:'CDB' | 'LCI' | 'LCA' | 'CRI' | 'CRA' | 'Debênture' | 'Tesouro Selic' | 'Poupança', 
        iyield_strategy:IYieldStrategy, 
        institute:str, 
        min_contribution:float,
        invested_amount:float,
        insurance_company: str,
        aplication_date: Date,
        due_date: Date,
        liquidity: str,
        venture: 'alto' | 'médio' | 'baixo' | 'baxissimo',
    ):
        if invested_amount < min_contribution:
            raise ValueError(
                f"Erro: O valor investido (R$ {invested_amount}) é menor que o mínimo permitido (R$ {min_contribution}) para este ativo."
            )

        self.__name = name 
        self.__iyield_strategy = iyield_strategy
        self.__institute = institute
        self.__min_contribution = min_contribution
        self.__invested_amount = invested_amount
        self.__aplication_date = aplication_date
        self.__due_date = due_date 
        self.__liquidity = liquidity
        self.__insurance_company = insurance_company
        self.__venture = venture

    def get_name(self):
        return self.__name

    def get_iyield_strategy(self):
        return self.__iyield_strategy

    def get_institute(self):
        return self.__institute

    def get_min_contribution(self):
        return self.__min_contribution
        
    def get_insurance_company(self):
        return self.__insurance_company

    def get_aplication_date(self):
        return self.__aplication_date

    def get_due_date(self):
        return self.__due_date

    def get_liquidity(self):
        return self.__liquidity

    def get_venture(self):
        return self.__venture

    def calculate_income(self, principal: float, days: int) -> float:
        gross_amount = self.__iyield_strategy.calculate_gross_amount(principal, days)
        taxes = self.__iyield_strategy.calculate_taxes(principal, gross_amount, days)
        final_amount = gross_amount - taxes
        return final_amount
        
    def simulate_current_status(self):
        today = date.today()
        days_passed = (today - self.__aplication_date).days
        if days_passed < 0: days_passed = 0
        
        # CORREÇÃO AQUI: Usamos o invested_amount, não o min_contribution
        gross = self.__iyield_strategy.calculate_gross_amount(self.__invested_amount, days_passed)
        taxes = self.__iyield_strategy.calculate_taxes(self.__invested_amount, gross, days_passed)
        net = gross - taxes
        
        return {
            "nome": self.__name,
            "dias_corridos": days_passed,
            "valor_investido": self.__invested_amount, # Útil mostrar isso no retorno
            "valor_bruto": round(gross, 2),
            "impostos": round(taxes, 2),
            "valor_liquido": round(net, 2),
            "lucro_liquido": round(net - self.__invested_amount, 2),
            "rentabilidade": self.__iyield_strategy.get_profitability_description()
        }       