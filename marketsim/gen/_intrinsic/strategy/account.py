from marketsim import (Side, event, request, types, _)

from marketsim.gen._intrinsic.trader.props import OnOrderMatched
from marketsim.gen._out.orderbook._OfTrader import OfTrader

class _Account_Impl(types.IAccount):
    
    def __init__(self):
        event.subscribe(self.inner.on_order_created, _(self).onOrderCreated, self)
        event.subscribe(OnOrderMatched(), _(self)._onOrderMatched, self)
        self.on_traded = event.Event()
        self.orderBook = OfTrader()
        self._balance = 0
        self._position = 0
        
    _internals = ["orderBook"]
        
    def _onOrderMatched(self, trader, order, price, volume):
        if getattr(order, '_strategy', None) == self.inner:
            pv = price * volume
            self._balance += pv if order.side == Side.Sell else -pv
            self._position += volume if order.side == Side.Buy else -volume
            self.on_traded.fire(self)
    
    @property
    def amount(self):
        return self._position
    
    @property
    def PnL(self):
        return self._balance
    
    def onOrderCreated(self, order, source):
        order._strategy = source

class _VirtualMarket_Impl(types.IAccount):

    def __init__(self):
        self._balance = 0
        self._position = 0
        self.on_traded = event.Event()
        self.orderBook = OfTrader()
        event.subscribe(self.inner.on_order_created, _(self).onOrderCreated, self)

    _internals = ['orderBook']

    @property
    def amount(self):
        return self._position

    @property
    def PnL(self):
        return self._balance

    def onOrderCreated(self, order, source):
        self.orderBook.process(
                    request.EvalMarketOrder(
                                order.side,
                                order.volumeUnmatched,
                                _(self,
                                  order.side,
                                  order.volumeUnmatched)._update))


    def _update(self, side, volume, (price, volumeUnmatched)):
        matched = volume - volumeUnmatched
        self._position += -matched if side == Side.Sell else matched
        self._balance += price if side == Side.Sell else -price
        self.on_traded.fire(self)
