from marketsim import (request, context, combine, Side, registry, meta, types, bind, 
                       event, _, ops, observable, orderbook)
import _limit 
from _floating_price import FloatingPrice
from marketsim.types import *
import _meta

def AlwaysBest2(order):
    """ AlwaysBest is a virtual order that ensures that it has the best price in the order book. 
    It is implemented as a limit order which is cancelled 
    once the best price in the order queue has changed 
    and is sent again to the order book 
    with a price one tick better than the best price in the book.
    """

    side = order.side
    book = orderbook.OfTrader()
    tickSize = observable.TickSize(book)
    askPrice = observable.AskPrice(book)
    bidPrice = observable.BidPrice(book)
    
    price = observable.MinEpsilon(askPrice, tickSize)\
                if side == Side.Sell else\
            observable.MaxEpsilon(bidPrice, tickSize)

    return FloatingPrice(order, price)

class Factory(types.IPersistentOrderGenerator):
    
    def __init__(self, factory = _limit.Price_Factory()):
        self.factory = factory
        
    _properties = { # IPersistentOrderFactory[Price]
        'factory' : types.IFunction[IOrderGenerator, float] 
    }
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    def __call__(self):
        proto = self.factory.create(price = 0)
        if proto is not None:
            order = AlwaysBest2(proto)
            context.bind(order, self._ctx)
        return order
