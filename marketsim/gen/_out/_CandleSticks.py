from marketsim import registry
from marketsim.gen._out._observable._observableicandlestick import ObservableICandleStick
from marketsim.gen._intrinsic.observable.candlestick import CandleSticks_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._icandlestick import ICandleStick
@registry.expose(["Basic", "CandleSticks"])
class CandleSticks_IObservableFloatFloat(ObservableICandleStick,CandleSticks_Impl):
    """ Observable returning at the end of every *timeframe*
    
     open/close/min/max price, its average and standard deviation
    
    Parameters are:
    
    **source**
    	 observable data source considered as asset price 
    
    **timeframe**
    	 size of timeframe 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._out._icandlestick import ICandleStick
        from marketsim.gen._out._observable._observableicandlestick import ObservableICandleStick
        from marketsim import deref_opt
        ObservableICandleStick.__init__(self)
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        self.timeframe = timeframe if timeframe is not None else 10.0
        rtti.check_fields(self)
        CandleSticks_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'timeframe' : float
    }
    
    
    def on_source_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'source', value)
    
    
    
    
    def __repr__(self):
        return "Candles_{%(source)s}" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def CandleSticks(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return CandleSticks_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for CandleSticks('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
