from marketsim import trader, order, indicator
from copy import copy

def createVirtual(constructor, kwargs):
    orderBook = kwargs['trader'].orderBook
    # to do something with labels
    kwargs['trader'] = trader.SASM(orderBook)
    kwargs['volumeDistr'] = lambda: 1
    kwargs['orderFactory'] = order.VirtualMarket.T 
    return constructor(*[], **kwargs)

def trend(source, alpha=0.015):
    return indicator.OnEveryDt(1, indicator.dEWMA(source, alpha))

def withEstimator(constructor, *args, **kwargs):
    assert len(args) == 0, "positional arguments are not supported"
    estimator = createVirtual(constructor, copy(kwargs))
    real = constructor(*args, **kwargs)
    real.estimator = estimator 
    return real

def suspendIfNotEffective(strategy):    # todo: parametrize by efficiency criteria
    efficiency = trend(indicator.InstEfficiency(strategy.estimator.trader))
    efficiency.on_changed += lambda _: strategy.suspend(efficiency.value < 0)
    return strategy
