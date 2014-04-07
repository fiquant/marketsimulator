from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => .ICandleStick
class IFunctionICandleStick(object):
    _types = [meta.function((),ICandleStick)]
    _types.append(IFunctionobject)
    pass



