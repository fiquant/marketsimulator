from marketsim import types
from marketsim.trader._proxy import SingleProxy

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
