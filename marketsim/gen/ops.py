from types import IFunction

Constant = {}

class Constant_float(IFunction[float]):
    
    def __init__(self, defvalue = 1.):
        self.defvalue = defvalue
        
    def getName(self):
        return "ops", ("Constant[float](%s)" % self.defvalue)
        
    def __repr__(self):
        return ".".join(self.getName())                 

Constant[float] = Constant_float

class Product(IFunction[float]):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return "(%(lhs)s * %(rhs)s)" % self.__dict__