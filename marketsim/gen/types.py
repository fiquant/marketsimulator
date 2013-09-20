
class Positive(object):
    
    def __init__(self, defvalue):
        self.defvalue = defvalue
        
    @property
    def constraint(self):
        return "types.positive"
    
    def __repr__(self):
        return "types.positive(%s)" % self.defvalue

class NonNegative(object):
    
    def __init__(self, defvalue):
        self.defvalue = defvalue
        
    @property
    def constraint(self):
        return "types.non_negative"
    
    def __repr__(self):
        return "types.non_negative(%s)" % self.defvalue
        
positive = Positive
non_negative = NonNegative
