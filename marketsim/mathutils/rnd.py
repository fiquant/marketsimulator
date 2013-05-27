import random
import math
import inspect
from marketsim import registry
from marketsim.types import *

template = """
@registry.expose(['Random', '%(alias)s'])
class %(name)s(object):
    \"\"\" %(docstring)s
    \"\"\"    

    def __init__(self, %(init)s):
        self.__dict__ = { %(dict_)s }
        
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
"""
    
def wrapper(name, alias, docstring, fields, rvtype='float'):
    def process(tmpl):
        return ",".join([tmpl % locals() for (name, ini, typ) in fields])
    
    init = process("%(name)s = %(ini)s")
    dict_= process("\'%(name)s\' : %(name)s")
    props= process("\'%(name)s\' : %(typ)s")
    call = process("self.%(name)s")
    
    return template % locals()

exec wrapper('expovariate', "Exponential distribution",
             "Exponential distribution. |lambda| is 1.0 divided by the desired mean. "
             "It should be greater zero. Returned values range from 0 to positive infinity",
             [('Lambda', '1.', 'positive')],
             'float')

exec wrapper('randint', "Uniform integer distribution",
             "Return a random integer *N* such that *a* <= *N* <= *b*.",
             [('Low',  '-10', 'int'), 
              ('High', '+10', 'int')],
             'int')

exec wrapper('uniform', "Uniform distribution",
             "Return a random floating point number *N* such that *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*."
             "\n"
             "The end-point value *b* may or may not be included in the range depending on floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.",
             [('Low',  '-10.', 'float'), 
              ('High', '+10.', 'float')])

exec wrapper('triangular', "Triangular distribution",
             "Return a random floating point number *N* such that *low* <= *N* <= *high* and "
             "with the specified *mode* between those bounds."
             " The *low* and *high* bounds default to zero and one."
             " The *mode* argument defaults to the midpoint between the bounds,"
             " giving a symmetric distribution.",
             [('Low',  '0.', 'float'), 
              ('High', '1.', 'float'), 
              ('Mode', '0.5', 'float')])

exec wrapper('betavariate', "Beta distribution",
             "Beta distribution. Conditions on the parameters are |alpha| > 0 and |beta| > 0."
             " Returned values range between 0 and 1.",
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])

exec wrapper('gammavariate',"Gamma distribution",
             r"""Gamma distribution. Conditions on the parameters are |alpha| > 0 and |beta| > 0.
             
             The probability distribution function is: ::
             
                         x ** (alpha - 1) * math.exp(-x / beta)
               pdf(x) =  --------------------------------------
                            math.gamma(alpha) * beta ** alpha""",
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])

exec wrapper('lognormvariate', "Log normal distribution",
             "Log normal distribution."
             " If you take the natural logarithm of this distribution, "
             "you'll get a normal distribution with mean |mu| and standard deviation |sigma|. "
             "|mu| can have any value, and |sigma| must be greater than zero.",
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'positive')])

exec wrapper('normalvariate', "Normal distribution",
             "Normal distribution. |mu| is the mean, and |sigma| is the standard deviation.",
             [('Mu', '0.', 'float'), 
              ('Sigma', '1.', 'float')])

exec wrapper('vonmisesvariate', "Von Mises distribution",
             "|mu| is the mean angle, expressed in radians between 0 and 2|pi|, "
             "and |kappa| is the concentration parameter, which must be greater than or equal to zero. "
             "If |kappa| is equal to zero, this distribution reduces "
             "to a uniform random angle over the range 0 to 2|pi|",
             [('Mu', '0.', 'less_than(2*math.pi, non_negative)'), 
              ('Kappa', '0.', 'non_negative')])

exec wrapper('paretovariate', "Pareto distribution",
             "Pareto distribution. |alpha| is the shape parameter.",
             [('Alpha', '1.', 'positive')])

exec wrapper('weibullvariate', "Weibull distribution",
             "Weibull distribution. |alpha| is the scale parameter and |beta| is the shape parameter.",
             [('Alpha', '1.', 'positive'), 
              ('Beta', '1.', 'positive')])
