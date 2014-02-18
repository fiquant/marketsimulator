from marketsim import types
from marketsim.gen._out.trader._singleproxy import SingleProxy
from marketsim import getLabel

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

class _OfTrader_Impl(Base):

    def __init__(self):
        self._alias = ["$(TraderAsset)"] if type(self.Trader) == SingleProxy else ['OfTrader']
        Base.__init__(self)

    @property
    def _impl(self):
        try:
            return self.Trader.orderBook
        except AttributeError:
            return None

class _Proxy_Impl(Base):

    def __init__(self):
        self._impl = None
        Base.__init__(self)

    @property
    def label(self):
        return self._impl.label if self._impl else '$(OrderBook)'

    def bind(self, ctx):
        assert self._impl is None
        self._impl = ctx.orderbook

