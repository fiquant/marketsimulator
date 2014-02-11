from marketsim.ops._all import Observable
from marketsim import str
from marketsim import registry
from marketsim.gen._intrinsic.observable.quote import Quote_Impl
from marketsim import Price
@registry.expose(["Basic", "Quote"])
class Quote_StringStringString(Observable[Price],Quote_Impl):
    """   and follows the price in scale 1 model unit of time = 1 real day
    """ 
    def __init__(self, ticker = None, start = None, end = None):
        from marketsim import Price
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
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
    
def Quote(ticker = None,start = None,end = None): 
    from marketsim import str
    from marketsim import rtti
    if ticker is None or rtti.can_be_casted(ticker, str):
        if start is None or rtti.can_be_casted(start, str):
            if end is None or rtti.can_be_casted(end, str):
                return Quote_StringStringString(ticker,start,end)
    raise Exception('Cannot find suitable overload for Quote('+str(ticker)+','+str(start)+','+str(end)+')')
