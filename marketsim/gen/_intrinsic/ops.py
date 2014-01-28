from marketsim.ops._all import Observable

class Base(Observable[float]):

    def __call__(self):
        x = self.x()
        y = self.y()
        return self.apply(x,y) if x is not None and y is not None else None


class _Div_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x / y if y != 0.0 else None

class _Mul_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x * y

class _Add_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x + y

class _Sub_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x - y

class _Condition_Impl(object):

    def __call__(self):
        c = self.cond()
        return None if c is None else self.ifpart() if c else self.elsepart()

from marketsim import Side

class _ConditionFloat_Impl(_Condition_Impl, Observable[float]): pass
class _ConditionSide_Impl(_Condition_Impl, Observable[Side]): pass