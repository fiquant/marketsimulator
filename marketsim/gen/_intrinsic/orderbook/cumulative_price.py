from marketsim import ops, event, request, Side, _, types

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class CumulativePrice_Impl(object):

    def __init__(self):
        from marketsim.gen._out.orderbook.ask._lasttradeprice import LastTradePrice as Ask
        from marketsim.gen._out.orderbook.bid._lasttradeprice import LastTradePrice as Bid
        self.ask = Ask(self.book)
        self.bid = Bid(self.book)

        self.reset()
        event.subscribe(self.ask, _(self)._update, self)
        event.subscribe(self.bid, _(self)._update, self)
        event.subscribe(self.depth, _(self)._update, self)

    _internals = ["ask", "bid"]

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
