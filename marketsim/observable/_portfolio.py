
from marketsim import event, _, types, ops

from marketsim.asset import StockBase

class PortfolioValue(ops.Observable[float]):
    def __init__(self, trader, exchange=None):
        super(PortfolioValue, self).__init__()
        self.trader = trader
        self.exchange = self.trader.exchange if exchange is None else exchange

    def __call__(self):
        return self.price(self.portfolio)

    def price(self, portfolio):
        return sum([amount*self.rough_price(asset) for asset, amount in portfolio.items()])

    @property
    def portfolio(self):
        return self.trader.portfolio

    def rough_price(self, asset):
        if isinstance(asset, StockBase):
            last_price = self.exchange[asset].lastTrade()
            return last_price[0] if last_price else 0.0
        else:
            # we suppose that the cash is worth 1 per unit
            return 1.0