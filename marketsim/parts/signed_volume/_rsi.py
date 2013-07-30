from marketsim import (Side, orderbook, observable, registry, trader as trader_, ops, _, types)
from marketsim.types import *

import _wrap
from _desired_position import DesiredPosition
    
class RSI_linear(ops.Observable[float]): # ops.Observable[SignedVolume]
    
    def getDefinitions(self):
        return { 'rsi' : observable.RSI(orderbook.OfTrader(self.trader), 
                                        self.timeframe, 
                                        self.alpha) }
    
    def getImpl(self):
        return DesiredPosition(observable.OnEveryDt(1, 
                                   (ops.constant(50) - _.rsi) * self.k), 
                               self.trader)
    
_wrap.function(RSI_linear, ['RSI_linear'], 
             """ """,
               [
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('k',                     'ops.constant(-0.04)',           'IFunction[float]'), 
                  ('timeframe',             '1.',                            'non_negative'), 
                  ('trader',                'trader_.SingleProxy()',         'types.ISingleAssetTrader'),
               ], globals())
