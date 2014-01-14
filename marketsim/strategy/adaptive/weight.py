from marketsim import event, _, meta, types, registry, ops, observable
from _virtual_market import VirtualMarket
from _account import Account

from marketsim.gen._out.strategy.weight._.f._f_AtanPow import f_AtanPow as atanpow
from marketsim.gen._out.strategy.weight._.f._f_Clamp0 import f_Clamp0 as clamp0
from marketsim.gen._out.strategy.weight._.f._f_IdentityF import f_IdentityF as identityF

def identity(x):
    return x

Ts = [float, meta.listOf(float), types.IFunction[float]]
identity._types = [meta.function((t,), t) for t in Ts]

registry.expose(alias=['identity'])(identity)

def cachedattr(obj, name, setter):
    if not hasattr(obj, name):
        setattr(obj, name, setter())
        
    return getattr(obj, name)

from marketsim.gen._out.strategy.weight._.trader._trader_Efficiency import trader_Efficiency as efficiency
from marketsim.gen._out.strategy.weight._.trader._trader_EfficiencyTrend import trader_EfficiencyTrend as efficiencyTrend

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

from marketsim.gen._out.strategy.weight._.trader._trader_Score import trader_Score as score
from marketsim.gen._out.strategy.weight._.trader._trader_Unit import trader_Unit as unit
