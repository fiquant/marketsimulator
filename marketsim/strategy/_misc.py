from marketsim import scheduler, order, mathutils, types   
from _basic import TwoSides
from _wrap import wrapper

class _Noise_Impl(TwoSides):
    
    def __init__( self, trader, params):
        self._params = params
        self._orderFactoryT = params.orderFactoryT
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
    
        TwoSides.__init__(self, trader)
        
    def _orderFunc(self):
        return (self._params.sideDistr(), (int(self._params.volumeDistr()),)) 

exec wrapper("Noise", 
             [("orderFactoryT",         "order.Market.T",               "None"),
              ("sideDistr",             "mathutils.rnd.randint(0,1)",   "() -> int"), # in fact it should be () -> Side
              ("volumeDistr",           "mathutils.rnd.expovariate(1.)",'() -> float'),
              ("creationIntervalDistr", "mathutils.rnd.expovariate(1.)",'() -> float')])
