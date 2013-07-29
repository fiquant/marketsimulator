from marketsim import (Side, observable, registry, meta, ops, _, orderbook, types)
from marketsim.types import *

import _wrap
from _signal import Signal
    
class TrendFollower(ops.Observable[Side]):
    
    def getDefinitions(self):
        orderBook = orderbook.OfTrader()
        
        return { 
                 'trend' : ops.Derivative(
                                observable.EWMA(
                                    observable.MidPrice(orderBook), 
                                    self.ewma_alpha))
            }
    
    def getImpl(self):
        return Signal(_.trend, self.threshold)
    
_wrap.function(TrendFollower, ['TrendFollower side'], 
                 """ Trend follower can be considered as a sort of a signal 
                     where the *signal* is a trend of the asset. 
                     Under trend we understand the first derivative of some moving average of asset prices. 
                     If the derivative is positive, the trader buys; if negative - it sells.
                     Since moving average is a continuously changing signal, we check its
                     derivative at random moments of time given by *creationIntervalDistr*. 
                     
                     It has following parameters:
                    
                     |ewma_alpha| 
                         parameter |alpha| for exponentially weighted moving average
                         (default: 0.15.)
                         
                     |threshold| 
                         threshold when the trader starts to act (default: 0.)
                 """,
                 [
                  ('ewma_alpha',             '0.15',                          'non_negative'),
                  ('threshold',              '0.',                            'non_negative'), 
                 ], globals())
