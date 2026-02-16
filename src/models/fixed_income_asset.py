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
        insurance_company: str,
        aplication_date: Date,
        due_date: Date,
        liquidity: LiquidityType,
        venture: 'alto' | 'médio' | 'baixo' | 'baxissimo',
    ):
        self.__name = name
        self.__iyield_strategy = iyield_strategy
        self.__institute = institute
        self.__min_contribution = min_contribution
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

    def simulate_current_value(self) -> dict:
        # Calcula dias passados (exemplo simples)
        days_passed = (date.today() - self.__aplication_date).days
        if days_passed < 0: days_passed = 0

        # Chama a estratégia para fazer a conta difícil
        gross = self.__iyield_strategy.calculate_final_amount(self.__min_contribution, days_passed)
        tax = self.__iyield_strategy.calculate_taxes(self.__min_contribution, gross, days_passed)
        net = gross - tax

        return {
            "valor_bruto": gross,
            "imposto_devido": tax,
            "valor_liquido": net,
            "rentabilidade": self.__iyield_strategy.get_profitability_description()
        }