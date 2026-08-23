import pandas as pd
import numpy as np

class BuySideValuationEngine:
    """
    Institutional 3-Statement DCF valuation engine incorporating dynamic corporate tax rate
    assumptions and WACC calculations for equity research.
    """
    def __init__(self, ticker: str, terminal_growth: float = 0.025, corporate_tax_rate: float = 0.214):
        self.ticker = ticker
        self.terminal_growth = terminal_growth
        self.tax_rate = corporate_tax_rate

    def calculate_wacc(self, cost_of_equity: float, cost_of_debt: float, equity_weight: float, debt_weight: float) -> float:
        after_tax_debt = cost_of_debt * (1 - self.tax_rate)
        return (equity_weight * cost_of_equity) + (debt_weight * after_tax_debt)

    def run_dcf(self, fcf_projections: list, wacc: float, net_debt: float, shares_outstanding: float) -> dict:
        discount_factors = [(1 + wacc) ** i for i in range(1, len(fcf_projections) + 1)]
        pv_fcf = [fcf / df for fcf, df in zip(fcf_projections, discount_factors)]
        
        terminal_value = (fcf_projections[-1] * (1 + self.terminal_growth)) / (wacc - self.terminal_growth)
        pv_terminal_value = terminal_value / discount_factors[-1]
        
        enterprise_value = sum(pv_fcf) + pv_terminal_value
        equity_value = enterprise_value - net_debt
        implied_share_price = equity_value / shares_outstanding

        return {
            "Ticker": self.ticker,
            "Tax_Rate_Assumption": f"{self.tax_rate:.1%}",
            "Calculated_WACC": f"{wacc:.2%}",
            "Enterprise_Value": f"${enterprise_value:,.2f}M",
            "Equity_Value": f"${equity_value:,.2f}M",
            "Implied_Share_Price": f"${implied_share_price:.2f}"
        }

if __name__ == "__main__":
    engine = BuySideValuationEngine(ticker="JPM", corporate_tax_rate=0.214)
    wacc = engine.calculate_wacc(cost_of_equity=0.095, cost_of_debt=0.045, equity_weight=0.80, debt_weight=0.20)
    
    # 5-Year Projected Free Cash Flows ($ Millions)
    projected_fcf = [22000, 24100, 26500, 28900, 31000]
    valuation = engine.run_dcf(
        fcf_projections=projected_fcf,
        wacc=wacc,
        net_debt=-15000,  # Net cash/debt offset
        shares_outstanding=2870
    )

    print("--- Buy-Side Valuation Report ---")
    for k, v in valuation.items():
        print(f"{k}: {v}")
