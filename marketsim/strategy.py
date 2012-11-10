import random
from marketsim import Side
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
