from abc import ABC, abstractmethod

class IYieldStrategy(ABC):
    """
    Interface (Contrato) que define como qualquer ativo de renda fixa deve se comportar.
    """

    @abstractmethod
    def calculate_gross_amount(self, principal: float, days: int) -> float:
        """Calcula o valor final bruto (sem descontar
        impostos) de uma aplicação em um período definido.
        @param principal: valor inicial investido
        @param days: número de dias da aplicação"""
        pass

    @abstractmethod
    def calculate_taxes(self, principal: float, gross_amount: float, days: int) -> float:
        """Calcula o valor total a ser descontado de impostos,
        baseado no valor bruto e no número de dias da aplicação.
        Se for isento, deve retornar 0.0
        @param principal: valor inicial investido
        @param gross_amount: valor bruto calculado
        @param days: número de dias da aplicação"""
        pass

    @abstractmethod
    def get_profitability_description(self) -> str:
        """Retorna uma string legível, ex: '100% do CDI'."""
        pass