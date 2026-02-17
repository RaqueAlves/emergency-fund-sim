from .iyield_strategy import IYieldStrategy
from .regressive_tax_strategy import RegressiveTaxStrategy

class CDBPosFixadoStrategy(RegressiveTaxStrategy):
    def __init__(self, percentage_of_cdi: float):
        self.__percentage_of_cdi = percentage_of_cdi
        self.__current_cdi_rate = 0.145 #Mock, em um cenário real, isso deveria ser atualizado dinamicamente com base na taxa CDI atual.

    def calculate_gross_amount(self, principal: float, days: int) -> float:
        daily_rate = (1 + (self.__current_cdi_rate * self.__percentage_of_cdi)) ** (1/252) - 1
        return principal * ((1 + daily_rate) ** days)

    def calculate_taxes(self, principal: float, gross_amount: float, days: int) -> float:
        return self.calculate_IR(principal, gross_amount, days) + self.calculate_IOF(principal, gross_amount, days)

    def get_profitability_description(self) -> str:
        '''Retorna uma string legível, ex: '100% do CDI' '''
        return f'{self.__percentage_of_cdi * 100:.0f}% do CDI'