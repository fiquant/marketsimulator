from marketsim import (Side, observable, registry, meta, ops, _, orderbook, types)
from marketsim.types import *

import _wrap
from _signal import Signal
    
class TwoAverages(ops.Observable[Side]):
    
    def getDefinitions(self):
        return { 
            'price' : observable.MidPrice(orderbook.OfTrader()),
        }
    
    def getImpl(self):
        return Signal((observable.EWMA(_.price, self.ewma_alpha1) 
                       - observable.EWMA(_.price, self.ewma_alpha2)),
                      self.threshold)
    
_wrap.function(TwoAverages, ['TwoAverages side'], 
             """ Two averages is a signal that compares two averages of price of the same asset but
                 with different parameters ('slow' and 'fast' averages) and when 
                 the first is greater than the second one it buys, 
                 when the first is lower than the second one it sells
                 
                 It has following parameters:

                 |ewma_alpha1| 
                     parameter |alpha| for the first exponentially weighted moving average
                     (default: 0.15.)
                      
                 |ewma_alpha2| 
                     parameter |alpha| for the second exponentially weighted moving average
                     (default: 0.015.)
                      
                 |threshold| 
                     threshold when the trader starts to act (default: 0.)
             """,
             [
              ('ewma_alpha1',           '0.15',                          'non_negative'),
              ('ewma_alpha2',           '0.015',                         'non_negative'),
              ('threshold',             '0.',                            'non_negative'), 
             ], 
               globals())
