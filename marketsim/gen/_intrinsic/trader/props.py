from marketsim import ops, event, _

from marketsim.gen._out._iaccount import IAccount

from marketsim.gen._out.trader._singleproxy import SingleProxy

from marketsim.gen._out._intrinsic_base.trader.props import Position_Base, Balance_Base, PendingVolume_Base

from marketsim.gen._out.event._event import Event_Impl

from marketsim.gen._out._intrinsic_base.trader.props import OnTraded_Base

class OnTraded_Impl(Event_Impl, OnTraded_Base):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self):
        Event_Impl.__init__(self)

    def bind_ex(self, ctx):
        if not hasattr(self, '_subscriptions'):
            event.subscribe(self.trader.on_traded, self.fire, self)

from marketsim.gen._out.event._event import Event_Impl

class OnOrderMatched(Event_Impl):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader = None):
        Event_Impl.__init__(self)
        self.trader = trader if trader else SingleProxy()

    def reset_ex(self, generation):
        self.trader.reset_ex(generation)
        self._subscriptions[0].reset_ex(generation)
        self._reset_generation_ex = generation

    def bind_ex(self, ctx):
        if not hasattr(self, '_subscriptions'):
            self.trader.bind_ex(ctx)
            event.subscribe(self.trader.on_order_matched, self.fire, self)
            self._subscriptions[0].bind_ex(ctx)
            self._bound_ex = True

    _properties = { 'trader' : IAccount }


class Position_Impl(Position_Base):
    """ Returns trader's position (i.e. number of assets traded)
    """

    def __init__(self):
        from marketsim.gen._out.trader._ontraded import OnTraded
        event.subscribe(OnTraded(self.trader), self.fire, self)

    def __call__(self):
        return self.trader.amount

    @property
    def digits(self):
        return 0

class Balance_Impl(Balance_Base):
    """ Returns balance of the given *trader*
    """

    def __init__(self):
        from marketsim.gen._out.trader._ontraded import OnTraded
        event.subscribe(OnTraded(self.trader), self.fire, self)

    @property
    def digits(self):
        return self.trader._digitsToShow

    def __call__(self):
        return self.trader.PnL

class _PendingVolume_Impl(object): # should be int

    def __init__(self, trader):
        self.trader = trader
        self._pendingVolume = 0

    def reset_ex(self, generation):
        self.trader.reset_ex(generation)
        for x in self._subscriptions:
            x.reset_ex(generation)
        self._reset_generation_ex = generation

    def bind_impl(self, ctx):
        if not hasattr(self, '_subscriptions'):
            self.trader.bind_ex(ctx)
            event.subscribe(self.trader.on_order_matched, _(self).onOrderMatched, self)
            event.subscribe(self.trader.on_order_disposed, _(self).onOrderDisposed, self)
            for x in self._subscriptions:
                x.bind_ex(ctx)
            self._bound_ex = True

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

class PendingVolume_Impl(PendingVolume_Base):

    @property
    def _impl(self):
        if '_pendingVolume' not in dir(self.trader):
            self.trader._pendingVolume = _PendingVolume_Impl(self.trader)
        return self.trader._pendingVolume

    def __call__(self):
        return self._impl()

