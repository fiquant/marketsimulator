import collections
import inspect

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
    
class listOf(collections.namedtuple("listOf", ["elementType"])):
    
    def toJS(self):
        def impl(convertToJs):
            return { "elementType" : convertToJs(self.elementType) }
        return impl
    
def sig(args, rv):
    def inner(f):
        f._types = [function(args, rv)]
        f._casts_to = f._types[0]._casts_to
        return f
    return inner

