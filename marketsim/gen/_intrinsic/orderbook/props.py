from marketsim import types, ops

class Proxy(types.IObservable[float], ops.Function[float]):

    def __iadd__(self, listener):
        self._impl.__iadd__(listener)
        return self

    def __isub__(self, listener):
        self._impl.__isub__(listener)
        return self

    def __call__(self):
        return self._impl.__call__()


    @property
    def _digitsToShow(self):
        return self._impl._digitsToShow

    @property
    def label(self):
        return self._impl.label

    def __repr__(self):
        return self._impl.label

    @property
    def attributes(self):
        return {}

class _BestPrice_Impl(object):

    def bind(self, ctx):
        from marketsim import event, _, context
        event.subscribe(self.queue.bestPrice, _(self).fire, self)
        context.bind(self._subscriptions, ctx)

    @property
    def __call__(self):
        return self.queue.bestPrice


class _TickSize_Impl(object):

    def __call__(self):
        return self.book.tickSize
