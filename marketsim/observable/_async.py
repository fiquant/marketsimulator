from marketsim import Side, getLabel, Event

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class Efficiency(object):
    
    def __init__(self, trader, eventSources=None):
        
        self._trader = trader
        if eventSources is None:
            self._eventSources = [trader.on_traded]
        
        self.on_changed = Event()
        self.attributes = {}
        
        def update(_):
            def callback(sign): 
                def inner((price, volume_unmatched)):
                    if volume_unmatched == 0: 
                        self._current = self._trader.PnL - sign*price
                        self.on_changed.fire(self)
                    else: # don't know what to do for the moment
                        self._current = None
                return inner
        
            side = Side.Buy if self._trader.amount < 0 else Side.Sell 
            self._trader.book.evaluateOrderPriceAsync(side, 
                                                      abs(self._trader.amount), 
                                                      callback(-sign(self._trader.amount)))
        
        for es in self._eventSources:
            es.advise(update)
            
        update(None)
        self.reset()
        
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
