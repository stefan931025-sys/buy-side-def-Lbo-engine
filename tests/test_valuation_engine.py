import pytest

def test_wacc_calculation():
    """Verify Weighted Average Cost of Capital (WACC) formulation."""
    cost_of_equity = 0.10  # 10%
    cost_of_debt = 0.05    # 5%
    tax_rate = 0.27        # 27% tax rate
    weight_equity = 0.60
    weight_debt = 0.40
    
    after_tax_cost_of_debt = cost_of_debt * (1 - tax_rate)
    wacc = (weight_equity * cost_of_equity) + (weight_debt * after_tax_cost_of_debt)
    
    assert pytest.approx(wacc, 0.0001) == 0.0746  # 7.46% WACC

def test_unlevered_free_cash_flow():
    """Verify Unlevered Free Cash Flow (FCFF) calculation."""
    ebit = 1000.0
    tax_rate = 0.27
    d_and_a = 150.0
    capex = 200.0
    nwc_change = 50.0
    
    nopat = ebit * (1 - tax_rate)  # 730.0
    fcff = nopat + d_and_a - capex - nwc_change  # 730 + 150 - 200 - 50 = 630.0
    
    assert pytest.approx(fcff, 0.01) == 630.0
