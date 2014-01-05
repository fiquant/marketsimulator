from marketsim import (request, context, combine, Side, registry, meta, types, bind, Order,
                       event, _, ops, observable, orderbook)
from marketsim.types import *

from marketsim.gen._intrinsic.order.meta.floating_price import Order_Impl as FloatingPrice

def Peg(order):
    """ Peg is a virtual order that ensures that it has the best price in the order book. 
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

# unfortunately we cannot use _floating_price.Factory since price function depends on the order side 
class Factory_Impl(ops.Observable[Order]):
    
    def __call__(self):
        proto = self.proto(ops.constant(0))()
        return Peg(proto) if proto is not None else None
