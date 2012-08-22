import random
from marketsim.scheduler import Timer, world
from marketsim import Side
from marketsim.order import *
from marketsim.indicator import AssetPrice
import math

class TraderBase(object):

    def __init__(self):
        self._PnL = 0
        self.on_order_sent = Event()
        self.on_traded = Event()

    def onOrderMatched(self, order, other, (price, volume)):
        pv = price * volume
        self._PnL += pv if order.side == Side.Sell else -pv
        
        self.on_traded.fire(self)

    @property
    def PnL(self):
        return self._PnL

    def makeSubscribedTo(self, order):
        order.on_matched += self.onOrderMatched
        return order
        
class SingleAssetTrader(TraderBase):

    def __init__(self):
        TraderBase.__init__(self)
        self._amount = 0

    def onOrderMatched(self, order, other, (price, volume)):
        self._amount += volume if order.side == Side.Buy else -volume
        TraderBase.onOrderMatched(self, order, other, (price,volume))
        
    def send(self, book, order):
        book.process(self.makeSubscribedTo(order))
        self.on_order_sent.fire(order)        

    @property
    def amount(self):
        return self._amount

class OneSideTrader(SingleAssetTrader):

    def __init__(   self,
                    orderBook,                 # book to place orders in
                    side,                        # side of orders to create
                    orderFactoryT,            # function to create orders
                    eventGen,                  # event generator to be listened
                    orderFunc):                # function to calculate order parameters

        SingleAssetTrader.__init__(self)

        self.side = side
        self.book = orderBook
        orderFactory = orderFactoryT(side)

        def wakeUp(signal):
            params = orderFunc(self)
            order = orderFactory(*params)
            self.send(orderBook, order)

        eventGen.advise(wakeUp)

class TwoSideTrader(SingleAssetTrader):

    def __init__(   self,
                    orderBook,                 # book to place orders in
                    orderFactoryT,            # function to create orders
                    eventGen,                  # event generator to be listened
                    orderFunc):                # function to calculate order parameters

        SingleAssetTrader.__init__(self)

        self.book = orderBook

        def wakeUp(signal):
            res = orderFunc(self)
            if res <> None:
                (side, params) = res
                order = orderFactoryT(side)(*params)
                self.send(orderBook, order)

        eventGen.advise(wakeUp)


def liquidityProviderFunc(defaultValue, priceDistr, volumeDistr):
    def inner(trader):
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

    def __init__(   self,
                    source=None,
                    cancellationIntervalDistr=(lambda: random.expovariate(1.)),
                    choiceFunc=lambda N: random.randint(0,N-1)):

        self._elements = []

        if source:
            source.on_order_sent += self.process

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

def fv_func(fundamentalValueFunc, volumeDistr):
    def inner(trader):
        side = None
        book = trader.book
        if not book.asks.empty and book.asks.best.price < fundamentalValueFunc():
            side = Side.Buy
        elif not book.bids.empty and book.bids.best.price > fundamentalValueFunc():
            side = Side.Sell
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

    return TwoSideTrader(book, orderFactory,
                                Timer(creationIntervalDistr),
                                fv_func(fundamentalValue, lambda _: volumeDistr()))
    
def DependanceTrader(book,
                     bookToDependOn,
                     orderFactory=MarketOrderT,
                     factor=1.,
                     volumeDistr=(lambda: random.expovariate(.1))):
    
    priceToDependOn = AssetPrice(bookToDependOn) 
    
    def wantedPrice():
        return priceToDependOn.value * factor
    
    def wantedVolume(side):
        oppositeQueue = book.queue(Side.opposite(side))
        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(wantedPrice())
        return min(oppositeVolume, volumeDistr())        

    return TwoSideTrader(book, orderFactory, priceToDependOn, fv_func(wantedPrice, wantedVolume))

def NoiseTrader(book,
                orderFactory=MarketOrderT,
                sideDistr=(lambda: random.randint(0,1)),
                volumeDistr=(lambda: random.expovariate(.1)),
                creationIntervalDistr=(lambda: random.expovariate(1.))):

    return TwoSideTrader(book, orderFactory,
                                Timer(creationIntervalDistr),
                                lambda _: (sideDistr(), (int(volumeDistr()),)))


class Signal(object):

    def advise(self, listener):
        self.on_changed += listener

    def __init__(self,
                 initialValue=0,
                 deltaDistr=(lambda: random.normalvariate(0.,1.)),
                 intervalDistr=(lambda: random.expovariate(1.))):

        self.on_changed = Event()
        self.value = initialValue

        def wakeUp(_):
            self.value += deltaDistr()
            self.on_changed.fire(self)

        Timer(intervalDistr).advise(wakeUp)

def signalTraderFunc(threshold, volumeDistr, signalFunc):
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
    
    return TwoSideTrader(book, orderFactory, signal, 
                         signalTraderFunc(threshold, volumeDistr, lambda: signal.value))

class EWMA(object):
    
    def __init__(self, alpha):
        self._alpha = alpha
        self._avg = None
        
    @property 
    def value(self):
        return self._avg
        
    def at(self, t):
        return \
            self._avg + (self._lastValue - self._avg)*(1 - (1 - self._alpha)**( t - self._lastTime)) \
            if self._avg is not None else None
    
    def derivativeAt(self, t):
        dt = t - self._lastTime
        return -(self._lastValue - self._avg)*math.log(1 - self._alpha)*(1 - self._alpha)**dt
        
    def update(self, time, value):
        self._avg = self.at(time) if self._avg is not None else value
        self._lastValue = value
        self._lastTime = time
        
class EWMA_Ex(EWMA):
    
    def __init__(self, source, alpha = 0.15):
        EWMA.__init__(self, alpha)
        source.on_changed += lambda _: self.update(world.currentTime, source.value)
      
def TrendFollower(book,
                  average = EWMA(alpha = 0.15),
                  threshold = 0., 
                  orderFactory=MarketOrderT,
                  creationIntervalDistr=(lambda: random.expovariate(1.)),
                  volumeDistr=(lambda: random.expovariate(1.))):
    
    AssetPrice(book).on_changed += \
        lambda assetPrice: average.update(world.currentTime, assetPrice.value)
    
    return TwoSideTrader(book, orderFactory, Timer(creationIntervalDistr), 
                         signalTraderFunc(threshold, volumeDistr, 
                                          lambda: average.derivativeAt(world.currentTime)))

