from marketsim import registry
from marketsim.gen._out._igraph import IGraph
from marketsim.gen._intrinsic.veusz import Graph_Impl
@registry.expose(["N/A", "Graph"])
class Graph_String(IGraph,Graph_Impl):
    """ **Graph to render at Veusz. Time series are added to it automatically in their constructor**
    
    
    Parameters are:
    
    **name**
    """ 
    def __init__(self, name = None):
        from marketsim import rtti
        self.name = name if name is not None else "graph"
        rtti.check_fields(self)
        Graph_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'name' : str
    }
    
    
    def __repr__(self):
        return "Graph(%(name)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        
        delattr(self, '_processing_ex')
    
def Graph(name = None): 
    from marketsim import rtti
    if name is None or rtti.can_be_casted(name, str):
        return Graph_String(name)
    raise Exception('Cannot find suitable overload for Graph('+str(name) +':'+ str(type(name))+')')
