from marketsim import types, Side, getLabel

class Base(types.IOrderBook):

    _properties = {}

    def __getattr__(self, name):
        if name[0:2] != '__' and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError

    def __str__(self):
        return getLabel(self._impl) if self._impl else ''

    def __repr__(self):
        return self.__str__()

class Queue(types.IOrderQueue):

    _properties = { 'side'      : types.Side }

    def __init__(self, side):
        self.side = side

    @property
    def _impl(self):
        try:
            return self.book.queue(self.side)
        except AttributeError:
            return None

    def __getattr__(self, name):
        if name[0:2] != '__' and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError

    def __str__(self):
        return getLabel(self._impl) if self._impl else ''

    def __repr__(self):
        return self.__str__()

class _Asks_Impl(Queue):

    def __init__(self):
        Queue.__init__(self, Side.Sell)

class _Bids_Impl(Queue):

    def __init__(self):
        Queue.__init__(self, Side.Buy)
