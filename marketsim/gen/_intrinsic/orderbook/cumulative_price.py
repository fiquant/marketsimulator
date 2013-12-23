from marketsim import ops, event, request, Side, _, types
from marketsim.gen._out.observable.orderbook._LastTradePrice import LastTradePrice

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class CumulativePrice_Impl(ops.Observable[float]):

    def __init__(self):

        ops.Observable[float].__init__(self)

        self.price = LastTradePrice(self.book)

        self.reset()
        event.subscribe(self.price, _(self)._update, self)
        event.subscribe(self.depth, _(self)._update, self)

    _internals = ["price"]

    @property
    def digits(self):
        return self.book._digitsToShow

    def _callback(self, sign, (price, volume_unmatched)):
        if volume_unmatched == 0:
            self._current = sign*price
            self.fire(self)
        else: # don't know what to do for the moment
            self._current = None

    def _update(self, dummy = None):
        depth = self.depth()
        side = Side.Buy if depth < 0 else Side.Sell
        self.book.process(
                        request.EvalMarketOrder(side,
                                                abs(depth),
                                                _(self, -sign(depth))._callback))

    def reset(self):
        self._current = None

    def __call__(self):
        return self._current
