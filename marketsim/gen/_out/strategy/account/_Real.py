from marketsim import registry
from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._intrinsic.strategy.account import _Account_Impl
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Strategy", "Real"])
class Real_ISingleAssetStrategy(IAccount,_Account_Impl):
    """   how orders sent by the strategy have been actually traded
    """ 
    def __init__(self, inner = None):
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIObservableIOrder as _strategy_Noise_IEventSideIObservableIOrder
        from marketsim import rtti
        self.inner = inner if inner is not None else _strategy_Noise_IEventSideIObservableIOrder()
        rtti.check_fields(self)
        _Account_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy
    }
    def __repr__(self):
        return "Real(%(inner)s)" % self.__dict__
    
def Real(inner = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        return Real_ISingleAssetStrategy(inner)
    raise Exception('Cannot find suitable overload for Real('+str(inner) +':'+ str(type(inner))+')')
def real(): 
    from marketsim.gen._out.strategy.account.inner._inner_real import inner_Real_ as _strategy_account_inner_inner_Real_
    from marketsim import rtti
    return _strategy_account_inner_inner_Real_()
    raise Exception('Cannot find suitable overload for real('++')')
