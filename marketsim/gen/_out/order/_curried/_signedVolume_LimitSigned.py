from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "LimitSigned"])
class signedVolume_LimitSigned(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, price = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.price = price if price is not None else _constant(100.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'price' : IFunction[float]
    }
    def __repr__(self):
        return "LimitSigned(%(price)s)" % self.__dict__
    
    def __call__(self, signedVolume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._LimitSigned import LimitSigned
        signedVolume = signedVolume if signedVolume is not None else _constant(1.0)
        price = self.price
        return LimitSigned(signedVolume, price)
    
signedVolume_LimitSigned = signedVolume_LimitSigned
