# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.ladder import MarketMaker_Impl
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
@registry.expose(["Price function", "LadderMM"])
class LadderMM_SideFloatIObservableIOrderIntInt(ISingleAssetStrategy,MarketMaker_Impl):
    """ 
    """ 
    def __init__(self, orderFactory = None, maximalSize = None, initialSize = None):
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_sideprice_Limit_Float())
        self.maximalSize = maximalSize if maximalSize is not None else 20
        self.initialSize = initialSize if initialSize is not None else 10
        rtti.check_fields(self)
        MarketMaker_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat,
        'maximalSize' : int,
        'initialSize' : int
    }
    
    
    
    
    
    
    def __repr__(self):
        return "LadderMM(%(orderFactory)s, %(maximalSize)s, %(initialSize)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.orderFactory.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def LadderMM(orderFactory = None,maximalSize = None,initialSize = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    from marketsim import rtti
    if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
        if maximalSize is None or rtti.can_be_casted(maximalSize, int):
            if initialSize is None or rtti.can_be_casted(initialSize, int):
                return LadderMM_SideFloatIObservableIOrderIntInt(orderFactory,maximalSize,initialSize)
    raise Exception('Cannot find suitable overload for LadderMM('+str(orderFactory) +':'+ str(type(orderFactory))+','+str(maximalSize) +':'+ str(type(maximalSize))+','+str(initialSize) +':'+ str(type(initialSize))+')')
