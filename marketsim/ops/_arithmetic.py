from marketsim import registry

from _all import BinaryOp

@registry.expose(['Arithmetic', '+'])
class Sum(BinaryOp[float]):
    """ Function returning Sum of the operands
    """
    
    def __init__(self, lhs = None, rhs = None):
        from marketsim.gen._out._constant import constant
        BinaryOp[float].__init__(self,
                                 lhs if lhs is not None else constant(1.),
                                 rhs if rhs is not None else constant(1.))
    
    def _call(self, lhs, rhs):
        return lhs + rhs

    sign = '+'         

@registry.expose(['Arithmetic', '*'])
class Product(BinaryOp[float]):
    """ Function returning product of the operands
    """
    
    sign = '*'
    
    def __init__(self, lhs = None, rhs = None):
        from marketsim.gen._out._constant import constant
        BinaryOp[float].__init__(self,
                                 lhs if lhs is not None else constant(1.),
                                 rhs if rhs is not None else constant(1.))
    
    def _call(self, lhs, rhs):
        return lhs * rhs
    
@registry.expose(['Arithmetic', '/'])
class Div(BinaryOp[float]):
    """ Function returning division of the operands
    """
    def __init__(self, lhs = None, rhs = None):
        from marketsim.gen._out._constant import constant
        BinaryOp[float].__init__(self,
                                 lhs if lhs is not None else constant(1.),
                                 rhs if rhs is not None else constant(1.))
    
    def _call(self, lhs, rhs):
        return lhs / rhs if rhs != 0 else None
    
    sign = '/'
    
    @property
    def label(self):
        return '\\frac{'+self.lhs.label+'}{'+self.rhs.label+'}'

@registry.expose(['Arithmetic', '-'])
class Sub(BinaryOp[float]):
    """ Function substructing the right operand from the left one
    """
    
    def __init__(self, lhs = None, rhs = None):
        from marketsim.gen._out._constant import constant
        BinaryOp[float].__init__(self,
                                 lhs if lhs is not None else constant(1.),
                                 rhs if rhs is not None else constant(1.))
    
    def _call(self, lhs, rhs):
        return lhs - rhs
    
    sign = '-'
