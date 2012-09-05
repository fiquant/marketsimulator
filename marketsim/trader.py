import random
from marketsim.scheduler import Timer, world
from marketsim import Side
from marketsim.order import *
from marketsim.indicator import AssetPrice, ewma, Fold
import math

class TraderBase(object):
    """ Base class for traders.
    Responsible for bookkeeping P&L of the trader and 
    maintaining on_order_sent and on_traded events
    """

    def __init__(self):
        # P&L is the minus sum of money spent for the trades done
        # if a trader sells P&L increases
        # if a trader buys P&L falls
        self._PnL = 0
        # event to be fired when an order has been sent
        self.on_order_sent = Event()
        # event to be fired when a trader's is traded
        self.on_traded = Event()

    def _onOrderMatched(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's P&L is updated and listeners are notified about the trade   
        """
        pv = price * volume
        self._PnL += pv if order.side == Side.Sell else -pv
        
        self.on_traded.fire(self)

    @property
    def PnL(self):
        """ Returns traders's P&L
        """
        return self._PnL
    
    def _makeSubscribedTo(self, order):
        """ Makes trader subscribed to 'order' on_matched event
        before sending it to the order book
        Returns the order itself 
        """
        order.on_matched += self._onOrderMatched
        return order

    def send(self, book, order):
        """ Sends 'order' to 'book'
        After having the order sent notifies listeners about it 
        """
        book.process(self._makeSubscribedTo(order))
        self.on_order_sent.fire(order)        

        
class SingleAssetTrader(TraderBase):
    """ Trader that trades only one asset 
    (should we consider a same asset on different markets as the same asset?)
    Maintains number of assets traded:
    positive if trader has bought more assets than sold them
    negative otherwise
    """

    def __init__(self):
        TraderBase.__init__(self)
        self._amount = 0

    def _onOrderMatched(self, order, other, (price, volume)):
        """ Called when a trader's 'order' is traded against 'other' order 
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade   
        """
        self._amount += volume if order.side == Side.Buy else -volume
        TraderBase._onOrderMatched(self, order, other, (price,volume))
        
    @property
    def amount(self):
        """ Number of assets traded:
        positive if trader has bought more assets than sold them
        negative otherwise
        """
        return self._amount

class OneSideTrader(SingleAssetTrader):
    """ Generic trader that sends orders of only one side of a single asset
    """

    def __init__(   self,
                    orderBook,                 
                    side,                        
                    orderFactoryT,            
                    eventGen,                  
                    orderFunc):                
        """ Initializes generic one side trader and makes it working
        orderBook - book to place orders in
        side - side of orders to create
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> *orderParams 
        """        

        SingleAssetTrader.__init__(self)

        self.side = side
        # we may calculate order factory right now
        orderFactory = orderFactoryT(side)
        # save book for later use in orderFuncs
        self.book = orderBook

        def wakeUp(signal):
            # determine parameters of an order to create
            params = orderFunc(self)
            # create an order with given parameters
            order = orderFactory(*params)
            # send the order to the order book
            self.send(orderBook, order)

        # start listening calls from eventGen
        eventGen.advise(wakeUp)

class TwoSideTrader(SingleAssetTrader):
    """ Generic trader that may send orders to two sides of a single asset
    """

    def __init__(   self,
                    orderBook,                 
                    orderFactoryT,            
                    eventGen,                  
                    orderFunc):                
        """ Initializes generic two side trader and makes it working
        orderBook - book to place orders in
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        

        SingleAssetTrader.__init__(self)

        # save book for later use in orderFuncs
        self.book = orderBook

        def wakeUp(signal):
            # determine side and parameters of an order to create
            res = orderFunc(self)
            if res <> None:
                (side, params) = res
                # create order given side and parameters
                order = orderFactoryT(side)(*params)
                # send order to the order book
                self.send(orderBook, order)

        # start listening calls from eventGen
        eventGen.advise(wakeUp)


def liquidityProviderFunc(defaultValue, priceDistr, volumeDistr):
    """ Calculates price and volume for a liquidity provider.
    defaultValue - price to be taken if the order queue is empty
    priceDistr - function returning a value 
                 that being multiplied to currentPrice gives price of order to create  
    volumeDistr - function returning volume of order to create
    Returns function: trader -> (price, volume) of order to create
    """
    def inner(trader):
        queue = trader.book.queue(trader.side)
        currentPrice = queue.best.price if not queue.empty else\
                       queue.lastPrice if queue.lastPrice is not None else\
                       defaultValue
        price = currentPrice * priceDistr()
        volume = int(volumeDistr())
        return (price, volume)
    return inner

def LiquidityProvider( \
                     orderBook,
                     side=Side.Sell,
                     orderFactoryT=LimitOrderT,
                     defaultValue=100,
                     creationIntervalDistr=(lambda: random.expovariate(1.)),
                     priceDistr=(lambda: random.lognormvariate(0., .1)),
                     volumeDistr=(lambda: random.expovariate(.1))):
    """ Creates a liquidity provider trader
    orderBook - book to place orders in
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

    return OneSideTrader(orderBook,
                                side,
                                orderFactoryT,
                                Timer(creationIntervalDistr),
                                liquidityProviderFunc(defaultValue, priceDistr, volumeDistr))


# TBD: TwoSides that takes a trader class and its parameters
# and instantiates a trader composed of a buyer and a seller
# with given distributions

# TBD: A MarketMaker -- trader that send a limit order which 
# is slightly better than the best order and cancels its elder one order
# In fact it can be considered as a trading strategy like Iceberg strategy
# AlwaysBetter strategy
# If there are more than one market maker, they will quickly annihilate each other
# So we really need to introduce notion of a remote order book 
# in order to model latency

# TBD: Latency, LocalOrderBook or RemoteOrderBook
# This class will imitate an order book
# it will send orders to the real order book with some latency
# also it will listen to the order book and update its own statistics
# with some latency (it can be accomplished by scheduling these updates)
# It may require changing and restricting OrderBook interface
# Users shall indicate explicitly what information should be collected 
# since it is a time consuming task

# TBD: TwoSides would produce TwoSidesTrader and TwoSidesTrader
# would have seller and buyer sides that might be suspended or resumed

# TBD: A strategy that suspends trading on a side that has a big disbalance 

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
                    book.process(CancelOrder(e))
                    return

        Timer(cancellationIntervalDistr).advise(wakeUp)

    def process(self, order):
        """ Puts 'order' to future cancellation list
        """
        self._elements.append(order)

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

def FVTrader(   book,
                orderFactory=MarketOrderT,
                fundamentalValue=lambda: 100,
                volumeDistr=(lambda: random.expovariate(.1)),
                creationIntervalDistr=(lambda: random.expovariate(1.))):
    """ Creates a fundamental value trader
    book - book to place orders in
    orderFactory - order factory function: side -> *orderParams -> Order
    fundamentalValue - defines fundamental value 
                            (default: constant 100)
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    """

    return TwoSideTrader(book, orderFactory,
                                Timer(creationIntervalDistr),
                                fv_func(fundamentalValue, lambda _: volumeDistr()))
    
def DependanceTrader(book,
                     bookToDependOn,
                     orderFactory=MarketOrderT,
                     factor=1.,
                     volumeDistr=(lambda: random.expovariate(.1))):
    """ Creates a trader that believes that fair asset price 
    can be obtained as current price of another asset multiplied by some factor
    Once this relation doesn't hold it tries to buy or sell orders with better price     

    book - book to place orders in
    bookToDependOn - asset that is considered as reference one
    orderFactory - order factory function: side -> *orderParams -> Order
    factor - multiplier to obtain fair the asset price by reference price
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    
    # start listening changes in a reference asset price
    priceToDependOn = AssetPrice(bookToDependOn) 
    
    def wantedPrice():
        """ Price of order to create """
        return priceToDependOn.value * factor
    
    def wantedVolume(side):
        """ Volume of order to create """        
        oppositeQueue = book.queue(side.opposite)
        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(wantedPrice())
        # we want to trade orders only with a good price
        return min(oppositeVolume, volumeDistr())        

    return TwoSideTrader(book, orderFactory, priceToDependOn, fv_func(wantedPrice, wantedVolume))

def NoiseTrader(book,
                orderFactory=MarketOrderT,
                sideDistr=(lambda: random.randint(0,1)),
                volumeDistr=(lambda: random.expovariate(.1)),
                creationIntervalDistr=(lambda: random.expovariate(1.))):
    """ Creates a noise trader: a trader that randomly chooses a side and volume to trade
    book - book to place orders in
    orderFactoryT - order factory function (default: MarketOrderT)
    sideDistr - side of orders to create 
                            (default: discrete uniform distribution P(Sell)=P(Buy)=.5)
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    volumeDistr - defines volumes of orders to create
                            (default: exponential distribution with \lambda=1)
    """

    return TwoSideTrader(book, orderFactory,
                                Timer(creationIntervalDistr),
                                lambda _: (sideDistr(), (int(volumeDistr()),)))


class Signal(object):
    """ A discrete signal with user-defined increments   
    """

    def __init__(self,
                 initialValue=0,
                 deltaDistr=(lambda: random.normalvariate(0.,1.)),
                 intervalDistr=(lambda: random.expovariate(1.)),
                 label=None):
        """ Initializes a signal
        initialValue - initial value of the signal (default: 0)
        deltaDistr - increment function (default: normal distribution with \mu=0, \sigma=1)
        intervalDistr - defines intervals between signal updates
        """

        self.on_changed = Event()
        
        self.label = label if label is not None else "#"+str(id(self))
        
        self.value = initialValue
        self.attributes = {"smooth":True}

        def wakeUp(_):
            self.value += deltaDistr()
            self.on_changed.fire(self)

        Timer(intervalDistr).advise(wakeUp)

    def advise(self, listener):
        """ Subscribes 'listener' to value changed events 
        """
        self.on_changed += listener

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

def SignalTrader( book,
                  signal,
                  threshold=0.7,
                  orderFactory=MarketOrderT,
                  volumeDistr=(lambda: random.expovariate(1.))):
    """ Creates a signal trader.
    book - book to place orders in
    signal - signal to be listened to 
    threshold - threshold when the trader starts to act
    orderFactory - order factory function: side -> *orderParams -> Order
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    return TwoSideTrader(book, orderFactory, signal, 
                         signalTraderFunc(threshold, volumeDistr, 
                                          lambda: signal.value))
        
def TrendFollower(book,
                  average = ewma(alpha = 0.15),
                  threshold = 0., 
                  orderFactory=MarketOrderT,
                  creationIntervalDistr=(lambda: random.expovariate(1.)),
                  volumeDistr=(lambda: random.expovariate(1.))):
    """ Creates a trend follower trader
    book - book to place orders in
    average - moving average object (update(time,value); derivativeAt(time))
    threshold - threshold of the moving average derivate when the trader starts to act
    orderFactory - order factory function: side -> *orderParams -> Order
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    
    trend = Fold(AssetPrice(book), average)
    
    return TwoSideTrader(book, orderFactory, Timer(creationIntervalDistr), 
                         signalTraderFunc(threshold, volumeDistr, trend.derivative))

