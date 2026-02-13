import pandas as pd

def calculate_debt_ebitda(debt, ebitda):
    return debt / ebitda

def interest_coverage(ebit, interest):
    return ebit / interest

def roe(net_income, equity):
    return net_income / equity

def net_margin(net_income, revenue):
    return net_income / revenue
