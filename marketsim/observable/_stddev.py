from marketsim import ops, types, event, _, getLabel,  registry

import fold
import math

from _misc import Sqr

from marketsim.gen._out.observable.Cumulative._Var import Var as Variance
from marketsim.gen._out.observable.Cumulative._StdDev import StdDev

from marketsim.gen._out.observable.Moving._Var import Var as MovingVariance

@registry.expose(alias = ['Statistics', 'StdDev', 'Moving'], 
                 args = (ops.constant(1.),10))
def StdDevRolling(source, timeframe):
    return ops.Sqrt(MovingVariance(source, timeframe))

from _ewma import EWMA

from marketsim.gen._out.observable.EW._Var import Var as EWMV
from marketsim.gen._out.observable.EW._StdDev import StdDev as StdDevEW

    