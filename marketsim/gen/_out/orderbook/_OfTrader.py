from marketsim import registry
from marketsim.gen._intrinsic.orderbook.of_trader import _OfTrader_Impl
from marketsim import IAccount
@registry.expose(["Asset", "OfTrader"])
class OfTrader(_OfTrader_Impl):
    """ 
    """ 
    def __init__(self, Trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        self.Trader = Trader if Trader is not None else _trader_SingleProxy()
        _OfTrader_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Trader' : IAccount
    }
    
