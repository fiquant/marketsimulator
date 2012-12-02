import random
from marketsim import Side, order, observable, scheduler, mathutils
from _basic import TwoSides

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

class Signal(SignalBase):
    
    def __init__(self, 
                 trader,
                 signal,
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
        self._eventGen = signal
        self._threshold = threshold
        self._orderFactoryT = orderFactory
        self._signalFunc = lambda: signal.value
        self._volume = lambda _: volumeDistr()
        
        SignalBase.__init__(self, trader)

class TwoAverages(SignalBase):
    
    def __init__(self, 
                 trader,
                 average1 = mathutils.ewma(alpha = 0.15),
                 average2 = mathutils.ewma(alpha = 0.015),
                 threshold = 0., 
                 orderFactory=order.Market.T,
                 creationIntervalDistr=(lambda: random.expovariate(1.)),
                 volumeDistr=(lambda: random.expovariate(1.))):
        
        self._eventGen = scheduler.Timer(creationIntervalDistr)
        self._volume = lambda _: volumeDistr()
        self._threshold = threshold
        self._orderFactoryT = orderFactory
        
        price = observable.Price(trader.orderBook)
        self._average1 = observable.Fold(price, average1)
        self._average2 = observable.Fold(price, average2)
        
        SignalBase.__init__(self, trader)
        
    def _signalFunc(self):
        avg1 = self._average1.value
        avg2 = self._average2.value
        return avg1 - avg2 if avg1 is not None and avg2 is not None else None 


class TrendFollower(SignalBase):
    
    def __init__(self, 
                 trader,
                 average = mathutils.ewma(alpha = 0.15),
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
        
        self._eventGen = scheduler.Timer(creationIntervalDistr)
        self._volume = lambda _: volumeDistr()
        self._threshold = threshold
        self._orderFactoryT = orderFactory
        
        trend = observable.Fold(observable.Price(trader.orderBook), observable.derivative(average))
        self._signalFunc = lambda: trend.value
        
        SignalBase.__init__(self, trader)
        