from marketsim import meta, Side, types, mathutils

class ConstantSide(object):
    """ Constant function always returning given *side*. 
    
    Note: We need it since our type system doesn't support for the moment generic
    Constant: () -> 'a
    """
    
    def __init__(self, side = Side.Sell):
        self.side = side
        self._alias = ['Constant side']
        
    _properties = { 'side' : Side }
    _types = [ meta.function((), Side) ]
        
    def __call__(self):
        return self.side
    
class Condition_Impl(object):
    
    def __init__(self, cond, ifpart, elsepart):
        self.cond = cond
        self.ifpart = ifpart
        self.elsepart = elsepart
        
    def __call__(self):
        c = self.cond()
        return None if c is None else self.ifpart() if c else self.elsepart()

condition_tmpl = """
class Condition%(T)s(Condition_Impl):

    def __init__(self, cond, ifpart, elsepart):
        Condition_Impl.__init__(self, cond, ifpart, elsepart)
        self._alias = ['Condition[%(T)s]']
        
    _types = [meta.function((), %(T)s)]
        
    _properties = [('cond', meta.function((), bool)), 
                   ('ifpart', meta.function((), %(T)s)), 
                   ('elsepart', meta.function((), %(T)s))]
"""  

for t in ['Side', 'float']:
    exec condition_tmpl % { 'T' : t }   
    
class NotNoneFloat(mathutils.Function[float]):
    
    def __init__(self, source, ifnone):
        self.source = source
        self.ifnone = ifnone
    
    _properties = { 'source' : types.IFunction[float], 
                    'ifnone' : types.IFunction[float]}
        
    def __call__(self):
        v = self.source()
        return v if v is not None else self.ifnone()
    
class less_float(mathutils.Function[float]):
    
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    _types = [meta.function((), bool)]
    
    _properties = [('lhs', types.IFunction[float]), 
                   ('rhs', types.IFunction[float])]
    
    def __call__(self):
        return self.lhs() < self.rhs()
    
class none_side(object):
    
    def __call__(self):
        return None
    
    _types = [meta.function((), Side)]
