import random
from marketsim import Side, scheduler, order

from _basic import TwoSides


def Noise(trader,
          orderFactory=order.MarketOrderT,
          sideDistr=(lambda: random.randint(0,1)),
          volumeDistr=(lambda: random.expovariate(.1)),
          creationIntervalDistr=(lambda: random.expovariate(1.))):
    """ Creates a noise trader: a trader that randomly chooses a side and volume to trade
    trader - single asset single market trader
    orderFactoryT - order factory function (default: MarketOrderT)
    sideDistr - side of orders to create 
                            (default: discrete uniform distribution P(Sell)=P(Buy)=.5)
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    volumeDistr - defines volumes of orders to create
                            (default: exponential distribution with \lambda=1)
    """

    return TwoSides(trader, orderFactory,
                    scheduler.Timer(creationIntervalDistr),
                    lambda _: (sideDistr(), (int(volumeDistr()),)))


