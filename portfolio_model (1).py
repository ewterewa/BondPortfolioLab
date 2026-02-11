
import numpy as np


class Bond:
    def __init__(self, name, ytm, duration, credit_score):
        '''
        name: bond name
        ytm: yield to maturity (%)
        duration: duration (years)
        credit_score: credit risk score (1 - low risk, 5 - high risk)
        '''
        self.name = name
        self.ytm = ytm
        self.duration = duration
        self.credit_score = credit_score


class BondPortfolio:
    def __init__(self, bonds, weights):
        '''
        bonds: list of Bond objects
        weights: list of portfolio weights (must sum to 1)
        '''
        if abs(sum(weights) - 1) > 1e-6:
            raise ValueError("Weights must sum to 1")
        self.bonds = bonds
        self.weights = weights

    def portfolio_yield(self):
        return sum(w * b.ytm for w, b in zip(self.weights, self.bonds))

    def portfolio_duration(self):
        return sum(w * b.duration for w, b in zip(self.weights, self.bonds))

    def modified_duration(self):
        y = self.portfolio_yield() / 100
        return self.portfolio_duration() / (1 + y)

    def price_sensitivity(self, delta_rate):
        '''
        delta_rate: change in interest rate (%)
        Returns approximate % change in portfolio value
        '''
        d_mod = self.modified_duration()
        return -d_mod * (delta_rate / 100)

    def credit_risk_index(self):
        return sum(w * b.credit_score for w, b in zip(self.weights, self.bonds))

    def summary(self, delta_rate=1):
        return {
            "Portfolio Yield (%)": round(self.portfolio_yield(), 2),
            "Portfolio Duration (years)": round(self.portfolio_duration(), 2),
            "Modified Duration": round(self.modified_duration(), 2),
            f"Price Change if rate +{delta_rate}% (%)":
                round(self.price_sensitivity(delta_rate) * 100, 2),
            "Credit Risk Index (1-5)": round(self.credit_risk_index(), 2)
        }


if __name__ == "__main__":
    # Example usage
    ofz = Bond("OFZ", 6.5, 5, 1)
    corp_inv = Bond("Corporate Investment Grade", 8.0, 6, 2)
    corp_high = Bond("High Yield Corporate", 11.0, 4, 4)

    portfolio = BondPortfolio(
        bonds=[ofz, corp_inv, corp_high],
        weights=[0.4, 0.4, 0.2]
    )

    print(portfolio.summary(delta_rate=1))
