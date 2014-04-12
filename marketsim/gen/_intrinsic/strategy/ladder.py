from marketsim.gen._out._intrinsic_base.strategy.ladder import OneSide_Base
from basic import Strategy

class OneSide_Impl(Strategy, OneSide_Base):

    def __init__(self):
        Strategy.__init__(self)
        from marketsim.gen._out.orderbook._queue import Queue
        from marketsim.gen._out.orderbook._oftrader import OfTrader
        from marketsim.gen._out.orderbook._ticksize import TickSize
        from marketsim import event, _
        from marketsim.gen._out._side import Side

        self._book = OfTrader()
        self._orderQueue = Queue(self._book, side = self.side)
        self._source = self._orderQueue.BestPrice
        self._sign = 1 if Side.Sell == self.side() else -1
        self._orders = None
        self._size = self.initialSize
        event.subscribe(self._source, _(self)._wakeUp, self)

    def _wakeUp(self, _):
        from marketsim.gen._out._constant import constant
        from marketsim import request
        price = self._source()

        if price is not None:
            ticks, _ = self._orderQueue.ticks(price)
            if self._orders is None:
                from collections import deque
                self._orders = deque()
                for i in range(0, self._size):
                    t = ticks + i
                    p = self._orderQueue.ticksToPrice(t)
                    order = self.orderFactory(self.side, constant(p))()
                    order.ticks = t
                    self._orders.append(order)
                    self._send(order)
            else:
                orderTicks = self._orders[0].ticks
                if orderTicks == ticks or self._orderQueue.best.owner == self._orders[0].owner:
                    pass
                else:
                    if ticks > orderTicks:
                        while self._orders and self._orders[0].ticks < ticks:
                            order = self._orders[0]
                            if not order.cancelled:
                                self._send(request.Cancel(order))
                            self._orders.popleft()
                        while len(self._orders) < self._size:
                            t = self._orders[len(self._orders) - 1].ticks + 1 if self._orders else ticks
                            order = self.orderFactory(self.side, constant(self._orderQueue.ticksToPrice(t)))()
                            order.ticks = t
                            self._orders.append(order)
                            self._send(order)
                    elif ticks < orderTicks:
                        while self._orders and self._orders[len(self._orders) - 1].ticks > ticks + self._size:
                            self._send(request.Cancel(self._orders[len(self._orders) - 1]))
                            self._orders.pop()
                        num_created = self._size - len(self._orders)
                        while len(self._orders) < self._size:
                            t = self._orders[0].ticks - 1 if self._orders else ticks + (self._size - 1)
                            order = self.orderFactory(self.side, constant(self._orderQueue.ticksToPrice(t)))()
                            order.ticks = t
                            self._orders.appendleft(order)
                        for i in range(num_created):
                            self._send(self._orders[i])
