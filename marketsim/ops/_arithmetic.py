from marketsim import registry

from _all import constant, BinaryOp

@registry.expose(['Arithmetic', '+'], args = (constant(1.), constant(1.)))    
class Sum(BinaryOp[float]):
    """ Function returning Sum of the operands
    """
    
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs + rhs

    sign = '+'         

@registry.expose(['Arithmetic', '*'], args = (constant(1.), constant(1.)))
class Product(BinaryOp[float]):
    """ Function returning product of the operands
    """
    
    sign = '*'
    
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs * rhs
    
@registry.expose(['Arithmetic', '/'], args = (constant(1.), constant(1.)))
class Div(BinaryOp[float]):
    """ Function returning division of the operands
    """
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs / rhs if rhs != 0 else None
    
    sign = '/'
    
    @property
    def label(self):
        return '\\frac{'+self.lhs.label+'}{'+self.rhs.label+'}'

@registry.expose(['Arithmetic', '-'], args = (constant(1.), constant(1.)))    
class Sub(BinaryOp[float]):
    """ Function substructing the right operand from the left one
    """
    
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs - rhs
    
    sign = '-'
