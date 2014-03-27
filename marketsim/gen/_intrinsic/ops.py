class Negate_Impl(object):

    def __call__(self):
        x = self.x()
        return -x if x is not None else None

class Base(object):

    def __call__(self):
        x = self.x()
        y = self.y()
        return self.apply(x,y) if x is not None and y is not None else None


class Div_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x / y if y != 0.0 else None

class Mul_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x * y

class Add_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x + y

class Sub_Impl(Base):

    @staticmethod
    def apply(x, y):
        return  x - y

class Condition_Impl(object):

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

class Equal_Impl(Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x == y

class NotEqual_Impl(Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x != y

class Less_Impl(Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x < y

class Greater_Impl(Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x > y

class LessEqual_Impl(Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x <= y

class GreaterEqual_Impl(Conditional_Base):

    @staticmethod
    def apply(x, y):
        return x >= y
