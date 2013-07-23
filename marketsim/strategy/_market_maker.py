from marketsim import orderbook, event, _, Side, order, types, mathutils, scheduler, ops, Event, observable
from marketsim.types import *
from _basic import Strategy
from _wrap import wrapper2

from marketsim.trader import TraderHistory, SingleProxy
from marketsim.order import Cancel

class _MarketMaker_Impl(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = scheduler.Timer(ops.constant(0.9))
        event.subscribe(self._eventGen, _(self)._wakeUp, self)

        self.book = orderbook.OfTrader()
        self.bids = observable.BidPrice(self.book)
        self.asks = observable.AskPrice(self.book)
        self.log = TraderHistory(SingleProxy())
        self.prev_mid = None

    _internals = ['book', 'bids', 'asks', 'log']

    def _wakeUp(self, dummy):
        for position in self.log.pending:
                self._trader.send(Cancel(position))

        mid = self.mid()

        if mid is not None:
            bid = mid+1-(self.log.amount/self.volume)
            ask = mid-1-(self.log.amount/self.volume)
            buyOrder = order.LimitFactory(Side.Buy)(bid, self.volume)
            sellOrder = order.LimitFactory(Side.Sell)(ask, self.volume)
            self._trader.send(self.log(buyOrder))
            self._trader.send(self.log(sellOrder))

    def mid(self):
        curBid, curAsk = self.bids(), self.asks()
        if curBid and curAsk:
            mid = (curAsk + curBid)/2
        else:
            mid = None
        return mid

exec  wrapper2("MarketMaker",
             """

             |volume|
                Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.
             """,
              [ ('volume', '20', 'Volume') ], register=False)