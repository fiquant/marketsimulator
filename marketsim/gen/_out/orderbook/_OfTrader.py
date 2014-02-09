from marketsim import registry
from marketsim.gen._intrinsic.orderbook.of_trader import _OfTrader_Impl
from marketsim import IAccount
@registry.expose(["Asset", "OfTrader"])
class OfTrader_IAccount(_OfTrader_Impl):
    """ 
      May be used only in objects that are held by traders (so it is used in trader properties and strategies)
    """ 
    def __init__(self, Trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import rtti
        self.Trader = Trader if Trader is not None else _trader_SingleProxy()
        rtti.check_fields(self)
        _OfTrader_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Trader' : IAccount
    }
    
def OfTrader(Trader = None): 
    from marketsim import IAccount
    from marketsim import rtti
    if Trader is None or rtti.can_be_casted(Trader, IAccount):
        return OfTrader_IAccount(Trader)
    raise Exception("Cannot find suitable overload")
