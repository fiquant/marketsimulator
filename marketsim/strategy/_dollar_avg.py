from marketsim import event, _, Side, order, types, mathutils, scheduler, ops, orderbook
from marketsim.types import *
from _basic import Strategy
from _wrap import wrapper2
from math import floor
from marketsim.trader import TraderHistory, SingleProxy

class _DollarAverage_Impl(Strategy):

    _internals = ['book']

    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        event.subscribe(self._eventGen, _(self)._wakeUp, self)
        self.book = orderbook.OfTrader()
        self.log = TraderHistory(SingleProxy())

        self.budget = 100
        self.profit_threshold = 0.01
        self.limit = 5

    def _wakeUp(self, dummy):

        if not self.log.pending:

            if self.profitable_to_sell:
                side = Side.Sell
                volume = self._trader.log.amount
            elif self.profitable_to_buy:
                side = Side.Buy
                ask = self.book.queue(Side.Sell).bestPrice()
                volume = self.budget / ask
                if volume + self.log.amount > self.limit:
                    volume = 0
            else:
                volume = 0

            if volume > 0:
                order = self.orderFactory(side)(volume)
                self._trader.send(order)

    @property
    def profitable_to_sell(self):

        bid = self.book.queue(Side.Buy).bestPrice()
        avg_price = self.log.averagePrice
        # print bid, avg_price
        profitable = avg_price and bid and bid > avg_price
        return profitable

    @property
    def profitable_to_buy(self):
        ask = self.book.queue(Side.Sell).bestPrice()
        avg_price = self.log.averagePrice
        return ask and (not avg_price or ask < avg_price)



exec  wrapper2("DollarAverage",
             """ Generic Market Maker strategy
             """,
              [('orderFactory',         'order.MarketFactory',     'Side -> Volume -> IOrder'),
               ('creationIntervalDistr', 'ops.constant(1)',        '() -> TimeInterval')],
               register=False)
