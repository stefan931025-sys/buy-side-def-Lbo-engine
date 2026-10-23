import argparse
import yfinance as yf

class BuySideValuationEngine:
    """
    Live Buy-Side 3-Statement DCF & Valuation Program.
    """
    def __init__(self, ticker: str, corporate_tax_rate: float = 0.214, terminal_growth: float = 0.025):
        self.ticker_str = ticker
        self.tax_rate = corporate_tax_rate
        self.terminal_growth = terminal_growth
        self.stock = yf.Ticker(ticker)

    def run_dcf(self, cost_of_equity: float = 0.10, cost_of_debt: float = 0.05, equity_weight: float = 0.85) -> dict:
        info = self.stock.info
        
        # Calculate WACC
        debt_weight = 1.0 - equity_weight
        after_tax_debt = cost_of_debt * (1 - self.tax_rate)
        wacc = (equity_weight * cost_of_equity) + (debt_weight * after_tax_debt)

        # Retrieve live market data
        current_price = info.get("currentPrice", info.get("previousClose", 0.0))
        shares_out = info.get("sharesOutstanding", 1) / 1e6  # Millions
        total_debt = info.get("totalDebt", 0.0) / 1e6
        cash = info.get("totalCash", 0.0) / 1e6
        net_debt = total_debt - cash

        # Estimate Free Cash Flow from Operating Cash Flow
        fcf_base = info.get("freeCashflow", info.get("operatingCashflow", 1000000000)) / 1e6
        
        # Project 5-year FCF assuming 5% steady growth baseline
        projected_fcf = [fcf_base * ((1.05) ** i) for i in range(1, 6)]
        discount_factors = [(1 + wacc) ** i for i in range(1, 6)]
        pv_fcf = [fcf / df for fcf, df in zip(projected_fcf, discount_factors)]

        terminal_value = (projected_fcf[-1] * (1 + self.terminal_growth)) / (wacc - self.terminal_growth)
        pv_terminal_value = terminal_value / discount_factors[-1]

        enterprise_value = sum(pv_fcf) + pv_terminal_value
        equity_value = enterprise_value - net_debt
        implied_share_price = equity_value / shares_out if shares_out > 0 else 0.0

        upside_downside = ((implied_share_price - current_price) / current_price) if current_price > 0 else 0.0

        return {
            "Ticker": self.ticker_str.upper(),
            "Current_Market_Price": f"${current_price:.2f}",
            "Tax_Rate_Assumption": f"{self.tax_rate:.1%}",
            "WACC": f"{wacc:.2%}",
            "Enterprise_Value": f"${enterprise_value:,.2f}M",
            "Equity_Value": f"${equity_value:,.2f}M",
            "Implied_Target_Price": f"${implied_share_price:.2f}",
            "Implied_Upside": f"{upside_downside:+.2%}"
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Buy-Side Valuation Engine")
    parser.add_argument("--ticker", type=str, default="JPM", help="Equity Ticker (e.g. JPM, AAPL, MSFT)")
    parser.add_argument("--tax_rate", type=float, default=0.214, help="Corporate tax rate (e.g. 0.214 for 21.4%)")
    args = parser.parse_args()

    engine = BuySideValuationEngine(ticker=args.ticker, corporate_tax_rate=args.tax_rate)
    report = engine.run_dcf()

    print("\n================ BUY-SIDE INSTITUTIONAL VALUATION ================")
    for k, v in report.items():
        print(f"{k:<24}: {v}")
    print("==================================================================\n")
