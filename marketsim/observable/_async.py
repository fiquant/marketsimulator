from marketsim import orderbook, request, Side, getLabel, Event, meta, types, bind, scheduler, event, _, ops

from _orderbook import LastTrade
from _trader import OnTraded

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class Efficiency(ops.Observable[float]):
    """ Observes trader's balance as if was cleared (trader's balance if its position was cleared).
    Can be None if there is not enough assets on the market to clear the position.
    This observable is updated when trader position is changed 
    (which is not fair since the asset price change influences on this parameter also)
    """
    
    def __init__(self, trader):
        
        super(Efficiency, self).__init__()
        self._trader = trader
        
        self.attributes = {}
        
        self._alias = ["Trader's", "Efficiency"]
        
        self.reset()
        event.subscribe(LastTrade(orderbook.OfTrader(trader)), _(self)._update, self)
        event.subscribe(OnTraded(trader), _(self)._update, self)
        
    @property
    def digits(self):
        return self._trader.orderBook._digitsToShow
    
    def _callback(self, sign, (price, volume_unmatched)): 
        if volume_unmatched == 0: 
            self._current = self._trader.PnL - sign*price
            self.fire(self)
        else: # don't know what to do for the moment
            self._current = None

    def _update(self, dummy = None):
        side = Side.Buy if self._trader.amount < 0 else Side.Sell 
        self._trader.orderBook.process(
                        request.EvalMarketOrder(side, 
                                                abs(self._trader.amount), 
                                                _(self, -sign(self._trader.amount))._callback))
    
        
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
