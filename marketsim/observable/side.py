from marketsim import (Side, registry, meta, orderbook,
                       mathutils, ops, defs, _, types, signal)

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

from _orderbook import AskPrice, BidPrice

class FundamentalValue(ops.Observable[Side]):
    
    def getImpl(self):
        return  (BidPrice(_.orderBook) > _.fv)[
                    ops.constant(Side.Sell), 
                    (AskPrice(_.orderBook) < _.fv)[
                        ops.constant(Side.Buy), 
                        ops._None[Side]()
                    ]                
                ]
        
    def getDefinitions(self):
        return {
            'fv'        : self.fundamentalValue, 
            'orderBook' : self.orderBook 
        }
    
_wrap.function(FundamentalValue, ['Fundamental value side'], 
                 """ If *fundamentalValue* > bid price then sells, 
                     if *fundamentalValue* < ask price then buys
                 """, 
                 [
                    ('orderBook',       'orderbook.OfTrader()','types.IOrderBook'),
                    ('fundamentalValue','ops.constant(200.)',  'types.IFunction[float]')
                 ], globals())    

