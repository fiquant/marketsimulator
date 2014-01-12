from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "MarketSigned"])
class signedVolume_MarketSigned(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self):
        pass
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "signedVolume_MarketSigned" % self.__dict__
    
    def __call__(self, signedVolume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._MarketSigned import MarketSigned
        signedVolume = signedVolume if signedVolume is not None else _constant(1.0)
        
        return MarketSigned(signedVolume)
    
