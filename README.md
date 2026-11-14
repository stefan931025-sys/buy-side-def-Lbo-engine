# Buy-Side DCF & LBO Valuation Engine

![CI Workflow](https://github.com/stefan931025-sys/buy-side-dcf-lbo-engine/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Institutional 3-statement Discounted Cash Flow (DCF) valuation engine and Leveraged Buyout (LBO) sensitivity suite designed for buy-side fundamental equity research, private credit, and special situations analysis.

## 🚀 Features & Financial Methodology

* **Dynamic WACC Calculation:** Computes Weighted Average Cost of Capital incorporating corporate tax shields, CAPM cost of equity, and target capital structure weights.
* **5-Year Unlevered Free Cash Flow (FCFF) Projections:** Models operating cash flows, capital expenditures, working capital deltas, Gordon Growth terminal values, and enterprise-to-equity value bridges.
* **LBO Debt Schedule & Returns Attribution:** Simulates mandatory amortization, cash sweeps, debt paydown, and sponsor IRR / MOIC sensitivity matrices across entry and exit multiples.
* **Scenario Sensitivity:** Evaluates Bull, Base, and Bear operating cases alongside WACC vs. Terminal Growth sensitivity tables.

---

## 📊 Mathematical Specifications

### 1. Weighted Average Cost of Capital (WACC)

$$\text{WACC} = \left(\frac{E}{V} \cdot R_e\right) + \left(\frac{D}{V} \cdot R_d \cdot (1 - T_c)\right)$$

### 2. Enterprise Value & Gordon Growth Terminal Value

$$\text{EV} = \sum_{t=1}^{5} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{FCFF}_5(1 + g)}{(\text{WACC} - g)(1 + \text{WACC})^5}$$

### 3. Sponsor Internal Rate of Return (IRR)

$$\text{IRR} = \left(\frac{\text{Exit Equity}}{\text{Initial Sponsor Equity}}\right)^{\frac{1}{n}} - 1$$

---

## 📁 Repository Structure

```text
buy-side-dcf-lbo-engine/
├── .devcontainer/     # Devcontainer configuration for Codespaces
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions automated test workflow
├── core/
│   └── financial_valuation_engine.py # DCF & LBO valuation modules
├── tests/
│   └── test_valuation_engine.py # Automated pytest suite
├── main.py            # Main execution pipeline script
├── repo_auditor.py    # Static AST analysis governance tool
├── requirements.txt   # Python dependencies
└── README.md          # System documentation
