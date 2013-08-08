from marketsim import request, combine, meta, types, _, registry, bind, Side

from _limit import LimitFactory

import _meta

class LimitMarket(_meta.Base):
    """ This a combination of a limit order and a cancel order sent immediately
    It works as a market order in sense that it is not put into the order queue 
    but can be matched (as a limit order) 
    only if there are orders with suitable price in the queue
    """
    
    def __init__(self, side, price, volume, owner = None):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        _meta.Base.__init__(self, volume, owner)
        self.side = side
        # we create a limit order
        self._order = LimitFactory(side)(price, volume)
        self._order.owner = self
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
        
    def processIn(self, orderBook):
        orderBook.process(self._order)
        orderBook.process(request.Cancel(self._order))
        
    @property 
    def volumeUnmatched(self):
        return self._order.volumeUnmatched 
    
    @staticmethod
    def Buy(price, volume): return LimitMarket(Limit.Buy, price, volume)
    
    @staticmethod
    def Sell(price, volume): return LimitMarket(Limit.Sell, price, volume)

class Factory(types.IOrderGenerator, combine.SidePriceVolume):
    
    def __call__(self):
        params = combine.SidePriceVolume.__call__(self)
        return LimitMarket(*params) if params is not None else None

    
@registry.expose(alias=['LimitMarket'])
@meta.sig(args=(Side,), rv=meta.function((types.Price,), types.IOrder))
def LimitMarketFactory(side):
    return bind.Construct(LimitMarket, side)

LimitMarketFactory.__doc__ = LimitMarket.__doc__

