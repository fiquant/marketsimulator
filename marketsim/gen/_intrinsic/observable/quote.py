from marketsim import ops, event, _

class Quote_Impl(ops.Observable[float]):

    def __init__(self):
        ops.Observable[float].__init__(self)
        self._quotes = None
        self._current = None
        event.subscribe(event.Every(ops.constant(1)), _(self)._wakeUp, self)

    @property
    def quotes(self):
        if self._quotes is None:
            from  marketsim.gen._intrinsic.historical.market import load
            self._quotes = load(self.ticker, self.start, self.end)['Adj Close']
        return self._quotes

    def bind(self, ctx):
        self._scheduler = ctx.world

    def _wakeUp(self, dummy):
        self._current = self.quotes[self._scheduler.currentTime]
        self.fire(self)

    def __call__(self):
        return self._current
