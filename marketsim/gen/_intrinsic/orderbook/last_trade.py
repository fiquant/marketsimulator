class LastTrade(object):

    def bind_impl(self, ctx):
        from marketsim import event, _, context
        if not hasattr(self, '_subscriptions'):
            event.subscribe(self.queue.lastTrade, _(self).fire, self)


    @property
    def _impl(self):
        return self.queue.lastTrade

from marketsim.gen._out._intrinsic_base.orderbook.last_trade import LastTradePrice_Base, LastTradeVolume_Base

class LastTradePrice_Impl(LastTrade, LastTradePrice_Base):

    def __call__(self):
        trade = self._impl()
        return trade[0] if trade is not None else None

    @property
    def label(self):
        return 'LastTradePrice_{' + self.queue.label + '}'

class LastTradeVolume_Impl(LastTrade, LastTradeVolume_Base):

    def __call__(self):
        return self._impl()[1] if self._impl() is not None else None

    @property
    def label(self):
        return 'LastTradeVolume_{' + self.queue.label + '}'
