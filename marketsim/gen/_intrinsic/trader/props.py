from marketsim import ops, event, IAccount

from marketsim.gen._out.trader._SingleProxy import SingleProxy

class OnTraded(event.Event):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader = None):
        event.Event.__init__(self)
        self.trader = trader if trader else SingleProxy()

    def bind(self, ctx):
        event.subscribe(self.trader.on_traded, self.fire, self, ctx)

class OnOrderMatched(event.Event):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader = None):
        event.Event.__init__(self)
        self.trader = trader if trader else SingleProxy()

    def bind(self, ctx):
        event.subscribe(self.trader.on_order_matched, self.fire, self, ctx)

    _properties = { 'trader' : IAccount }


class Position_Impl(ops.Observable[float]):
    """ Returns trader's position (i.e. number of assets traded)
    """

    def __init__(self):
        ops.Observable[float].__init__(self)
        event.subscribe(OnTraded(self.trader), self.fire, self)

    def __call__(self):
        return self.trader.amount

    @property
    def digits(self):
        return 0

class Balance_Impl(ops.Observable[float]):
    """ Returns balance of the given *trader*
    """

    def __init__(self):
        ops.Observable[float].__init__(self)
        event.subscribe(OnTraded(self.trader), self.fire, self)

    @property
    def digits(self):
        return self.trader._digitsToShow

    def __call__(self):
        return self.trader.PnL

class _PendingVolume_Impl(ops.Observable[float]): # should be int

    def __init__(self, trader):
        self.trader = trader
        ops.Observable[float].__init__(self)
        self._pendingVolume = 0

    def bind(self, ctx):
        event.subscribe(self.trader.on_order_matched, _(self).onOrderMatched, self, ctx)
        event.subscribe(self.trader.on_order_disposed, _(self).onOrderDisposed, self, ctx)

    def _onOrderSent(self, order):
        if 'volume' in dir(order):
            self._pendingVolume += order.volumeSigned
            self.fire(self)

    def onOrderMatched(self, t, order, price, volume):
        self._pendingVolume -= order.volumeSigned
        self.fire(self)

    def onOrderDisposed(self, t, order):
        self._pendingVolume -= order.volumeSigned
        self.fire(self)

    def __call__(self):
        return self._pendingVolume

from marketsim.gen._intrinsic.orderbook.props import Proxy

class PendingVolume_Impl(Proxy):

    @property
    def _impl(self):
        if '_pendingVolume' not in dir(self.trader):
            self.trader._pendingVolume = _PendingVolume_Impl(self.trader)
        return self.trader._pendingVolume

