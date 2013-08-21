from marketsim import _, event
from .._basic import Strategy

class TwoSides(Strategy):    
    
    def __init__(self):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        
        Strategy.__init__(self)
        event.subscribe(self._eventGen, _(self)._wakeUp, self)
        
    def _wakeUp(self, signal):
        # determine side and parameters of an order to create
        res = self._orderFunc()
        if res <> None:
            (side, params) = res
            # create order given side and parameters
            order = self.orderFactory(side)(*params)
            # send order to the order book
            self._send(order)

