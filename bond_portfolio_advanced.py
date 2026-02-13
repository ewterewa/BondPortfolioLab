import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# 1. Исходные данные по облигациям
# ==============================

bonds = pd.DataFrame({
    "Bond": [
        "OFZ 26238",
        "OFZ-IN 52002",
        "RZD 001R-28R",
        "Gazprom BO-26",
        "SIBUR BO-03"
    ],
    "Yield": [0.12, 0.11, 0.13, 0.14, 0.15],
    "Duration": [6, 5, 4, 4, 3],
    "Weight": [0.25, 0.15, 0.20, 0.25, 0.15]
})


# ==============================
# 2. Расчет параметров портфеля
# ==============================

portfolio_yield = np.sum(bonds["Yield"] * bonds["Weight"])
portfolio_duration = np.sum(bonds["Duration"] * bonds["Weight"])

print("\n===== PORTFOLIO PARAMETERS =====")
print("Portfolio Yield:", round(portfolio_yield * 100, 2), "%")
print("Portfolio Duration:", round(portfolio_duration, 2), "years")


# ==============================
# 3. Процентный риск
# ==============================

delta_rate = 0.01
price_change = -portfolio_duration * delta_rate

print("\n===== INTEREST RATE RISK =====")
print("Price change if rate increases by 1%:",
      round(price_change * 100, 2), "%")


# ==============================
# 4. Кредитные спреды
# ==============================

ofz_yield = 0.12
bonds["Spread_vs_OFZ"] = bonds["Yield"] - ofz_yield

print("\n===== CREDIT SPREADS =====")
print(bonds[["Bond", "Spread_vs_OFZ"]])


# ==============================
# 5. Финансовый анализ компаний
# ==============================

companies = pd.DataFrame({
    "Company": ["RZD", "Gazprom", "SIBUR"],
    "Debt": [500, 900, 400],
    "EBITDA": [200, 350, 180],
    "EBIT": [150, 300, 150],
    "Interest": [30, 60, 25],
    "Equity": [600, 1500, 500],
    "Net Income": [100, 250, 120],
    "Revenue": [1000, 2500, 900]
})

companies["Debt/EBITDA"] = companies["Debt"] / companies["EBITDA"]
companies["Interest Coverage"] = companies["EBIT"] / companies["Interest"]
companies["ROE"] = companies["Net Income"] / companies["Equity"]
companies["Net Margin"] = companies["Net Income"] / companies["Revenue"]

print("\n===== FINANCIAL ANALYSIS =====")
print(companies[[
    "Company",
    "Debt/EBITDA",
    "Interest Coverage",
    "ROE",
    "Net Margin"
]])


# ==============================
# 6. Value-at-Risk (VaR)
# ==============================

confidence = 0.95
z_score = 1.65

volatility = portfolio_duration * 0.01
VaR = z_score * volatility

print("\n===== VALUE AT RISK (95%) =====")
print("Portfolio VaR:", round(VaR * 100, 2), "%")


# ==============================
# 7. Визуализация
# ==============================

plt.figure()
plt.bar(bonds["Bond"], bonds["Weight"] * 100)
plt.xticks(rotation=45)
plt.ylabel("Weight (%)")
plt.title("Portfolio Structure")
plt.show()


rate_changes = np.linspace(-0.02, 0.02, 100)
price_changes = -portfolio_duration * rate_changes

plt.figure()
plt.plot(rate_changes * 100, price_changes * 100)
plt.xlabel("Interest Rate Change (%)")
plt.ylabel("Portfolio Price Change (%)")
plt.title("Interest Rate Sensitivity")
plt.grid()
plt.show()


# ==============================
# 8. Итог
# ==============================

print("\n===== CONCLUSION =====")
print("The portfolio provides a yield of approximately",
      round(portfolio_yield * 100, 2),
      "% with moderate duration risk and diversified credit exposure.")
