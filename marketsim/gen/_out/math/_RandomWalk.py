from marketsim import registry
from marketsim.gen._intrinsic.observable.randomwalk import _RandomWalk_Impl
from marketsim import float
from marketsim import float
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import str
@registry.expose(["Basic", "RandomWalk"])
class RandomWalk_Optional__Float___Optional________Float___Optional________Float___Optional__String_(_RandomWalk_Impl):
    """ 
    """ 
    def __init__(self, initialValue = None, deltaDistr = None, intervalDistr = None, name = None):
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.math.random._normalvariate import normalvariate as _math_random_normalvariate
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        self.initialValue = initialValue if initialValue is not None else 0.0
        if isinstance(initialValue, types.IEvent):
            event.subscribe(self.initialValue, self.fire, self)
        self.deltaDistr = deltaDistr if deltaDistr is not None else _math_random_normalvariate(0.0,1.0)
        if isinstance(deltaDistr, types.IEvent):
            event.subscribe(self.deltaDistr, self.fire, self)
        self.intervalDistr = intervalDistr if intervalDistr is not None else _math_random_expovariate(1.0)
        if isinstance(intervalDistr, types.IEvent):
            event.subscribe(self.intervalDistr, self.fire, self)
        self.name = name if name is not None else "-random-"
        if isinstance(name, types.IEvent):
            event.subscribe(self.name, self.fire, self)
        rtti.check_fields(self)
        _RandomWalk_Impl.__init__(self)
    
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
    
RandomWalk = RandomWalk_Optional__Float___Optional________Float___Optional________Float___Optional__String_
