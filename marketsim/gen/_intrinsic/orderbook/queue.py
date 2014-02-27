import heapq
import math

from marketsim import  _, types, ops

from marketsim.gen._out._observable._observablefloat import Observablefloat

class BestPrice(Observablefloat):

    def __init__(self, queue):
        Observablefloat.__init__(self)
        self.queue = queue

    @property
    def digits(self):
        return self.queue.book._digitsToShow

    @property
    def label(self):
        return self.queue.label

    def __call__(self):
        return None if self.queue.empty else self.queue.best.price


class LastTrade(Observablefloat):

    def __init__(self):
        Observablefloat.__init__(self)
        self._lastTrade = None

    def set(self, value):
        self._lastTrade = value
        self.fire(self)

    def _retranslate(self, source):
        self.set(source())


    # return (price, volume) of the last trade or None
    def __call__(self):
        return self._lastTrade

class Queue(object):
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
        self._tickSize = tickSize   # tick size
        self._book = book           # book the queue belongs to if any
        self.lastTrade = LastTrade()
        self.reset()
        self.bestPrice = BestPrice(self)

    def reset(self):
        self._elements = []         # pairs ((signedTicks, arrivalSeqNo), order) kept in a heap
        self._counter = 0           # arrival order counter
        self._lastBest = None       # pair (bestPrice, bestVolume)

    def bind(self, ctx):
        self._scheduler = ctx.world

    @property
    def book(self):
        """ Book the queue belongs to if any
        """
        return self._book

    def notifyIfBestChanged(self):
        """Notifies order queue listeners if the best order has changed
        """
        best = self.best
        bestpv = None if best is None else (best.price, best.volumeUnmatched)

        if bestpv != self._lastBest:
            self._lastBest = bestpv
            self._scheduler.async(_(self.bestPrice, self).fire)

    def __str__(self):
        return type(self).__name__ + "(" + str(self._elements) + ")"

    def __repr__(self):
        return self.__str__()

    def ticks(self, price):
        """ Corrects 'price' with respect to the tick size
        Returns signed integer number of ticks for the price
        and corrected unsigned order price
        """
        ticks = int(math.ceil(self.side.makePriceSigned(price) / self._tickSize))
        return (+ticks, self.side.makePriceSigned(ticks * self._tickSize))

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

    def cancelOrder(self, order):
        """ To be called when 'order' is marked as cancelled
        May fire 'on_best_changed' event
        """
        order.cancel()
        self._makeValid()
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

    def _match(self, top, other):
        if other.canBeMatched(top):
            pv = top.matchWith(other)
            if pv[1]:
                self.lastTrade.set(pv)
            if top.empty:
                # remove it from the queue
                self._makeValid()
                return True
        return False


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
            if not self._match(top, other):
                break
        self.notifyIfBestChanged()
        return other.empty

    @property
    def sorted(self):
        """ Enumerates orders in order of their price
        Enumeration best M orders requires O(MlogM) operations
        """
        if self._elements <> []:
            def nth(i):
                return (self._elements[i][0], i)
            grey = [nth(0)]
            while grey <> []:
                (_, idx) = heapq.heappop(grey)
                yield self._elements[idx][1]
                if idx * 2 + 1 < len(self._elements):
                    heapq.heappush(grey, nth(idx * 2 + 1))
                if idx * 2 + 2 < len(self._elements):
                    heapq.heappush(grey, nth(idx * 2 + 2))

    @property
    def sortedPVs(self):
        lastPV = (None, None)
        for x in self.sorted:
            if not x.cancelled and not x.empty:
                if x.price == lastPV[0]:
                    lastPV = (x.price, lastPV[1] + x.volumeUnmatched)
                else:
                    if lastPV[0] is not None:
                        yield lastPV
                    lastPV = (x.price, x.volumeUnmatched)
        if lastPV[0] is not None:
            yield lastPV

    def evaluateOrderPrice(self, volume):
        """ Evaluates price for a potential market order with given 'volume'
        Returns pair (price, volume_unmatched) where 'volume_unmatched' may be positive
        if there is not enough volume in the order queue
        Complexity of the operation: O(MlogM) where M - number of orders involved
        """
        price = 0
        for x in self.sorted:
            if volume > 0:
                v = min(volume, x.volumeUnmatched)
                price += x.price * v
                volume -= v
            else:
                break
        return (price, volume)

    def getVolumePrices(self, volumes):
        deltas = [volumes[0]] + [volumes[i] - volumes[i-1] for i in range(1, len(volumes))]
        i = 0
        lastPrice = None
        for x in self.sorted:
            v = x.volumeUnmatched
            lastPrice = x.price
            while i < len(deltas) and v > 0:
                if v > deltas[i]:
                    yield (volumes[i], x.price)
                    v -= deltas[i]
                    i += 1
                else:
                    deltas[i] -= v
                    break
            if i == len(deltas):
                return
        if i < len(deltas):
            yield (volumes[i], lastPrice)
            i += 1
        while i < len(deltas):
            yield (volumes[i], None)
            i += 1

    def withPricesBetterThan(self, limit, idx=0):
        """ Enumerates orders with price better than or equal to 'limit'
        """
        if len(self._elements) <= idx:
            return
        if not self.side.better(limit, self._elements[idx][1].price):
            yield self._elements[idx][1]
            for x in self.withPricesBetterThan(limit, idx * 2 + 1):
                yield x
            for x in self.withPricesBetterThan(limit, idx * 2 + 2):
                yield x

    def volumeWithPriceBetterThan(self, limit):
        """ Returns total volume of orders having price better than or equal to 'limit'
        """
        return sum([x.volumeUnmatched for x in self.withPricesBetterThan(limit)])

    def pvsForFixedBudget(self, budget):
        """ Returns (price, volume) for limit orders to be placed
            in order to buy or sell assets on total *price*
        """
        for p,v in self.sortedPVs:
            pv = p*v
            if pv < budget:
                yield p,v
                budget -= pv
            else:
                yield p, int(math.floor(budget / p))
                return
