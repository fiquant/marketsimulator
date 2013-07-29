from marketsim import (scheduler, observable, types, meta, defs, _, ops,
                       Side, registry, orderbook, bind, order, mathutils)

from _periodic import Periodic, Generic
from _signal import SignalBase
from _wrap import wrapper2
from _fv import FundamentalValueBase


import side

from marketsim.types import *


class _Dependency_Impl(FundamentalValueBase):
    
    def __init__(self):
        self._priceToDependOn = observable.MidPrice(self.bookToDependOn) 
        self._orderFactoryT = self.orderFactory
        FundamentalValueBase.__init__(self)

    def _fundamentalValue(self):
        return self._priceToDependOn() * self.factor \
            if self._priceToDependOn() is not None else None
    
    def _volume(self, side):
        oppositeQueue = self._trader.book.queue(side.opposite)
        # should we send limit and cancel orders here?
        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(self._fundamentalValue())
        # we want to trade orders only with a good price
        return min(oppositeVolume, self.volumeDistr())
    
    @property
    def _eventGen(self):
        return self._priceToDependOn        

exec wrapper2("Dependency", 
             """ Dependent price strategy believes that the fair price of an asset *A* 
                 is completely correlated with price of another asset *B* and the following relation 
                 should be held: *PriceA* = *kPriceB*, where *k* is some factor. 
                 It may be considered as a variety of a fundamental value strategy 
                 with the exception that it is invoked every the time price of another
                 asset *B* changes. 
             
                 It has following parameters: 
                 
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                 
                 |bookToDependOn| 
                     reference to order book for another asset used to evaluate fair price of our asset
                 
                 |factor| 
                     multiplier to obtain fair asset price from the reference asset price
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('bookToDependOn','None',                             'IOrderBook'),
              ('orderFactory',  'order.MarketFactory',              'Side -> Volume -> IOrder'),
              ('factor',        '1.',                               'positive'),
              ('volumeDistr',   'mathutils.rnd.expovariate(.1)',    '() -> Volume')], register=False)

import _wrap

class DependencyEx(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        return { 'dependee' : observable.MidPrice(self.bookToDependOn) * self.factor }

    def getImpl(self):
        orderBook = orderbook.OfTrader()
        return Periodic(orderFactory= self.orderFactory, 
                        volumeFunc  = self.volumeDistr, 
                        eventGen    = _.dependee, 
                        sideFunc    = side.FundamentalValue(
                                            orderBook, _.dependee))

_wrap.strategy(DependencyEx, ['Periodic', 'Dependency'],
         """ Dependent price strategy believes that the fair price of an asset *A* 
             is completely correlated with price of another asset *B* and the following relation 
             should be held: *PriceA* = *kPriceB*, where *k* is some factor. 
             It may be considered as a variety of a fundamental value strategy 
             with the exception that it is invoked every the time price of another
             asset *B* changes. 
         
             It has following parameters: 
             
             |orderFactory| 
                 order factory function (default: order.Market.T)
             
             |bookToDependOn| 
                 reference to order book for another asset used to evaluate fair price of our asset
             
             |factor| 
                 multiplier to obtain fair asset price from the reference asset price
                 
             |volumeDistr| 
                 defines volumes of orders to create 
                 (default: exponential distribution with |lambda| = 1)
         """,
         [
          ('bookToDependOn','orderbook.OfTrader()',             'IOrderBook'),
          ('orderFactory',  'order.MarketFactory',              'Side -> Volume -> IOrder'),
          ('factor',        '1.',                               'float'),
          ('volumeDistr',   'mathutils.rnd.expovariate(.1)',    '() -> Volume')
          ], globals())
                
class Dependency2Ex(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        orderBook = orderbook.OfTrader()
        return { 
            'dependee' : observable.MidPrice(self.bookToDependOn) * self.factor,
            'side' :     side.FundamentalValue(orderBook, _.dependee)
        }

    def getImpl(self):
        return Generic(self.orderFactory(_.side),  _.dependee)

_wrap.strategy(Dependency2Ex, ['Periodic', 'Dependency2'],
         """ Dependent price strategy believes that the fair price of an asset *A* 
             is completely correlated with price of another asset *B* and the following relation 
             should be held: *PriceA* = *kPriceB*, where *k* is some factor. 
             It may be considered as a variety of a fundamental value strategy 
             with the exception that it is invoked every the time price of another
             asset *B* changes. 
         
             It has following parameters: 
             
             |orderFactory| 
                 order factory function (default: order.Market.T)
             
             |bookToDependOn| 
                 reference to order book for another asset used to evaluate fair price of our asset
             
             |factor| 
                 multiplier to obtain fair asset price from the reference asset price
         """,
         [
          ('bookToDependOn','orderbook.OfTrader()',             'IOrderBook'),
          ('orderFactory',  'order.factory.Side_Market()',      'Side -> IOrderGenerator'),
          ('factor',        '1.',                               'float'),
          ], globals())
                
