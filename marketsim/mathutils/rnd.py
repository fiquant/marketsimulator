import random
import math
import inspect
from marketsim import registry
from marketsim.types import *

template = """
class %(name)s(object):    

    def __init__(self, %(init)s):
        self.__dict__ = { %(dict_)s }
        
    def reset(self):
        pass
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { %(props)s }
    _types = [function((), %(rvtype)s)]
    
    def _casts_to(self, dst):
        return %(name)s._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.%(name)s(%(call)s)
    
    def __repr__(self):
        rv = "%(name)s"
        rv += "("
        for k in %(name)s._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"
        
registry.insert(%(name)s(), '%(alias)s')
"""
    
def wrapper(name, alias, fields, rvtype='float'):
    def process(tmpl):
        return ",".join([tmpl % locals() for (name, ini, typ) in fields])
    
    init = process("%(name)s = %(ini)s")
    dict_= process("\'%(name)s\' : %(name)s")
    props= process("\'%(name)s\' : %(typ)s")
    call = process("self.%(name)s")
    
    return template % locals()

exec wrapper('expovariate', "Exponential distribution",
             [('Lambda', '1.', 'positive')],
             'float')

exec wrapper('randint', "Uniform integer distribution",
             [('Low',  '-10', 'int'), 
              ('High', '+10', 'int')],
             'int')

exec wrapper('uniform', "Uniform distribution",
             [('Low',  '-10.', 'float'), 
              ('High', '+10.', 'float')])

exec wrapper('triangular', "Triangular distribution",
             [('Low',  '0.', 'float'), 
              ('High', '1.', 'float'), 
              ('Mode', '0.5', 'float')])

exec wrapper('betavariate', "Beta distribution",
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])

exec wrapper('gammavariate',"Gamma distribution", 
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])

exec wrapper('gauss', "Gaussian distribution",
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'float')])

exec wrapper('lognormvariate', "Log normal distribution",
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'positive')])

exec wrapper('normalvariate', "Normal distribution",
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'float')])

exec wrapper('vonmisesvariate', "Von Mises distribution",
             [('Mu', '0.', 'less_than(2*math.pi, non_negative)'), 
              ('Kappa', '0.', 'non_negative')])

exec wrapper('paretovariate', "Pareto distribution",
             [('Alpha', '1.', 'positive')])

exec wrapper('weibullvariate', "Weibull distribution",
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])
