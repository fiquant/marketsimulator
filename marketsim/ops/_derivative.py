from marketsim import types

from _all import Function

class Derivative(Function[float]):
    
    def __init__(self, source):
        self.source = source
        self._alias = ['Basic', 'Derivative']
        
    @property
    def attributes(self):
        return {}
        
    _properties = { 'source' : types.IDifferentiable }
    
    @property
    def label(self):
        return '\\frac{d' + getLabel(self.source) + '}{dt}'
        
    def __call__(self):
        return self.source.derivative()

