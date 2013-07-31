from marketsim import (trader, orderbook, event, _, Side, order, types, mathutils, 
                       scheduler, ops, Event, observable, registry, combine)

from marketsim.types import *
from .._basic import Strategy
from _wrap import wrapper2

from marketsim.trader import TraderHistory, SingleProxy
from marketsim.order import Cancel


class _MarketMaker_Impl(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = scheduler.Timer(ops.constant(0.9))
        event.subscribe(self._eventGen, _(self)._wakeUp, self)

        self.book = orderbook.OfTrader()
        self.midprice = observable.MidPrice(self.book)
        self.log = TraderHistory(SingleProxy())
        self.prev_mid = None

    _internals = ['book', 'log', 'midprice']

    def _wakeUp(self, dummy):
        for position in self.log.pending:
                self._trader.send(Cancel(position))

        mid = self.midprice()

        if mid is not None:
            bid = mid+1-(self.log.amount/self.volume)
            ask = mid-1-(self.log.amount/self.volume)
            buyOrder = order.LimitFactory(Side.Buy)(bid, self.volume)
            sellOrder = order.LimitFactory(Side.Sell)(ask, self.volume)
            self._trader.send(buyOrder)
            self._trader.send(sellOrder)

exec  wrapper2("MarketMaker",
             """

             |volume|
                Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.
             """,
              [ ('volume', '20.', 'Volume') ], register=False)