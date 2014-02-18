from marketsim.gen._out._side import Side

from marketsim.gen._intrinsic.order.meta.floating_price import Order_Impl as FloatingPrice

def Peg(order):
    """ Peg is a virtual order that ensures that it has the best price in the order book. 
    It is implemented as a limit order which is cancelled 
    once the best price in the order queue has changed 
    and is sent again to the order book 
    with a price one tick better than the best price in the book.
    """
    from marketsim.gen._out.orderbook._oftrader import OfTrader
    from marketsim.gen._out.orderbook._ticksize import TickSize
    from marketsim.gen._out.orderbook.ask._price import Price as AskPrice
    from marketsim.gen._out.orderbook.bid._price import Price as BidPrice
    from marketsim.gen._out.math.Cumulative._maxepsilon import MaxEpsilon
    from marketsim.gen._out.math.Cumulative._minepsilon import MinEpsilon

    side = order.side
    book = OfTrader()
    tickSize = TickSize(book)
    askPrice = AskPrice(book)
    bidPrice = BidPrice(book)
    
    price = MinEpsilon(askPrice, tickSize)\
                if side == Side.Sell else\
            MaxEpsilon(bidPrice, tickSize)

    return FloatingPrice(order, price)

from marketsim.event import Event_Impl

# unfortunately we cannot use _floating_price.Factory since price function depends on the order side 
class Factory_Impl(Event_Impl):
    
    def __call__(self):
        from marketsim.gen._out._constant import constant
        proto = self.proto(constant(0))()
        return Peg(proto) if proto is not None else None
