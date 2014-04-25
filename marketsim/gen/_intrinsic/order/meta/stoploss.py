from marketsim import  event, _
from .. import market
import _meta

class Order_Impl(_meta.Base):
    
    def __init__(self, proto, maxloss):
        
        _meta.Base.__init__(self, proto.volumeUnmatched)
        
        self.side = proto.side
        self._proto = proto
        self._maxloss = maxloss
        self._stopLossOrder = None

    def bind_ex(self, ctx):
        self._ctx_ex = ctx
        self._proto.bind_ex(ctx)
        self._bound_ex = True

    def startProcessing(self):
        from marketsim.gen._out._side import Side
        self._obsPrice = self.orderBook.Asks.BestPrice \
                            if self.side == Side.Buy else \
                         self.orderBook.Bids.BestPrice
        self.send(self._proto)
        
    def onOrderMatched(self, order, price, volume):
        from marketsim.gen._out._side import Side
        if order is not self._stopLossOrder:
            if volume > 0:
                handler = event.GreaterThan((1+self._maxloss) * price, _(self)._onPriceChanged)\
                            if self.side == Side.Sell else\
                          event.LessThan((1-self._maxloss) * price, _(self)._onPriceChanged)
                            
                self._stopSubscription = event.subscribe(self._obsPrice, handler, self)
                self._stopSubscription.bind_ex(self._ctx_ex)
                self._stopSubscription.bind(self._ctx)
                self.onMatchedWith(price, +volume)
        else:
            self.onMatchedWith(price, -volume)
        
    def _onPriceChanged(self, dummy):
        # the stoploss is activated
        self._stopSubscription.dispose()
        self._stopLossOrder = self.send(market.Order_Impl(self.side.opposite,
                                                          self.volumeFilled))
                
