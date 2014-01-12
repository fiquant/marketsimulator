from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "LimitSigned"])
class signedVolume_LimitSigned(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, price = None):
        from marketsim.gen._out._constant import constant as _constant
        self.price = price if price is not None else _constant(100.0)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'price' : IFunction[float]
    }
    def __repr__(self):
        return "signedVolume_LimitSigned(%(price)s)" % self.__dict__
    
    def __call__(self, signedVolume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._LimitSigned import LimitSigned
        signedVolume = signedVolume if signedVolume is not None else _constant(1.0)
        price = self.price
        return LimitSigned(signedVolume, price)
    
