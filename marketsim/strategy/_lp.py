import random
from _basic import OneSide
from marketsim import order, Side, scheduler

def liquidityProviderFunc(side, defaultValue, priceDistr, volumeDistr):
    """ Calculates price and volume for a liquidity provider.
    defaultValue - price to be taken if the order queue is empty
    priceDistr - function returning a value 
                 that being multiplied to currentPrice gives price of order to create  
    volumeDistr - function returning volume of order to create
    Returns function: trader -> (price, volume) of order to create
    """
    def inner(trader):
        queue = trader.book.queue(side)
        currentPrice = queue.best.price if not queue.empty else\
                       queue.lastPrice if queue.lastPrice is not None else\
                       defaultValue
        price = currentPrice * priceDistr()
        volume = int(volumeDistr())
        return (price, volume)
    return inner

def LiquidityProviderSide( \
                     trader,
                     side=Side.Sell,
                     orderFactoryT=order.Limit.T,
                     defaultValue=100,
                     creationIntervalDistr=(lambda: random.expovariate(1.)),
                     priceDistr=(lambda: random.lognormvariate(0., .1)),
                     volumeDistr=(lambda: random.expovariate(.1))):
    """ Creates a liquidity provider trader
    trader - single asset single market trader
    side - side of orders to create (default: Sell)
    orderFactoryT - order factory function (default: LimitOrderT)
    defaultValue - default price which is taken if orderBook is empty (default: 100)
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    priceDistr - defines multipliers for current asset price when price of order ti create is calculated 
                            (default: log normal distribution with \mu=0 and \sigma=0.1)
    volumeDistr - defines volumes of orders to create
                            (default: exponential distribution with \lambda=1)
    """

    return OneSide(trader,
                   side,
                   orderFactoryT,
                   scheduler.Timer(creationIntervalDistr),
                   liquidityProviderFunc(side, defaultValue, priceDistr, volumeDistr))

def LiquidityProvider( \
                     trader,
                     orderFactoryT=order.Limit.T,
                     defaultValue=100,
                     creationIntervalDistr=(lambda: random.expovariate(1.)),
                     priceDistr=(lambda: random.lognormvariate(0., .1)),
                     volumeDistr=(lambda: random.expovariate(.1))):

    LiquidityProviderSide(trader, Side.Sell, orderFactoryT, defaultValue, creationIntervalDistr, priceDistr, volumeDistr)
    LiquidityProviderSide(trader, Side.Buy, orderFactoryT, defaultValue, creationIntervalDistr, priceDistr, volumeDistr)
    return trader

class Canceller(object):
    """ Randomly cancels created orders in specific moments of time    
    """

    def __init__(   self,
                    source,
                    cancellationIntervalDistr=(lambda: random.expovariate(1.)),
                    choiceFunc=lambda N: random.randint(0,N-1)):
        """ Initializes canceller with 
        cancellationIntervalDistr - intervals of times between order cancellations
                                    (default: exponential distribution with \lambda=1)
        choiceFunc - function N -> idx that chooses which order should be cancelled
        source - optional trader to subscribe to  
        """

        # orders created by trader
        self._elements = []

        # start listening its orders sent
        source.on_order_sent += self.process
        
        book = source.book

        def wakeUp(_):
            # if we have orders to cancel
            while self._elements <> []:
                # choose an order
                N = len(self._elements)
                idx = choiceFunc(N)
                e = self._elements[idx]
                # if the order is invalid
                if e.empty or e.cancelled:
                    # put the last order instead of it and repeat the procedure
                    if e <> self._elements[-1]:
                        self._elements[idx] = self._elements[-1]
                    # it converges since every time we pops an element from the queue
                    self._elements.pop()
                else:
                    # if order is valid, cancel it
                    book.process(order.Cancel(e))
                    return

        scheduler.Timer(cancellationIntervalDistr).advise(wakeUp)

    def process(self, order):
        """ Puts 'order' to future cancellation list
        """
        self._elements.append(order)

