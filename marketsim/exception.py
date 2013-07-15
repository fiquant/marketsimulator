class Constraint(Exception):
    
    def __init__(self, constraint, obj):
        self.constraint = constraint
        self.obj = obj
        
    def __str__(self):
        return "Constraint " + repr(self.constraint) + " violated on " + repr(self.obj)
    
