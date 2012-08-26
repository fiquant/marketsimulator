import heapq
import math

from marketsim import Side, Event


class OrderQueue(object):
    """ Queue of limit orders at one side (Sell or Buy).
    It is implemented over a heap so has following comlexity for operations:
    - pushing order: O(logN)
    - accessing to the best order: O(1)
    - popping the best order: O(logN)
    """
    def __init__(self, tickSize=1, book=None):
        """ Initializes an empty queue with given tickSize 
        and remembers order book the queue belong to if any
        """
        self._elements = []         # pairs ((signedTicks, arrivalSeqNo), order) kept in a heap
        self._tickSize = tickSize   # tick size
        self._counter = 0           # arrival order counter
        self.on_best_changed = Event()  # event to be called when the best order changes
        self._lastBest = None       # pair (bestPrice, bestVolume)
        self._lastPrice = None      # last valid price
        self._book = book           # book the queue belongs to if any

    @property
    def book(self):
        """ Book the queue belongs to if any
        """
        return self._book

    def notifyIfBestChanged(self):
        """Notifies order queue listeners if the best order has changed
        """
        best = self.best
        bestpv = None if best is None else (best.price, best.volume)
            
        if bestpv != self._lastBest:
            self._lastBest = bestpv
            if bestpv != None:
                self._lastPrice = bestpv[0]
            self.on_best_changed.fire(self)
            
    @property
    def lastPrice(self):
        return self._lastPrice
            
    def __str__(self):
        return type(self).__name__ + "(" + str(self._elements) + ")"

    def __repr__(self):
        return self.__str__()

    def push(self, order):
        """ Pushes 'order' into the queue.
        May correct limit price of the order with respect to the tick size
        May notify listeners about that the best order changed 
        """
        (ticks, correctedPrice) = self.ticks(order.price)
        if order.price != correctedPrice:
            # save corrected price in the order if needed
            order.price = correctedPrice
        heapq.heappush(self._elements, ((ticks, self._counter), order))
        self._counter += 1
        # notify listeners if the best order changed
        self.notifyIfBestChanged()

    def _makeValid(self):
        """ Ensures that the queue is either empty or has a valid order on top
        Valid order == not empty and not cancelled
        Returns True iff the queue is not empty
        """
        while self._elements != []:
            (_, top) = self._elements[0]
            if top.empty or top.cancelled:
                heapq.heappop(self._elements)
            else:
                return True
        return False

    @property
    def empty(self):
        """ Returns True iff queue is empty
        May remove invalid orders from it 
        """
        return not self._makeValid()

    @property
    def best(self):
        """ Returns the best order if any 
        Otherwise returns None 
        """
        return self._elements[0][1] if self._makeValid() else None

    def matchWith(self, other):
        """ Matches an order against our order queue
        Returns True iff the incoming order is matched completely
        The order is considered as market order for the moment
        May notify listeners if the best order changed
        """
        # while there are orders
        while not self.empty:
            # take the best one
            (_, top) = self._elements[0]
            # match the incoming order with our best one
            # and if our best order becomes empty,
            if not other.empty and top.matchWith(other):
                # remove it from the queue
                self._makeValid()
            else:
                # our best order is not matched completely
                break
        self.notifyIfBestChanged()
        return other.empty

    def withPricesBetterThan(self, limit, idx=0):
        """ Enumerates orders with price better than or equal to 'limit'
        """
        if len(self._elements) <= idx:
            return
        if not self.better(limit, self._elements[idx][1].price):
            yield self._elements[idx][1]
            for x in self.withPricesBetterThan(limit, idx * 2 + 1):
                yield x
            for x in self.withPricesBetterThan(limit, idx * 2 + 2):
                yield x
                
    def volumeWithPriceBetterThan(self, limit):
        """ Returns total volume of orders having price better than or equal to 'limit'
        """
        return sum([x.volume for x in self.withPricesBetterThan(limit)])


class Bids(OrderQueue):
    """ Queue of limit orders buy
    """
    
    def __init__(self, *args):
        OrderQueue.__init__(self, *args)
        
    @property
    def label(self):
        return self.book.label + "_{Bids}"

    def ticks(self, price):
        """ Corrects 'price' with respect to the tick size
        Returns signed integer number of ticks for the price 
        and corrected unsigned order price
        """
        ticks = int(math.floor(price / self._tickSize))
        return (-ticks, ticks * self._tickSize)

    @staticmethod
    def better(x, y):
        """ Predicate to compare two signed ticks
        """
        return x > y

    side = Side.Buy


class Asks(OrderQueue):
    """ Queue of limit orders buy
    """
    
    def __init__(self, *args):
        OrderQueue.__init__(self, *args)

    @property
    def label(self):
        return self.book.label + "^{Asks}"

    def ticks(self, price):
        """ Corrects 'price' with respect to the tick size
        Returns signed integer number of ticks for the price 
        and corrected unsigned order price
        """
        ticks = int(math.ceil(price / self._tickSize))
        return (ticks, ticks * self._tickSize)

    @staticmethod
    def better(x, y):
        """ Predicate to compare two signed ticks
        """
        return x < y

    side = Side.Sell


class OrderBook(object):
    """ Order book for a single asset in a market
    Maintains two order queues for orders of different sides
    """
    def __init__(self, tickSize=1, label=""):
        """ Initializes empty order book with given tick size
        """
        self._bids = Bids(tickSize, self)
        self._asks = Asks(tickSize, self)
        # queues indexed by their side
        self._queues = [0, 0]
        self._queues[self._bids.side] = self._bids
        self._queues[self._asks.side] = self._asks
        self._tickSize = tickSize
        self.label = label

    def queue(self, side):
        """ Returns queue of the given side
        """
        return self._queues[side]

    @property
    def tickSize(self):
        """ Returns the tick side
        """
        return self._tickSize

    def __str__(self):
        return type(self).__name__ + "(" + str(self._bids) + ", " + str(self._asks) + ")"

    def __repr__(self):
        return self.__str__()

    def process(self, order):
        """ Processes an order by calling its processIn method
        """
        order.processIn(self)

    def processLimitOrder(self, order):
        """ Processes 'order' as limit order:
        If it is not matched completely, it stays at the order queue
        """
        if not self.processMarketOrder(order):
            self._queues[order.side].push(order)

    def processMarketOrder(self, order):
        """ Processes 'order' as market order:
        Iff it is not matched completely, returns False
        """
        otherSide = Side.opposite(order.side)
        return self._queues[otherSide].matchWith(order)

    @property
    def bids(self):
        """ Returns buy side order queue
        """
        return self._bids

    @property
    def asks(self):
        """ Returns sell side order queue
        """
        return self._asks

    @property 
    def price(self):
        """ Returns middle arithmetic price if buy and sell sides are not empty,
        None otherwise 
        """
        return None if self.asks.empty or self.bids.empty \
                    else (self.asks.best.price + self.bids.best.price) / 2.0
                    
    @property
    def spread(self):
        """ Returns spread between sell and buy side if they are not empty,
        None otherwise
        """
        return None if self.asks.empty or self.bids.empty \
                    else self.asks.best.price - self.bids.best.price
                    
