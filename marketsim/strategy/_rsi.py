from marketsim import meta, types, order, mathutils, observable, Side, scheduler, orderbook, registry

from _generic import Generic

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