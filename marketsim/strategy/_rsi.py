from marketsim.types import *
from marketsim import (meta, types, order, _, defs, ops,
                       mathutils, observable, scheduler, orderbook, registry)

from _periodic import Periodic

@registry.expose(["RelativeStrengthIndexSide"])
class RelativeStrengthIndexSide(object):
    
    def __init__(self, orderBook=None, rsi=None, threshold=30):
        self.orderBook = orderBook if orderBook is not None else orderbook.OfTrader()
        self.rsi = rsi if rsi is not None else observable.Fold(observable.MidPrice(self.orderBook), 
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

    rsi = observable.Fold(observable.MidPrice(orderBook), mathutils.rsi(alpha))
    
    r = Periodic(orderFactory= orderFactory, 
                 volumeFunc  = volumeDistr, 
                 eventGen    = scheduler.Timer(creationIntervalDistr), 
                 sideFunc    = RelativeStrengthIndexSide(orderBook, rsi, threshold))
    
    return r

@registry.expose(["Periodic", "RSIbis"], args=())
def RSIbis (timeframe               = 1., 
            threshold               = 30,
            alpha                   = 1./14,
            orderFactory            = order.MarketFactory, 
            volumeDistr             = mathutils.rnd.expovariate(1.), 
            creationIntervalDistr   = mathutils.rnd.expovariate(1.)):
    
    thisBook = orderbook.OfTrader()
    
    return defs(Periodic(orderFactory = orderFactory, 
                         volumeFunc   = volumeDistr, 
                         eventGen     = scheduler.Timer(creationIntervalDistr),
                         sideFunc     = observable.side.Signal(ops.constant(50) - _.rsi, 
                                                               50-threshold)), 
                { 'rsi' : observable.RSI(thisBook, timeframe, alpha) })
    
from _desired_position import DesiredPosition
    
@registry.expose(['Desired position', 'RSI linear'])
def RSI_linear(timeframe               = 1., 
               alpha                   = 1./14,
               k                       = ops.constant(-0.04),
               orderFactory            = order.MarketFactory):
    
    thisBook = orderbook.OfTrader()
    
    return defs(DesiredPosition(
                        orderFactory = orderFactory, 
                        desiredPosition = observable.OnEveryDt(1, (ops.constant(50) - _.rsi) * k)), 
                { 'rsi' : observable.RSI(thisBook, timeframe, alpha) })
