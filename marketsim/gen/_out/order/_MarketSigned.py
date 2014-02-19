from marketsim.gen._out._observable import ObservableIOrder
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim import registry
@registry.expose(["Order", "MarketSigned"])
class MarketSigned_Float(ObservableIOrder,IObservableIOrder):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self, signedVolume = None):
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out._observable import ObservableIOrder
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        ObservableIOrder.__init__(self)
        self.signedVolume = signedVolume if signedVolume is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signedVolume' : IFunctionfloat
    }
    def __repr__(self):
        return "MarketSigned(%(signedVolume)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._out._side import Side
        from marketsim.gen._intrinsic.order.market import Order_Impl
        signedVolume = self.signedVolume()
        if signedVolume is None: return None
        side = Side.Buy if signedVolume > 0 else Side.Sell
        volume = abs(signedVolume)
        if abs(volume) < 1: return None
        volume = int(volume)
        return Order_Impl(side, volume)
    
def MarketSigned(signedVolume = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunctionfloat):
        return MarketSigned_Float(signedVolume)
    raise Exception('Cannot find suitable overload for MarketSigned('+str(signedVolume) +':'+ str(type(signedVolume))+')')
