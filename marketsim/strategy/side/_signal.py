import marketsim
from marketsim.types import *
from marketsim import (parts, Event, order, mathutils, types, meta, defs, _, ops,
                       registry, signal, bind, signal, ops, observable)
from .._generic import Generic
from .. import _wrap

class Signal(types.ISingleAssetStrategy):
    
    def getImpl(self):
        return Generic(
                    self.orderFactory(
                            parts.side.Signal(
                                        _.signal, 
                                        self.threshold)), 
                    _.signal)
        
    def getDefinitions(self):
        return {
            "signal" : self.signal
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
             [
              ("orderFactory",  "order.factory.side.Market()",  'Side -> IOrderGenerator'),             
              ('signal',        'marketsim.signal.RandomWalk()','IObservable[float]'),  
              ('threshold',     '0.7',                          'non_negative'),
             ], globals())
