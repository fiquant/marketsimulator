import random
from marketsim import Side, order, observable, scheduler, mathutils
from _basic import TwoSides

# TBD: fundamental trader and dependency traders should be written through signal trader
#      signal function for fundamental trader will be currentPrice - fv()
#      for dependent trader - currentPrice - wantedPrice()

def signalFunc(threshold, volumeDistr, signalFunc):
    """ Calculates side and volume for a signal trader
    threshold - when signal value is higher than threshold, the trader buys
                when signal value is less than -threshold, the trader sells
    volumeDistr - defines volumes of orders to create
    signalFunc - returns signal value
    Returns function: trader -> (side, (volume,))
    """
    def inner(trader):
        value = signalFunc()
        side = Side.Buy if value > threshold else Side.Sell if value < -threshold else None
        return (side, (volumeDistr(side),)) if side else None
    return inner

def Signal(trader,
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
    return TwoSides(trader, orderFactory, signal, 
                    signalFunc(threshold, lambda _: volumeDistr(), 
                               lambda: signal.value))

def TrendFollower(trader,
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
    
    trend = observable.Fold(observable.Price(trader.orderBook), observable.derivative(average))
    
    return TwoSides(trader, orderFactory, scheduler.Timer(creationIntervalDistr), 
                    signalFunc(threshold, lambda _: volumeDistr(), trend))
