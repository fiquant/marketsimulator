import math
from marketsim import types, registry, ops, registry

from marketsim.gen._out.math.EW._Avg import Avg as EWMA

from _computed import OnEveryDt
    
def dEWMA(source, alpha=0.15):
    """ Creates a folder with derivative of exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return ops.Derivative(EWMA(source, alpha))

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

def trend(source, alpha=0.015):
    return OnEveryDt(1, dEWMA(source, alpha))
