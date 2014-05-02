from marketsim.gen._out._igraph import IGraph

from marketsim.gen._out._intrinsic_base.js import Graph_Base

class Graph_Impl(Graph_Base):
    """ Generic 2D graph to be rendered by means of javascript libraries
    """
    
    @property
    def _alias(self):
        return [self.label]

    def addTimeSerie(self, ts):
        pass
    
    @_alias.setter
    def _alias(self, value):
        pass # not impl

    