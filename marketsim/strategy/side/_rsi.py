from marketsim.types import *
from marketsim import (event,parts, meta, types, order, _, defs, ops,
                       mathutils, observable, orderbook, registry)

from .. import _wrap
from .._generic import Generic

class RSIbis(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return { 'rsi' : observable.RSI(orderbook.OfTrader(), 
                                        self.timeframe, 
                                        self.alpha) }
    
    def getImpl(self):
        return Generic(
                  self.orderFactory(
                            parts.side.Signal(ops.constant(50) - _.rsi, 
                                              50-self.threshold)), 
                  event.Every(self.creationIntervalDistr))
        
_wrap.strategy(RSIbis, ['Periodic', 'RSI bis'], 
               """
               """, 
               [
                  ("orderFactory",  "order.factory.side.Market()",  'IFunction[Side] -> IOrderGenerator'),             
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('timeframe',             '1.',                            'non_negative'), 
                  ('threshold',             '30.',                           'non_negative'), 
                  ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
               ], globals())
