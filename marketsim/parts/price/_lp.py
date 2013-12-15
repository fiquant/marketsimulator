from marketsim import mathutils, ops, defs, _, observable, orderbook, types, Side, registry

from marketsim.gen._out.observable.orderbook._Queue import Queue
from marketsim.gen._out.observable.orderbook._SafeSidePrice import SafeSidePrice

import _wrap

class LiquidityProvider(ops.Observable[float]): # ops.Observable[Price]
    
    def getImpl(self):
        return SafeSidePrice(Queue(self.orderBook, ops.constant(self.side)),
                             ops.constant(self.initialValue)) * self.priceDistr
                                        
_wrap.function(LiquidityProvider, ['parts', 'price', 'LiquidityProvider side'], 
             """ Liquidity provider for one side has followng parameters:

                 |side|
                     side of orders to create (default: Side.Sell)
                     
                 |initialValue| 
                     initial price which is taken if orderBook is empty (default: 100)
                     
                 |priceDistr|
                     defines multipliers for current asset price when price of
                     order to create is calculated (default: log normal distribution with 
                     |mu| = 0 and |sigma| = 0.1)
                     
                 It checks the last best price of orders in the corresponding queue, takes *initialValue*
                 if it is empty, multiplies it by a value taken from *priceDistr* to obtain price
                 of the order to create
             """,
            [
              ('side',                  'Side.Sell',                            'types.Side'),
              ('initialValue',          '100',                                  'types.Price'),
              ('priceDistr',            'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
              ('orderBook',             'orderbook.OfTrader()',                 'types.IOrderBook'),
            ], globals())
