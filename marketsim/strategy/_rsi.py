from marketsim.types import *
from marketsim import (parts, meta, types, order, _, defs, ops,
                       mathutils, observable, scheduler, orderbook, registry)

from _generic import Generic

import _wrap

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
    
class RSI_linear(types.ISingleAssetStrategy):

    def getImpl(self):
        return Generic(
                    order.factory.MarketSigned(
                        parts.signed_volume.RSI_linear(self.alpha, 
                                                       self.k, 
                                                       self.timeframe)))

_wrap.strategy(RSI_linear, ['Desired position', 'RSI linear'], 
               """
               """, 
               [
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('k',                     'ops.constant(-0.04)',           'IFunction[float]'), 
                  ('timeframe',             '1.',                            'non_negative'), 
               ], globals())
    
