from marketsim.gen._out._observable._observableicandlestick import ObservableICandleStick
from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._intrinsic.observable.candlestick import CandleSticks_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
@registry.expose(["Basic", "CandleSticks"])
class CandleSticks_IObservableFloatFloat(ObservableICandleStick,CandleSticks_Impl):
    """  open/close/min/max price, its average and standard deviation
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim.gen._out._observable._observableicandlestick import ObservableICandleStick
        from marketsim import event
        from marketsim.gen._out._icandlestick import ICandleStick
        ObservableICandleStick.__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        event.subscribe(self.source, self.fire, self)
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
    def __repr__(self):
        return "Candles_{%(source)s}" % self.__dict__
    
def CandleSticks(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return CandleSticks_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for CandleSticks('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
