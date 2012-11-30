class Strategy(object):
    
    def __init__(self, trader):
        self._suspended = False
        self._trader = trader
        
    @property
    def suspended(self):
        return self._suspended
    
    def suspend(self, s):
        self._suspended = s
        
    @property
    def trader(self):
        return self._trader

class TwoSides(Strategy):    
    
    def __init__(self, trader, orderFactoryT, eventGen, orderFunc):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        
        Strategy.__init__(self, trader)
        
        def wakeUp(signal):
            if self._suspended:
                return
            # determine side and parameters of an order to create
            res = orderFunc(trader)
            if res <> None:
                (side, params) = res
                # create order given side and parameters
                order = orderFactoryT(side)(*params)
                # send order to the order book
                trader.send(order)

        # start listening calls from eventGen
        eventGen.advise(wakeUp)
        
class OneSide(Strategy):
    
    def __init__(self, trader):                
        """ Initializes generic one side trader and makes it working
        orderBook - book to place orders in
        side - side of orders to create
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> *orderParams 
        """     
        Strategy.__init__(self, trader)   
    
        def wakeUp(signal):
            if self._suspended:
                return
            # determine parameters of an order to create
            params = self._orderFunc()
            # create an order with given parameters
            order = self._orderFactory(*params)
            # send the order to the order book
            self._trader.send(order)
    
        # start listening calls from eventGen
        self._eventGen.advise(wakeUp)