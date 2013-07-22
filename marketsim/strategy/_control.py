from _basic import Base

class ControlStrategy(Base):

    def __init__(self, strategy):
        print "init"
        self._strategy = strategy

    def bind(self, context):
        self._strategy.bind(context)

    def __getattr__(self, item):
        print self._strategy.trader
        return self._strategy.__getattribute__(item)


class ControlledTrader(object):

    def __init__(self, trader):
        self._trader = trader
        self._side = None # current side

    def send(self, book, order):
        # if self._side is None or self._side == order.side.opposite:
        self._trader.send(book, order)

    def _onOrderMatched(self, order, other, (price, volume)):
        self._side = order.side if self._side is None else None
        self._trader._onOrderMatched(order, other, (price, volume))

    def __getattr__(self, item):
        return self._trader.__getattribute__(item)


