from marketsim import ops, event

from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy

class OnTraded(event.Event):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader = None):
        event.Event.__init__(self)
        self.trader = trader if trader else SingleProxy()

    def bind(self, ctx):
        event.subscribe(self.trader.on_traded, self.fire, self, ctx)


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

