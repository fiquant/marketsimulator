from marketsim import Side, getLabel, Event, meta, types, bind, scheduler

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class Efficiency(types.IObservable):
    """ Observes trader's balance as if was cleared (trader's balance if its position was cleared).
    Can be None if there is not enough assets on the market to clear the position.
    This observable is updated when trader position is changed 
    (which is not fair since the asset price change influences on this parameter also)
    """
    
    def __init__(self, trader):
        
        self._trader = trader
        self._update = bind.Method(self, '_update_impl')
        
        self.on_changed = Event()
        self.attributes = {}
        
        self._trader.on_traded += self._update
        
        self.reset()
        
    def bind(self, context):
        self._update()

    def _callback_impl(self, sign, (price, volume_unmatched)): 
        if volume_unmatched == 0: 
            self._current = self._trader.PnL - sign*price
            self.on_changed.fire(self)
        else: # don't know what to do for the moment
            self._current = None

    def _update_impl(self, _ = None):
    
        side = Side.Buy if self._trader.amount < 0 else Side.Sell 
        self._trader.book.evaluateOrderPriceAsync(side, 
                                                  abs(self._trader.amount), 
                                                  bind.Method(self, '_callback_impl', -sign(self._trader.amount)))
    
        
    @property
    def trader(self):
        return self._trader
    
    @trader.setter
    def trader(self, value):
        self._trader.on_traded -= self._update
        self._trader = value    
        self._trader.on_traded += self._update
            

    _properties = { 'trader' : types.ISingleAssetTrader }
    
        
    def reset(self):
        self._current = None

    @property
    def label(self):
        """ Returns indicator label
        """
        return "Efficiency_{"+getLabel(self._trader)+"}"
        
    def advise(self, listener):
        """ Subscribes 'listener' to value change event
        """
        self.on_changed += listener
        
    @property
    def value(self):
        """ Returns current value
        """
        return self._current
