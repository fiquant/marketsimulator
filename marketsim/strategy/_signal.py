import marketsim
from marketsim.types import *
from marketsim import (parts, Event, order, mathutils, types, meta, defs, _, ops,
                       registry, signal, bind, signal, ops, observable)
from _generic import Generic
import _wrap

class Signal(types.ISingleAssetStrategy):
    
    def getImpl(self):
        return Generic(order.factory.Market(_.side, self.volumeDistr), _.signal)
        
    def getDefinitions(self):
        return {
            "signal" : self.signal, 
            "side"   : parts.side.Signal(self.signal, self.threshold) 
        }

_wrap.strategy(Signal, ['Periodic', 'Signal'], 
             """ Signal strategy listens to some discrete signal
                 and when the signal becomes more than some threshold the strategy starts to buy. 
                 When the signal gets lower than -threshold the strategy starts to sell. 
                 
                 It has following parameters:

                 |signal| 
                      signal to be listened to (default: RandomWalk)
                      
                 |threshold| 
                     threshold when the trader starts to act (default: 0.7)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('signal',        'marketsim.signal.RandomWalk()','IObservable[float]'),  
              ('threshold',     '0.7',                          'non_negative'),
              ('volumeDistr',   'mathutils.rnd.expovariate(1.)','() -> Volume')], globals())
