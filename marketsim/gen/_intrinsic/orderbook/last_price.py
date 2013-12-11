from marketsim import ops, event

from marketsim.gen._out.observable.orderbook._BestPrice import BestPrice

class _LastPrice_Impl(ops.Observable[float]):

    def __init__(self):
        ops.Observable[float].__init__(self)
        self._price = BestPrice(self.queue)
        event.subscribe(self._price, _(self)._update, self)
        self._lastPrice = None

    def __call__(self):
        return self._lastPrice

    def _update(self, src):
        p = self._price()
        if p is not None:
            self._lastPrice = p
            self.fire(self)
