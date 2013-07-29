from marketsim import (Side, registry, meta, ops, _, types, signal)

from .. import _wrap
    
class Signal(ops.Observable[Side]):
    
    def getImpl(self):
        return ops.Less[float](_.threshold, _.source)[ 
                    ops.constant(Side.Buy), 
                    ops.less(_.source, ops.negate(_.threshold))[ 
                        ops.constant(Side.Sell), 
                        ops._None[Side]()
                    ]
                ]
        
    def getDefinitions(self):
        return { 'source'    : self.source, 
                 'threshold' : ops.constant(self.threshold) }
    
_wrap.function(Signal, ['Signal side'], 
                 """ If *signal* > *threshold* buys, if *signal* < -*threshold* sells
                 """, 
                 [
                    ('source',      'signal.RandomWalk()', 'types.IFunction[float]'),
                    ('threshold',   '0.',                  'types.non_negative')
                 ], globals())    
