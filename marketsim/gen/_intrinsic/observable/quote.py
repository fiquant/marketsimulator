from marketsim import  event, _

from marketsim.gen._out._constant import constant

from marketsim.gen._out._intrinsic_base.observable.quote import Quote_Base

class Quote_Impl(Quote_Base):

    def __init__(self):
        self._quotes = None
        self._current = None
        event.subscribe(event.Every(constant(1)), _(self)._wakeUp, self)

    @property
    def quotes(self):
        if self._quotes is None:
            from  marketsim.gen._intrinsic.historical.market import load
            self._quotes = load(self.ticker, self.start, self.end)['Adj Close']
        return self._quotes

    def bind_impl(self, ctx):
        if not hasattr(self, '_scheduler'):
            self._scheduler = ctx.world

    def _wakeUp(self, dummy):
        self._current = self.quotes[self._scheduler.currentTime]
        self.fire(self)

    def __call__(self):
        return self._current
