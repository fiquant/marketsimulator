from marketsim.gen._out._igraph import IGraph

class Graph(IGraph):
    """ Generic 2D graph to be rendered by means of javascript libraries
    """
    
    def __init__(self, name=""):
        self.label = name

    def bind_ex(self, ctx):
        self._bound_ex = True

    def reset_ex(self, generation):
        self._reset_generation_ex = generation
        
    @property
    def _alias(self):
        return [self.label]
    
    @_alias.setter
    def _alias(self, value):
        self.label = value[-1]        

    