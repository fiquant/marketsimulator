from marketsim import trader, order, scheduler, observable, order, registry, types
from copy import copy
from marketsim.types import *

from _basic import Strategy
from _wrap import wrapper

class _tradeIfProfitable_Impl(Strategy):

    def __init__(self, aTrader, params):
        
        self._strategy = params.strategy.runAt(aTrader)
        self._estimator = trader.SASM(aTrader.orderBook, label = "estimator_"+aTrader.label)
        self._estimator_strategy = params.estimator(params.strategy).runAt(self._estimator) 
                                                         
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

@registry.expose
@sig(args=(SingleAssetTrader,), rv=SingleAssetTrader, label="trader's efficiency trend")
def efficiencyTrend(trader):
    return observable.trend(observable.Efficiency(trader))

@registry.expose
@sig(args=(Strategy,), rv=Strategy, label='Virtual market orders with unit volume')
def virtualWithUnitVolume(strategy):
    return strategy.With(volumeDistr=lambda: 1, orderFactory=order.VirtualMarket.T)    

exec wrapper("tradeIfProfitable", 
             [('strategy',   'None',                  'None'), 
              ('efficiency', 'efficiencyTrend',       'SingleAssetTrader -> SingleAssetTrader'),
              ('estimator',  'virtualWithUnitVolume', 'Strategy -> Strategy')])

class TradeIfProfitable(tradeIfProfitable):
    
    def __init__(self, strategy, 
                 efficiency=efficiencyTrend, 
                 estimator=virtualWithUnitVolume, 
                 **kwargs):
        tradeIfProfitable.__init__(self, strategy.With(**kwargs), efficiency, estimator)
        self._constructAs = 'marketsim.strategy.TradeIfProfitable'
    
    def With(self, 
             strategy = None, 
             efficiency = None,
             estimator = None,
             **kwargs):
        
        if strategy is None: strategy = self.strategy
        
        # TODO: we should also make _properties as union of all members _properties
        # during this union we should also check that there is no conflicts
        # With method should be implemented as walk over _properties
        # but there is no clear answer about what shall we do in case of chooseTheBest 
        # OR: we may consider these classes as decorators to exisiting strategies and believe
        # that parameters are passed to strategies not to 'efficiency' or 'estimator'
        # if someone wants to change 'efficiency' or 'estimator' parameters he should do it explicitly 
        return tradeIfProfitable.With(self, strategy.With(**kwargs), efficiency, estimator)
        
        
        
class _chooseTheBest_Impl(Strategy):
    
    def __init__(self, aTrader, params):
        
        def _createInstance(sp):
            strategy = sp.runAt(aTrader)
            estimator = trader.SASM(aTrader.orderBook, label = "estimator_"+aTrader.label)
            estimator_strategy = params.estimator(sp).runAt(estimator)
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

exec wrapper("chooseTheBest",
             [('strategies',  '[]',                     'None'),
              ('efficiency',  'efficiencyTrend',        'None'),
              ('estimator',   'virtualWithUnitVolume',  'None')])