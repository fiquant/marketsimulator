from marketsim import (trader, order, orderbook, scheduler, observable, order, 
                       registry, types, meta, bind, mathutils, event)
from marketsim.types import *

from _basic import Strategy
from _wrap import wrapper2
from _fv import FundamentalValue

import numpy, random, bisect

from _trade_if_profitable import efficiencyTrend, virtualWithUnitVolume

class _MultiarmedBandit_Impl(Strategy):
    
    def _choose_impl(self,_):
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
                
    def __init__(self):

        Strategy.__init__(self) # TODO: eventGen should be a parameter
        self._eventGen = scheduler.Timer(mathutils.constant(1))

        def _createInstance(sp):
            estimator_strategy = self.estimator(sp)
            estimator = trader.SASM(orderbook.OfTrader(trader.SASM_ParentProxy()),estimator_strategy)
            efficiency = self.efficiency(estimator)
            
            return (sp, estimator, estimator_strategy, efficiency)
        
        self._strategies = [_createInstance(sp) for sp in self.strategies]
        
        self._choose = bind.Method(self, '_choose_impl')
        self._strategyWeights = self.weight( self._strategies )
        self._current = None
        # what is the data source for weight update?
        event.subscribe(self._eventGen, self._choose, self)
        
        # suspend all strategies
        for (s, _, _, _) in self._strategies:
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

class StrategyWeight(object):
    def __init__(self, strategies):
        self._strategies = strategies
        self._weights = self.zeros()
        
    def __call__(self):
        return self.update()
    
    def zeros(self):
        return [ 0 for _ in xrange(0,len(self._strategies))]
    
    def ones(self):
        return [ 1 for _ in xrange(0,len(self._strategies))]
    
    def update(self):
        self._weights = self.getWeights()
        return self._weights
       
class EfficiencyStrategyWeight(StrategyWeight):
    def __init__(self, strategies):
        StrategyWeight.__init__(self, strategies)
        
    def getWeights(self):
        return [ max( s[3](), 0) for s in self._strategies]
    
class EfficiencyAlpha(EfficiencyStrategyWeight):
    
    def __init__(self, strategies, alpha=0.5):
        EfficiencyStrategyWeight.__init__(self, strategies)
        self.alpha = alpha

    def getWeights(self):
        old = self._weights
        new = super(EfficiencyAlpha, self).getWeights()
        return [ self.alpha*x + (1-self.alpha)*y for x,y in zip(old, new)]
    
class TrackRecordWeight(EfficiencyStrategyWeight):
    
    def __init__(self, strategies):
        EfficiencyStrategyWeight.__init__(self, strategies)
        
    def getWeights(self):
        new = super(TrackRecordWeight, self).getWeights()
        return [ x + (y>0) for x,y in zip(self._weights, new)]
    
class ChooseTheBestWeight(EfficiencyStrategyWeight):
    
    def __init__(self, strategies):
        EfficiencyStrategyWeight.__init__(self, strategies)
    
    def getWeights(self):
        w = super(ChooseTheBestWeight, self).getWeights()
        mw = max(w)
        # index of the strategy with the highest (positive) efficiency
        max_idx = w.index(mw)
        weights = self.zeros()
        
        if mw > 0:
            weights[max_idx] = 1
        
        return weights
    
class UniformWeight(StrategyWeight):
    
    def __init__(self, strategies):
        StrategyWeight.__init__(self, strategies)
        self._weights = self.ones()
    
    def getWeights(self):
        return self._weights

            
exec wrapper2("MultiarmedBandit",
             """ A composite strategy initialized with an array of strategies. 
                 In some moments of time the most effective strategy 
                 is chosen and made running; other strategies are suspended.
                 The choice is made randomly among the strategies that have
                 a positive efficiency trend, weighted by the efficiency value.
                 
                 Parameters: 
                 
                     |weight|
                         weighing scheme for choosing strategies
                
                     |strategies| 
                        original strategies that can be suspended
                     
                     |efficiency| 
                         function estimating is the strategy efficient or not
                     
                     |estimator| 
                        function creating phantom strategy used for efficiency estimation
                 
                 """,
             [('strategies',  '[FundamentalValue()]',   'meta.listOf(ISingleAssetStrategy)'),
              ('weight',      'TrackRecordWeight',      'StrategyWeight'),
              ('efficiency',  'efficiencyTrend',        'ISingleAssetTrader -> ISingleAssetTrader'),
              ('estimator',   'virtualWithUnitVolume',  'ISingleAssetStrategy -> ISingleAssetStrategy')], category="Adaptive")