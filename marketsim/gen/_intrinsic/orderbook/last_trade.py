from props import Proxy

class LastTrade(Proxy):

    @property
    def _impl(self):
        return self.queue.lastTrade

class _LastTradePrice_Impl(LastTrade):

    def __call__(self):
        trade = LastTrade.__call__(self)
        return trade[0] if trade is not None else None

    @property
    def label(self):
        return 'LastTradePrice_{' + self.queue.label + '}'

class _LastTradeVolume_Impl(LastTrade):

    def __call__(self):
        return LastTrade.__call__(self)[1]

    @property
    def label(self):
        return 'LastTradeVolume_{' + self.queue.label + '}'
