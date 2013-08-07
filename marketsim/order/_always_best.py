from marketsim import (request, context, combine, Side, registry, meta, types, bind, 
                       event, _, ops, observable, orderbook)
from _limit import LimitFactory, Limit
from _limit import PriceVolume_Factory
from _floating_price import FloatingPrice
from marketsim.types import *
import _meta

def AlwaysBest2(pricevolume_factory, volume):
    """ AlwaysBest is a virtual order that ensures that it has the best price in the order book. 
    It is implemented as a limit order which is cancelled 
    once the best price in the order queue has changed 
    and is sent again to the order book 
    with a price one tick better than the best price in the book.
    """

    side = pricevolume_factory.side
    book = orderbook.OfTrader()
    tickSize = observable.TickSize(book)
    askPrice = observable.AskPrice(book)
    bidPrice = observable.BidPrice(book)
    
    price = observable.MinEpsilon(askPrice, tickSize)\
                if side == Side.Sell else\
            observable.MaxEpsilon(bidPrice, tickSize)

    return FloatingPrice(pricevolume_factory, price, volume)

class Factory(types.IPersistentOrderGenerator, combine.SideVolume):
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    def __call__(self):
        params = combine.SideVolume.__call__(self)
        if params is None:
            return None
        pricevolume_factory = PriceVolume_Factory(ops.constant(params[0]))
        order = AlwaysBest2(pricevolume_factory, params[1])
        context.bind(order, self._ctx)
        return order
