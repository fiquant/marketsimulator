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

IFunction = {}

class IFunction_float(object):
    
    def __init__(self, defvalue = None):
        if defvalue is None:
            import ops
            self.defvalue = ops.Constant[float]()
        else:
            self.defvalue = defvalue

    def __mul__(self, other):
        import ops
        return ops.Product(self, other)
        
    @property
    def constraint(self):
        return "types.IFunction[float]"
    
    def __repr__(self):
        return "types.IFunction[float](%s)" % self.defvalue
    
IFunction[float] = IFunction_float

## {{{ http://code.activestate.com/recipes/576563/ (r1)
def cached_property(f):
    """returns a cached property that is calculated by function f"""
    def get(self):
        try:
            return self._property_cache[f]
        except AttributeError:
            self._property_cache = {}
            x = self._property_cache[f] = f(self)
            return x
        except KeyError:
            x = self._property_cache[f] = f(self)
            return x
        
    return property(get)
