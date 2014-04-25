from marketsim.gen._out._intrinsic_base.strategy.ladder import OneSide_Base
from basic import Strategy
from marketsim import event, _, request
from marketsim.gen._out._side import Side
from marketsim.gen._out._constant import constant
from marketsim.gen._out.orderbook._queue import Queue
from marketsim.gen._out.orderbook._oftrader import OfTrader

from collections import deque

class OneSide_Impl(Strategy, OneSide_Base):
    """  Ladder strategy for one side
    """

    def __init__(self):
        Strategy.__init__(self)

        # our order book
        self._book = OfTrader()
        # our order queue
        self._orderQueue = Queue(self._book, side = self.side)
        # we are going to track best price changes
        self._source = self._orderQueue.BestPrice
        event.subscribe(self._source, _(self)._wakeUp, self)
        # deque containing issued orders
        self._orders = None
        # how many orders can be issued
        self._size = self.initialSize
        self._suspended = False

    @property
    def suspended(self):
        return self._suspended

    @suspended.setter
    def suspended(self, value):
        if value and self._orders:
            # if we are asked to suspend, cancel all our orders
            for o in self._orders:
                self._send(request.Cancel(o))
            self._orders = None
        self._suspended = value

    def extend(self):
        """ Adds an order with price one tick better
        """
        if self._orders and not self.suspended:
            self._orders.appendleft(self._makeOrder(self._first.ticks - 1))
            self._send(self._first)
        self._size += 1

    def _makeOrder(self, t):
        """ Creates an order with price equivalent to 't' ticks
        """
        p = self._orderQueue.ticksToPrice(t)
        order = self.orderFactory(self.side, constant(p))()
        order.ticks = t
        order.source = self
        return order

    @property
    def _first(self):
        """ Best order in our deque
        """
        return self._orders[0]

    @property
    def _last(self):
        """ Worst order in our queue
        """
        return self._orders[len(self._orders) - 1]

    def _wakeUp(self, _):

        if self.suspended:
            return

        # best price in our queue
        price = self._source()

        if price is not None:
            # translate it into ticks
            ticks, _ = self._orderQueue.ticks(price)

            if self._orders is None: # if we haven't created orders
                self._orders = deque()
                # let's create orders with ticks [ticks, ticks + self._size)
                for i in range(0, self._size):
                    self._orders.append(self._makeOrder(ticks + i))
                    self._send(self._last)
            else:
                orderTicks = self._orders[0].ticks # ticks of the best order
                if orderTicks == ticks or self._orderQueue.best.owner == self._first.owner:
                    pass
                else:
                    # if new price is worse than our best order price
                    # (it means that our orders traded)
                    if ticks > orderTicks:
                        # let's remove matched orders
                        while self._orders and self._first.ticks < ticks:
                            order = self._first
                            if not order.cancelled: # should be always False
                                self._send(request.Cancel(order))
                            self._orders.popleft()
                        # and add new ones to the end of the queue
                        while len(self._orders) < self._size:
                            t = self._last.ticks + 1 if self._orders else ticks
                            self._orders.append(self._makeOrder(t))
                            self._send(self._last)
                    # if new price is better than our best order price
                    elif ticks < orderTicks:
                        # let's remove bad orders
                        while self._orders and self._last.ticks > ticks + self._size:
                            self._send(request.Cancel(self._last))
                            self._orders.pop()
                        # calculate how many orders we should insert
                        num_created = self._size - len(self._orders)
                        # create better orders
                        while len(self._orders) < self._size:
                            t = self._first.ticks - 1 if self._orders else ticks + (self._size - 1)
                            self._orders.appendleft(self._makeOrder(t))
                        # and send them to the market
                        for i in range(num_created):
                            self._send(self._orders[i])

from marketsim.gen._out._intrinsic_base.strategy.ladder import MarketMaker_Base

class MarketMaker_Impl(Strategy, MarketMaker_Base):
    """ Sum of two ladder strategies.
    """

    def __init__(self):
        Strategy.__init__(self)
        from marketsim._pub import strategy, side

        self._seller = strategy.price.Ladder(self.orderFactory, self.initialSize, side.Sell())
        self._buyer = strategy.price.Ladder(self.orderFactory, self.initialSize, side.Buy())

        event.subscribe(self._seller.on_order_created, _(self)._send, self)
        event.subscribe(self._buyer.on_order_created, _(self)._send, self)

    @property
    def suspended(self):
        assert self._seller.suspended == self._buyer.suspended
        return self._seller.suspended

    @suspended.setter
    def suspended(self, value):
        self._seller.suspended = value
        self._buyer.suspended = value


    _internals = ['_seller', '_buyer']

    def dispose(self):
        for s in [self._seller, self._buyer]:
            s.dispose()

from marketsim.gen._out._intrinsic_base.strategy.ladder import Balancer_Base

class Balancer_Impl(Strategy, Balancer_Base):
    """ Strategy that wraps another ladder strategy and controls their sizes
    """

    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.inner.on_order_created, _(self)._send, self)

    @property
    def suspended(self):
        return self.inner.suspended

    @suspended.setter
    def suspended(self, value):
        self.inner.suspended = value

    @property
    def _seller(self):
        return self.inner._seller

    @property
    def _buyer(self):
        return self.inner._buyer

    def bind(self, context):
        if not hasattr(self, '_subscriptions'):
            event.subscribe(context.trader.on_order_matched, _(self)._onOrderMatched, self, context)

    def bind_impl(self, context):
        if not hasattr(self, '_subscriptions'):
            Strategy.bind_impl(self, context)
            event.subscribe(context.trader.on_order_matched, _(self)._onOrderMatched, self)

    def _onOrderMatched(self, trader, order, price, volume):
        # when our trader gets a notification about a trade done
        if order.empty and hasattr(order, 'source') and not self.suspended:
            # if strategy sent the order is seller
            if order.source == self._seller:
                # check buyer size,
                if self._buyer._size < self.maximalSize:
                    # and if it is ok, extend it
                    self._buyer.extend()
            if order.source == self._buyer:
                if self._seller._size < self.maximalSize:
                    self._seller.extend()

from marketsim.gen._out._intrinsic_base.strategy.ladder import Clearable_Base

class Clearable_Impl(Strategy, Clearable_Base):
    """ Clears trader positions if 'predicate' becomes True
    """

    def __init__(self):
        Strategy.__init__(self)
        from marketsim._pub import trader, orderbook
        self._balance = trader.Balance()
        self._position = trader.Position()
        self._pendingVolume = trader.PendingVolume()
        self._internalSuspended = False

        event.subscribe(self.inner.on_order_created, _(self)._send, self)
        event.subscribe(self.predicate, _(self)._wakeUp, self)

    _internals = ["_position", "_pendingVolume"]

    def clearPosition(self):
        from marketsim._pub import order, side
        position = self._position()
        pending = self._pendingVolume()
        if position is not None and pending is not None:
            self._internalSuspended = True
            self.suspended = True
            # signed number of assets that we have
            p = position + pending
            if p > 0: # if positive, we sell
                self._send(order.Market(side.Sell(), constant(p))())
            if p < 0: # if negative, we buy
                self._send(order.Market(side.Buy(), constant(-p))())

    def _wakeUp(self, r):
        # when predicate changes, check its value
        if not self.suspended and self.predicate():
            self.clearPosition()

    @property
    def suspended(self):
        return self.inner.suspended or self._internalSuspended

    @suspended.setter
    def suspended(self, value):
        self.inner.suspended = value or self._internalSuspended

from marketsim.gen._out._intrinsic_base.strategy.ladder import Suspend_Base

class Suspend_Impl(Strategy, Suspend_Base):
    """  Suspends inner strategy iff predicate evaluates to True
    """

    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.predicate, _(self)._wakeUp, self)
        event.subscribe(self.inner.on_order_created, _(self)._send, self)
        self._suspended = False

    @property
    def suspended(self):
        return self._suspended

    @suspended.setter
    def suspended(self, value):
        self._suspended = value
        if self._suspended:
            self.inner.suspended = True
        elif not self.predicate():
            self.inner.suspended = False

    def _wakeUp(self, _):
        if not self._suspended:
            c = self.predicate()
            if c is not None:
                self.inner.suspended = c
                #print self.inner.suspended
