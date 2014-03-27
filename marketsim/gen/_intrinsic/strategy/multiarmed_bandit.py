from marketsim import ( _, ops, event)

from basic import Strategy

import random, bisect
from marketsim.gen._out._constant import constant

from marketsim.gen._out._intrinsic_base.strategy.multiarmed_bandit import MultiarmedBandit2_Base

class MultiarmedBandit2_Impl(Strategy, MultiarmedBandit2_Base):
    
    def __init__(self):
        Strategy.__init__(self)
        self._current = None
        self._estimators = []
        for s in self.strategies:
            event.subscribe(s.on_order_created, _(self).send, self)
            e = self.normalizer(self.weight(self.account(s)))
            e._origin = s
            self._estimators.append(e)
        event.subscribe(event.Every(constant(1.)), _(self)._wakeUp, self)
            
    _internals = ['_estimators']

    def updateContext(self, context):
        context.parentTrader = context.trader
        context.strategies = self.strategies

    def send(self, order, origin):
        if origin == self._current:
            self._send(order)
            
    def _wakeUp(self, _):
        import numpy
        # random weighted selection from the set of efficient strategies
        choices = [s._origin for s in self._estimators]
        def opt(x): return 0 if x is None else x
        weights = [opt(e()) for e in self._estimators]
        weights = self.corrector(weights)()
        cumdist = list(numpy.cumsum(weights))
        
        if cumdist[-1] > 0:
            x = random.random() * cumdist[-1]
            chosen = choices[bisect.bisect(cumdist, x)]
            # activate the chose strategy
            self._current = chosen
        else:
            # none of the strategies is efficient, therefore we prefer not to trade
            self._current = None
