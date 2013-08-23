from marketsim import event, _, meta, types, registry, ops, observable
from _virtual_market import VirtualMarket
from _account import Account

@registry.expose(alias=['AtanPow'])
@meta.sig(args=(types.IFunction[float],), rv=types.IFunction[float])
def atanpow(f, base = 1.002):
    return ops.Atan(ops.Pow(ops.constant(base), f))

@registry.expose(alias=['Clamp0'])
@meta.sig(args=(types.IFunction[float],), rv=types.IFunction[float])
def clamp0(f):
    return ops.Max(f, ops.constant(0)) + 1

def identity(x):
    return x

Ts = [float, meta.listOf(float), types.IFunction[float]]
identity._types = [meta.function((t,), t) for t in Ts]

registry.expose(alias=['identity'])(identity)

def cachedattr(obj, name, setter):
    if not hasattr(obj, name):
        setattr(obj, name, setter())
        
    return getattr(obj, name)

@registry.expose(alias=['Efficiency'])
@meta.sig(args=(types.IAccount,), rv=types.IFunction[float])
def efficiency(trader):
    return cachedattr(trader, '_efficiency', 
                      lambda: observable.Efficiency(trader))

@registry.expose(alias=['Efficiency trend'])
@meta.sig(args=(types.IAccount,), rv=types.IFunction[float])
def efficiencyTrend(trader):
    return cachedattr(trader, '_efficiencyTrend', 
                      lambda: observable.trend(efficiency(trader), alpha=0.015))

@registry.expose(alias=['chooseTheBest '])
@meta.sig(args=(types.listOf(float),), rv=types.listOf(float))
def chooseTheBest(weights):
    mw = max(weights)
    # index of the strategy with the highest (positive) efficiency
    max_idx = weights.index(mw)
    weights = [0] * len(weights)
    
    if mw > 0:
        weights[max_idx] = 1
    
    return weights

class Score(ops.Function[float]):
    
    def __init__(self, trader):
        self.trader = trader
        self._efficiency = observable.Efficiency(trader)
        event.subscribe(
                observable.OnEveryDt(1, self._efficiency),
                 _(self)._update, self)
        self._score = 1
        self._last = 0
        
    _properties = { 'trader' : types.IAccount }
    
    def _update(self, dummy):
        e = self._efficiency()
        if e is not None:
            delta = e - self._last
            if delta > 0: self._score += 1
            if delta < 0 and self._score > 1: self._score -= 1
        
    def __call__(self):
        return self._score

@registry.expose(alias=['Score'])
@meta.sig(args=(types.IAccount,), rv=types.IFunction[float])
def score(trader):
    return cachedattr(trader, '_score', 
                      lambda: Score(trader))

@registry.expose(alias=['Uniform'])
@meta.sig(args=(types.IAccount,), rv=types.IFunction[float])
def unit(trader):
    return ops.constant(1.)