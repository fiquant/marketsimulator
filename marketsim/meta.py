import collections, inspect, itertools

def casts_to(src, dst):
    if src == dst: return True
    if dst == float and src == int: return True
    if dst == int and src == bool: return True
    if inspect.isclass(src) and inspect.isclass(dst):
        if issubclass(src, dst):
            return True
    if '_casts_to' in dir(src):
        return src._casts_to(dst)
    return False

from marketsim import rtti, exception

class function(collections.namedtuple("function", ["args", "rv"])):
    
    def _casts_to(self, dst):
        if dst is None:
            return True
        if type(dst) is function:
            for i in range(len(self.args)):
                if i >= len(dst.args):
                    return False
                if not(casts_to(dst.args[i], self.args[i])):
                    return False
            return casts_to(self.rv, dst.rv)
        return False
    
    def toJS(self):
        def impl(convertToJs):
            return { "args" : [convertToJs(x) for x in self.args], "rv" : convertToJs(self.rv) }
        return impl
    
    def usedTypes(self):
        return itertools.chain(*map(rtti.usedTypes, self.args + (self.rv,)))

    def check_constraint(self, x):
        for e in rtti.types(x):
            if e == self:
                return
        raise exception.Constraint(self, x)
    
class listOf(collections.namedtuple("listOf", ["elementType"])):
    
    def toJS(self):
        def impl(convertToJs):
            return { "elementType" : convertToJs(self.elementType) }
        return impl
    
    def usedTypes(self):
        return rtti.usedTypes(self.elementType)
    
    def check_constraint(self, x):
        if type(x) is list:
            for e in x:
                rtti.typecheck(self.elementType, e)
        else:
            raise exception.Constraint(self, x)
    
def sig(args, rv):
    def inner(f):
        f._types = [function(args, rv)]
        f._casts_to = f._types[0]._casts_to
        return f
    return inner

