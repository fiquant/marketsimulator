from marketsim import Side, getLabel, Event

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class EfficiencyEx(object):
    
    def __init__(self, eventSources, trader):
        
        self.on_changed = Event()
        self._current = None
        self._trader = trader
        self.attributes = {}
        
        def update(_):
            def callback(sign): 
                def inner((price, volume_unmatched)):
                    if volume_unmatched == 0: 
                        self._current = trader.PnL - sign*price
                        self.on_changed.fire(self)
                    else: # don't know what to do for the moment
                        self._current = None
                return inner
        
            side = Side.Buy if trader.amount < 0 else Side.Sell 
            trader.book.evaluateOrderPriceAsync(side, abs(trader.amount), callback(-sign(trader.amount)))
        
        for es in eventSources:
            es.advise(update)
            
        update(None)

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

def Efficiency(trader):
    return EfficiencyEx([trader.on_traded], trader)
