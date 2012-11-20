from marketsim import trader, order, scheduler, observable
from copy import copy

from _basic import Strategy

def createVirtual(constructor, kwargs):
    orderBook = kwargs['trader'].orderBook
    # to do something with labels
    kwargs['trader'] = trader.SASM(orderBook)
    kwargs['volumeDistr'] = lambda: 1
    kwargs['orderFactory'] = order.VirtualMarket.T 
    return constructor(*[], **kwargs)

trend = observable.trend

def withEstimator(constructor, *args, **kwargs): 
    assert len(args) == 0, "positional arguments are not supported"
    efficiencyFunc = kwargs['efficiencyFunc'] if 'efficiencyFunc' in kwargs \
                else lambda trader: trend(observable.Efficiency(trader)) 
    real = constructor(*args, **kwargs)
    real.estimator = createVirtual(constructor, copy(kwargs))
    real.efficiency = efficiencyFunc(real.estimator.trader)
    return real

def suspendIfNotEffective(strategy):    
    strategy.efficiency.on_changed += \
        lambda _: strategy.suspend(strategy.efficiency.value < 0)
    return strategy

class chooseTheBest(Strategy):

    def __init__(self, strategies, event_gen=None):
        assert all(map(lambda s: s.trader == strategies[0].trader, strategies))
        if event_gen is None:
            event_gen = scheduler.Timer(lambda: 1)
        Strategy.__init__(self, strategies[0].trader)
        self._strategies = strategies
        event_gen.advise(self._chooseTheBest)

    def _chooseTheBest(self, _):
        best = -10e38        
        for s in self._strategies:
            if s.efficiency.value > best:
                best = s.efficiency.value
        for s in self._strategies:
            s.suspend(best != s.efficiency.value)

    
    def suspend(self, s):
        Strategy.suspend(self, s)
        if not s:
            self._chooseTheBest(None)
        else:
            for s in self._strategies:
                s.suspend(True)