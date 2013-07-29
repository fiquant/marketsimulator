import random
from _one_side import OneSide
from _periodic import Periodic, Generic
from _wrap import wrapper2
from marketsim import (order, orderbook, scheduler, mathutils, ops,
                       event, types, registry, meta, defs, _, observable)
from marketsim.types import *

class _LiquidityProviderSide_Impl(OneSide):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        self._queue = orderbook.QueueProxy(orderbook.OfTrader(), self.side)
        self._lastPrice = observable.QueueLastPrice(self._queue)
        OneSide.__init__(self)
        
    _internals = ["_lastPrice"]
        
    @property
    def _orderFactory(self):
        return self.orderFactoryT(self.side)
    
    def _orderFunc(self):
        queue = self._trader.book.queue(self.side)
        currentPrice = queue.best.price if not queue.empty else\
                       self._lastPrice() if self._lastPrice() is not None else\
                       self.defaultValue
        price = currentPrice * self.priceDistr()
        volume = int(self.volumeDistr())
        return (price, volume)
    
    def dispose(self):
        OneSide.dispose(self)
        self._eventGen.cancel()

exec wrapper2("LiquidityProviderSide",
             """ Liquidity provider for one side has followng parameters:

                 |side|
                     side of orders to create (default: Side.Sell)
                     
                 |orderFactory| 
                     order factory function (default: order.Limit.T)
                     
                 |initialValue| 
                     initial price which is taken if orderBook is empty (default: 100)
                     
                 |creationIntervalDistr|
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                     
                 |priceDistr|
                     defines multipliers for current asset price when price of
                     order to create is calculated (default: log normal distribution with 
                     |mu| = 0 and |sigma| = 0.1)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 It wakes up in moments of time given by *creationIntervalDistr*, checks
                 the last best price of orders in the corresponding queue, takes *initialValue*
                 if it is empty, multiplies it by a value taken from *priceDistr* to obtain price
                 of the order to create, calculates order volume using *volumeDistr*, creates
                 an order via *orderFactoryT(side)* and tells the trader to send it.
             """,
             [('side',                  'Side.Sell',                            'Side'),
              ('orderFactoryT',         'order.LimitFactory',                   'Side -> (Price, Volume) -> IOrder'),
              ('defaultValue',          '100',                                  'Price'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',        '() -> TimeInterval'),
              ('priceDistr',            'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',        '() -> Volume')])


from marketsim import ops
               
def SafeSidePrice(orderBook, side, defaultValue):
    
    return defs(
        (ops._None[float]() == _.sidePrice)[
            (ops._None[float]() == _.lastPrice)[
                ops.constant(defaultValue),
                _.lastPrice
            ], 
            _.sidePrice        
        ],
        { 
          'lastPrice': observable.QueueLastPrice(_.queue), 
          'sidePrice': observable.QueuePrice(_.queue), 
          'queue'    : orderbook.QueueProxy(orderBook, side)
        })

import _wrap

class LiquidityProviderSideEx(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        return {
            'priceFunc' : SafeSidePrice(orderbook.OfTrader(), 
                                        self.side, self.defaultValue) \
                                    * self.priceDistr, 
        }
    
    def getImpl(self):
        orderBook = orderbook.OfTrader()
        return Generic(order.factory.Limit(
                            side = ops.constant(self.side),
                            price = _.priceFunc, 
                            volume = self.volumeDistr), 
                       scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(LiquidityProviderSideEx, ['Periodic', 'LiquidityProviderSide'],
             """ Liquidity provider for one side has followng parameters:

                 |side|
                     side of orders to create (default: Side.Sell)
                     
                 |initialValue| 
                     initial price which is taken if orderBook is empty (default: 100)
                     
                 |creationIntervalDistr|
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                     
                 |priceDistr|
                     defines multipliers for current asset price when price of
                     order to create is calculated (default: log normal distribution with 
                     |mu| = 0 and |sigma| = 0.1)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 It wakes up in moments of time given by *creationIntervalDistr*, checks
                 the last best price of orders in the corresponding queue, takes *initialValue*
                 if it is empty, multiplies it by a value taken from *priceDistr* to obtain price
                 of the order to create, calculates order volume using *volumeDistr*, creates
                 an order via *orderFactoryT(side)* and tells the trader to send it.
             """,
             [('side',                  'Side.Sell',                            'Side'),
              ('defaultValue',          '100',                                  'Price'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',        '() -> TimeInterval'),
              ('priceDistr',            'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',        '() -> Volume')],
               globals())
