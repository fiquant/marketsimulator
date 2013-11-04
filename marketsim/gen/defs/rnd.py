
from marketsim import registry, types, ops
import random
            
@registry.expose(['Random', 'Beta distribution'])
class betavariate(ops.Function[float]):
    """ 
     Conditions on the parameters are |alpha| > 0 and |beta| > 0.
     Returned values range between 0 and 1.
    """ 
    def __init__(self, Alpha = 1.0, Beta = 1.0):
        self.Alpha = Alpha
        self.Beta = Beta

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Alpha' : float,
        'Beta' : float
    }

    def __repr__(self):
        return "betavariate(Alpha = "+repr(self.Alpha)+" , Beta = "+repr(self.Beta)+" )" 

    def __call__(self, *args, **kwargs):
        return random.betavariate(self.Alpha, self.Beta)

    def _casts_to(self, dst):
        return betavariate._types[0]._casts_to(dst)


@registry.expose(['Random', 'Exponential distribution'])
class expovariate(ops.Function[float]):
    """ 
     |lambda| is 1.0 divided by the desired mean.
     It should be greater zero. Returned values range from 0 to positive infinity
    """ 
    def __init__(self, Lambda = 1.0):
        self.Lambda = Lambda

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Lambda' : float
    }

    def __repr__(self):
        return "expovariate(Lambda = "+repr(self.Lambda)+" )" 

    def __call__(self, *args, **kwargs):
        return random.expovariate(self.Lambda)

    def _casts_to(self, dst):
        return expovariate._types[0]._casts_to(dst)


@registry.expose(['Random', 'Uniform distribution'])
class uniform(ops.Function[float]):
    """ 
     Return a random floating point number *N* such that
     *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
     The end-point value *b* may or may not be included in the range depending on
     floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
    """ 
    def __init__(self, Low = -10.0, High = 10.0):
        self.Low = Low
        self.High = High

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Low' : float,
        'High' : float
    }

    def __repr__(self):
        return "uniform(Low = "+repr(self.Low)+" , High = "+repr(self.High)+" )" 

    def __call__(self, *args, **kwargs):
        return random.uniform(self.Low, self.High)

    def _casts_to(self, dst):
        return uniform._types[0]._casts_to(dst)


@registry.expose(['Random', 'Triangular distribution'])
class triangular(ops.Function[float]):
    """ 
     Return a random floating point number *N* such that *low* <= *N* <= *high* and
           with the specified *mode* between those bounds.
           The *low* and *high* bounds default to zero and one.
           The *mode* argument defaults to the midpoint between the bounds,
           giving a symmetric distribution.
    """ 
    def __init__(self, Low = 0.0, High = 1.0, Mode = 0.5):
        self.Low = Low
        self.High = High
        self.Mode = Mode

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Low' : float,
        'High' : float,
        'Mode' : float
    }

    def __repr__(self):
        return "triangular(Low = "+repr(self.Low)+" , High = "+repr(self.High)+" , Mode = "+repr(self.Mode)+" )" 

    def __call__(self, *args, **kwargs):
        return random.triangular(self.Low, self.High, self.Mode)

    def _casts_to(self, dst):
        return triangular._types[0]._casts_to(dst)


@registry.expose(['Random', 'Gamma distribution'])
class gammavariate(ops.Function[float]):
    """ 
      Conditions on the parameters are |alpha| > 0 and |beta| > 0.
    
      The probability distribution function is: ::
    
                   x ** (alpha - 1) * math.exp(-x / beta)
         pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    """ 
    def __init__(self, Alpha = 1.0, Beta = 1.0):
        self.Alpha = Alpha
        self.Beta = Beta

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Alpha' : float,
        'Beta' : float
    }

    def __repr__(self):
        return "gammavariate(Alpha = "+repr(self.Alpha)+" , Beta = "+repr(self.Beta)+" )" 

    def __call__(self, *args, **kwargs):
        return random.gammavariate(self.Alpha, self.Beta)

    def _casts_to(self, dst):
        return gammavariate._types[0]._casts_to(dst)


@registry.expose(['Random', 'Log normal distribution'])
class lognormvariate(ops.Function[float]):
    """ 
     If you take the natural logarithm of this distribution,
      you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
      |mu| can have any value, and |sigma| must be greater than zero.
    """ 
    def __init__(self, Mu = 0.0, Sigma = 1.0):
        self.Mu = Mu
        self.Sigma = Sigma

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Mu' : float,
        'Sigma' : float
    }

    def __repr__(self):
        return "lognormvariate(Mu = "+repr(self.Mu)+" , Sigma = "+repr(self.Sigma)+" )" 

    def __call__(self, *args, **kwargs):
        return random.lognormvariate(self.Mu, self.Sigma)

    def _casts_to(self, dst):
        return lognormvariate._types[0]._casts_to(dst)


@registry.expose(['Random', 'Normal distribution'])
class normalvariate(ops.Function[float]):
    """ 
      |mu| is the mean, and |sigma| is the standard deviation.
    """ 
    def __init__(self, Mu = 0.0, Sigma = 1.0):
        self.Mu = Mu
        self.Sigma = Sigma

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Mu' : float,
        'Sigma' : float
    }

    def __repr__(self):
        return "normalvariate(Mu = "+repr(self.Mu)+" , Sigma = "+repr(self.Sigma)+" )" 

    def __call__(self, *args, **kwargs):
        return random.normalvariate(self.Mu, self.Sigma)

    def _casts_to(self, dst):
        return normalvariate._types[0]._casts_to(dst)


@registry.expose(['Random', 'Von Mises distribution'])
class vonmisesvariate(ops.Function[float]):
    """ 
      |mu| is the mean angle, expressed in radians between 0 and 2|pi|,
          and |kappa| is the concentration parameter, which must be greater than or equal to zero.
          If |kappa| is equal to zero, this distribution reduces
          to a uniform random angle over the range 0 to 2|pi|
    """ 
    def __init__(self, Mu = 0.0, Kappa = 0.0):
        self.Mu = Mu
        self.Kappa = Kappa

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Mu' : float,
        'Kappa' : float
    }

    def __repr__(self):
        return "vonmisesvariate(Mu = "+repr(self.Mu)+" , Kappa = "+repr(self.Kappa)+" )" 

    def __call__(self, *args, **kwargs):
        return random.vonmisesvariate(self.Mu, self.Kappa)

    def _casts_to(self, dst):
        return vonmisesvariate._types[0]._casts_to(dst)


@registry.expose(['Random', 'Pareto distribution'])
class paretovariate(ops.Function[float]):
    """ 
      |alpha| is the shape parameter.
    """ 
    def __init__(self, Alpha = 1.0):
        self.Alpha = Alpha

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Alpha' : float
    }

    def __repr__(self):
        return "paretovariate(Alpha = "+repr(self.Alpha)+" )" 

    def __call__(self, *args, **kwargs):
        return random.paretovariate(self.Alpha)

    def _casts_to(self, dst):
        return paretovariate._types[0]._casts_to(dst)


@registry.expose(['Random', 'Weibull distribution'])
class weibullvariate(ops.Function[float]):
    """ 
      |alpha| is the scale parameter and |beta| is the shape parameter
    """ 
    def __init__(self, Alpha = 1.0, Beta = 1.0):
        self.Alpha = Alpha
        self.Beta = Beta

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Alpha' : float,
        'Beta' : float
    }

    def __repr__(self):
        return "weibullvariate(Alpha = "+repr(self.Alpha)+" , Beta = "+repr(self.Beta)+" )" 

    def __call__(self, *args, **kwargs):
        return random.weibullvariate(self.Alpha, self.Beta)

    def _casts_to(self, dst):
        return weibullvariate._types[0]._casts_to(dst)

