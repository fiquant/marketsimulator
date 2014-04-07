from marketsim import registry
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
@registry.expose(["Order", "MarketSigned"])
class MarketSigned_Float(ObservableIOrder,IObservableIOrder):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self, signedVolume = None):
        from marketsim import rtti
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim import deref_opt
        ObservableIOrder.__init__(self)
        self.signedVolume = signedVolume if signedVolume is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signedVolume' : IFunctionfloat
    }
    
    
    
    def __repr__(self):
        return "MarketSigned(%(signedVolume)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunctionfloat):
        return MarketSigned_Float(signedVolume)
    raise Exception('Cannot find suitable overload for MarketSigned('+str(signedVolume) +':'+ str(type(signedVolume))+')')
