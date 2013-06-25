from marketsim import (scheduler, observable, types, meta, 
                       Side, registry, orderbook, bind, order, mathutils)

from _periodic import Periodic
from _signal import SignalBase
from _wrap import wrapper2
from _fv import FundamentalValueBase, FundamentalValueSide

from marketsim.types import *


class _MeanReversion_Impl(FundamentalValueBase):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        myBook = orderbook.OfTrader()
        self._fundamentalValue = observable.Fold(observable.Price(myBook), 
                                                 self.average)
        FundamentalValueBase.__init__(self)

    _internals = ['_fundamentalValue']

exec wrapper2("MeanReversion",
             """ Mean reversion strategy believes that asset price should return to its average value.
                 It estimates this average using some functional and 
                 if the current asset price is lower than the average
                 it buys the asset and if the price is higher it sells the asset. 
             
                 It has following parameters: 
                 
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                 
                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                 
                 |average| 
                     functional used to calculate the average 
                     (default: exponentially weighted moving average with |alpha| = 0.15)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('orderFactory',          'order.MarketFactory',              'Side -> Volume -> IOrder'),
              ('average',               'mathutils.ewma(alpha = 0.15)',     'IUpdatableValue'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',    '() -> Volume'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')])


@registry.expose(["Periodic", "MeanReversion"], args = ())
def MeanReversionEx   (average               = mathutils.ewma(alpha = 0.15),
                       orderFactory          = order.MarketFactory, 
                       volumeDistr           = mathutils.rnd.expovariate(1.), 
                       creationIntervalDistr = mathutils.rnd.expovariate(1.)):

    orderBook = orderbook.OfTrader()
    avg = observable.Fold(observable.Price(orderBook), average)
    
    r = Periodic(orderFactory= orderFactory, 
                 volumeFunc  = volumeDistr, 
                 eventGen    = scheduler.Timer(creationIntervalDistr), 
                 sideFunc    = FundamentalValueSide(orderBook, avg))
    
    return r

