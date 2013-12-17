from marketsim import (registry, orderbook, request, Side, getLabel,
                       meta, types, bind, event, _, ops)

import marketsim

from _trader import volume_traded, profit_and_loss

from _orderbook import LastTrade

from marketsim.gen._out.observable.orderbook._CumulativePrice import CumulativePrice

@registry.expose(alias = ["Trader's", "Efficiency"])
class Efficiency(ops.Observable[float]):
    """ Observes trader's balance as if was cleared (trader's balance if its position was cleared).
    Can be None if there is not enough assets on the market to clear the position.
    This observable is updated when trader position is changed 
    (which is not fair since the asset price change influences on this parameter also)
    """
    
    def __init__(self, trader = None):
        
        super(Efficiency, self).__init__()
        
        self._trader = trader if trader else marketsim.trader.SingleProxy()
        
        self.attributes = {}

        self.amount = volume_traded(trader)
        self.balance = profit_and_loss(trader)
        
        self.price = CumulativePrice(orderbook.OfTrader(trader), self.amount)

        self.reset()
        event.subscribe(self.price, _(self)._update, self)
        event.subscribe(self.amount, _(self)._update, self)

    _internal = ["amount", "balance", "price"]
        
    @property
    def digits(self):
        return self._trader.orderBook._digitsToShow
    
    def _update(self, dummy = None):
        self._current = (self.balance - self.price)()
        self.fire(self)
        
    @property
    def trader(self):
        return self._trader
    
    @trader.setter
    def trader(self, value):
        self._trader = value    
        #self._event.switchTo(self._trader.on_traded)
            

    _properties = { 'trader' : types.IAccount }
    
        
    def reset(self):
        self._current = None

    @property
    def label(self):
        """ Returns indicator label
        """
        return "Efficiency_{"+getLabel(self._trader)+"}"
        
    def __call__(self):
        return self._current
