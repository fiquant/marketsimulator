from marketsim import registry
from marketsim.gen._intrinsic.observable.quote import Quote_Impl
@registry.expose(["Basic", "Quote"])
class Quote(Quote_Impl):
    """ 
    """ 
    def __init__(self, ticker = None, start = None, end = None):
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.ticker = ticker if ticker is not None else "^GSPC"
        self.start = start if start is not None else "2001-1-1"
        self.end = end if end is not None else "2010-1-1"
        Quote_Impl.__init__(self)
        if isinstance(ticker, types.IEvent):
            event.subscribe(self.ticker, self.fire, self)
        if isinstance(start, types.IEvent):
            event.subscribe(self.start, self.fire, self)
        if isinstance(end, types.IEvent):
            event.subscribe(self.end, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'ticker' : str,
        'start' : str,
        'end' : str
    }
    def __repr__(self):
        return "%(ticker)s" % self.__dict__
    
