from marketsim import registry, bind, observable, event, meta, _
from _market import MarketFactory

from _base import Base
from marketsim.types import *


class StopLoss(Base):
    
    def __init__(self, maxLoss, factory, side, volume):
        
        Base.__init__(self, side, volume)
        
        self._orderFactory = factory
        self._maxLoss = maxLoss
        self._current = None
        self._orderPrice = None
        self._totalVolume = volume
        self._price = None
        
    def processIn(self, book):
        self._book = book
        self._current = self._orderFactory(self._side)(self._volume)
        self._orderSubscription = event.subscribe(self._current.on_matched, 
                                                  _(self).onMatchedWith, 
                                                  self, {})
        self._book.processMarketOrder(self._current)
        self._price = observable.Price(self._book)   
        
    def onMatchedWith(self, order, other, (price, volume)):
        self._orderSubscription.dispose()
        Base.onMatchedWith(self, other, (price, volume))
        self._orderPrice = price
        handler = event.GreaterThan((1+self._maxLoss) * self._orderPrice, _(self)._onPriceChanged)\
                    if self._side == Side.Sell else\
                  event.LessThan((1-self._maxLoss) * self._orderPrice, _(self)._onPriceChanged)
                    
        self._stopSubscription = event.subscribe(
                                self._book.on_price_changed,
                                handler,
                                self)
        self._stopSubscription.bind(None) 

    def _onPriceChanged(self, dummy):
        if self._price is not None and self._price() is not None:
#            if (self._side == Side.Sell and  (1+self._maxLoss) * self._orderPrice < self._price() ) \
#                or (self.side == Side.Buy and (1-self._maxLoss) * self._orderPrice > self._price() ):
                # the stoploss is activated
                self._stopSubscription.dispose()
                
                # the order now changes sides
                self._side = self._side.opposite
                self._stopLossOrder = MarketFactory(self._side)(self._totalVolume)
                
                self._stopLossMatch = event.subscribe(self._stopLossOrder.on_matched, 
                                                      _(self)._onStopLossMatched, 
                                                      self, {})
                self._book.processMarketOrder(self._stopLossOrder)
            
    def _onStopLossMatched(self, order, other, (price, volume)):
        self._stopLossMatch.dispose()
        #print "stoploss: ", self._current.side, self._orderPrice, self._price()
        Base.onMatchedWith(self, other, (price, volume))
    
MarketOrderFactorySignature = function(args=(Side,), rv=function((Volume,), IOrder))

@registry.expose(['StopLoss'])
class StopLossFactory(object):
    
    def __init__(self, maxLoss = 0.1, orderFactory = MarketFactory):
        self.maxLoss = maxLoss
        self.orderFactory = orderFactory
        
    _types = [MarketOrderFactorySignature]
        
    _properties = {'maxLoss'  : float,
                   'orderFactory' : MarketOrderFactorySignature}
    
    def __call__(self, side):
        return bind.Construct(StopLoss, self.maxLoss, self.orderFactory, side)
