from marketsim import combine, registry, bind, observable, event, meta, _
from _market import MarketFactory

from marketsim.types import *

import _meta

class StopLoss(_meta.Base):
    
    def __init__(self, scheduler, maxLoss, factory, side, volume):
        
        _meta.Base.__init__(self, volume)
        
        self.side = side
        self._scheduler = scheduler
        self._orderFactory = factory
        self._maxLoss = maxLoss
        self._current = None
        self._orderPrice = None
        self._stopLossOrder = None
        self._price = None
        
    def processIn(self, book):
        self.orderBook = book
        self._obsPrice = observable.AskPrice(book) if self.side == Side.Buy else observable.BidPrice(book)   
        self._current = self.send(self._orderFactory(self.side)(self.volumeUnmatched))
        
    def onOrderMatched(self, order, price, volume):
        if order is not self._stopLossOrder:
            if volume > 0:
                handler = event.GreaterThan((1+self._maxLoss) * price, _(self)._onPriceChanged)\
                            if self.side == Side.Sell else\
                          event.LessThan((1-self._maxLoss) * price, _(self)._onPriceChanged)
                            
                self._stopSubscription = event.subscribe(self._obsPrice, handler, self, {})
                self.onMatchedWith(price, +volume)
        else:
            self.onMatchedWith(price, -volume)
        
    def _onPriceChanged(self, dummy):
        # the stoploss is activated
        self._stopSubscription.dispose()
        self._stopLossOrder = self.send(MarketFactory(self.side.opposite)(self.volumeFilled))
                

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
