from marketsim import meta, constraints, types

class _Constant_Impl(types.IObservable[float]):
    """ Constant function returning **value**.
    """

    def __iadd__(self, listener):
        return self

    def __isub__(self, listener):
        return self

    def _casts_to(self, dst):
        if type(dst) is meta.function:
            rv = dst.rv
            return rv is float or\
                (type(rv) is constraints.greater_or_equal and rv._bound <= self.x) or\
                (type(rv) is constraints.greater_than and rv._bound < self.x) or\
                (type(rv) is constraints.less_or_equal and rv._bound >= self.x) or\
                (type(rv) is constraints.less_than and rv._bound > self.x)
        return False

    def __call__(self, *args, **kwargs):
        return self.x

    @property
    def label(self):
        return str(self.x)

class _True_Impl(types.IObservable[bool]):

    def __call__(self):
        return True

class _False_Impl(types.IObservable[bool]):

    def __call__(self):
        return False


class _Null_Impl(types.IObservable[float]):
    """ Constant function returning None.
    """

    def __iadd__(self, listener):
        return self

    def __isub__(self, listener):
        return self

    def __call__(self, *args, **kwargs):
        return None

