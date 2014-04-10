from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.quote import Quote_Impl
@registry.expose(["Basic", "Quote"])
class Quote_StringStringString(Observablefloat,Quote_Impl):
    """ **Observable that downloads closing prices for every day from *start* to *end* for asset given by *ticker***
    
      and follows the price in scale 1 model unit of time = 1 real day
    
    Parameters are:
    
    **ticker**
    	 defines quotes to download 
    
    **start**
    	 defines first day to download in form YYYY-MM-DD 
    
    **end**
    	 defines last day to download in form YYYY-MM-DD 
    """ 
    def __init__(self, ticker = None, start = None, end = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.ticker = ticker if ticker is not None else "^GSPC"
        self.start = start if start is not None else "2001-1-1"
        self.end = end if end is not None else "2010-1-1"
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
        return "%(ticker)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
def Quote(ticker = None,start = None,end = None): 
    from marketsim import rtti
    if ticker is None or rtti.can_be_casted(ticker, str):
        if start is None or rtti.can_be_casted(start, str):
            if end is None or rtti.can_be_casted(end, str):
                return Quote_StringStringString(ticker,start,end)
    raise Exception('Cannot find suitable overload for Quote('+str(ticker) +':'+ str(type(ticker))+','+str(start) +':'+ str(type(start))+','+str(end) +':'+ str(type(end))+')')
