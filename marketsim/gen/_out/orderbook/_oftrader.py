from marketsim import registry
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.orderbook.of_trader import OfTrader_Impl
from marketsim.gen._out._iaccount import IAccount
@registry.expose(["Asset", "OfTrader"])
class OfTrader_IAccount(IOrderBook,OfTrader_Impl):
    """ **Phantom orderbook used to refer to the order book associated with a single asset trader**
    
    
      May be used only in objects that are held by traders (so it is used in trader properties and strategies)
    
    Parameters are:
    
    **Trader**
    """ 
    def __init__(self, Trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import deref_opt
        from marketsim import rtti
        self.Trader = Trader if Trader is not None else deref_opt(_trader_SingleProxy_())
        rtti.check_fields(self)
        OfTrader_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Trader' : IAccount
    }
    
    
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        self.Trader.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def OfTrader(Trader = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if Trader is None or rtti.can_be_casted(Trader, IAccount):
        return OfTrader_IAccount(Trader)
    raise Exception('Cannot find suitable overload for OfTrader('+str(Trader) +':'+ str(type(Trader))+')')
