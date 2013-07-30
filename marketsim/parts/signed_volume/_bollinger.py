from marketsim import (Side, orderbook, observable, registry, trader as trader_, ops, _, types)
from marketsim.types import *

import _wrap
from _desired_position import DesiredPosition
    
class Bollinger_linear(ops.Observable[float]): # ops.Observable[SignedVolume]
    
    def getDefinitions(self):
        return  { 'price' : observable.MidPrice(orderbook.OfTrader(self.trader)),
                  'mean'  : observable.EWMA(_.price, self.alpha), 
                  'stddev': observable.StdDevEW(_.price, self.alpha) }
            
    def getImpl(self):
        return DesiredPosition(
                    observable.IndicatorBase(
                        _.price, ops.Sub(_.price, _.mean) / _.stddev * self.k),
                    self.trader)
    
_wrap.function(Bollinger_linear, ['Bollinger_linear'], 
             """ """,
               [
                  ('alpha',                 '0.15',                          'non_negative'), 
                  ('k',                     'ops.constant(+0.5)',            'IFunction[float]'), 
                  ('trader',                'trader_.SingleProxy()',         'types.ISingleAssetTrader'),
               ], globals())
