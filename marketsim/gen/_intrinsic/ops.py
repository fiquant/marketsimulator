from marketsim.ops._all import Observable

class Base(Observable[float]):

    def __call__(self):
        x = self.x()
        y = self.y()
        return self.apply(x,y) if x is not None and y is not None else None


class _DivImpl(Base):

    @staticmethod
    def apply(x, y):
        return  x / y if y != 0.0 else None

class _MulImpl(Base):

    @staticmethod
    def apply(x, y):
        return  x * y

class _AddImpl(Base):

    @staticmethod
    def apply(x, y):
        return  x + y

class _SubImpl(Base):

    @staticmethod
    def apply(x, y):
        return  x - y
