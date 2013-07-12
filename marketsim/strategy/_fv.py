from marketsim import (scheduler, observable, types, meta, defs, _, ops,
                       Side, registry, orderbook, bind, order, mathutils)

from _periodic import Periodic
from _signal import SignalBase
from _wrap import wrapper2

from marketsim.types import *

class FundamentalValueBase(SignalBase):

    @property
    def threshold(self):
        return 0.
    
    def _signalFunc(self):
        book = self._trader.book
        fv = self._fundamentalValue()

        # Quick fix: sometimes fv returns a None value
        if fv is None:
            return None
        
        # if current price is defined, compare it with the fundamental value and define the side
        return +1 if not book.asks.empty\
                  and book.asks.best.price < fv else\
               -1 if not book.bids.empty\
                  and book.bids.best.price > fv else\
               None

class _FundamentalValue_Impl(FundamentalValueBase):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        FundamentalValueBase.__init__(self)
        
    @property
    def _fundamentalValue(self):
        return self.fundamentalValue  

exec  wrapper2("FundamentalValue", 
             """ Fundamental value strategy believes that an asset should have some specific price 
                 (*fundamental value*) and if the current asset price is lower than the fundamental value 
                 it starts to buy the asset and if the price is higher it starts to sell the asset. 
             
                 It has following parameters: 
                 
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                 
                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                 
                 |fundamentalValue| 
                     defines fundamental value (default: constant 100)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
              [('orderFactory',         'order.MarketFactory',          'Side -> Volume -> IOrder'),
               ('fundamentalValue',     'ops.constant(100)',      '() -> Price'),
               ('volumeDistr',          'mathutils.rnd.expovariate(1.)','() -> Volume'),
               ('creationIntervalDistr','mathutils.rnd.expovariate(1.)','() -> TimeInterval')])

def FundamentalValueSide(orderBook, fundamentalValue):
    
    return defs((observable.BidPrice(_.orderBook) > _.fv)[
                    ops.constant(Side.Sell), 
                    (observable.AskPrice(_.orderBook) < _.fv)[
                        ops.constant(Side.Buy), 
                        ops._None[Side]()
                    ]                
                ], 
            {
             'fv'        : fundamentalValue, 
             'orderBook' : orderBook 
            })

@registry.expose(["Periodic", "FundamentalValue"], args = ())
def FundamentalValueEx(fundamentalValue      = ops.constant(100.),
                       orderFactory          = order.MarketFactory, 
                       volumeDistr           = mathutils.rnd.expovariate(1.), 
                       creationIntervalDistr = mathutils.rnd.expovariate(1.)):
    
    orderBook = orderbook.OfTrader()
    r = Periodic(orderFactory= orderFactory, 
                 volumeFunc  = volumeDistr, 
                 eventGen    = scheduler.Timer(creationIntervalDistr), 
                 sideFunc    = FundamentalValueSide(orderBook, fundamentalValue))
    
    return r

