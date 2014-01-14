from marketsim import (trader, order, orderbook, observable, order, 
                       registry, types, meta, _, ops, event)

from .._basic import Strategy
from .._wrap import wrapper2

from .. import v0

from _virtual_market import virtualMarket
import weight

class _ChooseTheBest_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        self._current = None
        self._estimators = []
        for s in self.strategies:
            event.subscribe(s.on_order_created, _(self).send, self)
            e = self.performance(self.account(s))
            e._origin = s
            self._estimators.append(e)
        event.subscribe(event.Every(ops.constant(1.)), _(self)._wakeUp, self)
            
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

exec wrapper2("ChooseTheBest",
             """ A composite strategy initialized with an array of strategies. 
                 In some moments of time the most effective strategy 
                 is chosen and made running; other strategies are suspended.
                 
                 Parameters: 
                
                     |strategies| 
                        original strategies that can be suspended
                     
                     |efficiency| 
                         function estimating is the strategy efficient or not
                 """,
             [
              ('strategies',  '[v0.FundamentalValue()]',  'meta.listOf(types.ISingleAssetStrategy)'),
              ('account',     'virtualMarket()',            'types.ISingleAssetStrategy -> types.IAccount'),
              ('performance', 'weight.efficiencyTrend',   'types.IAccount -> types.IFunction[float]'),
             ], category="Adaptive")
