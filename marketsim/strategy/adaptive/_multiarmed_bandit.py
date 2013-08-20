from marketsim import (trader, order, orderbook, scheduler, observable, order,
                       registry, types, meta, _, ops, event)
from marketsim.types import *

from .._basic import Strategy
from .._wrap import wrapper2
from .. import v0

import weight

import numpy, random, bisect

from _trade_if_profitable import efficiencyTrend, virtualWithUnitVolume
from _trade_if_profitable import efficiencyTrend2


class _MultiarmedBandit2_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        self._current = None
        self._estimators = []
        for s in self.strategies:
            event.subscribe(s.on_order_created, _(self).send, self)
            e = self.evaluator(s)
            e._origin = s
            self._estimators.append(e)
        event.subscribe(scheduler.Timer(ops.constant(1.)), _(self)._wakeUp, self)
            
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
        weights = self.weightCorrection(weights)
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
              ('weight',     'weight.TrackRecord()',  'weight.Base'),
              ('evaluator',   'weight.score',     'ISingleAssetStrategy -> IFunction[float]'),
              ('weightCorrection', 'weight.no', 'listOf(float) -> listOf(float)')
             ], category="Adaptive")


class _MultiarmedBandit_Impl(Strategy):
    
    def _choose(self, _):
        if not self.suspended:
            
            # suspend current strategy
            if self._current:
                self._current.suspend(True)
            
            # random weighted selection from the set of efficient strategies
            choices = [s[0] for s in self._strategies]
            cumdist = list(numpy.cumsum(self.weights))
            
            if cumdist[-1] > 0:
                x = random.random() * cumdist[-1]
                chosen = choices[bisect.bisect(cumdist, x)]
                # activate the chose strategy
                chosen.suspend(False)
                self._current = chosen
            else:
                # none of the strategies is efficient, therefore we prefer not to trade
                self._current = None
                
    @property
    def weights(self):
        return self._strategyWeights()
        
    def updateContext(self, context):
        context.parentTrader = context.trader
        context.strategies = self._strategies
                
    def __init__(self):

        Strategy.__init__(self)  # TODO: eventGen should be a parameter
        self._eventGen = scheduler.Timer(ops.constant(1))

        def _createInstance(sp):
            estimator_strategy = self.estimator(sp)
            estimator = trader.SingleAsset(orderbook.OfTrader(trader.ParentProxy()), estimator_strategy)
            efficiency = self.efficiency(estimator)
            
            return (sp, estimator, estimator_strategy, efficiency)
        
        self._strategies = [_createInstance(sp) for sp in self.strategies]
        
        self._strategyWeights = self.weight
        self._current = None
        # what is the data source for weight update?
        event.subscribe(self._eventGen, _(self)._choose, self)
        
        # suspend all strategies
        for (s, d, d, d) in self._strategies:
            s.suspend(True)
            
    
    @property
    def _children_to_visit(self):
        for (strategy, estimator, estimator_strategy, efficiency) in self._strategies:
            yield estimator
            yield strategy
            yield efficiency
            yield estimator_strategy
        
            
    def suspend(self, s=True):
        Strategy.suspend(self, s)
        if self._current:
            self._current.suspend(s)
        for (_, _, estimator_strategy, _) in self._strategies:
            estimator_strategy.suspend(s)
exec wrapper2("MultiarmedBandit",
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
             [('strategies', '[v0.FundamentalValue()]',  'meta.listOf(ISingleAssetStrategy)'),
              ('weight',     'weight.TrackRecord()',  'weight.Base'),
              ('efficiency', 'efficiencyTrend',       'ISingleAssetTrader -> ISingleAssetTrader'),
              ('estimator',  'virtualWithUnitVolume', 'ISingleAssetStrategy -> ISingleAssetStrategy')], category="Adaptive")
