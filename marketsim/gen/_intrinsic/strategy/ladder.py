from marketsim.gen._out._intrinsic_base.strategy.ladder import OneSide_Base
from basic import Strategy
from marketsim import event, _, request
from marketsim.gen._out._side import Side
from marketsim.gen._out._constant import constant
from marketsim.gen._out.orderbook._queue import Queue
from marketsim.gen._out.orderbook._oftrader import OfTrader

from collections import deque

class OneSide_Impl(Strategy, OneSide_Base):

    def __init__(self):
        Strategy.__init__(self)

        self._book = OfTrader()
        self._orderQueue = Queue(self._book, side = self.side)
        self._source = self._orderQueue.BestPrice
        self._sign = 1 if Side.Sell == self.side() else -1
        self._orders = None
        self._size = self.initialSize
        event.subscribe(self._source, _(self)._wakeUp, self)

    def extend(self):
        if self._orders:
            self._orders.appendleft(self._makeOrder(self._first.ticks - 1))
            self._send(self._first)
        self._size += 1
        print self._size

    def _makeOrder(self, t):
        p = self._orderQueue.ticksToPrice(t)
        order = self.orderFactory(self.side, constant(p))()
        order.ticks = t
        order.source = self
        return order

    @property
    def _first(self):
        return self._orders[0]

    @property
    def _last(self):
        return self._orders[len(self._orders) - 1]

    def _wakeUp(self, _):
        price = self._source()

        if price is not None:
            ticks, _ = self._orderQueue.ticks(price)
            if self._orders is None:
                self._orders = deque()
                for i in range(0, self._size):
                    self._orders.append(self._makeOrder(ticks + i))
                    self._send(self._last)
            else:
                orderTicks = self._orders[0].ticks
                if orderTicks == ticks or self._orderQueue.best.owner == self._first.owner:
                    pass
                else:
                    if ticks > orderTicks:
                        while self._orders and self._first.ticks < ticks:
                            order = self._first
                            if not order.cancelled:
                                self._send(request.Cancel(order))
                            self._orders.popleft()
                        while len(self._orders) < self._size:
                            t = self._last.ticks + 1 if self._orders else ticks
                            self._orders.append(self._makeOrder(t))
                            self._send(self._last)
                    elif ticks < orderTicks:
                        while self._orders and self._last.ticks > ticks + self._size:
                            self._send(request.Cancel(self._last))
                            self._orders.pop()
                        num_created = self._size - len(self._orders)
                        while len(self._orders) < self._size:
                            t = self._first.ticks - 1 if self._orders else ticks + (self._size - 1)
                            self._orders.appendleft(self._makeOrder(t))
                        for i in range(num_created):
                            self._send(self._orders[i])

from marketsim.gen._out._intrinsic_base.strategy.ladder import MarketMaker_Base

class MarketMaker_Impl(Strategy, MarketMaker_Base):

    def __init__(self):
        Strategy.__init__(self)
        from marketsim._pub import strategy, side

        self._seller = strategy.price.Ladder(self.orderFactory, self.initialSize, side.Sell())
        self._buyer = strategy.price.Ladder(self.orderFactory, self.initialSize, side.Buy())

        event.subscribe(self._seller.on_order_created, _(self)._send, self)
        event.subscribe(self._buyer.on_order_created, _(self)._send, self)

    def bind(self, context):
        event.subscribe(context.trader.on_order_matched, _(self)._onOrderMatched, self, context)

    def _onOrderMatched(self, trader, order, price, volume):
        if order.empty and hasattr(order, 'source'):
            if order.source == self._seller:
                if self._buyer._size < self.maximalSize:
                    self._buyer.extend()
            if order.source == self._buyer:
                if self._seller._size < self.maximalSize:
                    self._seller.extend()

    _internals = ['_seller', '_buyer']

    def dispose(self):
        for s in [self._seller, self._buyer]:
            s.dispose()
