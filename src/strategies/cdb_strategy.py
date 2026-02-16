from .iyield_strategy import IYieldStrategy

class CDBStrategy(IYieldStrategy):
    def __init__(self, percentage_of_cdi: float):
        # AQUI ESTÁ A PROFITABILITY (Rentabilidade)
        # Ex: Se for 100% do CDI, passamos 1.0
        self.percentage_of_cdi = percentage_of_cdi
        # Supondo um CDI fixo para simulação. No futuro, pegaremos de uma API.
        self.current_cdi_rate = 0.12 # 12% a.a.

    def get_profitability_description(self) -> str:
        return f"{self.percentage_of_cdi * 100:.1f}% do CDI"

    def calculate_final_amount(self, principal: float, days: int) -> float:
        # Lógica de Juros Compostos
        daily_rate = (1 + (self.current_cdi_rate * self.percentage_of_cdi)) ** (1/252) - 1
        return principal * ((1 + daily_rate) ** days)

    def calculate_taxes(self, principal: float, gross_amount: float, days: int) -> float:
        # AQUI ESTÁ A TAX (Imposto)
        # Em vez de uma lista de strings, temos a lógica real da tabela regressiva
        profit = gross_amount - principal
        
        if days <= 180: rate = 0.225
        elif days <= 360: rate = 0.20
        elif days <= 720: rate = 0.175
        else: rate = 0.15
        
        return profit * rate