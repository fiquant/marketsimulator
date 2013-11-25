from marketsim import context, event, ops, registry, types, _

@registry.expose(['Pow/Log', 'sqr'])
class Sqr(ops.Observable[float]):
    """  Square of *x*

    """

    _internals = ['impl']

    def __init__(self, x = None):
        ops.Observable[float].__init__(self)
        self._x = x if x is not None else ops.constant(1.)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)

    def __call__(self):
        return self.impl()

    def bind(self, ctx):
        self._ctx = ctx.clone()

    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx:
            context.bind(self.impl, ctx)

    def getImpl(self):
        return self.x * self.x

    @property
    def label(self):
        return '{%s}^2' % self.x
        # return self.impl.label

    @property
    def attributes(self):
        return {}

    _properties = { 'x' : types.IFunction[float] }

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.reset()


