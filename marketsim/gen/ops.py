Constant = {}

class Constant_float(object):
    
    def __init__(self, defvalue = 1.):
        self.defvalue = defvalue
        
    def __repr__(self):
        return "ops.Constant[float](%s)" % self.defvalue                 

Constant[float] = Constant_float
