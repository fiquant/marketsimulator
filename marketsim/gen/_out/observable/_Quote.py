from marketsim import registry
from marketsim import Price
from marketsim import Price
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.quote import Quote_Impl
from marketsim import str
from marketsim import str
from marketsim import str
@registry.expose(["Basic", "Quote"])
class Quote_Optional__String___Optional__String___Optional__String_(Observable[Price],Quote_Impl):
    """   and follows the price in scale 1 model unit of time = 1 real day
    """ 
    def __init__(self, ticker = None, start = None, end = None):
        from marketsim import Price
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[Price].__init__(self)
        self.ticker = ticker if ticker is not None else "^GSPC"
        if isinstance(ticker, types.IEvent):
            event.subscribe(self.ticker, self.fire, self)
        self.start = start if start is not None else "2001-1-1"
        if isinstance(start, types.IEvent):
            event.subscribe(self.start, self.fire, self)
        self.end = end if end is not None else "2010-1-1"
        if isinstance(end, types.IEvent):
            event.subscribe(self.end, self.fire, self)
        rtti.check_fields(self)
        Quote_Impl.__init__(self)
    
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
    
Quote = Quote_Optional__String___Optional__String___Optional__String_
