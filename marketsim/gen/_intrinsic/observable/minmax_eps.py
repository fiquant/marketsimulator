from marketsim import bind, context, types, event, _, ops, registry

class Base(object):
    """ Observable that fires if underlying source value becomes greater previous maximum plus some epsilon
    """

    def __init__(self):
        self.my_fire = self.fire
        self.fire = bind.Method(self, "_dummy")
        self.value = None

    def _subscribe(self):
        self.value = self.source()
        self._handler = _(self)._fire_
        if self.value is not None:
            self._handler = self._predicate(self.value + self._sign*self.epsilon(), self._handler)
        self.source += self._handler

    def bind(self, ctx):
        self._subscribe()

    def __call__(self):
        return self.value

    def _dummy(self, dummy): pass

    def _fire_(self, dummy):
        if self.source() is not None:
            self.source -= self._handler
            self._subscribe()
            self.my_fire(dummy)

    @property
    def label(self):
        return self._label + "^{" + self.source.label + "}_{\epsilon}"

    @property
    def attributes(self):
        return {}


class MaxEpsilon_Impl(Base):
    """ Observable that fires if underlying source value becomes greater previous maximum plus some epsilon
    """
    _sign = +1
    _predicate = event.GreaterThan
    _label = "Max"

class MinEpsilon_Impl(Base):
    """ Observable that fires if underlying source value becomes less than previous minimum minus some epsilon
    """

    _sign = -1
    _predicate = event.LessThan
    _label = "Min"


