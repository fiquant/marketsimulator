import random
from marketsim import Side, order, observable, scheduler, mathutils
from _basic import TwoSides, Wrapper, currentframe


# TBD: fundamental trader and dependency traders should be written through signal trader
#      signal function for fundamental trader will be currentPrice - fv()
#      for dependent trader - currentPrice - wantedPrice()

class SignalBase(TwoSides):
    
    def __init__(self, trader):
        TwoSides.__init__(self, trader)
        
    def _orderFunc(self):
        threshold = self._threshold
        value = self._signalFunc()
        side = Side.Buy  if value > threshold else\
               Side.Sell if value < -threshold else\
               None
        return (side, (self._volume(side),)) if side else None

class _Signal_Impl(SignalBase):
    
    def __init__(self, trader, params):
        self._eventGen = params.signal
        self._threshold = params.threshold
        self._orderFactoryT = params.orderFactory
        self._signalFunc = lambda: params.signal.value
        self._volume = lambda _: params.volumeDistr()
        
        SignalBase.__init__(self, trader)

def Signal(signal,
           threshold=0.7,
           orderFactory=order.Market.T,
           volumeDistr=(lambda: random.expovariate(1.))):
    """ Creates a signal trader.
    trader - single asset single market trader
    signal - signal to be listened to 
    threshold - threshold when the trader starts to act
    orderFactory - order factory function: side -> *orderParams -> Order
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    return Wrapper(_Signal_Impl, currentframe())

class _TwoAverages_Impl(SignalBase):
    
    def __init__(self, trader, params):
        
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        self._volume = lambda _: params.volumeDistr()
        self._threshold = params.threshold
        self._orderFactoryT = params.orderFactory
        
        price = observable.Price(trader.orderBook)
        self._average1 = observable.Fold(price, params.average1)
        self._average2 = observable.Fold(price, params.average2)
        
        SignalBase.__init__(self, trader)
        
    def _signalFunc(self):
        avg1 = self._average1.value
        avg2 = self._average2.value
        return avg1 - avg2 if avg1 is not None and avg2 is not None else None 

def TwoAverages(average1 = mathutils.ewma(alpha = 0.15),
                average2 = mathutils.ewma(alpha = 0.015),
                threshold = 0., 
                orderFactory=order.Market.T,
                creationIntervalDistr=(lambda: random.expovariate(1.)),
                volumeDistr=(lambda: random.expovariate(1.))):

    return Wrapper(_TwoAverages_Impl, currentframe())

class _TrendFollower_Impl(SignalBase):
    
    def __init__(self, trader, params):
        
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        self._volume = lambda _: params.volumeDistr()
        self._threshold = params.threshold
        self._orderFactoryT = params.orderFactory
        
        trend = observable.Fold(observable.Price(trader.orderBook), 
                                observable.derivative(params.average))
        self._signalFunc = lambda: trend.value
        
        SignalBase.__init__(self, trader)
   
def TrendFollower(average = mathutils.ewma(alpha = 0.15),
                  threshold = 0., 
                  orderFactory=order.Market.T,
                  creationIntervalDistr=(lambda: random.expovariate(1.)),
                  volumeDistr=(lambda: random.expovariate(1.))):
    """ Creates a trend follower trader
    trader - single asset single market trader
    average - moving average object (update(time,value); derivativeAt(time))
    threshold - threshold of the moving average derivate when the trader starts to act
    orderFactory - order factory function: side -> *orderParams -> Order
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
     
    return Wrapper(_TrendFollower_Impl, currentframe())