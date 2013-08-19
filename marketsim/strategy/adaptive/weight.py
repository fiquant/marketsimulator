from marketsim import meta, types, registry, ops, observable

class Base(object):

    def bind(self, context):
        self._strategies = context.strategies
        self._weights = self.zeros()
        
    def __call__(self):
        return self.update()
    
    def zeros(self):
        return [ 0 for _ in xrange(0, len(self._strategies))]
    
    def ones(self):
        return [ 1 for _ in xrange(0, len(self._strategies))]
    
    def update(self):
        self._weights = self.getWeights()
        return self._weights

@registry.expose(['Efficiency'])       
class Efficiency(Base):
        
    def getWeights(self):
        return [ max(s[3](), 0) for s in self._strategies]
    
from _trade_if_profitable import efficiencyTrend2

@meta.sig(args=(types.IAccount,), rv=types.IFunction[float])
def efficiency(trader):
    if not hasattr(trader, '_efficiencyNormalized'):
        trader._efficiencyNormalized = \
            ops.Atan(
                ops.Pow(
                    ops.constant(1.002), 
                    efficiencyTrend2(trader)))

    return trader._efficiencyNormalized


    
@registry.expose(['Efficiency alpha'])       
class EfficiencyAlpha(Efficiency):
    
    def __init__(self, alpha=0.5):
        self.alpha = alpha
        
    _properties = { 'alpha' : types.less_than(1., types.non_negative) }

    def getWeights(self):
        old = self._weights
        new = super(EfficiencyAlpha, self).getWeights()
        return [ self.alpha * x + (1 - self.alpha) * y for x, y in zip(old, new)]
    
@registry.expose(['Track record'])       
class TrackRecord(Efficiency):
    
    def getWeights(self):
        new = super(TrackRecord, self).getWeights()
        return [ x + (y > 0) for x, y in zip(self._weights, new)]
    
@registry.expose(['Choose the best'])       
class ChooseTheBest(Efficiency):
    
    def getWeights(self):
        w = super(ChooseTheBest, self).getWeights()
        mw = max(w)
        # index of the strategy with the highest (positive) efficiency
        max_idx = w.index(mw)
        weights = self.zeros()
        
        if mw > 0:
            weights[max_idx] = 1
        
        return weights
    
@registry.expose(['Uniform'])       
class Uniform(Base):
    
    def bind(self, context):
        self._weights = self.ones()
    
    def getWeights(self):
        return self._weights

@meta.sig(args=(types.IAccount,), rv=types.IFunction[float])
def unit(trader):
    return ops.constant(1.)

