from marketsim.types import *
from marketsim import (parts, meta, types, order, _, defs, ops,
                       mathutils, observable, scheduler, orderbook, registry)

from .. import _wrap
from .._generic import Generic

class RSIbis(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return { 'rsi' : observable.RSI(orderbook.OfTrader(), 
                                        self.timeframe, 
                                        self.alpha) }
    
    def getImpl(self):
        return Generic(
                  order.factory.Market(
                     side = parts.side.Signal(ops.constant(50) - _.rsi, 
                                              50-self.threshold), 
                     volume = self.volumeDistr), 
                  scheduler.Timer(self.creationIntervalDistr))
        
_wrap.strategy(RSIbis, ['Periodic', 'RSI bis'], 
               """
               """, 
               [
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('timeframe',             '1.',                            'non_negative'), 
                  ('threshold',             '30.',                           'non_negative'), 
                  ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
                  ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')
               ], globals())
