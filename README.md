# Buy-Side DCF & LBO Valuation Engine

[![Buy-Side DCF & LBO Valuation Engine CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/stefan931025-sys/buy-side-def-Lbo-engine)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Institutional 3-statement Discounted Cash Flow (DCF) valuation engine and Leveraged Buyout (LBO) sensitivity suite designed for buy-side fundamental equity research, private credit, and special situations analysis.

---

## Features & Financial Methodology

* **Dynamic WACC Calculation:** Computes Weighted Average Cost of Capital incorporating corporate tax shields, CAPM cost of equity, and target capital structure weights.
* **5-Year Unlevered Free Cash Flow (FCFF) Projections:** Models operating cash flows, capital expenditures, working capital deltas, Gordon Growth terminal values, and enterprise-to-equity value bridges.
* **LBO Debt Schedule & Returns Attribution:** Simulates mandatory amortization, cash sweeps, debt paydown, and sponsor IRR / MOIC sensitivity matrices across entry and exit multiples.
* **Scenario Sensitivity:** Evaluates Bull, Base, and Bear operating cases alongside WACC vs. Terminal Growth sensitivity tables.

---

## Mathematical Specifications

### 1. Weighted Average Cost of Capital (WACC)
$$\text{WACC} = \left(\frac{E}{V} \cdot R_e\right) + \left(\frac{D}{V} \cdot R_d \cdot (1 - T_c)\right)$$

### 2. Enterprise Value & Gordon Growth Terminal Value
$$\text{EV} = \sum_{t=1}^{5} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{FCFF}_5 (1 + g)}{(\text{WACC} - g)(1 + \text{WACC})^5}$$

### 3. Sponsor Internal Rate of Return (IRR)
$$\text{IRR} = \left(\frac{\text{Exit Equity}}{\text{Initial Sponsor Equity}}\right)^{\frac{1}{n}} - 1$$

---

## System Architecture & Data Flow

```text
+-----------------------------------------------------------------------------------+
|                     HISTORICAL FINANCIALS & OPERATING ASSUMPTIONS                 |
|         (Revenue Growth, EBITDA Margins, CapEx, NWC, & Capital Structure)         |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                         3-STATEMENT DCF & LBO CORE ENGINE                         |
|  * Dynamic WACC & FCFF Discounting            * Debt Tranche & Cash Sweep Model   |
|  * Enterprise-to-Equity Value Bridge          * Sponsor IRR & MOIC Calculator     |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                       SCENARIO & SENSITIVITY OUTPUT MATRICES                      |
|         (Bull/Base/Bear Cases, WACC vs. Growth Grids, & Exit Multiple Tables)     |
+-----------------------------------------------------------------------------------+
