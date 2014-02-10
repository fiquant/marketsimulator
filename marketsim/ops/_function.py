
def convert(other):
    from marketsim.gen._out._constant import constant
    if type(other) in [int, float]:
        other = constant(other)
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

from marketsim import types
import marketsim

Function = types.Factory("Function", """(Function_impl, types.IFunction[%(T)s]):
    T = %(T)s
""", globals())
