from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._out._iobservable._iobservableicandlestick import IObservableICandleStick
from marketsim import meta
#(.IObservable[.Float],.Float) => .IObservable[.ICandleStick]
class IFunctionIObservableICandleStickIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservableICandleStick)]
    
    pass



