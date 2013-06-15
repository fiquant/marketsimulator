class Base(object):
    def __init__(self, strategies):
        self._strategies = strategies
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
       
class Efficiency(Base):
    def __init__(self, strategies):
        Base.__init__(self, strategies)
        
    def getWeights(self):
        return [ max(s[3](), 0) for s in self._strategies]
    
class EfficiencyAlpha(Efficiency):
    
    def __init__(self, strategies, alpha=0.5):
        Efficiency.__init__(self, strategies)
        self.alpha = alpha

    def getWeights(self):
        old = self._weights
        new = super(EfficiencyAlpha, self).getWeights()
        return [ self.alpha * x + (1 - self.alpha) * y for x, y in zip(old, new)]
    
class TrackRecord(Efficiency):
    
    def __init__(self, strategies):
        Efficiency.__init__(self, strategies)
        
    def getWeights(self):
        new = super(TrackRecord, self).getWeights()
        return [ x + (y > 0) for x, y in zip(self._weights, new)]
    
class ChooseTheBest(Efficiency):
    
    def __init__(self, strategies):
        Efficiency.__init__(self, strategies)
    
    def getWeights(self):
        w = super(ChooseTheBest, self).getWeights()
        mw = max(w)
        # index of the strategy with the highest (positive) efficiency
        max_idx = w.index(mw)
        weights = self.zeros()
        
        if mw > 0:
            weights[max_idx] = 1
        
        return weights
    
class Uniform(Base):
    
    def __init__(self, strategies):
        Base.__init__(self, strategies)
        self._weights = self.ones()
    
    def getWeights(self):
        return self._weights
