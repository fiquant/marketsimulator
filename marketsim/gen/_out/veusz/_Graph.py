from marketsim import registry
from marketsim.gen._intrinsic.veusz import _Graph_Impl
@registry.expose(["N/A", "Graph"])
class Graph(_Graph_Impl):
    """ 
    """ 
    def __init__(self, name = None):
        from marketsim import rtti
        self.name = name if name is not None else "graph"
        rtti.check_fields(self)
        _Graph_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'name' : str
    }
    def __repr__(self):
        return "Graph(%(name)s)" % self.__dict__
    
