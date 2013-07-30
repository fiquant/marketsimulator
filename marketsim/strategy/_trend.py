from marketsim.types import *
from marketsim import (parts, orderbook, observable, scheduler, order, mathutils, types, meta, 
                       registry, signal, bind, ops, _)
import _wrap
from _periodic import Generic

class TrendFollower(types.ISingleAssetStrategy):
    
    def getImpl(self):
        return Generic( order.factory.Market(
                            parts.side.TrendFollower(self.ewma_alpha, self.threshold), 
                            self.volumeDistr), 
                        scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(TrendFollower, ['Periodic', 'TrendFollower'], 
                 """ Trend follower can be considered as a sort of a signal strategy 
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
                         
                     |creationIntervalDistr|
                         defines intervals of time between order creation
                         (default: exponential distribution with |lambda| = 1)
                         
                     |volumeDistr| 
                         defines volumes of orders to create 
                         (default: exponential distribution with |lambda| = 1)
                 """,
                 [
                  ('ewma_alpha',             '0.15',                          'non_negative'),
                  ('threshold',              '0.',                            'non_negative'), 
                  ('orderFactory',           'order.MarketFactory',           'Side -> Volume -> IOrder'),
                  ('creationIntervalDistr',  'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
                  ('volumeDistr',            'mathutils.rnd.expovariate(1.)', '() -> Volume')
                 ], globals())
