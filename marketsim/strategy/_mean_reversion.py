from marketsim import (scheduler, observable, types, meta, _,
                       Side, registry, orderbook, bind, order, mathutils)

from _periodic import Periodic, Generic
from _signal import SignalBase
from _wrap import wrapper2
from _fv import FundamentalValueBase

from marketsim.types import *


class _MeanReversion_Impl(FundamentalValueBase):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        myBook = orderbook.OfTrader()
        self._fundamentalValue = observable.EWMA(observable.MidPrice(myBook), 
                                                 self.ewma_alpha)
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
                 
                 |ewma_alpha| 
                     |alpha| for exponentially weighted moving average 
                     (default: 0.15)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('orderFactory',          'order.MarketFactory',              'Side -> Volume -> IOrder'),
              ('ewma_alpha',            '0.15',                             'non_negative'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',    '() -> Volume'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')])

import _wrap

class MeanReversionEx(types.ISingleAssetStrategy):

    def getImpl(self):
        orderBook = orderbook.OfTrader()
        avg = observable.EWMA(observable.MidPrice(orderBook), self.ewma_alpha)

        return Periodic(orderFactory= self.orderFactory, 
                        volumeFunc  = self.volumeDistr, 
                        eventGen    = scheduler.Timer(self.creationIntervalDistr), 
                        sideFunc    = observable.side.FundamentalValue(orderBook, avg))

_wrap.strategy(MeanReversionEx, ['Periodic', 'Mean reversion'], 
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
                 
                 |ewma_alpha| 
                     |alpha| for exponentially weighted moving average 
                     (default: 0.15)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('orderFactory',          'order.MarketFactory',              'Side -> Volume -> IOrder'),
              ('ewma_alpha',            '0.15',                             'non_negative'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)',    '() -> Volume'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')], 
               globals())

class MeanReversion2Ex(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        orderBook = orderbook.OfTrader()
        avg = observable.EWMA(observable.MidPrice(orderBook), self.ewma_alpha)
        return { 'side' : observable.side.FundamentalValue(orderBook, avg) }

    def getImpl(self):

        return Generic(self.orderFactory(_.side), scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(MeanReversion2Ex, ['Periodic', 'Mean reversion2'], 
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
                 
                 |ewma_alpha| 
                     |alpha| for exponentially weighted moving average 
                     (default: 0.15)
             """,
             [('orderFactory',          'order.factory.Side_Market()',      'ISide_IOrderGenerator'),
              ('ewma_alpha',            '0.15',                             'non_negative'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')], 
               globals())

