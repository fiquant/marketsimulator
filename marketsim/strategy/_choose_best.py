from marketsim import (trader, order, orderbook, scheduler, observable, order, 
                       registry, types, meta, _, ops, event)
from marketsim.types import *

from _basic import Strategy
from _wrap import wrapper2
from _fv import FundamentalValue

from _trade_if_profitable import efficiencyTrend, virtualWithUnitVolume

class _ChooseTheBest_Impl(Strategy):
    
    def _chooseTheBest(self,_):
        if not self.suspended:
            best = -10e38
            idx = -1
            i = 0
            for (_, _, _, efficiency) in self._strategies:
                if efficiency() > best:
                    best = efficiency()
                    idx = i
                i += 1                  
            if best < 0:
                best = 0
            self._current = None
            i = 0
            for (strategy, _, _, efficiency) in self._strategies:
                strategy.suspend(i != idx)
                if i != idx:
                    self._current = strategy
                i += 1
        
    def updateContext(self, context):
        context.parentTrader = context.trader
                
    def __init__(self):
        
        Strategy.__init__(self) # TODO: eventGen should be a parameter
        self._eventGen = scheduler.Timer(ops.constant(1))

        def _createInstance(sp):
            estimator_strategy = self.estimator(sp)
            estimator = trader.SingleAsset(orderbook.OfTrader(trader.ParentProxy()),estimator_strategy)
            efficiency = self.efficiency(estimator)
            
            return (sp, estimator, estimator_strategy, efficiency)
        
        self._strategies = [_createInstance(sp) for sp in self.strategies]
        
        self._current = None
        event.subscribe(self._eventGen, _(self)._chooseTheBest, self)
    
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
            
exec wrapper2("ChooseTheBest",
             """ A composite strategy initialized with an array of strategies. 
                 In some moments of time the most effective strategy 
                 is chosen and made running; other strategies are suspended.
                 
                 Parameters: 
                
                     |strategies| 
                        original strategies that can be suspended
                     
                     |efficiency| 
                         function estimating is the strategy efficient or not
                     
                     |estimator| 
                        function creating phantom strategy used for efficiency estimation
                 
                 """,
             [('strategies',  '[FundamentalValue()]',   'meta.listOf(ISingleAssetStrategy)'),
              ('efficiency',  'efficiencyTrend',        'ISingleAssetTrader -> ISingleAssetTrader'),
              ('estimator',   'virtualWithUnitVolume',  'ISingleAssetStrategy -> ISingleAssetStrategy')], category="Adaptive")