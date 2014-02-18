from marketsim import _, event

import _meta

class Order_Impl(_meta.OwnsSingleOrder):
    """ Meta order controlling price of the underlying order
        When price changes it cancels underlying order and resends it with changed price
        For the moment we work only on limit orders but this mecanism might be extented to any persistent order
    """
    
    def __init__(self, proto, price):
        _meta.OwnsSingleOrder.__init__(self, proto)
        self._priceFunc = price
        event.subscribe(price, _(self)._update, self)
        
    def With(self, **kwargs):
        return Order_Impl(self.proto.With(**kwargs), self._priceFunc)
    
    def cancel(self):
        _meta.OwnsSingleOrder.cancel(self)
        
    def startProcessing(self):
        self._update(None)
        
    def _update(self, dummy):
        if self.active:
            self._dispose() 
            price = self._priceFunc()
            if price is not None:
                self.send(self.proto.With(price = price, 
                                          volume = self.volumeUnmatched))
            else:
                self.send(None)


from marketsim.gen._out._constant import constant

from marketsim.event import Event_Impl

class Factory_Impl(Event_Impl):
    
    def __call__(self):
        proto = self.proto(constant(0))()
        return Order_Impl(proto, self.floatingPrice) if proto is not None else None
