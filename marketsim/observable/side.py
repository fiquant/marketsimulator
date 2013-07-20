from marketsim import Side, registry, meta, mathutils, ops

import _wrap
    
class Random(ops.Function[Side]):
    
    def getImpl(self):
        return (mathutils.rnd.uniform(0.,1.) < 0.5)[ 
                    ops.constant(Side.Buy), 
                    ops.constant(Side.Sell)
               ]

_wrap.function(Random, ['Random side'], 
                 """ Chooses Sell or Buy side with equal probability
                 """, 
                 [], globals())    
