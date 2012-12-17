import random
import inspect
from marketsim import registry

class _Wrapper(object):
    
    def __init__(self, frame, original, label):
        values, constructAs = registry.meta(frame)
        self.__dict__ = values
        self._properties = dict([(k,float) for k in self.__dict__])
        self._constructAs = constructAs        
        self.__original = original
        self.__label = label
    
    def __call__(self, *args, **kwargs):
        return self.__original(self)
    
    def __repr__(self):
        rv = self.__label
        rv += "("
        for k in self.__dict__:
            if k[:2] != "__":
                rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"
    
def expovariate(Lambda=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.expovariate(p.Lambda),
                    "expovariate") 

def randint(A=-10,B=+10):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.randint(p.A, p.B),
                    "randint") 
    
def uniform(A=-10.,B=+10.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.uniform(p.A, p.B),
                    "uniform") 

def triangular(Low=0., High=1., Mode=0.5):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.triangular(p.Low, p.High, p.Mode),
                    "triangular") 

def betavariate(Alpha=1., Beta=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.betavariate(p.Alpha, p.Beta),
                    "betavariate") 
    
def gammavariate(Alpha=1., Beta=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.gammavariate(p.Alpha, p.Beta),
                    "gammavariate") 

def gauss(Mu=0., Sigma=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.gauss(p.Mu, p.Sigma),
                    "gauss") 
    
def lognormvariate(Mu=0., Sigma=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.lognormvariate(p.Mu, p.Sigma),
                    "lognormvariate") 

def normalvariate(Mu=0., Sigma=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.normalvariate(p.Mu, p.Sigma),
                    "normalvariate") 

def vonmisesvariate(Mu=0., Kappa=0.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.vonmisesvariate(p.Mu, p.Kappa),
                    "vonmisesvariate") 

def paretovariate(Alpha=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.paretovariate(p.Alpha),
                    "paretovariate") 

def weibullvariate(Alpha=1., Beta=1.):
    return _Wrapper(inspect.currentframe(), 
                    lambda p: random.weibullvariate(p.Alpha, p.Beta),
                    "weibullvariate")
