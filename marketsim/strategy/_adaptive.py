from marketsim import trader, order, scheduler, observable
from copy import copy

from _basic import Strategy

class _TradeIfProfitable_Impl(Strategy):

    def __init__(self, aTrader, params):
        
        self._strategy = params.strategy._ctor(aTrader, params.strategy)
        self._estimator = trader.SASM(aTrader.orderBook, label = "estimator_"+aTrader.label)
        self._estimator_strategy = params.strategy._ctor(self._estimator, 
                                                         params.estimator(params.strategy))
        self._efficiency = params.efficiency(self._estimator)
        
        self._efficiency.on_changed += \
            lambda _: self.suspend(self._efficiency.value < 0)
        
        Strategy.__init__(self, aTrader)
        
    def dispose(self):
        self._strategy.dispose()
        self._estimator_strategy.dispose()
        
    def suspend(self, s):
        self._strategy.suspend(s)
        
    @property
    def suspended(self):
        return self._strategy.suspended
        
class _ChooseTheBest_Impl(Strategy):
    
    def __init__(self, aTrader, params):
        
        def _createInstance(sp):
            strategy = sp._ctor(aTrader, sp)
            estimator = trader.SASM(aTrader.orderBook, label = "estimator_"+aTrader.label)
            estimator_strategy = sp._ctor(estimator, params.estimator(sp))
            efficiency = params.efficiency(estimator)
            return (strategy, estimator, estimator_strategy, efficiency)
        
        self._strategies = [_createInstance(sp) for sp in params.strategies]
        
        self._eventGen = scheduler.Timer(intervalFunc=lambda:1)
        
        self._eventGen.advise(self._chooseTheBest)
        self._current = None
            
        Strategy.__init__(self, aTrader)

    def _chooseTheBest(self,_):
        best = -10e38
        for (_, _, _, efficiency) in self._strategies:
            if efficiency.value > best:
                best = efficiency.value                   
        if best < 0:
            best = 0
        self._current = None
        for (strategy, _, _, efficiency) in self._strategies:
            strategy.suspend(efficiency.value != best)
            if efficiency.value != best:
                self._current = strategy
        
    def dispose(self):
        self._eventGen.unadvise(self._chooseTheBest)
        for (strategy, _, estimator_strategy, _) in self._strategies:
            strategy.dispose()
            estimator_strategy.dispose()
            
    def suspend(self, s):
        if self._current:
            self._current.suspend(s)
            
    @property
    def suspended(self):
        return not self._current or self._current.suspended

