from marketsim import ops, Side, types, combine, registry, context, bind, observable, event, meta, _
from .. import _market, _limit
import _meta

from marketsim.types import *

class StopLoss(_meta.Base):
    
    def __init__(self, proto, maxloss):
        
        _meta.Base.__init__(self, proto.volumeUnmatched)
        
        self.side = proto.side
        self._proto = proto
        self._maxloss = maxloss
        self._stopLossOrder = None
        
    def startProcessing(self):
        self._obsPrice = observable.AskPrice(self.orderBook) \
                            if self.side == Side.Buy else \
                         observable.BidPrice(self.orderBook)   
        self.send(self._proto)
        
    def onOrderMatched(self, order, price, volume):
        if order is not self._stopLossOrder:
            if volume > 0:
                handler = event.GreaterThan((1+self._maxloss) * price, _(self)._onPriceChanged)\
                            if self.side == Side.Sell else\
                          event.LessThan((1-self._maxloss) * price, _(self)._onPriceChanged)
                            
                self._stopSubscription = event.subscribe(self._obsPrice, handler, self, self._ctx)
                self.onMatchedWith(price, +volume)
        else:
            self.onMatchedWith(price, -volume)
        
    def _onPriceChanged(self, dummy):
        # the stoploss is activated
        self._stopSubscription.dispose()
        self._stopLossOrder = self.send(_market.Order(self.side.opposite, 
                                                      self.volumeFilled))
                

class Factory(types.IOrderGenerator): # in fact it is IPersistentOrderGenerator
    
    def __init__(self, maxloss, inner = _market.Factory()):
        self.maxloss = maxloss
        self.inner = inner
        
    _properties = {
        'maxloss': types.IFunction[float],
        'inner'  : types.IOrderGenerator,  
    }

    def __call__(self):
        maxloss = self.maxloss()
        proto = self.inner()
        return StopLoss(proto, maxloss) \
            if maxloss is not None and proto is not None else None 

@registry.expose(['Stoploss'])    
@sig((IFunction[Side],), IOrderGenerator)
class Side_Factory(object):
    
    def __init__(self, 
                 maxloss = ops.constant(0.1), 
                 factory = _market.Side_Factory()):
        self.maxloss = maxloss
        self.factory = factory
        
    _properties = {
        'maxloss':  IFunction[float],
        'factory' : meta.function((IFunction[Side],), IOrderGenerator)
    }
    
    def __call__(self, side):
        return Factory(self.maxloss, self.factory(side))

@registry.expose(['Stoploss'])    
@sig((IFunction[Side],IFunction[float]), IOrderGenerator)
class SidePrice_Factory(object):
    
    def __init__(self, 
                 maxloss = ops.constant(0.1), 
                 factory = _limit.SidePrice_Factory()):
        self.maxloss = maxloss
        self.factory = factory
        
    _properties = {
        'maxloss':  IFunction[float],
        'factory' : function((IFunction[Side],IFunction[float]), IOrderGenerator)
    }
    
    def __call__(self, side, price):
        return Factory(self.maxloss, self.factory(side, price))
