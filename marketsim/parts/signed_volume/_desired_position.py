from marketsim import (Side, observable, registry, meta, ops, _, trader as trader_, signal, types)
from marketsim.types import *

import _wrap
    
class DesiredPosition(ops.Observable[float]): # ops.Observable[SignedVolume]
    
    def getImpl(self):
        pending = observable.PendingVolume(self.trader)
        actual = observable.VolumeTraded(self.trader)
        
        return self.desiredPosition - actual - pending
    
_wrap.function(DesiredPosition, ['DesiredPosition'], 
             """ """,
             [
              ('desiredPosition',       'signal.RandomWalk()',          'types.IFunction[float]'),
              ('trader',                'trader_.SingleProxy()',        'types.ISingleAssetTrader'),
             ],
               globals())
