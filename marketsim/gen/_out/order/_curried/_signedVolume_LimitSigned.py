from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "LimitSigned"])
class signedVolume_LimitSigned_Float(IFunctionIObservableIOrderIFunctionfloat):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.price = price if price is not None else _constant_Float(100.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'price' : IFunctionfloat
    }
    def __repr__(self):
        return "LimitSigned(%(price)s)" % self.__dict__
    
    def __call__(self, signedVolume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._limitsigned import LimitSigned
        signedVolume = signedVolume if signedVolume is not None else _constant_Float(1.0)
        price = self.price
        return LimitSigned(signedVolume, price)
    
def signedVolume_LimitSigned(price = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunctionfloat):
        return signedVolume_LimitSigned_Float(price)
    raise Exception('Cannot find suitable overload for signedVolume_LimitSigned('+str(price) +':'+ str(type(price))+')')
