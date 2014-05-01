# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.canceller import Canceller_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Strategy", "Canceller"])
class Canceller_Float(ISingleAssetStrategy,Canceller_Impl):
    """ **Strategy that listens to all orders sent by a trader to the market**
    
      and in some moments of time it randomly chooses an order and cancels it
      Note: a similar effect can be obtained using order.WithExpiry meta orders
    
    Parameters are:
    
    **cancellationIntervalDistr**
    	 intervals between order cancellations 
    """ 
    def __init__(self, cancellationIntervalDistr = None):
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.cancellationIntervalDistr = cancellationIntervalDistr if cancellationIntervalDistr is not None else deref_opt(_math_random_expovariate_Float(1.0))
        rtti.check_fields(self)
        Canceller_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cancellationIntervalDistr' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "Canceller(%(cancellationIntervalDistr)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.cancellationIntervalDistr.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.cancellationIntervalDistr.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
def Canceller(cancellationIntervalDistr = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if cancellationIntervalDistr is None or rtti.can_be_casted(cancellationIntervalDistr, IFunctionfloat):
        return Canceller_Float(cancellationIntervalDistr)
    raise Exception('Cannot find suitable overload for Canceller('+str(cancellationIntervalDistr) +':'+ str(type(cancellationIntervalDistr))+')')
