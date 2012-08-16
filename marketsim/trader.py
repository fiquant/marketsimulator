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


class LiquidityProvider(SingleAssetTrader):

   def __init__(self,
                orderBook,
                side=Side.Sell,
                orderFactoryT=LimitOrderT,
                defaultValue=100,
                creationIntervalDistr=(lambda: random.expovariate(1.)),
                priceDistr=(lambda: random.lognormvariate(0., .1)),
                volumeDistr=(lambda: random.expovariate(.1))):

      SingleAssetTrader.__init__(self)

      orderFactory = orderFactoryT(side)

      self._side = side

      def wakeUp(_):
         queue = orderBook.queue(side)
         currentPrice = queue.best.price if not queue.empty else defaultValue
         price = currentPrice * priceDistr()
         volume = int(volumeDistr())
         order = orderFactory(price,volume)
         self.send(orderBook, order)

      Timer(creationIntervalDistr).advise(wakeUp)

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

class FVTrader(SingleAssetTrader):

   def __init__(self,
                book,
                orderFactory=MarketOrderT,
                fundamentalValue=100,
                volumeDistr=(lambda: random.expovariate(.1)),
                creationIntervalDistr=(lambda: random.expovariate(1.))):

      SingleAssetTrader.__init__(self)

      def wakeUp(_):
         side = None
         if not book.asks.empty and book.asks.best.price < fundamentalValue:
            side = Side.Buy
         if not book.bids.empty and book.bids.best.price > fundamentalValue:
            side = Side.Sell
         if side <> None:
            volume = int(volumeDistr())
            order = orderFactory(side)(volume)
            self.send(book, order)

      Timer(creationIntervalDistr).advise(wakeUp)

class NoiseTrader(SingleAssetTrader):

   def __init__(self,
                book,
                orderFactory=MarketOrderT,
                sideDistr=(lambda: random.randint(0,1)),
                volumeDistr=(lambda: random.expovariate(.1)),
                creationIntervalDistr=(lambda: random.expovariate(1.))):

      SingleAssetTrader.__init__(self)

      def wakeUp(_):
         side = sideDistr()
         volume = int(volumeDistr())
         order = orderFactory(side)(volume)
         self.send(book, order)

      Timer(creationIntervalDistr).advise(wakeUp)

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

class SignalTrader(SingleAssetTrader):

   def __init__(self,
                book,
                signal,
                threshold=0.7,
                orderFactory=MarketOrderT,
                volumeDistr=(lambda: random.expovariate(1.))):

      SingleAssetTrader.__init__(self)
      def onSignalChanged(signal):
         value = signal.value
         side = Side.Buy if value > threshold else Side.Sell if value < -threshold else None
         if side<>None:
            self.send(book, orderFactory(side)(volumeDistr()))

      signal.advise(onSignalChanged)
