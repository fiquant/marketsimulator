from marketsim import bind

from _basic import Strategy

class OneSide(Strategy):
    
    def __init__(self):                
        """ Initializes generic one side trader and makes it working
        orderBook - book to place orders in
        side - side of orders to create
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> *orderParams 
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
        # determine parameters of an order to create
        params = self._orderFunc()
        # create an order with given parameters
        order = self._orderFactory(*params)
        # send the order to the order book
        self._trader.send(order)

