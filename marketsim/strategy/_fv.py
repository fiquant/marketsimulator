from marketsim import (scheduler, observable, cached_property, types, meta,
                       Side, registry, orderbook, Method, order, mathutils)

from _basic import Strategy, Generic
from _trend import SignalBase, SignalValue, SignalEvent
from _wrap import wrapper

from marketsim.types import *

class FundamentalValueBase(SignalBase):

    def __init__(self, trader):
        SignalBase.__init__(self, trader)
        
    @property
    def _threshold(self):
        return 0.
    
    def _signalFunc(self):
        book = self._trader.book
        fv = self._fundamentalValue()
        
        # if current price is defined, compare it with the fundamental value and define the side
        return +1 if not book.asks.empty\
                  and book.asks.best.price < fv else\
               -1 if not book.bids.empty\
                  and book.bids.best.price > fv else\
               None

class _FundamentalValue_Impl(FundamentalValueBase):

    def __init__(self, trader, params):
        self._params = params
        self._orderFactoryT = params.orderFactory
        self._fundamentalValue = params.fundamentalValue  
        self._eventGen = scheduler.Timer(self._params.creationIntervalDistr)
        
        FundamentalValueBase.__init__(self, trader)
        
    def _volume(self, side):
        return self._params.volumeDistr()


exec  wrapper("FundamentalValue", 
             """ Fundamental value strategy believes that an asset should have some specific price 
                 (*fundamental value*) and if the current asset price is lower than the fundamental value 
                 it starts to buy the asset and if the price is higher it starts to sell the asset. 
             
                 It has following parameters: 
                 
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                 
                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                 
                 |fundamentalValue| 
                     defines fundamental value (default: constant 100)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
              [('orderFactory',         'order.MarketFactory',          'Side -> Volume -> IOrder'),
               ('fundamentalValue',     'mathutils.constant(100)',      '() -> Price'),
               ('volumeDistr',          'mathutils.rnd.expovariate(1.)','() -> Volume'),
               ('creationIntervalDistr','mathutils.rnd.expovariate(1.)','() -> TimeInterval')])

class FundamentalValueSide(object):
    
    def __init__(self, orderBook, fundamentalValue):
        self.orderBook = orderBook
        self.fundamentalValue = fundamentalValue
        self._alias = ["FundamentalValueSide"]
        
    _properties = { 'fundamentalValue'    : meta.function((), Price),
                    'orderBook'           : types.IOrderBook }
    
    _types = [meta.function((), Side)]
        
    def __call__(self):
        fv = self.fundamentalValue()
        book = self.orderBook
        return Side.Buy if not book.asks.empty\
                  and book.asks.best.price < fv else\
               Side.Sell if not book.bids.empty\
                  and book.bids.best.price > fv else\
               None

def FundamentalValueEx(fundamentalValue      = mathutils.constant(100.),
                       orderFactory          = order.MarketFactory, 
                       volumeDistr           = mathutils.rnd.expovariate(1.), 
                       creationIntervalDistr = mathutils.rnd.expovariate(1.)):
    
    r = Generic(orderFactory= orderFactory, 
                volumeFunc  = volumeDistr, 
                eventGen    = scheduler.Timer(creationIntervalDistr), 
                sideFunc    = FundamentalValueSide(orderbook.Proxy(), fundamentalValue))
    
    r._alias = ["Generic", "FundamentalValue"]
    
    return r

class _MeanReversion_Impl(FundamentalValueBase):

    def __init__(self,trader,params):

        self._orderFactoryT = params.orderFactory
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        avg = observable.Fold(observable.Price(trader.book), params.average)
        self._fundamentalValue = avg
        self._volume = Method(params, 'volumeDistr')  
        
        FundamentalValueBase.__init__(self, trader)

exec wrapper("MeanReversion",
             """ Mean reversion strategy believes that asset price should return to its average value.
                 It estimates this average using some functional and 
                 if the current asset price is lower than the average
                 it buys the asset and if the price is higher it sells the asset. 
             
                 It has following parameters: 
                 
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                 
                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                 
                 |average| 
                     functional used to calculate the average 
                     (default: exponentially weighted moving average with |alpha| = 0.15)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('orderFactory',          'order.MarketFactory',              'Side -> Volume -> IOrder'),
              ('average',               'mathutils.ewma(alpha = 0.15)',     'IUpdatableValue'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',    '() -> Volume'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')])

def MeanReversionEx   (average               = mathutils.ewma(alpha = 0.15),
                       orderFactory          = order.MarketFactory, 
                       volumeDistr           = mathutils.rnd.expovariate(1.), 
                       creationIntervalDistr = mathutils.rnd.expovariate(1.)):

    orderBook = orderbook.Proxy()
    avg = observable.Fold(observable.Price(orderBook), average)
    
    r = Generic(orderFactory= orderFactory, 
                volumeFunc  = volumeDistr, 
                eventGen    = scheduler.Timer(creationIntervalDistr), 
                sideFunc    = FundamentalValueSide(orderBook, avg))
    
    r._alias = ["Generic", "MeanReversion"]
    
    return r
        
class _Dependency_Impl(FundamentalValueBase):
    
    def __init__(self,trader,params):
        # start listening changes in a reference asset price
        self._params = params
        self._priceToDependOn = observable.Price(params.bookToDependOn) 
        self._orderFactoryT = params.orderFactory
        
        FundamentalValueBase.__init__(self, trader)

    def _fundamentalValue(self):
        return self._priceToDependOn.value * self._params.factor
    
    def _volume(self, side):
        oppositeQueue = self._trader.book.queue(side.opposite)
        # should we send limit and cancel orders here?
        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(self._fundamentalValue())
        # we want to trade orders only with a good price
        return min(oppositeVolume, self._params.volumeDistr())
    
    @property
    def _eventGen(self):
        return self._priceToDependOn        

exec wrapper("Dependency", 
             """ Dependent price strategy believes that the fair price of an asset *A* 
                 is completely correlated with price of another asset *B* and the following relation 
                 should be held: *PriceA* = *kPriceB*, where *k* is some factor. 
                 It may be considered as a variety of a fundamental value strategy 
                 with the exception that it is invoked every the time price of another
                 asset *B* changes. 
             
                 It has following parameters: 
                 
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                 
                 |bookToDependOn| 
                     reference to order book for another asset used to evaluate fair price of our asset
                 
                 |factor| 
                     multiplier to obtain fair asset price from the reference asset price
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('bookToDependOn','None',                             'IOrderBook'),
              ('orderFactory',  'order.MarketFactory',              'Side -> Volume -> IOrder'),
              ('factor',        '1.',                               'positive'),
              ('volumeDistr',   'mathutils.rnd.expovariate(.1)',    '() -> Volume')], register=False)
        

def DependencyEx      (bookToDependOn,
                       factor                = mathutils.constant(1.),
                       orderFactory          = order.MarketFactory, 
                       volumeDistr           = mathutils.rnd.expovariate(1.)):

    orderBook = orderbook.Proxy()
    priceToDependOn = observable.Price(bookToDependOn) 
    
    r = Generic(orderFactory= orderFactory, 
                volumeFunc  = volumeDistr, 
                eventGen    = SignalEvent(priceToDependOn), 
                sideFunc    = FundamentalValueSide(orderBook, SignalValue(priceToDependOn)))
    
    r._alias = ["Generic", "Dependency"]
    
    return r
