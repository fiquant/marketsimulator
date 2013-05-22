from marketsim import bind
from _basic import Strategy

class TwoSides(Strategy):    
    
    def __init__(self):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        
        Strategy.__init__(self, None)
        self._wakeUp = bind.Method(self, '_wakeUp_impl')
        # start listening calls from eventGen
        self._eventGen.advise(self._wakeUp)
        
    def reset(self):
        self._eventGen.schedule()
        
    def dispose(self):
        self._eventGen.unadvise(self._wakeUp)

    def _wakeUp_impl(self, signal):
        if self._suspended:
            return
        # determine side and parameters of an order to create
        res = self._orderFunc()
        if res <> None:
            (side, params) = res
            # create order given side and parameters
            order = self._orderFactoryT(side)(*params)
            # send order to the order book
            self._trader.send(order)

