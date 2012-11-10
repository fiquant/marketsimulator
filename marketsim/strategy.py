import random
from marketsim import Side
from marketsim import indicator
from marketsim.scheduler import Timer
from marketsim.order import MarketOrderT


def TwoSides(trader, orderFactoryT, eventGen, orderFunc):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        

        def wakeUp(signal):
            # determine side and parameters of an order to create
            res = orderFunc(trader)
            if res <> None:
                (side, params) = res
                # create order given side and parameters
                order = orderFactoryT(side)(*params)
                # send order to the order book
                trader.send(order)

        # start listening calls from eventGen
        eventGen.advise(wakeUp)
        return trader

def fv_func(fundamentalValueFunc, volumeDistr):
    """ Calculates side and volume for fundamental value trader
    fundamentalValueFunc -- function to determine current fundamental value
    volumeDistr - defines volume of order to create
    Returns function: trader -> (side,(volume,))
    """
    def inner(trader):
        book = trader.book
        # if current price is defined, compare it with the fundamental value and define the side
        side = Side.Buy  if not book.asks.empty and book.asks.best.price < fundamentalValueFunc() else\
               Side.Sell if not book.bids.empty and book.bids.best.price > fundamentalValueFunc() else\
               None
        if side <> None:
            volume = int(volumeDistr(side))
            return (side, (volume,))
        return None
    return inner

def FundamentalValue( trader,
                      orderFactory=MarketOrderT,
                      fundamentalValue=lambda: 100,
                      volumeDistr=(lambda: random.expovariate(.1)),
                      creationIntervalDistr=(lambda: random.expovariate(1.))):
    """ Creates a fundamental value trader
    trader - single asset single market trader
    orderFactory - order factory function: side -> *orderParams -> Order
    fundamentalValue - defines fundamental value 
                            (default: constant 100)
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    """

    return TwoSides(trader, orderFactory,
                    Timer(creationIntervalDistr),
                    fv_func(fundamentalValue, lambda _: volumeDistr()))

def Dependency(trader,
               bookToDependOn,
               orderFactory=MarketOrderT,
               factor=1.,
               volumeDistr=(lambda: random.expovariate(.1))):
    """ Creates a strategy that believes that fair asset price 
    can be obtained as current price of another asset multiplied by some factor
    Once this relation doesn't hold it tries to buy or sell orders with better price     

    trader - single asset single market trader
    bookToDependOn - asset that is considered as reference one
    orderFactory - order factory function: side -> *orderParams -> Order
    factor - multiplier to obtain fair the asset price by reference price
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    
    # start listening changes in a reference asset price
    priceToDependOn = indicator.AssetPrice(bookToDependOn) 
    
    def wantedPrice():
        """ Price of order to create """
        return priceToDependOn.value * factor
    
    def wantedVolume(side):
        """ Volume of order to create """        
        oppositeQueue = trader.book.queue(side.opposite)
        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(wantedPrice())
        # we want to trade orders only with a good price
        return min(oppositeVolume, volumeDistr())        

    return TwoSides(trader, orderFactory, priceToDependOn, fv_func(wantedPrice, wantedVolume))

def Noise(trader,
          orderFactory=MarketOrderT,
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
                    Timer(creationIntervalDistr),
                    lambda _: (sideDistr(), (int(volumeDistr()),)))

def signalTraderFunc(threshold, volumeDistr, signalFunc):
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
        return (side, (volumeDistr(),)) if side<>None else None
    return inner

def Signal(trader,
           signal,
           threshold=0.7,
           orderFactory=MarketOrderT,
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
                    signalTraderFunc(threshold, volumeDistr, 
                                     lambda: signal.value))

def TrendFollower(trader,
                  average = indicator.ewma(alpha = 0.15),
                  threshold = 0., 
                  orderFactory=MarketOrderT,
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
    
    trend = indicator.Fold(indicator.AssetPrice(trader.orderBook), indicator.derivative(average))
    
    return TwoSides(trader, orderFactory, Timer(creationIntervalDistr), 
                    signalTraderFunc(threshold, volumeDistr, trend))

