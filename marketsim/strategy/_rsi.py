from marketsim import meta, types, order, mathutils, observable, Side, scheduler, orderbook, registry

from _generic import Generic
from _signal import SignalSide

class RelativeStrengthIndexSide(object):
    
    def __init__(self, orderBook, rsi, threshold=30):
        self.orderBook = orderBook
        self.rsi = rsi
        self.threshold = threshold
        self._alias = ["RelativeStrengthIndexSide"]
        
    _properties = { 'rsi'       : meta.function((), types.Price),
                    'orderBook' : types.IOrderBook }
    
    _types = [meta.function((), Side)]
        
    def __call__(self):
        rsi = self.rsi()
        book = self.orderBook
        if rsi is None:
            return None

        return Side.Buy if not book.asks.empty\
                  and rsi < self.threshold else\
               Side.Sell if not book.bids.empty\
                  and rsi > (100 - self.threshold) else\
               None

@registry.expose(["Generic", "RSI"], args=())
def RSIEx    (         alpha                 = 1./14,
                       threshold             = 30,
                       orderFactory          = order.MarketFactory, 
                       volumeDistr           = mathutils.rnd.expovariate(1.), 
                       creationIntervalDistr = mathutils.rnd.expovariate(1.)):

    orderBook = orderbook.OfTrader()

    rsi = observable.Fold(observable.Price(orderBook), mathutils.rsi(alpha))
    
    r = Generic(orderFactory= orderFactory, 
                volumeFunc  = volumeDistr, 
                eventGen    = scheduler.Timer(creationIntervalDistr), 
                sideFunc    = RelativeStrengthIndexSide(orderBook, rsi, threshold))
    
    return r

def RSIbis (timeframe               = 0., 
            threshold               = 30,
            alpha                   = 1./14,
            orderFactory            = order.MarketFactory, 
            volumeDistr             = mathutils.rnd.expovariate(1.), 
            creationIntervalDistr   = mathutils.rnd.expovariate(1.)):
    
    thisBook = orderbook.OfTrader()
    
    rsi = observable.RSI(thisBook, timeframe, alpha)
    
    return Generic(orderFactory = orderFactory, 
                   volumeFunc   = volumeDistr, 
                   eventGen     = scheduler.Timer(creationIntervalDistr),
                   sideFunc     = SignalSide(mathutils.sub(mathutils.constant(50), 
                                                           rsi), 
                                             50-threshold))