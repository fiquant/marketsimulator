from marketsim import registry
from marketsim.gen._out.observable.trader import SingleProxy
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.orderbook.of_trader import _OfTrader_Impl



@registry.expose(['Proxies', 'OfTrader'])
class OfTrader(Function[float], _OfTrader_Impl):
    """ 
    """ 
    def __init__(self, Trader = None):
        self.Trader = Trader if Trader is not None else SingleProxy()
        _OfTrader_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "$(TraderAsset)" % self.__dict__
    
