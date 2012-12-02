import random
from _basic import OneSide, Strategy
from marketsim import order, Side, scheduler

class LiquidityProviderSide(OneSide):

    def __init__(self, \
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
        self._orderFactory = orderFactoryT(side)
        self._queue = trader.book.queue(side)
        self._defaultValue = defaultValue
        self._priceDistr = priceDistr
        self._volumeDistr = volumeDistr
        self._creationIntervalDistr = creationIntervalDistr
        self._eventGen = scheduler.Timer(creationIntervalDistr)
    
        OneSide.__init__(self, trader)
        
    def _orderFunc(self):
        currentPrice = self._queue.best.price if not self._queue.empty else\
                       self._queue.lastPrice if self._queue.lastPrice is not None else\
                       self._defaultValue
        price = currentPrice * self._priceDistr()
        volume = int(self._volumeDistr())
        return (price, volume)
    
class LiquidityProvider(Strategy):
    def __init__(self, 
                 trader,
                 orderFactoryT=order.Limit.T,
                 defaultValue=100,
                 creationIntervalDistr=(lambda: random.expovariate(1.)),
                 priceDistr=(lambda: random.lognormvariate(0., .1)),
                 volumeDistr=(lambda: random.expovariate(.1))):
        Strategy.__init__(self, trader)
        self._sell = LiquidityProviderSide(trader, Side.Sell, orderFactoryT, defaultValue, creationIntervalDistr, priceDistr, volumeDistr)
        self._buy = LiquidityProviderSide(trader, Side.Buy, orderFactoryT, defaultValue, creationIntervalDistr, priceDistr, volumeDistr)
    
    def suspend(self, s):
        Strategy.suspend(self, s)
        self._sell.suspend(s)
        self._buy.suspend(s)
        
    @property
    def suspended(self):
        assert self._sell.suspended == self._suspended
        assert self._buy.suspended == self._suspended
        return Strategy.suspended(self)

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

