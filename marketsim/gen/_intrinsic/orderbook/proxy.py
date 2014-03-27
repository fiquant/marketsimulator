from marketsim import getLabel
from marketsim.gen._out._side import Side

from marketsim.gen._out._intrinsic_base.orderbook.proxy import Queue_Base, Asks_Base, Bids_Base

class Base(object):

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

class Queue(object):

    def __init__(self, side):
        self._side = side

    @property
    def _impl(self):
        try:
            return self.book.queue(self._side)
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

class Queue_Impl(Queue, Queue_Base):

    def __init__(self):
        Queue.__init__(self, self.side())

class Asks_Impl(Queue, Asks_Base):

    def __init__(self):
        Queue.__init__(self, Side.Sell)

class Bids_Impl(Queue, Bids_Base):

    def __init__(self):
        Queue.__init__(self, Side.Buy)
