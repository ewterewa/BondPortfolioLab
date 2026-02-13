import numpy as np

class Bond:
    def __init__(self, name, yield_rate, duration, weight):
        self.name = name
        self.yield_rate = yield_rate
        self.duration = duration
        self.weight = weight


class BondPortfolio:
    def __init__(self, bonds):
        self.bonds = bonds

    def portfolio_yield(self):
        return sum(b.weight * b.yield_rate for b in self.bonds)

    def portfolio_duration(self):
        return sum(b.weight * b.duration for b in self.bonds)

    def price_change(self, delta_rate):
        D = self.portfolio_duration()
        return -D * delta_rate
