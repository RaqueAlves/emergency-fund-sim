from abc import ABC, abstractmethod

class IYieldStrategy(ABC):
    '''
    Interface que define APENAS o contrato de cálculo.
    Não guarda dados como nome, risco ou seguradora.
    '''

    @abstractmethod
    def calculate_final_amount(self, principal: float, days: int) -> float:
        """Calcula o valor final bruto (sem impostos)."""
        pass

    @abstractmethod
    def calculate_taxes(self, principal: float, gross_amount: float, days: int) -> float:
        """Calcula o valor total a ser descontado de impostos."""
        pass

    @abstractmethod
    def get_profitability_description(self) -> str:
        """Retorna uma string legível, ex: '100% do CDI'."""
        pass