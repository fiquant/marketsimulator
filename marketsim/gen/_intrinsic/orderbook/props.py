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

class _BestPrice_Impl(Proxy):

    @property
    def _impl(self):
        return self.queue.bestPrice

