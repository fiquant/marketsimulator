from marketsim import (Side, registry, meta, observable, orderbook, ops, _, types)

import _wrap

class FundamentalValue(ops.Observable[Side]):
    
    def getImpl(self):
        return  (observable.BidPrice(_.orderBook) > _.fv)[
                    ops.constant(Side.Sell), 
                    (observable.AskPrice(_.orderBook) < _.fv)[
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

