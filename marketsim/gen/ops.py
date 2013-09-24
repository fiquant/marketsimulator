Constant = {}

class Constant_float(object):
    
    def __init__(self, defvalue = 1.):
        self.defvalue = defvalue
        
    def getName(self):
        return "ops", ("Constant[float](%s)" % self.defvalue)
        
    def __repr__(self):
        return ".".join(self.getName())                 

Constant[float] = Constant_float
