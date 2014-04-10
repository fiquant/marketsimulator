from marketsim import registry
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["-", "RSI"])
class RSI_IObservableFloatFloatFloat(object):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        self.timeframe = timeframe if timeframe is not None else 10.0
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'timeframe' : float,
        'alpha' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        delattr(self, '_processing_ex')
    

    @property
    def Timeframe(self):
        from marketsim.gen._out.math._timeframe import Timeframe
        return Timeframe(self)
    
    @property
    def Value(self):
        from marketsim.gen._out.math._value import Value
        return Value(self)
    
    @property
    def Source(self):
        from marketsim.gen._out.math._source import Source
        return Source(self)
    
    @property
    def Raw(self):
        from marketsim.gen._out.math._raw import Raw
        return Raw(self)
    
    @property
    def Alpha(self):
        from marketsim.gen._out.math._alpha import Alpha
        return Alpha(self)
    
    pass
RSI = RSI_IObservableFloatFloatFloat
