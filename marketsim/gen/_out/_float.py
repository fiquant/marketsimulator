class Float(object):
    def gammavariate(self, Beta = None):
        from marketsim.gen._out.math.random._gammavariate import gammavariate
        return gammavariate(self,Beta)
    
    @property
    def constant(self):
        from marketsim.gen._out._constant import constant
        return constant(self)
    
    def OnEveryDt(self, x = None):
        from marketsim.gen._out.observable._oneverydt import OnEveryDt
        return OnEveryDt(self,x)
    
    def normalvariate(self, Sigma = None):
        from marketsim.gen._out.math.random._normalvariate import normalvariate
        return normalvariate(self,Sigma)
    
    @property
    def paretovariate(self):
        from marketsim.gen._out.math.random._paretovariate import paretovariate
        return paretovariate(self)
    
    def triangular(self, High = None,Mode = None):
        from marketsim.gen._out.math.random._triangular import triangular
        return triangular(self,High,Mode)
    
    def vonmisesvariate(self, Kappa = None):
        from marketsim.gen._out.math.random._vonmisesvariate import vonmisesvariate
        return vonmisesvariate(self,Kappa)
    
    def uniform(self, High = None):
        from marketsim.gen._out.math.random._uniform import uniform
        return uniform(self,High)
    
    @property
    def const(self):
        from marketsim.gen._out._const import const
        return const(self)
    
    def weibullvariate(self, Beta = None):
        from marketsim.gen._out.math.random._weibullvariate import weibullvariate
        return weibullvariate(self,Beta)
    
    def RandomWalk(self, deltaDistr = None,intervalDistr = None,name = None):
        from marketsim.gen._out.math._randomwalk import RandomWalk
        return RandomWalk(self,deltaDistr,intervalDistr,name)
    
    @property
    def expovariate(self):
        from marketsim.gen._out.math.random._expovariate import expovariate
        return expovariate(self)
    
    def lognormvariate(self, Sigma = None):
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate
        return lognormvariate(self,Sigma)
    
    def betavariate(self, Beta = None):
        from marketsim.gen._out.math.random._betavariate import betavariate
        return betavariate(self,Beta)
    
    pass
