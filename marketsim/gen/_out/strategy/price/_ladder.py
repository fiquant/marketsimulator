# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
from marketsim.gen._intrinsic.strategy.ladder import OneSide_Impl
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Price function", "Ladder"])
class Ladder_SideFloatIObservableIOrderIntSide(ISingleAssetStrategy,OneSide_Impl):
    """ 
    """ 
    def __init__(self, orderFactory = None, initialSize = None, side = None):
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim import deref_opt
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_sideprice_Limit_Float())
        self.initialSize = initialSize if initialSize is not None else 10
        self.side = side if side is not None else deref_opt(_side_Sell_())
        rtti.check_fields(self)
        OneSide_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat,
        'initialSize' : int,
        'side' : IFunctionSide
    }
    
    
    
    
    
    
    def __repr__(self):
        return "Ladder(%(orderFactory)s, %(initialSize)s, %(side)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.orderFactory.bind_ex(self._ctx_ex)
        self.side.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Ladder(orderFactory = None,initialSize = None,side = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim import rtti
    if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
        if initialSize is None or rtti.can_be_casted(initialSize, int):
            if side is None or rtti.can_be_casted(side, IFunctionSide):
                return Ladder_SideFloatIObservableIOrderIntSide(orderFactory,initialSize,side)
    raise Exception('Cannot find suitable overload for Ladder('+str(orderFactory) +':'+ str(type(orderFactory))+','+str(initialSize) +':'+ str(type(initialSize))+','+str(side) +':'+ str(type(side))+')')
