import sys, os

import types
from types import *

from templet import stringfunction
from werkzeug.utils import cached_property

class RandomImpl:
    
    def __init__(self, cls, alias, rvtype=float):
 
        self.alias = alias
        self.rvtype = rvtype.__name__
        self.name = cls.__name__
        self.docstring = cls.__doc__
        self.fields = []
        
        for n in dir(cls):
            if n[0:2] != '__':
                v = getattr(cls, n)
                constraint = getattr(v, "constraint", None)
                if constraint is not None:
                    self.fields.append((n, v.defvalue, constraint))
                else:
                    if type(v) in [float, int]:
                        self.fields.append((n, v, type(v).__name__))
                    else:
                        assert False, "unsupported type"

    @cached_property
    @stringfunction
    def header(self):
        """
        @registry.expose(['Random', '${self.alias}'])
        class ${self.name}(ops.Function[${self.rvtype}]):
        """

    @cached_property
    @stringfunction
    def doc(self):
        """
        ${{}}
            \"\"\" ${self.docstring}
            \"\"\"    
        """
        
    @cached_property
    def initfields(self):
        return self.joinfields("%(name)s = %(ini)s")
    
    @cached_property
    def assignfields(self):
        return self.joinfields("self.%(name)s = %(typ)s(%(name)s)", nl + 2*tab)
        
    @cached_property
    @stringfunction
    def init(self):
        """
        ${{}}

            def __init__(self, ${self.initfields}):
                ${self.assignfields}
        """
      
    @cached_property
    @stringfunction
    def label(self):
        """
        ${{}}

            @property
            def label(self):
                return repr(self)
        """
      
        
    @cached_property
    def propfields(self):
        return self.joinfields("\'%(name)s\' : %(typ)s", comma + nl + 2*tab)
        
    @cached_property
    @stringfunction
    def properties(self):
        """
        ${{}}

            _properties = { 
                ${self.propfields}
            }
        """

    @cached_property
    @stringfunction
    def casts_to(self):
        """
        ${{}}

            def _casts_to(self, dst):
                return ${self.name}._types[0]._casts_to(dst)
        """

        
    @cached_property
    def callfields(self):
        return self.joinfields("self.%(name)s")
    
    @cached_property
    @stringfunction
    def call(self):
        """
        ${{}}

            def __call__(self, *args, **kwargs):
                return random.${self.name}(${self.callfields})
        """
        
        
    @cached_property
    def reprfields(self):
        return self.joinfields("%(name)s = \" + str(self.%(name)s) + \"")

    @cached_property
    @stringfunction
    def repr(self):
        """
        ${{}}
        
            def __repr__(self):
                return "${self.name}(${self.reprfields})"
        """
        
    def joinfields(self, tmpl, sep = ", "):
        return sep.join([tmpl % locals() for (name, ini, typ) in self.fields])

    def __getitem__(self, key):
        return getattr(self, key)
    
    @property
    def members(self):
        return """
            header
            doc
            init
            label
            properties
            call
            casts_to
            repr
        """
        
    def __call__(self):
        return "".join(map(lambda name: getattr(self, name), 
                           self.members.split()))

template_meta = """
class %(name)s(object):
    \"\"\" %(docstring)s
    \"\"\"    

    def __init__(self, %(init)s):
        %(assign)s
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 
        %(props)s 
    }
    
    def _casts_to(self, dst):
        return %(name)s._types[0]._casts_to(dst)
    
    def __repr__(self):
        rv = "%(name)s"
        rv += "("
        for k in %(name)s._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"
"""

tab = "    "
nl = "\n"
comma = ","
slash = "\\"

def generate_meta(name, alias, docstring, fields, rvtype='float'):
    def process(tmpl, sep = ","):
        return sep.join([tmpl % locals() for (name, ini, typ) in fields])
    
    init = process("%(name)s = %(ini)s")
    assign = process("self.%(name)s = %(typ)s(%(name)s)", nl + 2*tab)
    props= process("\'%(name)s\' : %(typ)s", comma + nl + 2*tab)
    call = process("self.%(name)s")
    
    return template_meta % locals()

defs = ["from marketsim import registry, types, ops", "import random"]

def importedrandom(alias, t = float):
    
    def inner(cls):
        name = cls.__name__
        docstring = cls.__doc__
        fields = []
        
        for n in dir(cls):
            if n[0:2] != '__':
                v = getattr(cls, n)
                constraint = getattr(v, "constraint", None)
                if constraint is not None:
                    fields.append((n, v.defvalue, constraint))
                else:
                    if type(v) in [float, int]:
                        fields.append((n, v, type(v).__name__))
                    else:
                        assert False, "unsupported type"
        
        defs.append(RandomImpl(cls, alias, t)())
        #print generate_meta(name, alias, docstring, fields, t.__name__)
        exec generate_meta(name, alias, docstring, fields, t.__name__) in globals()
        return globals()[name]
    
    return inner

@importedrandom("Beta distribution")
class betavariate:
    """ Beta distribution. Conditions on the parameters are |alpha| > 0 and |beta| > 0.
        Returned values range between 0 and 1."""
    
    Alpha = positive(1.)
    Beta = positive(1.)
    
#print betavariate(2., 1.)
    
@importedrandom("Exponential distribution")
class expovariate:
    """ Exponential distribution. |lambda| is 1.0 divided by the desired mean. 
        It should be greater zero. Returned values range from 0 to positive infinity"""
    
    Lambda = positive(1.)

@importedrandom("Uniform integer distribution", int)
class randint:
    "Return a random integer *N* such that *a* <= *N* <= *b*."
    
    Low = -10 
    High = +10

@importedrandom("Uniform distribution")
class uniform:
    """ Return a random floating point number *N* such that 
            *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
        The end-point value *b* may or may not be included in the range depending on 
            floating-point rounding in the equation *a* + (*b*-*a*) * *random()*."""
             
    Low = -10. 
    High = +10.

@importedrandom("Triangular distribution")
class triangular:
    """ Return a random floating point number *N* such that *low* <= *N* <= *high* and 
        with the specified *mode* between those bounds.
        The *low* and *high* bounds default to zero and one.
        The *mode* argument defaults to the midpoint between the bounds,
        giving a symmetric distribution."""
    
    Low = 0. 
    High = 1.
    Mode = 0.5

@importedrandom("Gamma distribution")
class gammavariate:
    r"""Gamma distribution. Conditions on the parameters are |alpha| > 0 and |beta| > 0.
    
    The probability distribution function is: ::
    
                x ** (alpha - 1) * math.exp(-x / beta)
      pdf(x) =  --------------------------------------
                   math.gamma(alpha) * beta ** alpha"""
                   
    Alpha = positive(1.) 
    Beta = positive(1.)

@importedrandom("Log normal distribution")
class lognormvariate:
    """ Log normal distribution.
        If you take the natural logarithm of this distribution, 
        you'll get a normal distribution with mean |mu| and standard deviation |sigma|. 
        |mu| can have any value, and |sigma| must be greater than zero."""
    
    Mu = 0. 
    Sigma = positive(1.)

@importedrandom("Normal distribution")
class normalvariate:
    "Normal distribution. |mu| is the mean, and |sigma| is the standard deviation."
    
    Mu = 0. 
    Sigma = positive(1.)

@importedrandom("Von Mises distribution")
class vonmisesvariate:
    """ |mu| is the mean angle, expressed in radians between 0 and 2|pi|, 
        and |kappa| is the concentration parameter, which must be greater than or equal to zero. 
        If |kappa| is equal to zero, this distribution reduces 
        to a uniform random angle over the range 0 to 2|pi|"""
    
    Mu = 0. 
    Kappa = non_negative(0.)

@importedrandom("Pareto distribution")
class paretovariate:
    "Pareto distribution. |alpha| is the shape parameter."
    
    Alpha = positive(1.)

@importedrandom("Weibull distribution")
class weibullvariate:
    "Weibull distribution. |alpha| is the scale parameter and |beta| is the shape parameter."
    
    Alpha = positive(1.) 
    Beta = positive(1.)

import chk_ts
    
with open(chk_ts.target('rnd'), "w") as out:
    for d in defs:
        out.write(d)
        out.write('\n')