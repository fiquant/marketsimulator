from marketsim import combine, registry, bind, observable, event, meta, _
from _market import MarketFactory

from _base import Base
from marketsim.types import *


class StopLoss(Base):
    
    def __init__(self, scheduler, maxLoss, factory, side, volume):
        
        Base.__init__(self, side, volume)
        
        self._scheduler = scheduler
        self._orderFactory = factory
        self._maxLoss = maxLoss
        self._current = None
        self._orderPrice = None
        self._totalVolume = volume
        self._stopLossOrder = None
        self._price = None
        
    def processIn(self, book):
        self._book = book
        self._current = self._orderFactory(self._side)(self._volume)
        self._current.owner = self
        self._price = observable.MidPrice(self._book)   
        self._book.processMarketOrder(self._current)
        
    def _onOrderMatched(self, order, other, (price, volume)):
        if order is not self._stopLossOrder:
            self._orderPrice = price
            handler = event.GreaterThan((1+self._maxLoss) * self._orderPrice, _(self)._onPriceChanged)\
                        if self._side == Side.Sell else\
                      event.LessThan((1-self._maxLoss) * self._orderPrice, _(self)._onPriceChanged)
                        
            self._stopSubscription = event.subscribe(self._price, handler, self, {})
        self.owner._onOrderMatched(self, other, (price, volume))
        
    def _onOrderCancelled(self, order):
        self.owner._onOrderCancelled(self)
    
    def _onOrderCharged(self, price):
        self.owner._onOrderCharged(price)    
        
    def _onPriceChanged(self, dummy):
        # the stoploss is activated
        self._stopSubscription.dispose()
        
        # the order now changes sides
        self._side = self._side.opposite
        self._stopLossOrder = MarketFactory(self._side)(self._totalVolume)
        self._stopLossOrder.owner = self
        self._book.processMarketOrder(self._stopLossOrder)
                

class Factory(IOrderGenerator, combine.SideVolumeMaxLoss): # in fact it is IPersistentOrderGenerator
    
    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        params = combine.SideVolumeMaxLoss.__call__(self)
        if params is not None:
            (side, volume, maxloss) = params
            order = StopLoss(self._scheduler, maxloss, MarketFactory, side, volume)
            return order
        return None

    
MarketOrderFactorySignature = function(args=(Side,), rv=function((Volume,), IOrder))

@registry.expose(['StopLoss'])
class StopLossFactory(object):
    
    def __init__(self, maxLoss = 0.1, orderFactory = MarketFactory):
        self.maxLoss = maxLoss
        self.orderFactory = orderFactory
        
    def bind(self, ctx):
        self.scheduler = ctx.world
        
    _types = [MarketOrderFactorySignature]
        
    _properties = {'maxLoss'  : float,
                   'orderFactory' : MarketOrderFactorySignature}
    
    def __call__(self, side):
        return bind.Construct(StopLoss, self.scheduler, self.maxLoss, self.orderFactory, side)
