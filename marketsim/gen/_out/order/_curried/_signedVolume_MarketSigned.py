from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
@registry.expose(["Order", "MarketSigned"])
class signedVolume_MarketSigned_(IFunctionIObservableIOrderIFunctionfloat):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "MarketSigned" % self.__dict__
    
    def __call__(self, signedVolume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._marketsigned import MarketSigned
        signedVolume = signedVolume if signedVolume is not None else _constant_Float(1.0)
        
        return MarketSigned(signedVolume)
    
def signedVolume_MarketSigned(): 
    from marketsim import rtti
    return signedVolume_MarketSigned_()
    raise Exception('Cannot find suitable overload for signedVolume_MarketSigned('++')')
