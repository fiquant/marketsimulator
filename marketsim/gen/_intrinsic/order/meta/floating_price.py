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

    def bind_ex(self, ctx):
        self._ctx_ex = ctx
        self.proto.bind_ex(ctx)
        self._priceFunc.bind_ex(ctx)
        for x in self._subscriptions:
            x.bind_ex(ctx)
        self._bound_ex = True

    def reset_ex(self, generation):
        self.proto.reset_ex(generation)
        self._priceFunc.reset_ex(generation)
        
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
from marketsim.gen._out._intrinsic_base.order.meta.floating_price import Factory_Base

class Factory_Impl(Event_Impl, Factory_Base):
    
    def __call__(self):
        proto = self.proto(constant(0))()
        return Order_Impl(proto, self.floatingPrice) if proto is not None else None
