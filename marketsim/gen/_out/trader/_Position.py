from marketsim import registry
from marketsim.gen._intrinsic.trader.props import Position_Impl
from marketsim import IAccount
from marketsim import IAccount
@registry.expose(["Trader", "Position"])
class Position(Position_Impl):
    """   It is negative if trader has sold more assets than has bought and
      positive otherwise
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        self.trader = trader if trader is not None else _trader_SingleProxy()
        rtti.check_fields(self)
        Position_Impl.__init__(self)
        if isinstance(trader, types.IEvent):
            event.subscribe(self.trader, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Position(%(trader)s)" % self.__dict__
    
