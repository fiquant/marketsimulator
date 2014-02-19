class _Negate_Impl(object):

    def __call__(self):
        x = self.x()
        return -x if x is not None else None

class Base(object):

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

from marketsim.gen._out._side import Side

class _Conditional_Base(object):

    def __call__(self):
        x = self.x()
        y = self.y()
        return self.apply(x, y)

    def __getitem__(self, (ifpart, elsepart)):
        from marketsim.gen._out.ops._condition import Condition
        return Condition(self, ifpart, elsepart)

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
