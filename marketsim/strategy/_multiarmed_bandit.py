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
            
            # only choose among strategies with positive efficiency
            eff = [(s[0], s[3]()) for s in self._strategies if s[3]() > 0]
            
            if eff:
                # random weighted selection from the set of efficient strategies
                choices, weights = zip(*eff)
                cumdist = list(numpy.cumsum(weights))
                x = random.random() * cumdist[-1]
                chosen = choices[bisect.bisect(cumdist, x)]
                # activate the chose strategy
                chosen.suspend(False)
                self._current = chosen
            else:
                # none of the strategies is efficient, therefore we prefer not to trade
                self._current = None
        
    def updateContext(self, context):
        context.parentTrader = context.trader
                
    def __init__(self):
        
        self._choose = bind.Method(self, '_choose_impl')
        Strategy.__init__(self) # TODO: eventGen should be a parameter
        self._eventGen = scheduler.Timer(mathutils.constant(1))

        def _createInstance(sp):
            estimator_strategy = self.estimator(sp)
            estimator = trader.SASM(orderbook.OfTrader(trader.SASM_ParentProxy()),estimator_strategy)
            efficiency = self.efficiency(estimator)
            
            return (sp, estimator, estimator_strategy, efficiency)
        
        self._strategies = [_createInstance(sp) for sp in self.strategies]
        
        self._choose = bind.Method(self, '_choose_impl')
        self._current = None
        event.subscribe(self._eventGen, self._choose, self)
    
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
                
                     |strategies| 
                        original strategies that can be suspended
                     
                     |efficiency| 
                         function estimating is the strategy efficient or not
                     
                     |estimator| 
                        function creating phantom strategy used for efficiency estimation
                 
                 """,
             [('strategies',  '[FundamentalValue()]',   'meta.listOf(IStrategy)'),
              ('efficiency',  'efficiencyTrend',        'ISingleAssetTrader -> ISingleAssetTrader'),
              ('estimator',   'virtualWithUnitVolume',  'IStrategy -> IStrategy')], category="Adaptive")