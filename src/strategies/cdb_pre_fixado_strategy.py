from .iyield_strategy import IYieldStrategy
from .regressive_tax_strategy import RegressiveTaxStrategy

class CDBPreFixadoStrategy(RegressiveTaxStrategy):
    def __init__(self, percentage_of_cdi: float, anual_rate: float):
        self.__percentage_of_cdi = percentage_of_cdi
        self.__anual_rate = anual_rate

    def calculate_gross_amount(self, principal: float, days: int) -> float:
        return principal * (1 + self.__anual_rate) ** (days / 252)

    def calculate_taxes(self, principal: float, gross_amount: float, days: int) -> float:
        return self.calculate_IR(principal, gross_amount, days) + self.calculate_IOF(principal, gross_amount, days)

    def get_profitability_description(self) -> str:
        '''Retorna uma string legível, ex: '100% do CDI + 5% a.a.'''
        return f'{self.__percentage_of_cdi * 100:.0f}% do CDI + {self.__anual_rate * 100:.0f}% a.a.'