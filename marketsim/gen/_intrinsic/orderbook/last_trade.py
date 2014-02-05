class LastTrade(object):

    def bind(self, ctx):
        from marketsim import event, _, context
        event.subscribe(self.queue.lastTrade, _(self).fire, self)
        context.bind(self._subscriptions, ctx)

    @property
    def _impl(self):
        return self.queue.lastTrade

class _LastTradePrice_Impl(LastTrade):

    def __call__(self):
        trade = self._impl()
        return trade[0] if trade is not None else None

    @property
    def label(self):
        return 'LastTradePrice_{' + self.queue.label + '}'

class _LastTradeVolume_Impl(LastTrade):

    def __call__(self):
        return self._impl()[1]

    @property
    def label(self):
        return 'LastTradeVolume_{' + self.queue.label + '}'
