
def convert(other):
    from _all import constant
    if type(other) in [int, float]:
        other = constant(other)
    return other


class Function_impl(object):

    def __add__(self, other):
        from _arithmetic import Sum
        return Sum(self, convert(other))

    def __sub__(self, other):
        from _arithmetic import Sub
        return Sub(self, convert(other))

    def __mul__(self, other):
        from _arithmetic import Product
        return Product(self, convert(other))

    def __div__(self, other):
        from _arithmetic import Div
        return Div(self, convert(other))

    def __lt__(self, other):
        from _all import less
        return less(self, convert(other))

    def __gt__(self, other):
        from _all import greater
        return greater(self, convert(other))

    def __ge__(self, other):
        from _all import greater_equal
        return greater_equal(self, convert(other))

    def __eq__(self, other):
        from _all import equal
        return equal(self, convert(other))

    def __ne__(self, other):
        from _all import notequal
        return notequal(self, convert(other))

from marketsim import types
import marketsim

Function = types.Factory("Function", """(Function_impl, types.IFunction[%(T)s]):
    T = %(T)s
""", globals())
