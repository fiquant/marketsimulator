from marketsim import (trader, Side, Event, order, orderbook, scheduler, observable, order, 
                       request, registry, types, meta, _, ops, event)

from .._basic import Strategy
from .._wrap import wrapper2

from ..side import FundamentalValue


class _Account_Impl(types.IAccount):
    
    def __init__(self):
        event.subscribe(self.inner.on_order_created, _(self).onOrderCreated, self)
        event.subscribe(observable.OnOrderMatched(), _(self)._onOrderMatched, self)
        self.on_traded = Event()
        self.orderBook = orderbook.OfTrader()
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

exec wrapper2("Account", 
             "",
             [
              ('inner',     'FundamentalValue()', 'types.ISingleAssetStrategy'),
             ], register=False)


@registry.expose(alias=['actually traded'])
@meta.sig((types.ISingleAssetStrategy,), types.IAccount)
def account(strategy):
    return Account(strategy)