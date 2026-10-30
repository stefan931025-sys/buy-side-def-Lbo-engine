# Buy-Side DCF & LBO Valuation Engine

[![CI Pipeline](https://github.com/stefan931025-sys/buy-side-def-lbo-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/stefan931025-sys/buy-side-def-lbo-engine/actions/workflows/ci.yml)

![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Description

Institutional 3-statement Discounted Cash Flow (DCF) valuation engine and Leveraged Buyout (LBO) sensitivity suite designed for buy-side fundamental equity research.

## 📌 Features & Financial Methodology

* **Dynamic WACC Calculation:** Calculates weighted average cost of capital with exact corporate tax rate assumptions and capital structure weighting.
* **5-Year Unlevered Free Cash Flow (FCFF) Projections:** Incorporates terminal growth rate modeling and net debt equity adjustments.
* **Scenario Sensitivity:** Evaluates Bull/Base/Bear operating scenarios and exit multiple sensitivity matrices.

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/stefan931025-sys/buy-side-def-lbo-engine.git](https://github.com/stefan931025-sys/buy-side-def-lbo-engine.git)
cd buy-side-def-lbo-engine

# Run valuation engine from src directory
python src/financial_valuation_engine.py
