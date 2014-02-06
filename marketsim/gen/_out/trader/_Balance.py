from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.trader.props import Balance_Impl
from marketsim import IAccount
from marketsim import registry
from marketsim import Price
@registry.expose(["Trader", "Balance"])
class Balance_Optional__IAccount_(Observable[Price],Balance_Impl):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim import Price
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import event
        Observable[Price].__init__(self)
        self.trader = trader if trader is not None else _trader_SingleProxy()
        if isinstance(trader, types.IEvent):
            event.subscribe(self.trader, self.fire, self)
        rtti.check_fields(self)
        Balance_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Balance(%(trader)s)" % self.__dict__
    
def Balance(trader = None): 
    return Balance_Optional__IAccount_(trader)
