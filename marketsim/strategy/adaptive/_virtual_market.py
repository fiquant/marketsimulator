from marketsim import (orderbook, Event, Side, request, registry, types, meta, _, ops, event)

from .._basic import Strategy, Base
from .._wrap import wrapper2

from ..side import FundamentalValue


class _VirtualMarket_Impl(types.IAccount):
    
    def __init__(self):
        self._balance = 0
        self._position = 0
        self.on_traded = Event()
        self.orderBook = orderbook.OfTrader()
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

exec wrapper2("VirtualMarket", 
             "",
             [
              ('inner',   'FundamentalValue()', 'types.ISingleAssetStrategy')
             ], register=False)

@meta.sig((types.ISingleAssetStrategy,), types.IAccount)
def virtualMarket(strategy):
    return VirtualMarket(strategy)