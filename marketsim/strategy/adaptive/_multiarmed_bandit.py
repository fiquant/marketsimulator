from marketsim import (trader, order, orderbook, observable, order,
                       registry, types, meta, _, ops, event)
from marketsim.types import *

from .._basic import Strategy
from .._wrap import wrapper2
from .. import v0

import weight
from _virtual_market import virtualMarket

import numpy, random, bisect

class _MultiarmedBandit2_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        self._current = None
        self._estimators = []
        for s in self.strategies:
            event.subscribe(s.on_order_created, _(self).send, self)
            e = self.normalizer(self.weight(self.account(s)))
            e._origin = s
            self._estimators.append(e)
        event.subscribe(event.Every(ops.constant(1.)), _(self)._wakeUp, self)
            
    _internals = ['_estimators']

    def updateContext(self, context):
        context.parentTrader = context.trader
        context.strategies = self.strategies

    def send(self, order, origin):
        if origin == self._current:
            self._send(order)
            
    def _wakeUp(self, _):
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

exec wrapper2("MultiarmedBandit2",
             """ A composite strategy initialized with an array of strategies. 
                 In some moments of time the most effective strategy 
                 is chosen and made running; other strategies are suspended.
                 The choice is made randomly among the strategies that have
                 a positive efficiency trend, weighted by the efficiency value.
                 
                 Parameters: 
                 
                     |weight|
                         weighting scheme for choosing strategies
                
                     |strategies| 
                        original strategies that can be suspended
                     
                     |efficiency| 
                         function estimating is the strategy efficient or not
                     
                     |estimator| 
                        function creating phantom strategy used for efficiency estimation
                 
                 """,
             [
              ('strategies',  '[v0.FundamentalValue()]','meta.listOf(ISingleAssetStrategy)'),
              ('account',     'virtualMarket()',          'types.ISingleAssetStrategy -> types.IAccount'),
              ('weight',      'weight.efficiencyTrend()', 'types.IAccount -> types.IFunction[float]'),
              ('normalizer',  'weight.atanpow()',       'types.IFunction[float] -> types.IFunction[float]'),
              ('corrector',   'weight.identityL()',        'IFunction[listOf(float), listOf(float)]')
             ], category="Adaptive")
