from marketsim import _, ops, event

from basic import Strategy
from marketsim.gen._out._constant import constant

class ChooseTheBest_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        self._current = None
        self._estimators = []
        for s in self.strategies:
            event.subscribe(s.on_order_created, _(self).send, self)
            e = self.performance(self.account(s))
            e._origin = s
            self._estimators.append(e)
        event.subscribe(event.Every(constant(1.)), _(self)._wakeUp, self)
            
    _internals = ['_estimators']

    def send(self, order, origin):
        if origin == self._current:
            self._send(order)
            
    def _wakeUp(self, _):
        best = -10e38
        self._current = None
        for estimator in self._estimators:
            e = estimator()
            if e is not None and e > best:
                best = e
                self._current = estimator._origin
