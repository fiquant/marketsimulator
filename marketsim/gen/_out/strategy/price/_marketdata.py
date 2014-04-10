from marketsim import registry
@registry.expose(["-", "MarketData"])
class MarketData_StringStringStringFloatFloat(object):
    """ 
    """ 
    def __init__(self, ticker = None, start = None, end = None, delta = None, volume = None):
        from marketsim import rtti
        self.ticker = ticker if ticker is not None else "^GSPC"
        self.start = start if start is not None else "2001-1-1"
        self.end = end if end is not None else "2010-1-1"
        self.delta = delta if delta is not None else 1.0
        self.volume = volume if volume is not None else 1000.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'ticker' : str,
        'start' : str,
        'end' : str,
        'delta' : float,
        'volume' : float
    }
    
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "MarketData(%(ticker)s, %(start)s, %(end)s, %(delta)s, %(volume)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        
        delattr(self, '_processing_ex')
    

    @property
    def Delta(self):
        from marketsim.gen._out.strategy.price._delta import Delta
        return Delta(self)
    
    @property
    def Volume(self):
        from marketsim.gen._out.strategy.price._volume import Volume
        return Volume(self)
    
    @property
    def TwoSides(self):
        from marketsim.gen._out.strategy.price._twosides import TwoSides
        return TwoSides(self)
    
    def OneSide(self, side = None,sign = None):
        from marketsim.gen._out.strategy.price._oneside import OneSide
        return OneSide(self,side,sign)
    
    @property
    def Start(self):
        from marketsim.gen._out.strategy.price._start import Start
        return Start(self)
    
    @property
    def End(self):
        from marketsim.gen._out.strategy.price._end import End
        return End(self)
    
    @property
    def Ticker(self):
        from marketsim.gen._out.strategy.price._ticker import Ticker
        return Ticker(self)
    
    pass
MarketData = MarketData_StringStringStringFloatFloat
