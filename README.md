# fama-french-factor-analysis

# Analysis of Asset Returns using the Fama-French 3-Factor Model

## 1. Project Objective

The objective of this project is to determine the key risk factors that explain the daily returns of Apple Inc. (AAPL). We will first test the classic Capital Asset Pricing Model (CAPM) and then extend the analysis to the Fama-French 3-Factor Model to see if company size and value factors add significant explanatory power.

## 2. Data Sources

* **Asset Data**: Daily stock prices for AAPL were sourced from the Yahoo Finance API via the `yfinance` library in Python.
* **Factor Data**: The Fama-French 3 factors (Market Excess Return, SMB, HML) and the Risk-Free Rate were sourced directly from the Ken French Data Library.
* **Time Period**: The analysis covers the period from January 1, 2019, to December 31, 2023.

## 3. Methodology

The analysis was conducted using OLS regression in Python with the `statsmodels` library. Two models were estimated:

1.  **CAPM**:
    `Asset_Excess_Return = α + β_mkt * Market_Excess_Return`
2.  **Fama-French 3-Factor Model**:
    `Asset_Excess_Return = α + β_mkt * Market_Excess_Return + β_smb * SMB + β_hml * HML`

Heteroskedasticity-robust standard errors were used to ensure the reliability of the statistical tests.

## 4. Key Findings

* **Model Performance**: The Fama-French model (Adj. R-squared: 0.659) provides a substantially better fit for explaining Apple's returns compared to the simpler CAPM (Adj. R-squared: 0.602). This indicates that size and value are important factors.

* **Market Beta**: Apple exhibits a market beta of approximately **1.18**, which is statistically significant. This suggests that Apple is about 18% more volatile than the overall market.

* **Size and Value Exposure**:
    * The coefficient on the **SMB (size) factor** was significantly negative, indicating that Apple's stock behaves like a **large-cap stock**.
    * The coefficient on the **HML (value) factor** was also significantly negative, indicating that Apple's stock behaves like a **growth stock**.

## 5. Conclusion

This analysis demonstrates that while Apple's returns are strongly tied to the overall market, a more complete picture emerges from the Fama-French 3-Factor model. The results confirm Apple's well-known status as a large-cap growth stock. This project showcases a complete workflow from data sourcing and integration to model estimation and interpretation.
