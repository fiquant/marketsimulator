import random
from marketsim import order, scheduler, observable, cached_property, mathutils

from _trend import SignalBase
from _basic import Wrapper, currentframe
from codetools.util.cbook import wrap

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
        """ Creates a fundamental value trader
        trader - single asset single market trader
        orderFactoryT - order factory function: side -> *orderParams -> Order
        fundamentalValue - defines fundamental value 
                                (default: constant 100)
        volumeDistr - function to determine volume of orders to create 
                                (default: exponential distribution with \lambda=1) 
        creationIntervalDistr - defines intervals of time between order creation 
                                (default: exponential distribution with \lambda=1)
        """
        self._params = params
        self._orderFactoryT = params.orderFactory
        self._fundamentalValue = params.fundamentalValue  
        
        FundamentalValueBase.__init__(self, trader)
        
    def _volume(self, side):
        return self._params.volumeDistr()
        
    @cached_property
    def _eventGen(self):
        return scheduler.Timer(self._params.creationIntervalDistr)

def FundamentalValue(orderFactory=order.Market.T,
                     fundamentalValue=lambda: 100,
                     volumeDistr= lambda: random.expovariate(1.),
                     creationIntervalDistr=lambda: random.expovariate(1.)):
    
    return Wrapper(_FundamentalValue_Impl, currentframe())

class _MeanReversion_Impl(FundamentalValueBase):

    def __init__(self,trader,params):

        self._orderFactoryT = params.orderFactory
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        avg = observable.Fold(observable.Price(trader.book), params.average)
        self._fundamentalValue = lambda: avg.value
        self._volume = lambda side: params.volumeDistr()  
        
        FundamentalValueBase.__init__(self, trader)
        
def MeanReversion(orderFactory=order.Market.T,
                  average = mathutils.ewma(alpha = 0.15),
                  volumeDistr= lambda: random.expovariate(1.),
                  creationIntervalDistr=lambda: random.expovariate(1.)):
    
    return Wrapper(_MeanReversion_Impl, currentframe())

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

def Dependency(bookToDependOn,
               orderFactory=order.Market.T,
               factor=1.,
               volumeDistr=lambda: random.expovariate(.1)):
    """ Creates a strategy that believes that fair asset price 
    can be obtained as current price of another asset multiplied by some factor
    Once this relation doesn't hold it tries to buy or sell orders with better price     

    trader - single asset single market trader
    bookToDependOn - asset that is considered as reference one
    orderFactory - order factory function: side -> *orderParams -> Order
    factor - multiplier to obtain fair the asset price by reference price
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    
    return Wrapper(_Dependency_Impl, currentframe())