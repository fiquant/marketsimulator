from marketsim import Side, event, _
from .. import market
import _meta

from marketsim.gen._out.orderbook.ask._price import Price as AskPrice
from marketsim.gen._out.orderbook.bid._price import Price as BidPrice

from marketsim.types import *

class Order_Impl(_meta.Base):
    
    def __init__(self, maxloss, proto):
        
        _meta.Base.__init__(self, proto.volumeUnmatched)
        
        self.side = proto.side
        self._proto = proto
        self._maxloss = maxloss
        self._stopLossOrder = None
        
    def startProcessing(self):
        self._obsPrice = AskPrice(self.orderBook) \
                            if self.side == Side.Buy else \
                         BidPrice(self.orderBook)
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
        self._stopLossOrder = self.send(market.Order_Impl(self.side.opposite,
                                                          self.volumeFilled))
                
