from marketsim.ops._all import Observable

class _Negate_Impl(Observable[float]):

    def __call__(self):
        x = self.x()
        return -x if x is not None else None

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

class _Conditional_Base(Observable[bool]):

    def __call__(self):
        x = self.x()
        y = self.y()
        return self.apply(x, y)

    def __getitem__(self, (ifpart, elsepart)):
        from marketsim.gen._out.ops._Condition_Float import Condition_Float
        from marketsim.gen._out.ops._Condition_Side import Condition_Side
        T = Condition_Float if ifpart.T == float or elsepart.T == float else Condition_Side
        return T(self, ifpart, elsepart)

class _Equal_Impl(_Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x == y

class _NotEqual_Impl(_Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x != y

class _Less_Impl(_Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x < y

class _Greater_Impl(_Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x > y

class _LessEqual_Impl(_Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x <= y

class _GreaterEqual_Impl(_Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x >= y
