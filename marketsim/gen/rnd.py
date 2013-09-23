import sys, os

import types
from types import *

from _impl.random import *

defs = ["from marketsim import registry, types, ops", "import random"]

def importedrandom(alias, t = float):
    
    def inner(cls):
        defs.append(RandomImpl(cls, alias, t)())
        exec RandomMeta(cls, alias, t)() in globals()
        return globals()[cls.__name__]
    
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
