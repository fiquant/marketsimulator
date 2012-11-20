import random
from marketsim import order, Side, scheduler, observable

from _basic import TwoSides

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
                      orderFactory=order.Market.T,
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
                    scheduler.Timer(creationIntervalDistr),
                    fv_func(fundamentalValue, lambda _: volumeDistr()))

def Dependency(trader,
               bookToDependOn,
               orderFactory=order.Market.T,
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
    priceToDependOn = observable.Price(bookToDependOn) 
    
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
