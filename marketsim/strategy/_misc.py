import random
from marketsim import scheduler, order

from _basic import TwoSides

class Noise(TwoSides):
    
    def __init__( self,
                  trader,
                  orderFactoryT=order.Market.T,
                  sideDistr=lambda: random.randint(0,1),
                  volumeDistr=lambda: random.expovariate(.1),
                  creationIntervalDistr=lambda: random.expovariate(1.)):
        """ Noise(trader,\
              orderFactoryT=order.Market.T,\
              sideDistr=lambda: random.randint(0,1),\
              volumeDistr=lambda: random.expovariate(.1),\
              creationIntervalDistr=lambda: random.expovariate(1.))
        
        Creates a noise trader: a trader that randomly chooses a side and volume to trade
        
        Arguments:
        
            **trader**
                single asset single market trader
                
            **orderFactoryT**
                order factory function (default: MarketOrderT)
            
            **sideDistr**
                side of orders to create
                (default: discrete uniform distribution P(Sell)=P(Buy)=.5)
        
            **creationIntervalDistr**
                defines intervals of time between order creation 
                (default: exponential distribution with \lambda=1)
        
            **volumeDistr**
                defines volumes of orders to create
                (default: exponential distribution with \lambda=1)
        """
        self._orderFactoryT = orderFactoryT
        self._creationIntervalDistr = creationIntervalDistr
        self._eventGen = scheduler.Timer(self._creationIntervalDistr)
        self._sideDistr = sideDistr
        self._volumeDistr = volumeDistr
    
        TwoSides.__init__(self, trader)
        
    def _orderFunc(self):
        return (self._sideDistr(), (int(self._volumeDistr()),)) 

