from basic import Strategy

from marketsim.gen._out._intrinsic_base.strategy.generic import Generic_Base

class Generic_Impl(Strategy):
     
    def __init__(self):                
        Strategy.__init__(self)
        from marketsim import event, _
        event.subscribe(self.eventGen, _(self)._wakeUp, self)
         
    def _wakeUp(self, _):
        # determine side and parameters of an order to create
        order = self.orderFactory()
        # send order to the order book
        if order is not None:
            self._send(order)
