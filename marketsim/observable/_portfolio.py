
from marketsim import event, _, types, ops

from marketsim.asset import StockBase

class PortfolioValue(ops.Observable[float]):
    def __init__(self, trader):
        super(PortfolioValue, self).__init__()
        self.trader = trader

    def __call__(self):
        sum = 0
        for asset, amount in self.portfolio:
            price = self.rough_price(asset)
            if price is None:
                # return None
                pass
            else:
                sum += price
        return sum

    @property
    def portfolio(self):
        return self.trader.portfolio.iteritems()

    def rough_price(self, asset):
        if isinstance(asset, StockBase):
            last_price = self.trader.exchange[asset].lastTrade()
            return last_price[0] if last_price else None
        else:
            # we suppose that the cash is worth 1 per unit
            return 1.0
