import marketsim
from marketsim.meta import *

class Factory(object):
    
    def __init__(self, name, tmpl, g = None):
        self._types = {}
        self._name = name
        self._tmpl = tmpl
        self._globals = globals() if g is None else g
        
    def __setitem__(self, key, obj):
        assert key not in self._types
        self._types[key] = obj
        
    def override(self, key, obj):
        self._types[key] = obj

    def __getitem__(self, key):
        if key not in self._types:
            #print key
            def correct(key):
                if key.__name__ in self._globals:
                    M = ""
                else:
                    M = key.__module__ + '.' if key.__module__ not in ['__builtin__'] else ''
                N = key.__name__
                return M + N, N
            if type(key) is not tuple:
                T,N = correct(key)
                R = ""
            else:
                T,N = correct(key[0])
                R = ""
                for e in key[1:]:
                    t, n = correct(e)
                    N += '_' + n
                    if R != "": R += ','
                    R += t
                if len(key) == 2:
                    R += ","
            tmp= "class " + self._name + '_' + N + \
                 self._tmpl % {'T': T, 'R' : R, 'Name' : self._name} +\
                 "pass"
            #print tmp
            exec tmp in self._globals
            self._types[key] = eval(self._name + '_' + N, self._globals)
        return self._types[key]

def convert(other):
    from marketsim.gen._out._const import const
    if type(other) in [int, float]:
        other = const(other)
    return other


class Function_impl(object):

    def __add__(self, other):
        from marketsim.gen._out.ops._add import Add
        return Add(self, convert(other))

    def __sub__(self, other):
        from marketsim.gen._out.ops._sub import Sub
        return Sub(self, convert(other))

    def __mul__(self, other):
        from marketsim.gen._out.ops._mul import Mul
        return Mul(self, convert(other))

    def __div__(self, other):
        from marketsim.gen._out.ops._div import Div
        return Div(self, convert(other))

    def __lt__(self, other):
        from marketsim.gen._out.ops._less import Less
        return Less(self, convert(other))

    def __gt__(self, other):
        from marketsim.gen._out.ops._greater import Greater
        return Greater(self, convert(other))

    def __ge__(self, other):
        from marketsim.gen._out.ops._greaterequal import GreaterEqual
        return GreaterEqual(self, convert(other))

    def __eq__(self, other):
        from marketsim.gen._out.ops._equal import Equal
        return Equal(self, convert(other))

    def __ne__(self, other):
        from marketsim.gen._out.ops._notequal import NotEqual
        return NotEqual(self, convert(other))

