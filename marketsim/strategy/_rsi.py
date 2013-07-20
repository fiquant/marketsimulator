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

import _wrap

class RSIbis(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return { 'rsi' : observable.RSI(orderbook.OfTrader(), 
                                        self.timeframe, 
                                        self.alpha) }
    
    def getImpl(self):
        return Periodic(orderFactory = self.orderFactory, 
                        volumeFunc   = self.volumeDistr, 
                        eventGen     = scheduler.Timer(self.creationIntervalDistr),
                        sideFunc     = observable.side.Signal(
                                                ops.constant(50) - _.rsi, 
                                                50-self.threshold))
        
_wrap.strategy(RSIbis, ['Periodic', 'RSI bis'], 
               """
               """, 
               [
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('timeframe',             '1.',                            'non_negative'), 
                  ('threshold',             '30.',                           'non_negative'), 
                  ('orderFactory',          'order.MarketFactory',           'Side -> Volume -> IOrder'),
                  ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
                  ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')
               ], globals())

class RSIEx(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return { 'rsi' : observable.Fold(observable.MidPrice(orderbook.OfTrader()),
                                         mathutils.rsi(self.alpha)) }
    
    def getImpl(self):
        return  Periodic(orderFactory= self.orderFactory, 
                         volumeFunc  = self.volumeDistr, 
                         eventGen    = scheduler.Timer(self.creationIntervalDistr), 
                         sideFunc    = RelativeStrengthIndexSide(orderbook.OfTrader(), 
                                                                 _.rsi, 
                                                                 self.threshold))
        
_wrap.strategy(RSIEx, ['Periodic', 'RSI ex'], 
               """
               """, 
               [
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('threshold',             '30.',                           'non_negative'), 
                  ('orderFactory',          'order.MarketFactory',           'Side -> Volume -> IOrder'),
                  ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
                  ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')
               ], globals())

    
from _desired_position import DesiredPosition

class RSI_linear(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return { 'rsi' : observable.RSI(orderbook.OfTrader(), 
                                        self.timeframe, 
                                        self.alpha) }
    
    def getImpl(self):
        return DesiredPosition(
                    orderFactory = self.orderFactory, 
                    desiredPosition = observable.OnEveryDt(1, 
                                            (ops.constant(50) - _.rsi) * self.k))

_wrap.strategy(RSI_linear, ['Desired position', 'RSI linear'], 
               """
               """, 
               [
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('k',                     'ops.constant(-0.04)',           'IFunction[float]'), 
                  ('timeframe',             '1.',                            'non_negative'), 
                  ('orderFactory',          'order.MarketFactory',           'Side -> Volume -> IOrder'),
               ], globals())
    
