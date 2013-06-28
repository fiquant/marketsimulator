from marketsim.types import *
from marketsim import (meta, types, order, _, defs, ops,
                       mathutils, observable, scheduler, orderbook, registry)

from _periodic import Periodic
from _signal import SignalSide

@registry.expose(["RelativeStrengthIndexSide"])
class RelativeStrengthIndexSide(object):
    
    def __init__(self, orderBook=None, rsi=None, threshold=30):
        self.orderBook = orderBook if orderBook is not None else orderbook.OfTrader()
        self.rsi = rsi if rsi is not None else observable.Fold(observable.Price(self.orderBook), 
                                                               mathutils.rsi(1./14))
        self.threshold = threshold
        
    _properties = { 'rsi'       : types.IFunction[float],
                    'orderBook' : types.IOrderBook,
                    'threshold' : float }
    
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

@registry.expose(["Periodic", "RSI"], args=())
def RSIEx    (         alpha                 = 1./14,
                       threshold             = 30,
                       orderFactory          = order.MarketFactory, 
                       volumeDistr           = mathutils.rnd.expovariate(1.), 
                       creationIntervalDistr = mathutils.rnd.expovariate(1.)):

    orderBook = orderbook.OfTrader()

    rsi = observable.Fold(observable.Price(orderBook), mathutils.rsi(alpha))
    
    r = Periodic(orderFactory= orderFactory, 
                 volumeFunc  = volumeDistr, 
                 eventGen    = scheduler.Timer(creationIntervalDistr), 
                 sideFunc    = RelativeStrengthIndexSide(orderBook, rsi, threshold))
    
    return r

@registry.expose(["Periodic", "RSIbis"], args=())
def RSIbis (timeframe               = 0., 
            threshold               = 30,
            alpha                   = 1./14,
            orderFactory            = order.MarketFactory, 
            volumeDistr             = mathutils.rnd.expovariate(1.), 
            creationIntervalDistr   = mathutils.rnd.expovariate(1.)):
    
    thisBook = orderbook.OfTrader()
    
    return defs(Periodic(orderFactory = orderFactory, 
                         volumeFunc   = volumeDistr, 
                         eventGen     = scheduler.Timer(creationIntervalDistr),
                         sideFunc     = SignalSide(ops.constant(50) - _.rsi, 
                                                   50-threshold)), 
                { 'rsi' : observable.RSI(thisBook, timeframe, alpha) })