import random
from _one_side import OneSide
from _generic import Generic
from _wrap import wrapper2
from marketsim import order, orderbook, scheduler, mathutils, types, registry, meta
from marketsim.types import *

class _LiquidityProviderSide_Impl(OneSide):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        OneSide.__init__(self)
        
    _internals = ['_eventGen']
        
    @property
    def _orderFactory(self):
        return self.orderFactoryT(self.side)
    
    def _orderFunc(self):
        queue = self._trader.book.queue(self.side)
        currentPrice = queue.best.price if not queue.empty else\
                       queue.lastPrice if queue.lastPrice is not None else\
                       self.defaultValue
        price = currentPrice * self.priceDistr()
        volume = int(self.volumeDistr())
        return (price, volume)
    
    def dispose(self):
        OneSide.dispose(self)
        self._eventGen.cancel()

exec wrapper2("LiquidityProviderSide",
             """ Liquidity provider for one side has followng parameters:

                 |side|
                     side of orders to create (default: Side.Sell)
                     
                 |orderFactory| 
                     order factory function (default: order.Limit.T)
                     
                 |initialValue| 
                     initial price which is taken if orderBook is empty (default: 100)
                     
                 |creationIntervalDistr|
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                     
                 |priceDistr|
                     defines multipliers for current asset price when price of
                     order to create is calculated (default: log normal distribution with 
                     |mu| = 0 and |sigma| = 0.1)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 It wakes up in moments of time given by *creationIntervalDistr*, checks
                 the last best price of orders in the corresponding queue, takes *initialValue*
                 if it is empty, multiplies it by a value taken from *priceDistr* to obtain price
                 of the order to create, calculates order volume using *volumeDistr*, creates
                 an order via *orderFactoryT(side)* and tells the trader to send it.
             """,
             [('side',                  'Side.Sell',                            'Side'),
              ('orderFactoryT',         'order.LimitFactory',                   'Side -> (Price, Volume) -> IOrder'),
              ('defaultValue',          '100',                                  'Price'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',        '() -> TimeInterval'),
              ('priceDistr',            'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',        '() -> Volume')])


class ConstantSide(object):
    """ Constant function always returning given *side*. 
    
    Note: We need it since our type system doesn't support for the moment generic
    Constant: () -> 'a
    """
    
    def __init__(self, side = Side.Sell):
        self.side = side
        self._alias = ['Constant side']
        
    _properties = { 'side' : Side }
    _types = [ meta.function((), Side) ]
        
    def __call__(self):
        return self.side
    
class SafeSidePrice(object):
    """ Returns the best price of the given by *orderBook* and *side* order queue, 
        if there is no orders in the queue returns the price of the last trade and
        if there were no trades returns *defaultValue*.
    """
    
    def __init__(self, orderBook, side, defaultValue):
        self.orderBook = orderBook
        self.side = side
        self.defaultValue = defaultValue
        self._alias = ["Asset's", 'Safe order queue price']
        
    _properties = { 'orderBook'     : IOrderBook, 
                    'side'          : Side, 
                    'defaultValue'  : float }
    
    _types = [meta.function((), Price)]
        
    def __call__(self):
        queue = self.orderBook.queue(self.side)
        return queue.best.price if not queue.empty else\
               queue.lastPrice if queue.lastPrice is not None else\
               self.defaultValue

def LiquidityProviderSideEx(side                    = Side.Sell, 
                            orderFactory            = order.LimitFactory, 
                            defaultValue            = 100., 
                            creationIntervalDistr   = mathutils.rnd.expovariate(1.), 
                            priceDistr              = mathutils.rnd.lognormvariate(0., .1), 
                            volumeDistr             = mathutils.rnd.expovariate(1.)):
       
    orderBook = orderbook.OfTrader()
    r = Generic(eventGen    = scheduler.Timer(creationIntervalDistr),
                volumeFunc  = volumeDistr, 
                sideFunc    = ConstantSide(side),
                orderFactory= order.AdaptLimit(orderFactory,
                                               mathutils.product( 
                                                  SafeSidePrice(orderBook, side, defaultValue), 
                                                  priceDistr)))
    
    r._alias = ["Generic", 'LiquidityProviderSide']
    
    return r
