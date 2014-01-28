
def convert(other):
    from marketsim.gen._out._constant import constant
    if type(other) in [int, float]:
        other = constant(other)
    return other


class Function_impl(object):

    def __add__(self, other):
        from marketsim.gen._out.ops._Add import Add
        return Add(self, convert(other))

    def __sub__(self, other):
        from marketsim.gen._out.ops._Sub import Sub
        return Sub(self, convert(other))

    def __mul__(self, other):
        from marketsim.gen._out.ops._Mul import Mul
        return Mul(self, convert(other))

    def __div__(self, other):
        from marketsim.gen._out.ops._Div import Div
        return Div(self, convert(other))

    def __lt__(self, other):
        from marketsim.gen._out.ops._Less import Less
        return Less(self, convert(other))

    def __gt__(self, other):
        from marketsim.gen._out.ops._Greater import Greater
        return Greater(self, convert(other))

    def __ge__(self, other):
        from marketsim.gen._out.ops._GreaterEqual import GreaterEqual
        return GreaterEqual(self, convert(other))

    def __eq__(self, other):
        from marketsim.gen._out.ops._Equal import Equal
        return Equal(self, convert(other))

    def __ne__(self, other):
        from marketsim.gen._out.ops._NotEqual import NotEqual
        return NotEqual(self, convert(other))

from marketsim import types
import marketsim

Function = types.Factory("Function", """(Function_impl, types.IFunction[%(T)s]):
    T = %(T)s
""", globals())
