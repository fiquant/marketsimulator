from marketsim import registry
from marketsim.gen._intrinsic.observable.randomwalk import _RandomWalk_Impl
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Basic", "RandomWalk"])
class RandomWalk(_RandomWalk_Impl):
    """ 
    """ 
    def __init__(self, initialValue = None, deltaDistr = None, intervalDistr = None, name = None):
        from marketsim.gen._out.mathutils.rnd._normalvariate import normalvariate as _mathutils_rnd_normalvariate
        from marketsim.gen._out.mathutils.rnd._expovariate import expovariate as _mathutils_rnd_expovariate
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.initialValue = initialValue if initialValue is not None else 0.0
        self.deltaDistr = deltaDistr if deltaDistr is not None else _mathutils_rnd_normalvariate(0.0,1.0)
        self.intervalDistr = intervalDistr if intervalDistr is not None else _mathutils_rnd_expovariate(1.0)
        self.name = name if name is not None else "-random-"
        _RandomWalk_Impl.__init__(self)
        if isinstance(initialValue, types.IEvent):
            event.subscribe(self.initialValue, self.fire, self)
        if isinstance(deltaDistr, types.IEvent):
            event.subscribe(self.deltaDistr, self.fire, self)
        if isinstance(intervalDistr, types.IEvent):
            event.subscribe(self.intervalDistr, self.fire, self)
        if isinstance(name, types.IEvent):
            event.subscribe(self.name, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'initialValue' : float,
        'deltaDistr' : IFunction[float],
        'intervalDistr' : IFunction[float],
        'name' : str
    }
    def __repr__(self):
        return "%(name)s" % self.__dict__
    
