from marketsim import registry, bind, observable, event, meta
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
        self._onMatchedWith = bind.Method(self, '_onMatchedWith_impl')
        self._onPriceChanged = bind.Method(self, '_onPriceChanged_impl')
        self._onStopLossMatched = bind.Method(self, '_onStopLossMatched_impl')
        
        
        
    def processIn(self, book):
        self._book = book
        self._current = self._orderFactory(self._side)(self._volume)
        self._orderSubscription = event.subscribe(self._current.on_matched, 
                                                  self._onMatchedWith, 
                                                  self, {})
        self._book.processMarketOrder(self._current)
        self._price = observable.Price(self._book)   
        
    def _onMatchedWith_impl(self, order, other, (price, volume)):
        self._orderSubscription.dispose()
        self.onMatchedWith(other, (price, volume))
        self._orderPrice = price
        self._stopSubscription = event.subscribe(
                                self._book.on_price_changed,
                                self._onPriceChanged,
                                self)
        self._stopSubscription.bind(None) 

    def _onPriceChanged_impl(self, _):
        if self._price is not None and self._price() is not None:
            if (self._side == Side.Sell and  (1+self._maxLoss) * self._orderPrice < self._price() ) \
                or (self.side == Side.Buy and (1-self._maxLoss) * self._orderPrice > self._price() ):
                # the stoploss is activated
                self._stopSubscription.dispose()
                
                # the order now changes sides
                self._side = self._side.opposite
                self._stopLossOrder = MarketFactory(self._side)(self._totalVolume)
                
                self._stopLossMatch = event.subscribe(self._stopLossOrder.on_matched, 
                                                      self._onStopLossMatched, 
                                                      self, {})
                self._book.processMarketOrder(self._stopLossOrder)
            
    def _onStopLossMatched_impl(self, order, other, (price, volume)):
        self._stopLossMatch.dispose()
        #print "stoploss: ", self._current.side, self._orderPrice, self._price()
        self.onMatchedWith(other, (price, volume))
    
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
