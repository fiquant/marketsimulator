from marketsim import registry, Side
from _limit import LimitFactory
from _market import MarketFactory

@registry.expose(alias=['LimitMarketOrder'])
def LimitMarket(volume, price=None):
    """ Creates an order with a signed volume.
     If a price is provided, a Limit order is created.
     Else, a Market order is created instead.

     For example calling LimitMarket(volume = -1, price=10)
     creates a Sell Limit order at a price of 10.
    """
    side = Side.Sell if volume < 0 else Side.Buy
    if price:
        return LimitFactory(side)(price, abs(volume))
    else:
        return MarketFactory(side)(abs(volume))
