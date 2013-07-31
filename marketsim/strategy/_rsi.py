from marketsim.types import *
from marketsim import (parts, meta, types, order, _, defs, ops,
                       mathutils, observable, scheduler, orderbook, registry)

from _generic import Generic

import _wrap

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
    
