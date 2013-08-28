from marketsim import meta, types, bind, flags

class Graph(types.IGraph):
    """ Generic 2D graph to be rendered by means of javascript libraries
    """
    
    def __init__(self, label=""):
        self.label = label
        
    @property
    def _alias(self):
        return [self.label]
    
    @_alias.setter
    def _alias(self, value):
        self.label = value[-1]        

    