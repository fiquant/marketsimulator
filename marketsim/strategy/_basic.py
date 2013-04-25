from marketsim import types, Method, Event, mathutils, registry, order, scheduler, Side, meta
from marketsim.types import *

from _wrap import wrapper

class Strategy(types.IStrategy):
    
    def __init__(self, trader):
        self._suspended = False
        self._trader = trader
        
    @property
    def suspended(self):
        return self._suspended
    
    def suspend(self, s=True):
        self._suspended = s
        
    @property
    def trader(self):
        return self._trader

class TwoSides(Strategy):    
    
    def __init__(self, trader):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        
        Strategy.__init__(self, trader)
        self._wakeUp = Method(self, '_wakeUp_impl')
        
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
            if type(order.side) == int:
                a = 12
            # send order to the order book
            self._trader.send(order)

class _Generic_Impl(Strategy):    
    
    def __init__(self, trader, params):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        params.eventGen -- event that initiates strategy work
        params.sideFunc -- function '() -> Side option' that calculates side of order to create
        params.volumeFunc -- function '() -> Volume' calculating volume of order to create
        params.orderFactory -- function 'Side -> Volume -> IOrder' instantiating orders
        """        
        Strategy.__init__(self, trader)
        self._eventGen = params.eventGen
        self._sideFunc = params.sideFunc
        self._volumeFunc = params.volumeFunc
        self._orderFactory = params.orderFactory
        self._wakeUp = Method(self, '_wakeUp_impl')
        
        # start listening calls from eventGen
        self._eventGen.advise(self._wakeUp)
        
    def reset(self):
        self._eventGen.schedule()
        
    def dispose(self):
        self._eventGen.unadvise(self._wakeUp)

    def _wakeUp_impl(self, _):
        if self._suspended:
            return
        # determine side and parameters of an order to create
        side = self._sideFunc()
        if side <> None:
            volume = int(self._volumeFunc())
            if volume > 0:
                # create order given side and parameters
                order = self._orderFactory(side)(volume)
                # send order to the order book
                self._trader.send(order)

@registry.expose(alias = 'Random side')
@meta.sig(args=(), rv=Side)
def randomSide():
    return types.Side.byId(mathutils.rnd.randint(0,1)())

exec  wrapper("Generic", 
             """ Generic strategy that wakes up on events given by *eventGen*, 
                 chooses side of order to create using *sideFunc* and its volume by *volumeFunc*,
                 creates an order via *orderFactory* and sends the order to the market using its trader
             
                 Parameters:
                 
                     |orderFactory|
                         order factory function (default: order.Limit.T)
                         
                     |eventGen|
                         Event source making the strategy to wake up
                         
                     |volumeFunc|
                         defines volumes of orders to create 
                         (default: exponential distribution with |lambda| = 1)
                         
                     |sideFunc|
                         function choosing side of order to create (default: randomSide)
                         
             """,
              [('orderFactory',         'order.MarketFactory',                  'Side -> Volume -> IOrder'),
               ('eventGen',             'None',                                 'Event'),
               ('volumeFunc',           'mathutils.rnd.expovariate(1.)',        '() -> Volume'),
               ('sideFunc',             'randomSide',                           '() -> Side')], register=False)
        
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
        self._wakeUp = Method(self, '_wakeUp_impl')
    
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

    