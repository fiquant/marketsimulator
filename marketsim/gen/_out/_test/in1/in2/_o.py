from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["internal tests", "O"])
class O_IObservableFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import call
        from marketsim import event
        from marketsim.gen._out._test.in1.in2._intobs import IntObs_ as __test_in1_in2_IntObs_
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(__test_in1_in2_IntObs_,)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat
    }
    def __repr__(self):
        return "O(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        return self.x
    
def O(x = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        return O_IObservableFloat(x)
    raise Exception('Cannot find suitable overload for O('+str(x) +':'+ str(type(x))+')')
