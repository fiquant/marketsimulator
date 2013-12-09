from marketsim import types, Side

class Base(types.IOrderBook):

    _properties = {}

    def __getattr__(self, name):
        if name[0:2] != '__' and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError

    def __str__(self):
        return 'Proxy for ' + (self._impl.__str__() if self._impl else '')

    def __repr__(self):
        return self.__str__()

class Queue(types.IOrderQueue):

    _properties = { 'orderbook' : types.IOrderBook,
                    'side'      : types.Side }

    def __init__(self, orderbook, side):
        self.orderbook = orderbook
        self.side = side

    @property
    def _impl(self):
        try:
            return self.orderbook.queue(self.side)
        except AttributeError:
            return None

    def __getattr__(self, name):
        if name[0:2] != '__' and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError

    def __str__(self):
        return 'Proxy for ' + (self._impl.__str__() if self._impl else '')

    def __repr__(self):
        return self.__str__()


def _Asks_Impl(orderbook):
    return Queue(orderbook, Side.Sell)

def _Bids_Impl(orderbook):
    return Queue(orderbook, Side.Buy)
