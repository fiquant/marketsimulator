import random
import math
import inspect
from marketsim import registry
from marketsim.types import *

template = """
class %(name)s(object):    

    def __init__(self, %(init)s):
        self.__dict__ = { %(dict_)s }
        
    _properties = { %(props)s }
    _types = [function((), %(rvtype)s)]
    
    def __call__(self, *args, **kwargs):
        return random.%(name)s(%(call)s)
    
    def __repr__(self):
        rv = "%(name)s"
        rv += "("
        for k in self.__dict__:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"
"""
    
def wrapper(name, fields, rvtype='float'):
    def process(tmpl):
        return ",".join([tmpl % locals() for (name, ini, typ) in fields])
    
    init = process("%(name)s = %(ini)s")
    dict_= process("\'%(name)s\' : %(name)s")
    props= process("\'%(name)s\' : %(typ)s")
    call = process("self.%(name)s")
    
    return template % locals()

exec wrapper('expovariate', 
             [('Lambda', '1.', 'positive')])

exec wrapper('randint', 
             [('Low',  '-10', 'int'), 
              ('High', '+10', 'int')],
             rvtype = 'int')

exec wrapper('uniform', 
             [('Low',  '-10.', 'float'), 
              ('High', '+10.', 'float')])

exec wrapper('triangular', 
             [('Low',  '0.', 'float'), 
              ('High', '1.', 'float'), 
              ('Mode', '0.5', 'float')])

exec wrapper('betavariate', 
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])

exec wrapper('gammavariate', 
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])

exec wrapper('gauss', 
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'float')])

exec wrapper('lognormvariate', 
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'positive')])

exec wrapper('normalvariate', 
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'float')])

exec wrapper('vonmisesvariate', 
             [('Mu', '0.', 'less_than(2*math.pi, non_negative)'), 
              ('Kappa', '0.', 'non_negative')])

exec wrapper('paretovariate', 
             [('Alpha', '1.', 'positive')])

exec wrapper('weibullvariate', 
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])
