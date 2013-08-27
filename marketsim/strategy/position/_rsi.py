from marketsim.types import *
from marketsim import (parts, meta, types, order, _, defs, ops,
                       mathutils, observable, scheduler, orderbook, registry)

from .. import _wrap
from .._generic import Generic

class RSI_linear(types.ISingleAssetStrategy):

    def getImpl(self):
        return Generic(
                    self.orderFactory(
                        parts.signed_volume.RSI_linear(self.alpha, 
                                                       self.k, 
                                                       self.timeframe)))

_wrap.strategy(RSI_linear, ['Desired position', 'RSI linear'], 
               """
               """, 
               [
                  ('orderFactory', 'order.factory.signedvolume.Market()', 'IFunction[SignedVolume] -> IOrderGenerator'),
                  ('alpha',                 '1./14',                         'non_negative'), 
                  ('k',                     'ops.constant(-0.04)',           'IFunction[float]'), 
                  ('timeframe',             '1.',                            'non_negative'), 
               ], globals())
    
