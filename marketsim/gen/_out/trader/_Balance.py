from marketsim import registry
from marketsim.gen._intrinsic.trader.props import Balance_Impl
from marketsim import IAccount
@registry.expose(["Trader", "Balance"])
class Balance_Optional__IAccount_(Balance_Impl):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        self.trader = trader if trader is not None else _trader_SingleProxy()
        rtti.check_fields(self)
        Balance_Impl.__init__(self)
        if isinstance(trader, types.IEvent):
            event.subscribe(self.trader, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Balance(%(trader)s)" % self.__dict__
    
Balance = Balance_Optional__IAccount_
