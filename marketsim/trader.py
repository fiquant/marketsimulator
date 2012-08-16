import random
from marketsim.scheduler import *
from marketsim import Side
from marketsim.order import *

class TraderBase(object):

   def __init__(self):
      self._PnL = 0
      self.on_order_sent = set()
      self.on_traded = set()

   def onOrderMatched(self, order, other, (price, volume)):
       pv = price*volume
       if order.side == Side.Buy:
          pv = -pv
       self._PnL += pv

       for x in self.on_traded:
           x(self)

   @property
   def PnL(self):
       return self._PnL

   def send(self, book, order):
      order.on_matched.add(self.onOrderMatched)
      book.process(order)
      for x in self.on_order_sent: x(order)

class SingleAssetTrader(TraderBase):

   def __init__(self):
       TraderBase.__init__(self)
       self._amount = 0

   def onOrderMatched(self, order, other, (price, volume)):
       self._amount += volume if order.side == Side.Buy else -volume
       TraderBase.onOrderMatched(self, order, other, (price,volume))

   @property
   def amount(self):
      return self._amount

class OneSideTrader(SingleAssetTrader):

   def __init__(self,
                orderBook,             # book to place orders in
                side,                  # side of orders to create
                orderFactoryT,         # function to create orders
                eventGen,              # event generator to be listened
                orderFunc):            # function to calculate order parameters

      SingleAssetTrader.__init__(self)

      self.side = side
      self.book = orderBook
      orderFactory = orderFactoryT(side)

      def wakeUp(signal):
         params = orderFunc(self, signal)
         order = orderFactory(*params)
         self.send(orderBook, order)

      eventGen.advise(wakeUp)

class TwoSideTrader(SingleAssetTrader):

   def __init__(self,
                orderBook,             # book to place orders in
                orderFactoryT,         # function to create orders
                eventGen,              # event generator to be listened
                orderFunc):            # function to calculate order parameters

      SingleAssetTrader.__init__(self)

      self.book = orderBook

      def wakeUp(signal):
         res = orderFunc(self, signal)
         if res <> None:
            (side, params) = res
            order = orderFactoryT(side)(*params)
            self.send(orderBook, order)

      eventGen.advise(wakeUp)


def liquidityProviderFunc(defaultValue, priceDistr, volumeDistr):
   def inner(trader,_):
      queue = trader.book.queue(trader.side)
      currentPrice = queue.best.price if not queue.empty else defaultValue
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

   return OneSideTrader(orderBook,
                        side,
                        orderFactoryT,
                        Timer(creationIntervalDistr),
                        liquidityProviderFunc(defaultValue, priceDistr, volumeDistr))



class Canceller(object):

   def __init__(self,
                source=None,
                cancellationIntervalDistr=(lambda: random.expovariate(1.)),
                choiceFunc=lambda N: random.randint(0,N-1)):

      self._elements = []

      if source:
         source.on_order_sent.add(self.process)

      def wakeUp(_):
         while self._elements <> []:
            N = len(self._elements)
            idx = choiceFunc(N)
            e = self._elements[idx]
            if e.empty or e.cancelled:
               if e <> self._elements[-1]:
                  self._elements[idx] = self._elements[-1]
               self._elements.pop()
            else:
               e.cancel()
               return

      Timer(cancellationIntervalDistr).advise(wakeUp)

   def process(self, order):
      self._elements.append(order)

def fv_func(fundamentalValue, volumeDistr):
   def inner(trader, _):
      side = None
      book = trader.book
      if not book.asks.empty and book.asks.best.price < fundamentalValue:
         side = Side.Buy
      if not book.bids.empty and book.bids.best.price > fundamentalValue:
         side = Side.Sell
      if side <> None:
         volume = int(volumeDistr())
         return (side, (volume,))
      return None
   return inner

def FVTrader(   book,
                orderFactory=MarketOrderT,
                fundamentalValue=100,
                volumeDistr=(lambda: random.expovariate(.1)),
                creationIntervalDistr=(lambda: random.expovariate(1.))):

   return TwoSideTrader(book, orderFactory,
                        Timer(creationIntervalDistr),
                        fv_func(fundamentalValue, volumeDistr))

def NoiseTrader(book,
                orderFactory=MarketOrderT,
                sideDistr=(lambda: random.randint(0,1)),
                volumeDistr=(lambda: random.expovariate(.1)),
                creationIntervalDistr=(lambda: random.expovariate(1.))):

   return TwoSideTrader(book, orderFactory,
                        Timer(creationIntervalDistr),
                        lambda _,__: (sideDistr(), (int(volumeDistr()),)))


class Signal(object):

   def advise(self, listener):
      self.on_changed.add(listener)

   def __init__(self,
                initialValue=0,
                deltaDistr=(lambda: random.normalvariate(0.,1.)),
                intervalDistr=(lambda: random.expovariate(1.))):

      self.on_changed = set()
      self.value = initialValue

      def wakeUp(_):
         self.value += deltaDistr()
         for x in self.on_changed:
             x(self)

      Timer(intervalDistr).advise(wakeUp)

def signalFunc(threshold, volumeDistr):
   def inner(trader, signal):
      value = signal.value
      side = Side.Buy if value > threshold else Side.Sell if value < -threshold else None
      return (side, (volumeDistr(),)) if side<>None else None
   return inner

def SignalTrader(book,
                 signal,
                 threshold=0.7,
                 orderFactory=MarketOrderT,
                 volumeDistr=(lambda: random.expovariate(1.))):

   return TwoSideTrader(book, orderFactory, signal, signalFunc(threshold, volumeDistr))
