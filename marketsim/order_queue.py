import heapq
import math

from marketsim import Side

class OrderQueue(object):

   def __init__(self, tickSize=1):
      self._elements = []
      self._tickSize = tickSize
      self._counter = 0
      self.on_best_changed = set()
      self._lastBest = None

   def notifyIfBestChanged(self):
      if self._elements == []:
         if self._lastBest <> None:
            for x in self.on_best_changed:
               x(self, None)
      else:
         best = self._elements[0][1]
         bestpv = (best.price, best.volume)
         if self._lastBest <> bestpv:
            self._lastBest = bestpv
            for x in self.on_best_changed:
               x(self, best)

   def __str__(self):
      return type(self).__name__ + "(" + str(self._elements) + ")"

   def __repr__(self):
      return self.__str__()

   def push(self, order):
      (ticks, corrected) = self.ticks(order.price)
      if order.price <> corrected:
         order.price = corrected
      heapq.heappush(self._elements, ((ticks, self._counter), order))
      self._counter += 1
      self.notifyIfBestChanged()

   def makeValid(self):
      while self._elements <> []:
         (_,top) = self._elements[0]
         if top.empty or top.cancelled:
            heapq.heappop(self._elements)
         else:
            return True
      return False

   @property
   def empty(self):
      return not self.makeValid()

   @property
   def best(self):
      return self._elements[0][1] if self.makeValid() else None

   """
   Matches an order against our order queue
   Returns True iff the order is matched completely
   """
   def matchWith(self, other):
      while not self.empty:
         (_,top) = self._elements[0]
         if not other.empty and top.matchWith(other):
            heapq.heappop(self._elements)
         else:
            break
      self.notifyIfBestChanged()
      return other.empty

   def withPricesBetterThen(self, limit, idx=0):
      if len(self._elements) <= idx:
         return
      if not self.better(limit, self._elements[idx][1].price):
         yield self._elements[idx][1]
         for x in self.withPricesBetterThen(limit, idx*2+1):
            yield x
         for x in self.withPricesBetterThen(limit, idx*2+2):
            yield x

def oppositeSide(side):
   return 1 - side

class Bids(OrderQueue):
   def __init__(self, tickSize=1):
      OrderQueue.__init__(self, tickSize)

   def ticks(self, price):
      ticks = int(math.floor(price / self._tickSize))
      return (-ticks, ticks*self._tickSize)

   @staticmethod
   def better(x,y):
      return x > y

   side = Side.Buy

class Asks(OrderQueue):
   def __init__(self, tickSize=1):
      OrderQueue.__init__(self, tickSize)

   def ticks(self, price):
      ticks = int(math.ceil(price / self._tickSize))
      return (ticks, ticks*self._tickSize)

   @staticmethod
   def better(x,y):
      return x < y

   side = Side.Sell

class OrderBook(object):
   def __init__(self, tickSize = 1):
      self._bids = Bids(tickSize)
      self._asks = Asks(tickSize)
      self._queues = [0,0]
      self._queues[self._bids.side] = self._bids
      self._queues[self._asks.side] = self._asks
      self._tickSize = tickSize

   def queue(self, side):
      return self._queues[side]

   @property
   def tickSize(self):
      return self._tickSize

   def __str__(self):
      return type(self).__name__ + "(" + str(self._bids) + ", " + str(self._asks) + ")"

   def __repr__(self):
      return self.__str__()

   def process(self, order):
      order.processIn(self)

   def processLimitOrder(self, order):
      orderSide = order.side
      if not self.processMarketOrder(order):
         self._queues[order.side].push(order)

   def processMarketOrder(self, order):
      otherSide = oppositeSide(order.side)
      return self._queues[otherSide].matchWith(order)

   @property
   def bids(self):
      return self._bids

   @property
   def asks(self):
      return self._asks

