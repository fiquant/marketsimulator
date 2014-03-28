from marketsim.gen._out._intrinsic_base.ops import (Negate_Base, Div_Base, Mul_Base, Add_Base, Sub_Base, Condition_Base,
                                                         Less_Base, LessEqual_Base, Greater_Base,
                                                         GreaterEqual_Base, Equal_Base, NotEqual_Base)

class Negate_Impl(Negate_Base):

    def __call__(self):
        x = self.x()
        return -x if x is not None else None

class Base(object):

    def __call__(self):
        x = self.x()
        y = self.y()
        return self.apply(x,y) if x is not None and y is not None else None


class Div_Impl(Base, Div_Base):

    @staticmethod
    def apply(x, y):
        return  x / y if y != 0.0 else None

class Mul_Impl(Base, Mul_Base):

    @staticmethod
    def apply(x, y):
        return  x * y

class Add_Impl(Base, Add_Base):

    @staticmethod
    def apply(x, y):
        return  x + y

class Sub_Impl(Base, Sub_Base):

    @staticmethod
    def apply(x, y):
        return  x - y

class Condition_Impl(Condition_Base):

    def __call__(self):
        c = self.cond()
        return None if c is None else self.ifpart() if c else self.elsepart()

from marketsim.gen._out._side import Side

class Conditional_Base(object):

    def __call__(self):
        x = self.x()
        y = self.y()
        return self.apply(x, y)

    def __getitem__(self, (ifpart, elsepart)):
        from marketsim.gen._out.ops._condition import Condition
        return Condition(self, ifpart, elsepart)

class Equal_Impl(Conditional_Base, Equal_Base):

    @staticmethod
    def apply(x, y):
        return x == y

class NotEqual_Impl(Conditional_Base, NotEqual_Base):

    @staticmethod
    def apply(x, y):
        return x != y

class Less_Impl(Conditional_Base, Less_Base):

    @staticmethod
    def apply(x, y):
        return x < y

class Greater_Impl(Conditional_Base, Greater_Base):

    @staticmethod
    def apply(x, y):
        return x > y

class LessEqual_Impl(Conditional_Base, LessEqual_Base):

    @staticmethod
    def apply(x, y):
        return x <= y

class GreaterEqual_Impl(Conditional_Base, GreaterEqual_Base):

    @staticmethod
    def apply(x, y):
        return x >= y
