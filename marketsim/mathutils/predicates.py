class greater_than(object):

    def __init__(self, x, f = float):
        self._bound = x
        self._f = f
        
    def __repr__(self):
        return repr(self._f) + " > " + str(self._bound)
    
    def __call__(self, x):
        x = self._f(x)
        if not (x > self._bound):
            raise ValueError, "should be greater than " + str(self._bound)
        return x
    
class less_than(object):

    def __init__(self, x, f = float):
        self._bound = x
        self._f = f

    def __repr__(self):
        return repr(self._f) + " < " + str(self._bound)
    
    def __call__(self, x):
        x = self._f(x)
        if not (x < self._bound):
            raise ValueError, "should be less than " + str(self._bound)
        return x
    
class greater_or_equal(object):

    def __init__(self, x, f = float):
        self._bound = x
        self._f = f
    
    def __repr__(self):
        return repr(self._f) + " >= " + str(self._bound)
    
    def __call__(self, x):
        x = self._f(x)
        if not (x >= self._bound):
            raise ValueError, "should be greater or equal to " + str(self._bound)
        return x
    
positive = greater_than(0.)
non_negative = greater_or_equal(0.)
 
