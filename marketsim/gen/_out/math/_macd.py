from marketsim import registry
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["-", "macd"])
class macd_IObservableFloatFloatFloat(object):
    """ 
    """ 
    def __init__(self, source = None, slow = None, fast = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        self.slow = slow if slow is not None else 26.0
        self.fast = fast if fast is not None else 12.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'slow' : float,
        'fast' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "MACD_{%(fast)s}^{%(slow)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    

    def Histogram(self, timeframe = None,step = None):
        from marketsim.gen._out.math._histogram import Histogram
        return Histogram(self,timeframe,step)
    
    def Signal(self, timeframe = None,step = None):
        from marketsim.gen._out.math._signal import Signal
        return Signal(self,timeframe,step)
    
    @property
    def Fast(self):
        from marketsim.gen._out.math._fast import Fast
        return Fast(self)
    
    @property
    def Value(self):
        from marketsim.gen._out.math._value import Value
        return Value(self)
    
    @property
    def Slow(self):
        from marketsim.gen._out.math._slow import Slow
        return Slow(self)
    
    @property
    def Source(self):
        from marketsim.gen._out.math._source import Source
        return Source(self)
    
    pass
macd = macd_IObservableFloatFloatFloat
