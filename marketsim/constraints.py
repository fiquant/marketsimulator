def tojs(t, x):
    return lambda c: "combine("+t+"(" + str(x._bound) + "), "+c(x._f)+")"

from marketsim import meta

class IConstraint(object):
    
    def check_constraint(self, x):
        try:
            self(x)
        except ValueError, err:
            raise meta.ConstraintException(self, x)

class greater_than(IConstraint):

    def __init__(self, x, f = float):
        self._bound = x
        self._f = f
        
    def toJS(self):
        return tojs("greater", self)
        
    def _casts_to(self, dst):
        return dst is float or\
            (type(dst) is greater_than and dst._bound <= self._bound) or\
            (type(dst) is greater_or_equal and dst._bound <= self._bound)
        
    def __repr__(self):
        return repr(self._f) + " > " + str(self._bound)
    
    def __call__(self, x):
        x = self._f(x)
        if not (x > self._bound):
            raise ValueError, "should be greater than " + str(self._bound)
        return x
    
class less_than(IConstraint):

    def __init__(self, x, f = float):
        self._bound = x
        self._f = f

    def toJS(self):
        return tojs("less", self)
        

    def _casts_to(self, dst):
        return dst is float or\
            (type(dst) is less_than and dst._bound >= self._bound) or\
            (type(dst) is less_or_equal and dst._bound >= self._bound)
        
    def __repr__(self):
        return repr(self._f) + " < " + str(self._bound)
    
    def __call__(self, x):
        x = self._f(x)
        if not (x < self._bound):
            raise ValueError, "should be less than " + str(self._bound)
        return x
    
class greater_or_equal(IConstraint):

    def __init__(self, x, f = float):
        self._bound = x
        self._f = f
    
    def toJS(self):
        return tojs("greater_or_equal", self)
    
    def _casts_to(self, dst):
        return dst is float or\
            (type(dst) is greater_than and dst._bound < self._bound) or\
            (type(dst) is greater_or_equal and dst._bound <= self._bound)

    def __repr__(self):
        return repr(self._f) + " >= " + str(self._bound)
    
    def __call__(self, x):
        x = self._f(x)
        if not (x >= self._bound):
            raise ValueError, "should be greater or equal to " + str(self._bound)
        return x

class less_or_equal(IConstraint):

    def __init__(self, x, f = float):
        self._bound = x
        self._f = f
    
    def toJS(self):
        return tojs("less_or_equal", self)
        
    def _casts_to(self, dst):
        return dst is float or\
            (type(dst) is less_than and dst._bound > self._bound) or\
            (type(dst) is less_or_equal and dst._bound >= self._bound)
        
    def __repr__(self):
        return repr(self._f) + " <= " + str(self._bound)
    
    def __call__(self, x):
        x = self._f(x)
        if not (x <= self._bound):
            raise ValueError, "should be less or equal to " + str(self._bound)
        return x
    
positive = greater_than(0.)
non_negative = greater_or_equal(0.)
 
