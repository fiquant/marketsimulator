from marketsim import ops, event, _

from marketsim.gen._out.orderbook._bestprice import BestPrice

class LastPrice_Impl(object):

    def __init__(self):
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

