from marketsim import historical, ops, scheduler, event, _, registry

@registry.expose(alias = ["Asset's", "Quote"])
class Quote(ops.Observable[float]):
    
    def __init__(self, ticker = "^GSPC", start = "2001-1-1", end = "2010-1-1"):
        ops.Observable[float].__init__(self)
        self.ticker = ticker
        self.start = start
        self.end = end
        self._quotes = None
        self._current = None
        event.subscribe(scheduler.Timer(ops.constant(1)), _(self)._wakeUp, self)
        
    _properties = {
        'ticker': str,
        'start' : str,
        'end'   : str,
    }
    
    @property
    def quotes(self):
        if self._quotes is None:
            self._quotes = historical.market.load(self.ticker, self.start, self.end)['Adj Close']
        return self._quotes    
        
    def bind(self, ctx):
        self._scheduler = ctx.world

    def _wakeUp(self, dummy):
        self._current = self.quotes[self._scheduler.currentTime]
        self.fire(self)
        
    def __call__(self):
        return self._current
